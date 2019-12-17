import pandas as pd

# my_seriers  = pd.Series(['我', '是', '梦想', '橡皮檫'], index=['a', 'b', 'c', 'd'],name='梦想序列')
# # my_seriers1 = pd.Series({'a':'非本科程序员','b':'公众号'})
# # my_seriers2 = pd.Series([1, 1.2, True,'MyName'])
# #
# #
# # print(my_seriers)
# # print(my_seriers1)
# # print(my_seriers2)
# # print(my_seriers2[0])
# # print(my_seriers1['a'])
#
#
# # print(my_seriers.index)
# # print(my_seriers.name)
# # # print(my_seriers.data)
# # print(my_seriers.values)
# # print(my_seriers.shape)
# # print(my_seriers.size)
#
#
# # print(my_seriers.loc['a'])
# # print(my_seriers.iloc[3])
#
#
# # print(my_seriers.iloc[0:2])
# # print(my_seriers.loc['a':'c'])
#
# # print(my_seriers.tolist())
# # print(list(my_seriers.items()))
#
# print(my_seriers.keys())

s = pd.Series([3, 1, 4, 1, 5, 9, 2, 6, 8, 3, 6])
# print(s.max())
# print(s.min())
# print(s.sort_values())
# print(s.sort_index())
# sorted_s = s.sort_values(inplace=True)
# print(s)
# print(s.head(2))
# print(s.tail(2))
print(s.drop(labels=[0,1]))


# idx = pd.MultiIndex.from_arrays([
#     ['warm', 'warm', 'cold', 'cold'],
#     ['dog', 'falcon', 'fish', 'spider']]
#     ,names=['blooded', 'animal'])
#
# s = pd.Series([4, 2, 0, 8],name='legs', index=idx)
# print(s)
# print(s.min())
# print(s.max(level = 'blooded'))