## 0. 读取说明

本文依据 `801/文本/txt/An-efficient-uncertainty-propagation-method-for-nonline_2024_Chinese-Journal.txt` 的全文抽取进行拆解。抽取文本包含摘要、贡献列表、P-box process 定义、CADET 推导、Chebyshev 区间 ODE 求解、Duffing/车辆/运载火箭算例、误差和计算时间表。公式细节较多，本文按文本抽取复原方法逻辑；个别符号、图中曲线和流程图视觉细节需以 PDF 复核。

## 1. 基本信息与论文身份

- 题名：An efficient uncertainty propagation method for nonlinear dynamics with distribution-free P-box processes
- 期刊：Chinese Journal of Aeronautics, 37(12), 2024, 116-138
- 作者：Licong Zhang, Chunna Li, Hua Su, Yuannan Xu, Andrea Da Ronch, Chunlin Gong
- 关键词：Nonlinear dynamics; Uncertainty propagation; Imprecise probability; Distribution-free P-box processes; Chebyshev method

论文身份是“不精确概率过程驱动的非线性动力系统不确定性传播方法”论文。它的目标不是给某一具体工程系统做参数敏感性，而是提出一个通用计算框架：把 distribution-free P-box processes 输入下的非线性动力响应，转化为均值/协方差边界的区间 ODE 问题，并用 Chebyshev 方法非侵入式高效求解。

## 2. 摘要与核心信息提取

摘要的核心信息可以拆成四层：

1. 需求：实际动力系统的不确定性随时间变化，且概率信息常常不完整，无法可靠指定分布类型。
2. 表征：distribution-free P-box process 能表达这种时间变不确定性和分布不精确信息。
3. 难点：非线性动力系统下 P-box 传播计算量巨大，传统抽样型方法代价不可接受。
4. 方法：用 CADET 将 P-box 动力传播转为均值和协方差边界的区间 ODE，再用 Chebyshev 多项式近似求解；响应近似为参数化 Gaussian P-box process。

结果主张：Duffing 振子、车辆行驶和运载火箭黑盒模型中，相对误差小于 3%，计算时间低于参考方法的 0.2%。

一句话浓缩：本文用“统计线性化 + 区间分析 + Chebyshev 近似”替代暴力抽样，使 distribution-free P-box process 下的非线性动力不确定性传播变得可算。

## 3. 选题层深拆

选题针对的是不确定性传播领域的一个夹缝问题。传统随机过程方法要求已知概率分布和相关结构，但工程中常常只有上下界、少量样本或不完整统计信息。区间方法能处理不精确性，但难以给出概率边界。P-box 方法介于二者之间，用上下 CDF 表达分布不确定性；进一步扩展到 P-box process，可以描述随时间变化的不精确随机激励。

难点在非线性动力系统。若对每一种可能 CDF 实现、每一条随机过程样本都做非线性时域仿真，计算量会爆炸。尤其当系统是黑盒模型、单次仿真昂贵时，暴力 Monte Carlo 几乎不可用。

本文选题的亮点是没有试图精确追踪所有概率分布，而是转向响应均值、协方差和 Gaussian P-box 近似。它承认完整不确定性传播太贵，因此寻找一个工程可接受的近似层：先用 CADET 统计线性化给出均值/协方差演化，再通过区间和 Chebyshev 捕捉 P-box 输入导致的边界。

## 4. 领域位置与文献版图

领域版图可分为四块：

第一，随机动力学与不确定性传播。传统方法包括 Monte Carlo、随机摄动、Polynomial Chaos、随机等效线性化等，适合概率信息明确的场景。

第二，不精确概率与 P-box。P-box 通过 CDF 上下界表达分布不确定性，适合数据不足或分布类型未知的问题。

第三，随机过程不确定性建模。distribution-free P-box process 将静态 P-box 与高斯过程/translation theory 结合，用于构造时间相关的不精确随机过程。

第四，CADET 和区间求解。CADET 能把非线性随机动力学近似为均值/协方差 ODE；Chebyshev 多项式方法可非侵入式求解参数化区间问题。

本文位于第二、三、四块的交叉处：把 distribution-free P-box process 从定义和线性传播推进到非线性动力系统的高效近似传播。

## 5. Gap 制造机制

Gap 的制造分三步。

第一步：指出工程输入常常是“distribution-free”的。即只知道 CDF 上下界或支持区间，不知道精确分布类型和参数。传统概率方法要求过强。

第二步：指出 P-box process 已能表征随时间变化的不精确信息，但非线性系统传播难。输入一旦进入非线性动力方程，响应分布不再容易解析，直接嵌套抽样需要大量 CDF 实现和随机样本。

