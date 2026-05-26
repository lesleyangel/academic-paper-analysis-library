# Fabrication and thermoelectric properties of Ca-Co-O ceramics with negative Seebeck coefficient

## 0. 读取说明

- 文本来源：`801/文本/txt/Fabrication-and-thermoelectric-properties-of-Ca-Co-O-cerami_2018_Results-in-.txt`，PyMuPDF 抽取，6 页。
- 本文抽取存在正文/参考文献并排混排，尤其 Conclusions 区域被参考文献穿插；已按正文语义复原。
- 重要异常：CALC/Ag 电阻率在正文中出现 0.0663 -> 2.974 mΩ·cm，而摘要/结论写 0.0663 -> 0.2974 mΩ·cm，需要主线程或 PDF 复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：Introduction, Experimental method, Results and discussion, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Fabrication and thermoelectric properties of Ca-Co-O ceramics with negative Seebeck coefficient。
- 作者：Chunlin Gong, Zongmo Shi, Yi Zhang, Yongsheng Chen, Jiaxin Hu, Jianjun Gou, Mengjie Qin, Feng Gao。
- 期刊：Results in Physics，9，2018，1233-1238。
- 领域：氧化物热电材料、Ca-Co-O 陶瓷、n 型转化、还原退火、Ag/La 共掺杂。
- 论文类型：短篇实验发现论文。
- 研究对象：Ca2.55Ag0.3La0.15Co4O9 / x wt% Ag，x=0,10，文中样品主要称 CALC 和 CALC/Ag。
- 方法：固相反应、Ar 中烧结、石墨 + Ar 还原退火、XRD、SEM、XPS、热电性能、Hall 测试。
- 核心结果：Ca-Co-O 通常为 p 型正 Seebeck，本文通过还原退火获得负 Seebeck 的 n 型行为；CALC/Ag PF=1.536 mW/(m·K²) at 623 K，ZT=0.39 at 823 K。

## 2. 摘要与核心信息提取

本文核心主张是：即使 Ca-Co-O 陶瓷通常是 p 型正 Seebeck，通过 Ag/La 共掺和还原气氛退火，也可以得到负 Seebeck 的 n 型 Ca-Co-O 基热电陶瓷，并且具有较高 PF 和 ZT。

