"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
import numpy as np
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"""
textset = set(np.array(texts)[:, 0]) | set(np.array(texts)[:, 1])
callset = set(np.array(calls)[:, 0]) | set(np.array(calls)[:, 1])
union = textset | callset
count = len(union)
print("There are <%s> different telephone numbers in the records." % count)