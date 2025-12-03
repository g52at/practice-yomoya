# 関数についてです
yasai_list = ["ピーマン","ナス","長ナス","トマト","ミニトマト","夕顔","和尚"]
def add_tomato():
    yasai_list.append("トマト")
    print("トマトを追加しました")

def check_tomato():
    tomato_count = 0
    for i in yasai_list:
        if i == "トマト":
            print("トマトをゲット！🍅",end='')
            tomato_count+=1
    print("")
    print("アイテム" + str(tomato_count) + "個のトマトを収穫しました！")
    for i in range(tomato_count):
        print("🍅",end='')
    print("")
# ここでトマトを追加しています
for i in range(9):
    add_tomato()

# ここでトマトを表示しています
check_tomato()

# 実習問題です、トマトを100個収穫してください
