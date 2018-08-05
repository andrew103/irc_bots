from irc import IRC
from secrets import get_channel, get_server


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def filter_input(text):
    return "".join([c for c in text if c not in "0123456789" and ord(c) != 3])


def thanos_bot():
    channel = get_channel()
    server = get_server()
    nickname = "THANOS"

    irc = IRC()
    irc.connect(server, channel, nickname)

    # Infinite loop until disconnected
    while True:
        text = filtered_input(irc.get_text())
        print text

        if check_msg(text, channel) and "perfectly balanced" in text.lower():
            irc.send(channel, "As all things should be")

        if check_msg(text, channel) and "perfectly balanced"[::-1] in text.lower():
            irc.send(channel, "As all things should be"[::-1])

        if check_msg(text, channel) and "fun" in text.lower():
            irc.send(channel, "Fun isn't something one considers when balancing the universe")

        if check_msg(text, channel) and "you should have gone for the head"\
           in text.lower():
            irc.send(channel, "*snap*")


if __name__ == "__main__":
    thanos_bot()
