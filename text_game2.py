player = {
    "NAME": "Hiếu",
    "ATK": 100,
    "DEF": 50,
    "HP": 100,
    "SPD": 50,
}

enemy = {
    "NAME": "kẻ địch",
    "ATK": 50,
    "DEF": 40,
    "HP": 100,
    "SPD": 40,
}

m416 = {
    "NAME": "M416",
    "ATK": player["ATK"] + 20,
}

scar_l = {
    "NAME": "Scar-L",
    "ATK": enemy["ATK"] + 10,
}
def combat(attacker,defender):
    print(attacker["NAME"], "đang bắn", defender["NAME"])
    damage = attacker["ATK"] - defender["DEF"]
    if damage > 0:
        defender["HP"] -= damage
        print(defender["NAME"], "lost", damage, "HP")
    else:
        attacker["HP"] = abs(damage)
        print(attacker["NAME"], "lost", damage, "HP")

print("bạn đang ở trên máy bay")
print("chiếc máy bay đang bay ra đảo sanhok")
print("trên máy bay có 100 người bao gồm cả bạn")
print("bạn nhảy dù xuống hà tĩnh")
print("trong lúc nhảy dù, bạn thấy có 15 người")
print("bạn có 2 lựa chọn")
print("1.nhảy nhanh xuống nhà vệ sinh ngay dưới chân")
print("2.nhảy chậm xuống nhà kho to hướng 345")
cmd = input("bạn sẽ làm gì? ")
if cmd == "1":
    print("bạn nhặt đc cây M416 cùng 30 viên đạn 5.56")
    print("bạn đi ra ngoài thì thấy trước mặt có 1 thằng cầm scar-l")
    print("bạn có 2 lựa chọn: ")
    print("1.bắn nó")
    print("2.bỏ chạy")
    cmd = input("bạn sẽ làm gì? ")
    if cmd == "1":
        while True:
            combat(player,enemy)
            if player["HP"] <= 0 or enemy["HP"] <= 0:
                break
            combat(enemy,player)
            if player["HP"] <= 0 or enemy["HP"] <= 0:
                break
        if player["HP"] <= 0:
            print("bạn bị nó sấy chết")
            print("bạn ngu vl")
        elif player["HP"] > 0:
            print("bạn tiếp tục loot trong hà tĩnh")
            print("bạn tiến vào cái nhà kho")
            print("bạn thấy 1 thằng đang cầm kar98k ngắm 1 thằng")
            print("bạn có 3 lựa chọn: ")
            print("1.sấy nó")
            print("2.cầm chảo đập nó")
            print("3.ném bom nó")
            cmd = input("bạn sẽ làm gì")
            if cmd == "1":
                print("bạn giết đc nó")
                print("thằng nó vừa bắn nhìn thấy bạn")
                print("bạn ko còn đạn")
                print("trên tay bạn còn 1 quả choáng và cái chảo")
                print("bạn có 2 lựa chọn")
                print("1.chạy")
                print("ném flash và ra đập nó")
                cmd = input("bạn sẽ làm gì")
                if cmd == "1":
                    print("bạn chạy ra khỏi hà tĩnh với 1 flash và 1 chảo")
                    print("bạn bị bo ép chạy đến paradise resort")
                    print("bạn đi vào thì thấy có 1 thằng đang ở trên mái nhà")
                    print("nó ko nhìn thấy bạn")
                    print("bạn có 2 lựa chọn")
                    print("1.nhặt cây ak bên cạnh và sấy nó")
                    print("2.núp vào bụi cây")
                    cmd = input("bạn sẽ làm gì? ")
                    if cmd == "1":
                        print("ak quá giật và bạn cũng đéo phải là dj chip")
                        print("thế nên 30 viên đạn 7 bay vào mái nhà")
                        print("nó quay lại cho 1 viên kar vào đầu bạn")
                    elif cmd == "2":
                        print("trên bản đồ còn 6 thằng")
                        print("bạn vẫn đéo có gì ngoài cái chảo")
                        print("cú lừa vãi shit")
                        print("bo vào paradise")
                        print("bạn nhìn thấy 2 thằng team up")
                        print("bạn có 2 lựa chọn")
                        print("1.chạy ra cho nó bắn rồi report nó cho bluehole")
                        print("tiếp tục núp")
                        cmd = input("bạn sẽ làm gì? ")
                        if cmd == "1":
                            print("bạn có iq -200")
                            print("nhưng tổ quốc ghi công bạn")
                        elif cmd == "2":
                            print("1 thằng đẩy ngu bị chết")
                            print("trên map còn 4 thằng")
                            print("bạn chạy qua xác thằng vừa chết,chỉ còn 3 nade 1 lửa")
                            print("bạn nghe thấy tiếng bắn")
                            print("1 thằng vừa gục")
                            print("bạn đang ở top 3")
                            print("bạn lại tiếp tục chơi việt cộng soldier")
                            print("có thằng chạy đến cũng chơi việt cộng như bạn")
                            print("nhưng nó ko biết bạn núp bụi bên cạnh nó")
                            print("bạn có 2 lựa chọn: ")
                            print("1.tiến vào top 2")
                            print("2.chờ để trời định")
                            cmd = input("bạn sẽ làm gì")
                            if cmd == "1":
                                print("nó đéo hiểu chuyện gì xảy ra")
                                print("bạn có toàn bộ supplies của nó")
                                print("nhưng cú lừa là bạn bị lỗi game ko nhạt đc đồ")
                                print("thằng còn lại chạy xung quanh kiếm bạn")
                                print("nhưng lâu quá nên nó núp vào cái phòng nhỏ")
                                print("cái phòng đấy trong bo")
                                print("mọi lối lên đều dính bo")
                                print("bạn có 2 lựa chọn: ")
                                print("1.thoát game và lên page pubg vn chửi bluehole")
                                print("2.ném hết bom lên đấy và khô máu")
                                cmd = input("bạn sẽ làm gì")
                                if cmd == "1":
                                    print("bạn trẻ trâu vl")
                                elif cmd == "2":
                                    print("nó dính flash và ko nhìn thấy gì")
                                    print("thêm trái lửa và nó còn nửa cây máu")
                                    print("bạn lao lên bị bo đốt còn 1 giọt máu")
                                    print("bạn vụt 1 phát chảo vào nó")
                                    print("nó bắn lung tung đc 1 phát đạn vào người bạn")
                                    print("bây giờ bạn có 2 lựa chọn")
                                    print("1.donate cho thằng làm game")
                                    print("2.ko donate")
                                    cmd = input("bạn sẽ làm gì")
                                    if cmd == "1":
                                        print("bạn đc top 1 vì bạn vụt nhanh hơn phát đạn của nó")
                                    elif cmd == "2":
                                        print("ích kỉ vl")
                                        print("đéo donate thì đéo top 1")
                                        print("bạn vào top 2")
                            elif cmd == "2":
                                print("thằng còn lại nhìn thấy cả 2 trong bụi cỏ")
                                print("nó nhìn thấy vì nó là shroud")
                                print("bạn biết kết quả rồi đấy")
            elif cmd == "2":
                print("nó nghe thấy tiếng bước chân")
                print("nó quay lại cho bạn 1 băng vector")
                print("nó bật chat all bảo: that's cú lừa")
            elif cmd == "3":
                print("nó chết")
                print("nhưng có thằng bất ngờ xuất hiện từ sau")
                print("bạn ko kịp rút súng")
                print("đó là 1 cú lừa nữa")
    elif cmd == "2":
        print("bạn bị thằng khác bắn từ sau và bạn chết")
        print("that's cú lừa")
elif cmd == "2":
    print("chúng nó thấy bạn")
    print("chúng tập bắn chim")
    print("bạn chết trước khi chạm đất")
    print("bạn nhảy ngu vl")