import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB
df=pd.read_csv('D:\ABHISHEK\AICS\Crop Recommendation System\Crop recommendation\FinalData.csv')
array = df.values
X = array[:,0:7]
Y = array[:,7]
estimators = []
model1 = LogisticRegression()
estimators.append(('logistic', model1))
model2 = DecisionTreeClassifier()
estimators.append(('DTC', model2))
model3 = RandomForestClassifier()
estimators.append(('RF', model3))
model4 = GaussianNB()
estimators.append(('NB',model4))
# create the ensemble model
ensemble = VotingClassifier(estimators)
results = model_selection.cross_val_score(ensemble, X, Y, cv=2)
ensemble.fit(X,Y)
import pickle
with open('crop.pkl','wb') as f:
     pickle.dump(ensemble,f)

