import pandas as pd
import inputprocess as ip
import car as cr
import aimp
import time
import csv

# transform the car information and car purchase plan into standard class form for clearer output
def Car_info():
    car=cr.car_design()
    
    class car_info:
        def __init__(self,name,type0,seats,price,fuel,more_details):
            self.name = name
            self.type = type0
            self.seats = seats
            self.price = price
            self.fuel = fuel
            self.more_details = more_details

    if car.empty == True:
        car_information = car_info('--','--','--','--','--',car)
    else:
        car_information = car_info(list(car.Modelversion),list(car.Bodytype),list(car.Noofseats),list(car.price),list(car.Fuel),car)
    return car_information

def Car_pruchase_plan():
    class car_purchase:
        def __init__(self,car_information,Accessories,Insurance,Maintenance,Payment):
            self.car_information = car_information
            self.accessories_plan = Accessories
            self.insurance_plan = Insurance
            self.maintenance_plan = Maintenance
            self.way_of_payment = Payment

    car= Car_info()
    acc = aimp.Accessories()
    Ins = aimp.Insurance()
    Mai = aimp.Maintenance()
    Pay = aimp.Payment()

    car_purchase_plan = car_purchase(car,acc,Ins,Mai,Pay)
    return car_purchase_plan


