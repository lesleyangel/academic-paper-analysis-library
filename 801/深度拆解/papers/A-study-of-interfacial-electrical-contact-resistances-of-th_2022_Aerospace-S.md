# A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations

## 0. 读取说明

本文拆解依据 `801/文本/txt/A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.txt` 的全文抽取。由于抽取文本存在双栏串行、图表跨栏和公式错位，图像云图、色标、局部粗糙形貌与部分公式排版需要 PDF 图像复核。以下分析以可从 txt 稳定确认的信息为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The TEG and material properties of its components, 3 Two-scale numerical model, 4 Experimental measurement platform for ECR, 5 Results and discussions, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations
- 作者：Ge Gao, Dou Li, Jian-Jun Gou, Chun-Lin Gong, Shuang-Ming Li
- 期刊：Aerospace Science and Technology, 131, 107966
- 年份：2022
- 领域：高超声速飞行器热管理、热电发电器、界面电接触、电-热耦合仿真。
- 论文类型：实验测量 + 两尺度数值模拟 + 工程性能评估。
- 研究对象：高超声速飞行器用 TEG 中 TE legs 与 copper electrodes 之间四类电接触界面：E-N_l、E-N_u、E-P_l、E-P_u。
- 方法：真实粗糙表面测量与重构、微米尺度接触力学/电传导仿真、ECR 实验平台验证、毫米尺度 TEG 等效界面层模型。
- 主要证据：粗糙度测量、接触应力/真实接触面积、电势和电流密度云图、ECR 随温度/压力/间隙介质变化曲线、实验-仿真误差表、TEG 内阻与最大输出功率对比。
- 目标读者：高超声速热防护/热管理研究者、TEG 设计者、界面接触建模与实验测量研究者。

## 2. 摘要与核心信息提取

一句话主张：高超声速飞行器 TEG 中 TE legs 与电极之间的微米粗糙界面会产生显著 ECR，必须通过真实形貌两尺度模型和实验测量定量计入，否则会严重高估 TEG 输出功率。

