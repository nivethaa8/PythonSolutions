def TOH (n, fromRod, toRod, spareRod):
    if n==1:
        print ("Move disk 1 from", fromRod, "TO ROD", toRod)
        return
    TOH (n-1, fromRod, spareRod, toRod)
    print ("move disk", n, "from rod", fromRod, "TO ROD", toRod)
    TOH (n-1, spareRod, toRod, fromRod)


TOH(3, "left", "right", "middle")
