"""
helps you to keep track of your routine
"""
from tkinter import Menu, Button, Toplevel, Tk, simpledialog, messagebox as msg, StringVar, OptionMenu, END, Entry
import os 
import csv
import pandas as pd
class Routine_Creator():
    """ Routine Creator Class"""
    def __init__(self, master):
        self.master = master
        self.master.title("Routine Creator")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        if not os.path.exists("Routine"):
            os.mkdir("Routine")
            os.chdir("Routine")
        else:
            os.chdir("Routine")
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Create Routine", accelerator='Ctrl+O', command=self.creater)
        self.file_menu.add_command(label="Load Routine", accelerator='Ctrl+L', command=self.loadf)
        self.file_menu.add_command(label="Delete Routine", accelerator='Ctrl+D', command=self.delf)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Alt+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())
        self.master.bind('<Control-o>', lambda event: self.creater())
        self.master.bind('<Control-l>', lambda event: self.loadf())
        self.master.bind('<Control-d>', lambda event: self.delf())
        
        self.createb = Button(self.master, text="CREATE A ROUTINE", command=self.creater)
        self.createb.pack()
        
        self.loadb = Button(self.master, text="LOAD A ROUTINE", command=self.loadf)
        self.loadb.pack()
        
        self.deleteb = Button(self.master, text="DELETE A ROUTINE", command=self.delf)
        self.deleteb.pack()

    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    
    def helpmenu(self):
        msg.showinfo("Help", "This is the main menu")
    
    def aboutmenu(self):
        msg.showinfo("About", "About \nVersion 1.0")
    def check_routine_existence(self):
        flagexists = 0
        global createrou
        createrou = simpledialog.askstring("NEW ROUTINE", "Enter the name of the new routine", parent=self.master)
        while createrou == None:
            createrou = simpledialog.askstring("NEW ROUTINE", "Enter the name of the new routine", parent=self.master)
        if not os.path.exists(str(createrou)+str(".csv")):
            with open(str(createrou)+str(".csv"), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['TO DO'])
            msg.showinfo("SUCCESS", "ROUTINE SUCCESSFULLY CREATED")
        else:
            flagexists = 1
            msg.showerror("Error", "This routine exists")
        return flagexists
    
    def creater(self):
        flagexists = self.check_routine_existence()
        while flagexists == 1:
            createrou = simpledialog.askstring("NEW ROUTINE", "Enter the name of the new routine", parent=self.master)
            while createrou == None:
                createrou = simpledialog.askstring("NEW ROUTINE", "Enter the name of the new routine", parent=self.master)
            if not os.path.exists(createrou+str(".csv")):
                with open(str(createrou)+str(".csv"), 'a+') as d:
                    thewriter = csv.writer(d)
                    thewriter.writerow(['TO DO'])
                flagexists = 0
        root1 = Toplevel()
        Createl(root1)
    def loadf(self):
        root2 = Toplevel()
        Loadlist(root2)
    def delf(self):
        root3 = Toplevel()
        Delete(root3)
class Delete():
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Delete List")
        self.master.resizable(False, False)
        
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Delete", accelerator='Alt+D', command=self.deletefile)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Alt+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-d>', lambda event: self.deletefile())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu()) 
        f = os.listdir()
        if not f:
            msg.showerror("ERROR", "NO ROUTINE")
            self.master.destroy()
        else:
            self.flist = StringVar(master)
            self.flist.set(f[0])
            self.chomenu = OptionMenu(self.master, self.flist, *f)
            self.chomenu.pack()
            self.deleteb = Button(self.master, text="DELETE", command=self.deletefile)
            self.deleteb.pack()
    def deletefile(self):
        os.remove(self.flist.get())
        msg.showinfo("SUCCESS", "THE "+str(self.flist.get())+ " ROUTINE FILE HAS SUCCESSFULLY DELETED")
        self.master.destroy()
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def helpmenu(self):
        msg.showinfo("Help", "Here you can delete the routine files")
    def aboutmenu(self):
        msg.showinfo("About", "About \nVersion 1.0")
