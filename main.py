import hxt_read_video_file
import hxt_video_resize
import hxt_Picture_Baidu_API
import hxt_Picture_Yolo_darknet_API
import hxt_label_spilt_time_alg
import os
import hxt_key_frame_from_ffmpeg
import datetime
#功能：读取路径下所有MP4视频，并将时长高于5分钟的视频除去，只留下时长低于5分钟的视频
#返回参数1：now_path表示当前路径
#返回参数2：video_lists表示当前路径需要转换的视频列表
def step_1():
    print("\n\n步骤1：处理视频列表")
    now_path,video_lists = hxt_read_video_file.read_path()
    return now_path,video_lists

#功能：当前文件夹下寻找video文件夹，如果没有就创建一个video文件夹。将列表里所有视频转换为416*416分辨率保存到该文件夹下
#随后，在video文件夹里为每一个视频创建一个文件夹用于保存从其中提取出来的关键帧
#返回参数1：save_video_lists表示转换后的视频列表
#返回参数2：每一个视频对应其文件夹的dicts
def step_2(now_path,video_lists):
    video_path = hxt_video_resize.dir_for_video(now_path,'video')
    print("\n\n步骤2：开始压缩视频分辨率")
    save_video_lists,save_img_path_dicts = hxt_video_resize.Video_Resize(now_path,video_lists,video_path)
    print(save_video_lists)
    print(save_img_path_dicts)
    print("\n\n%s所有视频分辨率压缩完成" % (hxt_read_video_file.what_time_now()))
    return save_video_lists,save_img_path_dicts

#功能：从video文件夹下的每一个视频中提取关键帧，并将其保存到对应的文件夹里
def step_3(save_videos,save_img_path,value):
    print("\n\n步骤3：提取关键帧")
    print("%s该过程将耗费一段时间，请稍等" % (hxt_read_video_file.what_time_now()))
    hxt_key_frame_from_ffmpeg.key_frame_from_ffmpeg(save_videos,save_img_path,value)
    print("%s关键帧提取完毕" %(hxt_read_video_file.what_time_now()))

#功能：对每个文件夹里的图片进行内容识别（调用百度图像识别API）
def step_4_baidu_cloud(video_lists,save_dicts):
    print("\n\n步骤4：内容分析")
    labels = []
    j = 1
    print("开始图像识别....")
    for video_list in video_lists:
        i = 1
        images_path = save_dicts[video_list]
        images = os.listdir(images_path)
        print("\n\n短视频%d：" % j)
        for image in images:
            image_path = os.path.abspath(os.path.join(images_path,image))
            label = hxt_Picture_Baidu_API.load_one_image(image_path)
            print("图片%d：%s" %(i,label))
            i = i + 1
            if label in labels:
                pass
            else:
                labels.append(label)
        print("%s短视频%d识别结束" % (hxt_read_video_file.what_time_now(),j))
        j = j + 1
        print("\n\n%s该短视频相关标签有:\n%s" % (hxt_read_video_file.what_time_now(), labels))

        # 该视频名字
        video_path = os.path.abspath(os.path.join(now_path, 'video'))
        video_name = (video_list.strip(video_path)).replace('.', '')

        # 把该视频的标签保存到txt文本里
        file_path = os.path.abspath(os.path.join(now_path, 'labels.txt'))
        file = open(file_path, 'a+')
        file.write("%s--识别方法:%s--视频%s--%s\n" % (hxt_read_video_file.what_time_now(), "百度API", video_name, labels))
        print("\n标签保存完成")

    print("图像识别结束....")

#yolo_图像识别
def step_4_yolo(now_path,video_lists,save_dicts):
    print("\n\n步骤4：内容分析")
    print("开始图像识别....")
    for video_list in video_lists:
        #print("aaaaa",hxt_read_video_file.what_time_now())
        images_path = save_dicts[video_list]
        images = os.listdir(images_path)
        if len(images) > 0:
            j = 0
            j = j + 1
            labels = []
            print("\n\n短视频%d：" % j)
            for image in images:
                image_path = os.path.abspath(os.path.join(images_path,image))
                label_lists = hxt_Picture_Yolo_darknet_API.img_detect(image_path)
                if label_lists == '-1':
                    continue
                else:
                    for label_list in label_lists:
                        labels.append(label_list)
                    # for label_list in label_lists:
                    #     if label_list in labels:
                    #         continue
                    #     else:
                    #         labels.append(label_list)
            #一个短视频出现的所有标签都在这个labels里
            final_labels = hxt_label_spilt_time_alg.hxt_label_spilt_time_alg(labels,0.5)
            print("final_labels",final_labels)
            print("%s短视频%d识别结束" % (hxt_read_video_file.what_time_now(),j))
            print("%s该短视频相关标签有:\n%s" % (hxt_read_video_file.what_time_now(), final_labels))

            # 该视频名字
            video_path = os.path.abspath(os.path.join(now_path, 'video'))
            video_name = (video_list.strip(video_path)).replace('.', '')

            # 把该视频的标签保存到txt文本里
            file_path = os.path.abspath(os.path.join(now_path, 'labels.txt'))
            file = open(file_path, 'a+')
            file.write("%s--识别方法:%s--视频%s--%s\n" % (hxt_read_video_file.what_time_now(), "YOLOv3", video_name, final_labels))
            print("\n标签保存完成")
        else:
            #该视频名字
            video_path = os.path.abspath(os.path.join(now_path, 'video'))
            video_name = (video_list.strip(video_path)).replace('.','')

            #把该视频的标签保存到txt文本里
            file_path = os.path.abspath(os.path.join(now_path, 'labels.txt'))
            file = open(file_path,'a+')
            file.write("%s--识别方法:%s--视频%s--%s\n" % (hxt_read_video_file.what_time_now(),"YOLOv3",video_name,'[\'no labels\']'))
            print("\n标签保存完成")

    print("\n\n图像识别结束....")


if __name__ == '__main__':
    #第一步读取当前路径下的视频文件
    now_path,video_lists = step_1()
    #print(now_path,video_lists)
    #第二步，把所有视频文件统一分辨率为416*416 //ffmpeg //moivepy
    save_video_lists,save_img_path_dicts = step_2(now_path,video_lists)
    #第三步，采集视频的关键帧opencv numpy
    step_3(save_video_lists,save_img_path_dicts,0.65)
    #第四步，Yolo内容识别
    step_4_yolo(now_path,save_video_lists,save_img_path_dicts)
    #第四步，百度API内容识别
    #step_4_baidu_cloud(save_video_lists,save_img_path_dicts)











