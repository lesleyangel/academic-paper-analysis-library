# Microstructure and thermoelectric properties of non-equimolar high-entropy [Ca(1-x)/3Sr(1-x)/3Ba(1-x)/3Lax]TiO3 perovskite ceramics

## 0. 读取说明

本拆解基于 `801/文本/txt/Microstructure-and-thermoelectric-properties-of-non-equim_2024_Journal-of-Al.txt` 的全文抽取。文本中双栏排版导致部分段落交错，但材料制备、公式、图题、表格和结论可辨。XRD、SEM、TEM、Raman、XPS 图像的细节判读需结合 PDF 图像复核；本文仅依据文本描述分析。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Material and methods, 3 Result and discussion, 4 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Microstructure and thermoelectric properties of non-equimolar high-entropy [Ca(1-x)/3Sr(1-x)/3Ba(1-x)/3Lax]TiO3 perovskite ceramics。
- 作者：Ziyao Wei、Zhihao Lou、Shiyuan Chen、Jianjun Gou、Jie Xu、Chunlin Gong、Feng Gao。
- 期刊：Journal of Alloys and Compounds，1006，2024，176328。
- 领域：高熵陶瓷、SrTiO3 基热电材料、构型熵工程、微结构调控。
- 论文类型：材料制备 + 多尺度表征 + 热电性能机制解释。
- 研究对象：非等摩尔 A 位高熵 [Ca/Sr/Ba/La]TiO3 钙钛矿陶瓷，x=0.10-0.40。
- 主要方法：固相反应 + SPS + Ar+C 还原退火；XRD/Rietveld、SEM、TEM/EDX、Raman、XPS、Hall、热电性能测试。
- 核心指标：构型熵、容忍因子、晶粒尺寸、氧空位、晶格畸变、电导率、Seebeck 系数、热导率、PF、ZT。

## 2. 摘要与核心信息提取

一句话主张：SrTiO3 基热电陶瓷中，热电性能并不随构型熵单调提升；非等摩尔高熵设计能通过晶粒细化、晶格畸变、氧空位和多尺度缺陷共同优化电/热输运，其中 x=0.19、Delta SConf=11.483 J/mol/K 的样品获得最高 ZT=0.20。

