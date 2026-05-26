# A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles

## 0. 读取说明

本拆解基于 `801/文本/txt/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.txt`。文本抽取能确认摘要、章节、材料、主要方程、表格数值和结论；但 Fig. 2-Fig. 16 中热流分布、温度场、位移场、电势场和输出功率曲线的空间细节需要 PDF 图像复核。本文是 2021 年 MTPS 论文的前序工作，拆解时特别关注它如何提出初代 TE-material TPS 概念。

## 1. 基本信息与论文身份

- 题名：A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles
- 作者：Chun-Lin Gong, Jian-Jun Gou, Jia-Xin Hu, Feng Gao
- 期刊与年份：Aerospace Science and Technology, 77, 2018, 458-470
- 机构：Northwestern Polytechnical University
- 领域：高超声速热防护、热电材料、热-力-电耦合、工程热流预测
- 类型：概念结构设计 + 材料制备/选择 + 单胞数值模拟
- 研究对象：0.01 m2 量级的多功能 TPS 单胞结构，包含 TE couple 与传统热防护层。
- 关键材料：p-type Ca3Co4O9，n-type Sr0.9La0.1TiO3；n 型材料由固相反应法制备。
- 主要方法：工程算法计算气动热，建立 unit cell 模型，施加周期边界条件和底部对流边界，评估热-力和热电性能。

这篇论文的身份是“TE 热防护概念的首轮工程可行性证明”。它不像 2021 年论文那样强调多尺度边界和细观承载细节，而是先证明热电材料嵌入 TPS 可产生电能且不破坏基本热防护功能。

## 2. 摘要与核心信息提取

摘要采用典型 Applied Engineering 结构：传统 TPS 低效 -> 提出 TE-material based multifunctional TPS -> 给出热电材料组合 -> 对特定飞行器和轨迹计算气动热 -> 用单胞模型做非稳态热-力-电评估 -> 得出应用潜力。

一句话主张：将高温热电材料引入高超声速 TPS，可以在执行热防护的同时把部分气动热转化为电能，且该结构的性能可通过工程热流算法和单胞热-力-电耦合模型快速评估。

核心数据：

- 结构面积示例：0.01 m2，含 128 个 p-n couples。
- 底部对流系数 10/50/100/300 W/(m2 K) 下，底面最高温度约为 639/497/431/364 K。
- 对应 0.01 m2 结构平均输出功率约 0.406/0.618/0.756/0.913 W。
- 平均 TE 转换效率约 0.237%/0.400%/0.499%/0.607%。
- 主结论：主动冷却/底部对流能明显改善输出功率和转换效率。

## 3. 选题层深拆

选题从“高超声速飞行器速度提升带来气动热”切入。传统 TPS 的目标是保护结构，但热量被耗散或隔绝，能量利用效率低。作者没有直接做热电材料论文，而是把材料嵌入 TPS，使热防护系统本身成为电源补充。

问题定义很工程化：在一条典型 reusable launch vehicle 轨迹上，计算特定点 M 的气动热流，然后把热流作为单胞输入，评估结构热-力-电行为。这样做把“热电 TPS 是否有潜力”变成“在典型轨迹和给定材料组合下，底面温度、位移、应力、电势和功率能否接受”。

选题价值来自三方面：工程节能价值、快速评估方法价值、热电材料应用价值。它还为后续 2021 论文留下升级空间：初代结构证明概念，后续再补承载框架、两级 TE、真实机械边界。

## 4. 领域位置与文献版图

Introduction 的文献组织有四组：

- 气动热预测：CFD 精度高但成本大，工程算法效率高，适合快速 TPS 评价。
- 传统 TPS 材料：C/SiC、C/C、UHTC、隔热层等，重点是热防护。
- 热电材料：按工作温区分类，本文选高温/中高温材料而非低温 Bi2Te3 体系。
- TE generator/TPS 结合：已有热电发电和高超声速热复用设想，但缺少面向具体轨迹、具体 TPS 单胞和热-力-电耦合的完整评估。

作者站位是“应用创新 + 方法整合”：将已有热电材料和 TPS 设计结合，而不是提出全新材料物理。文献评价较温和，主要强调“传统 TPS 有热防护功能但效率不足”“CFD 准确但不适合快速评估”。

