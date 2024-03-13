import glob
import shutil
import os 


dir_files ={}

for orig_obj in glob.glob(r"..\data\*.pdf"):
    print(os.path.splitext(os.path.basename(orig_obj))[0][-6:-2])  #後ろから6文字目から4文字
    dest_dir = r"..\data\\" + os.path.splitext(os.path.basename(orig_obj))[0][-6:-2]
    dir_files.setdefault(dest_dir,[])
    dir_files[dest_dir].append(orig_obj)

# print(dir_files)
#辞書からキーを取り出す
for dest_dir in dir_files.keys():
    # print(dest_dir)
    os.mkdir(dest_dir)
    for orig_obj in dir_files[dest_dir]:
        # print(orig_obj)
        shutil.move(orig_obj, dest_dir)