# 论文深度拆解：A mesomechanical model for predicting the degradation in stiffness of FRP composites subjected to combined thermal and mechanical loading

> 生成依据：`801/cleantext/003-A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`003-A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material.pdf`
- 页数：7
- clean body 字符数：28620
- 摘要字符数：1102
- 参考文献条数：36
- 图题数：11
- 表题数：1
- 表格文件数：2
- 公式候选数：50
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[]

## 1. 身份层

- 标题：A mesomechanical model for predicting the degradation in stiffness of FRP composites subjected to combined thermal and mechanical loading
- 年份：2016
- 期刊/来源：Material
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material. Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formu- lation of the mathematical model.
- 主要证据：图表 12 个标题、公式 50 个候选、参考文献 36 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. The thermal softening, thermal decomposition of the matrix material”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Validation of the model was performed on glass fiber-reinforced epoxy composites and the agreement between predicted and experimental results was reasonably good. Thus, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points. Actually, when FRP composites are exposed to high temperatures, pyrolysis reaction o In order to determine temperature-dependent behavior of FRP composites under high temperatures, a three-zone annular furnace was installed on the universal testing machine (Instron 5500R, America), as shown in Fig.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
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
- 作者声明或文本中可见 gap：However, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6]. Although the temperature inside the chamber may in fact was not uniform as the temperature of the upper portion was higher than that of the lower portion, we assume that temperature near the specimen is uniform because the specimen size is small enough compared to the overall length of the furnace [28]. Then, the laminated SiFRP material was immersed with phenolic resin until the weight of the material did not change.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material. Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formu- lation of the mathematical model.
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
| A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. | 摘要/引言/结论候选 | 图：Fig. 1. The equipment for high-temperature compression experiment: (a) Facility; (b) Three zone furnace; (c) Temperature control system. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material. | 摘要/引言/结论候选 | 图：Fig. 2. The physical models in mesomechanical scale of polymer matrix and silica fibers. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Validation of the model was performed on glass fiber-reinforced epoxy composites and the agreement between predicted and experimental results was reasonably good. | 摘要/引言/结论候选 | 图：Fig. 3. Variation of measured compressive modulus versus temperature. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Liang [16,17] developed a further thermo-mechanical model in which the degradation functions were basically the same as in the Dimitrienko model, and employed meso-mechanical methods to predict ablation and phase transition, and thermo-mechanical behavior of m | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Based on the Arrhenius equation, Bai and Keller [19] presented a model to determine the temperature-dependent E-modulus, G-modulus, and effective coefficient of thermal expansion of FRP composites during different temperature ranges. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=body_inline] 125~^{\circ}\mathrm{C} | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Thus, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=body_inline] 800~^{\circ}\mathrm{C} | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The equipment for high-temperature compression experiment: (a) Facility; (b) Three zone furnace; (c) Temperature control system. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 2. The physical models in mesomechanical scale of polymer matrix and silica fibers. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Variation of measured compressive modulus versus temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4. Variation of volume fraction for each phase media in phenolic resin versus temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 5. Variation of volume fraction for each phase media in silica fiber versus temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. Change in elastic modulus of phase component materials versus temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 7. Change in elastic modulus of silica/phenolic composites versus temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. The fracture morphologies of silica/phenolic composite specimen after high- temperature compression experiment. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Schematic of a FRP composite specimen under combined one-sided heating and compression loading. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 10. Change in residual stiffness of silica/phenolic composite versus heating time when exposed to one-sided heat flux. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. The fracture morphologies of silica/phenolic composite specimen after hightemperature compression experiment. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=body_inline] 125~^{\circ}\mathrm{C} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] 800~^{\circ}\mathrm{C} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] 20-135~^{\circ}\mathrm{C} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] 350-650~^{\circ}\mathrm{C} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] E ( T ) = \frac {E _ {\mathrm{f}} + E _ {\mathrm{g}}} {2} - \frac {E _ {\mathrm{r}} - E _ {\mathrm{g}} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] E _ {\mathrm{r}} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] E _ {\mathrm{g}} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] T _ {\mathrm{g}} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The mechanical properties of Fiber Reinforced Polymer (FRP) composites decrease with increasing thermal exposure temperature and time. A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material. Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formu- lation of the mathematical model. High temperature compression experiments were conducted to measure the temperature-dependent elastic modulus. The accuracy of the model was further assessed by comparing simulat- ed and experimental modulus. The reduction in stiffness properties of FRP composites at high temperatures can be roughly divided into three stages by analyzing the predicted temperature-modulus curve. © 2015 Elsevier Ltd. All rights reserved.

### 7.4 摘要中文翻译

> 纤维增强聚合物 (FRP) 复合材料的机械性能随着热暴露温度和时间的增加而降低。提出了细观力学模型来预测高温下承受静态压缩载荷的 FRP 复合材料的退化行为。所开发的模型考虑了基体材料的热软化、热分解和增强纤维的相变​​，这些对复合材料的刚度性能产生不利影响。此外，为了评估高内压对刚度性能的影响，在数学模型的公式中应用了体积模量。进行高温压缩实验来测量与温度相关的弹性模量。通过比较模拟模量和实验模量进一步评估模型的准确性。通过分析预测的温度-模量曲线，FRP复合材料在高温下刚度性能的降低可大致分为三个阶段。 © 2015 爱思唯尔有限公司

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> The mathematical formulas for the mesomechanical model were established to predict the degraded stiffness properties at high temperatures. Thermal softening, viscoelastic creep and thermal decomposition of matrix material can cause the reduction to the mechanical properties of FRP composites under high temperatures. These effects were considered in the proposed model. Comparing the numerical and experimental results of elastic modulus, the proposed model can satisfactorily predict the temperature-dependent effective properties of FRP composites. When temperatures are around the glass transition temperature of the polymer matrix, the loss in stiffness properties of FRP composites is largely dependent on the thermal softening effect. The elastic modulus of the material rapidly degrades at $65-180~^{\circ}\mathrm{C}$ . At higher temperatures, the degradation in stiffness properties of the composite material occurs due to the thermal decomposition of polymer matrix and phase transition of reinforced fibers. The elastic modulus of FRP composites decreases drastically again at $500-1000~^{\circ}\mathrm{C}$

### 7.6 结论中文翻译

> 建立了细观力学模型的数学公式来预测高温下刚度性能的退化。高温下基体材料的热软化、粘弹性蠕变和热分解会导致FRP复合材料力学性能下降。所提出的模型中考虑了这些影响。比较弹性模量的数值结果和实验结果，所提出的模型可以令人满意地预测FRP复合材料随温度变化的有效性能。当温度在聚合物基体的玻璃化转变温度附近时，FRP 复合材料的刚度性能损失很大程度上取决于热软化效应。材料的弹性模量在 $65-180~^{\circ}\mathrm{C}$ 迅速下降。在较高温度下，由于聚合物基体的热分解和增强纤维的相变​​，复合材料的刚度性能会发生下降。 FRP复合材料的弹性模量在$500-1000再次大幅下降~^{\circ}\mathrm{C}$

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 4439 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Experimental procedure | 实验或测量设定 | 4689 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 3 | 3. Mesomechanical model for predicting the degraded stiffness properties | 方法建构 | 2138 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.2.1. Stiffness properties of matrix materials and reinforced fibers | 对象/条件/子问题展开 | 7219 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.2.2. Stiffness properties of FRP composites | 对象/条件/子问题展开 | 698 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 4.1. Stiffness degradation of matrix, fiber and silica/phenolic composites | 对象/条件/子问题展开 | 5324 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.2. Fracture morphology analysis | 结果验证/讨论 | 507 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 8 | 4.3. Compression modeling of silica/phenolic composite exposed to one-sided heating | 方法建构 | 1968 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 5. Conclusions | 主张回收/边界说明 | 1117 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(77)；theta(63)；temperature(57)；phase(56)；material(39)；properties(38)；modulus(36)；composites(29)；thermal(27)；frp(26)；stiffness(25)；temperatures(24)；transition(22)；silica(22)；virg(21)；composite(20)；elastic(20)；matrix(19)；phenolic(19)；volume(19)
- 高频学术名词/术语：temperature(57)；stiffness(25)；transition(22)；compression(17)；decomposition(14)；pressure(14)；inclusion(10)；degradation(9)；reaction(9)；ablation(6)；direction(6)；experiment(5)；elasticity(5)；fraction(5)；high-temperature(3)
- 高频学术动词：obtained(6)；predict(5)；presented(3)；predicted(2)；developed(2)；introduced(2)；compared(2)；investigate(2)；obtain(2)；evaluated(1)；validate(1)；estimated(1)；revealed(1)
- 高频形容词：material(39)；thermal(27)；elastic(20)；phenolic(19)；effective(13)；compressive(9)；internal(9)；residual(9)；experimental(8)；temperature-dependent(8)；mechanical(7)；constant(7)；mesomechanical(6)；component(6)；experiment(5)
- 高频副词：respectively(6)；drastically(4)；sufficiently(3)；additionally(3)；significantly(2)；relatively(2)；early(2)；similarly(2)；accordingly(2)；practically(2)；rapidly(2)；reasonably(1)
- 高频二词短语：frp composites(21)；mathrm virg(20)；theta mathrm(17)；theta theta(17)；elastic modulus(16)；circ mathrm(15)；stiffness properties(14)；gas phase(11)；high temperatures(10)；properties frp(10)；glass transition(10)；silica phenolic(10)；solid phase(10)；transition temperature(9)；phase transition(9)
- 高频三词短语：properties frp composites(9)；glass transition temperature(9)；left mathrm virg(6)；degraded stiffness properties(5)；silica phenolic composites(5)；phase gas phase(5)；mathrm virg mathrm(5)；tilde theta theta(5)；theta theta mathrm(5)；silica phenolic composite(5)；stiffness properties frp(4)；char phase gas(4)
- 被动语态估计：98
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：78
- 一般过去时线索：258
- 现在完成时线索：0
- 情态动词线索：38

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Therefore, it is necessary to study the degraded stiffness and strength properties of FRP composites, which is significant for further structure design, evaluation of integrity and reliability of thermal protection structures with this kind of composites.
  - 可迁移句型：{object}, it is necessary to study the degraded stiffness and strength properties of FRP composites, which is significant for further structure design, evaluation of integrity and reliability of thermal protection structures with this kind of composites.
### gap/转折句
- 原句：However, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6].
  - 可迁移句型：{object}, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6].
### 方法提出句
- 原句：A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures.
  - 可迁移句型：{object} mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures.
- 原句：The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material.
  - 可迁移句型：{object} thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material.
- 原句：Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formu- lation of the mathematical model.
  - 可迁移句型：{object}, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formu- lation of the mathematical model.
- 原句：The accuracy of the model was further assessed by comparing simulat- ed and experimental modulus.
  - 可迁移句型：{object} accuracy of the model was further assessed by comparing simulat- ed and experimental modulus.
### 结果证明句
- 原句：Validation of the model was performed on glass fiber-reinforced epoxy composites and the agreement between predicted and experimental results was reasonably good.
  - 可迁移句型：{object} of the model was performed on glass fiber-reinforced epoxy composites and the agreement between predicted and experimental results was reasonably good.
- 原句：Thus, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points.
  - 可迁移句型：{object}, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points.
- 原句：Actually, when FRP composites are exposed to high temperatures, pyrolysis reaction o In order to determine temperature-dependent behavior of FRP composites under high temperatures, a three-zone annular furnace was installed on the universal testing machine (Instron 5500R, America), as shown in Fig.
  - 可迁移句型：{object}, when FRP composites are exposed to high temperatures, pyrolysis reaction o In order to determine temperature-dependent behavior of FRP composites under high temperatures, a three-zone annular furnace was installed on the universal testing machine (In
- 原句：Three thermocouples were placed in the topmiddle-bottom of the annular furnace, thus, air temperatures of three zones in the furnace could be controlled separately by temperature control systems, as shown in Fig.
  - 可迁移句型：{object} thermocouples were placed in the topmiddle-bottom of the annular furnace, thus, air temperatures of three zones in the furnace could be controlled separately by temperature control systems, as shown in Fig.
### 贡献收束句
- 原句：A silica fiber-reinforced phenolic resin composite, kindly provided by Aerospace Research Institute of Materials and Processing Technology (Beijing, China), was selected and characterized in this study.
  - 可迁移句型：{object} silica fiber-reinforced phenolic resin composite, kindly provided by Aerospace Research Institute of Materials and Processing Technology (Beijing, China), was selected and characterized in This study.
### 边界/谨慎句
- 原句：The conclusions could be summarized from the reported literatures as follows: in the lower temperature range, thermal softening and viscoelastic creep can cause the reduction in the mechanical properties of FRP composite, while, when the temperature reaches and exceeds the glass transition temperature, the elastic modulus and strength drops significantly increase [9–12].
  - 可迁移句型：{object} conclusions could be summarized from the reported literatures as follows: in the lower temperature range, thermal softening and viscoelastic creep can cause the reduction in the mechanical properties of FRP composite, while, when the temperature reach
- 原句：Three thermocouples were placed in the topmiddle-bottom of the annular furnace, thus, air temperatures of three zones in the furnace could be controlled separately by temperature control systems, as shown in Fig.
  - 可迁移句型：{object} thermocouples were placed in the topmiddle-bottom of the annular furnace, thus, air temperatures of three zones in the furnace could be controlled separately by temperature control systems, as shown in Fig.
- 原句：The specimen temperature was measured by thermocouple 2 which could be placed at the specimen surface.
  - 可迁移句型：{object} specimen temperature was measured by thermocouple 2 which could be placed at the specimen surface.
- 原句：Although the temperature inside the chamber may in fact was not uniform as the temperature of the upper portion was higher than that of the lower portion, we assume that temperature near the specimen is uniform because the specimen size is small enough compared to the overall length of the furnace [28].
  - 可迁移句型：{object} the temperature inside the chamber may in fact was not uniform as the temperature of the upper portion was higher than that of the lower portion, we assume that temperature near the specimen is uniform because the specimen size is small enough compare

## 9. 引用风险层

- 正文引用簇估计：28
- 参考文献条数：36
- 可识别年份条目数：36
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：19
- 高频来源粗略识别：Compos. Mater(6)；Part A(6)；Sci. Technol(4)；Part B(2)；Mech. Sci. Technol(1)；Compos. Sin(1)；Sinica(1)；Technol(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] L. Bian, J. Xiao, J. Zeng, et al., Microstructural interpretation of the ablative properties of phenolic-quartz hybrid fabric reinforced phenolic resin composites, Mater. Des. 62 (2014) 424–429.
- [2] N. Guermazi, N. Haddar, K. Elleuch, H.F. Ayedi, Investigations on the fabrication and the characterization of glass/epoxy, carbon/epoxy and hybrid composites used in the reinforcement and the repair of aeronautic structures, Mater. Des. 56 (2014) 714–724.
- [3] P.R.S. Reddy, T.S. Reddy, V. Madhu, et al., Behavior of E-glass composite laminates under ballistic impact, Mater. Des. 84 (2015) 79–86.
- [4] P. Luangtriratana, B.K. Kandola, P. Myler, Ceramic particulate thermal barrier surface coatings for glass fibre-reinforced epoxy composites, Mater. Des. 68 (2015) 232–244.
- [5] E. Kandare, B.K. Kandola, P. Myler, G. Edwards, Thermo-mechanical responses of fiber-reinforced epoxy composites exposed to high temperature environments. Part I: experimental data acquisition, J. Compos. Mater. 44 (2010) 3093–3114.
- [6] A.M. Coppola, A.S. Griffin, N.R. Sottos, S.R. White, Retention of mechanical performance of polymer matrix composites above the glass transition temperature by vascular cooling, Compos. Part A 78 (2015) 412–423.
- [7] K. Wei, R. He, X. Cheng, et al., A lightweight, high compression strength ultra high temperature ceramic corrugated panel with potential for thermal protection system applications, Mater. Des. 66 (2015) 552–556.
- [8] B. Yu, V. Kodur, Effect of temperature on strength and stiffness properties of near- surface mounted FRP reinforcement, Compos. Part B 58 (2014) 510–517.
- [9] Y. Matsuura, K. Hirai, T. Kamita, et al., A challenge of modeling thermo-mechanical response of silica-phenolic composites under high heating rates, 49th AIAA Aerospace Sciences Meeting, Orland, Florida, 2011.
- [10] S.J. Kim, S.Y. Han, E.S. Shin, Micromechanics-based evaluation of the poroelastic effect and stress concentration in thermochemically-decomposed composites, J. Mech. Sci. Technol. 27 (2013) 3139–3147.
- [11] A.G. Gibson, Y.S. Wu, J.T. Evans, A.P. Mouritz, Laminate theory analysis of composites under load in fire, J. Compos. Mater. 40 (2006) 639–658.
- [12] M. Tsoi, J. Zhuge, R.H. Chen, J. Gou, Modeling and experimental studies of thermal degradation of glass fiber reinforced polymer composites, Fire Mater. 38 (2014) 247–263.
- [13] Y.I. Dimitrienko, Thermomechanical behaviour of composite materials and struc- tures under high temperatures: 1. Materials, Compos. Part A 28 (1997) 453–461.
- [14] Y.I. Dimitrienko, A structural thermo-mechanical model of textile composite materials at high temperatures, Compos. Sci. Technol. 59 (1999) 1041–1053.
- [15] Y.I. Dimitrienko, Thermomechanics of Composites Under High Temperatures, Kluwer Academic Publishers, London, 1999 73–108.

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
