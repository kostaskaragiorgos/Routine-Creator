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
        global createrou
        createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
        while createrou == None:
            createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
        if os.path.exists(str(createrou)+str(".csv")) == False:
            with open(str(createrou)+str(".csv"), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['TO DO'])
                f.close()
        else:
            flagexists = 1
            msg.showerror("Error","This routine exists")
        while flagexists == 1:
            createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
            while createrou == None:
                createrou = simpledialog.askstring("NEW ROUTINE","Enter the name of the new routine", parent = self.master)
            if os.path.exists(createrou+str(".csv")) == False:
                with open(str(createrou)+str(".csv"), 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['TO DO'])
                    f.close()
                flagexists  = 0
        root1 = Toplevel()
        creategui = Createl(root1)

            
            
    def loadf(self):
        root2 = Toplevel()
        loadgui = Loadlist(root2)
        
    
    def delf(self):
        root3 = Toplevel()
        delgui = Delete(root3)


class Delete():
    def __init__(self,master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Delete List")
        self.master.resizable(False,False)
        f = os.listdir()
        self.flist = StringVar(master)
        self.flist.set(f[0])
        self.chomenu = OptionMenu(self.master,self.flist,*f)
        self.chomenu.pack()
        self.deleteb = Button(self.master,text = "DELETE",command = self.deletefile)
        self.deleteb.pack()
    
    def deletefile(self):
        os.remove(self.flist.get())
        msg.showinfo("SUCCESS", "THE "+str(self.flist.get())+ " ROUTINE FILE HAS SUCCESSFULLY DELETED")
        self.master.destroy()
        
class Createl():
    def __init__(self,master):
        self.master = master
        self.master.geometry("250x150")
        self.master.title("Create List")
        self.master.resizable(False,False)
        self.texten = Entry(self.master,font = "Arial 24")
        self.texten.pack()
        self.insertb = Button(self.master,text = "INSERT",command = self.ins)
        self.insertb.pack()
        self.cancelb = Button(self.master,text = "CANCEL",command =self.cans)
        self.cancelb.pack()
        self.clearb = Button(self.master,text = "CLEAR",command = self.clearfun)
        self.clearb.pack()
        self.okb = Button(self.master,text = "OK",command = self.okb)
        self.okb.pack()
    
    def clearfun(self):
        self.texten.delete(0,END)
        
    def ins(self):
        with open(str(createrou)+str(".csv"), 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([self.texten.get()])
            f.close()
    
    def cans(self):
        if msg.askyesno("Cancel", "IF YOU CANCEL YOUR ROUTINE IS GOING TO BE DELETED") == True:
            os.remove(str(createrou)+str('.csv'))
            self.master.destroy()
        
    def okb(self):
        msg.showinfo("SAVE", "THE ROUTINE HAS SUCCESSFULLY SAVED")
        self.master.destroy()
        
        
class Loadlist():
    def __init__(self,master):
        self.master = master
        self.master.geometry("250x100")
        self.master.title("Load List")
        self.master.resizable(False,False)
        f = os.listdir()
        self.flist = StringVar(master)
        self.flist.set(f[0])
        self.chomenu = OptionMenu(self.master,self.flist,*f)
        self.chomenu.pack()
        self.loadb = Button(self.master,text = "LOAD")
        self.loadb.pack()
        """
        argotera
        self.insertb = Button(self.master,text = "INSERT")
        self.insertb.pack()
        self.cancelb = Button(self.master,text = "CANCEL")
        self.cancelb.pack()
        self.clearb = Button(self.master,text = "CLEAR")
        self.clearb.pack()
        self.okb = Button(self.master,text = "OK")
        self.okb.pack()
        """
def main():
    root=Tk()
    RC = Routine_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()