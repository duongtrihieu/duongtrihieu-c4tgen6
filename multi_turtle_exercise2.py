from turtle import*

turtle_list = []
for i in range(6):
    t = Turtle()
    turtle_list.append(t)

n = len(turtle_list)
print("i have", n ,"turtle")

position = int(input("turtle position: "))
tcolor = input("turtle color: ")
command = input("your command(fd, bd, lt, rt): ").lower()
turtle_list[position - 1].color(tcolor)
if command == "fd":
    turtle_list[position - 1].fd(300)
elif command == "bd":
    turtle_list[position - 1].backward(300)
elif command == "lt":
    turtle_list[position - 1].lt(90)
elif command == "rt":
    turtle_list[position - 1].rt(90)
else:
    print("wrong command! ")

d = 0
for t in turtle_list:
    t.lt(d)
    t.fd(100)
    d = d + 60

mainloop()