### 🔽🔽🔽INFO🔽🔽🔽 ###
# File name: GuessTheNumber.py
# Author: Thomas Crick, Abid Chowdhury
# Date created: 30/07/2021
# Last modified: 30/07/2021
# Python version: 3.9.0

from tkinter import *
from random import randint

EASYMODE = '#2ECC71'
EASYMODEDARK = '#24C267'
MEDIUMMODE = '#F4D03F'
MEDIUMMODEDARK = '#EAC635'
HARDMODE = '#E67E22'
HARDMODEDARK = '#DC7418'
INSANEMODE = '#E74C3C'
INSANEMODEDARK = '#DD4232'
GODMODE = '#A93226'
GODMODEDARK = '#9F281C'
ICON = 'WindowIcon.ico'

mainWindow = Tk()
mainWindow.title('Number Guesser')
mainWindow.config(bg='black')
mainWindow.iconbitmap(ICON)

title = Label(mainWindow, font=('LEIXO DEMO', 35, 'bold'), text='NUMBER GUESSER', bg='black', fg='white')
title.grid(column=0, row=0, columnspan=2)

# 🔽🔽🔽EASY MODE🔽🔽🔽 #
def easyMode():
    global number
    global lowestGuess
    global highestGuess

    mainWindow.withdraw()

    easyModeWindow = Tk()
    easyModeWindow.title('Number Guesser - Easy Mode')
    easyModeWindow.config(bg=EASYMODE)
    easyModeWindow.iconbitmap(ICON)

    # 🔽RANDOM NUMBER🔽 #
    number = randint(1, 100)

    # 🔽CHECK IF WIN🔽 #
    def checkIfWin():
        global lowestGuess
        global highestGuess
        guess = int(inp.get())

        if guess > number:
            tooHighLowLabel.config(text='TOO HIGH')
            tooHighLowLabel.grid(column=1, row=2)
            if highestGuess > guess:
                highestGuess = guess
                highestGuessLabel2.config(text=highestGuess)
                highestGuessLabel2.grid(column=2, row=2)

        elif guess < number:
            tooHighLowLabel.config(text='TOO LOW')
            tooHighLowLabel.grid(column=1, row=2)
            if lowestGuess < guess:
                lowestGuess = guess
                lowestGuessLabel2.config(text=lowestGuess)
                lowestGuessLabel2.grid(column=0, row=2)

        elif guess == number:
            tooHighLowLabel.config(text='CORRECT')
            tooHighLowLabel.grid(column=1, row=2)

        inp.delete(0, END)

    # 🔽INPUT🔽 #
    inp = Entry(easyModeWindow, font=('Arial', 30, 'bold'),
                bd=0, justify='center')
    inp.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

    # 🔽RESTART🔽 #
    def restart():
        global number
        global highestGuess
        global lowestGuess
        number = randint(1, 100)

        lowestGuess = 0
        lowestGuessLabel2.config(text='None')
        lowestGuessLabel2.grid(column=0, row=2)

        highestGuess = 100
        highestGuessLabel2.config(text='None')
        highestGuessLabel2.grid(column=2, row=2)

    restartButton = Button(easyModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='RESTART', relief=SUNKEN, bg=EASYMODEDARK, activebackground=EASYMODEDARK, bd=0, command=lambda: restart())
    restartButton.grid(column=0, row=3)

    # 🔽GO BACK🔽 #
    def goBack():
        easyModeWindow.withdraw()
        mainWindow.deiconify()

    goBackButton = Button(easyModeWindow, font=('LEIXO DEMO', 20, 'bold'),
                          text='GO BACK', bg=EASYMODEDARK, relief=SUNKEN, activebackground=EASYMODEDARK,bd=0, command=lambda: goBack())
    goBackButton.grid(column=2, row=3)

    # 🔽SUBMIT BUTTON🔽 #
    submitButton = Button(easyModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='SUBMIT', bg=EASYMODEDARK, relief=SUNKEN, activebackground=EASYMODEDARK,bd=0, command=lambda: checkIfWin())
    submitButton.grid(column=1, row=1)

    # 🔽LOWEST GUESS🔽 #
    lowestGuess = 0

    lowestGuessLabel = Label(easyModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                             text='Lowest\nGuess', bg=EASYMODEDARK)
    lowestGuessLabel.grid(column=0, row=1)

    lowestGuessLabel2 = Label(easyModeWindow, font=('Arial', 30, 'bold'),
                              text='None', bg=EASYMODEDARK)
    lowestGuessLabel2.grid(column=0, row=2)

    # 🔽HIGHEST GUESS🔽 #
    highestGuess = 100
    highestGuessLabel = Label(easyModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                              text='Highest\nGuess', bg=EASYMODEDARK)
    highestGuessLabel.grid(column=2, row=1)

    highestGuessLabel2 = Label(easyModeWindow, font=('Arial', 30, 'bold'),
                               text='None', bg=EASYMODEDARK)
    highestGuessLabel2.grid(column=2, row=2)

    # 🔽TOO HIGH/ TOO LOW🔽 #
    tooHighLowLabel = Label(easyModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='', bg=EASYMODEDARK)
    tooHighLowLabel.grid(column=1, row=2)

    easyModeWindow.mainloop()

