import joblib

def predict(data):
    clf = joblib.load("nisarg_model.pkl")
    return clf.predict(data)