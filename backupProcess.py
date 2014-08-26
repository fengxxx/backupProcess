import sys
import os
from os import startfile
reload(sys)
sys.setdefaultencoding('utf-8')
from win32com.client import GetObject

exeNames=[]


def onInit():
	global exeNames
	namesFile=open("activeNames.txt","rb")
	line=namesFile.readline()	

	while line:
		exeNames.append(line.replace("\r","").replace("\n",""))
		line=namesFile.readline()	

def onStop():
	global exeNames
	plnames=[]
	plcommandlines=[]
	nameList=""
	WMI = GetObject('winmgmts:')
	processes = WMI.InstancesOf('Win32_Process')
	for s in processes:
		plnames.append(s.Name)
		plcommandlines.append(s.commandline)
		for n in exeNames:
			if n==s.name:
				nameList+=s.Name+"|"+str(s.commandline)+"\n"
				print s.name

	setFile=open("fengx.fengx","w")
	setFile.write(nameList)
	setFile.close()

def onStart():
	plnames=[]
	plcommandlines=[]
	nameList=""
	WMI = GetObject('winmgmts:')
	processes = WMI.InstancesOf('Win32_Process')
	for s in processes:
		nameList+=s.Name+"|"+str(s.commandline)+"\n"
		plnames.append(s.Name)
		plcommandlines.append(s.commandline)

	setFile=setFile=open("fengx.fengx","rb")
	line=setFile.readline()

	cmds=""
	while line:
		if line!="":
			#print nc.replace("\n","")
			linePart=line.replace("\n","").replace("\r","").split("|")
			startOn=True
			for s in plnames:
				if s==linePart[0]:
					startOn=False
			if linePart[0]=="python.exe":
				startOn=False
			if startOn:
				cmds=("start"+ ' "" ' +linePart[1])+"&exit()"
				print linePart[0],cmds
				a=os.popen(cmds)
				
		line=setFile.readline()
	setFile.close()
onInit()

try:
    sys.argv[1]
except:
    raw_input("press  Enter to Exit!")
else:
    if sys.argv[1][:3]=="-su":
        onStart()
        os.popen("shutdown /a")

    elif sys.argv[1][:3]=="-st":
        onStop()
        #os.system("cmd")
        print  "shutdown /a"
        os.popen("shutdown /t 40 /s ")