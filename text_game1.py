player = {
    "NAME": "Hiếu",
    "HP": 200,
    "ATK": 50,
    "SPD": 20,
    "DEF": 100,
}

s_orc = {
    "NAME": "Orc nhỏ",
    "HP": 150,
    "ATK": 20,
    "SPD": 30,
    "DEF": 30,
}

l_orc = {
    "NAME": "Orc lớn",
    "HP": 300,
    "ATK": 40,
    "SPD": 10,
    "DEF": 150,
}

def combat(attacker, defender):
    print(attacker["NAME"], "đang đánh", defender["NAME"])
    damage = attacker["ATK"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] = abs(damage)
        print(attacker["NAME"], "lost", damage, "HP")

print("bạn đang ở trong 1 tòa lâu đài")
print("bạn có 2 lựa chọn: ")
print("1.ra khỏi lâu đài")
print("2.vào trong lâu đài")
cmd = ("lựa chọn của bạn: ")
if cmd == "1":
    print("có hai con đường: ")
    print("1.con đường đất vào rùng")
    print("2.con đường nhựa vào thành phố kế bên")
    cmd = input("bạn sẽ đi con đường nào")
    if cmd == "1":
        print("bạn gặp 1 con orc")
        print("bạn có 2 lựa chọn: ")
        print("1.đánh nó")
        print("2.bỏ chạy")
        cmd == input("bạn sẽ chọn gì?")
        if cmd == "1":
            while True:
                combat(player,s_orc)
                if player["HP"] <= 0 or s_orc["HP"] <= 0:
                    break
                combat(s_orc,player)
                if player["HP"] <= 0 or s_orc["HP"] <= 0:
                    break
            if player["HP"] >= 0:
                print("bạn đã vượt qua thủ thách đầu tiên")
                print("bạn tiếp tục đi trên con đường của mình")
                print("sau khi đánh nhau vs orc nhỏ")
                print("khu rừng chìm vào màn đêm")
                print("bạn ko nhìn thấy gì cả")
                print("trước mạt bạn có ánh lửa")
                print("bạn có 2 lựa chọn: ")
                print("1.chạy đến đó")
                print("2.tránh xa đó")
                cmd = input("bạn sẽ làm gì? ")
                if cmd == "1":
                    print("bạn gặp 1 con orc lớn")
                    print("nó chạy đến đánh bạn")
                    print("banjn có 2 lựa chọn")
                    print("1.ở lại đánh nó")
                    print("2.chạy đi")
                    cmd = input("bạn sẽ làm gì? ")
                    if cmd == 1:
                        while True:
                            combat(l_orc,player)
                            if player["HP"] <= 0 or l_orc["HP"] <= 0:
                                break
                            combat(player,l_orc)
                            if player["HP"] <= 0 or l_orc["HP"] <= 0:
                                break
                        if player["HP"] >= 0:
                            print("bạn đã hoàn thành thử thách và chiến thắng.")
                            print("hết game")
                        elif player["HP"] <= 0:
                            print("bạn đã chết")
                            print("hãy reset game")
                    elif cmd == "2":
                        print("bạn dần kiệt sức và chạy chậm lại")
                        print("con orc bắt đc bạn và bạn chết")
            elif player["HP"] <= 0:
                print("bạn đã thua")
                print("hãy reset game")
    elif cmd == "2":
        print("bạn gặp 1 băng cướp")
        print("bạn sẽ làm gì")
        print("1.bỏ đi")
        print("2.đánh nhau")
        cmd = input("bạn sẽ làm gì? ")
        if cmd == "1":
            print("bạn bị thị trưởng đuổi đi vì ko giúp người dân")
            print("bạn chết ngoài rìa thành phố vì đói và thú dữ")
        elif cmd == "2":
            print("băng cướp rất đông")
            print("bạn bị chúng đánh chết")

elif cmd == "2":
    print("ko ai cho bạn vào lâu đài và bạn bị chết ngoài lâu đài")
