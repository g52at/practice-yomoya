# 問題4ではエラーが出ていましたが、分岐処理を繰り返せばエラーをなくせます、3行目のisdigitで数字かどうか判定しています
num = input("数字を入力してください")
if num.isdigit():
    if num % 2 == 0:
        print('これは偶数です')
    else:
        print('これは奇数です')
else:
    print('数字以外が入力されました')