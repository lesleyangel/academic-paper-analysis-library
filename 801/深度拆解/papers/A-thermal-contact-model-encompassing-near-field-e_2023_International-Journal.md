# A thermal contact model encompassing near-field effects of multi-interface TEGs in hypersonic conditions

## 0. 读取说明

本文拆解依据 `801/文本/txt/A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal.txt` 的全文抽取。该 PDF 为双栏排版，公式和图注在 txt 中有多处跨栏错位；近场热辐射公式、图 12-22 的云图/曲线细节需要 PDF 图像复核。以下分析以文本稳定可读的研究链条、关键数值、表格和结论为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Thermal contact models, 3 Numerical models, 4 Experimental measurement platform for TCR, 5 Results and discussions, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A thermal contact model encompassing near-field effects of multi-interface TEGs in hypersonic conditions
- 作者：Ge Gao, Shi-Yuan Chen, Li-Qiang Ai, Nan Liu, Jian-Jun Gou, Chun-Lin Gong
- 期刊：International Journal of Heat and Mass Transfer, 216, 124543
- 年份：2023
- 领域：高超声速热管理、热电发电器、热接触电阻、近场热辐射、多界面传热。
- 论文类型：理论/数值模型 + 实验验证 + TEG 性能评估。
- 研究对象：高超声速条件下多界面 TEG 中 substrate-electrode 与 electrode-TE leg 的 TCR，尤其是真空/空气间隙中的 FFTR 与 NFTR。
- 方法：真实拓扑粗糙面建模、接触变形仿真、波动电动力学计算近/远场辐射、TCR 实验平台验证、等效界面层 TEG 性能模型。
- 主要证据：粗糙面测量与重构、TCC/TCR 公式、公开文献对比验证、TCR 随温度/压力/介质/热流路径变化、实验-数值对比、TEG 输出功率变化。
- 目标读者：传热学研究者、热电器件设计者、高超声速热防护与热管理工程师。

## 2. 摘要与核心信息提取

一句话主张：在高超声速 TEG 多异质界面的热接触建模中，近场热辐射不可忽略；把 NFTR 纳入真实拓扑 TCR 模型并经实验验证后，可更准确评估 TCR 和 TEG 输出功率。

