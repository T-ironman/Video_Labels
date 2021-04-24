import os

def img_detect(img,
               cfg_tiny_duc = 'cfg/yolov3-tiny.cfg',
               weight_tiny_duc = 'cfg/yolov3-tiny.weights',
               cfg_duc= 'cfg/yolov3.cfg',
               weight_duc= 'cfg/yolov3.weights'):
    detect_cmd = "darknet.exe detect %s %s %s" % (cfg_duc,weight_duc,img)
    #detect_cmd = "darknet.exe detect %s %s %s" % (cfg_duc, weight_duc, img)
    img_detect_file = os.popen(detect_cmd)
    img_detect_results = img_detect_file.readlines()
    img_detect_file.close()
    labels = []
    #对内容识别的字符串进行处理
    if len(img_detect_results) == 0:
        print("darknet识别错误")
        os._exit(0)  # 异常处理：darknet识别错误，程序自动结束
    del img_detect_results[0] #删除第一个元素，剩下的列表元素全是标签和得分情况
    if len(img_detect_results) > 0:
        for img_detect_result in img_detect_results:
            find_you = img_detect_result.find(':', 0, len(img_detect_result))
            if find_you != -1:
                label = img_detect_result[:find_you]
                labels.append(label)
        print(labels)
        return labels
    else:
        return '-1'


