# 论文深度拆解：The unit cell method in predictions of thermal expansion properties of textile reinforced composites

> 生成依据：`801/cleantext/043-The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`043-The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S.pdf`
- 页数：19
- clean body 字符数：62298
- 摘要字符数：1382
- 参考文献条数：43
- 图题数：24
- 表题数：10
- 表格文件数：13
- 公式候选数：239
- 提取质量分：0.99
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "12 formula(s) need manual review."}]

## 1. 身份层

- 标题：The unit cell method in predictions of thermal expansion properties of textile reinforced composites
- 年份：2018
- 期刊/来源：Composite S
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：A unit cell model should contain enough mesoscopic structure information, while for the macroscopic characteristics such as the related macro physical field that have been abandoned in the RVE formulation, we need to derive appropriate BCs to keep enough representation. Therefore, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
- 主要方法：In this paper, a general approach is developed for the establishment of such a unit cell model. The application scope of present unit cell method is clarified from the thermal and mechanical point of views. The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
- 主要证据：图表 34 个标题、公式 239 个候选、参考文献 43 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“A unit cell model should contain enough mesoscopic structure information, while for the macroscopic characteristics such as the related macro physical field that have been abandone”，可以通过“In this paper, a general approach is developed for the establishment of such a unit cell model. The application scope of present unit cell method is clarified from the thermal and mechanical point of views. The influence”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures. The results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the FE method is more capable in capturing details like the local physical fields. To be general, the weave process is always used to create two-dimensional (2D) laminate structures, while the knitting process is good at manufacturing three-dimensional (3D) structure, and the braidi Fiber yarns can be considered as unidirectional (UD) fiber reinforced composites and the typical transverse fiber distribution pattern in matrix is shown in Fig.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：A unit cell model should contain enough mesoscopic structure information, while for the macroscopic characteristics such as the related macro physical field that have been abandoned in the RVE formulation, we need to derive appropriate BCs to keep enough representation. Therefore, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
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
- 作者声明或文本中可见 gap：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell. According to Ref. [3], excluding the larger computational cost, another disadvantage of FE method is its dependency on the size of RVE. 6, the two black lines with arrow are the translation axes x and $y ,$ the blue lines are the reflection planes $P _ {x}$ and $P _ {y}$ (perpendicular to the paper), and the pink dot presents the rotation axis $L _ {z}$ As shown in Fig. $^ {6 ,}$ UC1 is formulated based on translational symmetries along xand y-axis, and then two reflectional symmetries about $P _ {x}$ and $P _ {y}$ planes can be observed in UC1 structure, and UC2 and UC3 will then be formulated based on them, respectively.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this paper, a general approach is developed for the establishment of such a unit cell model. The application scope of present unit cell method is clarified from the thermal and mechanical point of views. The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
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
| In this paper, a general approach is developed for the establishment of such a unit cell model. | 摘要/引言/结论候选 | 图：Fig. 2. Displacement fields in translational symmetric structures. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The application scope of present unit cell method is clarified from the thermal and mechanical point of views. | 摘要/引言/结论候选 | 图：Fig. 3. Reflectional symmetric structure and displacement fields. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures. | 摘要/引言/结论候选 | 图：Fig. 4. 180° Rotational symmetric structure and displacement fields. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The approach developed in this paper can be applied to thermal expansion studies of any other composites with relevant structure symmetries. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The effective properties of composites can be calculated by a representative volume element (RVE) model based on the known properties of each phase. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 203.51, 419.7, 217.43)]] Jian-Jun Goua,⁎, Chun-L | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 2. Displacement fields in translational symmetric structures. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Reflectional symmetric structure and displacement fields. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. 180° Rotational symmetric structure and displacement fields. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. Temperature and displacement distributions. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. Unit cells of UD composite. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Boundaries of unit cells of UD composite. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Symmetries and unit cells of plain woven composites. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. All the textiles are shown in a 2D top view, while for unit cells both 2D and 3D schematics are displayed. In this work, two unit cells of different siz | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 9. Multi-harness satin weave textiles and unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Geometric parameters and boundaries of unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Meshed models. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 11. The application of boundary conditions. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Coordinate systems involved in the calculation. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Displacement and stress fields of UD composite. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Transverse deformations after thermal expansion (UD). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 11 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 12 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 13 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 203.51, 419.7, 217.43)]] Jian-Jun Goua,⁎, Chun-Lin Gonga, Liang-Xian | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 686.56, 184.45, 704.34)]] ⁎ Corresponding author. E-mail address: jj | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (306.3, 358.6, 557.66, 370.12)]] = - ∇ = λ q T i x y z , , , i i 000 (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (306.36, 525.1, 557.65, 534.03)]] = - σ ε α T C( ) 000 (2-1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (306.48, 550.22, 557.65, 560.79)]] = = ε α T i x y z , , , ith i 00 (2-2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (44.01, 158.44, 167.16, 177.32)]] - = \pm - + - | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.15, 444.09, 557.65, 453.21)]] - = - ′ ′ u u u u M O M O (5-1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 462.4, 557.65, 471.52)]] - = - ′ ′ v v v v M O M O (5-2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Thermal expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell. In this paper, a general approach is developed for the establishment of such a unit cell model. For the derivation of unit cell boundary conditions, three rules are summarized according to the displacement fields in translational, reflectional and 180° rotational symmetric structures under a uniform temperature change loading. The application scope of present unit cell method is clarified from the thermal and mechanical point of views. Three typical composites, i.e., unidirectional fiber reinforced composite, plain woven composite and multi-harness (4HS, 5HS, 6HS, 7HS and 8HS) satin woven composites are then studied, and four, three and two size-reducing unit cells are formulated, respectively. The thermal expansion behaviors of each composite are analyzed, and the effective thermal expansion coefficients are predicted. The influence of structure symmetries on the deformation pattern of unit cell models is clarified. The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures. The approach developed in this paper can be applied to thermal expansion studies of any other composites with relevant structure symmetries.

### 7.4 摘要中文翻译

> 具有一定结构对称性的织物增强复合材料的热膨胀性能可以通过尺寸有限的晶胞有效地计算。本文提出了建立这种晶胞模型的通用方法。在晶胞边界条件的推导中，根据均匀温度变化载荷下平移、反射和180°旋转对称结构的位移场，总结出3条规则。从热学和力学的角度阐明了本晶胞方法的应用范围。然后研究了三种典型的复合材料，即单向纤维增强复合材料、平纹编织复合材料和多线(4HS、5HS、6HS、7HS和8HS)缎纹编织复合材料，并分别配制了四个、三个和两个尺寸减小的晶胞。分析了每种复合材料的热膨胀行为，并预测了有效热膨胀系数。阐明了结构对称性对晶胞模型变形模式的影响。数值模型通过从不同尺寸的晶胞获得的相同结果以及文献中可用的结果进行验证。本文开发的方法可应用于具有相关结构对称性的任何其他复合材料的热膨胀研究。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> This work developed an approach to formulate unit cells to predict effective coefficient of thermal expansion of textile reinforced composites. The displacement distribution patterns in translational, reflectional and $180 ^{\circ}$ rotational symmetric structures are summarized as unified equations and are confirmed by typical calculations. The application scope of the present method is defined in the point views of both thermal and mechanical physics. Multi-size unit cells of unidirectional fiber reinforced, plain woven and multi-harness $( 4 , 5 , 6 , 7$ and 8HS) satin woven composites are formulated, the corresponding BCs are derived, and the thermal expansion calculations are conducted. Four, three and two size-reducing unit cells are formulated for each type of composite, respectively. The developed method can be referenced by any composites with corresponding symmetric structures. The specific novel studies involved in this work are: the summary of relative displacement distribution rules for three basic symmetric structures, four unit cells of different sizes are formulated for UD composite, two smaller unit cells for satin woven composite are formulated, and the deformation pattern on unit cell boundaries and its relations with structure symmetries are clarified.
> 
> Several following conclusions can be summarized:
> 
> 1. For a composite with symmetric structures, the effective coefficient of thermal expansion can be efficiently calculated by a unit cell model. Such unit cell should be formulated based on structure symmetries, and relevant BCs can be derived based on displacement distribution rules summarized in this work. Such unit cell models can also be used to predict the local stress distributions in fiber yarns or textile reinforced composites and thus has potentials for damage analysis of these composites.
> 
> 2. The boundary conditions of unit cells are derived based on the assumption of uniform macro strain field, which can be resulted in by a uniform temperature loading. Thus, the current unit cell method can only be used to simulate thermal expansion behaviors under a uniform temperature loading, such as the thermal residual stresses after a specific heat treating.
> 
> 3. For boundaries that can be formulated by reflectional symmetries, the uniform normal displacement and the uniform deformation can be obtained in thermal expansion calculations; for boundaries that can only be formulated based on translational or rotational symmetries, the normal displacement and the relevant deformation are non-uniform.

### 7.6 结论中文翻译

> 这项工作开发了一种制定晶胞的方法来预测纺织增强复合材料的有效热膨胀系数。平动、反射和$180 ^{\circ}$旋转对称结构中的位移分布模式被总结为统一方程，并通过典型计算得到证实。本方法的应用范围是从热物理和机械物理的角度来定义的。制定了单向纤维增强、平纹编织和多线束$(4、5、6、7$和8HS)缎纹编织复合材料的多尺寸晶胞，推导了相应的BC，并进行了热膨胀计算。每种类型的复合材料分别配制有四个、三个和两个尺寸减小晶胞。所开发的方法可以被任何具有相应对称结构的复合材料参考。这项工作涉及的具体新颖研究是：总结了三种基本对称结构的相对位移分布规则，为UD复合材料制定了四种不同尺寸的晶胞，为缎纹编织复合材料制定了两种较小的晶胞，并阐明了晶胞边界的变形模式及其与结构对称性的关系。可以总结出以下几个结论： 1.对于具有对称结构的复合材料，可以通过晶胞模型有效地计算有效热膨胀系数。这种晶胞应该基于结构对称性来制定，并且可以根据本工作中总结的位移分布规则导出相关的BC。
> 
> 这种晶胞模型还可用于预测纤维纱线或纺织增强复合材料中的局部应力分布，因此具有对这些复合材料进行损伤分析的潜力。晶胞的边界条件是基于均匀宏观应变场的假设推导的，该宏观应变场可以由均匀的温度载荷产生。因此，目前的晶胞方法只能用于模拟均匀温度载荷下的热膨胀行为，例如特定热处理后的热残余应力。对于可以用反射对称性表述的边界，可以在热膨胀计算中得到均匀法向位移和均匀变形；对于只能基于平移或旋转对称性制定的边界，法向位移和相关变形是不均匀的。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8223 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Constitutive equations | 对象/条件/子问题展开 | 2617 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Temperature and displacement distributions in symmetric structures | 对象/条件/子问题展开 | 2576 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2.1. Translational symmetric structure | 对象/条件/子问题展开 | 4146 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.2.2. Reflectional symmetric structure | 对象/条件/子问题展开 | 1814 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 2.2.3. 180° rotational symmetric structure | 对象/条件/子问题展开 | 1506 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 2.2.4. Summary of displacement distribution rules | 对象/条件/子问题展开 | 1162 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 2.2.5. Application scopes | 对象/条件/子问题展开 | 3117 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3. Development of unit cells | 对象/条件/子问题展开 | 531 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.1.1. Formulation of unit cells | 方法建构 | 3246 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 3.1.2. Boundary conditions | 对象/条件/子问题展开 | 1560 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 3.2. Unit cells of plane woven composites | 对象/条件/子问题展开 | 801 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 3.2.1. Formulation of unit cells | 方法建构 | 1179 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 14 | 3.2.2. Boundary conditions | 对象/条件/子问题展开 | 1541 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 3.3.1. Formulation of unit cells | 方法建构 | 1795 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 16 | 3.3.2. Boundary conditions | 对象/条件/子问题展开 | 923 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 3.4. Summary | 对象/条件/子问题展开 | 571 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 4.1. Application of boundary conditions | 对象/条件/子问题展开 | 2406 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 4.2. Model discretization | 方法建构 | 2194 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 20 | Macro structure | 对象/条件/子问题展开 | 3153 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 21 | 4.3. Material properties | 对象/条件/子问题展开 | 641 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 22 | 5.1.1. Thermal expansion behaviors | 对象/条件/子问题展开 | 2872 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 23 | 5.1.2. Effective CTE and validation of numerical models | 方法建构 | 519 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 24 | 5.2.1. Thermal expansion behaviors | 对象/条件/子问题展开 | 1503 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 25 | 5.2.2. Effective CTE and validation of boundary conditions | 对象/条件/子问题展开 | 285 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 26 | 5.3.1. Thermal expansion behaviors | 对象/条件/子问题展开 | 1513 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 27 | 5.3.2. Effective CTE and validation of boundary conditions | 对象/条件/子问题展开 | 723 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 28 | 5.4. Normal displacement on boundary planes | 对象/条件/子问题展开 | 5111 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 29 | 6. Conclusions | 主张回收/边界说明 | 2557 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：unit(109)；thermal(70)；fig(60)；cell(57)；bcs(56)；uniform(55)；composites(53)；varepsilon(53)；temperature(51)；displacement(51)；cells(50)；structure(45)；boundary(45)；woven(45)；composite(43)；prime(43)；symmetric(42)；expansion(41)；respectively(40)；symmetries(38)
- 高频学术名词/术语：temperature(51)；displacement(51)；structure(45)；expansion(41)；distribution(21)；deformation(17)；rotation(14)；reference(14)；derivation(12)；reflection(12)；x-displacement(12)；formulation(10)；calculation(10)；direction(10)；y-displacement(10)
- 高频学术动词：obtained(26)；derived(23)；developed(7)；derive(5)；indicated(5)；obtain(3)；investigated(3)；predict(3)；compared(2)；validated(2)；revealed(2)；propose(1)；develop(1)；presented(1)；indicate(1)
- 高频形容词：thermal(70)；displacement(51)；boundary(45)；symmetric(42)；relative(38)；reflectional(29)；normal(25)；macroscopic(24)；translational(24)；rotational(24)；effective(23)；table(22)；periodic(19)；mechanical(15)；numerical(14)
- 高频副词：respectively(40)；separately(4)；carefully(3)；widely(2)；mainly(2)；entirely(2)；fully(2)；similarly(2)；totally(2)；finally(2)；easily(2)；frequently(1)
- 高频二词短语：unit cell(56)；unit cells(50)；thermal expansion(41)；satin woven(24)；woven composites(24)；varepsilon varepsilon(24)；boundary planes(23)；prime prime(21)；normal displacement(18)；plain woven(17)；symmetric structures(15)；big big(15)；woven composite(15)；bcs derived(14)；uniform temperature(14)
- 高频三词短语：satin woven composites(15)；thermal expansion behaviors(11)；varepsilon varepsilon varepsilon(10)；big big big(9)；uniform normal displacement(9)；relations symmetric nodes(8)；prime prime prime(8)；thermal expansion coefficient(7)；plain woven composites(7)；displacement distribution rules(7)；plain woven composite(7)；satin woven composite(7)
- 被动语态估计：244
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：352
- 一般过去时线索：445
- 现在完成时线索：0
- 情态动词线索：140

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Therefore, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
  - 可迁移句型：{object}, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
### gap/转折句
- 原句：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell.
  - 可迁移句型：{object} expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell.
- 原句：6, the two black lines with arrow are the translation axes x and $y ,$ the blue lines are the reflection planes $P _ {x}$ and $P _ {y}$ (perpendicular to the paper), and the pink dot presents the rotation axis $L _ {z}$ As shown in Fig. $^ {6 ,}$ UC1 is formulated based on translational symmetries along xand y-axis, and then two reflectional symmetries about $P _ {x}$ and $P _ {y}$ planes can be observed in UC1 structure, and UC2 and UC3 will then be formulated based on them, respectively.
  - 可迁移句型：6, the two black lines with arrow are the translation axes x and $y ,$ the blue lines are the reflection planes ${object} _ {x}$ and $P _ {y}$ (perpendicular to the paper), and the pink dot presents the rotation axis $L _ {z}$ As shown in Fig. $^ {6 ,}$ UC1 is
- 原句：If UC4 has a configuration as depicted by black dashed lines (see UC4 in Fig.
  - 可迁移句型：{object} UC4 has a configuration as depicted by black dashed lines (see UC4 in Fig.
- 原句：However, the approach developed in this work can be used to predict CTEs of any other composites with certain structure symmetries.
  - 可迁移句型：{object}, the approach developed in This study can be used to predict CTEs of any other composites with certain structure symmetries.
### 方法提出句
- 原句：In this paper, a general approach is developed for the establishment of such a unit cell model.
  - 可迁移句型：{object} This study, a general approach is developed for the establishment of such a unit cell model.
- 原句：The application scope of present unit cell method is clarified from the thermal and mechanical point of views.
  - 可迁移句型：{object} application scope of present unit cell method is clarified from the thermal and mechanical point of views.
- 原句：The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
  - 可迁移句型：{object} influence of structure symmetries on the deformation pattern of unit cell models is clarified.
- 原句：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
  - 可迁移句型：{object} numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
### 结果证明句
- 原句：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
  - 可迁移句型：{object} numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
- 原句：The results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the FE method is more capable in capturing details like the local physical fields.
  - 可迁移句型：{object} results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; 
- 原句：To be general, the weave process is always used to create two-dimensional (2D) laminate structures, while the knitting process is good at manufacturing three-dimensional (3D) structure, and the braidi Fiber yarns can be considered as unidirectional (UD) fiber reinforced composites and the typical transverse fiber distribution pattern in matrix is shown in Fig.
  - 可迁移句型：{object} be general, the weave process is always used to create two-dimensional (2D) laminate structures, while the knitting process is good at manufacturing three-dimensional (3D) structure, and the braidi Fiber yarns can be considered as unidirectional (UD) 
- 原句：The left diagram of the figure shows a schematic of UD composite, the red circles indicate fibers and the blue background is the matrix.
  - 可迁移句型：{object} left diagram of the figure shows a schematic of UD composite, the red circles indicate fibers and the blue background is the matrix.
### 贡献收束句
- 原句：The model length in axial direction (z-) will not influence the calculation accuracy provided that appropriate BCs are imposed on, and thus a unit axial length h is specified for each model in this work.
  - 可迁移句型：{object} model length in axial direction (z-) will not influence the calculation accuracy provided that appropriate BCs are imposed on, and thus a unit axial length h is specified for each model in This study.
### 边界/谨慎句
- 原句：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell.
  - 可迁移句型：{object} expansion properties of textile reinforced composites with certain structure symmetries can be effi- ciently calculated by a size-limited unit cell.
- 原句：The temperature of certain location in highspeed aerospace vehicles may increase from room temperature to above 1000 °C in a short time of 600 s [1].
  - 可迁移句型：{object} temperature of certain location in highspeed aerospace vehicles may increase from room temperature to above 1000 °C in a short time of 600 s [1].
- 原句：Under this condition, the thermal expansion behaviors of relevant composites and structures should be carefully considered, since the mismatch of thermal expansion coefficient between different phases may lead to damages of the composite, and that between different composites may lead to final failures of the structure.
  - 可迁移句型：{object} this condition, the thermal expansion behaviors of relevant composites and structures should be carefully considered, since the mismatch of thermal expansion coefficient between different phases may lead to damages of the composite, and that between d
- 原句：Before its application, the corresponding behaviors and effective properties should be well understood primarily.
  - 可迁移句型：{object} its application, the corresponding behaviors and effective properties should be well understood primarily.

## 9. 引用风险层

- 正文引用簇估计：21
- 参考文献条数：43
- 可识别年份条目数：42
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：17
- 高频来源粗略识别：Compos Struct(5)；Int J Heat Mass Transf(2)；Comput Mater Sci(2)；Compos A Appl Sci Manuf(2)；Compos Sci Technol(2)；The Mori-Tanaka method applied to textile composite materials. Acta Mater(1)；Compos B Eng(1)；Finite element modeling of mechanical properties of(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Chen X, Liu L, Yue Z. Coupled analysis of aerodynamic heating, radiative heat transfer and heat conduction for hypersonic vehicles. 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference. American Institute of Aeronautics and Astronautics; 2015.
- 1. For a composite with symmetric structures, the effective coefficient of thermal expansion can be efficiently calculated by a unit cell model. Such unit cell should be formulated based on structure symmetries, and relevant BCs can be derived based on displacement distribution rules summarized in this work. Such unit cell models can also be used to predict the local stress distributions in fiber yarns or textile reinforced composites and thus has potentials for damage analysis of these composit
- [2] Gommers B, Verpoest I, Van Houtte P. The Mori-Tanaka method applied to textile composite materials. Acta Mater 1998;46(6):2223–35.
- [3] Mortazavi B, Baniassadi M, Bardon J, Ahzi S. Modeling of two-phase random composite materials by finite element, Mori-Tanaka and strong contrast methods. Compos B Eng 2013;45(1):1117–25.
- 3. For boundaries that can be formulated by reflectional symmetries, the uniform normal displacement and the uniform deformation can be obtained in thermal expansion calculations; for boundaries that can only be formulated based on translational or rotational sym- metries, the normal displacement and the relevant deformation are non-uniform. 2014;108:578–83.
- [4] Yang B. A distributed transfer function method for heat conduction problems in multilayer composites. Numer Heat Transf, Part B: Fundam 2008;54(4):314–37.
- [5] Li DS, Fang DN, Jiang N, Yao XF. Finite element modeling of mechanical properties of 3D five-directional rectangular braided composites. Compos Part B: Eng 2011;42(6):1373–85.
- [6] Fang GD, Liang J, Wang Y, Wang BL. The effect of yarn distortion on the mechanical properties of 3D four-directional braided composites. Compos A Appl Sci Manuf 2009;40(4):343–50.
- [7] Dong K, Peng X, Zhang J, Gu B, Sun B. Temperature-dependent thermal expansion behaviors of carbon fiber/epoxy plain woven composites: Experimental and nu- merical studies. Compos Struct 2017;176:329–41.
- [8] Zeng T, Wu LZ, Guo LC. Mechanical analysis of 3D braided composites: a finite element model. Compos Struct 2004;64(3–4):399–404.
- [9] Sun XK, Sun CJ. Mechanical properties of three-dimensional braided composites. Compos Struct 2004;65(3–4):485–92.
- [10] Zhang C, Xu XW. Finite element analysis of 3D braided composites based on three unit-cells models. Compos Struct 2013;98:130–42.
- [11] Zeng T, Wu LZ, Guo LC. A finite element model for failure analysis of 3D braided composites. Mater Sci Eng A-Struct Mater Prop Microstruct Process 2004;366(1):144–51.
- [12] Fang GD, Liang J, Wang BL. Progressive damage and nonlinear analysis of 3D four- directional braided composites under unidirectional tension. Compos Struct 2009;89(1):126–33.
- [13] Lu ZX, Wang CY, Xia B, Zhou Y. Effect of interfacial properties on the thermo- physical properties of 3D braided composites: 3D multiscale finite element study. Polym Compos 2013;35(9):1690–700.

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
