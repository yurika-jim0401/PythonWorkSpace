from functools import reduce


class Perceptron(object):
    def __init__(self, input_num, activator):
        """
        感知器(神经元)类的初始化函数,其中包含两个参数
        :param input_num: 输入参数的个数(向量维度)
        :param activator: 激活函数
        """
        self.activator = activator
        # 初始化未开始训练时权重的维度和每一维的值(维度由输入参数维度决定,初值设为0)
        self.weights = [0.0 for _ in range(input_num)]
        # 初始化偏置项的值,设置为0
        self.bias = 0.0

    def __str__(self):
        """
        输出函数,将训练好的权重和偏置项的值打印到屏幕
        :return: 权重和偏置项
        """
        return "权重为\t:{}\n偏置值为\t:{}".format(self.weights, self.bias)

    def predict(self, input_vec):
        """
        根据输入计算出预测值
        1.将输入向量如[1,0]和已经计算好的权重[0.5,0.5]用zip组合成[(1,0.5),(0,0.5)]的形式
        2.用map来映射关系计算[(1,0.5),(0,0.5)] 得到一个[1*0.5,0*0.5]的list,最后调用reduce来将数组里数据相加
        3.调用reduce时候 参数1为迭代内容的运算规则,参数2为迭代的内容,参数3为初值
        4.算出最后的结果后加上偏置值bias后就可以传入到激活函数中得到最后的分类结果
        :param input_vec:输入向量
        :return: 感知器计算得到的结果,经过激活函数过后最终结果只有两个值(0或者1)
        """
        return self.activator(
            reduce(lambda a, b: a + b, map(
                lambda x_w: x_w[0] * x_w[1], zip(input_vec, self.weights)
            ), 0.0) + self.bias
        )

    def train(self, input_vecs, labels, iteration, rate):
        """
        训练函数
        :param input_vecs: 训练集的输入
        :param labels: 训练集输入对应的输出(标签)
        :param iteration: 要求训练迭代的次数
        :param rate: 学习率(每次调整权值和偏置值更新时的幅度大小)
        :return: none
        """
        for i in range(iteration):
            print("第{}次训练开始".format(i))
            self._one_iteration(input_vecs, labels, rate)
            print("第{}次训练结束".format(i))

    def _one_iteration(self, input_vecs, labels, rate):
        """
        一次训练的具体实现,一次训练就把所有的训练集数据过一次
        :param input_vecs: 训练集的输入
        :param labels: 训练集输入对应的输出(标签)
        :param rate: 学习率
        :return: none
        """
        # 先将输入和输出(标签)打包成一个样本
        samples = zip(input_vecs, labels)
        # 然后对于样本里的每条数据根据用感知器的规则来更新权重
        for (input_vec, label) in samples:
            # 先计算该条数据在当前权重下的输出
            output = self.predict(input_vec)
            # 根据上面的输出和标签来更新权重
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        """
        用于感知器的更新权重
        :param input_vec: 训练数据集的输入
        :param output: 根据当前权重计算的输出结果
        :param label: 标签的输出结果
        :param rate: 学习率
        :return: none
        """
        # 计算当前权重的结果和标签的差距
        delta = label - output
        # 更新权重 Wi = Wi + δW
        # δW = x*δy*rate
        self.weights = list(map(
            lambda x_w: x_w[1] + x_w[0]*rate*delta, zip(input_vec, self.weights)
        ))
        # 更新bias
        self.bias += delta*rate


def f(x):
    """
    激活函数:也就是一个阶跃函数当x>0时y=1;x为其他数时y=0
    :param x:
    :return:
    """
    return 1 if x > 0 else 0


def get_training_dataset():
    """
    根据真值表(and关系)的4项数据来设置训练集数据
    :return:input_vec和labels
    """
    # 真值表的4项输入数据
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    # 真值表的对应输出(标签)
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    """
    根据训练数据集来训练数据
    :return:训练好的感知器
    """
    # 创建传感器实例,参数1为训练数据维度(输入参数的个数),参数2为激活函数
    p = Perceptron(2, f)
    # 设置训练数据集
    input_vecs, labels = get_training_dataset()
    # 开始训练, 训练轮次10次, 学习速率0.1
    p.train(input_vecs, labels, 10, 0.1)
    return p


if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练出的权重
    print(and_perception)
    # 输入新数据进行测试
    print('1 and 1 = {}'.format(and_perception.predict([1, 1])))
    print('1 and 0 = {}'.format(and_perception.predict([1, 0])))
    print('0 and 1 = {}'.format(and_perception.predict([0, 1])))
    print('0 and 0 = {}'.format(and_perception.predict([0, 0])))