第三步：指出已有 CADET 在随机动力学中可高效传播均值/协方差，但通常假设精确概率或 Gaussian 输入。若能把 CADET 扩展到 P-box 输入，并用区间 ODE 求边界，就能填补“分布自由 P-box process + 非线性动力 + 高效率”的空白。

这个 gap 的说服力来自计算时间量级：Duffing 和车辆参考方法需要超过 1e5 s，火箭黑盒需要超过 4.12e6 s，而 proposed method 为几十秒到数千秒。

## 6. 创新性判断

强创新点：

- 明确提出 nonlinear dynamics with distribution-free P-box processes 的不确定性传播问题定义。
- 将 CADET 从精确随机过程扩展到 P-box 形式，把响应均值和协方差转化为区间 ODE 边界问题。
- 通过 P-box Gaussian assumption 将响应构造成参数化 Gaussian P-box process，从均值/协方差边界进一步得到 CDF 边界。
- 引入 Chebyshev 多项式方法非侵入式求解区间 ODE，避免嵌套 Monte Carlo。

中等创新点：

- 通过 domain analysis 保留均值与方差之间的依赖关系，而不是简单独立区间组合。
- 用三个层级算例验证：解析/半解析 Duffing、车辆二自由度模型、运载火箭黑盒轨迹。

创新边界：

- 响应 Gaussian P-box assumption 是核心近似，强非高斯响应可能失效。
- CADET 不提供自相关函数，因此首穿概率问题未真正求解。
- 方法主要输出 CDF 边界、均值/标准差误差带，对极端尾部或路径相关风险覆盖有限。

## 7. 论证链条复原

全文论证链如下：

1. 工程非线性动力系统存在时间变化且分布不明确的不确定输入。
2. distribution-free P-box process 可以表达这种输入，但直接传播计算昂贵。
3. CADET 可用统计线性化把非线性随机动力系统转化为均值/协方差 ODE。
4. 对 P-box 输入，输入均值/方差不是点值，而是由可能 CDF 构成的可行域。
5. 因此响应均值/协方差演化可转化为 interval ODE 或参数化区间 ODE。
6. 用 domain analysis 生成输入均值/方差可行域，并考虑二者依赖关系。
7. 用 Chebyshev 多项式在可行域上近似 ODE 解，减少端点扫描和重复仿真。
8. 用 Gaussian P-box assumption 由响应均值/协方差边界构造响应 CDF 上下界。
9. 三个算例显示误差小于 3%、计算时间大幅降低，支持方法有效。

## 8. 方法/理论/模型细拆

问题模型从非线性动力系统开始：状态方程形式为 `Xdot=f(X,t)+B(t)W(t)`，其中 `W(t)` 是 distribution-free P-box process。P-box 变量由 CDF 下界和上界定义，distribution-free 表示不预设分布类型。P-box process 通过静态 P-box 与随机过程构造结合，得到随时间演化的不精确随机输入。

CADET 部分是方法核心。对于非线性函数 `f`，CADET 通过统计线性化得到响应均值和协方差的常微分方程。对于精确随机输入，ODE 的系数和输入矩是确定的；对于 P-box 输入，输入均值/方差位于一个可行域，因此均值/协方差 ODE 变成区间 ODE。

Domain analysis 用于从 CDF 上下界生成均值/方差可行域。作者将 P-box 支持域离散为 `Ns=500` 个网格点，生成满足单调性的 CDF realization，并计算对应均值/方差样本。重要的是，均值与方差不是独立区间，作者区分了凸集 `CW` 和超矩形 `IW`，避免过度保守或错误组合。

Chebyshev 方法用于高效求解区间 ODE。测试中多项式阶数取 `d=2`，通过 Chebyshev interpolation points 求解少量 CADET ODE，再用多项式扫描可行域获得响应矩边界。它是非侵入式的，因为不需要改写原动力系统求解器，只需多次调用 CADET。

响应 CDF 构造依赖 Gaussian P-box assumption：用响应均值和方差边界组成一族 Gaussian CDF，从中提取上下 CDF。这个假设简化了完整响应分布传播，但也是方法风险点。

## 9. 证据系统与 Claim-Evidence 表

