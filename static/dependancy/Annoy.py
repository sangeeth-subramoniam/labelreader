MAGENTA = '\033[45m'
END = '\033[0m'
import configparser,time
import os
from tkinter import EXCEPTION
from . import DB
import tensorflow as tf
from annoy import AnnoyIndex
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras import Model
from tensorflow.keras.applications.vgg16 import preprocess_input


from labelreader.settings import BASE_DIR

def Ruigi_Img(imgpath):

    progress_file_path = os.path.join(BASE_DIR, 'static/progress/progress.txt')

    
    try:
        f = open(progress_file_path, "w")
        f.write("5")
        f.close()
    except:
        print('パーセンテージ更新できません')

    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    try:
        f = open(progress_file_path, "w")
        f.write("15")
        f.close()
    except:
        print('パーセンテージ更新できません')

    """比較したい画像の特徴量抽出"""
    start = time.time()

    try:
        f = open(progress_file_path, "w")
        f.write("20")
        f.close()
    except:
        print('パーセンテージ更新できません')


    base_model = tf.keras.applications.vgg16.VGG16(weights='imagenet')#weights=''にすれば処理は早くなるが、比較精度がかなり落ちる。  2.378833293914795[sec] 
    
    try:
        f = open(progress_file_path, "w")
        f.write("26")
        f.close()
    except:
        print('パーセンテージ更新できません')

    end = time.time()

    try:
        f = open(progress_file_path, "w")
        f.write("29")
        f.close()
    except:
        print('パーセンテージ更新できません')

    model = Model(inputs=base_model.input, outputs=base_model.get_layer("fc2").output)
    img_path = imgpath
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)

    try:
        f = open(progress_file_path, "w")
        f.write("45")
        f.close()
    except:
        print('パーセンテージ更新できません')

    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    fc2_features = model(x)#model.predict(x) model(x) 0.9550037384033203[sec]

    try:
        f = open(progress_file_path, "w")
        f.write("56")
        f.close()
    except:
        print('パーセンテージ更新できません')

    """比較実行"""
    trained_model = AnnoyIndex(4096)
    model = r'C:\\Users\\s-sangeeth-k\\Desktop\\django\\labelreader\\static\\data\\result.ann'
    trained_model.load(model)#学習済みデータファイルをロード
    # 第一引数に検索したいインデックス番号を指定。第二引数は得る個数。今回は3個get
    result = trained_model.get_nns_by_vector(fc2_features[0], 3, search_k=-1, include_distances=True)
    print(MAGENTA,"類似画像TOP3:",result,END)
    ruigiimg = []
    i = 0
    threshold = 0.01
    y = float(threshold)
    for x in result[1]:
        x = 1 - x #Annoyの比較は0に近いほど似ているため1から引き、分かりやすくする。
        if x >= y:#閾値
            ruigiimg.append([result[0][i],x])
        i += 1
    
    try:
        f = open(progress_file_path, "w")
        f.write("70")
        f.close()
    except:
        print('パーセンテージ更新できません')

    print(MAGENTA,"閾値を超えた画像のリスト:",ruigiimg,END)
    
    try:
        f = open(progress_file_path, "w")
        f.write("80")
        f.close()
    except:
        print('パーセンテージ更新できません')

    
    try:
        f = open(progress_file_path, "w")
        f.write("90")
        f.close()
    except:
        print('パーセンテージ更新できません')

    
    end = time.time()
    s = end -start
    print(MAGENTA,'Annoy:{0}'.format(s) + "[sec]",END)
    
    
    try:
        f = open(progress_file_path, "w")
        f.write("99")
        f.close()
    except:
        print('パーセンテージ更新できません')
    
    return result