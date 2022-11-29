from tkinter import *
import random

root = Tk()

root.title("Encapsulation")
root.geometry("500x500")

label_name = Label(root, font= ("Comic",20,"bold"), bg= "white")
label_name.place(relx=0.5,rely=0.5,anchor=CENTER)

class score:
    def __init__(self):
        self.__score = 0
    def updategame(self):
        self.text = ["BLUE","PURPLE","ORANGE","PINK","YELLOW","RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["blue","purple","orange","pink","yellow","red"]
        self.random_number_for_color = random.randint(0,5)
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
obj1 = score()

btn = Button(root,text="Start",relief=FLAT,command=obj1.updategame)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()