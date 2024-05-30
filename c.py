import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = 'localhost'
    server_port = 8080
    client_address = '0.0.0.0'
    client_port = 9050
    sock.bind((client_address,client_port))

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

            if len(fullMessage) > 2^12:
                return print('Message length exceeded limit')

            sent = sock.sendto(fullMessage.encode('UTF-8'), (server_address, server_port))

            # inbound message
            data, server = sock.recvfrom(4096)
            if data:
                print('received {!r}'.format(data))

        except Exception as e:
            print(f"Error writing to UDP: {e}")
            break                                           

main()