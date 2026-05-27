# 论文深度拆解：040-The-heat-dissipation-transport-and-reuse-management-for-_2021_Aerospace-Sci

> 生成依据：`801/cleantext/040-The-heat-dissipation-transport-and-reuse-management-for-_2021_Aerospace-Sci`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`040-The-heat-dissipation-transport-and-reuse-management-for-_2021_Aerospace-Sci`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.pdf`
- 页数：22
- clean body 字符数：84112
- 摘要字符数：1752
- 参考文献条数：58
- 图题数：18
- 表题数：8
- 表格文件数：10
- 公式候选数：272
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "28 formula(s) need manual review."}]

## 1. 身份层

- 标题：040-The-heat-dissipation-transport-and-reuse-management-for-_2021_Aerospace-Sci
- 年份：2021
- 期刊/来源：Aerospace Sci
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：工程应用 + 多物理场分析型
- 研究对象：In this work, a unified surface emissivity is needed in the calculation and it is assumed to be 0.8 according to the above references.
- 主要方法：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems. For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and 
- 主要证据：图表 26 个标题、公式 272 个候选、参考文献 58 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“In this work, a unified surface emissivity is needed in the calculation and it is assumed to be 0.8 according to the above references.”，可以通过“An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence,”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient. In comparison with the space shuttle which is a rocket-launched vehicle, the thermal condition for these subsequent hypersonic vehicles is more severe for two reasons: 1st, the current space vehicles flight in atmosphere for a longer period, thus the accumulation of aerodynamic heat over time is enormous; 2nd, for the current space vehicles, the air-breathing or combined cycle engines are widely adopted, the aerodynamic performance is more concerned and slender configurations are preferred, and thus the reduced bluntness of the fuselage leads to more severe heating effect. The techniques of thermal protection system (TPS) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：In this work, a unified surface emissivity is needed in the calculation and it is assumed to be 0.8 according to the above references.
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
- 作者声明或文本中可见 gap：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path. It should be noted that $q _ {i n}$ will be finally taken away by active TM subsystems, i.e., transported or reused by RC networks and TE components, thus such amount of heat can be considered as a sort of “take-away” heat. However, in this work, the amount of take-away heat should not be neglected.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The heat pipe technique is widely used in high-temperature components like vehicle leading edges [15] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems. For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance. The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
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
| An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rat | 摘要/引言/结论候选 | 图：Fig. 1. The hypersonic vehicle: (a) the flight schematic and (b) the management system of aerodynamic heat. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numer | 摘要/引言/结论候选 | 图：Fig. 2. Surface subregions of the vehicle. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified. | 摘要/引言/结论候选 | 图：Fig. 3. The physical properties of the coolant: (a) Liquid hydrogen (b) JET-A 3638. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the retirement of Space Shuttle, several subsequent hypersonic and space vehicle programs are proposed, such as NASP and succedent Hyper-X of USA, Skylon of UK, LAPCAT of EU, Space-Liner of Germany. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The techniques of thermal protection system (TPS) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 205.3, 367.08, 218.96)]] Jian-Jun Gou, Zheng-Wei | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The hypersonic vehicle: (a) the flight schematic and (b) the management system of aerodynamic heat. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Surface subregions of the vehicle. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. The physical properties of the coolant: (a) Liquid hydrogen (b) JET-A 3638. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The CFD model of the coolant convection (AFRSI-RC network). | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. The TE-AFRSI concept, unit cell, geometric model and meshed model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. The wall temperature and aerodynamic heat. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 7. Temperature on leeward and windward median lines. (For interpretation of the colors in the figure(s), the reader is referred to the web version of this  | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Aerodynamic heat and take-away heat on leeward and windward median lines. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Passive TPS concept for each surface subregion. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Assumed RC network and coolant mass flow rate. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Scales of TPS and RC network along with the equivalent heat transfer coefficient. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Temperature fields of coolant convection. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. The verification of grid independence. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Temperature on TPS bottom lines. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Coolant temperature at the outlet. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 205.3, 367.08, 218.96)]] Jian-Jun Gou, Zheng-Wei Yan, Jia-Xin Hu, Ge | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (41.17, 696.06, 204.7, 715.22)]] * Corresponding author. E-mail address: leonwood@nwpu.edu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (306.63, 499.38, 557.7, 512.82)]] α (Tr -T w) = εσ T 4 w + qin (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (37.5, 555.64, 288.71, 566.64)]] qin = heq′(T w -Tc) = hl(Tb -Tc) (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (37.5, 739.08, 288.71, 749.95)]] qin = heqT w (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 6, bbox (37.5, 121.35, 288.71, 132.28)]] heqT w A = m f cp�Tc (4) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (37.5, 435.36, 288.71, 447.59)]] heqT w A = U 2R/(2R)2 (5) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 6, bbox (37.8, 508.75, 288.71, 527.0)]] U = \|Sn�Tn\| + ��S p�T p �� (6) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Cummings Russell
> The thermal energy management (TM) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse. In this paper, the aerodynamic heat of a hypersonic cruiser is dissipated by passive thermal protection system (TPS), transported by regenerative cooling (RC) network, and reused by RC network and thermoelectric (TE) conversion component. The TM system accordingly includes three subsystems of TPS, RC network and TE component. An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems. For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance. The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified. The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient.

### 7.4 摘要中文翻译

> Cummings Russell 通讯 高超声速飞行器的热能管理（TM）应关注散热、运输和再利用的全过程。本文提出高超声速巡洋舰的气动热通过被动热保护系统（TPS）消散，通过再生冷却（RC）网络传输，并由RC网络和热电（TE）转换组件重新利用。 TM系统相应地包括TPS、RC网络和TE组件三个子系统。建立了等效热平衡模型和整体等效传热系数，以建立气动加热和TM系统之间的相互关系，而不是单向影响，并解释TM子系统的耦合设计原理。对于被动TPS，得到相关概念的分布、面积和权重；针对RC网络，建立了热容量和冷却剂质量流量的确定方法，并以碳氢化合物和液氢燃料为冷却剂，对特定车辆区域的热传输性能进行了数值分析；对于TE组件，通过将中低温TE阶段集成到先进的柔性可重复使用表面绝缘体（AFRSI）中，建立了TE-AFRSI概念，并通过考虑热防护、重量增量和热再利用性能来优化该概念。最后提出了TM系统的设计路线并明确了整体等效传热系数的影响。结果表明，气动热和输送或再利用的热量比例会增加，而被动式TPS的规模会随着整体等效传热系数的增加而减小。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this paper, a TM system is designed for a hypersonic vehicle with length of 15 m and wingspan of about 6 m under a certain cruise trajectory. The system consists of passive TPS, RC network and TE component, and the aerodynamic heat is dissipated by the passive TPS, transported by the RC network, and reused by the RC network and the TE component. An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and TM system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of RC network and TE component, and the rationale of the design of such a TM system is stated. For passive TPS, the distribution, area and weight of relevant concepts are determined; for RC network, the distribution of heat capacity requirement for the whole vehicle is obtained, a CFD model for AFRSI-RC is established, the hydrocarbon and liquid hydrogen fuel are considered as coolants, and the minimum limitation of mass-flow-rate is determined; for TE component, a TE-AFRSI concept is introduced, the optimal concepts are obtained based on the optimization of different objectives. The influence of overall equivalent HTC $( h _ {e q} = 0$ to 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot \mathrm{K} ) )$ and cold side temperature $\left( T _ {b} \right. = \left. 300 \right$ , 367 and 440 K) on the aerodynamic heat and TM system are studied.
> 
> The results show some conclusions:
> 
> 1. With the increasing of $h _ {e q}$ the wall temperature decreases, while the aerodynamic heat increases; the heat amount proportion that transported and reused increases, while that dissipated decreases; the required capacity of RC network and TE component should be enhanced, while the scale of TPS can be reduced.
> 
> 2. The wall temperature at the leading edge decreases from 1690 to 1675 K, the lowest wall temperature on the median line of leeward surface decreases from 762 to 601 K, the maximum wall temperature at the third compression surface decreases from 1028 to 964 K when $h _ {e q}$ increases from 0 to 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot \mathrm{K} )$
> 
> 3. The TPS weight decreases with the increasing $T _ {b}$ and $h _ {e q} ,$ and increasing $h _ {e q}$ is more efficient when $T _ {b}$ is small and vice versa. However, although increasing $T _ {b}$ is a very efficient way, it is still limited by the material option and the internal environment requirement of the vehicle. The weight of TPS is reduced by 62.7%, 54.0%, 36.4%, 1.3%, 0.7%, 0%, 0% and 0% for $h _ {e q} = 0 , 0.1 , 1 , 2 , 5 ,$ , 10, 15 and 20 ${\sf W} / ( {\sf m} ^ {2} \cdot {\sf K} ) ,$ , respectively.
> 
> 4. For RC network, the coolant m f decreases and the trend slows down with the increasing coolant temperature rise. The required $m _ {f}$ of $\mathrm{LH} _ {2}$ is much smaller than JET-A due to the larger specific heat capacity of $\mathrm{LH} _ {2}$ , and indicates that LH2 has stronger cooling ability. For $\mathrm{LH} _ {2}$ , the channel size has very little influence on the cooling performance, while for JET-A, the smaller channel size results into better cooling performance.
> 
> 5. The RC network with JET-A of the second and third leeward surface parts, for cases of $h _ {e q} \ = \ 0.1 ,$ 1 and $2 \ \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ the required $m _ {f}$ is mainly limited by $T _ {b}$ and it should be larger than 0.23 kg/s for $T _ {b} ~ = ~ 440$ K and 2.27 kg/s for $T _ {b} ~ = ~ 300$ K; while for cases of $h _ {e q} = 5$ and $10 \ \mathsf{W} / ( \mathsf{m} ^ {2} {\cdot} \mathsf{K} ) , m _ {f}$ is mainly limited by the heat capacity of the RC network and it should be larger than 2.5 and 20.1 kg/s, respectively; for $h _ {e q} = 15$ and 20 ${\sf W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ , the RC coolant convection involved in this work is unable to meet the heat capacity requirment.
> 
> 6. The RC network with LH2 of the second and third leeward surface parts, for cases of $h _ {e q} \ = \ 0.1 ,$ , 1 and $2 \ \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ , the required $m _ {f}$ is mainly limited by $T _ {b}$ and it should be larger than 0.015 and 0.02 kg/s for $T _ {b} = 440$ and 300 K, respectively, while for cases of $h _ {e q} = 5 \ \mathrm{W/(m} ^ {2} {\cdot} \mathrm{K} )$ , m f is mainly limited by the heat capacity of the RC network and it should be larger than 0.04 kg/s; for $h _ {e q} = 10$ , 15 and 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot \mathrm{K} )$ , the coolant convection involved in this work is unable to meet the heat capacity requirments.
> 
> 7. For the TE-AFRSI concept and the cruising trajectory in this work, the largest TE conversion efficiency is 0.90%, the largest electric power supply per unit volume density is $14.2 \times 10 ^ {- 6}$ $W {\cdot} \mathrm{m} ^ {3} / \mathrm{kg} ,$ the largest electric power supply per unit weight is 9.56 W/kg, the largest electric power supply per unit area is 178.4 W/m and the largest electric power supply per unit areal density is $0.94 \times 10 ^ {- 3}$ W·m2/kg.
> 
> 8. The maximum heat amount proportion that can be reused by RC network and TE component is 31.5%; if such a TE-AFRSI concept is used in the second and third leeward surface part, the largest electric power supply can be about 6.16 kW, while if it is adopted for the whole vehicle surface, the largest electric power supply can be above 20 kW.

### 7.6 结论中文翻译

> 本文针对长度为15 m、翼展约6 m的高超声速飞行器在一定巡航轨迹下设计了TM系统。该系统由无源TPS、RC网络和TE组件组成，气动热由无源TPS散发，由RC网络传输，并由RC网络和TE组件重新利用。建立了等效热平衡模型，建立了气动加热与TM系统之间的相互关系，引入整体等效传热系数来表示RC网络和TE组件的热容量，并阐述了该TM系统的设计原理。对于被动TPS，确定相关概念的分布、面积和权重；对于RC网络，得到整车热容量需求分布，建立AFRSI-RC的CFD模型，考虑碳氢化合物和液氢燃料作为冷却剂，确定质量流量的最小限制；对于TE组件，引入了TE-AFRSI概念，根据不同目标的优化得到最优概念。研究了总等效HTC $( h _ {e q} = 0$ to 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot \mathrm{K} ) )$ 和冷侧温度$\left( T _ {b} \right.= \left. 300 \right$ , 367 和 440 K) 对气动热和TM 系统的影响。结果表明： 1．随着$h _ {e q}$的增加，壁温降低，气动热增加；输送和再利用的热量比例增加，散发的热量比例减少；需要提高RC网络和TE组件的容量，同时减少TPS的规模。
> 
> 当 $h _ {e q}$ 从 0 增加到 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot 时，前缘壁温从 1690 K 降低到 1675 K，背风面中线最低壁温从 762 K 降低到 601 K，第三压缩面最高壁温从 1028 K 降低到 964 K。 \mathrm{K} )$ 3. TPS 权重随着 $T _ {b}$ 和 $h _ {e q} ,$ 的增加而减小，并且当 $T _ {b}$ 小时，增加 $h _ {e q}$ 效率更高，反之亦然。然而，虽然增加$T_{b}$是一种非常有效的方法，但它仍然受到材料选择和车辆内部环境要求的限制。对于 $h _ {e q} = 0 , 0.1 , 1 , 2 , 5 ,$ , 10, 15 和 20 ${\sf W} / ( {\sf m} ^ , TPS 权重减少 62.7%, 54.0%, 36.4%, 1.3%, 0.7%, 0%, 0% 和 0%分别为 {2} \cdot {\sf K} ) ,$ 。对于 RC 网络，随着冷却剂温升的增加，冷却剂 m f 减小且趋势减慢。由于$\mathrm{LH} _ {2}$的比热容较大，$\mathrm{LH} _ {2}$所需的$m _ {f}$远小于JET-A，表明LH2具有更强的冷却能力。对于 $\mathrm{LH} _ {2}$ ，通道尺寸对冷却性能影响很小，而对于 JET-A，较小的通道尺寸会带来更好的冷却性能。
> 
> 第二和第三背风面部分的 JET-A RC 网络，对于 $h _ {e q} \ = \ 0.1 ,$ 1 和 $2 \ \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ 的情况，所需的 $m _ {f}$ 主要受 $T _ {b}$ 限制，应大于 0.23 $T _ {b} ~ = ~ 440$ K 为 kg/s，$T _ {b} ~ = ~ 300$ K 为 2.27 kg/s；而对于 $h _ {e q} = 5$ 和 $10 \ \mathsf{W} / ( \mathsf{m} ^ {2} {\cdot} \mathsf{K} ) 的情况，m _ {f}$ 主要受 RC 网络热容量的限制，应分别大于 2.5 和 20.1 kg/s；对于 $h _ {e q} = 15$ 和 20 ${\sf W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ ，本工作中涉及的 RC 冷却剂对流无法满足热容量要求。第二、第三背风面部分的LH2 RC网络，对于$h _ {e q} \= \ 0.1 ,$ , 1 和 $2 \ \mathrm{W} / ( \mathrm{m} ^ {2} {\cdot} \mathrm{K} )$ 的情况，所需的$m _ {f}$主要受$T _ {b}$限制，应大于对于 $T _ {b} = 440$ 和 300 K 分别为 0.015 和 0.02 kg/s，而对于 $h _ {e q} = 5 \ \mathrm{W/(m} ^ {2} {\cdot} \mathrm{K} )$ 的情况，m f 主要受 RC 网络热容量的限制，应大于 0.04 kg/s；对于 $h _ {e q} = 10$ 、 15 和 20 ${\sf W} / ( \mathrm{m} ^ {2} \cdot \mathrm{K} )$ ，本工作涉及的冷却剂对流无法满足热容量要求。
> 
> （机器翻译失败，保留英文原文供复核。）For the TE-AFRSI concept and the cruising trajectory in this work, the largest TE conversion efficiency is 0.90%, the largest electric power supply per unit volume density is $14.2 \times 10 ^ {- 6}$ $W {\cdot} \mathrm{m} ^ {3} / \mathrm{kg} ,$ the largest electric power supply per unit weight is 9.56 W/kg, the largest electric power supply per unit area is 178.4 W/m and the largest electric power supply per unit areal density is $0.94 \times 10 ^ {- 3}$ W·m2/kg. The maximum heat amount proportion that can be reused by RC network and TE component is 31.5%; if such a TE-AFRSI concept is used in the second and third leeward surface part, the largest electric power supply can be about 6.16 kW, while if it is adopted for the whole vehicle surface, the largest electric power supply can be above 20 kW.

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9013 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The hypersonic cruise vehicle and its TM system | 对象/条件/子问题展开 | 3258 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. The fuel-coolant | 对象/条件/子问题展开 | 788 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3. Methodology of TM system design | 方法建构 | 224 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. The equivalent thermal equilibrium model and overall HTC | 方法建构 | 5225 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Correlation between aerodynamic heat and TM subsystems | 对象/条件/子问题展开 | 5188 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Calculation of aerodynamic heat | 对象/条件/子问题展开 | 2097 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.4.1. TPS concepts | 对象/条件/子问题展开 | 725 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.4.2. Design rationale | 对象/条件/子问题展开 | 2459 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.5. RC network and its CFD model | 方法建构 | 4267 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 3.6.1. TE-AFRSI concept and its numerical model | 方法建构 | 2845 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 3.6.2. The concept optimization | 对象/条件/子问题展开 | 2380 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 3.7. The unified governing equation | 对象/条件/子问题展开 | 1699 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.1.1. The aerodynamic heat and the take-away heat | 对象/条件/子问题展开 | 4722 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 4.1.2. The reliability of aerodynamic heat calculation | 对象/条件/子问题展开 | 1184 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.2. Passive TPS | 对象/条件/子问题展开 | 2297 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 4.3.1. The capacity of RC network | 对象/条件/子问题展开 | 4222 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 4.3.2. CFD results of AFRSI-RC network | 结果验证/讨论 | 9367 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 19 | 4.3.3. The determination of AFRSI-RC network for $F _ {I I - L}$ and $F _ {I I I - L}$ | 对象/条件/子问题展开 | 5775 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 4.4. Thermal protection and energy reuse performance of TE-AFRSI | 结果验证/讨论 | 6767 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 21 | 4.5. TM system and its design roadmap | 对象/条件/子问题展开 | 2957 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 22 | 5. Conclusions | 主张回收/边界说明 | 5396 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：heat(181)；mathrm(138)；temperature(127)；tps(101)；fig(80)；aerodynamic(77)；respectively(76)；network(71)；work(66)；electric(54)；cdot(53)；surface(51)；mathsf(51)；concept(50)；coolant(46)；lines(42)；vehicle(40)；cooling(40)；thus(39)；capacity(36)
- 高频学术名词/术语：temperature(127)；capacity(36)；calculation(23)；influence(20)；convection(20)；conversion(18)；optimization(18)；structure(13)；distribution(12)；radiation(11)；density(11)；proportion(11)；addition(10)；difference(10)；requirement(10)
- 高频学术动词：obtained(20)；developed(19)；indicated(16)；optimized(8)；obtain(6)；indicate(5)；introduced(3)；compared(3)；predicted(2)；evaluated(1)；investigated(1)；compare(1)；validated(1)；reveal(1)
- 高频形容词：aerodynamic(77)；electric(54)；coolant(46)；passive(35)；thermal(32)；boundary(27)；component(23)；table(22)；potential(21)；equivalent(20)；convective(15)；coefficient(15)；material(14)；specific(14)；hypersonic(13)
- 高频副词：respectively(76)；supply(20)；mainly(14)；widely(5)；finally(5)；relatively(4)；fully(4)；theoretically(2)；early(1)；extremely(1)；efficiently(1)；firstly(1)
- 高频二词短语：aerodynamic heat(56)；passive tps(35)；mathrm cdot(32)；heat capacity(29)；cdot mathrm(29)；heat transfer(25)；electric power(24)；heat flux(24)；mathsf mathsf(21)；electric potential(20)；power supply(19)；mathrm mathrm(19)；wall temperature(17)；network component(16)；aerodynamic heating(14)
- 高频三词短语：mathrm cdot mathrm(28)；electric power supply(14)；convective heat transfer(12)；overall equivalent htc(10)；power supply per(10)；supply per unit(10)；cases mathrm cdot(9)；mathsf mathsf cdot(9)；mathsf cdot mathsf(9)；heat capacity network(9)；largest electric power(9)；authors previous work(7)
- 被动语态估计：277
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：533
- 一般过去时线索：525
- 现在完成时线索：0
- 情态动词线索：119

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 未稳定识别，需从对应章节人工补充。
### gap/转折句
- 原句：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
  - 可迁移句型：{object}, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
- 原句：However, in this work, the amount of take-away heat should not be neglected.
  - 可迁移句型：{object}, in This study, the amount of take-away heat should not be neglected.
- 原句：As shown in the figure, the results with different mesh size have very limited deviations (smaller than 1%).
  - 可迁移句型：{object} shown in the figure, the results with different mesh size have very limited deviations (smaller than 1%).
- 原句：However, the calculated temperature distributions have some difference as the lower right picture (2 mm channel) shown, thus in this work, the mesh that results into smoother TPS bottom temperature line is adopted.
  - 可迁移句型：{object}, the calculated temperature distributions have some difference as the lower right picture (2 mm channel) shown, thus in This study, the mesh that results into smoother TPS bottom temperature line is adopted.
### 方法提出句
- 原句：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems.
  - 可迁移句型：{object} equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling desi
- 原句：For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
  - 可迁移句型：{object} passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is 
- 原句：The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
  - 可迁移句型：{object} design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
- 原句：With the retirement of Space Shuttle, several subsequent hypersonic and space vehicle programs are proposed, such as NASP and succedent Hyper-X of USA, Skylon of UK, LAPCAT of EU, Space-Liner of Germany.
  - 可迁移句型：{object} the retirement of Space Shuttle, several subsequent hypersonic and space vehicle programs are proposed, such as NASP and succedent Hyper-X of USA, Skylon of UK, LAPCAT of EU, Space-Liner of Germany.
### 结果证明句
- 原句：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient.
  - 可迁移句型：{object} results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient.
- 原句：The RC network is assumed to be under the bottom wall of passive The CFD results shown in this work are independent on the mesh size.
  - 可迁移句型：{object} RC network is assumed to be under the bottom wall of passive The CFD results shown in This study are independent on the mesh size.
- 原句：As shown in the figure, the results with different mesh size have very limited deviations (smaller than 1%).
  - 可迁移句型：{object} shown in the figure, the results with different mesh size have very limited deviations (smaller than 1%).
- 原句：Thus, for the statistical results, all the three meshed models are available.
  - 可迁移句型：{object}, for the statistical results, all the three meshed models are available.
### 贡献收束句
- 原句：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient.
  - 可迁移句型：{object} results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient.
- 原句：In comparison with the space shuttle which is a rocket-launched vehicle, the thermal condition for these subsequent hypersonic vehicles is more severe for two reasons: 1st, the current space vehicles flight in atmosphere for a longer period, thus the accumulation of aerodynamic heat over time is enormous; 2nd, for the current space vehicles, the air-breathing or combined cycle engines are widely adopted, the aerodynamic performance is more concerned and slender configurations are preferred, and thus the reduced bluntness of the fuselage leads to more severe heating effect.
  - 可迁移句型：{object} comparison with the space shuttle which is a rocket-launched vehicle, the thermal condition for these subsequent hypersonic vehicles is more severe for two reasons: 1st, the current space vehicles flight in atmosphere for a longer period, thus the acc
- 原句：The techniques of thermal protection system (TPS) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs.
  - 可迁移句型：{object} techniques of thermal protection system (TPS) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs.
- 原句：For instance, the concept alumina enhanced thermal barrier (AETB) that developed for X-43 (vehicle of Hyper-X project) is much stronger and has better performance of rain erosion.
  - 可迁移句型：{object} instance, the concept alumina enhanced thermal barrier (AETB) that developed for X-43 (vehicle of Hyper-X project) is much stronger and has better performance of rain erosion.
### 边界/谨慎句
- 原句：Communicated by Cummings Russell The thermal energy management (TM) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
  - 可迁移句型：{object} by Cummings Russell The thermal energy management (TM) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
- 原句：The aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive TPS, and a qualified passive TPS should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [8,9].
  - 可迁移句型：{object} aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive TPS, and a qualified passive TPS should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [8,9].
- 原句：The thermal equilibrium equation should be: $$\alpha ( T _ {r} - T _ {w} ) = \varepsilon \sigma T _ {w} ^ {4} + q _ {i n}\tag{1}$$ where α is the convective heat transfer coefficient of aerodynamic heating, $T _ {r}$ is the recovery temperature, $T _ {w}$ is the wall temperature, ε is the surface emissivity, $\sigma ~ = ~ 5.67 ~ \times ~ 10 ^ {- 8} ~ {\sf W} / ( {\mathrm m} ^ {2} {\cdot} {\bar {\mathrm{K}}} ^ {4} )$ is the Stefan-Boltzmann constant, and $q _ {i n}$ is the heat flux of the heat conduction into TPS.
  - 可迁移句型：{object} thermal equilibrium equation should be: $$\alpha ( T _ {r} - T _ {w} ) = \varepsilon \sigma T _ {w} ^ {4} + q _ {i n}\tag{1}$$ where α is the convective heat transfer coefficient of aerodynamic heating, $T _ {r}$ is the recovery temperature, $T _ {w}$
- 原句：In Ref. [46], the surface emissivity of ceramic materials $( \mathsf{C} / \mathsf{C} , \mathsf{C} / \mathsf{SiC} . \hdots )$ is assumed to be 0.8.
  - 可迁移句型：{object} Ref. [46], the surface emissivity of ceramic materials $( \mathsf{C} / \mathsf{C} , \mathsf{C} / \mathsf{SiC} . \hdots )$ is assumed to be 0.8.

## 9. 引用风险层

- 正文引用簇估计：58
- 参考文献条数：58
- 可识别年份条目数：56
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：11
- 高频来源粗略识别：Therm. Eng(10)；Sci. Technol(9)；J. Heat Mass Transf(8)；Manag(5)；Mater(3)；Aerosp. Sci(1)；Mater. Sci(1)；Sci. Eng. B(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] O. Tran, M. Heldmann, J. Fort, ECLSS Heat Sink for the NASP. 2nd International Aerospace Planes Conference, American Institute of Aeronautics and Astronau- tics, 1990.
- [2] S. Balland, V.F. Villace, J. Steelant, Thermal and Energy Management for Hy- personic Cruise Vehicles - Cycle Analysis. 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics, 2015.
- [3] T. Schwanekamp, F. Meyer, T. Reimer, I. Petkov, A. Tröltzsch, M. Siggel, Sys- tem Studies on Active Thermal Protection of a Hypersonic Suborbital Passenger Transport Vehicle. 19th AIAA International Space Planes and Hypersonic Sys- tems and Technologies Conference, American Institute of Aeronautics and As- tronautics, 2014.
- 4. For RC network, the coolant m f decreases and the trend slows down with the increasing coolant temperature rise. The re- quired m f of LH2 is much smaller than JET-A due to the larger specific heat capacity of LH2, and indicates that LH2 has stronger cooling ability. For LH2, the channel size has very lit- tle influence on the cooling performance, while for JET-A, the smaller channel size results into better cooling performance.
- [4] M.Y.M. Ahmed, N. Qin, Recent advances in the aerothermodynamics of spiked hypersonic vehicles, Prog. Aerosp. Sci. 47 (6) (2011) 425–449.
- [5] J. Huang, W-X. Yao, Heat reduction mechanism and aerodynamic optimization of combined non-ablative thermal protection system concept, Int. J. Heat Mass Transf. 152 (2020) 119549.
- [6] J. Huang, W-X. Yao, Parameter study on drag and heat reduction of a novel combinational spiked blunt body and rear opposing jet concept in hypersonic flows, Int. J. Heat Mass Transf. 150 (2020) 119236.
- 7. For the TE-AFRSI concept and the cruising trajectory in this work, the largest TE conversion efficiency is 0.90%, the largest electric power supply per unit volume density is 14.2 × 10−6
- [7] L. Zhu, Y. Li, X. Chen, H. Li, W. Li, C. Li, Hypersonic flow characteristics and relevant structure thermal response induced by the novel combined spike- aerodome and lateral jet strategy, Aerosp. Sci. Technol. 95 (2019) 105459.
- [8] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re-usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [9] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [10] D.E. Myers, C.J. Martin, M.L. Blosser, Parametric Weight Comparison of Ad- vanced Metallic, Ceramic Tile, and Ceramic Blanket Thermal Protection Sys- tems, NASA Langley Technical Report Server, 2000.
- [11] Y. Li, L. Zhang, R. He, Y. Ma, K. Zhang, X. Bai, B. Xu, Y. Chen, Integrated thermal protection system based on C/SiC composite corrugated core sandwich plane structure, Aerosp. Sci. Technol. 91 (2019) 607–616.
- [12] C. Cao, R. Wang, X. Xing, W. Liu, H. Song, C. Huang, Performance improve- ment of integrated thermal protection system using shaped-stabilized compos- ite phase change material, Appl. Therm. Eng. 164 (2020) 114529.
- [13] C-L. Gong, J-J. Gou, J-X. Hu, F. Gao, A novel TE-material based thermal pro- tection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470.

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
