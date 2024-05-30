import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = 'localhost'
    server_port = 8080
    client_address = '0.0.0.0'
    client_port = 9050
    sock.bind((client_address,client_port))

    username = input('Enter your name: ').encode('UTF-8')

    while True:
        try:
            # outbound message
            message = input('Enter your message: ').encode('UTF-8')
            if len(message) > 2^12:
                return print('Message length exceeded limit')

            sent = sock.sendto(message, (server_address, server_port))

            # inbound message
            data, server = sock.recvfrom(4096)
            if data:
                print('received {!r}'.format(data))

        except Exception as e:
            print(f"Error writing to UDP: {e}")
            break

main()