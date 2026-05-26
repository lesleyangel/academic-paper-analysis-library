# Multidisciplinary uncertainty propagation method considering correlated field variables for rocket systems

## 0. 读取说明

本拆解基于 `801/文本/txt/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.txt` 的全文抽取。文本包含方法公式、流程图题、表格和结论，但双栏抽取使部分公式附近语句交错；本拆解以可辨正文为主。流程图、PDF 曲线和相关系数图像细节均需 PDF 图像复核。

## 1. 基本信息与论文身份

- 题名：Multidisciplinary uncertainty propagation method considering correlated field variables for rocket systems。
- 作者：Siyi Du、Chunna Li、Yang Liu、Chunlin Gong、Weikai Gao。
- 期刊：Probabilistic Engineering Mechanics，82，2025，103857。
- 领域：多学科不确定性传播、相关随机变量、场变量降维、火箭系统可靠性/不确定性分析。
- 论文类型：方法提出 + 解析算例验证 + 固体火箭系统应用。
- 研究对象：火箭气动、发动机、轨迹学科之间既含数值变量又含场变量的相关不确定性传播。
- 主要方法：POD 降维场变量，Nataf transformation 生成相关样本，maximum entropy 根据前四阶矩估计 PDF，warm-start 加速 PDF 求解。
- 对比基准：MCS；同时比较 considering correlation 与 ignoring correlation。
- 核心指标：相关系数保真、输出变量前四阶矩误差、PDF 拟合、速度/总能量标准差和下界误差。

## 2. 摘要与核心信息提取

一句话主张：多学科 UP 中忽略上游状态变量之间的相关性会显著降低精度，尤其当变量是随时间/空间分布的场变量时；本文通过 POD + 改进 Nataf + warm-start maximum entropy 同时处理数值变量和场变量相关性，从而提升固体火箭系统速度和能量下界的不确定性预测精度。

摘要的结构是：工程背景（rocket lifecycle uncertainties）-> 现有 UP 方法缺陷（忽略 field variables correlation）-> 方法核心（Nataf 相关样本 + warm-start maximum entropy 加速 PDF）-> 案例证据（固体火箭多学科 UP）-> 量化收益（速度/总能量标准差精度分别提高 22.75% 和 32.57%，下界提高 5.20% 和 4.20%）。

## 3. 选题层深拆

选题来自多学科设计优化和不确定性传播中的工程痛点：火箭系统由气动、发动机、轨迹等学科耦合组成，为了工程流程可操作，通常要解耦各学科并用统计矩传递不确定性；但解耦后如果把上游输出变量视作独立，会破坏真实相关结构。

作者进一步把普通相关变量问题升级为“场变量相关”。数值变量只是一维标量，场变量如推力曲线、质量随时间变化、风场/温度场等是向量/函数，相关性不仅存在于变量之间，也存在于场的不同维度。这个定义使问题更有 Probabilistic Engineering Mechanics 的方法价值。

## 4. 领域位置与文献版图

文献组织先从 UMDO 和 multidisciplinary UP 的重要性讲起，再区分 numerical variables 与 field variables。随后引用单学科相关变量 UP、输入变量相关性处理、分布式多学科概率分析等研究，指出已有工作主要处理单学科或数值变量，尚未解决 multidiscipline + correlated field variables。

本文站位是把相关性从“输入随机变量”扩展到“跨学科传播的状态变量”，并把变量类型从标量扩展到场变量。POD、Nataf 和 maximum entropy 都是成熟工具，但组合后服务一个更复杂的多学科 UP 场景。

## 5. Gap 制造机制

Gap 很明确：existing studies have not yet addressed multidisciplinary UP with correlated field variables。作者没有只说“相关性被忽略”，而是先解释为什么解耦多学科时会出现相关性丢失，再说明 field variables 使相关性量化更难。

Gap 的层级是：多学科系统必须解耦 -> 解耦后通常用统计矩传递 -> 上游输出变量有相关性 -> 标量相关已有方法，场变量相关难 -> 火箭系统同时存在数值变量和场变量相关 -> 需要统一处理方法。

这个 gap 与方法设计紧密对应：POD 处理场变量维数，Nataf 处理相关结构，maximum entropy 处理未知边缘 PDF，warm-start 处理计算效率。

