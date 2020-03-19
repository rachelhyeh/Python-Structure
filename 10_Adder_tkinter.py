# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:31:11 2020

@author: rache
"""

import tkinter
import tkinter.messagebox


def main():
    count=0
    
    '''flag = True
    def change_label_text():
        
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)
    '''    
    
    def add_one():
        nonlocal count
        count += 1
        if count %2 == 0:
            color, msg = ('red', str(count))
        else:
            color, msg = ('blue', str(count))
        label.config(text=msg, fg=color)
        
    def add_two():
        nonlocal count
        count += 2
        if count %2 == 0:
            color, msg = ('red', str(count))
        else:
            color, msg = ('blue', str(count))
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Reminder', 'Ready to quite?'):
            '''top.quit()'''
            top.destroy()

    # Create top window
    top = tkinter.Tk()
    # Set window's size
    top.geometry('520x240')
    # Set window's title
    top.title('Simple Adder')
    # Create label objects and add to top window
    label = tkinter.Label(top, text='Here is a simple adder. Odd number is display in blue and even number is display in red.', font='Arial -32', fg='red')
    label.pack(expand=1)
    # Create a fram for buttoms
    panel = tkinter.Frame(top)
    # Create the buttom objects to frame and use 'command' to call define function
    button1 = tkinter.Button(panel, text='Add one', command=add_one)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='Add two', command=add_two)
    button2.pack(side='left')
    button3 = tkinter.Button(panel, text='Exist', command=confirm_to_quit)
    button3.pack(side='right')
    panel.pack(side='bottom')
    # Get into main loop
    tkinter.mainloop()


if __name__ == '__main__':
    main()