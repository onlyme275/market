from display import display
import datetime

'''  This is a page where retailer can import the product  '''

def add():
    while True:
        product_name = input("Enter a type name to add: ").strip().lower()
        with open("shoe.txt", "r") as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split(",") 
                    if parts[0].lower() == product_name:
                        print("We already have that brand! Move to 'sell product' instead.")
                        return
                
#---------------------------------------------------
#  || checking condition and taking output
#---------------------------------------------------

    
        try:
            vendor = input("Enter a vendor name: ")
            model_name = input("Enter model name: ").strip().replace(" ","")
            if  not model_name.isalpha():
                print("Enter a valid name!")
                break 

            quantity = int(input("Enter quantity: ")) 
            if quantity <= 0:
                print('Enter a valid quantity!')
                break

            rate = int(input("Enter rate: "))
            if rate <= 0:
                print('Enter a valid quantity!')
                break

            place = input("Enter a (domestic/international): ").lower()
            if  place not in ["domestic", "international"]:
                print("Enter a valid name!")
                return

            with open("shoe.txt", "a") as file:
                file.write(f"{product_name}, {model_name}, {quantity}, {rate}, {place}\n")

            include = []
            include.append("*****************************************************************************\n")
            include.append("=========================== Adding product =================================\n")
            include.append("******************************************************************************\n")
            include.append("vendor name: "+vendor+"\n")
            include.append(f"{str(datetime.datetime.now())}\n")
            include.append("Model name: "+model_name+"\n")
            include.append("quantity: "+str(quantity)+"\n")
            include.append("rate: "+str(rate)+"\n")
            include.append("The place is in: "+place+"\n"+"============================================================\n")

            with open(f"{vendor}{datetime.datetime.now()}.txt", "w") as files:
                files.writelines(include)

            so = input("Do you want to add more? (yes / no): ").strip().lower()
            if so == "no":
                break
#----------------------------------------------------
# | If no input goes then exception & again repeated
#----------------------------------------------------

        except:
            print(" Enter valid input! ")

#----------------------------------------------------------------------------------------------
''' This is main role where, I can sell product to customer as per their desire.'''
#----------------------------------------------------------------------------------------------

def sell():
    shoes = []
    file = "shoe.txt"
    with open(file, "r") as filename:
        for line in filename:
            if line.strip():
                types, brand, quantity, rate, place = line.strip().split(", ")
                shoes.append({"type": types, "brand": brand, "qty": int(quantity), "rate": int(rate), "place": place})
    
    display()
    total_discount = 0
    card = []
    name = input("Enter the name of the customer: ")
    while not name.isalpha():
        name = input("Enter the name of the customer: ")

    number = input("Enter a number: ")
    for i in range(1):
        if not name.isalpha():
            print("Enter a valid name!")
            break
    address = input("Enter a address: ")
    while True:
        try:
            num = int(input("Enter a shoe number to select, or enter 0 to finish: "))
            if num <= 0:
                print("Please, Enter a valid detail!")
                break
            
            elif 1 <= num <= len(shoes):
                selected = shoes[num - 1]
                quantity = int(input(f"Enter quantity for {selected['type']} product: "))
                if 0 < quantity <= selected["qty"]:
                    amount = selected["rate"] * quantity 
                    amount_vat = (selected["rate"] * quantity ) + (0.13 * quantity)
                    discount = 0
                    if quantity > 10:
                        if selected['place'].lower() == "domestic":
                            discount = amount * 0.07
                        else:
                            discount = amount * 0.05
                    total_discount += discount
                    card.append({'type': selected['type'], 'brand': selected['brand'], 'qty': quantity, 'rate': selected['rate']})
                    selected['qty'] -= quantity

                    with open(file, "w") as f:
                        for shoe in shoes:
                            line = f"{shoe['type']}, {shoe['brand']}, {shoe['qty']}, {shoe['rate']}, {shoe['place']}\n"
                            f.write(line)
                else:
                    print("Invalid quantity. Check stock and try again.")
            else:
                print("Invalid shoe number.")
        except Exception as ex:
            print("Invalid input. Please enter numbers only.")
    
    
    

        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# || This is where customer detail show as thier is excuted datetime, name, discount if more than 10 also with vat adding and many more as you can explore.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    if card: 
        print("*********************************************************************")
        print("\n   ------------------- Final Bill -------------------------")
        print("\n**********************************************************************")
        print(f"Customer Name: {name}","   ", end = " ")
        purchased_date = datetime.datetime.now()
        print( purchased_date)
        print()
        print(f"{'Type':<20} {'Brand':<15} {'Qty':<5} {'Rate':<10} {'Subtotal':<10}")
        print("-" * 60)
        for item in card:
            subtotal = item['qty'] * item['rate']
            print(f"{item['type']:<20} {item['brand']:<15} {item['qty']:<5} {item['rate']:<10} {subtotal:<10}")

        print("-" * 60)
        print(f"Total: Rs. {amount - total_discount}")
        print(f"Total with VAT Rs.{amount_vat}")
        print(f"Total Discount: Rs. {total_discount}")
        print("-" * 60)
        include = []
        include.append(f"********************************************************************************\n")
        include.append(f"========================= Generated a bill =====================================\n")
        include.append(f"********************************************************************************\n")
        include.append(f"    Customer name: {name}           Time purchased: {purchased_date}\n")
        include.append(f" Contact no. {number}     Address: {address}\n")
        include.append(f" Total: Rs. {amount}\n")
        include.append(f" Total with VAT: Rs. {amount_vat}\n")
        include.append(f" Total discount: Rs. {total_discount}\n ===========================================================================")

#---------------------------------------------------------------------
#  || As I, xitiz create a next txt file for saved  customer detail.
#---------------------------------------------------------------------

        with open(f"{name}{purchased_date}.txt","w") as files:
            files.writelines(include)
    else:
        print("No items purchased.")

