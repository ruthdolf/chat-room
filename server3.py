#server
#leave ok, re join ok, exit ok
import threading
import socket

host = '127.0.0.1'
port = 1027
clients_connected = []
clients_in_chat = []

def broadcast(message):
    for client in clients_in_chat:
        send_client(client[1], message)
        
def send_client(client, message):
    client.send(message.encode('ascii'))
    


def listen(client, name, address):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            
            if message == '/LEAVE':
                for i in clients_in_chat:
                    if i[1] == client:
                        clients_in_chat.remove(i)
                        break
                print(f'{name} left the chat')
                broadcast(f'{name} has left the chat')
                continue
            
            if message == '/JOIN':
                clients_in_chat.append((name, client))
                print(f'{name} joined the chat')
                broadcast(f'{name} joined the chat')
                continue
            
            if message == '/EXIT':
                for i in clients_connected:
                    if i[1] == client:
                        clients_connected.remove(i)
                        break
                print(f'{name} {address} disconnected')
                break
            
            if message == '/COUNT':
                global count
                count = str(len(clients_in_chat))
                send_client(client, count)
                continue
                

            else:
                nameAndMsg = name + ": " + message
                broadcast(nameAndMsg)
                #print(nameAndMsg + "    broadcasted" )
                
        except Exception as e:
            print("error: ", e)
            break
            


def main():
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server1.bind((host, port))
        print(f"This server is binded to host {host}: {port}")
        server1.listen()
        print("Server is listening..")

    except Exception as e:
        print(f"Unable to bind to host {host}:{port}: ", e)

        
    while True: #each iteration for each client
        client, address = server1.accept()
        connect_thread = threading.Thread(target=connect, args=(client, address))
        connect_thread.start()
        

    
def connect(client, address): #get name and connect
    global name
    try:
            name = client.recv(1024).decode('ascii')
            if name and not name.startswith('/'):
                clients_connected.append((name, client))
                print(f'{name} {address[0]}:{address[1]} connected')
                join_chat_thread = threading.Thread(target=listen, args=(client, name, address))
                join_chat_thread.start()
            else:
                print(f"Invalid or no name received from {address}. Closing connection.")
                client.close()
    except Exception as e:
        print(f"Connection error with {address}: {e}")
        client.close()
    


    
if __name__ == '__main__':
    main()
    
