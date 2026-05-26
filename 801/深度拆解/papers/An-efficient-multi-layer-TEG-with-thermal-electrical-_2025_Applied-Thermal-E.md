## 0. 读取说明

本文依据 `801/文本/txt/An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E.txt` 的全文抽取进行拆解。抽取文本包含摘要、引言、结构模型、粗糙接触模型、TEG 尺寸优化、火星 RTG 系统设计、实验验证、敏感性分析和结论，足以支撑深度拆解。由于原文有大量图示、截面、粗糙表面重构图和温度/电势云图，本文对无法从文本确认的图像细节标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The multi-layer TEG for Mars RTG, 3 Numerical models for interfaces and TEG, 4 Fabrication of TEG and the experimental test, 5 Results and discussions, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：An efficient multi-layer TEG with thermal-electrical interfaces for Mars rover RTGs
- 期刊：Applied Thermal Engineering, 280 (2025) 128383
- 作者：Shi-Yuan Chen, Xiao-Bing Ma, Jian-Jun Gou, Ge Gao, Chun-Lin Gong
- 机构：Northwestern Polytechnical University, Beijing Institute 等
- 关键词：Thermoelectric generator; Radioisotope power supply; Thermal contact resistance; Electrical contact resistance; Martian environment

论文身份是面向火星车放射性同位素热电发电系统的“结构-接触-系统一体化优化”论文。它不是只做单个热电臂材料性能分析，而是把多层热电材料匹配、热/电接触界面、火星大气环境、RTG 散热结构和重量功率密度目标串成一条工程设计链。

## 2. 摘要与核心信息提取

摘要的核心叙事是：现有 RTG 热电转换效率偏低，单层 TEG 难以覆盖宽温差；多层 TEG 能匹配不同温区材料，但大量界面引入热接触电阻和电接触电阻；火星大气既非真空也非地球空气，其接触传热/导电效应需要专门建模；因此本文提出带热-电界面的多层 TEG 设计与优化方法，并在 RTG 系统层面展示效率提升。

核心信息包括：

1. 多层结构：高温、中温、低温热电材料串联，利用不同材料温区优势。
2. 接触建模：粗糙尺度上计算 TCR/ECR，TEG 尺度上等效为附加界面层。
3. 环境设定：比较真空、火星、地球空气和银胶界面，突出火星稀薄 CO2 环境的特殊性。
4. 优化目标：最大化 TEG gravimetric power density，同时满足温度和结构约束。
5. 系统结果：优化后火星环境 TEG 效率 8.444%；RTG 系统设计效率 7.189%，高于传统 mmRTG 类水平。

