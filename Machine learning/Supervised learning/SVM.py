from sklearn import svm

X = [[0, 0], [1, 1]] # Training samples
y = [0, 1] # Class labels
clf = svm.SVC()
clf.fit(X, y) # Fit model

clf.predict([[2., 2.]])

clf.support_vectors_ # Get support vectors
clf.support_ # Get indices of support vectors
clf.n_support_ # get number of support vectors for each class