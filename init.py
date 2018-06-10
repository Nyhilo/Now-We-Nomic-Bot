#

#imports for python modules

#imports for local files
import thebot
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    thebot.init()

if __name__ == '__main__':
    main()