核心问题不是“TEG 能否发电”，而是“界面电接触非理想性是否足以改变 TEG 性能评估”。摘要先把工程背景定为高超声速气动热回收，再把瓶颈压缩到微米尺度粗糙度导致的电流收缩，最后用两尺度模型把微观 ECR 映射到宏观 TEG 输出功率。关键结论包括：空气间隙下 ECR 会使 TEG 最大输出功率较完美接触降低约 83%；银环氧胶间隙下影响约 2.0%；实验与数值整体吻合，最大差异在四个接触对中为 13.2%、14.9%、38.9%、17.7%。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.md`。

中文译文：

> 文章历史记录： 收到日期 2022年4月8日 以修订形式收到 2022年9月30日 接受日期 2022年10月19日 在线提供 2022年10月25日 由Jang-Kyo Kim传播
>
> 高超声速飞行器表面会产生大量的气动热，热电发电机（TEG）技术具有将气动热转化为电能的潜力。在 TEG 中，TE 腿和电极表面的微米级粗糙度会导致界面电流收缩并产生接触电阻 (ECR)。 TEG 的传热和转换过程很大程度上受此类 ECR 的影响。在这项工作中，TEG包括两个陶瓷基板，并建立了中间TE层，TE层由绝缘材料、N型和P型TE腿以及连接TE腿的电极组成。通过两尺度数值模拟和实验测量研究了 ECR 及其对 TEG 性能的影响。首先，测量TE腿和电极粗糙表面的实际形貌，并基于重建的形貌建立微米级ECR预测数值模型。
>
> 开发了ECR测量平台，该平台由压力装置、电源和数据采集系统组成，分别用于提供加载压力、电压以及电流和电压信号的采集。然后预测不同温度、加载压力和间隙介质下的 ECR，并通过一系列测量验证数值模型。其次，通过毫米级模型模拟TEG的TE转换过程，该模型包括绝缘材料、TE腿、电极和ECR的等效界面层。由此阐明了ECR对高超声速飞行器TEG TE性能的影响。 © 2022 Elsevier Masson SAS。版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

问题来源来自工程瓶颈：高超声速飞行器表面气动热巨大，传统热防护系统的重量和体积可能不可承受，TEG 被引入作为能量回收式热管理方案。但 TEG 不是理想多材料串联体，TE legs 与电极存在粗糙接触界面，真实接触区域极小，电流被迫收缩通过少量 asperity，从而产生 ECR。

作者的收束方式很清楚：从“飞行器热管理”收束到“高超声速 TEG”，再收束到“四个 TE leg-electrode 接触界面”，最后收束到 ECR 对最大输出功率的影响。这个选题的价值在于把一个常被等效忽略的界面参数变成可测、可算、可进入系统性能模型的工程量。

为什么现在值得研究：前文已有 TEG 高超声速应用、热电材料、ECR 理论/测量/预测模型，但这些研究要么不针对高超声速 TEG，要么粗糙形貌依赖假设，要么只定性说明 ECR 重要。本文的切入点是“真实形貌 + 实验验证 + TEG 性能降额”三件事同时完成。

## 4. 领域位置与文献版图

文献版图可分为四组。

第一组是高超声速 TEG 与热管理应用。作者先说明 aerodynamic heat、hot fuel、engine combustion heat 三类热源，并引用本团队和他人关于多级 TEG、scramjet、Brayton-cycle + TEG 的工作，证明 TEG 在高温差场景下有应用前景。

第二组是热电材料与 TEG 构型。CoSb3 基 skutterudite 被定位为 800 K 以下具有潜力的块体热电材料，这使本文选用 Yb0.29Co4Sb12 与 La0.1Ce0.8Fe3CoSb12 具有工程背景。

第三组是 ECR 理论、实验和数值预测。作者列举动态模型、体积接触理论、数字万用表测量、X-ray CT 间接测量、微接触模型、随机粗糙体模型等，指出许多数值模型在粗糙表面构造中采用假设，可靠性受限。

第四组是 ECR 对 TEG/TEC 性能影响。已有研究指出 ECR 可能严重影响 TEG/TEC 设计优化，但高超声速 TEG 很少考虑 ECR。因此本文站位不是从零提出 ECR，而是把 ECR 放入高超声速 TEG 的真实几何和任务温度范围。

## 5. Gap 制造机制

作者制造 gap 的方式是“已有研究重要，但缺一个可验证的工程闭环”。

- 对象 gap：已有 ECR 研究不一定覆盖高超声速飞行器 TEG 的 TE leg-electrode 异质界面。
- 方法 gap：许多数值模型用随机或理想化粗糙形貌，本文强调真实表面形貌测量与重构。
- 验证 gap：ECR 预测若没有实验平台支撑，难以用于设计。
- 系统 gap：已有 TEG 性能评估很少把四个 ECR 界面等效为宏观模型中的界面层。

这个 gap 基本真实且重要。最强的一点是作者没有只说“ECR 重要”，而是把其影响换算成最大输出功率下降 83%。最弱的一点是实验验证只在有限压力和 298 K 条件下直接测 ECR，高温条件的模型可信度主要来自材料参数和仿真推断。

## 6. 创新性判断

作者声明的贡献包括：建立高超声速 TEG；基于真实粗糙形貌建立微米尺度 ECR 预测模型；搭建 ECR 测量平台并验证模型；把 ECR 作为等效界面层纳入毫米尺度 TEG，评估输出功率影响。

真实创新更像“工程建模链条创新”而不是基础理论创新。它把表面测量、接触力学、电传导、实验标定和 TE 转换性能串成一条链。创新强度为中等偏强：单个模块并非全新，但组合后解决了高超声速 TEG 设计中一个具体且高影响的非理想因素。

可能被挑战的地方：银环氧胶间隙把 ECR 降低约 1000 倍，这个结论很工程有用，但长期高温、热循环、力学可靠性和界面老化没有展开；空气间隙下 83% 降额很强，但同时未计入 thermal contact resistance，因此系统级真实性仍需与热接触模型联用。

## 7. 论证链条复原

论证链条如下：

高超声速飞行器气动热管理困难 → TEG 有潜力回收热量并供电 → TEG 中 TE legs 与 electrodes 是串联电流路径的关键界面 → 微米粗糙度导致真实接触面积小、电流收缩和 ECR → 现有模型依赖粗糙面假设且高超声速 TEG 少有 ECR 定量 → 本文测量真实形貌并建立微尺度接触/电传导模型 → 用实验平台验证 ECR → 把 ECR 等效成 TEG 界面层 → 计算内阻和最大输出功率变化 → 得出 ECR 不能忽略，导电界面材料和预压可缓解。

闭合度较好。背景、gap、方法、证据、结论都能互相回扣。薄弱环节是实验工况覆盖范围窄于仿真工况，且污染膜/氧化膜未进模型，导致 E-P_l 最大差异达到 38.9%。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：需结合 Introduction 的文献转折句复核。
- 本文解决方式：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography. An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
- 学术或工程增量：An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法名称：真实形貌驱动的两尺度 ECR-TEG 性能预测框架。

输入包括：TE legs 与 electrodes 的 3D 光学测量表面、材料物性、温度、加载压力、间隙介质、TEG 几何和边界温度。输出包括：四个接触对的 ECR、等效界面层电导率、TEG 内阻和最大输出功率。

关键步骤：

1. 用 Bruker Contour GT-K 测量 TE legs 与 electrodes 粗糙面，每个粗糙面约 7700 数据点，并在 CATIA 中重构。
2. 在 ABAQUS 中建立微米尺度接触对模型，先做接触力学，再导入变形后的模型做电传导分析。
3. 对 ECR 计算等效界面层电导率，界面层厚度取对应粗糙面的平均距离。
4. 在 ANSYS Multiphysics 中建立毫米尺度 TEG 模型，因为 ABAQUS 不能模拟 Seebeck effect。
5. 搭建 ECR 实验平台，用压力装置、电源、数据采集系统和电阻箱测量不同压力下 ECR。

关键假设：闭合接触单元为 perfect contact；污染和氧化膜电阻不计；冷源假定为 kerosene，详细冷却过程不涉及；热接触电阻在本文 TEG 性能部分未考虑，主要考察 ECR 的电学影响。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 真实粗糙界面会显著限制实际电接触区域 | 方法与结果 5.1 | Fig. 2 重构粗糙面；Fig. 7/8 应力云图；真实接触面积在 0.3 MPa 以下最大小于 0.6% | 强 | 云图细节需 PDF 图像复核 |
| 加载压力增大可降低 ECR | 结果 5.3.2 | Fig. 15：四类接触对在空气与银环氧胶间隙下 ECR 随压力增大下降 | 强 | 压力范围有限，预压可靠性未评估 |
| 温度对 ECR 的影响依赖材料电导率变化 | 结果 5.3.1 | Fig. 14：N 型 ECR 随温度升高增加；P 型先增加后降低，解释为 TE 材料电导率变化 | 中-强 | 高温实验验证不足，主要来自仿真 |
| 银环氧胶间隙显著降低 ECR | 结果 5.2/5.3.2 | Fig. 10/13/15：银环氧胶提高非接触区电势与电流密度，ECR 约比空气小 1000 倍 | 强 | 长期服役、热循环和材料兼容性未展开 |
| 数值模型可预测不同环境下 ECR | 实验验证 5.3.3 | Table 4：四接触对实验-仿真最大差异 13.2%、14.9%、38.9%、17.7% | 中 | E-P_l 差异 38.9% 偏大，污染膜未建模 |
| ECR 会严重降低 TEG 最大输出功率 | 结果 5.4 | Fig. 19-21：空气间隙下 ECR 约为 TE 材料电阻 4 倍，最大输出功率降约 83% | 强 | 仅考察电接触，未和 TCR 同时耦合 |
| 高导电界面材料和适当预压可缓解负面影响 | 结论 | 银环氧胶条件功率仅降低约 2.0%，压力增大使 ECR 降低 | 中 | “适当预压”的结构安全边界需额外实验 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 TEG for hypersonic vehicles | 把宏观飞行器热管理问题收束到一个代表性 TEG 单元 | 研究对象具有工程真实性 | TEG 位于背风区，包含 substrates、TE legs、electrodes、PEEK shell | 需要 PDF 图像复核布局 |
| Table 1/2 材料物性 | 提供接触力学、电传导、TEG 仿真的参数基础 | 模型可复现 | 给出 TE 材料、铜、氧化铝、PEEK 的弹性、屈服、热/电导率 | 基本可从 txt 确认 |
| Fig. 2 粗糙面重构 | 支撑“真实形貌建模”创新 | 减少粗糙面假设 | 给出 N/P TE legs 与 electrode 的实测/重构表面 | 需要 PDF 图像复核粗糙面细节 |
| Fig. 3-5 模型和网格 | 说明两尺度模型如何连接 | 方法闭环 | 微尺度接触对与宏观 TEG 网格/界面层 | 需要 PDF 图像复核网格质量 |
| Eq. (12)-(13) TE 耦合控制方程 | 说明热、电、Seebeck/Peltier 耦合机制 | TEG 性能可计算 | 温度方程含 Joule/Peltier 项，电势方程含 Seebeck 项 | 公式排版需 PDF 复核 |
| Fig. 7-9 接触应力与面积 | 证明压力改变真实接触区域 | 压力降低 ECR 的物理原因 | 接触面积随压力近似线性增大 | 云图色标需 PDF 复核 |
| Fig. 10-13 电势/电流密度云图 | 揭示空气 vs 银环氧胶间隙的导电差异 | 高导电介质降低 ECR | 银环氧胶使非接触区电流显著增加 | 需要 PDF 图像复核 |
| Table 4 实验-数值 ECR | 验证模型可信度 | 模型可预测 ECR | 最大差异 38.9%，多数差异较小 | 可从 txt 确认 |
| Fig. 19-21 内阻与功率 | 将微观 ECR 转换为系统级输出降额 | ECR 不可忽略 | 空气间隙最大输出功率约为完美接触的 1/5 | 曲线细节需 PDF 复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The TEG and material properties of its components；3 Two-scale numerical model；4 Experimental measurement platform for ECR；5 Results and discussions；6 Conclusion，并含 Appendix A 材料制备与物性。

结构是典型工程建模论文：先立工程对象，再给材料和几何，再给模型，再给实验平台，最后结果分层展开。第 5 节内部顺序从 contact mechanics 到 electric conduction，再到 ECR 定量和 TEG performance，符合“微观机制 → 界面参数 → 系统性能”的推进逻辑。

标题命名偏好偏描述型，少用结论型标题。好处是稳健、工程论文可接受；缺点是标题本身不暴露最强发现，例如 `5.4 TE performance` 可以更有力地写成 “ECR-induced internal resistance dominates power degradation under air gaps”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The TEG and material properties of its components（对象/模块/过渡章节）
  - L3 p.3: 2.1 The TEG for hypersonic vehicles（对象/模块/过渡章节）
  - L3 p.4: 2.2 Physical properties of materials（对象/模块/过渡章节）
- L2 p.4: 3 Two-scale numerical model（方法/模型/算法）
  - L3 p.4: 3.1 Rough surfaces（对象/模块/过渡章节）
  - L3 p.4: 3.2 Contact mechanics and electric conduction analysis（对象/模块/过渡章节）
    - L4 p.4: 3.2.1 Model formation and meshing（方法/模型/算法）
    - L4 p.5: 3.2.2 Analysis method and boundary conditions（方法/模型/算法）
  - L3 p.7: 3.3 TE conversion performance evaluation（对象/模块/过渡章节）
  - L3 p.8: 3.4 Governing and constitutive equations（对象/模块/过渡章节）
    - L4 p.8: 3.4.1 Mechanical contact process（对象/模块/过渡章节）
    - L4 p.8: 3.4.2 Heat conduction and TE conversion processes（对象/模块/过渡章节）
- L2 p.9: 4 Experimental measurement platform for ECR（结果/验证/讨论）
- L2 p.9: 5 Results and discussions（结果/验证/讨论）
  - L3 p.9: 5.1 Contact mechanics（对象/模块/过渡章节）
  - L3 p.11: 5.2 Electric conduction（对象/模块/过渡章节）
  - L3 p.13: 5.3 Electrical contact resistance（对象/模块/过渡章节）
    - L4 p.13: 5.3.1 The influence of temperature（对象/模块/过渡章节）
    - L4 p.14: 5.3.2 The influence of loading pressure（对象/模块/过渡章节）
    - L4 p.14: 5.3.3 The experimental measurement results and the validation of numerical models（方法/模型/算法）
  - L3 p.15: 5.4 TE performance（对象/模块/过渡章节）
- L2 p.17: 6 Conclusion（结论/贡献回收）
- L2 p.17: CRediT authorship contribution statement（尾部材料）
- L2 p.17: Declaration of competing interest（尾部材料）
- L2 p.18: Data availability（尾部材料）
- L2 p.18: Acknowledgements（尾部材料）
- L2 p.18: Appendix A Fabrication and property testing of TE materials（尾部材料）
- L2 p.19: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The TEG and material properties of its components | 3 | 2 | 对象/模块/过渡章节 |
| 2.1 The TEG for hypersonic vehicles | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Physical properties of materials | 4 | 3 | 对象/模块/过渡章节 |
| 3 Two-scale numerical model | 4 | 2 | 方法/模型/算法 |
| 3.1 Rough surfaces | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Contact mechanics and electric conduction analysis | 4 | 3 | 对象/模块/过渡章节 |
| 3.2.1 Model formation and meshing | 4 | 4 | 方法/模型/算法 |
| 3.2.2 Analysis method and boundary conditions | 5 | 4 | 方法/模型/算法 |
| 3.3 TE conversion performance evaluation | 7 | 3 | 对象/模块/过渡章节 |
| 3.4 Governing and constitutive equations | 8 | 3 | 对象/模块/过渡章节 |
| 3.4.1 Mechanical contact process | 8 | 4 | 对象/模块/过渡章节 |
| 3.4.2 Heat conduction and TE conversion processes | 8 | 4 | 对象/模块/过渡章节 |
| 4 Experimental measurement platform for ECR | 9 | 2 | 结果/验证/讨论 |
| 5 Results and discussions | 9 | 2 | 结果/验证/讨论 |
| 5.1 Contact mechanics | 9 | 3 | 对象/模块/过渡章节 |
| 5.2 Electric conduction | 11 | 3 | 对象/模块/过渡章节 |
| 5.3 Electrical contact resistance | 13 | 3 | 对象/模块/过渡章节 |
| 5.3.1 The influence of temperature | 13 | 4 | 对象/模块/过渡章节 |
| 5.3.2 The influence of loading pressure | 14 | 4 | 对象/模块/过渡章节 |
| 5.3.3 The experimental measurement results and the validation of numerical models | 14 | 4 | 方法/模型/算法 |
| 5.4 TE performance | 15 | 3 | 对象/模块/过渡章节 |
| 6 Conclusion | 17 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 17 | 2 | 尾部材料 |
| Declaration of competing interest | 17 | 2 | 尾部材料 |
| Data availability | 18 | 2 | 尾部材料 |
| Acknowledgements | 18 | 2 | 尾部材料 |
| Appendix A Fabrication and property testing of TE materials | 18 | 2 | 尾部材料 |
| References | 19 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“高超声速热管理压力 → TEG 前景 → TEG 材料和结构 → 接触界面 ECR → 已有 ECR 研究 → 高超声速 TEG 未充分考虑 → 本文做什么”。每段都承担一个收束功能，没有长时间停留在大背景。

方法段落多采用“先给图，再解释图中的对象和参数，再说明软件/边界条件”的顺序。结果段落则经常以 “Fig. X shows...” 开头，然后分 a/b/c/d 子图逐一描述，最后用一句 “In short / Overall / In conclusion” 收束规律。

叙事节奏偏密集数据型。优点是证据充分；缺点是段落中数值很多，读者需要图表配合才能抓住主线。可学习的是每个结果小节都回到一个物理解释：接触面积、材料电导率、间隙介质导电性、内阻。

## 13. 文笔画像与语言习惯

整体语气谨慎但工程判断明确。高频表达包括 “It should be noted that”, “As shown in Fig.”, “In short”, “Overall”, “it can be found that”。作者很少用夸张形容词，更多用数值和趋势支撑判断。

时态上，背景和一般规律用一般现在时；实验和本文操作用一般过去时或现在完成时；图表解读用一般现在时。主动语态与被动语态混用，方法部分被动多，如 “is established”, “is simulated”, “is measured”；贡献陈述和结论中主动性较强，如 “we can conclude”。

情态动词使用克制，常用 “can be”, “should be”, “may”。名词化程度高：constriction, electrical contact resistance, compression displacement, equivalent interfacial layers, thermoelectric conversion process。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：37512
- 高频词：ecr(71)；contact(66)；teg(50)；loading(37)；temperature(37)；surface(35)；heat(32)；electric(32)；electrical(28)；legs(27)；surfaces(26)；rough(26)；resistance(25)；pressure(25)；leg(25)；electrodes(23)；gap(23)；contacting(23)；model(22)；increases(22)
- 高频名词化/学术名词：temperature(37)；resistance(25)；pressure(25)；conductivity(18)；compression(17)；displacement(17)；conversion(16)；performance(13)；influence(13)；conduction(11)；difference(10)；simulation(9)；mechanics(9)；density(8)；prediction(7)
- 高频学术动词：developed(7)；validated(4)；predicted(3)；provide(2)；predict(2)；optimized(1)；presented(1)；evaluated(1)；analyzed(1)；provided(1)；compare(1)；indicated(1)；compared(1)
- 高频形容词：electric(32)；electrical(28)；potential(20)；numerical(19)；hypersonic(18)；displacement(17)；current(15)；adhesive(14)；different(13)；thermal(12)；material(12)；experimental(12)；real(11)；aerodynamic(9)；coefficient(9)
- 高频副词：supply(5)；mainly(5)；gradually(5)；relatively(4)；greatly(2)；usually(2)；significantly(2)；slightly(2)；widely(1)；directly(1)；indirectly(1)；especially(1)；rarely(1)；evenly(1)；comprehensively(1)
- 高频二词短语：rough surfaces(21)；loading pressure(21)；legs electrodes(17)；compression displacement(15)；loading pressures(14)；surface leg(14)；upper surface(14)；contacting pairs(14)；hypersonic vehicles(13)；electrical conductivity(13)；contact resistance(12)；silver-epoxy adhesive(11)
- 高频三词短语：electrical contact resistance(10)；upper surface leg(9)；rough surfaces legs(8)；maximum output power(8)；surfaces legs electrodes(7)；output power teg(7)；contacting pairs model(7)；increases ecr decreases(7)；contacting pair composed(6)；pair composed electrode(6)；simulation carried out(6)；loading pressure maximum(6)
- 被动语态估计：97；`we + 动作动词` 主动句估计：0
- 一般现在时线索：191；一般过去时线索：208；现在完成时线索：3；情态动词线索：44

分章节正文词频：

- 1 Introduction: teg(28)；ecr(28)；heat(27)；contact(21)；hypersonic(13)；electrical(12)；electric(12)；legs(12)
- 2 The TEG and material properties of its components: teg(3)；temperature(2)；conductivity(2)；legs(2)；electrodes(2)；will(2)；real(2)；contact(2)
- 3 Two-scale numerical model: contact(19)；electric(13)；contacting(13)；model(13)；surface(13)；pairs(12)；rough(12)；surfaces(11)
- 4 Experimental measurement platform for ECR: test(7)；loading(7)；ecr(5)；wire(5)；resistance(5)；circuit(5)；data(4)；pressures(4)
- 5 Results and discussions: ecr(23)；increases(21)；contact(18)；loading(18)；temperature(17)；pressure(16)；surface(15)；leg(14)
- 6 Conclusion: ecr(10)；loading(7)；teg(6)；electrodes(5)；numerical(4)；experimental(4)；different(4)；pressures(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`For hypersonic vehicles, ... is one of the most critical issues...`
- Gap 句式：`reported research ... rarely considered the influence of ... Thus, this leaves some room for this work.`
- 方法句式：`The whole process contains three steps: first..., second..., third...`
- 图表句式：`Fig. X shows the variation of Y with Z under ...`
- 结果句式：`with the increase of ..., the ... decreases/increases gradually.`
- 验证句式：`The experimental and numerical results have a relatively good agreement.`
- 边界句式：`It should be noted that ... is not considered.`
- 结论句式：`The influence of X on Y cannot be ignored.`

可复用表达策略：少用“novel”堆叠，用“rarely considered”“based on measured practical topography”“validated by a series of measurements”把创新落到可验证动作上。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [2].
  可迁移模板：The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [X].
- 原句：For the influence of the ECR on TEGs, Shittu et al. [43] and Zhang et al. [44] found that it is very important to consider the ECR in the stage of the design and optimization of TEG.
  可迁移模板：For the influence of the METHOD on TEGs, Shittu et al. [X] and Zhang et al. [X] found that it is very important to consider the METHOD in the stage of the design and optimization of METHOD.
- 原句：In addition, for thermoelectric coolers (TECs) with a similar TE conversion process, Su et al. [47] found that both ECR and thermal contact resistances are important for the cooling performance of the TEC.
  可迁移模板：In addition, for thermoelectric coolers (TECs) with a similar METHOD conversion process, Su et al. [X] found that both METHOD and thermal contact resistances are important for the cooling performance of the METHOD.
#### Gap/转折句
- 原句：However, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.
  可迁移模板：However, due to the low working temperature of the substrate material, the use of the film-shaped METHOD materials in hypersonic vehicles is limited.
- 原句：The TE legs and electrodes have micrometer-scale rough surfaces, and such type of roughness will lead to very limited real contact region and a large proportion of contact gap for the contact interface.
  可迁移模板：The METHOD legs and electrodes have micrometer-scale rough surfaces, and such type of roughness will lead to very limited real contact region and a large proportion of contact gap for the contact interface.
#### 方法提出句
- 原句：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography.
  可迁移模板：First, the practical topography of rough surfaces for METHOD legs and electrodes is measured, and the micrometer-scale METHOD prediction numerical models are established based on the reconstructed topography.
- 原句：An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
  可迁移模板：An METHOD measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
- 原句：The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
  可迁移模板：The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
- 原句：Second, the TE conversion process of TEG is simulated by a millimeter-scale model including insulation materials, TE legs, electrodes, and equivalent interfacial layers of ECR.
  可迁移模板：Second, the METHOD conversion process of METHOD is simulated by a millimeter-scale model including insulation materials, METHOD legs, electrodes, and equivalent interfacial layers of METHOD.
- 原句：The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [2].
  可迁移模板：The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [X].
#### 结果呈现句
- 原句：The electric current only flows through the real contact region and the current constriction results into the so-called electrical contact resistance (ECR) which will influence the performance of a TEG.
  可迁移模板：The electric current only flows through the real contact region and the current constriction results into the so-called electrical contact resistance (METHOD) which will influence the performance of a METHOD.
- 原句：The experimental and numerical results have a relatively good agreement with largest differences of 13.2%, 14.9%, 38.9% and 17.7% for “E-N_l”, “E-N_u”, “E-P_l” and “E-P_u”, respectively. 6.
  可迁移模板：The experimental and numerical results have a relatively good agreement with largest differences of X, X, X and X for “E-N_l”, “E-N_u”, “E-P_l” and “E-P_u”, respectively. X.
#### 贡献/增量句
- 原句：In this work, a TEG includes two ceramic substrates and a middle TE layer is established, and the TE layer consists of insulation material, Nand P-type TE legs and electrodes to connect the TE legs.
  可迁移模板：In this work, a METHOD includes two ceramic substrates and a middle METHOD layer is established, and the METHOD layer consists of insulation material, Nand P-type METHOD legs and electrodes to connect the METHOD legs.
- 原句：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography.
  可迁移模板：First, the practical topography of rough surfaces for METHOD legs and electrodes is measured, and the micrometer-scale METHOD prediction numerical models are established based on the reconstructed topography.
- 原句：An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
  可迁移模板：An METHOD measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
- 原句：In this work, a TEG includes two ceramic substrates and a middle TE layer is established, and the TE layer consists of insulation material, Nand P-type TE legs and electrodes to connect the TE legs.
  可迁移模板：In this work, a METHOD includes two ceramic substrates and a middle METHOD layer is established, and the METHOD layer consists of insulation material, Nand P-type METHOD legs and electrodes to connect the METHOD legs.
- 原句：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography.
  可迁移模板：First, the practical topography of rough surfaces for METHOD legs and electrodes is measured, and the micrometer-scale METHOD prediction numerical models are established based on the reconstructed topography.
#### 限制/边界句
- 原句：In traditional design, the vehicle’s structure is insulated from most of the aerodynamic heat by thermal protection systems, whose weight and size could be unaffordable under hypersonic conditions.
  可迁移模板：In traditional design, the vehicle’s structure is insulated from most of the aerodynamic heat by thermal protection systems, whose weight and size could be unaffordable under hypersonic conditions.
- 原句：Thus, new heat management techniques [3] with potential high efficiency should be developed.
  可迁移模板：Thus, new heat management techniques [X] with potential high efficiency should be developed.
- 原句：A TEG should consist of the Nand P-type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
  可迁移模板：A METHOD should consist of the Nand P-type METHOD legs to convert heat into electricity by Seebeck effect, the electrodes to connect METHOD legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
- 原句：However, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.
  可迁移模板：However, due to the low working temperature of the substrate material, the use of the film-shaped METHOD materials in hypersonic vehicles is limited.
- 原句：The TE legs and electrodes have micrometer-scale rough surfaces, and such type of roughness will lead to very limited real contact region and a large proportion of contact gap for the contact interface.
  可迁移模板：The METHOD legs and electrodes have micrometer-scale rough surfaces, and such type of roughness will lead to very limited real contact region and a large proportion of contact gap for the contact interface.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用密度最高在 Introduction。作者先用高超声速热管理与 TEG 应用文献建立问题重要性，再用 TE 材料文献证明材料选择合理，随后集中引用 ECR 理论、实验和数值预测文献，最后引用 ECR 对 TEG/TEC 性能影响的研究来铺垫本文必要性。

引用姿态以继承和补充为主，批判较温和。作者不直接否定前人，而说已有模型“adopted some assumptions”或高超声速 TEG “rarely considered” ECR。这种写法适合工程应用论文：避免过度对立，同时明确留白。

gap 与引用的连接方式是：已有 TEG 应用证明重要性；已有 ECR 研究证明问题存在；已有 ECR 影响研究证明后果严重；但高超声速 TEG 真实界面缺验证模型，所以本文进入。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：86
- Introduction 引文簇数量估计：33
- References 条目数：51
- 可识别年份条目数：86
- 2021 年及以后文献数：25
- 2010 年前经典文献数：6
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Aerospace Science and Technology(2)
- 引文簇样例：[1], [2], [3], [12], [7], [13,14], [28], [15], [29], [19], [20], [21,22]

带引文的 gap/转折句样例：

- Besides, Kim [46] found that the ECR has a notable impact on TEGs with short length of TE legs.

References 解析样例（前 8 条）：

- 3. For the N-type Yb0.29Co4Sb12, the absolute value of the Seebeck coefficient increases, while the electrical conductivity and thermal conductivity decrease with the increase of temperature. The ranges of the Seebeck coefficient, electrical conductivity and thermal conductivity of Yb0.29Co4Sb12 are −164.1 to −117.2 μV/K, 68.5 to 80.7 S/mm and 2.2 to 2.5 W/(m·K) with the temperature increasing from 325 to 725 K, respectively. For the P-type La0.1Ce0.8Fe3CoSb12, the Seebeck coefficient increases and the electrical conductivity decreases with the temperature increases from 325 to 625 K, while the Seebeck coefficient decreases and the electrical conductivity increases with the temperature increases from 675 to 725 K. The thermal conductivity changes little in the whole temperature range. The ranges of the Seebeck coefficient, electrical conductivity and thermal conductivity of La0.1Ce0.8Fe3CoSb12 are 83.3 to 115.0 μV/K, 47.2 to 65.8 S/mm, 1.01 to 1.15 W/(m·K), respectively. As shown in Table 1, the density, elastic modulus, Poisson’s ratio and specific heat capacity of the Yb0.29Co4Sb12 are 6.9 g/cm3, 57.1 GPa, 0.23
G. Gao, D. Li, J.-J. Gou et al. Aerospace Science and Technology 131 (2022) 107966
Fig. A-
- 3. Seebeck coefficient, thermal and electrical conductivity of TE materials.
and 235 J/(kg·K), respectively; and that for the La0.1Ce0.8Fe3CoSb12 are 7.6 g/cm3, 33.3 GPa, 0.24 and 243 J/(kg·K), respectively.
References
- [1] K. An, Z yun Guo, X ping Xu, W Huang, A framework of trajectory design and optimization for the hypersonic gliding vehicle, Aerosp. Sci. Technol. 106 (2020) 106110, https://doi .org /10 .1016 /j .ast .2020 .106110.
- [2] W. Chen, R. Wang, X. Li, S. Lu, X. Fang, Study of the heat transfer design of an integrated thermal management system for hypersonic vehicles using supercritical nitrogen as expendable coolant, Aerosp. Sci. Technol. 123 (2022) 107440, https://doi .org /10 .1016 /j .ast .2022 .107440.
- [3] P. Fernández-Yáñez, V. Romero, O. Armas, G. Cerretti, Thermal management of thermoelectric generators for waste energy recovery, Appl. Therm. Eng. (2021) 196, https://doi .org /10 .1016 /j .applthermaleng .2021.117291.
- [4] G. Gao, J.J. Gou, C.L. Gong, J.X. Hu, R.C. Gao, A novel mechanical-thermalelectrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962, https://doi .org /10 .1016 /j .compstruct .2021.113962.
- [5] K. Cheng, J. Qin, H. Sun, C. Dang, S. Zhang, X. Liu, et al., Performance assessment of an integrated power generation and refrigeration system on hypersonic vehicles, Aerosp. Sci. Technol. 89 (2019) 192–203, https://doi .org /10 . 1016 /j .ast .2019 .04 .006.
- [6] K. Cheng, J. Qin, Y. Jiang, C. Lv, S. Zhang, W. Bao, Performance assessment of multi-stage thermoelectric generators on hypersonic vehicles at a large temperature difference, Appl. Therm. Eng. 130 (2018) 1598–1609, https:// doi .org /10 .1016 /j .applthermaleng .2017.11.057.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 实验验证温度主要在 298 K 和有限压力下，仿真拓展到 325-725 K 的可信度依赖材料参数与模型假设。
2. E-P_l 最大实验-数值差异 38.9%，虽然作者解释污染膜/氧化膜，但模型未纳入这一机制。
3. 闭合接触单元 perfect contact、污染膜不计、间隙介质理想化，可能低估真实 ECR。
4. 只讨论 ECR 对 TEG 电性能影响，没有与 TCR、热辐射、机械热循环等联立。
5. 银环氧胶作为缓解方案，需要耐高温、热膨胀失配、老化、脱粘等长期可靠性评估。
6. 冷源 kerosene 只是设定，没有展开燃油冷却系统边界，系统级应用仍是局部模型。

## 17. 可复用资产

- 选题套路：从宏观工程系统中挑一个被理想化忽略的界面非理想因素，证明其对系统性能有数量级影响。
- 方法套路：真实形貌测量 → 微尺度接触模型 → 实验验证 → 宏观等效层 → 系统性能降额。
- 证据套路：先机制云图，再参数曲线，再实验对比表，最后系统级性能图。
- 图表套路：用 Fig. 19-21 把局部界面电阻变成 TEG 内阻和输出功率，避免停留在局部现象。
- 写法套路：每一小节用 “As shown in Fig.” 展示，再用 “In short” 收束规律。

## 18. 对我写论文的启发

如果我的论文想研究工程系统中的局部界面/连接/接触问题，可以学习本文的“局部参数系统化”方法：不要只证明局部现象存在，而要把它等效进入整体模型，并用整体性能指标证明其不可忽略。

Introduction 可借鉴其渐进收束：大工程痛点不必展开太久，尽快进入具体部件和界面。Results 可借鉴其层层递进：几何/力学证据解释为什么有接触电阻，电学证据量化接触电阻，系统证据说明工程后果。

## 19. 最终浓缩

本文最值得学习的是把 ECR 这个微尺度接触问题写成了高超声速 TEG 设计必须考虑的系统级问题。最强证据是空气间隙下最大输出功率降低约 83%，最强写作资产是“两尺度模型 + 实验验证 + 等效界面层”的论证链。最大风险是高温、污染膜、热循环和热接触效应尚未完全纳入，适合与后续 TCR/NFTR 工作联读。
