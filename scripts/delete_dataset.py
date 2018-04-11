import os, shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CLASS = ROOT_DIR + "/../dataset/"
POS_CLASS = CLASS + "pos/"
NEG_CLASS = CLASS + "neg/"


if os.path.exists(CLASS):
    if os.path.exists(POS_CLASS):
        for the_file in os.listdir(POS_CLASS):
            file_path = os.path.join(POS_CLASS, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    else:
        print "NO DIRECTORY /pos/"

    if os.path.exists(NEG_CLASS):
        for the_file in os.listdir(NEG_CLASS):
            file_path = os.path.join(NEG_CLASS, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    else:
        print "NO DIRECTORY /neg/"
else:
    print "NO DIRECTORY /dataset/"



print("\r" + "DONE. \n")