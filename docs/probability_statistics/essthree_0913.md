# 条件概率及派生的三个公式

!>今天是由于小组的原因没有办法到课，因此做笔记。并且需要做习题与习题笔记。好在今晚时间还算比较的多。

## 条件概率

在实际情况中，事件之间总有一定的联系，从而事件B的发生会影响到另一个事件A的发生。**B发生条件下A发生的条件概率**，记为$P(A|B)$。

?>今天这个笔记要给老师检查，那么还是把例题看一下。

- *例 1.14：生二咳，一个已知女孩，另一个也是女孩的概率（假定男女等可能）*

    这里关于这个问题的解释中，我认为最值得一记的是这样一句“因为已知B发生是，样本空间已由$\Omega$缩减为$\Omega_B = B$”。这一句解释解释了为什么P(A)变了，本来是$\frac{1}{4}$，现在却成了$\frac{1}{3}$，不是事件A占有的样本点变化了，是样本空间变化了，样本空间变小了。

    清楚了这个，那么这样的条件概率就可以形象的描述了：在一个样本空间中，先确定发生了一个事件，那么现在这个事件之外的样本点就消失了，也就是样本空间缩减为了这个事件的样本点。那么原本样本空间中的其他事件所包含的样本点中不属于这个已确定发生的事件的样本点也同样失效。这样就有：
    $$
    P(A|B) = \frac{n_{AB}}{n_{B}} = \frac{\frac{n_{AB}}{n}}{\frac{n_B}{n}} = \frac{P(AB)}{P(B)}
    $$

就有**定义 1.3**：
$$
P(A|B) = \frac{P(AB)}{P(B)}, A,B为同一试验的两事件，且P(B)>0.
$$
称为事件B发生条件下A发生的条件概率。
条件概率有如下性质：
$$
1. P(A|B)>0;\\
2. P(\Omega|B) = 1\\
3. 若事件A_1,A_2,...,A_n,...两两互斥，则
\\ P(\bigcup_{i=1}^\infty {A}_i|B) = \sum_{i=1}^\infty P(A_i|B)
$$

教材指出“1和2是显然的，下面证明性质3”。
证明的方式，就是使用定义对条件概率进行展开并验证结果相等。

- *例 1.15：发洪水*
    
    用这个例子来说明条件概率是很有用的。

## 乘法公式

用语言叙述乘法公式：事件A和B同时发生的概率，等于事件B发生概率乘以事件B发生条件下事件A发生的概率，也等于事件A发生的概率乘以事件A发生条件下事件B发生的概率。

很直观的公式，不过在这一部分出现一个有意思的操作：
$$
P(A)=P(A\Omega)=P(B)P(A|B)=0.3\times 0.7
$$

在这个操作中，使用了将样本空间拆分成B与B的对立的方式。这会对下一节引入全概率公式有启发意义。

## 全概率公式与贝叶斯

作为条件公式与乘法公式的应用，我们可以解决两类较复杂的计算，这就是下面要讨论的全概率公式与贝叶斯公式。

>这么说，下面要学的东西就是高中的时候没有学习过的部分了？虽然说贝叶斯好像在哪里都看得到。

这里**例题 1.18**使用了信号线的信号能不能被无误差接受来说明这个问题。

|通信线|通信量的份额|无误差的信息的份额|
| :------: | :------: | :------: |
|1|0.4|0.9998|
|2|0.35|0.9999|
|3|0.25|0.9997|

首先，将这些写在表格中的已知量表示出来，那么这些已知量中第二列的是和为一的，而第三列中都是在它们前面的事件发生的情况下的条件概率。

所以由乘法公式，可以将B(无误差)发生的概率计算出来。就是将事件B拆分成分别在三个条件下发生的事件后合并回来，从式子中或许比文字的描述更加明了。
$$
P(B)=P(B\Omega)=P(B(A_1\cup A_2\cup A_3))=P(A_1B)+P(A_2B)+P(A_3B)
$$

上述计算的方法叫做全概率公式。

如果已知了一个信号有误差地被接受，该信号来自地i个通信线路的概率，就是使用贝叶斯公式计算。
在我的感受中，贝叶斯公式的运用实在太常用、太重要了，所以我还是将贝叶斯公式直接放下来：

(**贝叶斯公式**)若$P(B)>0$,有
$$
P(A_i|B) = \frac{P(A_i)P(B|A_i)}{P(B)} = \frac{P(Ai)P(B|A_i)}{\sum_{j=1}^nP(A_j)P(B|A_j)}, i=1,2,...,n.
$$

其中的$P(A_i)$的概率叫做$A_i$的先验概率，$P(A_i|B)$叫做$A_i$的后验概率——这是已知结果事件B发生后，追究由哪一个“原因事件”引起的概率。

>确实需要比较严格的概念解释才容易看懂。所以说贝叶斯公式就是用来在已经发生一件可能有多个原因导致的事的情况下，得到导致这件事发生的原因是这多个原因中的哪一个的概率。

在应用全概率公式和贝叶斯公式中，选择完备事件组较为常见的情形有两种：

- 某过程的第一个步骤的所有情况作为完备事件组
- 某先决条件A或A的对立是完备事件组

>我觉得这里需要对为啥要选择完备事件组说明。虽然说在这种情况下选择完备事件组是一件理所应当的事情，但是由于完备事件组与这两个公式都是之前没有接触到的东西，所以一见到这两个概念会有一些摸不着头脑。那么要理解为什么这里会使用完备事件组，首先要想起来晚辈事件组其实就可以看作对全部的基本事件进行分组。而全概率公式与贝叶斯方程的应用场景应该说都是在已经有一个事件发生的条件下使用的，因此由于这个事件的发生，实际上样本空间就通过这个事件被划分了。而划分出来的完备事件组中的某一组就成了前面提到的新的“样本空间”(现在我们理解了不是新的样本空间，只是一个事件组)。

接着使用例题来加以说明了这个说法，巩固了两个公式的使用。