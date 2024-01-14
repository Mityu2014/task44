# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?


from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# решение из задания
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(pd.get_dummies(data['whoAmI']))

# решение через др. библиотеки
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(data)
print(encoded_data.toarray())

data_lst = list(set(lst))
#решение через словарь (не совсем понял, что из себя представляет формат dataFrame, словарь со списками или список со списками)
dict_data = {'вид':data_lst}

for i in range(len(lst)):
    one_hot = []
    for count in data_lst:
        if lst[i] == count:
            one_hot.append(1)
        else:
            one_hot.append(0)
    dict_data[i] = one_hot

for key, value in dict_data.items(): # Более красивый вывод
    print(f'{key: <10}{value[0]: <10}{value[1]}')

# решение через список
data_lst_2 = [['вид'] + data_lst]
for i in range(len(lst)):
    one_hot = [i]
    for count in data_lst:
        if lst[i] == count:
            one_hot.append(1)
        else:
            one_hot.append(0)
    data_lst_2.append(one_hot)

for row in data_lst_2: # Более красивый вывод
    print('     '.join(list(map(str, row))))
