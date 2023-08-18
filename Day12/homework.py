#თქვენი სახელის და გვარისგან შექმენით სია  და დაპრინტეთ ხმოვნების რაოდენობა
#შექმენით სია რომელშიც პირველი სამი ელემენტი იქნება თქვენი სახელი : მშობლის სახელი და მეორე მშობლის სახელი
# ხოლო ბოლო სამი ელემენტი იქნება , ყველა გვარი დაპრინტეთ ყველა ადამიანის დაჯგუფებული სახელი და გვარი.


#part N1

name = "Lasha wamalaidze"

lower_name = name.lower()
xmovanebi = ['a', 'e', 'i', 'o', 'u']
xmovanebi_datvla = 0
for char in lower_name:
    if char in xmovanebi:
        xmovanebi_datvla += 1


print("Xmovanebis raodenoba :", xmovanebi_datvla)

#part N2
names=["lasha" , "baqo" , "marika" , " wamalaidze" ,"wamalaidze" , "zhvania"]
print(names[0] , names[3] , names[1] , names[4] , names[2] , names[5])