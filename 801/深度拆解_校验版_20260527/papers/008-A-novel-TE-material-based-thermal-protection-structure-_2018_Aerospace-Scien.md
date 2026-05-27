# 论文深度拆解：008-A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien

> 生成依据：`801/cleantext/008-A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`008-A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien.pdf`
- 页数：13
- clean body 字符数：47862
- 摘要字符数：1123
- 参考文献条数：40
- 图题数：16
- 表题数：3
- 表格文件数：3
- 公式候选数：185
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "10 formula(s) need manual review."}]

## 1. 身份层

- 标题：008-A-novel-TE-material-based-thermal-protection-structure-_2018_Aerospace-Scien
- 年份：2018
- 期刊/来源：Aerospace Scien
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle. At present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids resolution. These values provide references for the TPS design of vehicles with different internal temperature control demands.
- 主要方法：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory. The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9. For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is f
- 主要证据：图表 19 个标题、公式 185 个候选、参考文献 40 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle. At present, the numerical method still has some challenges, such as”，可以通过“In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a ty”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles. On the other hand, for a TPS based on non-ablative material [17–19], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency. The unit cell model (model formulation, model structure, mesh and boundaries) is shown in Fig.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle. At present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids resolution. These values provide references for the TPS design of vehicles with different internal temperature control demands.
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
- 作者声明或文本中可见 gap：However, they are much more efficient. However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission. However, the temperature on the top surface in Fig.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- For the application of flight vehicles, to the authors’ knowledge, the relevant researches are limited: Li and Wang [23] developed an integrated TE module with regenerative cooling system, and analyzed its performance based on the exergy analysis theory; Cheng et al. [24] developed a multi-stage TE module considering the suitable temperature of TE material, and analyzed its thermal protection performance.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory. The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9. For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：模型/预测 + 对比验证型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：模型/预测 + 对比验证型
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
| In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory. | 摘要/引言/结论候选 | 图：Fig. 1. The vehicle and the trajectory. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles. | 摘要/引言/结论候选 | 图：Fig. 2. The aerodynamic heat flux. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| During the last decades, numerous relevant studies have been carried on to develop appropriate numerical method (mainly CFD) for the aerodynamic heat prediction of flow fields/vehicle with different configurations [4–8]. | 摘要/引言/结论候选 | 图：Fig. 4. The heat transfer path. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| At present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids resoluti | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| On the other hand, the engineering-based algorithms and programs, such as MINIVER [9] and LATCH [10] which are developed based on empirical correlations and engineering purposes are very popular. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Ma et al. [11] developed an integrated TPS with additional insulation layer, and different insulation material/structure including Mullite blanket, ceramic tile and aerogel are evaluated. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (36.27, 696.06, 199.78, 715.22)]] * Corresponding author. E-mail addre | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The vehicle and the trajectory. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 2. The aerodynamic heat flux. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The heat transfer path. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. The multi-functional TPS structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. The fabrication of n-type material and the measurement of Seebeck coefficient. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The Seebeck coefficient and electric resistivity. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. The model, mesh and boundaries. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 8. Interfaces and relevant thermal contact resistances. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Temperature fields (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.) | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. Temperatures on the top and the bottom surface of the structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 11. The distribution of y-displacement. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. Results comparison between different boundary conditions (y-displacement). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. The distribution of electric potential. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. The total electric potential. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. The thermo-electric results of p and n couple. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (36.27, 696.06, 199.78, 715.22)]] * Corresponding author. E-mail address: leonwood @nwpu . | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (32.58, 209.57, 283.81, 222.98)]] q = hconv(Tr -T w) = σεT 4 w + qcond (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (35.09, 621.27, 245.62, 634.41)]] T ∗= Te + 0.58(T w -Te) + 0.19(Tr -Te) (Mae < 5) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (35.09, 634.35, 278.96, 647.5)]] T ∗= 0.7Te + 0.58(T w -Te) + 0.23(Tr -Te) (5 < Mae < 10) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (43.4, 639.62, 80.85, 656.62)]] Z T = kS2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 4, bbox (71.79, 640.97, 147.93, 663.57)]] λ T, S = -�E | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (76.34, 635.22, 126.98, 661.45)]] Thermal conductivity (p) (W/(m K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (147.37, 635.22, 197.3, 661.45)]] Thermal conductivity (n) (W/(m K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency. In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory. The thermoelectric module in the structure can convert a certain amount of aerodynamic heat into electricity supply. The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9. For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated. The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles.

### 7.4 摘要中文翻译

> 传统的高超声速飞行器热防护系统（TPS）通常仅用于热防护目的，效率较低。本文提出了一种基于热电材料的多功能TPS结构概念，并基于特定车辆和典型轨迹开发了其机械热电性能的评估方法。结构中的热电模块可以将一定量的空气动力热转化为电能。该模块由基于固相反​​应方法制备的n型Sr0.9La0.1TiO3化合物和广泛使用的p型Ca3Co4O9组成。针对具有典型弹道曲线的特定高超声速飞行器，通过工程化算法计算气动热，基于晶胞模型分析结构的非定常机械热电特性，最终评估热电转换效率。结果表明，多功能TPS结构在高超声速飞行器上具有显着的应用潜力。

### 7.5 结论完整摘录

识别到的结论位置：Conclusions

> In this work, a thermoelectric material based multifunctional TPS structure is proposed and the relevant evaluation approach is developed. The TE module in the structure can convert a certain amount of aerodynamic heat into electricity supply. The TE couple consists of $\mathsf{Ca} _ {3} \mathsf{Co} _ {4} \mathsf{O} _ {9}$ based p-type material, and $\mathrm{Sr} _ {0.9} \mathrm{La} _ {0.1} \mathrm{Ti} 0 _ {3}$ based n-type compound which is fabricated by solid state reaction method. The mechanical-thermoelectric performance of the structure is studied based on a unit cell model. The aerodynamic heat is calculated by an engineering-based method based on a typical reusable launch vehicle with a typical trajectory curve, and is used as the input boundary conditions for the numerical simulation. The simulation approach developed in this work can be used in analysis of other trajectories of hypersonic vehicles. The results show some conclusions:
> 
> 1. In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results.
> 
> 2. For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide references for the TPS design of vehicles with different internal temperature control demands.
> 
> 3. In the studied trajectory duration, a multi-functional TPS structure of 0.01 m2 can provide maximum average output powers of 0.406, 0.618, 0.756 and 0.913 W, respectively, and considering the large area of real vehicle, such TPS has potentials to provide a part substitution of power supply.
> 
> 4. Active cooling is very useful in improving the thermoelectric performance including the output power and the TE conversion efficiency.

### 7.6 结论中文翻译

> 在这项工作中，提出了一种基于热电材料的多功能TPS结构并开发了相关的评估方法。结构中的TE模块可以将一定量的空气动力热转化为电能。 TE电偶由 $\mathsf{Ca} _ {3} \mathsf{Co} _ {4} \mathsf{O} _ {9}$ 基 p 型材料和 $\mathrm{Sr} _ {0.9} \mathrm{La} _ {0.1} \mathrm{Ti} 0 _ {3}$ 基 n 型化合物组成，通过固态反应方法制备。基于晶胞模型研究了该结构的机械热电性能。基于具有典型弹道曲线的典型可重复使用运载火箭，采用工程化方法计算气动热，并作为数值模拟的输入边界条件。这项工作中开发的模拟方法可用于分析高超声速飞行器的其他轨迹。结果表明： 1. 在基于平移对称性建立的晶胞模型的热力研究中，周期性边界条件对于获得合理的结果至关重要。对于本文提出的TPS结构，如果在底部下方提供系数为10、50、100和300 W/(m2 K)的对流换热，则在研究的轨迹持续时间内，底面最高温度分别为639、497、431和364 K，这为不同内部温度控制需求的车辆的TPS设计提供参考。
> 
> 在研究的轨迹持续时间内，0.01 m2的多功能TPS结构可提供的最大平均输出功率分别为0.406、0.618、0.756和0.913 W，考虑到实际车辆的大面积，这种TPS具有提供部分电源替代的潜力。主动冷却对于提高热电性能（包括输出功率和TE转换效率）非常有用。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 5530 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. The vehicle, trajectory and aerodynamic heat | 对象/条件/子问题展开 | 636 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. The vehicle and trajectory | 对象/条件/子问题展开 | 1779 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Aerodynamic heat | 对象/条件/子问题展开 | 4057 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3. The multi-functional TPS structure | 对象/条件/子问题展开 | 2268 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.1. The choosing of p-type material | 对象/条件/子问题展开 | 1890 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.2. Fabrication of n-type material and its TE properties | 实验或测量设定 | 2466 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 8 | 3.3. Physical properties of other materials | 对象/条件/子问题展开 | 367 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.1. Governing and constitutive equations | 对象/条件/子问题展开 | 885 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | Mechanical: | 对象/条件/子问题展开 | 2909 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2. The unit cell model and its mesh | 方法建构 | 1153 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. The boundary and initial conditions | 对象/条件/子问题展开 | 2790 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | Planes: | 对象/条件/子问题展开 | 4431 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.4. Interfaces between different materials | 对象/条件/子问题展开 | 1393 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5. Results and discussions | 结果验证/讨论 | 329 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 16 | 5.1. Thermo-mechanical performance | 结果验证/讨论 | 4960 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 17 | 5.2. Thermoelectric performance | 结果验证/讨论 | 3516 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 5.3. Thermoelectric conversion efficiency | 对象/条件/子问题展开 | 3658 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | Conclusions | 主张回收/边界说明 | 1972 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 20 | Conflict of interest statement | 对象/条件/子问题展开 | 73 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(69)；heat(55)；temperature(51)；structure(45)；partial(42)；work(41)；mathsf(40)；material(39)；tps(38)；fig(37)；respectively(36)；aerodynamic(32)；materials(32)；vehicle(30)；surface(30)；boundary(30)；thermal(24)；bottom(24)；frac(24)；tcr(23)
- 高频学术名词/术语：temperature(51)；structure(45)；performance(17)；conversion(14)；condition(11)；calculation(11)；influence(9)；insulation(8)；duration(8)；deviation(8)；conductivity(7)；difference(7)；figure(7)；resistance(7)；evaluation(6)
- 高频学术动词：developed(11)；obtained(9)；evaluated(5)；predict(1)；develop(1)；introduced(1)；evaluate(1)；indicated(1)；validate(1)；indicate(1)
- 高频形容词：partial(42)；material(39)；aerodynamic(32)；boundary(30)；thermal(24)；electric(21)；coefficient(21)；convective(17)；potential(17)；typical(14)；electrical(11)；thermoelectric(9)；numerical(8)；periodic(8)；specific(7)
- 高频副词：respectively(36)；supply(5)；mainly(3)；especially(2)；carefully(2)；closely(2)；directly(2)；widely(2)；separately(2)；partly(1)；fly(1)；relatively(1)
- 高频二词短语：mathrm mathrm(30)；aerodynamic heat(28)；mathsf mathsf(22)；frac partial(21)；tps structure(18)；heat flux(15)；boundary conditions(14)；unit cell(14)；conversion efficiency(12)；convective coefficient(11)；electric potential(11)；partial frac(11)；partial partial(11)；bottom surface(11)；output power(10)
- 高频三词短语：mathrm mathrm mathrm(14)；partial frac partial(11)；frac partial partial(11)；mathsf mathsf mathsf(8)；temperature top surface(7)；aerodynamic heat flux(6)；frac partial tau(6)；partial tau partial(6)；tau partial frac(6)；displaystyle frac partial(6)；multi-functional tps structure(5)；mathsf mathsf mathrm(5)
- 被动语态估计：128
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：255
- 一般过去时线索：282
- 现在完成时线索：1
- 情态动词线索：76

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Thus, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle.
  - 可迁移句型：{object}, a reliable and efficient thermal protection system (TPS) is essential to ensure the safety of the vehicle.
- 原句：In the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results.
  - 可迁移句型：{object} the thermal-mechanical studies of a unit cell model that formulated based on translational symmetries, the periodic boundary condition is essential to obtaining reasonable results.
### gap/转折句
- 原句：At present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids resolution.
  - 可迁移句型：{object} present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids re
- 原句：However, they are much more efficient.
  - 可迁移句型：{object}, they are much more efficient.
- 原句：However, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
  - 可迁移句型：{object}, it is not applicable to a reusable vehicle due to its changing configuration during the flight mission.
- 原句：However, the temperature on the top surface in Fig.
  - 可迁移句型：{object}, the temperature on the top surface in Fig.
### 方法提出句
- 原句：In this paper, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory.
  - 可迁移句型：{object} This study, a thermoelectric material based multifunctional TPS structure concept is proposed and the evaluation approach of its mechanical- thermoelectric performance is developed based on a specific vehicle and a typical trajectory.
- 原句：The module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
  - 可迁移句型：{object} module consists of n-type Sr0.9La0.1TiO3 compound which is fabricated based on the solid state reaction method, and the widely used p-type Ca3Co4O9.
- 原句：For a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell model and the thermoelectric conversion efficiency is finally evaluated.
  - 可迁移句型：{object} a specific hypersonic flight vehicle with a typical trajectory curve, the aerodynamic heat is calculated by an engineering-based algorithm, the unsteady mechanical-thermoelectric characteristics of the structure is then analyzed based on a unit cell m
- 原句：There are two main methods to predict the aerodynamic heat, the engineering-based method and the numerical method.
  - 可迁移句型：{object} are two main methods to predict the aerodynamic heat, the engineering-based method and the numerical method.
### 结果证明句
- 原句：The results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles.
  - 可迁移句型：{object} results indicate that the multifunctional TPS structure has significant application potentials on the hypersonic flight vehicles.
- 原句：The unit cell model (model formulation, model structure, mesh and boundaries) is shown in Fig.
  - 可迁移句型：{object} unit cell model (model formulation, model structure, mesh and boundaries) is shown in Fig.
- 原句：As shown in the left picture of Fig.
  - 可迁移句型：{object} shown in the left picture of Fig.
- 原句：From left to right are results under 180, 495, 900 and 1400 s, respectively, and the corresponding trajectory parameters for each time are summarized in the top of the figure.
  - 可迁移句型：{object} left to right are results under 180, 495, 900 and 1400 s, respectively, and the corresponding trajectory parameters for each time are summarized in the top of the figure.
### 贡献收束句
- 原句：On the other hand, for a TPS based on non-ablative material [17–19], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
  - 可迁移句型：{object} the other hand, for a TPS based on non-ablative material [17–19], the surface radiation is the only dissipation of aerodynamic heat, and thus leaves some rooms for the improvement of its efficiency.
- 原句：These values provide references for the TPS design of vehicles with different internal temperature control demands.
  - 可迁移句型：{object} values provide references for the TPS design of vehicles with different internal temperature control demands.
- 原句：For the TPS structure proposed in this work, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 and 364 K, respectively, and this provide references for the TPS design of vehicles with different internal temperature control demands.
  - 可迁移句型：{object} the TPS structure proposed in This study, if a convection heat transfer with coefficients of 10, 50, 100 and 300 W/(m2 K) are provided under the bottom, in the studied trajectory duration the highest temperature of the bottom surface is 639, 497, 431 
- 原句：In the studied trajectory duration, a multi-functional TPS structure of 0.01 m2 can provide maximum average output powers of 0.406, 0.618, 0.756 and 0.913 W, respectively, and considering the large area of real vehicle, such TPS has potentials to provide a part substitution of power supply.
  - 可迁移句型：{object} the studied trajectory duration, a multi-functional TPS structure of 0.01 m2 can provide maximum average output powers of 0.406, 0.618, 0.756 and 0.913 W, respectively, and considering the large area of real vehicle, such TPS has potentials to provide
### 边界/谨慎句
- 原句：The traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency.
  - 可迁移句型：{object} traditional thermal protection system (TPS) of hypersonic flight vehicles is usually designed for thermal protection purpose only with low efficiency.
- 原句：For a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than 1800 K [1–3].
  - 可迁移句型：{object} a supersonic vehicle, at some specific locations of leading edge, the temperature may reach to a value of higher than 1800 K [1–3].
- 原句：At present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids resolution.
  - 可迁移句型：{object} present, the numerical method still has some challenges, such as the high requirement to mesh generation, especially the grid near the vehicle surface should be very carefully considered since the temperature gradient is very sensitive to the grids re
- 原句：For the insulation layer, the basic requirement should be the low weight and low thermal conductivity [11,12].
  - 可迁移句型：{object} the insulation layer, the basic requirement should be the low weight and low thermal conductivity [11,12].

## 9. 引用风险层

- 正文引用簇估计：20
- 参考文献条数：40
- 可识别年份条目数：42
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：14
- 高频来源粗略识别：Sci. Technol(8)；Therm. Eng(7)；Aerosp. Sci(2)；Phys. Lett(2)；Mater(2)；Spacecr. Rockets(1)；Mater. Sci(1)；Manag(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re-usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [2] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [3] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [4] D. Knight, H. Yan, A.G. Panaras, A. Zheltovodov, Advances in CFD prediction of shock wave turbulent boundary layer interactions, Prog. Aerosp. Sci. 39 (2) (2003) 121–184.
- [5] D. Knight, J. Longo, D. Drikakis, D. Gaitonde, A. Lani, I. Nompelis, B. Reimann, L. Walpot, Assessment of CFD capability for prediction of hypersonic shock in- teractions, Prog. Aerosp. Sci. 48 (Supplement C) (2012) 8–26.
- [6] Y. Kerboua, A.A. Lakis, Numerical model to analyze the aerodynamic behavior of a combined conical–cylindrical shell, Aerosp. Sci. Technol. 58 (Supplement C) (2016) 601–617.
- [7] P. Panagiotou, P. Kaparos, C. Salpingidou, K. Yakinthos, Aerodynamic design of a MALE UAV, Aerosp. Sci. Technol. 50 (Supplement C) (2016) 127–138.
- [8] P.D. Bravo-Mosquera, L. Botero-Bolivar, D. Acevedo-Giraldo, H.D. Cerón-Muñoz, Aerodynamic design analysis of a UAV for superficial research of volcanic envi- ronments, Aerosp. Sci. Technol. 70 (Supplement C) (2017) 600–614.
- [9] C.D. Engel, S.C. Praharaj, MINIVER Upgrade for the AVID System. Vol. 1: LAN- MIN User’s Manual, Nasa Cr, 1983.
- [10] E.V. Zoby, K. Sutton, Approximate convective-heating equations for hypersonic flows, J. Spacecr. Rockets 18 (1) (1981) 64.
- [11] Y. Ma, B. Xu, M. Chen, R. He, W. Wen, T. Cheng, D. Fang, Optimization design of built-up thermal protection system based on validation of corrugated core homogenization, Appl. Therm. Eng. 115 (2017) 491–500.
- [12] S. Kumar, S.P. Mahulikar, Reconstruction of aero-thermal heating and ther- mal protection material response of a reusable launch vehicle using inverse method, Appl. Therm. Eng. 103 (Supplement C) (2016) 344–355.
- [13] R. Savino, M. De Stefano Fumo, D. Paterna, M. Serpico, Aerothermodynamic study of UHTC-based thermal protection systems, Aerosp. Sci. Technol. 9 (2) (2005) 151–160.
- [14] S. Liu, B. Zhang, Effects of active cooling on the metal thermal protection sys- tems, Aerosp. Sci. Technol. 15 (7) (2011) 526–533.
- [15] R.J. Tobe, R.V. Grandhi, Hypersonic vehicle thermal protection system model optimization and validation with vibration tests, Aerosp. Sci. Technol. 28 (1) (2013) 208–213.

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
