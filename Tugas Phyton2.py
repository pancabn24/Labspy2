print("Program penentu bilangan terbesar")
print("==================================")

print ("Masukan nilangan yang di inginkan")

X= int(input("Masukan bilangan pertama:"))
Y= int(input("Masukan bilangan kedua  :"))
Z= int(input("Masukan bilangan ketiga :"))
if X > Y and Y > Z:
    print(X, "Terbesar dari 3 bilangan yang di input")
elif Y > X and Y > Z:
    print(Y, "Terbesar dari 3 bilangan yang di input")
else:
    print(Z, "Terbesar dari 3 bilangan yang di input")
