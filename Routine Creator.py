from tkinter import *

class Routine_Creator():
    def __init__(self,master):
        self.master = master
        self.master.title("Routine Creator")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        
        self.createb = Button(self.master,text ="CREATE A ROUTINE")
        self.createb.pack()
        
        self.loadb = Button(self.master,text = "LOAD A ROUTINE")
        self.loadb.pack()
        
        self.deleteb = Button(self.master,text = "DELETE A ROUTINE")
        self.deleteb.pack()
                
def main():
    root=Tk()
    RC = Routine_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()