# my function for generating a dataset
# X is a 2D array with 1000 points per category.
# y is category label.
X, y = blob_data(noise_level=0.25, correlated=0.8)
K = len(set(y)) # number of classes

# Import and instantiate and LDA.
from sklearn import discriminant_analysis as da
lda = da.LinearDiscriminantAnalysis()
lda.fit(X, y) # fit it to data.

cat = lda.predict([[1, 1]])
