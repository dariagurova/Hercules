import os
import sys

class bc:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if not len(sys.argv) > 2:
	print bc.FAIL + " -> usage: python birds.py [name] [language] <-"  + bc.RESET
	sys.exit()

HOME = os.environ['HOME']
login = os.environ['LOGNAME']
name = sys.argv[1]
lang = sys.argv[2]
path = HOME + '/' + name

def makefile( name ):
	file = open(path + '/Makefile','wr+')
	file.write('# MAKEFILE : ' + name + '\n\n' + 'name = ' + name + '\n\n' + 'SRC += main.c' + '\n\n' + 'OBJ = $(SRC:.c=.o)')
	make_lft = ""
	flag_lft = ""
	libft = 'libft'
	if (raw_input(' -> Copy libft from home directory into project root (y/n)? ') == 'y'):
		if os.path.exists(HOME + '/' + libft):
			if not os.path.exists(path + '/libft'):
				os.system('mkdir ' + path + '/libft')
			os.system('cp -a ' + HOME + '/' + libft + '/. ' + path + '/libft/')
		else:
			print bc.FAIL + " (Error) no libft/ directory found in " + HOME + bc.RESET
		make_lft = "\tmake -C libft/\n"
		flag_lft = " -L libft -lft"
		print bc.GREEN + " => libft/ added to project.\n" + bc.RESET
	name_rules = "$(name): $(OBJ)\n" + make_lft + "\t$(CC) $(OBJ) -o $(name)" + flag_lft + '\n\n'
	file.write('\n\n' + 'CC = gcc -Wall -Wextra -Werror\n\n')
	file.write(name_rules + 'all: $(name)\n\nclean:\n\t@rm -rf $(OBJ)\n\nfclean: clean\n\t@rm -rf $(name) $(OBJ) \n\nre: fclean $(name)')
	print bc.GREEN + ' => Makefile will create exe ./' + name + '\n' + bc.RESET
	file.close()

def gitignore( lang, name ):
	gitignore = open(path + '/.gitignore', 'wr+')
	gitignore.write('# System Files\n*.DS*\n*.swp*\n*._*\n*.dll\n\n')
	if (lang == 'C' or lang == 'c'):
		gitignore.write('# C\n*.o\n\n# Executables\n*.exe\n*.out\n\n# Debug Files\n*.dSYM/\n\n')
	print bc.GREEN + ' => .gitignore added.\n' + bc.RESET
	gitignore.close()

def header_file( name ):
	header = open(path + '/' + name + '.h','wr+')
	header.write('#ifndef ' + name.upper() + '_H\n# define ' + name.upper() + '_H\n\n# include <libraries>\n\n#endif')
	print bc.GREEN + ' => ' + name + '.h created.\n' + bc.RESET
	header.close()

def author_file( name ):
	author = open(path + '/' + 'author','wr+')
	author.write(login + '\n')
	print bc.GREEN + ' => author file (' + lang + ') created.\n' + bc.RESET
	author.close()

def make_project( lang, name ):
	if (lang == 'C' or lang == 'c'):
		makefile(name)
		header_file(name)
		gitignore(lang, name)
	if (raw_input(' -> Do you want to create an author file (y/n)? ') == 'y'):
		author_file(name)

if not os.path.exists(path):
	os.makedirs(path)
	print bc.GREEN + '\n => created directory ' + path + '\n' + bc.RESET
else:
	print bc.GREEN + ' => verified directory ' + path + ' already exists.\n' + bc.RESET
make_project(lang, name)

print bc.BLUE + '\n -> Project was created. <- \n' + bc.RESET
