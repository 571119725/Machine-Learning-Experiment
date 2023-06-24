#加载数据集
from constant import *
import pandas as pd

def data_loader(train):
    #两种形式，1. return中使用双分支结构 2. return参数
    return train_data_preprogress() if train else test_data_preprogress()
    
def train_data_preprogress():
    return read_data(True)

def test_data_preprogress():
    df = read_data(False)
    df = df[df['Smiles'].notnull()]
    df = df.sort_values('Standard Value').drop_duplicates(['Molecule ChEMBL ID'])  # 有的分子有多个IC50数据，仅保留一个
    return df

def read_data(train):
    df = pd.read_csv(DATA_PATH + (TRAINING_DATA if train else TESTING_DATA), sep = ';')
    df = df[NAMES]
    return df