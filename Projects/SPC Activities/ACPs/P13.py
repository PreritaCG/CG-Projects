r = int(input(" Enter the Total Number of Rows  : "))

print("Mirrored Right Triangle Star Pattern") 
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j <= r -i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()