## 6. 创新性判断

作者声明的贡献有两点：一是能够在多学科 UP 中考虑场变量相关性；二是引入 warm-start maximum entropy 加速 Nataf 中场变量 PDF 计算。

真实创新属于“方法集成 + 应用场景扩展”。Nataf、POD、最大熵不是新方法，但将它们组织成可同时处理数值变量和场变量的多学科传播流程，并在固体火箭系统中演示，有明确工程价值。

创新强度中等。优点是流程完整、指标清晰；风险是相关性主要按 Pearson 线性相关处理，场变量必须同维，边缘 PDF 只由前四阶矩近似。

## 7. 论证链条复原

1. 火箭系统生命周期中存在多源随机不确定性，需要多学科 UP 支撑可靠设计。
2. 工程上常解耦学科独立分析，但上游学科输出的状态变量往往相关。
3. 忽略相关性会使下游 UP 的标准差、下界和 PDF 偏离。
4. 场变量相关性难处理，因为场样本维度高且分布复杂。
5. 用 POD 把场变量映射到低维模态系数，用前四阶矩和相关系数描述传播信息。
6. 用 Nataf transformation 依据边缘 CDF 和 Pearson 相关生成相关样本。
7. 对复杂场变量边缘 PDF，用 maximum entropy 根据前四阶矩估计；用 warm-start 按与标准正态矩差异排序加速求解。
8. 解析四子系统算例验证方法能保留数值变量和场变量相关性，且比 MCS 大幅减少响应函数调用。
9. 固体火箭气动-发动机-轨迹案例显示考虑相关性显著改善速度和总能量标准差/下界。
10. 结论承认同维场变量限制，并提出未来预处理统一维度。

## 8. 方法/理论/模型细拆

整体流程以某一当前学科 UP 为例。上游输出样本 X_C 包含数值样本 S_CN 和场样本 S_CF。场样本先经 POD 降维，得到模态矩阵 phi 和模态系数 a；再计算数值样本和模态系数的前四阶统计矩，以及相关系数矩阵 rho。当前学科源输入变量假设相互独立，通过反 CDF 生成独立输入样本。

相关转换分两部分。对于数值变量和场变量的低维模态系数，以某个参考场样本/模态系数为 reference，使用改进 Nataf transformation 将独立样本转成相关样本。对于场变量，先用模态系数重构独立场样本，再以参考场样本做 Nataf 相关转换，最终组合数值和场相关样本输入当前学科模型。

Nataf transformation 的作用是：用边缘 CDF 把原变量映射到标准正态空间，用 Cholesky 分解在标准正态空间施加目标相关矩阵，再反变换回原空间。maximum entropy 用均值、标准差、偏度、峰度作为约束求 PDF；warm-start 的技巧是对场维度按统计矩与标准正态矩差异排序，上一维优化得到的特征参数作为下一维初值，以加速 PDF 计算。

