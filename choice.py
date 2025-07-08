import sys

global dictionary

(IN, PRO, CON, QUE, AST, LNK, OUT) = range(7)
mode_map = {
    "<": IN,
    "+": PRO,
    "-": CON,
    "?": QUE,
    "*": AST,
    "#": LNK,
    ">": OUT,
}

#(CON, QUE, PRO, IN, OUT, AST, LNK) = range(-1, 6)

err_map = {
    IndexError: 0-1j,
    ValueError: 0j,
}

def strips(s, keys):
    for v in keys:
        if v in s:
            s.strip(v)
    return s


def read_line(line:str) -> tuple[int, int, str]:
    try:
        first = line.strip()[0]
    except IndexError:
        return 0, err_map[IndexError], line
    white = len(line.strip('\n')) - len(line.strip('\n').strip('\t').strip())
    #white = len(strips(line, '\n')) - len(strips(line, ['\n', ' ', '\t']))
    if first in mode_map.keys():
        return mode_map.get(first), white, line
    elif first.isalpha():
        return err_map[ValueError], white, line
    else:
        raise ValueError(
            "Line \"{}\" wasn't read, key {} is unprocessable"
            .format(line, first)
        )


def process_line(*args):
    print(*args)
    if args[0] == 0:
        if args[1] == IN:
            pass # INPUT
        if args[1] == err_map["index"]:
            pass # SPACE - NEXT OPRTION
        if args[1] == OUT:
            pass # OUTPUT
    else:
        pass #

'''
def process_lines(lines:list[tuple], prev:str= None):
    for x in lines:
        if x[0] > 1:
            if x[0] == 2:
                pass # INPUT / FORK
            if x[0] == 3:
                pass # PROGRAM OUTPUT
            if x[0] == 4:
                pass # ASTRISK - ADDITIONAL INFO
            if x[0] == 5:
                pass # HASH - LINKING
'''


for i in range(1, len(sys.argv)):
    lines = list()
    print(sys.argv[i])
    with open(sys.argv[i], 'r') as r:
        for line in r.readlines():
            l = read_line(line)
            print(l)
            lines.append(l)
    
    
