
nakupovalni_listek = []

x = raw_input("Ali zelite dodati izdelek na nakupovalni seznam? ")
if x.capitalize() == "Ne":
    print "Hvala za obisk, se vidimo naslednjic."
elif x.capitalize() == "Da":
    y = raw_input("Napisite izdelek, ki ga zelite dodati: ")
    nakupovalni_listek.append(y)
    z = raw_input("Ali zelite dodati se kaksen izdelek? ")
    if z.capitalize() == "Ne":
        print nakupovalni_listek
        print "Hvala za nakup, se vidimo naslednjic."
    else:
        while z.capitalize() == "Da":
            y = raw_input("Napisite izdelek, ki ga zelite dodati: ")
            nakupovalni_listek.append(y)
            z = raw_input("Ali zelite dodati se kaksen izdelek? ")
        else:
            print nakupovalni_listek
            print "Hvala za nakup, se vidimo naslednjic."


