#თქვენი სახელის და გვარისგან შექმენით სია  და დაპრინტეთ ხმოვნების რაოდენობა
#შექმენით სია რომელშიც პირველი სამი ელემენტი იქნება თქვენი სახელი : მშობლის სახელი და მეორე მშობლის სახელი
# ხოლო ბოლო სამი ელემენტი იქნება , ყველა გვარი დაპრინტეთ ყველა ადამიანის დაჯგუფებული სახელი და გვარი.


#part N1
saxeli_gvari=["L" , "a" , "s" , "h" , "a" , "w" ,"a","m","a","l","a","i","d","z","e"]
num=0
i=0
while (i < len(saxeli_gvari)):
    if saxeli_gvari[i] == "a" or saxeli_gvari[i] == "e" or saxeli_gvari[i] == "i" or saxeli_gvari[i] == "o" or saxeli_gvari[i]=="u":
        num=num+1
        i=i=1
        print(num)

    












#part N2
names=["lasha" , "baqo" , "marika" , " wamalaidze" ,"wamalaidze" , "zhvania"]
print(names[0] , names[3] , names[1] , names[4] , names[2] , names[5])