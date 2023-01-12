from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

root=Tk()
root.geometry("1200x650+100+30")
root.title("Student QR-Code Generator")
root.resizable(False,False)


title=Label(root,text="Student QR-Code Generator",font=("times new roman" ,32),bg='#333',fg='#fff').place(x=0,y=0,relwidth=1)

details_frame=Frame(root,bd=2,relief=RIDGE,bg='white')
details_frame.place(x=50,y=100,width=600,height=500)
details_title=Label(details_frame,text="Student Details",font=("times new roman" ,28),bg='#333',fg='#fff').place(x=0,y=0,relwidth=1)

name_var=StringVar()
parent_var=StringVar()
class_var=StringVar()
roll_var=StringVar()
contect_var=StringVar()
address_var=StringVar()

def generate():
    if name_var.get()=='' or parent_var.get()=='' or class_var.get()=='' or roll_var.get()=='' or contect_var.get()=='' or address_var.get()=='':
        msg='All Feilds are Reqiuired!!!'
        msg_label.config(text=msg, fg='red')
    else:
        data=(f"Student`s Name: {name_var.get()}\nParents`s Name: {parent_var.get()}\nClass: {class_var.get()}\nRoll NO: {roll_var.get()}\nContect No: {contect_var.get()}\nAddress: {address_var.get()}")
        qr=qrcode.make(data)
        print(qr)
        qr=resizeimage.resize_cover(qr,[250,250])
        im=ImageTk.PhotoImage(qr)
        QR_code_label.config(image=im)
        qr.save('E:/QR-code Generator/Student_details_QR/'+roll_var.get()+' QR_Code.png')
        msg='QR-Code generated successfully!!!'
        msg_label.config(text=msg, fg='green')

def clear():
    name_var.set('')
    parent_var.set('')
    class_var.set('')
    roll_var.set('')
    contect_var.set('')
    address_var.set('')
    msg=''
    msg_label.config(text=msg)
    QR_code_label.config(image='')

name=Label(details_frame,text="Student`s Name:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=60)
name_input=Entry(details_frame,textvariable=name_var ,font=('verdana' ,17), bg='lightyellow', width=20).place(x=250,y=60)

parent=Label(details_frame,text="Parent`s Name:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=110)
parent_input=Entry(details_frame,textvariable=parent_var ,font=('verdana' ,17), bg='lightyellow').place(x=250,y=110)

stu_class=Label(details_frame,text="Class:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=160)
class_input=Entry(details_frame,textvariable=class_var ,font=('verdana' ,17), bg='lightyellow').place(x=250,y=160)

roll=Label(details_frame,text="Roll No:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=210)
roll_input=Entry(details_frame,textvariable=roll_var ,font=('verdana' ,17), bg='lightyellow').place(x=250,y=210)

contect=Label(details_frame,text="Contect No:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=260)
contect_input=Entry(details_frame,textvariable=contect_var ,font=('verdana' ,17), bg='lightyellow').place(x=250,y=260)

address=Label(details_frame,text="Address:  ",font=("verdana" ,17, 'bold'),bg='white').place(x=25,y=310)
address_input=Entry(details_frame,textvariable=address_var ,font=('verdana' ,17), bg='lightyellow').place(x=250,y=310)
        
generator_btn=Button(details_frame, text="Generate QR-Code",command=generate ,font=('times new roman', 15,'bold'),fg='#fff',bg='green',borderwidth=6).place(x=25,y=360)
generator_btn=Button(details_frame, text="Clear",command=clear ,font=('times new roman', 15,'bold'),fg='#fff',bg='red',borderwidth=6).place(x=490,y=360)

msg=''
msg_label=Label(details_frame,text=msg,font=('times new roman', 16,'bold'), bg='white', fg='green')
msg_label.place(x=145,y=430)

QR_frame=Frame(root,bd=2,relief=RIDGE,bg='white')
QR_frame.place(x=700,y=100,width=440,height=500)
QR_title=Label(QR_frame,text="Student`s QR-Code",font=("times new roman" ,28),bg='#333',fg='#fff').place(x=0,y=0,relwidth=1)

QR_code_label=Label(QR_frame,text='No QR-Code\n\nAvailable',bd=3,relief=RIDGE,font=('times new roman' ,18,'bold'),fg='#fff',bg='#333')
QR_code_label.place(x=95,y=140,width=250,height=250)





root.mainloop()
