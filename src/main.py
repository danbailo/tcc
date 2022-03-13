import json

import matplotlib.pyplot as plt
from mongoengine import connect, disconnect_all
from sklearn.metrics import RocCurveDisplay

from .core.classifier import Classifier
from .utils import mongo_to_df

plt.grid(True)

if __name__ == '__main__':
    connect("tcc")
    df = mongo_to_df()
    disconnect_all()

    result = {}

    classifier = Classifier(df)

    classifier.prepare_data()

    epochs = 10

    acc_lr = 0
    acc_dt = 0
    acc_rf = 0
    acc_svm = 0
    for epoch in range(epochs):
        logistic_regression = classifier._logistic_regression()
        if logistic_regression[0]['accuracy'] > acc_lr:
            acc_lr = logistic_regression[0]['accuracy']
            best_lr = logistic_regression

        decision_tree = classifier._decision_tree()
        if decision_tree[0]['accuracy'] > acc_dt:
            acc_dt = decision_tree[0]['accuracy']
            best_dt = decision_tree

        random_forest = classifier._random_forest()
        if random_forest[0]['accuracy'] > acc_rf:
            acc_rf = random_forest[0]['accuracy']
            best_rf = random_forest

        svm = classifier._svm()
        if svm[0]['accuracy'] > acc_svm:
            acc_svm = svm[0]['accuracy']
            best_svm = svm

    lr_classifier = best_lr[1]
    dt_classifier = best_dt[1]
    rf_classifier = best_rf[1]
    svm_classifier = best_svm[1]

    result['first_models'] = {
        'Logistic regression': [
            best_lr[0], lr_classifier.get_params()
        ],
        'Decision Tree': [
            best_dt[0], dt_classifier.get_params()
        ],
        'Random Forest': [
            best_rf[0], rf_classifier.get_params()
        ],
        'SVM': [
            best_svm[0], svm_classifier.get_params()
        ],
        'Lenght from dataset': len(df),
        'columns': len(df.columns)
    }

    lr_roc = RocCurveDisplay.from_estimator(
            lr_classifier, classifier.X_test, classifier.y_test
        )
    dt_roc = RocCurveDisplay.from_estimator(
            dt_classifier, classifier.X_test, classifier.y_test
        )
    rf_roc = RocCurveDisplay.from_estimator(
            rf_classifier, classifier.X_test, classifier.y_test
        )
    svm_roc = RocCurveDisplay.from_estimator(
            svm_classifier, classifier.X_test, classifier.y_test
        )
    plt.close("all")

    ax = plt.gca()
    lr_roc.plot(ax=ax, alpha=0.8)
    dt_roc.plot(ax=ax, alpha=0.8)
    rf_roc.plot(ax=ax, alpha=0.8)
    svm_roc.plot(ax=ax, alpha=0.8)
    plt.grid()
    plt.savefig('img/first_models.pdf')

    with open('output/result.json', 'w') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)
