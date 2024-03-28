import pandas as pd
data = pd.read_csv("titanic_train.csv")
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
print(f"x_train{x_train.shape}")
print(f"x_test{y_test.shape}")
print(f"y_train{x_train.shape}")
print(f"x_test{y_test.shape}")

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model
model.fit(x_train,y_train)
model.predict([[32,50000,3,0,0,1,1,1,1,0,0]])
y_predict=model.predict(x_test)
y_predict
from sklearn.metrics import accuracy_score
accuracy_score(y_predict,y_test)
from sklearn.metrics import f1_score
f1_score(y_predict,y_test)
from sklearn.metrics import recall_score
recall_score(y_predict,y_test)
from sklearn.metrics import classification_report
print(classification_report(y_predict,y_test))
pip install joblib
import joblib
joblib.dump(model,"nisarg_model.pkl")