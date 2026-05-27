## 1. 身份层

这是一篇基于径向基函数的序贯代理可靠性分析方法论文。metadata 中题名和作者均为空；根据目录名、摘要和正文，可推断题名为 “A sequential surrogate method for reliability analysis based on radial basis function” 一类。论文面向 expensive implicit limit-state function，目标是在少量真实函数调用下估计失效概率。

材料读取边界：本报告读取了 `metadata.json`、`abstract.txt`、`clean_body.md`、`figure_captions.txt`、`table_captions.txt`、`tables/*.md`、`equations.txt`、`references.txt`。核心文件均存在；明显抽取问题是 metadata 题名/作者缺失，正文误抽出 `where` 作为二级标题，图题合并/错位，部分公式和表格 OCR 噪声较大。

论文的身份是 structural reliability 中的 active surrogate/reliability algorithm，不是某个工程零件论文。圆管裂纹、超球面、悬臂梁、减速器轴、悬臂管、非线性振子和高维算例都用于展示 SSRM 的适应性。

## 2. 主张层

中心主张是：传统 FORM/SORM 对非线性极限状态和高维问题误差较大，直接 MCS 又昂贵；如果用 RBF surrogate 表示极限状态，并通过序贯优化把新增样本放在高概率密度且接近 surrogate limit-state boundary 的区域，同时保持与已有样本的最小距离，就能以较少真实 LSF 调用获得准确失效概率。

摘要中的主张是：特殊优化问题会迭代更新 surrogate LSF；目标是在满足近似 LSF 和最小距离约束下寻找 PDF 最大的新点。这样既强化 high failure probability region 和 LSF boundary 的精度，也通过 min distance 改善 less-important region。

结论中的主张是：SSRM 对强非线性和高维问题都有适应性；低维算例中精度和效率优势明显；高维算例中精度与 2SMART 相当而函数调用数显著更少；但优势主要体现在原始 LSF 昂贵的隐式 FEA 问题中。

## 3. 选题层

选题切中结构可靠性中最常见的矛盾：失效概率积分通常发生在小概率尾部，需要大量样本；而真实结构的 LSF 往往来自有限元或复杂计算，不能承受 MCS 的百万级调用。

已有方法各有短板。FORM/SORM 快但受线性化和正态变换影响，对非线性边界误差大；传统 response surface、Kriging、SVR、ANN 等 surrogate 需要合适采样策略，否则会在重要失效边界附近不够准；一些 active learning 方法过度关注 limit-state boundary，可能忽略 less-important region 的整体形状。

本文的选题把新增样本选择设计成一个可靠性几何问题：既要靠近标准正态空间原点以获得高 PDF，又要在代理边界上，还要与已有样本保持距离。这种三重约束使样本自动聚焦在“最可能影响失效概率”的区域。

## 4. 位置层

论文位于 RBF surrogate、active learning reliability 和 U-space reliability transformation 的交叉位置。RBF 提供插值型全局近似，Rosenblatt transformation 把随机变量转到标准正态空间，序贯优化则决定下一次昂贵 LSF 评估在哪里发生。

相对 MPP-based FORM，SSRM 不直接在真实 LSF 上找 MPP，而是在 surrogate boundary 上寻找高 PDF 新样本，再用真实 LSF 校正 surrogate。这样可以避免每轮都对昂贵模型做梯度或可靠指标优化。

相对 AK-MCS 或 EFF 等 Kriging 方法，SSRM 的特色不是不确定性函数，而是 PDF maximization + limit-state equality + minimum distance。它更偏几何采样策略，RBF 本身也比 Kriging 训练轻。

## 5. 贡献层

第一项贡献是构造基于 RBF 的 surrogate LSF。论文讨论 Gaussian、inverse multiquadric、thin plate spline 等径向基函数，并通过 LOOCV 选择 shape parameter c，因为插值模型在训练点 RMSE 为零，不能用普通训练误差调参。

第二项贡献是提出 SSRM 序贯采样优化。新增样本在标准正态 U-space 中求解：最小化 `||u||`，等价于最大化标准正态 PDF；约束为 surrogate LSF 等于 0、与已有样本距离不小于 d_min，并限制搜索边界在 [-5,5]。

第三项贡献是引入最小距离约束。该约束避免新增点全部堆在同一个局部 MPP 附近，使代理模型在 less-important region 也逐步改善，降低非线性或多区域边界下的漏判风险。

第四项贡献是用七类算例展示适应性，从低维解析问题到高维 40/100/250 维问题。每个算例都比较 FORM、SORM、MCS、IS、DS、AK-MCS、2SMART 等方法中的一部分，用函数调用数和相对误差说明效率。

## 6. 方法层

方法输入包括随机变量分布、原始 LSF、初始样本规模、RBF kernel、shape parameter 选择规则、MCS 样本数和序贯停止准则。输出是 surrogate-based failure probability 估计、最终 RBF 模型和真实 LSF 调用次数。

