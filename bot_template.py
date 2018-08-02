from irc import IRC
from secrets import get_channel, get_server


channel = get_channel()
server = get_server()
nickname = "test_bot"


irc_obj = IRC()
irc_obj.connect(server, channel, nickname)


while True:
    text = irc_obj.get_text()
    print text

    if "PRIVMSG" in text and channel in text and "test" in text.lower():
        irc_obj.send(channel, "Test successful!")
