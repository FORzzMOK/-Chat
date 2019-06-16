#!python2
#!-*-coding: utf-8-*-

import socket, host, time
from threading import Thread

RUN = True
MaxClients = 5
clientsAddr = []
clientsConn = {}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host.ip, host.port))
sock.listen(MaxClients)

def sockAppend():
    while RUN:
        conn, addr = sock.accept()
        Name = conn.recv(1024).decode('utf-8')
        conn.send("Hello, " + Name + "!")
        clientsAddr.append(addr)
        clientsConn[addr[1]] = conn
        thread_2 = Thread(target=connRecv, args=(conn, addr, Name))
        thread_2.start()
    thread_2.join()
    return True

def sockDelete(conn, addr, text):
    if 'StopProgramm' in text:
        del clientsConn[addr[1]]
        clientsAddr.remove(addr)
        conn.close()
        print 'All Ok'
        return False

def connRecv(conn, addr, Name):
    while RUN:
        print clientsAddr
        result = conn.recv(1024).decode('utf-8')
        if sockDelete(conn, addr, result) == False:
            break
        broadcast(result, Name)
    return True

def broadcast(text, Name):
    for client in clientsConn.values():
        client.send(Name+': '+text)

thread_1 = Thread(target=sockAppend, args=())
thread_1.start()
thread_1.join()

time.sleep(2)


