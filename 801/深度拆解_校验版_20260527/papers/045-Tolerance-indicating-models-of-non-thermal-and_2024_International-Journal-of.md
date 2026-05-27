# 论文深度拆解：Tolerance indicating models of non-thermal and thermal damages for a heat transport system

> 生成依据：`801/cleantext/045-Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`045-Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of.pdf`
- 页数：20
- clean body 字符数：71149
- 摘要字符数：1289
- 参考文献条数：133
- 图题数：26
- 表题数：6
- 表格文件数：9
- 公式候选数：343
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "26 formula(s) need manual review."}]

## 1. 身份层

- 标题：Tolerance indicating models of non-thermal and thermal damages for a heat transport system
- 年份：2024
- 期刊/来源：International Journal of
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：Thus, a certain tolerance of damages is essential for a qualified HT system.
- 主要方法：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing. Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data. For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivitie
- 主要证据：图表 32 个标题、公式 343 个候选、参考文献 133 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Thus, a certain tolerance of damages is essential for a qualified HT system.”，可以通过“In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability m”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Lu et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K. To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on $\mathrm{ZrB} _ {2}$ and $\mathrm{HfB} _ {2}$ are proposed. Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high temperatures, and test results indicated that a ZrO skeleton was formed resulting in improvement of the ablation resistance.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Thus, a certain tolerance of damages is essential for a qualified HT system.
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
- 作者声明或文本中可见 gap：However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase. The usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41]. For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for $T _ {\mathrm{max}}$ 3.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing. Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data. For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivities (higher than 500 W/(m⋅K) in [12]).
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
| In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient an | 摘要/引言/结论候选 | 图：Fig. 1. The high-speed vehicle and HT systems. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data. | 摘要/引言/结论候选 | 图：Fig. 2. Topology optimization model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivities (higher than 500 W/(m⋅K) in [12]). | 摘要/引言/结论候选 | 图：Fig. 3. The HT path and Temperature distributions. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Lu et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smalle | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on $\mathrm{ZrB} _ {2}$ and $\mathrm{HfB} _ {2}$ are proposed. | 摘要/引言/结论候选 | 表：Table 3 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at hig | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 205.75, 377.8, 223.92)]] Jia-Xin Hu a, Li-Qiang Ai b, Nan Liu  | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The high-speed vehicle and HT systems. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Topology optimization model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. The HT path and Temperature distributions. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4. Geometric and mesh models of the HT path with non-thermal damage. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. Variations of Th, Tn with different Tf and β. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 6. Distributions of Th with different Tf and β. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 7. Distributions of thermal damages with different Tf and β. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Geometric and mesh models of the HT path with thermal damage. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 9. Temperature distribution of the HT path with non-thermal damage. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. The influences of damage on the thermal performance of HT paths. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Temperature distributions of HT paths based on the orthogonal design. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. Numerical results of the samples. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. The influences of damage on the mean thermal performance of HT paths. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. First-order fittings of the normalized results of non-thermal damage. Fig. 15. Second-order fittings of the normalized results of non-thermal damage. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 16. Temperature distributions of HT paths with different Tf and β. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 205.75, 377.8, 223.92)]] Jia-Xin Hu a, Li-Qiang Ai b, Nan Liu b, Jian-Jun Gou a,*, | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 206.24, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 352.12, 716.91)]] https://doi.org/10.1016/j.ijheatmasstransf | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (307.96, 415.36, 379.76, 440.45)]] Min : Tgeoav = ( 1 \|Ω\| | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (340.95, 439.63, 384.41, 459.32)]] ki∇TidΩ = ∫ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (307.95, 277.82, 398.09, 289.51)]] Find : X = {ρ1, ρ2, ..., ρNE}T | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (307.96, 305.72, 353.44, 314.88)]] Min : Tgeoav = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (307.96, 328.23, 358.26, 336.59)]] s.t. KT = Q | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> For reusable high-speed vehicles, the damage accumulation in heat transfer paths during multitudes of missions leads to resistance augment, performance undermining, and even failures of heat transport (HT) systems. The quantitative characterization of tolerance for various damages becomes crucial to a reliable HT system. In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing. A dendritic HT system is obtained by topologic optimization with the objective of the lowest geometric average temperature, and the heat transfer with multiple distributions of non-thermal and thermal damages is analyzed. The effects of size and volume fraction for non-thermal damage and that of constraint temperature and probability gradient for thermal damage on the HT performance are clarified. Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data.

### 7.4 摘要中文翻译

> 对于可重复使用的高速车辆，在多次执行任务期间传热路径中的损坏累积会导致阻力增大、性能下降，甚至热传输（HT）系统故障。对各种损坏的耐受性的定量表征对于可靠的 HT 系统至关重要。在这项工作中，使用尺寸和体积分数的随机模型来描述由机械振动、冲击、腐蚀等各种非热载荷引起的非热损伤，并建立了考虑概率梯度和局部、参考、极限和约束温度的概率模型来表征随着温度升高而产生的热损伤。通过拓扑优化得到了以几何平均温度最低为目标的树枝状高温体系，并分析了非热损伤和热损伤多重分布的传热情况。阐明了非热损伤的尺寸和体积分数以及热损伤的约束温度和概率梯度对HT性能的影响。然后通过多项式拟合提出了考虑 HT 性能的两个损伤容限指示模型，并通过扩展数值数据进行了验证。

### 7.5 结论完整摘录

识别到的结论位置：The results show some conclusions:

> 1. The damage tolerance indicating models encompass the average temperature, $T _ {\mathrm{avg}} ,$ the maximum temperature, $T _ {\mathrm{max}} ,$ , and the standard deviation of temperature, $s _ {T} ,$ to evaluate the thermal performance of an HT path.
> 
> 2. For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for $T _ {\mathrm{max}}$
> 
> 3. For thermal damages, the transition region increases, the hightemperature region decreases and the damage tolerance of the HT path is thus enhanced with the decrease of the maximum damage probability gradient, β and the increase of constraint temperature, $T _ {\mathrm{f}}$
> 
> 4. The tolerances of non-thermal damages vary between 0.302 and 0.926 when the volume fraction and radius vary between 2.12% to 16.33% and 0.94 mm to 5.00 mm; the maximum deviations of the damage model are $0.83 \% , \ - 7.54 \%$ , and 7.90% for average $T _ {\mathrm{avg}} ,$ $T _ {\mathrm{max}} ,$ and $s _ {T} ,$ respectively.
> 
> 5. The tolerances of thermal damages vary between 0.13 and 0.787 when $\beta$ and $T _ {\mathrm{f}}$ vary between 13.5 to 15.5 and 373 K to 383 K; the maximum deviations of the damage model are $0.90 \% , - 1.50 \%$ , and − 4.82% for average $T _ {\mathrm{avg}} , \ T _ {\mathrm{max}} ,$ , and $s _ {T} ,$ respectively, when the damage volume fraction is larger than 10.98%.
> 
> 6. For a dendritic HT path with certain damages, the thermal performance can be obtained by the damage models, and the tolerance of non-thermal damage is better than that of thermal damage under the same damage level.

### 7.6 结论中文翻译

> 损伤容限指示模型包含平均温度 $T _ {\mathrm{avg}} ,$ 最高温度 $T _ {\mathrm{max}} ,$ 和温度标准偏差 $s _ {T} ,$ 来评估 HT 路径的热性能。对于非热损伤，随着损伤体积分数V和半径R的增加，损伤区域增大，而热性能和耐受性降低；然而，损伤的随机性会导致一些奇异性，特别是对于$T _ {\mathrm{max}}$ 3. 对于热损伤，随着最大损伤概率梯度β的减小和约束温度$T _ {\mathrm{f}}$的增加，过渡区增加，高温区减小，HT路径的损伤容限因此增强。 4. 非热损伤的容差在0.302和0.302之间变化。当体积分数和半径在2.12％至16.33％和0.94mm至5.00mm之间变化时，为0.926；损伤模型的平均 $T _ {\mathrm{avg}} 、$ $T _ {\mathrm{max}} 、$ 和 $s _ {T} ,$ 的最大偏差分别为 $0.83 \% 、 \ - 7.54 \%$ 和 7.90% 。当 $\beta$ 和 $T _ {\mathrm{f}}$ 在 13.5 到 15.5 以及 373 K 到 383 K 之间变化时，热损伤容差在 0.13 到 0.787 之间变化；当损伤体积分数大于 10.98% 时，平均 $T _ {\mathrm{avg}} 、\T _ {\mathrm{max}} 、$ 和 $s _ {T} ,$ 损伤模型的最大偏差分别为 $0.90 \% 、- 1.50 \%$ 和 − 4.82% 。对于存在一定损伤的树枝状高温路径，通过损伤模型可以获得热性能，并且在相同损伤水平下，非热损伤的耐受性优于热损伤。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8699 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. The high-speed vehicle and its HT system | 对象/条件/子问题展开 | 1823 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3. The physical model and HT path design | 方法建构 | 6692 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 4. Mathematical models of damage | 方法建构 | 1522 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 4.1. The mathematical model of non-thermal damage | 方法建构 | 4809 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 4.2. The mathematical model of thermal damage | 方法建构 | 8824 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 5. The damage tolerance indicating model | 方法建构 | 5693 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 6.1. The non-thermal damage model | 方法建构 | 10463 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 6.2. The thermal damage model | 方法建构 | 2804 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 6.3.1. The non-thermal damage tolerance | 对象/条件/子问题展开 | 10210 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 6.3.2. The thermal damage tolerance | 对象/条件/子问题展开 | 4779 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 6.3.3. The relationships between volume fraction and damage tolerance | 对象/条件/子问题展开 | 1114 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 7. Conclusion | 主张回收/边界说明 | 834 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 14 | The results show some conclusions: | 结果验证/讨论 | 1740 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 15 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 411 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(448)；damage(179)；thermal(119)；cdot(117)；respectively(85)；max(79)；avg(78)；temperature(75)；fig(63)；path(50)；performance(49)；heat(46)；tolerance(45)；non-thermal(45)；frac(43)；left(41)；right(41)；beta(36)；maximum(33)；array(32)
- 高频学术名词/术语：temperature(75)；performance(49)；tolerance(45)；fraction(27)；conductivity(25)；probability(20)；prediction(17)；distribution(11)；simulation(10)；optimization(10)；deviation(10)；generation(9)；structure(8)；resistance(7)；density(7)
- 高频学术动词：obtained(29)；indicate(17)；obtain(8)；developed(6)；indicated(5)；optimized(3)；predict(3)；revealed(2)；investigate(2)；presented(1)；validated(1)；compared(1)；constructed(1)；evaluate(1)
- 高频形容词：thermal(119)；non-thermal(45)；material(16)；mathematical(13)；table(13)；specific(12)；gradient(12)；represent(11)；boundary(10)；various(9)；numerical(8)；constant(8)；element(7)；typical(7)；geometric(6)
- 高频副词：respectively(85)；generally(4)；rapidly(4)；mainly(3)；mostly(3)；linearly(3)；quickly(2)；additionally(2)；slowly(2)；approximately(2)；positively(2)；specifically(1)
- 高频二词短语：mathrm avg(78)；mathrm max(75)；mathrm mathrm(75)；avg mathrm(60)；cdot cdot(50)；thermal performance(37)；thermal damage(36)；damage tolerance(35)；non-thermal damage(31)；max respectively(29)；mathrm respectively(25)；thermal conductivity(21)；volume fraction(21)；max mathrm(18)；respectively mathrm(17)
- 高频三词短语：mathrm avg mathrm(60)；avg mathrm max(52)；mathrm max respectively(29)；cdot cdot cdot(27)；mathrm mathrm mathrm(23)；mathrm max mathrm(16)；respectively deviations mathrm(13)；deviations mathrm avg(13)；mathrm mathrm lim(12)；mathrm lim mathrm(12)；left cdot cdot(12)；respectively mathrm avg(12)
- 被动语态估计：144
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：317
- 一般过去时线索：307
- 现在完成时线索：0
- 情态动词线索：92

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Thus, a certain tolerance of damages is essential for a qualified HT system.
  - 可迁移句型：{object}, a certain tolerance of damages is essential for a qualified HT system.
- 原句：The optimization model can be given as: Find : $\rho ( x ) , x \in \Omega$ $$\begin{array} {l l} {\displaystyle \mathrm{Min} :} & {T _ {\mathrm{geouv 1.
  - 可迁移句型：{object} optimization model can be given as: Find : $\rho ( x ) , x \in \Omega$ $$\begin{array} {l l} {\displaystyle \mathrm{Min} :} & {T _ {\mathrm{geouv 1.
### gap/转折句
- 原句：However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
  - 可迁移句型：{object}, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
- 原句：The usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41].
  - 可迁移句型：{object} usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41].
- 原句：For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for $T _ {\mathrm{max}}$ 3.
  - 可迁移句型：{object} non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for 
- 原句：For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for $T _ {\mathrm{max}}$ 3.
  - 可迁移句型：{object} non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for 
### 方法提出句
- 原句：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing.
  - 可迁移句型：{object} This study, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability grad
- 原句：Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data.
  - 可迁移句型：{object} damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data.
- 原句：For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivities (higher than 500 W/(m⋅K) in [12]).
  - 可迁移句型：{object} instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conductivities (higher than 500 W/(m⋅K) in [12]).
- 原句：Lu et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
  - 可迁移句型：{object} et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of 
### 结果证明句
- 原句：Lu et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
  - 可迁移句型：{object} et al. [4] developed a temperature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of 
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high temperatures, and test results indicated that a ZrO skeleton was formed resulting in improvement of the ablation resistance.
  - 可迁移句型：{object} et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at h
- 原句：UHTC based on ZrB2 and HfB2 could achieve thermal conductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
  - 可迁移句型：{object} based on ZrB2 and HfB2 could achieve thermal conductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
- 原句：However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
  - 可迁移句型：{object}, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
### 贡献收束句
- 原句：Materials with high thermal conductivities are always adopted to enhance the heat conduction property at certain orientations to form an HT system.
  - 可迁移句型：{object} with high thermal conductivities are always adopted to enhance the heat conduction property at certain orientations to form an HT system.
- 原句：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on $\mathrm{ZrB} _ {2}$ and $\mathrm{HfB} _ {2}$ are proposed.
  - 可迁移句型：{object} improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on $\mathrm{ZrB} _ {2}$ and $\mathrm{HfB} _ {2}$ are proposed.
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high temperatures, and test results indicated that a ZrO skeleton was formed resulting in improvement of the ablation resistance.
  - 可迁移句型：{object} et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at h
- 原句：A case in square plate (100 mm × 100 mm) with heat sources of 10 W was provided, and the heat conduction path with better heat performance was obtained.
  - 可迁移句型：{object} case in square plate (100 mm × 100 mm) with heat sources of 10 W was provided, and the heat conduction path with better heat performance was obtained.
### 边界/谨慎句
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high temperatures, and test results indicated that a ZrO skeleton was formed resulting in improvement of the ablation resistance.
  - 可迁移句型：{object} et al. [16] and Luo et al. [17] prepared sharp leading edge structures using $\mathbf {Z r B} _ {2} - \mathbf {S i C}$ based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at h
- 原句：UHTC based on ZrB2 and HfB2 could achieve thermal conductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
  - 可迁移句型：{object} based on ZrB2 and HfB2 could achieve thermal conductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
- 原句：Therefore, a typical problem should be studied in order to obtain some universal conclusions.
  - 可迁移句型：{object}, a typical problem should be studied in order to obtain some universal conclusions.
- 原句：The usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41].
  - 可迁移句型：{object} usual configuration of a two-dimensional VP problem contains a rectangular area with a distributed heat source, and one or more heat sinks with limited size and constant temperature on the borders of the area [41].

## 9. 引用风险层

- 正文引用簇估计：48
- 参考文献条数：133
- 可识别年份条目数：91
- 2021 年及以后参考文献数：29
- 2010 年以前经典文献数：9
- 高频来源粗略识别：J. Heat Mass Transf(9)；Eur. Ceram. Soc(4)；Therm. Eng(3)；Sci. Technol(3)；Fail. Anal(3)；B Eng(2)；Commun. Heat Mass Transf(2)；Diamond(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Gori, S.
- Corasaniti, W.M.
- Worek, W.J.
- Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130, https://doi.org/10.1016/j.applthermaleng.2011.07.012. [2] B.
- Behrens, M.
- Müller, Technologies for thermal protection systems applied on re- usable launcher, Acta Astronaut. 55 (2004), https://doi.org/10.1016/j. actaastro.2004.05.034. [3] Y.
- Rong, Y.
- Wei, R.
- Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (2016) 322–327, https://doi.org/10.1016/J.AST.2015.11.014. [4] W.
- Lu, J.
- Li, J.
- Miao, L.
- Chen, J.
- Wei, J.
- Liu, C.

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
