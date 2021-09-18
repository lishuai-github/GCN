# GCN

GCN流程：聚合、更新、循环。

GNN是一个提取特征的方法。

图G：

> V：顶点集
>
> A:邻接矩阵
>
> X：节点特征，m*|V|，m维特征

$$
h^0_v=x_v\\
h^k_v = \sigma\left(W_k\sum_{u \in N(v)}{\frac{h_u^{k-1}}{|N(v)|}+B_kh_v^{k-1}}\right),  \forall k \in \{{1,...,K}\}\\
z_v=h_v^K\\
等价表示\\
H^{(l+1)} = \sigma \left(H^{(l)}W_0^{(l)}+\overline AH^{(l)}W_1^{(l)}\right)\\
\overline A = D^{-\frac {1}{2}}AD^{-{1 \over 2}}
$$

每一次迭代的共享参数$W_0和W_1$。有很好的的泛化能力。
$$
H^{(l+1)} = \sigma \left(\overline D^{-\frac {1}{2}}\overline A \overline D^{-{1 \over 2}}H^{(l)}W^{(l)}\right)
$$

$\overline AH^{(l)}$聚合相邻节点信息，更新自己。

$D^{- {1\over 2}}$:度越大，影响越小。

## 发展过程

<img src="..\Image\image-20210913105103683.png" alt="image-20210913105103683" style="zoom:25%;" />

## 空域

巴拿赫不动点定理保证收敛性

过平滑问题，在迭代的过程中节点值趋于一致，无法进行后续分类。

GGNN：改进激活函数GRU，不限制迭代收敛。 

GCN：是为了提取特征

利用邻居节点更新自己的信息。

MPNN：消息传递和消息更新

GraphSage：节点太多的话，利用采样点信息更新信息。

GAT：修改更新函数。

<img src="..\Image\image-20210913111724638.png" alt="image-20210913111724638" style="zoom:25%;" />









 

### 频域


拉普拉斯矩阵

通过卷积定理类比过来

卷积核表示方法

GCN的输出函数选择

# GAT

注意力机制$\alpha$是一个单层的前馈神经网络。

<img src=".\Image\image-20210913171607117.png" alt="image-20210913171607117" style="zoom:70%;" />

<img src=".\Image\image-20210913192419269.png" alt="image-20210913192419269" style="zoom:50%;" />

LeakyReLU：negative input slope  $\alpha = 0.2$

<img src=".\Image\image-20210913174233536.png" alt="image-20210913174233536" style="zoom:80%;" />

**multi_head attention**

重复K次上述过程，将结果拼接。

<img src=".\Image\image-20210913174631087.png" alt="image-20210913174631087" style="zoom:80%;" />

concatenation is no longer sensible， averaging

<img src=".\Image\image-20210913174915711.png" alt="image-20210913174915711" style="zoom:80%;" />

K=3

<img src=".\Image\image-20210913192443811.png" alt="image-20210913192443811" style="zoom: 80%;" />

比较

1. 时间复杂度低，可以并行运算K。

2. 给不同的邻居节点不同的权值，分析权值可以模型可解释性提供帮助。

3. 注意力机制只与邻接节点有关，而不需要知道整张图信息。

4. 由于LSTM。

5. 是特殊的MoNet。

   



