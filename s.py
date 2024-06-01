import socket
import os
from datetime import datetime

"""
Serverに必要な機能
1. クライアントのIP Adress, Port、len(username), username, Message、最後のメッセージの時間を格納する機能
2. "username: message"となるような機能(ただしこれは同じポートの場合はメッセージを表示しない、ポートが異なる場合に表示)
3. (一定時間が経過したら、リレーシステムから削除)
"""

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
    # 次に、現在の作業ディレクトリに「temp」という名前のフォルダが存在するかどうかをチェックします。存在しない場合は、os.makedirs() 関数を使用してフォルダを作成します。このフォルダは、クライアントから受信したファイルを格納するために使用されます。
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