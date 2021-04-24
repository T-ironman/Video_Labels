from moviepy.editor import VideoFileClip
import os

#找到video文件夹后，在video文件夹下为每个视频单独创建一个文件夹用于存放其关键帧，并将时长高于5分钟的视频除去，只留下时长低于5分钟的视频
#now_path，exe程序存在的路径，video_lists为所有要转换的视频列表
#save_path为保存转换视频的路径，save_video_lists为转换后的视频列表
def Video_Resize(now_path,video_lists,save_path,mp4 = '.mp4',avi = '.avi',flv = '.flv',mkv = '.mkv'):
    save_video_lists = []
    save_img_path_dicts = {}

    #这个循环用于转换视频分辨率
    all_path = os.path.abspath(now_path)
    for video_list in video_lists:
        video_name = video_list.lstrip(all_path)
        save_video = os.path.abspath(os.path.join(save_path,video_name))
        clip = VideoFileClip(video_list)
        clip = clip.resize(newsize=(416,416))
        clip.write_videofile(save_video)

    #这个循环用于保存已经转换的视频到一个列表中
    for dir_item in os.listdir(save_path):
        all_path = os.path.abspath(os.path.join(save_path, dir_item))
        if os.path.isdir(all_path):
            continue
        else:
            if dir_item.endswith(mp4):
                save_video_lists.append(all_path)
            else:
                pass

    #这个循环用于为转换的视频创建对应的文件夹并且将对应的视频和文件夹生成到字典里
    for save_video_list in save_video_lists:
        video_dir_name = save_video_list.lstrip(save_path)
        if video_dir_name.endswith(mp4):
            value = save_video_list.rstrip(mp4) + 'mp4'
            save_img_path_dicts[save_video_list] = value
            video_dir_name = video_dir_name.strip(mp4) + 'mp4'
            if is_dir_there(save_path,video_dir_name) is not True:
                mkdir_dir(save_path,video_dir_name)
            else:
                pass
        # elif video_dir_name.endswith(avi):
        #     video_dir_name = video_dir_name.strip(avi) + 'avi'
        #     if is_dir_there(save_path, video_dir_name) is not True:
        #         mkdir_dir(save_path, video_dir_name)
        #     else:
        #         pass
        # elif video_dir_name.endswith(flv):
        #     video_dir_name = video_dir_name.strip(flv) + 'flv'
        #     if is_dir_there(save_path, video_dir_name) is not True:
        #         mkdir_dir(save_path, video_dir_name)
        #     else:
        #         pass
        else:
            continue
    return save_video_lists,save_img_path_dicts



#判断video_path路径中是否存在tht_path_you_want文件夹
#如果存在返回bool True，不存在返回bool False
def is_dir_there(video_path,the_path_you_want):
    dir_items = os.listdir(video_path)
    #print(dir_items)
    for dir_item in dir_items:
        all_path = os.path.abspath(os.path.join(video_path,dir_item))
        if os.path.isdir(all_path):
            if the_path_you_want in dir_item:
                return True
            else:
                continue
        else:
            pass

    return False

#输入参1：某个文件夹路径
#输入参2：想要在该文件夹路径下创建的文件夹名字
def mkdir_dir(video_path,the_dirname_that_you_want_creat):
    path = os.path.abspath(os.path.join(video_path,the_dirname_that_you_want_creat))
    os.mkdir(path)



#找到当前文件夹下的video文件夹，如果没有找到则创建一个video文件夹
#返回值：当前文件夹下的video文件夹绝对路径
def dir_for_video(now_path,dir_name):
    if is_dir_there(now_path,dir_name) is not True:
        mkdir_dir(now_path,dir_name)
    else:
        pass
    video_path = os.path.abspath(os.path.join(now_path, dir_name))
    return video_path


















