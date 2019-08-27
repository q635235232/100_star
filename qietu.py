from PIL import Image


# 剪裁图像
def main2():
    filename = str(input('请输入文件名'))
    print(filename)
    image = Image.open(filename)
    print(image.size)
    rect1 = image.size[0]
    rect2 = image.size[1]
    i = 1050
    j = 1
    k = 0
    while i <= rect2:
        print(k, i)
        rect = 0, k, 750, i
        image.crop(rect).save(filename.split('.')[0] + str(j) + '.png')
        j += 1
        k += 1050
        i += 1050
        if i >= rect2:
            print(i)
            rect = 0, k, 750, rect2
            image.crop(rect).save(filename.split('.')[0] + str(j) + '.png')


if __name__ == '__main__':
    main2()
