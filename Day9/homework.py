#დავალება N1
#მომხმარებელს უნდა შემოვატანინოთ მისი ასაკი და რამდენი წლისაცაა იმდენჯერ 
#დაპრინტოს გილოცავ შენ გახდი 0,1,2 წლის
age = int(input("Your Age: "))
while age > 0:
    print("glocav shen gaxdi" , age)
    age= age-1

#დავალება N2 დაპრინტეთ 1 დან 100მდე ყველა კენტი რიცხვი
for i in range(1,102,2):
    print(int(i))