## 5. Gap 制造机制

本文 gap 是多层制造的：

- 效率 gap：传统 TPS 通常只用于 thermal protection，气动热没有被复用。
- 评价 gap：高保真 CFD 代价高，工程上需要能快速输入轨迹热流的评估方法。
- 材料-结构 gap：高温 TE 材料有潜力，但如何嵌入 TPS 并承受热-力环境缺少具体结构和单胞验证。
- 边界 gap：单胞模型如果不使用合适的周期边界，结果可能不合理。

这个 gap 的强度中等偏强。它能支撑一篇概念和评估论文，但如果作为“热电效率突破”论文则不足，因为输出效率仍低。作者通过把目标定位为“application potentials”而非成熟系统，降低了 gap 过度承诺风险。

## 6. 创新性判断

作者声明的创新包括 TE-material based TPS concept、n 型 Sr0.9La0.1TiO3 制备与 p 型 Ca3Co4O9 组合、评价方法和单胞性能计算。

真实创新判断：

- 应用创新：较强。热电材料嵌入高超声速 TPS，面向具体轨迹。
- 方法创新：中等。工程热流 + unit cell + 周期边界 + 热电后处理的集成流程。
- 材料创新：弱-中。n 型材料制备是必要支撑，但不是全文最强创新。
- 结构创新：中等。构型足以说明概念，但相较后续 MTPS 细节较粗。

创新的可信证据主要是 Table 3 的功率和效率、Fig. 9-Fig. 16 的温度/位移/电势/功率曲线。最容易被挑战的是“significant application potentials”的强度，因为平均效率最高也只有 0.607%。

## 7. 论证链条复原

论证链条：

高超声速飞行器热环境严酷 -> TPS 必须保护结构但传统系统热利用效率低 -> 热电材料可在温差下产生电势 -> 选择合适高温 p/n 型材料并形成多功能 TPS 单胞 -> 用工程算法计算轨迹热流 -> 建立热-力-电耦合单胞模型并施加周期边界与底部对流 -> 分析温度、位移、电势、输出功率和效率 -> 得出该结构有供电潜力，且主动冷却可提高 TE 性能。

逻辑闭合处在“热流输入 -> 温差 -> 电输出”这一主线。薄弱处在“结构长期可靠性”和“系统级收益”，因为论文没有做重量、寿命、疲劳、实际电路或界面退化评估。

## 8. 方法/理论/模型细拆

方法分四段：

1. 车辆与轨迹：给出飞行器几何和典型轨迹，确定待分析点 M。
2. 气动热：使用工程算法估算气动热流，避免 CFD 代价。
3. 多功能 TPS 单胞：设计包含 TE module 和 TPS 层的单胞，选择 Ca3Co4O9 与 Sr0.9La0.1TiO3。
4. 数值模型：使用耦合热-力-电方程，建立 unit cell mesh；对横向缩尺模型施加周期边界；设置底部对流系数；考虑材料界面热接触电阻 TCR 的影响。

关键假设：

- 单胞通过周期边界代表宏观结构。
- TE couple 在理想负载匹配时用 E2/(4r) 估算最大功率。
- 底部对流相当于内部主动冷却或热管理条件。
- TCR 取 0 与 10^-4 K m2/W 比较，作为界面影响近似。

