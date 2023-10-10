from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle


def lgr_model(X_train, X_test, y_train, y_test):
    logmodel = LogisticRegression(max_iter=500)
    logmodel.fit(X_train,y_train)
    y_pred=logmodel.predict(X_test)
    print(classification_report(y_test,y_pred))
    pickle.dump(logmodel, open("lgr.pkl", "wb"))


def knn_model(X_train, X_test, y_train, y_test,k):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    print(accuracy_score(y_test, y_pred_knn))
    pickle.dump(knn_model, open("knn.pkl", "wb"))