import socket
from datetime import datetime
import time
import threading
from queue import Queue


def scan(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((addr,135))
    if result == 0:
        return 1
    else:
        return 0


def run1():
    net = input("Enter the subnet address: ")
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = 1
    en1 = int(input("Enter the ending last Octet: "))
    en1 += 1
    t1 = datetime.now()
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        if scan(addr):
            port_start()
        else:
            continue
         

def portscan(port):
    t_IP = ''
    print_lock = threading.Lock()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
    except IOError:
        pass
    finally:
        con.close()


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


def port_start():
    socket.setdefaulttimeout(0.25)
    q = Queue()
    start_time = time.time()
       
    for x in range(100):
       t = threading.Thread(target=threader)
       t.daemon = True
       t.start()
       
    for worker in range(1, 500):
       q.put(worker)
       
    q.join()
    print('Time port scanning took:', time.time() - start_time)


def start():
    run1()
    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in:", total)


if __name__ == '__main__':
    start()
