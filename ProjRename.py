#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Find and Rename script
#The script take three variables as input - path to the folder, target word and a new word.
#It searches through the project's folders, files and text data for occurences of the target word and renames them to the new word.

import sys, os, shutil, mmap

path = ""
target = ""
name = ""

#Command 1: gathering user input
def GatherInputs():
	inputs = sys.argv
	if len(inputs) < 3:
		print """Incorrect number of input variables. Please, specify three variables:
path to the project folder, target word and a word to which target will be renamed."""
	else:
		global path
		global target
		global name
		path = sys.argv[1]
		if not os.access(path, os.F_OK):
			print "The path you have stated is either incorrect or inaccessible."
		target = sys.argv[2]
		name = sys.argv[3:]
		if len(name)>1:
			fullname = ""
			for e in name:
				fullname = fullname + " " + str(e)
			name=fullname	
		else:
			name=str(name[0])
	return path, target, name

#Command 2: find and rename words
def FindAndRename(path,target,name):
	os.chdir(path)
	filelist = os.listdir(path)
	if len(filelist) > 0:
		for e in filelist:
			if os.path.isdir(path+"/"+e):
				FindAndRename(path+"/"+e,target,name)
				os.chdir(path)
			else:
				'''file_object = open(e)
				data_string = mmap.mmap(file_object.fileno(), 0, access=mmap.ACCESS_WRITE)
				point = data_string.find(" " + target + " ")
				target_size = len(" " + target + " ")
				while point != -1:
					end = point + target_size + 1
					data_string[point:end] = name
					point = data_string[end:].find(" " + target + " ")'''
				extension = e.split(".")[-1]
				if e == target+"."+extension:
					if os.path.exists(path+"/"+name+"."+extension):
						print "The file with such name already exists."
					else:
						os.rename(e,name+"."+extension)
	base=os.path.basename(path)
	path=path[:path.rfind("/"+base)]
	os.chdir(path)
	if base == target:
		if os.path.exists(path+"/"+name):
			print "Such directory already exists."
		else:
			shutil.move(base,name)

#Main function
def main():
	GatherInputs()
	FindAndRename(path,target,name)

main()
