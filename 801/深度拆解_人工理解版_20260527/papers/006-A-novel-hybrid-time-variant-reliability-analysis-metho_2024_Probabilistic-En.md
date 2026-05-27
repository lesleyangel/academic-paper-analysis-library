## 1. 身份层

这是一篇混合不确定性下时变可靠性分析方法论文，题名为 “A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory”。metadata 中作者为空；论文面向同时包含随机不确定性和区间/认知不确定性的 time-variant reliability analysis。

材料读取边界：本报告读取了 `metadata.json`、`abstract.txt`、`clean_body.md`、`figure_captions.txt`、`table_captions.txt`、`tables/*.md`、`equations.txt`、`references.txt`。核心文件均存在；明显抽取问题是部分公式 OCR 噪声重，表格编号因 Nomenclature 表而整体偏移，metadata 作者缺失。

论文的核心身份是 reliability method，而不是某个结构案例论文。四个算例包括 corroded steel beam、10-bar truss、solid rocket engine shell 和 rocket inter-stage，主要服务于证明 HABMPPT 方法在不同复杂度结构上的准确性和效率。

## 2. 主张层

中心主张是：混合不确定性时变可靠性分析的计算瓶颈来自大量原始 limit-state function 评估和每个离散时刻的可靠性搜索；如果用 bound-most-probable point trajectory 近似上下界极限状态超曲面，就可以把高维、时变、混合不确定性问题转化为一组线性化 Gaussian processes，再用 EOLE 和 Monte Carlo 高效估计失效概率上下界。

摘要中的主张链是：时间离散把 HTRA 转化为 time-independent series system reliability；每个时刻搜索 lower/upper bound most-probable point；沿时间形成 BMPPT；在 BMPPT 上线性化上下界 LSF；用 active learning Kriging 近似 BMPPT，减少逐时刻 BMPP 搜索；最终在工程算例中同时获得高精度和高效率。

结论中的主张较为克制：HABMPPT 的函数调用量通常低于 TDHTRA 的十分之一，同时保持相近精度；但仍存在相关不确定性处理、BMPP 搜索效率、非光滑或不连续 BMPPT 等问题。

## 3. 选题层

选题抓住了时变可靠性中一个很硬的成本问题。结构可靠性若只在单一时刻分析，FORM/SORM 或代理模型已相对成熟；但实际结构常有载荷随时间变化、强度退化、腐蚀演化、火箭壳体压力峰值等时变过程，失效事件是时间区间内任一时刻越界。

混合不确定性进一步放大难度。随机变量可以用概率模型，认知不确定性往往只能给区间；时变区间过程还会有 mid/radius 和相关函数。如果直接对所有随机样本、区间样本、时间步和极限状态函数做嵌套计算，成本会迅速失控。

论文的选题技巧是绕开“全局近似原始时变 LSF”这条难路，改为近似最重要的边界轨迹 BMPPT。也就是说，它不试图把整个高维时空极限状态面都学出来，而是只学可靠性积分最敏感的 most-probable point trajectory。

## 4. 位置层

论文在时变可靠性文献中处于 TDTRA/PHI2/outcrossing/极值方法之后。已有 time-dependent reliability analysis 方法要么依赖大量 MCS，要么需要在多个离散时刻做 FORM/MPP 搜索。对于混合不确定性 HTRA，这些方法会因为上下界极限状态和区间优化而变得更贵。

本文的位置是把 MPP trajectory 思路推广为 bound-most-probable point trajectory：对混合不确定性的 lower/upper bound 分别找最可能失效点，并沿时间形成轨迹。然后用主动学习 Kriging 只在时间维度上补充 BMPP 点，而不是高维输入空间里盲目加样。

相对深度神经网络或全局代理模型，HABMPPT 更像局部可靠性几何近似。它保留了 FORM 在 most probable region 附近的效率，又通过 EOLE+MCS 处理时变 Gaussian process 越界概率。

## 5. 贡献层

第一项贡献是定义 BMPPT。对于存在随机变量和区间变量的混合不确定性问题，瞬时极限状态不是一张单独曲面，而是上下界曲面包围的 strip；论文分别定义 LBMPP 和 UBMPP，并把它们随时间变化的轨迹作为关键可靠性对象。

第二项贡献是提出 HABMPPT 流程：用 K-L 展开描述区间过程，采用两层嵌套优化搜索上下界 BMPP，在 BMPPT 附近线性化极限状态函数，把上下界 LSF 转化为 Gaussian processes，再用 EOLE 和 Monte Carlo 估计失效概率上下界。

第三项贡献是用 active learning Kriging 近似 BMPPT。初始只选三个时刻，计算真实 LBMPP/UBMPP；再用平均分量误差构造学习函数，选择误差最大的时间点补充 BMPP，直到误差低于阈值。这直接减少了昂贵的 BMPP 搜索次数。

第四项贡献是用四个难度递增算例验证。算例从解析/半解析结构到含有限元和 BPNN 的 rocket inter-stage，展示方法在低维、结构系统、火箭壳体和工程级结构上的泛化。

## 6. 方法层

方法输入包括随机变量、区间变量、时变随机或区间过程、极限状态函数、时间区间和可靠性精度要求。输出是整个时间区间内失效概率的 lower/upper bounds，以及 BMPPT 近似轨迹。

