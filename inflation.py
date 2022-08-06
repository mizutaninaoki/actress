import os
import cv2
import glob
from scipy import ndimage
"""
Faceディレクトリから画像を読み込んで回転、ぼかし、閾値処理をしてFaceEditedディレクトリに保存する.
"""
ImgSize=(250,250)
SearchName = ["aragaki","hirose","ishihara","takei"]

for name in SearchName:
    print("{}の写真を増やします。".format(name))
    in_dir = "./Face/"+name+"_face/*"
    out_dir = "./FaceEdited/"+name
    os.makedirs(out_dir, exist_ok=True)
    in_jpg=glob.glob(in_dir)
    img_file_name_list=os.listdir("./Face/"+name+"_face/")
    for i in range(len(in_jpg)):
        img = cv2.imread(str(in_jpg[i]))
        # 回転
        for ang in [-10,0,10]:
            img_rot = ndimage.rotate(img,ang)
            img_rot = cv2.resize(img_rot,ImgSize)
            fileName=os.path.join(out_dir,str(i)+"_"+str(ang)+".jpg")
            cv2.imwrite(str(fileName),img_rot)
            # 閾値
            img_thr = cv2.threshold(img_rot, 100, 255, cv2.THRESH_TOZERO)[1]
            fileName=os.path.join(out_dir,str(i)+"_"+str(ang)+"thr.jpg")
            cv2.imwrite(str(fileName),img_thr)
            # ぼかし
            img_filter = cv2.GaussianBlur(img_rot, (5, 5), 0)
            fileName=os.path.join(out_dir,str(i)+"_"+str(ang)+"filter.jpg")
            cv2.imwrite(str(fileName),img_filter)

print("画像の水増しに大成功しました！")