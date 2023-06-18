from constant import *
from sklearn import svm 
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from dataset_processing import save, load

def train_model(descriptors_ki):
    clf = svm.SVC(gamma='scale')  #定义分类器classifier。(合理使用SVM需要调参确定C和gamma，这里不做展开，仅用默认参数)

    features = descriptors_ki.columns[:-1]
    y = descriptors_ki['labels'].values
    X = descriptors_ki[features].values

    scaler = preprocessing.StandardScaler().fit(X)
    X = scaler.fit_transform(X)  #将数据标准化 

    X_train, X_test, y_train, y_test = train_test_split(X,y) # 分割为训练集（3/4）和测试集(1/4)，
    clf.fit(X_train, y_train)
    save((clf,scaler,features),PARAMS_PATH + MODEL_NAME)
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

        return df, active, true_active, df_true_active