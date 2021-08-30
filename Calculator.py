import tkinter as tk

layout = tk.Tk()
layout.title('계산기')

entry = tk.Entry(layout, width=30)
entry.grid(column = 0, row = 0, columnspan = 4, ipady = 20)

button = tk.Button(layout, 
    text = 1, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 0, row = 1)
button = tk.Button(layout, 
    text = 2, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 1, row = 1)
button = tk.Button(layout, 
    text = 3, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 2, row = 1)
button = tk.Button(layout, 
    text = 4, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 3, row = 1)


button = tk.Button(layout, 
    text = 5, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 0, row=2)
button = tk.Button(layout, 
    text = 6, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 1, row=2)
button = tk.Button(layout, 
    text = 7, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 2, row=2)
button = tk.Button(layout, 
    text = 8, 
    width = 5, 
    height = 2,
    bg = 'gray',
    fg = 'black'
)
button.grid(column = 3, row=2)


layout.mainloop()