import socket
import os
from datetime import datetime

def extractInfoFromByteMessage(byte_data):
    # Extract username length
    usernameLen = int(byte_data[0:1].decode('utf-8'))
    # Extract  username
    username = byte_data[1:1+usernameLen].decode('utf-8')
    # Extract the message from the remaining data
    message = byte_data[1+usernameLen:].decode('utf-8')
    return username, message

# def broadcast

def main():
    serverAddress = 'localhost'
    serverPort = 8080
    sizeLimit = 4096
    # AF_INETを使用し、UDPソケットを作成
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # ソケットを特殊なアドレスとポートに紐付け
    sock.bind((serverAddress, serverPort))
    print('starting up on port {}'.format(serverPort))

    clientInfos = {}

    """
    dpath = 'temp'
    if not os.path.exists(dpath):
        os.makedirs(dpath)
    """

    while True:
        # storing data, IP address, username, message, timestamp
        data, clientAddress = sock.recvfrom(sizeLimit)
        username, message = extractInfoFromByteMessage(data)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # print byte_data
        print('received: ',data)

        # storing above infos in dictionary, with clientAddress being a key
        clientInfos[clientAddress] = {
            'username': username,
            'message': message,
            'time': timestamp
        }
        # create list of Address
        listOfClientAddress = list(clientInfos.keys())

        if data:
            for adr in listOfClientAddress:
                if clientAddress != adr:
                    sent = sock.sendto(data, adr)
                    print('sent {} to {}'.format(sent, adr))

main()
