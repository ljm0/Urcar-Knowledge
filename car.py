import pandas as pd
import inputprocess as ip
import time
import csv

# do the car purchase plan design(car component design) procedure
# start_time = time.time()

def car_design():

    car_database = ip.read_db()#car database
    # print(car_database)

    customer_basic_info=ip.CustomerBasicInfo()# name age sex salary hobby
    requirements=ip.Requirements()
    preferences=ip.Preferences()
    car_specific_requirements = requirements[0] #car type, car purpose, car seats
    #maintainance frequency,money         insurcace object, money
    extra_requirements = preferences[1] #extra_functions, extra_requirements

    if int(customer_basic_info.age) >=35: # age influence total car classification
        a1 = car_database.loc[car_database['Car classification']=='Medium car']
    else:
        a1 = car_database.loc[car_database['Car classification']=='Compact car']

    budget=int(customer_basic_info.salary)*15
    a2 = a1.loc[a1['price']<=budget] # budget is based on the salary

    if customer_basic_info.hobby=='SOT': #if the hobby is sport or travel
        a3 = a2.loc[a2['Power']>=150]
    elif customer_basic_info.hobby=='SP': #if the hobby is shopping or sth similar
        a3 = a2.loc[(a2['Power']<150) & (a2['Power']>=90)]
    else: # no specific requirements
        a3 = a2
    
    a4 = a3.loc[a3['Noofseats']>=int(car_specific_requirements.car_seats)] #car seats requiremnets

    t = car_specific_requirements.car_type         # body type selection, first specific selection, then selection according to purpose
    if t =='Saloon' or t=='Estate' or t=='Liftback' or t=='Coupe' or t=='Cabrio' or t=='Hatchback' or t=='MPV': 
        a5 = a4.loc[a4['Bodytype']==car_specific_requirements.car_type]
    elif car_specific_requirements.car_purpose=='B': #purpose: Business use
        a5 = a4.loc[a4['Bodytype']=='Saloon']
    elif car_specific_requirements.car_purpose=='F': #purpose: Family use
        a5 = a4.loc[a4['Bodytype']=='Estate']
    elif car_specific_requirements.car_purpose=='S': #purpose: Travel and sport use
        a5 = a4.loc[a4['Bodytype']=='Liftback']
    else:
        a5 = a4

    if extra_requirements.extra_requirements=='Clean_Energy': # preferences: extra_requirements. extra_functions is processed in acceorssies
        a6 = a5.loc[a5['Fuel']!= 'Diesel']
    elif extra_requirements.extra_requirements=='Cheap':
        a6 = a5.loc[a5['price']<=budget*0.75]
    elif extra_requirements.extra_requirements=='Automatic':
        a6 = a5.loc[a5['Automatic']>6]
    else:
        a6 = a5

    a7 = a6.sort_values(by = 'price',axis = 0,ascending = False)
    if a7.empty==True:
        car = a7
    else:
        car=a7.iloc[[0]] # find the car which most meet the requirements

    return car



# temp=car_design()
# print(temp)


# a1 = car_database.loc[car_database['Body type']=='Coupe']
# a2 = a1.loc[a1['price']<=30000]

# if a2.empty == True:
#     print('no results')


# end_time= time.time()
# print('running time =', end_time-start_time)