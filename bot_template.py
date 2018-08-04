from irc import IRC
from secrets import get_channel, get_server


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def bot_template():
    channel = get_channel()
    server = get_server()
    nickname = "test_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    while True:
        text = irc.get_text()
        print text

        if check_msg(text, channel) and "test" in text.lower():
            irc.send(channel, "Test successful!")


if __name__ == "__main__":
    bot_template()