| Claim | Evidence | 论证功能 | 潜在限制 |
|---|---|---|---|
| 方法在 Duffing 非线性系统上精度高 | 四个 P-box case 中 eUU、eLL、FUV、FLV 多数低于 1.7%，最大约 1.65%；非线性参数 e=1-50 时最大 eLL 约 2.44 | 验证基础非线性算例中的准确性 | Duffing 维度低，不能代表所有非线性 |
| 方法显著降低 Duffing 计算成本 | 参考方法时间 >1.25e5 s，本文方法约 71.61-75.50 s，约 0.06% | 支撑效率主张 | 参考方法为大量 MC，可能不是唯一基准 |
| 方法适用于车辆行驶二自由度系统 | quarter-car 算例四个 case 多数误差 <1.2%，FUXs Case 4 约 1.99；时间约 87.47-90.63 s，相对参考 <0.07% | 证明方法可处理工程型动力系统 | 路面激励形式和系统阶数仍较简单 |
| 方法可用于黑盒运载火箭模型 | LV trajectory 中 Vz 和 Z 的误差最大约 2.99%，计算时间 7812.59 s vs 参考 >4.12e6 s，节省 99.81% | 强化工程复杂模型可用性 | 误差接近 3%，且黑盒细节不可完全审计 |
| Chebyshev 低阶近似已足够 | 算例中使用 d=2 即获得 <3% 误差 | 说明方法实现成本低 | 对更高维、更强非线性输入域可能需更高阶 |
| Domain analysis 考虑均值/方差依赖 | 文中构造 `CW`/`IW`，从 CDF realization 计算均值-方差可行域 | 避免简单区间独立组合导致的过保守 | 抽样离散精度依赖 Ns=500 |
| 方法无法完整覆盖首穿概率 | 文中说明 CADET 不提供自相关函数，first-passage probability 不求解 | 作者主动限定适用范围 | 对可靠性问题是重要短板 |

## 10. 图表、公式与结果叙事提取

| 类型 | 内容 | 论证功能 | 复核备注 |
|---|---|---|---|
| Eq. 1 | 非线性系统 `Xdot=f(X,t)+B(t)W(t)` | 定义研究对象 | 符号需 PDF 核对 |
| Eq. 3 | P-box process 构造 | 表达 distribution-free 随机过程输入 | 公式细节需核对 |
| P-box CDF 图 | CDF 上下界和可能 CDF realization | 直观解释不精确概率 | 需要 PDF 图像复核 |
| Eq. 15 | CADET 均值/协方差 ODE | 将非线性随机动力学转成矩传播 | 符号需 PDF 核对 |
| Eq. 17 | P-box 输入下的 interval ODE | 全文方法核心转换 | 公式编号需核对 |
| Domain analysis 图 | 均值/方差可行域 `CW` 与 `IW` | 说明依赖关系处理 | 需要 PDF 图像复核 |
| Chebyshev 插值公式/节点图 | 用低阶多项式近似区间 ODE 解 | 支撑效率来源 | 节点分布需核对 |
| Fig. 9 流程图 | P-box 输入分析、CADET、Chebyshev、CDF 边界输出 | 展示算法完整流程 | 需要 PDF 图像复核 |
| Duffing 误差表 Table 3 | eUU/eLL/FUV/FLV 和计算时间 | 基础验证 | 数值来自文本抽取 |
| Vehicle ride Table 6 | quarter-car 误差和时间 | 工程系统验证 | 数值来自文本抽取 |
| Launch vehicle Table 8 | Vz/Z 误差和时间 | 黑盒复杂模型验证 | 数值来自文本抽取 |

结果叙事从低维经典非线性系统开始，再到车辆工程模型，最后到黑盒运载火箭轨迹。这个递进让读者逐步接受方法从可控系统到复杂应用的迁移。

## 11. 章节结构与篇章布局

文章结构可复原为：

1. Introduction：不完整概率信息、P-box process、非线性传播计算瓶颈和贡献声明。
2. Problem definition：非线性动力系统、distribution-free P-box process、UP 指标。
3. Proposed method：CADET 扩展、domain analysis、Chebyshev interval ODE、Gaussian P-box response。
4. Numerical examples：Duffing oscillator、vehicle ride comfort、launch vehicle trajectory。
5. Discussion/limitations：误差、效率、首穿概率限制、适用范围。
6. Conclusions：总结 <3% 误差和 <0.2% 时间成本。

布局上的优点是贡献列表很前置，读者能提前知道方法要解决什么。方法部分概念密集，因此后文用三个算例反复呈现同一套误差/时间指标。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/An-efficient-uncertainty-propagation-method-for-nonline_2024_Chinese-Journal.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                       in particular, is the most well-known and is widely applied in | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 8 R 1           1 | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Uncertainty propagation problems under P-box processes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Chebyshev-polynomial-based method for interval ODEs | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.2.1 Uncertainty propagation problems | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

