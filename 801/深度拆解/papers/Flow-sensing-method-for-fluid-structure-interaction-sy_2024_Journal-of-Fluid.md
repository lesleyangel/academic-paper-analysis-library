# Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition

## 0. 读取说明

- 文本来源：`801/文本/txt/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.txt`，PyMuPDF 抽取，34 页。
- 本文图非常多，包含模式、误差区域、流线、等值线、瞬态算例等；图像空间细节全部需要 PDF 图像复核。
- 这篇的重点是“用结构变形实时感知/预测复杂 FSI 流场”，核心技术是结构 POD + 流场 multilayer POD + DNN 系数映射。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Flow sensing method, 3 Numerical simulation methods and model description of the FSI systems, 4 Test cases, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition。
- 作者：Xuyi Jia, Chunlin Gong, Wen Ji, Chunna Li。
- 期刊：Journal of Fluids and Structures，124，2024，104023。
- 领域：流固耦合、流场感知、降阶模型、POD、多层 POD、深度神经网络、柔性丝/仿生传感。
- 论文类型：方法论文 + 数值算例验证。
- 研究对象：两个 FSI 系统：圆柱后夹持柔性丝绕流；二维多柔性丝阵列绕流。
- 方法组合：LBM 流体求解、FEM 结构求解、IBM 流固耦合、结构 POD、流场 multilayer POD、DNN 映射结构模态系数到流体模态系数。
- 目标输出：用结构变形实时 forecast 流场速度、压力、涡量等属性。

## 2. 摘要与核心信息提取

本文核心主张是：传统 POD 对复杂 FSI 流场的全域建模会在涡结构和柔性结构附近产生较大误差；通过 multilayer POD 逐层识别高误差区域并对残差流场再建模，再用 DNN 从结构模态系数预测各层流体模态系数，可以在复杂、多柔性结构和瞬态流入条件下实现稳定的流场感知。

