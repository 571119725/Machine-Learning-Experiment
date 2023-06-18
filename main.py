from constant import *
from data_fetch import data_loader
from data_collation import data_collation
from dataset_processing import create_training_data, create_testing_data
from model import train_model, test_model
from model_evaluation import train_evaluation, test_evaluation

if __name__ == "__main__":
    if RUN_TYPE:
        df = data_loader(True)
        active, inactive = data_collation(df)
        descriptors_ki = create_training_data(active, inactive)
        X_test, y_test = train_model(descriptors_ki)
        train_evaluation(X_test, y_test)
    else:
        df = data_loader(False)
        descriptors_ic50 = create_testing_data(df)
        df, active, true_active, df_true_active = test_model(descriptors_ic50, df)
        test_evaluation(df, active, true_active, df_true_active)