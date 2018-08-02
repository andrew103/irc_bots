from irc import IRC
from secrets import get_channel, get_server


channel = get_channel()
server = get_server()
nickname = "THANOS"

irc_obj = IRC()
irc_obj.connect(server, channel, nickname)


while True:
    text = irc_obj.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "perfectly balanced"\
       in text.lower():
        irc_obj.send(channel, "As all things should be")

    if "PRIVMSG" in text and channel in text and "fun"\
       in text.lower():
        irc_obj.send(channel, "Fun isn't something one considers when balancing the universe")

    if "PRIVMSG" in text and channel in text and\
       "you should have gone for the head" in text.lower():
        irc_obj.send(channel, "*snap*")