摘要的核心信息是三段式。第一，建立包含 NFTR 的多界面 TEG 热接触模型，并用 fluctuational electrodynamics 处理远场/近场辐射。第二，分析平均界面温度、间隙距离、热流方向、加载压力、间隙介质对 TCR 的影响。第三，把 TCR 等效进入 TEG 性能模型，得到 NFTR 使 TE leg-electrode 与 substrate-electrode 间 TCR 分别降低若干比例，并使最大输出功率在真空/空气间隙下分别提高约 8.02% 和 1.29%（0.1 MPa, 650 K）。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal.md`。

中文译文：

> 高超音速飞行器的高效热收集需要精心设计的热电（TE）转换过程。热电发电机（TEG）在传热路径中包含多个界面，具有一定纳米级效应的界面热接触对其TE转换过程有显着影响。本文建立了一个热接触模型，该模型涵盖了基板、电极和 TE 腿之间具有异质界面的 TEG 的近场热辐射 (NFTR) 效应，并在高超声速条件下进行了实验验证。首先，建立了基于真实拓扑的热接触热阻（TCR）预测模型，并通过波动电动力学考虑异质界面的远场和近场辐射传热，并通过直接和间接实验测量验证了该模型。
>
> 其次，分析了平均界面温度、间隙距离和相对传热路径对热辐射的影响，明确了平均界面温度、加载压力和间隙介质对TCR的影响。第三，在TEG性能评估模型中等效考虑TCR，并定量计算NFTR效应。结果表明：在考虑NFTR的情况下，TE腿与电极、基板与电极之间的TCR在真空间隙下分别降低了约3.90%~17.0%和0.510%~6.40%，在空气间隙下分别降低了1.30%~5.50%和0.220%~2.00%；在真空和空气间隙（0.1 MPa，650 K）下，TEG的最大输出功率分别增加了约8.02%和1.29%。实际接触区域非常有限，接触间隙比例很大。
>
> 当热量流经热侧基板、热侧电极、N型和P型TE脚、冷侧电极和冷侧基板时，各接触界面的接触间隙导致接触热阻(TCR)。这种累积的界面TCR对传热过程有显着影响，并削弱TEG的TE性能。 TCR预测主要包含粗糙表面表征、接触变形分析和传热计算三个步骤。粗糙表面的正确表征对于准确估计 TCR 至关重要。粗糙表面可以基于GW统计模型[7]、Weier strass-Mandelbrot分形模型[8]、欧几里得几何统计模型[9]、面部模型[10]和基于半确定性的方法[11]来重建。
>
> 虽然上述表征中涉及的假设削弱了它们的准确性。光学轮廓仪可以准确测量粗糙表面形貌[12]。弗雷克斯等人。 [13]提出了一种基于微观尺度的接触传热预测数值方法
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

问题来源是热电热管理系统中的“多界面累积热阻”。高超声速 TEG 要利用大温差发电，但热流必须穿过 substrates、electrodes、N/P TE legs 等多材料界面。粗糙表面导致真实接触区有限，大量间隙区域让热传输不仅有固体接触传导，也可能有远场和近场辐射。

作者把大问题收束为：在 600-800 K 高超声速工作温度附近，微/纳间隙中 NFTR 对多异质界面 TCR 和 TEG 性能有多大影响。这个收束很有效，因为它既有基础传热机理（evanescent waves, SPPs/SPhPs, fluctuational electrodynamics），又有工程对象（TEG 多界面）。

选题价值包括理论价值和工程价值：理论上把 NFTR 放进真实粗糙界面的 TCR 预测；工程上量化 TEG 输出功率是否会因忽略 NFTR 而评估偏差。

## 4. 领域位置与文献版图

文献版图分为五组。

第一组是高超声速 TPS/TEG 热管理，说明传统热防护重量和能效问题，以及 TEG 作为回收式热管理方案的潜力。

第二组是 TCR 预测方法，包括 GW 统计模型、Weierstrass-Mandelbrot 分形模型、几何统计模型、真实拓扑测量方法等。作者指出理想化粗糙面假设削弱预测精度。

第三组是近场热辐射基础。作者引用热辐射特征波长、黑体极限、纳米间隙下热流增强、SPPs/SPhPs 等研究，说明 NFTR 在工程粗糙面尺度可能与固体传导同量级。

第四组是 TCR 实验测量，尤其是 steady-state 方法和 TEG 系统界面测量。作者指出多数工作测 TEG 与冷热源之间的 TCR，较少关注 TEG 内部异质界面。

第五组是 TCR 对 TEG 性能影响的理论和数值研究。作者强调已有工作缺乏完整可靠的内部异质界面 TCR 数据，且之前工作未同时考虑 substrates-electrodes 与 TE legs-electrodes。

## 5. Gap 制造机制

本文 gap 的制造很强，因为它连续指出三个“不够”：

- 机理不够：以往 TCR 模型多关注固体传导，少考虑 FFTR，NFTR 更少被纳入真实 TEG 界面。
- 对象不够：NFTR 文献常见材料是 Al、C/SiC、HTA 等，TE 材料研究有限。
- 系统不够：已有 TEG TCR 多测外部冷热源界面或只测 TE leg-electrode，未系统覆盖 substrate-electrode 和多界面累积效应。

gap 的说服力来自材料和尺度匹配：300 K 时热辐射特征波长约 10 μm，而工程表面粗糙度可与此尺度相当甚至更小，高温下辐射贡献更不应凭直觉忽略。

## 6. 创新性判断

作者声明的创新包括：建立真实拓扑 TCR 模型并纳入 NFTR；用 fluctuational electrodynamics 计算异质界面远/近场辐射；分析温度、压力、介质和热流路径；用直接/间接实验验证；将 TCR 等效纳入 TEG 性能评价。

真实创新属于“多物理机制整合 + 工程量化”。NFTR 理论不是新理论，真实粗糙 TCR 也有前序工作，但把它们用于高超声速多界面 TEG，并把 NFTR 对 TCR 和输出功率的贡献数值化，是较强的工程科学贡献。

创新强度为强。尤其是结论中给出 NFTR 对 TE leg-electrode TCR 的降低范围 3.90%-17.0%（真空）和 1.30%-5.50%（空气），以及输出功率提升 0.883%-8.02%，让“近场效应重要”变成可用于设计的数字。

## 7. 论证链条复原

高超声速 TEG 需要高效热量收集 → 多材料内部界面产生 TCR 并削弱热电性能 → 粗糙间隙中的热传输不仅有固体传导，也有 FFTR/NFTR → 已有 TCR 模型和 TEG 研究对 NFTR、内部多界面和异质界面覆盖不足 → 本文测量并重构 substrate/electrode/TE leg 真实粗糙面 → 用接触力学得到间隙分布和真实接触区 → 用 fluctuational electrodynamics 计算辐射 TCC → 在 ABAQUS 中预测 TCR → 搭建实验平台测 TCR 验证模型 → 将 TCR 等效为 TEG 界面层 → 评估温差、电压和最大输出功率 → 得出 NFTR 在 TEG 性能评价中不可忽略。

链条闭合度很高。薄弱处在于实验测量温度和压力点较少，且 NFTR 的纳米尺度贡献在真实粗糙面统计中的空间分布很依赖表面测量精度和介质假设。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The proper characterization of rough sur face is essential in accurately estimating the TCR. The contribution of the thermal radiation to the total heat flux of “E-N_l”, “E-N_u”, “E-P_l” and “EP_u” reached about 48.9%, 46.6%, 71.4% and 81.6% at 725 K, respectively; in which the contribution of the NFTR is about 20.9%, 20.0%, 29.3% and 34.2%, respectively. 3 The NFTR effect is essential for precisely evaluate the TCRs at het erogeneous interfaces of TEGs.
- 已有研究不足/GAP：The result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively; and the maximum output power of the TEG increases by about 8.02% and 1.29% under vacuum and air clearance (0.1 MPa, 650 K), respectively. very limited real contact region and a large proportion of contact clearance.
- 本文解决方式：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions. First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the farand near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements. Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法名称：包含 NFTR 的真实拓扑多界面 TCR-TEG 性能预测模型。

输入：substrate、电极、N/P TE leg 粗糙面坐标；材料介电函数参数；加载压力/压缩位移；真空或空气间隙；热流方向；界面温度；TEG 几何和边界温度。

关键模型：

1. 接触变形模型：弹性/塑性平衡方程、几何方程和本构方程，获得真实接触区与间隙距离。
2. TCR 计算：`TCR = ΔT / (qc + qnr + qfr)`，其中固体传导、近场辐射和远场辐射共同构成热流。
3. 辐射计算：基于 fluctuational electrodynamics，将 propagating contribution 视为远场，evanescent contribution 视为近场；通过 Fresnel reflection coefficient 和材料 dielectric function 描述材料响应。
4. 材料介电函数：金属/半导体用 Drude model，alumina 用 oscillator model。
5. TEG 性能模型：将八个界面 TCR 等效为界面层，热导率等于层厚除以 TCR，在 ANSYS Multiphysics 中做热电耦合。

实验平台包括加热系统、压力装置、冷却系统和数据采集系统，测 substrates/electrodes/TE legs 组合样品的温度与电压信号。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| NFTR 需要纳入异质界面 TCR 模型 | 摘要/方法/结果 5.2 | Eq. (7)-(12) 将 NFTR/FFTR 与固体传导共同计入；Fig. 14-17 给出贡献 | 强 | 公式和曲线细节需 PDF 复核 |
| 近场辐射在纳米间隙下远高于远场辐射 | 结果 3.3/Fig. 4 | alumina-copper 在 1 nm 时 NFTR TCC 可比 FFTR 高 10^5 或 10^2 量级 | 强 | 依赖介电函数参数和理想平面近似 |
| 加载压力降低 TCR | 结果 5.1/5.2.4 | Fig. 9/20：真实接触面积随压力增大，五类接触对 TCR 随压力下降 | 强 | 高预压下 TE 材料损伤边界需更多验证 |
| 空气间隙下 TCR 小于真空间隙 | 结果 5.1/5.2 | Fig. 11-13：空气传导贡献使温度梯度小于真空间隙 | 强 | 微间隙中空气导热模型需边界适用性讨论 |
| 热流路径对 substrate-electrode TCR 有明显影响 | 结果 5.2.2 | Fig. 19：S-E 不同热流路径在真空 480 K 处最大差异约 10.0% | 中-强 | TE leg-electrode 路径不敏感，结论需限定对象 |
| 实验验证支持数值模型 | 结果 5.2.5/Table 5 | 五类接触对最大差异约 6.07%、-6.00%、-5.76%、6.56%、6.13% | 强 | 实验不确定度对 TE leg-electrode 达 10%-12% |
| NFTR 会改变 TEG 性能评估 | 结果 5.3/结论 | Fig. 21-22：考虑 NFTR 后最大输出功率提升 0.883%-8.02% | 强 | 系统模型边界较理想，实际飞行热边界更复杂 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 热接触模型示意 | 建立系统对象和微观机制 | 多界面 TEG 内部存在 TCR | TEG 应用在背风区，含八个关键界面 | 需要 PDF 图像复核 |
| Fig. 2 粗糙面测量/重构 | 支撑真实拓扑建模 | 减少理想粗糙假设 | substrate/electrode/TE legs 粗糙度参数 | 需要 PDF 图像复核 |
| Eq. (7)-(9) TCR/TCC | 将固体传导、FFTR、NFTR 合并 | TCR 计算框架 | TCR 由 qc、qnr、qfr 共同决定 | 公式排版需 PDF 复核 |
| Eq. (10)-(12) 波动电动力学热流 | 解释近/远场辐射来源 | NFTR 可定量计算 | propagating vs evanescent contribution | 公式排版需 PDF 复核 |
| Fig. 3 文献结果对比 | 验证辐射计算程序 | 计算程序可信 | 与公开文献近场热流/TCC 一致 | 需要 PDF 图像复核 |
| Fig. 4 辐射 TCC | 解释材料和间隙距离影响 | alumina-copper NFTR 强 | 1 nm 下 NFTR 远大于 FFTR | 曲线需 PDF 复核 |
| Fig. 9-13 接触面积/温度云图 | 从力学和温度场解释 TCR 变化 | 压力、介质影响 TCR | 接触面积增大、空气间隙温度梯度小 | 需要 PDF 图像复核 |
| Fig. 14-17 热辐射对 TCR/热流贡献 | 核心结果图 | NFTR/FFTR 降低 TCR | 真空下 TE leg-electrode 辐射贡献最高 | 需要 PDF 图像复核 |
| Table 5 实验-数值对比 | 验证模型 | 误差在可接受范围 | 最大差异约 6.56% 量级 | 可从 txt 确认 |
| Fig. 21-22 TEG 性能 | 系统级收束证据 | NFTR 提高输出功率 | 真空低压下影响更明显 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Thermal contact models；3 Numerical models；4 Experimental measurement platform for TCR；5 Results and discussions；6 Conclusion。结果节细分为 contact mechanics and heat transfer、thermal contact resistance、TEG performance。

布局是“机理先行 + 模型验证 + 系统应用”。第二节先从物理层面解释 TEG 多界面和 NFTR，第三节再给数值模型和公式，第四节给实验平台，第五节按尺度推进：接触对 → TCR 参数规律 → 实验验证 → TEG 性能。

标题命名较稳健，但 `5.2.1 The quantitative description of thermal radiation` 是一个较好的结果型小标题，直接告诉读者这一节要做贡献定量。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Thermal contact models（方法/模型/算法）
  - L3 p.3: 2.1 The multi-interface TEG and TCR（对象/模块/过渡章节）
  - L3 p.4: 2.2 Rough surfaces（对象/模块/过渡章节）
- L2 p.5: 3 Numerical models（方法/模型/算法）
  - L3 p.5: 3.1 Governing equations（对象/模块/过渡章节）
  - L3 p.5: 3.2 Calculation method of TCR（方法/模型/算法）
  - L3 p.6: 3.3 Evaluation of radiative heat transfer（对象/模块/过渡章节）
  - L3 p.7: 3.4 Model and meshed model（方法/模型/算法）
  - L3 p.9: 3.5 Boundary conditions（对象/模块/过渡章节）
- L2 p.10: 4 Experimental measurement platform for TCR（结果/验证/讨论）
- L2 p.11: 5 Results and discussions（结果/验证/讨论）
  - L3 p.11: 5.1 Contact mechanics and heat transfer（对象/模块/过渡章节）
  - L3 p.13: 5.2 Thermal contact resistance（对象/模块/过渡章节）
    - L4 p.13: 5.2.1 The quantitative description of thermal radiation（问题定义）
    - L4 p.16: 5.2.2 The influence of heat transfer path（对象/模块/过渡章节）
    - L4 p.17: 5.2.3 The influence of average interfacial temperature（对象/模块/过渡章节）
    - L4 p.17: 5.2.4 The influence of loading pressure（对象/模块/过渡章节）
    - L4 p.17: 5.2.5 The comparison with experimental results（结果/验证/讨论）
  - L3 p.19: 5.3 The evaluation of thermal radiation on TEG performance（对象/模块/过渡章节）
- L2 p.19: 6 Conclusion（结论/贡献回收）
- L2 p.20: CRediT authorship contribution statement（尾部材料）
- L2 p.20: Declaration of Competing Interest（尾部材料）
- L2 p.20: Data availability（尾部材料）
- L2 p.20: Acknowledgments（尾部材料）
- L2 p.20: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Thermal contact models | 3 | 2 | 方法/模型/算法 |
| 2.1 The multi-interface TEG and TCR | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Rough surfaces | 4 | 3 | 对象/模块/过渡章节 |
| 3 Numerical models | 5 | 2 | 方法/模型/算法 |
| 3.1 Governing equations | 5 | 3 | 对象/模块/过渡章节 |
| 3.2 Calculation method of TCR | 5 | 3 | 方法/模型/算法 |
| 3.3 Evaluation of radiative heat transfer | 6 | 3 | 对象/模块/过渡章节 |
| 3.4 Model and meshed model | 7 | 3 | 方法/模型/算法 |
| 3.5 Boundary conditions | 9 | 3 | 对象/模块/过渡章节 |
| 4 Experimental measurement platform for TCR | 10 | 2 | 结果/验证/讨论 |
| 5 Results and discussions | 11 | 2 | 结果/验证/讨论 |
| 5.1 Contact mechanics and heat transfer | 11 | 3 | 对象/模块/过渡章节 |
| 5.2 Thermal contact resistance | 13 | 3 | 对象/模块/过渡章节 |
| 5.2.1 The quantitative description of thermal radiation | 13 | 4 | 问题定义 |
| 5.2.2 The influence of heat transfer path | 16 | 4 | 对象/模块/过渡章节 |
| 5.2.3 The influence of average interfacial temperature | 17 | 4 | 对象/模块/过渡章节 |
| 5.2.4 The influence of loading pressure | 17 | 4 | 对象/模块/过渡章节 |
| 5.2.5 The comparison with experimental results | 17 | 4 | 结果/验证/讨论 |
| 5.3 The evaluation of thermal radiation on TEG performance | 19 | 3 | 对象/模块/过渡章节 |
| 6 Conclusion | 19 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 20 | 2 | 尾部材料 |
| Declaration of Competing Interest | 20 | 2 | 尾部材料 |
| Data availability | 20 | 2 | 尾部材料 |
| Acknowledgments | 20 | 2 | 尾部材料 |
| References | 20 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落推进非常密：工程背景、TEG 结构、TCR 预测方法、NFTR 基础、TCR 测量、TEG 性能影响，最后进入本文。它的特点是每段都在收窄 gap，而不是堆背景。

方法段落采用“定义物理对象 → 给公式 → 解释变量 → 给软件/网格/边界条件”的节奏。结果段落则采用典型的图驱动叙事：`Fig. X shows... As shown... In conclusion...`。每个结果小节都不只是描述曲线，而是解释为什么：真空间隙固体传导弱、空气传导贡献大、alumina/copper 近场 TCC 非对称等。

结论采用六条编号，覆盖模型、辐射贡献、NFTR 量化、热流路径、实验验证、TEG 性能，和正文证据一一对应。

## 13. 文笔画像与语言习惯

文笔偏高密度技术叙述，常见词有 thermal contact resistance, near-field thermal radiation, equivalent thermal conductance, heterogeneous interfaces, clearance medium, loading pressure, average interfacial temperature。

语气上，作者对核心 claim 很明确：`essential`, `cannot be ignored`, `crucial` 等词出现，但通常后接数值范围。方法部分被动语态多，如 “is established”, “is calculated”, “is validated”；结果部分用主动观察句 “One can find that...”。

时态稳定：文献事实用现在时，本文方法用过去/现在完成混合，图表发现用现在时。情态动词 `should`、`can` 常用于边界判断，如 “should not be neglected”。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：35129
- 高频词：thermal(61)；tcr(59)；clearance(53)；heat(52)；contact(42)；temperature(41)；radiation(36)；transfer(30)；electrodes(29)；vacuum(26)；surface(26)；legs(25)；nftr(25)；loading(25)；tcrs(25)；displacement(21)；pressure(20)；compression(20)；contacting(18)；air(18)
- 高频名词化/学术名词：clearance(53)；temperature(41)；radiation(36)；displacement(21)；pressure(20)；compression(20)；reduction(17)；influence(11)；distance(11)；conduction(10)；conductivity(8)；roughness(7)；prediction(7)；performance(7)；conductance(7)
- 高频学术动词：validated(7)；compared(6)；analyzed(5)；developed(4)；predict(2)；predicted(2)；derived(1)；estimated(1)；evaluated(1)；provided(1)；indicate(1)；evaluate(1)
- 高频形容词：thermal(61)；displacement(21)；interfacial(14)；real(13)；radiative(11)；thermoelectric(9)；heterogeneous(8)；optical(7)；coefficient(7)；dimensionless(7)；hypersonic(5)；fluctuational(5)；experimental(5)；geometric(5)；numerical(5)
- 高频副词：mainly(4)；experimentally(3)；equivalently(3)；quantitatively(3)；accurately(2)；tively(2)；exponentially(2)；relatively(2)；similarly(2)；actually(1)；recently(1)；approximately(1)；theoretically(1)；widely(1)；finally(1)
- 高频二词短语：thermal radiation(32)；heat transfer(26)；vacuum clearance(21)；compression displacement(19)；loading pressure(18)；air clearance(17)；reduction rate(15)；thermal contact(14)；legs electrodes(12)；interfacial temperature(12)；real contact(12)；substrates electrodes(11)
- 高频三词短语：average interfacial temperature(11)；vacuum clearance air(11)；near-field thermal radiation(8)；tcrs legs electrodes(8)；radiative heat transfer(7)；dimensionless real contact(7)；real contact area(7)；maximum reduction rate(7)；minimum reduction rate(7)；thermal contact resistance(6)；heat transfer paths(6)；far-field thermal radiation(6)
- 被动语态估计：49；`we + 动作动词` 主动句估计：0
- 一般现在时线索：137；一般过去时线索：137；现在完成时线索：0；情态动词线索：21

分章节正文词频：

- 1 Introduction: thermal(32)；heat(26)；electrodes(18)；radiation(17)；tcr(17)；contact(14)；teg(13)；transfer(13)
- 2 Thermal contact models: surface(11)；wave(7)；rough(5)；energy(4)；interface(4)；medium(4)；surfaces(4)；leg(4)
- 3 Numerical models: contact(13)；thermal(8)；heat(7)；equations(6)；temperature(5)；elastic(5)；ijkl(5)；tcc(5)
- 4 Experimental measurement platform for TCR: temperature(10)；test(6)；block(5)；heat(4)；system(4)；sample(3)；loading(3)；tcr(3)
- 5 Results and discussions: clearance(31)；tcr(28)；compression(19)；displacement(18)；loading(17)；vacuum(17)；reduction(17)；pressure(16)
- 6 Conclusion: thermal(10)；nftr(8)；tcr(7)；clearance(7)；effect(7)；radiation(6)；heat(6)；model(5)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`High efficiency heat harvest of hypersonic vehicles claims elaborate design of...`
- Gap 句式：`few of them consider...`; `the study of TE materials is very limited.`
- 方法句式：`A real-topology-based ... prediction model is developed...`
- 机理句式：`This is mainly due to...`
- 量化句式：`reduced by about X to Y under...`
- 验证句式：`the program calculation results ... are in good agreement with...`
- 边界句式：`It should be noted that...`
- 系统意义句式：`For a TEG containing about ... interfaces, it is crucial to consider...`

可复用表达：对复杂机理最好用“贡献范围”而非单点数值，例如 `about 3.90% to 17.0% under vacuum clearance`，能同时表达条件依赖和结论强度。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The proper characterization of rough sur face is essential in accurately estimating the TCR.
  可迁移模板：The proper characterization of rough sur face is essential in accurately estimating the METHOD.
- 原句：The proper characterization of rough sur face is essential in accurately estimating the TCR.
  可迁移模板：The proper characterization of rough sur face is essential in accurately estimating the METHOD.
- 原句：The contribution of the thermal radiation to the total heat flux of “E-N_l”, “E-N_u”, “E-P_l” and “EP_u” reached about 48.9%, 46.6%, 71.4% and 81.6% at 725 K, respectively; in which the contribution of the NFTR is about 20.9%, 20.0%, 29.3% and 34.2%, respectively. 3 The NFTR effect is essential for precisely evaluate the TCRs at het erogeneous interfaces of TEGs.
  可迁移模板：The contribution of the thermal radiation to the total heat flux of “E-N_l”, “E-N_u”, “E-P_l” and “EP_u” reached about X, X, X and X at METHOD, respectively; in which the contribution of the METHOD is about X, X, X and X, respectively. XThe METHOD effect is essential for precisely evaluate the TCRs at het erogeneous interfaces of TEGs.
#### Gap/转折句
- 原句：However, the above researches mainly concentrated in the effect of solid conduction on the heat transfer process, and few of them consider the far-field thermal radiation (FFTR) effect.
  可迁移模板：However, the above researches mainly concentrated in the effect of solid conduction on the heat transfer process, and few of them consider the far-field thermal radiation (METHOD) effect.
- 原句：The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
  可迁移模板：The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [X] and even reach a similar order of magnitude of heat conduction [X,X].
- 原句：Most of the current work involved in TEGs [34,36,37] are measured the TCR between the TEG and cold/ heat source, and only a few focused on the heterogeneous interfaces inside of the TEG.
  可迁移模板：Most of the current work involved in TEGs [X,X,X] are measured the METHOD between the METHOD and cold/ heat source, and only a few focused on the heterogeneous interfaces inside of the METHOD.
- 原句：For the influence of the TCR on the TEG, a lot of works in theoretical analysis [38] and numerical simula tions [39–42] are carried, but lack of complete and reliable data on the TCRs of the heterogeneous interfaces inside of TEGs.
  可迁移模板：For the influence of the METHOD on the METHOD, a lot of works in theoretical analysis [X] and numerical simula tions [X–X] are carried, but lack of complete and reliable data on the TCRs of the heterogeneous interfaces inside of TEGs.
#### 方法提出句
- 原句：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions.
  可迁移模板：In this paper, a thermal contact model encompassing near-field thermal radiation (METHOD) effects of TEGs with heterogeneous interfaces between substrates, electrodes and METHOD legs is established and experimentally validated in hypersonic conditions.
- 原句：First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the farand near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements.
  可迁移模板：First, a real-topology-based thermal contact resistance (METHOD) prediction model is developed and the farand near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements.
- 原句：Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
  可迁移模板：Third, the METHOD is equivalently considered in a METHOD perfor mance evaluation model and the METHOD effects is quantitatively counted.
- 原句：The rough surface can be reconstructed based on GW statistical model [7], Weier strass–Mandelbrot fractal ones [8], Euclidean geometric statistical ones [9], facial ones [10], and semi-deterministic-based approach [11].
  可迁移模板：The rough surface can be reconstructed based on METHOD statistical model [X], Weier strass–Mandelbrot fractal ones [X], Euclidean geometric statistical ones [X], facial ones [X], and semi-deterministic-based approach [X].
- 原句：Frekers et al. [13] proposed a micro-scale numerical method to predict the contact heat transfer based For hypersonic vehicles with the characteristics of slender configu ration and high-speed, the long-time flight in dense atmosphere will lead to serious aerodynamic heat concentration and accumulation [1,2].
  可迁移模板：Frekers et al. [X] proposed a micro-scale numerical method to predict the contact heat transfer based For hypersonic vehicles with the characteristics of slender configu ration and high-speed, the long-time flight in dense atmosphere will lead to serious aerodynamic heat concentration and accumulation [X,X].
#### 结果呈现句
- 原句：The results show some conclusions: 1 In the numerical prediction of the TCR, the thermal analysis is completed by considering of the solid conduction, the farand the near-field thermal radiation between the real-topology-based rough surfaces.
  可迁移模板：The results show some conclusions: XIn the numerical prediction of the METHOD, the thermal analysis is completed by considering of the solid conduction, the farand the near-field thermal radiation between the real-topology-based rough surfaces.
#### 贡献/增量句
- 原句：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions.
  可迁移模板：In this paper, a thermal contact model encompassing near-field thermal radiation (METHOD) effects of TEGs with heterogeneous interfaces between substrates, electrodes and METHOD legs is established and experimentally validated in hypersonic conditions.
- 原句：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions.
  可迁移模板：In this paper, a thermal contact model encompassing near-field thermal radiation (METHOD) effects of TEGs with heterogeneous interfaces between substrates, electrodes and METHOD legs is established and experimentally validated in hypersonic conditions.
- 原句：The authors [14] established a TCR prediction model based on the measured real topology and the model is validated by experiments.
  可迁移模板：The authors [X] established a METHOD prediction model based on the measured real topology and the model is validated by experiments.
- 原句：In this work, a thermal contact model encompassing NFTR of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic condi tions.
  可迁移模板：In this work, a thermal contact model encompassing METHOD of TEGs with heterogeneous interfaces between substrates, electrodes and METHOD legs is established and experimentally validated in hypersonic condi tions.
- 原句：Gao et al. with heterogeneous interfaces between substrates, electrodes and ther moelectric (TE) legs is established and experimentally validated in hy personic conditions.
  可迁移模板：Gao et al. with heterogeneous interfaces between substrates, electrodes and ther moelectric (METHOD) legs is established and experimentally validated in hy personic conditions.
#### 限制/边界句
- 原句：In traditional thermal protection system (TPS), the heat is mainly dissi pated by the thermal radiation of the insulated structure, whose size and weight could be unaffordable under hypersonic conditions [2,3].
  可迁移模板：In traditional thermal protection system (METHOD), the heat is mainly dissi pated by the thermal radiation of the insulated structure, whose size and weight could be unaffordable under hypersonic conditions [X,X].
- 原句：Xian et al. [26] adopted the fluctuational electrody namics to calculate the NFTR on the TCR, and found that the NFTR should not be neglected even at room temperature when the effective roughness is near to the submicron scale.
  可迁移模板：Xian et al. [X] adopted the fluctuational electrody namics to calculate the METHOD on the METHOD, and found that the METHOD should not be neglected even at room temperature when the effective roughness is near to the submicron scale.
- 原句：Chen et al. [27] predicted the high temperature TCR between HTA and C/ZrB2-SiC considering NFTR, and found that the TCR account for the solid conduction and the thermal radiation is reduced to 1/25 of that only considering the solid conduc tion at 1100 K.
  可迁移模板：Chen et al. [X] predicted the high temperature METHOD between METHOD and C/ZrB2-SiC considering METHOD, and found that the METHOD account for the solid conduction and the thermal radiation is reduced to X/Xof that only considering the solid conduc tion at METHOD.
- 原句：Most of the current work involved in TEGs [34,36,37] are measured the TCR between the TEG and cold/ heat source, and only a few focused on the heterogeneous interfaces inside of the TEG.
  可迁移模板：Most of the current work involved in TEGs [X,X,X] are measured the METHOD between the METHOD and cold/ heat source, and only a few focused on the heterogeneous interfaces inside of the METHOD.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是“从工程系统到基础机理再回工程系统”。前几条引用高超声速 TPS/TEG，本团队前作较多，用来建立工程连续性；中段引用粗糙面 TCR 经典模型和测量方法；再引用 NFTR 基础与最新研究，说明近场效应不是附会；最后引用 TEG TCR 和性能影响文献，指出内部异质界面数据不足。

作者对前人态度多为补充式批判：已有粗糙面模型有假设，已有 TEG TCR 多关注外界面或局部界面，已有 NFTR 材料体系不是 TE materials。这样的引用让本文显得是沿着前人缺口自然推进。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：96
- Introduction 引文簇数量估计：28
- References 条目数：50
- 可识别年份条目数：86
- 2021 年及以后文献数：20
- 2010 年前经典文献数：13
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：International Journal of Heat and Mass Transfer(1)
- 引文簇样例：[1,2], [2,3], [7], [8], [9], [10], [11], [12], [13], [14], [23], [15]

带引文的 gap/转折句样例：

- The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
- For the studies of TCRs with near-filed effect, Persson et al. [25] approximately estimated the influence of the NFTR on the TCR at the first time, and found that the contribution of the radiative heat transfer is not weaker than that of the solid conduction.
- Xian et al. [26] adopted the fluctuational electrody namics to calculate the NFTR on the TCR, and found that the NFTR should not be neglected even at room temperature when the effective roughness is near to the submicron scale.
- Most of the current work involved in TEGs [34,36,37] are measured the TCR between the TEG and cold/ heat source, and only a few focused on the heterogeneous interfaces inside of the TEG.

References 解析样例（前 8 条）：

- [1] J.J. Gou, J.X. Hu, Z.W. Yan, G. Gao, C.L. Gong, Effects of physical dimensions, temperature ranges and interfacial thermal contacts on the multi-stage thermoelectric generators for a hypersonic vehicle, Int. J. Energy Res. (2022) 1–18, https://doi.org/10.1002/er.7799.
- [2] J.J. Gou, Z.W. Yan, J.X. Hu, G. Gao, C.L. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021), 106373, https://doi. org/10.1016/j.ast.2020.106373.
- [3] B.X. Shen, W.Q. Liu, Insulating and absorbing heat of transpiration in a combinational opposing jet and platelet transpiration blunt body for hypersonic vehicle, Int. J. Heat Mass Transf. 138 (2019) 314–325, https://doi.org/10.1016/j. ijheatmasstransfer.2019.04.057.
- [4] G. Gao, J.J. Gou, C.L. Gong, J.X. Hu, R.C. Gao, A novel mechanical-thermalelectrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021), 113962, https://doi.org/10.1016/j.compstruct.2021.113962.
- [5] C.L. Gong, J.J. Gou, J.X. Hu, F. Gao, A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470, https://doi.org/10.1016/j.ast.2018.03.028.
- [6] K. Cheng, J. Qin, Y. Jiang, C. Lv, S. Zhang, W. Bao, Performance assessment of multi-stage thermoelectric generators on hypersonic vehicles at a large temperature difference, Appl. Therm. Eng. (2018) 1598–1609, https://doi.org/ 10.1016/j.applthermaleng.2017.11.057.
- [7] J.A. Greenwood, J.B.P. Williamson, Contact of nominally flat surfaces, Proc. R. Soc. Lond. Ser. A Math. Phys. Sci. 295 (1966) 300–319, https://doi.org/10.1098/ rspa.1966.0242.
- [8] M.V. Berry, Z.V Lewis, On the Weierstrass-Mandelbrot fractal function, Proc. R. Soc. Lond. A Math. Phys. Sci. 370 (1980) 459–484, https://doi.org/10.1098/ rspa.1980.0044.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. NFTR 计算使用局部平面/介电函数框架，真实粗糙、涂层、氧化和污染对近场耦合的影响可能复杂。
2. 实验验证点数量有限，且 TE leg-electrode TCR 不确定度约 10%-12%，比数值误差同量级。
3. 空气微间隙传导是否需要考虑稀薄气体或 Knudsen 效应，文本中讨论不足。
4. TEG 性能模型边界为 650 K/300 K 和少量压力/介质条件，距离真实飞行热边界仍有简化。
5. 接触状态采用 step-by-step coupling，温度对接触变形影响被认为有限，但高温热膨胀可能改变界面。
6. 多界面 TCR 与 ECR、热机械应力、材料退化的长期耦合没有同时讨论。

## 17. 可复用资产

- 选题套路：把“已知但常被忽略的微尺度效应”放进具体工程器件，量化其系统后果。
- 论证套路：基础物理公式验证 → 接触对仿真 → 实验验证 → 系统性能评估。
- 图表设计：先用 Fig. 4 证明近场热辐射量级，再用 Fig. 14-17 证明对 TCR 的贡献，最后用 Fig. 22 证明对输出功率的贡献。
- 句式资产：`It is necessary to consider X when Y has large difference in magnitude.`
- 风险控制：用真空/空气、正/负热流路径、不同温度/压力多条件展开，避免单一条件过度外推。

## 18. 对我写论文的启发

如果我的研究涉及多物理耦合，不应只把新机理放在理论层解释，而要像本文一样做三重验证：先与公开文献验证基础计算程序，再与实验验证工程模型，最后放入系统模型展示性能影响。

Introduction 可学习其 gap 组合方式：不是单一“没人做过”，而是“已有 TCR 模型 + 已有 NFTR 理论 + 已有 TEG 应用”三者之间没有完成真实多界面闭环。

## 19. 最终浓缩

本文最强之处是把 NFTR 从传热物理概念变成高超声速多界面 TEG 性能评估中可计量的设计因素。它证明 NFTR 可使 TE leg-electrode TCR 在真空下降低 3.90%-17.0%，并让 TEG 最大输出功率提升最高约 8.02%。最可复用的是“机理公式-程序验证-真实形貌仿真-实验验证-系统性能”的完整证据链；最大风险是近场模型和真实服役界面的复杂性仍需更多实验覆盖。
