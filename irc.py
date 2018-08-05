import socket


class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " :" + msg + "\n")

    def quit(self, msg):
        self.irc.send("QUIT " + msg + "\n")
        self.irc.close()

    def change_nick(self, nick):
        self.irc.send("NICK " + nick + "\n")

    def connect(self, server, channel, botnick):
        # Defines the socket
        print("Connecting to: "+server)
        # Connects to the server
        self.irc.connect((server, 6667))
        # User authentication
        # (botnick + " ")*3 has been used for code optimization
        # as requested in the Pull Request #1
        self.irc.send("USER " + (botnick + " ")*3 + ":This is a fun bot!\n")
        self.irc.send("NICK " + botnick + "\n")
        # Join the channel
        self.irc.send("JOIN " + channel + "\n")

    def get_text(self):
        # Receive the text
        text = self.irc.recv(2040)

        if text.find('PING') != -1:
            self.irc.send('PONG ' + text.split()[1] + '\r\n')

        return text
