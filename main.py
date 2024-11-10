from flask import Flask, render_template, request, session, redirect, url_for   
from flask_socketio import SocketIO, emit
from flask_mysqldb import MySQL
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from threading import Thread
import os



app = Flask(__name__)

app.secret_key = 'hey this is my secret key okk' 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'proj'
app.config['MYSQL_PASSWORD'] = 'project@123'
app.config['MYSQL_DB'] = 'chat_app'
app.config['MYSQL_CHARSET'] = 'utf8mb4'


mysql = MySQL(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        # Create a cursor and execute the query to insert the new user
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        mysql.connection.commit()
        cur.close()

        # Redirect to login page after successful registration
        return redirect(url_for('log_in'))
    
    # For GET request, just render the registration page
    return render_template('register.html')

@app.route('/test_db')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT 1")
        cur.close()
        return "Database connection successful!"
    except Exception as e:
        return str(e)
    
@app.route('/log_in')
def log_in():
    return render_template('login.html')


@socketio.on('send_message')
def handle_send_message(data):
    username = session['username']
    message = data['message']
    
    # Store message in database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO messages (username, message) VALUES (%s, %s)", (username, message))
    mysql.connection.commit()
    cur.close()

    # Broadcast message to all clients
    socketio.emit('receive_message', {'username': username, 'message': message, 'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@app.route('/logout')
def logout():
    # Clear the session data to log the user out
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        
        # Create a cursor and execute the query to check if the user exists
        cur = mysql.connection.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()

        if user:
            hashed_password = user[0]
            # Check if the entered password matches the hashed password in the database
            if check_password_hash(hashed_password, password):
                # If successful, store user information in the session

                session['username'] = username
                return redirect(url_for('chat'))
            else:
                error = "Invalid credentials. Please try again."
        else:
            error = "Username not found."

        return render_template('login.html', error=error)
    
    # For GET request, just render the login page
    return render_template('login.html')

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    else:
        return redirect(url_for('login'))



@socketio.on('get_history')
def handle_get_history():
    cur = mysql.connection.cursor()
    
    # Fetch the last 10 messages
    cur.execute("SELECT username, message, timestamp FROM messages ORDER BY timestamp DESC")
    messages = cur.fetchall()
    cur.close()
    
    # Reverse the order to have the oldest messages first
    messages = messages[::-1]
    
    # Send chat history to client
    emit('chat_history', [{'username': msg[0], 'message': msg[1], 'timestamp': msg[2].strftime("%Y-%m-%d %H:%M:%S")} for msg in messages])

def run_ngrok():
    os.system("ngrok http --url https://dominant-chief-chow.ngrok-free.app 5000")

if __name__ == '__main__':
    thread = Thread(target=run_ngrok)
    thread.start()
    socketio.run(app, host='0.0.0.0', port=5000)
    app.run(debug=True)
