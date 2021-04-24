import os
from hxt_rgb_to_hsv import RGB_TO_HSV
import hxt_pic_similar

''' 
save_video_lists        [视频的绝对路径]
save_img_path_dicts     {视频的绝对路径:视频的绝对路径对应的文件夹}

example:

    save_video_lists: ['G:\\My_code\\4_IMAGE_PYTHON\\video\\haha.mp4']
    save_img_path_dicts: {'G:\\My_code\\4_IMAGE_PYTHON\\video\\haha.mp4': 'G:\\My_code\\4_IMAGE_PYTHON\\video\\hahamp4'}
'''

def key_frame_from_ffmpeg(save_video_lists,save_img_path_dicts,value):
    for save_video_list in save_video_lists:
        save_path = save_img_path_dicts[save_video_list]
        #code = "ffmpeg -i %s -vf select='eq(pict_type\,I)' -vsync 2 -s 1920*1080 -f image2 %s/%%02d.jpg" % (save_video_list,save_path)
        code = "ffmpeg -i %s -vf select='eq(pict_type\,I)' -vsync 2 -f image2 %s/%%02d.jpg" % (save_video_list,save_path)
        a = os.popen(code)
        a.close()

        RGB_TO_HSV(save_path) #为每张RGB图像生成HSV图像

        images = os.listdir(save_path)
        l_r = []
        for image in images:
            if 'hsv' in image:
                image_path = os.path.abspath(os.path.join(save_path, image))
                l_r.append(image_path)
        i = 0
        key_frames = []
        while i < len(l_r) - 1:
            l = l_r[i]
            r = l_r[i + 1]
            i = i + 1
            core = hxt_pic_similar.calc_similar_by_path(l, r)
            if core < value:
                key_pic = r.lstrip(save_path + '/hsv')
                key_frames.append(key_pic)

        for key_frame in key_frames:
            images.remove(key_frame)

        for img in images:
            remove_img = os.path.abspath(os.path.join(save_path,img))
            os.remove(remove_img)




if __name__ == '__main__':
    key_frame_from_ffmpeg()