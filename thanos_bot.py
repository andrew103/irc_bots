from irc import *
from secrets import *
import unicodedata

channel = get_channel()
server = get_server()
nickname = "THANOS"

irc = IRC()
irc.connect(server, channel, nickname)


def check_msg(text):
    return "PRIVMSG" in text and channel in text


def filter_input(text):
    return "".join([c for c in text if c not in "0123456789" and ord(c) != 3])

while 1:
    text = irc.get_text()
    print filter_input(text)

    if check_msg(text) and "perfectly balanced" in filter_input(text).lower():
        irc.send(channel, "As all things should be")

    if check_msg(text) and "perfectly balanced"[::-1] in filter_input(text).lower():
        irc.send(channel, "As all things should be"[::-1])

    if check_msg(text) and "fun" in filter_input(text).lower():
        irc.send(channel, "Fun isn't something one considers when balancing the universe")

    if check_msg(text) and "you should have gone for the head" in filter_input(text).lower():
        irc.send(channel, "*snap*")
