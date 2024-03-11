# import tkinter as tk 
# def showselection():
#     selection.set(var1.get())
#     selection2.set(var2.get())
    
# root = tk.Tk()
# var1=tk.BooleanVar()
# var2=tk.BooleanVar()
# selection=tk.StringVar()
# selection2=tk.StringVar()
# check1=tk.Checkbutton(root,text="option1",variable=var1)
# check2=tk.Checkbutton(root,text="option2",variable=var2)
# button=tk.Button(root,text="show selection",command=showselection)
# label1=tk.Label(root,textvariable=selection)
# label2=tk.Label(root,textvariable=selection2)

# check1.pack()
# check2.pack()
# label1.pack()
# label2.pack()
# button.pack()
# root.mainloop()





# import tkinter as tk 
# def showselection():
#     selection1.set(var.get())
#     # selection2.set(var.get())
# root = tk.Tk()
# var=tk.StringVar()
# selection1=tk.StringVar()
# # selection2=tk.StringVar()
# radio1=tk.Radiobutton(root,text="red",variable=var,value="red")
# radio2=tk.Radiobutton(root,text="option2",variable=var,value="option2")
# button=tk.Button(root,text="show selection",command=showselection)
# label1=tk.Label(root,textvariable=selection1)
# # label2=tk.Label(root,textvariable=selection2)
# radio1.pack()
# radio2.pack()
# button.pack()
# label1.pack()
# # label2.pack()
# root.mainloop()


import tkinter as tk 
def show_selection():
    selected=listbox.get(tk.ACTIVE)
    selection.set(selected)
root = tk.Tk()
selection=tk.StringVar()
listbox=tk.Listbox(root)
listbox.insert(1,"item1")
listbox.insert(2,"item2")
listbox.insert(3,"item3")
button=tk.Button(root,text="Showlselection",command=show_selection)
label=tk.Label(root,textvariable=selection)

listbox.pack()
button.pack()
label.pack()
root.mainloop()