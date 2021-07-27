import tkinter

root = tkinter.Tk()
root.title("Compound Interest")

# Create function(s)
def calculate_FP() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    FP = (round((1+i)**n, 3)*u)
    label_result['text'] = f'{FP}'

def calculate_PF() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    PF = (round(1/((1+i)**n), 4)*u)
    label_result['text'] = f'{PF}'

def calculate_FA() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    FA = (round((((1+i)**n)-1)/i, 3)*u)
    label_result['text'] = f'{FA}'

def calculate_AF() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    AF = (round(i/(((1+i)**n)-1), 4)*u)
    label_result['text'] = f'{AF}'

def calculate_PA() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    PA = (round((((1+i)**n)-1)/(i*((1+i)**n)), 3)*u)
    label_result['text'] = f'{PA}'

def calculate_AP() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    AP = (round((i*((1+i)**n))/(((1+i)**n)-1), 4)*u)
    label_result['text'] = f'{AP}'

def calculate_PG() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    PG = (round((((1+i)**n)-(1+n*i))/((i**2)*((1+i)**n)), 3)*u)
    label_result['text'] = f'{PG}'

def calculate_AG() :
    i = float(entry_i.get())
    n = int(entry_n.get())
    u = float(entry_u.get())
    i /= 100
    AG = (round((1/i)-(n/(((1+i)**n)-1)), 3)*u)
    label_result['text'] = f'{AG}'

# Create GUI
label_i = tkinter.Label(root, text="INTEREST : ")
label_i.grid(column=0, row=0)

entry_i = tkinter.Entry(root)
entry_i.grid(column=1, row=0)

label_n = tkinter.Label(root, text="PERIOD : ")
label_n.grid(column=0, row=1)

entry_n = tkinter.Entry(root)
entry_n.grid(column=1, row=1)

label_u = tkinter.Label(root, text="UNIT : ")
label_u.grid(column=0, row=2)

entry_u = tkinter.Entry(root)
entry_u.grid(column=1, row=2)

FP_cal = tkinter.Button(root, text="F/P", command=calculate_FP)
FP_cal.grid(column=2, row=0)

PF_cal = tkinter.Button(root, text="P/F", command=calculate_PF)
PF_cal.grid(column=3, row=0)

FA_cal = tkinter.Button(root, text="F/A", command=calculate_FA)
FA_cal.grid(column=2, row=1)

AF_cal = tkinter.Button(root, text="A/F", command=calculate_AF)
AF_cal.grid(column=3, row=1)

PA_cal = tkinter.Button(root, text="P/A", command=calculate_PA)
PA_cal.grid(column=2, row=2)

AP_cal = tkinter.Button(root, text="A/P", command=calculate_AP)
AP_cal.grid(column=3, row=2)

PG_cal = tkinter.Button(root, text="P/G", command=calculate_PG)
PG_cal.grid(column=2, row=3)

AG_cal = tkinter.Button(root, text="A/G", command=calculate_AG)
AG_cal.grid(column=3, row=3)

result = tkinter.Label(root, text="RESULT :")
result.grid(column=0, row=3)

label_result = tkinter.Label(root, text="")
label_result.grid(column=1, row=3)

root.mainloop()