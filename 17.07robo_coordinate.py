#horizontal path/length
#x1------------------------------->x2
# 0
# roboX - robot coordinate

lenght = int(input('lenght - '))

if lenght <=2 or lenght>80 :
    print("not interest")
    quit()

roboX = int(input('place of roboX(0 < roboX <= lenght) - '))

if roboX>lenght or roboX<1:
    print('does not meet the conditions, try again')
    exit()

##########################################part 2 #####
x=1

print("\n")
while x <=lenght:
    if x==roboX:
        print("R",end="")
    else:
        print("-", end="")
        ###################################
    x +=1
print("\n")