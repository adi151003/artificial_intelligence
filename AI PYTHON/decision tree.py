#importing libraries
from sklearn import datasets
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

X,y=datasets.load_breast_cancer(return_X_y=True)
DT=DecisionTreeClassifier()
DT_model=DT.fit(X,y)
X_tr,X_ts,y_tr,y_ts=model_selection.train_test_split(X,y,test_size=0.20,random_state=30)
DT_model =DT.fit(X_tr,y_tr)
DT_pred=DT_model.predict(X_ts)

print("Accuracy :",metrics.accuracy_score(DT_pred,y_ts))
print(metrics.confusion_matrix(DT_pred,y_ts))
print(metrics.classification_report(DT_pred,y_ts))
print("ROC AUC:",metrics.roc_auc_score(DT_pred,y_ts))


