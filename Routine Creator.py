from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox as msg


class Routine_Creator():
    def __init__(self,master):
        self.master = master
        self.master.title("Routine Creator")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu,tearoff = 0)
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
        pass
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass
    
    def creater(self):
        createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
            
    def loadf(self):
        pass
    def delf(self):
        pass
    
                
def main():
    root=Tk()
    RC = Routine_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()