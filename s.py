import socket
import os

# AF_INETを使用し、UDPソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = 'localhost'
server_port = 8080
# ソケットを特殊なアドレスとポートに紐付け
sock.bind((server_address, server_port))
print('starting up on port {}'.format(server_port))

# 次に、現在の作業ディレクトリに「temp」という名前のフォルダが存在するかどうかをチェックします。存在しない場合は、os.makedirs() 関数を使用してフォルダを作成します。このフォルダは、クライアントから受信したファイルを格納するために使用されます。
dpath = 'temp'
if not os.path.exists(dpath):
    os.makedirs(dpath)


while True:
   # print('\nwaiting to receive message')
   data, client_address = sock.recvfrom(4096)

   print('received {} bytes from {}'.format(len(data), client_address))
   print(data)

   if data:
       sent = sock.sendto(data, client_address)
       print('sent {} bytes back to {}'.format(sent, client_address))