摘要采取“领域热词 + 关系不清 + 实验系列 + 机制链 + 最优值”的结构。它先承认 entropy engineering 是优化 SrTiO3 热电性能的重要手段，再指出 configurational entropy 与 thermoelectric properties 的关系不清；随后给出样品体系和制备方法；结果部分把高熵效应连到 microstructure、lattice distortions、oxygen vacancies；最后用最高 ZT 和“theoretical and experimental bases”收束贡献。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Microstructure-and-thermoelectric-properties-of-non-equim_2024_Journal-of-Al.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Microstructure-and-thermoelectric-properties-of-non-equim_2024_Journal-of-Al.md`。

中文译文：

> 熵工程已成为优化SrTiO3基热电材料性能的重要手段。然而，构型熵与热电性质之间的关系目前尚不清楚。本工作中，非等摩尔高熵热电陶瓷[Ca(1-x)/3Sr(1-x)/3Ba(1-x)/
>
> 通过放电等离子烧结制备3Lax]TiO3 (0.10 ≤x ≤0.40)。并研究了成分和构型熵对材料微观结构和热电性能的影响。研究表明，高熵效应深刻改变了材料的微观结构。晶粒尺寸随着构型熵的增加而减小，多种阳离子的相互作用导致晶格畸变，烧结和退火过程会导致氧空位的产生，从而显着影响热电性能。当镧含量为0.19时获得最高的ZT（0.20）（ΔSConf=11.483 J/mol/K）。该工作为利用高熵设计优化材料的热电性能提供了理论和实验基础。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自热电材料中的经典矛盾：高 ZT 需要高 Seebeck、高电导、低热导，但这些参数相互耦合、相互制约。SrTiO3 熔点高、有效质量高、结构稳定，是有潜力的氧化物热电材料，但本征热导率高限制应用。

高熵设计提供降低热导的新工具，但当前研究偏重等摩尔高熵成分。作者抓住一个更细的 gap：性能与构型熵不是线性关系，非等摩尔或中熵材料可能更优。因此，本文不是“再做一个高熵 SrTiO3”，而是系统扫 La 含量和构型熵，找“适宜熵”而非“最高熵”。

这个选题适合 JALCOM，因为它同时有成分设计、制备工艺、结构表征和性能数据，材料证据链比较完整。

## 4. 领域位置与文献版图

文献版图先从热电能源回收背景入手，然后引出 SrTiO3 优缺点，再列举提高 SrTiO3 性能的传统方法：离子掺杂、第二相复合、缺陷工程。随后转向高熵设计，引用 Banerjee、Lou 等高熵 SrTiO3/钙钛矿陶瓷研究说明高熵可降低热导。

关键位置在于对等摩尔设计的修正。作者引用 Bi、Zhu 等中熵/非等摩尔体系，说明高熵最大化不一定最优。本文站在这一分支之后，用 [Ca/Sr/Ba/La]TiO3 A 位多阳离子体系实验证明“moderate configuration entropy”可获得更优热电性能。

## 5. Gap 制造机制

Gap 的表述是：entropy engineering 已被用于优化 SrTiO3，但 configurational entropy 与 thermoelectric properties 的关系目前 unclear；现有设计多集中在等摩尔高熵成分，忽视非等摩尔构型熵的最优区间。

作者制造 gap 的技巧是把“高熵”从一个单向正面概念拆开：高熵可增强声子散射，但也可能因孔隙、载流子散射、晶界密度、晶格畸变和氧空位改变电输运，从而让 ZT 出现非单调峰值。这个 gap 后文用 L10-L40 六组样品和 Fig. 11 的抛物线关系回应。

## 6. 创新性判断

作者声明的创新是制备非等摩尔高熵 CSBL 陶瓷并系统研究构型熵变化对微结构和热电性能的影响。

真实创新是“成分路径 + 机制整合”。单个表征手段不新，SPS/还原退火也常见；新意在于把 La 含量、构型熵、晶粒尺寸、Raman 畸变、XPS 氧空位、Hall 载流子、热导和 ZT 连接成一条非单调优化链。

创新强度中等。最高 ZT=0.20 对 SrTiO3 基高熵陶瓷有一定竞争力，但不是颠覆性数值；贡献更偏“证明盲目追求最大构型熵不如寻找最适构型熵”。

## 7. 论证链条复原

1. 热电材料需要在电输运和热输运之间平衡，SrTiO3 本征热导高。
2. 高熵设计可通过多组元无序增强声子散射，但构型熵与性能关系不清。
3. 构造 [Ca(1-x)/3Sr(1-x)/3Ba(1-x)/3Lax]TiO3 系列，调节 x 和 Delta SConf。
4. 用容忍因子 t 证明成分可形成稳定钙钛矿结构，再用 XRD/Rietveld 验证单相立方钙钛矿。
5. SEM/TEM/EDX/Raman/XPS 证明高熵设计导致晶粒细化、元素均匀分布、晶格畸变、缺陷和氧空位。
6. 电输运表明 La/氧空位提高载流子浓度，但过高无序、孔隙和晶界会降低迁移率/电导。
7. 热输运表明多尺度缺陷和晶格畸变增强声子散射，L19 具有低热导。
8. 综合 PF 和 kappa 后，ZT 随构型熵呈非单调，L19 达最高 ZT=0.20。
9. 结论回到 gap：entropy engineering 不是追求最高熵，而是寻找最合适的构型熵。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Entropy engineering has emerged as an important means of optimizing the properties of SrTiO3-based thermo electric materials. Nevertheless, the interconnectivity and constraints of each thermoelectric parameter render the achievement of the optimal ZT value a challenging endeavor. Journal of Alloys and Compounds 1006 (2024) 176328 Contents lists available at ScienceDirect Journal of Alloys and Compounds journal homepage: www.elsevier.com/locate/jalcom Entropy engineering has emerged as an important means of optimizing the properties of SrTiO3-based thermo electric materials.
- 已有研究不足/GAP：However, the relationship between configurational entropy and thermoelectric properties is currently unclear. However, its high κ limits its application in the thermoelectric * Corresponding author. However, the relationship between configurational entropy and thermoelectric properties is currently unclear.
- 本文解决方式：As human society and civilization continue to develop, the impact of the energy shortage is becoming increasingly significant. The use of fossil fuels, nuclear decay and other traditional methods of obtaining energy results in a significant loss of energy in the form of heat, which in turn exacerbates the energy crisis [1].
- 学术或工程增量：It is revealed that high entropy effect profoundly modified the microstructure of the material. This work provides theoretical and experimental bases for optimizing the thermoelectric properties of the materials by using high entropy design. Nevertheless, the interconnectivity and constraints of each thermoelectric parameter render the achievement of the optimal ZT value a challenging endeavor.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

成分设计采用 A 位 Ca、Sr、Ba、La 混合，x=0.10、0.13、0.19、0.22、0.25、0.40，对应 L10-L40。用 Goldschmidt tolerance factor t=(RA+RO)/sqrt(2)(RB+RO) 预判钙钛矿稳定性；用 Sconf=-R sum xi ln xi 计算构型熵。

制备流程是常规固相 + SPS + 还原退火：原料称量、酒精球磨 12h、1200 C 煅烧 4h、再球磨、1250 C 真空 SPS、Ar+C 1400 C 退火。还原退火既提高导电性，也引入氧空位和孔隙，是性能机制的关键。

表征链非常完整：XRD/Rietveld 判相和晶格常数；SEM 看晶粒和孔隙；TEM/HRTEM/SAED/IFFT/EDX 看 L19 晶体结构、位错和元素均匀性；Raman 看 Ti-O-Ti/[TiO6] 畸变；XPS O 1s 分峰估算氧空位；Hall 测 n 和迁移率；热电测试测 sigma、S、kappa、PF、ZT。

理论解释使用 SPB 模型解释 Seebeck 与载流子浓度/有效质量关系；Arrhenius 方程解释小极化子导电激活能；Wiedemann-Franz 和 Debye relaxation time 解释电子/晶格热导分解和声子散射。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| CSBL 系列可形成稳定单相立方钙钛矿 | 3.1 | Table 1 t 接近 1；Fig. 1 XRD/Rietveld，Rwp<10%；Table 2 晶格常数 | 强 | XRD 小杂相需 PDF 图像复核 |
| 构型熵升高总体细化晶粒并增加边界密度 | 3.1 | SEM 前后退火，平均晶粒从 0.25-0.39 um 到 1.63-4.35 um，随构型熵有减小趋势 | 中强 | 粒径统计在补充图，需复核 |
| L19 具有明显晶格畸变和微结构无序 | 3.1 | TEM/HRTEM/SAED/IFFT，Raman 中 TO4 shift 最大 | 强 | 位错和超晶格斑点需 PDF 图像复核 |
| 还原退火和 La 掺杂诱导高浓度氧空位 | 3.1 | XPS O 1s 分峰，Vo/[O]total 从 L10 25.4% 到 L40 36.1% | 强 | XPS 拟合参数需复核 |
| 电导先升后降，过高 x/无序会降低迁移率 | 3.2 | Fig. 8，Hall 表：n 增大一个数量级，muH 下降一个数量级；L22 673 K sigma=32146.9 S/m | 强 | 温区内机制转换需更多温度点复核 |
| L19 获得低热导和较高 PF 的平衡 | 3.2 | kappa_total 1073 K 为 2.13 W/m/K，PF 444.43 uW/m/K2 | 强 | PF 与最高 PF L22 的关系需注意 |
| ZT 与构型熵非单调，L19 最高 | 3.2/结论 | Fig. 11，L19 ZT=0.20 at 1073 K，比等摩尔高熵陶瓷高 19% | 强 | 对比文献条件差异需谨慎 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Eq. 1 | 容忍因子公式 | 成分可形成钙钛矿 | t 接近 1，随 x 增大略降 | 文本可确认 |
| Eq. 2/Table 1 | 构型熵计算和样品设计 | 非等摩尔熵调控 | L25 熵最高，L19 为适中熵 | 文本可确认 |
| Fig. 1/Table 2 | 判相与晶格常数 | 单相钙钛矿与晶格收缩 | 主峰向大角度偏移，a 从 3.9225 到 3.9166 A | 需要 PDF 图像复核 |
| Fig. 2 | 晶粒和孔隙 | 高熵/退火改变微结构 | 退火晶粒长大，L40 孔隙更明显 | 需要 PDF 图像复核 |
| Fig. 3-4 | L19 微结构与元素分布 | 元素均匀、缺陷存在 | edge dislocations、EDX 均匀 | 需要 PDF 图像复核 |
| Fig. 5/Table 3 | Raman 畸变证据 | [TiO6] 八面体畸变 | L19 TO4 shift 最大 | 需要 PDF 图像复核 |
| Fig. 6-7/Table 4 | XPS 氧空位 | 氧空位影响电输运 | Vo 含量随 x 增加 | 需要 PDF 图像复核 |
| Fig. 8/Table 5 | 电输运 | n、muH、sigma、S、PF 平衡 | L22 PF 高，L40 电性能差 | 文本可确认，曲线需复核 |
| Eq. 4-10/Fig. 9-10 | SPB、小极化子、热导分解和声子散射 | 热/电输运机制 | 多尺度缺陷散射宽频声子 | 文本可确认，示意图需复核 |
| Fig. 11 | ZT 和构型熵关系 | 适中熵最优 | L19 ZT=0.20，非单调峰值 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

章节为 Introduction -> Material and methods -> Result and discussion -> Conclusion。Results 内部实际分为 3.1 Microstructure 和 3.2 Electrical and thermal transport properties。

Introduction 从能源危机和热电材料大背景切入，再缩小到 SrTiO3、高熵设计、非等摩尔 gap。Methods 先讲样品制备，再列测试手段。Results 采用“结构先行、性能后置”的材料论文经典结构：先证明材料做成了、结构有什么变化，再解释这些结构变化如何影响电输运和热输运，最后用 ZT 整合。

标题偏简洁，3.1 和 3.2 分别对应“微结构证据”和“性能证据”，没有过多机制标题；机制主要在段落内部展开。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Material and methods（方法/模型/算法）
- L2 p.2: 3 Result and discussion（结果/验证/讨论）
  - L3 p.2: 3.1 Microstructure of CSBL ceramics（对象/模块/过渡章节）
  - L3 p.5: 3.2 Electrical and thermal transport properties of CSBL ceramics（对象/模块/过渡章节）
- L2 p.9: 4 Conclusion（结论/贡献回收）
- L2 p.10: CRediT authorship contribution statement（尾部材料）
- L2 p.11: Declaration of Competing Interest（尾部材料）
- L2 p.11: Data Availability（尾部材料）
- L2 p.11: Acknowledgements（尾部材料）
- L2 p.11: Appendix A Supporting information（尾部材料）
- L2 p.11: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Material and methods | 2 | 2 | 方法/模型/算法 |
| 3 Result and discussion | 2 | 2 | 结果/验证/讨论 |
| 3.1 Microstructure of CSBL ceramics | 2 | 3 | 对象/模块/过渡章节 |
| 3.2 Electrical and thermal transport properties of CSBL ceramics | 5 | 3 | 对象/模块/过渡章节 |
| 4 Conclusion | 9 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 10 | 2 | 尾部材料 |
| Declaration of Competing Interest | 11 | 2 | 尾部材料 |
| Data Availability | 11 | 2 | 尾部材料 |
| Acknowledgements | 11 | 2 | 尾部材料 |
| Appendix A Supporting information | 11 | 2 | 尾部材料 |
| References | 11 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

结果段落节奏典型：图表观察 -> 结构/物理解释 -> 与下一性能指标连接。XRD 段证明单相；SEM 段讨论晶粒和孔隙；TEM/Raman/XPS 段逐步把“高熵导致无序/缺陷/氧空位”坐实；电热输运段再把这些结构因素转译为 sigma、S、kappa、ZT。

文中多次使用“并非单因素决定”的段落策略。例如 Raman 段指出构型熵不是晶格畸变的唯一决定因素，还要考虑电荷和缺陷；ZT 段指出高熵是有效策略，但不代表更高构型熵必然更好。

## 13. 文笔画像与语言习惯

文笔是材料表征论文的“证据堆叠型”：大量使用 “Fig. X shows/illustrates/presents”、“It can be observed”、“indicating that”。claim 强度在结构判定上较强，在机制解释上会用 “mainly due to”、“related to”、“suggests” 控制。

高频名词：configurational entropy、microstructure、grain size、lattice distortion、oxygen vacancies、phonon scattering、thermal conductivity、electrical conductivity、Seebeck coefficient、power factor、ZT。

形容词偏材料属性：stable、single-phase、cubic、high-density、dramatic、uniform、excellent、ultra-low、glassy、moderate。时态上 Methods 用过去时，规律性机制用现在时，结果读图用现在时。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：22253
- 高频词：ceramics(39)；high(32)；entropy(29)；thermoelectric(24)；energy(15)；lattice(14)；perovskite(13)；properties(13)；grain(13)；annealing(13)；due(13)；materials(12)；conductivity(12)；material(12)；scattering(12)；structure(11)；samples(11)；temperature(10)；thermal(10)；defects(10)
- 高频名词化/学术名词：ceramics(39)；conductivity(12)；structure(11)；temperature(10)；concentration(10)；distortion(9)；activation(8)；microstructure(7)；density(7)；composition(6)；reduction(6)；configuration(6)；presence(4)；ramics(4)；diffusion(4)
- 高频学术动词：achieved(3)；analyze(2)；compared(2)；provided(2)；develop(1)；revealed(1)；demonstrated(1)；analyzed(1)；evaluated(1)；presented(1)；predicted(1)；indicate(1)；indicated(1)；optimize(1)
- 高频形容词：thermoelectric(24)；material(12)；thermal(10)；configurational(9)；total(9)；constant(8)；ceramic(6)；atomic(6)；cubic(5)；component(5)；thermodynamic(4)；structural(4)；chemical(4)；coefficient(3)；stable(3)
- 高频副词：mainly(4)；extremely(3)；finally(2)；dramatically(2)；generally(2)；increasingly(1)；typically(1)；usually(1)；currently(1)；profoundly(1)；significantly(1)；successfully(1)；largely(1)；thoroughly(1)；firstly(1)
- 高频二词短语：high entropy(11)；thermoelectric properties(10)；configurational entropy(9)；perovskite structure(8)；lattice distortion(8)；grain size(6)；configuration entropy(6)；activation energy(6)；thermal conductivity(5)；cubic perovskite(5)；thermodynamic temperature(4)；lax tio(4)
- 高频三词短语：cubic perovskite structure(4)；thermoelectric properties materials(4)；high entropy design(4)；work non-equimolar high-entropy(3)；spark plasma sintering(3)；average grain size(3)；carrier effective mass(2)；relationship configurational entropy(2)；ceramics lax tio(2)；microstructure thermoelectric properties(2)；creation oxygen vacancies(2)；single-phase high entropy(2)
- 被动语态估计：48；`we + 动作动词` 主动句估计：0
- 一般现在时线索：86；一般过去时线索：143；现在完成时线索：3；情态动词线索：9

分章节正文词频：

- 1 Introduction: thermoelectric(21)；high(14)；entropy(14)；materials(10)；properties(10)；sintering(7)；energy(6)；ceramics(6)
- 2 Material and methods: thermal(4)；hours(3)；ceramics(3)；conductivity(3)；total(3)；tio(2)；powder(2)；samples(2)
- 3 Result and discussion: ceramics(26)；high(15)；lattice(13)；entropy(11)；grain(11)；perovskite(10)；due(10)；annealing(10)
- 4 Conclusion: ceramics(4)；entropy(4)；conductivity(3)；high(3)；high-entropy(2)；tio(2)；thermoelectric(2)；ceramic(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：X has emerged as an important means of optimizing...
- Gap 句式：However, the relationship between X and Y is currently unclear.
- 方法句式：The effects of composition and configurational entropy on X were investigated.
- 结构结果句：The diffraction peaks are in good accordance with...
- 机制句式：This is mainly due to... / This strongly indicates that...
- 限定句式：It does not necessarily mean that higher X leads to superior Y.
- 结论句式：It is not necessary to blindly pursue high configuration entropy, but rather to find the most suitable configuration entropy.

可复用术语：entropy engineering、non-equimolar high-entropy ceramics、configuration entropy、lattice distortion effects、oxygen vacancy、small polaron conduction、broadband scattering of phonons、moderate level of entropy。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Entropy engineering has emerged as an important means of optimizing the properties of SrTiO3-based thermo electric materials.
  可迁移模板：Entropy engineering has emerged as an important means of optimizing the properties of SrTiO3-based thermo electric materials.
#### Gap/转折句
- 原句：However, the relationship between configurational entropy and thermoelectric properties is currently unclear.
  可迁移模板：However, the relationship between configurational entropy and thermoelectric properties is currently unclear.
- 原句：However, its high κ limits its application in the thermoelectric * Corresponding author.
  可迁移模板：However, its high κ limits its application in the thermoelectric * Corresponding author.
- 原句：However, the relationship between configurational entropy and thermoelectric properties is currently unclear.
  可迁移模板：However, the relationship between configurational entropy and thermoelectric properties is currently unclear.
- 原句：However, recent studies have demonstrated that the thermoelectric properties of materials do not exhibit a straightforward linear relationship with configurational entropy.
  可迁移模板：However, recent studies have demonstrated that the thermoelectric properties of materials do not exhibit a straightforward linear relationship with configurational entropy.
#### 方法提出句
- 原句：As human society and civilization continue to develop, the impact of the energy shortage is becoming increasingly significant.
  可迁移模板：As human society and civilization continue to develop, the impact of the energy shortage is becoming increasingly significant.
- 原句：The use of fossil fuels, nuclear decay and other traditional methods of obtaining energy results in a significant loss of energy in the form of heat, which in turn exacerbates the energy crisis [1].
  可迁移模板：The use of fossil fuels, nuclear decay and other traditional methods of obtaining energy results in a significant loss of energy in the form of heat, which in turn exacerbates the energy crisis [X].
- 原句：The common methods to enhance the thermoelectric properties of SrTiO3-based materials mainly include ion doping [4,5], second-phase composite [6–9] and defect engineering [10], etc.
  可迁移模板：The common methods to enhance the thermoelectric properties of SrTiO3-based materials mainly include ion doping [X,X], second-phase composite [X–X] and defect engineering [X], etc.
- 原句：The current approach to entropy engineering design for thermo electric ceramics is largely focused on the high-entropy equimolar ratio composition.
  可迁移模板：The current approach to entropy engineering design for thermo electric ceramics is largely focused on the high-entropy equimolar ratio composition.
- 原句：Zhu et al. [14]. used the conventional solid phase method to prepare (Ca0.33Sr0.33Ba0.33)(Ti0.5-xZr0.5-xNbx)O3 in a reducing atmosphere and obtained an ultra-low glassy κ of 1.6–1.9 W/m/K from room temperature to 873 K, which is among the lowest reported κ for perovskite oxides.
  可迁移模板：Zhu et al. [X]. used the conventional solid phase method to prepare (Ca0.XSr0.XBa0.X)(Ti0.X-xZr0.X-xNbx)O3 in a reducing atmosphere and obtained an ultra-low glassy κ of X–METHOD/m/K from room temperature to METHOD, which is among the lowest reported κ for perovskite oxides.
#### 结果呈现句
- 原句：The use of fossil fuels, nuclear decay and other traditional methods of obtaining energy results in a significant loss of energy in the form of heat, which in turn exacerbates the energy crisis [1].
  可迁移模板：The use of fossil fuels, nuclear decay and other traditional methods of obtaining energy results in a significant loss of energy in the form of heat, which in turn exacerbates the energy crisis [X].
- 原句：Nevertheless, the interconnectivity and constraints of each thermoelectric parameter render the achievement of the optimal ZT value a challenging endeavor.
  可迁移模板：Nevertheless, the interconnectivity and constraints of each thermoelectric parameter render the achievement of the optimal METHOD value a challenging endeavor.
- 原句：However, recent studies have demonstrated that the thermoelectric properties of materials do not exhibit a straightforward linear relationship with configurational entropy.
  可迁移模板：However, recent studies have demonstrated that the thermoelectric properties of materials do not exhibit a straightforward linear relationship with configurational entropy.
- 原句：The high-entropy design results in the presence of high-density defects and stress fields within the ce ramics.
  可迁移模板：The high-entropy design results in the presence of high-density defects and stress fields within the ce ramics.
- 原句：The symmetry of the ceramics reduces, and the [TiO6] octahedra undergo stretching and torsion, this microstructural disorder achieves broadband scattering of phonons and reduces the thermal conductivity of the material.
  可迁移模板：The symmetry of the ceramics reduces, and the [TiO6] octahedra undergo stretching and torsion, this microstructural disorder achieves broadband scattering of phonons and reduces the thermal conductivity of the material.
#### 贡献/增量句
- 原句：It is revealed that high entropy effect profoundly modified the microstructure of the material.
  可迁移模板：It is revealed that high entropy effect profoundly modified the microstructure of the material.
- 原句：This work provides theoretical and experimental bases for optimizing the thermoelectric properties of the materials by using high entropy design.
  可迁移模板：This work provides theoretical and experimental bases for optimizing the thermoelectric properties of the materials by using high entropy design.
- 原句：It is revealed that high entropy effect profoundly modified the microstructure of the material.
  可迁移模板：It is revealed that high entropy effect profoundly modified the microstructure of the material.
- 原句：This work provides theoretical and experimental bases for optimizing the thermoelectric properties of the materials by using high entropy design. field.
  可迁移模板：This work provides theoretical and experimental bases for optimizing the thermoelectric properties of the materials by using high entropy design. field.
- 原句：SPS and annealing induction in a reducing atmosphere produced a high concentration of oxygen vacancies, which achieved semi-conductivity of the ceramics and contributed to the high electrical conductivity of the materials.
  可迁移模板：METHOD and annealing induction in a reducing atmosphere produced a high concentration of oxygen vacancies, which achieved semi-conductivity of the ceramics and contributed to the high electrical conductivity of the materials.
#### 限制/边界句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略服务三层：热电材料大背景和 ZT 定义；SrTiO3 优缺点和传统优化路径；高熵/中熵 SrTiO3 相关最新工作。作者用 Banerjee、Lou 说明高熵可降热导，用 Bi、Zhu 说明中熵/非等摩尔可能更优，从而自然引出本文成分设计。

Discussion 中引用用于机制解释，例如 A 位缺位补偿、Raman 峰、氧空位、小极化子、Debye 模型和热导下限等。引用密度在 Introduction 和机制解释段较高，在结果描述段较低。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：78
- Introduction 引文簇数量估计：9
- References 条目数：45
- 可识别年份条目数：69
- 2021 年及以后文献数：34
- 2010 年前经典文献数：8
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Journal of Alloys and Compounds(2)
- 引文簇样例：[4,5], [10], [11], [1], [2], [12], [3], [13], [14], [16], [17], [15]

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 176328.
Z. Wei et al. Journal of Alloys and Compounds 1006 (2024) 176328
Fig.
- 11. Thermoelectric performance of CSBL ceramics, (a) ZT variation curve with temperature; (b) The variation curve of S and σ with configuration entropy; (c) The variation curve of ZT with configuration entropy;(d) Comparison of ZT between L19 ceramics and previously published high-entropy SrTiO3-based ceramics.
References
- [1] M. Mukherjee, A. Srivastava, A. Singh, Recent advances in designing thermoelectric materials, J. Mater. Chem. C. 10 (35) (2022) 12524–12555, https:// doi.org/10.1039/D2TC02448A.
- [2] Y.B. Zhu, D. Ekren, J.Y. Cao, X.D. Liu, S.R. Mudd, R. Boston, X.Q. Xia, Y. Li, I. A. Kinloch, D.J. Lewis, R. Freer, Effect of graphene oxide and carbon black on the thermoelectric performance of niobium doped strontium titanate, J. Alloy. Compd. 988 (2024) 10, https://doi.org/10.1016/j.jallcom.2024.174242.
- [3] X.J. Li, S. Gao, Q. Chen, X. Fan, D.Y. Zhou, W.T. Ji, Y.Q. Chen, Y.W. Zhang, H. A. Ma, X.P. Jia, High pressure and Ti promote oxygen vacancies in perovskites for enhanced thermoelectric performance, J. Alloy. Compd. 922 (2022) 8, https://doi. org/10.1016/j.jallcom.2022.166247.
- [4] A.V. Kovalevsky, A.A. Yaremchenko, S. Populoh, P. Thiel, D.P. Fagg, A. Weidenkaff, J.R. Frade, Towards a high thermoelectric performance in rareearth substituted SrTiO3: effects provided by strongly-reducing sintering conditions, Phys. Chem. Chem. Phys. 16 (48) (2014) 26946–26954, https://doi. org/10.1039/c4cp04127e.
- [5] K. Singsoog, T. Seetawan, A. Vora-Ud, C. Thanachayanont, Theoretical enhancement of thermoelectric properties of Sr1-xLaxTiO3, Integr. Ferroelectr. 155 (1) (2014) 111–118, https://doi.org/10.1080/10584587.2014.905364.
- [6] P. Dey, S.S. Jana, F. Anjum, T. Bhattacharya, T. Maiti, Effect of semiconductor to metal transition on thermoelectric performance in oxide nanocomposites of SrTi0.85Nb0.15O3 with graphene oxide, Appl. Mater. Today 21 (2020) 9, https://doi. org/10.1016/j.apmt.2020.100869.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 构型熵、La 含量、氧空位、孔隙率同时变化，因果拆分不够彻底。
2. L19 最优可能来自多因素偶然平衡，未做独立控制变量实验。
3. XPS 氧空位分峰定量有模型依赖，缺少 EPR/热重或正电子湮没等互证。
4. 晶粒尺寸和孔隙率对热导/电导影响显著，但统计和误差条需复核。
5. ZT=0.20 与文献比较需要考虑温度、密度、测量方法、还原气氛差异。
6. 长期高温稳定性、循环稳定性和实际热电器件输出未验证。
7. 公式和机理解释较多，但没有 DFT 或声子谱实测来直接支撑声子散射频段分配。

## 17. 可复用资产

- 选题资产：把“越高熵越好”的流行直觉改写成“最适构型熵”的问题。
- 证据链资产：成分设计 -> 单相验证 -> 微结构缺陷 -> 电输运 -> 热输运 -> ZT。
- 图表资产：Fig. 11 将构型熵与 S、sigma、ZT 联系，是全篇主 claim 的收束图。
- 机制资产：用多尺度缺陷散射宽频声子解释低热导，用氧空位/载流子/迁移率解释电导非单调。
- 写作资产：在结论中用“not blindly pursue high entropy”形成可记忆的观点。

## 18. 对我写论文的启发

材料论文如果变量很多，要避免只堆表征。本文的启发是把所有表征都绑定到最终性能矛盾：电导为何升降、Seebeck 为何降低、热导为何下降、ZT 为何在中间峰值。这样 XRD/SEM/TEM/Raman/XPS 都不是孤立图，而是因果链上的节点。

另一个启发是，可以反转领域热词。高熵是热点，但文章的真正观点是“适中熵最优”，这比单纯追高熵更容易形成论文记忆点。

## 19. 最终浓缩

这篇论文证明非等摩尔高熵 CSBL 钙钛矿陶瓷中，热电性能不是构型熵越高越好，而是在 L19 的适中构型熵处获得最佳结构-性能平衡。最值得学习的是多表征证据如何服务一个非单调机制；主要复核点是图像细节、氧空位定量、孔隙/晶粒统计和文献 ZT 对比公平性。
