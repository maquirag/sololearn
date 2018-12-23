"""Cowsay Woody Allen quotes"""


from random import choice


def splitsay(text, length=50):
    lines = []
    while len(text) > length:
        pos = text.find(' ',length)
        if pos == -1:
            break
        lines.append(text[:pos])
        text = text[pos+1:]
    if text:
        lines.append(text)
    return lines


def getboxchar(line,maxlines,side):
    if side == 'left':
        if maxlines == 1:
            return '<'
        elif line == 1:
            return '/'
        elif line == maxlines:
            return '\\'
        else:
            return '|'
    elif side == 'right':
        if maxlines == 1:
            return '>'
        elif line == 1:
            return '\\'
        elif line == maxlines:
            return '/'
        else:
            return '|'
    return None


def cowsay(text):
    lines = splitsay(text)
    maxlen = len(max(lines, key=lambda m: len(m)))
    print(' '+'-'*(maxlen+2))
    for k, v in enumerate(lines):
        print('{} '.format(getboxchar(k+1,len(lines),'left')),end='')
        print('{:^{w}}'.format(v, w=maxlen),end='')
        print(' {}'.format(getboxchar(k+1,len(lines),'right')), end='\n')
    print(' '+'-'*(maxlen+2))
    print(*cow, sep='\n')


cow = [
    ' ' * 6 + '\   ^__^',
    ' ' * 7 + '\  (oo)\_______',
    ' ' * 10 + '(__)\       )\\/\\',
    ' ' * 14 + '||----w |',
    ' ' * 14 + '||     ||'
]

say = [
    'I am thankful for laughter, except when milk comes out of my nose.',
    'It\'s not that I\'m afraid to die, I just don\'t want to be there when it happens.',
    'Sex is better than talk. Ask anybody in this bar. Talk is what you suffer through so you can get to sex.',
    'I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me.',
    'I don\'t want to achieve immortality through my work; I want to achieve immortality through not dying.',
    'All people know the same truth. Our lives consist of how we chose to distort it.',
    'I don\'t believe in an afterlife, although I am bringing a change of underwear.',
    'I can\'t listen to that much Wagner. I start getting the urge to conquer Poland.',
    'Love is the answer. But while you\'re waiting for the answer, sex raises some pretty good questions.',
    'Can we actually "know" the universe? My God, it\'s hard enough finding your way around in Chinatown.',
    'Money is better than poverty, if only for financial reasons.',
    'Sex without love is an empty experience ... but as empty experiences go, it\'s one of the best.',
    'Life doesn\'t imitate art, it imitates bad television.',
    'Science is an intellectual dead end, you know? It\'s a lot of little guys in tweed suits cutting up frogs on foundation grants.',
    'What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.',
    'A deranged person is supposed to have the strength of ten men. I have the strength of one small boy ... with polio.',
    'The lion and the calf shall lie down together but the calf won\'t get much sleep.'
]

moo = choice(say)
cowsay(moo)