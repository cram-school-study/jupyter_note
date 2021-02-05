#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_median(data):
    # 1. data 리스트 자체를 정렬 하는것
    # data.sort()
    # 2. data 리스트 리턴 값만 정렬해서 보내는 것
    # sorted.data
    # 3. sort 함수의 리턴값을 받는것 이므로 None 타입이 반환된다.
    # data.sort
    
    data.sort()
    center_index = len(data) // 2
    if len(data) % 2 == 1:
        return data[center_index]
    else:
        return (data[center_index]+data[-center_index-1])/2
    
def most_frequent(data):
    count_list=[]
    for x in data:
        count_list.append(data.count(x))
    return data[count_list.index(max(count_list))]

def to_snake_case(data):
    for i in data:
        if i.isupper():
            data=data.replace(i, '_'+i.lower())
    return data.strip('_')

def to_camel_case(data):
    return data.title().replace("_","")


# In[ ]:




