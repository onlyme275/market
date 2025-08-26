#----------------------------------------------
#|| display the following product inside shop
#----------------------------------------------

def display():
    shoes = []
    file = "shoe.txt"
    with open(file, "r") as filename:
        for line in filename:
            if line.strip():
                _type, brand, quantity, rate, place = line.strip().split(", ")
                shoes.append({"type": _type, "brand": brand, "qty": int(quantity), "rate": int(rate), "place": place})
            else:
                print("No such file.")
    print("\n*******************************************************")            
    print("|   ----- Available shoes are mentioned below -----   |")
    print("*******************************************************\n")
    print(f"{'No':<5} {'Type':<20} {'Brand':<15} {'Quantity':<10} {'Rate':<10} {'Place':<10}")
    print("-" * 80)
    
    for i, shoe in enumerate(shoes, start=1):
        print(f"{i:<5} {shoe['type']:<20} {shoe['brand']:<15} {shoe['qty']:<10} {shoe['rate']:<10} {shoe['place']:<10}")
    print("-" * 80)

