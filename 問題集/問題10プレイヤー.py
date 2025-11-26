player_name = "bob"
player_hp = 100
player_attack = 10
player_defence = 2
player_spawn_message = "好きな文字を入れてください"
player_attack_message = "攻撃時メッセージ"
player_death_message = "かっこいいダウン時のメッセージを入れてください"

enemy_name = "python"
enemy_hp = 100
enemy_attack = 5
enemy_defence = 5
enemy_spawn_message = "敵の登場にふさわしいメッセージ"
enemy_attack_message = "enemy_attack()"
enemy_death_message = "悪役にふさわしいメッセージを入れてください"
# 初期化だけ変数
dmg = 0
player_action = 0
end_flag = 0

def player_action():
    global player_hp
    global enemy_hp
    player_action = int(input("アクションを指定してください（1=攻撃,2=回復(10%)"))
    if player_action == 1:
        dmg = player_attack - enemy_defence
        print(player_name + '　は' + enemy_name + 'に' + str(dmg) + 'のダメージを与えた！')
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
    dmg = enemy_attack - player_defence
    print(enemy_name + '　は' + player_name +'に' + str(dmg) + 'のダメージを与えた！')
    print(enemy_attack_message)
    player_hp -= dmg

def stats():
    print("プレイヤーのHP:"+ str(player_hp),end="")
    print("敵のHP" + str(enemy_hp))

for i in range(100):
    player_action()
    enemy_action()
    stats()
#勝敗の処理
    if player_hp < 1:
        print("プレイヤーが敗北しました…")
        break
    if enemy_hp < 1:
        print("敵が敗北しました！おめでとうございます！")
        break
    if i > 99:
        print("長すぎるので終了です（バグが発生した場合もこのメッセージが出力されます")