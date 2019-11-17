#!/usr/bin/env python3
import sys
import argparse
import socket
import smtplib
import ssl

def honey(address,port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        port=int(port)
        s.bind((address, port))
        s.listen()
        conn,addr = s.accept()
        print('System breach tried from ' + addr[0])
        portemail = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "testtesttest1234567887654321@gmail.com"
        receiver_email = "thalor.manish01@gmail.com"
        password = "codesnag@12345678"
        message = "System breach tried by " + addr[0]
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, portemail, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
        while True:
            data=conn.recv(1024)
            if data == b'\r\n':
                s.close()
                s.exit()
    except:
        s.close()
        s.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='honeypot prototype')
    parser.add_argument('-addr','--address',help='server ip address to use',action='store', required=True)
    parser.add_argument('-portno','--portno',help='server port to use',action='store', required=True)
    args = parser.parse_args()
    honey(args.address,args.portno)
