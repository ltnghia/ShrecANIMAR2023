import zipfile
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor
import time
import os
from os.path import join as path_join

from_dir = 'download'
des = 'unzip'

try:
    os.mkdir(des)
except:
    pass

def do_unzip(zip_path, out_path):
    print(zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(out_path)

filename = 'shrec23_test_final_dataset'
zip_path = path_join(from_dir, filename + '.zip')
do_unzip(zip_path, des)

filename = 'shrec23_test_predict'
zip_path = path_join(from_dir, filename + '.zip')
do_unzip(zip_path, des)

filename = 'shrec23_train_merge_final_dataset'
zip_path = path_join(from_dir, filename + '.zip')
do_unzip(zip_path, des)


