# 论文深度拆解：Appropriate utilization of the unit cell method in thermal calculation of composites

> 生成依据：`801/cleantext/027-Appropriate-utilization-of-the-unit-cell-method-in-th_2018_Applied-Thermal-E`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`027-Appropriate-utilization-of-the-unit-cell-method-in-th_2018_Applied-Thermal-E`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Appropriate-utilization-of-the-unit-cell-method-in-th_2018_Applied-Thermal-E.pdf`
- 页数：12
- clean body 字符数：40542
- 摘要字符数：1216
- 参考文献条数：36
- 图题数：11
- 表题数：3
- 表格文件数：8
- 公式候选数：198
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "15 formula(s) need manual review."}]

## 1. 身份层

- 标题：Appropriate utilization of the unit cell method in thermal calculation of composites
- 年份：2018
- 期刊/来源：Applied Thermal E
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：For composites with random phase distributions such as needled composites (randomly distributed short fibers) [3,4], fiber layers in proton exchange membrane fuel cell (randomly distributed short fibers and pores) [5–8], porous materials (random pores) [9–11], granular composite (random reinforcing granula) [12] and thermal barrier coatings (random pores) [13,14], the RVE is formulated based on statistical parameters (e.g., phase volume fraction) of the composite structure. Each UC needs corresp
- 主要方法：The unit cell method is widely used in thermal calculations of composite. In this work, two issues are studied to further appropriate utilization of such method. The effective thermal properties of composites can be efficiently calculated by a representative volume element (RVE) model.
- 主要证据：图表 14 个标题、公式 198 个候选、参考文献 36 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“For composites with random phase distributions such as needled composites (randomly distributed short fibers) [3,4], fiber layers in proton exchange membrane fuel cell (randomly di”，可以通过“The unit cell method is widely used in thermal calculations of composite. In this work, two issues are studied to further appropriate utilization of such method. The effective thermal properties of composites can be effi”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The translational symmetry is always used to formulate a full UC first, and the other two symmetries can then be used to reduce the UC size. In the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symmetries will reduce the UC size while lead to more complicated BC. 1–3 show different paths from composite to unit cells for UD, plain woven and 3D4d braided composite, respectively.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：For composites with random phase distributions such as needled composites (randomly distributed short fibers) [3,4], fiber layers in proton exchange membrane fuel cell (randomly distributed short fibers and pores) [5–8], porous materials (random pores) [9–11], granular composite (random reinforcing granula) [12] and thermal barrier coatings (random pores) [13,14], the RVE is formulated based on statistical parameters (e.g., phase volume fraction) of the composite structure. Each UC needs corresponding boundary condition (BC) to represent the macro structure. At present, the complex coupling relation between these four factors needs further studies, mainly in two aspects.
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
- 作者声明或文本中可见 gap：For another type of composite with certain geometric symmetries such as textile reinforced composites [15–26] and idealized foam materials [27–30], the RVE can be formulated based on structure symmetries. Compare with the RVE of randomly structured composites, a UC model for symmetrically structured composites can be theoretically accurate in representing the macro composite; however, the formulation of an accurate UC is relatively complicated. First, in previous literatures, the utilization of different combination of symmetries (expressed as UC formulation path in this work) means different configurations and different BC of the UC; however, sometimes different symmetries may formulate the same geometric configuration and meanwhile the derived BC are still different; this brings about some confusions in simulations and needs to be clarified.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Second, the typical uniform temperature BC (UBC) is very easy to apply, good for convergence, and thus preferred by many simulations; however, sometimes it is used without rigorous mathematical derivations or physical considerations because the researchers pay more attention on other issues [24,35,36]; in this paper the application scope of UBC will be determined and the authors hope it could be a good supplement to those previous works.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：The unit cell method is widely used in thermal calculations of composite. In this work, two issues are studied to further appropriate utilization of such method. The effective thermal properties of composites can be efficiently calculated by a representative volume element (RVE) model.
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
| The effective thermal properties of composites can be efficiently calculated by a representative volume element (RVE) model. | 摘要/引言/结论候选 | 图：Fig. 1. Paths from UD composite to unit cells. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Each UC needs corresponding boundary condition (BC) to represent the macro structure. | 摘要/引言/结论候选 | 图：Fig. 2. Paths from plain woven composite to unit cells. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symmetries | 摘要/引言/结论候选 | 图：Fig. 3. Paths from 3D four-directional braided composite to unit cells. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Compare with the RVE of randomly structured composites, a UC model for symmetrically structured composites can be theoretically accurate in representing the macro composite; however, the formulation of an accurate UC is relatively complicated. | 摘要/引言/结论候选 | 表：Table 4 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| At present, the complex coupling relation between these four factors needs further studies, mainly in two aspects. | 摘要/引言/结论候选 | 表：Table 5 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| It should be noted that these three types of composites are studied because: first, UD composite is relevant to all textile reinforced composites since the textile fiber yarn is a sort of UD composite; second, the plain woven composite is a typical 2D woven co | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 686.56, 184.45, 704.34)]] ⁎ Corresponding author | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Paths from UD composite to unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Paths from plain woven composite to unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Paths from 3D four-directional braided composite to unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Unit cell models for three types of composites. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. Boundaries of the unit cell. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Meshed models. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. Temperature fields of UD composites. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Temperature fields of plain woven composites. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Further structure symmetries in plain woven composites. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 10. Temperature fields of 3D four-directional braided composites. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 11. Further structure symmetries in 3D four-directional braided composites. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 686.56, 184.45, 704.34)]] ⁎ Corresponding author. E-mail address: jj | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (37.29, 688.09, 288.65, 699.63)]] = -∇ = q T i x y z λ , , , i i 000 (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (306.29, 475.3, 557.66, 484.43)]] - = - ′ ′ T T T T STS: M O M O (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (306.54, 492.53, 557.66, 501.66)]] - = - ′ ′ T T T T ATS: M O O M (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 5, bbox (312.6, 641.77, 520.68, 657.12)]] P5 Symmetries Transl. (z) + refl. (⊥z) Tra | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 5, bbox (312.6, 671.93, 520.68, 687.22)]] P6 Symmetries Transl. (z) + refl. (⊥z) Tra | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (314.97, 59.74, 413.51, 67.72)]] - - = ∇ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (314.73, 73.18, 413.42, 81.16)]] - - = ∇ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The unit cell method is widely used in thermal calculations of composite. The formulation of a unit cell involves construction of geometric configuration and derivation of boundary conditions. The process is closely related to the structure symmetries of composites and the macro heat flux. In this work, two issues are studied to further appropriate utilization of such method. First, unit cells that formulated based on different paths with different structure symmetries could have the same configuration while different boundary conditions, and leads to some confusions; second, the uniform temperature boundary condition is frequently used without rigorous mathe- matical derivation and physical consideration, and leaves some uncertainty of its reliability. In this work, three typical composites, unidirectional fiber reinforced, plain woven and three-dimensional four-directional braided composites are studied. For each composite, one unit cell is formulated and two types of boundary conditions are derived. The influence of formulation path on unit cell formulation and the application scope of uniform tem- perature boundary conditions are then clarified based on corresponding calculations and analysis.

### 7.4 摘要中文翻译

> 晶胞法广泛应用于复合材料的热计算。晶胞的制定涉及几何构型的构造和边界条件的推导。该过程与复合材料的结构对称性和宏观热通量密切相关。在这项工作中，研究了两个问题以进一步适当利用这种方法。首先，基于具有不同结构对称性的不同路径形成的晶胞可能在不同的边界条件下具有相同的配置，并导致一些混乱；其次，经常使用均匀温度边界条件，而没有经过严格的数学推导和物理考虑，导致其可靠性存在一定的不确定性。在这项工作中，研究了三种典型的复合材料：单向纤维增强、平纹编织和三维四向编织复合材料。对于每种复合材料，都会制定一个晶胞并导出两种类型的边界条件。通过相应的计算分析，明确了配方路径对晶胞配方的影响以及均匀温度边界条件的应用范围。

### 7.5 结论完整摘录

识别到的结论位置：7. Conclusions

> In this work, the utilization of unit cell method in thermal calculation of composites is studied and two issues, i.e., the confusion of one unit cell configuration with different boundary conditions and the application scope of uniform temperature boundary condition are clarified. Three types of composites, unidirectional fiber reinforced, plain woven and three-dimensional four-directional braided composites are studied. For each composite, one unit cell is formulated, and two types of boundary conditions are derived based on two different formulation paths: Path a of translational symmetries, and Path b of combinations of translational with reflectional or rotational symmetries. The numerical results show some conclusions:
> 
> 1. A unit cell can be formulated by different paths and can have different boundary conditions, whereas the numerical results are unique. For such a unit cell, the specific formulation path is not concerned provided that the boundary condition is derived rigorously. Thus, one can choose a formulation path and derive corresponding boundary conditions that appropriate for his own work.
> 
> 2. For unit cells and boundaries that can be formulated by reflectional symmetries, the widely used uniform temperature boundary condition (UBC) is correct, while for unit cells that can only be formulated by translational symmetries or $180 ^{\circ}$ rotational ones, it is inappropriate. For UD composites, UBC is correct for thermal calculations in all directions; for plain woven composites, it is correct in x- and y-direction while inappropriate in z-direction; for three-dimensional four-directional braided composites, it is inappropriate for all directional thermal calculations. For some problems, the UBC can be a good and easy approximation since the temperature nonuniformity could be relatively small, however, it is essential to evaluate possible errors first.
> 
> 3. The calculated temperature fields on boundary planes always indicate further structure symmetries that can be used to formulate unit cells with smaller size.
> 
> $P _ {1} \sim P _ {6} {:}$ : Transl. $\mathbf {+ 180} ^{\circ}$ Rot. 
> (a) ${\{q _ {x}} ^ {0} \}$
> 
> $$P _ {1} \sim P _ {6} \mathrm {{:}}$$

### 7.6 结论中文翻译

> 本文对晶胞法在复合材料热计算中的应用进行了研究，阐明了不同边界条件下晶胞构型的混淆和均匀温度边界条件的应用范围两个问题。研究了单向纤维增强复合材料、平纹编织复合材料和三维四向编织复合材料三种类型的复合材料。对于每种复合材料，都会制定一个晶胞，并根据两种不同的制定路径导出两种类型的边界条件：平移对称性的路径 a 以及平移与反射或旋转对称性组合的路径 b。数值结果显示了一些结论： 1. 晶胞可以通过不同的路径来表示，并且可以具有不同的边界条件，而数值结果是唯一的。对于这样的晶胞，只要严格推导边界条件，就不需要关心具体的公式路径。因此，人们可以选择一条表述路径并导出适合自己工作的相应边界条件。对于可以用反射对称性表示的晶胞和边界，广泛使用的均匀温度边界条件（UBC）是正确的，而对于只能用平移对称性或$180 ^{\circ}$旋转对称性表示的晶胞来说，它是不合适的。对于 UD 复合材料，UBC 对于各个方向的热计算都是正确的；对于平纹编织复合材料，x、y 方向正确，z 方向不合适；对于三维四向编织复合材料，不适合全方向热计算。
> 
> 对于某些问题，UBC 可以是一个良好且简单的近似值，因为温度不均匀性可能相对较小，但是，必须首先评估可能的误差。边界面上计算的温度场总是表明进一步的结构对称性，可用于制定更小尺寸的晶胞。 $P _ {1} \sim P _ {6} {:}$ : 翻译。 $\mathbf {+ 180} ^{\circ}$ 旋转。 (a) ${\{q _ {x}} ^ {0} \}$ $$P _ {1} \sim P _ {6} \mathrm {{:}}$$

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 4376 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Constitutive equations | 对象/条件/子问题展开 | 788 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3. Two formulation paths of the unit cell | 方法建构 | 1331 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. UD composite | 对象/条件/子问题展开 | 1705 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.2. Plain woven composite | 对象/条件/子问题展开 | 652 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.3. Three-dimensional four-directional braided composite | 对象/条件/子问题展开 | 736 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | Three formulation paths | 方法建构 | 523 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.4. Path summary and unit cell models | 方法建构 | 1913 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.1. Macro thermal stimuli | 对象/条件/子问题展开 | 3129 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.2. Boundary conditions from Path a | 对象/条件/子问题展开 | 3374 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.3. Boundary conditions from Path b | 对象/条件/子问题展开 | 11084 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 5. Model discretization | 方法建构 | 802 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 13 | 6.1. UD composites | 对象/条件/子问题展开 | 1008 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 6.2. Plain woven composites | 对象/条件/子问题展开 | 1600 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 6.3. 3D four-directional braided composites | 对象/条件/子问题展开 | 3166 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 6.4. Summary | 对象/条件/子问题展开 | 1483 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 7. Conclusions | 主张回收/边界说明 | 2199 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：symmetries(62)；boundary(59)；composites(53)；nabla(49)；planes(42)；composite(41)；path(40)；temperature(34)；woven(32)；fig(32)；mathrm(31)；formulation(30)；unit(29)；translational(29)；plain(29)；braided(28)；reflectional(26)；structure(25)；paths(25)；symmetric(23)
- 高频学术名词/术语：temperature(34)；formulation(30)；structure(25)；direction(20)；reflection(11)；rotation(10)；calculation(9)；derivation(8)；z-direction(8)；condition(7)；y-direction(6)；translation(5)；configuration(5)；combination(5)；situation(4)
- 高频学术动词：derived(23)；indicated(9)；derive(8)；obtained(4)；compared(3)；compare(2)；obtain(2)；investigated(2)；indicate(2)；evaluate(2)
- 高频形容词：boundary(59)；translational(29)；reflectional(26)；symmetric(23)；periodic(20)；thermal(17)；rotational(17)；table(14)；axial(11)；specific(9)；relevant(8)；derive(8)；four-directional(7)；numerical(7)；gradient(6)
- 高频副词：respectively(22)；separately(5)；mainly(4)；totally(4)；rigorously(4)；randomly(3)；relatively(3)；closely(3)；apply(3)；directly(2)；finally(2)；imply(2)
- 高频二词短语：boundary planes(30)；plain woven(29)；braided composites(21)；translational symmetries(17)；boundary conditions(17)；colon nabla(16)；unit cells(15)；heat flux(15)；unit cell(14)；macro heat(13)；structure symmetries(12)；rotational symmetries(12)；formulation path(12)；formulation paths(12)；woven composite(12)
- 高频三词短语：macro heat flux(12)；plain woven composite(11)；nabla colon nabla(11)；nabla mathfrak nabla(11)；mathfrak nabla mathfrak(11)；plain woven braided(8)；woven braided composites(8)；mathrm mathrm mathrm(8)；colon nabla colon(7)；four-directional braided composites(6)；reflectional rotational symmetries(6)；path translational symmetries(6)
- 被动语态估计：127
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：186
- 一般过去时线索：254
- 现在完成时线索：0
- 情态动词线索：96

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：For some problems, the UBC can be a good and easy approximation since the temperature nonuniformity could be relatively small, however, it is essential to evaluate possible errors first.
  - 可迁移句型：{object} some problems, the UBC can be a good and easy approximation since the temperature nonuniformity could be relatively small, however, it is essential to evaluate possible errors first.
### gap/转折句
- 原句：Compare with the RVE of randomly structured composites, a UC model for symmetrically structured composites can be theoretically accurate in representing the macro composite; however, the formulation of an accurate UC is relatively complicated.
  - 可迁移句型：{object} with the RVE of randomly structured composites, a UC model for symmetrically structured composites can be theoretically accurate in representing the macro composite; however, the formulation of an accurate UC is relatively complicated.
- 原句：First, in previous literatures, the utilization of different combination of symmetries (expressed as UC formulation path in this work) means different configurations and different BC of the UC; however, sometimes different symmetries may formulate the same geometric configuration and meanwhile the derived BC are still different; this brings about some confusions in simulations and needs to be clarified.
  - 可迁移句型：{object}, in previous literatures, the utilization of different combination of symmetries (expressed as UC formulation path in This study) means different configurations and different BC of the UC; however, sometimes different symmetries may formulate the same
- 原句：However, sometimes different formulation paths will build up the same UC configuration.
  - 可迁移句型：{object}, sometimes different formulation paths will build up the same UC configuration.
- 原句：For some problems, the UBC can be a good and easy approximation since the temperature nonuniformity could be relatively small, however, it is essential to evaluate possible errors first.
  - 可迁移句型：{object} some problems, the UBC can be a good and easy approximation since the temperature nonuniformity could be relatively small, however, it is essential to evaluate possible errors first.
### 方法提出句
- 原句：The unit cell method is widely used in thermal calculations of composite.
  - 可迁移句型：{object} unit cell method is widely used in thermal calculations of composite.
- 原句：In this work, two issues are studied to further appropriate utilization of such method.
  - 可迁移句型：{object} This study, two issues are studied to further appropriate utilization of such method.
- 原句：The effective thermal properties of composites can be efficiently calculated by a representative volume element (RVE) model.
  - 可迁移句型：{object} effective thermal properties of composites can be efficiently calculated by a representative volume element (RVE) model.
- 原句：Due to the structure stochasticity, such RVE is an approximate rather than accurate model.
  - 可迁移句型：{object} to the structure stochasticity, such RVE is an approximate rather than accurate model.
### 结果证明句
- 原句：In the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symmetries will reduce the UC size while lead to more complicated BC.
  - 可迁移句型：{object} the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symm
- 原句：1–3 show different paths from composite to unit cells for UD, plain woven and 3D4d braided composite, respectively.
  - 可迁移句型：1–3 show different paths from composite to unit cells for {object}, plain woven and 3D4d braided composite, respectively.
- 原句：(z: 4h) formulate UC1 based on some 180° rotational symmetries indicated in UC2 structure, and UC2 can also be formulated based on that of UC1.
  - 可迁移句型：(z: 4h) formulate UC1 based on some 180° rotational symmetries indicated in UC2 structure, and UC2 can also be formulated based on that of UC1.
- 原句：The numerical results show some conclusions: 1.
  - 可迁移句型：{object} numerical results show some conclusions: 1.
### 贡献收束句
- 原句：The translational symmetry is always used to formulate a full UC first, and the other two symmetries can then be used to reduce the UC size.
  - 可迁移句型：{object} translational symmetry is always used to formulate a full UC first, and the other two symmetries can then be used to reduce the UC size.
- 原句：In the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symmetries will reduce the UC size while lead to more complicated BC.
  - 可迁移句型：{object} the authors’ works about plain woven [20], satin woven [32,33], threedimensional four-directional braided (3D4d) [34] composites, the reflectional and 180° rotational symmetries are used to formulate unit cells, and the results show that such two symm
- 原句：For such a unit cell, the specific formulation path is not concerned provided that the boundary condition is derived rigorously.
  - 可迁移句型：{object} such a unit cell, the specific formulation path is not concerned provided that the boundary condition is derived rigorously.
### 边界/谨慎句
- 原句：First, unit cells that formulated based on different paths with different structure symmetries could have the same configuration while different boundary conditions, and leads to some confusions; second, the uniform temperature boundary condition is frequently used without rigorous mathe- matical derivation and physical consideration, and leaves some uncertainty of its reliability.
  - 可迁移句型：{object}, unit cells that formulated based on different paths with different structure symmetries could have the same configuration while different boundary conditions, and leads to some confusions; second, the uniform temperature boundary condition is frequen
- 原句：For a high-speed vehicle like hypersonic one, the surface temperature may reach a value of 1600 °C or even higher [1,2] in a very short time of hundreds of seconds.
  - 可迁移句型：{object} a high-speed vehicle like hypersonic one, the surface temperature may reach a value of 1600 °C or even higher [1,2] in a very short time of hundreds of seconds.
- 原句：Under this condition, a reliable and efficient thermal protection system (TPS) is required, and the thermal characteristics of relevant TPS composites should be deeply studied.
  - 可迁移句型：{object} this condition, a reliable and efficient thermal protection system (TPS) is required, and the thermal characteristics of relevant TPS composites should be deeply studied.
- 原句：The derivation of BC should be based on rigorous mathematical and thermo-physical considerations [32].
  - 可迁移句型：{object} derivation of BC should be based on rigorous mathematical and thermo-physical considerations [32].

## 9. 引用风险层

- 正文引用簇估计：13
- 参考文献条数：36
- 可识别年份条目数：37
- 2021 年及以后参考文献数：1
- 2010 年以前经典文献数：7
- 高频来源粗略识别：Therm. Eng(8)；J. Heat Mass Transf(8)；Struct(7)；Sci. Technol(2)；J. Therm. Sci(2)；Mater. Res. Technol(1)；Royal Soc. a-Math. Phys. Eng. Sci(1)；J. Heat Fluid Flow(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [2] T. Ji, R. Zhang, B. Sunden, G. Xie, Investigation on thermal performance of high temperature multilayer insulations for hypersonic vehicles under aerodynamic heating condition, Appl. Therm. Eng. 70 (1) (2014) 957–965.
- [3] J. Xie, J. Liang, G. Fang, Z. Chen, Effect of needling parameters on the effective properties of 3D needled C/C-SiC composites, Compos. Sci. Technol. 117 (2015) 69–77.
- [4] W.Z. Fang, J.J. Gou, H. Zhang, Q. Kang, W.Q. Tao, Numerical predictions of the effective thermal conductivity for needled C/C-SiC composite materials, Numerical Heat Transfer, Part A: Appl. 70 (10) (2016) 1101–1117.
- [5] L. Chen, H.B. Luan, Y.L. He, W.Q. Tao, Pore-scale flow and mass transport in gas diffusion layer of proton exchange membrane fuel cell with interdigitated flow fields, Int. J. Therm. Sci. 51 (2012) 132–144.
- [6] X. He, Y. Guo, M. Li, N. Pan, M. Wang, Effective gas diffusion coefficient in fibrous materials by mesoscopic modeling, Int. J. Heat Mass Transf. 107 (2017) 736–746.
- [7] M. Wang, Q. Kang, N. Pan, Thermal conductivity enhancement of carbon fiber composites, Appl. Therm. Eng. 29 (2–3) (2009) 418–421.
- [8] X. Huang, Q. Zhou, J. Liu, Y. Zhao, W. Zhou, D. Deng, 3D stochastic modeling, simulation and analysis of effective thermal conductivity in fibrous media, Powder Technol. 320 (Supplement C) (2017) 397–404.
- [9] M. Wang, N. Pan, Modeling and prediction of the effective thermal conductivity of random open-cell porous foams, Int. J. Heat Mass Transf. 51 (5–6) (2008) 1325–1331.
- [10] P. Ranut, On the effective thermal conductivity of aluminum metal foams: review and improvement of the available empirical and analytical models, Appl. Therm. Eng. 101 (2016) 496–524.
- [11] H. Liu, X. Xia, X. Xie, Q. Ai, D. Li, Experiment and identification of thermal con- ductivity and extinction coefficient of silica aerogel composite, Int. J. Therm. Sci. 121 (Supplement C) (2017) 192–203.
- [12] J. Su, X. Liu, M. Charmchi, H. Sun, Experimental and numerical study of anisotropic thermal conductivity of magnetically aligned PDMS/Ni particle composites, Int. J. Heat Mass Transf. 97 (2016) 645–652.
- [13] Y. Wang, H. Liu, X. Ling, Y. Weng, Effects of pore microstructure on the effective thermal conductivity of thermal barrier coatings, Appl. Therm. Eng. 102 (Supplement C) (2016) 234–242.
- [14] M. Moayeri, A. Kaflou, Effect of powder shape on effective thermal conductivity of Cu–Ni porous coatings, J. Mater. Res. Technol. (2017).
- [15] R.P.A. Rocha, M.A.E. Cruz, Computation of the effective conductivity of unidirec- tional fibrous composites with an interfacial thermal resistance, Numerical Heat Transfer, Part A: Appl. 39 (2) (2001) 179–203.

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
