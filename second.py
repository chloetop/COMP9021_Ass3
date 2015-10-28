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

numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]

def roman_to_arabic(number):
    index_by_letter = {}
    for index in range(len(numerals)):
        index_by_letter[numerals[index]['letter']] = index

    result = 0
    previous_value = None
    for letter in reversed(number):
        index = index_by_letter[letter]
        value = numerals[index]['value']
        if (previous_value is None) or (previous_value <= value):
            result += value
        else:
            result -= value
        previous_value = value

    return result
# print(roman_to_arabic('V'))
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
    print('I expect one, two or three command line arguments,\nthe second one being "minimally" in case two of those are provided\nand "using" in case three of those are provided.',error)
    sys.exit()

def roman_error(error):
    print('The provided sequence of so-called generalised roman symbols is invalid,\neither because it does not consist of letters only \nor because some letters are repeated.',error)
    sys.exit()

def the_input_error(error):
    print('The input is not a valid arabic number,\nor is too large an arabic number,\nor is not a valid (possibly generalised) roman number,\ndepending on what is expected.',error)
    sys.exit()


# program starts here
provided_input = sys.argv[1:]
# range_list = [x for x in range(1,4000)]
global flag
flag =1
if len(provided_input) == 1 or len(provided_input) ==2 or len(provided_input)==3:
    # set_of_third_input = set(provided_input)
    if len(provided_input) == 1:
        # print(provided_input[0])
        regex = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
        if provided_input[0].isdigit():
            if int(provided_input[0])>0 and int(provided_input[0])<4000:
                if provided_input[0].startswith('0'):
                    the_input_error('8')
                else:
                    print(intToRoman(int(provided_input[0])))
            else:
                the_input_error('10')
        else:
            if regex.match((provided_input[0])):
                print(roman_to_arabic(provided_input[0]))
            else:
                the_input_error('11')
    elif len(provided_input) == 2:
        if provided_input[1] == 'minimally':
            print('correct')
        else:
            print(provided_input[1])

            raise_error('2')
    elif len(provided_input) == 3:
        values = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

        if provided_input[1] == 'using' and values.match(provided_input[2]):
                print('correct',roman_to_arabic(provided_input[0]))

        elif not values.match(provided_input[2]):
            # flag = 1
            for i in range(len(provided_input[2])):
                # flag = 1
                if provided_input[2][i].isdigit():
                    roman_error('6')
                    # break
                    # flag +=1
        if len(provided_input[2]) != len(set(provided_input[2])):
            roman_error('7')


        else:
            raise_error('3')

else:
    raise_error('1')