方法复杂度与目标匹配：这不是高保真全机模型，而是快速可评估框架，适合概念筛选。复现风险在于工程热流算法细节、材料温度依赖参数和 TCR 实现需要进一步查图表/公式。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| TE-material TPS 可把部分气动热转化为电能 | 摘要、5.2、5.3、结论 | 电势分布 Fig. 13-Fig. 15，功率/效率 Fig. 16，Table 3 | 中 | 基于仿真和理想负载，缺实验电输出 |
| 周期边界对单胞热-力分析是必要的 | 4.3、结论 | 不同边界条件下 y-displacement 对比 Fig. 12；结论第 1 点 | 中 | 需要 PDF 图像复核曲线差异和误差量 |
| 底部对流/主动冷却改善 TE 性能 | 5.3、结论 | 对流系数从 10 到 300 W/(m2 K)，平均效率由 0.237% 到 0.607%，平均功率由 0.406 到 0.913 W | 强 | 底部冷却实现代价未纳入系统权衡 |
| 该结构可以满足不同内部温控需求 | 结论 | 底面最高温度随对流系数为 639/497/431/364 K | 中 | 只是温度指标，未讨论内部设备真实温度限制 |
| TCR 对该工况下温度和电势影响较小 | 5.2 | TCR 与无 TCR 最大/平均温度偏差 0.6%/0.2%，电势偏差 4%/1% | 中 | 只测试特定 TCR；真实界面随热循环变化 |
| 大面积真实飞行器可能获得千瓦级供电 | 5.3 | 由 0.01 m2 输出外推到大面积，文本称最大/平均可达更高量级 | 弱-中 | 外推过强，未考虑布置面积、线缆、热流不均和质量 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：飞行器和轨迹，确定工程场景和热流输入来源。
- Table 1：不同区域气动热预测方法，支撑工程算法的适用范围。
- Fig. 2：气动热流曲线，是后续热-力-电分析的输入证据；需要 PDF 图像复核峰值和时间段。
- Fig. 3-Fig. 4：多功能 TPS 结构和热传递路径，承担概念图功能。
- Fig. 5-Fig. 6：n 型材料制备与 Seebeck/电阻率测试，支撑材料选择。
- Table 2：TE 材料物性，连接材料数据与仿真。
- Fig. 7：单胞模型、网格和边界，支撑方法复现性。
- Fig. 9-Fig. 12：温度场、位移、边界条件对比，是热-力安全性证据；需要 PDF 图像复核。
- Fig. 13-Fig. 15：电势和 p/n couple 热电结果，支撑“温差产生电输出”。
- Fig. 16/Table 3：输出功率和转换效率，是全文核心结果证据。
- 公式：气动热流工程算法、TE figure of merit、热-力-电控制方程、周期边界约束、功率 E2/(4r)。公式承担“从轨迹热流到电输出可计算”的桥梁功能。

## 11. 章节结构与篇章布局

真实章节：1 Introduction -> 2 The vehicle, trajectory and aerodynamic heat -> 3 The multi-functional TPS structure -> 4 Numerical model -> 5 Results and discussions -> Conclusions。

结构属于“应用场景先行”的工程论文：先定义车辆和热流，再讲结构，再建模，再给结果。与很多方法论文相比，它没有单独 Related Work，而是把文献综述压在 Introduction 中。

标题命名偏好是描述型：`The vehicle, trajectory and aerodynamic heat`, `The multi-functional TPS structure`, `Numerical model`。优点是读者很容易跟随工程输入到模型输出；缺点是结果小节标题略宽泛，`Thermoelectric conversion efficiency` 是最有信息量的小标题。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：10
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                         to mesh generation, especially the grid near the vehicle surface | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Aerodynamic heat | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Fabrication of n-type material and its TE properties | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Physical properties of other materials | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 4 Numerical model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Governing and constitutive equations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 The unit cell model and its mesh | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Thermo-mechanical performance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.2 Thermoelectric performance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 先从热环境讲必要性，再比较热流预测方法，接着介绍 TPS 材料与热电材料，最后落到“本文开发快速评估方法”。段落推进是“工程需求 -> 方法选择 -> 材料机会 -> 本文方案”。

结构和模型段落的节奏偏说明书式：每段围绕一个对象（车辆、热流、材料、边界、界面）展开。结果段落先描述图，再给数值，再解释趋势。例如功率结果段先说明最大功率计算方式，再用不同对流系数曲线说明趋势，最后外推到真实面积。

可学习之处是将“热流输入”单独成节，这让后续所有性能结果都有明确上游来源。热管理论文若缺少这一层，容易显得只是理想边界下的结构演示。

## 13. 文笔画像与语言习惯

整体语气是“概念提出 + 潜力证明”，常用 `proposed`, `developed`, `evaluated`, `indicate`, `potential`。相比 2021 年论文，这篇更谨慎，常用 “has potentials” 而非“can replace power supply”。