class Createl():
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x150")
        self.master.title("Create List")
        self.master.resizable(False, False)
        self.texten = Entry(self.master, font="Arial 24")
        self.texten.pack()
        self.insertb = Button(self.master, text="INSERT", command=self.ins)
        self.insertb.pack()
        self.cancelb = Button(self.master, text="CANCEL", command=self.cans)
        self.cancelb.pack()
        self.clearb = Button(self.master, text="CLEAR", command=self.clearfun)
        self.clearb.pack()
        self.okb = Button(self.master, text="OK", command=self.okbff)
        self.okb.pack()
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert", accelerator='Alt+I', command=self.ins)
        self.file_menu.add_command(label="Cancel", accelerator='Alt+C', command=self.cans)
        self.file_menu.add_command(label="Clear", accelerator='Ctrl+C', command=self.clearfun)
        self.file_menu.add_command(label="Ok", accelerator='Ctrl+O', command=self.okbff)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.showroutinem = Menu(self.menu, tearoff=0)
        self.showroutinem.add_command(label="Show Routine", accelerator='Alt+O', command=self.showroutine)
        self.menu.add_cascade(label="Show", menu=self.showroutinem)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Alt+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-i>', lambda evnet: self.ins())
        self.master.bind('<Alt-c>', lambda event: self.cans())
        self.master.bind('<Control-c>', lambda event: self.clearfun())
        self.master.bind('<Control-o>', lambda event: self.okbff())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.showroutine())
    def clearfun(self):
        self.texten.delete(0, END)
    def ins(self):
        global createrou
        with open(str(createrou)+str(".csv"), 'a+') as o:
            thewriter = csv.writer(o)
            thewriter.writerow([self.texten.get()])
        self.texten.delete(0, END)
        msg.showinfo("SUCCESS", "TO DO SUCCESSFULLY CREATED")
    def cans(self):
        global createrou
        if msg.askyesno("Cancel", "IF YOU CANCEL YOUR ROUTINE IS GOING TO BE DELETED") == True:
            os.remove(str(createrou)+str('.csv'))
            self.master.destroy()
    def okbff(self):
        msg.showinfo("SAVE", "THE ROUTINE HAS SUCCESSFULLY SAVED")
        self.master.destroy()
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def helpmenu(self):
        msg.showinfo("Help", "Here you create routine")
    def aboutmenu(self):
        msg.showinfo("About", "About \nVersion 1.0")
    def showroutine(self):
        df = pd.read_csv(str(createrou)+str(".csv"))
        msg.showinfo("ROUTINE", str(df))
class Loadlist():
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Load List")
        self.master.resizable(False, False)
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Load", accelerator='Ctrl+L', command=self.load)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Alt+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-l>', lambda event: self.load())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())
        global flist
        f = os.listdir()
        if not f:
            msg.showerror("ERROR", "THERE IS NO ROUTINE")
            self.master.destroy()
        else:
            flist = StringVar(master)
            flist.set(f[0])
            self.chomenu = OptionMenu(self.master, flist, *f)
            self.chomenu.pack()
            self.loadb = Button(self.master, text="LOAD", command=self.load)
            self.loadb.pack()
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def helpmenu(self):
        msg.showinfo("Help", "Here you can choose the routine you want to load")
    def aboutmenu(self):
        msg.showinfo("About", "About \nVersion 1.0")
        
    def load(self):
        msg.showinfo("SUCCESS", "TO DO SUCCESSFULLY LOADED")
        root5 = Toplevel()
        Loader(root5)
class Loader():
    def __init__(self, master):
        self.master = master
        self.master.geometry("250x150")
        self.master.title("Loader")
        self.master.resizable(False, False)
        self.texten = Entry(self.master, font="Arial 24")
        self.texten.pack()
        self.insertb = Button(self.master, text="INSERT", command=self.ins)
        self.insertb.pack()
        self.cancelb = Button(self.master, text="CANCEL", command=self.cans)
        self.cancelb.pack()
        self.clearb = Button(self.master, text="CLEAR", command=self.clearfun)
        self.clearb.pack()
        self.okb = Button(self.master, text="OK", command=self.okbf)
        self.okb.pack()
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert", accelerator='Alt+I', command=self.ins)
        self.file_menu.add_command(label="Cancel", accelerator='Alt+C', command=self.cans)
        self.file_menu.add_command(label="Clear", accelerator='Ctrl+C', command=self.clearfun)
        self.file_menu.add_command(label="Ok", accelerator='Ctrl+O', command=self.okbf)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.showroutinem = Menu(self.menu, tearoff=0)
        self.showroutinem.add_command(label="Show Routine", accelerator='Alt+O', command=self.showroutine)
        self.menu.add_cascade(label="Show", menu=self.showroutinem)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=self.aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Alt+F1', command=self.helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        
        self.master.bind('<Alt-i>', lambda evnet: self.ins())
        self.master.bind('<Alt-c>', lambda event: self.cans())
        self.master.bind('<Control-c>', lambda event: self.clearfun())
        self.master.bind('<Control-o>', lambda event: self.okbf())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: self.helpmenu())
        self.master.bind('<Control-i>', lambda event: self.aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.showroutine())
    def aboutmenu(self):
        msg.showinfo("About", "About \nVersion 1.0")
    def helpmenu(self):
        msg.showinfo('Help', 'Loads a routine file')
    def clearfun(self):
        self.texten.delete(0, END)
    def ins(self):
        global createrou
        creatorou = flist.get()
        with open(str(createrou)+str(".csv"), 'a+') as t:
            thewriter = csv.writer(t)
            thewriter.writerow([self.texten.get()])
    def cans(self):
        global createrou
        creatorou = flist.get()
        if msg.askyesno("Cancel", "IF YOU CANCEL YOUR ROUTINE IS GOING TO BE DELETED") == True:
            os.remove(str(createrou)+str('.csv'))
            self.master.destroy()
    def okbf(self):
        msg.showinfo("SAVE", "THE ROUTINE HAS SUCCESSFULLY SAVED")
        self.master.destroy()
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def showroutine(self):
        df = pd.read_csv(str(createrou)+str(".csv"))
        msg.showinfo("ROUTINE", str(df))
def main():
    """ main function """
    root = Tk()
    Routine_Creator(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
