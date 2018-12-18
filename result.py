from tkinter import *
import struc4carandplan as st
import application as ap
import pandas as pd
import os

def design_plan():

        t = st.Car_pruchase_plan()
        t.car_information.more_details.to_csv(os.getcwd()+"/output/details.csv",index=False,sep=',')
        root = Tk()
        root.title("Your plan")
        Label(root,fg = 'blue', anchor = 'nw',text="Personalized plan",font=(None,20, "bold")).grid(row=0)# plan illustration
        Label(root,fg = 'blue', anchor = 'nw',text="Car information:",font=(None,15, "bold")).grid(row=1)# Car info block
        Label(root, text="Car name:",font=(None, 10, "bold")).grid(row=2,column = 0)
        Label(root, text=t.car_information.name).grid(row=2,column = 1)
        Label(root, text="Car type:",font=(None, 10, "bold")).grid(row=3,column = 0)
        Label(root, text=t.car_information.type).grid(row=3,column = 1)
        Label(root, text="Car seats:",font=(None, 10, "bold")).grid(row=4,column = 0)
        Label(root, text=t.car_information.seats).grid(row=4,column = 1)
        Label(root, text="Car price:",font=(None, 10, "bold")).grid(row=5,column = 0)
        Label(root, text=t.car_information.price).grid(row=5,column = 1)
        Label(root, text="Car fuel:",font=(None, 10, "bold")).grid(row=6,column = 0)
        Label(root, text=t.car_information.fuel).grid(row=6,column = 1)
        Label(root,fg = 'blue', anchor = 'nw',text="Accessories plan:",font=(None,15, "bold")).grid(row=8)# Accessories plan block
        Label(root, text="Accessories list:",font=(None, 10, "bold")).grid(row=9,column = 0)
        Label(root, text=t.accessories_plan.accessories_list).grid(row=9,column = 1)
        Label(root,fg = 'blue', anchor = 'nw',text="Insurance plan:",font=(None,15, "bold")).grid(row=10)# Insurance plan block
        Label(root, text="Object:",font=(None, 10, "bold")).grid(row=11,column = 0)
        Label(root, text=t.insurance_plan.object).grid(row=11,column = 1)
        Label(root, text="Budget:",font=(None, 10, "bold")).grid(row=12,column = 0)
        Label(root, text=t.insurance_plan.budget).grid(row=12,column = 1)
        Label(root,fg = 'blue', anchor = 'nw',text="Maintenance program:",font=(None,15, "bold")).grid(row=13)# Maintainance program block
        Label(root, text="Frequency:",font=(None, 10, "bold")).grid(row=14,column = 0)
        Label(root, text=t.maintenance_plan.frequency).grid(row=14,column = 1)
        Label(root, text="Budget:",font=(None, 10, "bold")).grid(row=15,column = 0)
        Label(root, text=t.maintenance_plan.budget).grid(row=15,column = 1)
        Label(root,fg = 'blue', anchor = 'nw',text="Way of payment:",font=(None,15, "bold")).grid(row=16)# payment way block
        Label(root, text="Way of payment:",font=(None, 10, "bold")).grid(row=17,column = 0)
        Label(root, text=t.way_of_payment.way_of_payment).grid(row=17,column = 1)
        Label(root,fg = 'red', anchor = 'nw',text="Unsatisfied? Re-input the information pls",font=(None,10, "bold")).grid(row=18, sticky=W)# critique

        def detail():
                os.system(os.getcwd()+"/output/details.csv")

        def process():
                root.destroy()
                ap.app() # check and re-do the car purchase plan generate procedure

        Button(root, text="More car details", width=15,command=detail).grid(row=7, column=0, sticky=W, padx=10, pady=5)
        Button(root, text="reinput", width=10,command=process).grid(row=18, column=1, sticky=E, padx=10, pady=5)
        Button(root, text="exit", width=10,command=root.destroy).grid(row=20, column=1, sticky=E, padx=10, pady=5)
        mainloop()