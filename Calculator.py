import tkinter as tk

layout = tk.Tk()
layout.title('계산기')

entry = tk.Entry(layout, width=30)
entry.grid(column = 0, row = 0, columnspan = 4, ipady = 20)

layoutIndex = [
    ["1","2","3","4"],
    ["5","6","7","8"],
    ["9","2","3","4"]
]

for i, layerDetail in enumerate(layoutIndex):
    for k, value in enumerate(layerDetail):
        button = tk.Button(layout, 
            text = value, 
            width = 10, 
            height = 3,
            bg = 'gray',
            fg = 'black'
        )
        button.grid(column = k, row = (i + 1))


layout.mainloop()