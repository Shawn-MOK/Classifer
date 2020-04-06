filename <- "/Users/shawnmok/HF/chr_all.profile"
dat <- read.table(filename,header = T)
head(dat)
library(dplyr)
library(pROC)

dat=dplyr::filter(dat,PHENO!=-9)
category=dat$PHENO
prediction=dat$SCORESUM

roc_obj <- roc(category, prediction)
auc(roc_obj)

rocobj <- plot.roc(category, prediction)
plot(rocobj)





