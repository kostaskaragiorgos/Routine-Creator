from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox as msg

import os 
import csv

class Routine_Creator():
    def __init__(self,master):
        self.master = master
        self.master.title("Routine Creator")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        if os.path.exists("Routine") == False:
            os.mkdir("Routine")
            os.chdir("Routine")
        os.chdir("Routine")
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Create Routine",accelerator = 'Ctrl+O',command = self.creater)
        self.file_menu.add_command(label = "Load Routine",accelerator = 'Ctrl+L',command = self.loadf)
        self.file_menu.add_command(label = "Delete Routine",accelerator = 'Ctrl+D',command = self.delf)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator= 'Alt+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        self.createb = Button(self.master,text ="CREATE A ROUTINE", command = self.creater)
        self.createb.pack()
        
        self.loadb = Button(self.master,text = "LOAD A ROUTINE",command = self.loadf)
        self.loadb.pack()
        
        self.deleteb = Button(self.master,text = "DELETE A ROUTINE",command = self.delf)
        self.deleteb.pack()

    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        msg.showinfo("About","About \nVersion 1.0")
    
    def creater(self):
        flagexists = 0
        createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
        if os.path.exists(str(createrou)+str(".csv")) == False:
            with open(createrou+str(".csv"), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['TO DO'])
                f.close()
        else:
            flagexists = 1
            msg.showerror("Error","This routine exists")
        while flagexists == 1:
            createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
            if os.path.exists(createrou+str(".csv")) == False:
                with open(createrou+str(".csv"), 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['TO DO'])
                    f.close()
                flagexists  = 0

            
            
    def loadf(self):
        root1 = Toplevel()
        loadgui = Loadlist(root1)
        
    
    def delf(self):
        root1 = Toplevel()
        delgui = Delete(root1)


class Delete():
    def __init__(self,master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Delete List")
        self.master.resizable(False,False)

class Loadlist():
    def __init__(self,master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Load List")
        self.master.resizable(False,False)
        
        
def main():
    root=Tk()
    RC = Routine_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()