POD 的作用是降低场变量维度，使场变量相关可转化为低维模态系数相关。作者建议累积能量贡献超过 99%，高精度需求超过 99.9%。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 方法能保持数值变量相关系数 | 解析算例/Table 1 | 原始与重采样 rho_ca1d1、rho_ca1d2 误差 0.01%，rho_d1d2 误差 1.5% | 强 | 解析变量分布较简单 |
| 方法能保持场变量相关结构 | 解析算例/Fig. 7 | c1 与 c2 原始/重采样 Pearson 相关系数曲线接近 | 中强 | 曲线细节需 PDF 图像复核 |
| 考虑相关性显著改善解析输出 e 的标准差 | Table 2 | μ2 相对误差考虑相关为 0.06%，忽略相关为 21.33% | 强 | μ3 相对误差很大但数值小 |
| 方法大幅降低计算代价 | Table 2 | MCS nf=1e6，本文 nf=1e3 | 强 | 只针对该解析算例 |
| 火箭气动学科中升阻相关保持良好 | Table 6 | lift/drag 相关系数最大相对误差 0.24% | 强 | 仅列若干飞行条件 |
| 发动机场变量 thrust/mass 相关保持良好 | Fig. 10-11/结论 | 关键时间点与模态系数最大误差 5.80%，场样本最大误差 3.08% | 强 | 场变量必须同维 |
| 固体火箭 UP 精度提升明显 | Tables 7-8 | 速度/总能量标准差精度提升 22.75%/32.57%，下界提升 5.20%/4.20% | 强 | MCS 样本与 surrogate 模型误差需复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 说明多学科 UP 中相关变量被忽略的问题 | gap 建立 | y1/y2 相关在下游传播中丢失 | 需要 PDF 图像复核 |
| Fig. 2-3 | 总流程和上游数据处理 | 方法完整性 | 数值/场变量分离，场变量 POD 降维 | 需要 PDF 图像复核 |
| Eq. 1-4 | POD 模态系数和统计矩差异 | 场变量降维与 warm-start 排序 | 用前四阶矩组织 PDF 求解 | 文本可确认 |
| Fig. 4-5 | 相关转换和 warm-start 最大熵流程 | 方法机制 | reference + Nataf + ME 组合 | 需要 PDF 图像复核 |
| Eq. 5-13 | Nataf 正反变换 | 生成相关样本 | 标准正态空间施加相关性 | 文本可确认 |
| Eq. 14-18 | Maximum entropy PDF | 边缘分布估计 | 前四阶矩约束，求 Lagrange 参数 | 文本可确认 |
| Fig. 6-8/Tables 1-2 | 解析算例验证 | 方法准确和高效 | 相关性保留，PDF 贴近 MCS | 需要 PDF 图像复核 |
| Fig. 9/Tables 3-5 | 火箭系统 UP 关系与源不确定性 | 工程应用场景 | 气动/发动机/轨迹学科输入明确 | 需要 PDF 图像复核 |
| Tables 7-8/Figs. 12-13 | 输出矩和 PDF 比较 | 考虑相关性更准 | 标准差和下界明显改善 | 表格可确认，PDF 图需复核 |

## 11. 章节结构与篇章布局

章节为 Introduction -> Method -> Analytical validation -> Solid rocket application -> Conclusion。结构是方法论文的“先搭框架、再用玩具算例验证、再上工程案例”的标准路线。

Introduction 花较多篇幅区分 numerical variable 与 field variable，这一步很重要，因为它让读者理解为什么普通相关随机变量方法不够。Section 2 是技术核心，按 UP 流程、相关转换、Nataf、maximum entropy、POD 依次展开。Section 3 用解析例证明方法机制；Section 4 用固体火箭证明工程意义；Conclusion 明确给出三条贡献和一个限制。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：2
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：章节标题数量较少，难以判断并列性。
- 章节名主要风格：方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Multidisciplinary uncertainty propagation method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Method validation by the analytical test | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

方法段落高度步骤化，经常使用 “Step 1/2/3/4” 和 a/b/c/d 子步骤。它不是纯理论推导，而是面向可实现流程，把每个变量从上游样本到当前学科输入的变换讲清楚。

验证段落节奏是“建立系统关系 -> 说明哪些变量相关 -> 对比相关系数 -> 对比输出矩/PDF”。工程案例段落则是“火箭学科关系 -> 不确定性源表 -> 相关性保持验证 -> 输出 UP 精度比较”。

## 13. 文笔画像与语言习惯

文风偏概率工程方法，术语密度高但叙述线性。高频词包括 uncertainty propagation、correlation、field variables、numerical variables、Nataf transformation、maximum entropy、POD、statistical moments、resampled samples、MCS。

