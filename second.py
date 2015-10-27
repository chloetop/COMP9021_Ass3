import sys
import math
import re
# regex = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
romanList = [
    (1000, "M"), (900, "CM"),
    (500, "D"), (400, "CD"), 
    (100, "C"), (90, "XC"), 
    (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"),
    (5, "V"), (4, "IV"),
    (1, "I")
]

def intToRoman(integer):
    result = []
    parenscount = 0
    while integer:
        integer, num = divmod(integer, 4000)
        romanResult = ""
        for value, rchar in romanList:
            count, num = divmod(num, value)

            romanResult += count * rchar
        if romanResult:
            result.append('{}{}{}'.format(
                '(' * parenscount, romanResult, ')' * parenscount))
        parenscount += 1
    return ' '.join(result[::-1])

def raise_error(error):
    print('I expect one, two or three command line arguments,'
'the second one being "minimally" in case two of those are provided'
 'and "using" in case three of those are provided.',error)


# program starts here
provided_input = sys.argv[1:]
range_list = [x for x in range(1,4000)]

if len(provided_input) == 1 or len(provided_input) ==2 or len(provided_input)==3:
    if len(provided_input) == 1:
        if int(provided_input[0]) in range_list:

            print(intToRoman(int(provided_input[0])))
        else:
            raise_error('invalid input')
    elif len(provided_input) == 2:
        if provided_input[1] == 'minimally':
            print('correct')
        else:
            print(provided_input[1])

            raise_error('2')
    elif len(provided_input) == 3:
        values = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

        if provided_input[1] == 'using' and values.match(provided_input[2]):
            print('correct')
        else:
            raise_error('3')

else:
    raise_error('1')

