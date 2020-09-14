d = input ("Enter a bearing from 0 to 359: ")

if (0<d<=45) or (315<d<360):
    print ("North")
elif 46<d<134:
    print ("East")
elif 135<d<225:
    print ("South")
elif 226<d<314:
    print ("West")
else:
    print ("Entered Invalid bearing, try again.")

