from PIL import Image
import os


def shiyan():
    filename = str(input('请输入文件路径：'))
    print(filename)
    filelist = os.listdir(filename)
    path1 = filename.split('\\')[-2]
    isExists = os.path.exists(path1)
    if isExists:
        print('目录已存在，请删除目录或者查看目录')
    os.makedirs(path1)
    for i in range(len(filelist)):
        image = Image.open(filename + '/' + filelist[i])
        print('读取成功:%s' % filelist[i])
        rect1 = image.size[0]  # 宽度
        rect2 = image.size[1]  # 总高度
        if rect2 < 1050 and r'封面图' not in filelist[i]:
            image.save('./' + path1 + '/' + filelist[i])
            print('%s保存成功' % filelist[i])
            continue
        high2 = 1050  # 切割高度
        j = 1
        high1 = 0  # 初始高度
        if r'封面图' in filelist[i]:
            image.save('./' + path1 + '/' + '封面图.png')
            print('封面图保存成功')
            continue
        while high2 <= rect2:
            rect = 0, high1, rect1, high2  # 左上右下
            image.crop(rect).save(
                './' + path1 + '/' + filelist[i].split('.')[0] + '_' + str(j) + '.png')
            j += 1
            high1 += 1050
            high2 += 1050
            if high2 > rect2:
                rect = 0, high1, rect1, rect2
                image.crop(rect).save(
                    './' + path1 + '/' + filelist[i].split('.')[0] + '_' + str(j) + '.png')
        print('切割完成' + filelist[i])


if __name__ == '__main__':
    shiyan()
