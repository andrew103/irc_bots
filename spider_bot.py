from irc import *
from secrets import *
import os
import random
import time

channel = get_channel()
server = get_server()
nickname = "spider_bot"

irc = IRC()
irc.connect(server, channel, nickname)


while 1:
    text = irc.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "*snap*" in text.lower():
        irc.send(channel, "Alexis...I don't feel so good...")
        irc.quit("disintegrated")

        if nickname == "spider_bot":
            nickname = "CAPTAIN_MARVEL"
        elif nickname == "CAPTAIN_MARVEL":
            nickname = "spider_bot"

        time.sleep(5)

        irc = IRC()
        irc.connect(server, channel, nickname)

    if "PRIVMSG" in text and channel in text and "goat" in text.lower():
        irc.send(channel, "THE HERD")

    if "PRIVMSG" in text and channel in text and ("tom brady" in text.lower() or "tb12" in text.lower() or "touchdown tommy" in text.lower()):
        irc.send(channel, "the GOAT")

    if "PRIVMSG" in text and channel in text and "spider_bot" in text.lower():
        irc.send(channel, ":D")

    if "PRIVMSG" in text and channel in text and "the herd" in text.lower():
        irc.send(channel, "ALL THE GOATS")

    if "PRIVMSG" in text and channel in text and "idea" in text.lower():
        irc.send(channel, "it's gonna be HUUUGGEEE")
