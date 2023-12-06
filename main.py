from tkinter import *
from tkinter import StringVar , Label , ttk , scrolledtext , filedialog,simpledialog , messagebox
from frame import *
import csv

# TO verify New Student entries
def verifier():
    b=c=d=e=f=i=j=0
    txt.delete(1.0,END)

    if not bb.get():
        txt.insert(INSERT,"!!RECORDS NOT ADDED!!\nCheck First Name \n")
        b=1
    if not cc.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd.get() or dd.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee.get() or ee.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff.get() or ff.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    
    if not ii.get()  or ii.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj.get() !=34 :
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if  b==1 or c==1 or d==1 or e==1 or f==1 or i==1 or j==1 :
        return 1
    else:
        return 0

# TO verify Update Student entries
def verifier1():
    b=c=d=e=f=i=j=k=0
    txt.delete(1.0,END)
    if not roll_roll1.get():
        txt.insert(INSERT,"!!RECORDS NOT UPDATED!!\nType Roll Number \n")
        k=1
    if not bb1.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc1.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd1.get() or dd1.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee1.get() or ee1.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff1.get() or ff1.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    
    if not ii1.get() or ii1.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj1.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if b==1 or c==1 or d==1 or e==1 or f==1 or i==1 or j==1 :
        return 1
    else:
        return 0

