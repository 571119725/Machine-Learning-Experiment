#定义系统使用的常量
# 只在读取的csv中关注这几列数据
NAMES = ['Molecule ChEMBL ID', 'Molecule Name', 'Smiles', 
        'Standard Type', 'Standard Relation', 'Standard Value', 'Standard Units',
        'Data Validity Comment', 'Comment',] 
#源数据存储路径
DATA_PATH = 'data/'
#训练集测试集模型参数存储路径
PARAMS_PATH = 'params/'
#训练集源数据
TRAINING_DATA = 'AChE.Ki.csv'
#测试集源数据
TESTING_DATA = 'AChE.IC50.csv'
#训练集数据
TRAINING_SET = 'descriptors-ki.data'
#测试集数据
TESTING_SET = 'descriptors-ic50.data'
#模型参数文件名
MODEL_NAME = 'model'
#代码运行方式，True为训练模型，False为测试模型
RUN_TYPE = True