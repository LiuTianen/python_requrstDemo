#嵌套列表
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# # scores = [[None] * len(courses)] * len(names)
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# def bubble_sort(origin_items, comp=lambda x, y: x > y):
#     """高质量冒泡排序(搅拌排序)"""
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items