# 🔽🔽🔽MEDIUM MODE🔽🔽🔽 #
def mediumMode():
    
    global number
    global lowestGuess
    global highestGuess

    mainWindow.withdraw()

    mediumModeWindow = Tk()
    mediumModeWindow.title('Number Guesser - Medium Mode')
    mediumModeWindow.config(bg=MEDIUMMODE)
    mediumModeWindow.iconbitmap(ICON)

    # 🔽RANDOM NUMBER🔽 #
    number = randint(1, 1000)

    # 🔽CHECK IF WIN🔽 #
    def checkIfWin():
        global lowestGuess
        global highestGuess
        guess = int(inp.get())

        if guess > number:
            tooHighLowLabel.config(text='TOO HIGH')
            tooHighLowLabel.grid(column=1, row=2)
            if highestGuess > guess:
                highestGuess = guess
                highestGuessLabel2.config(text=highestGuess)
                highestGuessLabel2.grid(column=2, row=2)

        elif guess < number:
            tooHighLowLabel.config(text='TOO LOW')
            tooHighLowLabel.grid(column=1, row=2)
            if lowestGuess < guess:
                lowestGuess = guess
                lowestGuessLabel2.config(text=lowestGuess)
                lowestGuessLabel2.grid(column=0, row=2)

        elif guess == number:
            tooHighLowLabel.config(text='CORRECT')
            tooHighLowLabel.grid(column=1, row=2)

        inp.delete(0, END)

    # 🔽INPUT🔽 #
    inp = Entry(mediumModeWindow, font=('Arial', 30, 'bold'),
                bd=0, justify='center')
    inp.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

    # 🔽RESTART🔽 #
    def restart():
        global number
        global highestGuess
        global lowestGuess
        number = randint(1, 1000)

        lowestGuess = 0
        lowestGuessLabel2.config(text='None')
        lowestGuessLabel2.grid(column=0, row=2)

        highestGuess = 1000
        highestGuessLabel2.config(text='None')
        highestGuessLabel2.grid(column=2, row=2)

    restartButton = Button(mediumModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='RESTART', bg=MEDIUMMODEDARK, activebackground=MEDIUMMODEDARK,relief=SUNKEN, bd=0, command=lambda: restart())
    restartButton.grid(column=0, row=3)

    # 🔽GO BACK🔽 #
    def goBack():
        mediumModeWindow.withdraw()
        mainWindow.deiconify()

    goBackButton = Button(mediumModeWindow, font=('LEIXO DEMO', 20, 'bold'),
                          text='GO BACK', bg=MEDIUMMODEDARK, relief=SUNKEN,activebackground=MEDIUMMODEDARK, bd=0, command=lambda: goBack())
    goBackButton.grid(column=2, row=3)

    # 🔽SUBMIT BUTTON🔽 #
    submitButton = Button(mediumModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='SUBMIT', bg=MEDIUMMODEDARK, activebackground=MEDIUMMODEDARK, relief=SUNKEN,bd=0, command=lambda: checkIfWin())
    submitButton.grid(column=1, row=1)

    # 🔽LOWEST GUESS🔽 #
    lowestGuess = 0

    lowestGuessLabel = Label(mediumModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                             text='Lowest\nGuess', bg=MEDIUMMODEDARK)
    lowestGuessLabel.grid(column=0, row=1)

    lowestGuessLabel2 = Label(mediumModeWindow, font=('Arial', 30, 'bold'),
                              text='None', bg=MEDIUMMODEDARK)
    lowestGuessLabel2.grid(column=0, row=2)

    # 🔽HIGHEST GUESS🔽 #
    highestGuess = 1000
    highestGuessLabel = Label(mediumModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                              text='Highest\nGuess', bg=MEDIUMMODEDARK)
    highestGuessLabel.grid(column=2, row=1)

    highestGuessLabel2 = Label(mediumModeWindow, font=('Arial', 30, 'bold'),
                               text='None', bg=MEDIUMMODEDARK)
    highestGuessLabel2.grid(column=2, row=2)

    # 🔽TOO HIGH/ TOO LOW🔽 #
    tooHighLowLabel = Label(mediumModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='', bg=MEDIUMMODEDARK)
    tooHighLowLabel.grid(column=1, row=2)

    mediumModeWindow.mainloop()

