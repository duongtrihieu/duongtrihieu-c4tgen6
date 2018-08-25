command = input(print("welcome to our shop, what do you want (C,R,U,D)"))
shop_item = ["T-Shirt, Sweater"]

if command == "C" or command == "c":
    print(shop_item)
elif command == "C" or command == "c":
    new_item = input(print("new item? "))
    shop_item.append(new_item)
elif command == "U" or command == "u":
    position = int(input(print("Update position? ")))
    vitri = position - 1
    shop_item.pop(vitri)
    shop_item.insert(vitri,input(print("new item? ")))
    print("our item: ", shop_item)
elif command == "D" or command == "d":
    xoavitri = int(input(print("Delete position? ")))