时态：引言综述用现在时和过去时；实验/制备用过去时；结果图表用现在时。被动语态较多，用于材料制备、模型建立和边界条件；主动语态主要出现在 `In this work` 开头的贡献句。

高频词围绕 `temperature`, `material`, `heat`, `thermoelectric`, `TPS`, `coefficient`, `power`, `efficiency`。形容词偏工程性能：`efficient`, `reliable`, `high-temperature`, `multi-functional`, `typical`。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：heat(62)；structure(49)；temperature(48)；thermal(46)；tps(43)；material(42)；work(41)；based(37)；aerodynamic(37)；vehicle(36)；materials(36)；respectively(32)；coe(31)；surface(30)；boundary(29)；power(28)；cient(26)；electric(26)；model(24)；bottom(24)
- 高频学术名词：structure(98)；temperature(48)；material(42)；materials(36)；model(24)；performance(22)；results(21)；conditions(21)；method(20)；protection(19)；condition(18)；science(16)；supplement(14)；analysis(12)；properties(12)；system(10)
- 高频学术动词：shown(18)；developed(11)；evaluated(6)；shows(5)；proposed(5)；formulated(4)；simulated(3)；indicates(2)；indicate(2)；validate(1)；show(1)；evaluate(1)；predict(1)；develop(1)
- 高频形容词：thermal(46)；material(42)；aerodynamic(37)；boundary(29)；cient(26)；electric(26)；thermoelectric(22)；numerical(18)；convective(17)；potential(16)；hypersonic(15)；supplement(14)；typical(13)；different(13)；electrical(11)；high(10)
- 高频副词/连接副词：respectively(32)；however(7)；supply(6)；therefore(5)；widely(3)；mainly(3)；especially(2)；carefully(2)；closely(2)；directly(2)；separately(2)；tively(2)；spectively(2)；usually(1)；nally(1)；partly(1)
- 高频二词短语：aerodynamic heat(27)；coe cient(23)；tps structure(20)；thermal protection(16)；conversion ciency(15)；unit cell(15)；aerospace science(14)；science technology(14)；boundary conditions(13)；convective coe(13)；gong aerospace(12)；electric potential(12)；bottom surface(12)；output power(12)；cell model(11)；aerosp sci(10)
- 高频三词短语：aerospace science technology(14)；gong aerospace science(12)；unit cell model(10)；aerosp sci technol(8)；convective coe cient(7)；thermal protection system(6)；seebeck coe cient(6)；output power conversion(6)；power conversion ciency(6)；convective coe cients(5)；appl therm eng(5)；sci technol supplement(5)

**主动、被动与句法**

- 被动语态估计次数：132
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：441
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：277
- 一般过去时线索：45
- 现在完成时线索：4
- 情态动词线索：77
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：based(5)；structure(5)；hypersonic(5)；ight(5)；thermoelectric(5)；thermal(4)；protection(4)；vehicle(4)
- 1. Introduction                                                         to mesh generation, especially the grid near the vehicle surface：vehicle(16)；heat(16)；tps(14)；material(13)；aerodynamic(10)；work(9)；trajectory(9)；based(8)
- 2.2. Aerodynamic heat：heat(30)；work(19)；structure(18)；temperature(17)；material(17)；aerodynamic(16)；boundary(16)；coe(14)
- 4.2. The unit cell model and its mesh：tcr(13)；edges(5)；vertices(5)；elements(5)；structure(4)；planes(4)；work(4)；related(4)
- 5. Results and discussions：mechanical(1)；thermal(1)；electrical(1)；performances(1)；structure(1)；analyzed(1)；along(1)；typical(1)
- 5.1. Thermo-mechanical performance：surface(13)；temperature(11)；bottom(11)；top(9)；boundary(8)；structure(7)；convective(7)；coe(7)
- 5.2. Thermoelectric performance：power(26)；thermal(17)；respectively(16)；output(14)；average(14)；thermoelectric(14)；supplement(14)；conversion(13)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

背景句：

- `For a flight vehicle, the increasing flying speed brings about a large amount of aerodynamic heat...`
- 可复用结构：对于 X 系统，性能提升同时带来 Y 极端环境，因此 Z 成为安全运行的关键。

