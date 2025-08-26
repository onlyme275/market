from display import display
import datetime

#-------------------------------------------------------------------------
#|| As you can restock your value in it, by including more quantities
#-------------------------------------------------------------------------

def restock():
    shoes = []
    file = "shoe.txt"
    with open(file, "r") as filename:
        for line in filename:
            if line.strip():
                types, brand, quantity, price, place = line.strip().split(", ")
                shoes.append({"types": types, "brand": brand, "quantity": int(quantity), "price": int(price),"place": place})

    try:    
        vendor = input("Enter a vendor name: ")
        product_name = input("Enter a product (brand) name: ")
    except:
        print("Invalid input! ")
        return

    try:
        quantity = int(input("Enter a quantity to restock: "))
    except Exception as ex:
        print("Quantity must be a number!")
        return
    
    if quantity <= 0:
        print("You cannot enter 0 or any negative value in quantity.")
        return

    hello = False
    for shoe in shoes:
        if shoe["brand"].lower() == product_name.lower():
            shoe["quantity"] += quantity       
            hello = True
            break

    if not hello:
        print("Product not found in System!")
        return

    with open(file, "w") as filess:
        for s in shoes:
            filess.write(f"{s['types']}, {s['brand']}, {s['quantity']}, {s['price']}, {s['place']}\n")
            
#----------------------------------------------------------
# || generate bill of the restock value
#----------------------------------------------------------

    inputfile = []
    inputfile.append("================== Restock Bill ==================\n")
    inputfile.append(f"Vendor name : {vendor}\n")
    inputfile.append(f"Date/Time   : {datetime.datetime.now()}\n")
    inputfile.append(f"Product     : {product_name}\n")
    inputfile.append(f"Quantity    : {quantity}\n")
    inputfile.append(f"Price       : Rs. {shoe['price']}\n")
    inputfile.append("==================================================\n")


    time = datetime.datetime.now()
    with open(f"{vendor}{product_name}{time}.txt", "w") as outputfile:
        outputfile.writelines(inputfile)

    print(f"Restock complete.")
    print("thanks for visit!")
