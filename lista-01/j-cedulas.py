c=int(input())
cem=c//100
cin=c%100//50
vin=c%100%50//20
dez=c%100%50%20//10
f=c%100%50%20%10//5
t=c%100%50%20%10%5//2
o=c%100%50%20%10%5%2//1
print(c)
print(cem, "nota(s) de R$ 100,00")
print(cin, "nota(s) de R$ 50,00")
print(vin, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(f, "nota(s) de R$ 5,00")
print(t, "nota(s) de R$ 2,00")
print(o, "nota(s) de R$ 1,00")