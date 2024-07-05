print('HELLO EVERYONE')
print('My Name is KANAUJIYA ADARSH KUMAR PREMNARAYAN')
print('Class : SYJC      DIV : G     ROLL NO : 798')
print('MY PROJRCT IS A GAME , WHOSE NAME IS \n TIC TAC TOE \n ')
A=str(input('Enter PlayerX Name :'))
B=str(input('Enter PlayerO Name :'))

import tkinter.messagebox
from tkinter import*

window = tkinter.Tk()
window.geometry('1000x750')
window.title('TIC TAC TOE')
window.configure(background = 'Cadet Blue')

MainFrame = Frame(window,bd=10, bg ='Powder Blue', width =1000,height =600)
MainFrame.grid(row=1 , column=0)


var_1 = Frame(window, bg ='Cadet Blue', width =1000 ,height =100, relief =RIDGE)
var_1.grid(row=0 , column=0)


l1 =tkinter.Label(var_1,font=('arial',50,'bold'),bd=21, text='TIC TAC TOE GAME',bg='Cadet Blue',fg='cornsilk')
l1.grid(row=0, column=0)

LeftFrame = Frame(MainFrame,bd=10 ,width=550, height=500, pady=2,padx=10,bg='Cadet Blue', relief =RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame,bd=10, width=360, height=500, pady=2,padx=10,bg='Cadet Blue', relief =RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame,width=360,bd=10, height=200, pady=2,padx=10,bg='Cadet Blue', relief =RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame,bd=10,width=360, height=200, pady=2,padx=10,bg='Cadet Blue', relief =RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

tkinter.messagebox.showinfo('GAME INSTRUCTION','PLAYER CHOOSE THE PLACE AND PLAY \n GAME WIL START WITH X \n IF THE ROUND END WITH X THE NEXT ROUND START WITH O')
tkinter.messagebox.showinfo('GAME INSTRUCTION','USE RESET BUTTON FOR RESTART THE GAME WITHOUT CHANGING THE SCORE \n USE NEW GAME BUTTON FOR NEW GAME WITH 0 SCORE ')
tkinter.messagebox.showinfo('GAME INSTRUCTION','IF THEIR IS A TIES CLICK ON REST BUTTON')
tkinter.messagebox.showinfo('GAME INSTRUCTION',"DON'T CHEAT AND DON'T MAKE CHANGES IN THE SCORE,IT WILL EFFECT THE ENJOYMENT")

buttons = StringVar()
click = True

def check(buttons):
    global click
    if buttons['text']=='  ' and click == True:
        buttons['text'] = 'X'
        click = False
        score()
    elif buttons['text']=='  ' and click == False:
        buttons['text'] = 'O'
        click = True
        score()


def reset():
    button1['text']='  '
    button2['text']='  '
    button3['text']='  '
    button4['text']='  '
    button5['text']='  '
    button6['text']='  '
    button7['text']='  '
    button8['text']='  '
    button9['text']='  '

    button1.configure(background = 'gainsboro')
    button2.configure(background = 'gainsboro')
    button3.configure(background = 'gainsboro')
    button4.configure(background = 'gainsboro')
    button5.configure(background = 'gainsboro')
    button6.configure(background = 'gainsboro')
    button7.configure(background = 'gainsboro')
    button8.configure(background = 'gainsboro')
    button9.configure(background = 'gainsboro') 

def newgame():
    PlayerX.set(0)
    PlayerO.set(0)
    reset()
    
def end():
    tkinter.messagebox.showinfo('GAME INSTRUCTION','SEE THE IDLE SHEEL ')
    exit()



def score():
    if (button1['text']=='X' and button2['text']=='X' and button3['text']=='X'):
        button1.configure(background = 'yellow')
        button2.configure(background = 'yellow')
        button3.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button4['text']=='X' and button5['text']=='X' and button6['text']=='X'):
        button4.configure(background = 'yellow')
        button5.configure(background ='yellow')
        button6.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button7['text']=='X' and button8['text']=='X' and button9['text']=='X'):
        button7.configure(background = 'yellow')
        button8.configure(background = 'yellow')
        button9.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button1['text']=='X' and button4['text']=='X' and button7['text']=='X'):
        button1.configure(background = 'yellow')
        button4.configure(background = 'yellow')
        button7.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button2['text']=='X' and button5['text']=='X' and button8['text']=='X'):
        button2.configure(background = 'yellow')
        button5.configure(background = 'yellow')
        button8.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button3['text']=='X' and button6['text']=='X' and button9['text']=='X'):
        button3.configure(background = 'yellow')
        button6.configure(background = 'yellow')
        button9.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()

    if (button1['text']=='X' and button5['text']=='X' and button9['text']=='X'):
        button1.configure(background = 'yellow')
        button5.configure(background = 'yellow')
        button9.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()
       
    if (button3['text']=='X' and button5['text']=='X' and button7['text']=='X'):
        button3.configure(background = 'yellow')
        button5.configure(background = 'yellow')
        button7.configure(background = 'yellow')
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo('Winner X','Player X is a winner ')
        reset()




    if (button1['text']=='O' and button2['text']=='O' and button3['text']=='O'):
        button1.configure(background = 'GREEN')
        button2.configure(background = 'GREEN')
        button3.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    if (button4['text']=='O' and button5['text']=='O' and button6['text']=='O'):
        button4.configure(background = 'GREEN')
        button5.configure(background = 'GREEN')
        button6.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    if (button7['text']=='O' and button8['text']=='O' and button9['text']=='O'):
        button7.configure(background ='GREEN')
        button8.configure(background ='GREEN')
        button9.configure(background ='GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    if (button1['text']=='O' and button4['text']=='O' and button7['text']=='O'):
        button1.configure(background = 'GREEN')
        button4.configure(background = 'GREEN')
        button7.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    if (button2['text']=='O' and button5['text']=='O' and button8['text']=='O'):
        button2.configure(background = 'GREEN')
        button5.configure(background = 'GREEN')
        button8.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()
        
    if (button3['text']=='O' and button6['text']=='O' and button9['text']=='O'):
        button3.configure(background = 'GREEN')
        button6.configure(background = 'GREEN')
        button9.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    if (button1['text']=='O' and button5['text']=='O' and button9['text']=='O'):
        button1.configure(background = 'GREEN')
        button5.configure(background = 'GREEN')
        button9.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()
        
    if (button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        button3.configure(background = 'GREEN')
        button5.configure(background = 'GREEN')
        button7.configure(background = 'GREEN')
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo('Winner O','Player O is a winner ')
        reset()

    

l1PlayerX = Label(RightFrame1,font=('arial',20,'bold'), text='Player X:',pady=2,padx=2,bg='Cadet Blue')
l1PlayerX.grid(row=0, column=0)
l1PlayerX = Label(RightFrame1,font=('arial',15,'bold'), text=A,pady=2,padx=2,bg='Cadet Blue')
l1PlayerX.grid(row=1, column=0)
txtPlayerX = Entry(RightFrame1,font=('arial',15,'bold'),relief=RIDGE,textvariable = PlayerX)
txtPlayerX.grid(row=1,column=1)


l1PlayerO = Label(RightFrame1,font=('arial',20,'bold'), text='Player O:',pady=2,padx=2,bg='Cadet Blue')
l1PlayerO.grid(row=2, column=0)
l1PlayerO = Label(RightFrame1,font=('arial',15,'bold'), text=B,pady=2,padx=2,bg='Cadet Blue')
l1PlayerO.grid(row=3, column=0)
txtPlayerO = Entry(RightFrame1,font=('arial',15,'bold'),relief=RIDGE,textvariable = PlayerO)
txtPlayerO.grid(row=3,column=1)

butRESET = Button(RightFrame2, text='RESET THE ROUND', font=('arial' ,10, 'bold'), height=2, width=16, bg='gainsboro',command=reset)
butRESET.grid(row=0, column=0)

butNEWGAME = Button(RightFrame2, text='START NEW GAME', font=('arial' ,10, 'bold'), height=2, width=16, bg='gainsboro',command=newgame)
butNEWGAME.grid(row=1, column=0)


butQUIT = Button(RightFrame2, text='QUIT THE GAME', font=('arial', 15 ,'bold'), height=2, width=16, bg='gainsboro',command=end)
butQUIT.grid(row=2, column=0)


button1 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button1))
button1.grid(row=1, column=0)

button2 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button2))
button2.grid(row=1, column=1)

button3 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button3))
button3.grid(row=1, column=2)

button4 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button4))
button4.grid(row=2, column=0)

button5 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button5))
button5.grid(row=2, column=1)

button6 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button6))
button6.grid(row=2, column=2)

button7 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button7))
button7.grid(row=3, column=0)

button8 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button8))
button8.grid(row=3, column=1)

button9 = Button(LeftFrame, text='  ', font=('Time 26 bold'), height=3, width=8, bg='gainsboro',command=lambda:check(button9))
button9.grid(row=3, column=2 )



window.mainloop()