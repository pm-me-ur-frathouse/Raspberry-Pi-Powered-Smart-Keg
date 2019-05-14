import RaspberryBeer as rb

keg = rb.keg
user = rb.user

if keg.isEmpty == False:
    if user.isFrat == True:
        if user.isPike == True:
            rb.performButtchug()
        else:
            rb.pourBeer()
    elif user.isPledge == True:
        rb.pretendToPour()
    else:
        print(“Fuck off geed”)
else:
    print(“Keg is empty”)

