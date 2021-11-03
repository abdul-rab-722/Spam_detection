import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import confusion_matrix

data = pd.read_csv(".\\datasets\\spam.csv", encoding = "latin-1")
data = data[['v1', 'v2']]
data = data.rename(columns = {'v1': 'analysis', 'v2': 'message'})

def normalize(message):
    message = message.lower()
    return message

data['message'] = data['message'].apply(normalize)

X_train, X_test, y_train, y_test = train_test_split(data['message'], data['analysis'], test_size = 0.1, random_state = 1)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

svm = svm.SVC(C=1000)
svm.fit(X_train, y_train)

#X_test = vectorizer.transform(X_test)
#y_pred = svm.predict(X_test) 
#print(confusion_matrix(y_test, y_pred))
 
def check_spam(message):
    message = vectorizer.transform([message])
    prediction = svm.predict(message)
    return prediction[0]
