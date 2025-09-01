from sklearn.tree import DecisionTreeClassifier
features = [[150,0],
           [130,0],
           [140,0],
           [110,1],
           [105,1]]
labels = ['apple','apple','apple','orange','orange']
clf = DecisionTreeClassifier()
clf = clf.fit(features,labels)
clf.predict([[150,1],[100,0]]) # Fill your own values here to know the answer!!!!
