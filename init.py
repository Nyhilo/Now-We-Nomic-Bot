#

#imports for python modules
import discord

#imports for local files
import thebot
import point_management
import events

def main():
    thebot.init()
    point_management.init()
    events.init()


if __name__ == '__main__':
    main()