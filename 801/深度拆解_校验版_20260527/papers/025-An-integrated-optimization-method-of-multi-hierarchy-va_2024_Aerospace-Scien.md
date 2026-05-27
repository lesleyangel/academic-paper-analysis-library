# 论文深度拆解：An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths

> 生成依据：`801/cleantext/025-An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`025-An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-integrated-optimization-method-of-multi-hierarchy-va_2024_Aerospace-Scien.pdf`
- 页数：10
- clean body 字符数：45817
- 摘要字符数：1380
- 参考文献条数：38
- 图题数：20
- 表题数：0
- 表格文件数：0
- 公式候选数：104
- 提取质量分：0.96
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "14 formula(s) need manual review."}]

## 1. 身份层

- 标题：An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths
- 年份：2024
- 期刊/来源：Aerospace Scien
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
- 主要方法：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction. A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered. A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size an
- 主要证据：图表 20 个标题、公式 104 个候选、参考文献 38 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth be”，可以通过“In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %. Under some circumstances, the beam presence and absence are determined by its size, i.e., smaller than a specified value reveals beam absence and vice versa, thus, the topology and size optimizations are always conducted simultaneously or sequentially and iteratively $[ 19 , 21$ , 22]. 1(b) shown by the above optimization model, beams in the ground structure should be much more closely arranged, α should be smaller than γ and the optimization cost would be unaffordable (depends on $\gamma )$ .
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
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
- 作者声明或文本中可见 gap：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions. The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, excessive beams will lead to high cost and low efficiency of optimizations. Two hierarchies of variables, $\mathrm{i.e.,}$ topology and size are involved in such optimization problem, and the mathematic model can be described as $\operatorname{Eq.}$ (1): Find $X _ {T} , X _ {S}$ Min M(XT , XS) $$\mathrm{S.T.} \quad g _ {i} ( X _ {T} , X _ {S} ) < g _ {i \mathrm{max}} \quad i = 1 , \cdots , d\tag{1}$$ $$X _ {T j} \in \{0 , 1 \} \quad j = 1 , \cdots , n$$ $$X _ {S j} \in \left[ L B _ {S j} , U B _ {S j} \right] \quad j = 1 , \cdots , n$$ (b) Potential optimal structure where $X _ {T}$ and $X _ {S}$ are optimization variables, which indicate the topology and the size (cross-sectional width in this work) of beams, respectively; $M ( X _ {T} , X _ {S} )$ indicates the objective parameters such as the structural mass; $g _ {i} ( X _ {T} , X _ {S} )$ is the mechanical or thermal parameters like stress or temperature of the ith beam, and $g _ {\mathrm{imax}}$ indicates the available limits of such parameters; d is the number of beams of the present structure; $X _ {T j}$ is the topology of the jth beam with two values of 0 or 1 which represent the removing or remaining of the beam, respectively; $X _ {S j}$ is the size of the jth beam, and $L B _ {S j}$ and $U B _ {S j}$ represent the lower and upper bounds of $X _ {S j} ,$ respectively; n is the total beam number of the ground structure.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
- It was found that in general, the particle swarm algorithm has similar effectiveness while higher efficiency when handling continuous problems, however, the genetic algorithm performs greater effectiveness for problems involving discrete variables [33].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction. A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered. A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
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
| In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam dire | 摘要/引言/结论候选 | 图：Fig. 1. Ground structure and possible structure after optimization. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effec | 摘要/引言/结论候选 | 图：Fig. 2. The single-point crossover operator for three hierarchy variables. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %. | 摘要/引言/结论候选 | 图：Fig. 3. The simple mutation operator. Fig. 4. The derivation of the angle variable. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The topology to some extent indicates the presence or absence of structural constituents, while the size indicates the specific width, length, thickness or cross-sectional area of the constituent. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 205.75, 416.62, 223.92)]] Jian-Jun Gou a,*, Shu-Zhen Jia b, Ha | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In some researches, the structural shape which represents the location and the boundary of the structural constituent is assumed as an additional hierarchy between the topology and size ones [11]. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 336.59, 690.38)]] * Corresponding author | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| For continuous-type structures, the density-based homogenization [12] and SIMP optimization methods [13,14] coupling with finite element simulation are always adopted, where the structural constituent is represented by element and its presence or absence is de | 摘要/引言/结论候选 | 图：Fig. 1. Ground structure and possible structure after optimization. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Ground structure and possible structure after optimization. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. The single-point crossover operator for three hierarchy variables. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. The simple mutation operator. Fig. 4. The derivation of the angle variable. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. The geometric and meshed models of ground structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. The meshed model and pressure fields of aerodynamic calculation. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 7. The lifting surface and its grid. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. The optimization path. Fig. 9. The optimization process of statics problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The beam angle and size of statics problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. The beam, displacement and stress distribution of statics problem. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. The optimization process of aeroelastic problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The beam angle and size of static aeroelastic problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Comparison with two-hierarchy optimization process for stat ics problem. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 16. Comparison with two-hierarchy optimization process for static aero elastic problem. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 3. The simple mutation operator. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The derivation of the angle variable. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 205.75, 416.62, 223.92)]] Jian-Jun Gou a,*, Shu-Zhen Jia b, Hai-Tao Tian b, Jia-Xi | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 336.59, 690.38)]] * Corresponding authors. E-mail addresses: | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 341.98, 716.91)]] https://doi.org/10.1016/j.ast.2024.109115  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (309.26, 711.87, 391.03, 721.03)]] XTj ∈{0, 1} j = 1, ⋯, n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (310.57, 697.64, 434.11, 706.5)]] S.T. gi(XT, XS) < gimax i = 1, ⋯, d | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (364.42, 719.86, 409.91, 734.69)]] ] j = 1, ⋯, n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (41.61, 498.59, 177.41, 507.45)]] S.T. gi(XT, XA, XS) < gimax i = 1, ⋯, d | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (40.25, 512.82, 122.08, 521.98)]] XTj ∈{0, 1} j = 1, ⋯, n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The optimization of structures with beam-like force transfer paths for flight vehicles is closely dependent on the hierarchy decomposition and interaction effects of variables. In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction. A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered. A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively. The statics problem with objective of minimum structural mass and constraints of stress and displacement, and the static aeroelastic problem with objective of minimum influence quantity and constraints of structural mass, stress and displacement are solved. The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.

### 7.4 摘要中文翻译

> 飞行器类梁力传递路径结构的优化密切依赖于变量的层次分解和相互作用效应。在这项工作中，径向梁舵结构的变量被分解为传统的拓扑和尺寸层次结构和新的非常规角度层次结构，这是一个具有径向梁方向隐式表达的表征变量。提出了离散变量拓扑和连续变量角度、尺寸的统一编码形式，并基于遗传算法提出了多层次变量的集成优化方法，并充分考虑了不同层次之间的相互作用影响。然后分别构建了拓扑和尺寸的两级优化模型和拓扑、尺寸和角度的三级优化模型。求解了以最小结构质量为目标、受应力、位移约束的静力学问题和以最小影响量为目标、受结构质量、应力、位移约束的静力气动弹性问题。结果表明，三层次优化模型比两层次优化模型效率更高，结构质量减少了18.9%，气动弹性影响量减少了4.3%。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> In this work, an integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths is developed. The optimization variable of a rudder with radial beams is decomposed into two hierarchies of topology and size, three hierarchies of topology, size and angle, and a two-hierarchy and a three-hierarchy optimization model are then constructed, respectively. The integrated optimization method of multi-hierarchy variables is developed based on the genetic algorithm. The statics problem with objective of minimum structural mass and constraints of stress and displacement, and the static aeroelastic problem with objective of minimum influence quantity and constraints of mass, stress and displacement are solved, and the results show some conclusions as follows.
> 
> (1) In general, the integrated multi-hierarchy optimization process has rapid progressions at the initial stage, gradual progressions at subsequent stages and several sudden progressions occasionally.
> 
> (2) For the statics problem solved by the three-hierarchy optimization method, the mass reductions of the optimal structure comparing with the ground and the first qualified one are 77.0 % and 51.1 %, respectively.
> 
> (3) For the static aeroelastic problem solved by the three-hierarchy optimization method, the aeroelastic influence quantity of the optimal structure is reduced by 37.9 %.
> 
> (4) Comparing with the two-hierarchy model, the three-hierarchy one will have positive effect and growing advantages after the evolution of certain generations.
> 
> (5) The three-hierarchy optimization is more efficient than the twohierarchy one with structural mass reduction of 18.9 % for the statics problem and aeroelastic influence quantity reduction of 4.3 % for the static aeroelastic problem.

### 7.6 结论中文翻译

> （机器翻译失败，保留英文原文供复核。）In this work, an integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths is developed. The optimization variable of a rudder with radial beams is decomposed into two hierarchies of topology and size, three hierarchies of topology, size and angle, and a two-hierarchy and a three-hierarchy optimization model are then constructed, respectively. The integrated optimization method of multi-hierarchy variables is developed based on the genetic algorithm. The statics problem with objective of minimum structural mass and constraints of stress and displacement, and the static aeroelastic problem with objective of minimum influence quantity and constraints of mass, stress and displacement are solved, and the results show some conclusions as follows. (1) In general, the integrated multi-hierarchy optimization process has rapid progressions at the initial stage, gradual progressions at subsequent stages and several sudden progressions occasionally. (2) For the statics problem solved by the three-hierarchy optimization method, the mass reductions of the optimal structure comparing with the ground and the first qualified one are 77.0 % and 51.1 %, respectively. (3) For the static aeroelastic problem solved by the three-hierarchy optimization method, the aeroelastic influence quantity of the optimal structure is reduced by 37.9 %. (4) Comparing with the two-hierarchy model, the three-hierarchy one will have positive effect and growing advantages after the evolution of certain generations. (5) The three-hierarchy optimization is more efficient than the twohierarchy one with structural mass reduction of 18.9 % for the statics problem and aeroelastic influence quantity reduction of 4.3 % for the static aeroelastic problem.

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9344 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Optimization problem | 对象/条件/子问题展开 | 1163 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. General models | 方法建构 | 3343 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3. The multi-hierarchy integrated optimization algorithm | 方法建构 | 368 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. Unified chromosome encoding with gray code | 对象/条件/子问题展开 | 1378 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Selection, crossover and mutation operators | 对象/条件/子问题展开 | 2524 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Fitness function | 对象/条件/子问题展开 | 1933 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.1. The optimization model and the implicit angle variable | 方法建构 | 5197 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.2. The numerical model | 方法建构 | 314 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | (a) Statics problem | 对象/条件/子问题展开 | 3859 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | (b) Static aeroelastic problem | 对象/条件/子问题展开 | 1502 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. The optimization path | 对象/条件/子问题展开 | 1842 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.1. Statics problem | 对象/条件/子问题展开 | 3322 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.2. Static aeroelastic problem | 对象/条件/子问题展开 | 3231 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.3. Comparison with two-hierarchy optimization | 对象/条件/子问题展开 | 3359 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 6. Conclusions | 主张回收/边界说明 | 1798 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 17 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 543 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：optimization(99)；respectively(50)；size(49)；structure(48)；beam(47)；beams(45)；mathcal(40)；partial(40)；topology(39)；structural(38)；angle(37)；generation(36)；process(34)；fig(34)；mass(33)；mathrm(32)；problem(30)；variable(29)；aeroelastic(28)；ground(27)
- 高频学术名词/术语：optimization(99)；structure(48)；generation(36)；distribution(18)；displacement(18)；function(18)；influence(16)；quantity(15)；statics(15)；reduction(14)；fitness(10)；variation(9)；pressure(9)；element(8)；simulation(8)
- 高频学术动词：obtained(20)；developed(8)；indicate(7)；optimized(7)；obtain(6)；compared(4)；indicated(3)；constructed(2)；reveal(1)；derived(1)；validated(1)
- 高频形容词：mathcal(40)；partial(40)；structural(38)；variable(29)；aeroelastic(28)；objective(21)；static(18)；optimal(18)；displacement(18)；genetic(14)；initial(9)；general(9)；element(8)；individual(8)；positive(8)
- 高频副词：respectively(50)；actually(4)；closely(4)；specifically(4)；theoretically(3)；widely(3)；relatively(3)；occasionally(3)；firstly(2)；inherently(2)；randomly(2)；mostly(1)
- 高频二词短语：mathcal mathcal(29)；ground structure(23)；frac partial(20)；optimization process(19)；structural mass(18)；static aeroelastic(16)；one find(14)；objective function(14)；influence quantity(13)；topology size(11)；integrated optimization(11)；angle size(11)；stress displacement(11)；partial partial(11)；aeroelastic influence(11)
- 高频三词短语：mathcal mathcal mathcal(21)；frac partial partial(11)；aeroelastic influence quantity(11)；partial frac partial(11)；static aeroelastic problem(9)；topology angle size(7)；cdots cdots cdots(7)；end array tag(6)；angle size variables(6)；objective function value(6)；frac partial sigma(6)；partial sigma partial(6)
- 被动语态估计：145
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：252
- 一般过去时线索：270
- 现在完成时线索：0
- 情态动词线索：56

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 未稳定识别，需从对应章节人工补充。
### gap/转折句
- 原句：Such method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs complex beam reconstructions.
  - 可迁移句型：{object} method is mostly appropriate to structures without any prespecified force transfer paths, while for beam-like structures, its element deleting process will lead to unsmooth beam boundaries (gray densities between white and black [15]) and needs comple
- 原句：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, excessive beams will lead to high cost and low efficiency of optimizations.
  - 可迁移句型：{object} performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, excessive beams will lead 
- 原句：Two hierarchies of variables, $\mathrm{i.e.,}$ topology and size are involved in such optimization problem, and the mathematic model can be described as $\operatorname{Eq.}$ (1): Find $X _ {T} , X _ {S}$ Min M(XT , XS) $$\mathrm{S.T.} \quad g _ {i} ( X _ {T} , X _ {S} ) < g _ {i \mathrm{max}} \quad i = 1 , \cdots , d\tag{1}$$ $$X _ {T j} \in \{0 , 1 \} \quad j = 1 , \cdots , n$$ $$X _ {S j} \in \left[ L B _ {S j} , U B _ {S j} \right] \quad j = 1 , \cdots , n$$ (b) Potential optimal structure where $X _ {T}$ and $X _ {S}$ are optimization variables, which indicate the topology and the size (cross-sectional width in this work) of beams, respectively; $M ( X _ {T} , X _ {S} )$ indicates the objective parameters such as the structural mass; $g _ {i} ( X _ {T} , X _ {S} )$ is the mechanical or thermal parameters like stress or temperature of the ith beam, and $g _ {\mathrm{imax}}$ indicates the available limits of such parameters; d is the number of beams of the present structure; $X _ {T j}$ is the topology of the jth beam with two values of 0 or 1 which represent the removing or remaining of the beam, respectively; $X _ {S j}$ is the size of the jth beam, and $L B _ {S j}$ and $U B _ {S j}$ represent the lower and upper bounds of $X _ {S j} ,$ respectively; n is the total beam number of the ground structure.
  - 可迁移句型：{object} hierarchies of variables, $\mathrm{i.e.,}$ topology and size are involved in such optimization problem, and the mathematic model can be described as $\operatorname{Eq.}$ (1): Find $X _ {T} , X _ {S}$ Min M(XT , XS) $$\mathrm{S.T.} \quad g _ {i} ( X _ 
- 原句：At present, the γ-distribution with gathered beams in high-load regions is still lack of effective method.
  - 可迁移句型：{object} present, the γ-distribution with gathered beams in high-load regions is still lack of effective method.
### 方法提出句
- 原句：In this work, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial beam direction.
  - 可迁移句型：{object} This study, the variable of a rudder structure with radial beams is decomposed into conventional hierarchies of topology and size and a new unconventional hi erarchy of angle, which is a representational variable with implicit expression for radial be
- 原句：A unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interaction effects between different hierarchies are fully considered.
  - 可迁移句型：{object} unified code form is proposed for discrete variable, i.e., topology and continuous variables, i.e., angle and size, and then an integrated optimization method of multi-hierarchy variables is developed based on the genetic al gorithm and the interactio
- 原句：A two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
  - 可迁移句型：{object} two-hierarchy optimi zation model of topology and size and a three-hierarchy optimization model of topology, size and angle are then constructed, respectively.
- 原句：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
  - 可迁移句型：{object} results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
### 结果证明句
- 原句：The results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
  - 可迁移句型：{object} results show that the three-hierarchy optimization model is more efficient than the two-hierarchy one with structural mass reduction of 18.9 % and aeroelastic influence quantity reduction of 4.3 %.
- 原句：The topology to some extent indicates the presence or absence of structural constituents, while the size indicates the specific width, length, thickness or cross-sectional area of the constituent.
  - 可迁移句型：{object} topology to some extent indicates the presence or absence of structural constituents, while the size indicates the specific width, length, thickness or cross-sectional area of the constituent.
- 原句：Under some circumstances, the beam presence and absence are determined by its size, i.e., smaller than a specified value reveals beam absence and vice versa, thus, the topology and size optimizations are always conducted simultaneously or sequentially and iteratively $[ 19 , 21$ , 22].
  - 可迁移句型：{object} some circumstances, the beam presence and absence are determined by its size, i.e., smaller than a specified value reveals beam absence and vice versa, thus, the topology and size optimizations are always conducted simultaneously or sequentially and i
- 原句：Two hierarchies of variables, $\mathrm{i.e.,}$ topology and size are involved in such optimization problem, and the mathematic model can be described as $\operatorname{Eq.}$ (1): Find $X _ {T} , X _ {S}$ Min M(XT , XS) $$\mathrm{S.T.} \quad g _ {i} ( X _ {T} , X _ {S} ) < g _ {i \mathrm{max}} \quad i = 1 , \cdots , d\tag{1}$$ $$X _ {T j} \in \{0 , 1 \} \quad j = 1 , \cdots , n$$ $$X _ {S j} \in \left[ L B _ {S j} , U B _ {S j} \right] \quad j = 1 , \cdots , n$$ (b) Potential optimal structure where $X _ {T}$ and $X _ {S}$ are optimization variables, which indicate the topology and the size (cross-sectional width in this work) of beams, respectively; $M ( X _ {T} , X _ {S} )$ indicates the objective parameters such as the structural mass; $g _ {i} ( X _ {T} , X _ {S} )$ is the mechanical or thermal parameters like stress or temperature of the ith beam, and $g _ {\mathrm{imax}}$ indicates the available limits of such parameters; d is the number of beams of the present structure; $X _ {T j}$ is the topology of the jth beam with two values of 0 or 1 which represent the removing or remaining of the beam, respectively; $X _ {S j}$ is the size of the jth beam, and $L B _ {S j}$ and $U B _ {S j}$ represent the lower and upper bounds of $X _ {S j} ,$ respectively; n is the total beam number of the ground structure.
  - 可迁移句型：{object} hierarchies of variables, $\mathrm{i.e.,}$ topology and size are involved in such optimization problem, and the mathematic model can be described as $\operatorname{Eq.}$ (1): Find $X _ {T} , X _ {S}$ Min M(XT , XS) $$\mathrm{S.T.} \quad g _ {i} ( X _ 
### 贡献收束句
- 原句：(3) For the static aeroelastic problem solved by the three-hierarchy optimization method, the aeroelastic influence quantity of the optimal structure is reduced by 37.9 %.
  - 可迁移句型：(3) {object} the static aeroelastic problem solved by the three-hierarchy optimization method, the aeroelastic influence quantity of the optimal structure is reduced by 37.9 %.
### 边界/谨慎句
- 原句：The optimization should consider variables of different hierarchies such as the basic ones, i.e., structural topology and size.
  - 可迁移句型：{object} optimization should consider variables of different hierarchies such as the basic ones, i.e., structural topology and size.
- 原句：In some researches, the structural shape which represents the location and the boundary of the structural constituent is assumed as an additional hierarchy between the topology and size ones [11].
  - 可迁移句型：{object} some researches, the structural shape which represents the location and the boundary of the structural constituent is assumed as an additional hierarchy between the topology and size ones [11].
- 原句：In this method, the ground structure should be considered as the initial structure, certain trusses or beams should be specified firstly and will be partly removed during the optimization.
  - 可迁移句型：{object} this method, the ground structure should be considered as the initial structure, certain trusses or beams should be specified firstly and will be partly removed during the optimization.
- 原句：The performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, excessive beams will lead to high cost and low efficiency of optimizations.
  - 可迁移句型：{object} performance and efficiency of such optimization process are closely related with the scale of variable set, i.e., the optimal structure can only be obtained from the ground structure with sufficient number of beams, however, excessive beams will lead 

## 9. 引用风险层

- 正文引用簇估计：22
- 参考文献条数：38
- 可识别年份条目数：40
- 2021 年及以后参考文献数：13
- 2010 年以前经典文献数：10
- 高频来源粗略识别：Sci. Technol(8)；Multidiscipl. Optimizat(6)；Methods Appl. Mech. Eng(3)；Optimizat(1)；Comput. Phys(1)；Struct. Eng(1)；Design(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] K. Liang, Z. Yin, Investigation on nonlinear buckling performance of the optimized wing structure under the realistic flight cases, Aerosp. Sci. Technol. 139 (2023) 108416.
- [2] P.D.R. Santos, et al., Effect of design parameters on the mass of a variable-span morphing wing based on finite element structural analysis and optimization, Aerosp. Sci. Technol. 80 (2018) 587–603.
- [3] O. Dababneh, T. Kipouros, Influence of high fidelity structural models on the predicted mass of aircraft wing using design optimization, Aerosp. Sci. Technol. 79 (2018) 164–173.
- [4] D.J. Munk, J.D. Miller, Topology optimization of aircraft components for increased sustainability, AIAA J. 60 (1) (2021) 445–460. Vol. 60, No. 1.
- [5] S. Chintapalli, et al., The development of a preliminary structural design optimization method of an aircraft wing-box skin-stringer panels, Aerosp. Sci. Technol. 14 (3) (2010) 188–198.
- [6] M. Saporito, et al., Robust multidisciplinary analysis and optimization for conceptual design of flexible aircraft under dynamic aeroelastic constraints, Aerosp. Sci. Technol. 138 (2023) 108349.
- [7] D. Li, et al., Aeroelastic global structural optimization using an efficient CFD-based reduced order model, Aerosp. Sci. Technol. 94 (2019) 105354.
- [8] D. Sarojini, D. Mavris, Structural analysis and optimization of wings subjected to dynamic loads, AIAA Journal 60 (2) (2022) 1013–1023.
- [9] E. Jonsson, et al., High-fidelity gradient-based wing structural optimization including geometrically nonlinear flutter constraint, AIAA J. 0 (0) (2023) 1–17.
- [10] E. Jonsson, et al., Flutter and post-flutter constraints in aircraft design optimization, Progress Aerospace Sci. 109 (2019) 100537.
- [11] Querin, O.M., et al., "Chapter 1 - Introduction, in topology design methods for structural optimization", O.M. Querin, et al., Eds. 2017, Academic Press: Oxford. p. 1–13.
- [12] M.P. Bendsøe, N. Kikuchi, Generating optimal topologies in structural design using a homogenization method, Comput. Methods Appl. Mech. Eng. 71 (2) (1988) 197–224.
- [13] M.P. Bendsøe, Optimal shape design as a material distribution problem, Struct. Optimizat. 1 (4) (1989) 193–202.
- [14] M. Tarek, T. Ray, Adaptive continuation solid isotropic material with penalization for volume constrained compliance minimization, Comput. Methods Appl. Mech. Eng. 363 (2020) 112880.
- [15] C. Wang, X. Qian, A density gradient approach to topology optimization under design-dependent boundary loading, J. Comput. Phys. 411 (2020) 109398.

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
