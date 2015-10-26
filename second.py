import sys
import math

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
        # print('integer=',integer,'num =',num)
        romanResult = ""
        for value, rchar in romanList:
            # print(value,'value',rchar,'rchar')
            count, num = divmod(num, value)
            # print('count=',count,'num =',num,)
            romanResult += count * rchar
            # print(romanResult)
        if romanResult:
            result.append('{}{}{}'.format(
                '(' * parenscount, romanResult, ')' * parenscount))
        parenscount += 1
    return ' '.join(result[::-1])

def raise_error(error):
    print('I expect one, two or three command line arguments,'
'the second one being "minimally" in case two of those are provided'
'and "using" in case three of those are provided.',error)

provided_input = sys.argv[1:]
range_list = [x for x in range(1,4000)]
# print(provided_input)
# regex_to_validate_roman_numerals = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
if len(provided_input) == 1 or len(provided_input) ==2 or len(provided_input)==3:
    if len(provided_input) == 1:
        if int(provided_input[0]) in range_list:
            # print('check')
            # regex_to_validate_roman_numerals = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
            # if provided_input.match()
            print(intToRoman(int(provided_input[0])))
        else:
            raise_error('invalid input')
    if len(provided_input) == 2:
        if provided_input[1] == 'minimally':
            pass
        raise_error('2')
    if len(provided_input) == 3:
        if provided_input[1] == 'using':
            pass
        raise_error('3')

    # print('') 
else:
    raise_error('1')






# p = intToRoman(80)
# print(p)



