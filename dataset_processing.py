from sklearn import svm 
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
import pandas as pd
from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole # 在jupyter-notebook中显示分子结构
from mordred import Calculator, descriptors
from molvs import Standardizer
import pickle
import os
from constant import *

def calc_descriptors(SMI_df):
    # create descriptor calculator with all descriptors
    calc = Calculator(descriptors, ignore_3D=True)
    s = Standardizer()
    mols = [Chem.MolFromSmiles(smi) for smi in SMI_df]
    mols = [s.largest_fragment(m) for m in mols]
    df = calc.pandas(mols)
    return df
# --- I/O function
def save(data,f):
    with open(f,"wb") as f1:
        pickle.dump(data,f1)

def load(f):
    with open(f,"rb") as f1:
        d = pickle.load(f1,encoding='iso-8859-1')
    return d

def create_training_data(active, inactive):
    if os.path.isfile(PARAMS_PATH + TRAINING_SET) :
        active_descriptors,inactive_descriptors = load(PARAMS_PATH + TRAINING_SET)
    else:
        active_descriptors = calc_descriptors(active['Smiles'])
        inactive_descriptors = calc_descriptors(inactive['Smiles'])
        save((active_descriptors,inactive_descriptors), PARAMS_PATH + TRAINING_SET)
    active_descriptors['labels']=1
    inactive_descriptors['labels']=0
    descriptors_ki = pd.concat([active_descriptors,inactive_descriptors],ignore_index=True)
    descriptors_ki = descriptors_ki.select_dtypes(include='number')
    return descriptors_ki

def create_testing_data(df):
    if os.path.isfile(PARAMS_PATH + TESTING_SET) :
        descriptors_ic50 = load(PARAMS_PATH + TESTING_SET)
    else:
        descriptors_ic50 = calc_descriptors(df['Smiles'])
        save(descriptors_ic50, PARAMS_PATH + TESTING_SET)
    return descriptors_ic50