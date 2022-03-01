from pyzbar.pyzbar import decode
from PIL import Image
from . import DB

def BarcordRead(img_path):

    # 画像ファイルの指定

    #image = "static/image/test1234/img1.jpg"
    
    #media_directory_path = r'C:\Users\s-sangeeth-k\Desktop\django\labelreader\media\'
    #image_name = str(img_path)
    
    image = img_path
    print('image path is ', image)
    # バーコードの読取り
    data = decode(Image.open(image))
    print(data)
    # コード内容を出力
    try:
        bar=(data[0][0].decode('utf-8', 'ignore'))
        bar = str(bar)
        #print("撮影したバーコード:",bar)
    except:
        res = 'バーコードを撮影してください。'
        return res

    return bar