流程先用 Rosenblatt transformation 把变量转到标准正态空间，再用 LHS 生成 m+1 或 2m+1 个初始样本并计算真实 LSF。随后拟合 RBF surrogate，通过 LOOCV 选取 shape parameter c。

每轮迭代中，用固定随机种子的 MCS 在当前 surrogate 上估计失效概率，检查相对/绝对收敛；若未收敛，则求解新增样本优化问题，将新点带回真实 LSF 计算，加入样本集并重建 RBF。

d_min 通常取为 `λ` 倍最大最近邻距离，λ=0.2。对于高维问题，论文也给出 penalty 形式的无约束优化版本，用遗传算法求解，牺牲部分全局精度换取可求解性。

## 7. 证据层

图 1 展示不同代理近似 LSF 的效果，图 2 展示初始 surrogate，图 3 给出 SSRM 流程，图 4 到图 7 展示二维算例的序贯采样过程。它们直观说明新增点如何沿高概率边界扩展。

低维算例证据较强。圆管裂纹算例中，3 个初始点加 4 个新增点即可得到 Pf≈0.034347，相对误差约 0.0175%。超球面算例中，3 个初始点加 9 个新增点得到 Pf≈3.381e-2，明显优于 FORM/SORM。悬臂梁和减速器轴算例中，SSRM 分别用 18 和 44 次真实 LSF 调用获得约 1% 或近零误差。

中等维工程算例包括 9 维悬臂管和非线性振子。悬臂管中 SSRM 用 18 次调用得到 Pf≈1.052e-3，误差约 0.574%；非线性振子中用 19 次调用得到 Pf≈2.880e-2，误差约 1.623%，与更高调用数的 active Kriging 方法相比具有竞争力。

高维算例 m=40、100、250 时，SSRM 总调用数分别约 198、348、734，相对误差约 2.53%、0.58%、3.77%；相比 2SMART 的 3729、6036、10707 次调用，函数调用仅约 5.3%-6.9%。这支撑了“高维下效率显著提高，但精度略有折中”的结论。

## 8. 结构语言层

文章结构是可靠性方法论文的标准路线：Introduction 批判 FORM/SORM/MCS 和现有 surrogate，随后介绍 RBF construction 与 validation，再给 SSRM 算法，最后用大量算例证明。方法段落相对短，算例篇幅较大，说明作者主要靠实证对比建立可信度。

语言上，作者强调 “important region”“high failure probability”“limit-state boundary”“less-important region” 这些空间概念，把抽象采样策略变成 U-space 中的几何直觉。读者能理解为什么新增点不是随机加，而是被 PDF 和边界共同牵引。

可复用的表达是“代理模型精度应该优先改善失效概率积分最敏感的区域，而不是全域均匀变准”。这是可靠性主动学习论文中很有价值的论证句式。

抽取层面，正文误抽了 `where` 标题，图题有合并和错位，部分表格尤其迭代过程表 OCR 混乱。当前资料足以理解算法和主要算例结果，但不能直接照抄所有表格数值。

## 9. 引用风险层

引用链覆盖 MVM、FORM、SORM、MCS、响应面、Kriging、SVR、ANN、RBF 和多个可靠性 benchmark。作为 RBF-based sequential surrogate reliability method 引用比较稳妥。

主要风险是 RBF surrogate 的维数适应性。高维算例显示函数调用数仍会随维数增加，且需要 2m+1 级别初始点；对于极高维且强非线性多失效域问题，RBF 插值可能需要更多样本或变量筛选。

第二个风险是新增样本优化本身。算法需要在 surrogate boundary 上求解带距离约束的优化问题；如果 surrogate 边界有多个孤立区域，遗传算法可能漏掉关键区域。论文的 min distance 只能缓解，不能完全保证全局探索。

第三个风险是它依赖固定随机种子的 surrogate-MCS 收敛判断。失效概率很小时，MCS 样本数和随机波动会影响停止判断；正式工程应用应做重复计算或置信区间分析。

## 10. 复用层

可复用的选题模板是：对于昂贵隐式 LSF，不追求全空间代理精度，而设计能自动靠近高概率失效边界的序贯采样规则，以少量真实模型调用估计 Pf。

可复用的方法链是：`U-space transformation -> LHS initial design -> RBF surrogate with LOOCV shape parameter -> surrogate-MCS Pf estimate -> constrained new-point search on surrogate boundary -> true LSF update -> convergence check`。

可复用的证据组织是低维可视化展示采样轨迹，中维工程算例证明复杂非线性，最后用高维算例证明调用数优势。每个算例都同时报 Pf、relative error 和 LSF evaluations。

自检：本报告只使用十个指定标题；摘要、结论、图表、公式、引用风险和抽取问题均收进十层。明显抽取问题为 metadata 题名/作者缺失、误抽 `where` 标题、图题错位和部分表格 OCR 噪声。
