#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sentence embedding utils
'''
USE: universal sentence encoder
version 2 trained with DAN
version 3 trained with transformer architecture
'''
#load libraries, takes a while because USE models are very large
url_use_2 = r'https://tfhub.dev/google/universal-sentence-encoder/2'
url_use_3 = r"https://tfhub.dev/google/universal-sentence-encoder-large/3"
import tensorflow_hub as hub
import tensorflow as tf
embed_use_2 = hub.Module(url_use_2)
embed_use_3 = hub.Module(url_use_3)

# Generate the embedding and print out some descriptive data
def generate_embedding(messages, method='use-3'):
    if method=='use-3':
        message_embeddings = embed_use_3(messages)
    elif method=='use-2':
        message_embeddings = embed_use_2(messages)
    return(message_embeddings)

#Convert categories to encoded vectors
def message2vector(messages, batch_size=20000, method='use-3'):
    n = (len(messages)//batch_size) + 1
    begin=0
    end=batch_size
#    result = np.array([])
    while(n>0):
        if end<len(messages):
            out = generate_embedding(messages[begin:end], method)
        else:
            out = generate_embedding(messages[begin:], method)
        if n==len(messages)//batch_size+1:
            result = out
        else:
            result = np.concatenate((result, out), axis=0)
        n = n -1
        begin=begin+batch_size
        end=end+batch_size               
    return result

