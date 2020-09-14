row = raw_input("Enter a row (A-N): ")
seat = input("Enter a seat (1-17 for A-C & 1-16 D-N): ")

if (row == "E" and (1 <= seat <= 3 or 10 <= seat <=13)) or ((row == "J") and (8 <= seat <= 12)) or ((row == "M") and (9 <= seat <= 10)) or ((row=="N") and (7 <= seat <= 15)):
    print ("Unavailable")
elif ((row == "D") and (14 <= seat <= 16)):
    print ("Not valid seat")
elif ((row == "D") and ((3 <= seat <= 4) or (10 <= seat <= 11))):
    print ("Wheelchair accessible")

else:
    print ("Available")


