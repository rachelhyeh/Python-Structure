# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:18:04 2020

@author: rache
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread



def main():
        
    # Download function without using Thread
    """
    def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('Caution!', 'Finish download!')
    """
    
    """
    class DownloadTaskHandler(Thread):
        def run(self):
            if tkinter.messagebox.askquestion('Process', 'Ready to download?') == 'yes':
                time.sleep(10)
                tkinter.messagebox.showinfo('Caution!', 'Finish download!')
                # Enable the buttom1
                button1.config(state=tkinter.NORMAL)
            else:
                tkinter.messagebox.showinfo('Caution!', 'Cancel download!')
    def download():
        # Disable the buttom1
        button1.config(state=tkinter.DISABLED)
        # Set 'daemon thread' as true (Main process exists)
        # Proces the download in thread
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'Download: sleeping for 10 seconds.')
    """
    
    
    class DownloadTaskHandler(Thread):
        def run(self):
            clear = 0
            if tkinter.messagebox.askquestion('Process', 'Ready to download?') == 'yes':
                while clear<4:
                    time.sleep(3)
                    tkinter.messagebox.showinfo('Caution!', 'Finish one of them!')
                    clear += 1
                    # Enable the buttom1
                tkinter.messagebox.showinfo('Caution!', 'All of them are cleaned!')
                button1.config(state=tkinter.NORMAL)
            else:
                tkinter.messagebox.showinfo('Caution!', 'Cancel process!')
    def download():
        # Disable the buttom1
        button1.config(state=tkinter.DISABLED)
        # Set 'daemon thread' as true (Main process exists)
        # Proces the download in thread
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('About', 'Cleaning by Rachel Yeh')
    
    
    top = tkinter.Tk()
    top.title('MultiThreading')
    top.geometry('600x250')
    top.wm_attributes('-topmost', True)
    label = tkinter.Label(top, text='Cleaning the House: Livingroom, Kitchen, Bedroom, Bathroom.', font='Arial -20', fg='blue')
    label.pack(expand=True, fill=tkinter.BOTH)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='Cleaning', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='About', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()



if __name__ == '__main__':
    main()