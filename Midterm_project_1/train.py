import pandas as pd
import numpy as np
import bentoml

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier

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



## randomforest
model = RandomForestClassifier(n_estimators=200,
                            max_depth=10,
                            min_samples_leaf=3,
                            random_state=1)
model.fit(X_train, y_train)

y_pred = model.predict_proba(X_test)[:, 1]
print(roc_auc_score(y_test, y_pred))


bentoml.sklearn.save_model('cars_purchase_decision_classify',
                            model,     
                            custom_objects={'dictVectorizer': dv}
                            )


