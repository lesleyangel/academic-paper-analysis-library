# A sequential surrogate method for reliability analysis based on radial basis function

## 0. 读取说明

本拆解基于 `801/文本/txt/A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural-.txt`。抽取文本包含公式、表格和多数比较数值，但若需核对 Fig. 4-Fig. 12 中迭代点位置、失效边界曲线和高维问题收敛曲线，需要 PDF 图像复核。由于全文公式抽取存在换行与符号错位，公式解读以功能和逻辑为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Surrogate model, 3 Sequential surrogate reliability method, 4 Numerical examples, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A sequential surrogate method for reliability analysis based on radial basis function
- 作者：Xu Li, Chunlin Gong, Liangxian Gu, Wenkun Gao, Zhao Jing, Hua Su
- 期刊与年份：Structural Safety, 73, 2018, 42-53
- 领域：结构可靠性分析、代理模型、主动学习、RBF、失效概率估计
- 类型：方法论文 + 数值/工程算例验证
- 研究对象：隐式且计算昂贵的 limit state function (LSF) 的失效概率估计。
- 主要方法：基于 RBF 的 sequential surrogate reliability method (SSRM)，通过优化问题迭代选择新增样本点。
- 主要证据：圆管、超球边界、悬臂梁、减速器轴、悬臂管、非线性振子和高维问题等 7 个算例，与 MCS、FORM、SORM、响应面、AK-MCS、2SMART 等方法比较。

这篇论文是典型 Structural Safety 方法文：核心不是新工程对象，而是提出一种更省 LSF 调用的可靠性计算流程。

## 2. 摘要与核心信息提取

摘要的逻辑非常紧：提出 RBF-based SSRM -> 每次求解一个特殊优化问题找新样本 -> 新点要落在近似 LSF 上且离已有点有最小距离 -> 通过迭代提高重要失效边界和非重要区域精度 -> 减少昂贵有限元 LSF 调用 -> 多算例验证准确性和效率。

一句话主张：SSRM 利用联合概率密度和近似失效边界信息，在 RBF 代理模型上顺序添加高价值样本，从而以较少昂贵 LSF 调用获得可靠失效概率。

核心贡献：