# 🔽🔽🔽HARD MODE🔽🔽🔽 #
def hardMode():
    global number
    global lowestGuess
    global highestGuess

    mainWindow.withdraw()

    hardModeWindow = Tk()
    hardModeWindow.title('Number Guesser - Hard Mode')
    hardModeWindow.config(bg=HARDMODE)
    hardModeWindow.iconbitmap(ICON)

    # 🔽RANDOM NUMBER🔽 #
    number = randint(1, 10000)

    # 🔽CHECK IF WIN🔽 #
    def checkIfWin():
        global lowestGuess
        global highestGuess
        guess = int(inp.get())

        if guess > number:
            tooHighLowLabel.config(text='TOO HIGH')
            tooHighLowLabel.grid(column=1, row=2)
            if highestGuess > guess:
                highestGuess = guess
                highestGuessLabel2.config(text=highestGuess)
                highestGuessLabel2.grid(column=2, row=2)

        elif guess < number:
            tooHighLowLabel.config(text='TOO LOW')
            tooHighLowLabel.grid(column=1, row=2)
            if lowestGuess < guess:
                lowestGuess = guess
                lowestGuessLabel2.config(text=lowestGuess)
                lowestGuessLabel2.grid(column=0, row=2)

        elif guess == number:
            tooHighLowLabel.config(text='CORRECT')
            tooHighLowLabel.grid(column=1, row=2)

        inp.delete(0, END)

    # 🔽INPUT🔽 #
    inp = Entry(hardModeWindow, font=('Arial', 30, 'bold'),
                bd=0, justify='center')
    inp.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

    # 🔽RESTART🔽 #
    def restart():
        global number
        global highestGuess
        global lowestGuess
        number = randint(1, 10000)

        lowestGuess = 0
        lowestGuessLabel2.config(text='None')
        lowestGuessLabel2.grid(column=0, row=2)

        highestGuess = 10000
        highestGuessLabel2.config(text='None')
        highestGuessLabel2.grid(column=2, row=2)

    restartButton = Button(hardModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='RESTART', activebackground=HARDMODEDARK,relief=SUNKEN, bg=HARDMODEDARK, bd=0, command=lambda: restart())
    restartButton.grid(column=0, row=3)

    # 🔽GO BACK🔽 #
    def goBack():
        hardModeWindow.withdraw()
        mainWindow.deiconify()

    goBackButton = Button(hardModeWindow, font=('LEIXO DEMO', 20, 'bold'),
                          text='GO BACK', bg=HARDMODEDARK,  activebackground=HARDMODEDARK,relief=SUNKEN, bd=0, command=lambda: goBack())
    goBackButton.grid(column=2, row=3)

    # 🔽SUBMIT BUTTON🔽 #
    submitButton = Button(hardModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='SUBMIT', relief=SUNKEN,activebackground=HARDMODEDARK, bg=HARDMODEDARK, bd=0, command=lambda: checkIfWin())
    submitButton.grid(column=1, row=1)

    # 🔽LOWEST GUESS🔽 #
    lowestGuess = 0

    lowestGuessLabel = Label(hardModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                             text='Lowest\nGuess', bg=HARDMODEDARK)
    lowestGuessLabel.grid(column=0, row=1)

    lowestGuessLabel2 = Label(hardModeWindow, font=('Arial', 30, 'bold'),
                              text='None', bg=HARDMODEDARK)
    lowestGuessLabel2.grid(column=0, row=2)

    # 🔽HIGHEST GUESS🔽 #
    highestGuess = 10000
    highestGuessLabel = Label(hardModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                              text='Highest\nGuess', bg=HARDMODEDARK)
    highestGuessLabel.grid(column=2, row=1)

    highestGuessLabel2 = Label(hardModeWindow, font=('Arial', 30, 'bold'),
                               text='None', bg=HARDMODEDARK)
    highestGuessLabel2.grid(column=2, row=2)

    # 🔽TOO HIGH/ TOO LOW🔽 #
    tooHighLowLabel = Label(hardModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='', bg=HARDMODEDARK)
    tooHighLowLabel.grid(column=1, row=2)

    hardModeWindow.mainloop()

