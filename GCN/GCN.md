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


graph sage->GAT

