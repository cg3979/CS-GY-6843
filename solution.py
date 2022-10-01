from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n It's not what I am underneath, but what I do that defines me"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailServer = smtp.gmail.com
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailServer)
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "Mail From:<cgtest123@gmail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    print(recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "Reciept To:<cg3979@nyu.edu>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024)
    print(recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = "Data\r\n"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024)
    print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encocde())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024)
    print(recv5)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    noMas = "Quit\r\n"
    clientSocket.send(noMas.encode())
    recv6 = clientSocket.rev(1024)
    print(recv6)
    clientSocket.close()
    # Fill in end


##if __name__ == '__main__':
   # smtp_client(1025, '127.0.0.1')
