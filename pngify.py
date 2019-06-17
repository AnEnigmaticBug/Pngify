#!/usr/bin/python3

from argparse import ArgumentParser
from subprocess import call, DEVNULL
from sys import stderr

def pngify(wd, ht, png_name, svg_name):
    try:
        call(['inkscape', '-z', '-e', png_name, '-w', str(wd), '-h', str(ht), svg_name], stderr=DEVNULL)
    except FileNotFoundError:
        print('Error: Inkscape isn\'t installed', file=stderr)
        exit(-1)

parser = ArgumentParser(description='Get PNGs from SVGs. Useful for Flutter.')
parser.add_argument('--wd', required=True, type=int)
parser.add_argument('--ht', required=True, type=int)
parser.add_argument('--variants', required=False, nargs='+', type=float)
parser.add_argument('--svgs', required=True, nargs='+')

args = parser.parse_args()

call(['mkdir', '-p', 'images'])

if args.variants is not None:
    for variant in args.variants:
        call(['mkdir', '-p', 'images/' + str(variant) + 'x'])

for svg_name in args.svgs:
    img_name, _, _ = svg_name.partition('.svg')

    png_name = 'images/' + img_name + '.png'
    pngify(args.wd, args.ht, png_name, svg_name)

    if args.variants is not None:
        for variant in args.variants:
            wd = int(args.wd * variant)
            ht = int(args.ht * variant)
            png_name = 'images/' + str(variant) + 'x' + '/' + img_name + '.png'
            pngify(wd, ht, png_name, svg_name)