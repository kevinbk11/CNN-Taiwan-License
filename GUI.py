import tkinter as tk

import os

import tkinter.messagebox

import threading as th


windows = tk.Tk()

windows.withdraw()




changewindows=tk.Toplevel()
changewindows.withdraw()
changewindows.title("密碼變更")
changewindows.geometry("280x125")
changewindows.resizable(0,0)
changewindows.config(bg="skyblue")

changewindows.attributes("-alpha",0.85)

changewindows.attributes("-topmost",1)
DataBase=tk.Toplevel()

DataBase.withdraw()

DataBase.title("車牌資料庫")

DataBase.geometry("170x590")



DataBase.resizable(0,0)



DataBase.config(bg="skyblue")

DataBase.attributes("-alpha",0.85)

DataBase.attributes("-topmost",1)

listbox=tk.Listbox(DataBase,height=23)







log=tk.Toplevel()

log.title("登入")



log.geometry("210x125")



log.resizable(0,0)



log.config(bg="skyblue")

log.attributes("-alpha",0.85)

log.attributes("-topmost",1)



windows.geometry("280x125")



windows.resizable(0,0)



windows.config(bg="skyblue")

windows.attributes("-alpha",0.85)

windows.attributes("-topmost",1)



windows.title("資料庫介面")


acc=""
class features():

    

    def __init__(self):



        super().__init__()  



    def disable_event(self):

        pass
    def ChangePassword(self):
        fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\account.pt","r")
        list1=fp.readlines()
        fp.close()
        fx=open(r".vscode\car\save.pt","r")
        NowUser=fx.readline()
        for x in list1:
            if x == NowUser:
                newp=newpassword.get()
                list1.remove(NowUser)
                fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\account.pt","w")
                for w in list1:
                    fp.write(w)
                a,b=NowUser.split()
                fp.write(a+" "+newp+"\n")
        tk.messagebox.showinfo(title="成功!",message="已成功更改密碼!")

    def Change(self):

        changewindows.deiconify()
        ChangeButton.place(x=200,y=45)
        newpassword.place(x=30,y=50)


    def write(self):

        fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","a")

        if cartext.get()!="":

            fp.write(cartext.get()+'\n')

            tk.messagebox.showinfo(title="成功!",message="已新增車牌:"+cartext.get())

            cartext.delete(0,"end")

        else:

            tk.messagebox.showerror(title="錯誤!",message="車牌不能為空")

        fp.close()

    def exit(self):

        

        left=tk.messagebox.askquestion(title="離開",message="確定要離開?")

        if left=="yes":

            windows.destroy()



    def login(self):

        User=account.get()+ " " +password.get()+"\n"
        print(User)
        fp=open(r".vscode\car\account.pt","r")
        list1=fp.readlines()
        fp.close()
        print(list1)
        if User in list1:



            tk.messagebox.showinfo(title="登入訊息",message="登入成功")



            log.destroy()

            windows.deiconify()

            showcarbutton.place(x=5,y=45)

            addcar.place(x=5,y=5)

            cartext.place(x=100,y=9,width=175)

            delcar.place(x=100,y=45)

            DeleteAllCar.place(x=5,y=85)

            ChangePassword.place(x=100,y=85)
            fx=open(r".vscode\car\save.pt","w")
            fx.write(User)
            fx.close()
        else:

            tk.messagebox.showerror("登入訊息","帳號或密碼錯誤")



    def showdata(self):



        listbox.delete(0,'end')

        fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","r")

        list1=fp.readlines()

        DataBase.deiconify()

        fp.close()

        for x in list1:

            listbox.insert(0,x)

        listbox.pack()



    def delete(self):

        list1=[]

        car=cartext.get()

        car=car+"\n"

        fp1=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","r")

        list1=fp1.readlines()

        fp1.close()

        fp2=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","w")

        if car in list1:

            c,n=car.split("\n")

            MESSAGE="成功刪除車牌: "+c+" !"

            print(MESSAGE)

            tk.messagebox.showinfo(title="成功",message=MESSAGE)

            list1.remove(car)

            for a in list1:

                fp2.write(a)

                fp2.close()

        else:

            tk.messagebox.showerror(title="失敗",message="查無此車牌!")

            for a in list1:

                fp2.write(a)

                fp2.close()

    def deleteALL(self):

        YorNo=tk.messagebox.askquestion(title="清除資料庫",message="確定要清除嗎?")

        if YorNo=="yes":

                YorNo2=tk.messagebox.askquestion(title="清除資料庫",message="清除後無法復原,還是要清除嗎?")

                if YorNo2=="yes":

                    fp1=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","w")

                    fp1.write("")

                    fp1.close()

                

    def refresh(self):


        listbox.delete(0,'end')

        fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","r")

        list1=fp.readlines()

        fp.close()

        for x in list1:

            listbox.insert(0,x)

    def Break(self):

        DataBase.withdraw()

