# 1-mashq
s = input("Kirish: ")
words = s.split()
code = ''.join(w[0] for w in words if w)
print("Chiqish:", code)


# 2-mashq
royxat = [4, 7, 2, 5, 1, 10]
natija = []

for i in range(len(royxat)):
    natija.append(i * royxat[i])

print(natija)
