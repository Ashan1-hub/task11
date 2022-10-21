import math

menu = input("please select 'investment' or 'bond' : \n").lower() # chose weather they want to bond or investment calulator
    
if menu == 'investment': # the formuola has been provided in the format below for investment
    deposite = int(input("please enter the amount yoy want to depositing : \n"))

    interest = float(input("please enter the interest amount you would like :\n"))# the interst amount you want (eg. 5-10-8..%)
    num_of_years = int(input("please enter the number of years you want to invest for:\n")) # how many years you want to invest for (eg.).1-20-30
    interest_1 = input("pleace enter if you want 'simple' or 'compound' interest : \n")

    if  interest_1 == 'simple' :
        a_calculation = (deposite*(1+interest * num_of_years))
        print(round(a_calculation))
    elif interest =='compound':
        a_2calculation = deposite*math.pow((1+interest),num_of_years)
        print(round(a_2calculation))

if menu == 'bond': # this is the bond formula. have used the formula provided 
    property_amount = float(input("enter the amount of the property :\n"))
    repayments = float(input("enter the number of months you plan on repaying the bond : \n")) # how much you will pay back
    bond_inter = float(input("enter interest rate "))/100/12 # 
    total = (bond_inter * property_amount) /(1-(1+ bond_inter))**(- repayments)
    print(total)

else :
       print("you haven't entered anything")
