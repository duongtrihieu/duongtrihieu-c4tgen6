from turtle import*

turtle_list = []
for i in range(6):
    t = Turtle()
    turtle_list.append(t)
tposition = input("turtle position: ")
tcolor = input("turtle color: ")
tshape = input("turtle shape: ")

cmd = input("your command: ").lower()
cmd_list = cmd.split(" ")

turtle_list[tposition].color(tcolor)
turtle_list[tposition].shape(tshape)

for cmd in cmd_list:
    if cmd == "fd":
        turtle_list[tposition].fd(200)
    elif cmd == "bd":
        turtle_list[tposition].backward(200)
    elif cmd == "rt":
        turtle_list[tposition].rt(90)
    elif cmd == "lt":
        turtle_list[tposition].lt(90)
    else:
        print("wrong command! ")

mainloop()
