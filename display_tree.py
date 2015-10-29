# Sublime Text 3 for OS X
# Copyright (c) 2015 Subramanya Vajiraya
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# 
# Written by Subramanya Vajiraya (z5081713) and Eric Martin for COMP9021

import sys

default_nodestyle = None
grow_style = None
nodes = []
op_ready=[]
filename = None
def process_arguments():
	global filename
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
			filename = args[0]
			open_file(filename)
		if not args[0].endswith('.txt') and len(args)==1:
			raise_error(5)
	if len(args) > 1:
		valid = [True for x in args[:len(args)-1] if x.endswith('.txt')]
		if len(valid)==1:
			raise_error(4)
		else:
			if args[0] == '-nodestyle':
				if args[1] in nodestyles:
					default_nodestyle = args[1]
				else:
					raise_error(7)
				if len(args) > 3:
					if args[2] == '-grow':
						if args[3] in grow_list:
							grow_style = args[3]
						else:
							raise_error(6)
					else:
						raise_error(9)

			if args[0] == '-grow':
				if args[1] in grow_list:
					grow_style = args[1]
				else:
					raise_error(7)
				if len(args) > 3:
					if args[2] == '-nodestyle':
						if args[3] in nodestyles:
							default_nodestyle = args[3]
						else:
							raise_error(6)
					else:
						raise_error(9)
		filename = args[len(args)-1]
		open_file(filename)

def open_file(filename):
	num_space = 0
	with open(filename, 'r') as file:
		x = scan_file(file)
lines = 0
def scan_file(file):
	parents = [None]*100
	space_validation = []
	global lines 
	x = 0
	y = 0
	parent = None
	global nodes
	for line in file:
		if len(line.strip()) > 0:
			lines += 1
			if lines == 1:
				x = len(line) - len(line.lstrip(' '))
				root = line.strip()
				parents[0] = None
				nodes.append([root,1,parents[0],None])
				space_validation.append(x)
				
			elif lines == 2:
				y = len(line) - len(line.lstrip(' '))
				y = y-x
				num_space = len(line) - len(line.lstrip(' '))
				curr_node = line.strip()
				parents[1] = root
				nodes.append([curr_node,2,parents[1],None])
				parents[2] = curr_node
				prev_numspace = num_space
				space_validation.append(num_space)
				
			else:
				num_space = len(line) - len(line.lstrip(' '))
				if not (num_space) - y in space_validation:
					raise_error(8)
				if num_space > prev_numspace and not num_space == (prev_numspace + y):
					raise_error(10)
				space_validation.append(num_space)
				level = int((num_space - x)/y) + 1
				curr_node = line.strip()
				if curr_node == '':
					nodes.append(['child',level,parents[level-1],1])
					if level >= 1:
						parents[level] = curr_node
				elif curr_node == '':
					nodes.append(['child[fill=none] {edge from parent[draw=none]}',level,parents[level-1],2])
					if level >= 1:
						parents[level] = curr_node
				else:
					nodes.append([curr_node,level,parents[level-1],None])
					prev_node = curr_node
					if level >= 1:
						parents[level] = curr_node
					prev_numspace = num_space

	if lines < 2:
		raise_error(3)
	else:
		create_file()

def raise_error(_id):
	global lines
	if _id >= 8:
		print("Wrong number of leading spaces on nonblank line ",lines)
	else:
		print('Incorrect invocation')
	sys.exit()

