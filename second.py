import sys
import math

def raise_error(error):
	print('I expect one, two or three command line arguments,'
'the second one being "minimally" in case two of those are provided'
'and "using" in case three of those are provided.',error)

provided_input = sys.argv[1:]

if len(provided_input) == 1 or len(provided_input) ==2 or len(provided_input)==3:
	if len(provided_input) == 2:
		if provided_input[1] == 'minimally':
			pass
		raise_error('2')
	if len(provided_input) == 3:
		if provided_input[1] == 'using':
			pass
		raise_error('3')

	print('') 
else:
	raise_error('1')




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

p = intToRoman(100)
print(p)