Gap 句：

- `and thus leaves some rooms for the improvement of its efficiency.`
- 可复用结构：尽管已有方案可满足基本功能，但从效率/耦合/系统集成角度仍有改进空间。

方法句：

- `the aerodynamic heat is calculated by an engineering-based algorithm`
- 可复用结构：为兼顾工程效率和边界真实性，本文采用 X 方法计算输入载荷，并将其施加到 Y 模型。

结果句：

- `The results indicate that the multifunctional TPS structure has significant application potentials...`
- 可复用结构：结果表明，该结构在给定工况下具备 X 潜力，但仍需进一步系统级验证。

常用短语：`thermal protection purpose only`, `low efficiency`, `typical trajectory`, `unit cell model`, `convective coefficient`, `TE conversion efficiency`, `periodic boundary condition`。

## 15. 引用策略与文献使用

引用分布集中在 Introduction，功能是快速搭建应用背景。作者先引用气动热和高温边界问题，再引用 CFD/工程算法，再引用 TPS 材料和热电材料。文献使用姿态以“补充”和“转折”为主：CFD 精度高但低效，工程算法低精度但高效；传统 TPS 可靠但不复用热；热电材料有潜力但需要结构集成。

引用没有形成很细的热电材料机制综述，因为本文目标不是材料机理。但这也带来风险：对 TE 材料性能、稳定性、氧化和热循环文献讨论略薄。

## 16. 审稿人视角风险

- 效率偏低：平均转换效率 0.237%-0.607%，应用潜力需要系统级面积和质量收益证明。
- 结构简化：单胞结构没有后续论文中的承载框、胶层、导电片嵌入等细节，热应力风险可能低估。
- 主动冷却代价：底部对流提高性能，但引入冷却系统后是否仍“高效”未讨论。
- 实验不足：n 型材料制备有测试，但结构级热-力-电性能没有实验验证。
- 外推风险：从 0.01 m2 外推到全机千瓦级供电可能过强。
- 图像复核：温度场、电势场、位移对比和功率曲线需 PDF 复核。

## 17. 可复用资产

- 选题资产：从“传统系统只满足主功能但效率低”切入，提出“附加能量回收功能”。
- 方法资产：轨迹热流工程算法 + 单胞快速评估，适合早期概念筛选。
- 图表资产：热流输入曲线、结构路径图、材料性能图、边界条件对比图、输出效率表。
- 句式资产：`The simulation approach developed in this work can be used in...`
- 结论资产：按“边界条件必要性 -> 温度控制 -> 输出功率 -> 主动冷却影响”组织结论。

## 18. 对我写论文的启发

这篇论文提醒我，工程概念论文不一定要一开始就做到完整系统级仿真；可以先选择典型轨迹、典型位置和典型单胞，把核心物理链路闭合。只要边界和适用范围讲清楚，单胞论文也能有说服力。

如果模仿它，最好补一个“系统收益”指标，比如单位质量功率、单位面积功率、冷却代价后的净收益，否则容易被审稿人认为只是把复杂度转移到系统层。

## 19. 最终浓缩

最值得学习：用具体轨迹热流和单胞耦合模型证明“热防护 + 热电供电”的早期可行性。

最大风险：功率和效率仍低，且结构级验证依赖仿真和理想边界。

可迁移三点：

1. 把“低效”写成系统 gap，而不是只说材料性能不足。
2. 用典型轨迹和典型点把应用场景钉牢。
3. 在结论中用参数表说明主动冷却、温度和电输出的权衡。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.txt` 与 `801/文本/metadata/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 The vehicle, trajectory and aerodynamic heat （对象/问题/模块）
  - L3 p.2: 2.1 The vehicle and trajectory （对象/问题/模块）
  - L3 p.3: 2.2 Aerodynamic heat （对象/问题/模块）
- L2 p.3: 3 The multi-functional TPS structure （对象/问题/模块）
  - L3 p.4: 3.1 The choosing of p-type material （对象/问题/模块）
  - L3 p.4: 3.2 Fabrication of n-type material and its TE properties （对象/问题/模块）
  - L3 p.5: 3.3 Physical properties of other materials （对象/问题/模块）
