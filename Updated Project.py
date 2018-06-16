def edit():
    s = int(input("Enter Size: ")) #initialize string size
    value1 = []
    value2 = []
    value3 = value1
    for i in range(s):
        n = str(input("Enter Character: "))
        value1.append(n)    #inserting values into array
    print(value1)
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    size = int(input("Enter Size: "))   #initializing the array size for second string to be converted from first string
    for i in range(size):
        temp = "NULL"
        select = int(input("Choose: \n1. Insert \n2. Delete \n3. Copy \n4. Twiddle \n5. Replace \n6. Kill \nEnter: "))
        if select == 1:
            val = input("Input: ")
            value2.insert(i+1,val)  #inserting value in array
            a = a+1     #cost calculation
        elif select == 2:
            del value1[i]   #deleting value from array
            value1.insert(i, '')
            b = b+1     #cost calculation
        elif select == 3:
            value2.append(value1[i])    #copying value from one array to another
            c = c+1     #cost calculation
        elif select == 4:
            #swapping or twiddling characters in array
            temp = value1[i]
            value1[i] = value1[i+1]
            value1[i+1] = temp
            value2.append(value1[i])
            value2.append(value1[i+1])
            d = d+1     #cost calculation
        elif select == 5:
            del value1[i]   #deleting value from index
            val = input("Input: ")
            value1.insert(i,val)
            value2.append(value1[i])    #replacing by another character at index
            e = e+1     #cost calculation
        elif select == 6:
            print("Main String: " + str(value3))
            print("Editing in Main String: " + str(value1))
            print("Obtained String: " + str(value2))
            #Calculation total cost by each operation
            print("Cost: \nInsertion: %d \nDeletion: %d \nCopying: %d \nTwiddling %d \nReplacing: %d \nKilling: 1"%(a,b,c,d,e))
            #killing cost of operation will always be 1
            sum = a+b+c+d+e+1
            print("Total Cost: ",sum)
            return 0
        else:
            print("Invalid Input...")
        i = i+1
        print("Main String: "+str(value3))
        print("Editing in Main String: "+str(value1))
        print("Obtained String: "+str(value2))

print("Edit Distance Code")
edit()      #Function call