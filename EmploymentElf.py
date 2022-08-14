##Admin password is:career_elf

#Importing tkinter
from tkinter import *
from tkinter.ttk import*
from tkinter.scrolledtext import*



#****************************************************************************************************************************
#****************************************************************************************************************************


def admin():
    global window1
    window1.destroy
    adm_window = Tk()
    adm_window.title('Admin')
    adm_window.configure(bg='#FFF633')
    adm_window.geometry('300x100')

    emp_lb = Label(adm_window,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#FFF633')
    emp_lb.pack(side=TOP,padx=10,pady=10)
    
    lbl=Label(adm_window,text="Password", font=('Calibri'),background='#FFDA33')
    lbl.pack(side= LEFT)
    txt = Entry(adm_window,width=20,show='*')
    txt.pack(side= LEFT)

    

    def check_adm():
        
        if txt.get()=='career_elf':
            lbl.pack_forget()
            txt.pack_forget()
            bt.pack_forget()
            width= adm_window.winfo_screenwidth()  
            height= adm_window.winfo_screenheight() 
            adm_window.geometry("%dx%d" % (width, height))
            
            
            fdb = Label(adm_window,text='Feedbacks left by users', font=('Broadway',14,'bold','underline'), background = '#FFF633')
            fdb.pack(side=TOP, padx=50,pady=20)
            
            sc_fdb = ScrolledText(adm_window,wrap   = WORD,width  = adm_window.winfo_screenwidth(),height = adm_window.winfo_screenheight(), font = ('Calibri',10,'bold'), background="#FFF633",foreground="red")
            sc_fdb.pack(side=BOTTOM,padx=10,pady=10)
            
            import mysql.connector as ms
            con=ms.connect(host='localhost',user='root',passwd='tiger',database='career')
            cur=con.cursor()

            con=ms.connect(host='localhost',user='root',passwd='tiger',database='career')
            cur=con.cursor()
            cur.execute('select * from login where Feedback is not null')
            data=cur.fetchall()
            
            fdb_msg=''
            for row in data:
               fdb_msg += row[3] + ': '+str(row[13])+'\n'
               
            sc_fdb.insert(INSERT,fdb_msg)
                         
            
            
        else:
            from tkinter import messagebox
            messagebox.showerror("Admin Error", 'Enter correct password')

    
    bt=Button(adm_window,text="Enter",command=check_adm)
    bt.pack(side=LEFT)
    
def feedback():
    root7 = Tk()
    root7.title('Feedback')
    root7.configure(bg='#BEFF33')

    emp_lb = Label(root7,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.grid(column=1,row=1,padx=10,pady=10)
    
    ei = Label(root7, text="Email_Id", font=('Calibri',16,'bold'),background='#A2CA4A')
    ei.grid(column=1,row=2)
    txt1 = Entry(root7, width = 20)
    txt1.grid(column=3,row=2)
    
    fb = Label(root7, text="Feedback", font=('Calibri', 16, 'bold'),background='#A2CA4A')
    fb.grid(column=1,row=4)
    txt2 = Text(root7, width = 50, height=20)
    txt2.grid(column=3,row=4)
    
    
    def feed_click():
        import mysql.connector as ms
        con = ms.connect(host='localhost',user='root',passwd='tiger',database='career')
        cur=con.cursor()
        cur.execute("select * from login where Email_Id='{}'".format(txt1.get()))
        data = cur.fetchone()
        if data!=None:
            x = "update login set Feedback='{}' where Email_Id='{}'".format(txt2.get("1.0",END),txt1.get())
            cur.execute(x)
            con.commit()
            from tkinter import messagebox
            messagebox.showinfo("Feedback Success", "Thank you for dropping your feedback!")
        else:
            from tkinter import messagebox
            messagebox.showerror("Email Error", 'Enter valid email-id')
        
        root7.destroy()

    bt = Button(root7,text = 'SUBMIT', command=feed_click)   
    bt.grid(column = 2, row =5)
    
    root7.mainloop()
    
def wind2_1():
    global window2,window,root4
    window.destroy()
    root4.destroy()
    window2 = Tk()
    window2.title('Register')
    window2.configure(bg='#BEFF33')
    width= window2.winfo_screenwidth()  
    height= window2.winfo_screenheight() 
    window2.geometry("%dx%d" % (width, height))
    
    emp_lb = Label(window2,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.pack(side=TOP,padx=10,pady=10)
    
    msg = Message(window2,width = window2.winfo_screenwidth(),text = "Our website provides a wide variety of features. To access them, you'll have to first register yourself"+'\n'+"Note: Once you register, you will immediately be directed to the career quiz", font =('Calibri',16), foreground= '#C2185B',background='#BEFF33')
    msg.pack(side=TOP,padx=10,pady=10)

    img = PhotoImage(file="Elfie.png",master=window2)
    lb1 = Label(window2, image=img).pack(side = TOP,padx=10,pady=10)

    style_but=Style(window2)
    style_but.configure('TButton',font=
                     ("Harrington",16,"bold"),
                     foreground = "red", background="#33FFAC")
    
    
    
    bt1 = Button(window2, text = 'Register Now!', command=CRegister)
    bt1.pack(side=TOP, padx=10, pady=15)
    bt2 = Button(window2, text = 'Or have you already done it?', command=CLogin)
    bt2.pack(side=TOP, padx=10, pady=15)
    bt3 = Button(window2, text = 'Back to Main Page', command=wind3_2)
    bt3.pack(side=TOP, padx=10, pady=15)
    window2.mainloop()


def wind2_2():
    global window2,window
    window.destroy()
    window2 = Tk()
    window2.title('Register')
    window2.configure(bg='#BEFF33')
    width= window2.winfo_screenwidth()  
    height= window2.winfo_screenheight() 
    window2.geometry("%dx%d" % (width, height))
    
    emp_lb = Label(window2,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.pack(side=TOP,padx=10,pady=10)
    
    msg = Message(window2,width = window2.winfo_screenwidth(),text = "Our website provides a wide variety of features. To access them, you'll have to first register yourself"+'\n'+"Note: Once you register, you will immediately be directed to the career quiz", font =('Calibri',16), foreground= '#C2185B',background='#BEFF33')
    msg.pack(side=TOP,padx=10,pady=10)

    img = PhotoImage(file="Elfie.png",master=window2)
    lb1 = Label(window2, image=img).pack(side = TOP,padx=10,pady=10)

    style_but=Style(window2)
    style_but.configure('TButton',font=
                     ("Harrington",16,"bold"),
                     foreground = "red", background="#33FFAC")
    
    
   
    bt1 = Button(window2, text = 'Register Now!', command=CRegister)
    bt1.pack(side=TOP, padx=10, pady=15)
    bt2 = Button(window2, text = 'Or have you already done it?', command=CLogin)
    bt2.pack(side=TOP, padx=10, pady=15)
    bt3 = Button(window2, text = 'Back to Main Page', command=wind3_2)
    bt3.pack(side=TOP, padx=10, pady=15)
    window2.mainloop()

#Window 3--Main Page
def wind3_2():
    global window,window2
    window2.destroy()
    window = Tk()
    width= window.winfo_screenwidth()  
    height= window.winfo_screenheight() 
    window.geometry("%dx%d" % (width, height))
    window.title('EmploymentElf')
    window.configure(bg='#BEFF33')
    l1 = Label(window,text = "Hello! Welcome to EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22' , background = '#BEFF33').pack(side=TOP)
    msg2 = Message(window, text='''EmploymentElf-the one stop destination for all your career related queries.
    Now that you've taken up the Career Assessment Quiz, it's time to check out our other features.
    Click on any one of the buttons to explore!''', font=('Calibri',16,'bold'), foreground='red', background='#BEFF33').pack(side=TOP)
    style3=Style(window)
    style3.configure('TButton',font=
                     ("Harrington",16,"bold"),
                     foreground = "red", background="#33FFAC")

    
       
    bt2=Button(window,text="Career Options",command=Career_Options)
    bt2.pack(side=TOP,padx=10, pady=15)
    bt3 = Button(window,text = 'FAQs', command=FAQs)
    bt3.pack(side=TOP,padx=10, pady=15)
    bt4 = Button(window,text = 'Career Consultation', command=Consult)   
    bt4.pack(side=TOP,padx=10, pady=15)
    bt5 = Button(window,text = 'Go back to registration', command=wind2_2)   
    bt5.pack(side=TOP,padx=10, pady=15)
    bt6 = Button(window,text = 'Give us your valuable feedback', command=feedback)   
    bt6.pack(side=TOP,padx=10, pady=15)
    
    window.mainloop()



def wind3_1():
    global window
    window = Tk()
    width= window.winfo_screenwidth()  
    height= window.winfo_screenheight() 
    window.geometry("%dx%d" % (width, height))  
    window.title('EmploymentElf')
    window.configure(bg='#BEFF33')
    l1 = Label(window,text = "Hello! Welcome to EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22' , background = '#BEFF33').pack(side=TOP)
    msg2 = Message(window, text='''EmploymentElf-the one stop destination for all your career related queries.
    Now that you've taken up the Career Assessment Quiz, it's time to check out our other features.
    Click on any one of the buttons to explore!''', font=('Calibri',16,'bold'), foreground='red', background='#BEFF33').pack(side=TOP)
    style3=Style(window)
    style3.configure('TButton',font=
                     ("Harrington",16,"bold"),
                     foreground = "red", background="#33FFAC")

    bt2=Button(window,text="Career Options",command=Career_Options)
    bt2.pack(side=TOP,padx=10, pady=15)
    bt3 = Button(window,text = 'FAQs', command=FAQs)
    bt3.pack(side=TOP,padx=10, pady=15)
    bt4 = Button(window,text = 'Career Consultation', command=Consult)   
    bt4.pack(side=TOP,padx=10, pady=15)
    bt5 = Button(window,text = 'Go back to registration', command=wind2_1)   
    bt5.pack(side=TOP,padx=10, pady=15)
    bt6 = Button(window,text = 'Give us your valuable feedback', command=feedback)   
    bt6.pack(side=TOP,padx=10, pady=15)
    
    window.mainloop()

    
#Function for Registration Window
click = 0  #click is a variable which has been used to link the register/login function with the career quiz and it's result analysis
passwd, email, errormsg = '', '',''
def CRegister():
    global window2,name,click,errormsg
    click = 0
    root3 = Tk()
    root3.title("Register")
    root3.configure(bg='#A2CA4A')

    emp_lb = Label(root3,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#A2CA4A')
    emp_lb.grid(column=2,row=0, padx=10,pady=10)
    
    sg = Label(root3, text="Enter your details first", font=('Calibri',14), foreground ='#9900CC', background='#A2CA4A')
    sg.grid(column=2,row=1)
    
    
    nm = Label(root3,width=25, text="Name (only alphabets)", font=('Calibri'),background='#A2CA4A')
    nm.grid(column=1,row=2)
    txt1 = Entry(root3, width = 20)
    txt1.grid(column=3,row=2)
    
    age = Label(root3,width=25, text="Age (min 10)",font=('Calibri'),background='#A2CA4A')
    age.grid(column=1,row=3)
    txt2 = Entry(root3, width = 20)
    txt2.grid(column=3,row=3)
    
    sex = Label(root3,width=25, text="Sex (m,f,o)",font=('Calibri'),background='#A2CA4A')
    sex.grid(column=1,row=4)
    txt3 = Entry(root3, width = 20)
    txt3.grid(column=3,row=4)
    
    ei = Label(root3, width=25,text="Email_Id (eg:elf@emp.com)",font=('Calibri'),background='#A2CA4A')
    ei.grid(column=1,row=5)
    txt4 = Entry(root3, width = 20)
    txt4.grid(column=3,row=5)
    
    pwd = Label(root3,width=25, text="Password (min 8 characters)",font=('Calibri'),background='#A2CA4A')
    pwd.grid(column=1,row=6)
    txt5 = Entry(root3, width = 20, show='*')
    txt5.grid(column=3,row=6)
    
    def check():
        global errormsg
        if txt1.get().isalpha() or (' ' in txt1.get()):
            if  txt2.get().isdigit():
                if len(txt2.get())==2:
                    if txt3.get() in ['F','M','O','f','m','o']:
                        if '@' in txt4.get() and '.com' in txt4.get():
                            if len(txt5.get())>=8:
                                return True
                            else:
                                errormsg='Password should contain atleast 8 characters'
                                return False
                        else:
                            errormsg='Email Id is not valid'
                            return False
                    else:
                        errormsg="Sex should be in ['F','M','O']"
                        return False
                else:
                    if len(txt2.get())==1:
                        errormsg='You are too young'
                        return False
                    else:
                        errormsg='Enter valid age'
                        return False
            else:
                errormsg='Enter age in digits only'
                return False
        else:
            errormsg='Enter name in alphabets only'
            return False
        
    ##SQL Connection1
    import mysql.connector as sqLtor
    def clicked():
        global passwd,click,email,errormsg
        email=txt4.get()
        passwd = txt5.get()
        mycon = sqLtor.connect(host = 'localhost', user = 'root', passwd='tiger', database = 'Career')
        cursor=mycon.cursor()
        cursor.execute("select * from login where Email_Id='{}'".format(email))
        data = cursor.fetchone()
                       
        if data==None:
            st = "insert into login(Name, Age, Sex, Email_Id, Password) values('{}','{}','{}','{}','{}')".format(txt1.get(), txt2.get(), txt3.get(), email, passwd)
                
            if check():
                cursor.execute(st)
                mycon.commit()
                root3.destroy()
                from tkinter import messagebox
                messagebox.showinfo("Registered", "Registration successful!")
                window2.destroy()
                CQuiz_full()
                
                click = 1  #This is to indicate the quiz can be attempted
                
            else:
                from tkinter import messagebox
                messagebox.showerror("Register_Error", errormsg)
                root3.destroy()
                

        else:
            from tkinter import messagebox
            messagebox.showerror("Register_Error", ' This Email_Id has already been taken' )
            root3.destroy()
            
            
    bt = Button(root3,text='SUBMIT', command=clicked)
    bt.grid(column=2,row=8)
    
#****************************************************************************************************************************
#Function for Login Screen
def CLogin():    
    global window2,name,click
    root3 = Tk()
    root3.title("Login")
    root3.configure(bg='#A2CA4A')

    emp_lb = Label(root3,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#A2CA4A')
    emp_lb.grid(column=2,row=0, padx=10,pady=10)
    
    sg = Label(root3, text="Enter your credentials", font=('Calibri'), foreground ='#9900CC', background='#A2CA4A')
    sg.grid(column=2,row=1)
    
  
    ei = Label(root3, text="Email_Id",font=('Calibri'),background='#A2CA4A')
    ei.grid(column=1,row=2)
    txt1 = Entry(root3, width = 20)
    txt1.grid(column=3,row=2)

    pwd = Label(root3, text="Password", font=('Calibri'),background='#A2CA4A')
    pwd.grid(column=1,row=5)
    txt2 = Entry(root3, width = 20, show='*')
    txt2.grid(column=3,row=5)

    import mysql.connector as sqLtor
    def clicked():
        global passwd,click,email
        email = txt1.get()
        passwd=txt2.get()
        mycon = sqLtor.connect(host = 'localhost', user = 'root', passwd='tiger', database = 'Career')
        cursor=mycon.cursor()
        cursor.execute("select * from login where Email_Id='{}' and Password='{}'".format(email,passwd))
        data = cursor.fetchone()
                       
        if data!=None:
            from tkinter import messagebox
            if messagebox.askyesno("Career Quiz", "Do you want to retake the quiz?"):
                click=0 #User wishes to retake the quiz
            else:
                click=2 #User doesn't want to retake the quiz
            root3.destroy()
            window2.destroy()
            CQuiz_full()
            

        else:
            from tkinter import messagebox
            messagebox.showerror("Login_Error", "Enter valid details")
            root3.destroy()
            


    def passwd_forget():
        mycon = sqLtor.connect(host = 'localhost', user = 'root', passwd='tiger', database = 'Career')
        cursor=mycon.cursor()
        cursor.execute("delete from login where Email_Id='{}'".format(email))
        
        CRegister()
    bt1 = Button(root3,text='SUBMIT', command=clicked)
    bt1.grid(column=1,row=8,sticky = W, pady=10,)
    bt2 = Button(root3,text='Forgot password?\nCreate New Account!', command=passwd_forget)
    bt2.grid(column=3,row=8,sticky = W, pady=10,)



#****************************************************************************************************************************
#****************************************************************************************************************************

#Career Quiz

def CQuiz():
    global Cat,lim
    ques = [' ']
    with open('career quiz.txt','r') as cquiz:  #Taking questions from csv file
        for line in cquiz:
            ques.append(line.rstrip())

    Cat = {'1':['Arts, Audio/Video Technology and Communications',0], '2':['Education and Training',0], '3':['Manufacturing',0], '4':['Science,Technology,Engineering and Mathematics',0], '5':['Architecture and Construction',0], '6':['Business Management and Administration',0], '7':['Health Science',0], '8':['Law,Public Safety, Corrections and Security',0]}
    root2 = Tk()
    width= root2.winfo_screenwidth()  
    height= root2.winfo_screenheight() 
    root2.geometry("%dx%d" % (width, height))  
    root2.title("Career Quiz")
    root2.configure(bg='#BEFF33')

    style1 = Style(root2)
    style1.configure('W.TButton', font =
               ('calibri', 20, 'bold', 'underline'), 
                foreground = 'red')
    style2 = Style(root2) 
    style2.configure("TRadiobutton",background ='#BEFF33', font = ("arial", 10, "bold"))

    img = PhotoImage(file="Elfie.png",master=root2)
    lb1 = Label(root2, image=img).grid(column=2,row=10)
    
    #Creating RadioButtons
    var = IntVar()
    emp_lb = Label(root2,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.grid(column=2,row=2)
    lb = Label(root2, text = "Career Quiz", font=('Calibri',20,'bold','underline'), foreground='red', background='#BEFF33')
    lb.grid(column=2, row=3, sticky = W, pady=10)
    ins_lb = Label(root2, text ='''In order for us to estimate your personal interests and usual style,
you will first need to answer a series of questions.
Read each set of phrases below and decide which one of the four most describes you,
then select the radio button next to that phrase.''',font=('Calibri',12),background='#BEFF33')
    ins_lb.grid(column=2,row=4,padx=10,pady=10)
    rad1= Radiobutton(root2, text=ques[1], variable=var, value=1)
    rad1.grid(column=1, row=5, sticky = W, pady=2)
    rad2= Radiobutton(root2, text=ques[2], variable=var, value=2)
    rad2.grid(column=3, row=5, sticky = W, pady=2)
    rad3= Radiobutton(root2, text=ques[3], variable=var, value=3)
    rad3.grid(column=1, row=6, sticky = W, pady=2)
    rad4= Radiobutton(root2, text=ques[4], variable=var, value=4)
    rad4.grid(column=3, row=6, sticky = W, pady=2)
    lim = 5
    def select():
        op = str(var.get())
        return op
    def quit():
        rad1.grid_forget()
        rad2.grid_forget()
        rad3.grid_forget()
        rad4.grid_forget()
        bt.configure(text='DONE',command=root2.destroy) 
    def Sel_sc():
        val= select()
        global Cat,lim

        if val in ['1', '14', '22', '27', '33']:
            Cat['1'][1]+=1
        elif val in ['2', '7', '17', '25', '37']:
            Cat['2'][1]+=1
        elif val in ['6', '12', '13', '29', '40']:
            Cat['3'][1]+=1
        elif val in ['15', '20', '28', '30', '35']:
            Cat['4'][1]+=1
        elif val in ['3', '5', '9', '21', '31']:
            Cat['5'][1]+=1
        elif val in ['8', '16', '23', '36', '38']:
            Cat['6'][1]+=1
        elif val in ['4', '10', '18', '24', '32']:
            Cat['7'][1]+=1
        elif val in ['11', '19', '26', '34', '39']:
            Cat['8'][1]+=1
        if lim==41:
            quit()
        try:
            rad1.configure(text =ques[lim], value=lim)
            rad2.configure(text =ques[lim+1], value=lim+1)
            rad3.configure(text =ques[lim+2], value=lim+2)
            rad4.configure(text =ques[lim+3], value=lim+3)
            lim+=4
        except:
            root2.destroy
    
    bt = Button(root2, text = "Enter", command=Sel_sc, style = 'W.TButton')
    bt.grid(column=2, row=7, sticky = W, pady = 2)
    root2.mainloop()
        
#****************************************************************************************************************************    
def CQuiz_Result():
    global email,root4
    
    global Cat, click

        
    T = A= ind = 0
    l = []
                   
    for j in Cat:
        l.append(Cat[j][1])
        
    t = tuple(l)
    for i in t:
        T+=i
    

    while T!=10:
        root4_1 = Tk()
        root4_1.title('Result')
        root4_1.configure(bg='#BEFF33')
        lb5 = Label(root4_1, text = 'Attempt the Quiz',font=('Calibri',16,'bold'), background='#BEFF33')
        lb5.grid(column=0, row=0)
        root4_1.mainloop()
        CQuiz()
        T = A= ind = 0
        l = []
                   
        for j in Cat:
            l.append(Cat[j][1])
        
        t = tuple(l)
        for i in t:
            T+=i
        
    if T==10:  #In the quiz, the user has totally selected 10 answers
        global root4
        root4 = Tk()
        root4.title('Result')
        width= root4.winfo_screenwidth()  
        height= root4 .winfo_screenheight() 
        root4 .geometry("%dx%d" % (width, height))  
        root4 .configure(bg='#BEFF33')
        def percent(n):
            return (n/T)*100
        
        ##SQL Connection2
        import mysql.connector as ms
        con = ms.connect(host='localhost', user='root', passwd='tiger', database='Career')
        cur = con.cursor()
        
        for j in Cat:
            perc = percent(Cat[j][1])
            if j=='1':
                cur.execute("update login set Cat1={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='2':
                cur.execute("update login set Cat2={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='3':
                cur.execute("update login set Cat3={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='4':
                cur.execute("update login set Cat4={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='5':
                cur.execute("update login set Cat5={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='6':
                cur.execute("update login set Cat6={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='7':
                cur.execute("update login set Cat7={} where Email_Id='{}'".format(perc,email))
                con.commit()
            elif j=='8':
                cur.execute("update login set Cat8={} where Email_Id='{}'".format(perc,email))
                con.commit()

               
        def prop(n): 
            return 360.0 * n / T

        
        
        if T!=0:
            lab = Label(root4 , text='Your Result Analysis', font=('Harrington',16,'bold'), foreground='red', background='#BEFF33')
            lab.grid(column=2, row=0)
            emp_lb = Label(root4,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
            emp_lb.grid(column=3, row=0)
            cl_lb = Label(root4,text='''**Click each category to know
it's colour on the pie chart''', font=('Calibri',14,'bold'),foreground='red',background='#BEFF33')
            cl_lb.grid(column=4,row=1)
            c = Canvas(root4 ,width=154, height=154, background='#BEFF33')
            c.grid(column=2, row = 1)
        Colours = ("gold", "indigo", "lime", "#DC143C", "teal", "orange", "#BA55D3","brown")
        for i in t:
            c.create_arc((2,2,152,152), fill=Colours[ind], outline=Colours[ind], start=prop(A), extent = prop(i))
            
            if prop(i)!=0:
                import tkinter as tk
                cat_rad = tk.Radiobutton(root4,text=Cat[str(ind+1)][0]+'('+str(int((i/T)*100))+'%)',font=('Calibri',16,'bold'),bg='#BEFF33',selectcolor=Colours[ind],activebackground=Colours[ind])
                cat_rad.grid(column = 3, row = ind+2)
                
            A+=i
            ind+=1
            
        
        try:
            cur.execute("select * from login where Email_Id='{}'".format(email))
            data = cur.fetchone()
            name = data[0]
            msg4 = Message(root4 ,width='200', text='Name: '+data[0]+'\n'+'Age: '+str(data[1]), font =('Harrington',20,'bold'),foreground='red', background='#33FFAC')
            msg4.grid(column=3, row=1)
            
        except:
            msg4 = Message(root4 , text="No saved data")
            msg4.grid(column=3, row=1)

        style2 = Style(root4)
        style2.configure('W.TButton', font =
                   ('Harrington', 18, 'bold'), 
                    foreground = 'red', background = "#33FFAC")
        bt = Button(root4 ,text = 'Click to continue', command=wind3_1, style='W.TButton')
        bt.grid(column = 3, row =11, padx=10,pady=10)

        res_mes = Message(root4,width='800',text = "Hello " + name +'''! Thank you for taking up our career quiz.
Career quizzes and tests can help you choose, change or develop your career. You can use them as a starting point in your journey to get to know yourself better and explore the wide range of career opportunities available to you.
The pie chart provides a detailed analysis of all the career fields you might be interested in.
A higher percentage indicates better suitability. Hope you find this useful and select the best path for yourself.
All the best!''',font =('Calibri',12),background='#BEFF33')
        res_mes.grid(column = 3, row =10, padx=10,pady=10)
        
        root4.mainloop()
        click = 1 #Quiz has been attempted
            

        

#****************************************************************************************************************************
def CQuiz_full():
    global click,root4
    ind=A=0
    Cat_res = {'1':['Arts, Audio/Video Technology and Communications',0], '2':['Education and Training',0], '3':['Manufacturing',0], '4':['Science,Technology,Engineering and Mathematics',0], '5':['Architecture and Construction',0], '6':['Business Management and Administration',0], '7':['Health Science',0], '8':['Law,Public Safety, Corrections and Security',0]}
    if click==2:#This implies the user doesn't want to retake the quiz
        root4= Tk()
        width= root4.winfo_screenwidth()  
        height= root4.winfo_screenheight() 
        root4.geometry("%dx%d" % (width, height))  
        root4.title('Result')
        root4.configure(bg='#BEFF33')
        
        from tkinter import messagebox
        messagebox.showinfo("Registered", "You have already attempted the quiz!")

        ##SQL Connection3
        import mysql.connector as ms
        con = ms.connect(host='localhost', user='root', passwd='tiger', database='career')
        cur = con.cursor()
        cur.execute("select Cat1,Cat2,Cat3,Cat4,Cat5,Cat6,Cat7,Cat8 from login where Email_Id='{}'".format(email))
        data = cur.fetchone()
        def pro(n):
            return (360.0/100) * float(n)
        
        lab = Label(root4, text='Your Result Analysis', font=('Harrington',16,'bold'), foreground='red', background='#BEFF33')
        lab.grid(column=2, row=0)
        emp_lb = Label(root4,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
        emp_lb.grid(column=3,row=0, padx=10,pady=10)
        cl_lb = Label(root4,text='''**Click each category to know
it's colour on the pie chart''', font=('Calibri',14,'bold'),foreground='red',background='#BEFF33')
        cl_lb.grid(column=4,row=1)
        c = Canvas(root4,width=154, height=154, background='#BEFF33')
        c.grid(column=2, row = 1)
        Colours = ("gold", "indigo", "#279228", "#DC143C", "teal", "orange", "#BA55D3","brown")
        for i in data:
            c.create_arc((2,2,152,152), fill=Colours[ind], outline=Colours[ind], start=pro(A), extent = pro(i))
            if pro(i)!=0:
                import tkinter as tk
                cat_rad = tk.Radiobutton(root4,text=Cat_res[str(ind+1)][0]+'('+str(int(i))+'%)',font=('Calibri',16,'bold'),bg='#BEFF33',selectcolor=Colours[ind],activebackground=Colours[ind])
                cat_rad.grid(column = 3, row = ind+2)
                
            A+=i
            ind+=1

        cur.execute("select * from login where Email_Id='{}'".format(email))
        data = cur.fetchone()
        name = data[0]
        msg4 = Message(root4,width='200', text='Name: '+str(data[0])+'\n'+'Age: '+str(data[1]), font =('Harrington',20,'bold'),foreground='red', background='#33FFAC')
        msg4.grid(column=3, row=1)

        style2 = Style(root4)
        style2.configure('W.TButton', font =
                   ('Harrington', 18, 'bold'), 
                    foreground = 'red', background = "#33FFAC")
        bt = Button(root4,text = 'Click to continue', command=wind3_1,style='W.TButton')
        bt.grid(column = 3, row =11,padx=10,pady=10)

        res_mes = Message(root4,width='800',text = "Hello " + name +'''! Thank you for taking up our career quiz.
Career quizzes and tests can help you choose, change or develop your career. You can use them as a starting point in your journey to get to know yourself better and explore the wide range of career opportunities available to you.
The pie chart provides a detailed analysis of all the career fields you might be interested in.
A higher percentage indicates better suitability. Hope you find this useful and select the best path for yourself.
All the best!''',font =('Calibri',12),background='#BEFF33')
        res_mes.grid(column = 3, row =10, padx=10,pady=10)

        
        root4.mainloop()
        
        
        
    else:
        CQuiz()
        CQuiz_Result()
            



#****************************************************************************************************************************
#****************************************************************************************************************************

#Career Options
def COp_Reader(file):  #To display details based on category selected
    global inst,pc,ree
    fname = file+'.csv'
    import csv
    with open(fname, "r", newline = '\r\n') as fh:
        creader = csv.reader(fh)
        inst,pc,ree=[],[],[]
        for rec in creader:
            try:
                #Taking each category as a separate list
                inst.append(rec[0])
                pc.append(rec[1])
                ree.append(rec[2])
            except:
                break
            
def Career_Options(): #To display all possible categories
    CV = {'Arts, Audio&Video Technology and Communications':1, 'Education and Training':2, 'Manufacturing':3, 'Science,Technology,Engineering and Mathematics':4, 'Architecture and Construction':5, 'Business Management and Administration':6, 'Health Science':7, 'Law,Public Safety, Corrections and Security':8}
    CVCat=[]
    for i in CV:
        CVCat.append(i)
    root1 = Tk()
    width= root1.winfo_screenwidth()  
    height= root1.winfo_screenheight() 
    root1.geometry("%dx%d" % (width, height))  
    root1.title("Career Options")
    root1.configure(bg='#BEFF33')
    root1.geometry('1500x800')

    emp_lb = Label(root1,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.grid(column=3,row=0, padx=10,pady=10)

    msg2 = Message(root1,width  = '300', text='''EmploymentElf: Ground-breaking  career information! ''', font=('Calibri',16,'bold'), foreground='red', background='#BEFF33').grid(column=1,row=1)

    msg3 = Message(root1,width='300', text='''Our sources are 100% accurate.''', font=('Calibri',16,'bold'), foreground='red', background='#BEFF33').grid(column=3,row=1)

    msg4 = Message(root1,width='300', text='''Select a category from the menu to view the various options:Institutions,Career possibilies
and Related entrance exams.''', font=('Calibri',16,'bold'), foreground='red', background='#BEFF33').grid(column=5,row=1)

    combo = Combobox(root1, values = CVCat, width=50)  #Displaying categories as a combobox widget
    combo.grid(column = 3, row =2,pady=5)
    def select():
        op = combo.get()    #Getting the value stored in the combobox
        COp_Reader(op)  #Invoking previous function
        global inst,pc,ree
        sc1 = ScrolledText(root1,wrap   = WORD,width  = 50,height = 10, font = ('Calibri',14,'bold'), background="#A2CA4A",foreground="#A10000")
        sc1.grid(column = 1, row = 5,padx=10)
        inst_str = ''
        for i in inst:
            if i==' ':
                inst.remove(i)#Removing Extra Characters
            else:
                inst_str+='*'+i+'\n' #Converting list into multiline string
        sc1.insert(INSERT,"SOME POPULAR INDIAN INSTITUTIONS\n", INSERT,inst_str)

        sc2 = ScrolledText(root1,wrap   = WORD,width  = 50,height = 10, font = ('Calibri',14,'bold'), background="#A2CA4A",foreground="#A10000")
        sc2.grid(column = 3, row = 5)
        pc_str = ''
        for i in pc:
            if i=='':
                pc.remove(i)
            else:
                pc_str+='*'+i+'\n'
        sc2.insert(INSERT,"SOME POSSIBLE CAREERS\n", INSERT,pc_str)

        sc3 = ScrolledText(root1,wrap   = WORD,width  = 20,height = 10, font = ('Calibri',14,'bold'), background="#A2CA4A",foreground="#A10000")
        sc3.grid(column = 5, row = 5)
        ree_str = ''
        for i in ree:
            if i=='':
                ree.remove(i)
            else:
                ree_str+='*'+i+'\n'
        sc3.insert(INSERT,"RELATED ENTRANCE EXAMS\n", INSERT,ree_str)
    bt = Button(root1,text = 'Enter', command=select)   #Button which performs the operation
    bt.grid(column = 3, row =4,pady=5)
    
    root1.mainloop()

        
#****************************************************************************************************************************
#****************************************************************************************************************************
#FAQs
def FAQs():
    file = open(r'faqs.txt', 'r')
    win = Tk()
    width= win.winfo_screenwidth()  
    height= win.winfo_screenheight() 
    win.geometry("%dx%d" % (width, height))  
    win.title('Frequently Asked Questions')
    win.configure(bg='#BEFF33')

    emp_lb = Label(win,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.pack(side=TOP, padx=10,pady=10)

    '''img = PhotoImage(file="Elfie.png",master=win)
    lb1 = Label(win, image=img).pack(side = RIGHT)'''
    
    sc1 = ScrolledText(win,width= win.winfo_screenwidth(),wrap   = WORD,height= win.winfo_screenheight() , font = ('Calibri',20,'bold'),background="#A2CA4A",foreground="#A10000")
    sc1.pack(side=TOP,padx=10,pady=10)
    faq_str =''
    for i in file:
            faq_str+=i #Converting list into multiline string
    sc1.insert(INSERT,"SOME FREQUENTLY ASKED QUESTIONS\n", INSERT,faq_str)
    win.mainloop()#Exitinng tkinter window


#****************************************************************************************************************************
#****************************************************************************************************************************
#Career Consultation Window
def Consult():
    file = open(r'consult.txt', 'r')
    win1 = Tk()
    width= win1.winfo_screenwidth()  
    height= win1.winfo_screenheight() 
    win1.geometry("%dx%d" % (width, height))  
    win1.title('Our Career Experts')
    win1.configure(bg='#BEFF33')

    emp_lb = Label(win1,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
    emp_lb.pack(side=TOP, padx=10,pady=10)
    
    sc1 = ScrolledText(win1,width= win1.winfo_screenwidth(),wrap   = WORD,height= win1.winfo_screenheight() , font = ('Calibri',20,'bold'), background="#A2CA4A",foreground="#A10000")
    sc1.pack(side=TOP,padx=10,pady=10)

    img = PhotoImage(file="Elfie.png",master=win1)
    lb1 = Label(win1, image=img).pack(side = TOP,padx=10,pady=10)
    
    faq_str =''
    for i in file:
            faq_str+=i #Converting list into multiline string
    sc1.insert(INSERT,"CONTACT OUR CAREER EXPERTS\n", INSERT,faq_str)
    win1.mainloop()
    file.close()


#****************************************************************************************************************************
#****************************************************************************************************************************
#****************************************************************************************************************************
#****************************************************************************************************************************


def wind2_from1():
    global window2,window1
    window1.destroy()
    window2 = Tk()
    window2.title('Register')
    window2.configure(bg='#BEFF33')
    width= window2.winfo_screenwidth()  
    height= window2.winfo_screenheight() 
    window2.geometry("%dx%d" % (width, height))

    emp_lb = Label(window2 , text='EmploymentElf', font = ('Harrington', 26,'bold'),foreground = '#E67E22',background='#BEFF33')
    emp_lb.pack(side=TOP,padx=10,pady=10)
    
    style2 = Style(window2)
    style2.configure('TButton', font =
                   ('Harrington', 18, 'bold'), 
                    foreground = 'red', background = "#33FFAC")

    msg = Message(window2,width= window2.winfo_screenwidth(),text ="Our website provides a wide variety of features. To access them, you'll have to first register yourself"+'\n'+"Note: Once you register, you will immediately be directed to the career quiz" , font =('Calibri',16), foreground= '#C2185B',background='#BEFF33')
    msg.pack(side=TOP,padx=10,pady=10)

    img = PhotoImage(file="Elfie.png",master=window2)
    lb1 = Label(window2, image=img).pack(side = TOP,padx=10,pady=10)
    
    bt1 = Button(window2, text = 'Register Now!', command=CRegister)
    bt1.pack(side=TOP, padx=10, pady=15)

    bt2 = Button(window2, text = 'Or have you already done it?', command=CLogin)
    bt2.pack(side=TOP, padx=10, pady=15)
    
    window2.mainloop()
    
#Creating various windows
            
#Window 1--Starting page
window1 = Tk()
width= window1.winfo_screenwidth()  
height= window1.winfo_screenheight() 
window1.geometry("%dx%d" % (width, height))  
window1.title('EmploymentElf')
window1.configure(bg='#BEFF33')

emp_lb = Label(window1,text = "EmploymentElf", font = ('Harrington', 26,'bold'), foreground = '#E67E22',background='#BEFF33')
emp_lb.pack(side=TOP, padx=10,pady=10)

img1 = PhotoImage(file = 'Elf_logo.png')
style = Style(window1)
style.configure('W.TButton', font =
               ('Harrington', 18, 'bold'), 
                foreground = 'red', background = "#33FFAC")
# Setting icon of master window 
window1.iconphoto(True, img1)
img = PhotoImage(file="Career_Elf.png")
lb1 = Label(window1, image=img).pack(side = TOP)
msg = Message(window1,width='1000',text = ''' 'Career' - what does it mean to you? Choosing a career path can be overwhelming but fear not because we've got your back.
Here at EmploymentElf you will find a variety of options to explore and we can assure you that you will finally have the confidence to achieve your dreams.
EmploymentElf enables you to take up a career quiz to assess your interests and capabilties. We also provide a list of career choices in each field and list out the top institutions and exams corresponding to the same. Seek guidance to plan the next steps and achieve your career goals!

So, what are you waiting for? Go ahead and click to continue.''', font =('Calibri',12,'bold'),background='#BEFF33').pack(side=TOP,pady=10)
bt1 = Button(window1, text='Click to Continue', command=wind2_from1,style = 'W.TButton').pack(side=TOP,pady=5)
bt2 = Button(window1,text='Are you the admin?', command=admin , style = 'W.TButton').pack(side=TOP,pady=5)
window1.mainloop()






    

#****************************************************************************************************************************
    

        
