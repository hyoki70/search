
### 検索ツールサンプル
### これをベースに課題の内容を追記してください


# 検索ソース
def read_kimetu():
    import csv
    f = open("kimetu.csv","r") 
    dataread = csv.reader(f)
    name_list = next(dataread)
    return name_list
    f.close()


### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print(f"{word}が見つかりした")
    else:
        source.append(word)
        print(f"{word}は見つかりませんでした")


def write_kimetu():
    import csv
    f = open("kimetu.csv","w")
    writer = csv.writer(f)
    writer.writerow(source)
    f.close()


if __name__ == "__main__":
    source = read_kimetu()
    search()
    write_kimetu()