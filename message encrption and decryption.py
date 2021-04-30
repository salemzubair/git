##importing mmodules

from tkinter import *
import base64
import  tkinter as tk

#initialize window
root = Tk()
root.geometry('600x400')
root.resizable(0,0)



#title of the window
root.title("Message Encode and Decode")



#label

Label(root, text ='ENCRYPTION && DECRYPTION', font = 'arial 20 bold').pack()
Label(root, text ='SALEM', font = 'arial 20 bold').pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-Encrypt, d-Decrypt)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)



#result

######result button
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=250, y = 270)
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =100,bg ='blue' ,command = Mode).place(x=190, y = 300)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =7, command = Reset,bg = 'Green', padx=50).place(x=50, y = 190)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 7, command = Exit,bg = 'Red', padx=50, pady=2).place(x=390, y = 190)
root.mainloop()

