from irc import IRC
from secrets import get_channel, get_server


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def filter_input(text, nums=False, chars=False, symbols=False, nofilter=False):
    if nofilter:
        return text

    output = "".join([c for c in text if ord(c) > 31])

    if nums:
        output = "".join([c for c in output if not (ord(c)>47 and ord(c)<58)])

    if chars:
        output = "".join([c for c in output if not (ord(c)>64 and ord(c)<91)
                                            and not(ord(c)>96 and ord(c)<123)])

    if symbols:
        output = "".join([c for c in output if not (ord(c)>31 and ord(c)<48)
                                            and not(ord(c)>57 and ord(c)<65)
                                            and not(ord(c)>90 and ord(c)<97)
                                            and not(ord(c)>122)])

    return output


def bot_template():
    channel = get_channel()
    server = get_server()
    nickname = "test_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    while True:
        text = filter_input(irc.get_text())
        print text

        if check_msg(text, channel) and "test" in text.lower():
            irc.send(channel, "Test successful!")


if __name__ == "__main__":
    bot_template()
