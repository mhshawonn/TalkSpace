import socket
import select
import os

HEADER_LENGTH = 8192
IP = '192.168.0.111'
PORT = 1234
path = os.path.join(SERVER_FOLDER, "uploads")
FORMAT = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

sockets_list = [server_socket]

clients = {}
print("Server is running...")


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message:
                splits = message.split(":")
            if len(splits) == 2:
                nick = splits[0]
                file_name = splits[1] # it use this type of operation done by client
            else:
                continue
            # close to close the client
            if file_name.upper() == 'CLOSE':
                client.send('CLOSE:a'.encode(FORMAT))
                try:
                    client.close()
                except:
                    print("Error closing client")
            #list to list the name of the files avaiable to upload
            elif file_name.upper() == 'LIST':
                #store files name to give response of list command
                files = sorted(os.listdir(path))
                mess = 'LIST'
                for file in files:
                    mess = f'{mess}:{file}'
                client.send(mess.encode(FORMAT))
            elif nick.upper() == 'SEARCH':
                #store files name to give response of search command
                files = sorted(os.listdir(path))
                file_name = file_name.upper()
                mess = 'LIST'
                for file in files:
                    if file_name in file.upper():
                        mess = f'{mess}:{file}'
                client.send(mess.encode(FORMAT))
            else:
                ok = True
                try:
                    file_path = os.path.join(path, file_name)
                    file_size = os.path.getsize(file_path)
                    #DATA is indicator to client to server sending file
                    mess = f'DATA:{file_name}'
                    client.send(mess.encode(FORMAT))
                    with open(file_path, "rb") as file:
                        file_data = file.read(SIZE)
                        while file_data:
                           client.send(file_data)
                           file_data = file.read(SIZE)
                        #ensure complete of transmission
                        client.send(b"FILE_TRANSMISSION_COMPLETE")
                        #print with file send where
                        print(f'{file_name} sent to {nick}')
                except:
                   mess = f'Error:No such file'
                   ok = False
                   client.send(mess.encode(FORMAT))
                indexc = clients.index(client)
                if ok:
                    print(f'{nicknames[indexc]} {file_name} send')
        except Exception as e:
            print(f"Error in handling client: {e}")
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break
def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(
                f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
        else:
            message = receive_message(notified_socket)
            if message is False:
                print(f"Closed Connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}:{message["data"].decode("utf-8")}')

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

