def table(num):
    
    i=1
    while i<= 10:
        print(num, "*", i, " = ", i*num);
        i += 1
        
try:
    num = int(input("Enter the number: "))
    print("You entered:", num)
    table(num)
except ValueError:
    print("Invalid value!")            
    