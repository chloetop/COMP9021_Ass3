import sys
# added Comm

default_nodestyle = None
grow_style = None

def process_arguments():
	global default_nodestyle
	global grow_style
	nodestyles = ['circle','rectangle','ellipse']
	grow_list = ['up','down','left','right']
	args = sys.argv[1:]
	if len(args) == 0 or len(args) > 5:
		raise_error(1)
	if len(args) % 2 == 0:
		raise_error(2)
	else:
		if len(args) == 1 and args[0].endswith('.txt'):
			open_file(args[0])
		if not args[0].endswith('.txt') and len(args)==1:
			raise_error(5)
	if len(args) > 1:
		valid = [True for x in args[:len(args)-1] if x.endswith('.txt')]
		print(valid)
		if len(valid)==1:
			raise_error(4)
		else:
			if args[0] == '-nodestyle':
				if args[1] in nodestyles:
					default_nodestyle = args[1]
			if len(args) > 2:
				if args[2] == '-nodestyle':
					if args[3] in nodestyles:
						default_nodestyle = args[3]
			if args[0] == '-grow':
				if args[1] in grow_list:
					grow_style = args[1]
			if len(args) > 2:
				if args[2] == '-grow':
					if args[3] in grow_list:
						grow_style = args[3]



def open_file(filename):
	num_space = 0
	with open(filename, 'r') as file:
		x = scan_file(file)

def scan_file(file):
	lines = 0
	x = 0
	y = 0
	nodes = []
	for line in file:
			if len(line.strip()) > 0:
				lines += 1
				if lines == 1:
					x = len(line) - len(line.lstrip(' '))
					nodes.append([])
				if lines == 2:
					y = len(line) - len(line.lstrip(' '))
					y = y-x

	if lines < 2:
		raise_error(3)
	else:
		print("X: ",x,'Y: ',y)
		return [x,y]

def raise_error(_id):
	print('Incorrect invocation',_id)
	sys.exit()

process_arguments()
