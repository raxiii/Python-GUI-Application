from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os.path
import sqlite3


Script = ("Seoge Script",12,"bold")

class Coffee_shop:
        conn = sqlite3.connect("Skybank.db", timeout=100)
        
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                            
        def __init__(self,root):                       
                        self.login = True
                        self.cur = self.conn.cursor()
                        self.conn.commit()
                        self.root = root
                        
                        #============variables======================================
                        self.username=StringVar()
                        self.password=StringVar()       
                        #====================================
                        self.frame = Frame ( self.root, bg="white",width="600",height="500",bd=10,highlightcolor="cyan",highlightthickness=7,highlightbackground="cyan")
                        #self.frame.attributes("-alpha", 0.3)
                        #self.frame.attributes('-alpha', 0.8)
                        self.logo=PhotoImage(file="logo.png")
                        self.lbl2=Label(self.frame,image=self.logo,bg="white")
                        self.lbl2.place(x=180,y=55)
                        
                        self.st1= Label(self.frame, text="Expertise you need. Service you deserve!",fg="cyan",bg="white",font=("Gabriola",18,"bold"),pady=2)
                        self.st1.place(x=100,y=150)
                        self.frame.place(x=80, y=150)
                        #Login Page Form Components
                        #==========images===============
                        self.user=PhotoImage(file="user2.png")
                        self.keys=PhotoImage(file="key2.png")
                         #=================================
                        self.frame1=LabelFrame(self.frame,text="Log In",bd=5,relief=SOLID,width=550,height=230,highlightbackground="cyan",highlightcolor="cyan",font=("Segoe Script",16,"bold"),fg="cyan",bg="white")
                        self.frame1.place(x=10,y=230)
                        self.luser=Label(self.frame1,image=self.user,bg="white").place(x=150,y=30)
                        self.lkeys=Label(self.frame1,image=self.keys,bg="white").place(x=150,y=70)
                        self.uname=Entry(self.frame1,textvariable=self.username,width=18, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="#0ff").place(x=200,y=30)
                        self.pwd=Entry(self.frame1,textvariable=self.password,show="*",width=18,font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="#0ff").place(x=200,y=70)

                        self.btn1 = Button(self.frame1, text = 'Log In',command=self.verify, width=15,bg="cyan",fg="white",font=("Calibri",12,"bold"),activebackground="white",activeforeground="cyan",relief=RIDGE,bd=3) 
                        self.btn1.place(x=150,y=120)
                        self.btn2 = Button(self.frame1, text = 'Register',command = self.register, width=15,bg="cyan",fg="white",font=("Calibri",12,"bold"),activebackground="white",activeforeground="cyan",relief=RIDGE,bd=3) 
                        self.btn2.place(x=300,y=120)

        #--------------------------------------------------------------------------------------------------------------
        def verify(self):#verifying for authorised user
                ac = False
                self.temp = self.conn.execute("select username,password from cafe_details where username = ? and password=? ", (self.username.get(),self.password.get()))
               
                for i in self.temp:
                    #self.ac = i[0]
                    print("welcom "+i[0])
                    if i[0] == self.username.get() and i[1] == self.password.get() :
                       
                        m = "{} Login SucessFull".format(i[0])
                       # self.database_fetch()
                        messagebox._show("Login Info", m)
                        self.frame.destroy()
                        self.MainMenu(i[0])
                    else:
                        ac = True
                        m = " Login UnSucessFull ! Wrong Password"
                        messagebox._show("Login Info!", m)

                """if not ac:
                    m = " Wrong Username !"
                    messagebox._show("Login Info!", m)"""

        #--------------------------------------------------------------------------------------------------------------
        def validate(self):
                self.value=str(self.option.get())
                self.n=str(self.name.get())
                self.emp_id=str(self.id.get())
                self.ag=int(self.age.get())
                self.c_no=int(self.contact.get())
                self.u_name=str(self.uname.get())
                self.passwrd=str(self.passd.get())
                self.add=str(self.address.get())
                """if self.username.get() == "" or self.password.get() == "" or self.name.get()==""or self.id.get()==""or self.age.get()=="" or self.contact.get()==""or self.address.get()=="":
                        messagebox.showerror("Registration Failed","Empty fields!")"""
                
                self.cursor.execute('INSERT INTO cafe_login_details (name,id,age,contact,username, password,gender,address) VALUES(?,?,?,?,?,?,?,?)',(self.n,self.emp_id,self.ag,self.c_no,self.u_name,self.passwrd,self.value,self.add))
                self.conn.commit()
                messagebox.showinfo("Registration Successful","Congratulation! successfully registered")
                self.frame.destroy()
                self.__init__();
                #except:
                        #messagebox.showerror("Registration Failed","Something went Wrong")
        #--------------------------------------------------------------------------------------------------------------
        def register(self):
                self.frame.destroy()
                #============variables======================================
                image=Image.open("background.jpeg")
                bg=ImageTk.PhotoImage(image)
                self.l1=Label(self.root,image=bg)
                self.l1.pack()
                self.name=StringVar()
                self.id=StringVar()
                self.age=StringVar()
                self.contact=StringVar()
                self.uname=StringVar()
                self.passd=StringVar()
                self.option=StringVar()
                self.address=StringVar()
                #=======================================================
                self.frame = Frame ( self.root, bg="white",width="400",height="600",bd=10,highlightcolor="cyan",highlightthickness=7,highlightbackground="cyan")
                self.logo=PhotoImage(file="logo.png")
                self.lbl2=Label(self.frame,image=self.logo,bg="white")
                self.lbl2.place(x=100,y=150)
                
                self.st1= Label(self.frame, text="Expertise you need. Service you deserve!",fg="cyan",bg="white",font=("Gabriola",18,"bold"),pady=2)
                self.st1.place(x=20,y=350)
                self.frame.place(x=70, y=50)
                #---------------------------------------------------------------------------------------------------------------------------------------------------------
                self.frame2 = Frame ( self.root, bg="white",width="700",height="600",bd=10,highlightcolor="cyan",highlightthickness=7,highlightbackground="cyan")
                self.frame1=LabelFrame(self.frame2,text="Register Yourself",bd=5,relief=SOLID,width=650,height=550, highlightcolor="cyan",font=("Segoe Script",24,"bold"),fg="cyan",bg="white")

                self.lbl_name= Label(self.frame1, text="Name:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=5,y=10)
                self.e_name=Entry(self.frame1,textvariable=self.name,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=55,y=45)

                self.lbl_id= Label(self.frame1, text="Employee ID:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=310,y=10)
                self.e_id=Entry(self.frame1,textvariable=self.id,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=360,y=45)

                self.lbl_age= Label(self.frame1, text="Age:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=5,y=90)
                self.e_age=Entry(self.frame1,textvariable=self.age,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=55,y=125)

                self.lbl_contact= Label(self.frame1, text="Contact:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=310,y=90)
                self.e_contact=Entry(self.frame1,textvariable=self.contact,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=360,y=125)

                self.lbl_uname= Label(self.frame1, text="Username:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=5,y=170)
                self.e_uname=Entry(self.frame1,textvariable=self.uname,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=55,y=205)

                self.lbl_passd= Label(self.frame1, text="Password:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=310,y=170)
                self.e_passd=Entry(self.frame1,show="*",textvariable=self.passd,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=360,y=205)

                self.lbl_gender= Label(self.frame1, text="Gender:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=5,y=250)
                self.e_male = Radiobutton(self.frame1, text="Male", fg="cyan",bg="white",font=("Gabriola",14,"bold"),variable=self.option, value="Male").place( x=80,y=280)
                self.e_female = Radiobutton(self.frame1, text="Female", fg="cyan",bg="white",font=("Gabriola",14,"bold"),variable=self.option, value="Female").place( x=80,y=310)
                self.e_others = Radiobutton(self.frame1, text="Others", fg="cyan",bg="white",font=("Gabriola",14,"bold"),variable=self.option, value="Others").place( x=80,y=340)

                self.lbl_address= Label(self.frame1, text="Address:",fg="cyan",bg="white",font=("Gabriola",14,"bold"),padx=50,pady=2).place(x=310,y=250)
                self.e_add=Entry(self.frame1,textvariable=self.address,width=20, font=("Comic sans ms",12),fg="black",highlightthickness=2,highlightbackground="cyan",highlightcolor="cyan").place(x=360,y=290)

                self.btn3 = Button(self.frame1, text = 'Register',command=self.validate, width=15,bg="cyan",fg="black",font=("Calibri",12,"bold"),activebackground="cyan",activeforeground="white",relief=RIDGE,bd=3) 
                self.btn3.place(x=150,y=400)
                self.btn4 = Button(self.frame1, text = 'Clear',command = self.register, width=15,bg="cyan",fg="black",font=("Calibri",12,"bold"),activebackground="cyan",activeforeground="white",relief=RIDGE,bd=3) 
                self.btn4.place(x=350,y=400)

                self.frame1.place(x=10,y=10)
                self.frame2.place(x=470, y=50)

        def MainMenu(self,userName):
                self.frame.destroy()
                self.frame = Frame ( self.root, bg="white",width="400",height="600",bd=10,highlightcolor="cyan",highlightthickness=7,highlightbackground="cyan")
                self.userName=Label(self.frame,text="  Welcome To Skyhigh Bank\n"+userName,bg="white",font=("Segoe Script",15,"bold"),fg="cyan")
                self.userName.place(x=10,y=20)
                self.logo=PhotoImage(file="logo.png")
                self.lbl2=Label(self.frame,image=self.logo,bg="white")
                self.lbl2.place(x=55,y=150)
                
                self.st1= Label(self.frame, text="Expertise you need. Service you deserve!",fg="cyan",bg="white",font=("Gabriola",14,"bold"),pady=2)
                self.st1.place(x=35,y=250)
                self.frame.place(x=70, y=50)
                


                                                                    
root = Tk()
root.geometry("1350x900")

image=Image.open("background.jpeg")
bg=ImageTk.PhotoImage(image)
lbl=Label(root,image=bg)
lbl.pack()
userName=Label(root,text="  Welcome To Skyhigh Bank\n",bg="#000000",font=("Segoe Script",15,"bold"),fg="red")
userName.place(x=1,y=1)

obj = Coffee_shop(root)
root.mainloop()


