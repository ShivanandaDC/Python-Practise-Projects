def celsius(F):
    return (5/9)*(F-32)
def fahrenheit(C):
    return (C*(9/5))+32
temp = float(input("Enter the temperature:"))
select = int(input("Enter 1 for C to F \nEnter 2 for F to C\n"))
if select == 1:
    print(fahrenheit(temp), 'F')
elif select == 2:
    print(celsius(temp), 'C')
elif select != 1&2:
    print('Enter a valid number')

    
    
