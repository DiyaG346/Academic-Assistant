from tkinter import *
import tkinter.ttk as ttk
import math
import time
from ttkthemes import themed_tk as tk  #Extra module, needs to be downloaded externally
from tkinter import ttk
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import *
import wikipedia


path=os.getcwd()   #Change the file path according to your system
path_photo=f'{path}\\photos'
os.chdir(f'{path}')


root=tk.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title('Academic Assitant')
photo_icon=PhotoImage(file=f'{path_photo}\\logo.png')
root.iconphoto(False,photo_icon)
root.geometry('720x470')
root.minsize(720,470)
root.maxsize(720,470)

frame_front=Frame(root)
frame_front.grid(sticky='news')
photo=PhotoImage(file=f'{path_photo}\\front page.png')
label=Label(frame_front,image=photo)
label.grid(row=0,column=0,rowspan=10,columnspan=20)

bar=ttk.Progressbar(frame_front,orient=HORIZONTAL,length=720)
bar.grid(row=9,column=0)
for i in range(5):
    time.sleep(1)
    bar['value']+=20
    bar.update()

bar.destroy()

frame_front.destroy()

a=2

colour='gray90'

#============================================================================================================================

#=========================================Notepad====================================================

def Notes():
    global root,window_frame

    window_frame.destroy()
    
    class Notepad:
        global root

        frame_note=Frame(root,height=470,width=720)
        frame_note.grid(row=0,column=0,sticky='news')
        
        thisWidth = 720
        thisHeight = 470
        thisTextArea = Text(frame_note,height=470,width=720)
        thisMenuBar = Menu(frame_note)
        thisFileMenu = Menu(thisMenuBar, tearoff=0)
        thisEditMenu = Menu(thisMenuBar, tearoff=0)

        thisScrollBar = Scrollbar(frame_note)
        file = None

        def __init__(self,**kwargs):

            self.root=root

            try:
                self.root.wm_iconbitmap("Notepad.ico")
            except:
                pass

            try:
                self.thisWidth = kwargs['width']
            except KeyError:
                pass

            try:
                self.thisHeight = kwargs['height']
            except KeyError:
                pass

            self.root.title("Academic Assistant- Untitled - Notepad")

            screenWidth = self.root.winfo_screenwidth()
            screenHeight = self.root.winfo_screenheight()

            left = (screenWidth / 2) - (self.thisWidth / 2)
            top = (screenHeight / 2) - (self.thisHeight /2)

            self.root.geometry('%dx%d+%d+%d' % (self.thisWidth,self.thisHeight,left, top))

            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(0, weight=1)

            self.thisTextArea.grid(sticky = N + E + S + W)

            self.thisFileMenu.add_command(label="New",command=self.newFile)

            self.thisFileMenu.add_command(label="Open",command=self.openFile)

            self.thisFileMenu.add_command(label="Save",command=self.saveFile)

            self.thisFileMenu.add_separator()

            self.thisFileMenu.add_command(label="Exit",command=self.quitApplication)

            self.thisMenuBar.add_cascade(label="File",menu=self.thisFileMenu)

            self.thisEditMenu.add_command(label="Cut",command=self.cut)

            self.thisEditMenu.add_command(label="Copy",command=self.copy)

            self.thisEditMenu.add_command(label="Paste",command=self.paste)

            self.thisMenuBar.add_cascade(label="Edit",menu=self.thisEditMenu)

            self.root.config(menu=self.thisMenuBar)

            self.thisScrollBar.grid(sticky='nes')

            self.thisScrollBar.config(orient='vertical',command=self.thisTextArea.yview)
            self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

        def quitApplication(self):
            self.frame_note.destroy()
            MainScreen()

        def openFile(self):

            self.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.file == "":
                self.file = None

            else:
                self.root.title(os.path.basename(self.file) + " - Notepad")
                self.thisTextArea.delete(1.0,END)
                file = open(self.file,"r")
                self.thisTextArea.insert(1.0,file.read())
                file.close()
                return

        def newFile(self):
            self.root.title("Academic Assistant- Untitled - Notepad")
            self.file = None
            self.thisTextArea.delete(1.0,END)
            return

        def saveFile(self):
            if self.file == None:
                self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt", 
					      filetypes=[("All Files","*.*"), 
					      ("Text Documents","*.txt")])
                if self.file == "":
                    self.file = None
                else:
                    file = open(self.file,"w")
                    file.write(self.thisTextArea.get(1.0,END))
                    file.close()
                    self.root.title(os.path.basename(self.file) + " - Notepad")

            else:
                file = open(self.file,"w")
                file.write(self.thisTextArea.get(1.0,END))
                file.close()
            return

        def cut(self):
            self.thisTextArea.event_generate("<<Cut>>")

        def copy(self):
            self.thisTextArea.event_generate("<<Copy>>")

        def paste(self):
            self.thisTextArea.event_generate("<<Paste>>")

        def run(self):
            self.root.mainloop()

    Notepad().run() 



#============================================================================================================================

#=========================================Calculator====================================================

def Back_Calc():
    calc.destroy()
    MainScreen()
    