摘要的卖点非常集中：材料体系反常转型，即 positive Seebeck -> negative Seebeck；机制上归因于还原气氛中氧空位和载流子浓度/迁移率变化；性能上用 PF 和 ZT 与其他 p/n 型氧化物热电材料对比。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Fabrication-and-thermoelectric-properties-of-Ca-Co-O-cerami_2018_Results-in-.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Fabrication-and-thermoelectric-properties-of-Ca-Co-O-cerami_2018_Results-in-.md`。

中文译文：

> Ca-Co-O陶瓷是典型的p型热电材料，具有正塞贝克系数。在这项工作中，通过在还原气氛中烧结和退火制备了具有负塞贝克系数的n型Ca-Co-O陶瓷。研究了陶瓷的微观结构和热电性能。结果表明，样品在还原气氛中退火后，载流子浓度和载流子迁移率显着增加。随着温度从323 K升高到823 K，电阻率从0.0663 mΩ·cm增加到0.2974 mΩ·cm，负塞贝克系数从-24.9 μV/K变化到-56.3 μV/K，并且在623 K时获得最大功率因数（PF，1.536 mW/m·K2）。样品具有n型热电特性，大的 PF 值和 ZT 值（ZT = 0.39, 823 K）。这一不同寻常的结果将为研究Ca-Co-O热电陶瓷开辟新的途径。空气中温度为 1373 K。目前，大多数研究的Ca-Co-O材料都具有较高的正塞贝克系数作为p型半导体[11-13]，并且已经采取了许多有效的方法来增强Ca-Co-O热电材料的性能，如掺杂、引入纳米相和采用新颖的烧结工艺[4-8]。
>
> 对于空气中的高温应用，热电（TE）模块的制造和表征采用p型和n型TE氧化物材料的各种组合作为分段TE腿，例如p型Ca-Co-O和n型CaMnO3、SrTiO3等[12-15]。然而，p型Ca-Co-O和n型材料在高温下热膨胀系数的差异导致连接器接线片中的热应力以及腿和电极之间的连接问题。因此，必须开发具有相似成分的兼容 p 腿和 n 腿，以缓解这些问题并简化制备过程 [13]。由于p型和n型TE氧化物材料的物理特性相互矛盾，很难制备同时具有p型和n型热电性能的化合物。我们在前期工作中，通过石墨在氩气气氛中退火制备了具有负塞贝克系数的La-Bi共掺杂SrTiO3陶瓷，陶瓷的电阻率降低了6-7个数量级，绝对塞贝克系数也降低了
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自高温氧化物热电模块的配对难题。Ca-Co-O 是成熟 p 型氧化物，但实际 TE 模块需要 p-leg 和 n-leg。若 n 型材料采用 CaMnO3、SrTiO3 等不同体系，会带来热膨胀失配、连接应力和电极兼容问题。因此，开发同一 Ca-Co-O 体系中的 n 型材料有工程吸引力。

作者的切入点是“还原气氛能否把本来 p 型的 Ca-Co-O 转成 n 型”。这不是传统增大 PF 的小优化，而是导电类型反转。论文篇幅短，但选题具有很强的惊奇性和模块应用动机。

## 4. 领域位置与文献版图

Introduction 的文献版图包括：

- 金属氧化物热电材料适合航天/高温环境，因为稳定、环保、寿命长。
- Ca-Co-O 系统包括 CaCo2O4、Ca2Co2O5、Ca3Co4O9、Ca3Co2O6 等，多数为 p 型。
- 高温 TE 模块需要 p/n legs，但不同材料体系热膨胀和连接不兼容。
- 作者前期在 La-Bi co-doped SrTiO3 中通过石墨/Ar 退火获得负 Seebeck，给本文提供工艺迁移依据。

本文的位置是“把还原退火诱导 n 型行为的思路迁移到 Ca-Co-O 系统”，并用 Ag 纳米颗粒进一步增强电导。

## 5. Gap 制造机制

gap 是应用兼容性 gap 与现象 gap 的结合：

1. p 型 Ca-Co-O 性能研究多，但同组成兼容的 n 型 Ca-Co-O 缺乏。
2. 传统 n 型氧化物材料与 p 型 Ca-Co-O 在热膨胀和连接上不匹配。
3. Ca-Co-O 在低氧分压/还原气氛下是否能稳定表现出负 Seebeck，需要实验验证。

作者没有做复杂文献批判，而是用“模块应用需要”和“材料类型反常”制造研究必要性。

## 6. 创新性判断

- 创新类型：实验现象创新 + 工艺迁移。
- 真实创新：在 Ca-Co-O 基陶瓷中通过 Ag/La 共掺和 Ar+C 退火获得负 Seebeck，并报告较高 PF/ZT。
- 创新强度：中等。机制解释相对粗，但现象具有新颖性。
- 证据充分性：XRD/XPS/Hall/热电曲线形成基本闭环；但缺少长期稳定性、可重复性和相组成定量误差。
- 易被挑战处：多相体系复杂，负 Seebeck 是否来自特定 CoO/CaO/Ag 相或界面网络，而非 Ca-Co-O 主体本征转型，需要更细微区分析。

## 7. 论证链条复原

背景：氧化物 TE 适合高温航天废热利用。

痛点：p 型 Ca-Co-O 与其他 n 型氧化物组成不兼容，模块连接存在热应力。

假设：还原退火和 Ag/La 掺杂可改变缺陷化学和载流子类型，使 Ca-Co-O 出现 n 型行为。

制备：固相反应得到 Ca2.55Ag0.3La0.15Co4O9/xAg，Ar 烧结，Ar+C 退火。

结构证据：XRD 显示退火后 Ca3Co2O6、CoO、CaO、Ag 多相，CoO 从 17.1% 增至 26.9%；SEM 显示 Ag 熔融聚集促进致密化；XPS 显示 Co2+ 和氧空位增加。

性能证据：Seebeck 为负，PF 和 ZT 较高；Hall 显示 n 型、载流子浓度和迁移率显著提高。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：During supersonic and hypersonic flight, metal oxide based thermoelectric material has potential to transfer aeroheating energy into essential electrical energy for avionics. Ca2CoO3 layers play an important role in generating thermopower and CoO2 sheets determine the thermal conductivity [7].
- 已有研究不足/GAP：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes. Due to the contradicting physical characteristics of the p-type and n-type TE oxide materials, it is difficult to prepare a compound with both p-type and n-type thermoelectric performance.
- 本文解决方式：Nowadays, most of the investigated Ca-Co-O materials have high positive Seebeck coefficient as p-type semiconductors [11–13], and a lot of effective methods have been taken to enhance the properties of Ca-Co-O thermoelectric materials, such as doping, introducing nano-phases, and using novel sintering process [4–8]. Thus, it is imperative to develop compatible p-legs and n-legs with similar composition to mitigate these problems and simplify the preparation process [13].
- 学术或工程增量：In our previous work, we fabricated La-Bi co-doped SrTiO3 ceramics with negative Seebeck coefficient by annealing with graphite in argon atmosphere, the electrical resistivity of the ceramics reduce 6–7 orders of magnitude, and the absolute Seebeck coefficient decreases Metal oxide based thermoelectric generation is expected to make considerable power conversion efficiency improvements in the satellite and spaceship [1–3].
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

材料配方为 Ca2.55Ag0.3La0.15Co4O9/x wt% Ag，其中 Ag 纳米颗粒平均约 50 nm，用于形成渗流网络并提高电导。粉体球磨 24 h，313 K 干燥，1203 K 空气煅烧 4 h，1473 K Ar 中烧结 10 h，再 1373 K 石墨/Ar 退火 8 h。

结构表征：XRD 判断相组成；SEM 看断口微结构；XPS 用 O 1s 峰拟合估算氧空位相对含量，并用 Co 2p 判断 Co2+；Hall 测载流子浓度和迁移率。

热电计算：电阻率 ρ、Seebeck S、热导率 κ，ZT=(S²T)/(ρκ)，PF=S²/ρ。机制解释涉及 La3+ 替位产生 Ca vacancy、低氧分压下氧空位电离释放电子、Ag 形成导电网络和能量过滤势垒。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| Ca-Co-O 基陶瓷可获得负 Seebeck | 摘要/热电性能 | CALC/Ag 在 323-823 K 范围内 S 为负，823 K 为 -56.3 μV/K | 强 | 需确认测量方向与符号校准 |
| 还原退火增加氧空位 | XPS/表 1 | VO 比例 CALC 从 18.7% 到 20.5%，CALC/Ag 从 21.8% 到 27.9% | 中强 | O 1s 峰拟合模型需复核 |
| Ag 有助于导电网络和致密化 | SEM/实验描述 | Ag 熔点低于烧结温度，可能熔融聚集成网络；密度从 5.19 到 5.47 g/cm³ | 中 | “可能”机制，缺少直接 Ag 网络成像 |
| 多相 Ca-Co-O 退火后相组成改变 | XRD | Ca3Co4O9、Ca3Co2O6、CoO、CaO、Ag；退火后 CoO 增至 26.9% | 中强 | 定量相分析细节需 PDF 复核 |
| CALC/Ag 具有较高 PF | Fig. 6/Table 2 | PF=1.536 mW/(m·K²) at 623 K，高于多种 p/n 型对比材料 | 强 | 对比材料测试条件不完全一致 |
| CALC/Ag 具有可观 ZT | Fig. 8/结论 | ZT=0.39 at 823 K，被称为 n 型氧化物中较高水平 | 强 | 热导率较高，ZT 是否可重复需验证 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 | XRD 相分析 | 退火和 Ag 改变相组成 | Ca3Co2O6/CoO/CaO/Ag 多相；CoO 增加 | 需要 PDF 图像复核 |
| Fig. 2 | SEM 微结构 | Ag 促进致密化/粒径变化 | 退火后平均粒径约 2 μm，密度增加 | 需要 PDF 图像复核 |
| Fig. 3/4 + Table 1 | XPS 和氧空位 | 还原气氛产生 VO | O 1s 峰拟合，VO 比例上升 | 需要 PDF 图像复核 |
| Eq. (1)/(2) | Ca-Co-O 相转变 | 热处理导致相变 | Ca3Co4O9 -> Ca3Co2O6 + CoO；Ca3Co2O6 -> CaO + CoO | 文本足够 |
| Eq. (4)-(6) | 缺陷反应 | La 掺杂/还原产生电子 | Ca vacancy、Co 价态、氧空位释放电子 | 文本足够 |
| Fig. 5 | ρ 与 S 随温度变化 | n 型负 Seebeck 和金属化 | S 为负，ρ 随温度上升 | 需要 PDF 图像复核 |
| Fig. 6-8/Table 2/3 | PF、κ、ZT、Hall | 性能优越和机制支撑 | PF=1.536，ZT=0.39，载流子显著增加 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实结构较短：Introduction；Experimental method；Results and discussion；Microstructure of Ca-Co-O/xAg ceramics；Thermoelectric properties of Ca-Co-O/Ag ceramics；Conclusions。

这是 Results in Physics 风格的短论文：背景和实验快速进入，结果分“微结构/相/缺陷”和“热电性能”两块。结构不复杂，但它把负 Seebeck 现象放在性能部分集中爆发，前半段先铺相变和氧空位机制。

章节标题较朴素，未把“negative Seebeck”放进结果小节标题；标题靠主标题承担卖点。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: Introduction（背景定位/文献缺口）
- L2 p.2: Experimental method（方法/模型/算法）
- L2 p.2: Results and discussion（结果/验证/讨论）
  - L3 p.2: Microstructure of Ca-Co-O/xAg ceramics（对象/模块/过渡章节）
  - L3 p.4: Thermoelectric properties of Ca-Co-O/Ag ceramics（对象/模块/过渡章节）
- L2 p.6: Conclusions（结论/贡献回收）
- L2 p.6: Acknowledgments（尾部材料）
- L2 p.6: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| Introduction | 1 | 2 | 背景定位/文献缺口 |
| Experimental method | 2 | 2 | 方法/模型/算法 |
| Results and discussion | 2 | 2 | 结果/验证/讨论 |
| Microstructure of Ca-Co-O/xAg ceramics | 2 | 3 | 对象/模块/过渡章节 |
| Thermoelectric properties of Ca-Co-O/Ag ceramics | 4 | 3 | 对象/模块/过渡章节 |
| Conclusions | 6 | 2 | 结论/贡献回收 |
| Acknowledgments | 6 | 2 | 尾部材料 |
| References | 6 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 先讲应用，再讲 Ca-Co-O p 型传统，再讲 p/n legs 兼容性，再引入前期还原退火经验。实验段非常压缩，几乎是工艺清单。结果段先用 XRD/SEM/XPS 建立“退火改变相和缺陷”的事实，再用电输运曲线说明 n 型行为，最后用对比表把 PF/ZT 放到文献坐标中。

文中机制解释常常跟在图后立即出现，例如 O 1s 峰后马上解释 VO，电阻率/Seebeck 后马上给出缺陷反应式。

## 13. 文笔画像与语言习惯

文笔简洁直接，甚至略显粗糙，适合短通讯式结果展示。常用词包括 annealing、Ca-Co-O、CALC、Seebeck、n-type、oxygen vacancies、Ag nanoparticles。claim 强度较高，如 “will pave a new way”，但机制论证相对简略。

时态上实验和发现多用过去时，材料常识用一般现在时。被动语态频繁。语言中存在少量拼写/排版问题，如 CACL/CLAC/CALC 混用、conductivity 拼写错误，这也提示需要 PDF 复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：11571
- 高频词：annealing(23)；thermoelectric(18)；ca-co-o(18)；coo(17)；ceramics(15)；samples(14)；fit(12)；materials(11)；atmosphere(11)；oxygen(11)；seebeck(10)；peak(10)；calc(9)；high(8)；carrier(8)；temperature(8)；pick(8)；energy(7)；electrical(7)；coefficient(7)
- 高频名词化/学术名词：ceramics(15)；temperature(8)；mobility(6)；concentration(5)；resistivity(5)；conductivity(4)；composition(3)；characteristics(3)；reaction(3)；performance(2)；radiation(2)；equipment(2)；valence(2)；generation(1)；conversion(1)
- 高频学术动词：develop(1)；demonstrate(1)；compared(1)
- 高频形容词：thermoelectric(18)；electrical(7)；coefficient(7)；different(6)；thermal(5)；negative(5)；cumulative(4)；metal(3)；material(3)；chemical(3)；content(3)；metallic(3)；positive(2)；conventional(2)；semi-conductive(2)
- 高频副词：dramatically(3)；typically(2)；recently(1)；monotonically(1)；specifically(1)
- 高频二词短语：fit pick(8)；reducing atmosphere(7)；seebeck coefficient(6)；thermoelectric properties(5)；negative seebeck(5)；carrier concentration(5)；electrical resistivity(5)；ca-co-o ceramics(4)；ceramics negative(4)；seebeck coefficients(4)；samples annealed(4)；ca-co-o thermoelectric(4)
- 高频三词短语：ceramics negative seebeck(4)；cumulative fit peak(4)；peak fit pick(4)；negative seebeck coefficients(3)；sintering annealing reducing(3)；annealing reducing atmosphere(3)；annealed reducing atmosphere(3)；ca-co-o thermoelectric ceramics(3)；graphite argon atmosphere(3)；cao metallic phases(3)；annealing binding energy(3)；binding energy annealing(3)
- 被动语态估计：38；`we + 动作动词` 主动句估计：0
- 一般现在时线索：37；一般过去时线索：99；现在完成时线索：2；情态动词线索：11

分章节正文词频：

- Introduction: thermoelectric(14)；ca-co-o(11)；ceramics(8)；materials(8)；high(7)；seebeck(6)；oxide(5)；coefficient(5)
- Experimental method: samples(4)；argon(3)；rate(3)；min(3)；nanoparticles(2)；size(2)；raw(2)；materials(2)
- Results and discussion: annealing(18)；coo(13)；fit(12)；oxygen(10)；peak(10)；pick(8)；calc(7)；ca-co-o(6)
- Conclusions: carrier(5)；concentration(3)；thermoelectric(2)；seebeck(2)；coefficient(2)；reducing(2)；atmosphere(2)；samples(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：Metal oxide based thermoelectric generation is expected to...
- gap 句式：It is imperative to develop compatible p-legs and n-legs with similar composition.
- 现象句式：The samples possess n-type semi-conductive characteristics.
- 机制句式：This should be ascribed to the change in carrier concentration and oxygen vacancy.
- 对比句式：Compared with other n-type oxide thermoelectric ceramics, the ZT value shows a high level.
- 可复用模板：通过还原气氛调控缺陷化学，把传统 p 型氧化物体系转化为 n 型候选材料。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：During supersonic and hypersonic flight, metal oxide based thermoelectric material has potential to transfer aeroheating energy into essential electrical energy for avionics.
  可迁移模板：During supersonic and hypersonic flight, metal oxide based thermoelectric material has potential to transfer aeroheating energy into essential electrical energy for avionics.
- 原句：Ca2CoO3 layers play an important role in generating thermopower and CoO2 sheets determine the thermal conductivity [7].
  可迁移模板：Ca2CoO3 layers play an important role in generating thermopower and CoO2 sheets determine the thermal conductivity [X].
#### Gap/转折句
- 原句：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
  可迁移模板：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
- 原句：Due to the contradicting physical characteristics of the p-type and n-type TE oxide materials, it is difficult to prepare a compound with both p-type and n-type thermoelectric performance.
  可迁移模板：Due to the contradicting physical characteristics of the p-type and n-type METHOD oxide materials, it is difficult to prepare a compound with both p-type and n-type thermoelectric performance.
- 原句：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
  可迁移模板：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
- 原句：Due to the contradicting physical characteristics of the p-type and n-type TE oxide materials, it is difficult to prepare a compound with both p-type and n-type thermoelectric performance.
  可迁移模板：Due to the contradicting physical characteristics of the p-type and n-type METHOD oxide materials, it is difficult to prepare a compound with both p-type and n-type thermoelectric performance.
#### 方法提出句
- 原句：Nowadays, most of the investigated Ca-Co-O materials have high positive Seebeck coefficient as p-type semiconductors [11–13], and a lot of effective methods have been taken to enhance the properties of Ca-Co-O thermoelectric materials, such as doping, introducing nano-phases, and using novel sintering process [4–8].
  可迁移模板：Nowadays, most of the investigated Ca-Co-O materials have high positive Seebeck coefficient as p-type semiconductors [X–X], and a lot of effective methods have been taken to enhance the properties of Ca-Co-O thermoelectric materials, such as doping, introducing nano-phases, and using novel sintering process [X–X].
- 原句：Thus, it is imperative to develop compatible p-legs and n-legs with similar composition to mitigate these problems and simplify the preparation process [13].
  可迁移模板：Thus, it is imperative to develop compatible p-legs and n-legs with similar composition to mitigate these problems and simplify the preparation process [X].
- 原句：Nowadays, most of the investigated Ca-Co-O materials have high positive Seebeck coefficient as p-type semiconductors [11–13], and a lot of effective methods have been taken to enhance the properties of Ca-Co-O thermoelectric materials, such as doping, introducing nano-phases, and using novel sintering process [4–8].
  可迁移模板：Nowadays, most of the investigated Ca-Co-O materials have high positive Seebeck coefficient as p-type semiconductors [X–X], and a lot of effective methods have been taken to enhance the properties of Ca-Co-O thermoelectric materials, such as doping, introducing nano-phases, and using novel sintering process [X–X].
- 原句：Thus, it is imperative to develop compatible p-legs and n-legs with similar composition to mitigate these problems and simplify the preparation process [13].
  可迁移模板：Thus, it is imperative to develop compatible p-legs and n-legs with similar composition to mitigate these problems and simplify the preparation process [X].
- 原句：In this work, we prepare (Ag, La) co-doped Ca-Co-O ceramics by the conventional solid state reaction method and process them in a similar fashion. n-type semi-conductive Ca-Co-O thermoelectric ceramics are obtained and the mechanism has been discussed.
  可迁移模板：In this work, we prepare (Ag, La) co-doped Ca-Co-O ceramics by the conventional solid state reaction method and process them in a similar fashion. n-type semi-conductive Ca-Co-O thermoelectric ceramics are obtained and the mechanism has been discussed.
#### 结果呈现句
- 原句：The results show that the carrier concentration and the carrier mobility dramatically increase after the samples were annealed in the reducing atmosphere.
  可迁移模板：The results show that the carrier concentration and the carrier mobility dramatically increase after the samples were annealed in the reducing atmosphere.
- 原句：The unusual results will pave a new way for studying Ca-Co-O thermoelectric ceramics. at 1373 K in air.
  可迁移模板：The unusual results will pave a new way for studying Ca-Co-O thermoelectric ceramics. at METHOD in air.
- 原句：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
  可迁移模板：However, the difference in thermal expansion coefficient between p-type Ca-Co-O and ntype materials at high temperatures results in thermal stress in the connector lug and connection problems between the legs and electrodes.
- 原句：The results show that the carrier concentration and the carrier mobility dramatically increase after the samples were annealed in the reducing atmosphere.
  可迁移模板：The results show that the carrier concentration and the carrier mobility dramatically increase after the samples were annealed in the reducing atmosphere.
- 原句：The unusual results will pave a new way for studying Ca-Co-O thermoelectric ceramics. at 1373 K in air.
  可迁移模板：The unusual results will pave a new way for studying Ca-Co-O thermoelectric ceramics. at METHOD in air.
#### 贡献/增量句
- 原句：In our previous work, we fabricated La-Bi co-doped SrTiO3 ceramics with negative Seebeck coefficient by annealing with graphite in argon atmosphere, the electrical resistivity of the ceramics reduce 6–7 orders of magnitude, and the absolute Seebeck coefficient decreases Metal oxide based thermoelectric generation is expected to make considerable power conversion efficiency improvements in the satellite and spaceship [1–3].
  可迁移模板：In our previous work, we fabricated La-Bi co-doped SrTiO3 ceramics with negative Seebeck coefficient by annealing with graphite in argon atmosphere, the electrical resistivity of the ceramics reduce X–Xorders of magnitude, and the absolute Seebeck coefficient decreases Metal oxide based thermoelectric generation is expected to make considerable power conversion efficiency improvements in the satellite and spaceship [X–X].
#### 限制/边界句
- 原句：With increasing temperature, the electrical resistivity of CALC/Ag increases from 0.0663 mΩ·cm to 0.2974 mΩ·cm, the Seebeck coefficient varies from −24.9 μV/K to −56.3 μV/K, which should be ascribed to the change in carrier concentration and oxygen vacancy.
  可迁移模板：With increasing temperature, the electrical resistivity of METHOD/Ag increases from XmΩ·cm to XmΩ·cm, the Seebeck coefficient varies from −XμV/K to −XμV/K, which should be ascribed to the change in carrier concentration and oxygen vacancy.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用主要用于三件事：证明氧化物 TE 的高温应用价值；说明 Ca-Co-O 通常是 p 型体系；把本文 PF/ZT 放进与 p 型 Ca-Co-O 和 n 型 SrTiO3/CaMnO3/ZnAlGaO 等材料对比的坐标中。

引用姿态偏“结果对比”而非系统综述。Table 2 是关键引用资产：它把本文 CALC/Ag 的 PF 和 ZT 与多种材料并列，使短论文的性能 claim 更容易成立。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：52
- Introduction 引文簇数量估计：6
- References 条目数：27
- 可识别年份条目数：27
- 2021 年及以后文献数：0
- 2010 年前经典文献数：7
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：[7,8], [9], [13], [7], [10], [14,15], [7], [14], [15], [22], [5], [9]

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- [1] Terasaki I. Transport properties and electronic states of the thermoelectric oxide NaCo2O4. Phys B 2003;328:63–7.
- [2] Yin LH, Ang R, Li LJ, Zhao BC, Fu YK, Zhu XB, Yang ZR, Song WH, Sun YP. Thermoelectric properties of sol–gel derived cobaltite Bi2Ca2.4Co2Oy. Phys B 2011;406:2914–8.
- [3] Wang Y, Sui Y, Cheng JG, Wang XJ, Su WH, Liu XY, Fan HJ. Doping-induced metalinsulator transition and the thermal transport properties in Ca3-xYxCo4O9. J Phys Chem C 2010;114:5174–81.
- [4] Li CH, Guo DL, Li KJ, Shao B, Chen DM, Ma YL, Sun JC. Excellent thermoelectricity performance of p-type SnSe along b axis. Phys B 2018;530:264–9.
- [5] Boyle C, Liang L, Chen Y, Prucz J, Cakmak E, Watkins TR, Lara-Curzio E, Song XY. Competing dopants grain boundary segregation and resultant seebeck coefficient and power factor enhancement of thermoelectric calcium cobaltite ceramics. Ceram Int 2017;43:11523–8.
- [6] Ohta H, Sugiura K, Koumoto K. Recent progress in oxide thermoelectric materials: p-type Ca3Co4O9 and n-type SrTiO3. Inorg Chem 2008;47:8429–36.
- [7] Fergus JW. Oxide materials for high temperature thermoelectric energy conversion. J Eur Ceram Soc 2012;32:525–40.
- [8] Kahraman F, Madre MA, Rasekh S, Salvador C, Bosque P, Torre MA, Diez JC, Sotelo A. Enhancement of mechanical and thermoelectric properties of Ca3Co4O9 by Ag addition. J Eur Ceram Soc 2015;43:3835–41.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 电阻率数值不一致：0.2974 和 2.974 mΩ·cm 冲突，必须 PDF 复核。
- 多相归因风险：n 型行为可能来自 CoO/Ag 网络等局部相，而非 Ca-Co-O 主相统一转型。
- 机制证据较粗：Ag 能量过滤、导电网络、氧空位释放电子都合理，但直接证据有限。
- 稳定性缺失：高温还原态 n 型 Ca-Co-O 在空气/热循环中的稳定性未充分讨论。
- 样品组较少：主要 x=0/10 wt% Ag，缺少系统 Ag 含量和退火条件优化。
- 语言和排版问题可能影响可信度，需要核查原 PDF。

## 17. 可复用资产

- 选题资产：同一材料体系中构建 p/n 兼容 legs，解决模块集成问题。
- 论证资产：异常符号/类型转变可以作为论文核心卖点。
- 图表资产：XRD 相变 + XPS 缺陷 + Hall 载流子 + S 符号 + PF/ZT 对比表。
- 写作资产：短论文可用“反常现象 + 简明机制 + 对比表”快速完成说服。
- 机制资产：还原气氛、氧空位、金属纳米相网络、能量过滤。

## 18. 对我写论文的启发

如果实验发现足够“反常”，文章不一定需要复杂模型。本文最有效的写法是把“通常 p 型”的领域常识和“本文负 Seebeck”的结果并置，形成强烈落差。

但它也提醒：短论文中数值、符号、样品名必须极其干净，否则读者会怀疑结果可靠性。写自己的论文时，异常现象越强，越要补足复现、校准和稳定性证据。

## 19. 最终浓缩

本文最值得学的是用还原退火和 Ag/La 掺杂把传统 p 型 Ca-Co-O 推向 n 型负 Seebeck 候选材料。最强证据是负 Seebeck、Hall n 型、氧空位增加、PF=1.536 mW/(m·K²) 和 ZT=0.39。最大风险是多相机制不够清楚、稳定性不足，且电阻率数值存在抽取/原文冲突，必须 PDF 复核。
