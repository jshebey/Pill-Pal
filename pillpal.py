import tkinter as tk
import webbrowser

# Global Variables
medNames = []
dosages  = []
amMed = []
midMed= []
pmMed = []

AM  = "8:00 AM"
Mid = "12:00 PM"
PM  = "8:00 PM"
doseTime = ""

# Function Definition

def loadMedQuestion():
    questionFrame.pack()
    medDataFrame.pack()
    nameLabel.pack()
    nameEntry.pack()
    doseLabel.pack()
    doseEntry.pack()
    scheduleDataFrame.pack()
    amCheckbox.pack()
    midCheckbox.pack()
    pmCheckbox.pack()
    addMedButton.pack(pady= 5)
    moveOnButton.pack()
    return nameEntry, doseEntry

def saveMedData():
    amount = amCheck.get() + midCheck.get() + pmCheck.get()
    if nameEntry.get() == '' or amount == 0 or doseEntry.get() == '' or not doseEntry.get().isnumeric():
        return
    global medNames
    global dosages
    global doseTime
    doseTime = ""
    pills = ''
    medNames += [nameEntry.get()]
    dosages  += [doseEntry.get()]
    amMed.append(amCheck.get())
    midMed.append(midCheck.get())
    pmMed.append(pmCheck.get())
    if int(doseEntry.get()) == 1:
        pills = 'pill'
    else:
        pills = 'pills'
    if amount == 1:
        if amCheck.get():
            doseTime += AM
        if midCheck.get():
            doseTime += Mid
        if pmCheck.get():
            doseTime += PM
    elif amount == 2:
        if amCheck.get():
            doseTime = doseTime + AM + ' and '
        if midCheck.get():
            if amCheck.get():
                doseTime += Mid
            else:    
                doseTime = doseTime + Mid + ' and '
        if pmCheck.get():
            doseTime += PM
    else:
        doseTime += AM + ', ' + Mid + ', and ' + PM
    
    textbox.insert(tk.END, "\nTake " + doseEntry.get() + ' ' + pills + " of " + nameEntry.get() + " at " + doseTime)

def clearEntries():
    nameEntry.delete(0, tk.END)
    doseEntry.delete(0, tk.END)
    amCheck.set(0)
    midCheck.set(0)
    pmCheck.set(0)

def finish():
    questionFrame.destroy()
    medDataFrame.destroy()
    scheduleDataFrame.destroy()
    textbox.destroy()
    addMedButton.destroy()
    title.destroy()
    finishFrame.pack()
    endMessage = tk.Label(finishFrame, text="Finished! Thank you for using PillPal!", bg='#3A3B3C', fg='#1ED760', font=('Arial', 16))
    endMessage.pack(pady=50)
    quit_button = tk.Button(finishFrame, text='Quit', bg='#3A3B3C', fg='#1ED760', font=('Arial', 14), command=quit)
    quit_button.pack()
    secret_button = tk.Button(finishFrame, text='shh', bg='#3A3B3C', fg='#1ED760', font=('Arial', 6), command=secret)
    secret_button.pack(pady=300)

def secret():
    webbrowser.open_new('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
# Initialize App

window = tk.Tk()
photo=tk.PhotoImage(file="PillPalLogo.png")

window.wm_iconphoto(False, photo)

window.geometry('800x900')
window.title('PillPal')
window['background']='#3A3B3C'

questionFrame= tk.Frame(bg='#3A3B3C')
medDataFrame = tk.Frame(questionFrame, bg='#3A3B3C')
scheduleDataFrame = tk.Frame(questionFrame, bg='#3A3B3C')
finishFrame = tk.Frame(bg='#3A3B3C')

title = tk.Label(window, text='Say Hello To Your PillPal', font=('Arial', 20, 'bold'), bg='#3A3B3C', fg='#1ED760')

textbox=tk.Text(bg='#404040', fg='#1ED760', font=('Arial', 12), height=20)

nameLabel= tk.Label(medDataFrame, text="Medication Name", font=('Arial', 14), bg='#3A3B3C', fg='#1ED760')
doseLabel= tk.Label(medDataFrame, text="How many pills per Dose?", font=('Arial', 14), bg='#3A3B3C', fg='#1ED760')

nameEntry = tk.Entry(medDataFrame, font=('Arial', 12), bg='#3A3B3C', fg='#1ED760')
doseEntry = tk.Entry(medDataFrame, font=('Arial', 12), bg='#3A3B3C', fg='#1ED760')

addMedButton = tk.Button(questionFrame, text="Add Medication", command=lambda: [saveMedData(), clearEntries()], bg='#3A3B3C', fg='#1ED760', font=('Arial', 14))
moveOnButton = tk.Button(questionFrame, text="Finish", command=lambda: [saveMedData(), clearEntries(), finish()], bg='#3A3B3C', fg='#1ED760', font=('Arial', 14))

amCheck =tk.IntVar()
midCheck=tk.IntVar()
pmCheck =tk.IntVar()
amCheckbox = tk.Checkbutton(scheduleDataFrame, variable = amCheck, onvalue=1, offvalue=0, text="AM", bg='#3A3B3C', fg='#1ED760', font=('Arial', 12))
midCheckbox = tk.Checkbutton(scheduleDataFrame, variable= midCheck, onvalue=1, offvalue=0, text="Midday", bg='#3A3B3C', fg='#1ED760', font=('Arial', 12))
pmCheckbox = tk.Checkbutton(scheduleDataFrame, variable=pmCheck, onvalue=1, offvalue=0, text="PM", bg='#3A3B3C', fg='#1ED760', font=('Arial', 12))



title.pack(pady=15)
textbox.pack(pady=15)
loadMedQuestion()

window.mainloop()

data={"medNames": medications, "dosages":dose, "schedule":schedule}
 

