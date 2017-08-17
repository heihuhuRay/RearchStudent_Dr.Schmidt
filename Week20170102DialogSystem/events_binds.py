# #!/usr/bin/python3
# # write tkinter as Tkinter to be Python 2.x compatible
# from Tkinter import *
# def hello(event):
#     print("Single Click, Button-l") 
# def quit(event):                           
#     print("Double Click, so let's stop") 
#     import sys; sys.exit() 

# widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', hello)
# widget.bind('<Double-1>', quit) 
# widget.mainloop()

dialog_dic = {
				 0 : [1],
				 1 : [2,3],
				 2 : [3],
				 3 : [4, 5, 6],
				 4 : [7],
				 5 : [7],
				 6 : [8],
				 7 : [8],
			   
			   }

print(dialog_dic[3])