# Numerical investigation of the effects of different parameters on the thrust performance of three dimensional flapping wings

## 0. 读取说明

本拆解基于 `801/文本/txt/Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie.txt` 的全文抽取。文本包含公式、图题、表格和结论，但存在 OCR 中 “trust/thrust” 等拼写混杂。本拆解按论文语境统一理解为 thrust。涡量云图、Q-criterion 涡结构和速度云图细节需 PDF 图像复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Numerical method and validation, 3 Independence validation, 4 Results and discussions, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Numerical investigation of the effects of different parameters on the thrust performance of three dimensional flapping wings。
- 作者：Chunlin Gong、Jiakun Han、Zongjing Yuan、Zhe Fang、Gang Chen。
- 期刊：Aerospace Science and Technology，84，2019，431-445。
- 领域：仿生扑翼推进、三维非定常流、IB-LBM、涡结构机制。
- 论文类型：数值方法验证 + 参数影响研究。
- 研究对象：三维 pitching-heaving 扑翼在不同翼型、展弦比、pitch-bias angle 下的推力性能和涡结构。
- 主要方法：D3Q19 Lattice Boltzmann Method + immersed boundary method，虚拟边界力模型，TianHe-II 大规模并行计算。
- 核心输出：升力/推力系数、周期平均速度场、翼展对称面涡量、Q-criterion 三维尾涡结构。

## 2. 摘要与核心信息提取

一句话主张：大规模并行 IB-LBM 能解析三维扑翼细致涡结构，并显示翼型、展弦比和偏置攻角通过改变前缘涡、尾缘涡和尾迹射流来显著影响推力性能，其中椭圆翼推力最佳，NACA0012 在 AR=3 附近推力最大，偏置攻角增大会迅速降低推力甚至转为阻力。

