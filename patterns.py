def printDownTringlePattern(intNumberOfLines):
    for rows in range(intNumberOfLines):
        print(' ' * rows, ' *' * (intNumberOfLines-rows))


def printUpTringlePattern(intNumberOfLines):
    for rows in range(intNumberOfLines):
        print(' ' * (intNumberOfLines-rows), ' *' * rows)

def printUpwardTringlePattern(intNumberOfLines):
    for rows in range(intNumberOfLines):
        print('* ' * rows, ' ' * (intNumberOfLines-rows))

    for rows in range(intNumberOfLines):
        print('* ' * (intNumberOfLines - rows))


printUpTringlePattern(18)
printDownTringlePattern(18)
printUpwardTringlePattern(5)
