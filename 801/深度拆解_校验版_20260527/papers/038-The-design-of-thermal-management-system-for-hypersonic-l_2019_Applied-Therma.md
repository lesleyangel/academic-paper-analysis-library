# 论文深度拆解：The design of thermal management system for hypersonic launch vehicles based on active cooling networks

> 生成依据：`801/cleantext/038-The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`038-The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.pdf`
- 页数：14
- clean body 字符数：53363
- 摘要字符数：1348
- 参考文献条数：45
- 图题数：17
- 表题数：1
- 表格文件数：6
- 公式候选数：162
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "5 formula(s) need manual review."}]

## 1. 身份层

- 标题：The design of thermal management system for hypersonic launch vehicles based on active cooling networks
- 年份：2019
- 期刊/来源：Applied Therma
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：工程应用 + 多物理场分析型
- 研究对象：The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS). The design key for such a TPS is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulation layer).
- 主要方法：In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design. The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coef- ficient.
- 主要证据：图表 18 个标题、公式 162 个候选、参考文献 45 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management syste”，可以通过“In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, dete”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions. The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling. The thermal equilibrium equation at surface of TPS is shown in Eq.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS). The design key for such a TPS is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulation layer).
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
- 作者声明或文本中可见 gap：For TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission. The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area. However, for a flight vehicle, $q _ {i n}$ and hl should vary with aeroheating level $( \mathrm{i} . \mathrm{e} . , T _ {w} )$ at different regions, thus they are inappropriate to be selected as design parameters directly.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS).
- For TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission.
- The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design. The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coef- ficient.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：工程应用 + 多物理场分析型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：工程应用 + 多物理场分析型
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
| In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. | 摘要/引言/结论候选 | 图：Fig. 1. The vehicle and trajectory. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions. | 摘要/引言/结论候选 | 图：Fig. 2. Thermal equilibrium model. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design. | 摘要/引言/结论候选 | 图：Fig. 3. Connection pattern of cooling channels. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer c | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 678.48, 219.68, 702.97)]] ⁎ Corresponding author | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this work, the TPS concepts are mainly those developed in Space Shuttle engineering by NASA [4], which consists of three types, i.e., flexible ceramic blankets (e.g., tailorable advanced blanket insulation, TABI), rigid ceramic tiles (e.g., alumina enhanced | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 3, bbox (306.36, 406.54, 557.68, 419.57)]] = q h T T ( ) in l b c (2) | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The vehicle and trajectory. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 2. Thermal equilibrium model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Connection pattern of cooling channels. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Process of TMS design. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. One-dimensional heat transfer analysis model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. The maximum temperature on the windward and leeward median lines. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. The highest wall temperature. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. The transient wall temperature along the trajectory. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. The transient aerodynamic heat flux along the trajectory. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 10. The heat, heat flux and local heat transfer coefficient of active cooling. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The aerodynamic heat and active cooled heat on median lines. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. The partition of the vehicle surface. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. The distribution of TPS concept. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. The assumed active cooling system. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Capacity of active cooling network. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 678.48, 219.68, 702.97)]] ⁎ Corresponding author. E-mail address: le | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.36, 406.54, 557.68, 419.57)]] = q h T T ( ) in l b c (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.36, 584.21, 557.68, 597.24)]] = q h T T ( ) in eq w c (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.36, 249.95, 557.68, 263.1)]] = = + q T T T q ( ) aero r w W in 4 (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.35, 55.38, 288.67, 68.41)]] = q A m c T · · · in f (5) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (100.83, 298.29, 146.2, 309.96)]] = x x | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (110.31, 298.29, 116.05, 307.62)]] = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (85.95, 310.77, 128.05, 331.14)]] < = < | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. The system consists of a passive thermal protection system (TPS) and an active cooling network (ACN) with coolant of kerosene. In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions. A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design. The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coef- ficient. The model and the coefficient act as the rationale and the equivalent parameter of the whole process, respectively. The TMS of a reusable launch vehicle is established under a typical trajectory. The influences of equivalent heat transfer coefficient on aerodynamic heating, passive TPS and ACN are studied. The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.

### 7.4 摘要中文翻译

> 本文提出了一种高超声速飞行器热管理系统（TMS）的设计方法。该系统由被动热保护系统（TPS）和采用煤油冷却剂的主动冷却网络（ACN）组成。在以往的大多数研究中，被动式TPS和ACN总是分开设计，从而导致结果过于保守，偏离实际工程条件。目前的工作提出了一种耦合设计方法，该方法包括气动热计算、被动TPS概念分布的确定、TPS和ACN尺度的计算以及迭代设计。耦合设计基于两个关键实现，主动冷却通过等效热平衡模型耦合到TPS中的气动加热和传热，主动冷却的总体能力由等效传热系数表示。模型和系数分别作为整个过程的理论依据和等效参数。可重复使用运载火箭的TMS是在典型轨迹下建立的。研究了等效传热系数对气动加热、被动TPS和ACN的影响。结果表明，随着主动冷却的增强，被动TPS的重量减少，而冷却剂质量流量增加。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this paper, a design method of thermal management system (TMS) for reusable flight vehicles is developed. The system consists of a passive thermal protection system (TPS) and an active cooling network (ACN) with kerosene as coolant. Based on an equivalent heat equilibrium model, the TPS and ACN are designed in a coupled way. A parameter equivalent HTC, $h _ {e q} ,$ is proposed to indicate the capacity of active cooling. The design process includes four steps, the calculation of aerodynamic heat, the determination of TPS concept distribution, the calculation of scales of TPS and ACN, and the final design of TMS after several iterations. A reusable launch vehicle of 30 m long with a certain trajectory is studied in this work. The influence of equivalent HTC $( h _ {e q} = 0-30 \mathrm{W} / ( \mathrm{m} ^ {2} \mathrm{K} ) )$ and cold side temperature $( T _ {b} = 330 , 367$ and 440 K) on aerodynamic heat, TPS and ACN are studied. The results show some useful conclusions:
> 
> (1) The aerodynamic heat flux and the proportion of heat taken by ACN increase, while the wall temperature decreases with the rise of equivalent HTC.
> 
> (2) The higher equivalent HTC will result in lighter TPS while higher product of coolant mass flow rate and coolant temperature rise for ACN.
> 
> (3) Increasing the constrained cold side temperature is very useful for the weight reduction of passive TPS, and it is more efficient with small equivalent HTC. The weight of TPS is reduced by 30.1%, 16.9%, 8.5%, 7.3%, 0.9%, 0% and 0% with $T _ {b}$ increasing from 330 to 440 K, for $h _ {e q} = 0 , \ 0.1 , \ 1$ , 2, 5, 10, 20, and $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ , respectively.
> 
> (4) The ACN can reduce the TPS weight, and it is more efficient with low cold side temperature. The weight of passive TPS is reduced by 40.0% and 14.1% with the equivalent HTC increases from 0 to $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ for $T _ {b} = 330$ and $T _ {b} = 440 \mathrm{;}$ , respectively.
> 
> (5) The method proposed in this work can be used to design ACN for the whole vehicle, as well as specific regions like the head of fuselage. For ACN of the vehicle head, the required mass flow rate decreases from 9.4 to 0.188 kg/s, 93.4 to 1.87 kg/s, 187 to 3.73 kg/ s, 462 to 9.25 kg/s, 910 to 18.2 kg/s, 1765 to 35.3 kg/s and 2565 to 51.3 kg/s, when the coolant temperature rise increases from 1 to 50 K for $h _ {e q} = 0.1$ , 1, 2, 5, 10, 20 and $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ respectively. However, for the whole vehicle, the mass flow rate will decrease from 30.6 to 0.612 kg/s, 305 to 6.12 kg/s, 608 to 12.15 kg/s, 1499 to 30.0 kg/s, 2926 to 58.5 kg/s, 5560 to 111 kg/s and 7945 to 159 kg/s, when the coolant temperature rise increases from 1 to 50 K for $h _ {e q} = 0.1 , 1 , 2 , 5 , 10$ , 20 and $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$

### 7.6 结论中文翻译

> 本文提出了一种可重复使用飞行器热管理系统（TMS）的设计方法。该系统由被动热保护系统（TPS）和以煤油为冷却剂的主动冷却网络（ACN）组成。基于等效热平衡模型，TPS和ACN采用耦合方式设计。提出了等效 HTC 参数 $h _ {e q} ,$ 来指示主动冷却的能力。设计过程包括气动热计算、TPS概念分布确定、TPS和ACN尺度计算以及经过多次迭代后TMS的最终设计四个步骤。本文研究了一种长30 m、具有一定弹道的可重复使用运载火箭。研究了等效HTC $( h _ {e q} = 0-30 \mathrm{W} / ( \mathrm{m} ^ {2} \mathrm{K} ) )$和冷端温度$( T _ {b} = 330 , 367$和440 K)对气动热、TPS和ACN的影响。结果表明：(1)随着等效热传递系数的升高，气动热通量和ACN吸热比例增大，而壁温降低。 (2) 当量 HTC 越高，TPS 越轻，而 ACN 的冷却液质量流量和冷却液温升乘积越高。 (3)提高约束冷侧温度对于被动式TPS的减重非常有用，并且当量HTC较小时效率更高。随着 $T _ {b}$ 从 330 增加到 440 K，TPS 的权重减少了 30.1%、16.9%、8.5%、7.3%、0.9%、0% 和 0%，其中 $h _ {e q} = 0 、\ 0.1 、\ 1$ 、2、5、10、20 和 $30分别为 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ 。 (4) ACN可减轻TPS重量，冷侧温度低，效率更高。
> 
> 被动 TPS 的权重减少了 40.0% 和 14.1%，等效 HTC 从 0 增加到 $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$，分别为 $T _ {b} = 330$ 和 $T _ {b} = 440 \mathrm{;}$ 。 (5)本文提出的方法可用于整车以及机身头部等特定区域的ACN设计。对于车头ACN，所需质量流量从9.4降至0.188 kg/s、93.4降至1.87 kg/s、187降至3.73 kg/s、462降至9.25 kg/s、910降至18.2 kg/s、1765降至35.3 kg/s和2565降至51.3 kg/s，当冷却液温升从 1 增加到 50 K 时，分别为 $h _ {e q} = 0.1$ 、 1、2、5、10、20 和 $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$。但对于整车来说，质量流量将从30.6降至0.612 kg/s、305降至6.12 kg/s、608降至12.15 kg/s、1499降至30.0 kg/s、2926降至58.5 kg/s、5560降至111 kg/s和7945降至159 kg/s，当冷却液温升从 1 增加到 50 K 时 $h _ {e q} = 0.1 , 1 , 2 , 5 , 10$ , 20 和 $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6419 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. The vehicle and its trajectory | 对象/条件/子问题展开 | 2398 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3.1. Equivalent thermal equilibrium model and HTC | 方法建构 | 6213 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.2. Calculation of aerodynamic heat | 对象/条件/子问题展开 | 3403 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.3. Process of TMS design | 对象/条件/子问题展开 | 3904 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.4. TPS concept database | 对象/条件/子问题展开 | 2479 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.1. Thermal conditions | 对象/条件/子问题展开 | 8148 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.2. Heat transferred by active cooling | 对象/条件/子问题展开 | 4702 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 4.3. Passive TPS | 对象/条件/子问题展开 | 4462 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.4. Active cooling network | 对象/条件/子问题展开 | 6120 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.5. Influence of equivalent HTC | 对象/条件/子问题展开 | 1731 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 5. Conclusions | 主张回收/边界说明 | 2903 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(125)；temperature(103)；tps(98)；heat(85)；fig(68)；cooling(57)；acn(57)；vehicle(56)；aerodynamic(47)；respectively(45)；coolant(44)；work(39)；design(38)；active(37)；flow(36)；passive(33)；equivalent(33)；htc(32)；rate(28)；weight(27)
- 高频学术名词/术语：temperature(103)；capacity(20)；distribution(16)；influence(12)；calculation(12)；addition(9)；insulation(7)；condition(7)；protection(6)；high-temperature(6)；convection(6)；propulsion(6)；configuration(6)；structure(5)；thickness(5)
- 高频学术动词：obtained(15)；developed(10)；indicate(8)；obtain(4)；indicated(4)；evaluated(3)；develop(1)；optimized(1)；compared(1)；reveal(1)
- 高频形容词：aerodynamic(47)；coolant(44)；active(37)；passive(33)；equivalent(33)；thermal(23)；specific(14)；boundary(14)；table(10)；regenerative(8)；allowable(7)；final(7)；real(7)；vertical(7)；efficient(6)
- 高频副词：respectively(45)；finally(8)；mainly(4)；especially(3)；widely(2)；directly(2)；similarly(2)；closely(2)；averagely(2)；obviously(1)；purely(1)；firstly(1)
- 高频二词短语：mathrm mathrm(60)；aerodynamic heat(32)；active cooling(30)；passive tps(30)；flow rate(28)；equivalent htc(26)；mass flow(24)；heat flux(20)；wall temperature(18)；whole vehicle(16)；temperature rise(16)；mathrm respectively(15)；leading edge(13)；aerodynamic heating(12)；tps acn(12)
- 高频三词短语：mass flow rate(24)；mathrm mathrm mathrm(23)；mathrm mathrm respectively(11)；cold side temperature(10)；aerodynamic heat flux(9)；mathrm cdot mathrm(9)；coolant mass flow(8)；flow rate temperature(8)；rate temperature rise(8)；passive tps acn(7)；mathrm mathrm cdot(7)；average maximum rising(6)
- 被动语态估计：152
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：284
- 一般过去时线索：342
- 现在完成时线索：0
- 情态动词线索：100

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area.
  - 可迁移句型：{object} heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat f
### gap/转折句
- 原句：The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS).
  - 可迁移句型：{object} high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS).
- 原句：For TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission.
  - 可迁移句型：{object} TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however,
- 原句：The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area.
  - 可迁移句型：{object} heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat f
- 原句：However, for a flight vehicle, $q _ {i n}$ and hl should vary with aeroheating level $( \mathrm{i} . \mathrm{e} . , T _ {w} )$ at different regions, thus they are inappropriate to be selected as design parameters directly.
  - 可迁移句型：{object}, for a flight vehicle, $q _ {i n}$ and hl should vary with aeroheating level $( \mathrm{i} . \mathrm{e} . , T _ {w} )$ at different regions, thus they are inappropriate to be selected as design parameters directly.
### 方法提出句
- 原句：In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed.
  - 可迁移句型：{object} This study, a design method of thermal management system (TMS) for hypersonic vehicles is developed.
- 原句：A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design.
  - 可迁移句型：{object} coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design.
- 原句：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coef- ficient.
  - 可迁移句型：{object} coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat trans
- 原句：The model and the coefficient act as the rationale and the equivalent parameter of the whole process, respectively.
  - 可迁移句型：{object} model and the coefficient act as the rationale and the equivalent parameter of the whole process, respectively.
### 结果证明句
- 原句：In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
  - 可迁移句型：{object} most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
- 原句：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coef- ficient.
  - 可迁移句型：{object} coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat trans
- 原句：The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
  - 可迁移句型：{object} results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
- 原句：The thermal equilibrium equation at surface of TPS is shown in Eq.
  - 可迁移句型：{object} thermal equilibrium equation at surface of TPS is shown in Eq.
### 贡献收束句
- 原句：The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
  - 可迁移句型：{object} results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
- 原句：In this work, the TPS concepts are mainly those developed in Space Shuttle engineering by NASA [4], which consists of three types, i.e., flexible ceramic blankets (e.g., tailorable advanced blanket insulation, TABI), rigid ceramic tiles (e.g., alumina enhanced thermal barrier, AETB) and metallic panels (e.g., superalloy honeycomb sandwich panels, SA-HC).
  - 可迁移句型：{object} This study, the TPS concepts are mainly those developed in Space Shuttle engineering by NASA [4], which consists of three types, i.e., flexible ceramic blankets (e.g., tailorable advanced blanket insulation, TABI), rigid ceramic tiles (e.g., alumina e
- 原句：The weight of TPS is reduced by 30.1%, 16.9%, 8.5%, 7.3%, 0.9%, 0% and 0% with $T _ {b}$ increasing from 330 to 440 K, for $h _ {e q} = 0 , \ 0.1 , \ 1$ , 2, 5, 10, 20, and $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ , respectively.
  - 可迁移句型：{object} weight of TPS is reduced by 30.1%, 16.9%, 8.5%, 7.3%, 0.9%, 0% and 0% with $T _ {b}$ increasing from 330 to 440 K, for $h _ {e q} = 0 , \ 0.1 , \ 1$ , 2, 5, 10, 20, and $30 \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ , respectively.
- 原句：(4) The ACN can reduce the TPS weight, and it is more efficient with low cold side temperature.
  - 可迁移句型：(4) {object} ACN can reduce the TPS weight, and it is more efficient with low cold side temperature.
### 边界/谨慎句
- 原句：The well designed TMS should be able to manage the transfer process, and control the dissipation and even the reuse of aerodynamic heat in an efficient way.
  - 可迁移句型：{object} well designed TMS should be able to manage the transfer process, and control the dissipation and even the reuse of aerodynamic heat in an efficient way.
- 原句：The design key for such a TPS is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulation layer).
  - 可迁移句型：{object} design key for such a TPS is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulatio
- 原句：Sometimes, especially for hypersonic vehicles, the size and the weight of such a purely passive TPS could be unacceptable.
  - 可迁移句型：{object}, especially for hypersonic vehicles, the size and the weight of such a purely passive TPS could be unacceptable.
- 原句：The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area.
  - 可迁移句型：{object} heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat f

## 9. 引用风险层

- 正文引用簇估计：31
- 参考文献条数：45
- 可识别年份条目数：49
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：15
- 高频来源粗略识别：Therm. Eng(12)；Sci. Technol(9)；The system consists of a passive thermal protection system(1)；J. Heat Mass Transf(1)；Appl. Mech(1)；J. Hydrogen Energy(1)；Flame(1)；Eng. Gas Turbines Power(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re- usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [2] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [3] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [4] D.E. Myers, C.J. Martin, M.L. Blosser, Parametric Weight Comparison of Advanced Metallic, Ceramic Tile, and Ceramic Blanket Thermal Protection Systems, NASA Langley Technical Report Server, 2000.
- 5. Conclusions In this paper, a design method of thermal management system (TMS) for reusable flight vehicles is developed. The system consists of a passive thermal protection system (TPS) and an active cooling network (ACN) with kerosene as coolant. Based on an equivalent heat equili- brium model, the TPS and ACN are designed in a coupled way. A parameter equivalent HTC, heq, is proposed to indicate the capacity of active cooling. The design process includes four steps, the calculation of aerod
- [5] A. Riccio, F. Raimondo, A. Sellitto, V. Carandente, R. Scigliano, D. Tescione, Optimum design of ablative thermal protection systems for atmospheric entry ve- hicles, Appl. Therm. Eng. 119 (2017) 541–552.
- [6] M. Rivier, J. Lachaud, P.M. Congedo, Ablative thermal protection system under uncertainties including pyrolysis gas composition, Aerosp. Sci. Technol. 84 (2019) 1059–1069.
- [7] N. Blet, S. Lips, V. Sartre, Heats pipes for temperature homogenization: A literature review, Appl. Therm. Eng. 118 (2017) 490–509.
- [8] L. Shen, J. Wang, Numerical investigation on the optimization of local transpiration cooling effectiveness, Appl. Therm. Eng. 127 (2017) 58–69.
- [9] P. Jiang, Z. Liao, Z. Huang, Y. Xiong, Y. Zhu, Influence of shock waves on supersonic transpiration cooling, Int. J. Heat Mass Transf. 129 (2019) 965–974.
- [10] R. Ding, J. Wang, F. He, G. Dong, L. Tang, Numerical investigation on the perfor- mances of porous matrix with transpiration and film cooling, Appl. Therm. Eng. 146 (2019) 422–431.
- [11] M. Cui, J. Mei, B.-W. Zhang, B.-B. Xu, L. Zhou, Y. Zhang, Inverse identification of boundary conditions in a scramjet combustor with a regenerative cooling system, Appl. Therm. Eng. 134 (2018) 555–563.
- [12] T. Jing, G. He, W. Li, F. Qin, X. Wei, Y. Liu, Z. Hou, Flow and thermal analyses of regenerative cooling in non-uniform channels for combustion chamber, Appl. Therm. Eng. 119 (2017) 89–97.
- [13] R. Savino, M. De Stefano Fumo, D. Paterna, M. Serpico, Aerothermodynamic study Hypersonic Systems and Technologies Conference, AIAA-2015-3606, 2015.
- [14] S. Liu, B. Zhang, Effects of active cooling on the metal thermal protection systems, Aerosp. Sci. Technol. 15 (7) (2011) 526–533.

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
