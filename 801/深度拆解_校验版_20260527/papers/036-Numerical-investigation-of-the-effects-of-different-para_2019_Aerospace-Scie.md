# 论文深度拆解：036-Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie

> 生成依据：`801/cleantext/036-Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`036-Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie.pdf`
- 页数：15
- clean body 字符数：44847
- 摘要字符数：1733
- 参考文献条数：57
- 图题数：23
- 表题数：5
- 表格文件数：5
- 公式候选数：84
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "19 formula(s) need manual review."}]

## 1. 身份层

- 标题：036-Numerical-investigation-of-the-effects-of-different-para_2019_Aerospace-Scie
- 年份：2019
- 期刊/来源：Aerospace Scie
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：It still is a great challenge to develop more high-resolution and cheaper experimental techniques. To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation. The effect of the structural flexibility is also very important and obvious for true fish, insects and birds.
- 主要方法：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. In this paper, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed. Using Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
- 主要证据：图表 28 个标题、公式 84 个候选、参考文献 57 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“It still is a great challenge to develop more high-resolution and cheaper experimental techniques. To capture the flow mechanism and fine vortex structures of three-dimensional com”，可以通过“Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. In this paper, a general large- scale parallel so”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack. For example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius. The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：It still is a great challenge to develop more high-resolution and cheaper experimental techniques. To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation. The effect of the structural flexibility is also very important and obvious for true fish, insects and birds.
- 问题来源：多来自工程瓶颈、计算/实验成本、复杂多物理场耦合、可靠性/不确定性传播或材料性能优化需求。
- 为什么重要：该类问题通常直接影响热防护设计、结构安全、飞行性能、能量管理、可靠性评估或材料服役性能。
- 研究边界：以本文模型、实验对象、材料体系、飞行轨迹、结构形式或数据集为边界；外推到其它平台或工况需谨慎。
- 可写作学习点：先给工程必要性，再把大问题压缩成可验证的模型/方法/性能指标问题。

## 4. 位置层：文献版图与 gap

- 已有研究分类推断：
  - 物理/数值模型类：提供机理和高保真基准，但成本较高或边界较窄。
  - 数据驱动/降阶/代理模型类：提升效率，但依赖数据覆盖和泛化验证。
  - 实验/测量类：提供真实证据，但工况、样本和尺度有限。
  - 优化/可靠性/不确定性类：处理设计决策，但常受模型复杂度和计算成本限制。
- 作者声明或文本中可见 gap：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5]. In particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. In this paper, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed. Using Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：实验/测量 + 性能分析型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：实验/测量 + 性能分析型
- 输入：材料/结构/轨迹/工况/几何/传感器/样本/仿真参数等，需按方法章节和表格核查。
- 输出：性能指标、预测结果、优化方案、可靠性指标、温度/应力/流场/电热性能等。
- 关键步骤推断：
  1. 定义研究对象、几何/材料/工况边界；
  2. 建立理论、数值、实验或数据驱动模型；
  3. 设置参数、网格、样本、训练或测试条件；
  4. 与基准/实验/高保真模型对比；
  5. 用图表和误差/性能指标回收 claim。
- 关键假设：模型边界、材料参数、载荷/温度/流场条件、数据分布或实验测量条件。
- 复现信息充分性：中等。文本和表格提供主流程，但参数完整性、代码/数据开放性和 PDF 图像细节仍需人工核查。

## 7. 证据层

### 7.1 Claim-Evidence 全表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| In this paper, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed. | 摘要/引言/结论候选 | 图：Fig. 1. Comparison of verification results. The hydrodynamics coefficients of verification example and our results. (a) Lift coefficient with combined parameter of frequency and time. (b) Thrust coefficient with combined parameter of frequency and time. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Using Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information. | 摘要/引言/结论候选 | 图：Fig. 2. (a) is NACA0012 flapping wing model, (b) is the flow field calculation domain. The flow field employed a standard Cartesian grid. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes. | 摘要/引言/结论候选 | 图：Fig. 3. The hydrodynamics coefficients of flapping wings at different grid numbers for St = 0.6, Re = 200, ϕ = π/2 and Aθ = π/6 case. (a) Lift force coefficient. (b) Trust force coefficient. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [1]. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (46.08, 696.06, 203.21, 715.22)]] * Corresponding author | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Comparison of verification results. The hydrodynamics coefficients of verification example and our results. (a) Lift coefficient with combined parameter | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 2. (a) is NACA0012 flapping wing model, (b) is the flow field calculation domain. The flow field employed a standard Cartesian grid. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 3. The hydrodynamics coefficients of flapping wings at different grid numbers for St = 0.6, Re = 200, ϕ = π/2 and Aθ = π/6 case. (a) Lift force coefficient | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The vorticity contour plot of NACA0012 flapping wing spread spanwise symmetry plane under three different grids. (a) Coarse grid, (b) Nominal grid, (c)  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. The hydrodynamics coefficients of flapping wings at different time steps for St = 0.6, Re = 200, ϕ = π/2 and Aθ = π/6 case. (a) Lift force coefficient,  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The vorticity contour plot of NACA0012 flapping wing spread spanwise symmetry plane under three different time steps. (a) Loose time, (b) Nominal time,  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Average velocity contour in one flapping cycle at the spanwise symmetry plane under different wing shapes. (a) Ellipsoidal wing, (b) NACA0012 wing, (c)  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. The hydrodynamics coefficients of flapping wings at different at different wing shape. (a) Lift force coefficient, (b) Thrust force coefficient. Both re | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. The vorticity contour plot of NACA0012 flapping wing spread wing span symmetry plane at different wing shapes. (a) Ellipsoidal wing, (b) NACA0012 wing,  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Partial magnification of the vorticity contour in the wing span symmetry plane. Where, three-dimensional flapping wing is black. The three states used  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The vortices varieties of the NACA0012 wing movement in one cycle at different time. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. The vortex structure of the flapping wing identified by Q-criterion (Q = 0.1) in the wake zone of flapping wings at different wing shapes. Where, the p | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 13. One-cycle average velocity contours of NACA0012 wing with different aspect ratios. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The hydrodynamics coefficients of flapping wings at different at different aspect ratios. (a) Lift force coefficient. (b) Thrust force coefficient. Bot | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Partial magnification of the vorticity contour in the wing span symmetry plane at different aspect ratios. The five states used the same color space. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (46.08, 696.06, 203.21, 715.22)]] * Corresponding author. E-mail address: aa | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (303.43, 718.86, 411.45, 729.23)]] fi(x + eiδt,t + δt) -fi(x,t) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (310.18, 731.7, 333.25, 746.93)]] = -1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 2, bbox (334.86, 730.02, 430.13, 750.44)]] � fi(x,t) -f eq i (x,t) � + 3 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (42.56, 153.29, 59.07, 164.16)]] ei = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (42.56, 223.83, 61.26, 235.13)]] ωi = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (44.25, 273.16, 81.98, 287.71)]] f eq i = ρωi | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (42.56, 328.23, 293.62, 338.55)]] υ = (2τ -1)/6 (5) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> After billions of years of evolution, many creatures employing flapping wing in nature tend to have excellent flight capabilities. To understand the bionic wings flow mechanism will be helpful to design high performance underwater vehicles and new conception aircrafts. The geometric parameters, kinematic parameters and flow parameters have great effects on the bionic wings thrust performance. Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method. In this paper, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed. The evolution procedures of the 3D flapping wing leading edge vortex and wake flow vortex structures were analyzed in detail. Our study explained the 3D flapping wing thrust performance variation with different wing shapes, aspect ratios and pitch-bias angles of attack. Using Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information. It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes. With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack. The discussion of these parameters will provide a theoretical basis for improving flapping-like vehicles propulsive performance.

### 7.4 摘要中文翻译

> 经过数十亿年的进化，自然界中许多使用扑翼的生物往往具有出色的飞行能力。了解仿生机翼的流动机理将有助于设计高性能水下航行器和新概念飞行器。几何参数、运动学参数和流动参数对仿生机翼推力性能影响较大。面对多样的参数，用传统的数值模拟方法很难探索三维（3D）仿生扑翼流动机理。在本文中，开发了一种使用浸入边界格子玻尔兹曼方法（IB-LBM）的通用大规模并行求解器。详细分析了3D扑翼前缘涡和尾流涡结构的演化过程。我们的研究解释了 3D 扑翼推力性能随不同机翼形状、展弦比和俯仰偏攻角的变化。利用中国超级计算机天河二号为并行IB-LBM的进一步发展提供了广泛的可能性，采用千万级网格将有助于我们获得更完整、更准确的3D扑翼流场信息。表明与其他尖翼形状相比，钝翼具有最好的推力性能。随着展弦比的增大，扑翼的推力系数先增大后减小，并且随着偏航角的增大，推力系数迅速减小，甚至在大偏航角时出现阻力现象。这些参数的讨论将为提高扑翼飞行器推进性能提供理论依据。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> The influence of geometrical and motion parameters on the flow mechanism and thrust performance of bionic flapping wing is one of the key issues in the design of wing shape and motion control law for bionic flapping aircraft and underwater vehicles. To capture the flow mechanism and fine vortex structures of three-dimensional complex flapping wings is a time-consuming challenge task, especially for the parameter influence investigations in large-scale calculation. In this paper, a three-dimensional parallel IB-LBM solver suitable for running on TianHe-II Supercomputer was developed and validated.
> 
> (a)
> 
> (b)
> 
> (a) α0 =0°
> 
> (c) $\alpha _ {0} = 20 ^{\circ}$
> 
> (b) α0 =10 
> (d) $\alpha _ {0} = 30 ^{\circ}$
> 
> The wing shape, aspect ratio and pitch-bias angle of attack have great influences on the thrust performance of the flapping wings. The numerical results show the ellipsoidal wing has the best thrust performance in the three flapping wings, whose leading-edge vortex is full and close to the wing surface. The vortex structures of NACA0012 wing and ellipsoidal wing are very similar, which causes also the similar thrust performance. The vortex structure of the cuboid wing is small and far from the wing which leads to the worst thrust performance. With the increase of aspect ratio, the average thrust coefficient of NACA0012 flapping wings increases firstly and then decreases. The two-dimensional characteristics of the vorticity distribution is obviously exhibited with the increase of the aspect ratio. It means that for the small aspect ratio flapping wing, its three-dimensional effects in thrust performance must be taking into accounting for. With the pitch-bias angle of attack increases, the thrust coefficient of NACA0012 flapping wing decrease, or even shown resistance phenomenon at the large pitch-bias angel of attack. The evolution procedures of the leading edge vortex and wake flow vortex structures are the possible main reasons which could be used to explain the thrust performance changes with parameter variation of the flapping wing.
> 
> In future work, much more fluid parameters such as Reynolds numbers, Strouhal number, and more different motion patterns such as amplitude, frequency, would be further investigated. At the same time, we will further explore the influence of 3D thickness and leading edge curvature on thrust performance. The effect of the structural flexibility is also very important and obvious for true fish, insects and birds. Taking into account for the fluid-structural interaction effects based on IB-LBM method is also expected in next step, although it is a challenge task in large scale simulation.

### 7.6 结论中文翻译

> 几何参数和运动参数对仿生扑翼流动机理和推力性能的影响是仿生扑翼飞行器和水下航行器机翼形状和运动控制律设计的关键问题之一。捕捉三维复杂扑翼的流动机制和精细涡流结构是一项耗时的挑战任务，特别是对于大规模计算中的参数影响研究。本文开发并验证了适合在天河二号超级计算机上运行的三维并行IB-LBM求解器。 (a) (b) (a) α0 =0° (c) $\alpha _ {0} = 20 ^{\circ}$ (b) α0 =10 (d) $\alpha _ {0} = 30 ^{\circ}$ 机翼形状、展弦比和俯仰攻角对扑翼的推力性能影响较大。数值结果表明，三种扑翼中，椭圆机翼的推力性能最好，其前缘涡充分且接近翼面。 NACA0012机翼和椭球机翼的涡流结构非常相似，这也导致了相似的推力性能。长方体机翼涡流结构较小且距机翼较远，推力性能最差。随着展弦比的增大，NACA0012扑翼的平均推力系数先增大后减小。随着展弦比的增大，涡度分布的二维特征表现得更加明显。这意味着对于小展弦比扑翼，必须考虑其推力性能的三维效应。
> 
> 随着偏俯攻角的增大，NACA0012扑翼的推力系数减小，甚至在大偏俯攻角处出现阻力现象。前缘涡和尾流涡结构的演化过程是可能的主要原因，可以用来解释扑翼参数变化推力性能的变化。在未来的工作中，将进一步研究更多的流体参数，如雷诺数、斯特劳哈尔数，以及更多不同的运动模式，如振幅、频率。同时，我们将进一步探讨3D厚度和前缘曲率对推力性能的影响。对于真正的鱼类、昆虫和鸟类来说，结构灵活性的影响也非常重要和明显。基于IB-LBM方法考虑流固相互作用效应也有望在下一步实现，尽管这在大规模模拟中是一项挑战任务。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9614 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The lattice Boltzmann method | 方法建构 | 2468 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. The immersed boundary method | 方法建构 | 2383 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. The IB-LBM | 对象/条件/子问题展开 | 1543 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.4. Solver validation | 对象/条件/子问题展开 | 2349 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3. Independence validation | 对象/条件/子问题展开 | 392 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.1. Mesh independence validation | 对象/条件/子问题展开 | 2194 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2. Time independence validation | 对象/条件/子问题展开 | 1014 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.1. Problem statement | 对象/条件/子问题展开 | 879 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.2. The influence of wing shape on thrust performance | 结果验证/讨论 | 9784 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 11 | 4.3. The influence of aspect ratio on thrust performance | 结果验证/讨论 | 6040 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 12 | 4.4. The influence of pitch-bias angle of attack on thrust performance | 结果验证/讨论 | 2875 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 13 | 5. Conclusions | 主张回收/边界说明 | 2657 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 14 | Conflict of interest statement | 对象/条件/子问题展开 | 33 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

### 8.2 章节推进逻辑

- 摘要：通常按“问题重要性 -> 既有方法不足 -> 本文方法 -> 验证对象 -> 主要结果/性能增量”组织。
- Introduction：先把工程/学术问题放大，再通过文献分类制造 gap，最后收束到本文贡献。
- Method/Model：把 claim 变成可执行流程，读者需要在这里看到变量、假设、输入输出和边界。
- Results/Discussion：把方法有效性转化为图表证据，常通过对比、误差、趋势和敏感性说明。
- Conclusion：回收主要发现，通常也暴露外推边界和未来工作。

### 8.3 段落功能样例

| 段落来源 | 功能 | 推进方式 | 可学习点 |
| --- | --- | --- | --- |
| Introduction 前段 | 背景/重要性 | 从工程必要性进入研究对象 | 先建立“为什么要研究” |
| Introduction 文献段 | 文献分类/gap | 用 however/limited/remain 等转折缩小问题 | gap 要和后文方法一一对应 |
| Method 开头 | 方法总览 | 先给框架，再拆步骤 | 降低复杂方法的阅读成本 |
| Results 开头 | 验证设置 | 说明对比对象和指标 | 让审稿人知道证据如何支撑 claim |
| Conclusion | 主张回收 | 用编号或并列句总结贡献 | 不新增未验证 claim |

### 8.4 词频、词类、短语与语态

- 高频词：wing(147)；vortex(87)；thrust(83)；flapping(82)；mathbf(55)；fig(44)；velocity(40)；performance(37)；flow(37)；wings(33)；aspect(32)；average(32)；time(29)；edge(28)；force(27)；fluid(25)；parameters(25)；leading(25)；ratio(24)；boundary(24)
- 高频学术名词/术语：velocity(40)；performance(37)；structure(19)；motion(16)；mechanism(16)；independence(14)；movement(12)；vorticity(11)；distribution(11)；influence(10)；simulation(9)；equation(9)；direction(9)；information(7)；validation(7)
- 高频学术动词：compared(8)；investigated(7)；obtain(5)；obtained(5)；reveal(3)；introduced(3)；indicated(3)；develop(2)；validate(2)；developed(2)；indicate(2)；investigate(1)；introduce(1)；constructed(1)；compare(1)
- 高频形容词：boundary(24)；coefficient(23)；three-dimensional(18)；numerical(15)；bionic(12)；movement(12)；ellipsoidal(12)；two-dimensional(11)；computational(8)；consistent(8)；table(7)；quantitative(6)；hydrodynamic(6)；traditional(6)；previous(6)
- 高频副词：respectively(10)；obviously(5)；significantly(5)；gradually(5)；clearly(4)；firstly(3)；widely(3)；basically(3)；especially(2)；greatly(2)；relatively(2)；particularly(1)
- 高频二词短语：flapping wing(40)；thrust performance(26)；flapping wings(25)；leading edge(25)；aspect ratio(24)；edge vortex(19)；mathbf mathbf(19)；average velocity(18)；thrust coefficient(16)；vortex structure(15)；naca wing(15)；pitch-bias angle(14)；cuboid wing(14)；angle attack(13)；fig shows(12)
- 高频三词短语：leading edge vortex(17)；pitch-bias angle attack(9)；big mathbf mathbf(5)；mathbf mathbf big(5)；mesh time step(5)；mathbf big mathbf(5)；average thrust coefficient(5)；average thrust coefficients(5)；flow field information(4)；mathbf mathbf delta(4)；mathbf cdot mathbf(4)；mathbf mathbf mathbf(4)
- 被动语态估计：70
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：261
- 一般过去时线索：216
- 现在完成时线索：1
- 情态动词线索：48

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The lattice Boltzmann equation describing the motion of fluid particles is as follows [48]: $$\begin{array} {l} {f _ {i} ( \mathbf {x} + \mathbf {e} _ {i} \delta t , t + \delta t ) - f _ {i} ( \mathbf {x} , t )} \\ {\displaystyle = - \frac {1} {\tau} \big [ f _ {i} ( \mathbf {x} , t ) - f _ {i} ^ {e q} ( \mathbf {x} , t ) \big ] + \frac {3} {2} \omega _ {i} \mathbf {f} \cdot \mathbf {e} _ {i} \delta t} \end{array}\tag{1}$$ where $f _ {i}$ is the particle density distribution function, $f _ {i} ^ {e q}$ is the corresponding equilibrium state distribution function, τ is the dimensionless relaxation time, δt is the time step, f is the fluid density, $\mathbf {e} _ {i}$ is the particle velocity, $\omega _ {i}$ is the weight coefficient, ei and $\omega _ {i}$ are related to discrete density model.
  - 可迁移句型：{object} lattice Boltzmann equation describing the motion of fluid particles is as follows [48]: $$\begin{array} {l} {f _ {i} ( \mathbf {x} + \mathbf {e} _ {i} \delta t , t + \delta t ) - f _ {i} ( \mathbf {x} , t )} \\ {\displaystyle = - \frac {1} {\tau} \big
- 原句：The effect of the structural flexibility is also very important and obvious for true fish, insects and birds.
  - 可迁移句型：{object} effect of the structural flexibility is also very important and obvious for true fish, insects and birds.
### gap/转折句
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  - 可迁移句型：{object} the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 原句：The creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5].
  - 可迁移句型：{object} creatures’ amazing ability of flying or swimming inspires a few investigations about flapping wing thrust performance [3–5].
- 原句：However, experiment research for bionic movement has also some disadvantages, such as poor repeatability, lack of enough detail of the flow field and also very expensive.
  - 可迁移句型：{object}, experiment research for bionic movement has also some disadvantages, such as poor repeatability, lack of enough detail of the flow field and also very expensive.
- 原句：It still is a great challenge to develop more high-resolution and cheaper experimental techniques.
  - 可迁移句型：{object} still is a great challenge to develop more high-resolution and cheaper experimental techniques.
### 方法提出句
- 原句：Facing the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
  - 可迁移句型：{object} the diverse parameters, it’s very difficult to explore the three-dimensional (3D) bionic flapping wing flow mechanism with traditional numerical simulation method.
- 原句：In this paper, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed.
  - 可迁移句型：{object} This study, a general large- scale parallel solver using Immersed Boundary-Lattice Boltzmann Method (IB-LBM) was developed.
- 原句：Using Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
  - 可迁移句型：{object} Chinese supercomputer TianHe- II presents a wide range of possibilities for the further development of parallel IB-LBM, employing tens of millions grids will help us to obtain more complete and accurate 3D flapping wing flow field information.
- 原句：With the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [1].
  - 可迁移句型：{object} the rapid development of aviation technologies and related disciplines, the modern aircraft design is pursuing long distance flight, high maneuverability and low energy performances [1].
### 结果证明句
- 原句：It’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
  - 可迁移句型：{object}’s indicated that the obtuse wing has the best thrust performance compared with other sharp wing shapes.
- 原句：With the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large pitch-bias angel of attack.
  - 可迁移句型：{object} the increase of the aspect ratio, the thrust coefficient of flapping wing increases firstly and then decreases, and with pitch-bias angles of attack increases, the thrust coefficient decreases quickly or even shown resistance phenomenon at the large p
- 原句：The actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement.
  - 可迁移句型：{object} actual circumstances of birds, insects and fishes employing flapping motion are very complicated, so that experimental observation, theoretical analysis and numerical simulation are all used together to reveal the mechanism of the bionic movement.
- 原句：Theoretical analysis can give quantitative hydrodynamic results by means of simplified approximation and explains the inherent fluid mechanism of like-flapping fish swimming.
  - 可迁移句型：{object} analysis can give quantitative hydrodynamic results by means of simplified approximation and explains the inherent fluid mechanism of like-flapping fish swimming.
### 贡献收束句
- 原句：The discussion of these parameters will provide a theoretical basis for improving flapping-like vehicles propulsive performance.
  - 可迁移句型：{object} discussion of these parameters will provide a theoretical basis for improving flapping-like vehicles propulsive performance.
- 原句：For example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius.
  - 可迁移句型：{object} example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius.
- 原句：Experimental investigation can obtain force and some flow field information to further reveals the nature of the bionic movements and provide basis test data for numerical method.
  - 可迁移句型：{object} investigation can obtain force and some flow field information to further reveals the nature of the bionic movements and provide basis test data for numerical method.
- 原句：Therefore, provides a powerful platform for solving the problem of flapping wing unsteady flow mechanism and is broadly applicable to a variety of parameter research.
  - 可迁移句型：{object}, provides a powerful platform for solving the problem of flapping wing unsteady flow mechanism and is broadly applicable to a variety of parameter research.
### 边界/谨慎句
- 原句：For example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius.
  - 可迁移句型：{object} example, the turning radius of anglerfish is only 6% of its body length [2], while the underwater vehicle has to reduce more than 50% of its speed to decrease the turning radius.
- 原句：In particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture.
  - 可迁移句型：{object} particularly, the flapping wing benefits from using simple translational motions compared to existing conventional propulsion systems, which not only exhibits superior performance in unsteady flow but also is easier to manufacture.
- 原句：But the theoretical analysis can only solve the bionic movement with very simple structures and simple movement parameters.
  - 可迁移句型：{object} the theoretical analysis can only solve the bionic movement with very simple structures and simple movement parameters.
- 原句：The fluid is seen as a fluid micelle that can only move toward the surrounding grid point or stand still.
  - 可迁移句型：{object} fluid is seen as a fluid micelle that can only move toward the surrounding grid point or stand still.

## 9. 引用风险层

- 正文引用簇估计：33
- 参考文献条数：57
- 可识别年份条目数：57
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：28
- 高频来源粗略识别：Fluids Struct(7)；Fluid Mech(6)；Fluids(4)；Comput. Phys(4)；Sci. Technol(3)；Exp. Biol(3)；Nonlinear Soft Matter Phys(2)；Aircr(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Brian P. Danowsky, et al., Incorporation of feedback control into a high-fidelity aeroservoelastic fighter aircraft model, J. Aircr. 47 (4) (2012) 1274–1282.
- [2] Paolo Domenici, R.W. Blake, The kinematics and performance of the escape response in the angelfish (Pterophyllum eimekei), Can. J. Zool. 71 (11) (1991) 2319–2326.
- [3] M.F. Platzer, et al., Flapping wing aerodynamics: progress and challenges, AIAA J. 46 (9) (2008) 2136–2149.
- [4] W. Shyy, et al., Aerodynamics, sensing and control of insect-scale flapping-wing flight, Proc. Math. Phys. Eng. Sci. 472 (2186) (2016) 20150712.
- [5] Farooq Umar, M. Sun, Aerodynamic force and power for flapping wing at low Reynolds number in ground effect, in: International Bhurban Conference on Applied Sciences and Technology, 2018, pp. 553–558.
- [6] George V. Lauder, et al., Design and Performance of a Fish Fin-Like Propulsor for AUVs, 2005.
- [7] Earl H. Dowell, Some recent advances in nonlinear aeroelasticity, in: A Modern Course in Aeroelasticity, 2015, pp. 609–649.
- [8] Wolfgang Geissler, B.G.V.D. Wall, Dynamic stall control on flapping wing air- foils, Aerosp. Sci. Technol. 62 (2017) 1–10.
- [9] J. Gray, Studies in animal locomotion V: resistance reflexes in the Eel, J. Exp. Biol. 13 (2) (1936) 181–191.
- [10] M.J. Lighthill, Large-amplitude elongated-body theory of fish locomotion, Proc. R. Soc. Lond. 179 (1055) (1971) 125–138.
- [11] Che Shu Lin, C. Hwu, W.B. Young, The thrust and lift of an ornithopter’s mem- brane wings with simple flapping motion, Aerosp. Sci. Technol. 10 (2) (2006) 111–119.
- [12] Shuanghou Deng, B.V. Oudheusden, Wake structure visualization of a flapping- wing micro-air-vehicle in forward flight, Aerosp. Sci. Technol. 50 (2016) 204–211.
- [13] Mittal Dong, Najjar, Wake topology and hydrodynamic performance of low- aspect-ratio flapping foils, J. Fluid Mech. 566 (566) (2006) 309–343.
- [14] Yun Fei Zhang, Y.E. Zheng-Yin, Three-dimensional Navier–Stokes simulation of flapping wing with pitching elasticity, J. Aerosp. Power 26 (4) (2011) 880–889.
- [15] Chengyu Li, H. Dong, Three-dimensional wake topology and propulsive perfor- mance of low-aspect-ratio pitching-rolling plates, Phys. Fluids 28 (7) (2016) 2413.

### 9.2 审稿风险清单

| 风险 | 具体表现 | 严重度 | 应对方式 |
| --- | --- | --- | --- |
| gap 风险 | gap 若只靠泛化措辞而非最近文献支撑，会显得不够真实 | P1 | 增补最近五年最接近工作并公平比较 |
| 方法必要性 | 若简单 baseline 已可解决问题，新模型复杂度会被质疑 | P1 | 加入消融、复杂度收益和边界条件说明 |
| 证据外推 | 单一算例/样本/轨迹/材料体系支撑大 claim | P1 | 扩展工况或明确适用边界 |
| 图表可读性 | 文本抽取无法确认图像细节 | P2 | 回看 PDF 图像、坐标轴、误差条和图例 |
| 公式/符号 | 公式抽取可能低置信或符号缺失 | P2 | 按 PDF 逐式核查变量定义 |

## 10. 复用层

- 可复用选题角度：把复杂工程/物理问题转化为“效率、精度、可靠性、性能或可解释性”的可验证改进。
- 可复用 gap 表达：已有方法在高保真、低成本、跨工况、耦合机制或工程适用性之间存在张力。
- 可复用贡献表达：提出/构建一个面向具体对象的模型或实验框架，并通过对比验证其精度、效率或性能收益。
- 可复用论证链：问题重要性 -> 文献分类 -> 明确 gap -> 方法设计 -> 验证设置 -> 图表证据 -> 结论回收。
- 可复用图表设计：先给对象/框架示意图，再给流程图/参数表，最后给对比结果、误差和敏感性图。
- 不可直接模仿：具体数据、实验平台、材料体系、仿真模型、团队资源和未公开代码。
- 迁移到自己论文的三件事：
  1. 让 Introduction 的 gap 与 Method 的输入输出一一对应；
  2. 让每个强 claim 至少对应一个图表、一个指标和一个对比对象；
  3. 在 Conclusion 中只回收已验证内容，主动标注适用边界。

## 11. 质量自检

- 模式：精细拆解
- 对象：单篇论文
- 样本边界是否清晰：是
- 十层字段是否覆盖：是
- Claim-Evidence 是否完成：是，基于自动抽取的强 claim 候选和图表/公式/参考文献证据
- 图表功能是否解释：是，但图像细节需 PDF 核查
- 引用策略是否解释：是
- 风险是否具体：是
- 可复用资产是否具体：是
- 不确定项：公式符号、图像细节、部分图表标题和真实段落位置仍需 PDF 视觉核查
- 下一步建议：若要用于正式写作模仿，应人工复核 PDF 中关键图、公式和 Introduction 文献转折段。