def add_student() :
    if verifier() == 0 :
        student = {"first_name" : bb.get() , "last_name" : cc.get() , "class" : dd.get() ,  "section" : ee.get() , "gender" : ff.get() , "mobile" : ii.get(),"address" : jj.get()}

        return_data = student_create(student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            roll=str(key)
            txt.insert(INSERT,"\nSTUDENT ADDED SUCCESSFULLY\n")
            txt.insert(INSERT,"Your Details -->>""\n\nRoll No. : "+roll+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")
 
        bb.delete(0,END)
        cc.delete(0,END)
        dd.delete(0,END)
        ee.delete(0,END)
        ff.delete(0,END)
        ii.delete(0,END)
        jj.delete(0,END)
      

def view_student() :
    return_data = student_list()
    txt.delete(1.0,END)
    txt.insert(INSERT,"\n ROLL NO.\t\tSTUDENT NAME\t\t\t\tCLASS\t\tSECTION\t\tGENDER\t\tMOBILE\t\tADDRESS\n")
    for key, value in return_data.items() :
        if return_data[key] == "THIS RECORD IS DELETED FROM THE SYSTEM!" :
            continue
        else :
            roll=str(key)
            txt.insert(INSERT,"\n"+roll+"\t\t"+return_data[key]["first_name"]+"  "+return_data[key]["last_name"]+"\t\t\t\t"+return_data[key]["class"]+"\t\t"+return_data[key]["section"]+"\t\t"+return_data[key]["gender"]+"\t\t"+return_data[key]["mobile"]+"\t\t"+return_data[key]["address"],"  \n")

def update_student() :
    if verifier1() == 0 :
        rollNo = roll_roll1.get()
        student = {"first_name" : bb1.get() , "last_name" : cc1.get() , "class" : dd1.get() ,  "section" : ee1.get() , "gender" : ff1.get(),"mobile" : ii1.get(),"address" : jj1.get()}
        return_data = student_update(rollNo,student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            if key == rollNo :
                rollNo=str(key)
                txt.insert(INSERT,"\nRECORDS UPDATED SUCCESSFULLY\n")
                txt.insert(INSERT,"Updated Details -->>"+"\n\nRoll No. : "+rollNo+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")

        bb1.delete(0,END)
        cc1.delete(0,END)
        dd1.delete(0,END)
        ee1.delete(0,END)
        ff1.delete(0,END)
        ii1.delete(0,END)
        jj1.delete(0,END)
        
def delete_student() :
    messagebox.showwarning("Warning","Are you sure ?")
    data = student_delete(entry_delete.get())
    txt.delete(1.0,END)
    txt.insert(INSERT,data)

def search_by_class() :
    pass

def clse() :
    sys.exit()


def saveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.csv')
    if f!= None:
        data = txt.get('1.0',END)
    try:
        f.write(data)
        txt.delete(1.0,END)
        txt.insert(INSERT,"RECORD SAVED SUCCESSFULLY!")
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")

def classwise() :
    return_data = student_list()
    txt.delete(1.0,END)
    txt.insert(INSERT,"\n ROLL NO.\t\tSTUDENT NAME\t\t\t\tCLASS\t\tSECTION\t\tGENDER\t\tMOBILE\t\tADDRESS\n")
    if combo_class.get() in ("FORM 1","FORM 2","FORM 3","FORM 4") :
        for key, value in return_data.items() :
            if return_data[key] == "!!YOU DELETED THIS RECORD FROM THE SYSTEM!!" :
                continue
            else :
                roll=str(key)
                if combo_class.get() == return_data[key]["class"]:
                    txt.insert(INSERT,"\n"+roll+"\t\t"+return_data[key]["first_name"]+"  "+return_data[key]["last_name"]+"\t\t\t\t"+return_data[key]["class"]+"\t\t"+return_data[key]["section"]+"\t\t"+return_data[key]["gender"]+"\t\t"+return_data[key]["mobile"]+"\t\t"+return_data[key]["address"],"  \n")
                    
if __name__=="__main__":
    root=Tk()
    w=1100
    h=750
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/1) - (w/1)    
    y = (hs/1) - (h/1)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Developed by Emmanuel Frederick")
    
    # ----------------------
    
    
    fn = StringVar()
    ln = StringVar()
    cl = StringVar()
    sect = StringVar()
    gen = StringVar()
    mob = IntVar()
    ad = IntVar()
    
    heading=Label(root,text="NEW STUDENT",font=("Arial",12),foreground ="red")
    label_b=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f=Label(root,text="Gender :",font=("Arial",10),width=10)
    label_i=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j=Label(root,text="Address :",font=("Arial",10),width=10)
    
   
  
    
    bb=Entry(root,textvariable=fn,width=30)    # first name
    
    cc=Entry(root,textvariable=ln,width=30)    # last name
    
    dd = ttk.Combobox(root,width=28)    # class name
    dd['values']= ("SELECT","FORM 1","FORM 2","FORM 3","FORM 4")
    dd.current(0) #set the selected item
    
    ee = ttk.Combobox(root,width=28)    # section name
    ee['values']= ("A","B","C","G","V","W")
    ee.current(0) #set the selected item
    
    ff = ttk.Combobox(root,width=28)    # gender
    ff['values']= ("SELECT","Male","Female")
    ff.current(0) #set the selected item
    
    ii=Entry(root,textvariable=mob,width=30)    # mobile
    
    jj=Entry(root,textvariable=ad,width=30)    # address
   
     # ----------------------

    heading1=Label(root,text="UPDATE STUDENT",font=("Arial",12),foreground ="red")
    label_roll=Label(root,text="Roll Number :",font=("Arial",10),width=10)
    label_b1=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c1=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d1=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e1=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f1=Label(root,text="Gender :",font=("Arial",10),width=10)
    label_i1=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j1=Label(root,text="Address :",font=("Arial",10),width=10)

    roll1 = IntVar()
    fn1 = StringVar()
    ln1 = StringVar()
    cl1 = StringVar()
    sect1 = StringVar()
    gen1 = StringVar()
    mob1 = IntVar()
    ad1 = IntVar()

    roll_roll1=Entry(root,textvariable=roll1,width=10)    # Roll Number

    
    
    bb1=Entry(root,textvariable=fn,width=30)    # first name
    
    cc1=Entry(root,textvariable=ln,width=30)    # last name
    
    dd1 = ttk.Combobox(root,width=28)    # class name
    dd1['values']= ("SELECT","FORM 1","FORM 2","FORM 3","FORM 4")
    dd1.current(0) #set the selected item
    
    ee1 = ttk.Combobox(root,width=28)    # section name
    ee1['values']=  ("A","B","C","G","V","W")
    ee1.current(0) #set the selected item
    
    ff1 = ttk.Combobox(root,width=28)    # gender
    ff1['values']= ("SELECT","Male","Female")
    ff1.current(0) #set the selected item
    

    
    ii1=Entry(root,textvariable=mob,width=30)   # mobile
    
    jj1=Entry(root,textvariable=ad,width=30)    # address

    # ----------------------
    roll_delete = IntVar()
    heading2=Label(root,text="DELETE STUDENT",font=("Arial",12),foreground ="red")
    label_del=Label(root,text="Record",font=("Arial",12),width=10)
    label_delete=Label(root,text="Roll Number :",font=("Arial",12),width=10)
    entry_delete=Entry(root,textvariable=roll_delete,font=("Arial",12),width=10)
    
    def addnew():
        
        heading.grid(row=8 , column=1,columnspan=2)
        
        
        label_b.grid(row=9 , column=1)
        label_c.grid(row=10 , column=1)
        label_d.grid(row=11 , column=1)
        label_e.grid(row=12 , column=1)
        label_f.grid(row=13 , column=1)
        label_i.grid(row=14 , column=1)
        label_j.grid(row=15 , column=1)
  
         
        bb.grid(row=9 , column=2)
        cc.grid(row=10 , column=2)
        dd.grid(row=11 , column=2)
        ee.grid(row=12 , column=2)
        ff.grid(row=13 , column=2)
        ii.grid(row=14 , column=2)
        jj.grid(row=15 , column=2)

        b1=Button(root,text="ADD",command=lambda: add_student(),width=10,background = 'blue',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
        b1.grid(row=21 , column=1, columnspan=2,ipadx = 10,padx = 10)
    def update() :
        
        heading1.grid(row=8 , column=3,columnspan=2)
        
        label_roll.grid(row=9 , column=3)
        
        label_b1.grid(row=10 , column=3)
        label_c1.grid(row=11 , column=3)
        label_d1.grid(row=12 , column=3)
        label_e1.grid(row=13 , column=3)
        label_f1.grid(row=14 , column=3)
        label_i1.grid(row=15 , column=3)
        label_j1.grid(row=16 , column=3)
  
        roll_roll1.grid(row=9 , column=4)
         
        bb1.grid(row=10 , column=4)
        cc1.grid(row=11 , column=4)
        dd1.grid(row=12 , column=4)
        ee1.grid(row=13 , column=4)
        ff1.grid(row=14 , column=4)
        ii1.grid(row=15 , column=4)
        jj1.grid(row=16 , column=4)

        b2=Button(root,text="OK",command=lambda: update_student(),width=10,background = 'GREEN',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
        b2.grid(row=21 , column=3, columnspan=2,ipadx = 10,padx = 10)
    # ----------------------
    
    def delete() :

        heading2.grid(row=8 , column=5,columnspan=1)
        
     #   label_del.grid(row=9 , column=5 )
        label_delete.grid(row=14 , column=5 )
        entry_delete.grid(row=15 , column=5)

        b3=Button(root,text="DELETE",command=lambda: delete_student(),width=10,background = 'red',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
        b3.grid(row=21 , column=5, columnspan=1,ipadx = 10,padx = 10)


    dashboard=Label(root,text="RIQUE HIGH SCHOOL",font=("lucida",25,'bold'),foreground="BLACK")
    dashboard.grid(row=0,column=3)

    view=Button(root,text="VIEW ALL",command=lambda: view_student(),width=10,background = 'white',bd=7,relief = GROOVE, foreground ="black",font=("lucida",12,"bold"))
    view.grid(row=30, column=1, columnspan=1,ipadx = 10,padx = 10)

    add=Button(root,text="NEW",command=addnew,width=10,background = 'blue',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
    add.grid(row=30, column=2, columnspan=1,ipadx = 10,padx = 10)

    update=Button(root,text="UPDATE",command=update,width=10,background = 'orange',bd=7,relief = GROOVE, foreground ="black",font=("lucida",12,"bold"))
    update.grid(row=30, column=3, columnspan=1,ipadx = 10,padx = 10)

    delete=Button(root,text="DELETE",command=delete,width=10,background = 'red',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
    delete.grid(row=30 , column=4, columnspan=1,ipadx = 10,padx = 10)


    txt = scrolledtext.ScrolledText(root,width=135,height=10,background = 'WHITE', foreground ="BLACK",font=("times new roman",11))
    txt.grid(row=29,column=0,rowspan=1, columnspan=9)

    save=Button(root,text="SAVE",command=saveFile,width=10,background = 'green',bd=7,relief = GROOVE, foreground ="white",font=("lucida",12,"bold"))
    save.grid(row=30 , column=5,ipadx = 10,padx = 10)

    combo_class = ttk.Combobox(root,width=15)    # Filter Searches
    combo_class['values']= ("CLASS","FORM 1","FORM 2","FORM 3","FORM 4")
    combo_class.current(0) #set the selected item
    combo_class.grid(row=0,column=4)

    combo_class_button=Button(root,text="SEARCH",command=classwise,width=10,background = 'yellow', foreground ="black",font=("lucida",12,"bold"))
    combo_class_button.grid(row=0 , column=5,)

    
 

    root.mainloop()
    
