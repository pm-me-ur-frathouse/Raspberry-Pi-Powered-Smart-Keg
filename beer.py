import RaspberryBeer as rb

keg = rb.keg
user = rb.user

if keg != empty and user != geed:
    if user.isFrat == True:
        if user.isPike == True:
            rb.performButtchug()
        else:
            rb.pourBeer()
    elif user.isPledge == True:
        rb.pretendToPour()
elif keg != empty:
    print(“Fuck off geed”)
else:
    print(“Keg is empty”)