引言段落从“概率信息不足”开始，而不是从某一工程案例开始，这使论文具有方法普适性。随后引入 P-box process，接着指出非线性传播代价，最后自然推出 CADET 和 Chebyshev。

方法段落是层层转化式：系统方程 -> P-box process -> 矩传播 ODE -> 区间 ODE -> Chebyshev 近似 -> Gaussian P-box 输出。每一层都把问题变得更可计算。

算例段落节奏非常统一：定义系统和输入不确定性，给出参考方法，展示 CDF/均值/标准差结果，报告误差和时间。统一格式有助于审稿人横向比较。

## 13. 文笔画像与语言习惯

本文文风偏理论计算与方法学。常见词包括 “distribution-free”, “imprecise probability”, “uncertainty propagation”, “interval ordinary differential equations”, “non-intrusive”, “computational efficiency”。句子通常较长，包含多个限定条件。

常用表达：

- “To the best of the authors' knowledge...”
- “The main contributions are summarized as follows...”
- “The original problem is transformed into...”
- “The proposed method decouples ... from ...”
- “The reference results are obtained by Monte Carlo simulations...”

文章很强调“decoupling”：把 P-box excitation analysis 与 nonlinear stochastic analysis 分离，把昂贵的嵌套抽样转为矩方程边界求解。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：method(118)；p-box(113)；nonlinear(75)；analysis(59)；follows(59)；processes(55)；denotes(54)；bounds(53)；presented(53)；mean(50)；proposed(47)；uncertainty(46)；cdf(45)；dynamics(43)；distribution-free(43)；based(43)；process(40)；interval(40)；time(37)；system(36)
- 高频学术名词：analysis(118)；method(118)；system(36)；model(34)；propagation(30)；assumption(28)；variance(23)；probability(22)；solutions(21)；reference(19)；section(17)；information(14)；results(13)；response(13)；parameters(12)；realization(12)
- 高频学术动词：proposed(47)；shown(21)；solved(14)；solve(8)；investigated(6)；developed(6)；formulated(5)；compared(4)；shows(4)；evaluate(3)；show(2)；evaluated(2)；demonstrate(2)；validated(2)；derived(2)；demonstrated(2)
- 高频形容词：nonlinear(75)；dynamic(60)；interval(40)；cient(28)；stochastic(25)；probabilistic(16)；relative(15)；linear(14)；numerical(14)；signal(14)；parametric(13)；polynomial(13)；basic(12)；static(10)；equal(10)；dynamical(9)
- 高频副词/连接副词：respectively(31)；therefore(18)；however(13)；generally(8)；finally(6)；moreover(5)；ciently(5)；subsequently(5)；notably(4)；cantly(4)；mathematically(4)；easily(4)；recently(3)；accordingly(3)；usually(3)；analytically(2)
- 高频二词短语：p-box processes(46)；distribution-free p-box(37)；nonlinear dynamics(29)；proposed method(29)；uncertainty propagation(26)；expressed follows(21)；flw fuw(20)；dynamics distribution-free(18)；cdf bounds(18)；mean variance(18)；method nonlinear(17)；propagation method(15)；reference solutions(14)；syst signal(14)；cient uncertainty(13)；p-box process(13)
- 高频三词短语：distribution-free p-box processes(24)；nonlinear dynamics distribution-free(18)；dynamics distribution-free p-box(17)；method nonlinear dynamics(14)；cient uncertainty propagation(13)；uncertainty propagation method(13)；propagation method nonlinear(13)；mech syst signal(13)；syst signal process(13)；parametric gaussian p-box(6)；gaussian p-box processes(6)；basic p-box processes(6)

**主动、被动与句法**

- 被动语态估计次数：253
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：779
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：288
- 一般过去时线索：39
- 现在完成时线索：20
- 情态动词线索：78
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：method(9)；p-box(9)；chinese(5)；aeronautics(5)；distribution-free(5)；processes(5)；astronautics(4)；nonlinear(4)
- 1. Introduction                                                       in particular, is the most well-known and is widely applied in：p-box(32)；method(24)；nonlinear(20)；dynamics(17)；distribution-free(17)；denotes(15)；proposed(12)；methods(12)
- 2.2. Uncertainty propagation problems under P-box processes：p-box(53)；method(49)；mean(41)；presented(40)；follows(33)；bounds(30)；processes(27)；cdf(25)
- 4.2.1. Uncertainty propagation problems：method(36)；analysis(33)；nonlinear(30)；uncertainty(26)；dynamic(25)；process(22)；mech(22)；model(20)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

可复用关键词：

