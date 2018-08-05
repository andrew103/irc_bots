from irc import IRC
from secrets import get_channel, get_server
import emoji


def check_msg(text, channel):
    return "PRIVMSG" in text and channel in text


def emoji_bot_help(irc, channel):
    irc.send(channel, "Emojis available:")
    irc.send(channel, "smiles, winks, laughs, fistbombs, heart, smirks, sleeps, cool, cries, tongue")
    irc.send(channel, "Use '*' before and after the option. Ex: *smiles*")


def emoji_bot():

    channel = get_channel()
    server = get_server()
    nickname = "emoji_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    # Implicitly render Emojibot help on every successful connection attempt
    emoji_bot_help(irc, channel)

    # Infinite loop until disconnected
    while True:
        text = irc.get_text()
        print text

        # Retrieve Emojibot help  whenever "emoji_bot --help" is called
        if check_msg(text, channel) and "emoji_bot --help" in text.lower():
            emoji_bot_help(irc, channel)

        # -------------------- Various emojis implemented ---------------------

        if check_msg(text, channel) and "*smiles*" in text.lower():
            irc.send(channel, emoji.emojize(':smiley:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*winks*" in text.lower():
            irc.send(channel, emoji.emojize(':wink:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*laughs*" in text.lower():
            irc.send(channel, emoji.emojize(':joy:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*fistbombs*" in text.lower():
            irc.send(channel, emoji.emojize(':punch:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*heart*" in text.lower():
            irc.send(channel, emoji.emojize(':hearts:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*smirks*" in text.lower():
            irc.send(channel, emoji.emojize(':smirk:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*sleeps*" in text.lower():
            irc.send(channel, emoji.emojize(':zzz:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*cool*" in text.lower():
            irc.send(channel, emoji.emojize(':sunglasses:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*cries*" in text.lower():
            irc.send(channel, emoji.emojize(':cry:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        if check_msg(text, channel) and "*tongue*" in text.lower():
            irc.send(channel, emoji.emojize(':stuck_out_tongue:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))

        # Secret mic_drop emoji not included in the emoji_bot_help
        if check_msg(text, channel) and "*mic drop*" in text.lower():
            irc.send(channel, emoji.emojize(':microphone:',
                                            use_aliases=True).encode(
                                                "utf-8", "replace"))


if __name__ == "__main__":
    emoji_bot()
