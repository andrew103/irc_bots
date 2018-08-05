from irc import IRC
from secrets import get_channel, get_server


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def thanos_bot():
    channel = get_channel()
    server = get_server()
    nickname = "THANOS"

    irc = IRC()
    irc.connect(server, channel, nickname)

    # Infinite loop until disconnected
    while True:
        text = irc.get_text()
        print text

        if check_msg(text, channel) and "perfectly balanced" in text.lower():
            irc.send(channel, "As all things should be")

        if check_msg(text, channel) and "fun" in text.lower():
            irc.send(channel, "Fun isn't something one considers when balancing the universe")

        if check_msg(text, channel) and "you should have gone for the head"\
           in text.lower():
            irc.send(channel, "*snap*")


if __name__ == "__main__":
    thanos_bot()
