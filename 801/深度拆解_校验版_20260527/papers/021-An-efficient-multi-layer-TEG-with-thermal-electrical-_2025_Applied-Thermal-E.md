# 论文深度拆解：An efficient multi-layer TEG with thermal-electrical interfaces for Mars rover RTGs

> 生成依据：`801/cleantext/021-An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`021-An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-efficient-multi-layer-TEG-with-thermal-electrical-_2025_Applied-Thermal-E.pdf`
- 页数：26
- clean body 字符数：68354
- 摘要字符数：2670
- 参考文献条数：53
- 图题数：23
- 表题数：11
- 表格文件数：15
- 公式候选数：176
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "13 formula(s) need manual review."}]

## 1. 身份层

- 标题：An efficient multi-layer TEG with thermal-electrical interfaces for Mars rover RTGs
- 年份：2025
- 期刊/来源：Applied Thermal E
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands. The Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover. However, most of the TE material
- 主要方法：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. A typical TEG is fabricated and the numerical model is validated by the experi- mental measured voltage. The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
- 主要证据：图表 34 个标题、公式 176 个候选、参考文献 53 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance”，可以通过“A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. A typical TEG is fabricated and the numerical model is validated by the experi- mental measured volt”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：In this work, a multi-layer TEG consists of high-, mid- and low- temperature TE materials is formulated with optimal operating conditions for each layer to improve the con- version efficiency. In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated. Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands. The Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover. However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
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
- 作者声明或文本中可见 gap：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials. However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13]. However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. A typical TEG is fabricated and the numerical model is validated by the experi- mental measured voltage. The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：方法/算法 + 数值验证型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：方法/算法 + 数值验证型
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
| In this work, a multi-layer TEG consists of high-, mid- and low- temperature TE materials is formulated with optimal operating conditions for each layer to improve the con- version efficiency. | 摘要/引言/结论候选 | 图：Fig. 1. The TEGs in Mars RTG. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and tem | 摘要/引言/结论候选 | 图：Fig. 2. The multi-layer TEG with multiple interfaces. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24]. | 摘要/引言/结论候选 | 图：Fig. 3. Seebeck coefficient, thermal conductivity, electrical conductivity and ZT of TE materials. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| At present, the radioisotope thermoelectric generator (RTG) is widely utilized in more than 50 deep-space exploration missions of NASA, e.g., the Voyager [1], Galileo [2], Cassini [3], Curiosity [4] and Perseverance [5]. | 摘要/引言/结论候选 | 表：Table 3 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| All RTGs in these missions show great power-supply performance. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.22, 427.64, 223.92)]] Shi-Yuan Chen a, Xiao-Bing Ma a,b,*, | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The TEGs in Mars RTG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. The multi-layer TEG with multiple interfaces. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Seebeck coefficient, thermal conductivity, electrical conductivity and ZT of TE materials. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The multi-layer TEG and equivalent interfacial layers. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Optimization of multi-layer TEG considering interfacial contact effects. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Contact-type measurement of rough surfaces. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Meshed models and boundary conditions of roughness-scale contact model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 8. Meshed models and boundary conditions of TEG-scale contact model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 9. Components and manufacturing process of TEG sample. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Experimental measurement of TEG performance. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Dimensionless real contact area varied with loading pressure. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Stress distribution of rough surfaces for contacting pairs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. Temperature distribution of contacting pairs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. Potential distribution of contacting pairs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. TCRs under different clearances. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 11 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 12 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.22, 427.64, 223.92)]] Shi-Yuan Chen a, Xiao-Bing Ma a,b,*, Jian-Jun Gou a,** , | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 348.82, 716.91)]] https://doi.org/10.1016/j.applthermaleng.2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 519.91, 62.66, 534.82)]] Kn = λl | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 581.49, 73.21, 606.43)]] λl = kbT ̅̅̅ 2 √ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 682.5, 78.02, 704.04)]] κ = κp 1 + 2-α α | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (78.46, 684.39, 288.67, 706.15)]] 4εT γ+1 Kn (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (307.95, 256.81, 452.2, 298.53)]] κ(T) = -9.38276141369587 \times 10-11T3+ 1.3200931682370 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (43.6, 394.52, 498.02, 405.49)]] Silver-epoxy adhesive 2.3 / / 0.3504 / 108 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The radioisotope is the most promising power supply technology for Mars exploration and the thermoelectric generator (TEG) is the key component that convert the heat from isotope decay into electrical energy. However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials. In this work, a multi-layer TEG consists of high-, mid- and low- temperature TE materials is formulated with optimal operating conditions for each layer to improve the con- version efficiency. A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated. In the TEG-scale, the contact effect is equivalent to an additional layer and considered in the structural optimization with the objective of maximum gravimetric power density under typical isotope decay heat conditions. A typical TEG is fabricated and the numerical model is validated by the experi- mental measured voltage. The optimal TEG for Martian environment is finally obtained with conversion effi- ciency of 8.444%.
> The primary limitation of the current TEG technology is the rela- tively low conversion efficiency, which is typically lower than 6 % that have been applied in Mars exploration engineering. However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13]. Therefore, the invention of TEGs with high conversion efficiency has become a pressing research priority. In the design and application of conventional TEG, the single-layer TE structure is widely used [14–20]. However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands. The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24]. Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.

### 7.4 摘要中文翻译

> 放射性同位素是火星探测最有前途的供电技术，而热电发电机（TEG）是将同位素衰变产生的热量转化为电能的关键部件。然而，当前 TEG 的关键缺点是由于热电 (TE) 材料的工作温度范围有限而导致转换效率低。在这项工作中，由高、中、低温TE材料组成的多层TEG被配制为每层的最佳操作条件，以提高转换效率。建立了两尺度接触模型来阐明多层之间的热电界面效应。在粗糙度尺度上，对界面火星大气间隙下的热接触电阻和电接触电阻进行了数值计算，并与真空、地球大气和银环氧树脂粘合剂下的热接触电阻和电接触电阻进行了比较，阐明了压力和温度的影响，并对数值结果进行了实验验证。在 TEG 尺度中，接触效应相当于附加层，并在结构优化中考虑，目标是在典型同位素衰变热条件下获得最大重量功率密度。制作了一个典型的 TEG，并通过实验测量电压验证了数值模型。最终得到适合火星环境的最优TEG，转换效率为8.444%。目前TEG技术的主要局限性是转换效率相对较低，在火星探测工程中应用的转换效率通常低于6%。
> 
> 然而，对于最新的RTG，即毅力号火星车中的RTG，TE转换效率仍然低于6.3％，7％是NASA下一代RTG的目标效率[13]。因此，发明高转换效率的TEG已成为紧迫的研究重点。在传统TEG的设计和应用中，广泛使用单层TE结构[14-20]。然而，大多数TE材料都有明确的最佳工作温度，因此这种单层结构的工作温度范围有限，并且性能在一定程度上较弱，逐渐无法满足日益增长的性能需求。每层具有适当温度范围的多层结构TEG往往会表现出更好的性能[21-24]。因此，本文在火星环境下创新创建了多层TEG，并以最大重力功率密度为目标优化尺寸，以实现更高的输出功率和TE转换效率。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work, a multi-layer TEG composed of high-, mid- and lowtemperature TE materials is formulated for the power supply of Mars exploration. A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers. In the roughness-scale, the thermal and electrical contact resistances under interfacial vacuum, Earth’s atmosphere, Martian atmosphere and silverepoxy adhesive clearances are numerically calculated and the numerical results are experimentally validated. In the TEG-scale, the contact effect is equivalent to an additional layer and considered in the structural optimization with the objective of maximum gravimetric power density under typical radioisotope decay heat conditions. The following conclusions are drawn:
> 
> 1. The TCR decreases with the increase of loading pressure and is influenced by the average interfacial temperature and interfacial clearance medium. Under Martian atmosphere, TCR decreases with the increase of the average interfacial temperature, and similar rules are also presented under Earth’s atmosphere and silver-epoxy adhesive ones. The TCR of contacting pairs between substrate and electrode decreases from $2.961 \times 10 ^ {- 4} \mathrm{to} 1.906 \times 10 ^ {- 4}$ in the range of 261.0 to 923.6 K under Martian atmosphere clearance.
> 
> 2. The ECR decreases with the increase of loading pressure and is influenced by the interfacial clearance medium. When the loading pressure increases from 1.201 to 3.041 MPa, the ECR decreases from
> 
> $2.578 \times 10 ^ {- 8} \mathrm{to} 1.019 \times 10 ^ {- 8} \mathrm{and} 6.778 \times 10 ^ {- 10} \mathrm{to} 6.711 \times 10 ^ {- 10} \Omega$ $\mathtt {m} ^ {2}$ under vacuum/atmosphere and silver-epoxy adhesive clearances, respectively.
> 
> 3. The numerical prediction models of TCR and ECR are validated by experimental measurement with the maximum deviations of 15.4 % and 4.59 %, respectively. Additionally, the TEG performance evaluation model is verified with maximum deviation of 12.1 % in output voltage.
> 
> 4. The interfacial contact affects the TEG performance. Compared with the ideal model, the conversion efficiency considering the interfacial contact effects decreases by 63.28 %, 61.76 % and 61.89 % under vacuum, Earth’s atmosphere and Martian atmosphere clearances, respectively. The output power of TEG under Martian atmosphere is 3.803 % higher than that under vacuum, and 0.3352 % lower than that under Earth’s atmosphere.
> 
> 5. The gravimetric power density and TE conversion efficiency of the multi-layer TEG are 3.514 W/kg and 8.444 % in Martian environment, respectively. The maximum gravimetric power density, conversion efficiency and output power of radioisotope power supply are 1.998 W/kg, 7.189 % and 107.8 W, respectively.
> 
> The limitations of this study are listed: Firstly, the proposed TEG configuration is conducted under the assumption of constant heat source power, without considering its attenuation over time. Additionally, this study focuses on designing for one combination of high-, mid, and lowtemperature TE materials. The optimal TEG configuration is sensitive to TE material properties, and variations in input parameters of TE material properties exceeding 10 % can lead to changes in the optimal TEG configuration.

### 7.6 结论中文翻译

> 本工作配制了一种由高、中、低温TE材料组成的多层TEG，用于火星探测电源。建立了两尺度接触模型来阐明多层之间的热电界面效应。在粗糙度尺度上，对界面真空、地球大气、火星大气和银环氧树脂粘合剂间隙下的热接触电阻和电接触电阻进行了数值计算，并对数值结果进行了实验验证。在 TEG 尺度中，接触效应相当于附加层，并在结构优化中考虑，目标是在典型放射性同位素衰变热条件下获得最大重量功率密度。得出以下结论： 1、TCR随着加载压力的增加而减小，并受平均界面温度和界面间隙介质的影响。在火星大气层下，TCR随着平均界面温度的升高而降低，在地球大气层和银环氧粘合剂下也呈现类似的规律。在火星大气间隙下，在 261.0 到 923.6 K 范围内，基板和电极之间的接触对的 TCR 从 $2.961 \times 10 ^ {- 4} \mathrm{下降到} 1.906 \times 10 ^ {- 4}$。 ECR随着加载压力的增加而减小，并且受界面间隙介质的影响。当加载压力从1.201增加到3.041 MPa时，ECR从$2.578 \times 10 ^ {- 8} \mathrm{下降到} 1.019 \times 10 ^ {- 8} \mathrm{和} 6.778 \times 10 ^ {- 10} \mathrm{到} 6.711 \times 10 ^ {- 10} \Omega$ $\mathtt {m} ^ {2}$ 分别在真空/大气和银环氧树脂粘合剂间隙下。
> 
> 通过实验测量验证了TCR和ECR的数值预测模型，最大偏差分别为15.4%和4.59%。此外，TEG 性能评估模型经过验证，输出电压最大偏差为 12.1%。界面接触影响 TEG 性能。与理想模型相比，在真空、地球大气层和火星大气层间隙下，考虑界面接触效应的转换效率分别降低了63.28%、61.76%和61.89%。 TEG在火星大气层下的输出功率比真空下高3.803%，比地球大气层下低0.3352%。在火星环境中，多层TEG的重量功率密度和TE转换效率分别为3.514 W/kg和8.444%。放射性同位素电源的最大重量功率密度、转换效率和输出功率分别为1.998 W/kg、7.189%和107.8 W。本研究的局限性如下： 首先，所提出的 TEG 配置是在热源功率恒定的假设下进行的，没有考虑其随时间的衰减。此外，本研究重点关注高温、中温和低温 TE 材料的一种组合的设计。最佳 TEG 配置对 TE 材料属性敏感，TE 材料属性输入参数的变化超过 10% 可能会导致最佳 TEG 配置发生变化。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6440 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The RTG and Martian environment | 对象/条件/子问题展开 | 5866 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. The radioisotope heat source of TEG | 对象/条件/子问题展开 | 3187 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. The multi-layer TEG and structural optimization model | 方法建构 | 8589 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. Governing equations | 对象/条件/子问题展开 | 3340 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Interfaces reconstruction and TCR, ECR calculations | 对象/条件/子问题展开 | 3853 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Roughness-scale contact model | 方法建构 | 2793 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.4. TEG-scale contact model | 方法建构 | 5256 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.1. Fabrication of TEG | 实验或测量设定 | 981 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 10 | 4.2. Measurement of TCR and TEG output voltage | 实验或测量设定 | 2101 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 11 | 4.3. Measurement of ECR | 实验或测量设定 | 1660 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 12 | 5.1.1. Contact deformation | 对象/条件/子问题展开 | 1092 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.1.2. Heat transfer and electrical conduction | 对象/条件/子问题展开 | 2513 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.1.3. The TCR and ECR under different clearances | 对象/条件/子问题展开 | 4540 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.2.1. The influence of contact effects under different clearances | 对象/条件/子问题展开 | 3043 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5.2.2. The performance of multi-layer TEG under Martian atmosphere | 结果验证/讨论 | 3365 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 17 | 5.2.3. The performance of radioisotope power supply | 结果验证/讨论 | 2723 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 5.3.1. Measured and numerically calculated TCRs and ECRs | 对象/条件/子问题展开 | 2505 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 6. Conclusion | 主张回收/边界说明 | 3288 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：teg(111)；power(86)；contact(82)；heat(78)；temperature(75)；atmosphere(75)；mathrm(75)；clearance(65)；interfacial(62)；thermal(56)；respectively(55)；martian(48)；fig(45)；tcr(44)；times(41)；partial(40)；conversion(38)；output(38)；legs(36)；frac(36)
- 高频学术名词/术语：temperature(75)；clearance(65)；conversion(38)；density(34)；conductivity(34)；pressure(33)；resistance(27)；performance(25)；optimization(23)；environment(14)；insulation(14)；conduction(13)；configuration(13)；exploration(12)；measurement(12)
- 高频学术动词：compared(12)；developed(4)；investigated(4)；evaluate(4)；validated(4)；optimized(3)；indicate(3)；presented(3)；predict(1)；estimated(1)；revealed(1)；indicated(1)；constructed(1)；obtained(1)；predicted(1)
- 高频形容词：interfacial(62)；thermal(56)；partial(40)；adhesive(30)；electrical(27)；gravimetric(27)；equivalent(21)；table(18)；potential(17)；material(16)；optimal(15)；environment(14)；real(14)；measurement(12)；experimental(11)
- 高频副词：respectively(55)；supply(22)；numerically(10)；slightly(7)；primarily(4)；relatively(4)；significantly(4)；widely(3)；mainly(3)；directly(3)；effectively(3)；experimentally(3)
- 高频二词短语：martian atmosphere(35)；power density(30)；multi-layer teg(28)；earth atmosphere(28)；loading pressure(28)；gravimetric power(27)；thermal conductivity(27)；conversion efficiency(25)；output power(25)；contact effects(24)；silver-epoxy adhesive(24)；interfacial contact(21)；power supply(21)；times mathrm(20)；atmosphere clearance(19)
- 高频三词短语：gravimetric power density(26)；interfacial contact effects(18)；radioisotope power supply(14)；silver-epoxy adhesive clearance(14)；times mathrm times(12)；power density conversion(11)；density conversion efficiency(11)；average interfacial temperature(10)；equivalent interfacial layers(10)；radioisotope heat source(9)；partial frac partial(9)；frac partial partial(9)
- 被动语态估计：159
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：356
- 一般过去时线索：305
- 现在完成时线索：0
- 情态动词线索：28

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：However, the development of efficient TEGs for Mars exploration requires accurate quantification of the TCR and ECR under interfacial Martian atmosphere clearance.
  - 可迁移句型：{object}, the development of efficient TEGs for Mars exploration requires accurate quantification of the TCR and ECR under interfacial Martian atmosphere clearance.
### gap/转折句
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  - 可迁移句型：{object}, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
- 原句：However, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].
  - 可迁移句型：{object}, for the latest RTG, i.e., RTG in Perseverance Mars rovers, the TE conversion efficiency is still lower than 6.3 %, and 7 % is the target efficiency for NASA’s next-generation RTG [13].
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands.
  - 可迁移句型：{object}, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands
- 原句：The Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover.
  - 可迁移句型：{object} Mars exploration mission is full of challenges, and the radioisotope is the most promising technology to supply stable and reliable power during the long-duration exploration mission for the Mars rover.
### 方法提出句
- 原句：A two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
  - 可迁移句型：{object} two-scale contact model is established to clarify the thermal-electrical interfacial effects between multiple layers.
- 原句：A typical TEG is fabricated and the numerical model is validated by the experi- mental measured voltage.
  - 可迁移句型：{object} typical TEG is fabricated and the numerical model is validated by the experi- mental measured voltage.
- 原句：The multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
  - 可迁移句型：{object} multi-layer structure TEG with appropriate temperature range for each layer tends to present better performance [21–24].
- 原句：At present, the radioisotope thermoelectric generator (RTG) is widely utilized in more than 50 deep-space exploration missions of NASA, e.g., the Voyager [1], Galileo [2], Cassini [3], Curiosity [4] and Perseverance [5].
  - 可迁移句型：{object} present, the radioisotope thermoelectric generator (RTG) is widely utilized in more than 50 deep-space exploration missions of NASA, e.g., the Voyager [1], Galileo [2], Cassini [3], Curiosity [4] and Perseverance [5].
### 结果证明句
- 原句：In the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure and temperature are clarified and the numerical results are experimentally validated.
  - 可迁移句型：{object} the roughness-scale, the thermal and electrical contact resistances under interfacial Martian atmosphere clearance are numerically calculated and compared with the vacuum, Earth’s atmosphere, and silver-epoxy adhesive ones, the influence of pressure a
- 原句：Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
  - 可迁移句型：{object}, in This study, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
- 原句：All RTGs in these missions show great power-supply performance.
  - 可迁移句型：{object} RTGs in these missions show great power-supply performance.
- 原句：Therefore, in this paper, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
  - 可迁移句型：{object}, in This study, a multi-layer TEG is innovatively created under Martian environment and the dimension is optimized with the objective of maximum gravimetric power density to achieve higher output power and TE conversion efficiency.
### 贡献收束句
- 原句：In this work, a multi-layer TEG consists of high-, mid- and low- temperature TE materials is formulated with optimal operating conditions for each layer to improve the con- version efficiency.
  - 可迁移句型：{object} This study, a multi-layer TEG consists of high-, mid- and low- temperature TE materials is formulated with optimal operating conditions for each layer to improve the con- version efficiency.
- 原句：The silver-epoxy adhesive can substantially enhance both heat transfer and electrical conduction.
  - 可迁移句型：{object} silver-epoxy adhesive can substantially enhance both heat transfer and electrical conduction.
- 原句：The red arrow denotes the direction of heat flow, providing enhanced clarity in visualizing thermal transfer.
  - 可迁移句型：{object} red arrow denotes the direction of heat flow, providing enhanced clarity in visualizing thermal transfer.
- 原句：The cooling fins of the radioisotope power supply improve the performance of the radioisotope power supply by enhancing heat dissipat In this work, a multi-layer TEG composed of high-, mid- and lowtemperature TE materials is formulated for the power supply of Mars exploration.
  - 可迁移句型：{object} cooling fins of the radioisotope power supply improve the performance of the radioisotope power supply by enhancing heat dissipat In This study, a multi-layer TEG composed of high-, mid- and lowtemperature TE materials is formulated for the power supp
### 边界/谨慎句
- 原句：However, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
  - 可迁移句型：{object}, the crucial drawback of current TEGs is the low conversion efficiency due to the limited operating temperature range for thermoelectric (TE) materials.
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands.
  - 可迁移句型：{object}, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak perfor- mance to some extent, which gradually failed to meet the growing performance demands
- 原句：However, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
  - 可迁移句型：{object}, most of the TE material has a well-defined optimal operating temperature, thus such single-layer structure has a limited operating temperature range and weak performance to some extent, which gradually failed to meet the growing performance demands.
- 原句：Most published reports of interfacial contact effects are limited to conventional environments, such as air under standard conditions.
  - 可迁移句型：{object} published reports of interfacial contact effects are limited to conventional environments, such as air under standard conditions.

## 9. 引用风险层

- 正文引用簇估计：29
- 参考文献条数：53
- 可识别年份条目数：56
- 2021 年及以后参考文献数：22
- 2010 年以前经典文献数：7
- 高频来源粗略识别：Therm. Eng(7)；J. Heat Mass Transf(6)；Energy(5)；J. Energy Res(3)；J. Therm. Sci(3)；Electron. Mater(2)；Astrophys(1)；Spacecr. Rockets(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] R. Lallement, J.L. Bertaux, E. Qu´emerais, B.R. Sandel, Galactic cosmic rays measured by UVS on Voyager 1 and the end of the modulation, Astron. Astrophys. 563 (2014) A108.
- [2] J.W. Stultz, Thermal design of the Galileo spun and despun science, J. Spacecr. Rockets 28 (2) (1991) 139–145.
- [3] S. Guarro, B. Bream, L.K. Rudolph, R.J. Mulvihill, The Cassini mission risk assessment framework and application techniques, Reliab. Eng. Syst. Saf. 49 (3) (1995) 293–302.
- [4] S.J. Gomez, D. Cheikh, T. Vo, P. Von Allmen, K. Lee, M. Wood, G.J. Snyder, B. S. Dunn, J. Fleurial, S.K. Bux, Synthesis and characterization of vacancy-doped neodymium telluride for thermoelectric applications, Chem. Mat. 31 (12) (2019) 4460–4468.
- [5] T. Widdicombe, R.A. Borrelli, MCNP modelling of radiation effects of the Dragonfly mission’s RTG on Titan II: Atmospheric ionization effects, Acta Astronaut. 186 (2021) 517–522.
- [6] M.B. Naseem, J. Lee, S. In, Radioisotope thermoelectric generators (RTGs): a review of current challenges and future applications, Chem. Commun. 60 (96) (2024) 14155–14167.
- [7] C.P. Bankston, K.L. Atkins, E.F. Mastal, D.G. Mcconnell, Technology development issues in space nuclear-power for planetary exploration, Acta Astronaut. 24 (1991) 161–170.
- [8] X. Liu, H. Sun, S.M. Tang, C.L. Wang, W.X. Tian, S.Z. Qiu, G.H. Su, Thermal- hydraulic design features of a micronuclear reactor power source applied for multipurpose, Int. J. Energy Res. 43 (9) (2019) 4170–4183.
- [9] L.S. Hewawasam, A.S. Jayasena, M.M.M. Afnan, R.A.C.P. Ranasinghe, M. A. Wijewardane, Waste heat recovery from thermo-electric generators (TEGs), Energy Rep. 6 (2020) 474–479.
- [10] M.A. Zoui, S. Bentouba, J.G. Stocholm, M. Bourouis, A review on thermoelectric generators: progress and applications, Energies 13 (14) (2020). 2.578 × 10−8 to 1.019 × 10−8 and 6.778 × 10−10 to 6.711 × 10−10 Ω m2 under vacuum/atmosphere and silver-epoxy adhesive clearances, respectively.
- [11] Y.C. Lan, J.H. Lu, S.L. Wang, An experimental study on the performance of TEGs using uniform flow distribution heat exchanger for low-grade thermal energy recovery, Energy 292 (2024) 15.
- [12] Z. Wang, F.H. Han, Y.L. Ji, W.H. Li, Redundant energy combination and recovery scheme for dual fuel carriers based on thermoelectric harvesting with a large temperature range, Int. J. Energy Res. 45 (5) (2021) 7404–7420.
- [13] T.C. Holgate, R. Bennett, T. Hammel, T. Caillat, S. Keyser, B. Sievers, Increasing the efficiency of the multi-mission radioisotope thermoelectric generator, J. Electron. Mater. 44 (6) (2015) 1814–1821.
- [14] J. Joung, Y. Kang, Y. Nam, J. Jeong, Analysis of power generation considering design and finishing materials of thermoelectric energy harvesting blocks, Renew. Energy 231 (2024) 15.
- [15] J. Wei, J.W. Hui, T.T. Wang, Y. Wang, Y.P. Guo, S.Q. Zhang, Y.B. Zhang, X.Y. Qiao, A thermoelectric energy harvesting system for pavements with a fin cooling structure, Sustain. Energ. Fuels 7 (1) (2022) 248–262.

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
