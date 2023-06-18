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
    sns.distplot(df['Standard Value'].fillna(1e15),kde=False,rug=True,color='r') # database IC50 counts
    plt.show()
    sns.distplot(active['Standard Value'].fillna(1e15),kde=False,rug=True,color='b') # active IC50 counts
    plt.show()
    sns.distplot(df[df['Standard Value']<1e4]['Standard Value'],kde=False,rug=True,color='r') #
    plt.show()
    sns.distplot(active[active['Standard Value']<1e4]['Standard Value'],kde=False,rug=True,color='b') # 
    plt.show()

def train_evaluation(X_test, y_test):
    clf,scaler,features = load(PARAMS_PATH + 'model')
    accuracy = clf.score(X_test, y_test)
    print(accuracy)