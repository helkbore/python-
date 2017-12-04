#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'读取文件夹内的文件 2017年12月1日'
import book_db
import os
import math

# print(os.path.abspath("."))
book_dir = "E:\\book\\"

#
# print('begin')
# print(book_dir)
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print('----root')
        # print(root)
        #
        # # list，包含了当前dirpath路径下所有的子目录名字（不包含目录路径）；
        # print('----dirs')
        # print(dirs)
        #
        # # list，包含了当前dirpath路径下所有的非目录子文件的名字（不包含目录路径）
        # print('----files')
        # print(files)

        # 遍历books里面的图书, 获取文件名
        for file in files:
            # print(file)
            print(os.path.splitext(file))


# file_name(book_dir)
files = os.listdir(book_dir)
for file in files:
    book = {}
    # print(file)
    book['origin_name'] = os.path.splitext(file)[0]
    book['book_name'] = book['origin_name'].split('-')[0]
    book['author'] = book['origin_name'].split('-')[1] if len(book['origin_name'].split('-'))  > 1 else '未知'
    book['size'] = os.path.getsize(os.path.join(book_dir, file))
    # book['size'] = math.ceil(os.path.getsize(os.path.join(book_dir, file)) / 1024)
    book['ext'] = os.path.splitext(file)[1][1:]

    # for d in book:
    #
    #    print(d)
    #    print(book[d])
    # print("over")
    # print(book.keys())
    # print(book.values())

    # save_dict(book)

    book_db.save_book('book', book)
    # print(os.path.abspath("."))
    # print(os.path.abspath("book_db.py"))
print("---end")
