import pandas as pd
import numpy as np
import bentoml
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.inspection import permutation_importance

import xgboost as xgb

import bentoml
from bentoml.io import JSON


df=pd.read_csv("data.csv")


df["Gender"]=df["Gender"].apply(lambda x: 1 if x=="Male" else 0)
X = pd.DataFrame(df, columns=['Gender', 'Age', 'AnnualSalary'])
y = df.Purchased
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

dv = DictVectorizer(sparse=False)
train_dicts = X_train.fillna(0).to_dict(orient='records')
X_train = dv.fit_transform(train_dicts)
test_dicts = X_test.fillna(0).to_dict(orient='records')
X_test = dv.transform(test_dicts)



dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

## XGBoost
xgb_params = {
    'eta': 0.1, 
    'max_depth': 10,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=50)
y_pred = model.predict(dtest)
print(roc_auc_score(y_test, y_pred))


bentoml.xgboost.save_model('cars_purchase_decision',
                            model,     
                            custom_objects={'dictVectorizer': dv}
                            )