# 🔽🔽🔽INSANE MODE🔽🔽🔽 #
def insaneMode():
    global number
    global lowestGuess
    global highestGuess

    mainWindow.withdraw()

    insaneModeWindow = Tk()
    insaneModeWindow.title('Number Guesser - Insane Mode')
    insaneModeWindow.config(bg=INSANEMODE)
    insaneModeWindow.iconbitmap(ICON)

    # 🔽RANDOM NUMBER🔽 #
    number = randint(1, 100000)

    # 🔽CHECK IF WIN🔽 #
    def checkIfWin():
        global lowestGuess
        global highestGuess
        guess = int(inp.get())

        if guess > number:
            tooHighLowLabel.config(text='TOO HIGH')
            tooHighLowLabel.grid(column=1, row=2)
            if highestGuess > guess:
                highestGuess = guess
                highestGuessLabel2.config(text=highestGuess)
                highestGuessLabel2.grid(column=2, row=2)

        elif guess < number:
            tooHighLowLabel.config(text='TOO LOW')
            tooHighLowLabel.grid(column=1, row=2)
            if lowestGuess < guess:
                lowestGuess = guess
                lowestGuessLabel2.config(text=lowestGuess)
                lowestGuessLabel2.grid(column=0, row=2)

        elif guess == number:
            tooHighLowLabel.config(text='CORRECT')
            tooHighLowLabel.grid(column=1, row=2)

        inp.delete(0, END)

    # 🔽INPUT🔽 #
    inp = Entry(insaneModeWindow, font=('Arial', 30, 'bold'),
                bd=0, justify='center')
    inp.grid(column=0, row=0, columnspan=3, padx=5, pady=5)

    # 🔽RESTART🔽 #
    def restart():
        global number
        global highestGuess
        global lowestGuess
        number = randint(1, 100000)

        lowestGuess = 0
        lowestGuessLabel2.config(text='None')
        lowestGuessLabel2.grid(column=0, row=2)

        highestGuess = 100000
        highestGuessLabel2.config(text='None')
        highestGuessLabel2.grid(column=2, row=2)

    restartButton = Button(insaneModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='RESTART', relief=SUNKEN, activebackground=INSANEMODEDARK, bg=INSANEMODEDARK, bd=0, command=lambda: restart())
    restartButton.grid(column=0, row=3)

    # 🔽GO BACK🔽 #
    def goBack():
        insaneModeWindow.withdraw()
        mainWindow.deiconify()

    goBackButton = Button(insaneModeWindow, font=('LEIXO DEMO', 20, 'bold'),
                          text='GO BACK', relief=SUNKEN, bg=INSANEMODEDARK,activebackground=INSANEMODEDARK,  bd=0, command=lambda: goBack())
    goBackButton.grid(column=2, row=3)

    # 🔽SUBMIT BUTTON🔽 #
    submitButton = Button(insaneModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='SUBMIT', relief=SUNKEN, bg=INSANEMODEDARK, activebackground=INSANEMODEDARK, bd=0, command=lambda: checkIfWin())
    submitButton.grid(column=1, row=1)

    # 🔽LOWEST GUESS🔽 #
    lowestGuess = 0

    lowestGuessLabel = Label(insaneModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                             text='Lowest\nGuess', bg=INSANEMODEDARK)
    lowestGuessLabel.grid(column=0, row=1)

    lowestGuessLabel2 = Label(insaneModeWindow, font=('Arial', 30, 'bold'),
                              text='None', bg=INSANEMODEDARK)
    lowestGuessLabel2.grid(column=0, row=2)

    # 🔽HIGHEST GUESS🔽 #
    highestGuess = 100000
    highestGuessLabel = Label(insaneModeWindow, font=('LEIXO DEMO', 15, 'bold'),
                              text='Highest\nGuess', bg=INSANEMODEDARK)
    highestGuessLabel.grid(column=2, row=1)

    highestGuessLabel2 = Label(insaneModeWindow, font=('Arial', 30, 'bold'),
                               text='None', bg=INSANEMODEDARK)
    highestGuessLabel2.grid(column=2, row=2)

    # 🔽TOO HIGH/ TOO LOW🔽 #
    tooHighLowLabel = Label(insaneModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='', bg=INSANEMODEDARK)
    tooHighLowLabel.grid(column=1, row=2)

    insaneModeWindow.mainloop()