- 用 RBF 构造 LSF 代理模型。
- 以“最大化 PDF + 位于近似 LSF + 与已有点保持最小距离”为新增样本准则。
- 用 MCS 在代理模型上估计失效概率，避免反复调用原始昂贵模型。
- 通过低维非线性和高维算例证明方法兼具准确性和效率。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural-.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-sequential-surrogate-method-for-reliability-analysis-base_2018_Structural-.md`。

中文译文：

> 提出了一种基于径向基函数（RBF）的顺序代理可靠性方法（SSRM），该方法通过解决特殊的优化问题来迭代更新极限状态函数（LSF）的代理模型。优化问题的目标是找到一个新点来最大化概率密度函数（PDF），但受到新点位于近似LSF上并且到现有点的最小距离大于或等于给定距离的约束。通过用新点更新代理模型，LSF代理模型在失效概率较高的重要区域和LSF边界上变得越来越准确。此外，由于最小距离约束，不重要区域的精度在迭代内进一步提高。 SSRM利用PDF和LSF的信息来捕获失效特征，这减少了由昂贵的有限元分析定义的隐式LSF的样本。数值算例表明，SSRM以较少的样本量提高了失效边界周围重要区域代理模型的精度，并且对非线性LSF具有更好的适应性，从而提高了可靠性分析的精度和效率。 �2018 Elsevier Ltd. 保留所有权利。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自结构可靠性中常见但高价值的计算瓶颈：失效概率本质是多维积分，直接 MCS 或数值积分在隐式有限元模型上代价极高；FORM/SORM 依赖局部 Taylor 展开，非线性强时误差大；传统响应面和已有主动学习方法可能局部过密采样或初始点依赖强。

作者把问题收束为“如何在有限样本预算下，让代理模型优先准确描述高失效概率区域和 LSF 边界”。这比泛泛提高代理模型精度更具体，因为可靠性分析真正关心的是失效边界附近，而不是全域均匀误差。

选题价值是方法价值：如果原始 LSF 是有限元、CFD 或多学科仿真，少调用几十到几千次就能带来巨大成本下降。

## 4. 领域位置与文献版图

Introduction 按可靠性方法谱系组织：

- MVM：高效但要求输入变量正态且只适合低非线性。
- FORM：在 MPP 做一阶展开，较 MVM 准确，但需要优化找 MPP，强非线性误差大。
- SORM：二阶展开，非线性适应性提升，但二阶梯度代价高。
- Response surface / surrogate methods：用代理模型替代昂贵 LSF，可结合 MCS/IS。
- Adaptive/active learning：迭代增加重要区域样本，提高局部精度。
- 代理模型家族：PRSM、RBF、Kriging、SVR、ANN；本文选择 RBF，因为非线性适应性好且易实现。

本文位置是“主动学习可靠性方法”的一个 RBF 变体。它的差异在于新增样本准则同时利用 PDF、近似 LSF 和最小距离约束，而不是只追踪 MPP 或单一学习函数。

## 5. Gap 制造机制

作者制造 gap 的方式是逐个指出既有方法的适用边界：

- FORM/SORM：局部近似，对复杂非线性边界有限。
- 响应面：样本少时可能捕捉不到复杂结构行为。
- 已有迭代响应面/代理模型：可能在重要区域局部收敛，非重要区域精度改善不足，或 MPP 搜索不稳。
- 高维问题：带等式约束的样本搜索可能难收敛。

本文 gap 是“如何在重要区域和较不重要区域之间平衡采样，使代理模型既贴近失效边界，又不在局部过拟合”。最小距离约束就是针对这个 gap 的方法设计。

## 6. 创新性判断

作者声明的创新是 SSRM：通过求解新增样本优化问题，顺序改进 RBF 代理模型。

真实创新判断：

- 算法准则创新：中等偏强。`maximize PDF`、`on approximated LSF`、`minimum distance` 三者组合清晰回应可靠性采样需求。
- 工程价值：强。大量算例显示低维问题显著减少 LSF 调用，高维问题也比 2SMART 更高效。
- 理论创新：中等。没有提出新的可靠性理论，但提出一个可执行采样策略。
- 验证强度：较强。7 个算例覆盖解析、结构和高维问题。

创新风险是该方法仍依赖 GA、MCS 和 RBF 参数优化；当原始 LSF 不昂贵时，代理模型内部开销可能不值得。

## 7. 论证链条复原

论证链条：

可靠性失效概率积分昂贵 -> 经典近似方法存在非线性和梯度代价问题 -> 代理模型可降低原始 LSF 调用，但采样位置决定精度 -> RBF 适合构造非线性代理 -> 本文提出 SSRM，用 PDF 与 LSF 边界共同引导新增样本，并用最小距离避免局部拥挤 -> 通过 MCS 在代理模型上估计 Pf 并迭代收敛 -> 多算例显示 SSRM 在准确性和 LSF 调用数上优于或接近已有方法。

闭合较强：每个方法设计都能回到“失效边界 + 高概率区域 + 省样本”。薄弱点是终止准则和 GA 搜索参数对结果的敏感性没有像算例对比那样充分展开。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
- 已有研究不足/GAP：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models. However, it re In this paper, an efficient method for reliability analysis named SSRM is proposed. However, as the parameter optimization of the surrogate model, MCS, and GA take a number of surrogate evaluations, SSRM shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis).
- 本文解决方式：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively. By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd.
- 学术或工程增量：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint. Several numerical examples show that SSRM improves the accuracy of the surrogate model in the important region around the failure boundary with a small number of samples and has a better adaptability to the nonlinear LSF, hence increases the accuracy and efficiency of the reliability analysis. �2018 Elsevier Ltd. Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

SSRM 的流程：

1. 用 LHS 选初始样本，计算真实 LSF 响应。
2. 用 RBF 插值构造初始代理模型。
3. 基于代理模型做 MCS，估计当前失效概率 Pf。
4. 求解新增点优化问题：目标是最大化 PDF；约束是新点位于近似失效边界，且与已有样本距离不小于给定 dmin。
5. 对新增点调用真实 LSF，更新样本集和 RBF。
6. 重复直到达到最大迭代、相对收敛或绝对收敛条件。

关键设计：

- RBF：以径向基函数线性组合逼近 LSF，强调易实现和非线性能力。
- 最小距离约束：防止新增点全部挤在 MPP 附近，也让非重要区域逐步改善。
- 高维处理：将强约束优化问题通过惩罚函数思想转化为近似无约束问题，再用 GA 搜索。
- 终止条件：相邻 Pf 变化满足相对误差 1e-4 和绝对误差 1e-3 等条件，或达到样本上限。

方法的边界：适合原始 LSF 调用昂贵的隐式模型；如果 LSF 显式且便宜，GA、MCS、代理参数优化的内部成本反而可能不划算。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| SSRM 能用较少样本逼近失效边界 | 摘要、4.1-4.2 | 圆管、超球问题迭代图；圆管仅少量新增样本后 Pf 接近 MCS | 强 | 迭代点位置需 PDF 图像复核 |
| SSRM 对非线性 LSF 适应性好 | 摘要、4.2、4.6 | 超球、非线性振子等非线性算例；相对误差接近 MCS | 中-强 | 非线性类型仍是选定算例，不能覆盖全部复杂边界 |
| SSRM 在低维工程问题中比 FORM/SORM 更准确高效 | 4.3-4.5 | 悬臂梁、减速器轴、悬臂管表格中 SSRM 相对误差小且 LSF 调用少 | 强 | 表格抽取需核对列对齐 |
| SSRM 在高维问题中比 2SMART 更高效 | 4.7 | m=40/100/250 时 SSRM LSF evaluations 为 198/348/734，2SMART 为 3729/6036/10707；Pf 接近 MCS | 强 | 高维算例为特定 benchmark |
| 最小距离约束能兼顾重要与非重要区域 | 方法、结论 | 方法逻辑和迭代图说明样本不只集中于 MPP | 中 | 缺少无最小距离约束的消融实验 |
| SSRM 只有在 LSF 昂贵时优势明显 | 结论 | 作者承认 RBF 参数优化、MCS、GA 需要大量代理模型评估 | 强 | 这是方法适用边界，也是实际部署前必须判断的成本条件 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：MVM/FORM/SORM 在原始空间和标准正态空间的 LSF 近似示意，承担“经典方法局限”教学功能。
- Table 1：RBF 类型，支撑代理模型选择。
- Fig. 3：SSRM 流程图，是全文方法核心图。
- Fig. 4-Fig. 7：圆管、超球、悬臂梁、减速器轴的迭代过程，展示样本逐步贴近失效边界。需要 PDF 图像复核。
- Fig. 8-Fig. 10：悬臂管和非线性振子对象示意，承担工程/动力学算例定义功能。
- Fig. 11-Fig. 12：非线性振子和高维问题迭代过程，支持高维/动态响应适用性。
- Table 3/Table 5/Table 7/Table 9/Table 11/Table 13/Table 15：不同可靠性方法的 Pf、相对误差、LSF evaluations，是主要证据表。
- 公式 (1)：失效概率积分定义，给出问题本体。
- 公式 (2)-(7)：RBF 代理构造。
- 新增点优化问题相关公式：定义 PDF 最大化、LSF 边界和最小距离约束，是方法创新所在。
- 公式 (13)-(14)：代理模型 MCS 失效概率和 CoV，支撑 Pf 估计。

## 11. 章节结构与篇章布局

真实章节：1 Introduction -> 2 Surrogate model -> 3 Sequential surrogate reliability method -> 4 Numerical examples -> 5 Conclusions。

结构是标准方法论文：先铺可靠性方法谱系，再介绍基础代理模型，再给新算法，再用大量算例验证。第 4 节篇幅最大，按算例难度从低维解析/结构逐步推进到动态响应和高维问题，形成“由易到难”的证据节奏。

标题命名直接而简洁。优点是读者能迅速定位方法和验证；不足是 `Numerical examples` 下小节多但标题只是对象名，若改写可突出验证目的，如 `Hyper-sphere bound problem for nonlinear boundary tracking`。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Surrogate model（方法/模型/算法）
  - L3 p.2: 2.1 Construction of surrogate model（方法/模型/算法）
  - L3 p.3: 2.2 Validation of surrogate model（方法/模型/算法）
- L2 p.3: 3 Sequential surrogate reliability method（方法/模型/算法）
- L2 p.5: 4 Numerical examples（对象/模块/过渡章节）
  - L3 p.5: 4.1 Circular pipe structure（对象/模块/过渡章节）
  - L3 p.5: 4.2 Hyper-sphere bound problem（问题定义）
  - L3 p.5: 4.3 Cantilever beam（对象/模块/过渡章节）
  - L3 p.5: 4.4 Speed reducer shaft（对象/模块/过渡章节）
  - L3 p.7: 4.5 Cantilever tube problem（问题定义）
  - L3 p.9: 4.6 Dynamic response of a nonlinear oscillator（对象/模块/过渡章节）
  - L3 p.9: 4.7 High-dimensional problem（问题定义）
- L2 p.11: 5 Conclusions（结论/贡献回收）
- L2 p.11: Acknowledgements（尾部材料）
- L2 p.11: Appendix A Supplementary data（尾部材料）
- L2 p.11: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Surrogate model | 2 | 2 | 方法/模型/算法 |
| 2.1 Construction of surrogate model | 2 | 3 | 方法/模型/算法 |
| 2.2 Validation of surrogate model | 3 | 3 | 方法/模型/算法 |
| 3 Sequential surrogate reliability method | 3 | 2 | 方法/模型/算法 |
| 4 Numerical examples | 5 | 2 | 对象/模块/过渡章节 |
| 4.1 Circular pipe structure | 5 | 3 | 对象/模块/过渡章节 |
| 4.2 Hyper-sphere bound problem | 5 | 3 | 问题定义 |
| 4.3 Cantilever beam | 5 | 3 | 对象/模块/过渡章节 |
| 4.4 Speed reducer shaft | 5 | 3 | 对象/模块/过渡章节 |
| 4.5 Cantilever tube problem | 7 | 3 | 问题定义 |
| 4.6 Dynamic response of a nonlinear oscillator | 9 | 3 | 对象/模块/过渡章节 |
| 4.7 High-dimensional problem | 9 | 3 | 问题定义 |
| 5 Conclusions | 11 | 2 | 结论/贡献回收 |
| Acknowledgements | 11 | 2 | 尾部材料 |
| Appendix A Supplementary data | 11 | 2 | 尾部材料 |
| References | 11 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 段落是“方法族谱式综述”：每段介绍一种可靠性方法，先讲原理，再讲优点，最后指出限制。这个模式非常适合方法论文制造 gap。

方法段落节奏是“定义符号 -> 给公式 -> 解释变量 -> 说明算法步骤”。结果段落每个算例通常先定义 LSF 和变量分布，再说明初始样本和新增样本数，最后用表格比较 Pf、误差和 LSF evaluations。

可学习之处：作者在每个算例中不只给数值，还解释为什么 SSRM 在该算例表现好或一般，例如低维问题 MPP 易捕捉，高维问题 Taylor 方法误差大。这让结果不是表格堆砌，而是和方法机制相互解释。

## 13. 文笔画像与语言习惯

整体语气是方法稳健型，常用 `proposed`, `constructed`, `captures`, `improves`, `reduces`, `demonstrate`。claim 强度较高，但由大量 benchmark 表支撑。

主动/被动：方法提出处用主动或无主句；公式和算法步骤大量被动，如 `is constructed`, `is solved`, `is selected`。时态稳定：已发表文献用过去时/现在完成时，方法定义用一般现在时，算例结果用一般现在时描述表格。

高频词：`surrogate`, `reliability`, `failure probability`, `LSF`, `samples`, `RBF`, `MCS`, `optimization`, `boundary`, `nonlinear`。语言风格偏数学工程，不重修辞，重变量和比较指标。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：20958
- 高频词：model(57)；surrogate(40)；lsf(37)；samples(36)；sample(28)；failure(27)；ssrm(25)；mcs(19)；method(19)；probability(18)；reliability(18)；region(17)；variables(17)；step(16)；function(15)；optimization(15)；initial(15)；random(14)；space(14)；accuracy(13)
- 高频名词化/学术名词：failure(27)；probability(18)；reliability(18)；function(15)；optimization(15)；information(8)；distance(8)；iteration(7)；distribution(6)；approximation(6)；nonlinearity(6)；section(6)；prediction(6)；dimension(6)；adaptability(5)
- 高频学术动词：constructed(3)；construct(3)；presented(3)；compared(2)；analyzed(1)；predicted(1)；optimize(1)；estimate(1)；estimated(1)；achieve(1)；evaluate(1)；demonstrate(1)
- 高频形容词：initial(15)；important(11)；original(10)；normal(10)；different(8)；sequential(7)；boundary(5)；less(5)；local(4)；radial(4)；variable(4)；integral(3)；numerical(3)；computational(3)；iterative(3)
- 高频副词：eventually(2)；strictly(2)；iteratively(2)；essentially(1)；analytically(1)；finally(1)；commonly(1)；gradually(1)；sequentially(1)；directly(1)；instinctually(1)；roughly(1)；fully(1)；briefly(1)；totally(1)
- 高频二词短语：surrogate model(36)；failure probability(13)；reliability analysis(10)；random variables(10)；important region(9)；model lsf(8)；standard normal(7)；minimum distance(7)；optimization problem(7)；response surface(6)；sequential surrogate(6)；sample set(6)
- 高频三词短语：surrogate model lsf(7)；standard normal space(5)；sequential surrogate model(4)；initial surrogate model(4)；limit state function(3)；carlo simulation mcs(3)；original design space(3)；less important region(3)；construction surrogate model(3)；mcs reliability analysis(3)；monte carlo simulation(2)；performs first-order taylor(2)
- 被动语态估计：60；`we + 动作动词` 主动句估计：0
- 一般现在时线索：136；一般过去时线索：109；现在完成时线索：0；情态动词线索：18

分章节正文词频：

- 1 Introduction: lsf(15)；method(10)；model(10)；failure(9)；region(9)；reliability(9)；mpp(7)；important(7)
- 2 Surrogate model: model(20)；surrogate(10)；samples(9)；sample(7)；prediction(6)；rbf(6)；matrix(5)；method(4)
- 3 Sequential surrogate reliability method: model(22)；samples(21)；surrogate(20)；lsf(20)；step(16)；sample(16)；initial(14)；failure(13)
- 4 Numerical examples: example(5)；variables(4)；ssrm(3)；mcs(3)；random(3)；examples(2)；different(2)；space(2)
- 5 Conclusions: ssrm(5)；surrogate(5)；model(5)；failure(4)；probability(3)；method(2)；analysis(2)；sample(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

背景句：

- `When uncertainties are involved, the failure probability ... should be examined.`
- 模仿：当系统包含不可避免的不确定性时，X 的概率评估成为设计决策的核心。

Gap 句：

- `However, the approximation error increases with the increase of the nonlinearity.`
- 模仿：然而，随着问题非线性/维度/耦合程度提高，现有近似误差显著增加。

方法句：

- `This section presents the detailed procedure of the proposed...`
- 模仿：本节给出所提方法的完整流程，并说明每个步骤如何服务目标函数。

结果句：

- `As expected, ... obtains more accurate result with fewer samples.`
- 模仿：结果符合方法设计预期，即在关键区域增加样本后，模型以更少高保真调用达到相近精度。

边界句：

- `SSRM shows its superiority only when the LSFs are time-consuming implicit functions.`
- 模仿：该方法的优势主要出现在 X 成本较高的场景；对于低成本问题，其额外优化开销可能不经济。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
  可迁移模板：By updating the surrogate model with the new points, the surrogate model of METHOD becomes more and more accurate in the important region with a high failure probability and on the METHOD boundary.
- 原句：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
  可迁移模板：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
- 原句：Pf is essentially a multi-dimensional integral formulated as Pf ¼ Z Z ��� Z D pðxÞdx1dx2 ���dxm ð1Þ where D is the failure region defined as D ¼ fxjgðxÞ 6 0; x 2 Rmg, and p(x) is the joint probability function.
  可迁移模板：Pf is essentially a multi-dimensional integral formulated as Pf ¼ Z Z ��� Z D pðxÞdx1dx2 ���dxm ð1Þ where D is the failure region defined as D ¼ fxjgðxÞ METHOD; x XRmg, and p(x) is the joint probability function.
- 原句：To calculate the integral with the original LSF faces enormous computational challenges [1–2].
  可迁移模板：To calculate the integral with the original METHOD faces enormous computational challenges [X–X].
- 原句：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
  可迁移模板：By updating the surrogate model with the new points, the surrogate model of METHOD becomes more and more accurate in the important region with a high failure probability and on the METHOD boundary.
#### Gap/转折句
- 原句：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
  可迁移模板：The numerical integral and direct Monte Carlo Simulation (METHOD) are difficult for a complex system with implicit time-consuming analysis models.
- 原句：However, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems.
  可迁移模板：However, it requires the independent input variables obey normal distribution, which is difficult to be satisfied in practical problems.
- 原句：However, the optimization with an equality constraint to find the MPP increases the number of the LSF evaluations.
  可迁移模板：However, the optimization with an equality constraint to find the METHOD increases the number of the METHOD evaluations.
- 原句：Moreover, the adaptability to nonlinear boundary is still limited [10–11].
  可迁移模板：Moreover, the adaptability to nonlinear boundary is still limited [X–X].
- 原句：However, since the accuracy of the response surface method is poor with numbered samples, the complex structural behavior might not be captured.
  可迁移模板：However, since the accuracy of the response surface method is poor with numbered samples, the complex structural behavior might not be captured.
#### 方法提出句
- 原句：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively.
  可迁移模板：A radial basis function (METHOD) based sequential surrogate reliability method (METHOD) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (METHOD) iteratively.
- 原句：By updating the surrogate model with the new points, the surrogate model of LSF becomes more and more accurate in the important region with a high failure probability and on the LSF boundary.
  可迁移模板：By updating the surrogate model with the new points, the surrogate model of METHOD becomes more and more accurate in the important region with a high failure probability and on the METHOD boundary.
- 原句：The numerical integral and direct Monte Carlo Simulation (MCS) are difficult for a complex system with implicit time-consuming analysis models.
  可迁移模板：The numerical integral and direct Monte Carlo Simulation (METHOD) are difficult for a complex system with implicit time-consuming analysis models.
- 原句：The mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig. 1), in which the LSF is assumed to be normal distribution. ⇑Corresponding author.
  可迁移模板：The mean value method (METHOD) [X–X] performs a first-order Taylor expansion of the METHOD at the mean point (as shown in Fig. X), in which the METHOD is assumed to be normal distribution. ⇑Corresponding author.
- 原句：A radial basis function (RBF) based sequential surrogate reliability method (SSRM) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (LSF) iteratively.
  可迁移模板：A radial basis function (METHOD) based sequential surrogate reliability method (METHOD) is proposed, in which a special optimization problem is solved to update the surrogate model of the limit state function (METHOD) iteratively.
#### 结果呈现句
- 原句：The mean value method (MVM) [3–4] performs a first-order Taylor expansion of the LSF at the mean point (as shown in Fig. 1), in which the LSF is assumed to be normal distribution. ⇑Corresponding author.
  可迁移模板：The mean value method (METHOD) [X–X] performs a first-order Taylor expansion of the METHOD at the mean point (as shown in Fig. X), in which the METHOD is assumed to be normal distribution. ⇑Corresponding author.
- 原句：The first-order reliability method (FORM) [5–8] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [9] and then performs a first-order Taylor expansion at the most probable point (MPP) which has the maximum failure probability on the LSF (as shown in Fig. 1).
  可迁移模板：The first-order reliability method (METHOD) [X–X] transforms random variables with different distributions into the same standard normal space U by Rosenblatt transformation [X] and then performs a first-order Taylor expansion at the most probable point (METHOD) which has the maximum failure probability on the METHOD (as shown in Fig. X).
- 原句：Several examples including numerical and engineering cases demonstrate that SSRM has a good adaptability to the LSFs with different nonlinearity and dimensions.
  可迁移模板：Several examples including numerical and engineering cases demonstrate that METHOD has a good adaptability to the LSFs with different nonlinearity and dimensions.
- 原句：However, as the parameter optimization of the surrogate model, MCS, and GA take a number of surrogate evaluations, SSRM shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis).
  可迁移模板：However, as the parameter optimization of the surrogate model, METHOD, and METHOD take a number of surrogate evaluations, METHOD shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis).
#### 贡献/增量句
- 原句：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
  可迁移模板：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
- 原句：Therefore, different approximations of the LSF are adopted to improve the computational efficiency of reliability analysis.
  可迁移模板：Therefore, different approximations of the METHOD are adopted to improve the computational efficiency of reliability analysis.
- 原句：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
  可迁移模板：Moreover, the accuracy of the unimportant region is further improved within the iteration due to the minimum distance constraint.
- 原句：When considering factors such as the failure boundary and probability density, more samples are required to improve the local accuracy.
  可迁移模板：When considering factors such as the failure boundary and probability density, more samples are required to improve the local accuracy.
- 原句：Therefore, iterative response surface reliability analysis methods are proposed [20–30], which increases the samples in the important region near the MPP, and gradually improves the accuracy of the approximation model.
  可迁移模板：Therefore, iterative response surface reliability analysis methods are proposed [X–X], which increases the samples in the important region near the METHOD, and gradually improves the accuracy of the approximation model.
#### 限制/边界句
- 原句：In engineering design, when uncertainties are involved, the failure probability Pf of the limit state function (LSF) g(x) should be examined.
  可迁移模板：In engineering design, when uncertainties are involved, the failure probability Pf of the limit state function (METHOD) g(x) should be examined.
- 原句：Moreover, the adaptability to nonlinear boundary is still limited [10–11].
  可迁移模板：Moreover, the adaptability to nonlinear boundary is still limited [X–X].
- 原句：The response surface is a different commonly used reliability analysis method [14–16].
  可迁移模板：The response surface is a different commonly used reliability analysis method [X–X].
- 原句：However, as the parameter optimization of the surrogate model, MCS, and GA take a number of surrogate evaluations, SSRM shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis).
  可迁移模板：However, as the parameter optimization of the surrogate model, METHOD, and METHOD take a number of surrogate evaluations, METHOD shows its superiority only when the LSFs are time-consuming implicit functions (e.g. finite element analysis).
- 原句：In the future study, the information of the computationally cheap low-fidelity model can be involved to construct a variable-fidelity surrogate model, so that the number of time-consuming high-fidelity sample points is expected to be further reduced.
  可迁移模板：In the future study, the information of the computationally cheap low-fidelity model can be involved to construct a variable-fidelity surrogate model, so that the number of time-consuming high-fidelity sample points is expected to be further reduced.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用密度最高在 Introduction 和代理模型背景段。引用功能：

- 教科书/经典方法：MVM、FORM、SORM、可靠性基础。
- 方法对比：响应面、Kriging、SVR、ANN、AK-MCS、active learning。
- 算例来源：多个 benchmark 结果引用前人，用于表格横向比较。

作者使用引用制造 gap 的方式很规范：每一种前人方法都不是被否定，而是被限定适用边界。这种“承认价值 + 指出失效条件”的姿态比直接批评更适合 Structural Safety。

风险：比较表依赖不同文献中的结果，需确保计算条件完全一致；否则审稿人可能质疑横向比较公平性。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：75
- Introduction 引文簇数量估计：2
- References 条目数：55
- 可识别年份条目数：54
- 2021 年及以后文献数：0
- 2010 年前经典文献数：31
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：[9], [47], [53], [10], [47], [47], [46], [9], [20,53], [4], [9], [6]

带引文的 gap/转折句样例：

- To calculate the integral with the original LSF faces enormous computational challenges [1–2].
- Moreover, the adaptability to nonlinear boundary is still limited [10–11].

References 解析样例（前 8 条）：

- [1] Crespo LG, Kenny SP, Giesy DP. The Nasa Langley Multidisciplinary Uncertainty Quantification Challenge//AIAA Non-Deterministic Approaches Conference, 2015.
- [2] Yao W, Chen X, Luo W, et al. Review of Uncertainty-based Multidisciplinary Design Optimization Methods for Aerospace Vehicles. Prog Aerosp Sci 2011;47 (1):450–79.
- [3] Choi SK, Canfield RA, Grandhi RV. Reliability-based Structural Design. London: Springer; 2007. p. 207–12.
- [4] Verma AK, Srividya A, Karanki DR. Reliability and Safety Engineering. Springer; 2009. p. 15–167.
- [5] Cawlfield JD. Application of First-order (form) and Second-order (sorm) Reliability Methods: Analysis and Interpretation of Sensitivity Measures Related to Groundwater Pressure Decreases and Resulting Ground Subsidence. Sensitivity Anal, 317–327.
- [6] Du X. Unified Uncertainty Analysis By the First Order Reliability Method. J Mech Des, 2008;130(9).
- [7] Haldar A, Mahadevan S. First-order and Second-order Reliability Methods. Springer Us 1995:27–52.
- [8] Verderaime V. Illustrated Structural Application of Universal First-order Reliability Method. Nasa Sti/recon Technical Report N, 1994, 95(August 1994).
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 缺消融：没有系统比较去掉最小距离约束或只用 PDF/只用 LSF 的版本。
- GA 参数敏感性：新增点搜索依赖 GA，参数和随机性对结果影响未充分讨论。
- 代理内部成本：MCS、RBF 参数优化和 GA 虽不调用原始 LSF，但在高维时仍可能重。
- 初始样本策略：LHS 初始样本数量 m+1 或 2m+1 的经验规则可能影响收敛。
- 高维扩展：m=250 benchmark 表现不错，但真实工程高维耦合 LSF 可能有多失效域。
- 图表复核：迭代点和失效边界图需要 PDF 核对，文本抽取无法显示点分布。

## 17. 可复用资产

- 选题套路：从“直接积分昂贵”切入，逐个限定经典方法边界。
- Gap 套路：已有方法可行但在非线性、高维、昂贵 LSF 下不稳或低效。
- 方法图资产：流程图必须显示初始样本、代理构建、样本搜索、真实评估、MCS 和终止。
- 表格资产：统一用 Pf、relative error、number of LSF evaluations 三列比较。
- 结论资产：在强调优势后主动声明适用边界和未来 variable-fidelity surrogate 方向。

## 18. 对我写论文的启发

方法论文最需要把“新增设计选择”变成可解释的约束。SSRM 的最小距离约束不是数学装饰，而是回应局部过密采样问题；这种设计-问题对应关系很值得模仿。

另一个启发是验证集要有梯度：低维解析、工程结构、动态响应、高维问题逐步升级，比只用一个复杂案例更能说服审稿人。

## 19. 最终浓缩

最值得学习：把可靠性分析的样本选择问题重新表述为 PDF、LSF 边界和样本距离三者平衡的优化问题。

最大风险：算法有效性依赖 GA 搜索、RBF 参数和 benchmark 条件；缺少消融与真实复杂有限元大算例。

可迁移三点：

1. 综述经典方法时按“原理-优点-局限”写。
2. 方法创新要用一个清晰准则公式承载。
3. 验证表统一指标，使准确性和计算成本一眼可比。
