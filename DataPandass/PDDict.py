import pandas as pd

# dict = {
#     'boys':[1,2,3],
#     'girl':[5,6,7]
# }
#
# df = pd.DataFrame(dict,index=['a','b','c'])
# print(df)

df = pd.DataFrame([[1,5],[2,6],[3,7]],columns=['boys','girls'],index=['class1','class2','class3'])
# print(df)
# print(df[['boys','girls']])
# print(df.ix[0])
# print(df.ix['class1'])
# print(df['boys'][0])
# print(df['boys']['class1'])
# print(df.ix['class1'][0])
# print(df.index)
# print(df.columns)
# print(df.values)
print(df.size)
print(df.shape)