- L2 p.5: 4 Numerical model （方法/模型）
  - L3 p.5: 4.1 Governing and constitutive equations （对象/问题/模块）
  - L3 p.6: 4.2 The unit cell model and its mesh （方法/模型）
  - L3 p.6: 4.3 The boundary and initial conditions （对象/问题/模块）
  - L3 p.7: 4.4 Interfaces between different materials （对象/问题/模块）
- L2 p.8: 5 Results and discussions （结果/讨论/验证）
  - L3 p.8: 5.1 Thermo-mechanical performance （对象/问题/模块）
  - L3 p.10: 5.2 Thermoelectric performance （对象/问题/模块）
  - L3 p.11: 5.3 Thermoelectric conversion efﬁciency （对象/问题/模块）
- L2 p.11: Conclusions （结论）
- L2 p.12: Conﬂict of interest statement （对象/问题/模块）
- L2 p.12: Acknowledgements （对象/问题/模块）
- L2 p.12: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 The vehicle, trajectory and aerodynamic heat | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 The vehicle and trajectory | 2 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Aerodynamic heat | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 The multi-functional TPS structure | 3 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 The choosing of p-type material | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Fabrication of n-type material and its TE properties | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Physical properties of other materials | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Numerical model | 5 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Governing and constitutive equations | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 The unit cell model and its mesh | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 The boundary and initial conditions | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.4 Interfaces between different materials | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Results and discussions | 8 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.1 Thermo-mechanical performance | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2 Thermoelectric performance | 10 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3 Thermoelectric conversion efﬁciency | 11 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Conclusions | 11 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Conﬂict of interest statement | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 12 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 文章历史记录： 2017年11月21日收到 2018年1月15日以修订形式收到 2018年3月17日接受 2018年3月21日在线提供
> 
> 传统的高超声速飞行器热防护系统（TPS）通常仅用于热防护目的，效率较低。本文提出了一种基于热电材料的多功能TPS结构概念，并基于特定车辆和典型轨迹开发了其机械热电性能的评估方法。结构中的热电模块可以将一定量的空气动力热转化为电能。该模块由基于固相反​​应方法制备的n型Sr0.9La0.1TiO3化合物和广泛使用的p型Ca3Co4O9组成。针对具有典型弹道曲线的特定高超声速飞行器，通过工程化算法计算气动热，基于晶胞模型分析结构的非定常机械热电特性，最终评估热电转换效率。结果表明，多功能TPS结构在高超声速飞行器上具有显着的应用潜力。 © 2018 Elsevier Masson SAS。版权所有。

### 20.5 结论完整摘录（本地证据）

结论章节识别：Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项工作中，提出了一种基于热电材料的多功能TPS结构并开发了相关的评估方法。结构中的TE模块可以将一定量的气动热转化为电能。 TE电偶由Ca3Co4O9基p型材料和Sr0.9La0.1TiO3基n型化合物组成，通过固相反应方法制备。基于晶胞模型研究了该结构的机械热电性能。基于具有典型弹道曲线的典型可重复使用运载火箭，采用工程化方法计算气动热，并作为数值模拟的输入边界条件。这项工作中开发的模拟方法可用于分析高超声速飞行器的其他轨迹。结果显示了一些结论：
> 
> 对流系数(W/(m2·K))
> 
> 晶胞（单个 p-n 耦合）
> 
> 10 0.0182 0.00317 2.33 0.406 2.63 0.237 50 0.0189 0.00483 2.42 0.618 2.79 0.400 100 0.0195 0.00591 2.50 0.756 3.39 0.499 300 0.0209 0.00713 2.68 0.913 4.09 0.607
> 
> 1. 在基于平移对称性建立的晶胞模型的热机械研究中，周期性边界条件对于获得合理的结果至关重要。 2.
> 
> 对于本文提出的TPS结构，如果底部下方提供系数为10、50、100和300 W/(m2 K)的对流换热，则在研究的轨迹持续时间内，底部表面的最高温度分别为639、497、431和364 K，这提供了

### 20.7 论文逻辑脉络复核

