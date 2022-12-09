
#!/usr/bin/python3
import catboost
from catboost.datasets import titanic


train, test = titanic()

train.to_csv("/home/evgeny/git/USSB_PROJECT/data/row/train.csv",columns = train.columns)
test.to_csv ("/home/evgeny/git/USSB_PROJECT/data/row/test.csv",columns = test.columns)


