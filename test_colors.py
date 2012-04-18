#!/usr/bin/env python

from __future__ import print_function

from colors import color, COLORS, STYLES


for bg in (None,) + COLORS:
    for fg in (None,) + COLORS:
        for style in (None,) + STYLES:
            text = ('%s' % (fg or 'normal')).ljust(7)
            print(color(text, fg=fg, bg=bg, style=style), end=' ')
        print()

for i in range(256):
    if i % 64 == 0:
        print()
    print(color(' ', bg=i), end='')

print()
