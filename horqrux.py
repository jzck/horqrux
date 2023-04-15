#!/bin/env python

import random
import sys
from copy import copy

import qrcode
import qrcode.image.svg
from bs4 import BeautifulSoup
from more_itertools import chunked_even

factory = qrcode.image.svg.SvgFragmentImage
qrcode = qrcode.make(sys.argv[1], image_factory=factory)
svg_string = qrcode.to_string(encoding='unicode')
with open("horcrux_full.svg", 'w') as f:
    f.write(svg_string)
svg = BeautifulSoup(svg_string, 'xml')
svg_object = svg.find('svg:svg')

rects = svg.find_all('svg:rect')
random.shuffle(rects)
horcruxes = chunked_even(rects, len(rects)//6)

svg_object.clear()

# write horcruxes to svg files
for idx, horcrux in enumerate(horcruxes):
    horcrux_svg = copy(svg_object)
    for rect in horcrux:
        horcrux_svg.append(rect)
    with open(f"horcrux_{idx + 1}.svg", 'w') as f:
        f.write(str(horcrux_svg))
