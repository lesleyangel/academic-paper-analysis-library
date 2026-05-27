# 论文深度拆解：047-Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal

> 生成依据：`801/cleantext/047-Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`047-Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.pdf`
- 页数：18
- clean body 字符数：56715
- 摘要字符数：1970
- 参考文献条数：35
- 图题数：25
- 表题数：6
- 表格文件数：11
- 公式候选数：140
- 提取质量分：0.99
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "24 formula(s) need manual review."}]

## 1. 身份层

- 标题：047-Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal
- 年份：2017
- 期刊/来源：Applied Thermal
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：To realize an applicable thermal management, the thermal characteristics of relevant composites need to be obtained firstly. Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost. Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
- 主要方法：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. In this paper, a general rule of such unit cell formulation is developed. Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
- 主要证据：图表 31 个标题、公式 140 个候选、参考文献 35 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“To realize an applicable thermal management, the thermal characteristics of relevant composites need to be obtained firstly. Such a model should contain adequate information of bot”，可以通过“Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. In this paper, a general rule of such unit cell formulation is develope”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and sum- marized as two equations, and can be used to derive boundary conditions of unit cells. An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view. Then, for more com- plex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary condi- tions are derived in a unified form, and the identical results obtained by multi-size unit cells validate the unit cell and the boundary conditions.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：To realize an applicable thermal management, the thermal characteristics of relevant composites need to be obtained firstly. Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost. Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
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
- 作者声明或文本中可见 gap：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. It contains enough microscopic structure information and the more notable appropriate boundary conditions (BCs) to get related to the macroscopic information that has been abandoned in the model establishment. On the other hand, for composites with ordered The formulation of unit cells and thermal BCs of several typical textile reinforced composites are studied in the author’s previous work [29,30], however, the general rules and concepts are not yet clarified.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. In this paper, a general rule of such unit cell formulation is developed. Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
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
| Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. | 摘要/引言/结论候选 | 图：Fig. 1. Formulation process of unit cells based on structure symmetries. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this paper, a general rule of such unit cell formulation is developed. | 摘要/引言/结论候选 | 图：Fig. 2. Translational symmetric structures. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure. | 摘要/引言/结论候选 | 图：Fig. 3. Temperature fields under different thermal stimuli. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and sum- marized as two equations, and can be used to derive boundary condi | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view. | 摘要/引言/结论候选 | 表：Table 3 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Then, for more com- plex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary condi- tions are derived in a unified | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (32.83, 217.37, 432.46, 231.03)]] Jian-Jun Gou a, Chun-L | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Formulation process of unit cells based on structure symmetries. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Translational symmetric structures. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Temperature fields under different thermal stimuli. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4. Physical meanings of symmetric and antisymmetric thermal stimuli. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Typical reflectional symmetric structures. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. Temperature fields in reflectional symmetric structures. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 7. Typical 180�rotational symmetric structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 8. Temperature fields in 180�rotational symmetric structures. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 9. Calculation model of UD composite and its boundary conditions. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 10. Effective axial thermal conductivities of UD composites. Fig. 11. DTD of symmetric nodes on boundary planes in x-direction. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Unit cells for transverse structure of UD composites. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 13. Boundary edges of unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Temperature fields calculated by four unit cells. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Satin weave textile and unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 18. Unit cell model of 4HS satin woven composite. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (32.83, 217.37, 432.46, 231.03)]] Jian-Jun Gou a, Chun-Lin Gong a, Liang-Xia | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.13, 702.06, 202.88, 720.0)]] ⇑Corresponding author. E-mail address: wqta | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 7, bbox (41.22, 190.43, 275.28, 205.45)]] parallel STS/Eq. (3) STS/Eq. (3) STS/Eq. (3) perpendicul | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 8, bbox (312.89, 541.65, 488.34, 552.34)]] qxjx¼0 ¼ �qxjx¼a ¼ q1; ðb �cÞ=26 y 6 ðb þ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 8, bbox (312.89, 580.88, 365.89, 591.29)]] q1=q2 ¼ 10 : 1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 8, bbox (312.89, 554.24, 537.83, 564.99)]] qxjx¼0 ¼ �qxjx¼a ¼ q2; 0 < y < ðb �cÞ=2 o | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 9, bbox (371.17, 733.78, 552.74, 752.69)]] L3; L4 : qðx1;0Þ ¼ qðx1;b=2Þ ¼ 0 ð11-1Þ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 10, bbox (106.75, 644.32, 221.55, 656.12)]] L4 : Tðx1;b=2Þ �Tð0;0Þ ¼ �brT0 y=2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. In this paper, a general rule of such unit cell formulation is developed. Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure. The route from the experiment specimen to the unit cell model, especially the evolution of relevant boundary conditions is clarified. The macro- scopic heat flux in experiments is defined as symmetric and antisymmetric thermal stimulus by its direc- tions. For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and sum- marized as two equations, and can be used to derive boundary conditions of unit cells. An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view. For the transverse direction of the composite, four unit cell models of reducing sizes are established, and the basic process of unit cell formulations and boundary conditions derivations is stated. Then, for more com- plex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary condi- tions are derived in a unified form, and the identical results obtained by multi-size unit cells validate the unit cell and the boundary conditions. The approach developed in this paper can be applied to thermal studies of any other composites with relevant structure symmetries. �2017 Elsevier Ltd. All rights reserved.

### 7.4 摘要中文翻译

> 具有对称结构的宏观复合材料的有效热性能可以通过尺寸有限的代表性晶胞来有效计算。在本文中，开发了这种晶胞公式的一般规则。其中涉及结构对称性识别和边界条件推导两个关键步骤，第一步建立几何模型，第二步赋予模型物理意义以表示原始结构。阐明了从实验样本到晶胞模型的路线，特别是相关边界条件的演变。实验中的宏观热通量被定义为其方向的对称和反对称热刺激。对于三种典型的平移、反射和180°旋转对称结构，不同宏观热刺激下的温度分布规律被揭示并概括为两个方程，可用于推导晶胞的边界条件。对单向纤维增强复合材料进行轴向研究，以从物理机制的角度证明导出的边界条件和不适当的边界条件之间的差异。对于复合材料的横向，建立了四种尺寸减小的晶胞模型，阐述了晶胞公式和边界条件推导的基本过程。然后，对于更复杂的缎纹编织复合材料，研究了4、5、6、7和8综织物中所示的结构对称性，制定了两个不同尺寸的晶胞并以统一的形式导出了相应的边界条件，并且通过多尺寸晶胞获得的相同结果验证了晶胞和边界条件。
> 
> 本文开发的方法可应用于具有相关结构对称性的任何其他复合材料的热研究。 �2017 爱思唯尔有限公司

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this paper, a general rule of unit cell formulation for thermal calculation of composites with symmetric structures is developed. The rule is based on the macroscopic experimental specimen and measurement conditions. The macroscopic heat flux in experiment is defined as symmetric thermal stimuli (STS) and antisymmetric thermal stimuli (ATS) by its directions for translational, reflectional and 180 rotational symmetric structures, respectively. The temperature distribution disciplines in different symmetric structures are described by corresponding equations and confirmed by typical calculations, and can be used to derive boundary conditions of unit cells. A case of axial study of unidirectional fiber reinforced composite is conducted to show the necessity of derived boundary conditions, and a transverse study is presented to introduce the basic process of unit cell formulations and boundary conditions derivation, and then for more complex $4 - , 5 - , 6 - , 7 -$ and 8-harness satin woven composites, two unit cells of different sizes are formulated, the corresponding boundary conditions are derived in a unified form, and the numerical models are validated by the identical results and also the experimental results available in reference. The approach developed in this paper can be referenced by thermal calculations of any other composites with symmetric structures. It can be concluded that:
> 
> 1. Effective thermal properties of composites with symmetric structures can be efficiently calculated by a unit cell model, which should be formulated based on the symmetries indicated in the structures, and the corresponding boundary conditions should be derived based on temperature distribution disciplines clarified in this work.
> 
> 2. The basic process of the formulation of a unit cell has four steps: the identification of structure symmetries, the establishment of geometric configuration, the determination of $q ^ {0}$ direction and the derivation of boundary conditions.
> 
> 3. Each utilization of symmetries can create a new unit cell with smaller size, and new boundary conditions should be derived strictly since inappropriate boundary conditions will affect the calculation accuracy.
> 
> 4. For the studied satin woven composites, the in-plane thermal conductivity increases, while the out-plane one decreases very slightly with the increasing harness of composites.

### 7.6 结论中文翻译

> 本文提出了用于对称结构复合材料热计算的晶胞公式的一般规则。该规则基于宏观实验样本和测量条件。实验中的宏观热通量根据平移、反射和180°旋转对称结构的方向分别定义为对称热刺激（STS）和反对称热刺激（ATS）。不同对称结构中的温度分布规律由相应的方程描述并通过典型计算得到证实，可用于推导晶胞的边界条件。以单向纤维增强复合材料的轴向研究为例，说明导出边界条件的必要性；通过横向研究，介绍晶胞公式化和边界条件推导的基本过程，然后对于更复杂的4-、5-、6-、7-、8线缎纹编织复合材料，制定两个不同尺寸的晶胞，以统一的形式导出相应的边界条件，并通过相同的结果和公式对数值模型进行验证。实验结果可供参考。本文开发的方法可以被任何其他具有对称结构的复合材料的热计算所参考。可以得出以下结论： 1. 具有对称结构的复合材料的有效热性能可以通过晶胞模型有效计算，该模型应根据结构中指示的对称性进行制定，并应根据本文阐明的温度分布规律推导相应的边界条件。
> 
> 晶胞表述的基本过程有四个步骤：结构对称性的识别、几何构型的建立、$q^{0}$方向的确定和边界条件的推导。每次利用对称性都会产生一个尺寸更小的新晶胞，并且必须严格推导新的边界条件，因为不合适的边界条件会影响计算精度。对于所研究的缎纹编织复合材料，随着复合材料硬度的增加，面内导热率增加，而面外导热率则略有下降。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7985 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Unit cell formulation rules in thermal calculations | 方法建构 | 1146 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Unit cells and thermal boundary conditions | 对象/条件/子问题展开 | 5064 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Temperature disciplines in translational symmetric structures | 对象/条件/子问题展开 | 2172 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Temperature disciplines in reflectional and 180 rotational symmetric structures | 对象/条件/子问题展开 | 495 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 2.3.1. Two thermal stimuli definition | 对象/条件/子问题展开 | 4199 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 2.3.2. Temperature distribution disciplines in reflectional structures | 对象/条件/子问题展开 | 1361 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 2.3.3. Temperature distribution disciplines in 180 rotational structures | 对象/条件/子问题展开 | 2838 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.1. Unit cell and boundary conditions | 对象/条件/子问题展开 | 4158 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.2. Axial effective thermal conductivities | 对象/条件/子问题展开 | 4333 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4. Study of typical composites with symmetric structures | 对象/条件/子问题展开 | 715 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.1.1. Unit cells and boundary conditions | 对象/条件/子问题展开 | 5388 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1.2. Temperature fields and effective thermal conductivities | 对象/条件/子问题展开 | 1999 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.2.1. Unit cells formulation | 方法建构 | 4589 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 4.2.2. Coordinate systems | 对象/条件/子问题展开 | 1097 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.2.3. Boundary conditions | 对象/条件/子问题展开 | 1619 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 4.2.4. Temperature fields and effective thermal conductivities | 对象/条件/子问题展开 | 4070 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 5. Conclusions | 主张回收/边界说明 | 2390 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：unit(86)；thermal(75)；symmetric(64)；temperature(56)；boundary(55)；structure(53)；bcs(51)；structures(51)；composites(47)；cell(45)；composite(42)；respectively(42)；fig(41)；fiber(39)；symmetries(38)；cells(38)；macroscopic(36)；heat(36)；two(35)；prime(35)
- 高频学术名词/术语：temperature(56)；structure(53)；direction(31)；distribution(22)；section(22)；conductivity(20)；calculation(15)；derivation(15)；reflection(12)；figure(12)；rotation(10)；equation(10)；translation(9)；formulation(8)；condition(7)
- 高频学术动词：derived(23)；obtained(12)；indicated(9)；compared(8)；presented(7)；developed(6)；obtain(5)；derive(4)；investigated(4)；revealed(3)；demonstrated(3)；demonstrate(3)；validated(2)；indicate(2)；validate(1)
- 高频形容词：thermal(75)；symmetric(64)；boundary(55)；macroscopic(36)；translational(29)；rotational(27)；effective(25)；reflectional(24)；axial(15)；numerical(14)；typical(14)；relative(12)；specific(11)；table(11)；periodic(10)
- 高频副词：respectively(42)；widely(4)；certainly(3)；finally(2)；clearly(2)；separately(2)；strictly(2)；slightly(2)；obviously(1)；firstly(1)；entirely(1)；nearly(1)
- 高频二词短语：unit cell(43)；unit cells(38)；heat flux(31)；symmetric structures(26)；boundary conditions(23)；thermal conductivity(20)；macroscopic heat(19)；effective thermal(16)；lambda lambda(16)；symmetric nodes(16)；thermal conductivities(15)；fig shows(15)；sts ats(15)；reflectional rotational(14)；satin woven(14)
- 高频三词短语：macroscopic heat flux(18)；end array tag(11)；effective thermal conductivities(10)；satin woven composites(10)；sts ats equations(9)；formulated translational symmetries(7)；lambda lambda lambda(7)；temperature distribution disciplines(7)；unidirectional fiber reinforced(6)；reflectional rotational symmetries(6)；unit cells formulated(6)；rotational symmetric structures(6)
- 被动语态估计：206
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：351
- 一般过去时线索：407
- 现在完成时线索：0
- 情态动词线索：98

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
  - 可迁移句型：{object}, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
### gap/转折句
- 原句：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  - 可迁移句型：{object} thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句：For such composites, the reproduce of the real random multiphase microstructure is the first challenge in RVE model establishment.
  - 可迁移句型：{object} such composites, the reproduce of the real random multiphase microstructure is the first challenge in RVE model establishment.
- 原句：On the other hand, for composites with ordered The formulation of unit cells and thermal BCs of several typical textile reinforced composites are studied in the author’s previous work [29,30], however, the general rules and concepts are not yet clarified.
  - 可迁移句型：{object} the other hand, for composites with ordered The formulation of unit cells and thermal BCs of several typical textile reinforced composites are studied in the author’s previous work [29,30], however, the general rules and concepts are not yet clarified
- 原句：Among all the woven composites, the satin one has glossier surface and is more flexible due to its less interlacing points of weft and warp yarns, however, the specialized study of its unit cells is very limited.
  - 可迁移句型：{object} all the woven composites, the satin one has glossier surface and is more flexible due to its less interlacing points of weft and warp yarns, however, the specialized study of its unit cells is very limited.
### 方法提出句
- 原句：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  - 可迁移句型：{object} thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句：In this paper, a general rule of such unit cell formulation is developed.
  - 可迁移句型：{object} This study, a general rule of such unit cell formulation is developed.
- 原句：Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
  - 可迁移句型：{object} key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
- 原句：The route from the experiment specimen to the unit cell model, especially the evolution of relevant boundary conditions is clarified.
  - 可迁移句型：{object} route from the experiment specimen to the unit cell model, especially the evolution of relevant boundary conditions is clarified.
### 结果证明句
- 原句：For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and sum- marized as two equations, and can be used to derive boundary conditions of unit cells.
  - 可迁移句型：{object} three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and sum- marized as two equations, and can be used to derive boundary 
- 原句：An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
  - 可迁移句型：{object} axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
- 原句：Then, for more com- plex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary condi- tions are derived in a unified form, and the identical results obtained by multi-size unit cells validate the unit cell and the boundary conditions.
  - 可迁移句型：{object}, for more com- plex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary condi- tions are derived in a uni
- 原句：15 shows the textile structures (left) and unit cells (right) for each harness textile, and the matrix is not shown to display the yarn orientation clearly.
  - 可迁移句型：15 shows the textile structures (left) and unit cells (right) for each harness textile, and the matrix is not shown to display the yarn orientation clearly.
### 贡献收束句
- 未稳定识别，需从对应章节人工补充。
### 边界/谨慎句
- 原句：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  - 可迁移句型：{object} thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句：Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost.
  - 可迁移句型：{object} a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost.
- 原句：Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
  - 可迁移句型：{object}, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
- 原句：The reconstructed model is assumed to be representative enough if it has effective structure parameters, i.e. satisfy certain deviation standard, compared with the real composites.
  - 可迁移句型：{object} reconstructed model is assumed to be representative enough if it has effective structure parameters, i.e. satisfy certain deviation standard, compared with the real composites.

## 9. 引用风险层

- 正文引用簇估计：19
- 参考文献条数：35
- 可识别年份条目数：33
- 2021 年及以后参考文献数：0
- 2010 年以前经典文献数：14
- 高频来源粗略识别：J. Heat Mass Transf(8)；Struct(6)；Therm. Eng(3)；Sci. and Technol(1)；J. Therm. Sci(1)；Comput. Phys(1)；J. Solids Struct(1)；Mater. Res(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- 1. Effective thermal properties of composites with symmetric structures can be efficiently calculated by a unit cell model, which should be formulated based on the symmetries indicated in the structures, and the corresponding boundary conditions should be derived based on temperature distribution disciplines clarified in this work.
- [2] J. Xie, J. Liang, G. Fang, Z. Chen, Effect of needling parameters on the effective properties of 3D needled C/C-SiC composites, Compos. Sci. and Technol. 117 (2015) 69–77.
- [3] W.Z. Fang, J.J. Gou, H. Zhang, Q. Kang, W.Q. Tao, Numerical predictions of the effective thermal conductivity for needled C/C-SiC composite materials, Numer. Heat Transf. Part A: Appl. 70 (10) (2016) 1101–1117.
- 3. Each utilization of symmetries can create a new unit cell with smaller size, and new boundary conditions should be derived strictly since inappropriate boundary conditions will affect the calculation accuracy.
- [4] L. Chen, H.-B. Luan, Y.-L. He, W.-Q. Tao, Pore-scale flow and mass transport in gas diffusion layer of proton exchange membrane fuel cell with interdigitated flow fields, Int. J. Therm. Sci. 51 (2012) 132–144.
- 4. For the studied satin woven composites, the in-plane thermal conductivity increases, while the out-plane one decreases very slightly with the increasing harness of composites.
- [5] X. He, Y. Guo, M. Li, N. Pan, M. Wang, Effective gas diffusion coefficient in fibrous materials by mesoscopic modeling, Int. J. Heat Mass Transf. 107 (2017) 736–746.
- [6] M. Wang, N. Pan, Modeling and prediction of the effective thermal conductivity of random open-cell porous foams, Int. J. Heat Mass Transf. 51 (5–6) (2008) 1325–1331.
- [7] P. Ranut, On the effective thermal conductivity of aluminum metal foams: review and improvement of the available empirical and analytical models, Appl. Therm. Eng. 101 (2016) 496–524.
- [8] J. Su, X. Liu, M. Charmchi, H. Sun, Experimental and numerical study of anisotropic thermal conductivity of magnetically aligned PDMS/Ni particle composites, Int. J. Heat Mass Transf. 97 (2016) 645–652.
- [9] M. Wang, N. Pan, Predictions of effective physical properties of complex multiphase materials, Mater. Sci. Eng. R: Rep. 63 (1) (2008) 1–30.
- [10] M. Wang, Q. Kang, N. Pan, Thermal conductivity enhancement of carbon fiber composites, Appl. Therm. Eng. 29 (2–3) (2009) 418–421.
- [11] M. Wang, N. Pan, Elastic property of multiphase composites with random microstructures, J. Comput. Phys. 228 (16) (2009) 5978–5988.
- [12] B. Yang, A Distributed Transfer Function Method for Heat Conduction Problems in Multilayer Composites, Numer. Heat Transf. Part B: Fundam. 54 (4) (2008) 314–337.

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
