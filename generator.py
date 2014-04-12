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
    2048:"#BB0000"
}

def main(amount_mapping):
    yield """<html>
        <head>
            <title>Jotari QR Codes</title>
        </head>"""
    yield """<body style="font-family:arial; font-size:80px">"""

    yield "\n".join(generate_table(amount_mapping))

    yield """\n\t</body></html>"""

def generate_table(amount_mapping):
    cells = generate_cards(amount_mapping)
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

def generate_cards(amount_mapping):
    for value, amount in amount_mapping.iteritems():
        for i in range(amount):
            yield """<div style='
                border: solid 1px; 
                text-align: center; 
                width: 200px; 
                height: 240px; 
                line-height: 240px;
                margin: 5px; 
                vertical-align:bottom; 
                padding: 10px;
                font-size: 80px;
                background-color: {1}'>
            {0}</div>""".format(value, colors[value])

if __name__ == "__main__":
    filename = sys.argv[1]

    amount_mapping = OrderedDict()
    for k in range(1,12):
        amount_mapping[2**k] = 20

    with file(filename, "w+") as f:
        for html in main(amount_mapping):
            f.write(html)