#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, shutil
path = sys.argv[1]
name = sys.argv[2:]
if len(name)>1:
	fullname = ""
	for e in name:
		fullname = fullname + " " + str(e)
	name=fullname	
else:
	name=str(name[0])
def RenameFolders (path,name,base):
	count=os.listdir(path).count(name)
	if base[0].isupper and name[0].islower:
		name[0].upper
	elif base[0].islower and name[0].isupper:
		name[0].lower
	if count < 1:
		shutil.move(base,name)
	else:
		RenameFolders(path,name+"|",base)
def RenameFiles (path,name,e,extension):
	count=os.listdir(path).count(name+"."+extension)
	if e[0].isupper and name[0].islower:
		name[0].upper
	elif e[0].islower and name[0].isupper:
		name[0].lower
	if count < 1:
		os.rename(e,name+"."+extension)
	else:
		RenameFiles(path,name+"|",e,extension)
def ProjectRename(path,name):
	if os.access(path, os.F_OK):
		os.chdir(path)
		filelist = os.listdir(path)
		if len(filelist) > 0:
			for e in filelist:
				if os.path.isdir(path+"/"+e):
					ProjectRename(path+"/"+e,name)
					os.chdir(path)
				else:
					extension=e.split(".")[-1]
					RenameFiles(path,name,e,extension)
		base=os.path.basename(path)
		path=path[:path.rfind("/"+base)]		
		os.chdir(path)
		RenameFolders(path,name,base)
	else:
		print """The path you have specified was not found.
Please, check your inputs and try again."""
ProjectRename(path,name)
