#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1 Практическое задание


# In[ ]:


text = input('введите слово')
while True:
    if len(text) % 2 == 0:
        print(text[len(text) // 2 - 1:len(text) // 2 + 1])
        break
    else:
        print(text[len(text) // 2])
        break

# In[ ]:


# 2 практическое


# In[ ]:


a = []
while True:
    n = int(input('Введите число'))
    if n == 0:
        print(sum(a))
        break
    else:
        a.append(n)

# In[47]:


# 3


# In[25]:


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
bs = sorted(boys)
gs = sorted(girls)
if len(bs) != len(gs):
    print('Кто-то без пары')
else:
    print('Идеальные пары:')
    for i in range(len(bs)):
        print(bs[i], gs[i], sep=' И ')

# #4

# In[46]:


import math

ct = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
for i in range(len(ct)):
    cn = ct[i][0]
    cat = ct[i][1]
    print(cn, '-', round((math.fsum(cat) / len(cat) - 32) / 1.8, 1), 'C')

# In[48]:


# 5


# In[51]:


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
idsv = ids.values()
values = []
for i in idsv:
    for j in i:
        values.append(j)
print(set(values))

# In[52]:


# 6


# In[80]:


qu = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
d = 0
f = 0
c = 0
a = []
for i in qu:
    a.append(i.split())
d = len(a)
for j in a:
    b = len(j)
    if b == 2:
        c = c + 1
    elif b == 3:
        f = f + 1
print('Поисковых запросов, содержащих 3 слов(а):', round((f / d) * 100, 2), '%')
print('Поисковых запросов, содержащих 2 слов(а):', round((c / d) * 100, 2), '%')

# In[81]:


# 7


# In[109]:


results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
results1 = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
ROI = {}
flag = 0
cost = 0
revenue = 0
for keys in results:
    for roi in results[keys].values():
        flag = flag + 1
        if flag == 1:
            revenue = roi
        else:
            cost = roi
            flag = 0
        if cost != 0:
            ROI['ROI'] = round((revenue / cost - 1) * 100, 2)
            results1[keys] |= ROI
            revenue = 0
            cost = 0

print(results1)

# In[110]:


# 8


# In[115]:


stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
key = max(stats.items(), key=operator.itemgetter(1))[0]
print('Максимальный объем продаж на рекламном канале:', key)

# In[119]:


# initialize
a = []

# create the table (name, age, job)
a.append(["Nick", 30, "Doctor"])
a.append(["John", 8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])

# sort the table by age
import operator

a.sort(key=operator.itemgetter(1))

# print the table
print(a)

# In[ ]:




