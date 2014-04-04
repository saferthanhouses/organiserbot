import os
import re
import shutil

#0. LOOK AT THIS DIRECTORY

def dir_path():
	'''Returns the directory path.'''

	# This file's filepath
	here = os.path.realpath(__file__) 

	# This file's directory
	a = here.split('/')
	b = a[:-1]
	here = '/'.join(b)

	return here



def get_cont(here):
	''' Returns a dictionary of the files and folders in this directory.'''
	
	dir_cont = [n for n in os.listdir(here)]

	arr_cont = {'files':[], 'folders':[]}

	for n in dir_cont:
		if os.path.isfile(n): arr_cont[files].append(n)
		else: arr_cont[folders].append(n)

	return arr_cont




#2. OPEN AND SORT ORGANISE_INSTRUCT.TXT INTO MEMORY

def build_instr(inst_path):
	'''Given the instruction path, return a dictionary representation.'''

	instructions = {}

	with open(inst_path, encoding='utf-8') as inst:
		for line in inst:
			raw= [n.strip() for n in line.split(None)]
			if (len(raw) < 2) or (raw[0][0]=='.'):
				raise BadInstructionsError()
			else:
				instructions[raw[0]]=raw[1]

	return instructions



#3. FOR EACH FOLDER IN ORGANISE_INSTRUCT.TXT : - DETERMINE IF IT EXISTS ELSE CREATE IT.

def check_setup(here, instruct):
	'''Check that the folders listed in the instructions exist. If not, make them.'''

	for dirs in instruct.keys(): 
			dpath = os.path.join(here, dirs)

			if not os.path.exists(dpath):
				os.makedirs(dpath) 			



# 4. FOR EACH FILE IN THIS DIR:	- LOOK UP THE TARGET DIR.
#								- MOVE THE FILE

def move_files(dir_cont, instr, here):
	'''for each file in the contents, extract the filename, look it up in the instructions and move it there.'''
															
	for f in dir_cont['files']:

		ftype = extract_ftype(f) 		
		if ftype: 
			dest = find_dest(ftype)		

		if dest: 
			fpath = os.path.join(here, f)
			dpath = os.path.join(here, dest)

			shutil.move(fpath, dpath)



def extract_ftype(f):

	if f="organiser_bot.py" or "ORGANISE_INSTRUCT.txt":
		return None
	elif f[0]=='.':
		return None

	ft_regexp = r'(\.[a-z]+)?'
	ft = re.findall(ft_regexp, file_name)	
	
	return ''.join(file_type)



def find_dest(ftype, instr):
	f_types = [ft for dv in instr.values() for ft in dv]		# Flatten the lists of filetypes

	if ftype in f_types:										# Reverse Lookup not appropriate approach to dict/
		for n in instr:											# Not appropriate datatype for approach.
			if ftype in instr[n]:								# Solution? Tuples? ('picture', ['.jpg', '.gif'])
				return instr[n]

	else:
		return None



def main():

	here = dir_path()		# 0.

	instr_path = os.path.join(here), 'ORGANISE_INSTRUCT.txt')

	if os.path.exists(instr_path):			# 1.
		contents = get_cont(here)		# 0.

		instruct = build_instr(instr_path)  # 2.

		check_setup(here, instruct)		# 3.

		move_files(contents, instruct, here)


	else:
		pass # Something ...
