# 论文深度拆解：031-Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and

> 生成依据：`801/cleantext/031-Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`031-Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.pdf`
- 页数：23
- clean body 字符数：79247
- 摘要字符数：2499
- 参考文献条数：52
- 图题数：18
- 表题数：1
- 表格文件数：1
- 公式候选数：139
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "4 formula(s) need manual review."}]

## 1. 身份层

- 标题：031-Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and
- 年份：2022
- 期刊/来源：Journal of Fluids and
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Article history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021 Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. In recent years, the relevant vegetated flows have been studied experimentally and numerically by researchers, from single vegetation (O’Connor and Revell, 2019; Zhang et al., 2020) to dual v
- 主要方法：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it. The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
- 主要证据：图表 19 个标题、公式 139 个候选、参考文献 52 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Article history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021 Vegetation canopies, such as seagras”，可以通过“The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumpt”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 2002).
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Article history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021 Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. In recent years, the relevant vegetated flows have been studied experimentally and numerically by researchers, from single vegetation (O’Connor and Revell, 2019; Zhang et al., 2020) to dual vegetation (Zhang et al., 2020) an Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. (2007), but the detailed mechanism behind it still needs to be investigated further.
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
- 作者声明或文本中可见 gap：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore. However, the dynamic motion of the vegetation elements as well as the variation of the response with bending rigidity and canopy density, is still relevant to the real vegetation canopy.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it. The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
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
| The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving. | 摘要/引言/结论候选 | 图：Fig. 1. Velocity profile and the wavelike motion of vegetation canopy. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation. | 摘要/引言/结论候选 | 图：Fig. 2. Schematic of computational domain. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the veget | 摘要/引言/结论候选 | 图：Fig. 3. Instantaneous snapshots of out-of-plane vorticity and vegetation deflections for six representative cases. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 3, bbox (63.46, 410.35, 505.9, 432.93)]] ∂f ∂t + e · ∇xf + F · ∇ef = Ωf (1) | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 2002). | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 3, bbox (62.27, 482.75, 91.99, 498.47)]] Ωf = 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Velocity profile and the wavelike motion of vegetation canopy. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Schematic of computational domain. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Instantaneous snapshots of out-of-plane vorticity and vegetation deflections for six representative cases. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Parameter map with observed behavior modes for the vegetation canopy. The range of bending rigidity and canopy density is given by K0∼K11 and Φ0∼Φ10. (F | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Flow over the canopy for different bending rigidities. Flow streamlines displayed over contours of vertical velocity.. (For interpretation of the refere | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The mean drag coefficient and the amplitude of drag coefficient of the vegetation along canopy. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. The mean deflection angle and the angular amplitude of oscillation of vegetation across the canopy (Φ4K1). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Snapshot of out-of-plane vorticity and vegetation deflections for Φ4K1 case with K2 vegetation.. (For interpretation of the references to color in this  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Instantaneous snapshots of vorticity and vegetation deflection for different canopy densities. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Flow over the start of the canopy for different canopy densities. Flow streamlines displayed over contours of vertical velocity. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Variation of the streamwise velocity and its gradient in the wall-normal direction for different canopy densities. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. Waving frequencies of vegetation canopy in different test cases. The range of bending rigidity and canopy density is given by K1∼K10 and Φ1∼Φ9. Marker  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. The estimated KH frequencies of vegetation canopy for different canopy density branches (Φ0.25∼Φ9). The range of bending rigidity is given by K0∼K11. M | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The influence of mixing layer on the waving frequencies of vegetation for different canopy density branches (Φ2, Φ4 and Φ7). The range of bending rigid | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Parameter map with observed behavior modes for the vegetation canopy. The range of bending rigidity and canopy density is given by K 0∼K 11 and Φ0∼Φ10.  | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (63.46, 410.35, 505.9, 432.93)]] ∂f ∂t + e · ∇xf + F · ∇ef = Ωf (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.27, 482.75, 91.99, 498.47)]] Ωf = 1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (87.0, 483.74, 133.73, 504.7)]] τ ( f (eq) -f ) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (62.27, 533.91, 109.7, 549.84)]] υ = ( τ -1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.27, 603.37, 106.52, 616.27)]] f (eq) α = ρwα | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (62.27, 672.27, 89.76, 689.05)]] Fα = ( | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (62.27, 70.32, 93.97, 81.91)]] ρ = ∑ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (128.39, 95.77, 192.7, 117.27)]] 2 f δt = ρv∗+ 1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The waving motion of a submerged vegetation canopy is associated with the generation of coherent vortices on the top of the canopy, which arise as the manifestation of the mixing layer instability. The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it. The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving. The vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation. In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © 2021 Elsevier Ltd. All rights reserved.
> Article history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021
> Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). Most of these services are implemented through the fluid–structure interactions (FSI) between vegetation and the fluid flows they thrive in. Understanding the mechanisms of such interactions is crucial in predicting the flow stimulus on vegetation growth (Moulia and Combes, 2006) and avoiding the flow-induced damage to crops (Berry et al., 2004). In recent years, the relevant vegetated flows have been studied experimentally and numerically by researchers, from single vegetation (O’Connor and Revell, 2019; Zhang et al., 2020) to dual vegetation (Zhang et al., 2020) an

### 7.4 摘要中文翻译

> 水下植被冠层的波动运动与冠层顶部相干涡流的产生有关，这是混合层不稳定性的表现。混合层上方的不稳定流之间的相互作用及其对植被冠层本身的影响仍然相对未得到充分探索，大多数先前的研究都采用重要的建模假设来简化系统。在本文中，采用完全耦合的流体-结构建模方法来研究植被冠层与其上方出现的混合层之间的相互作用机制。探讨了植被行为对弯曲刚度和冠层密度的依赖性，观察了植被的五种代表性行为状态：静态、扑动、双重、规则波动和不规则波动。比较了在与每个状态相关的混合层中观察到的涡流结构，并研究了冠层密度对混合层发展的影响，特别关注与植被相关的流动特征。此外，在混合层不稳定频率与植被固有频率的交叉区域观察到锁定效应，这表明混合层对植被波动频率的吸引作用。 © 2021 Elsevier Ltd. 文章历史： 接收日期 2021 年 1 月 26 日 收到修订版 2021 年 9 月 30 日 接受日期 2021 年 12 月 3 日 在线提供 2021 年 12 月 22 日 海草草甸、农田和茂密森林等植被冠层在自然界中丰富，在广泛的生态服务中发挥着重要作用。
> 
> 这些树冠可以为野生动物提供栖息地（Carpenter 和 Lodge，1986），捕获悬浮沉积物（Palmer 等，2004），调节温度（Karlsson，2000）并改善水/空气质量（Moore，2004）。大多数这些服务是通过植被和它们赖以生长的流体之间的流固相互作用（FSI）来实现的。了解这种相互作用的机制对于预测流对植被生长的刺激（Moulia 和 Combes，2006）和避免流引起的对作物的损害（Berry 等，2004）至关重要。近年来，研究人员对相关植被流进行了实验和数值研究，从单一植被（O’Connor和Revell，2019；Zhang等，2020）到双植被（Zhang等，2020）和

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> A direct fluid–structure modeling approach realized via a lattice Boltzmann-immersed boundary-finite element model is used to investigate the interaction between a vegetation canopy and the mixing layer. The dependence of vegetation behaviors on the bending rigidity and canopy density is explored and five representative response modes are observed: static, flapping, dual, regular waving and irregular waving. Through comparison of the vortical structures associated with different behavior modes, the influence of bending rigidity on the vortical structures in the mixing layer is investigated. In the flapping behavior, the centers of coherent vortices are lower than the tip of the vegetation, causing the vegetation to exhibit strong shear stress and to undergo mode-two deformation. While in the waving behavior, the rotational centers of coherent vortices are shifted upwards as the resistance of vegetation against the mixing layer is increased. As a result, the shear stress of the vegetation is negligible and its deformation transits to mode-one. The imbalance between the mixing layer production and canopy dissipation causes temporal and spatial variation in the waving amplitude of the vegetation; the waving motion of vegetation transits from a regular state to an irregular one. In addition, a spontaneous vertical transport from the canopy to the mixing layer is found in the flapping behavior, which is associated with the sandification of land. This finding indicates that increasing the canopy density and bending rigidity of the vegetation are both able to protect land from sandification. Finally, inspired by the dual behavior, a protection strategy for fragile crops is proposed by interspersing crop of different rigidity.
> 
> The influence of canopy density on the development of the mixing layer instability indicates that increasing the canopy density can decrease the vertical flow exchange between the canopy and the overlying flow, and further increase the intensity of the mixing layer. As a result, the onset of the mixing layer instability moves forward along canopy. The dynamic response of the canopy is the collective result of canopy density and bending rigidity of the vegetation. The increase of these two parameters can improve the resistance of the vegetation canopy, but also acts to increase the mixing layer intensity above the canopy. However, increasing these two parameters further acts to suppress the initial oscillation of vegetation, arresting the development of the mixing layer instability altogether.
> 
> The measured frequency response of the vegetation canopy is found to follow the first-order natural frequency in the waving branch and the second-order natural frequency in the flapping branch. The lock-in effect is observed in the cross region between the KH frequency and the natural frequency of the vegetation. These findings reveal an attraction effect of the mixing layer on the waving frequencies of vegetation and indicate that the governing mechanism for the dynamic motion of the vegetation is a coupling of the mixing layer and structural properties. The structural properties play a dominant role on the dynamic motion of the vegetation, while the mixing layer causes the waving frequency to display a deviation on its original trend. As the Reynolds number of the flow increases further, the attractive effect of the mixing layer is expected to become more dominant.
> 
> Although further insight and some meaningful conclusions are obtained in the present work, several areas remain for further investigation. Firstly, the spontaneous vertical transport found in the flapping behavior of the vegetation has a great significance for the control of the local wind erosion and/or the sandification. In further studies, the influence of gravity and buoyancy on this vertical transport should be incorporated. The proposed protection strategy for fragile crops also warrants further investigation. Finally, although physical insight gained from two-dimensional study is expected to be instructive, a fully three-dimensional analysis should be undertaken to confirm the extent of this approximation, exploring the impact of reduced blockage and an assessment of the transverse motion in the vegetation canopy.
> 
> (a) Range (minimum, maximum and time-averaged value) of tip deflection of each vegetation element along the canopy. 
> (b) Time histories of tip deflection of the 100th vegetation element over the final 10 seconds of simulation. 
> Fig. A.1. Results of the grid independence test for different grid resolutions $( N _ {I B M} = 30 , 40 , 50 \ \mathrm{and} \ 60 )$

### 7.6 结论中文翻译

> 通过格子玻尔兹曼浸没边界有限元模型实现的直接流体结构建模方法用于研究植被冠层和混合层之间的相互作用。探讨了植被行为对弯曲刚度和冠层密度的依赖性，并观察到五种代表性的响应模式：静态、扑动、双重、规则波动和不规则波动。通过比较不同行为模式下的涡结构，研究了弯曲刚度对混合层涡结构的影响。在扑动行为中，相干涡中心低于植被尖端，导致植被表现出强烈的剪应力并发生二模态变形。在波动行为中，随着植被对混合层的阻力增加，相干涡旋的旋转中心向上移动。因此，植被的剪应力可以忽略不计，其变形过渡到模式一。混合层产生与冠层消散之间的不平衡导致植被波动幅度的时空变化；植被的波动从规则状态转变为不规则状态。此外，在扑动行为中发现了从冠层到混合层的自发垂直传输，这与土地沙化有关。这一发现表明，增加植被的冠层密度和弯曲刚度都能够保护土地免受沙化。最后，受双重行为的启发，提出了一种通过散布不同硬度作物来保护脆弱作物的策略。
> 
> 冠层密度对混合层不稳定性发展的影响表明，增加冠层密度可以减少冠层与上覆流之间的垂直流交换，进一步增加混合层的强度。结果，混合层不稳定的开始沿着树冠向前移动。冠层的动态响应是冠层密度和植被弯曲刚度的共同结果。这两个参数的增加可以提高植被冠层的抵抗力，同时也起到增加冠层上方混合层强度的作用。然而，增加这两个参数进一步抑制植被的初始振荡，完全阻止混合层不稳定性的发展。发现植被冠层的测量频率响应遵循摆动分支中的一阶固有频率和摆动分支中的二阶固有频率。在 KH 频率和植被自然频率之间的交叉区域观察到锁定效应。这些发现揭示了混合层对植被波动频率的吸引效应，并表明植被动态运动的控制机制是混合层和结构特性的耦合。结构特性对植被的动态运动起主导作用，而混合层则导致波动频率偏离原来的趋势。随着流动雷诺数进一步增加，混合层的吸引力预计将变得更加占主导地位。
> 
> 尽管在目前的工作中获得了进一步的见解和一些有意义的结论，但仍有几个领域需要进一步研究。首先，植被拍打行为中发现的自发垂直输送对于控制局部风蚀和/或沙化具有重要意义。在进一步的研究中，应考虑重力和浮力对这种垂直传输的影响。拟议的脆弱作物保护策略也值得进一步研究。最后，虽然从二维研究中获得的物理见解预计具有指导意义，但应进行完整的三维分析来确认这种近似的程度，探索减少堵塞的影响并评估植被冠层的横向运动。 (a) 沿冠层的每个植被元素的尖端偏转范围（最小值、最大值和时间平均值）。 (b) 在模拟的最后 10 秒内第 100 个植被单元的尖端偏转的时间历史。不同网格分辨率的网格独立性测试结果$( N _ {IB M} = 30 , 40 , 50 \ \mathrm{and} \ 60 )$

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 10216 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Lattice Boltzmann method | 方法建构 | 2756 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Finite element method | 方法建构 | 2010 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. Immersed boundary method | 方法建构 | 2491 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 2.4. fluid–structure coupling | 对象/条件/子问题展开 | 2473 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3. Numerical settings and parameter space | 对象/条件/子问题展开 | 5309 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.1. Dynamic behaviors of vegetation canopy | 对象/条件/子问题展开 | 3706 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.2. Vortical structures in different vegetation behaviors | 对象/条件/子问题展开 | 15042 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.3. The influence of canopy density on mixing layer instability | 对象/条件/子问题展开 | 9890 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.4. Lock in effect | 对象/条件/子问题展开 | 13770 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.5. Discussion on the effects of other parameters | 结果验证/讨论 | 6074 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 12 | 5. Conclusions | 主张回收/边界说明 | 4629 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 13 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 279 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：vegetation(252)；canopy(191)；layer(114)；mixing(113)；waving(89)；pmb(86)；flow(84)；frequency(80)；fig(79)；instability(68)；velocity(55)；behavior(55)；density(51)；fluid(50)；vortices(48)；flapping(47)；bending(45)；frequencies(42)；rigidity(41)；natural(40)
- 高频学术名词/术语：vegetation(252)；instability(68)；velocity(55)；density(51)；rigidity(41)；motion(29)；structure(28)；deflection(27)；element(25)；intensity(24)；section(18)；inflection(16)；addition(14)；influence(14)；resistance(14)
- 高频学术动词：indicated(14)；investigated(14)；obtained(10)；compared(6)；predicted(6)；investigate(6)；demonstrated(6)；presented(5)；estimated(2)；introduced(2)；demonstrate(2)；obtain(1)；validated(1)；reveal(1)；indicate(1)
- 高频形容词：natural(40)；coherent(36)；dynamic(31)；coefficient(26)；vertical(25)；element(25)；dual(24)；static(24)；boundary(15)；previous(13)；aquatic(12)；partial(12)；terrestrial(11)；development(9)；several(8)
- 高频副词：respectively(10)；gradually(10)；slightly(8)；finally(6)；clearly(5)；fully(4)；widely(4)；highly(4)；generally(4)；rapidly(4)；eventually(4)；relatively(3)
- 高频二词短语：mixing layer(111)；vegetation canopy(41)；layer instability(38)；bending rigidity(38)；canopy density(36)；coherent vortices(34)；natural frequency(29)；drag coefficient(25)；see fig(17)；vegetation element(17)；fluid structure(16)；inflection point(16)；vegetation elements(16)；irregular waving(16)；connor revell(15)
- 高频三词短语：mixing layer instability(38)；intensity mixing layer(14)；mean drag coefficient(11)；amplitude drag coefficient(9)；left pmb right(8)；bending rigidity increases(8)；increasing canopy density(8)；dynamic motion vegetation(7)；regular waving irregular(7)；waving irregular waving(7)；bending rigidity canopy(7)；waving frequency vegetation(7)
- 被动语态估计：185
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：347
- 一般过去时线索：478
- 现在完成时线索：3
- 情态动词线索：71

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Article history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021 Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
  - 可迁移句型：{object} history: Received 26 January 2021 Received in revised form 30 September 2021 Accepted 3 December 2021 Available online 22 December 2021 Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an impor
- 原句：In recent years, the relevant vegetated flows have been studied experimentally and numerically by researchers, from single vegetation (O’Connor and Revell, 2019; Zhang et al., 2020) to dual vegetation (Zhang et al., 2020) an Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
  - 可迁移句型：{object} recent years, the relevant vegetated flows have been studied experimentally and numerically by researchers, from single vegetation (O’Connor and Revell, 2019; Zhang et al., 2020) to dual vegetation (Zhang et al., 2020) an Vegetation canopies, such as 
- 原句：Then the macroscopic fluid quantities can be obtained by: $$\begin{array} {l} {\displaystyle \rho = \sum _ {\alpha} f _ {\alph In the present study, the effects of bending rigidity and canopy density on the dynamics of vegetation canopy are investigated by only varying these two parameters while keeping the other fixed.
  - 可迁移句型：{object} the macroscopic fluid quantities can be obtained by: $$\begin{array} {l} {\displaystyle \rho = \sum _ {\alpha} f _ {\alph In the present study, the effects of bending rigidity and canopy density on the dynamics of vegetation canopy are investigated by
- 原句：In this case, three-dimensional (3-D) physical effects become very important and the current 2-D model will be insufficient.
  - 可迁移句型：{object} this case, three-dimensional (3-D) physical effects become very important and the current 2-D model will be insufficient.
### gap/转折句
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  - 可迁移句型：{object} interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  - 可迁移句型：{object}, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
- 原句：However, the dynamic motion of the vegetation elements as well as the variation of the response with bending rigidity and canopy density, is still relevant to the real vegetation canopy.
  - 可迁移句型：{object}, the dynamic motion of the vegetation elements as well as the variation of the response with bending rigidity and canopy density, is still relevant to the real vegetation canopy.
- 原句：However, these gravity/buoyancy forces do have influences on the dynamics of vertical flow currents and vegetation elements.
  - 可迁移句型：{object}, these gravity/buoyancy forces do have influences on the dynamics of vertical flow currents and vegetation elements.
### 方法提出句
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  - 可迁移句型：{object} interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句：In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
  - 可迁移句型：{object} This study a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
- 原句：The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
  - 可迁移句型：{object} dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
- 原句：The vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation.
  - 可迁移句型：{object} vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation.
### 结果证明句
- 原句：In addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the vegetation. © 2021 Elsevier Ltd.
  - 可迁移句型：{object} addition, the lock-in effect is observed in the crossover region between the frequency of the mixing layer instability and the natural frequency of the vegetation, which indicates an attraction effect of the mixing layer on the waving frequency of the
- 原句：In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 2002).
  - 可迁移句型：{object} addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 20
- 原句：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig.
  - 可迁移句型：{object} wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig.
- 原句：(1996) indicated that some characteristics of terrestrial/aquatic flows through and over vegetation canopies resembled those of a mixing layer (a free shear layer characterized by two regions of velocity separated by a confined region containing an inflection point, see Fig.
  - 可迁移句型：(1996) indicated that some characteristics of terrestrial/aquatic flows through and over vegetation canopies resembled those of a mixing layer (a free shear layer characterized by two regions of velocity separated by a confined region containing an inflection 
### 贡献收束句
- 原句：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
  - 可迁移句型：{object} canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
- 原句：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
  - 可迁移句型：{object} canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
- 原句：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig.
  - 可迁移句型：{object} wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig.
- 原句：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  - 可迁移句型：{object}, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
### 边界/谨慎句
- 原句：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  - 可迁移句型：{object}, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
- 原句：Then the macroscopic fluid quantities can be obtained by: $$\begin{array} {l} {\displaystyle \rho = \sum _ {\alpha} f _ {\alph In the present study, the effects of bending rigidity and canopy density on the dynamics of vegetation canopy are investigated by only varying these two parameters while keeping the other fixed.
  - 可迁移句型：{object} the macroscopic fluid quantities can be obtained by: $$\begin{array} {l} {\displaystyle \rho = \sum _ {\alpha} f _ {\alph In the present study, the effects of bending rigidity and canopy density on the dynamics of vegetation canopy are investigated by
- 原句：In further studies, the influence of gravity and buoyancy on this vertical transport should be incorporated.
  - 可迁移句型：{object} further studies, the influence of gravity and buoyancy on this vertical transport should be incorporated.
- 原句：Finally, although physical insight gained from two-dimensional study is expected to be instructive, a fully three-dimensional analysis should be undertaken to confirm the extent of this approximation, exploring the impact of reduced blockage and an assessment of the transverse motion in the vegetation canopy.
  - 可迁移句型：{object}, although physical insight gained from two-dimensional study is expected to be instructive, a fully three-dimensional analysis should be undertaken to confirm the extent of this approximation, exploring the impact of reduced blockage and an assessment

## 9. 引用风险层

- 正文引用簇估计：17
- 参考文献条数：52
- 可识别年份条目数：53
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：34
- 高频来源粗略识别：J. Fluid Mech(3)；Phys. Fluids(2)；J. Geophys. Res. Oceans(2)；J. Comput. Phys(2)；Annu. Rev. Fluid Mech(1)；Understanding and reducing lodging in cereals. Adv. Agron(1)；Phys. Rev(1)；Effects of submersed macrophytes on ecosystem processes. Aquat. Bot(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Belcher, S.E., Harman, I.N., Finnigan, J.J., 2012. The wind in the willows: flows in forest canopies in complex terrain. Annu. Rev. Fluid Mech. 44, 479–504.
- Belcher, S., Jerram, N., Hunt, J., 2003. Adjustment of a turbulent boundary layer to a canopy of roughness elements. J. Fluid Mech. 488, 369–398.
- Berry, P.M., Sterling, M., Spink, J.H., Baker, C.J., Sylvester-Bradley, R., Money, S.J., Tams, A.R., Ennos, A.R., Sparks, D.L., 2004. Understanding and reducing lodging in cereals. Adv. Agron. 84, 217–271.
- Bhatnagar, P.L., Gross, E.P., Krook, M., 1954. A model for collision processes in gases. I. Small amplitude processes in charged and neutral one-component systems. Phys. Rev. 94 (3), 511–525.
- Carpenter, S.R., Lodge, D.M., 1986. Effects of submersed macrophytes on ecosystem processes. Aquat. Bot. 26, 341–370.
- Chandler, M., Colarusso, P., Buchsbaum, R., 1996. A study of eelgrass beds in Boston Harbor and northern Massachusetts bays. In: Proj. Rep. Off. Res. Dev. US EPA, Narragansett, RI.
- Chen, S., Doolen, G.D., 1998. Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech. 30, 329–364.
- Chung, H., Chen, S.S., 1984. Hydrodynamic Mass (No. CONF-840647–9). Argonne National Lab., United States.
- De, L.E., 2008. Effects of wind on plants. Annu. Rev. Fluid Mech. 40, 141–168. De Rosis, A., Falcucci, G., Ubertini, S., Ubertini, F., 2014b. Aeroelastic study of flexible flapping wings by a coupled lattice Boltzmann-finite element approach with immersed boundary method. J. Fluids Struct. 49, 516–533. De Rosis, A., Ubertini, S., Ubertini, F., 2014a. A partitioned approach for two-dimensional fluid–structure interaction problems by a coupled lattice Boltzmann-finite element method with immersed 
- Dong, D., Chen, W., Shi, S., 2016. Coupling motion and energy harvesting of two side-by-side flexible plates in a 3D uniform flow. Appl. Sci. 6 (5), 141.
- Doyle, J.F., Desantiago, E., 2001. Nonlinear Analysis of Thin-Walled Structures: Statics, Dynamics, and Stability. In: Mechanical Engineering Series, Springer New York.
- Ebeling, J.M., Jenkins, B.M., 1985. Physical and chemical properties of biomass fuels. Trans. ASAE 28 (3), 898–901.
- Fang, Z., Gong, C., Revell, A., Chen, G., Harwood, A., O’Connor, J., 2019. Passive separation control of a NACA0012 airfoil via a flexible flap. Phys. Fluids 31 (10), 101904.
- Favier, J., Li, C., Kamps, L., Revell, A., O’Connor, J., Brücker, C., 2017. The pelskin project – part I: fluid–structure interaction for a row of flexible flaps: a reference study in oscillating channel flow. Meccanica 52 (8), 1767–1780.
- Felippa, C.A., Haugen, B., 2005. A unified formulation of small-strain corotational finite elements: I. theory. Comput. Methods Appl. Mech. Eng. 194 (21–24), 2285–2335.

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
