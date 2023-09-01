import turtle


t = turtle.Turtle()

# for background
screen = turtle.Screen()
screen.bgcolor("yellow")

#color and speed
# of turtle
# creating the house
t.color("black")
t.shape("turtle")
t.speed(4)

# for creating base of
# the house
t.fillcolor('cyan')
t.begin_fill()
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.right(90)
t.end_fill()

# for top of
# the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()

# for door and
# windows
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(75)
t.left(90)
t.forward(15)
t.left(90)
t.forward(200)
t.right(90)
t.forward(15)
t.right(90)
t.forward(75)






















#davaleba2
side=int(input("kvadratis etri  gverdis sigrdze :"))
p=side * 4
s=side * side
print("perimetri tolia :" ,p )
print("fartobi tolia :" , s)


#davaleba3

side1=int(input("samkutxedis gverdis sigrdze :"))
side2=int(input("meore gverdis sigrdze :"))
side3=int(input("mesame gverdis sigrdze :"))
perimetri=side1 + side2 + side3
print("samkutxedis perimetri udris :",perimetri)

#დავალება4
for num in range(99, 0, -1):
    if num > 1:
        bottles = "bottles" if num > 2 else "bottle"
        print(f"{num} {bottles} of beer on the wall, {num} {bottles} of beer.")
        print(f"Take one down and pass it around, {num - 1} {'bottles' if num - 1 > 1 else 'bottle'} of beer on the wall.\n")
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")