# 🔽🔽🔽GOD MODE🔽🔽🔽 #
def godMode():
    mainWindow.withdraw()

    godModeWindow = Tk()
    godModeWindow.title('Number Guesser - GOD Mode')
    godModeWindow.config(bg=GODMODE)
    godModeWindow.iconbitmap(ICON)

    # 🔽RANDOM NUMBER🔽 #
    number = randint(1,1000000)
    
    # 🔽CHECK IF WIN🔽 #
    def checkIfWin():
        def announceWin():
            godModeWindow.withdraw()
            
            winWindow = Tk()
            winWindow.title('Number Guesser - WIN')
            winWindow.config(bg='#0f0')
            winWindow.iconbitmap(ICON)
            
            winLabel = Label(winWindow,font=('LEIXO DEMO',50,'bold'),text='YOU WIN!',bg='#0f0')
            winLabel.grid(column=0,row=0)
            
            # 🔽MAIN MENU🔽 #
            def mainMenu():
                winWindow.withdraw()
                mainWindow.deiconify()
            
            mainMenuButton = Button(winWindow, relief=SUNKEN,bg='#00fe00', activebackground='#00fe00',font=('LEIXO DEMO', 20, 'bold'),
                          text='Main Menu',bd=0, command=lambda: mainMenu())
            mainMenuButton.grid(column=0,row=1)
            winWindow.mainloop()
        def announceLose():
            godModeWindow.withdraw()
            
            loseWindow = Tk()
            loseWindow.title('Number Guesser - LOSE')
            loseWindow.config(bg='#f00')
            loseWindow.iconbitmap(ICON)
            
            loseLabel = Label(loseWindow,font=('LEIXO DEMO',50,'bold'),text='YOU LOSE!',bg='#f00')
            loseLabel.grid(column=0,row=0)
            
            # 🔽MAIN MENU🔽 #
            def mainMenu():
                loseWindow.withdraw()
                mainWindow.deiconify()
            
            mainMenuButton = Button(loseWindow,  relief=SUNKEN, font=('LEIXO DEMO', 20, 'bold'),
                          text='Main Menu', bg='#fe0000',activebackground='#fe0000', bd=0, command=lambda: mainMenu())
            mainMenuButton.grid(column=0,row=1)
            
            loseWindow.mainloop()

        guess = int(inp.get())
        
        if guess == number:
            announceWin()
        else:
            announceLose()
            
    # 🔽INPUT🔽 #
    inp = Entry(godModeWindow, font=('Arial', 30, 'bold'),
                bd=0, justify='center')
    inp.grid(column=0, row=0, columnspan=3, padx=5, pady=5)
    
    # 🔽RESTART🔽 #
    def restart():
        global number
        number = randint(1, 100000)

    restartButton = Button(godModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='RESTART',  activebackground=GODMODEDARK,relief=SUNKEN, bg=GODMODEDARK, bd=0, command=lambda: restart())
    restartButton.grid(column=0, row=3)
    
    # 🔽GO BACK🔽 #
    def goBack():
        godModeWindow.withdraw()
        mainWindow.deiconify()

    goBackButton = Button(godModeWindow, font=('LEIXO DEMO', 20, 'bold'),
                          text='GO BACK',  relief=SUNKEN,activebackground=GODMODEDARK, bg=GODMODEDARK, bd=0, command=lambda: goBack())
    goBackButton.grid(column=2, row=3)
    
    # 🔽SUBMIT BUTTON🔽 #
    submitButton = Button(godModeWindow, font=(
        'LEIXO DEMO', 20, 'bold'), text='SUBMIT', activebackground=GODMODEDARK, relief=SUNKEN, bg=GODMODEDARK, bd=0, command=lambda: checkIfWin())
    submitButton.grid(column=1, row=1)

    godModeWindow.mainloop()

# 🔽🔽🔽MODE BUTTONS🔽🔽🔽 #
easyModeButton = Button(text='Easy\n1-100', fg=EASYMODE, activeforeground=EASYMODE, command=lambda: easyMode())
easyModeButton.grid(column=0, row=1)

mediumModeButton = Button(text='Medium\n1-1k', fg=MEDIUMMODE, activeforeground=MEDIUMMODE, command=lambda: mediumMode())
mediumModeButton.grid(column=1, row=1)

hardModeButton = Button(text='Hard\n1-10k', fg=HARDMODE, activeforeground=HARDMODE, command=lambda: hardMode())
hardModeButton.grid(column=0, row=2)

insaneModeButton = Button(text='Insane\n1-100k', fg=INSANEMODE, activeforeground=INSANEMODE, command=lambda: insaneMode())
insaneModeButton.grid(column=1, row=2)

godModeButton = Button(text='God\n1-1m', fg=GODMODE, activeforeground=GODMODE, command=lambda:godMode())
godModeButton.grid(column=0, row=3, columnspan=2)

modeButtons = [easyModeButton, mediumModeButton, hardModeButton, insaneModeButton, godModeButton]

for b in modeButtons:
    b.config(font=('LEIXO DEMO', 20, 'bold'), bg='black', activebackground='black', relief=SUNKEN, bd=0)

mainWindow.mainloop()
