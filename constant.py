NAMES = ['Molecule ChEMBL ID', 'Molecule Name', 'Smiles', 
        'Standard Type', 'Standard Relation', 'Standard Value', 'Standard Units',
        'Data Validity Comment', 'Comment',] # 仅关注这几列数据
DATA_PATH = 'data/'
PARAMS_PATH = 'params/'

TRAINING_DATA = 'AChE.Ki.csv'
TESTING_DATA = 'AChE.IC50.csv'

TRAINING_SET = 'descriptors-ki.data'
TESTING_SET = 'descriptors-ic50.data'
MODEL_NAME = 'model'
RUN_TYPE = False