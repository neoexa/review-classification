import os, shutil

folder_pos = './working_set/pos/'
folder_neg = './working_set/neg/'

for the_file in os.listdir(folder_pos):
    file_path = os.path.join(folder_pos, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

for the_file in os.listdir(folder_neg):
    file_path = os.path.join(folder_neg, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
