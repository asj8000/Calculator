import tkinter as tk

def clickFunc(value):
    if value.isdigit():
        enterCommand(value)
    else:
        enterNumber(value)

def enterCommand(value):
    print(value)

def enterNumber(value):
    print(value)





layout = tk.Tk()
layout.title('계산기')

entryaa = tk.Entry(layout, width=30, state="disable")
entryaa.grid( columnspan = 4, ipady = 10, ipadx=30)
inputEntry = tk.Entry(layout, width=30)
inputEntry.grid( columnspan = 4, ipady = 10, ipadx=30)

layoutIndex = [
    ["%","CE","C","<-"],
    ["1/x","x2","2/x","/"],
    ["7","8","9","x"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["+/-","0",".","="]
]

for i, layerDetail in enumerate(layoutIndex):
    for k, value in enumerate(layerDetail):
        button = tk.Button(layout, 
            text = value, 
            width = 10,      
            height = 3,
            bg = 'white',   
            fg = 'black',
            command = lambda 
            val = value: clickFunc(val)
        )
        button.grid(column = k, row = (i + 2))
layout.mainloop()