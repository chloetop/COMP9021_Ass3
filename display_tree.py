import sys
# added Comm
def process_arguments():
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
	two_node_flag = 0
	root = 0
	for line in file:
			if not line.strip():
				two_node_flag += 1
				if root == 0:
					spaces_before_nodes = len(line) - len(line.lstrip(' '))
					root = 1
	if two_node_flag < 2:
		raise_error(3)
	else:
		return spaces_before_nodes

def raise_error(_id):
	print('Incorrect invocation',_id)
	sys.exit()

process_arguments()
