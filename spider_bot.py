from irc import IRC
from secrets import get_server, get_channel
from time import sleep


channel = get_channel()
server = get_server()
nickname = "spider_bot"


irc_obj = IRC()
irc_obj.connect(server, channel, nickname)


# Infinite loop until disconnected
while True:
    text = irc_obj.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "*snap*" in text.lower():
        irc_obj.send(channel, "Alexis...I don't feel so good...")
        irc_obj.quit("disintegrated")

        if nickname == "spider_bot":
            nickname = "CAPTAIN_MARVEL"
        elif nickname == "CAPTAIN_MARVEL":
            nickname = "spider_bot"

        sleep(5)

        irc_obj = IRC()
        irc_obj.connect(server, channel, nickname)

    if "PRIVMSG" in text and channel in text and "goat" in text.lower():
        irc_obj.send(channel, "THE HERD")

    if "PRIVMSG" in text and channel in text and ("tom brady" in text.lower()
                                                  or "tb12" in text.lower() or
                                                  "touchdown tommy" in
                                                  text.lower()):
        irc_obj.send(channel, "the GOAT")

    if "PRIVMSG" in text and channel in text and "spider_bot" in text.lower():
        irc_obj.send(channel, ":D")

    if "PRIVMSG" in text and channel in text and "the herd" in text.lower():
        irc_obj.send(channel, "ALL THE GOATS")

    if "PRIVMSG" in text and channel in text and "idea" in text.lower():
        irc_obj.send(channel, "it's gonna be HUUUGGEEE")
