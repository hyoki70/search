
### 検索ツールサンプル
### これをベースに課題の内容を追記してください


# 検索ソース
import csv
f = open("kimetu.csv","r") 
dataread = csv.reader(f)
source = next(dataread)
f.close()


### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        source.append(word)
        print("{}は見つかりませんでした".format(word))


if __name__ == "__main__":
    search()


f = open("kimetu.csv","w")
writer = csv.writer(f)
writer.writerow(source)
f.close()