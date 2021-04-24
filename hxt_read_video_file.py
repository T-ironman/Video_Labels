import os
import datetime as dt


def what_time_now():
    now_time = dt.datetime.now().strftime('%F-%T')
    return now_time


#如果某个文件夹路径不存在，则创建该空文件夹
def creat_dir(dir_item):
    if os.path.exists(dir_item) is not True:
        os.mkdir(dir_item)
    else:
        pass

#获取输入视频的时长
def getLength(input_video):
    cmd = 'ffprobe -i %s -show_entries format=duration -v quiet -of csv="p=0"' % input_video
    output =os.popen(cmd,'r')
    output = output.read()
    return output.rstrip('\n')


#支持mp4,avi,flv,mkv视频格式
#返回参数1：当前所在文件夹绝对路径
#返回参数2：视频文件列表
def read_path():
    video_lists = []
    now_path = os.getcwd()
    print("当前所在位置：",now_path)
    for dir_item in os.listdir(now_path):
        all_path = os.path.abspath(os.path.join(now_path,dir_item))
        #print(all_path)
        if os.path.isdir(all_path):
            #read_path(all_path)
            continue
        else:
            if dir_item.endswith('.mp4'):
                if float(getLength(dir_item)) < 300:
                    video_lists.append(all_path)
                else:
                    pass
            else:
                pass
    if len(video_lists) >= 1:
        pass
    else:
        print("当前文件夹下没有读取到支持格式的视频文件")
        os._exit(0)    # 异常处理：如果没有获取到视频文件，程序自动结束
    print("%s:...."% (what_time_now()))
    print("%s:视频文件已读取到列表中" % (what_time_now()))
    return now_path,video_lists

if __name__ == '__main__':
    print(read_path())
