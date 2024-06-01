import socket

def extractInfoFromByteMessage(byte_data):
    # Extract username length
    usernameLen = int(byte_data[0:1].decode('utf-8'))
    # Extract  username
    username = byte_data[1:1+usernameLen].decode('utf-8')
    # Extract the message from the remaining data
    message = byte_data[1+usernameLen:].decode('utf-8')
    return username, message

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = 'localhost'
    server_port = 8080
    client_address = '0.0.0.0'
    client_port = 9050
    sock.bind((client_address,client_port))
    sizeLimit = 4096

    # .encode('UTF-8')
    username = input('Enter your username: ')
    if len(username) > 10:
        username = input('Username must be less than 10 characters. Enter your username: ')    
    usernameLen = len(username)

    while True:
        try:
            # outbound message
            message = input('Enter your message: ')
            fullMessage = str(usernameLen) + username + message

            if len(fullMessage) > sizeLimit:
                return print('Message length exceeded limit')

            sent = sock.sendto(fullMessage.encode('UTF-8'), (server_address, server_port))
            print('Message sent')

            # inbound message
            data, server = sock.recvfrom(sizeLimit)

            if data:
                username, message = extractInfoFromByteMessage(data)
                print('{}: {}'.format(username, message))

        except Exception as e:
            print(f"Error writing to UDP: {e}")
            break                                           

main()