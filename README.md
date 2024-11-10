# Chatting Application README

## Overview

Welcome to the **Chatting Application**! This is a full-featured chat app designed to help users communicate seamlessly. The application includes a modern, user-friendly interface with the following key features:

- **Index Page**: The landing page where users can get an overview of the app.
- **Login Page**: Allows users to securely log in to their accounts.
- **Group Chat**: A space where users can communicate with multiple participants in real-time.

Once the server is set up, the application can be accessed globally, enabling users to interact from anywhere in the world.

## Features

- **User Authentication**: Secure login and registration features ensure that each user has a personalized experience.
- **Real-time Communication**: The app uses WebSockets (or another real-time technology) for instant messaging, ensuring users can send and receive messages without delay.
- **Group Chats**: Users can create and join group chats, allowing for conversations with multiple participants at the same time.
- **Global Access**: Once deployed, the server can be accessed from anywhere around the world, making it easy to stay connected with friends, family, or colleagues.

## Prerequisites

Before setting up the server, make sure you have the following installed:

- **Python 3.x** (for the backend)
- **Flask** (for the web framework)
- **Flask-SocketIO** (for WebSocket support)
- **Mysql** (or another database for user and chat storage)
- **pip** (Python's package installer)
- **Web browser** (for accessing the web application)

## Setting Up the Server
### Clone the Repository
Start by cloning the repository to your local machine.

``` bash
git clone https://github.com/your-username/chatting-application.git
```
``` bash
cd chatting-application
```

## Setting Up the MySQL Database

Follow the steps below to set up the MySQL database for your application:

### Step 1: Log in to MySQL Server

Log in to your MySQL server using the `mysql` command-line client or your preferred MySQL client:

```bash
mysql -u root -p
```
- Enter your MySQL root password when prompted.

### Step 2: Create the Database
- Once you are logged in, create a new database called messages:

```sql
CREATE DATABASE messages CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
- This command creates a database named messages with the utf8mb4 character set, which supports emojis and other multi-byte characters.

### Step 3: Create Tables
- Now, switch to the newly created database:

```sql
USE messages;
```
Create messages Table
Create a table to store the chat messages with the following columns: id, username, message, and timestamp:
``` sql
CREATE TABLE messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  message TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf
```
``` sql
Create user Table
Create a table to store user credentials with the columns: username and password:
```
``` sql
CREATE TABLE user (
  username VARCHAR(255) PRIMARY KEY,
  password VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
- **username**: The username of the user (unique and serves as the primary key).
- **password**: The hashed password for the user.
###Step 4: Exit MySQL
Once both tables are created, exit the MySQL client:

``` sql
EXIT;
```
### Step 4: Check If All Libraries Are Installed

- Before running the application, make sure you have all the necessary libraries installed. You can check and install the required Python libraries by following these steps:

**Install Dependencies**:

Ensure that the following libraries are installed on your local system:

- **Flask**: Web framework for Python
- **Flask-SocketIO**: Real-time messaging via WebSocket
- **mysql-connector-python**: MySQL database connector for Python

### Step 5: Run the Flask Application
Once the configuration is complete and the required libraries are installed, you can run the Flask application:

- **Run the Server**:

Use the following command to start the Flask application:

``` bash
python main.py
```
Or, if you are using Python 3:

``` bash
python3 main.py
```

- **Access the Application**:

Once the server is running, open your web browser and go to:

``` link
http://localhost:5000
```
This will open the login page where you can authenticate and start chatting!
![index page](https://github.com/Subhamkonar84/online_chatting_application/blob/main/index.png)
![login page](https://github.com/Subhamkonar84/online_chatting_application/blob/main/login.png)
![chat page](https://github.com/Subhamkonar84/online_chatting_application/blob/main/chat.png)

