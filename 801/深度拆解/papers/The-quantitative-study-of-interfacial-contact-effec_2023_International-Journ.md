# The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.txt` 的全文抽取，并参考 `801/文本/metadata/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 中的题名、期刊、目录与页数信息。该文长达 30 页，txt 抽取在公式、附录、表格和参考文献处存在明显双栏串行，尤其 Fig. 21-Fig. 24、Table 7、Appendix A-E 附近。本文依据可读文本做深度拆解，涉及温度云图、粗糙面拓扑图、TCR/ECR 曲线、输出功率公式和实验平台图像的细节均标注“需要 PDF 图像复核”。主体为中文分析，只保留 TCR、ECR、real-topology-based simulation、indirect test、equivalent layers 等关键词。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The TEG, rough surfaces and electric power generation, 3 Numerical models, 4 Experimental measurement, 5 Results and discussions, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests。
- 作者：Ge Gao, Dou Li, Jian-Jun Gou, Chun-Lin Gong, Shuang-Ming Li。
- 期刊与年份：International Journal of Heat and Mass Transfer, 201, 2023, Article 123579。
- DOI：10.1016/j.ijheatmasstransfer.2022.123579。
- 关键词：Quantitative study；Contact effects；Thermoelectric generators；Real-topology-based simulation；Indirect test。
- 论文类型：热电发电器界面热/电接触效应的定量建模、实验测量与简化公式论文。
- 研究对象：用于高超声速气动热采集潜力的 TEG 中，TE legs 与 electrodes 之间的热接触阻抗 TCR 和电接触阻抗 ECR。
- 核心方法：基于真实粗糙表面拓扑的接触对数值预测；考虑热传导、热辐射、弹塑性接触、电传导；新型间接 TCR 实验；ECR 与 TEG 输出实验；等效界面层模拟 TEG 热电转换；最大输出功率预测公式。
- 主要证据：不同温度、压力、gap medium 和 thermal radiation 下 TCR/ECR；TCR 间接测试平台与数值验证；TEG 电源输出实验；公式与数值最大偏差 7.7%；实验/数值电压最大差异 8.73%。
- 目标读者：热电器件、界面传热、电接触、粗糙面接触建模和高超声速热能采集研究者。

这篇论文是 Batch 7 中接触效应系列的基础方法论文。2025 年 TEG 论文把接触模型用于多界面真实器件，而本文更像“把 TCR/ECR 影响 TEG 输出的机制、测量和简化预测公式定量打通”。

## 2. 摘要与核心信息提取

一句话主张：TEG 中 TE legs 与 electrodes 的异质粗糙界面会产生显著 TCR/ECR，进而削弱热传递、电流流动和最大输出功率；本文用真实拓扑数值模拟和新型间接实验定量描述这些接触效应，并提出可预测最大输出功率的简化公式。

摘要按四步推进。第一步，预测不同 temperature、pressure、gap medium、thermal radiation 条件下的 TCR/ECR。第二步，开发依赖 TE conversion characteristics 的 novel indirect TCR test approach，并建立实验平台验证数值模型。第三步，用 equivalent layers 将接触效应纳入 TEG 热电转换模拟，并通过 TEG 输出功率实验验证。第四步，推导两个考虑接触效应的最大输出功率预测公式，公式与数值结果最大偏差 7.7%。

