import sys 


money = int(sys.argv[1])
if money >= 50:
    print(money // 50, 'Billetes de 50 euros')
    money = money%50
if money >=20:
    print(money // 20, 'Billetes de 20 euros')
    money = money%20
if money >=10:
    print(money // 10, 'Billetes de 10 euros')
    money = money%10

if money >=5:
    print(money // 5, 'Billetes de 5 euros')
    money = money%5

if money >=2:
    print(money // 2, 'Monedas de 2 euros')
    money = money%2

if money >=1:
    print(money // 1, 'Monedas de 1 euros')
    