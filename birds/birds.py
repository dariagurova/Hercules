import os
import sys

class color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

HOME = os.environ['HOME']
login = os.environ['USER']
name = sys.argv[1]
lang = sys.argv[2]
path = HOME + '/' + name

if not len(sys.argv) > 2:
	print color.RED + " -> usage: python birds.py [name] [language] <-"  + color.RESET
	sys.exit()

def header_file( name ):
	header = open(path + '/' + name + '.h','wr+')
	header.write('#ifndef ' + name.upper() + '_H\n# define ' + name.upper() + '_H\n\n# include <libraries>\n\n#endif')
	print color.GREEN + ' => ' + name + '.h created.\n' + color.RESET
	header.close()

def author_file( name ):
	author = open(path + '/' + 'author','wr+')
	author.write(login + '\n')
	print color.GREEN + ' => author file was created.\n' + color.RESET
	author.close()

def gitignore( lang, name ):
	gitignore = open(path + '/.gitignore', 'wr+')
	gitignore.write('# System Files\n*.DS*\n*.swp*\n*._*\n*.dll\n\n')
	if (lang == 'C' or lang == 'c'):
		gitignore.write('# C files\n*.o\n\n# Executables\n*.exe\n*.out\n\n# Debug Files\n*.dSYM/\n\n')
	print color.GREEN + ' => .gitignore added.\n' + color.RESET
	gitignore.close()

def makefile( name ):
	file = open(path + '/Makefile','wr+')
	file.write('name = ' + name + '\n\n' + 'SRC += main.c' + '\n\n' + 'OBJ = $(SRC:.c=.o)')
	lft = ""
	Lflag = ""
	libft = 'libft'
	if (raw_input(' -> Get libft from home dir into project dir (y/n)? ') == 'y'):
		if os.path.exists(HOME + '/' + libft):
			if not os.path.exists(path + '/libft'):
				os.system('mkdir ' + path + '/libft')
			os.system('cp -a ' + HOME + '/' + libft + '/. ' + path + '/libft/')
		else:
			print color.RED + " Error: libft/ directory was not found " + HOME + color.RESET
		lft = "\tmake -C libft/\n"
		Lflag = " -L libft -lft"
		print color.GREEN + " => libft/ added to project.\n" + color.RESET
	rules = "$(name): $(OBJ)\n" + lft + "\t$(CC) $(OBJ) -o $(name)" + Lflag + '\n\n'
	file.write('\n\n' + 'CC = gcc -Wall -Wextra -Werror\n\n')
	file.write(rules + 'all: $(name)\n\nclean:\n\t@rm -rf $(OBJ)\n\nfclean: clean\n\t@rm -rf $(name) $(OBJ) \n\nre: fclean $(name)')
	print color.GREEN + ' => Makefile will create exe ./' + name + '\n' + color.RESET
	file.close()

def create_project( lang, name ):
	if (lang == 'C' or lang == 'c'):
		makefile(name)
		header_file(name)
		gitignore(lang, name)
	if (raw_input(' -> Do you want to create an author file (y/n)? ') == 'y'):
		author_file(name)
if not os.path.exists(path):
	os.makedirs(path)
	print color.GREEN + '\n => created directory ' + path + '\n' + color.RESET
else:
	print color.GREEN + ' => directory ' + path + ' already exists.\n' + color.RESET
create_project(lang, name)

print color.BLUE + '\n -> Project was created. <- \n' + color.RESET