核心信息是“接触效应被从局部界面阻抗转化为整机输出功率预测”。文章没有停在“接触阻抗随压力变化”这一层，而是进一步问：这些 TCR/ECR 如何降低 TEG 的电压和功率？能不能用简化公式在设计阶段快速估算？

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.md`。

中文译文：

> 异质界面接触效应的精确定量描述是开发具有高超音速气动热收集潜力的热电发电机（TEG）的关键问题。本文通过基于实拓扑的数值预测和新颖的间接实验测试研究了热电（TE）腿和电极之间的热电接触效应，并提出了两个简化公式来定量表达它们对 TEG 的影响。首先，预测了不同温度、压力、间隙介质和热辐射条件下的热接触电阻和电接触电阻。其次，开发了一种基于TE转换特性的新型间接热接触热阻（TCR）测试方法，建立了相应的平台并对数值模型进行了验证。第三，考虑等效层的接触效应，模拟了TEG的TE转换过程，开发了TCR测试平台来测量TEG的输出功率，并对数值模型进行了验证。最后推导了考虑接触效应的TEG最大输出功率预测的两个预测公式，与数值结果吻合较好，最大偏差为7.7%。 © 2022 Elsevier Ltd. 保留所有权利。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来源是高超声速飞行器热管理中的 TEG 可靠设计需求。TEG 可能将气动热转化为电能，但真实 TEG 包含多个 TE leg-electrode 界面，TE 材料和电极表面均为微尺度粗糙面，真实接触面积有限，大量接触间隙造成 heat flow 和 electric current constriction。这种 constriction 直接表现为 TCR/ECR，最终削弱输出功率。

作者把大问题收束为“定量描述异质界面接触效应”。这不是泛泛地说“接触不好会影响性能”，而是要在不同温度、压力、介质和辐射条件下预测 TCR/ECR，建立可测平台验证，并将其映射到最大输出功率公式。

选题价值有三层。物理层面，它把粗糙面真实接触、热辐射、热传导、电导通和 TE 转换连接起来。方法层面，它解决 TE 材料脆、难以打孔直接测 TCR 的测量难题，提出利用 Seebeck 特性的间接测试。工程层面，它给 TEG 设计提供接触效应快速估算公式，而不是每次都做微尺度数值模型。

这类选题非常适合 International Journal of Heat and Mass Transfer，因为它的核心是界面传热/传质/电传导与器件性能的定量关系。

## 4. 领域位置与文献版图

Introduction 首先从高超声速飞行器热积累和 TPS 重量问题引出 TE conversion。随后详细说明 TEG 的四个关键界面：N 型腿与电极热/冷侧、P 型腿与电极热/冷侧。这个界面枚举很重要，直接说明 TCR/ECR 不是单一界面小修正，而是每个 TE couple 的多界面系统问题。

文献版图分成 TCR 预测、TCR 测量、ECR 预测/测量、TCR/ECR 对 TEG 的影响几类。TCR 预测部分强调粗糙面表征、接触变形和传热分析；已有方法包括统计参数、semi-deterministic 和 measured real topology。作者指出许多材料是 Ti alloy、C/SiC 等，TE materials 研究有限。TCR 测量方面，steady-state 方法用于 bulk materials，但 TE leg-electrode 界面难以直接测量，因为 TE 材料脆、不易打孔测温。

ECR 文献则强调已有数值模型较少基于真实粗糙表面拓扑，实验方法对简单对象也可能复杂。TEG 性能影响文献承认已有理论/数值研究，但接触效应的定量公式和可验证间接测试仍不足。

本文站位：用 real-topology-based simulation 提升接触预测真实性，用 indirect tests 解决测量难题，用 formulas 连接界面效应和整机最大功率。

## 5. Gap 制造机制

文章制造 gap 的方式非常扎实。第一是材料/对象 gap：已有 TCR/ECR 研究多关注常规材料、TEG 与热/冷源界面，而不是 TE legs 与 electrodes 的异质界面。第二是测量 gap：直接测 TE leg-electrode TCR 困难，尤其 TE 材料脆、样品尺寸小、界面内部温度难以布点。第三是模型 gap：ECR/TCR 模型若不基于真实粗糙面拓扑，难以准确表示真实接触面积和间隙。第四是设计 gap：现有工作缺少把 TCR/ECR 快速映射到 TEG 最大输出功率的简化公式。

这个 gap 的可信度很强，因为作者在 Introduction 中逐条说明了为什么传统方法不足，并在后文逐条回应：真实拓扑重构回应模型 gap，Seebeck 间接测量回应实验 gap，等效层和功率公式回应设计 gap。

可被追问的是：真实拓扑测量本身来自有限样本，是否能代表批量 TE legs/electrodes；间接测试依赖若干热电参数和模型近似，误差传播如何控制；公式适用范围较窄，能否推广到其他尺寸和材料。

## 6. 创新性判断

作者声明的创新包括：基于重构真实粗糙表面预测 TCR/ECR；提出利用 TE 转换特性的间接 TCR 测试方法和平台；将接触效应用 equivalent layers 纳入 TEG 热电转换模拟；建立两个最大输出功率预测公式，并验证其最大偏差为 7.7%。

真实创新属于“实验方法 + 多尺度定量桥接 + 简化公式”。其中最强的是 indirect TCR test approach：它利用 TE 材料的 Seebeck 效应，通过电势/温差关系反推出界面热阻，绕开直接测界面温度的困难。第二个强点是把 TCR/ECR 分别和共同作用下的 TEG 最大功率降低建立公式，使研究不只是现象报告。

创新强度：强。虽然接触热阻和电接触阻抗本身是经典问题，但对象、实验方法和公式桥接使本文有较明确的方法贡献。它比 2025 TEG 论文更偏基础定量方法。

创新边界也很清楚：公式适用范围在 loading pressure 0.104-0.187 MPa、temperature 323-523 K、roughness 3.55-32.53 μm、vacuum/air/silver-epoxy gap medium 内，作者在结论中明确写出，这有助于控制外推风险。

## 7. 论证链条复原

全文论证链如下：

1. 高超声速飞行器热电采集需要可靠 TEG，而 TEG 的 TE leg-electrode 粗糙界面会产生 TCR/ECR。
2. TCR/ECR 由真实接触面积、间隙介质、压力、温度和热辐射共同决定，传统简化模型不够。
3. 基于真实拓扑重构的数值模型可更准确预测 contact mechanics、heat transfer 和 electric conduction。
4. TE leg-electrode TCR 难以直接测量，可利用 Seebeck 转换特性设计间接测试平台，并同步测 ECR 和输出功率。
5. 数值模型在不同压力/温度下与实验结果相对吻合，说明 TCR/ECR 预测可信。
6. 将 TCR/ECR 用 equivalent layers 表示，嵌入 TEG 热电模型，可量化接触效应对电压、温差、内阻和最大输出功率的影响。
7. TCR 与 ECR 单独/共同影响可被解耦近似，进而推导最大输出功率预测公式。
8. 公式与数值最大偏差 7.7%，实验电压最大差异 8.73%，证明方法可用于设计估算。

这条链的关键是从界面参数到整机输出的闭合。很多界面论文只到 TCR/ECR 曲线，本文继续走到 TEG 最大输出功率，这让接触效应对工程设计的意义变得可量化。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The TCR under air gap is about half of that under vacuum gap, and the TCR under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
- 已有研究不足/GAP：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 本文解决方式：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG. Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

研究对象为用于飞行器背风区域的 TEG，工作温度约 600-800 K 背景来自前期飞行器描述。样品包括 alumina ceramic substrates、N/P TE legs、copper electrodes 和 PEEK shell。TEG 有四类关键界面，界面粗糙导致真实接触区域有限，vacuum/air gap 下热量通过真实接触固体传导和间隙热辐射传递，电流只能通过真实接触区域；silver-epoxy adhesive gap 下，热流和电流还可通过介质传递。

数值模型包括接触力学、热传导、电传导和 TE 耦合。接触力学考虑弹性/塑性阶段，求真实接触面积和间隙距离；TCR 计算考虑 solid conduction、gap/radiation；ECR 计算考虑电流收缩和真实接触路径；TEG 整机中用 equivalent layers 表示接触阻力。

实验方法的创新点在 TCR 间接测量。基本思路是：设置加载压力和热源温度，待稳态后由不锈钢块温度梯度计算热流，通过电极测得 TE leg 电势差，再结合 TE leg 电阻和 ECR，利用 TE 转换特性推算热端/冷端界面 TCR。平台还可调整用于 ECR 和 TEG power generation 测量。

公式方法将最大输出功率写成电势差和内阻的函数，再引入 TCR 导致的温差变化、ECR 导致的内阻增加，以及二者耦合影响。作者比较 decoupling prediction 与更保守的乘积预测，指出 silver-epoxy gap 下预测精度高，vacuum/air 下公式趋于保守。

## 9. 证据系统与 Claim-Evidence 表

证据系统覆盖数值趋势、实验验证、公式验证和不确定性附录。结论中列出 7 条，基本对应全文 claim。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 基于真实粗糙拓扑的模型可预测不同温度/压力/介质下 TCR | Conclusion 1、Fig. 8-15 | 重构 TE legs/electrodes 粗糙面，计算热传导和辐射 | 数值模型 | 强 | 拓扑样本代表性需复核 |
| thermal radiation 对 TCR 的影响随界面平均温度升高而增强 | Conclusion 2、Fig. 11-13 | vacuum/air gap 下辐射贡献随温度增大；vacuum 主要受 TE 材料导热影响，air 下 TCR 随温度升高下降 | 数值分析 | 中强 | 近场辐射被简化，附录说明多数间隙 >5 μm |
| 加载压力增加会降低 TCR，且趋势放缓 | Conclusion 3、Fig. 14-15 | pressure 增大真实接触面积，TCR 下降；air gap 约为 vacuum 的一半，silver-epoxy 约为 vacuum 的千分之一 | 数值曲线 | 强 | 具体数量需 PDF 图像复核 |
| 间接 TCR 测试平台可获得合理实验结果 | Conclusion 4、Fig. 5-7/Table 4-6 | 实验与数值最大差异 -27.51%，平台也可测 ECR 和 TEG power supply | 实验验证 | 中 | -27.51% 偏差较大 |
| ECR 对 TEG 的负面影响在 vacuum/air 下高于 TCR | Conclusion 5、Fig. 22-24 | vacuum/air 下 ECR 降低电场/输出更显著；silver-epoxy 下 TCR 略高于 ECR | 数值比较 | 强 | 依赖特定材料和界面 |
| contact effects 在 silver-epoxy gap 下导致性能退化不超过 4%，air gap 下超过 96% | Conclusion 5、Fig. 24 | 相比 perfect contact，air/vacuum 下最大输出功率降低约 96.3-97.8%，silver-epoxy 降低约 2.6-3.8% | 整机模拟 | 强 | silver-epoxy 高温可靠性未完全验证 |
| 最大输出功率预测公式最大偏差 7.7% | Abstract、Conclusion 7、Table 7 | loading pressure 0.104-0.187 MPa、temperature 323-523 K、roughness 3.55-32.53 μm 等范围内公式与数值吻合 | 公式验证 | 强 | 适用范围较窄 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | TEG 与界面接触示意 | 研究对象具体化 | 四类 TE leg-electrode 界面和 gap medium | 需要 PDF 图像复核 |
| Fig. 2 | 粗糙面重构与接触模型 | real-topology-based simulation | 真实粗糙拓扑进入接触计算 | 需要 PDF 图像复核 |
| Fig. 3-Fig. 4 | 边界条件与网格 | 模型可复现性 | 接触对和 TEG 网格设置 | 需要 PDF 图像复核 |
| Fig. 5-Fig. 6 | 间接 TCR 测试方法与平台 | 实验方法创新 | 利用 TE 转换特性反推 TCR | 需要 PDF 图像复核 |
| Fig. 7/Table 7 | ECR 与 TEG power generation 实验 | 整机输出验证 | 电压实验与数值最大差异 8.73% | 表格需 PDF 复核 |
| Fig. 8-Fig. 10 | 不同介质下温度/热流云图 | TCR 机制 | vacuum/air/silver-epoxy 热路径不同 | 需要 PDF 图像复核 |
| Fig. 11-Fig. 15 | 辐射、温度、压力对 TCR 影响 | TCR 定量规律 | TCR 随压力下降；silver-epoxy 最低 | 需要 PDF 图像复核 |
| Fig. 16-Fig. 21 | TCR 对 TEG 温差、平均温度和最大功率影响 | TCR 降低热电输出 | contact effects 改变 TE legs 温差 | 需要 PDF 图像复核 |
| Fig. 22-Fig. 24 | TCR+ECR 耦合影响与功率预测 | ECR/TCR 共同削弱输出 | air/vacuum 功率降幅巨大，公式最大偏差 7.7% | 需要 PDF 图像复核 |
| Appendix A-E | 辐射、边界、实验、不确定性 | 控制审稿风险 | 近场辐射、边界条件和测量不确定性说明 | 公式需 PDF 复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The TEG, rough surfaces and electric power generation；3 Numerical models；4 Experimental measurement；5 Results and discussions；6 Conclusion，并有 Appendix A-E。第 2 章先定义 TEG、材料、理论功率和粗糙面；第 3 章给控制方程、TCR/ECR 计算、边界条件和网格；第 4 章讲 TCR、ECR 和输出功率实验；第 5 章分 contact mechanics/heat transfer、TCR/ECR、contact effects in TEG 三大块。

结构逻辑是“对象与理论 -> 数值模型 -> 实验测量 -> 结果与公式”。比 2025 TEG 论文更基础，因为它先花大量篇幅解释 TCR/ECR 如何定义和测量，再进入整机 TEG。

附录很重要：Appendix A 处理 thermal radiation，Appendix B 给接触模型边界，Appendix C/D 给实验测量细节，Appendix E 给不确定性分析。这说明作者预判审稿人会追问辐射简化、边界条件和测量误差。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The TEG, rough surfaces and electric power generation（对象/模块/过渡章节）
  - L3 p.3: 2.1 The TEG and material properties（对象/模块/过渡章节）
  - L3 p.4: 2.2 Theoretical power generation of TEG with consideration of contact effects（对象/模块/过渡章节）
  - L3 p.5: 2.3 Rough surfaces and contacting models（方法/模型/算法）
- L2 p.5: 3 Numerical models（方法/模型/算法）
  - L3 p.5: 3.1 Governing equations（对象/模块/过渡章节）
    - L4 p.6: 3.1.1 Equilibrium equation（对象/模块/过渡章节）
    - L4 p.6: 3.1.2 Geometric equation（对象/模块/过渡章节）
    - L4 p.6: 3.1.3 Constitutive equations for elastic stage（对象/模块/过渡章节）
    - L4 p.6: 3.1.4 Constitutive equations for plastic stage（对象/模块/过渡章节）
  - L3 p.6: 3.2 Calculation methods of TCR and ECR（方法/模型/算法）
  - L3 p.6: 3.3 Boundary conditions（对象/模块/过渡章节）
  - L3 p.7: 3.4 Meshed models（方法/模型/算法）
- L2 p.8: 4 Experimental measurement（结果/验证/讨论）
  - L3 p.8: 4.1 Experimental method for TCR（方法/模型/算法）
  - L3 p.9: 4.2 Experimental platform for TCR（结果/验证/讨论）
  - L3 p.9: 4.3 Experimental measurements of ECR and power generation（结果/验证/讨论）
- L2 p.9: 5 Results and discussions（结果/验证/讨论）
  - L3 p.9: 5.1 Contact mechanics and heat transfer（对象/模块/过渡章节）
  - L3 p.13: 5.2 Thermal and electrical contact resistance（对象/模块/过渡章节）
    - L4 p.13: 5.2.1 The influence of thermal radiation（对象/模块/过渡章节）
    - L4 p.13: 5.2.2 The influence of average interface temperature（对象/模块/过渡章节）
    - L4 p.15: 5.2.3 The influence of loading pressure（对象/模块/过渡章节）
    - L4 p.16: 5.2.4 The experimental results of thermal contact resistance（结果/验证/讨论）
    - L4 p.19: 5.2.5 Electrical contact resistance（对象/模块/过渡章节）
  - L3 p.19: 5.3 The quantitative description of contact effects in TEG（问题定义）
    - L4 p.19: 5.3.1 Considering the impact of TCR（对象/模块/过渡章节）
    - L4 p.23: 5.3.2 Considering the impact of both TCR and ECR（对象/模块/过渡章节）
- L2 p.26: 6 Conclusion（结论/贡献回收）
- L2 p.26: Data availability statement（尾部材料）
- L2 p.26: Declaration of Competing Interest（尾部材料）
- L2 p.26: CRediT authorship contribution statement（尾部材料）
- L2 p.26: Acknowledgments（尾部材料）
- L2 p.26: Appendix A Calculation method of thermal radiation（方法/模型/算法）
- L2 p.27: Appendix B Boundary conditions of contacting models（方法/模型/算法）
- L2 p.27: Appendix C Experimental measurement of TCR（结果/验证/讨论）
- L2 p.28: Appendix D Experimental measurement of power generation（结果/验证/讨论）
- L2 p.28: Appendix E Uncertainty analysis（尾部材料）
- L2 p.29: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The TEG, rough surfaces and electric power generation | 3 | 2 | 对象/模块/过渡章节 |
| 2.1 The TEG and material properties | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Theoretical power generation of TEG with consideration of contact effects | 4 | 3 | 对象/模块/过渡章节 |
| 2.3 Rough surfaces and contacting models | 5 | 3 | 方法/模型/算法 |
| 3 Numerical models | 5 | 2 | 方法/模型/算法 |
| 3.1 Governing equations | 5 | 3 | 对象/模块/过渡章节 |
| 3.1.1 Equilibrium equation | 6 | 4 | 对象/模块/过渡章节 |
| 3.1.2 Geometric equation | 6 | 4 | 对象/模块/过渡章节 |
| 3.1.3 Constitutive equations for elastic stage | 6 | 4 | 对象/模块/过渡章节 |
| 3.1.4 Constitutive equations for plastic stage | 6 | 4 | 对象/模块/过渡章节 |
| 3.2 Calculation methods of TCR and ECR | 6 | 3 | 方法/模型/算法 |
| 3.3 Boundary conditions | 6 | 3 | 对象/模块/过渡章节 |
| 3.4 Meshed models | 7 | 3 | 方法/模型/算法 |
| 4 Experimental measurement | 8 | 2 | 结果/验证/讨论 |
| 4.1 Experimental method for TCR | 8 | 3 | 方法/模型/算法 |
| 4.2 Experimental platform for TCR | 9 | 3 | 结果/验证/讨论 |
| 4.3 Experimental measurements of ECR and power generation | 9 | 3 | 结果/验证/讨论 |
| 5 Results and discussions | 9 | 2 | 结果/验证/讨论 |
| 5.1 Contact mechanics and heat transfer | 9 | 3 | 对象/模块/过渡章节 |
| 5.2 Thermal and electrical contact resistance | 13 | 3 | 对象/模块/过渡章节 |
| 5.2.1 The influence of thermal radiation | 13 | 4 | 对象/模块/过渡章节 |
| 5.2.2 The influence of average interface temperature | 13 | 4 | 对象/模块/过渡章节 |
| 5.2.3 The influence of loading pressure | 15 | 4 | 对象/模块/过渡章节 |
| 5.2.4 The experimental results of thermal contact resistance | 16 | 4 | 结果/验证/讨论 |
| 5.2.5 Electrical contact resistance | 19 | 4 | 对象/模块/过渡章节 |
| 5.3 The quantitative description of contact effects in TEG | 19 | 3 | 问题定义 |
| 5.3.1 Considering the impact of TCR | 19 | 4 | 对象/模块/过渡章节 |
| 5.3.2 Considering the impact of both TCR and ECR | 23 | 4 | 对象/模块/过渡章节 |
| 6 Conclusion | 26 | 2 | 结论/贡献回收 |
| Data availability statement | 26 | 2 | 尾部材料 |
| Declaration of Competing Interest | 26 | 2 | 尾部材料 |
| CRediT authorship contribution statement | 26 | 2 | 尾部材料 |
| Acknowledgments | 26 | 2 | 尾部材料 |
| Appendix A Calculation method of thermal radiation | 26 | 2 | 方法/模型/算法 |
| Appendix B Boundary conditions of contacting models | 27 | 2 | 方法/模型/算法 |
| Appendix C Experimental measurement of TCR | 27 | 2 | 结果/验证/讨论 |
| Appendix D Experimental measurement of power generation | 28 | 2 | 结果/验证/讨论 |
| Appendix E Uncertainty analysis | 28 | 2 | 尾部材料 |
| References | 29 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一段从高超声速热积累和 TE-TPS 潜力进入，随后马上拆出 TEG 中至少四个关键界面，制造接触效应重要性。然后分别综述 TCR 预测、TCR 测量、ECR 预测/测量和 contact effects 对 TEG 的影响。最后一段列出本文流程，几乎就是后文目录。

方法段落节奏偏严密：先讲材料和几何，再讲理论功率公式，再讲粗糙面接触模型。公式较多，读者负担大，但每个公式都服务于后面“最大输出功率预测”。

结果段落采用从局部到整机的节奏。5.1 先讲 contact mechanics and heat transfer，5.2 讲 TCR/ECR 的影响因素和实验，5.3 讲 TEG 中 contact effects 的量化描述和公式。这个顺序合理，因为没有前两节的 TCR/ECR 定量，后面的功率公式就缺支撑。

## 13. 文笔画像与语言习惯

文笔是 IJHMT 典型的机理-模型-实验混合风格。高频词包括 precise quantitative description、heterogeneous interfaces、real-topology-based predictions、novel indirect tests、thermal radiation、loading pressure、gap medium、maximum output power。

作者喜欢用 “First/Second/Third/Finally” 串联贡献，用 “it should be noted that” 处理假设和边界，用 “in good agreement” 描述模型验证。结果描述非常数字化，结论中保留适用范围和最大偏差，显示作者重视定量可信度。

语气总体谨慎。即使 claim 较强，也会给出最大差异、适用范围和保守性说明。例如 decoupling method 在 vacuum/air 下趋于 conservative，这比单纯说公式准确更有工程可信度。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：35710
- 高频词：tcr(89)；leg(72)；temperature(69)；type(53)；ecr(49)；teg(47)；contact(43)；electrode(42)；thermal(39)；gap(37)；heat(36)；surface(35)；side(35)；electric(34)；increases(33)；legs(32)；average(31)；power(29)；electrodes(28)；rough(24)
- 高频名词化/学术名词：temperature(69)；resistance(23)；compression(19)；displacement(19)；radiation(14)；pressure(14)；conductivity(12)；influence(11)；difference(10)；measurement(9)；simulation(8)；prediction(7)；conversion(6)；conduction(6)；measure(6)
- 高频学术动词：developed(5)；predicted(5)；validated(5)；predict(2)；analyzed(1)
- 高频形容词：thermal(39)；electric(34)；displacement(19)；numerical(18)；experimental(18)；electrical(15)；real(10)；adhesive(10)；material(9)；internal(9)；measurement(9)；potential(8)；different(8)；coefficient(7)；elastic(6)
- 高频副词：mainly(8)；supply(6)；relatively(3)；significantly(3)；finally(3)；gradually(3)；publicly(1)；greatly(1)；widely(1)；firstly(1)；negatively(1)；positively(1)；thirdly(1)；slightly(1)
- 高频二词短语：type leg(43)；surface type(27)；average interface(21)；interface temperature(21)；cold side(20)；rough surfaces(19)；maximum output(18)；output power(18)；compression displacement(18)；leg electrode(16)；hot side(15)；legs electrodes(15)
- 高频三词短语：surface type leg(27)；average interface temperature(21)；maximum output power(18)；upper surface type(14)；lower surface type(13)；interface temperature increases(13)；side leg electrode(12)；output power teg(9)；electrode lower surface(9)；electrode upper surface(9)；absolute value compression(9)；value compression displacement(9)
- 被动语态估计：60；`we + 动作动词` 主动句估计：0
- 一般现在时线索：166；一般过去时线索：156；现在完成时线索：1；情态动词线索：33

分章节正文词频：

- 1 Introduction: tcr(38)；leg(32)；ecr(27)；type(26)；teg(22)；electrode(22)；side(20)；heat(19)
- 2 The TEG, rough surfaces and electric power generation: type(20)；legs(18)；electric(14)；electrodes(13)；leg(13)；teg(11)；ecr(11)；surface(11)
- 3 Numerical models: contact(7)；ijkl(7)；temperature(5)；equations(5)；elastic(5)；equation(5)；heat(4)；stage(4)
- 4 Experimental measurement: leg(15)；side(12)；tcr(8)；electrode(8)；temperature(8)；cold(7)；num(6)；hot(5)
- 5 Results and discussions: increases(32)；temperature(30)；tcr(23)；average(22)；interface(19)；compression(18)；displacement(18)；gap(14)
- 6 Conclusion: gap(14)；tcr(13)；teg(12)；thermal(8)；contact(8)；loading(6)；power(6)；vacuum(6)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：thermal contact resistance、electrical contact resistance、real contact area、gap medium、thermal radiation、real-topology-based simulation、indirect test、equivalent layers、maximum output power、loading pressure。

可复用问题句式：`The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing TEGs.` 适合界面/器件论文开头。

可复用 gap 句式：`Few published reports are on measuring the TCR between TE legs and electrodes.` 简洁地把测量对象具体化。

可复用方法句式：`A novel indirect TCR test approach relying on the TE conversion characteristics is developed.` 适合强调测量创新。

可复用结果句式：`Compared with the perfect contact condition, the maximum output power is reduced by ...` 适合量化非理想效应。

可复用边界句式：`The prediction formulas are applicable for loading pressure from ..., temperature from ..., roughness from ..., and gap medium of ...` 适合公式论文主动限定范围。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Proper characterization of rough surfaces is essential for the accurate estimation of TCR.
  可迁移模板：Proper characterization of rough surfaces is essential for the accurate estimation of METHOD.
- 原句：The essential assumptions involved in above characterizations weakens their accuracy.
  可迁移模板：The essential assumptions involved in above characterizations weakens their accuracy.
- 原句：ECRs play an important role in ensuring the energy efficiency, thermal behavior and stable operation of electrical connections.
  可迁移模板：ECRs play an important role in ensuring the energy efficiency, thermal behavior and stable operation of electrical connections.
- 原句：The TCR under air gap is about half of that under vacuum gap, and the TCR under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
  可迁移模板：The METHOD under air gap is about half of that under vacuum gap, and the METHOD under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. XThe developed METHOD test approach is essential to obtain reasonable experimental results for the test sample containing one METHOD leg and two electrodes.
#### Gap/转折句
- 原句：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  可迁移模板：METHOD legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 原句：Nevertheless, few published reports are on measuring the TCR between TE legs and electrodes.
  可迁移模板：Nevertheless, few published reports are on measuring the METHOD between METHOD legs and electrodes.
- 原句：Since the TE material is brittle (difficult to punch signal holes), it is difficult to measure the TCR by direct methods.
  可迁移模板：Since the METHOD material is brittle (difficult to punch signal holes), it is difficult to measure the METHOD by direct methods.
- 原句：However, few numerical models for predicting the ECR are based on the reconstructed real rough surface topography.
  可迁移模板：However, few numerical models for predicting the METHOD are based on the reconstructed real rough surface topography.
- 原句：Nevertheless, previous studies lack of complete and reliable data to clarify the quantitative influence of TCR and ECR on TEGs, e.g., most of the numerical models are not verified by experimental measurement.
  可迁移模板：Nevertheless, previous studies lack of complete and reliable data to clarify the quantitative influence of METHOD and METHOD on TEGs, e.g., most of the numerical models are not verified by experimental measurement.
#### 方法提出句
- 原句：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
  可迁移模板：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
- 原句：In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG.
  可迁移模板：In this paper, the thermal and electrical contact effects between thermoelectric (METHOD) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on METHOD.
- 原句：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句：Third, the TE conversion process of TEG is simulated with considering the contact effects by equivalent layers, the TCR test platform is developed to measure the out power of TEG and the numerical models are then validated.
  可迁移模板：Third, the METHOD conversion process of METHOD is simulated with considering the contact effects by equivalent layers, the METHOD test platform is developed to measure the out power of METHOD and the numerical models are then validated.
- 原句：In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG.
  可迁移模板：In this paper, the thermal and electrical contact effects between thermoelectric (METHOD) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on METHOD.
#### 结果呈现句
- 原句：Finally, two simplified formulas to predict the maximum output power of the TEG are established, which are in good agreement with the numerical results.
  可迁移模板：Finally, two simplified formulas to predict the maximum output power of the METHOD are established, which are in good agreement with the numerical results.
- 原句：The results show some conclusions: 1 In the numerical prediction of the TCR, heat conduction and thermal radiation are considered, and the model is established based on the reconstructed real rough surface topographies of the TE legs and electrodes.
  可迁移模板：The results show some conclusions: XIn the numerical prediction of the METHOD, heat conduction and thermal radiation are considered, and the model is established based on the reconstructed real rough surface topographies of the METHOD legs and electrodes.
- 原句：The TCR under air gap is about half of that under vacuum gap, and the TCR under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
  可迁移模板：The METHOD under air gap is about half of that under vacuum gap, and the METHOD under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. XThe developed METHOD test approach is essential to obtain reasonable experimental results for the test sample containing one METHOD leg and two electrodes.
- 原句：The corresponding experimental platform can measure the TCR under different temperatures and loading pressures, and the experimental and numerical results have a relatively good agreement with the largest difference of -27.51%.
  可迁移模板：The corresponding experimental platform can measure the METHOD under different temperatures and loading pressures, and the experimental and numerical results have a relatively good agreement with the largest difference of -X.
#### 贡献/增量句
- 原句：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句：The authors tried to establish TCR prediction models based on the measured real topology and the models have relatively good agreement with experiments.
  可迁移模板：The authors tried to establish METHOD prediction models based on the measured real topology and the models have relatively good agreement with experiments.
- 原句：Sun et al. [17] and Chen et al. [20] measured the TCR under vacuum gap, and Chen et al. [20] found that thermal radiation contributes greatly to heat transfer in high temperatures (higher than 600 °C).
  可迁移模板：Sun et al. [X] and Chen et al. [X] measured the METHOD under vacuum gap, and Chen et al. [X] found that thermal radiation contributes greatly to heat transfer in high temperatures (higher than X°C).
- 原句：For the theoretical and numerical study of the influences of TCR and ECR on TEG, Kim [32] established a computer simulation program, and Shittu et al. [33] established a numerical model.
  可迁移模板：For the theoretical and numerical study of the influences of METHOD and METHOD on METHOD, Kim [X] established a computer simulation program, and Shittu et al. [X] established a numerical model.
#### 限制/边界句
- 原句：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  可迁移模板：METHOD legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略按问题链组织。作者先引用高超声速热防护和 TE-TPS 文献，说明应用动机；再引用粗糙面 TCR 模型，包括统计、真实拓扑和 diffuse interface 等；随后引用 TCR 测量方法，区分 steady-state 和 transient；再引用 ECR 预测/实验；最后引用 TCR/ECR 对 TEG 性能影响的理论与数值研究。

这种引用不是按时间线，而是按“预测-测量-器件影响”组织，正好对应本文三项贡献。每类文献都被指出一个具体不足：对象不是 TE leg-electrode、直接测量困难、ECR 模型不基于真实粗糙面、缺少简化公式。

引用中团队前作较多，如 C/C-SiC/Ti alloy 真实拓扑 TCR 模型、高超声速 TEG 多级研究等。这说明本文是已有真实拓扑方法向 TE 界面的迁移与扩展。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：83
- Introduction 引文簇数量估计：31
- References 条目数：42
- 可识别年份条目数：83
- 2021 年及以后文献数：16
- 2010 年前经典文献数：1
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：International Journal of Heat and Mass Transfer(2)
- 引文簇样例：[1], [6], [7], [8], [9], [10], [11], [12], [22], [23], [24], [16]

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- [1] JJ Gou, JX Hu, ZW Yan, G Gao, CL. Gong, Effects of physical dimensions, temperature ranges and interfacial thermal contacts on the multi-stage thermoelectric generators for a hypersonic vehicle, Int. J. Energy Res. 46 (2022) 20 021–20 038, doi: 10.1002/er.7799 .
- [2] JJ Gou, ZW Yan, JX Hu, G Gao, CL. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021) 106373, doi: 10.1016/j.ast.2020.106373 .
- [3] BX Shen, WQ. Liu, Insulating and absorbing heat of transpiration in a combinational opposing jet and platelet transpiration blunt body for hypersonic vehicle, Int. J. Heat Mass Transf. 138 (2019) 314–325, doi: 10.1016/j. ijheatmasstransfer.2019.04.057 .
- [4] G Gao, J-J Gou, C-L Gong, J-X Hu, R-C. Gao, A novel mechanical-thermalelectrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962, doi: 10.1016/j.compstruct.2021.113962 .
- [5] CL Gong, JJ Gou, JX Hu, F. Gao, A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470, doi: 10.1016/j.ast.2018.03.028 .
- [6] T Cui, Q Li, Y. Xuan, Characterization and application of engineered regular rough surfaces in thermal contact resistance, Appl. Therm. Eng. 71 (2014) 400– 409, doi: 10.1016/j.applthermaleng.2014.07.020 .
- [7] J Liu, C Ma, S Wang, S Wang, B. Yang, Thermal contact resistance between bearing inner ring and shaft journal, Int. J. Therm. Sci. 138 (2019) 521–535, doi: 10.1016/j.ijthermalsci.2019.01.022 .
G. Gao, D. Li, J.-J. Gou et al. International Journal of Heat and Mass Transfer 201 (2023) 123579
- [8] PG Siddappa, A. Tariq, Contact area and thermal conductance estimation based on the actual surface roughness measurement, Tribol. Int. 148 (2020) 106358, doi: 10.1016/j.triboint.2020.106358 .
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 间接测试误差较大：TCR 实验与数值最大差异 -27.51%，需要充分解释误差来源和不确定性。
2. 公式适用范围有限：压力、温度、粗糙度和介质范围明确，但超出范围不能外推。
3. silver-epoxy 假设风险：其在高温、热循环、长期服役中的导热/导电和粘接稳定性需验证。
4. 近场辐射简化风险：附录解释多数间隙大于 5 μm，近场影响有限，但在更光滑/更高压界面可能不同。
5. TE 参数温度依赖风险：材料 Seebeck、电导、热导和接触状态随温度变化，参数不确定会传递到公式。
6. TEG 实验尺度风险：样品尺寸和真实飞行器大面积 TEG 阵列之间仍有尺度差异。
7. 图表复核风险：Fig. 16-24 和 Table 7 是关键功率证据，需 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把器件性能下降追溯到异质界面接触效应，形成从微观界面到宏观功率的链条。
- 方法资产：真实拓扑模拟 + 间接测试 + 等效层 + 简化公式的四段式。
- 实验资产：利用 Seebeck 特性反推 TCR，绕开直接测界面温度困难。
- 公式资产：将 TCR/ECR 引起的温差变化和内阻变化转成最大输出功率估算。
- 风险控制资产：在结论中明确公式适用范围和最大偏差。
- 附录资产：把辐射模型、边界条件、实验测量和不确定性放入附录，增强方法可信度。

## 18. 对我写论文的启发

这篇论文最值得学习的是“不要停在局部参数”。如果研究界面接触，不只报告 TCR 随压力变化，还要说明它如何影响器件输出、系统效率或设计公式。本文通过最大输出功率公式把界面研究推到了工程可用层。

第二个启发是实验方法可以来自被测对象的物理特性。TE 材料有 Seebeck 效应，作者就用这个效应做间接 TCR 测试。自己的研究中也可以寻找“对象自带的物理响应”来设计测量方法。

第三个启发是公式要写边界。作者明确 pressure、temperature、roughness、gap medium 范围，使公式看起来更可信。模糊地说“适用于 TEG”反而容易被审稿人攻击。

## 19. 最终浓缩

这篇论文的核心贡献是定量打通 TEG 中 TE leg-electrode 界面接触效应与整机最大输出功率之间的关系。作者用真实拓扑接触模型预测 TCR/ECR，用基于 Seebeck 特性的间接实验验证 TCR，并将接触效应用等效层纳入 TEG 热电模型，最终给出最大输出功率预测公式，最大偏差 7.7%。最值得学习的是“微观界面 -> 实验测量 -> 整机性能 -> 设计公式”的完整论证链；最需要复核的是 TCR 实验偏差、Fig. 16-24 的功率/场图细节、Table 7 电压数据和公式适用范围。
