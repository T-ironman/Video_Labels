from aip import AipImageClassify
import time

"""我的AppID, API Key, Secret Key"""



APP_ID = 'xxx'        # 请添加你在百度智能云申请的APP_ID
API_Key = 'xxx'  # 请添加你在百度智能云申请的API_Key
Secret_Key = 'xxx'  # 请添加你在百度智能云申请的Secret_Key
hxt = AipImageClassify(APP_ID, API_Key, Secret_Key)

#读取某张图片
def get_image(image_path):
    img = open(image_path,'rb')#二进制形式只读打开文件
    return img.read()#读取整个文件，将文件内容放到一个字符串变量中

#通用物体识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_advancedGeneral(image_path):
    image = get_image(image_path)
    result = hxt.advancedGeneral(image)
    #print(result)
    keyword = ((result['result'])[0])['keyword']
    score = ((result['result'])[0])['score']
    return keyword,score

#菜品识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_dishDetect(image_path):
    image = get_image(image_path)
    result = hxt.dishDetect(image)
    #print(result)
    name = ((result['result'])[0])['name']
    probability = ((result['result'])[0])['probability']
    return name,probability

#车辆识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_carDetec(image_path):
    image = get_image(image_path)
    result = hxt.carDetect(image)
    #print(result)
    name = ((result['result'])[0])['name']
    score = ((result['result'])[0])['score']
    color = result['color_result']
    color_and_name = "%s%s" % (color,name)
    return color_and_name,score

#logo商标识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_logoSearch(image_path):
    image = get_image(image_path)
    result = hxt.logoSearch(image)
    #print(result)
    if result['result_num'] is not True:
        name = '非logo'
        probability = 0
        return name,probability
    else:
        name = ((result['result'])[0])['name']
        probability = ((result['result'])[0])['probability']
        return name,probability

#动物识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_animalDetect(image_path):
    image = get_image(image_path)
    result = hxt.animalDetect(image)
    #print(result)
    name = ((result['result'])[0])['name']
    score = ((result['result'])[0])['score']
    return name,score

#植物识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_plantDetect(image_path):
    image = get_image(image_path)
    result = hxt.plantDetect(image)
    #print(result)
    name = ((result['result'])[0])['name']
    score = ((result['result'])[0])['score']
    return name,score

#地标识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_landmark(image_path):
    image = get_image(image_path)
    result = hxt.landmark(image)
    #print(result)
    mark = ((result['result'])['landmark'])
    if mark is True:
        return mark
    else:
        mark = '非地标'
        return mark

#食材识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_ingredient(image_path):
    image = get_image(image_path)
    result = hxt.ingredient(image)
    #print(result)
    name = ((result['result'])[0])['name']
    score = ((result['result'])[0])['score']
    return name,score

#红酒识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_redwine(image_path):
    image = get_image(image_path)
    result = hxt.redwine(image)
    #print(result)
    name = (result['result'])['wineNameCn']
    if name is True:
        return name
    else:
        name = '非红酒'
        return name

#货币识别
#输入：一张图片
#输出：概率最大的标签
#输出type:str
def hxt_currency(image_path):
    image = get_image(image_path)
    result = hxt.currency(image)
    #print(result)
    name = (result['result'])['currencyName']
    if name is True:
        return name
    else:
        name = '非货币'
        return name

def load_one_image(image_path):
    labels = {}
    score_lists = []
    words = {}
    time.sleep(1)
    keyword,score = hxt_advancedGeneral(image_path)
    labels[keyword] = score
    #print("通用物体识别：",keyword,score)
    time.sleep(1)
    name, probability = hxt_dishDetect(image_path)
    labels[name] = probability
    time.sleep(1)
    #print("菜品识别：",name, probability)
    color_and_name,score = hxt_carDetec(image_path)
    labels[color_and_name] = score
    time.sleep(1)
    #print("车辆识别：",color_and_name,score)
    name,probability = hxt_logoSearch(image_path)
    labels[name] = probability
    time.sleep(1)
    #print("logo商标识别：",name,probability)
    name,score = hxt_animalDetect(image_path)
    labels[name] = score
    time.sleep(1)
    #print("动物识别：",name,score)
    name, score = hxt_plantDetect(image_path)
    labels[name] = score
    time.sleep(1)
    #print("植物识别：",name, score)
    mark = hxt_landmark(image_path)
    labels[mark] = 0
    time.sleep(1)
    #print("地标识别：",mark)
    name,score = hxt_ingredient(image_path)
    labels[name] = score
    time.sleep(1)
    #print("食材识别：",name,score)
    name = hxt_redwine(image_path)
    labels[name] = 0
    time.sleep(1)
    #print("红酒识别：",name)
    name = hxt_currency(image_path)
    labels[name] = 0
    time.sleep(1)
    #print("货币识别：",name)
    #print("labels：",labels)
    for label in labels:
        if "非菜" in label or "非车类" in label or "非logo" in label or "非动物" in label or "非植物" in label or "非地标" in label or "非果蔬食材" in label or "非红酒" in label or "非货币" in label:
            continue
        else:
            score_lists.append(labels[label])
            words[labels[label]] = label
    return words[max(score_lists)]


if __name__ == '__main__':
    image_path = 'G:/IMAGE_PYTHON/horses.jpg'
    name = hxt_advancedGeneral(image_path)
    print(name)




