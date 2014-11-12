#!/usr/bin/python

import sys, os, itertools
from collections import OrderedDict

def generate_colors():
    start = (0xFF, 0xFF, 0xCC)
    step = 0x11

    for power in range(11):
        color = (start[0], start[2], (start[2] + power*step))
        yield color

colors = {
    2   :"#FFFFCC",
    4   :"#FFFF99",
    8   :"#FFFF66",
    16  :"#FFFF33",
    32  :"#FFCC33",
    64  :"#FFCC00",
    128 :"#FF9900",
    256 :"#FF6600",
    512 :"#FF3300",
    1024:"#FF0000",
    2048:"#BB0000",
    ':' :"#000000"
}

def main(amount_mapping, use_color=True, border_colored=True):
    yield """<html>
        <head>
            <title>2048</title>
        </head>"""
    yield """<body style="font-family:arial; font-size:80px">"""

    yield "\n".join(generate_table(amount_mapping, use_color, border_colored))

    yield """\n\t</body></html>"""

def generate_table(amount_mapping, use_color=True, border_colored=True):
    cells = generate_cards(amount_mapping, use_color, border_colored)
    #import ipdb; ipdb.set_trace()
    total = sum(amount_mapping.values())
    columns = 4
    rows = (total/columns)+1

    yield "\n\t\t<table>"
    for rowno in range(rows):
        yield "\t\t\t<tr>"

        for i in range(columns):
            #print rowno, i
            try:
                cell = cells.next()
                yield "\t\t\t\t<td>"
                yield cell
                yield "\t\t\t\t</td>"
            except StopIteration:
                break
        #import pdb; pdb.set_trace()
        yield "\t\t\t</tr>"
    yield "\t\t</table>"

def generate_cards(amount_mapping, use_color=True, border_colored=True):
    #import ipdb; ipdb.set_trace()
    for value, amount in amount_mapping.iteritems():
        for i in range(amount):
            height,width = 180,180
            fill = colors[value] if use_color else "#ffffff"
            border = colors[value] if border_colored else "#000000"
            border_width = 10 if border_colored else 1
            height -= 2*border_width
            width -= 2*border_width
        
            yield """<div style='
                border: solid {5}px;
                border-color: {4};
                text-align: center; 
                width: {3}px; 
                height: {2}px; 
                line-height: {2}px;
                margin: 5px; 
                vertical-align:bottom; 
                padding: 10px;
                font-size: 70px;
                background-color: {1}'>
            {0}</div>""".format(value, fill, height, width, border, border_width)

if __name__ == "__main__":
    filename = sys.argv[1]
    if len(sys.argv) >= 3:
        use_color_arg = sys.argv[2]
        use_color = use_color_arg == "colored"
    else:
        use_color = False

    amount_mapping = OrderedDict()
    for k in range(1,12):
        amount_mapping[2**k] = 20

    amount_mapping[':'] = 12

    with file(filename, "w+") as f:
        for html in main(amount_mapping, use_color=False, border_colored=True):
            f.write(html)
