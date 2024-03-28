import glob
import shutil
import os


for orig_obj in glob.glob(r"data/*.pdf"):   
    # print(orig_obj)
    # print(os.path.split(orig_obj)[1])   #ファイル名のみを取得
    # print(os.path.split(orig_obj)[0])   #フォルダ名を取得
    # print(os.path.basename(orig_obj))   #拡張子を含むファイル名
    # print(os.path.splitext(os.path.basename(orig_obj)))
    # print(os.path.splitext(os.path.basename(orig_obj))[0])
    print(os.path.splitext(os.path.basename(orig_obj))[0][-6:-2])  #後ろから6文字目から4文字
    dest_dir = r"data/" + os.path.splitext(os.path.basename(orig_obj))[0][-6:-2]
    # print(dest_dir)
    # print(os.path.exists(dest_dir))
    if os.path.exists(dest_dir):
        shutil.move(orig_obj, dest_dir)
    else:
        os.mkdir(dest_dir)
        shutil.move(orig_obj, dest_dir)