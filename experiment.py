p=int(input("Enter Number: "))
for i in range(0,p):
    for j in range(i,p):
        if i*i + j*j ==p:
            print([i,j])
