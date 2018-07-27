from irc import *
from secrets import *
import os
import random
import time

channel = get_channel()
server = get_server()
nickname = "test_bot"

irc = IRC()
irc.connect(server, channel, nickname)


while 1:
    text = irc.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "test" in text.lower():
        irc.send(channel, "test successful")
