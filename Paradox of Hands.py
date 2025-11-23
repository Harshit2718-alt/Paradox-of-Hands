import tkinter as tk
import random, time, threading


class GameRPS:
    def __init__(self):
        self.p = 0
        self.c = 0
        self.d = 0
        self.r = 1
        self.h = []
        self.wl = 5
        
        self.pics = {
            "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",


"scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
        }

        self.ops = ["rock","paper","scissors"]


    def calc(self, u, cc):
        if u == cc:
            return "draw"
        xx = {"rock":"scissors","paper":"rock","scissors":"paper"}
        if xx.get(u)==cc:
            return "win"
        return "lose"



    def save(self, u,cm,rr):
        self.h.append((self.r,u,cm,rr))


    def done(self):
        if self.p==self.wl:
            return "p"
        if self.c==self.wl:
            return "c"
        return None




g=GameRPS()


root=tk.Tk()
root.title("Rps???")
root.geometry("530x535")


lb1=tk.Label(root,text="Your Choice:",font=("Arial",11))
lb1.pack(pady=5)

lb2=tk.Label(root,text="CPU:",font=("Arial",11))
lb2.pack(pady=4)

lb3=tk.Label(root,text="Result:",font=("Arial",15))
lb3.pack(pady=10)

lb4=tk.Label(root,text="Score: 0 - 0",font=("Arial",14,'bold'))
lb4.pack(pady=6)

lb5=tk.Label(root,text="Round: 1",font=("Arial",11))
lb5.pack(pady=4)

txt=tk.Text(root,width=58,height=14)
txt.pack(pady=12)




def pressed(x):
    t=threading.Thread(target=goRound,args=(x,),daemon=True)
    t.start()




def goRound(m):

    lb1.config(text="Your Choice: "+m.capitalize())

    txt.delete("1.0",tk.END)
    txt.insert(tk.END,"cpu choosing...")
    time.sleep(0.27)

    txt.delete("1.0",tk.END)
    txt.insert(tk.END,"cpu hmm...\n")
    time.sleep(0.4)

    cm = random.choice(g.ops)
    lb2.config(text="CPU: "+cm.capitalize())

    big = "YOU:\n"+g.pics[m]+"\nCPU:\n"+g.pics[cm]
    txt.delete("1.0",tk.END)
    txt.insert(tk.END,big)

    rr=g.calc(m,cm)

    if rr=="win":
        g.p+=1
        lb3.config(text="Result: You Won!")
    elif rr=="lose":
        g.c+=1
        lb3.config(text="Result: CPU Won!")
    else:
        g.d+=1
        lb3.config(text="Result: Draw")

    lb4.config(text="Score: "+str(g.p)+" - "+str(g.c))

    g.save(m,cm,rr)

    f=g.done()
    if f:
        if f=="p":
            tmsg="YOU WON!!!"
        else:
            tmsg="CPU WON!!!"

        w=tk.Toplevel(root)
        w.title("Done!")
        tk.Label(w,text=tmsg,font=("Arial",17,'bold')).pack(pady=17)
        tk.Label(w,text="Final Score: "+str(g.p)+" - "+str(g.c),font=("Arial",13)).pack(pady=8)
        tk.Button(w,text="ok",command=root.destroy).pack(pady=15)
        return


    g.r+=1
    lb5.config(text="Round: "+ str(g.r))






fr=tk.Frame(root)
fr.pack(pady=18)

bt1=tk.Button(fr,text="Rock",width=10,command=lambda: pressed("rock"))
bt1.pack(side=tk.LEFT,padx=10)

bt2=tk.Button(fr,text="Paper",width=10,command=lambda: pressed("paper"))
bt2.pack(side=tk.LEFT,padx=10)

bt3=tk.Button(fr,text="Scissors",width=10,command=lambda: pressed("scissors"))
bt3.pack(side=tk.LEFT,padx=10)


root.mainloop()