作者常用 “To address this challenge”、“The procedure is shown”、“The results indicate”、“Notably” 等推进词。claim 语气在方法能力上较强，如 “enables accurate generation”，但在限制处也明确写 “requires correlated field variables to have the same dimension”。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：variables(86)；samples(65)；field(62)；method(61)；correlation(56)；uncertainty(39)；numerical(38)；multidisciplinary(33)；correlations(32)；transformation(32)；rocket(31)；discipline(27)；correlated(23)；among(23)；variable(23)；coefficient(23)；input(22)；nataf(21)；entropy(21)；maximum(21)
- 高频学术名词：field(62)；method(61)；correlation(56)；analysis(40)；transformation(32)；system(19)；energy(16)；propagation(13)；optimization(12)；velocity(10)；separation(10)；reference(10)；model(9)；results(9)；comparison(9)；function(9)
- 高频学术动词：proposed(12)；shown(3)；compared(3)；indicates(3)；propose(3)；estimate(3)；indicate(2)；capture(2)；estimated(1)；validate(1)；show(1)；evaluate(1)；demonstrate(1)；formulate(1)
- 高频形容词：numerical(76)；multidisciplinary(33)；variable(23)；coefficient(23)；probabilistic(17)；statistical(17)；independent(15)；relative(14)；normal(11)；analytical(10)；total(9)；original(9)；current(8)；previous(7)；aerodynamic(7)；critical(6)
- 高频副词/连接副词：respectively(12)；significantly(8)；however(6)；subsequently(5)；accurately(5)；notably(4)；effectively(4)；usually(4)；explicitly(3)；directly(3)；typically(3)；similarly(3)；closely(3)；consequently(2)；systematically(2)；therefore(2)
- 高频二词短语：field variables(23)；field samples(18)；maximum entropy(16)；correlation coefficient(15)；nataf transformation(14)；probabilistic engineering(13)；numerical samples(12)；correlated field(11)；correlations among(11)；statistical moments(11)；entropy method(10)；solid rocket(10)；coefficient matrix(10)；mode coefficients(10)；uncertainty propagation(9)；total energy(9)
- 高频三词短语：maximum entropy method(8)；correlated field variables(7)；total energy first-stage(7)；correlation coefficient matrix(7)；solid rocket system(6)；eng eng mech(6)；multidisciplinary uncertainty propagation(5)；energy first-stage separation(5)；first-stage separation point(5)；warm-start-based maximum entropy(5)；field samples scf(5)；first four statistical(5)

**主动、被动与句法**

- 被动语态估计次数：80
- `we + 动作动词` 主动句估计次数：8
- 名词化表达估计次数：498
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：130
- 一般过去时线索：31
- 现在完成时线索：3
- 情态动词线索：21
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：variables(24)；field(18)；multidisciplinary(17)；method(15)；correlations(15)；among(9)；rocket(8)；design(8)
- 2. Multidisciplinary uncertainty propagation method：samples(63)；variables(62)；correlation(54)；method(45)；field(44)；uncertainty(32)；numerical(32)；transformation(27)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：Throughout a system's lifecycle, numerous random uncertainties can significantly influence performance.
- Gap 句式：Existing UP methods often neglect correlations among field variables, leading to reduced accuracy.
- 方法句式：We propose a method that explicitly incorporates these correlations.
- 流程句式：The overall process is illustrated in the flowchart, with the detailed steps described as follows.
- 结果句式：The close alignment demonstrates the method's ability to accurately capture...
- 对比句式：Ignoring correlations can cause significant deviations...
- 限制句式：Future work could address this limitation by introducing...

可复用术语：correlated field variables、mode coefficient matrix、first four statistical moments、warm-start strategy、maximum entropy principle、inverse CDF method、reference variable、lower bound accuracy。

## 15. 引用策略与文献使用

引用先服务工程背景：火箭不确定性、UMDO、多学科设计成本。随后引用相关性处理文献，说明单学科或数值变量相关已有基础。方法部分引用 Nataf、maximum entropy、POD 的经典用途，为组合方法背书。工程案例引用固体火箭模型和 PCE surrogate 相关工作，证明案例设置不是凭空搭建。

引用姿态是“承认已有工作解决了一部分，但场变量和多学科耦合仍未覆盖”。这种 posture 很适合方法扩展型论文。

## 16. 审稿人视角风险

1. 相关性使用 Pearson 相关，非线性/尾部相关和 copula 结构可能刻画不足。
2. Maximum entropy 只用前四阶矩，复杂多峰或重尾分布可能近似不充分。
3. warm-start 提速效果没有单独给出详细 CPU 对比，贡献二的证据略弱。
4. 场变量要求同维，真实多学科场变量常不同网格/不同时间步。
5. POD 线性降维可能丢失局部非线性场特征，尤其在强非平稳场中。
6. 固体火箭案例使用 PCE 代理气动/发动机模型，代理误差如何影响 UP 未展开。
7. 只展示考虑/忽略相关两种设置，缺少与其他相关场变量方法的横向比较。
8. μ3 相对误差很高，作者用“数值小影响小”解释，但在尾部风险/下界敏感问题中仍需谨慎。

## 17. 可复用资产