- 提出的问题：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle. In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. 2.
- 旧方法/已有研究不足：需结合 Introduction 的文献转折句复核。
- 本文解决方式：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory. The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9. For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
- 学术/工程增量：For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：61
- Introduction 引用簇数量（估计）：10
- References 条目数（解析）：41
- 可识别年份条目数：44
- 近五年/近年文献（2021+）数量：0
- 经典文献（2010年前）数量：14
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Aerospace Science and Technology(2)
- 引用簇样例：[9], [10], [4], [11,12], [11], [20], [21], [22], [23], [28], [24], [29]

带引用的 gap/转折句样例：

- For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [23] developed an integrated TE module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [24] developed a multi-stage TE module considering the suitable temperature of TE material, and analyzed its thermal protection performance.

References 解析样例（前12条）：

- [1] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re-usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [2] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [3] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [4] D. Knight, H. Yan, A.G. Panaras, A. Zheltovodov, Advances in CFD prediction of shock wave turbulent boundary layer interactions, Prog. Aerosp. Sci. 39 (2) (2003) 121–184.
- [5] D. Knight, J. Longo, D. Drikakis, D. Gaitonde, A. Lani, I. Nompelis, B. Reimann, L. Walpot, Assessment of CFD capability for prediction of hypersonic shock interactions, Prog. Aerosp. Sci. 48 (Supplement C) (2012) 8–26.
- [6] Y. Kerboua, A.A. Lakis, Numerical model to analyze the aerodynamic behavior of a combined conical–cylindrical shell, Aerosp. Sci. Technol. 58 (Supplement C) (2016) 601–617.
- [7] P. Panagiotou, P. Kaparos, C. Salpingidou, K. Yakinthos, Aerodynamic design of a MALE UAV, Aerosp. Sci. Technol. 50 (Supplement C) (2016) 127–138.
- [8] P.D. Bravo-Mosquera, L. Botero-Bolivar, D. Acevedo-Giraldo, H.D. Cerón-Muñoz, Aerodynamic design analysis of a UAV for superficial research of volcanic environments, Aerosp. Sci. Technol. 70 (Supplement C) (2017) 600–614.
- [9] C.D. Engel, S.C. Praharaj, MINIVER Upgrade for the AVID System. Vol. 1: LANMIN User’s Manual, Nasa Cr, 1983.
- [10] E.V. Zoby, K. Sutton, Approximate convective-heating equations for hypersonic flows, J. Spacecr. Rockets 18 (1) (1981)
- 64.
C.-L. Gong et al. / Aerospace Science and Technology 77 (2018) 458–470 469
Output power (W) TE conversion efficiency (%)
TPS structure (128 p–n couples)
Maximum Average Maximum Average Maximum Average
- [11] Y. Ma, B. Xu, M. Chen, R. He, W. Wen, T. Cheng, D. Fang, Optimization design of built-up thermal protection system based on validation of corrugated core homogenization, Appl. Therm. Eng. 115 (2017) 491–500.

### 20.9 常用词、词类、语态与时态

- 高频词：heat(53)；structure(40)；temperature(36)；fig(36)；material(34)；tps(32)；work(32)；aerodynamic(29)；thermal(27)；vehicle(26)；materials(26)；surface(23)；boundary(23)；layer(22)；coe(22)；cient(20)；its(19)；will(19)；conditions(16)；respectively(16)
- 高频名词化/学术名词：structure(40)；temperature(36)；performance(14)；science(11)；conductivity(9)；calculation(8)；protection(7)；condition(7)；evaluation(6)；expansion(6)；radiation(5)；high-temperature(5)；insulation(5)；ture(5)；difference(5)
- 高频学术动词：developed(8)；indicate(1)；predict(1)；develop(1)；indicated(1)；validate(1)
- 高频形容词：material(34)；aerodynamic(29)；thermal(27)；boundary(23)；cient(20)；electric(13)；convective(10)；typical(9)；thermoelectric(7)；numerical(7)；hypersonic(6)；mechanical-thermoelectric(6)；multi-functional(6)；potential(6)；additional(5)
- 高频副词：respectively(16)；only(5)；widely(3)；mainly(3)；carefully(2)；closely(2)；directly(2)；separately(2)；tively(2)；usually(1)；supply(1)；nally(1)；especially(1)；partly(1)；relatively(1)
- 高频二词短语：aerodynamic heat(24)；coe cient(17)；tps structure(14)；aerospace science(10)；science technology(10)；unit cell(10)；boundary conditions(9)；page gong(8)；gong aerospace(8)；bottom surface(8)；convective coe(8)；seebeck coe(7)
- 高频三词短语：aerospace science technology(10)；page gong aerospace(8)；gong aerospace science(8)；science technology fig(6)；seebeck coe cient(6)；multi-functional tps structure(4)；convective coe cient(4)；while bottom surface(4)；hypersonic ight vehicles(3)；work aerodynamic heat(3)；dahlem buck modi(3)；buck modi newtonian(3)
- 被动语态估计：99；`we + 动作动词` 主动句估计：0
- 一般现在时线索：204；一般过去时线索：245；现在完成时线索：0；情态动词线索：56

