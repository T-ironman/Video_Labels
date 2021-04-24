# -*- encoding=utf-8 -*-
from  PIL import Image
'''
直方图能够描述一幅图像中颜色的全局分布，而且容易理解和实现，所以入门级的图像相似度计算都是使用它的。

直方图算法是对源图像与要筛选的图像进行直方图数据采集

对采集的各自图像直方图进行归一化再使用巴氏系数算法对直方图数据进行计算

最终得出图像相似度值，其值范围在[0, 1]之间0表示极其不同，1表示极其相似（相同）。

算法步骤大致可以分为两步，根据源图像与候选图像的像素数据，生成各自直方图数据。

第二步：使用第一步输出的直方图结果，运用巴氏系数（Bhattacharyya coefficient）算法，计算出相似程度值。

'''
def calc_similar_by_path(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    return calc_similar(li, ri)

def make_regalur_image(img, size=(256, 256)):
    """我们有必要把所有的图片都统一到特别的规格，在这里我选择是的256x256的分辨率。"""
    return img.resize(size)


def calc_similar(li, ri):
    return sum(hist_similar( l.histogram(), r.histogram() ) for l, r in zip(split_image(li), split_image(ri))) / 16.0
#将两张图片的全等面积像素进行对比

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def split_image(img, part_size = (64, 64)):
    w, h = img.size
    pw, ph = part_size
    assert w % pw == h % ph == 0
    return [img.crop((i, j, i+pw, j+ph)).copy() for i in range(0, w, pw) \
            for j in range(0, h, ph)]
    #返回图片部分像素

if __name__ == '__main__':
    img1_path = '1.jpg'
    img2_path = '3.jpg'
    similary = calc_similar_by_path(img1_path, img2_path)
    print("两张图片相似度为:%s" % similary)


