from multiprocessing import Process
from time import sleep

"""
This bot eradicates the need to run every bot individually
by clustering and running all of them together with
a single script
"""


def bot_import(bot_list):
    modules = map(__import__, bot_list)
    bot_process(modules, bot_list)


def bot_process(modules, bot_list):
    for mod in modules:
        # Changed the bot function names to bot_run()
        # to be able to use single interface attribute
        bot_process = Process(target=mod.bot_run)
        bot_process.start()
        sleep(1)


if __name__ == "__main__":
    # If you want to add a bot inorder to run it with
    # this script, just add module name to bot_list
    # without (.py) as demonstrated below and it will
    # be automatically imported and ran simultaneously
    bot_list = ["thanos_bot", "spider_bot", "emoji_bot"]
    bot_import(bot_list)
