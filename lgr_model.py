from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle


def model(X_train, X_test, y_train, y_test):
    logmodel = LogisticRegression(max_iter=500)
    logmodel.fit(X_train,y_train)
    y_pred=logmodel.predict(X_test)
    print(classification_report(y_test,y_pred))
    pickle.dump(model, open("lgr.pkl", "wb"))