# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 06:03:31 2022

@author: berka
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv('sepet.txt', header = None) # kolon başlıkları olmadığı için headerı none yaptık

#veriler düz bir satır olduğu için list of list yapıcaz
t = []
for i in range(0,7501): #7501 tane veri vardı txt' de
    t.append([str(veriler.values[i,j]) for j in range (0,20)])






from apyori import apriori
kurallar = apriori(t, min_support = 0.01, min_confidence = 0.2, min_lift = 3, min_lenght = 2)

print(list(kurallar))

#lift değeri ne kadar yüksek olursa o ürünlerin beraber alınma ihtimali artıyor
#burada lift değerini belirttiğimizde birbirleri alınma ihtimali 3 değerinin altında ise beraber alma diye sınırlıyoruz




