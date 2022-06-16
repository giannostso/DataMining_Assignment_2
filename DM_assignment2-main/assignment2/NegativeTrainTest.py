from pathlib import Path
import os
import pandas as pd

p = Path('.')
fake = p / 'op_spam_v1.4'/ 'negative_polarity' / 'deceptive_from_MTurk'
real = p / 'op_spam_v1.4'/ 'negative_polarity' / 'truthful_from_Web'

fake_folds = [x for x in fake.iterdir() if x.is_dir()]
real_folds = [x for x in real.iterdir() if x.is_dir()]

for i in range(5):
    filesfake = [os.listdir(fake_folds[i])]
    filesreal = [os.listdir(real_folds[i])]
    print(fake_folds[i])
    #f_list = []
    #r_list = []
    text_list = []
    target_list = [] # 0 real , 1 fake
    for j in range(len(filesfake[0])):
        #create the paths for both the fake and the real review
        f_txt= os.path.join(fake_folds[i], filesfake[0][j])
        r_txt = os.path.join(real_folds[i], filesreal[0][j])
        #open each txt and save the text into the designated list
        #fake
        File_object = open(f_txt, "r")
        txt = File_object.readlines()
        File_object.close()
        #f_list.append(txt[0])
        text_list.append(txt[0])
        target_list.append(1)
        #real
        File_object = open(r_txt, "r")
        txt = File_object.readlines()
        File_object.close()
        #r_list.append(txt[0])
        text_list.append(txt[0])
        target_list.append(0)
    d = {'Review': text_list, 'Fake': target_list}
    name = "fold" + str(i+1)+ ".csv"
    df = pd.DataFrame(d)
    df.to_csv(name, index=False)
    """
    #places to save
    name_fake = "fake_fold" + str(i+1) + ".txt"
    name_real = "real_fold" + str(i+1) + ".txt"
    with open(name_fake, 'w') as f:
        for item in f_list:
            f.write("%s\n" % item)
    with open(name_real, 'w') as f:
        for item in r_list:
            f.write("%s\n" % item)
            """