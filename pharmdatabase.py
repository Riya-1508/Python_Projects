import sqlite3
con = sqlite3.connect('Pharmacy.db')
cur = con.cursor()
cur.execute('CREATE TABLE Pharma(RefNo INTEGER primary key,MedName STRING)')
cur.execute('CREATE TABLE Pharma1(Reference INTEGER,comName STRING,MedType STRING,Medicine STRING,Lot INTEGER,ManDate INTEGER,ExpDate INTEGER,Uses STRING,SideEff STRING,Warning STRING,Dosage STRING,Price INTEGER,ProQT INTEGER)')
