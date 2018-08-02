from irc import IRC
from secrets import get_channel, get_server
import emoji

channel = get_channel()
server = get_server()
nickname = "emoji_bot"  # Bot name


def check_msg(text):
    return "PRIVMSG" in text and channel in text


def emoji_bot_help():
    irc.send(channel, "Emojis available:")
    irc.send(channel, "smiles, winks, laughs, fistbombs, heart, smirks, sleeps, cool, cries, tongue")
    irc.send(channel, "Use '*' before and after the option. Ex: *smiles*")


def emoji_bot():
    # Infinite loop until disconnected
    while True:
        text = irc.get_text()
        print text

        # Retrieve Emojibot helper  whenever "emoji_bot --help" is called
        if check_msg(text) and "emoji_bot --help" in text.lower():
            emoji_bot_help()

        # -------------------- Various emojis implemented ---------------------

        if check_msg(text) and "*smiles*" in text.lower():
            irc.send(channel, emoji.emojize(':smiley:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*winks*" in text.lower():
            irc.send(channel, emoji.emojize(':wink:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*laughs*" in text.lower():
            irc.send(channel, emoji.emojize(':joy:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*fistbombs*" in text.lower():
            irc.send(channel, emoji.emojize(':punch:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*heart*" in text.lower():
            irc.send(channel, emoji.emojize(':hearts:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*smirks*" in text.lower():
            irc.send(channel, emoji.emojize(':smirk:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*sleeps*" in text.lower():
            irc.send(channel, emoji.emojize(':zzz:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*cool*" in text.lower():
            irc.send(channel, emoji.emojize(':sunglasses:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*cries*" in text.lower():
            irc.send(channel, emoji.emojize(':cry:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text) and "*tongue*" in text.lower():
            irc.send(channel, emoji.emojize(':stuck_out_tongue:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        # Secret mic_drop emoji not included in the emoji_bot_help
        if check_msg(text) and "*mic drop*" in text.lower():
            irc.send(channel, emoji.emojize(':microphone:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))


if __name__ == "__main__":
    irc = IRC()
    irc.connect(server, channel, nickname)

    # Implicitly render Emojibot helper on every successful connection attempt
    emoji_bot_help()
    emoji_bot()