摘要的信息组织很直接：先从自然界扑翼飞行/游动引入仿生价值；再指出几何、运动和流动参数众多，传统模拟难以系统探索；然后提出并行 IB-LBM；结果层面先说分析 leading edge vortex 和 wake vortex，再给三个参数结论；最后强调 TianHe-II 和千万级网格带来的三维流场解析能力。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie.md`。

中文译文：

> 文章历史记录： 2018年5月24日收到 2018年9月26日以修订形式收到 2018年10月18日接受 2018年10月23日在线提供
>
> 经过数十亿年的进化，自然界中许多使用扑翼的生物往往具有出色的飞行能力。了解仿生机翼的流动机理将有助于设计高性能水下航行器和新概念飞行器。几何参数、运动学参数和流动参数对仿生机翼推力性能影响较大。面对多样的参数，用传统的数值模拟方法很难探索三维（3D）仿生扑翼流动机理。在本文中，开发了一种使用浸入边界格子玻尔兹曼方法（IB-LBM）的通用大规模并行求解器。详细分析了3D扑翼前缘涡和尾流涡结构的演化过程。我们的研究解释了 3D 扑翼推力性能随不同机翼形状、展弦比和俯仰偏攻角的变化。使用中国超级计算机天河二号为并行IB-LBM的进一步发展提供了广泛的可能性，采用千万级网格将有助于我们获得更完整、更准确的3D扑翼流场信息。
>
> 表明与其他尖翼形状相比，钝翼具有最好的推力性能。随着展弦比的增大，扑翼的推力系数先增大后减小，并且随着偏航角的增大，推力系数迅速减小，甚至在大偏航角时出现阻力现象。这些参数的讨论将为提高扑翼飞行器推进性能提供理论依据。 © 2018 Elsevier Masson SAS。版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自仿生飞行/水下推进设计中的两个需求：一是理解三维扑翼如何产生推力，二是在参数空间中找到有利于推进的几何和运动设置。传统二维扑翼能解释 reverse Karman vortex street，但忽略翼展方向变化和三维尾涡拓扑；实验又昂贵、细节有限、重复性不足。

作者把研究范围收束为三类参数：翼型、展弦比、pitch-bias angle。这个收束清楚且工程可用，因为它们都是仿生翼设计中可直接调整的形状/运动控制变量。

选题价值主要在三维机制：文章不是只报推力系数，而是用平均速度射流、前缘涡贴附程度、涡环完整性、尾涡交织/破裂来解释为什么某些参数组合更优。

## 4. 领域位置与文献版图

文献版图从仿生推进优势讲起，随后分实验、理论、数值三类。理论如 Lighthill 大振幅细长体理论能给简化水动力解释，但结构和运动参数受限；实验如风洞/PIV 能测力和部分流场，但成本高且细节不足；数值模拟适合解析流场细节，但传统 body-fitted CFD 在移动边界和大网格上成本高。

本文站在 IBM 和 LBM 结合路线之后。IBM 避免移动边界重构网格，LBM 使用 Cartesian grids、并行性好，二者结合适合大变形/主动运动边界问题。作者的定位是用大规模并行 IB-LBM 进入传统二维研究难以覆盖的三维参数机制。

## 5. Gap 制造机制

Gap 的核心是：大量扑翼参数研究仍基于二维或大展弦比近似，三维几何变化对推力的影响和涡拓扑机制没有被充分解析；传统 CFD 又受网格体量和移动边界效率限制。

作者制造 gap 的方式是先承认已有二维研究提供了 reverse Karman、Strouhal、攻角等粗解释，再指出三维涡结构远比二维复杂，翼尖涡、涡环破裂和三维尾迹会改变推力。因此需要可在千万级网格上解析三维流场的并行 IB-LBM。

## 6. 创新性判断

作者声明的创新包括：开发/使用三维并行 IB-LBM 求解器；详细分析三维扑翼前缘涡和尾涡演化；解释翼型、展弦比、偏置攻角对推力性能的影响。

真实创新偏工程数值研究。IB-LBM 不是全新方法，但将其用于三维扑翼大规模参数研究，并将推力差异与涡结构可视化联系起来，有应用价值。创新强度中等，最大贡献是数据和机制图谱，而非理论模型。

易被挑战的是参数范围不够广：暂时不考虑频率、振幅、Re、St、柔性等关键变量；结论更像在固定运动模式下的局部规律。

## 7. 论证链条复原

1. 仿生扑翼具有高机动和高推进潜力，需要理解推力机制。
2. 三维效应对扑翼推力重要，但二维研究和传统 CFD 难以充分解析。
3. IB-LBM 适合固定 Cartesian 网格和移动边界，适合大规模并行。
4. 先用三维椭圆扑翼算例验证 IB-LBM 与文献 NS-IBM 结果一致，再做网格/时间步独立性。
5. 固定基本运动和 Re/St 等参数，分别改变翼型、展弦比和 pitch-bias angle。
6. 通过升力/推力系数给出定量性能，通过平均速度场和涡量/Q-criterion 给出机制解释。
7. 翼型影响前缘涡贴附和尾涡完整性：椭圆/NACA0012 优于 cuboid。
8. 展弦比存在最优：AR 从 1 到 3 推力增加，继续到 5/7 推力下降。
9. 偏置攻角增加打破对称射流，增强尾缘涡并降低推力，20/30 度甚至出现阻力。
10. 结论把参数规律回扣到 leading edge vortex 和 wake vortex 演化。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The effect of the structural flexibility is also very important and obvious for true fish, insects and birds.
- 已有研究不足/GAP：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5]. Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 本文解决方式：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. In this paper, a general largescale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed. Using Chinese supercomputer TianHeII presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
- 学术或工程增量：The discussion of these parameters will provide a theoretical basis for improving flapping-like vehicles propulsive performance. © 2018 Elsevier Masson SAS.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

流场用 D3Q19 LBM，离散粒子分布函数 fi 在格点间碰撞迁移，平衡分布包含速度二阶项，粘性系数与松弛时间 tau 相关。宏观速度和压力由分布函数求和得到。

移动边界用 immersed boundary method。IBM 把物体边界作用转成流体内部力，不需要每步重建 body-fitted mesh。由于研究对象是刚性主动扑翼，作者选择 virtual boundary model，集中力由速度反馈和速度积分项构造，再扩散到 Euler 网格。

运动模式是 pitching-heaving：翼中心按 Z(t)=Az sin(2 pi f t) heave，同时绕中心 pitch，theta(t)=alpha0+A_theta sin(2 pi f t+phi)。无量纲参数包括 St=2Az f/U_inf，Re=U_inf L/nu。推力/升力系数用 0.5 rho U_inf^2 A' 归一化。

验证包括两个层次：与 Dong 等三维椭圆扑翼文献力系数对比；NACA0012 扑翼的网格独立性（28.1M、48.6M、77.1M，总体误差约 0.86%-1.3%）和时间步独立性（dt=0.0005/0.001/0.0015，误差 1.6%/0.08%）。

参数设置：翼型比较含 ellipsoidal、NACA0012、cuboid；展弦比 AR=1、2、3、5、7；偏置攻角 alpha0=0、10、20、30 度。其他运动参数保持验证算例设置。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| IB-LBM 求解器能可靠模拟三维扑翼 | 2.4/3 | Fig. 1 与 Dong 文献力系数吻合；网格/时间步独立性表 | 强 | 只展示特定验证算例 |
| 椭圆翼推力最好，cuboid 最差 | 4.2 | 平均推力系数：ellipsoidal 0.4809，NACA0012 0.4587，cuboid 0.1125 | 强 | 翼型比较只在固定 AR/alpha0 |
| 前缘涡贴近且饱满会增强推力 | 4.2 | Fig. 10 局部涡量；椭圆翼 V1 更贴近翼面且更强 | 中强 | 图像细节需 PDF 图像复核 |
| 尾涡结构完整性解释推力差异 | 4.2 | Fig. 12 Q-criterion，cuboid 涡环交织破裂导致尾流速度减弱 | 中强 | Q 阈值敏感性未讨论 |
| 展弦比存在非单调最优 | 4.3 | 平均推力系数 AR1/2/3/5/7 为 0.3426/0.4587/0.5098/0.3852/0.1997 | 强 | 只在 NACA0012、固定运动参数 |
| pitch-bias angle 增大显著降低推力甚至变阻力 | 4.4 | 平均推力系数 0/10/20/30 度为 0.5098/0.3714/-0.0104/-0.5055 | 强 | 大攻角下流动状态和失速机制需更细验证 |
| 推力变化可由前缘涡、尾缘涡和尾迹射流解释 | 4.2-4.4/结论 | 平均速度云图、涡量图、Q-criterion 图组 | 中强 | 因果主要基于可视化相关 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Eq. 1-8 | LBM 控制方程 | 方法可计算流场 | D3Q19、粘性/压力/速度闭合 | 文本可确认 |
| Eq. 9-14 | IBM 和虚拟边界力 | 移动边界高效处理 | 边界力由速度反馈构造 | 文本可确认 |
| Eq. 15-18 | 扑翼运动和力系数定义 | 参数研究可归一化 | heaving/pitching、St、Re、CT、CL | 文本可确认 |
| Fig. 1/Table 2 | 求解器验证 | IB-LBM 可信 | 与文献力系数吻合 | 需要 PDF 图像复核 |
| Fig. 3-6/Tables 3-4 | 网格和时间独立性 | 数值结果稳定 | nominal 48.6M 网格、dt=0.001 合理 | 需要 PDF 图像复核 |
| Fig. 7-12 | 翼型影响 | 椭圆/NACA 优于 cuboid | 前缘涡强、尾涡完整带来高推力 | 需要 PDF 图像复核 |
| Fig. 13-16 | 展弦比影响 | AR=3 最优 | 尾迹射流和涡结构随 AR 非单调变化 | 需要 PDF 图像复核 |
| Fig. 17-19 | 偏置攻角影响 | alpha0 增大降低推力 | 非对称射流、尾缘涡增强 | 需要 PDF 图像复核 |
| Table 5 | 参数空间总览 | 研究范围清楚 | 三类参数逐项变化 | 文本可确认 |

## 11. 章节结构与篇章布局

章节为 Introduction -> Numerical method and validation -> Independence validation -> Results and discussions -> Conclusions。Results 内部按参数分块：problem statement、wing shape、aspect ratio、pitch-bias angle。

结构很传统但有效。前两章为“方法可信度”服务，第三章为“数值收敛性”服务，第四章才进入物理结果。这样安排对数值论文很重要，因为如果求解器和网格不可信，后面的涡机制解释就没有根基。

标题命名偏描述型，直接暴露变量，如 “The influence of wing shape on thrust performance”。这类标题适合参数研究型论文。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Numerical method and validation（方法/模型/算法）
  - L3 p.2: 2.1 The lattice Boltzmann method（方法/模型/算法）
  - L3 p.3: 2.2 The immersed boundary method（方法/模型/算法）
  - L3 p.3: 2.3 The IB-LBM（对象/模块/过渡章节）
  - L3 p.3: 2.4 Solver validation（结果/验证/讨论）
- L2 p.4: 3 Independence validation（结果/验证/讨论）
  - L3 p.4: 3.1 Mesh independence validation（结果/验证/讨论）
  - L3 p.5: 3.2 Time independence validation（结果/验证/讨论）
- L2 p.5: 4 Results and discussions（结果/验证/讨论）
  - L3 p.5: 4.1 Problem statement（问题定义）
  - L3 p.6: 4.2 The inﬂuence of wing shape on thrust performance（对象/模块/过渡章节）
  - L3 p.10: 4.3 The inﬂuence of aspect ratio on thrust performance（对象/模块/过渡章节）
  - L3 p.12: 4.4 The inﬂuence of pitch-bias angle of attack on thrust performance（对象/模块/过渡章节）
- L2 p.12: 5 Conclusions（结论/贡献回收）
- L2 p.14: Conﬂict of interest statement（对象/模块/过渡章节）
- L2 p.14: Acknowledgements（尾部材料）
- L2 p.14: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Numerical method and validation | 2 | 2 | 方法/模型/算法 |
| 2.1 The lattice Boltzmann method | 2 | 3 | 方法/模型/算法 |
| 2.2 The immersed boundary method | 3 | 3 | 方法/模型/算法 |
| 2.3 The IB-LBM | 3 | 3 | 对象/模块/过渡章节 |
| 2.4 Solver validation | 3 | 3 | 结果/验证/讨论 |
| 3 Independence validation | 4 | 2 | 结果/验证/讨论 |
| 3.1 Mesh independence validation | 4 | 3 | 结果/验证/讨论 |
| 3.2 Time independence validation | 5 | 3 | 结果/验证/讨论 |
| 4 Results and discussions | 5 | 2 | 结果/验证/讨论 |
| 4.1 Problem statement | 5 | 3 | 问题定义 |
| 4.2 The inﬂuence of wing shape on thrust performance | 6 | 3 | 对象/模块/过渡章节 |
| 4.3 The inﬂuence of aspect ratio on thrust performance | 10 | 3 | 对象/模块/过渡章节 |
| 4.4 The inﬂuence of pitch-bias angle of attack on thrust performance | 12 | 3 | 对象/模块/过渡章节 |
| 5 Conclusions | 12 | 2 | 结论/贡献回收 |
| Conﬂict of interest statement | 14 | 2 | 对象/模块/过渡章节 |
| Acknowledgements | 14 | 2 | 尾部材料 |
| References | 14 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

每个参数小节基本遵循同一节奏：先说明参数设置；再读平均速度云图预测推力趋势；再用力系数量化；最后用涡量/Q-criterion 解释机制。这种重复结构降低读者理解成本。

翼型小节的叙事最完整：先从动量定理和射流速度判断推力，再给平均推力系数，最后细化到前缘涡和涡环完整性。展弦比和偏置攻角小节延续同样模式。

结论段紧凑地回收三类参数规律，并把未来工作限制在 Re、St、振幅、频率、厚度、前缘曲率和柔性 FSI 上。

## 13. 文笔画像与语言习惯

文笔偏早期工程数值论文，语言直接，有少量语法不自然之处，但逻辑明确。高频词包括 flapping wing、thrust performance、vortex structure、leading edge vortex、wake flow、aspect ratio、pitch-bias angle、IB-LBM。

常用表达是 “It can be seen that”、“This indicates that”、“In order to explain the mechanism”、“From the perspective of...” 这些句式有很强的图表解读感。claim 强度多靠数值和云图支撑，少用复杂修辞。

时态上，方法用现在时，结果用现在时读图，结论用过去式/现在时混用。被动语态较多，但机制解释常用主动因果，如 “the trailing edge vortex increases, which leads to...”

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：39702
- 高频词：wing(143)；thrust(82)；flapping(80)；vortex(77)；performance(45)；flow(40)；velocity(38)；aspect(33)；wings(29)；parameters(29)；time(28)；different(26)；ratio(26)；fluid(26)；force(26)；edge(25)；angle(25)；pitch-bias(24)；average(24)；leading(23)
- 高频名词化/学术名词：performance(45)；velocity(38)；mechanism(18)；motion(16)；structure(16)；influence(13)；movement(12)；distribution(11)；simulation(10)；independence(10)；equation(9)；direction(9)；information(8)；evolution(7)；density(7)
- 高频学术动词：compared(6)；developed(3)；indicated(3)；reveal(3)；analyzed(2)；provide(2)；develop(2)；validate(2)；analyze(2)；indicate(2)；achieved(1)；constructed(1)；compare(1)；identify(1)；presented(1)
- 高频形容词：different(26)；coefficient(23)；boundary(23)；three-dimensional(19)；bionic(15)；numerical(14)；movement(12)；two-dimensional(11)；ellipsoidal(10)；traditional(7)；consistent(6)；geometric(5)；theoretical(5)；experimental(5)；quantitative(5)
- 高频副词：firstly(4)；obviously(4)；significantly(4)；gradually(4)；widely(3)；clearly(3)；quickly(2)；especially(2)；basically(2)；relatively(2)；particularly(1)；early(1)；experimentally(1)；systematically(1)；accurately(1)
- 高频二词短语：flapping wing(43)；thrust performance(32)；aspect ratio(26)；leading edge(23)；flapping wings(21)；edge vortex(17)；thrust coefficient(17)；pitch-bias angle(17)；angle attack(15)；average velocity(15)；vortex structure(12)；naca wing(12)
- 高频三词短语：leading edge vortex(15)；pitch-bias angle attack(11)；mesh time step(7)；flow field information(5)；increase aspect ratio(5)；immersed boundary method(5)；flapping wing thrust(4)；wing thrust performance(4)；bionic flapping wing(4)；wake flow vortex(4)；virtual boundary model(4)；average thrust coefficient(4)
- 被动语态估计：68；`we + 动作动词` 主动句估计：1
- 一般现在时线索：224；一般过去时线索：205；现在完成时线索：1；情态动词线索：45

分章节正文词频：

- 1 Introduction: flapping(33)；wing(25)；flow(19)；parameters(18)；performance(17)；method(15)；thrust(13)；numerical(12)
- 2 Numerical method and validation: fluid(20)；force(14)；model(13)；boundary(13)；wing(10)；velocity(7)；lattice(6)；density(6)
- 3 Independence validation: time(14)；independence(8)；mesh(6)；step(6)；wing(5)；grid(5)；direction(4)；naca(3)
- 4 Results and discussions: wing(91)；vortex(60)；thrust(55)；velocity(31)；flapping(30)；aspect(24)；average(22)；edge(21)
- 5 Conclusions: wing(12)；thrust(10)；flapping(9)；performance(8)；vortex(6)；wings(4)；aspect(4)；ratio(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：To understand the flow mechanism will be helpful to design...
- Gap 句式：It is necessary to overcome the problem of mesh volume and moving boundary...
- 方法句式：A general large-scale parallel solver using IB-LBM was developed.
- 验证句式：The numerical results were in good agreement with...
- 结果句式：With the increase of X, the thrust coefficient increases firstly and then decreases.
- 机制句式：A leading edge vortex that is closer to the wing surface and has stronger vortex strength results in greater thrust.
- 未来工作句式：In future work, much more parameters such as... would be further investigated.

可复用术语：pitching-heaving motion、leading-edge vortex、trailing-edge vortex、wake jet、Q-criterion、spanwise symmetry plane、average thrust coefficient、large-scale parallel solver。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：It still is a great challenge to develop more high-resolution and cheaper experimental techniques.
  可迁移模板：It still is a great challenge to develop more high-resolution and cheaper experimental techniques.
- 原句：Dash et al. pointed out flapping wing experiences thrust deterioration when the flapping frequency exceeds a certain critical value basing on N–S method [18], which need choose new angle of attack profiles.
  可迁移模板：Dash et al. pointed out flapping wing experiences thrust deterioration when the flapping frequency exceeds a certain critical value basing on N–S method [X], which need choose new angle of attack profiles.
- 原句：However, for the parameters analysis of the hydrodynamic mechanism for three-dimensional flapping wings, it is very important and useful to capture much more details of the evolution procedure of the unsteady vortex structures in much larger scale simulations.
  可迁移模板：However, for the parameters analysis of the hydrodynamic mechanism for three-dimensional flapping wings, it is very important and useful to capture much more details of the evolution procedure of the unsteady vortex structures in much larger scale simulations.
- 原句：The LBM solvers have the same numerical accuracy as the NS solver under the unremitting efforts of many scholars, which has become an important tool for simulating complex flow in a broad application prospect [39–42].
  可迁移模板：The METHOD solvers have the same numerical accuracy as the METHOD solver under the unremitting efforts of many scholars, which has become an important tool for simulating complex flow in a broad application prospect [X–X].
- 原句：To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation.
  可迁移模板：To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation.
#### Gap/转折句
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  可迁移模板：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (METHOD) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 原句：The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5].
  可迁移模板：The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [X–X].
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  可迁移模板：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (METHOD) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 原句：However, experiment research for bionic movement has also some disadvantages, such as poor repeatability, lack of enough detail of the flow field and also very expensive.
  可迁移模板：However, experiment research for bionic movement has also some disadvantages, such as poor repeatability, lack of enough detail of the flow field and also very expensive.
- 原句：However, it is necessary to overcome the problem of mesh volume and moving boundary using traditional CFD method to solve three-dimensional problems.
  可迁移模板：However, it is necessary to overcome the problem of mesh volume and moving boundary using traditional METHOD method to solve three-dimensional problems.
#### 方法提出句
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  可迁移模板：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (METHOD) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 原句：In this paper, a general largescale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed.
  可迁移模板：In this paper, a general largescale parallel solver using Immersed Boundary-Lattice Boltzmann Method (METHOD) was developed.
- 原句：Using Chinese supercomputer TianHeII presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
  可迁移模板：Using Chinese supercomputer TianHeII presents a wide range of possibilities for the further development of parallel METHOD, employing tens of millions grids will help us to obtain more complete and accurate METHOD flapping wing flow field information.
- 原句：With the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [1].
  可迁移模板：With the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [X].
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  可迁移模板：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (METHOD) bionic flapping wing flow mechanism with traditional numerical simulation method.
#### 结果呈现句
- 原句：It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
  可迁移模板：It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
- 原句：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack.
  可迁移模板：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack.
- 原句：It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
  可迁移模板：It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
- 原句：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack.
  可迁移模板：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack.
- 原句：Theoretical analysis can give quantitative hydrodynamic results by means of simplified approximation and explains the inherent fluid mechanism of like-flapping fish swimming.
  可迁移模板：Theoretical analysis can give quantitative hydrodynamic results by means of simplified approximation and explains the inherent fluid mechanism of like-flapping fish swimming.
#### 贡献/增量句
- 原句：The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement.
  可迁移模板：The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement.
- 原句：Experimental investigation can obtain force and some flow field information to further reveals the nature of the bionic movements and provide basis test data for numerical method.
  可迁移模板：Experimental investigation can obtain force and some flow field information to further reveals the nature of the bionic movements and provide basis test data for numerical method.
- 原句：The deformation of the wing involving the moving boundary can improve the performance of the flapping wing MAV.
  可迁移模板：The deformation of the wing involving the moving boundary can improve the performance of the flapping wing METHOD.
#### 限制/边界句
- 原句：For example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius.
  可迁移模板：For example, the turning radius of anglerfish is only X of its body length [X], while the underwater vehicle has to reduce more than X of its speed to decrease the turning radius.
- 原句：In particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture.
  可迁移模板：In particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture.
- 原句：But the theoretical analysis can only solve the bionic movement with very simple structures and simple movement parameters.
  可迁移模板：But the theoretical analysis can only solve the bionic movement with very simple structures and simple movement parameters.
- 原句：In fact, in the two-dimensional approximation, only the cross-flow component of the vorticity is considered.
  可迁移模板：In fact, in the two-dimensional approximation, only the cross-flow component of the vorticity is considered.
- 原句：The evolution procedures of the leading edge vortex and wake flow vortex structures are the possible main reasons which could be used to explain the thrust performance changes with parameter variation of the flapping wing.
  可迁移模板：The evolution procedures of the leading edge vortex and wake flow vortex structures are the possible main reasons which could be used to explain the thrust performance changes with parameter variation of the flapping wing.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是先铺仿生运动背景，再列实验、理论、数值方法，最后引出 IBM/LBM。作者引用 Lighthill 等理论、PIV/风洞实验、NS/IBM/DNS 数值研究、Peskin IBM 和 LBM 相关基础文献，为“为什么需要并行 IB-LBM”服务。

引用在 Introduction 密度高，Results 中较少。方法部分引用主要用于数值格式来源，验证部分引用 Dong 的三维椭圆扑翼作为 benchmark。整体引用姿态以继承为主，不强批判前人。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：90
- Introduction 引文簇数量估计：20
- References 条目数：58
- 可识别年份条目数：58
- 2021 年及以后文献数：0
- 2010 年前经典文献数：28
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Aerospace Science and Technology(1)
- 引文簇样例：[1], [9], [2], [10], [11], [12], [36], [13], [14], [37], [38], [15]

带引文的 gap/转折句样例：

- The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5].

References 解析样例（前 8 条）：

- [1] Brian P. Danowsky, et al., Incorporation of feedback control into a high-fidelity aeroservoelastic fighter aircraft model, J. Aircr. 47 (4) (2012) 1274–1282.
- [2] Paolo Domenici, R.W. Blake, The kinematics and performance of the escape response in the angelfish (Pterophyllum eimekei), Can. J. Zool. 71 (11) (1991) 2319–2326.
- [3] M.F. Platzer, et al., Flapping wing aerodynamics: progress and challenges, AIAA J. 46 (9) (2008) 2136–2149.
- [4] W. Shyy, et al., Aerodynamics, sensing and control of insect-scale flapping-wing flight, Proc. Math. Phys. Eng. Sci. 472 (2186) (2016) 20150712.
- [5] Farooq Umar, M. Sun, Aerodynamic force and power for flapping wing at low Reynolds number in ground effect, in: International Bhurban Conference on Applied Sciences and Technology, 2018, pp. 553–558.
- [6] George V. Lauder, et al., Design and Performance of a Fish Fin-Like Propulsor for AUVs, 2005.
- [7] Earl H. Dowell, Some recent advances in nonlinear aeroelasticity, in: A Modern Course in Aeroelasticity, 2015, pp. 609–649.
- [8] Wolfgang Geissler, B.G.V.D. Wall, Dynamic stall control on flapping wing airfoils, Aerosp. Sci. Technol. 62 (2017) 1–10.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 参数范围有限，暂未系统研究 Re、St、频率、振幅、相位差和柔性。
2. 只研究刚性主动扑翼，真实生物翼柔性会显著改变前缘涡和推力。
3. 机制解释主要基于流场可视化，缺少更严格的涡动力学量化，如涡量积分、环量、能量耗散。
4. Q-criterion 阈值固定为 0.1，阈值敏感性未说明。
5. 计算域和边界条件虽有经验说明，但边界影响未系统分析。
6. 大规模网格强调计算能力，但并行效率、加速比、内存消耗等性能指标未充分展示。
7. 语言中有部分拼写/表达问题，可能影响国际读者对严谨性的感受。
8. 推力最优结论适用于固定运动参数，不宜直接泛化为所有扑翼设计。

## 17. 可复用资产

- 参数研究结构：每类参数都按“平均速度场 -> 力系数 -> 涡结构”三层证据展开。
- 机制表达资产：把推力差异归因于前缘涡贴附/强度、尾缘涡强度、尾涡结构完整性。
- 数值可信资产：先 benchmark，再网格独立，再时间步独立，最后才做参数扫描。
- 图表资产：一组云图配一组力系数曲线，再配 Q-criterion 三维涡结构，是流体参数论文的强组合。
- 写法资产：即使结果是参数扫描，也要给出可设计的结论，如 avoiding sharp/blunt adverse leading edge、AR 最优、pitch-bias 需谨慎。

## 18. 对我写论文的启发

参数论文最容易写成“变量 A 增大，指标 B 变化”。本文的启发是每个趋势都要配机制图：为什么变好/变差必须落到流场结构、载荷来源或能量路径上。

另一个启发是，数值论文的前置可信度非常重要。方法验证和独立性验证虽然不新，但它们决定后文机理解释是否站得住。

## 19. 最终浓缩

这篇论文用大规模三维并行 IB-LBM 研究扑翼推力参数影响，证明翼型、展弦比和 pitch-bias angle 通过改变前缘涡、尾缘涡和尾迹射流控制推力。最值得学习的是“力系数 + 速度云图 + 涡结构”的三层证据链；主要复核点是涡图细节、参数范围外推、Q 阈值和刚性翼假设。
