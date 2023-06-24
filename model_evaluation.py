#测试评价模型
import matplotlib.pyplot as plt
import seaborn as sns
from dataset_processing import load
from constant import *

def test_evaluation(df, active, true_active, df_true_active):
    print ("N predicted: %d; N True Positive:%d; Accuracy:%f" % (active.shape[0],true_active.shape[0],true_active.shape[0]*1.0/active.shape[0]))
    print ("N True Positive in Database: %d" % df_true_active.shape[0])

    # 数据集中IC50<1e4的分子数占55%，SVM预测的活性分子中IC50<1e4的分子数占82% 
    print(df[df['Standard Value'] < 1e4].shape[0]*1.0/df.shape[0])
    #pandas库函数，填充nan数据为1e15
    # fillna函数接受一个value参数,可以接受一个待填充的值,根据指定的value参数,可以使用常量,也可以使用字典来填充DataFrame中的各个列。
    # fillna()函数还能够接受另外一个参数method,可以是pad、ffill或者bfill,也就是用前一个非缺失值去填充当前的缺失值,或者用下一个非缺失值去填充当前的缺失值
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 2, 1)
    sns.distplot(df['Standard Value'].fillna(1e15),kde=False,rug=True,color='r') # database IC50 counts
    plt.subplot(2, 2, 2)
    sns.distplot(active['Standard Value'].fillna(1e15),kde=False,rug=True,color='b') # active IC50 counts
    plt.subplot(2,2,3)
    sns.distplot(df[df['Standard Value']<1e4]['Standard Value'],kde=False,rug=True,color='r') #
    plt.subplot(2,2,4)
    sns.distplot(active[active['Standard Value']<1e4]['Standard Value'],kde=False,rug=True,color='b') # 
    plt.show()

def train_evaluation(X_test, y_test):
    clf,scaler,features = load(PARAMS_PATH + 'model')
    accuracy = clf.score(X_test, y_test)
    print(accuracy)