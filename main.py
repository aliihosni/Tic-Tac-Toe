from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

root = Tk()
root.title("Tic Tac Toe")
style = Style()
style.theme_use('clam')

ActivePlayer = 1
P1 = []
P2 = []
Winner = -1

button1 = Button(root, text=' ')
button1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
button1.config(command=lambda: BClick(1))

button2 = Button(root, text=' ')
button2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
button2.config(command=lambda: BClick(2))

button3 = Button(root, text=' ')
button3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
button3.config(command=lambda: BClick(3))

button4 = Button(root, text=' ')
button4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
button4.config(command=lambda: BClick(4))

button5 = Button(root, text=' ')
button5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
button5.config(command=lambda: BClick(5))

button6 = Button(root, text=' ')
button6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
button6.config(command=lambda: BClick(6))

button7 = Button(root, text=' ')
button7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
button7.config(command=lambda: BClick(7))

button8 = Button(root, text=' ')
button8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
button8.config(command=lambda: BClick(8))

button9 = Button(root, text=' ')
button9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
button9.config(command=lambda: BClick(9))


def SetLayout(i, text):
    if (i == 1):
        button1.config(text=text)
        button1.state(['disabled'])
    elif (i == 2):
        button2.config(text=text)
        button2.state(['disabled'])
    elif (i == 3):
        button3.config(text=text)
        button3.state(['disabled'])
    elif (i == 4):
        button4.config(text=text)
        button4.state(['disabled'])
    elif (i == 5):
        button5.config(text=text)
        button5.state(['disabled'])
    elif (i == 6):
        button6.config(text=text)
        button6.state(['disabled'])
    elif i == 7:
        button7.config(text=text)
        button7.state(['disabled'])
    elif i == 8:
        button8.config(text=text)
        button8.state(['disabled'])
    elif (i == 9):
        button9.config(text=text)
        button9.state(['disabled'])


def CheckWinner():
    global Winner

    if set([1, 2, 3]).issubset(P1):
        Winner = 1
    elif set([1, 4, 7]).issubset(P1):
        Winner = 1
    elif set([1, 5, 9]).issubset(P1):
        Winner = 1
    elif set([3, 6, 9]).issubset(P1):
        Winner = 1
    elif set([7, 8, 9]).issubset(P1):
        Winner = 1
    elif set([3, 5, 7]).issubset(P1):
        Winner = 1

    if set([1, 2, 3]).issubset(P2):
        Winner = 1
    elif set([1, 4, 7]).issubset(P2):
        Winner = 2
    elif set([1, 5, 9]).issubset(P2):
        Winner = 2
    elif set([3, 6, 9]).issubset(P2):
        Winner = 2
    elif set([7, 8, 9]).issubset(P2):
        Winner = 2
    elif set([3, 5, 7]).issubset(P2):
        Winner = 2


def BClick(i):
    global ActivePlayer
    global P1
    global P2

    if ActivePlayer == 1:
        SetLayout(i, 'X')
        P1.append(i)
        ActivePlayer = 2
        root.title("Tic Tac Toe | Player 2")

    elif ActivePlayer == 2:
        SetLayout(i, 'O')
        P2.append(i)
        ActivePlayer = 1
        root.title("Tic Tac Toe | Player 1")

    CheckWinner()

    if Winner == 1:
        showinfo('Congratulation', 'Player 1 win')
    elif Winner == 2:
        showinfo('Congratulation', 'Player 2 win')


# bouton=Button(root, text="Fermer", command=root.quit)
# bouton.pack(SIDE=BOTTOM)




root.mainloop()
