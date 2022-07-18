#horizontal path/length
#x1------------------------------->x2
# 0
# roboX - robot coordinate

lenght = 20
roboX = 5

##########################################part 2 #####

print("\n")
for x in range(1,lenght):
    if x==roboX:
        print("R",end="")
    else:
        print("-", end="")
        ###################################
    
print("\n")