https://github.com/shigenkawasaki/OnlineChat/assets/24628052/01086e3a-bb7d-4d6d-bf2a-274b43c74fa1


# UDP Chat Application

This is a simple UDP-based chat application written in Python. It allows users to send and receive messages concurrently. The application demonstrates basic usage of Python's `socket` and `threading` modules to handle UDP communication.

## Features

- Send and receive messages concurrently using threads.
- Display incoming messages without interrupting the message input prompt.
- Handle different message formats including user messages and confirmation messages.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/udp-chat-app.git
    cd udp-chat-app
    ```

2. Install any required dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the server:

    ```bash
    python server.py
    ```

2. Run the client:

    ```bash
    python client.py
    ```

3. Enter your username when prompted, then start sending and receiving messages.

## Code Overview

### `client.py`

- Sets up a UDP client socket.
- Continuously sends messages entered by the user.
- Receives messages from other clients and displays them without interrupting the input prompt.

### `server.py`

- Sets up a UDP server socket.
- Receives messages from clients and broadcasts them to all connected clients.
- Sends a confirmation message back to the sender.

### Main Functions

- `extractInfoFromByteMessage(byte_data)`: Extracts the username and message from the received byte data.
- `receive_messages(sock, sizeLimit)`: Thread function to handle incoming messages.
- `main()`: Main function to run the client application.

## Example

```bash
Enter your username: Alice
Enter your message: Hi there!
Message sent
Bob: Hello, Alice!
Enter your message:
