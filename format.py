
def center(text, length, rightAligned):
    spaces = length - len(text)
    if spaces <= 0:
        return text[0:length]
    else:
        spacesLeft = int(spaces / 2)
        spacesRight = int(spaces - spacesLeft)
        
        if rightAligned:
            return spacer(spacesRight) + text + spacer(spacesLeft)
        else:
            return spacer(spacesLeft) + text + spacer(spacesRight)
        
def spacer(length):
    return " " * length
