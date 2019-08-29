from PIL import Image, ImageFilter
from time import sleep


def main1():
    image = Image.open('./res/guido.jpg')
    print(image.format, image.size, image.mode)
    image.show()


# 剪裁图像
def main2():
    image = Image.open('./res/guido.jpg')
    rect = 80, 20, 310, 360
    image.crop(rect).show()


# 缩略图
def main3():
    image = Image.open('./res/guido.png')
    size = image.size[0]/2, image.size[1]/2
    image.thumbnail(size)
    image.save('./res/suo_nue.png')


# 缩放和黏贴
def main4():
    image1 = Image.open('./res/luohao.png')
    image2 = Image.open('./res/guido.jpg')
    rect = 80, 20, 310, 360
    guido_head = image2.crop(rect)  # 裁剪
    width, height = guido_head.size
    image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
    image1.save('./res/image-paste.png')


# 旋转和翻转
def main5():
    image = Image.open('./res/guido.jpg')
    image.show()
    image.rotate(180).show()
    image.transpose(Image.FLIP_LEFT_RIGHT).show()


# 滤镜效果
def main6():
    image = Image.open('./res/guido.jpg')
    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    main3()
