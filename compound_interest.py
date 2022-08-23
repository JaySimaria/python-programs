#4-7-22
#compound interest
def compound_interest(Principle,rate,time):
    #calculate ci
    Amount=Principle*(pow((1+rate/100),time))
    CI= Amount-Principle
    print("The compound Interest is",CI)


#Driver code
compound_interest(15000,45.5,10)