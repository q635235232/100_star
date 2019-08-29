import cv2
import os


def suofang():
    img = cv2.imread('./res/guido.png')
    height, width = img.shape[:2]
    print(height, width)
    # suo
    size = (int(width * 0.5), int(height * 0.5))  # 缩小比例
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    cv2.imwrite('./res/suo.png', shrink)
    # fang
    fx = 1  # 放大宽度倍数
    fy = 2  # 放大高度倍数
    enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('./res/fang1.png', enlarge)


if __name__ == '__main__':
    suofang()
