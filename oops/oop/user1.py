def getInt(msg):
    v = input(msg+": ")
    try:
        v = int(v)
    except ValueError:
        print('Invalid Input!, Please Enter The Number only (no space)')
        return getInt(msg)
    else:
        print("getInt function End")
        return v
    
def tableInt(msg):
    v = input(msg+": ")
    try:
        v = int(v)
    except ValueError:
        print('Invalid Input!, Please Enter The Number only (no space)')
        return getInt(msg)
    else:
        print(m * num)
    print("getInt function End")

num = getInt("enter a number: ")
for m in range(1,13):
    print(f"{num} x {m} = {num * m}")