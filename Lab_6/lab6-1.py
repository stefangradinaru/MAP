from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("240x240")
def showrules():
 messagebox.showinfo("Rules", f"Game rules are: \n[ROCK] -> [SCISSORS]\n[SCISSORS] -> [PAPER]\n[PAPER] -> [ROCK]\nBest of 3!")
 
label_rules = Button(window, text="Rules", command=showrules, justify="center", fg="#08c9ac", pady=5)
label_rules.pack(side="top")
label_human = IntVar(window, value=0, name="Human")
label_pc = IntVar(window, value=0, name="PC")
label_gamestatus = Label(window, text=f"Game Status:\nUser: {label_human)}  - Opponent: {label_pc} ", fg="#08c9ac")
label_gamestatus.pack(side="bottom")

# Game Logic
def game(user_select):
    options = ["Rock", "Paper", "Scissors"]
    global pc_counter, user_counter
    pc_counter = 0
    user_counter = 0
    pc_select = random.choice(options)
    # Message constructor
    msg = f"The Computer chose:\n{pc_select}\n"
    
    
    if pc_select == user_select:
        msg += "[TIE]"
    elif (user_select == "Rock" and pc_select == "Scissors") or \
        (user_select == "Paper" and pc_select == "Rock") or \
            (user_select == "Scissors" and pc_select == "Paper"):
                msg+= "[YOU WIN!]"
                user_counter+= 1
                label_human.set(user_counter)
                label_gamestatus.config()
    else:
        msg+= "[YOU LOSE!]"
        pc_counter += 1
        label_pc.set(pc_counter)
    messagebox.showinfo("Game Results", msg)
    
    if pc_counter == 3:
        messagebox.showinfo("Loss", "You lost the game.\n\nBetter luck next time!")
        user_counter = 0
        pc_counter = 0
        label_pc.set(pc_counter)
        label_human.set(user_counter)
    elif user_counter == 3:
        messagebox.showinfo("Victory", "You won the game!\n \nCongratulations!")
        user_counter = 0
        pc_counter = 0
        label_pc.set(pc_counter)
        label_human.set(user_counter)
        

ButtonRock = Button(window, text = "Rock", width=10, command=lambda:game("Rock")).pack(side="left")
ButtonPaper = Button(window, text="Paper", width=10, command=lambda:game("Paper")).pack(side="left")
ButtonScissor = Button(window, text="Scissors", width=10, command=lambda:game("Scissors")).pack(side="left")


mainloop()