直接 HTRA 需要在每个时间离散点、每组随机样本和区间样本上反复评估极限状态，并求最大/最小响应。HABMPPT 改为先在标准正态空间中找到离原点最近的上下界失效点，也就是 LBMPP/UBMPP，然后把原极限状态在这些点附近一阶线性化。

主动学习部分只在时间轴上工作。Kriging 模型拟合 LBMPPT/UBMPPT 的各分量随时间变化，学习函数衡量当前轨迹预测的不确定性或误差，新增样本点是误差最大的时刻。这样新增的不是普通 LSF 样本，而是新的 BMPP 搜索结果。

线性化后，上下界极限状态过程具有均值约为负可靠指标、标准差为 1 的 Gaussian process 表达。EOLE 用特征展开生成过程样本，MCS 统计时间区间内是否越界，从而得到 lower/upper failure probability。

## 7. 证据层

图 1 展示 MPP trajectory 思想，图 2 给出混合不确定性下的 limit-state strip，图 3 展示 SSL 搜索，图 4 是 HABMPPT 总流程。这四幅图是方法理解的骨架。

第一个 corroded steel beam 算例中，直接 MCS 结果约为 lower 5.222e-2、upper 3.945e-1；HABMPPT 给出 lower 5.252e-2、upper 3.853e-1，相对误差约 0.57% 和 2.33%，只需 8 次 BMPP 搜索和约 27137 次函数调用，远少于 TDHTRA-200 的 400 次 BMPP 搜索。

第二个 10-bar truss 算例中，MCS 为 9.623e-3/3.434e-2，HABMPPT 为 9.169e-3/3.325e-2，相对误差约 4.72%/3.17%，函数调用约 2690 次。第三个 solid rocket engine shell 算例中，MCS 为 1.163e-4/2.941e-3，HABMPPT 为 1.120e-4/2.962e-3，误差约 3.70%/0.71%，函数调用约 944 次。

第四个 rocket inter-stage 算例最能体现工程价值。有限元模型有 57529 个 shell elements，并用 BPNN 近似最大应力响应；HABMPPT 给出 1.128e-3/5.134e-3，与 MCS 的 1.103e-3/4.989e-3 相差约 2.27%/2.91%，平均约 16.4 次 BMPP 搜索和 15903 次函数调用，避免了不可承受的直接 MCS 规模。

## 8. 结构语言层

文章结构非常方法论化：先给 TRA 和 HTRA 问题定义，再说明 direct MCS 为什么不可行，随后定义 BMPPT 和近似方法，最后用四个算例层层加码。它的叙事不是“提出一个代理模型”，而是“找到可靠性问题中最值得近似的轨迹”。

语言上，作者反复使用 “bound-most-probable point trajectory”“approximating limit-state hypersurface”“linearized Gaussian processes” 等术语，把复杂的混合不确定性问题压缩成几何直觉：真正重要的是上下界失效面离原点最近的轨迹。

可复用的写法是把计算效率分解成 N_FE 和 N_BMPP 两个指标。普通函数调用数说明整体成本，BMPP 搜索次数说明最昂贵的可靠性子任务数量，两者一起比单报运行时间更有解释力。

抽取层面，公式区有明显 OCR 噪声，尤其是 Eq24-30 附近的自相关、均值和方差表达。表格编号也因 Nomenclature 表而偏移，引用表格时需按内容而不是抽取文件名判断。

## 9. 引用风险层

引用链覆盖 time-dependent reliability、PHI2/outcrossing、FORM/MPP、hybrid reliability、interval process、Kriging active learning 和 EOLE。作为“混合不确定性时变可靠性高效算法”引用是合适的。

主要风险是方法依赖局部线性化。若极限状态面高度非线性、非光滑、多失效区域或 BMPPT 不连续，一阶近似和 Kriging 轨迹拟合可能不足。作者在结论中也承认 unsmooth/discontinuous BMPPT 是未来问题。

第二个风险是 BMPP 搜索本身。方法减少了搜索次数，但每次搜索仍是两层优化；如果原始极限状态昂贵、变量维数很高或约束不规则，BMPP 求解可能成为瓶颈。

第三个风险是相关不确定性处理。当前流程主要展示常见随机/区间过程，复杂相关结构、非高斯相关过程或强耦合 epistemic uncertainty 可能需要额外扩展。

## 10. 复用层

可复用的选题模板是：面对昂贵的时变可靠性，不要全局近似整个 LSF，而是识别可靠性积分最敏感的几何对象，例如 MPP trajectory、outcrossing boundary 或 failure strip，再对该对象做主动学习。

可复用的方法链是：`hybrid uncertainty modeling -> time discretization -> LBMPP/UBMPP search -> BMPPT active learning -> local linearization -> Gaussian process approximation -> EOLE/MCS failure probability bounds`。

可复用的证据组织是四级算例：解析低维算例验证精度，结构桁架验证多变量，火箭壳体验证工程响应面，有限元级 inter-stage 验证复杂工程可行性。每级都报 MCS/TDHTRA 对照、误差、N_BMPP 和 N_FE。

自检：本报告只使用十个指定标题；摘要、结论、图表、公式、引用风险和抽取问题均已收进十层。明显抽取问题为 metadata 作者缺失、公式 OCR 噪声、表格编号偏移和个别正文 typo。