- 问题定义资产：先区分 numerical variable 和 field variable，让 gap 具体化。
- 方法组合资产：POD 降维 + Nataf 相关变换 + 最大熵边缘 PDF，是处理复杂随机场的可迁移框架。
- 证据资产：相关系数保真和输出 UP 精度要同时展示，前者证明方法过程，后者证明工程结果。
- 表格资产：把 “MCS / consider correlation / ignore correlation” 并列，是非常清楚的对比设计。
- 限制写法：结论最后单独承认同维场变量限制，避免被审稿人抓住后显得作者没有意识。

## 18. 对我写论文的启发

如果自己的方法是多个成熟工具组合，必须让组合逻辑服务一个明确难点。本文不是把 POD、Nataf、ME 简单堆起来，而是让每个工具对应一个障碍：维数高、相关性、边缘分布未知、计算慢。

写多学科方法时，解析算例和工程算例最好都要有。解析算例用于可控地证明机制，工程算例用于说明实际价值，这比只给复杂工程案例更容易说服。

## 19. 最终浓缩

这篇论文提出一种考虑相关场变量的多学科不确定性传播方法，用 POD 降维场变量，用 Nataf 生成相关样本，用 warm-start 最大熵估计 PDF 并加速。最强贡献是把“忽略相关性导致 UP 偏差”量化到固体火箭速度/能量标准差和下界上；主要复核点是 PDF 图像、warm-start 加速证据、同维场变量限制和非线性相关刻画能力。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.txt` 与 `801/文本/metadata/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 Multidisciplinary uncertainty propagation method considering correlated field variables for the rocket system （方法/模型）
  - L3 p.3: 2.1 Multidisciplinary uncertainty propagation process considering correlated field variables （对象/问题/模块）
  - L3 p.4: 2.2 Correlation transformation method for both numerical and field samples （方法/模型）
    - L4 p.5: 2.2.1 Improved Nataf transformation method based on warm-start-based maximum entropy （方法/模型）
    - L4 p.5: 2.2.2 Nataf transformation （对象/问题/模块）
    - L4 p.6: 2.2.3 Maximum entropy method （方法/模型）
  - L3 p.6: 2.3 POD method （方法/模型）
- L2 p.6: 3 Method validation by the analytical test （方法/模型）
- L2 p.8: 4 Multidisciplinary uncertainty propagation of a solid rocket system （对象/问题/模块）
  - L3 p.8: 4.1 Problem description （对象/问题/模块）
  - L3 p.9: 4.2 Uncertainty propagation analysis of the solid rocket system considering field variable correlations （对象/问题/模块）
- L2 p.10: 5 Conclusion （结论）
- L2 p.11: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.12: Declaration of competing interest （对象/问题/模块）
- L2 p.12: Acknowledgments （对象/问题/模块）
- L2 p.12: Data availability （对象/问题/模块）
- L2 p.12: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Multidisciplinary uncertainty propagation method considering correlated field variables for the rocket system | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Multidisciplinary uncertainty propagation process considering correlated field variables | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Correlation transformation method for both numerical and field samples | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.1 Improved Nataf transformation method based on warm-start-based maximum entropy | 5 | 4 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.2 Nataf transformation | 5 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.3 Maximum entropy method | 6 | 4 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 POD method | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Method validation by the analytical test | 6 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Multidisciplinary uncertainty propagation of a solid rocket system | 8 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Problem description | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Uncertainty propagation analysis of the solid rocket system considering field variable correlations | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusion | 10 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 11 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 12 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 在火箭的整个生命周期中，大量的随机不确定性会显着影响性能。然而，现有的多学科系统的不确定性传播（UP）方法经常忽略场变量之间的相关性，导致精度降低。为了克服这一限制，我们提出了一种明确包含这些相关性的多学科 UP 方法。对于上层学科传播的变量，应用Nataf变换生成当前学科的相关输入样本，作为不确定性分析的基础。为了加速 Nataf 变换中场变量概率密度函数的计算，我们进一步引入了与最大熵方法相结合的热启动策略。在固体火箭系统多学科UP案例研究中，以蒙特卡洛模拟（MCS）为基准，引入变量相关性，取得了显着的改进：第一级分离点速度和总能量的标准差精度分别提高了22.75%和32.57%，下界精度提高了5.20%和4.20%。
> 
> 这些结果表明，所提出的方法有效地解决了涉及数值和场相关变量的UP问题，显着提高了UP的准确性。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusion；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Multidisciplinary-uncertainty-propagation-method-cons_2025_Probabilistic-Eng.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在本研究中，我们提出了一种多学科 UP 方法，该方法考虑了传播过程中场状态变量之间的相关性。主要结论如下。 1）使用改进的Nataf变换和基于热启动的最大熵方法，可以准确地生成相关场变量。在固体火箭情况下，重采样现场样本的最大误差为 3.08%。 2）通过在相关变换过程中引入参考，该方法可以处理数值变量和场变量。在固体火箭研究中，这使得关键时间点（数值）以及推力和质量（场变量）能够进行相关变换。 3）所提出的方法提高了复杂系统多学科UP的准确性。其中，固体火箭系统第一级分离速度和总能量标准差精度分别提高了22.75%和32.57%，下限精度分别提高了5.20%和4.20%。值得注意的是，所提出的方法要求相关场变量具有相同的维度。未来的工作可以通过在 UP 分析之前引入预处理步骤来统一场变量维度，并根据每个问题的特征定制方法来解决这一限制。 S.杜等人。概率工程力学82(2025)103857

