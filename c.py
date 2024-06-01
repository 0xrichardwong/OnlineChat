import socket
import threading

def extractInfoFromByteMessage(byte_data):
    # Extract username length
    usernameLen = int(byte_data[0:1].decode('utf-8'))
    # Extract username
    username = byte_data[1:1+usernameLen].decode('utf-8')
    # Extract the message from the remaining data
    message = byte_data[1+usernameLen:].decode('utf-8')
    return username, message

def receive_messages(sock, sizeLimit):
    while True:
        try:
            data, server = sock.recvfrom(sizeLimit)
            if data:
                try:
                    username, message = extractInfoFromByteMessage(data)
                    print(f'\n{username}: {message}\nEnter your message: ', end='', flush=True)
                except ValueError:
                    # If the first byte is not an integer, print the received byte data
                    print(data.decode('UTF-8'))
        except Exception as e:
            print(f"Error reading from UDP: {e}")
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = 'localhost'
    server_port = 8080
    client_address = '0.0.0.0'
    client_port = 9050
    sock.bind((client_address, client_port))
    sizeLimit = 4096

    username = input('Enter your username: ')
    while len(username) > 10:
        username = input('Username must be less than 10 characters. Enter your username: ')    
    usernameLen = len(username)

    # Start the thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock, sizeLimit))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        try:
            # outbound message
            message = input('Enter your message: ')
            fullMessage = str(usernameLen) + username + message

            if len(fullMessage) > sizeLimit:
                print('Message length exceeded limit')
                continue

            sock.sendto(fullMessage.encode('UTF-8'), (server_address, server_port))
            print('Message sent')

        except Exception as e:
            print(f"Error writing to UDP: {e}")
            break                                           

if __name__ == "__main__":
    main()
