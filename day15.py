from PIL import Image, ImageFilter
from time import sleep


def main1():
    image = Image.open('./res/guido.jpg')
    print(image.format, image.size, image.mode)
    image.show()


# 剪裁图像
def main2():
    filename=str(input('请输入文件名'))
    image = Image.open('./res/'+filename)
    print(image.size)
    rect1 = image.size[0]
    rect2 = image.size[1]
    i = 1050
    j = 1
    k = 0
    while i <= rect2:
        print(k, i)
        rect = 0, k, 750, i
        image.crop(rect).save('./res/' + str(j) + '.png')
        j += 1
        k += 1050
        i += 1050
        if i >= rect2:
            print(i)
            rect = 0, k, 750, rect2
            image.crop(rect).save('./res/' + str(j) + '.png')


# 缩略图
def main3():
    image = Image.open('./res/guido.jpg')
    size = 128, 128
    image.thumbnail(size)
    image.save('./res/guido1.png')
    image.show()


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
    main2()
