from constant import *
from sklearn import svm 
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from dataset_processing import save, load
import pandas as pd
import time

def train_model(descriptors_ki):
    clf = svm.SVC(gamma='scale')  #定义分类器classifier。(合理使用SVM需要调参确定C和gamma，这里不做展开，仅用默认参数)
    # clf = KNeighborsClassifier(n_neighbors = 5)
    # clf = LogisticRegression(C = 4)
    # clf = DecisionTreeClassifier(max_depth = 5)

    features = descriptors_ki.columns[:-2 + 1] #读取数据集中的第一列到倒数第二列的标签
    y = descriptors_ki['labels'].values
    X = descriptors_ki[features].values

    scaler = preprocessing.StandardScaler().fit(X)
    X = scaler.fit_transform(X)  #将数据标准化 

    X_train, X_test, y_train, y_test = train_test_split(X,y) #分割为训练集（3/4）和测试集(1/4)，
    start_time = time.time()
    clf.fit(X_train, y_train) #拟合模型
    end_time = time.time()
    print("训练花费的时间：", end_time - start_time)
    save((clf,scaler,features),PARAMS_PATH + MODEL_NAME) #在路径下保存模型参数
    return X_test, y_test

def test_model(descriptors_ic50, df):
    try:
        clf,scaler,features = load(PARAMS_PATH + MODEL_NAME)
    except IOError:
        print('读取文件出错')
    else:
        X = descriptors_ic50[features].values
        X = scaler.fit_transform(X)   # 用训练集中的scaler参数标准化数据集
        y_prediction = clf.predict(X)
        df['label'] = y_prediction
        active = df[ df['label'] == 1 ]
        true_active = active[ active['Standard Value']<1e4 ]
        df_true_active = df[df['Standard Value']<1e4]
        df.to_csv(PARAMS_PATH + PREDICTION, index = False)
        return df, active, true_active, df_true_active