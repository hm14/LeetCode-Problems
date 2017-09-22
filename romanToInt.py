# Problem prompt
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(self, s):
    intValue = 0
    previous = ''

    for c in s:
        if c == 'I':
            intValue += 1
        elif c == 'V':
            if previous == 'I':
                intValue += 3
            else:
                intValue += 5
        elif c == 'X':
            if previous == 'I':
                intValue += 8
            else:
                intValue += 10
        elif c == 'L':
            if previous == 'X':
                intValue += 30
            else:
                intValue += 50
        elif c == 'C':
            if previous == 'X':
                intValue += 80
            else:
                intValue += 100
        elif c == 'D':
            if previous == 'C':
                intValue += 300
            else:
                intValue += 500
        elif c == 'M':
            if previous == 'C':
                intValue += 800
            else:
                intValue += 1000
        previous = c

    return intValue        
