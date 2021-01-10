import re, sys

def cleanURL(txt):
    replDict = {
        ' ' : '-',
        '.' : ''
    }
    for key, value in replDict.items():
        txt = txt.replace(key, value)
    return txt

def addPadding(mark, level):
    marks = ''
    for i in range(level * 2):
        marks += mark
    return marks

def createTOC(inputFile, outputFile, mark='.'):
    """Creates a simple table of contents based on the links of the markdown file provided to the function.
    Then it writes it to a file"""
    with open(inputFile, 'r') as f:
        data = f.read()

    with open(outputFile, 'w') as f:
        f.write('## Table of Contents\n\n')
        pattern = re.compile(r'(?P<Level>#*)\s*(?P<Heading>.*)')
        for line in data.splitlines():
            if line.startswith('##'):
                match = pattern.search(line)
                if len(match.group('Level')) == 2:
                    f.write(f"**[{match.group('Heading')}](#{cleanURL(match.group('Heading'))})**\n\n")
                else:
                    f.write(f"**[{addPadding(mark, len(match.group('Level')))}{match.group('Heading')}](#{cleanURL(match.group('Heading'))})**\n\n")

if __name__ == '__main__':
    outputFile = sys.argv[2]
    inputFile = sys.argv[1]
    try:
        createTOC(inputFile, outputFile, sys.argv[4])
    except IndexError:
        createTOC(inputFile, outputFile)