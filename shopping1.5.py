print("Welcome to fancy shopping mall")
customerTotal = 0
Next = True
cust_items = ""

itemsList = {
    "lamp": 39.99,
    "laptop": 250.55,
    "scissors": 1.99,
    "mouse": 5.99
}

cust_inpu = {
    "(A) lamp : 39.99" : "A",
    "(B) laptop: 250.55" : "B",
    "(C) scissors: 1.99" : "C",
    "(D) mouse 5.99" : "D"
}

items = "A" , "B" , "C", "D"

instock= {
    "lamp": 4,
    "laptop": 1,
    "scissors": 2,
    "mouse": 3
}


print("We currently have these items in stock:")
for key, value in cust_inpu.items():
    print (key)

while Next is True:
    customer = input("What would you like to buy today?: (A), (B), (C), (D) ")
    customer = customer.capitalize()  



    if customer == str("A"):
        print("We currently have " + str(instock["lamp"]) + " lamps in stock")
        lampquan = input("How many Lamps would you like to buy? ")
        if float(lampquan) > float(instock["lamp"]):
            print("Sorry we do not have that many lamps in stock")

        else:
            cust_items += str(lampquan) + " Lamp(s),"
            customerTotal += itemsList["lamp"]
            customerTotal += itemsList["lamp"] * (float(lampquan) - 1)
            instock["lamp"]= int(instock["lamp"]) - int(lampquan)

    elif customer == str("B"):
        print("We currently have " + str(instock["laptop"]) + " laptops in stock")
        laptopquan = input("How many laptops would you like to buy? ")
        if float(laptopquan) > float(instock["laptop"]):
            print("Sorry we do not have that many laptops in stock")

        else:
            cust_items += str(laptopquan) + " Laptop(s),"
            customerTotal += itemsList["laptop"]
            customerTotal += itemsList["laptop"] * (float(laptopquan) - 1)
            instock["laptop"]= int(instock["laptop"]) - int(laptopquan)

    elif customer == str("C"):
        print("We currently have " + str(instock["mouse"]) + " mice in stock")
        mousequan = input("How many mice would you like to buy? ")
        if float(mousequan) > float(instock["mouse"]):
            print("Sorry we do not have that many mice in stock")

        else:    
            cust_items += str(mousequan) + " Mice,"    
            customerTotal += itemsList["mouse"]
            customerTotal += itemsList["mouse"] * (float(mousequan) - 1)
            instock["mouse"]= int(instock["mouse"]) - int(mousequan)

    elif customer == str("D"):
        print("We currently have " + str(instock["scissors"]) + " scissors in stock")
        scissorsquan = input("How many scissors would you like to buy? ")
        if float(scissorsquan) > float(instock["scissors"]):
            print("Sorry we do not have that many scissors in stock")

        else:    
            cust_items += str(scissorsquan) + " Scissors,"  
            customerTotal += itemsList["scissors"]
            customerTotal += itemsList["scissors"] * (float(scissorsquan) - 1)
            instock["scissors"]= int(instock["scissors"]) - int(scissorsquan)

    else: print("Sorry the item you entered is not in our database, Please try again.")
        
    exito = input("Would you like to buy anything else? (y)es, (n)o: ")
    exito = exito.lower()

    if exito == "n": #goes to total calculation
        Next = False
    if exito == "y": #repeats the ask loop
        Next = True

def checkoutInfo(customerTotal, rebate):
    print("The items you will be buying today are: " + cust_items)
    print("your subtotal is: $"+ (format( customerTotal , ".2f")) )

    if rebate == 0:
        #calculate tax
        custTotal = custTotal * 1.08
        endo = (format(custTotal, ".2f"))

    elif rebate == 1:
        #discount
        print("You will receive a 5% discount on your subtotal today")
        customerTotal = customerTotal / 1.05
        customerTotale = (format( customerTotal , ".2f")) 
        print("your subtotal after discount is: $"+ str(customerTotale))
        #calculate tax
        customerTotal = customerTotal * 1.08
        endo = (format(customerTotal, ".2f"))
    print("Your total after tax is : $" + str(endo))
        
# Total
if Next is False:
    if customerTotal > 200:
        rebateEligible = 1
        checkoutInfo(customerTotal , rebateEligible )

    elif customerTotal < 200:
        rebateEligible = 0
        checkoutInfo(customerTotal , rebateEligible )
