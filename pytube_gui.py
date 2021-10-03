import tkinter as tk
from pytube import YouTube

def download():
    print("Hello World")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.urllabel = tk.Label(root, text='URL')
        self.urllabel.pack(side='top')
        self.urlwidget = tk.Text(root, height=2)
        self.urlwidget.pack(side='top')

        self.download = tk.Button(self, text="Download", fg="blue", command=download)
        # self.download.pack(side='bottom')
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
root.title("Pytube")
root.geometry("300x300")

app = Application(master=root)
app.mainloop()
