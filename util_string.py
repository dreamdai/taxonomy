#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
input:
category: a string which represents a category
howto: choices of how you want the new category be extracted,for example, as of 'A,B,C,D,E'
       'first':  the first tier category, 'A'
       'last': the last tier category, 'E'
       'first_half': the first half of the categories, 'A,B', if the just 1 tier, first and second halves will be the same.
       'second_half'：the second half of the categories, 'C,D,E'
       'fill': fill the missing categories upto 5 tier with the fill_string provided. 
               For example, for 'A,B,C', it will be'A,B,C,fill_str,fill_str'
       ''
output：return a categoty string with respect to the 'howto' methods mentioned above
'''
def new_category(category, howto='last', fill_str='AbCxYZ'):
    temp = category.split(',')
    if howto=='first':
        return temp[0]
    elif howto=='last':
        return temp[-1]
    elif howto=='first_half':
        if len(temp)==1:
            return temp[0]
        else:
            return ','.join(i for i in temp[:len(temp)//2])
    elif howto=='second_half':
        return ','.join(i for i in temp[len(temp)//2:])
    elif howto=='filled':
        while(len(temp)<5):
            temp.append(fill_str)
        return ','.join(i for i in temp)

