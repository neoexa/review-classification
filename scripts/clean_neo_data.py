import os, shutil

POS_CLASS = "./neo_data/pos/"
NEG_CLASS = "./neo_data/neg/"

for the_file in os.listdir(POS_CLASS):
    file_path = os.path.join(POS_CLASS, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

for the_file in os.listdir(NEG_CLASS):
    file_path = os.path.join(NEG_CLASS, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
