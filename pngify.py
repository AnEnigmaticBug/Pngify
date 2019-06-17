#!/usr/bin/python3

from argparse import ArgumentParser

parser = ArgumentParser(description='Get PNGs from SVGs. Useful for Flutter.')
parser.add_argument('--wd', required=True, type=int)
parser.add_argument('--ht', required=True, type=int)
parser.add_argument('--variants', required=False, nargs='+', type=float)
parser.add_argument('--svgs', required=True, nargs='+')

print(parser.parse_args())