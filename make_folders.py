import os
# オリジナル画像用のフォルダ
os.makedirs("./Original", exist_ok=True)
# 顔の画像用のフォルダ
os.makedirs("./Face", exist_ok=True)
# ImgSizeで設定したサイズに編集された顔画像用のフォルダ
os.makedirs("./FaceEdited", exist_ok=True)
# テストデータを入れる用のフォルダ
os.makedirs("./test", exist_ok=True)