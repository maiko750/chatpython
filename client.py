import socket
import threading

nickname = input("Choose a nickname: ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 39485))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

#get input from user. runs all the time
def write():
    while True:
        message  = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


#we need a thread running for all messages we going to send
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
