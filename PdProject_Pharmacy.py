import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PharmacyManagement:
    def addMedFunc(self):
        if self.addRef.get() != "" and self.addMed.get() != "":
            try:
                con = sqlite3.connect('Pharmacy.db')
                cur =con.cursor()
                cur.execute('INSERT INTO Pharma VALUES(?,?)',(self.refNoEntry.get(),self.medNameEntry.get()))
                con.commit()
                self.fetch_med()
                con.close()
                messagebox.showinfo('ADDED', 'MEDICINE NAME SUCCESSFULLY ADDED')
                # cur.execute('SELECT * FROM Pharma')
                # print(cur.fetchall())
            except:
                messagebox.showerror("ERROR",'Already existing medicine')
        else:
             messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
    def fetch_med(self):
        
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        cur.execute('SELECT * FROM Pharma')
        r = cur.fetchall()
        if len(r)!=0:
            self.medTable.delete(*self.medTable.get_children())
            for i in r:
                self.medTable.insert("",'end',values = i)    
        con.commit()
        con.close()
    def getCursor(self,event = ""):
        cur_r = self.medTable.focus()
        cont = self.medTable.item(cur_r)
        row = cont["values"]
        self.addRef.set(row[0])
        self.addMed.set(row[1])
    def updateMedFunc(self):
        if self.addRef.get() == "" or self.addMed.get() == "":
            messagebox.showerror("Error","All fields are needed")
        else:
            delete1 = messagebox.askyesno('CONFIRMATION','DO YOU WANT TO UPDATE THE RECORD')
            if delete1>0 :
                con = sqlite3.connect('Pharmacy.db')
                cur =con.cursor()
                cur.execute('UPDATE Pharma SET MedName = ? WHERE RefNo = ?',(
                    self.addMed.get(),
                    self.addRef.get()
                ))
            con.commit()
            self.fetch_med()
        con.close()
        messagebox.showinfo('SUCCESS','MEDICINE SUCCESSFULLY UPDATED')
    def deleteMedFunc(self):
        if self.addRef.get() !='' and self.addMed.get() !='':
            delete1 = messagebox.askyesno('CONFIRMATION','DO YOU WANT TO DELETE THE RECORD')
            if delete1>0 :
                con = sqlite3.connect('Pharmacy.db')
                cur =con.cursor()
                cur.execute('DELETE FROM Pharma WHERE RefNo = ?',(self.addRef.get(),))
                con.commit()
                self.fetch_med()
                return
            con.close()
        else:
            messagebox.showerror("ERROR","ENTER A VALUE TO BE DELETED")
       
    def clearFunc(self):
        self.addRef.set("")
        self.addMed.set("")
    def addData(self):
        
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        if self.ref1.get() != "" and self.lotNum.get() != "":
            cur.execute('INSERT INTO Pharma1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(
            self.ref1.get(),
            self.company.get(),
            self.medtype.get(),
            self.med1.get(),
            self.lotNum.get(),
            self.manu.get(),
            self.expDate.get(),
            self.use1.get(),
            self.sideEff.get(),
            self.warning1.get(),
            self.dosage1.get(),
            self.price1.get(),
            self.productqt1.get(),
            )
            )
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo('SUCCESS',"DETAILS ADDED TO DATABASE")
        else:
            messagebox.showerror("ERROR",'ALL THE FIELDS  ARE REQUIRED')

    def fetch_data(self):
        
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        cur.execute('SELECT * FROM Pharma1')
        rdown = cur.fetchall()
        if len(rdown)!=0:
            self.pharTable.delete(*self.pharTable.get_children())
            for i in rdown:
                self.pharTable.insert("",'end',values = i)    
        con.commit()
        con.close()
    def getCursorBotTab(self,event = ""):
        cur_row = self.pharTable.focus()
        content = self.pharTable.item(cur_row)
        row = content["values"]
        self.ref1.set(row[0])
        self.company.set(row[1])
        self.medtype.set(row[2])
        self.med1.set(row[3])
        self.lotNum.set(row[4])
        self.manu.set(row[5])
        self.expDate.set(row[6])
        self.use1.set(row[7])
        self.sideEff.set(row[8])
        self.warning1.set(row[9])
        self.dosage1.set(row[10])
        self.price1.set(row[11])
        self.productqt1.set(row[12])
    def updateBotTab(self):
        if self.ref1.get() == "" or self.lotNum.get() == "":
            messagebox.showerror("Error","All fields are needed")
        else:
            delete1 = messagebox.askyesno('CONFIRMATION','DO YOU WANT TO UPDATE THE RECORD')
            if delete1>0 :
                con = sqlite3.connect('Pharmacy.db')
                cur =con.cursor()
                cur.execute('UPDATE Pharma1 SET comName =?,MedType = ?,Medicine = ?,Lot = ?,ManDate  = ?,ExpDate = ?,Uses = ?,SideEff = ?,Warning = ?,Dosage = ?,Price = ?,ProQT = ? WHERE Reference = ?',(
                
                self.company.get(),
                self.medtype.get(),
                self.med1.get(),
                self.lotNum.get(),
                self.manu.get(),
                self.expDate.get(),
                self.use1.get(),
                self.sideEff.get(),
                self.warning1.get(),
                self.dosage1.get(),
                self.price1.get(),
                self.productqt1.get(),
                self.ref1.get(),
                ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo('UPDATE','FIELDS SUCCESSFULLY UPDATED')

    def deletebotTab(self):
        
        delete1 = messagebox.askyesno('CONFIRMATION','DO YOU WANT TO DELETE THE RECORD')
        if delete1>0 :
            con = sqlite3.connect('Pharmacy.db')
            cur =con.cursor()
            cur.execute('DELETE FROM Pharma1 WHERE Reference = ?',(self.ref1.get(),))
            con.commit()
            messagebox.showinfo("DELETE","DELETED SUCCESSFULLY")
            self.fetch_data()
            con.close()
    def resetBot(self):
        
            self.company.set(""),
            self.lotNum.set("")
            self.manu.set("")
            self.expDate.set("")
            self.use1.set("")
            self.sideEff.set("")
            self.warning1.set("")
            self.dosage1.set("")
            self.price1.set("")
            self.productqt1.set("")
    def exitBot(self):
        exit = messagebox.askyesno("CONFIRMATION","ARE YOU SURE YOU WANT TO EXIT?")
        if exit>0:
            self.parent.destroy()
            return
        
    def searchByTab(self):
        # try:
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        
        
        if self.search_by.get() == "Reference":
            sql = "SELECT * FROM Pharma1 WHERE Reference = ?"
        if self.search_by.get() == "Medicine":
            sql = "SELECT * FROM Pharma1 WHERE Medicine = ?"
        if self.search_by.get() == "Lot":
            sql = "SELECT * FROM Pharma1 WHERE Lot = ?"
        searched = self.searchtxt.get()
        
        if searched != "":
            name = (searched,)
            result = cur.execute(sql,name)
            row = cur.fetchall()

            if len(row)!=0:
                self.pharTable.delete(*self.pharTable.get_children())
                for i in row:
                    self.pharTable.insert("",'end',values = i)
                con.commit()
            
            else:
                messagebox.showerror("ERROR","MEDICINE NOT FOUND IN THE STORE")
            con.close()
        else:
            messagebox.showerror("ERROR","ADD VALUE TO SEARCH")        
    def __init__(self,parent):
        self.parent = parent
        #Add med variable
        self.addMed = tk.StringVar()
        self.addMed.set("")
        self.addRef =tk. StringVar() 
        self.addRef.set("")
        #Add database variables
        self.ref1 = tk.StringVar()
        self.med1 = tk.StringVar()
        self.company = tk.StringVar()
        self.medtype = tk.StringVar()
        self.lotNum = tk.StringVar()
        self.manu = tk.StringVar()
        self.expDate = tk.StringVar()
        self.use1 = tk.StringVar()
        self.sideEff = tk.StringVar()
        self.warning1 = tk.StringVar()
        self.dosage1 = tk.StringVar()
        self.price1 = tk.StringVar()
        self.productqt1 = tk.StringVar()
        #Label for title
        self.titleLabel = tk.Label(text = "ALL  HEALTH  PHARMACY",bd = 10,relief = 'ridge',bg = "#EF9A9A",fg = "black",font = ("Calibri",55,"bold"),padx = 2,pady = 4)
        self.titleLabel.pack(side = 'top',fill = 'x')

        #Data frame
        self.dataframe = tk.Frame(parent,bd = 17,relief = 'ridge',padx = 24,bg = "#D4E6F1")
        self.dataframe.place(x = 0,y = 120,width = 1535,height = 400)
        self.leftdataframe = tk.LabelFrame(self.dataframe,bd = 10,relief = 'ridge',padx = 24,text = 'Information of Medicines',fg = "darkblue",font = ('Calibri',14,'bold'),bg = "#D4E6F1")
        self.leftdataframe.place(x = 0,y = 5,width = 910,height = 355)
        self.rightdataframe = tk.LabelFrame(self.dataframe,bd = 10,relief = 'ridge',padx = 24,text = 'Update Medicines Department',fg = "darkblue",font = ('Calibri',14,'bold'),bg = "#D4E6F1")
        self.rightdataframe.place(x = 910,y = 5,width = 570,height = 355)

        #Button Frame:
        self.buttonframe = tk.Frame(parent,bd = 17,relief = 'ridge',padx = 24)
        self.buttonframe.place(x = 0,y = 520,width = 1600,height = 70)

        #Main Buttons:
        self.addData = tk.Button(self.buttonframe,text = 'Add to Database',font = ('Calibri',15,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.addData)
        self.addData.grid(row = 0,column = 0)

        self.addData = tk.Button(self.buttonframe,text = 'Update',font = ('Calibri',15,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.updateBotTab)
        self.addData.grid(row = 0,column = 1)

        self.addData = tk.Button(self.buttonframe,text = 'Delete',font = ('Calibri',14,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.deletebotTab)
        self.addData.grid(row = 0,column = 2)

        self.addData = tk.Button(self.buttonframe,text = 'Reset',font = ('Calibri',14,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.resetBot)
        self.addData.grid(row = 0,column = 3)

        self.addData = tk.Button(self.buttonframe,text = 'Exit',font = ('Calibri',14,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.exitBot)
        self.addData.grid(row = 0,column = 4)

        #Search
        self.searchlabel = tk.Label(self.buttonframe,font = ('Calibri',19,'bold'),width = 13,text = 'Search By',padx = 2,bg = '#AD1457',fg = 'white')
        self.searchlabel.grid(row = 0,column = 5,sticky ='W')
        self.search_by = tk.StringVar()
        self.search_item = ttk.Combobox(self.buttonframe,text = self.search_by,width = 13,font = ('Calibri',19,'bold'),state = "readonly")
        self.search_item["values"] = ("Reference","Medicine","Lot")
        self.search_item.grid(row = 0,column = 6)
        self.search_item.current(0)
        self.searchtxt = tk.StringVar()
        self.searchtext = tk.Entry(self.buttonframe,textvariable = self.searchtxt,bd = 4,relief = 'ridge',width = 12,font = ('Calibri',16,'bold'))
        self.searchtext.grid(row = 0,column = 8)

        self.search= tk.Button(self.buttonframe,text = 'Search',font = ('Calibri',14,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.searchByTab)
        self.search.grid(row = 0,column = 7)

        self.showAll = tk.Button(self.buttonframe,text = 'Show All',font = ('Calibri',14,'bold'),width = 13,bg = '#EF9A9A',fg = 'black',command = self.fetch_data)
        self.showAll.grid(row = 0,column = 9)

        #Label and Entry
        self.refNo = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Reference No",padx = 4)
        self.refNo.grid(row = 0,column = 0,sticky = 'w')
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        cur.execute("SELECT RefNo FROM Pharma")
        r1 = cur.fetchall()
        self.search_item = ttk.Combobox(self.leftdataframe,textvariable = self.ref1,width = 18,font = ('Calibri',14,'bold'),state = "readonly")
        self.search_item["values"] = r1
        self.search_item.grid(row = 0,column = 1)
        #self.search_item.current(0)

        self.companyName = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Medicine Company Name:",padx = 4)
        self.companyName.grid(row = 1,column = 0,sticky = 'w')
        self.companyNameEntry = tk.Entry(self.leftdataframe,textvariable = self.company,font = ('Calibri',14,'bold'))
        self.companyNameEntry.grid(row = 1,column = 1,sticky = 'w')

        self.medType = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Medicine Type:",padx = 4)
        self.medType.grid(row = 2,column = 0,sticky = 'w')
        self.med_item = ttk.Combobox(self.leftdataframe,width = 18,textvariable = self.medtype,font = ('Calibri',14,'bold'),state = "readonly")
        self.med_item["values"] = ("Tablets","Capsules","Syrup","Inhaler","Drops","Injections")
        self.med_item.grid(row = 2,column = 1)
        self.med_item.current(0)

        self.issueDate = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Medicine Name",padx = 4)
        self.issueDate.grid(row = 3,column = 0,sticky = 'w')
        con = sqlite3.connect('Pharmacy.db')
        cur =con.cursor()
        cur.execute("SELECT MedName FROM Pharma")
        r2 = cur.fetchall()
        self.search_item = ttk.Combobox(self.leftdataframe,textvariable = self.med1,width = 18,font = ('Calibri',14,'bold'),state = "readonly")
        self.search_item["values"] = r2
        self.search_item.grid(row = 3,column = 1)
        #self.search_item.current(0)

        self.expiryDate = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Expiry Date:",padx = 4,pady = 4)
        self.expiryDate.grid(row = 4,column = 0,sticky = 'w')
        self.expiryDateEntry = tk.Entry(self.leftdataframe,textvariable = self.expDate,font = ('Calibri',14,'bold'))
        self.expiryDateEntry.grid(row = 4,column = 1,sticky = 'w')

        self.manuDate = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Manufactured Date:",padx = 4,pady = 4)
        self.manuDate.grid(row = 5,column = 0,sticky = 'w')
        self.manuDateEntry = tk.Entry(self.leftdataframe,textvariable = self.manu,font = ('Calibri',14,'bold'))
        self.manuDateEntry.grid(row = 5,column = 1,sticky = 'w')

        self.use = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Use:",padx = 4,pady = 4)
        self.use.grid(row = 6,column = 0,sticky = 'w')
        self.useEntry = tk.Entry(self.leftdataframe,textvariable = self.use1,font = ('Calibri',14,'bold'))
        self.useEntry.grid(row = 6,column = 1,sticky = 'w')
        
        self.sideEffects = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Side Effects:",padx = 4,pady = 4)
        self.sideEffects.grid(row = 7,column = 0,sticky = 'w')
        self.sideEffectsEntry = tk.Entry(self.leftdataframe,textvariable = self.sideEff,font = ('Calibri',14,'bold'))
        self.sideEffectsEntry.grid(row = 7,column = 1,sticky = 'w')

        self.warning = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Warning:",padx = 4,pady = 4)
        self.warning.grid(row = 0,column = 2,sticky = 'w')
        self.warningEntry = tk.Entry(self.leftdataframe,textvariable = self.warning1,font = ('Calibri',14,'bold'))
        self.warningEntry.grid(row = 0,column = 3,sticky = 'w')

        self.dosage = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Dosage:",padx = 4,pady = 4)
        self.dosage.grid(row = 1,column = 2,sticky = 'w')
        self.dosageEntry = tk.Entry(self.leftdataframe,textvariable = self.dosage1,font = ('Calibri',14,'bold'))
        self.dosageEntry.grid(row = 1,column = 3,sticky = 'w')

        self.medPrice = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Medicine Price:",padx = 4,pady = 4)
        self.medPrice.grid(row = 2,column = 2,sticky = 'w')
        self.medPrice = tk.Entry(self.leftdataframe,textvariable = self.price1,font = ('Calibri',14,'bold'))
        self.medPrice.grid(row = 2,column = 3,sticky = 'w')

        self.prodqt = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Product QT:",padx = 4,pady = 4)
        self.prodqt.grid(row = 3,column = 2,sticky = 'w')
        self.prodqt = tk.Entry(self.leftdataframe,textvariable = self.productqt1,font = ('Calibri',14,'bold'))
        self.prodqt.grid(row = 3,column = 3,sticky = 'w')

        self.lotNo = tk.Label(self.leftdataframe,font = ('Calibri',14,'bold'),text = "Lot No:",padx = 4,pady = 4)
        self.lotNo.grid(row = 8,column = 0,sticky = 'w')
        self.lotNoEntry = tk.Entry(self.leftdataframe,textvariable = self.lotNum,font = ('Calibri',14,'bold'))
        self.lotNoEntry.grid(row = 8,column = 1,sticky = 'w')

        self.refNolabel = tk.Label(self.rightdataframe,font = ('Calibri',14,'bold'),text = "Reference No:",padx = 4)
        self.refNolabel.place(x = 0,y = 20)
        self.refNoEntry = tk.Entry(self.rightdataframe,textvariable = self.addRef,font = ('Calibri',14,'bold'))
        self.refNoEntry.place(x = 140,y = 20)

        self.medNamelabel = tk.Label(self.rightdataframe,font = ('Calibri',14,'bold'),text = "Medicine Name:",padx = 4)
        self.medNamelabel.place(x = 0,y = 55)
        self.medNameEntry = tk.Entry(self.rightdataframe,textvariable = self.addMed,font = ('Calibri',14,'bold'))
        self.medNameEntry.place(x = 140,y = 55)

        #Side Frame
        self.sideFrame = tk.Frame(self.rightdataframe,bd = 5,relief = 'ridge',bg = "#D6EAF8")
        self.sideFrame.place(x = 0,y = 95,width = 300,height = 200)

        self.scrollx = ttk.Scrollbar(self.sideFrame,orient = 'horizontal')
        self.scrollx.pack(side = 'bottom',fill = 'x')
        self.scrolly = ttk.Scrollbar(self.sideFrame,orient = 'vertical')
        self.scrolly.pack(side = 'right',fill = 'y')
        self.s = ttk.Style()
        self.s.theme_use("clam")
        self.s.configure('Treeview.Heading',background = "#5499C7",foreground = "white",font = ("Calibri",14,"bold"))
        self.medTable = ttk.Treeview(self.sideFrame,column = ("ref","medname"),xscrollcommand = self.scrollx.set,yscrollcommand = self.scrolly.set)
        
        self.scrollx.config(command = self.medTable.xview)
        self.scrolly.config(command = self.medTable.yview)

        self.medTable.heading("ref",text = "Reference")
        self.medTable.heading("medname",text = "Medicine Name")
        self.medTable["show"] = "headings"
        self.medTable.pack(fill = 'both',expand = 2)

        self.medTable.column("ref",width = 100)
        self.medTable.column("medname",width =100)

        self.medTable.bind("<ButtonRelease-1>",self.getCursor)
        #Add Medicine Buttons
        self.downFrame = tk.Frame(self.rightdataframe)
        self.downFrame.place(x = 330,y = 150,width = 120,height = 160)

        self.addButton = tk.Button(self.downFrame,text = 'ADD',font = ('Calibri',14,'bold'),width = 11,bg = '#880E4F',fg = 'white',command = self.addMedFunc)
        self.addButton.grid(row = 0,column = 0)

        self.addButton = tk.Button(self.downFrame,text = 'UPDATE',font = ('Calibri',14,'bold'),width = 11,bg = '#880E4F',fg = 'white',command = self.updateMedFunc)
        self.addButton.grid(row = 1,column = 0)

        self.addButton = tk.Button(self.downFrame,text = 'DELETE',font = ('Calibri',14,'bold'),width = 11,bg = '#880E4F',fg = 'white',command = self.deleteMedFunc)
        self.addButton.grid(row = 2,column = 0)

        self.addButton = tk.Button(self.downFrame,text = 'CLEAR',font = ('Calibri',14,'bold'),width = 11,bg = '#880E4F',fg = 'white',command = self.clearFunc)
        self.addButton.grid(row = 3,column = 0)

        self.detailsframe = tk.Frame(parent,bd = 14,relief = 'ridge')
        self.detailsframe .place(x = 0,y = 580,width = 1535,height = 215)

        self.tableframe = tk.Frame(self.detailsframe,bd = 14,relief = 'ridge')
        self.tableframe .place(x = 0,y = 3,width = 1500,height = 170)

        self.scrollx = ttk.Scrollbar(self.detailsframe,orient = 'horizontal')
        self.scrollx.pack(side = 'bottom',fill = 'x')
        self.scrolly = ttk.Scrollbar(self.detailsframe,orient = 'vertical')
        self.scrolly.pack(side = 'right',fill = 'y')
        self.s = ttk.Style()
        self.s.theme_use("clam")
        self.s.configure('Treeview.Heading',background = "#5499C7",foreground = "white",font = ("Calibri",11,"bold"))
        self.pharTable = ttk.Treeview(self.detailsframe,column = ("reg","companyname","type","medname","lotno","manfdate","expdate","uses","sideffect","warning","dosage","price","productqt"),xscrollcommand = self.scrollx.set,yscrollcommand = self.scrolly.set)

        self.scrollx.config(command = self.pharTable.xview)
        self.scrolly.config(command = self.pharTable.yview)
        self.pharTable["show"] = ["headings"]
        self.pharTable.heading("reg",text = "Reference No")
        self.pharTable.heading("companyname",text = "Company Name")
        self.pharTable.heading("type",text = "Medicine Type")
        self.pharTable.heading("medname",text = "Medicine Name")
        self.pharTable.heading("lotno",text = "Lot No")
        self.pharTable.heading("manfdate",text = "Manufacture Date")
        self.pharTable.heading("expdate",text = "Expiry Date")
        self.pharTable.heading("uses",text = "Uses")
        self.pharTable.heading("sideffect",text = "Side Effects")
        self.pharTable.heading("warning",text = "Warning")
        self.pharTable.heading("dosage",text = "Dosage")
        self.pharTable.heading("price",text = "Price")
        self.pharTable.heading("productqt",text = "Product QT")
        self.pharTable.pack(fill = 'both',expand = 2)

        self.pharTable.column("reg",width =100)
        self.pharTable.column("companyname",width =100)
        self.pharTable.column("type",width =100)
        self.pharTable.column("medname",width =100)
        self.pharTable.column("lotno",width =100)
        self.pharTable.column("manfdate",width =100)
        self.pharTable.column("expdate",width =100)
        self.pharTable.column("uses",width =60)
        self.pharTable.column("sideffect",width =100)
        self.pharTable.column("warning",width =100)
        self.pharTable.column("dosage",width =100)
        self.pharTable.column("price",width =60)
        self.pharTable.column("productqt",width =100)
        self.fetch_med()
        self.fetch_data()
        self.pharTable.bind("<ButtonRelease-1>",self.getCursorBotTab)
if __name__ == '__main__':
    window = tk.Tk()
    myapp = PharmacyManagement(window)
    window.title('Pharmacy Management')
    window.geometry("2900x850+0+0")
    window.config()
    window.mainloop()