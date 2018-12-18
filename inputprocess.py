import pandas as pd
import time
import csv
import os

# transform the input information (car database(dataframe form) and the customers' input) into different class and subclasses, including customer basic information,
# requirements(sub-class: car, maintainance and insurance specific requirements) and preferences(sub-class: extra functions and extra requirements)
# start_time = time.time()

def read_db(): # read database
    excelFile = r'cardetail.xls'
    df = pd.DataFrame(pd.read_excel(excelFile))
    df=df.convert_objects(convert_numeric=True) # transfer 'object' to 'int' 'float'...https://stackoverflow.com/questions/21197774/assign-pandas-dataframe-column-dtypes
                                                #https://blog.csdn.net/a18312800683/article/details/80428315
#    print(df.iloc[0])
#    print(df)
    return df


def CustomerBasicInfo(): # customer basic information, names are consistant with domain schema

    with open(os.getcwd()+'/input/customer.csv') as f:
        reader = csv.reader(f)
        customer_basic_information=list(reader)[0]    
        
    class Customer:
        def __init__(self,n,a,se,sa,ho):
            self.name = n
            self.age = a
            self.sex = se
            self.salary = sa
            self.hobby = ho

    customer0 = Customer(customer_basic_information[0], customer_basic_information[1], customer_basic_information[2], customer_basic_information[3], customer_basic_information[4])
    return customer0
# customer=CustomerBasicInfo()
# print(customer.name)


def Requirements(): # requirements, names are consistant with domain schema

    with open(os.getcwd()+'/input/requirements.csv') as f:
        reader = csv.reader(f)
        requirements_total=list(reader)
        car_requirements=requirements_total[0]
        maintainance_requirements=requirements_total[1]
        insurance_requirements=requirements_total[2]
    # print(car_requirements)
    # print(maintainance_requirements)
    # print(insurance_requirements)

    class Requirements:
        def __init__(self,defaultvalue):
            self.type=defaultvalue
    # aaa=Requirements('This is requirements')
    # print(aaa.type)

    class Car_specific_requirements(Requirements):
        def __init__(self,type,car_type,car_purpose,car_seats):
            super(Car_specific_requirements,self).__init__(type)
            self.car_type=car_type
            self.car_purpose=car_purpose
            self.car_seats=car_seats
    
    car_specific_requirements=Car_specific_requirements('This is car specific requirements',car_requirements[0],car_requirements[1],car_requirements[2])
    # print(car_specific_requirements.type)

    class Maintainance_specific_requirements(Requirements):
        def __init__(self,type,frequency,money):
            super(Maintainance_specific_requirements,self).__init__(type)
            self.maintainance_frequency=frequency
            self.maintainance_money=money
    
    maintainance_specific_requirements=Maintainance_specific_requirements('This is maintainance specific requirements',maintainance_requirements[0],maintainance_requirements[1])
    # print(maintainance_specific_requirements.maintainance_frequency)

    class Insurance_specific_requirements(Requirements):
        def __init__(self,type,money,object0):
            super(Insurance_specific_requirements,self).__init__(type)
            self.insurance_money=money
            self.insurance_object=object0
    
    insurance_specific_requirements=Insurance_specific_requirements('This is insurance specific requirements',insurance_requirements[0],insurance_requirements[1])
    # print(insurance_specific_requirements.insurance_object)
    
    return car_specific_requirements, maintainance_specific_requirements, insurance_specific_requirements
# totalrequirements = Requirements()
# car_specific_requirements = totalrequirements[0]
# maintainance_specific_requirements = totalrequirements[1]
# print(car_specific_requirements.type)
# print(maintainance_specific_requirements.type)

def Preferences(): # preferences, names are consistant with domain schema

    with open(os.getcwd()+'/input/preferences.csv') as f:
        reader = csv.reader(f)
        preferences_total=list(reader)
        extra_functions=preferences_total[0][0]
        extra_requirements=preferences_total[1][0]
    # print(extra_functions)
    # print(extra_requirements)

    class Preferences:
        def __init__(self,defaultvalue):
            self.type=defaultvalue

    class Extra_functions(Preferences):
        def __init__(self,type,functions):
            super(Extra_functions,self).__init__(type)
            self.extra_functions=functions    
    ExtraFunctions = Extra_functions('This is extra functions', extra_functions)
    

    class Extra_requirements(Preferences):
        def __init__(self,type,requirements):
            super(Extra_requirements,self).__init__(type)
            self.extra_requirements=requirements
    ExtraRequirements = Extra_requirements('This is extra requirements', extra_requirements)

    return ExtraFunctions, ExtraRequirements
# totalpreferences = Preferences()
# extra_functions = totalpreferences[0]
# extra_requirements = totalpreferences[1]
# print(extra_functions.extra_functions)
# print(extra_requirements.extra_requirements)


# end_time= time.time()
# print('running time1 =', end_time-start_time)