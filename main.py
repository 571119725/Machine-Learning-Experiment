#主程序
from constant import *
from data_fetch import data_loader
from data_collation import data_collation
from dataset_processing import create_training_data, create_testing_data
from model import train_model, test_model
from model_evaluation import train_evaluation, test_evaluation

if __name__ == "__main__":
    if RUN_TYPE: #RUN_TYPE为True，训练模型，为False测试模型
        df = data_loader(True) #加载训练集
        active, inactive = data_collation(df) #整理数据
        descriptors_ki = create_training_data(active, inactive) #建立训练集
        X_test, y_test = train_model(descriptors_ki) #训练模型
        train_evaluation(X_test, y_test) #评价模型
    else:
        df = data_loader(False) #加载测试集
        descriptors_ic50 = create_testing_data(df) #建立测试集
        df, active, true_active, df_true_active = test_model(descriptors_ic50, df) #测试模型
        test_evaluation(df, active, true_active, df_true_active) #展示测试结果