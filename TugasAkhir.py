from tkinter import *
from tkinter import \
    ttk
import random
from ctypes import resize
from tkinter import messagebox
from tkinter.messagebox import *

class Application():
    def __init__(self,hp,atk,defe):
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.grid()

    def sethp(self, hp):
        self.hp = hp

    def gethp(self):
        return self.hp

    def setatk(self, atk):
        self.atk = atk

    def getatk(self):
        return self.atk

    def setdefe(self, defe):
        self.defe = defe

    def getdefe(self):
        return self.defe

    def serang ():
        if saber.hp <= 0:
            story = " musuh telah mati "
        else:
            saber.hp -= player.atk-saber.defe
            saberhp = str(saber.hp)
            story = " HP musuh tersisa: "
            story += saberhp
            if saber.hp <= 0:
                story += " musuh telah mati "
            story += " "
            player.hp -= saber.atk - player.defe
            plahp =str(player.hp)
            story += " HP player tersisa: "
            story += plahp
            if saber.hp <= 0:
                story+= " player mati. "
        sto = Label(window,
                          text=story,
                          font=("times new roman", 10), fg ="red" ).place(x=0, y=30)

    def bertahan ():
        story = "player bertahan, DEF player menjadi"
        player.defe += player.defe * 0.5
        sadef = str(player.defe)
        story += sadef
        player.hp -= saber.atk - player.defe
        plahp = str(player.hp)
        story += ". HP player tersisa: "
        story += plahp
        sto = Label(window,
                          text=story,
                          font=("times new roman", 10), fg = "green").place(x=0, y=30)

    def info():
        ph = str(player.hp)
        pdf = str(player.defe)
        pa = str(player.atk)
        sh = str(saber.hp)
        sdf = str(saber.defe)
        sa = str(saber.atk)
        story = "info player:  HP : "
        story += ph
        story += " ATK : "
        story += pa
        story += " DEF : "
        story += pdf
        story += "  "
        story += "info musuh:  HP : "
        story += sh
        story += " ATK : "
        story += sa
        story += " DEF : "
        story += sdf
        sto = Label(window,
                          text=story,
                          font=("times new roman", 10), fg ="yellow", bg = "blue").place(x=0, y=30)

    def start():
        bttn = Button()
        bttn["text"] = "serang"
        bttn["command"] = Application.serang
        bttn.grid(row=0, column=0, columnspan=1, sticky=W)

        bttn = Button()
        bttn["text"] = "bertahan"
        bttn["command"] = Application.bertahan
        bttn.grid(row=0, column=1, columnspan=1, sticky=W)

        bttn = Button()
        bttn["text"] = "info"
        bttn["command"] = Application.info
        bttn.grid(row=0, column=2, columnspan=1, sticky=W)

        story_txt = Text( width=60, height=20, wrap=WORD)
        story_txt.grid(row=3, column=0, columnspan=3, sticky=W)



player = Application(1500,400,200)
saber = Application(1000,500,100)

window = Tk()
window.title(" One Click RPG ")
window.geometry("500x200")
window.resizable(width = 0, height = 0)
menu = Menu(window)
window.config(menu=menu)
start = Button(window,
               text = "start",
               command = Application.start,
               font =("Calibri", 14),
               fg = "green",
               bg = "black",
               ).place(x= 215, y =80)

window.config(menu=menu)
quit = Button(window,
               text = "keluar",
               command = quit,
               font =("Calibri", 14),
               fg = "red",
               bg = "white",
               ).place(x= 210, y =120)
labelnama = Label(window,
text = "One Click RPG\t:",
font = ("times new roman", 20)).place(x=100, y=20)


window.mainloop()