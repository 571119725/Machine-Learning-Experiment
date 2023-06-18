##### 全局变量`（constant.py）`

```python
#数据存储路径
data_path
#训练集文件名
training_set
#测试集文件名
testing_set
#模型文件名
model
```

##### 数据读取`(data_fetch.py)`

读取数据，测试集数据需要排序去重，训练集不需要

```python
#读取数据，判断是否为训练集
def data_load(train):
	#返回读取出的数据结果
	return df
#训练集数据处理
def train_data_preprogress(df):
	return df
#测试集数据处理
def test_data_preprogress(df):
	reutrn df
```

##### 数据整理`(data_collation.py)`

去除数据中不符合规范的值并划分活跃分子和不活跃分子

```python
#参数为从csv文件的读取结果
def data_collation(df):
	#返回活跃分子和不活跃分子
	return active, inactive
```

##### 数据集制作`(dataset_processing.py)`

制作svm模型训练的数据集

```python
#输入参数为两种分子
def create_training_set(active, inactive):
	#数据集最终保存在数据路径下的训练集文件中
	#返回为做好标注的训练数据
	return descriptors
	
def create_testing_set(df):
	#返回计算好的测试集数据
	return descriptors_ic50

#制作训练集所用的分子描述计算
def calc_descriptors(SMI_df):
    return df
    
#保存文件
def save(data,f):

#读取文件
def load(f):
	#返回训练集数据
	return d
```

##### 训练/测试模型`(model.py)`

训练/测试svm模型

```python
#输入做好标注的训练数据
def train_model(descriptors):
	#训练结束保留模型参数，返回准确率
	return accuracy

#输入训练数据
def test_model(descriptors_ic50):
	return df, active, true_active， df_true_active
def data_normalization():

```

##### 数据分布可视化`(model_evaluation.py)`

评价模型指标

```python
def model_evaluation(df, active, true_active， df_true_active)
```

