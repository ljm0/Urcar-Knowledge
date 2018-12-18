from tkinter import *
import csv
import result as re
import os

def app():
    root = Tk()
    root.title("Urcar System")
    Label(root,fg = 'blue', anchor = 'nw',text="Urcar System",font=(None,20, "bold")).grid(row=0)# Title

    Label(root,fg = 'red', anchor = 'nw',wraplength= 200,text="Need help?").grid(column=1, row=0, sticky=E)#help block
    Label(root,fg = 'blue', anchor = 'nw',wraplength= 200,text="Please input your basic info: (input 0 if you have no idea)").grid(row=1)#input structure: personal information
    Label(root, text="Name").grid(row=2)
    Label(root, text="Age").grid(row=3)
    Label(root, text="Sex").grid(row=4)
    Label(root, text="Salary").grid(row=5)
    Label(root, text="Hobby(sport shopping or travel)").grid(row=6)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)
    e5 = Entry(root)
    e1.insert(10,"Somebody")
    e2.insert(10,"25")
    e3.insert(10,"M")
    e4.insert(10,"2500")
    e5.insert(10,"shopping")
    e1.grid(row=2, column=1, padx=10,pady=5)
    e2.grid(row=3, column=1, padx=10,pady=5)
    e3.grid(row=4, column=1, padx=10,pady=5)
    e4.grid(row=5, column=1, padx=10,pady=5)
    e5.grid(row=6, column=1, padx=10,pady=5)

    Label(root,fg = 'blue', anchor = 'nw',text="Please input car specific requirements:").grid(row=7)#input structure: car specific requirements
    Label(root, text="Car type (Saloon, Estate, Liftback, Coupe, Cabrio, Hatchback or MPV)").grid(row=8)
    Label(root, text="Car purpose (Family, Business, Travel or Sport)").grid(row=9)
    Label(root, text="Car seats").grid(row=10)
    e6 = Entry(root)
    e7 = Entry(root)
    e8 = Entry(root)
    e6.insert(10,"Estate")
    e7.insert(10,"Family")
    e8.insert(10,"5")
    e6.grid(row=8, column=1, padx=10,pady=5)
    e7.grid(row=9, column=1, padx=10,pady=5)
    e8.grid(row=10, column=1, padx=10,pady=5)

    Label(root,fg = 'blue', anchor = 'nw',text="Please input Maintenance specific requirements:").grid(row=11)#input structure: maintenance specific requirements
    Label(root, text="Frequency").grid(row=12)
    Label(root, text="Money").grid(row=13)
    e9 = Entry(root)
    e10 = Entry(root)
    e9.insert(10,'0')
    e10.insert(10,'0')
    e9.grid(row=12, column=1, padx=10,pady=5)
    e10.grid(row=13, column=1, padx=10,pady=5)

    Label(root,fg = 'blue', anchor = 'nw',text="Please input Insurance specific requirements:").grid(row=14)#input structure: Insurance specific requirements
    Label(root, text="Money").grid(row=15)
    Label(root, text="Object").grid(row=16)
    e11 = Entry(root)
    e12 = Entry(root)
    e11.insert(10,'0')
    e12.insert(10,'0')
    e11.grid(row=15, column=1, padx=10,pady=5)
    e12.grid(row=16, column=1, padx=10,pady=5)

    Label(root,fg = 'blue', anchor = 'nw',text="Please input additional information:").grid(row=17)#input structure: Preferences
    Label(root, text="Extra functions (Bluetooth or Wireless)").grid(row=18)
    Label(root, text="Extra requirements (Clean_Energy, Cheap or Automatic)").grid(row=19)
    e13 = Entry(root)
    e14 = Entry(root)
    e13.insert(10,'Bluetooth')
    e14.insert(10,'Clean_Energy')
    e13.grid(row=18, column=1, padx=10,pady=5)
    e14.grid(row=19, column=1, padx=10,pady=5)

    def process():

        t1 = e5.get()
        if t1=='shopping':
            t1='SP'
        elif t1 == 'travel':
            t1 = 'SOT'
        elif t1 == 'sport':
            t1 = 'SOT'
        else:
            pass #transform input

        stu1 = [e1.get(),e2.get(),e3.get(),e4.get(),t1]

        path = os.getcwd()+'/input/customer.csv'
        with open(path,'w',newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(stu1) # for the customer basic information

        t2 = e7.get()
        if t2=='Family':
            t2 = 'F'
        elif t2=='Business':
            t2 = 'B'
        elif t2 =='Travel':
            t2 = 'S'
        elif t2=='Sport':
            t2 = 'S'
        else:
            pass
        
        stu2 = [e6.get(),t2,e8.get()]
        stu3 = [e9.get(),e10.get()]
        stu4 = [e11.get(),e12.get()]

        path1 = os.getcwd()+'/input/requirements.csv'
        with open(path1,'w',newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(stu2) # for the car requirements
            csv_write.writerow(stu3) # for maintenance requirements
            csv_write.writerow(stu4) # for insurance requirements

        path2 = os.getcwd()+'/input/preferences.csv'
        with open(path2,'w',newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([e13.get()]) # for extra functions
            csv_write.writerow([e14.get()]) # for extra requirements

        root.destroy()


        re.design_plan() # generate final car purchase plan
    def helpme():
        os.system("helpme.txt")
        


    Button(root, text="Help me", width=10,command=helpme).grid(row=1, column=1, sticky=E, padx=10, pady=5)
    Button(root, text="Confirm", width=10,command=process).grid(row=20, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="exit", width=10,command=root.destroy).grid(row=20, column=1, sticky=E, padx=10, pady=5)
    mainloop()