摘要的逻辑是：FSI 多柔性结构带来复杂非定常流和大量传感器；结构变形可作为流场感知输入；POD 降维结构，multilayer POD 提升复杂局部流场建模精度，DNN 建立结构-流体系数映射；两个算例和恒定/瞬态来流验证空间-时间性能。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.md`。

中文译文：

> 流量传感广泛用于预测流固耦合（FSI）系统中的流场。具有多种柔性结构的FSI系统通常涉及复杂的非定常流动和大量的传感器，这使得流量传感变得困难。在本研究中，提出了一种通过多层本征正交分解（POD）的 FSI 系统流量传感方法，以利用结构变形实现流场的实时预测。首先，我们建立了结构变形的POD模型。为了提高流场模型的精度，我们提出了多层POD模型，主要关注流场结构复杂的区域的局部建模精度。然后，建立流场的多层模型。此外，采用深度神经网络模型将结构的模态系数映射到多层POD的所有模态系数。所提出的方法应用于两个 FSI 系统，包括流过夹在圆柱体后面的柔性细丝的流动和流过柔性细丝组的流动。恒定流入和瞬态流动条件均被考虑。结果表明，所提出的流量传感方法表现出优异的时空性能，流特性预测准确，适用于相干涡等复杂流结构的FSI系统。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题源于仿生流场感知和工程监测需求：很多系统无法直接获得全流场，只能通过结构/少量传感器测量推断流动。FSI 系统中结构运动和流场相互耦合，因此结构变形包含流场信息。但复杂 FSI 系统的流场高维、局部涡结构强、传感维度多，直接黑箱建模网络大且可解释性差。

作者把问题收束为：如何用灰箱模型减少数据维度，同时不牺牲局部复杂流场的精度。multilayer POD 的切入点很具体：第一层 POD 建模全域主模态，误差大的局部区域再用残差 POD 建模，直到误差满足阈值。

## 4. 领域位置与文献版图

Introduction 的文献组织很清晰：

- 流场感知的生物启发和工程应用：鱼侧线、柔性纤毛、压力重构、传感器优化。
- 流场建模三类方法：white-box 高保真但慢；black-box 快但网络复杂、解释性弱；gray-box ROM 兼顾降维和可解释。
- 稳态流/静结构非定常流已有 POD、DMD、LSTM、CNN 等研究。
- 移动结构/FSI 流场更复杂，已有研究多集中简单系统或局部气动力/压力，复杂多柔性结构全流场实时感知不足。

本文站在 gray-box 路线内：不是放弃 DNN，而是让 DNN 只学习低维模态系数映射，把复杂空间结构交给 POD/multilayer POD。

## 5. Gap 制造机制

gap 是由复杂 FSI 的局部非线性和高维数据共同制造：

1. black-box 直接从结构到全流场，维度高、网络大、解释性弱。
2. conventional POD 对全域建模，能抓主相干结构，但对柔性结构附近、尾迹和强涡局部误差大。
3. 现有 FSI flow sensing 多在简单系统上验证，对多柔性结构和 transient inflow 条件研究不足。

作者的 gap 有方法针对性：不是说 POD 不好，而是说单层全域 POD 不关心复杂局部区域，因此需要 residual/local multilayer strategy。

## 6. 创新性判断

- 创新类型：降阶建模策略 + FSI 应用验证。
- 真正创新：把 multilayer POD 用作流场局部残差建模，并与结构 POD 和 DNN 系数映射组合成完整 flow sensing pipeline。
- 创新强度：中等偏强。POD/DNN/FSI 都不是新概念，但“误差阈值驱动的多层局部 POD”在复杂 FSI 流场感知中有清晰价值。
- 可信度：两个算例、恒定与瞬态条件、多物理量展示较充分；但结果完全基于数值仿真，缺少实验传感噪声和真实测量验证。

## 7. 论证链条复原

背景：流场感知需要从结构/传感器测量恢复流场。

已有方法：黑箱可预测但维度大，灰箱 ROM 可解释但传统 POD 局部误差大。

方法：用结构 POD 得结构模态系数 as；用 multilayer POD 对流场逐层建模，第一层全域、后续层在误差超过阈值的局部区域建残差；用 DNN 学习 as -> af；预测时由结构快照得到 as，再预测各层流体系数并融合重构流场。

验证：在 case A 单柔性丝和 case B 51 根柔性丝阵列中，分别考察恒定来流和随机瞬态来流；对速度、压力、流线、RMSE 和层数影响进行比较。

结论：多层 POD 每增加一层流场重构误差近似降低一个数量级，预测误差不随时间累积，复杂涡结构区域也能保持较好空间预测。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing. The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 本文解决方式：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD model of structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 学术或工程增量：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures. In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

结构 POD：对结构变形快照 Ds 建模，获得结构模态 ξs 和系数 as；以最大重构误差 Es≤1.0×10^-3D 作为结构精度条件。Case A 选 10 个结构模态，前 4 个模态能量 99.96%。

流体 multilayer POD：第一层对全流场 Df 建 POD；计算平均重构误差 E1f；选取 E1f>σ 的网格区域作为下一层建模区域；下一层对残差流 D2f 建 POD；重复直到无超阈值区域。最终 Df 由各层流场逐元素相加重构。

DNN：输入结构 POD 系数，输出所有流体 multilayer POD 系数。DNN 只处理低维系数，空间复杂性由 POD 模式承载。

数值 FSI：流体用 LBM，结构用 FEM，耦合用 IBM。Case A 计算域 4.1D×25D，D=0.10 m；Case B 计算域 3h×90h，51 根柔性丝，间距 h。网格 Δs=0.02l，每根丝 20 个 FEM 单元。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 结构 POD 能高精度表达结构变形 | 4.2.1 | Case A 前 4 模态能量 99.96%；10 模态 Es=8.88×10^-4D，小于阈值 | 强 | 图 8/9 需 PDF 复核 |
| multilayer POD 能定位并降低局部流场误差 | 4.2.2/4.3.2 | Case A Vx 三层：8/27/54 模态，误差区域从 100% 到 63.19% 到 2.46% 再到 0%；Case B 类似降至 0% | 强 | 阈值 σ 选择敏感性有限 |
| 多层模型效率仍可接受 | 4.3.2 | Case B 第二层数据维度减少 71.62%、建模时间减少 78.75%；第三层维度减少 98.96%、时间减少 97.91% | 强 | 仅报告 Vx 示例 |
| DNN 系数映射能预测流场 | 4.2.3/4.3.3 | 预测速度、压力和流线与数值参考总体吻合，误差集中在尾迹/柔性丝附近 | 中强 | 图像定性证据多，需要 PDF 复核 |
| 预测误差不随时间累积 | 4.2.3/结论 | 不同时刻独立预测，RMSE 呈周期/随机波动但不累积 | 强 | 真实闭环在线预测可能不同 |
| 方法可处理瞬态流入 | 4.2.4/4.3.4 | Case A 测试含 Re 72-120 区间，Case B Re 137-162；总体仍匹配，但准确性低于恒定来流 | 中强 | 作者承认只适用于一定 Reynolds 数范围 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1/2 | DNN 与 flow sensing 架构 | 方法流程完整 | 建模阶段和预测阶段分开 | 需要 PDF 图像复核 |
| Eq. (4)-(17) | 数学定义 POD/multilayer POD/DNN 映射 | 方法可复现 | 残差流场、误差阈值、层融合 | 文本足够 |
| Fig. 3/4 + Eq. (31)-(35) | FSI 数值模型 | 验证场景可信 | LBM/FEM/IBM 和 Re/K/M 定义 | 需要 PDF 图像复核 |
| Fig. 8/9 | 结构 POD | 结构降维准确 | Case A 10 模态满足误差阈值 | 需要 PDF 图像复核 |
| Fig. 11/29 + Table 2/3 | 多层 POD 参数和误差区域 | 局部残差建模有效 | 每层模式数、区域比例、平均误差、时间 | 需要 PDF 图像复核 |
| Fig. 12-18/30-36 | 恒定来流预测 | 速度/压力/流线预测可用 | 误差集中在尾迹/丝附近，层数越多越准 | 需要 PDF 图像复核 |
| Fig. 19-25/37-41 | 瞬态来流预测 | 方法有 transient 能力 | 预测整体匹配但误差更大 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Flow sensing method；2.1 POD；2.2 DNN；2.3 Flow sensing model via multilayer POD；3 Numerical simulation methods and model description；4 Test cases；4.1 physical/numerical settings；4.2 Case A；4.3 Case B；5 Conclusions。

篇章布局很工程化：先把工具链讲完，再讲 FSI 求解器，再用两个 case 做层层验证。第 4 章结构重复性强：POD for structure -> multilayer POD for fluid -> training and forecasting -> transient conditions。这种重复让读者能直接比较 case A/B。

标题命名偏功能型，不结果前置。Case B 标题“Flow past 2D flexible filament set”直接暴露复杂性，是很好的应用小节名。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Flow sensing method（方法/模型/算法）
  - L3 p.3: 2.1 Proper orthogonal decomposition（对象/模块/过渡章节）
  - L3 p.4: 2.2 Deep neural network（对象/模块/过渡章节）
  - L3 p.5: 2.3 Flow sensing model via multilayer POD（方法/模型/算法）
- L2 p.6: 3 Numerical simulation methods and model description of the FSI systems（方法/模型/算法）
  - L3 p.6: 3.1 Lattice Boltzmann method for fluid（方法/模型/算法）
  - L3 p.8: 3.2 Finite element method for structure（方法/模型/算法）
  - L3 p.8: 3.3 Immersed boundary method（方法/模型/算法）
- L2 p.9: 4 Test cases（结果/验证/讨论）
  - L3 p.9: 4.1 Physical models and numerical settings of the FSI systems（方法/模型/算法）
  - L3 p.12: 4.2 Case A: 2D flow past a flexible filament clamped behind a cylinder（结果/验证/讨论）
    - L4 p.12: 4.2.1 POD for structure（对象/模块/过渡章节）
    - L4 p.13: 4.2.2 Multilayer POD for fluid（对象/模块/过渡章节）
    - L4 p.19: 4.2.3 Training and forecasting（对象/模块/过渡章节）
    - L4 p.23: 4.2.4 Case A study with transient flow conditions（结果/验证/讨论）
  - L3 p.26: 4.3 Case B: Flow past 2D flexible filament set（结果/验证/讨论）
    - L4 p.26: 4.3.1 POD for structure（对象/模块/过渡章节）
    - L4 p.26: 4.3.2 Multilayer POD for fluid（对象/模块/过渡章节）
    - L4 p.28: 4.3.3 Training and forecasting（对象/模块/过渡章节）
    - L4 p.30: 4.3.4 Case B study with transient flow conditions（结果/验证/讨论）
- L2 p.30: 5 Conclusions（结论/贡献回收）
- L2 p.32: CRediT authorship contribution statement（尾部材料）
- L2 p.32: Declaration of Competing Interest（尾部材料）
- L2 p.32: Data availability（尾部材料）
- L2 p.32: Acknowledgments（尾部材料）
- L2 p.32: Appendix A. Algorithms for POD（方法/模型/算法）
- L2 p.33: Appendix B. Validation of Grid independence（结果/验证/讨论）
- L2 p.33: Appendix C. Numerical simulation results（结果/验证/讨论）
- L2 p.33: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Flow sensing method | 3 | 2 | 方法/模型/算法 |
| 2.1 Proper orthogonal decomposition | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Deep neural network | 4 | 3 | 对象/模块/过渡章节 |
| 2.3 Flow sensing model via multilayer POD | 5 | 3 | 方法/模型/算法 |
| 3 Numerical simulation methods and model description of the FSI systems | 6 | 2 | 方法/模型/算法 |
| 3.1 Lattice Boltzmann method for fluid | 6 | 3 | 方法/模型/算法 |
| 3.2 Finite element method for structure | 8 | 3 | 方法/模型/算法 |
| 3.3 Immersed boundary method | 8 | 3 | 方法/模型/算法 |
| 4 Test cases | 9 | 2 | 结果/验证/讨论 |
| 4.1 Physical models and numerical settings of the FSI systems | 9 | 3 | 方法/模型/算法 |
| 4.2 Case A: 2D flow past a flexible filament clamped behind a cylinder | 12 | 3 | 结果/验证/讨论 |
| 4.2.1 POD for structure | 12 | 4 | 对象/模块/过渡章节 |
| 4.2.2 Multilayer POD for fluid | 13 | 4 | 对象/模块/过渡章节 |
| 4.2.3 Training and forecasting | 19 | 4 | 对象/模块/过渡章节 |
| 4.2.4 Case A study with transient flow conditions | 23 | 4 | 结果/验证/讨论 |
| 4.3 Case B: Flow past 2D flexible filament set | 26 | 3 | 结果/验证/讨论 |
| 4.3.1 POD for structure | 26 | 4 | 对象/模块/过渡章节 |
| 4.3.2 Multilayer POD for fluid | 26 | 4 | 对象/模块/过渡章节 |
| 4.3.3 Training and forecasting | 28 | 4 | 对象/模块/过渡章节 |
| 4.3.4 Case B study with transient flow conditions | 30 | 4 | 结果/验证/讨论 |
| 5 Conclusions | 30 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 32 | 2 | 尾部材料 |
| Declaration of Competing Interest | 32 | 2 | 尾部材料 |
| Data availability | 32 | 2 | 尾部材料 |
| Acknowledgments | 32 | 2 | 尾部材料 |
| Appendix A. Algorithms for POD | 32 | 2 | 方法/模型/算法 |
| Appendix B. Validation of Grid independence | 33 | 2 | 结果/验证/讨论 |
| Appendix C. Numerical simulation results | 33 | 2 | 结果/验证/讨论 |
| References | 33 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 是典型“方法谱系筛选”：先列 white/black/gray box，再逐渐排除 black-box 的高维缺点，保留 gray-box + DNN 的组合。方法段节奏是公式密集型：每一步定义快照矩阵、模态、系数、误差、阈值和重构。

结果段按图推进：先描述模式和误差区域，再报告训练/测试集长度，随后展示单时刻结果、流线、时间 RMSE、不同层数对比。它不是只报平均误差，而是不断指向“复杂局部区域”的改善。

## 13. 文笔画像与语言习惯

语言偏应用计算流体论文，常用 forecasted/reference/reconstruction error/modeling region/layer/modes。claim 通常用 “agree well”“stable temporal performance”“forecasting error is mainly remained in...”。

主动语态较多，尤其 “we propose/establish/define/select”。时态上方法定义用现在时，实验设置和结果描述用现在时与过去时混合。副词常用 mainly、generally、obviously、basically，强调图像观察。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：23057
- 高频词：flow(105)；pod(49)；fluid(41)；structure(36)；sensing(33)；method(33)；model(28)；fsi(23)；field(21)；methods(21)；unsteady(20)；velocity(20)；represents(19)；modeling(18)；systems(16)；multilayer(16)；structural(16)；system(13)；flexible(13)；coefficients(13)
- 高频名词化/学术名词：structure(36)；velocity(20)；deformation(9)；prediction(9)；filament(8)；simulation(7)；density(7)；function(6)；pressure(5)；section(5)；fluid-structure(4)；decomposition(4)；performance(4)；reconstruction(4)；distribution(4)
- 高频学术动词：achieved(5)；achieve(3)；propose(2)；predict(2)；constructed(2)；identified(2)；validated(2)；validate(2)；indicate(1)；optimize(1)；developed(1)；presented(1)
- 高频形容词：structural(16)；flexible(13)；boundary(9)；filament(8)；numerical(7)；neural(5)；transient(5)；computational(5)；local(4)；aerodynamic(4)；dynamic(4)；external(4)；element(4)；orthogonal(3)；static(3)
- 高频副词：widely(4)；specifically(4)；usually(3)；directly(3)；accurately(2)；similarly(2)；fully(2)；mainly(1)；generally(1)；considerably(1)；quickly(1)；rapidly(1)；comprehensively(1)；especially(1)；effectively(1)
- 高频二词短语：flow sensing(30)；flow field(21)；unsteady flow(15)；fsi systems(14)；multilayer pod(13)；sensing method(12)；mode coefficients(10)；structural deformation(9)；fsi system(8)；flow properties(8)；fluid structure(6)；sensing methods(6)
- 高频三词短语：flow sensing method(11)；flow sensing methods(5)；flow past flexible(4)；past flexible filament(4)；transient flow conditions(4)；flow sensing model(4)；sensing method fsi(3)；method fsi systems(3)；proper orthogonal decomposition(3)；flow field structural(3)；field structural deformation(3)；model structural deformation(3)
- 被动语态估计：66；`we + 动作动词` 主动句估计：1
- 一般现在时线索：137；一般过去时线索：161；现在完成时线索：0；情态动词线索：25

分章节正文词频：

- 1 Introduction: flow(80)；sensing(24)；methods(21)；pod(20)；model(18)；field(17)；unsteady(17)；method(15)
- 2 Flow sensing method: pod(12)；flow(11)；structure(6)；sensing(5)；method(5)；fsi(4)；model(4)；section(4)
- 3 Numerical simulation methods and model description of the FSI systems: fluid(30)；structure(18)；pod(16)；velocity(14)；represents(12)；coefficients(9)；boundary(9)；point(9)
- 4 Test cases: fsi(5)；filament(5)；numerical(4)；simulation(4)；case(4)；represents(4)；fluid(4)；method(3)
- 5 Conclusions: flow(5)；transient(3)；conditions(3)；method(3)；case(2)；study(2)；validate(2)；sensing(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- gap 句式：The conventional POD approach typically models the entire flow field without specifically focusing on regions with variations.
- 方法句式：The region that satisfies E>σ is taken as the modeling region for the next layer.
- 结果句式：The forecasted results agree well with the numerical simulation results in general.
- 局限句式：The method is only suitable for a certain range of Reynolds numbers.
- 对比句式：With an increase in the number of layers, the forecasting error gradually decreases.
- 可复用模板：全域低阶模型捕捉主结构，局部残差模型补偿复杂区域，低维神经网络只学习模态系数映射。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Since the unsteady flow with moving structure usually involves fluid-structure interaction (FSI), which is more complex than steady flow and unsteady flow with static structure, it brings more challenges for flow sensing methods in modeling strategy and accuracy.
  可迁移模板：Since the unsteady flow with moving structure usually involves fluid-structure interaction (METHOD), which is more complex than steady flow and unsteady flow with static structure, it brings more challenges for flow sensing methods in modeling strategy and accuracy.
#### Gap/转折句
- 原句：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
  可迁移模板：The METHOD system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 原句：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
  可迁移模板：The METHOD system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 原句：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
  可迁移模板：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., X; Zhang et al., X).
- 原句：While the black-box and gray-box methods are data-driven modeling methods that can quickly obtain flow solutions with high accuracy.
  可迁移模板：While the black-box and gray-box methods are data-driven modeling methods that can quickly obtain flow solutions with high accuracy.
- 原句：Specifically, the black-box methods build an input-output mapping model directly by surrogate model * Corresponding author.
  可迁移模板：Specifically, the black-box methods build an input-output mapping model directly by surrogate model * Corresponding author.
#### 方法提出句
- 原句：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
- 原句：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  可迁移模板：To improve model accuracy for flow field, we propose the multilayer METHOD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 原句：Then, we establish the multilayer model of flow field.
  可迁移模板：Then, we establish the multilayer model of flow field.
- 原句：Furthermore, the deep neural network model is employed to map the mode coefficients of the structure to all the mode coefficients of the multilayer POD.
  可迁移模板：Furthermore, the deep neural network model is employed to map the mode coefficients of the structure to all the mode coefficients of the multilayer METHOD.
#### 结果呈现句
- 原句：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices.
  可迁移模板：The results indicate that the proposed METHOD exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for METHOD systems with complex flow structures such as coherent vortices.
- 原句：For steady flow, (Zhao et al., 2021) constructed a compressed sensing method using proper orthogonal decomposition (POD), and achieved high-precision reconstruction of airfoil pressure by a few measurement data.
  可迁移模板：For steady flow, (Zhao et al., X) constructed a compressed sensing method using proper orthogonal decomposition (METHOD), and achieved high-precision reconstruction of airfoil pressure by a few measurement data.
- 原句：Zhang et al. (2022) proposed a flow sensing method combining DMD and long short-term memory (LSTM) network, and achieved prediction of unsteady flow around a circular cylinder from sparse sensor measurements.
  可迁移模板：Zhang et al. (X) proposed a flow sensing method combining METHOD and long short-term memory (METHOD) network, and achieved prediction of unsteady flow around a circular cylinder from sparse sensor measurements.
#### 贡献/增量句
- 原句：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
- 原句：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  可迁移模板：To improve model accuracy for flow field, we propose the multilayer METHOD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 原句：Then, we establish the multilayer model of flow field.
  可迁移模板：Then, we establish the multilayer model of flow field.
- 原句：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
- 原句：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  可迁移模板：To improve model accuracy for flow field, we propose the multilayer METHOD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
#### 限制/边界句
- 原句：In above studies, many deep learning algorithms are used in the black-box methods, but only POD is used in the gray-box methods.
  可迁移模板：In above studies, many deep learning algorithms are used in the black-box methods, but only METHOD is used in the gray-box methods.
- 原句：Li et al. (2019) used LSTM to forecast unsteady aerodynamics of airfoil pitching and plunging system under different flow conditions, but this study only focused on predicting aerodynamic coefficients.
  可迁移模板：Li et al. (X) used METHOD to forecast unsteady aerodynamics of airfoil pitching and plunging system under different flow conditions, but this study only focused on predicting aerodynamic coefficients.
- 原句：Most of the existing flow sensing research was only carried out on simple FSI systems, and the research on real-time flow sensing methods for complex FSI systems with multi flexible structures is insufficient, which is necessary and meaningful to biomimetic flow sensing.
  可迁移模板：Most of the existing flow sensing research was only carried out on simple METHOD systems, and the research on real-time flow sensing methods for complex METHOD systems with multi flexible structures is insufficient, which is necessary and meaningful to biomimetic flow sensing.
- 原句：Directly constructing flow sensing model using black-box model can lead to issues such as large network architecture, high computational complexity, and limited interpretability.
  可迁移模板：Directly constructing flow sensing model using black-box model can lead to issues such as large network architecture, high computational complexity, and limited interpretability.
- 原句：However, the flow field may exhibit variations in flow characteristics and complexities at different locations.
  可迁移模板：However, the flow field may exhibit variations in flow characteristics and complexities at different locations.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用按流场感知对象和建模方法双轴组织：稳态流、静结构非定常流、移动结构/FSI；白箱、黑箱、灰箱。作者大量引用 DMD/LSTM/CNN/POD 等方法，让自己的路线看起来是综合而非孤立。

gap 前的引用策略很有效：先承认 black-box 和 gray-box 都能处理 flow sensing，再指出 black-box 高维、conventional POD 局部精度不足。这样 multilayer POD 的必要性自然出现。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：0
- Introduction 引文簇数量估计：0
- References 条目数：93
- 可识别年份条目数：78
- 2021 年及以后文献数：36
- 2010 年前经典文献数：4
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Journal of Fluids and Structures(2)
- 引文簇样例：未识别

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 2021. Deep learning to replace, improve, or aid CFD analysis in built environment applications: a review. Build. Environ. 206, 108315 https:// doi.org/10.1016/j.buildenv.2021.
- 108315. Castellanos, R., Cornejo Maceda, G.Y., De La Fuente, I., Noack, B.R., Ianiro, A., Discetti, S.,
- 2022. Machine-learning flow control with few sensor feedback and measurement noise. Phys. Fluids 34, 047118. https://doi.org/10.1063/5.
- 0087208. Chen, S., Doolen, G.D.,
- 1998. Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech. 30 (1), 329–364. https://doi.org/10.1146/annurev.fluid.30.1.
- 329. Connor, J.O., Revell, A.,
- 2019. Dynamic interactions of multiple wall-mounted flexible flaps. J. Fluid Mech. 870, 189–216. https://doi.org/10.1017/jfm.2019.
- 266. Dang, F., Nasreen, S., Zhang, F.,
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 数据全来自数值仿真，缺少真实传感器噪声、测量误差和实验流场验证。
- DNN 架构细节、超参数和泛化能力若不足，可能影响复现。
- transient 条件只在一定 Re 范围内有效，外推能力有限。
- multilayer POD 阈值 σ 的选择对层数、效率和精度影响很大，敏感性可进一步展开。
- 压力场在柔性丝附近存在 Gibbs/非平滑问题，说明线性 POD 对强非线性跳变仍有局限。
- Case B 多丝系统复杂，但仍是二维数值模型，三维真实 FSI 需验证。

## 17. 可复用资产

- 方法资产：POD 降维 + error-threshold local residual POD + DNN coefficient mapping。
- 图表资产：模型架构图、误差区域图、层数-时间误差图、不同层数等值线对比、恒定/瞬态来流对比。
- 论证资产：不仅展示预测好，还展示为什么单层 POD 不好、多层如何逐步修补。
- 写作资产：用两个 case 复用完全一致的小节结构，增强可比性。
- 局限表达资产：明确承认 transient forecasting 只在一定 Re 范围内适用。

## 18. 对我写论文的启发

如果提出“深度学习 + ROM”的方法，最好像本文一样把深度网络限制在低维系数空间，而不是直接预测高维场。这样既能减少网络复杂度，也能保留 ROM 的可解释性。

另外，结果展示要围绕失败区域展开。本文不断指出误差集中在尾迹、柔性丝附近、压力突变区，然后证明 multilayer POD 对这些区域有改进，这比只报全域 RMSE 更有说服力。

## 19. 最终浓缩

本文最值得学的是用误差阈值驱动的 multilayer POD 修补传统 POD 对复杂局部流场的弱点，再用 DNN 学结构-流体系数映射。最强证据是两个 FSI 算例中多层 POD 使重构误差近似逐层数量级下降，且预测误差不随时间积累。最大风险是完全数值验证、阈值敏感和瞬态 Re 范围有限，后续应加入实验噪声和三维场景验证。
