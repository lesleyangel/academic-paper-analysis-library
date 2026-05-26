# A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles

## 0. 读取说明

本拆解基于 `801/文本/txt/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.txt`。文本抽取能确认摘要、章节、材料、主要方程、表格数值和结论；但 Fig. 2-Fig. 16 中热流分布、温度场、位移场、电势场和输出功率曲线的空间细节需要 PDF 图像复核。本文是 2021 年 MTPS 论文的前序工作，拆解时特别关注它如何提出初代 TE-material TPS 概念。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The vehicle, trajectory and aerodynamic heat, 3 The multi-functional TPS structure, 4 Numerical model, 5 Results and discussions, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.md`。

中文译文：

> 文章历史记录： 2017年11月21日收到 2018年1月15日以修订形式收到 2018年3月17日接受 2018年3月21日在线提供
>
> 传统的高超声速飞行器热防护系统（TPS）通常仅用于热防护目的，效率较低。本文提出了一种基于热电材料的多功能TPS结构概念，并基于特定车辆和典型轨迹开发了其机械热电性能的评估方法。结构中的热电模块可以将一定量的空气动力热转化为电能。该模块由基于固相反​​应方法制备的n型Sr0.9La0.1TiO3化合物和广泛使用的p型Ca3Co4O9组成。针对具有典型弹道曲线的特定高超声速飞行器，通过工程化算法计算气动热，基于晶胞模型分析结构的非定常机械热电特性，最终评估热电转换效率。结果表明，多功能TPS结构在高超声速飞行器上具有显着的应用潜力。 © 2018 Elsevier Masson SAS。版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle. In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. 2.
- 已有研究不足/GAP：需结合 Introduction 的文献转折句复核。
- 本文解决方式：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory. The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9. For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
- 学术或工程增量：For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 The vehicle, trajectory and aerodynamic heat（对象/模块/过渡章节）
  - L3 p.2: 2.1 The vehicle and trajectory（对象/模块/过渡章节）
  - L3 p.3: 2.2 Aerodynamic heat（对象/模块/过渡章节）
- L2 p.3: 3 The multi-functional TPS structure（对象/模块/过渡章节）
  - L3 p.4: 3.1 The choosing of p-type material（对象/模块/过渡章节）
  - L3 p.4: 3.2 Fabrication of n-type material and its TE properties（对象/模块/过渡章节）
  - L3 p.5: 3.3 Physical properties of other materials（对象/模块/过渡章节）
- L2 p.5: 4 Numerical model（方法/模型/算法）
  - L3 p.5: 4.1 Governing and constitutive equations（对象/模块/过渡章节）
  - L3 p.6: 4.2 The unit cell model and its mesh（方法/模型/算法）
  - L3 p.6: 4.3 The boundary and initial conditions（对象/模块/过渡章节）
  - L3 p.7: 4.4 Interfaces between different materials（对象/模块/过渡章节）
- L2 p.8: 5 Results and discussions（结果/验证/讨论）
  - L3 p.8: 5.1 Thermo-mechanical performance（对象/模块/过渡章节）
  - L3 p.10: 5.2 Thermoelectric performance（对象/模块/过渡章节）
  - L3 p.11: 5.3 Thermoelectric conversion efﬁciency（对象/模块/过渡章节）
- L2 p.11: Conclusions（结论/贡献回收）
- L2 p.12: Conﬂict of interest statement（对象/模块/过渡章节）
- L2 p.12: Acknowledgements（尾部材料）
- L2 p.12: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The vehicle, trajectory and aerodynamic heat | 2 | 2 | 对象/模块/过渡章节 |
| 2.1 The vehicle and trajectory | 2 | 3 | 对象/模块/过渡章节 |
| 2.2 Aerodynamic heat | 3 | 3 | 对象/模块/过渡章节 |
| 3 The multi-functional TPS structure | 3 | 2 | 对象/模块/过渡章节 |
| 3.1 The choosing of p-type material | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Fabrication of n-type material and its TE properties | 4 | 3 | 对象/模块/过渡章节 |
| 3.3 Physical properties of other materials | 5 | 3 | 对象/模块/过渡章节 |
| 4 Numerical model | 5 | 2 | 方法/模型/算法 |
| 4.1 Governing and constitutive equations | 5 | 3 | 对象/模块/过渡章节 |
| 4.2 The unit cell model and its mesh | 6 | 3 | 方法/模型/算法 |
| 4.3 The boundary and initial conditions | 6 | 3 | 对象/模块/过渡章节 |
| 4.4 Interfaces between different materials | 7 | 3 | 对象/模块/过渡章节 |
| 5 Results and discussions | 8 | 2 | 结果/验证/讨论 |
| 5.1 Thermo-mechanical performance | 8 | 3 | 对象/模块/过渡章节 |
| 5.2 Thermoelectric performance | 10 | 3 | 对象/模块/过渡章节 |
| 5.3 Thermoelectric conversion efﬁciency | 11 | 3 | 对象/模块/过渡章节 |
| Conclusions | 11 | 2 | 结论/贡献回收 |
| Conﬂict of interest statement | 12 | 2 | 对象/模块/过渡章节 |
| Acknowledgements | 12 | 2 | 尾部材料 |
| References | 12 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 先从热环境讲必要性，再比较热流预测方法，接着介绍 TPS 材料与热电材料，最后落到“本文开发快速评估方法”。段落推进是“工程需求 -> 方法选择 -> 材料机会 -> 本文方案”。

结构和模型段落的节奏偏说明书式：每段围绕一个对象（车辆、热流、材料、边界、界面）展开。结果段落先描述图，再给数值，再解释趋势。例如功率结果段先说明最大功率计算方式，再用不同对流系数曲线说明趋势，最后外推到真实面积。

可学习之处是将“热流输入”单独成节，这让后续所有性能结果都有明确上游来源。热管理论文若缺少这一层，容易显得只是理想边界下的结构演示。

## 13. 文笔画像与语言习惯

整体语气是“概念提出 + 潜力证明”，常用 `proposed`, `developed`, `evaluated`, `indicate`, `potential`。相比 2021 年论文，这篇更谨慎，常用 “has potentials” 而非“can replace power supply”。

时态：引言综述用现在时和过去时；实验/制备用过去时；结果图表用现在时。被动语态较多，用于材料制备、模型建立和边界条件；主动语态主要出现在 `In this work` 开头的贡献句。

高频词围绕 `temperature`, `material`, `heat`, `thermoelectric`, `TPS`, `coefficient`, `power`, `efficiency`。形容词偏工程性能：`efficient`, `reliable`, `high-temperature`, `multi-functional`, `typical`。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：30039
- 高频词：heat(51)；structure(38)；temperature(35)；material(31)；aerodynamic(30)；tps(30)；work(30)；vehicle(24)；thermal(23)；boundary(22)；surface(21)；method(19)；layer(19)；materials(19)；model(17)；performance(15)；should(15)；will(15)；tcr(15)；conditions(14)
- 高频名词化/学术名词：structure(38)；temperature(35)；performance(15)；condition(9)；conductivity(9)；calculation(9)；evaluation(7)；influence(6)；expansion(6)；protection(5)；insulation(5)；convection(5)；electricity(4)；reaction(4)；conversion(4)
- 高频学术动词：developed(11)；analyzed(7)；evaluated(5)；provide(3)；provided(2)；predict(1)；develop(1)；indicate(1)；analyze(1)；evaluate(1)；indicated(1)；validate(1)
- 高频形容词：material(31)；aerodynamic(30)；thermal(23)；boundary(22)；coefficient(14)；thermoelectric(9)；typical(9)；convective(8)；specific(7)；numerical(7)；different(7)；electric(7)；mechanical-thermoelectric(6)；hypersonic(5)；additional(5)
- 高频副词：widely(3)；mainly(2)；supply(2)；finally(2)；carefully(2)；closely(2)；directly(2)；separately(2)；usually(1)；especially(1)；partly(1)；fly(1)；relatively(1)；firstly(1)；fully(1)
- 高频二词短语：aerodynamic heat(26)；tps structure(13)；unit cell(13)；heat flux(12)；cell model(9)；boundary conditions(8)；thermal conductivity(7)；boundary layer(7)；top surface(6)；bottom surface(6)；thermal protection(5)；typical trajectory(5)
- 高频三词短语：unit cell model(9)；aerodynamic heat flux(5)；amount aerodynamic heat(4)；vehicle typical trajectory(4)；convection heat transfer(4)；temperature top surface(4)；multifunctional tps structure(3)；fabricated solid state(3)；solid state reaction(3)；state reaction method(3)；aerodynamic heat calculated(3)；tps structure work(3)
- 被动语态估计：110；`we + 动作动词` 主动句估计：0
- 一般现在时线索：186；一般过去时线索：235；现在完成时线索：0；情态动词线索：53

分章节正文词频：

- 1 Introduction: heat(14)；tps(14)；material(14)；aerodynamic(11)；vehicle(9)；developed(9)；method(8)；structure(8)
- 2 The vehicle, trajectory and aerodynamic heat: heat(16)；aerodynamic(13)；vehicle(11)；work(8)；calculation(8)；layer(8)；flow(8)；field(7)
- 3 The multi-functional TPS structure: material(12)；heat(8)；materials(8)；thermal(7)；structure(6)；coefficient(6)；seebeck(5)；high(5)
- 4 Numerical model: boundary(13)；tcr(13)；work(12)；model(12)；structure(11)；conditions(10)；heat(9)；unit(9)
- 5 Results and discussions: temperature(9)；surface(9)；bottom(8)；top(6)；structure(5)；convective(5)；time(4)；coefficient(3)
- Conclusions: structure(4)；work(3)；heat(3)；unit(3)；cell(3)；material(2)；tps(2)；approach(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle.
  可迁移模板：Thus, a reliable and efficient thermal protection system (METHOD) is essential to ensure the safety of the vehicle.
- 原句：At present, the numerical method still has some challenges, such as the high requirement * Corresponding author.
  可迁移模板：At present, the numerical method still has some challenges, such as the high requirement * Corresponding author.
- 原句：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. 2.
  可迁移模板：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. X.
#### Gap/转折句
- 原句：However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
  可迁移模板：However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
- 原句：For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [23] developed an integrated TE module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [24] developed a multi-stage TE module considering the suitable temperature of TE material, and analyzed its thermal protection performance.
  可迁移模板：For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [X] developed an integrated METHOD module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [X] developed a multi-stage METHOD module considering the suitable temperature of METHOD material, and analyzed its thermal protection performance.
- 原句：The very limited research activities motivate further studies.
  可迁移模板：The very limited research activities motivate further studies.
#### 方法提出句
- 原句：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory.
  可迁移模板：In this paper, a thermoelectric material based multifunctional METHOD structure concept is proposed and the evaluation approach of its mechanicalthermoelectric performance is developed based on a specific vehicle and a typical trajectory.
- 原句：The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
  可迁移模板：The module consists of n-type Sr0.XLa0.XTiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
- 原句：For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
  可迁移模板：For a specific TARGET SYSTEM with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
- 原句：There are two main methods to predict the aerodynamic heat, the engineering-based method and the numerical method.
  可迁移模板：There are two main methods to predict the aerodynamic heat, the engineering-based method and the numerical method.
- 原句：During the last decades, numerous relevant studies have been carried on to develop appropriate numerical method (mainly CFD) for the aerodynamic heat prediction of flow fields/vehicle with different configurations [4–8].
  可迁移模板：During the last decades, numerous relevant studies have been carried on to develop appropriate numerical method (mainly METHOD) for the aerodynamic heat prediction of flow fields/vehicle with different configurations [X–X].
#### 结果呈现句
- 原句：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. 2.
  可迁移模板：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results. X.
#### 贡献/增量句
- 原句：On the other hand, for a TPS based on non-ablative material [17–19], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
  可迁移模板：On the other hand, for a METHOD based on non-ablative material [X–X], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
- 原句：For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide
  可迁移模板：For the METHOD structure proposed in this work, if a convection heat transfer with coefficients of X, X, Xand METHOD/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is X, X, Xand METHOD, respectively, and this provide
#### 限制/边界句
- 原句：For a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than 1800 K [1–3].
  可迁移模板：For a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than METHOD [X–X].
- 原句：The traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency.
  可迁移模板：The traditional thermal protection system (METHOD) of TARGET SYSTEM is usually designed for thermal protection purpose only with low efficiency.
- 原句：For the insulation layer, the basic requirement should be the low weight and low thermal conductivity [11,12].
  可迁移模板：For the insulation layer, the basic requirement should be the low weight and low thermal conductivity [X,X].
- 原句：On the other hand, for a TPS based on non-ablative material [17–19], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
  可迁移模板：On the other hand, for a METHOD based on non-ablative material [X–X], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
- 原句：For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [23] developed an integrated TE module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [24] developed a multi-stage TE module considering the suitable temperature of TE material, and analyzed its thermal protection performance.
  可迁移模板：For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [X] developed an integrated METHOD module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [X] developed a multi-stage METHOD module considering the suitable temperature of METHOD material, and analyzed its thermal protection performance.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用分布集中在 Introduction，功能是快速搭建应用背景。作者先引用气动热和高温边界问题，再引用 CFD/工程算法，再引用 TPS 材料和热电材料。文献使用姿态以“补充”和“转折”为主：CFD 精度高但低效，工程算法低精度但高效；传统 TPS 可靠但不复用热；热电材料有潜力但需要结构集成。

引用没有形成很细的热电材料机制综述，因为本文目标不是材料机理。但这也带来风险：对 TE 材料性能、稳定性、氧化和热循环文献讨论略薄。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：61
- Introduction 引文簇数量估计：10
- References 条目数：41
- 可识别年份条目数：44
- 2021 年及以后文献数：0
- 2010 年前经典文献数：14
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Aerospace Science and Technology(2)
- 引文簇样例：[9], [10], [4], [11,12], [11], [20], [21], [22], [23], [28], [24], [29]

带引文的 gap/转折句样例：

- For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [23] developed an integrated TE module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [24] developed a multi-stage TE module considering the suitable temperature of TE material, and analyzed its thermal protection performance.

References 解析样例（前 8 条）：

- [1] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re-usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [2] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [3] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [4] D. Knight, H. Yan, A.G. Panaras, A. Zheltovodov, Advances in CFD prediction of shock wave turbulent boundary layer interactions, Prog. Aerosp. Sci. 39 (2) (2003) 121–184.
- [5] D. Knight, J. Longo, D. Drikakis, D. Gaitonde, A. Lani, I. Nompelis, B. Reimann, L. Walpot, Assessment of CFD capability for prediction of hypersonic shock interactions, Prog. Aerosp. Sci. 48 (Supplement C) (2012) 8–26.
- [6] Y. Kerboua, A.A. Lakis, Numerical model to analyze the aerodynamic behavior of a combined conical–cylindrical shell, Aerosp. Sci. Technol. 58 (Supplement C) (2016) 601–617.
- [7] P. Panagiotou, P. Kaparos, C. Salpingidou, K. Yakinthos, Aerodynamic design of a MALE UAV, Aerosp. Sci. Technol. 50 (Supplement C) (2016) 127–138.
- [8] P.D. Bravo-Mosquera, L. Botero-Bolivar, D. Acevedo-Giraldo, H.D. Cerón-Muñoz, Aerodynamic design analysis of a UAV for superficial research of volcanic environments, Aerosp. Sci. Technol. 70 (Supplement C) (2017) 600–614.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

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
