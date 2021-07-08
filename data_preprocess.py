# coding: utf-8
import random


def data_split(full_list, ratio, shuffle=True):
    """
    数据集拆分: 将列表full_list按比例ratio（随机）划分为2个子列表sublist_1与sublist_2
    :param full_list: 数据列表
    :param ratio:     子列表1
    :param shuffle:   子列表2
    :return:
    """
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2


file_list = ['个人史.txt', '婚育史.txt', '家族史.txt', '既往史.txt']
number_list = [0, 1, 2, 3]

all_data = []
for file, number in zip(file_list, number_list):
    with open(r'EHR/' + file, 'r') as f:
        for line in f.readlines():
            if line.strip():
                all_data.append((line.strip(), number))

with open(r'EHR/data/all_data.txt', 'w') as f:
    for i in all_data:
        f.write(i[0] + '\t' + str(i[1]) + '\n')


train_list, rest_list = data_split(all_data, 0.6)
test_list, dev_list = data_split(rest_list, 0.5)

with open(r'EHR/data/all_data.txt', 'w') as f:
    for i in all_data:
        f.write(i[0] + '\t' + str(i[1]) + '\n')

with open(r'EHR/data/dev.txt', 'w') as f:
    for i in dev_list:
        f.write(i[0] + '\t' + str(i[1]) + '\n')

with open(r'EHR/data/test.txt', 'w') as f:
    for i in test_list:
        f.write(i[0] + '\t' + str(i[1]) + '\n')

with open(r'EHR/data/train.txt', 'w') as f:
    for i in train_list:
        f.write(i[0] + '\t' + str(i[1]) + '\n')