一句话浓缩：本文试图把“多层热电材料的温区匹配优势”从理想模型推进到含真实界面和火星环境的 RTG 工程设计。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E.md`。

中文译文：

> 放射性同位素是火星探测最有前途的供电技术，而热电发电机（TEG）是将同位素衰变产生的热量转化为电能的关键部件。然而，当前 TEG 的关键缺点是由于热电 (TE) 材料的工作温度范围有限而导致转换效率低。在这项工作中，由高、中、低温TE材料组成的多层TEG被配制为每层的最佳操作条件，以提高转换效率。建立了两尺度接触模型来阐明多层之间的热电界面效应。在粗糙度尺度上，对界面火星大气间隙下的热接触电阻和电接触电阻进行了数值计算，并与真空、地球大气和银环氧树脂粘合剂下的热接触电阻和电接触电阻进行了比较，阐明了压力和温度的影响，并对数值结果进行了实验验证。在 TEG 尺度中，接触效应相当于附加层，并在结构优化中考虑，目标是在典型同位素衰变热条件下获得最大重量功率密度。制作了一个典型的 TEG，并通过实验测量电压验证了数值模型。
>
> 最终得到适合火星环境的最优TEG，转换效率为8.444%。目前TEG技术的主要局限性是转换效率相对较低，在火星探测工程中应用的转换效率通常低于6%。然而，对于最新的RTG，即毅力号火星车中的RTG，TE转换效率仍然低于6.3％，7％是NASA下一代RTG的目标效率[13]。因此，发明高转换效率的TEG已成为紧迫的研究重点。在传统TEG的设计和应用中，广泛使用单层TE结构[14-20]。然而，大多数TE材料都有明确的最佳工作温度，因此这种单层结构的工作温度范围有限，并且性能在一定程度上较弱，逐渐无法满足日益增长的性能需求。每层具有适当温度范围的多层结构TEG往往会表现出更好的性能[21-24]。因此，本文在火星环境下创新创建了多层TEG，并以最大重力功率密度为目标优化尺寸，以实现更高的输出功率和TE转换效率。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题的现实入口很强：火星车需要长期、稳定、不依赖太阳光的电源，RTG 是核心方案；但传统 RTG 热电转换效率通常低于 6%-7%，直接限制系统质量、热源规模和任务能力。NASA 对更高效率放射性同位素电源存在明确需求。

技术矛盾有两层。第一层是材料温区矛盾：单一热电材料只在有限温度区间具有较优 ZT，高温热源到低温散热端的宽温差难以被单材料充分利用。多层 TEG 可以让高温、中温、低温材料分别工作在适合区间。第二层是界面矛盾：多层意味着更多电极、材料、基底和绝缘界面，而接触热阻和电阻会吞噬理想性能。多层越复杂，界面损失越不能忽略。

文章选题的关键切入点就是第二层矛盾。很多热电优化论文会把界面当成简化参数或忽略项，但本文把界面本身作为主角，尤其加入火星低压 CO2 环境下接触间隙传热和电接触效应。这使选题从普通 TEG 尺寸优化升级为“火星环境下的真实界面多层 TEG 设计”。

## 4. 领域位置与文献版图

领域版图可以分为四块：

第一块是 RTG 和空间放射性同位素电源。这里的文献用于说明传统 RTG 效率瓶颈、火星车任务需求和 238PuO2 热源选择。

第二块是多层或分段式热电发电器。文献强调材料在不同温区的性能差异，以及通过高/中/低温材料组合提升热电转换效率的基本逻辑。

第三块是热/电接触阻力。该部分涉及粗糙表面真实接触面积、界面气体导热、压力与温度对接触阻力的影响。本文把 TCR/ECR 同时纳入，而不是只考虑热阻。

第四块是系统级 RTG 热设计，包括散热翅片、热源衰减、火星尘埃和火星外部换热条件。本文把 TEG 子模块结果进一步放到 RTG 系统中比较，使论文不止停留在器件层。

## 5. Gap 制造机制

本文的 gap 由“理想多层 TEG 设计”与“真实火星界面运行”之间的落差构成。

作者首先指出现有 RTG 低效率与多层 TEG 的潜力，然后转向多层结构的副作用：界面数量急剧增加。若忽略 TCR/ECR，优化出来的结构会高估输出功率和效率。抽取文本显示，理想无接触模型的 TEG 为 3.126 W/kg、7.957%，而考虑火星接触后降至 1.192 W/kg、3.033%，性能下降约 61.89%。这个结果本身就把 gap 数字化：界面不是小修正，而是决定性因素。

第二个 gap 是环境特异性。真空、地球空气、火星低压 CO2 和银胶界面之间的等效导热/导电差异明显，直接套用真空或地球空气接触模型会偏离火星任务真实状态。

因此本文的 gap 可以表述为：多层 TEG 被认为能提升 RTG 效率，但缺少一个同时考虑火星稀薄大气、粗糙接触热阻/电阻和系统重量功率密度的优化模型。

## 6. 创新性判断

创新性主要体现在工程模型完整度和跨尺度耦合。

较强创新点：

- 建立火星大气环境下粗糙接触尺度的 TCR/ECR 模型，并与真空、地球空气、银胶界面进行比较。
- 将粗糙尺度接触效应等效为 TEG 尺度的附加界面层，实现从微观粗糙度到器件性能的耦合。
- 面向火星 RTG 建立高/中/低温多层 TEG，并以 gravimetric power density 为优化目标。
- 将优化 TEG 集成到 RTG 系统设计中，比较翅片、尘埃、发射率和传统 RTG 指标。

中等创新点：

- 采用 Nelder-Mead 在 COMSOL 框架内优化热电臂高度和直径。
- 用实验测得电压、TCR 和 ECR 对模型进行多层次验证。

创新边界：

- 热电材料组合只测试一种高/中/低温方案。
- 优化变量主要是几何尺寸，材料选择、层数、拓扑和电连接方式没有系统搜索。
- RTG 系统假设热源功率恒定，未充分考虑同位素衰减长期影响。

## 7. 论证链条复原

全文论证链可以拆成九步：

1. 火星车 RTG 需要更高效率和更高重量功率密度。
2. 单层 TEG 温区匹配不足，多层 TEG 理论上能提高宽温差利用率。
3. 多层 TEG 引入大量热-电接触界面，接触损失会显著降低实际输出。
4. 火星环境下界面间隙气体为低压 CO2，不能简单等同于真空或地球空气。
5. 通过粗糙表面重构和接触力学/传热/导电模型计算不同界面的 TCR/ECR。
6. 将 TCR/ECR 等效为 TEG 尺度附加层，评估理想、真空、地球、火星、银胶条件下的性能差异。
7. 在考虑火星接触效应的前提下优化多层 TEG 几何尺寸，获得更高 GPD 和效率。
8. 将优化 TEG 放入 RTG 系统，设计散热翅片并检验尘埃/发射率敏感性。
9. 通过 TCR/ECR 与输出电压实验验证模型合理性。

这条链条的关键是：先证明界面效应足够大，再证明在考虑界面后仍可通过结构优化实现效率提升。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 已有研究不足/GAP：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials. However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13]. However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 本文解决方式：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. A typical TEG is fabricated and the numerical model is validated by the experimental measured voltage. The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
- 学术或工程增量：In this work, a multi-layer TEG consists of high-, midand lowtemperature TE materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency. Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency. In this work, a multi-layer TEG consists of high-, mid- and lowtemperature TE materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法可以按尺度分为三层。

粗糙界面尺度：作者用 W-M 分形模型重构基底、电极、热电腿等粗糙表面。文本给出 measured Ra 与 reconstructed Ra 的对比：基底、电极、TE 腿分别约 4.107、3.215、1.799 μm，重构后偏差约 7.18%、4.20%、6.44%。在此基础上计算真实接触面积、气体间隙导热、固体接触导热和电接触阻力。压力增大使真实接触面积增加，从而降低 TCR/ECR。

TEG 器件尺度：多层 TEG 包括高温、中温和低温热电材料层，每层包含电极、N/P 热电腿、基底或绝缘界面。界面效应通过等效热导率、电导率和附加层厚度进入 COMSOL 多物理场模型。单个 TEG 截面为 50 mm x 50 mm，优化变量为 `XCE=[h1,h2,h3,d]`，即三层热电腿长度和直径。

RTG 系统尺度：热源为 238PuO2，冷端通过翅片向火星环境散热。系统设计需要同时考虑热源输入、TEG 输出、散热翅片尺寸、尘埃带来的热阻增加和表面发射率衰减。最终系统含 72 个多层 TEG，设计输出约 107.8 W。

优化目标是最大化 `varpi=Poutput/MTEGtotal`，约束包括 Al 壳温度不超过 570 K，高/中/低温材料热端温度不超过 1300/900/650 K。算法使用 Nelder-Mead，搜索范围为 h1/h2/h3 5-20 mm，d 5-10 mm。

## 9. 证据系统与 Claim-Evidence 表

| Claim | Evidence | 论证功能 | 潜在限制 |
|---|---|---|---|
| 火星界面接触效应不能忽略 | 无接触理想 TEG 为 3.126 W/kg、7.957%；火星接触条件下降至 1.192 W/kg、3.033%，效率下降约 61.89% | 将界面建模从细节提升为核心问题 | 依赖接触模型和表面粗糙度设定 |
| 火星环境与真空/地球空气不同 | S-E 等效导热率：真空约 1.412-1.522，火星约 1.689-2.623，地球约 1.878-2.666 W/mK，银胶约 53.11-53.41 W/mK | 证明不能直接套用常规界面条件 | 不同压力、温度区间外需再验证 |
| 压力增加会降低 TCR/ECR | S-E TCR 在 261.0-923.6 K 下由 2.961e-4 降至 1.906e-4 K m2/W；E-TE-M ECR 也随压力从 1.201 到 3.041 MPa 降低 | 支撑接触模型的物理合理性 | 压力加载和实际装配工艺对应关系需复核 |
| 银胶可显著改善界面性能 | 银胶条件输出 0.1333 W、3.232 W/kg、8.223%，相对真空/地球/火星输出提升约 181.5%/177.3%/177.7% | 展示界面工程对性能的巨大影响 | 空间长期稳定性和高温兼容性需额外论证 |
| 考虑火星接触后优化仍能达到高效率 | 54 次迭代后 h1=5.76、h2=15.0、h3=7.62、d=7.25 mm，GPD 3.514 W/kg，效率 8.444% | 证明模型不只是揭示损失，也能指导改进 | 优化变量有限，局部最优风险 |
| RTG 系统级效率优于传统方案 | 设计 RTG 输入 1500 W、输出 107.8 W、效率 7.189%；对比 mmRTG 约 6.3%、MHW-RTG 6.5%、GPHS-RTG 6.7% | 将器件优化价值延伸到系统层 | 传统系统对比需统一任务条件和质量口径 |
| 模型有实验支撑 | TCR 最大偏差约 -14.5%/15.4%，ECR 修正氧化膜后最大偏差约 -3.51%/4.81%，输出电压最大差异约 -11.7% 和 -12.1% | 降低纯仿真模型的不确定性 | 电压差异仍不小，装配缺陷影响明显 |

## 10. 图表、公式与结果叙事提取

| 类型 | 内容 | 论证功能 | 复核备注 |
|---|---|---|---|
| RTG/TEG 结构图 | 热源、TEG、散热翅片、单层/多层 TEG 截面 | 展示工程对象和多层界面来源 | 需要 PDF 图像复核 |
| 火星环境参数表/图 | Mars 190-300 K、低压 CO2、对流系数约 1.24-2.4 W/Km2 | 说明界面与外部换热边界 | 单位和条件需按 PDF 核对 |
| 粗糙表面重构图 | 基底、电极、热电腿的 W-M 表面和 Ra 对比 | 证明接触模型输入来自可测粗糙度 | 需要 PDF 图像复核 |
| TCR 公式 Eq. 15 | 接触热阻计算 | 将压力、温度、气体环境映射到热阻 | 公式符号需 PDF 核对 |
| ECR 公式 Eq. 17 | 接触电阻计算 | 将真实接触面积和材料电性映射到电阻 | 公式符号需 PDF 核对 |
| 等效层公式 Eq. 18/19 | 将微观 TCR/ECR 转换为器件尺度附加层 | 打通粗糙尺度与 TEG 仿真 | 公式编号需核对 |
| 接触压力/真实面积结果图 | 高温腿位移、压力、真实接触面积变化 | 解释 TCR/ECR 随压力降低的机理 | 需要 PDF 图像复核 |
| TCR/ECR 对比图 | 真空、火星、地球、银胶条件下的界面阻力 | 支撑环境差异主张 | 需要 PDF 图像复核 |
| TEG 性能表 | 无接触、真空、地球、火星、银胶输出功率/GPD/效率 | 量化界面对器件性能的影响 | 数值来自文本抽取 |
| 优化迭代结果 | 54 次迭代，几何变量收敛到最优组合 | 证明优化过程有效 | 收敛曲线需要 PDF 图像复核 |
| RTG 系统比较表 | 设计 RTG 与 mmRTG、MHW-RTG、GPHS-RTG 对比 | 将器件贡献转为系统贡献 | 质量和边界条件口径需复核 |
| 实验验证图/表 | TCR/ECR 和输出电压与实验对比 | 支撑模型可信度 | 实验装置细节需要 PDF 图像复核 |

结果叙事的关键安排是：先对界面进行物理建模和环境比较，再展示界面造成的巨大性能衰减，随后用优化把性能追回，最后上升到 RTG 系统级指标。

## 11. 章节结构与篇章布局

文章结构大致为：

1. Introduction：RTG 低效率、多层 TEG 潜力、界面阻力和火星环境 gap。
2. Multi-layer TEG and Martian RTG configuration：定义热源、TEG 结构、材料和环境边界。
3. Thermal-electrical interface model：粗糙表面重构、TCR/ECR 计算和等效层转换。
4. TEG-scale numerical model and optimization：器件仿真、变量、约束、目标和优化算法。
5. Results and discussion：接触阻力、不同环境性能、优化结果、敏感性和系统设计。
6. Experimental validation：TCR/ECR/电压验证。
7. Conclusions：回收界面重要性、多层优化性能和系统效率。

这是一种“模型层层上推”的布局：微观界面 -> 器件 -> RTG 系统。每一层都有对应证据，避免只在单一尺度上自洽。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The multi-layer TEG for Mars RTG（对象/模块/过渡章节）
  - L3 p.3: 2.1 The RTG and Martian environment（对象/模块/过渡章节）
  - L3 p.4: 2.2 The radioisotope heat source of TEG（对象/模块/过渡章节）
  - L3 p.5: 2.3 The multi-layer TEG and structural optimization model（方法/模型/算法）
- L2 p.7: 3 Numerical models for interfaces and TEG（方法/模型/算法）
  - L3 p.7: 3.1 Governing equations（对象/模块/过渡章节）
  - L3 p.8: 3.2 Interfaces reconstruction and TCR, ECR calculations（对象/模块/过渡章节）
  - L3 p.9: 3.3 Roughness-scale contact model（方法/模型/算法）
  - L3 p.10: 3.4 TEG-scale contact model（方法/模型/算法）
- L2 p.13: 4 Fabrication of TEG and the experimental test（结果/验证/讨论）
  - L3 p.13: 4.1 Fabrication of TEG（对象/模块/过渡章节）
  - L3 p.13: 4.2 Measurement of TCR and TEG output voltage（对象/模块/过渡章节）
  - L3 p.14: 4.3 Measurement of ECR（对象/模块/过渡章节）
- L2 p.17: 5 Results and discussions（结果/验证/讨论）
  - L3 p.17: 5.1 The TE transfer and conversion processes（对象/模块/过渡章节）
    - L4 p.17: 5.1.1 Contact deformation（对象/模块/过渡章节）
    - L4 p.17: 5.1.2 Heat transfer and electrical conduction（对象/模块/过渡章节）
    - L4 p.18: 5.1.3 The TCR and ECR under different clearances（对象/模块/过渡章节）
  - L3 p.19: 5.2 The multi-layer TEG and performance（对象/模块/过渡章节）
    - L4 p.19: 5.2.1 The influence of contact effects under different clearances（对象/模块/过渡章节）
    - L4 p.20: 5.2.2 The performance of multi-layer TEG under Martian atmosphere（对象/模块/过渡章节）
    - L4 p.22: 5.2.3 The performance of radioisotope power supply（对象/模块/过渡章节）
  - L3 p.23: 5.3 The comparison of simulation and experimental measurement（结果/验证/讨论）
    - L4 p.23: 5.3.1 Measured and numerically calculated TCRs and ECRs（对象/模块/过渡章节）
    - L4 p.24: 5.3.2 Measured and numerically calculated output voltage of TEG sample（对象/模块/过渡章节）
- L2 p.24: 6 Conclusion（结论/贡献回收）
- L2 p.25: Declaration of competing interest（尾部材料）
- L2 p.25: Data availability（尾部材料）
- L2 p.25: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The multi-layer TEG for Mars RTG | 3 | 2 | 对象/模块/过渡章节 |
| 2.1 The RTG and Martian environment | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 The radioisotope heat source of TEG | 4 | 3 | 对象/模块/过渡章节 |
| 2.3 The multi-layer TEG and structural optimization model | 5 | 3 | 方法/模型/算法 |
| 3 Numerical models for interfaces and TEG | 7 | 2 | 方法/模型/算法 |
| 3.1 Governing equations | 7 | 3 | 对象/模块/过渡章节 |
| 3.2 Interfaces reconstruction and TCR, ECR calculations | 8 | 3 | 对象/模块/过渡章节 |
| 3.3 Roughness-scale contact model | 9 | 3 | 方法/模型/算法 |
| 3.4 TEG-scale contact model | 10 | 3 | 方法/模型/算法 |
| 4 Fabrication of TEG and the experimental test | 13 | 2 | 结果/验证/讨论 |
| 4.1 Fabrication of TEG | 13 | 3 | 对象/模块/过渡章节 |
| 4.2 Measurement of TCR and TEG output voltage | 13 | 3 | 对象/模块/过渡章节 |
| 4.3 Measurement of ECR | 14 | 3 | 对象/模块/过渡章节 |
| 5 Results and discussions | 17 | 2 | 结果/验证/讨论 |
| 5.1 The TE transfer and conversion processes | 17 | 3 | 对象/模块/过渡章节 |
| 5.1.1 Contact deformation | 17 | 4 | 对象/模块/过渡章节 |
| 5.1.2 Heat transfer and electrical conduction | 17 | 4 | 对象/模块/过渡章节 |
| 5.1.3 The TCR and ECR under different clearances | 18 | 4 | 对象/模块/过渡章节 |
| 5.2 The multi-layer TEG and performance | 19 | 3 | 对象/模块/过渡章节 |
| 5.2.1 The influence of contact effects under different clearances | 19 | 4 | 对象/模块/过渡章节 |
| 5.2.2 The performance of multi-layer TEG under Martian atmosphere | 20 | 4 | 对象/模块/过渡章节 |
| 5.2.3 The performance of radioisotope power supply | 22 | 4 | 对象/模块/过渡章节 |
| 5.3 The comparison of simulation and experimental measurement | 23 | 3 | 结果/验证/讨论 |
| 5.3.1 Measured and numerically calculated TCRs and ECRs | 23 | 4 | 对象/模块/过渡章节 |
| 5.3.2 Measured and numerically calculated output voltage of TEG sample | 24 | 4 | 对象/模块/过渡章节 |
| 6 Conclusion | 24 | 2 | 结论/贡献回收 |
| Declaration of competing interest | 25 | 2 | 尾部材料 |
| Data availability | 25 | 2 | 尾部材料 |
| References | 25 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

引言段落先用任务需求拉开问题，再用传统 RTG 低效率制造紧迫感，随后引入多层 TEG 作为潜在方案。接着转向界面损失，这是本文真正的新问题。

方法段落偏密集，常用“first/then/finally”式的构建方式。粗糙尺度模型中，段落功能是从表面参数到真实接触面积，再到 TCR/ECR；器件尺度模型中，段落功能是从结构、材料、边界到优化变量。

结果段落节奏明显：先解释接触压力和真实面积的物理趋势，再比较不同环境下 TCR/ECR，然后展示对 TEG 输出的影响。后半部分转向“工程可用性”：优化、敏感性、散热翅片、尘埃和传统 RTG 对比。

## 13. 文笔画像与语言习惯

本文文风是典型 Applied Thermal Engineering 风格：工程对象具体、模型堆叠较多、结果数值密集。语言偏重 “considering”, “influence”, “effect”, “optimization”, “validation”。

常见写法：

- “The effects of thermal and electrical contact resistances are considered...”
- “The equivalent layer method is adopted to...”
- “The gravimetric power density is selected as the optimization objective...”
- “Compared with the case without contact resistance...”
- “The proposed design shows a higher conversion efficiency than...”

文章喜欢用百分比下降/提升表达工程意义，例如效率下降 61.89%、银胶输出提升 177%-181%、尘埃导致 GPD 轻微下降。这种写法让复杂多物理仿真结果更易被审稿人抓住。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：57984
- 高频词：teg(87)；power(83)；temperature(80)；heat(78)；atmosphere(68)；contact(67)；thermal(64)；interfacial(62)；clearance(60)；martian(46)；tcr(45)；conversion(40)；conductivity(39)；ecr(39)；density(37)；output(36)；efficiency(34)；contacting(34)；radioisotope(31)；electrical(30)
- 高频名词化/学术名词：temperature(80)；clearance(60)；conversion(40)；conductivity(39)；density(37)；pressure(28)；resistance(27)；performance(23)；optimization(15)；environment(15)；measurement(14)；exploration(11)；conduction(11)；insulation(11)；difference(10)
- 高频学术动词：compared(11)；validated(6)；provide(5)；developed(4)；evaluate(3)；indicate(3)；optimized(2)；achieve(1)；predict(1)；estimated(1)；revealed(1)；indicated(1)；constructed(1)；analyze(1)；predicted(1)
- 高频形容词：thermal(64)；interfacial(62)；electrical(30)；adhesive(29)；equivalent(24)；gravimetric(23)；material(19)；optimal(15)；environment(15)；potential(15)；measurement(14)；coefficient(11)；thermoelectric(10)；numerical(10)；experimental(10)
- 高频副词：supply(19)；numerically(7)；slightly(6)；primarily(4)；experimentally(4)；relatively(4)；widely(3)；mainly(3)；effectively(3)；substantially(3)；significantly(3)；directly(2)；finally(2)；gradually(2)；indirectly(2)
- 高频二词短语：martian atmosphere(32)；thermal conductivity(30)；power density(29)；conversion efficiency(27)；output power(26)；earth atmosphere(25)；silver-epoxy adhesive(23)；gravimetric power(23)；contact effects(20)；interfacial contact(19)；loading pressure(19)；power supply(18)
- 高频三词短语：gravimetric power density(23)；interfacial contact effects(16)；average interfacial temperature(15)；silver-epoxy adhesive clearance(11)；radioisotope power supply(10)；power density conversion(9)；density conversion efficiency(9)；vacuum earth atmosphere(8)；atmosphere silver-epoxy adhesive(8)；earth atmosphere martian(8)；equivalent interfacial layers(7)；equivalent thermal conductivity(6)
- 被动语态估计：143；`we + 动作动词` 主动句估计：0
- 一般现在时线索：317；一般过去时线索：268；现在完成时线索：0；情态动词线索：26

分章节正文词频：

- 1 Introduction: teg(24)；contact(20)；temperature(19)；tcr(14)；conversion(13)；thermal(13)；interfacial(12)；heat(11)
- 2 The multi-layer TEG for Mars RTG: heat(32)；power(25)；teg(22)；density(15)；legs(14)；radioisotope(14)；carbon(14)；temperature(13)
- 3 Numerical models for interfaces and TEG: thermal(23)；contact(20)；surface(17)；conductivity(17)；interfacial(16)；equivalent(16)；electrical(13)；heat(11)
- 4 Fabrication of TEG and the experimental test: voltage(12)；temperature(11)；resistance(8)；electrodes(7)；test(7)；teg(6)；legs(6)；heat(6)
- 5 Results and discussions: atmosphere(40)；power(36)；clearance(32)；temperature(25)；teg(24)；tcr(20)；efficiency(20)；interfacial(19)
- 6 Conclusion: atmosphere(10)；teg(8)；power(8)；interfacial(8)；martian(6)；decreases(6)；contact(5)；vacuum(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用关键词：

- multi-layer thermoelectric generator
- radioisotope thermoelectric generator
- thermal contact resistance
- electrical contact resistance
- Martian atmosphere
- equivalent interface layer
- gravimetric power density
- segmented thermoelectric materials
- rough surface reconstruction
- thermal-electrical coupling

可复用句式：

- “The interface effect is not a secondary correction but a dominant factor in the practical performance of the multi-layer TEG.”
- “To bridge the roughness-scale contact model and the TEG-scale simulation, the contact resistances are converted into equivalent interface layers.”
- “The Martian atmosphere cannot be simply treated as vacuum or Earth air because the dilute CO2 in the contact gap changes the interfacial heat transfer.”
- “The optimization is carried out under temperature constraints of the shell and thermoelectric materials.”
- “The system-level comparison indicates that the gain at the device level can be translated into a higher RTG conversion efficiency.”

中文可复用表达：

- “多层结构带来的温区匹配收益与界面损失之间存在天然拉扯。”
- “界面建模的价值在于把理想热电性能拉回装配和环境约束下的真实性能。”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover.
  可迁移模板：The Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover.
- 原句：However, the development of efficient TEGs for Mars exploration requires accurate quantification of the TCR and ECR under interfacial Martian atmosphere clearance.
  可迁移模板：However, the development of efficient TEGs for Mars exploration requires accurate quantification of the METHOD and METHOD under interfacial Martian atmosphere clearance.
#### Gap/转折句
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  可迁移模板：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (METHOD) materials.
- 原句：However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].
  可迁移模板：However, for the latest METHOD, i.e., METHOD in Perseverance Mars rovers, the METHOD conversion efficiency is still lower than X, and X is the target efficiency for METHOD’s next-generation METHOD [X].
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
  可迁移模板：However, most of the METHOD material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  可迁移模板：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (METHOD) materials.
- 原句：However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].
  可迁移模板：However, for the latest METHOD, i.e., METHOD in Perseverance Mars rovers, the METHOD conversion efficiency is still lower than X, and X is the target efficiency for METHOD’s next-generation METHOD [X].
#### 方法提出句
- 原句：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
  可迁移模板：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
- 原句：A typical TEG is fabricated and the numerical model is validated by the experimental measured voltage.
  可迁移模板：A typical METHOD is fabricated and the numerical model is validated by the experimental measured voltage.
- 原句：The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
  可迁移模板：The multi-layer structure METHOD with appropriate temperature range for each layer tends to present better performance [X–X].
- 原句：At present, the radioisotope thermoelectric generator (RTG) is widely utilized in more than 50 deep-space exploration missions of NASA, e.g., the Voyager [1], Galileo [2], Cassini [3], Curiosity [4] and Perseverance [5].
  可迁移模板：At present, the radioisotope thermoelectric generator (METHOD) is widely utilized in more than Xdeep-space exploration missions of METHOD, e.g., the Voyager [X], Galileo [X], Cassini [X], Curiosity [X] and Perseverance [X].
- 原句：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
  可迁移模板：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
#### 结果呈现句
- 原句：In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated.
  可迁移模板：In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated.
- 原句：Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
  可迁移模板：Therefore, in this paper, a multi-layer METHOD is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and METHOD conversion efficiency.
- 原句：All RTGs in these missions show great power-supply performance.
  可迁移模板：All RTGs in these missions show great power-supply performance.
- 原句：In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated.
  可迁移模板：In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated.
- 原句：Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
  可迁移模板：Therefore, in this paper, a multi-layer METHOD is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and METHOD conversion efficiency.
#### 贡献/增量句
- 原句：In this work, a multi-layer TEG consists of high-, midand lowtemperature TE materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency.
  可迁移模板：In this work, a multi-layer METHOD consists of high-, midand lowtemperature METHOD materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency.
- 原句：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
  可迁移模板：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
- 原句：In this work, a multi-layer TEG consists of high-, midand lowtemperature TE materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency.
  可迁移模板：In this work, a multi-layer METHOD consists of high-, midand lowtemperature METHOD materials is formulated with optimal operating conditions for each layer to improve the conversion efficiency.
- 原句：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
  可迁移模板：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
- 原句：Li et al. [37] estimated the TCR and ECR under difference clearance mediums of air, graphene sheet and thermal grease, and revealed that the TEG system delivered better performance at relatively low TCR and ECR.
  可迁移模板：Li et al. [X] estimated the METHOD and METHOD under difference clearance mediums of air, graphene sheet and thermal grease, and revealed that the METHOD system delivered better performance at relatively low METHOD and METHOD.
#### 限制/边界句
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  可迁移模板：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (METHOD) materials.
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
  可迁移模板：However, most of the METHOD material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  可迁移模板：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (METHOD) materials.
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
  可迁移模板：However, most of the METHOD material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 原句：Most published reports of interfacial contact effects are limited to conventional environments, such as air under standard conditions.
  可迁移模板：Most published reports of interfacial contact effects are limited to conventional environments, such as air under standard conditions.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是“任务需求 + 技术路径 + 缺失环节”。RTG 文献用于说明效率瓶颈和火星任务背景；热电材料与分段 TEG 文献用于说明多层方案的合理性；接触热阻/电阻文献用于说明界面损失的理论基础；火星环境和系统热设计文献用于证明边界条件不能随意简化。

这篇论文的引用并不只是罗列材料性能，而是服务于一个逐步收缩的论点：既然 RTG 需要高效率，既然多层 TEG 有潜力，既然多层必然带来更多界面，那么界面在火星环境下的建模就是不可跳过的研究空缺。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：82
- Introduction 引文簇数量估计：17
- References 条目数：54
- 可识别年份条目数：58
- 2021 年及以后文献数：24
- 2010 年前经典文献数：7
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Applied Thermal Engineering(2)
- 引文簇样例：[13], [1], [2], [3], [4], [5], [6,7], [8,9], [35], [36], [37], [29]

带引文的 gap/转折句样例：

- However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].

References 解析样例（前 8 条）：

- [1] R. Lallement, J.L. Bertaux, E. Qu´emerais, B.R. Sandel, Galactic cosmic rays measured by UVS on Voyager 1 and the end of the modulation, Astron. Astrophys. 563 (2014) A108.
- [2] J.W. Stultz, Thermal design of the Galileo spun and despun science, J. Spacecr. Rockets 28 (2) (1991) 139–145.
- [3] S. Guarro, B. Bream, L.K. Rudolph, R.J. Mulvihill, The Cassini mission risk assessment framework and application techniques, Reliab. Eng. Syst. Saf. 49 (3) (1995) 293–302.
- [4] S.J. Gomez, D. Cheikh, T. Vo, P. Von Allmen, K. Lee, M. Wood, G.J. Snyder, B. S. Dunn, J. Fleurial, S.K. Bux, Synthesis and characterization of vacancy-doped neodymium telluride for thermoelectric applications, Chem. Mat. 31 (12) (2019) 4460–4468.
- [5] T. Widdicombe, R.A. Borrelli, MCNP modelling of radiation effects of the Dragonfly mission’s RTG on Titan II: Atmospheric ionization effects, Acta Astronaut. 186 (2021) 517–522.
- [6] M.B. Naseem, J. Lee, S. In, Radioisotope thermoelectric generators (RTGs): a review of current challenges and future applications, Chem. Commun. 60 (96) (2024) 14155–14167.
- [7] C.P. Bankston, K.L. Atkins, E.F. Mastal, D.G. Mcconnell, Technology development issues in space nuclear-power for planetary exploration, Acta Astronaut. 24 (1991) 161–170.
- [8] X. Liu, H. Sun, S.M. Tang, C.L. Wang, W.X. Tian, S.Z. Qiu, G.H. Su, Thermalhydraulic design features of a micronuclear reactor power source applied for multipurpose, Int. J. Energy Res. 43 (9) (2019) 4170–4183.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 材料组合单一：只采用一组高/中/低温热电材料，不能证明该层级组合是全局最优。
2. 优化变量有限：主要优化三层腿长和直径，层数、材料选择、电极设计、界面材料和电路拓扑没有同时优化。
3. 长期服役风险：238Pu 衰减、热循环、火星尘埃长期沉积、界面老化和银胶稳定性没有完全覆盖。
4. 实验验证尺度风险：实验电压存在约 10% 级偏差，且实验装配条件与完整 RTG 空间环境仍有距离。
5. 模型复杂性风险：多尺度模型参数多，粗糙度、接触压力、氧化膜、间隙气体状态等参数不确定性可能放大。
6. 系统对比口径风险：与传统 RTG 比较时，热源功率、质量统计、任务边界和可靠性要求需统一。

## 17. 可复用资产

可复用研究框架：

1. 先识别理想器件与真实系统之间的关键损失机制。
2. 在微观尺度建立损失模型。
3. 将微观损失等效到器件尺度。
4. 重新评估理想设计在真实环境下的性能。
5. 在真实损失模型下做尺寸或结构优化。
6. 将器件优化结果推到系统层，并与工程基准比较。
7. 用实验验证关键损失参数和输出性能。

可复用表格设计：

- 环境条件对比表：真空/火星/地球/界面材料。
- 接触界面对比表：S-E、E-TE-H、E-TE-M、E-TE-L。
- 理想与真实性能表：power、GPD、efficiency。
- 优化变量与约束表。
- 系统级 RTG 对比表。

## 18. 对我写论文的启发

这篇论文最值得学习的是“把损失项变成创新点”。多层 TEG 的优势是常识性方向，但作者没有停留在性能堆高，而是抓住多层结构不可避免的界面损失，并证明这个损失足以颠覆理想预测。这样选题就从“优化一个 TEG”变成“真实环境下重新认识多层 TEG”。

第二个启发是尺度递进写法。微观接触模型如果单独写会显得太局部，RTG 系统设计如果单独写又可能太粗糙；本文通过等效层把两者串起来，使每个尺度都服务于最终效率指标。

第三个启发是结果要有“反差”。理想模型 7.957% 与火星接触 3.033% 的落差，银胶 8.223% 的恢复，优化后 8.444% 的提升，系统 7.189% 的落地，构成连续的数值故事。

## 19. 最终浓缩

本文针对火星车 RTG 中多层热电发电器的真实界面损失问题，建立了从粗糙接触 TCR/ECR 到器件等效界面层、再到 RTG 系统热设计的多尺度模型。文章证明界面效应会使理想多层 TEG 性能大幅下降，而火星低压 CO2 环境又不能简单等同于真空或地球空气。在考虑接触效应后，作者优化得到火星环境下效率 8.444%、GPD 3.514 W/kg 的多层 TEG，并进一步设计出效率 7.189% 的 RTG 系统。论文最核心的价值是把多层 TEG 的理想材料优势放回真实装配界面和火星环境中评估。
