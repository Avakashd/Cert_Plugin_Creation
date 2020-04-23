import sys
import os
import re
import shutil
from distutils.dir_util import copy_tree

#oldPlugin = input(" Enter the old plugin name")
#newPlugin = input(" Enter the new plugin name")
#oldESXver = input(" Enter the Old ESX Version")
#newESXver = input(" Enter the New ESX Version")
#oldWorkbenchVer = input(" Enter the Old Workbench Version")
#newWorkbenchVer = input(" Enter the New Workbench Version")

#path = input(" Ente The Path").replace("\\","/")

buildcertkits = "" #input(" Enter the path of filename build-certkits.xml").replace("\\","/")
certkitsfilter = "" #input(" Enter the path of filename certkits_filters.py").replace("\\","/")
buildcallelements = "" #input(" Enter the path of filename build-certkits-allElements.xml").replace("\\","/")
certrpmmainfest = "" #input(" Enter the path of filename certkits.rpm.manifest").replace("\\","/")

def AddBuildCertkallelements(buildcallelements):
    lineArray = []
    os.chmod(buildcallelements, 0o777)
    with open(buildcallelements, "r") as in_file:
        buf = in_file.readlines()

    with open(buildcallelements, "w") as out_file:
        for line in buf:
            ReplacedLine = line
            if re.search(oldPlugin, line,re.IGNORECASE) is not None:
                ReplacedLine = (line.replace(re.search(oldplugin,(re.search(oldPlugin, line,re.IGNORECASE)).group(0)).group(0),newplugin))
                print ("Replaced Lines are \n " +ReplacedLine)
                if re.search(oldPlugin, ReplacedLine,re.IGNORECASE) is not None:
                    ReplacedLine = (line.replace(re.search(oldplugin,(re.search(regexp, ReplacedLine)).group(0)).group(0),newplugin))
                    print ("Replaced Lines are \n " +ReplacedLine)
            #ReplacedLine = (line.replace(bytes((oldPlugin), 'utf-8'),bytes((newPlugin), 'utf-8')))
            out_file.write(ReplacedLine)
    out_file.close()
    
def check():
    if not os.path.exists(buildcertkits):
        print ("\n"+buildcertkits+"Path doesnot exist")
        sys.exit()
    if not os.path.exists(certkitsfilter):
        print ("\n"+certkitsfilter+"Path doesnot exist")
        sys.exit()
    if not os.path.exists(buildcallelements):
        print ("\n"+buildcallelements+"Path doesnot exist")
        sys.exit()
    if not os.path.exists(certrpmmainfest):
        print ("\n"+certrpmmainfest+"Path doesnot exist")
        sys.exit()
    else :
        AddBuildCertkallelements(buildcertkits)
        AddBuildCertkallelements(certkitsfilter)
        AddBuildCertkallelements(buildcallelements)
        AddBuildCertkallelements(certrpmmainfest)

def check_extension(filename,filePath,oldPath):
    print ("entered to check_extention")
    print ("filename "+filename)
    print ("filePath "+filePath)
    for ext in fileexts:
        print ("extents "+ext)
        if filename.endswith(ext):
            print ('The file: ', filename, ' has the extension: ', ext)
            return True
        else:
            return False

def CreateDirectory(root1,subdir,oldPlugin,newPlugin):
    print ("Replacing ................................")
    print ("\n Existing directory name is "+subdir)
    replace = subdir.replace(oldPlugin,newPlugin)
    replacePath=root1+"/"+replace
    print ("path ....................................")
    print ("\n New directory name is "+replace)
    if not os.path.exists(replacePath):
        os.makedirs(replacePath)
        print ("\n"+replace+" Directory created ..............")
    else:
        print ("\n\n"+replacePath+" specified path Exist")
        sys.exit()


