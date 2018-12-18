import pandas as pd
import inputprocess as ip
import car as cr
import time
import csv

# do the car purchase plan design(Accessories_Insurance_Maintenance_Payment 4 components design) procedure
# start_time = time.time()

def Accessories():
    Accessories_list=[]
    car=cr.car_design()
    preferences=ip.Preferences()
    extra_functions = preferences[0]
    if car.empty == True:
        Accessories_list.append('No recommendation')
    else:
        if int(car.Automatic) != 8:
            Accessories_list.append('Automatic assist system') #first approval of accessories

        if extra_functions.extra_functions=='Bluetooth': #find the accessories according to extra functions
            Accessories_list.append('Bluetooth system')
        elif extra_functions.extra_functions=='Wireless':
            Accessories_list.append('Wireless system')
        else:
            Accessories_list=Accessories_list
        
        if Accessories_list==[]:
            Accessories_list.append('No recommendation for Accessories')
    
    class accessor:
        def __init__(self,accessories_list):
            self.accessories_list = accessories_list

    accessories_plan = accessor(Accessories_list)
    
    return accessories_plan
    
def Insurance():
    class Insurance:
        def __init__(self, object1, budget):
            self.object = object1
            self.budget = budget

    car=cr.car_design()
    requirements=ip.Requirements()
    insurance_specific_requirements = requirements[2]
    customer_basic_info=ip.CustomerBasicInfo()

    if car.empty == True:
        if int(insurance_specific_requirements.insurance_money)!=0: #insurance plan was influenced by input money or car price
            bud = insurance_specific_requirements.insurance_money
        else:
            bud = int(customer_basic_info.salary)*0.35
        t = int(bud)

        if int(insurance_specific_requirements.insurance_object) !=0:#insurance object was influenced by input object or budget
            obj = insurance_specific_requirements.insurance_object
        elif t < 1000:
            obj = 'Compulsory'
        elif t>1800:
            obj = 'Full'
        else:
            obj = 'Compulsory&half'
    else:
        if int(insurance_specific_requirements.insurance_money)!=0: #insurance plan was influenced by input money or car price
            bud = insurance_specific_requirements.insurance_money
        else:
            bud = int(car.price)*0.05

        t = int(bud)

        if int(insurance_specific_requirements.insurance_object) !=0:#insurance object was influenced by input object or budget
            obj = insurance_specific_requirements.insurance_object
        elif t < 1000:
            obj = 'Compulsory'
        elif t>1800:
            obj = 'Full'
        else:
            obj = 'Compulsory&half'
    
    insurance_plan=Insurance(obj,bud)
    
    return insurance_plan

def Maintenance():
    class Maintenance_p:
        def __init__(self, frequency, budget):
            self.frequency = frequency
            self.budget = budget

    car=cr.car_design()
    requirements=ip.Requirements()
    maintenance_specific_requirements = requirements[1]
    customer_basic_info=ip.CustomerBasicInfo()

    if car.empty == True:
        if int(maintenance_specific_requirements.maintainance_money)!=0: #maintenance plan was influenced by input money or car price
            bud = maintenance_specific_requirements.maintainance_money
        else:
            bud = int(customer_basic_info.salary)*0.15

        if int(maintenance_specific_requirements.maintainance_frequency) !=0:#maintenance frequency was influenced by input object or budget
            fre = maintenance_specific_requirements.maintainance_frequency
        elif int(bud) >400:
            if customer_basic_info.hobby=='SOT': #if customer travels a lot
                fre = 2
            else:
                fre = 1
        else:
            if customer_basic_info.hobby=='SOT':
                fre = 1
            else:
                fre = 0.5
    else:
        if int(maintenance_specific_requirements.maintainance_money)!=0: #maintenance plan was influenced by input money or car price
            bud = maintenance_specific_requirements.maintainance_money
        else:
            bud = int(car.price)*0.015-int(customer_basic_info.salary)*0.07

        t = int(bud)

        if int(maintenance_specific_requirements.maintainance_frequency) !=0:#maintenance frequency was influenced by input object or budget
            fre = maintenance_specific_requirements.maintainance_frequency
        elif t >400:
            if customer_basic_info.hobby=='SOT': #if customer travels a lot
                fre = 2
            else:
                fre = 1
        else:
            if customer_basic_info.hobby=='SOT':
                fre = 1
            else:
                fre = 0.5
    
    maintenance_plan = Maintenance_p(fre,bud)
    return maintenance_plan

def Payment():#salary and car price influence way of payment
    car=cr.car_design()
    customer_basic_info=ip.CustomerBasicInfo()

    if car.empty == True:
        if int(customer_basic_info.salary)>5000:
            way4pay = 'One-time-payment'
        else:
            way4pay = 'Loan'
    else:
        if int(car.price) > int(customer_basic_info.salary)*12:
            way4pay = 'Loan'
        else:
            way4pay = 'One-time-payment'

    class pay:
        def __init__(self, way4p):
            self.way_of_payment = way4p
    
    way_of_payment = pay(way4pay)

    return way_of_payment

#end_time= time.time()
#print('running time =', end_time-start_time)