### 20.7 论文逻辑脉络复核

- 提出的问题：To improve perfor mance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3]. Notably, the proposed method requires correlated field variables to have the same dimension.
- 旧方法/已有研究不足：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. Within the UMDO process, however, the accuracy of multidisciplinary UP is crucial, as it directly affects the reliability of design outcomes. However, decoupling introduces a major * Corresponding author.
- 本文解决方式：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy. To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations. To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
- 学术/工程增量：In the case study of UP across multiple disciplines of a solid rocket system, using Monte Carlo simulation (MCS) as the benchmark, incorporating variable correlations yields notable improve ments: the standard deviation accuracy of velocity and total energy at the first-stage separation point increased by 22.75 % and 32.57 %, respectively, while the accuracy of their lower bounds improved by 5.20 % and 4.20 %. These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP. To improve perfor mance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：40
- Introduction 引用簇数量（估计）：7
- References 条目数（解析）：29
- 可识别年份条目数：29
- 近五年/近年文献（2021+）数量：16
- 经典文献（2010年前）数量：4
- 同刊引用数量（按 subject 粗略匹配）：1
- 高频来源期刊（粗略）：Probabilistic Engineering Mechanics(1)
- 引用簇样例：[1], [2,3], [10], [11], [15], [16], [17], [21], [22,23], [27], [0, 10], [28]

带引用的 gap/转折句样例：

- By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
- To address the challenge of incorporating correlations in UP, re searchers have carried out extensive investigations [12–14].

References 解析样例（前12条）：

- [1] X. Du, W. Chen, Efficient uncertainty analysis methods for multidisciplinary robust design, AIAA J. 40 (3) (2002) 545–552.
- [2] N. Zou, C. Gong, L. Zhang, et al., A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory, Probab. Eng. Eng. Mech. 75 (2024) 103558.
- [3] L. Casalino, F. Masseni, D. Pastrone, Uncertainty analysis and robust design for a hybrid rocket upper stage, J. Spacecraft Rockets 56 (5) (2019) 1424–1431.
- [4] C. Wang, H. Fan, X. Qiang, A review of uncertainty-based multidisciplinary design optimization methods based on intelligent strategies, Symmetry-Basel 15 (10) (2023) 1875.
- [5] Z. Liu, Z. Song, P. Zhu, A novel polynomial chaos expansion-based method for feedback-coupled multidisciplinary design optimization under metamodel uncertainty, Struct. Multidiscip. Optim. 65 (5) (2022) 117.
- [6] M.R. Setayandeh, Surrogate model–based robust multidisciplinary design optimization of an unmanned aerial vehicle, J. Aero. Eng. 34 (4) (2021) 04021029.
- [7] W. Yao, X. Chen, W. Luo, et al., Review of uncertainty-based multidisciplinary design optimization methods for aerospace vehicles, Prog. Aeosp. Sci. 47 (6) (2011) 450–479.
- [8] H. Zhu, H. Luo, P. Wang, et al., Uncertainty analysis and design optimization of solid rocket motors with finocyl grain, Struct. Multidiscip. Optim. 62 (2020) 3521–3537.
- [9] H.Z. Huang, X. Zhang, W. Yuan, Collaborative reliability analysis under the environment of multidisciplinary design optimization, Concurr. Eng. 19 (3) (2011) 245–
- 254.
S. Du et al. Probabilistic Engineering Mechanics 82 (2025) 103857
- [10] F. Alhama, A. Campo, Network simulation of the rapid temperature changes in the composite nozzle wall of an experimental rocket engine during a ground firing test, Appl. Therm. Eng. 23 (1) (2003) 37–47.
- [11] S. Li, K. Gurley, Y. Guo, et al., Numerical investigation of turbulence effect on flight trajectory of spherical windborne debris: a multi-layered approach, Probab. Eng. Eng. Mech. 77 (2024) 103661.

