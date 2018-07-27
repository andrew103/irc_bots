from irc import *
from secrets import *
import os
import random
import time

channel = get_channel()
server = get_server()
nickname = "THANOS"

irc = IRC()
irc.connect(server, channel, nickname)


while 1:
    text = irc.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "perfectly balanced" in text.lower():
        irc.send(channel, "As all things should be")

    if "PRIVMSG" in text and channel in text and "fun" in text.lower():
        irc.send(channel, "Fun isn't something one considers when balancing the universe")

    if "PRIVMSG" in text and channel in text and "you should have gone for the head" in text.lower():
        irc.send(channel, "*snap*")
