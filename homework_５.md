## 1. Summarize the reasons of overfitting and underfitting. Put them in github repository.

### underfitting的原因
**数据方面的原因：**
 - 缺乏重要训练样本特征
 - 噪音特性没有清洗
 - 特征集过少、数据集过少、抽样数据不合理
 
**模型方面的原因：**
 - 训练的代数太少
 - 模型不够复杂（如使用了线性模型而不是非线性模型，或者使用更大的神经网络）


### overfitting的原因

**数据方面的原因：**
 - 训练集和测试集特征分布不一致
 - 降维（如对特征进行聚类、主题模型进行处理等）
 - 特征选取不合理-》人工筛选特征，使用特征选择算法
 
**模型方面的原因：**
 - 减少训练迭代次数
 - 换更“简单”的模型（如减少网络的层数和神经元的个数）
 - 没有正则化参数用于限制学习得到的参数，使参数太大


---

## 2. install the numpy, scikit-learning, keras, tensorflow
环境ubuntu linux
```
sudo apt install python-pip

mkdir -p ~/.pip

#配置阿里的pip源
cat > ~/.pip/pip.conf << EOF
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
EOF

sudo pip install  numpy

sudo apt-get install python-matplotlib ipython ipython-notebook

sudo apt-get install python-pandas python-sympy python-nose

sudo pip install scipy

sudo pip install -U scikit-learn # 更新scikit-learn

pip list |  grep "scikit-learn" # 查看安装列表
 
```
---
## 3. Writing down three sceneries that machine learning has been used now.
1. 京东个性化推荐商品
2. 支付宝刷脸支付
3. 搜狗输入法，根据语音输入汉字
---
## 4. Come out with three new sceneries with which machine learning may be applied.
1. 根据交通视频监控，动态调整交通灯
2. 垃圾自动识别分类
3. 早期癌症识别