章节词频：

- Abstract: structure(4)；tps(3)；hypersonic(3)；flight(3)；thermoelectric(3)；received(2)；march(2)；thermal(2)
- Introduction: heat(14)；tps(14)；material(14)；aerodynamic(11)；vehicle(9)；developed(9)；structure(8)；its(8)
- Conclusion: structure(4)；work(3)；heat(3)；unit(3)；cell(3)；material(2)；tps(2)；approach(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle.
  可迁移模板：Thus, a reliable and efficient thermal protection system (METHOD) is essential to ensure the safety of the vehicle.
- 原句/结构：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. 2.
  可迁移模板：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. X.
#### Gap句
- 原句/结构：At present, the numerical method still has some challenges, such as the high requirement * Corresponding author.
  可迁移模板：At present, the numerical method still has some challenges, such as the high requirement * Corresponding author.
- 原句/结构：However, they are much more efficient.
  可迁移模板：However, they are much more efficient.
- 原句/结构：However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
  可迁移模板：However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
#### 方法句
- 原句/结构：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory.
  可迁移模板：In this paper, a thermoelectric material based multifunctional METHOD structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory.
- 原句/结构：The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
  可迁移模板：The module consists of n-type Sr0.XLa0.XTiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
- 原句/结构：For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
  可迁移模板：For a specific Y with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
#### 结果句
- 原句/结构：The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles. © 2018 Elsevier Masson SAS.
  可迁移模板：The results indicate that the multifunctional METHOD structure has significant application potentials on the Y. © XElsevier Masson METHOD.
- 原句/结构：The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles. © 2018 Elsevier Masson SAS.
  可迁移模板：The results indicate that the multifunctional METHOD structure has significant application potentials on the Y. © XElsevier Masson METHOD.
- 原句/结构：The results show some conclusions: Convective coefficient (W/(m2 K)) Unit cell (single p–n couple) 10 0.0182 0.00317 2.33 0.406 2.63 0.237 50 0.0189 0.00483 2.42 0.618 2.79 0.400 100 0.0195 0.00591 2.50 0.756 3.39 0.499 300 0.0209 0.00713 2.68 0.913 4.09 0.607 1.
  可迁移模板：The results show some conclusions: Convective coefficient (W/(m2 K)) Unit cell (single p–n couple) METHOD.
#### 贡献句
- 原句/结构：For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide
  可迁移模板：For the METHOD structure proposed in this work, if a convection heat transfer with coefficients of X, X, Xand METHOD/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is X, X, Xand METHOD, respectively, and this provide
#### 限制/边界句
- 原句/结构：Article history: Received 21 November 2017 Received in revised form 15 January 2018 Accepted 17 March 2018 Available online 21 March 2018 The traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency.
  可迁移模板：Article history: Received XNovember XReceived in revised form XJanuary XAccepted XMarch XAvailable online XMarch XThe traditional thermal protection system (METHOD) of Y is usually designed for thermal protection purpose only with low efficiency.
- 原句/结构：For a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than 1800 K [1–3].
  可迁移模板：For a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than METHOD [X–X].
- 原句/结构：The traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency.
  可迁移模板：The traditional thermal protection system (METHOD) of Y is usually designed for thermal protection purpose only with low efficiency.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
