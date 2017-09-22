"""

Ref: http://scikit-learn.org/stable/unsupervised_learning.html

1) Load data
2) Featurize (i.e. derive some additional features that may or may not turn out to be useful to the model)
3) Feed into a unsupervised SK learn Model.
4) Output 10 rows for each identified category

Discuss why the model performs well (or more likely given the small amount of data and limited model building time)
why it performs poorly and what would be done next.
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def main():
    df = pd.read_excel("data/movies.xlsx")

    #enc = OneHotEncoder()
    kn = KMeans()
    p = Pipeline([#('encode', enc),
                  ('model', kn)])

    X = df[["Budget Gross Millions", "Box Office Billions", "Running Time"]]
    # Fix data types
    for value in ["Budget Gross Millions", "Box Office Billions", "Running Time"]:
        X[value] = X[value].apply(lambda x: None if x == "na" else float(x))
    # Drop missing
    X.dropna(axis=0, how='any', inplace=True)

    ft = p.fit_transform(X)
    preditions = p.predict(X)
    print(preditions)


if __name__ == "__main__":
    main()
