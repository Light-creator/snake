from tkinter import *

root = Tk()
entry = Entry(root, width = 35, borderwidth = 5)
entry.grid(column = 0, row = 0, columnspan=3, padx=10, pady=10)


def button_click(number):
	curr = entry.get()
	entry.delete(0, END)
	i = str(curr) + str(number)
	entry.insert(0, i)


def button_clear():
	entry.delete(0, END)


def button_add():
	first_num = entry.get()

	global f_num
	global point

	point = "add"
	f_num = int(first_num)
	entry.delete(0, END)


def button_minus():
	first_num = entry.get()

	global f_num
	global point

	point = "minus"
	f_num = int(first_num)
	entry.delete(0, END)


def button_multiply():
	first_num = entry.get()

	global f_num
	global point

	point = "multiply"
	f_num = int(first_num)
	entry.delete(0, END)


def button_divide():
	first_num = entry.get()

	global f_num
	global point
	
	point = "divide"
	f_num = int(first_num)
	entry.delete(0, END)


def button_equal():
	second_number = entry.get()
	s_num = int(second_number)
	entry.delete(0, END)

	if point == "add":
		entry.insert(0, f_num + s_num)
	elif point == "multiply":
		entry.insert(0, f_num * s_num)
	elif point == "minus":
		entry.insert(0, f_num - s_num)
	else:
		entry.insert(0, f_num / s_num)

root.geometry("390x500")
b1 = Button(root, text = " 1 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(1)).grid( row = 2, column = 1)
b2 = Button(root, text = " 2 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(2)).grid(row = 2, column = 2)
b3 = Button(root, text = " 3 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(3)).grid(row = 2, column = 3)
b4 = Button(root, text = " 4 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(4)).grid(row = 3, column = 1)
b5 = Button(root, text = " 5 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(5)).grid(row = 3, column = 2)
b6 = Button(root, text = " 6 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(6)).grid(row = 3, column = 3)
b7 = Button(root, text = " 7 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(7)).grid(row = 4, column = 1)
b8 = Button(root, text = " 8 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(8)).grid(row = 4, column = 2)
b9 = Button(root, text = " 9 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(9)).grid(row = 4, column = 3)
b0 = Button(root, text = " 0 ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_click(0)).grid(row = 5, column = 2)
badd = Button(root, text = " + ", width = 20, height = 3, bg = "grey", fg = "black", command =button_add).grid(row = 6, column = 1)
bequal = Button(root, text = " = ", width = 20, height = 3, bg = "grey", fg = "black", command =  button_equal).grid(row = 6, column = 2)
bclear = Button(root, text = " C ", width = 20, height = 3, bg = "grey", fg = "black", command = lambda: button_clear()).grid(row = 6, column = 3)
bminus = Button(root, text = " - ", width = 20, height = 3, bg = "grey", fg = "black", command =  button_minus).grid(row = 7, column = 1)
bmult = Button(root, text = " * ", width = 20, height = 3, bg = "grey", fg = "black", command =  button_multiply).grid(row = 7, column = 2)
bdevide = Button(root, text = " / ", width = 20, height = 3, bg = "grey", fg = "black", command = button_divide).grid(row = 7, column = 3)
root.mainloop()