### 20.9 常用词、词类、语态与时态

- 高频词：variables(86)；samples(65)；field(62)；correlation(56)；numerical(38)；uncertainty(32)；correlations(32)；transformation(31)；rocket(28)；multidisciplinary(27)；discipline(27)；fig(24)；correlated(23)；among(23)；variable(23)；coefficient(23)；input(22)；matrix(21)；nataf(20)；entropy(19)
- 高频名词化/学术名词：correlation(56)；transformation(31)；mechanics(13)；propagation(13)；velocity(10)；separation(10)；reference(10)；function(9)；distribution(8)；density(7)；deviation(6)；optimization(6)；probability(5)；section(5)；skewness(5)
- 高频学术动词：propose(3)；compared(3)；presented(3)；estimate(2)；indicate(2)；demonstrate(1)；estimated(1)；validate(1)
- 高频形容词：numerical(38)；multidisciplinary(27)；variable(23)；coefficient(23)；statistical(17)；independent(15)；probabilistic(14)；relative(14)；table(12)；normal(11)；total(9)；original(9)；current(8)；previous(7)；aerodynamic(7)
- 高频副词：respectively(12)；subsequently(5)；accurately(5)；significantly(4)；effectively(4)；usually(4)；explicitly(3)；directly(3)；typically(3)；similarly(3)；closely(3)；only(2)；primarily(2)；notably(2)；properly(1)
- 高频二词短语：field variables(23)；field samples(18)；correlation coefficient(15)；maximum entropy(14)；probabilistic engineering(13)；engineering mechanics(13)；nataf transformation(13)；page probabilistic(12)；numerical samples(12)；correlated field(11)；both numerical(11)；correlations among(11)
- 高频三词短语：probabilistic engineering mechanics(13)；page probabilistic engineering(12)；both numerical field(8)；correlated field variables(7)；total energy first-stage(7)；correlation coefficient matrix(7)；solid rocket system(6)；multidisciplinary uncertainty propagation(5)；energy first-stage separation(5)；first-stage separation point(5)；warm-start-based maximum entropy(5)；engineering mechanics fig(5)
- 被动语态估计：61；`we + 动作动词` 主动句估计：7
- 一般现在时线索：136；一般过去时线索：252；现在完成时线索：3；情态动词线索：21

章节词频：

