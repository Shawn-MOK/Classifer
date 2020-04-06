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



#plot
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_prob, pos_label=1)

plt.plot(fpr, tpr, color='blue', lw=2,
             label='ROC curve of SbayesR area ='+ str(auc) )

plt.plot([0, 1], [0, 1], 'k--', lw=3)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to SbayesR')
plt.legend(loc="lower right")
plt.show()