def create_file():
	global filename
	global default_nodestyle
	global grow_style
	par_flag = False
	endflag = False
	spcflag = False
	brackets_req = True
	prev_level = 1
	openlevel = 0
	a = 1
	parents = list()
	op_file = open(filename[:-4]+'.tex','w')
	op_file.write("\documentclass[10pt]{article}\n\\usepackage{tikz}\n\\usetikzlibrary{shapes}\n\pagestyle{empty}\n\n\\begin{document}\n\n\\begin{center}\n\\begin{tikzpicture}\n")
	if not grow_style == None:
		op_file.write("[grow'="+grow_style+"]\n")
	if not default_nodestyle == None:
		op_file.write("\\tikzstyle{every node}=["+default_nodestyle+",draw]\n")
	for k in nodes:
		parents.append(k[2])
	for i in range(0,len(nodes)):
		if nodes[i][2] == None:
			op_file.write("\\node {"+nodes[i][0]+"}\n")
			curr_parent = nodes[i][0]
			prev_parent_node = nodes[i][0]
		else:
			if nodes[i][3] == None:
				if prev_level - nodes[i][1] > 1 and brackets_req:
					spcflag = True
				if not spcflag:
					for j in range(0,4*(nodes[i][1]-1)):
						op_file.write(" ")
				if prev_level > nodes[i][1]:
					if prev_level - nodes[i][1] > 1 and brackets_req:
						req_range = prev_level - nodes[i][1]
						for m in range(req_range,0,-1):
							for j in range(0,(4*m)):
								op_file.write(" ")
							op_file.write("}\n")
							openlevel -= 1
							par_flag = False
							a += 1
						spcflag = False
					elif brackets_req:
						op_file.write("}\n")
						openlevel -= 1
						par_flag = False
					for j in range(0,4*(nodes[i][1]-1)):
						op_file.write(" ")
				if nodes[i][0] not in parents:
					if prev_level > nodes[i][1] and par_flag:
						for j in range(0,4*(nodes[i][1]-1)):
							op_file.write(" ")
						op_file.write("}\n")
						openlevel -= 1
						par_flag = False

					if i == len(nodes)-1 and not par_flag:
						op_file.write("child {node {"+nodes[i][0]+"}};\n")
						endflag = True
					else:
						op_file.write("child {node {"+nodes[i][0]+"}}\n")
					if i == len(nodes)-1 and openlevel == 1:
						brackets_req = False
					if i == len(nodes)-1 and par_flag:
						if prev_level - nodes[i][1] > 1 and brackets_req:
							a = 1
							req_range = prev_level - nodes[i][1] 
							for m in range(0,req_range):
								for j in range(0,4*(nodes[i][1]-(a))):
									op_file.write(" ")
								op_file.write("}\n")
								openlevel -= 1
								par_flag = False
								a += 1
						elif brackets_req:
							for j in range(0,4*(nodes[i][1]-2)):
								op_file.write(" ")
							op_file.write("}\n")
							openlevel -= 1
							brackets_req = False
				else:
					op_file.write("child {node {"+nodes[i][0]+"}\n")
					openlevel += 1
					par_flag = True
					brackets_req = True
			if nodes[i][3] == 1:
				if prev_level > nodes[i][1] and par_flag and not prev_level - nodes[i][1] > 1:
					for j in range(0,4*(nodes[i][1]-1)):
						op_file.write(" ")
					op_file.write("}\n")
					openlevel -= 1
					par_flag = False
				if prev_level - nodes[i][1] > 1 and brackets_req:
					req_range = prev_level - nodes[i][1]
					a= 0
					for m in range(0,req_range):
						for j in range(0,4*(nodes[i][1]+(a))):
							op_file.write(" ")
						a -= 1
						op_file.write("}\n")
						openlevel -= 1
						par_flag = False
						
				try:
					if nodes[i+1][1] > nodes[i][1]:
						brackets_req = False
						for j in range(0,4*(nodes[i][1]-1)):
							op_file.write(" ")
						op_file.write(nodes[i][0]+' {\n')
						openlevel += 1
						par_flag = True
						brackets_req = True
					else:
						for j in range(0,4*(nodes[i][1]-1)):
							op_file.write(" ")
						op_file.write(nodes[i][0]+'\n')
				except IndexError:
					pass

			elif nodes[i][3] == 2:
				for j in range(0,4*(nodes[i][1]-1)):
						op_file.write(" ")
				op_file.write("child[fill=none] {edge from parent[draw=none]}\n")
			prev_level = nodes[i][1]
	if endflag == False:
		op_file.write("    };\n")
	op_file.write("\\end{tikzpicture}\n\\end{center}\n\n\\end{document}\n")

process_arguments()
