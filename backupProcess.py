import sys
import os
from os import startfile
reload(sys)
sys.setdefaultencoding('utf-8')
from win32com.client import GetObject
import wmi
import getpass,subprocess,time



currentUserName=getpass.getuser()

exeNames=[]

activeNamesPath="d:/activeNames.txt"
fengxPath="d:/fengx.fengx"

def onInit():
	global exeNames
	namesFile=open(activeNamesPath,"rb")
	line=namesFile.readline()

	while line:
		if	line!="":
			exen=line.replace("\r","").replace("\n","").split("|")[0]
			if exen!="":
				exeNames.append(exen)
		line=namesFile.readline()

def onStop():
	global exeNames
	plnames=[]
	plcommandlines=[]
	nameList=[]

	nameCmd=[]
	#
	# WMI = GetObject('winmgmts:')
	# processes = WMI.InstancesOf('Win32_Process')
	# print "xx",processes,processes[1].name
	#print exeNames
	processes=wmi.WMI().Win32_Process()
	# print l.name, l.path,l.GetOwner()[2]
	for s in processes:
		plnames.append(s.name)
		# plcommandlines.append(s.commandline)
		# print s.executablepath
		# plcommandlines.append(s.executablepath)
		plcommandlines.append(s.executablepath)
		#print s.GetOwner()[2],currentUserName
		if s.GetOwner()[2]==currentUserName:
			#print s.name
			if s.name in exeNames and s.name not in nameList:
				if s.executablepath != None:
					nameList.append(s.name)
					nameCmd.append(s.name+u"|"+str(s.executablepath))
					print s.name

	setFile=open(fengxPath,"w")
	for l in nameCmd:
		setFile.write(l+"\n")
	setFile.close()

def onStart():
	# plnames=[]
	# plcommandlines=[]
	# nameList=""
	# WMI = GetObject('winmgmts:')
	# processes = WMI.InstancesOf('Win32_Process')
	# for s in processes:
	# 	nameList+=s.Name+"|"+str(s.commandline)+"\n"
	# 	plnames.append(s.Name)
	# 	plcommandlines.append(s.commandline)

	setFile=setFile=open(fengxPath,"rb")
	line=setFile.readline()

	cmds=""
	while line:
		if line!="":
			#print nc.replace("\n","")
			linePart=line.replace("\n","").replace("\r","").split("|")
			startOn=True
			# for s in plnames:
			# 	if s==linePart[0]:
			# 		startOn=False
			# if linePart[0]=="python.exe":
			# 	startOn=False
			if startOn:
				#cmds='\"'+linePart[1]+'\"'
				#print linePart[0],cmds
				subprocess.Popen([linePart[1]])
				#os.startfile(cmds)
				#a=os.popen(cmds)
				#print a.read()

		line=setFile.readline()
	setFile.close()

testPs=["cloudmusic.exe","chrome.exe","Python.exe","DingTalk.exe"]
# testPs=["Pythonw.exe"]
def test():
	plnames=[]
	plcommandlines=[]
	nameList=""
	WMI = GetObject('winmgmts:')
	processes = WMI.InstancesOf('Win32_Process')
	print dir(processes[40])
	b=processes[40]
	print b.Name
	print b.commandline
	print b.executablepath

	for s in processes:
		nameList+=s.Name+"|"+str(s.commandline)+"\n"
		plnames.append(s.Name)
		plcommandlines.append(s.executablepath)
		#
		# if s.Name in testPs:
		# 	print s.Name,"|",s.commandline
			# print s.,"|"

	# print  plnames
	print  plcommandlines
	# print  nameList


# test()
# onInit()
# onStop()
#
# import wmi
# ll=wmi.WMI().Win32_Process()
# # print dir(ll[1])
#
# l=ll[89]
# print l.name, l.path,l.GetOwner()[2]


# for i in ll:
#     # print('%s, %s, %s' % (i.Name, i.ProcessId, i.GetOwner()[2]))
#     print('%s, %s, %s' % (i.Name, i.ProcessId, i.GetOwner()))
#
# #import psutil
# import psutil
# print dir(psutil)
# for process in psutil.get_process_list():
#     try:
#         print('Process: %s, PID: %s, Owner: %s' % (process.name, process.pid,
#                                                    process.username))
#     except psutil.AccessDenied:
#         print('Access denied!')

# print dir(os)
# import win32com.client
# wmi=win32com.client.GetObject('winmgmts:')
# for p in wmi.InstancesOf('win32_process'):
#     print p.Name, p.Properties_('ProcessId'), \
#         int(p.Properties_('UserModeTime').Value)+int(p.Properties_('KernelModeTime').Value)
#     children=wmi.ExecQuery('Select * from win32_process where ParentProcessId=%s' %p.Properties_('ProcessId'))
#     for child in children:
#         print '\t',child.Name,child.Properties_('ProcessId'), \
#             int(child.Properties_('UserModeTime').Value)+int(child.Properties_('KernelModeTime').Value)
#onInit()

try:
    sys.argv[1]
except:
    raw_input("press  Enter to Exit!")
else:

    if sys.argv[1][:3]=="-st":
        onInit()
        onStart()
        #os.popen("shutdown /a")

    elif sys.argv[1][:3]=="-sd":
        onInit()
        onStop()
        #os.system("cmd")
        print  "shutdown /a"
        #os.popen("shutdown /t 40 /s ")
	l=open("d:/log.txt",'w')

	l.write("test:\n")
	l.write(str(time.localtime().tm_min))
	l.close()