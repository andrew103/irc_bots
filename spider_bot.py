from irc import IRC
from secrets import get_server, get_channel
from time import sleep


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def spider_bot():
    channel = get_channel()
    server = get_server()
    nickname = "spider_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    # Infinite loop until disconnected
    while True:
        text = irc.get_text()
        print text

        if check_msg(text, channel) and "*snap*" in text.lower():
            irc.send(channel, "Alexis...I don't feel so good...")
            irc.quit("disintegrated")

            if nickname == "spider_bot":
                nickname = "CAPTAIN_MARVEL"
            elif nickname == "CAPTAIN_MARVEL":
                nickname = "spider_bot"

            sleep(5)

            # Because quitting closes the conntection with the server
            irc = IRC()
            irc.connect(server, channel, nickname)

        if check_msg(text, channel) and "goat" in text.lower():
            irc.send(channel, "THE HERD")

        if check_msg(text, channel)\
           and ("tom brady" in text.lower()
                or "tb12" in text.lower()
                or "touchdown tommy" in
                text.lower()):
            irc.send(channel, "the GOAT")

        if check_msg(text, channel) and "spider_bot" in text.lower():
            irc.send(channel, ":D")

        if check_msg(text, channel) and "the herd" in text.lower():
            irc.send(channel, "ALL THE GOATS")

        if check_msg(text, channel) and "idea" in text.lower():
            irc.send(channel, "it's gonna be HUUUGGEEE")


if __name__ == "__main__":
    spider_bot()
