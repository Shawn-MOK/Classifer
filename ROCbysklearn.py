#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:26:25 2020

@author: shawnmok
"""

import numpy as np
from sklearn import metrics
import pandas as pd

dat=pd.read_csv("/Users/shawnmok/HF/chr_all.profile",sep="\s+")


booleans=[]
for result in dat["PHENO"]:
    if result==-9:
        booleans.append(False)
    else:
        booleans.append(True)

filtered=pd.Series(booleans)
dat1=dat[filtered]


y_true=dat1["PHENO"]
y_prob=dat1["SCORESUM"]
y_true=y_true.replace(1,0)
y_true=y_true.replace(2,1)
auc=metrics.roc_auc_score(y_true,y_prob)
print(auc)