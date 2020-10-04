print('inserisci la tua età')
eta = input()
if int(eta) >= 18 and int(eta) < 21:
    print('sei maggiorenne in italia')
elif int(eta) >= 21:
    print('sei maggiorenne sia in italia sia negli stati uniti')
else:
    print('sei minorenne')