- distribution-free P-box process
- imprecise probability
- uncertainty propagation
- nonlinear dynamic system
- CADET
- interval ordinary differential equations
- Chebyshev polynomial approximation
- Gaussian P-box process
- probability bounds
- non-intrusive interval analysis

可复用句式：

- “The uncertainty information is insufficient to specify a unique probability distribution.”
- “The propagation problem is reformulated as the computation of bounds of response moments.”
- “By decoupling the analysis of the P-box excitation from nonlinear dynamic simulations, the repeated sampling cost can be substantially reduced.”
- “The response process is approximated as a parametric Gaussian P-box process.”
- “The relative errors remain below 3%, while the computational time is less than 0.2% of the reference approach.”

中文可复用表达：

- “该方法并不追求恢复响应的完整未知分布，而是通过矩边界和 Gaussian P-box 近似获得工程可用的概率边界。”
- “P-box 的难点不在于表示不确定性，而在于非线性系统中如何避免对所有可能分布逐一传播。”

## 15. 引用策略与文献使用

引用策略是先建立问题谱系，再定位本文空白。随机动力学文献说明传统 UP 方法丰富；P-box 和不精确概率文献说明分布不确定性表达已有基础；P-box process 文献说明时间相关输入已可建模；CADET 和 Chebyshev 文献说明本文采用的计算工具有理论基础。

作者的引用逻辑不是“前人都不行”，而是“前人分别解决了表达和计算的一部分”：P-box process 解决输入表征，CADET 解决随机非线性矩传播，Chebyshev 解决区间求解效率。本文把这些拼接成面向 nonlinear dynamics 的完整传播框架。

## 16. 审稿人视角风险

1. Gaussian P-box assumption 风险：强非高斯、双峰或尾部主导响应可能无法由均值/方差边界充分描述。
2. 首穿概率缺失：文中明确 CADET 无法给出自相关函数，因此 first-passage probability 未解决，对可靠性评估是明显限制。
3. 高维扩展风险：Chebyshev 插值在输入矩可行域维度升高时可能遭遇维数灾难。
4. 区间保守性风险：`CW`/`IW` 可行域构造会影响上下界宽度，过松或过紧都可能影响可信度。
5. 参考方法风险：以大量 MC 作为 reference 虽直观，但 MC 自身误差和计算预算会影响误差评估。
6. 黑盒模型可解释性风险：运载火箭算例证明工程可用性，但模型细节不足时难以判断误差来源。

## 17. 可复用资产

可复用研究问题表述：

- “当输入概率信息不足以指定唯一随机过程时，传统随机动力学传播方法面临模型假设风险。”
- “直接传播 P-box process 需要对可能分布和随机样本进行嵌套计算，导致非线性系统中不可接受的成本。”

可复用方法框架：

1. 用 P-box 表征分布不精确性。
2. 构造随时间变化的 P-box process。
3. 将非线性随机系统转化为响应矩 ODE。
4. 将输入 P-box 导致的矩不确定性转化为区间 ODE。
5. 用非侵入式多项式近似求解区间边界。
6. 用响应矩边界构造概率边界。
7. 用误差和时间双指标验证。

可复用验证指标：

- CDF 上下界误差：F upper/lower。
- 均值/标准差误差带：eUU/eLL 等。
- 相对计算时间百分比。
- 不同非线性强度下的稳定性。

## 18. 对我写论文的启发

这篇论文的最大启发是：复杂不确定性问题可以通过“降低输出目标的野心”来变得可解。作者没有承诺完整响应分布精确传播，而是选择均值/协方差边界和 Gaussian P-box CDF 边界，这使问题从不可计算转为工程可用。

第二个启发是理论方法论文需要递进算例。Duffing 提供可理解非线性，车辆模型提供工程动力学，运载火箭黑盒提供复杂应用。三个算例共同支持“不是玩具问题”的主张。

第三个启发是要主动承认限制。首穿概率无法求解、Gaussian 近似可能失效，这些如果由作者自己说明，会比被审稿人指出更稳妥。

## 19. 最终浓缩

本文提出一种用于 distribution-free P-box processes 驱动非线性动力系统的不确定性传播方法。它把 P-box 输入下的非线性随机响应传播，通过 CADET 转化为响应均值和协方差边界的区间 ODE 问题，再用 Chebyshev 多项式非侵入式求解，并以 Gaussian P-box assumption 构造响应概率边界。Duffing、车辆和运载火箭算例显示误差通常低于 3%，计算时间相对嵌套抽样参考方法低于 0.2%。论文的关键贡献是把“分布未知 + 时间相关 + 非线性动力”这一昂贵传播问题转化为可快速求解的矩边界问题。