class features_key(): 



    def __init__(self):



        super().__init__()  



    def exit(self,event):



        left=tk.messagebox.askquestion(title="離開",message="確定要離開?")

        if(left=="yes"):

            windows.destroy()



    def login(self,event):

        User=account.get()+ " " +password.get()+"\n"
        print(User)
        fp=open(r".vscode\car\account.pt","r")
        list1=fp.readlines()
        fp.close()
        print(list1)
        if User in list1:



            tk.messagebox.showinfo(title="登入訊息",message="登入成功")



            log.destroy()

            windows.deiconify()

            showcarbutton.place(x=5,y=45)

            addcar.place(x=5,y=5)

            cartext.place(x=100,y=9,width=175)

            delcar.place(x=100,y=45)

            DeleteAllCar.place(x=5,y=85)

            ChangePassword.place(x=100,y=85)
            fx=open(r".vscode\car\save.pt","w")
            fx.write(User)
            fx.close()
        else:

            tk.messagebox.showerror("登入訊息","帳號或密碼錯誤")



    def Break(self,event):



        DataBase.withdraw()



F=features()

F_K=features_key()

##-------------------------------------------------------

showcarbutton=tk.Button(text="查看資料庫",command=F.showdata,height=1,width=8)



btn=tk.Button(log,text="login",bg="yellow",command=F.login,height=1,width=7)



btn2=tk.Button(text="exit",bg="red",command=F.exit,height=1,width=7)



account=tk.Entry(log,width=14)

newpassword=tk.Entry(changewindows,width=20)

password=tk.Entry(log,width=14,show="*")



AccountLabel=tk.Label(log,text="帳號",width=8)



PasswordLabel=tk.Label(log,text="密碼",width=8)



addcar=tk.Button(text="加入車牌",command=F.write,width=8,height=1)



cartext=tk.Entry()



delcar=tk.Button(text="刪除車牌",command=F.delete,width=8,height=1)

ChangePassword=tk.Button(text="更改密碼",command=F.Change,width=8,height=1)

DeleteAllCar=tk.Button(text="清除資料庫",command=F.deleteALL,height=1,width=8)

ChangeButton = tk.Button(changewindows,text="更改",command=F.ChangePassword,width=8,height=1)

ref=tk.Button(DataBase,text="refresh",command=F.refresh,width=18,height=1)



logexit=tk.Button(log,text="exit",bg="red",command=F.exit,height=1,width=7)



base_exit=tk.Button(DataBase,text="exit",bg="red",command=F.Break,height=1,width=8)

##----------------------------------------------------



password.bind("<Return>",F_K.login)



account.bind("<Return>",F_K.login)



windows.bind("<Escape>",F_K.exit)



log.bind("<Escape>",F_K.exit)



DataBase.bind("<Escape>",F_K.Break)



windows.protocol("WM_DELETE_WINDOW", F.disable_event)



log.protocol("WM_DELETE_WINDOW", F.disable_event)



DataBase.protocol("WM_DELETE_WINDOW", F.disable_event)



base_exit.place(x=70,y=550)

logexit.place(x=25,y=85)

btn.place(x=115,y=85)

btn2.place(x=190,y=85)

account.place(x=80,y=20)

password.place(x=80,y=50)

AccountLabel.place(x=10,y=20)

PasswordLabel.place(x=10,y=50)

ref.pack()



log.mainloop()