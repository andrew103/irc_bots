from irc import IRC
from secrets import get_server, get_channel
from time import sleep


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


def bot_run():
    channel = get_channel()
    server = get_server()
    nickname = "spider_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    # Infinite loop until disconnected
    while True:
        text = filter_input(irc.get_text())
        print text

        if check_msg(text, channel) and "*snap*" in text.lower():
            irc.send(channel, "Alexis...I don't feel so good...")
            irc.quit("disintegrated")

            if nickname == "spider_bot":
                nickname = "CAPTAIN_MARVEL"
            elif nickname == "CAPTAIN_MARVEL":
                nickname = "spider_bot"

            sleep(5)

            # Because quitting closes the connection with the server
            irc = IRC()
            irc.connect(server, channel, nickname)

        if check_msg(text, channel) and "goat" in text.lower():
            with open("./static/battle_goat.txt", "r") as goat:
                lines = goat.readlines()
                for line in lines:
                    irc.send(channel, line.strip("""\n"""))

        if check_msg(text, channel) and "pineapple" in text.lower():
            with open("./static/pineapple.txt", "r") as pineapple:
                lines = pineapple.readlines()
                for line in lines:
                    irc.send(channel, line.strip("""\n"""))

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
            irc.send(channel, "it's gonna be YUUUGGEEE")

        if "QUIT" in text:
            irc.send(channel, "*mic drop*")


if __name__ == "__main__":
    bot_run()
