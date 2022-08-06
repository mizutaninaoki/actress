import os

SearchNames = ["aragaki","hirose","ishihara","takei"]

for name in SearchNames:
    files = os.listdir(f"./Original/{name}")
    for file in files:
        # 000123.jpgみたいなファイル名の000部分を削除
        changed_filename = str(int(file.replace('.jpg', '')))
        # 変更前ファイル
        path1 = f'./Original/{name}/{file}.jpg'
        # 変更後ファイル
        path2= f'./Original/{name}/{changed_filename}.jpg'
        # ファイル名の変更
        os.rename(path1, path2)
