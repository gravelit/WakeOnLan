import argparse
import configparser
import re

from wakeonlan import send_magic_packet

parser = argparse.ArgumentParser(description='Calculates the cost of a deck using the Scryfall API')
parser.add_argument(dest='computer', nargs='?', default=None, help='Computer to wake')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read('wake.ini')

mac_pattern = r'\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2}'

computer = args.computer
mac = None
if computer:
    if computer.lower() in config:
        mac = config[computer.lower()]['mac']
        print('Waking {}...'.format(computer))
    elif re.match(mac_pattern, computer):
        mac = computer
        print('Waking {}...'.format(mac))

    if mac:
        send_magic_packet(mac)
    else:
        print('Could not find target computer {}'.format(computer))
