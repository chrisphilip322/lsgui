
from tkinter import *
import re
import subprocess
from tkinter import messagebox

class GUI:
    def __init__(self,rootwin):
        self.win = rootwin

        self.addURLEntry = Entry(self.win, width=80)
        self.addURLEntry.grid(row=1, column=3,padx=5,pady=5)

        Button(self.win, text='Add Stream', command=self.addURLPressed).grid(row=1,column=1,columnspan=2,sticky=EW,padx=5,pady=5)

        Frame(self.win, height=3, bd=1, relief=SUNKEN).grid(row=2,column=1,columnspan=3,sticky=EW,padx=5,pady=5)
        
        self.readfile()

        for i in range(len(streamList)):
            StreamButtons(4+i,streamList[i],self.win)

        self.rowPos = 4+len(streamList)
            
    def readfile(self):
        global streamList
        streamList=[]
        try:
            f = open('streamlist.txt','r')
            contents = f.read()
            streamList = re.findall('.+',contents)
            f.close()
        except:
            pass#messagebox.showinfo(title='Warning',message='No stream list yet, or an error with it')
        return

    def addURLPressed(self):
        streamList.append(self.addURLEntry.get())
        StreamButtons(self.rowPos,streamList[-1],self.win)
        self.rowPos+=1
        writeFileBack()
        return

class StreamButtons:
    def __init__(self,_row,streamURL,win):
        self.stream=streamURL
        
        self.launchButton = Button(win,text='Launch',command=self.launch,width=10)
        self.launchButton.grid(row=_row,column=1,padx=5,pady=5)
        self.deleteButton = Button(win,text='Delete',command=self.delete,width=10)
        self.deleteButton.grid(row=_row,column=2,padx=5,pady=5)
        Label(win,text=self.stream).grid(row=_row,column=3,sticky=W,padx=5,pady=5)

    def launch(self):
        if LOGGING:
            subprocess.Popen([lsloc,self.stream,quality,'>>log.out','2>>&1'],shell=True)
        else:
            subprocess.Popen([lsloc,self.stream,quality],shell=True)
        return
    def delete(self):
        result = messagebox.askquestion("Delete",'Delete '+self.stream+'?')
        if result == 'yes':
            self.launchButton.config(state=DISABLED)
            self.deleteButton.config(state=DISABLED)
            del streamList[streamList.index(self.stream)]
            writeFileBack()
        return

def writeFileBack():
    f = open('streamlist.txt','w')
    for stream in streamList:
        f.write(stream+'\n')
    f.close()
    return

def readConfigFile():
    global lsloc, quality, LOGGING

    lsloc = 'C:\\Program Files(x86)\\Livestreamer\\livestreamer.exe'
    quality = 'best'
    LOGGING = False

    try:    
        f = open('lsgui.conf','r')
        config = f.read()
        config = re.findall('.+',config)
        for line in config:
            if len(re.findall('^livestreamer_location=',line)) > 0:
                lsloc=line[len('livestreamer_location='):]
                #print(lsloc)
            if len(re.findall('^quality=',line)) > 0:
                quality = line[len('quality='):]
            if len(re.findall('^logging=',line)) > 0:
                LOGGING = line[len('quality='):]=='ON'
        f.close()
    except:
        pass#messagebox.showinfo(title='Warning',message='No config file, or an error with it')
    try:
        f = open('log.out','a')
        f.write('\n----- NEW LOLOLOL INSTANCE -----\n\n')
        f.close()
    except:
        pass

<<<<<<< HEAD
=======
LOGGING = False
>>>>>>> 3cf44fa0c21e55c3d29347ca7eae27bcac13506a
if __name__ == '__main__':
    readConfigFile()
    myWin = Tk()
    myObj = GUI(myWin)
    myWin.wm_title('Livestreamer GUI')
    print('Starting program!!')

    myWin.mainloop()
