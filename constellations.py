"""Web Scraping from Wikipedia
idea inspired by David Ashton
code prepared for Mitali Contest #2 :)
"""
import urllib.request, re, random

url = 'http://en.wikipedia.org/wiki/IAU_designated_constellations'
with urllib.request.urlopen(url) as file:
    #html = str(file.read().decode('utf-8'))
    html = str(file.read())
    table = re.findall('<table.*?>(.*?)</table>', html)
    tr = re.findall("<tr>(.*?)</tr>", table[0])
    while '<th' in tr[0]:
        tr.pop(0)
    samp = random.sample(tr, 5)
    clean = lambda s: re.sub(r'(<span.*</span>)|(<sup.*</sup>)|(<.*?>)|(&.*?;)', '', s)
    for row in samp:
        cell = re.findall('<td.*?>(.*?)</td>', row)
        print(f'Constellation : {clean(cell[0])}')
        print(f'IAU Abbrev.   : {cell[1]}')
        print(f'NASA Abbrev.  : {cell[2]}')
        print(f'Genitive      : {clean(cell[3])}')
        print(f'Origin        : {clean(cell[4])}')
        print(f'Meaning       : {clean(cell[5])}')
        print(f'Brightest Star: {clean(cell[6])}')
        print()