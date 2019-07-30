import re

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""


def main1():
    username = input('请输入用户名')
    qq = input('请输入qq号')
    m1 = re.match(r'^\w{6,20}$', username)
    if not m1:
        print('请输入有效的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的qq')
    if m1 and m2:
        print('你输入的信息是有效的')


def main2():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    pattern1 = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = ''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------华丽的分隔线--------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


# 替换字符串中不良内容
def main3():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
    print(purified)


# 拆分长字符串
def main4():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    setence_list = re.split(r'[,.，。]', poem)
    while '' in setence_list:
        setence_list.remove('')
    print(setence_list)


if __name__ == '__main__':
    main4()
