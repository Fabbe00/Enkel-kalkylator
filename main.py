def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print(
        "1 Addera 2 Subtrahera 3 Multiplicera 4 Dividera"
    )
    while True:
        try:
            select = int( input("Välj funktion 1, 2, 3, 4 : "))
        
        except:
            print("Ingen siffra, försök igen")

        else:
            break

    nummer_1 = int( input ("Mata in första siffran: "))
    nummer_2 = int( input ("Mata in andra siffran: "))

    
    if select == 1:
        print(nummer_1, "+", nummer_2, "=", add(nummer_1, nummer_2))

    elif select == 2:
        print(nummer_1, "-", nummer_2, "=", subtract(nummer_1, nummer_2))

    elif select == 3:
        print(nummer_1, "*", nummer_2, "=", multiply(nummer_1, nummer_2))
   
    elif select == 4:
        print(nummer_1, "/", nummer_2, "=", divide(nummer_1, nummer_2) )

    fortsatt = input("Vill du använda miniräknaren igen? j/n : ")
    if fortsatt == "n":
        break