- Abstract: variables(4)；accuracy(4)；correlations(3)；field(3)；rocket(2)；significantly(2)；uncertainty(2)；multidisciplinary(2)
- Introduction: variables(23)；field(16)；correlations(14)；multidisciplinary(13)；among(9)；accuracy(8)；design(7)；within(7)
- Conclusion: field(7)；variables(5)；improved(3)；transformation(3)；solid(3)；rocket(3)；accuracy(3)；multidisciplinary(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Rockets, as critical spacecraft transportation systems, are exposed to random uncertainties throughout their lifecycle due to complex design, fabrication processes, and flight environments [1].
  可迁移模板：Rockets, as critical spacecraft transportation systems, are exposed to random uncertainties throughout their lifecycle due to complex design, fabrication processes, and flight environments [X].
- 原句/结构：To improve perfor mance and ensure reliability, accounting for these uncertainties at every design stage is essential [2,3].
  可迁移模板：To improve perfor mance and ensure reliability, accounting for these uncertainties at every design stage is essential [X,X].
- 原句/结构：Notably, the proposed method requires correlated field variables to have the same dimension.
  可迁移模板：Notably, the proposed method requires correlated field variables to have the same dimension.
#### Gap句
- 原句/结构：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
  可迁移模板：However, existing uncertainty propagation (METHOD) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
- 原句/结构：Within the UMDO process, however, the accuracy of multidisciplinary UP is crucial, as it directly affects the reliability of design outcomes.
  可迁移模板：Within the METHOD process, however, the accuracy of multidisciplinary METHOD is crucial, as it directly affects the reliability of design outcomes.
- 原句/结构：However, decoupling introduces a major * Corresponding author.
  可迁移模板：However, decoupling introduces a major * Corresponding author.
#### 方法句
- 原句/结构：However, existing uncertainty propagation (UP) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
  可迁移模板：However, existing uncertainty propagation (METHOD) methods for multidisciplinary systems often neglect correlations among field variables, leading to reduced accuracy.
- 原句/结构：To overcome this limitation, we propose a multidisciplinary UP method that explicitly incorporates these correlations.
  可迁移模板：To overcome this limitation, we propose a multidisciplinary METHOD method that explicitly incorporates these correlations.
- 原句/结构：To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
  可迁移模板：To accelerate the calculation of the probability density function of field variables within the Nataf transformation, we further introduce a warm-start strategy integrated with the maximum entropy method.
#### 结果句
- 原句/结构：These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP.
  可迁移模板：These results demonstrate that the proposed method effectively addresses METHOD problems involving both numerical and field correlated variables, significantly enhancing the accuracy of METHOD.
- 原句/结构：These results demonstrate that the proposed method effectively addresses UP problems involving both numerical and field correlated variables, significantly enhancing the accuracy of UP. limitation: correlations among state variables are usually neglected, leading to reduced accuracy in the independent UP process.
  可迁移模板：These results demonstrate that the proposed method effectively addresses METHOD problems involving both numerical and field correlated variables, significantly enhancing the accuracy of METHOD. limitation: correlations among state variables are usually neglected, leading to reduced accuracy in the independent METHOD process.
- 原句/结构：These correlations must be properly considered to ensure accurate results of UP.
  可迁移模板：These correlations must be properly considered to ensure accurate results of METHOD.
#### 贡献句
- 原句/结构：This enables independent analysis within each discipline and aligns with practical engineering design practices.
  可迁移模板：This enables independent analysis within each discipline and aligns with practical engineering design practices.
- 原句/结构：By integrating a warm-start-based maximum entropy approach into the Nataf transformation, the method enables efficient and accurate handling of field variables.
  可迁移模板：By integrating a warm-start-based maximum entropy approach into the Nataf transformation, the method enables efficient and accurate handling of field variables.
- 原句/结构：The main contributions of this work are summarized as follows. 1) The proposed method uniquely enables consideration of correlations among field variables within multidisciplinary UP—a capability not available in existing approaches—which significantly improves UP accuracy. 2) To address the computational challenges of calculating the proba bility density function (PDF) of field variables within the Nataf transformation, we introduce a warm-start strategy integrated with the maximum entropy method.
  可迁移模板：The main contributions of this work are summarized as follows. X) The proposed method uniquely enables consideration of correlations among field variables within multidisciplinary METHOD—a capability not available in existing approaches—which significantly improves METHOD accuracy. X) To address the computational challenges of calculating the proba bility density function (METHOD) of field variables within the Nataf transformation, we introduce a warm-start strategy integrated with the maximum entropy method.
#### 限制/边界句
- 原句/结构：By explicitly considering the interactions and synergies among different disciplines, UMDO not only enhances overall system performance but also reduces development costs and shortens the design cycle [7–9].
  可迁移模板：By explicitly considering the interactions and synergies among different disciplines, METHOD not only enhances overall system performance but also reduces development costs and shortens the design cycle [X–X].
- 原句/结构：Research on incorporating correlations among input variables in multidisciplinary systems remains limited.
  可迁移模板：Research on incorporating correlations among input variables in multidisciplinary systems remains limited.
- 原句/结构：Future work could address this limitation by introducing a preprocessing step to unify field variable dimensions before UP analysis, with the approach tailored to the characteristics of each problem.
  可迁移模板：Future work could address this limitation by introducing a preprocessing step to unify field variable dimensions before METHOD analysis, with the approach tailored to the characteristics of each problem.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