def RenameFile(root1,filePath1,filename,oldPlugin,newPlugin):
    print ("Replacing ................................")
    print ("\n Existing file name is "+filename)
    replace = filename.replace(oldPlugin,newPlugin)
    replacePath = os.path.join(filePath1, replace)
    print ("path ....................................")
    print ("\n New file name is "+replace)
    if check_extension(filename,filePath1,root1) is False:  
        if not os.path.exists(replacePath):
            os.chmod(root1, 0o777)
            with open(replacePath, 'wb') as list_file:
                print ("Renaming...........................")
                with open(root1, 'rb') as f:
                    for line in f:
                        line1 = line.decode("utf-8")
                        ReplacedLine = line1
                        if re.search(regexp, line1) is not None:
                            ReplacedLine = (line1.replace(re.search(oldplugin,(re.search(regexp, line1)).group(0)).group(0),newplugin))
                        if re.search(ESXRegexp, ReplacedLine) is not None:
                            ReplacedLine = (ReplacedLine.replace(re.search(oldESXVer,(re.search(ESXRegexp, ReplacedLine)).group(0)).group(0),newESXVer)) 
                        if re.search(WorkbenchRegexp, ReplacedLine) is not None:
                            ReplacedLine = (ReplacedLine.replace(re.search(oldWbVer,(re.search(WorkbenchRegexp, ReplacedLine)).group(0)).group(0),newWbVer))
                        list_file.write(ReplacedLine.encode())
            list_file.close()
            print ("\n"+replace+" file created ..............")
        else:
            print ("\n\n"+replacePath+" specified path Exist")
            sys.exit()
    else:
        print ("copying .zip Folder..............................")
        print ("old path "+root1)
        print ("New path "+filePath1)
        if not os.path.exists(replacePath):
            os.chmod(root1, 0o777)
            with open(replacePath, 'wb') as list_file:
                print ("Renaming...........................")
                with open(root1, 'rb') as f:
                    f_content = f.read()
                    list_file.write(f_content)
                    list_file.close()
            list_file.close()
            print ("\n"+replace+" file created ..............")
        else:
            print ("\n\n"+replacePath+" specified path Exist")
            sys.exit()
            print("copied ......................")
        
    
    
def main(walk_dir1):
    print('walk_dir (absolute) = ' + os.path.abspath(walk_dir1))
    for root, subdirs, files in os.walk(walk_dir1):
        print('--\nroot = ' + root)
        root1 = root.replace(oldPlugin,newPlugin)
        if not os.path.exists(root1):
            os.makedirs(root1)
        for subdir in subdirs:
            print('\n\n\t- subdirectory ' + subdir)
            subdirPath = root.replace(oldPlugin,newPlugin)
            if not os.path.exists(subdirPath):
                print ("\n"+subdirPath+" Path does not Exist please try with correct path")
                sys.exit()
            else :
                print ("\nPath of sub dir element is "+subdirPath)
                print ("Creating new sub directory .................")
                CreateDirectory(subdirPath,subdir,oldPlugin,newPlugin)

        for filename in files:
            file_path = os.path.join(root, filename)
            print('\n\n\t- file name ' + filename)
            filePath = root.replace(oldPlugin,newPlugin)
            print ("Old file path is "+file_path)
            if not os.path.exists(filePath):
                print ("\n"+filePath+" Path does not Exist please try with correct path")
                sys.exit()
            else :
                print ("\nPath of file element is "+filePath)
                print ("Creating new file .................")
                RenameFile(file_path,filePath,filename,oldPlugin,newPlugin)

        
def main1(old_plugin1,newPlugin1,oldESXver1,newESXVer1,oldWorkbenchVer1,newWorkbenchVer1,path1):
	globals()['path'] = path1
	path.replace("\\","/")
	walk_dir = path
	print(path)
	globals()['oldplugin'] = old_Plugin1[-2:]
	globals()['newplugin'] = newPlugin1[-2:]
	globals()['oldESXVer'] = oldESXver1[-3:]
	globals()['newESXVer'] = newESXver1[-3:]
	globals()['oldWbVer'] = oldWorkbenchVer1[-3:]
	globals()['newWbVer'] = newWorkbenchVer1[-3:]
	regexp= r'[a-zA-Z]+'+re.escape(oldplugin)
	ESXRegexp= r'[a-zA-Z]+\s'+re.escape(oldESXVer)
	WorkbenchRegexp= r'[a-zA-Z]+\s'+re.escape(oldWbVer)
	fileexts = ['.zip','.tar.gz']
	print('walk_dir = ' + walk_dir)
	check()
	if not os.path.exists(walk_dir):
		print ("\n"+walk_dir+"Path doesnot exist")
	else:
		for name in os.listdir(walk_dir):
			if newPlugin in name:
				print (name+" Plugin name exist")
				sys.exit()
			else:
				continue
		for name in os.listdir(walk_dir):
			if oldPlugin in name:
				print (name)
				main(os.path.join(walk_dir, name))
			else:
				continue
        
