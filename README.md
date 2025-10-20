# TCP Chat Room Application

This project is a **Python-based TCP chat room** with a client-server architecture. It allows multiple users to connect, join a chat session, send messages, and see the number of users currently online. The application demonstrates concepts in **networking, multithreading, GUI development, and socket programming**.

## Features

* **User Login:** Users enter their name before joining the chat.
* **Join/Leave Chat:** Users can join or leave the chat dynamically.
* **Real-time Messaging:** Messages are broadcasted to all connected clients.
* **Online User Count:** Displays the number of users currently in the chat room, with a manual refresh option.
* **Graphical User Interface:** Built with **Tkinter** for an interactive client experience.
* **Threaded Communication:** Handles multiple clients simultaneously using Python **threading**.
* **Graceful Exit:** Users can leave the chat or exit the program without crashing the server.

## Technologies Used

* **Python 3**
* **Socket Programming** (`socket`)
* **Multithreading** (`threading`)
* **GUI Development:** `Tkinter`, `ScrolledText`
* **ASCII Encoding** for client-server communication

## Project Structure

```
├── client.py    # The chat client with GUI
├── server.py    # The chat server managing clients and broadcasting messages
└── README.md    # Project documentation
```

## How to Run

1. **Start the Server:**

   ```bash
   python server.py
   ```

   The server listens on `127.0.0.1:1027`.

2. **Start a Client:**

   ```bash
   python client.py
   ```

   * Enter your name and join the chat.
   * Use the text box to send messages.
   * Click **Leave Chat** to exit the chat or **Exit Program** to disconnect entirely.

3. **Multiple Clients:**
   Open multiple instances of `client.py` to simulate multiple users connecting to the server.

## Key Concepts Demonstrated

* **TCP/IP Networking:** Client-server communication using sockets.
* **Threading:** Handling multiple clients concurrently.
* **GUI Design:** Tkinter-based interface for client interactions.
* **Data Handling:** Sending and receiving ASCII-encoded messages.
* **Collaboration Features:** Online user count, join/leave notifications, and message broadcasting.

## Future Improvements

* **Cross-Network Communication:** Enable clients to connect across different machines via a public IP or LAN.
* **Authentication & Security:** Add username/password authentication and encrypted communication.
* **Persistent Chat History:** Save messages to a file or database to allow history retrieval.
* **Enhanced GUI:** Improve the interface with better layouts, emojis, or message timestamps.
* **File Sharing:** Allow users to send files alongside text messages.
* **Scalability:** Refactor server code to handle a large number of simultaneous clients efficiently.
