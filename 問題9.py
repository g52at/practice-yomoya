# 簡単なゲームです、変更できる場所の数字を変更して3ターンで相手を倒せるようにしてください
import sys
# ---------------ここから変更できる場所---------------
player_name = "アンパンマン" #文字
player_hp_max = 100 #最大HP　
player_attack = 10 #攻撃力　
player_defence = 3 #防御力　
player_spawn_message = "来たなおじゃまむしめ"
player_attack_message = "出たなバイキンマン"
player_death_message = "顔が濡れて力が出ない"

enemy_name = "バイキンマン"
enemy_hp_max = 100 #最大HP
enemy_attack = 5 #攻撃力
enemy_defence = 5 #防御力
enemy_spawn_message = "はっひふっへほー！"
enemy_attack_message = "これでもくらえー！"
enemy_death_message = "ばいばいきーん！💫"
#---------------ここまで変更できる場所---------------


# ゲーム内処理用の初期化だけ変数
dmg = 0
player_action = 0
end_flag = 0
allow_command = [1,2]#コマンドの数
player_hp_now = player_hp_max
enemy_hp_now = enemy_hp_max
bar_length = 15
turn = 0

# 状態把握用
def stats():
    #print("プレイヤーのHP:"+ str(player_hp_now),end="")
    #print("敵のHP" + str(enemy_hp_now))
    player_percentage = player_hp_now / player_hp_max
    player_filled_length = int(bar_length * player_percentage)
    player_empty_length = bar_length - player_filled_length
    bar = '=' * player_filled_length
    empty = '-' * player_empty_length
    player_hp_info = f"{player_hp_now}/{player_hp_max}HP"
    print("player" + f"[{bar}/{empty}]{player_hp_info}")
    enemy_percentage = enemy_hp_now / enemy_hp_max
    enemy_filled_length = int(bar_length * enemy_percentage)
    enemy_empty_length = bar_length - enemy_filled_length
    enemy_bar = '=' * enemy_filled_length
    enemy_empty = '-' * enemy_empty_length
    enemy_hp_info = f"{enemy_hp_now}/{enemy_hp_max}HP"
    print("enemy " + f"[{enemy_bar}/{enemy_empty}]{enemy_hp_info}")

## プレイヤーの動作、1Tあたり1回
def player_action():
    global player_hp_now
    global enemy_hp_now
# 正常な数字が入力されるまで続行
    while True:
        player_action = input("アクションを指定してください（1=攻撃,2=回復(10%),stop=終了")
        try:
            if player_action == "stop":
                print("終了します")
                sys.exit()
            if int(player_action) not in allow_command:
                print("数字が範囲外です")
                stats()
                continue
            if not player_action.strip():  # 空文字・空白のみ
                print("何も入力されていません。数字を入力してください。")
                stats()
                continue
            print("debug_範囲内のコマンド")
            if int(player_action) == 1:
                dmg = player_attack - enemy_defence
                print(player_name + '　は' + enemy_name + 'に' + str(dmg) + 'のダメージを与えた！')
                print(player_attack_message)
                enemy_hp_now -= dmg
            elif int(player_action) == 2:
                print("回復")
                heal = int(player_hp_max / 10)
                if player_hp_max < player_hp_now + heal:
                    print("debug_HPが過剰")
                    heal = player_hp_max - player_hp_now
                player_hp_now += heal
                print("現在HP:" + str(player_hp_now) + "、HPを" + str(heal) + "回復した！")
            else:
                print("数字が範囲外です")
                stats()
                break
            break
        except ValueError:    
            print("範囲外の入力")
            stats()
    print("dev_player_action:" + str(player_action))
def enemy_action():
    global player_hp_now
    global enemy_hp_now
    dmg = enemy_attack - player_defence
    print(enemy_name + '　は' + player_name +'に' + str(dmg) + 'のダメージを与えた！')
    print(enemy_attack_message)
    player_hp_now -= dmg

#1ターンごとの処理
print(player_spawn_message)
print(enemy_spawn_message)
for i in range(100):
    turn += 1
    player_action()#増やすともう一度攻撃できます
    enemy_action()
    stats()
#勝敗の処理
    if player_hp_now < 1:
        print(player_death_message)
        print("プレイヤーが敗北しました…")
        print("経過ターン数:" + str(turn))
        break
    if enemy_hp_now < 1:
        print(enemy_death_message)
        print("敵が敗北しました！おめでとうございます！")
        print("経過ターン数:" + str(turn))
        break
    if i > 99: #暴走対策
        print("100T経過したので中止します")