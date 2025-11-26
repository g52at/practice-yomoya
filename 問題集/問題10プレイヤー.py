player_name = "bob"
player_hp = 100
player_attack = 10
player_defence = 2
player_spawn_message = "好きな文字を入れてください"
player_attack_message = "攻撃時メッセージ"
player_death_message = "かっこいいダウン時のメッセージを入れてください"

enemy_hp = 100
enemy_attack = 5
enemy_defence = 5
enemy_spawn_message = "敵の登場にふさわしいメッセージ"
enemy_attack_message = "かっこいいセリフを入れてください"
enemy_death_message = "悪役にふさわしいメッセージを入れてください"
# 初期化だけ変数
dmg = 0
player_action = 0

def action():
    global player_hp
    global enemy_hp
    player_action = int(input("アクションを指定してください（1=攻撃,2=回復(10%)"))
    if player_action == 1:
        dmg = player_attack - enemy_defence
        print(player_name + '　は' + str(dmg) + 'のダメージを与えた！')
        print(player_attack_message)
        enemy_hp -= dmg
    elif player_action == 2:
        heal = int(player_hp / 10)
        player_hp += heal
        print("現在HP:" + str(player_hp) + "、HPを" + str(heal) + "回復した！")
    else:
        print("不正な操作が検出されました")

    def enemy_action():
        global player_hp
        global enemy_hp
        enemy_action = 
        if player_action == 1:
            dmg = player_attack - enemy_defence
            print(player_name + '　は' + str(dmg) + 'のダメージを与えた！')
            print(player_attack_message)
            enemy_hp -= dmg
        elif player_action == 2:
            heal = int(player_hp / 10)
            player_hp += heal
            print("現在HP:" + str(player_hp) + "、HPを" + str(heal) + "回復した！")

action()