def Calculator():
    global calc,window_frame

    window_frame.destroy()
    
    root.title('Academic Assistant-Calculator')
    root.configure(background='powder blue')
    root.geometry('720x470')
    calc=Frame(root)
    calc.grid(row=0,column=0,rowspan=7,columnspan=8,sticky='n')

    menubar=Menu(calc)
    menubar.add_command(label='Back',command=Back_Calc)

    root.configure(menu=menubar)
    
    class Calc():
        def __init__(self):
            self.total=0
            self.current=''
            self.input_value=True
            self.check_sum=False
            self.op=''
            self.result=False
            
        def numberEnter(self,num):
            self.result=False
            firstnum=txtDisplay.get()
            secondnum=str(num)
            if self.input_value:
                self.current=secondnum
                self.input_value=False
            else:
                if secondnum=='.':
                    if secondnum in firstnum:
                        return
                self.current=firstnum+secondnum
            self.display(self.current)
            
        def sum_of_total(self):
            self.result=True
            self.current=float(self.current)
            if self.check_sum==True:
                self.valid_function()
            else:
                self.total=float(txtDisplay.get())
                
        def display(self,value):
            txtDisplay.delete(0,END)
            txtDisplay.insert(0,value)
            
        def valid_function(self):
            if self.op=='add':
                self.total+=self.current
            if self.op=='sub':
                self.total-=self.current
            if self.op=='multi':
                self.total*=self.current
            if self.op=='divide':
                self.total/=self.current
            if self.op=='mod':
                self.total%=self.current
            self.input_value=True
            self.check_sum=False
            self.display(self.total)
            
        def operation(self,op):
            self.current=float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total=self.current
                self.input_value=True
            self.check_sum=True
            self.op=op
            self.result=False
            
        def pi(self):
            self.result=False
            self.current=math.pi
            self.display(self.current)

        def tau(self):
            self.result=False
            self.current=math.tau
            self.display(self.current)
            
        def e(self):
            self.result=False
            self.current=math.e
            self.display(self.current)
            
        def Clear_Entry(self):
            self.result=False
            self.current='0'
            self.display(0)
            self.input_value=True
            
        def all_Clear_Entry(self):
            self.Clear_Entry()
            self.total=0
            
        def mathPM(self):
            self.result=False
            self.current=-(float(txtDisplay.get()))
            self.display(self.current)
            
        def Sqrt(self):
            self.result=False
            self.current=math.sqrt(float(txtDisplay.get()))
            self.display(self.current)
            
        def sin(self):
            self.result=False
            self.current=math.sin(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def sinh(self):
            self.result=False
            self.current=math.sinh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def cos(self):
            self.result=False
            self.current=math.cos(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def cosh(self):
            self.result=False
            self.current=math.cosh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def tan(self):
            self.result=False
            self.current=math.tan(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def tanh(self):
            self.result=False
            self.current=math.tanh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def acosh(self):
            self.result=False
            self.current=math.acosh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def asinh(self):
            self.result=False
            self.current=math.asinh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
            
        def expm1(self):
            self.result=False
            self.current=math.expm1(float(txtDisplay.get()))
            self.display(self.current)
            
        def lgamma(self):
            self.result=False
            self.current=math.lgamma(float(txtDisplay.get()))
            self.display(self.current)
            
        def degrees(self):
            self.result=False
            self.current=math.degrees(float(txtDisplay.get()))
            self.display(self.current)
            
        def log(self):
            self.result=False
            self.current=math.log(float(txtDisplay.get()))
            self.display(self.current)
            
        def log2(self):
            self.result=False
            self.current=math.log2(float(txtDisplay.get()))
            self.display(self.current)
            
        def log10(self):
            self.result=False
            self.current=math.log10(float(txtDisplay.get()))
            self.display(self.current)
            
        def log1p(self):
            self.result=False
            self.current=math.log1p(float(txtDisplay.get()))
            self.display(self.current)
            
    added_value=Calc()

    txtDisplay=Entry(calc,font=('arial',20,'bold'),bg='powder blue',bd=30,width=44,justify=RIGHT)
    txtDisplay.grid(row=1,column=0,columnspan=9,pady=1)
    txtDisplay.insert(0,'0')

    numpad='789456123'
    i=0
    btn=[]
    for j in range(3,6):
        for k in range(3):
            btn.append(Button(calc,width=6,height=2,font=('arial',15,'bold'),bd=4,text=numpad[i]))  
            btn[i]['command']=lambda x=numpad[i]:added_value.numberEnter(x)
            btn[i].grid(row=j,column=k)
            i+=1
    btnclear=Button(calc,text=chr(67),width=7,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.Clear_Entry).grid(row=2,column=0)
    btnclear2=Button(calc,text=chr(67)+chr(69),width=7,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.all_Clear_Entry).grid(row=2,column=1)
    
    btnSq=Button(calc,text='√',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.Sqrt)
    btnSq.grid(row=2,column=2)
    btnAdd=Button(calc,text='+',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.operation('add'))
    btnAdd.grid(row=2,column=3)
    btnSub=Button(calc,text='-',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.operation('sub'))
    btnSub.grid(row=3,column=3)
    btnMult=Button(calc,text='*',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.operation('multi'))
    btnMult.grid(row=4,column=3)
    btnDiv=Button(calc,text=chr(247),width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.operation('divide'))
    btnDiv.grid(row=5,column=3)
    
    btnZero=Button(calc,text='0',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.numberEnter(0))
    btnZero.grid(row=6,column=0) 
    btnDot=Button(calc,text='.',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=lambda:added_value.numberEnter('.'))
    btnDot.grid(row=6,column=1)
    btnPM=Button(calc,text=chr(177),width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.mathPM)
    btnPM.grid(row=6,column=2)
    btnEquals=Button(calc,text='=',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.sum_of_total)
    btnEquals.grid(row=6,column=3)

    btnpi=Button(calc,text='π',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.tau)
    btnpi.grid(row=2,column=5)
    btncos=Button(calc,text='cos',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.cos)
    btncos.grid(row=2,column=6)
    btntan=Button(calc,text='tan',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.tan)
    btntan.grid(row=2,column=7)
    btnsin=Button(calc,text='sin',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.sin)
    btnsin.grid(row=2,column=8)
    
    btn2pi=Button(calc,text='2π',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.pi)
    btn2pi.grid(row=3,column=5)
    btncosh=Button(calc,text='cosh',width=6,height=2,font=('arial',15,'bold'),command=added_value.cosh)
    btncosh.grid(row=3,column=6)
    btntanh=Button(calc,text='tanh',width=6,height=2,font=('arial',15,'bold'),command=added_value.cosh)
    btntanh.grid(row=3,column=7)
    btnsinh=Button(calc,text='sinh',width=6,height=2,font=('arial',15,'bold'),command=added_value.cosh)
    btnsinh.grid(row=3,column=8)
    
    btnlog=Button(calc,text=chr(177),width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.log)
    btnlog.grid(row=4,column=5)
    btnexp=Button(calc,text='Exp',width=6,height=2,font=('arial',15,'bold'))
    btnexp.grid(row=4,column=6) ###################
    btnmod=Button(calc,text='Mod',width=6,height=2,font=('arial',15,'bold'),command=lambda:added_value.operation('mod'))
    btnmod.grid(row=4,column=7)
    btne=Button(calc,text='e',width=6,height=2,font=('arial',15,'bold'),command=added_value.e)
    btne.grid(row=4,column=8)
    
    btnlog2=Button(calc,text='log2',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.log2)
    btnlog2.grid(row=5,column=5)
    btndeg=Button(calc,text='Deg',width=6,height=2,font=('arial',15,'bold'),command=added_value.degrees)
    btndeg.grid(row=5,column=6)
    btnacosh=Button(calc,text='acosh',width=6,height=2,font=('arial',15,'bold'),command=added_value.acosh)
    btnacosh.grid(row=5,column=7)
    btnasinh=Button(calc,text='asinh',width=6,height=2,font=('arial',15,'bold'),command=added_value.asinh)
    btnasinh.grid(row=5,column=8)
    
    btnlog10=Button(calc,text='log10',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.log10)
    btnlog10.grid(row=6,column=5)
    btnlog1p=Button(calc,text='log1p',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.log1p)
    btnlog1p.grid(row=6,column=6)
    btnexpm1=Button(calc,text='expm1',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.expm1)
    btnexpm1.grid(row=6,column=7)
    btnlgamma=Button(calc,text='lgamma',width=6,height=2,font=('arial',15,'bold'),bg='powder blue',command=added_value.lgamma)
    btnlgamma.grid(row=6,column=8)


#============================================================================================================================

#====================================Wikipedia=========================================================


def Wiki():

    window_frame.destroy()
    
    class SearchApp:
        global search,root
        
        def __init__(self,root):
            self.root=root
            self.root.title('Academic Assistant-Wikipedia')
            root.geometry('720x470')
            root.configure(background=colour)
            self.search=Frame(self.root,bg=colour)
            self.search.grid(row=0,column=0,rowspan=7,columnspan=8,sticky='n')

            photo=PhotoImage(file=f'{path_photo}\\Wikipedia.png')
            label=Label(self.search,image=photo)
            label.image=photo
            label.grid(row=0,column=0,columnspan=200)

            label1=Label(self.search,bg=colour,fg='#262626',text='Enter word',font=('times new roman',15,'bold'))
            label1.grid(row=1,column=1,columnspan=10)
        
            self.var_search=StringVar()
            txt_word=Entry(self.search,font=('times new roman',15),textvariable=self.var_search)
            txt_word.grid(row=1,column=13,columnspan=5)

            label=Label(self.search,text='',width=1,bg=colour).grid(row=1,column=22)
        
            btn_search=Button(self.search,text='Search',font=('times new roman',12,'bold'),width=8,bg='lightyellow',fg='#262626',command=self.searchword)
            btn_search.grid(row=1,column=23,columnspan=9)
            label=Label(self.search,text=' ',width=1,bg=colour).grid(row=1,column=36)
            btn_clear=Button(self.search,text='Clear',font=('times new roman',12,'bold'),width=9,bg='lightyellow',fg='#262626',command=self.clear)
            btn_clear.grid(row=1,column=38,columnspan=9)
            label=Label(self.search,text=' ',width=1,bg=colour).grid(row=1,column=52)
            btn_enable=Button(self.search,text='Enable',font=('times new roman',12,'bold'),width=9,bg='lightyellow',fg='#262626',command=self.enable)
            btn_enable.grid(row=1,column=53,columnspan=9)
            label=Label(self.search,text=' ',width=1,bg=colour).grid(row=1,column=67)
            btn_disable=Button(self.search,text='Disable',font=('times new roman',12,'bold'),width=9,bg='lightyellow',fg='#262626',command=self.disable)
            btn_disable.grid(row=1,column=68,columnspan=9)

            frame1=Frame(self.search,bd=2,height=400,width=700,relief=RIDGE)
            frame1.grid(row=4,column=0,rowspan=50,columnspan=200)

            self.label_mode=Label(self.search,text='MODE:',font=('times new roman',15),bg=colour,fg='goldenrod3')
            self.label_mode.grid(row=3,column=2,columnspan=10)

            self.label_mode2=Label(self.search,text='',font=('times new roman',15),bg=colour,fg='goldenrod3')
            self.label_mode2.grid(row=3,column=10,columnspan=5)
        
            scroll=Scrollbar(self.search,orient='vertical')
            scroll.grid(row=4,column=75,rowspan=50,sticky='ns')

            self.txt_area=Text(frame1,font=('times new roman',10),width=110,height=19,yscrollcommand=scroll.set)
            self.txt_area.grid(row=4,column=0,columnspan=200,sticky='news')
            scroll.config(command=self.txt_area.yview)

            menubar=Menu(self.search)
            menubar.add_command(label='Back',command=self.Back_Wiki)
            self.root.configure(menu=menubar)

        def enable(self):
            self.txt_area.config(state=NORMAL)
            self.label_mode2.config(text='Enabled')
            
        def disable(self):
            self.txt_area.config(state=DISABLED)
            self.label_mode2.config(text='Disabled')
            
        def searchword(self):
            if self.var_search.get()=='':
                tmsg.showerror('Error','Search area should not be blank')
            else:
                try:
                    fetch_data=wikipedia.summary(self.var_search.get())
                    self.txt_area.insert('1.0',fetch_data)
                except:
                    tmsg.showerror('Error','No internet connecion. Try again later...')
                    
        def clear(self):
            self.label_mode2.config(text='')
            self.txt_area.config(state=NORMAL)
            self.var_search.set('')
            self.txt_area.delete('1.0',END)
            
        def Back_Wiki(self):   
            self.search.destroy()
            MainScreen()

            
    obj=SearchApp(root)

#============================================================================================================================

#============================================Time Table====================================================

def Back_TT():
    window_frame.destroy()
    MainScreen()

def TimeTable():
    global root,window_frame,frame1,frame2,label,buttons,frame3,name

    root.title('Academic Assistant-Time Table')

    os.chdir(f'{path}\\{name}')

    window_frame.destroy()

    #constants
    c=0

    window_frame=Frame(root)
    window_frame.grid(row=0,column=0,rowspan=13,columnspan=15,sticky='n')

    for i in range(8):
        l=Label(window_frame,text=' ',height=2).grid(row=i,column=0)
    for j in range(10):
        l=Label(window_frame,text=' ',height=1,width=3).grid(row=0,column=j)
        
    frame1=ttk.Frame(window_frame)
    frame1.grid(row=0,column=0,rowspan=5,columnspan=15)

    frame3=ttk.Frame(window_frame,padding='7 0 7 13')
    frame3.grid(row=6,rowspan=11,column=0,columnspan=13,sticky='ew')

    frame2=ttk.Frame(window_frame)
    frame2.grid(row=15,column=0,sticky='ew')
    
    row_list=[]
    list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    #heading=ttk.Label(frame1,text='TIMETABLE   ',font='Times 20 italic').grid(row=1,column=0,columnspan=10)
    photo=PhotoImage(file=f'{path_photo}\\Timetable.png')
    label=Label(frame1,image=photo)
    label.photo=photo
    label.grid(row=0,column=0,columnspan=6)

    for i in list:
        button=ttk.Button(frame1,text=i,width=8,command=lambda i=i:Time(i))
        button.grid(row=1,column=c)
        c+=1

    label2=ttk.Label(frame1,text=' ',width=1,).grid(row=1,column=c)
    label3=ttk.Label(frame1,text=' ',anchor='center',width=100).grid(row=3,column=0,columnspan=10)
    label4=ttk.Label(frame1,text='Select any day\n',foreground='grey',anchor='center',width=100).grid(row=4,column=0,columnspan=10)
    label5=ttk.Label(frame1,text=' ',anchor='center',width=100).grid(row=5,column=0,columnspan=10)
    label6=ttk.Label(frame1,text=' ',anchor='center',width=100).grid(row=6,column=0,columnspan=10)

    button=ttk.Button(frame1,text='Add +',width=7,command=Edit).grid(row=5,column=0,columnspan=10)

    menu1=Menu(window_frame)
    menu1.add_command(label='Back',command=Back_TT)
    
    root.config(menu=menu1)

def Edit():
    global e1,e2,e3,e4,window3,window1
    
    window3=Toplevel()
    window3.title('Add Entry')
    window3.geometry('420x300')

    l=Label(window3,text=' ',height=4).grid(row=0,column=0)
    
    for i in range(1,8):
        l=Label(window3,text=' ',height=2).grid(row=i,column=0)
    for j in range(10):
        l=Label(window3,text=' ',height=1,width=3).grid(row=0,column=j)

    photo=PhotoImage(file=f'{path_photo}\\Add_Entry.png')
    label=Label(window3,image=photo)
    label.grid(row=0,column=0,columnspan=8,sticky='n')
    
    l1=ttk.Label(window3,text='Day       : ',font='15').grid(row=1,column=3)
    l2=ttk.Label(window3,text='Time      : ',font='15').grid(row=2,column=3)
    l3=ttk.Label(window3,text='Subject  : ',font='15').grid(row=3,column=3)
    l4=ttk.Label(window3,text='Chapter  : ',font='15').grid(row=4,column=3)
    
    e1=StringVar(window3)   #day
    e2=StringVar(window3)   #Time
    e3=StringVar(window3)   #Subject
    e4=StringVar(window3)   #Chapter Name
    e1.set('Select Day')
    e2.set('Select Time')

    
    drop1=ttk.OptionMenu(window3,e1,'Monday   ','Tuesday  ','Wednesday','Thursday ','Friday   ','Saturday ').grid(row=1,column=4)
    drop2=ttk.OptionMenu(window3,e2,'09-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22').grid(row=2,column=4)
    entry1=ttk.Entry(window3,textvariable=e3).grid(row=3,column=4)
    entry2=ttk.Entry(window3,textvariable=e4).grid(row=4,column=4)

    submit=ttk.Button(window3,text='SUBMIT',width=20,command=Submit).grid(row=5,column=2,columnspan=4)
    
    window3.mainloop()
    

def Submit():
    global name
    
    tmsg.showinfo('Submitted','Your info has been updated. Press OK to continue.')
    window3.destroy()

    os.chdir(f'{path}\\{name}\\{e1.get()}')
    
    file=open(f'{e2.get()}','w')
    file.write('Day:'+e1.get()+'\n')
    file.write('Time:'+e2.get()+'\n')
    file.write('Subject:'+e3.get()+'\n')
    file.write('Chapter Name:'+e4.get()+'\n'+'\n')


def Time(day):
    
    frame_container=ttk.Frame(window_frame)
    frame_container.grid(row=5,column=0,columnspan=12)

    canvas=Canvas(frame_container,height=50,width=690)

    frame2=ttk.Frame(canvas)

    scrollbar=ttk.Scrollbar(frame_container,orient='horizontal',command=canvas.xview)
    canvas.create_window((0,0),window=frame2,anchor='nw')
   
    c=0
    l=['09-10','10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18','18-19','19-20','20-21','21-22']
    
    for j in l:
        button=ttk.Button(frame2,text=j,command=lambda j=j:View(day,j))
        button.grid(row=8,column=c)
        c+=1

    frame2.update()
    canvas.configure(xscrollcommand=scrollbar.set,scrollregion="0 0 %s 0" %frame2.winfo_width())

    canvas.grid(column=0)
    scrollbar.grid(sticky='we')

    frame_container.grid()

def View(day,time):
    global frame3,a,name
    
    os.chdir(f'{path}\\{name}\\{day}')

    if a<=8:
        try:
            file=open(f'{time}','r')

            label=ttk.Label(frame3,text=f'\n{file.read()}').grid(row=8,column=a)
            label2=ttk.Label(frame3,text=' ').grid(row=8,column=a+1)
            clear=ttk.Button(frame3,text='Quit',width=4,command=Quit).grid(row=13,column=13,sticky='se')

            a+=2

            file.close()
        
        except:
            tmsg.showinfo('Error','No Entry has been filled for this time. Press OK to continue.')
    else:
        tmsg.showinfo('Error',"The Screen is full! Press the 'Quit' button and continue")

def Quit():
    global frame3,a,root
    
    frame3.destroy()
    a=2

    frame3=ttk.Frame(window_frame,padding='10 0 14 13')
    frame3.grid(row=6,rowspan=14,column=0,columnspan=13,sticky='ew')


#============================================================================================================================

#============================================Exit====================================================

def Exit():

    frame_1.destroy()

    frame_exit=Frame(root)
    frame_exit.grid(sticky='news')

    for i in range(1,5):
        photo=PhotoImage(file=f'{path_photo}\\Exit\\'+str(i)+'.png')
        label=Label(frame_exit,image=photo)
        label.photo=photo
        label.grid(row=0,column=0)
        label.update()
        time.sleep(1)
        continue
    
    for i in range(3,0,-1):
        photo=PhotoImage(file=f'{path_photo}\\Exit\\'+str(i)+'.png')
        label=Label(root,image=photo)
        label.photo=photo
        label.grid(row=0,column=0)
        label.update()
        time.sleep(1)
        continue

    root.destroy()
    root.mainloop()


#============================================================================================================================

#============================================Help====================================================

def Back_Help():
    global root,frame_help

    frame_help.destroy()
    MainScreen()
    
def Help():
    global window_frame,root,frame_help

    root.title('Academic Assistant-Help')
    window_frame.destroy()
    frame_help=Frame(root)
    frame_help.grid(sticky='news')

    for i in range(10):
        l=Label(frame_help,text=' ',height=2).grid(row=i,column=0)
    for j in range(15):
        l=Label(frame_help,text=' ',height=1,width=3).grid(row=0,column=j)

    def page1():
        photo_label=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\1.png')
        label_1=Label(frame_help,image=photo_label)
        label_1.photo=photo_label
        label_1.grid(row=0,column=0,rowspan=11,columnspan=15)
        photo_button2=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Next.png')
        button_next=Button(frame_help,borderwidth=0,image=photo_button2,command=page2)
        button_next.photo=photo_button2
        button_next.grid(row=5,column=14,columnspan=15)

    def page2():
        photo_label=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\2.png')
        label_1=Label(frame_help,image=photo_label)
        label_1.photo=photo_label
        label_1.grid(row=0,column=0,rowspan=11,columnspan=15)
        photo_button1=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Back.png')
        button_back=Button(frame_help,borderwidth=0,image=photo_button1,command=page1)
        button_back.photo=photo_button1
        button_back.grid(row=5,column=0,sticky='w')
        photo_button2=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Next.png')
        button_next=Button(frame_help,borderwidth=0,image=photo_button2,command=page3)
        button_next.photo=photo_button2
        button_next.grid(row=5,column=14,columnspan=15)

    def page3():
        photo_label=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\3.png')
        label_1=Label(frame_help,image=photo_label)
        label_1.photo=photo_label
        label_1.grid(row=0,column=0,rowspan=11,columnspan=15)
        photo_button1=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Back.png')
        button_back=Button(frame_help,borderwidth=0,image=photo_button1,command=page2)
        button_back.photo=photo_button1
        button_back.grid(row=5,column=0,sticky='w')
        photo_button2=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Next.png')
        button_next=Button(frame_help,borderwidth=0,image=photo_button2,command=page4)
        button_next.photo=photo_button2
        button_next.grid(row=5,column=14,columnspan=15)

    def page4():
        photo_label=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\4.png')
        label_1=Label(frame_help,image=photo_label)
        label_1.photo=photo_label
        label_1.grid(row=0,column=0,rowspan=11,columnspan=15)
        photo_button1=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Back.png')
        button_back=Button(frame_help,borderwidth=0,image=photo_button1,command=page3)
        button_back.photo=photo_button1
        button_back.grid(row=5,column=0,sticky='w')
        photo_button2=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Next.png')
        button_next=Button(frame_help,borderwidth=0,image=photo_button2,command=page5)
        button_next.photo=photo_button2
        button_next.grid(row=5,column=14,columnspan=15)

    def page5():
        photo_label=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\5.png')
        label_1=Label(frame_help,image=photo_label)
        label_1.photo=photo_label
        label_1.grid(row=0,column=0,rowspan=11,columnspan=15)
        photo_button1=PhotoImage(file='F:\\Time Table\\New Folder\\photos\\help\\Back.png')
        button_back=Button(frame_help,borderwidth=0,image=photo_button1,command=page4)
        button_back.photo=photo_button1
        button_back.grid(row=5,column=0,sticky='w')

        
    page1()
    

    menubar=Menu(frame_help)
    menubar.add_command(label='Back',command=Back_Help)
    root.configure(menu=menubar)
    

#============================================================================================================================

#============================================Main Screen====================================================

def Back():
    window_frame.destroy()

def MainScreen():
    global root,window_frame,frame2,label,buttons,frame3,frame_1,name

    root.title('Academic Assistant-Main Menu')

    window_frame=Frame(root)
    window_frame.grid(row=0,column=0,rowspan=13,columnspan=15)

    for i in range(8):
        l=Label(window_frame,text=' ',height=2).grid(row=i,column=0)
    for j in range(10):
        l=Label(window_frame,text=' ',height=1,width=3).grid(row=0,column=j)
       
    frame1=ttk.Frame(window_frame)
    frame1.grid(row=0,column=0,rowspan=5,columnspan=16)

    frame3=ttk.Frame(window_frame,padding='7 0 7 13')
    frame3.grid(row=6,rowspan=11,column=0,columnspan=13,sticky='ew')

    frame2=ttk.Frame(window_frame)
    frame2.grid(row=15,column=0,sticky='ew')
   
    list=['Time Table','Notes','Calculator','Wikipedia','Quit','Help']

    photo=PhotoImage(file=f'{path_photo}\\Main_screen.png')
    label=Label(frame1,image=photo)
    label.photo=photo
    label.grid(row=0,column=0,rowspan=3,columnspan=7,pady=5,sticky='n')

    label2=ttk.Label(frame1,text='Welcome, '+name).grid(row=7,column=3)

    button_TT=ttk.Button(frame1,text='Time Table',width=18,command=TimeTable)
    button_TT.grid(row=8,column=3,pady=10)

    button_N=ttk.Button(frame1,text='Notes',width=18,command=Notes)
    button_N.grid(row=9,column=3)

    button_C=ttk.Button(frame1,text='Calculator',width=18,command=Calculator)
    button_C.grid(row=10,column=3,pady=10)

    button_W=ttk.Button(frame1,text='Wikipedia',width=18,command=Wiki)
    button_W.grid(row=11,column=3,pady=3)

    button_H=ttk.Button(frame1,text='Help',width=18,command=Help)
    button_H.grid(row=12,column=3,pady=5)

    button_Q=ttk.Button(frame1,text='Logout',width=18,command=Logout)
    button_Q.grid(row=13,column=3,pady=5)

    label=Label(frame1).grid(row=14)
    
def Logout():
    global window_frame

    window_frame.destroy()
    a=2
    Execution()

#========================================Account Page====================================================

def Login():
    global frame_1,frame_2,frame_3,frame_4,name

    root.title('Academic Assistant-Login')

    def CheckButton():
        if CheckValue.get()==1:
            entry_2.config(show='')
        elif CheckValue.get()==0:
            entry_2.config(show='*')

    def Login_Button():
        global name
        
        try:
            os.chdir(f'{path}\\{e1.get()}')

            file=open('Password','r')
            
            if file.read()==e2.get():  
                tmsg.showinfo('Continue','Correct Password. Press OK to continue')
                name=e1.get()
                frame_1.destroy()
                MainScreen()
            
            else:      
                tmsg.showinfo('Error','Wrong Username or Password. Enter again!!')
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                
        except:     
            if e1.get()=='':
                tmsg.showinfo('Error','Username field cannot be blank. Enter again.')
            else:
                tmsg.showinfo('Invalid username',f'Username {e1.get()} does not exist. Try again.')
            entry_1.delete(0,END)
            entry_2.delete(0,END)
        return

    frame_3=Frame(frame_2,bg='royal blue')
    frame_3.grid(row=0,column=0,rowspan=10,columnspan=17,sticky='news')

    for i in range(10):
        l=Label(frame_3,text=' ',height=2,bg='royal blue').grid(row=i,column=0)
    for j in range(22):
        l=Label(frame_3,text=' ',bg='royal blue').grid(row=0,column=j)

    heading=Label(frame_3,text='Login',fg='yellow',bg='royal blue',font='calibri 30 bold underline')
    heading.grid(row=1,column=0,columnspan=33)

    l1=Label(frame_3,text='Username',fg='white',bg='royal blue',font='Times 15 bold').grid(row=3,column=4)
    l2=Label(frame_3,text='Password',fg='white',bg='royal blue',font='Times 15 bold').grid(row=4,column=4)

    e1=StringVar(frame_3)
    e2=StringVar(frame_3)    

    entry_1=ttk.Entry(frame_3,textvariable=e1,width=40)
    entry_1.grid(row=3,column=7,columnspan=20)
    entry_2=ttk.Entry(frame_3,show='*',textvariable=e2,width=40)
    entry_2.grid(row=4,column=7,columnspan=20)

    frame_x=Frame(frame_3,bg='royal blue')
    frame_x.grid(row=5,column=4,columnspan=5)

    CheckValue=IntVar()

    checkbox=Checkbutton(frame_x,bg='royal blue',variable=CheckValue,onvalue=1,offvalue=0,command=CheckButton)
    checkbox.grid(row=5,column=4,sticky='w')

    label_x=Label(frame_x,text='Show Password',bg='royal blue',fg='white',font='Times 12 bold')
    label_x.grid(row=5,column=5,columnspan=6,sticky='w')

    b1=Button(frame_3,text='Log In',bg='Seagreen1',width=10,relief='groove',command=Login_Button).grid(row=5,column=22,columnspan=5)
    
def SignUp():
    global frame_1,frame_2,frame_3,frame_4

    root.title('Academic Assistant-Sign Up')

    def CheckButton():
        if CheckValue.get()==1:
            entry_2.config(show='')
        elif CheckValue.get()==0:
            entry_2.config(show='*')

    def Submit_Button():
        if e1.get()=='':
            tmsg.showinfo('Error','Username field cannot be blank. Enter again.')
        else:
            os.mkdir(f'{e1.get()}')     #A new folder with name as the 'Username' will be created
            os.chdir(f'{e1.get()}')     #Program will refer to the created foler as the new location
            file=open('Password','w')   #A new text file with name 'Password' will be created
            file.write(f'{e2.get()}')   #and store the entered Password
            file.close()
            file=open('Email-Contact','w')   
            file.write(f'{e3.get()}'+'\n'+f'{e4.get()}')   
            file.close()
            file=open('Forgot Question','w')   
            file.write(f'{e5.get()}'+'\n'+f'{e6.get()}')   
            file.close()
        
            #Creating 6 Folders in the new created folder
            list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
            for i in list:
                os.mkdir(f'{i}')
            tmsg.showinfo('Continue','Account Created. Press OK to continue')
        return

    frame_3=Frame(frame_2,bg='brown1')
    frame_3.grid(row=0,column=0,rowspan=10,columnspan=17,sticky='news')

    for i in range(10):
        l=Label(frame_3,text=' ',height=2,bg='brown1').grid(row=i,column=0)
    for j in range(22):
        l=Label(frame_3,text=' ',bg='brown1').grid(row=0,column=j)

    heading=Label(frame_3,text='Sign Up',fg='white',bg='brown1',font='calibri 30 bold underline')
    heading.grid(row=1,column=0,columnspan=33)

    l1=Label(frame_3,text='Username',fg='white',bg='brown1',font='Times 15 bold').grid(row=3,column=4)
    l2=Label(frame_3,text='Password',fg='white',bg='brown1',font='Times 15 bold').grid(row=4,column=4)
    l3=Label(frame_3,text='Email   ',fg='white',bg='brown1',font='Times 15 bold').grid(row=5,column=4)
    l4=Label(frame_3,text='Contact ',fg='white',bg='brown1',font='Times 15 bold').grid(row=6,column=4)

    e1=StringVar(frame_3)
    e2=StringVar(frame_3)
    e3=StringVar(frame_3)
    e4=StringVar(frame_3)
    e5=StringVar(frame_3)
    e6=StringVar(frame_3)
    e5.set('Forget Ques')

    drop1=ttk.OptionMenu(frame_3,e5,'Forget Ques','  Nickname ','SchoolName ',' Home Town ','    DOB    ','occupation ').grid(row=7,column=4)
    
    entry_1=ttk.Entry(frame_3,textvariable=e1,width=40)
    entry_1.grid(row=3,column=7,columnspan=20)
    entry_2=ttk.Entry(frame_3,show='*',textvariable=e2,width=40)
    entry_2.grid(row=4,column=7,columnspan=20)
    entry_3=ttk.Entry(frame_3,textvariable=e3,width=40)
    entry_3.grid(row=5,column=7,columnspan=20)
    entry_4=ttk.Entry(frame_3,textvariable=e4,width=40)
    entry_4.grid(row=6,column=7,columnspan=20)
    entry_5=ttk.Entry(frame_3,textvariable=e6,width=40)
    entry_5.grid(row=7,column=7,columnspan=20)

    frame_x=Frame(frame_3,bg='brown1')
    frame_x.grid(row=8,column=4,columnspan=5)

    CheckValue=IntVar()

    checkbox=Checkbutton(frame_x,bg='brown1',variable=CheckValue,onvalue=1,offvalue=0,command=CheckButton)
    checkbox.grid(row=5,column=4,sticky='w')

    label_x=Label(frame_x,text='Show Password',bg='brown1',fg='white',font='Times 12 bold')
    label_x.grid(row=5,column=5,columnspan=6,sticky='w')
    
    b1=Button(frame_3,text='Sign Up',bg='Seagreen1',width=10,relief='groove',command=Submit_Button)
    b1.grid(row=8,column=22,columnspan=5)

def Forgot():
    global screen,frame_1,frame_2,frame_3,frame_4

    root.title('Academic Assistant-Forgot password')

    def Forgot_Button():
        global name
        try:
            if e1.get()=='':
                tmsg.showinfo('Error','Username field cannot be blank. Enter again.')
            else:
                os.chdir(f'{path}\\{e1.get()}')

                file=open('Forgot Question','r')
                ques=file.read(11)
                file.read(1)
                ans=file.read()
            
                if ques==e2.get() and ans==e3.get():  
                    tmsg.showinfo('Continue','Correct Information. Press OK to continue')
                    name=e1.get()
                    frame_1.destroy()
                    MainScreen()
            
                else:      
                    tmsg.showinfo('Error','Wrong Answer. Enter again!!')
                    entry_1.delete(0,END)
                    e2.set('Select Ques')
                    entry_3.delete(0,END)
         
        except:     
            tmsg.showinfo('Invalid username',f'Username {e1.get()} does not exist. Try again.')
            entry_1.delete(0,END)
            e2.set('Select Ques')
            entry_3.delete(0,END)
        return
    
    frame_3=Frame(frame_2,bg='gray40')
    frame_3.grid(row=0,column=0,rowspan=10,columnspan=17,sticky='news')

    for i in range(10):
        l=Label(frame_3,text=' ',height=2,bg='gray40').grid(row=i,column=0)
    for j in range(22):
        l=Label(frame_3,text=' ',bg='gray40').grid(row=0,column=j)

    heading=Label(frame_3,text='Forget',fg='white',bg='gray40',font='calibri 30 bold underline')
    heading.grid(row=1,column=0,columnspan=33)
    
    l1=Label(frame_3,text='Username',fg='white',bg='gray40',font='Times 15 bold').grid(row=3,column=4)
    l2=Label(frame_3,text='Select Ques',fg='white',bg='gray40',font='Times 15 bold').grid(row=4,column=4)
    l3=Label(frame_3,text='Your Ans',fg='white',bg='gray40',font='Times 15 bold').grid(row=5,column=4)

    e1=StringVar(frame_3)
    e2=StringVar(frame_3)
    e2.set('Select Ques')
    e3=StringVar(frame_3)

    entry_1=ttk.Entry(frame_3,textvariable=e1,width=40)
    entry_1.grid(row=3,column=7,columnspan=20)
    drop1=ttk.OptionMenu(frame_3,e2,'Select Ques','  Nickname ','SchoolName',' Home Town ','    DOB    ','occupation')
    drop1.grid(row=4,column=7,columnspan=20)
    entry_3=ttk.Entry(frame_3,textvariable=e3,width=40)
    entry_3.grid(row=5,column=7,columnspan=20)

    labels1=Label(frame_3,text='         ',bg='gray40').grid(row=3,column=29)

    b1=Button(frame_3,text='Submit',bg='Seagreen1',width=10,relief='groove',command=Forgot_Button).grid(row=6,column=22,columnspan=5)

#============================================================================================================================

#========================================Program Execution=================================================
    
def Execution():
    global frame_1,frame_2,frame_3,frame_front
    
    frame_front.destroy

    frame_1=Frame(root)
    frame_1.grid(row=0,column=0,rowspan=7,columnspan=20,sticky='w')

    for i in range(12):
        l=Label(frame_1,text=' ',height=2).grid(row=i,column=0)
    for j in range(22):
        l=Label(frame_1,text=' ',height=1,width=3).grid(row=0,column=j)
    photo=PhotoImage(file=f'{path_photo}\\front page.png')
    label=Label(frame_1,image=photo)
    label.photo=photo
    label.grid(row=0,column=0,rowspan=3,columnspan=3,sticky='nw')

    frame_2=Frame(frame_1)
    frame_2.grid(row=1,column=1)

    for i in range(10):
        l=Label(frame_2,text='',height=2).grid(row=i,column=0)
    for j in range(26):
        l=Label(frame_2,text='',height=1,width=2).grid(row=0,column=j)
    frame_3=Frame(frame_2,bg='salmon1',width=10)
    frame_3.grid(row=0,column=0,rowspan=10,columnspan=17)

    frame_4=Frame(frame_2,bg='white')
    frame_4.grid(row=0,column=17,rowspan=10,columnspan=10,sticky='news')

    for i in range(10):
        l=Label(frame_4,text=' ',height=2,bg='white').grid(row=i,column=0)
    for j in range(5):
        l=Label(frame_4,text=' ',bg='white').grid(row=0,column=j)

    SignUp()
    Forgot()
    Login()

    photo2=PhotoImage(file=f'{path_photo}\\logo.png')
    label2=Label(frame_4,image=photo2,borderwidth=0)
    label2.photo=photo2
    label2.grid(row=0,column=2,rowspan=4)

    button1=ttk.Button(frame_4,text='Login',width=17,command=Login)
    button1.grid(row=4,column=2)
    button2=ttk.Button(frame_4,text='Sign Up',width=17,command=SignUp)
    button2.grid(row=5,column=2)
    button3=ttk.Button(frame_4,text='Forgot Password',width=17,command=Forgot)
    button3.grid(row=6,column=2)
    button4=ttk.Button(frame_4,text='Quit',width=17,command=Exit)
    button4.grid(row=7,column=2)
    

Execution()
root.mainloop()
