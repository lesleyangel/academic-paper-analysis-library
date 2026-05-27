# 论文深度拆解：A kernel ridge regression combining nonlinear ROMs for accurate flow-field reconstruction with discontinuities

> 生成依据：`801/cleantext/002-A-kernel-ridge-regression-combining-nonlinear-ROMs-for-_2025_Aerospace-Scien`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`002-A-kernel-ridge-regression-combining-nonlinear-ROMs-for-_2025_Aerospace-Scien`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-kernel-ridge-regression-combining-nonlinear-ROMs-for-_2025_Aerospace-Scien.pdf`
- 页数：26
- clean body 字符数：49354
- 摘要字符数：1593
- 参考文献条数：36
- 图题数：56
- 表题数：3
- 表格文件数：3
- 公式候选数：147
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "33 formula(s) need manual review."}]

## 1. 身份层

- 标题：A kernel ridge regression combining nonlinear ROMs for accurate flow-field reconstruction with discontinuities
- 年份：2025
- 期刊/来源：Aerospace Scien
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. These discontinuities significantly impact the overall flow behavior and performance, demanding high-fidelity simulation tools. Therefore, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dim
- 主要方法：Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. Inspired by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features present in the flow fields.
- 主要证据：图表 59 个标题、公式 147 个候选、参考文献 36 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. These disco”，可以通过“Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. To address this challenge, a novel recon”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. Then, we combine these coefficients and modes to achieve accurate recon struction of flow fields with discontinuities. Comparison results demonstrate that the method can achieve better reconstruction accuracy than the existing approaches.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. These discontinuities significantly impact the overall flow behavior and performance, demanding high-fidelity simulation tools. Therefore, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dimensions.
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
- 作者声明或文本中可见 gap：However, the reconstruction from low- dimensional manifold coordinates to high-dimensional flow fields often introduces considerable reconstruction errors, leading to inaccurate reconstruction in the location with nonlinear flow structures, especially the region with discontinuities. However, since the sharp gradients and nonlinear nature of discontinuities are poorly approximated by the smooth modes from POD or DMD, these POD-based or DMD-based methods often struggle to accurately capture the discontinuities in the flow fields. The mathematical foundation of the kernel method lies in the concept of mapping data into a higher-dimensional space $\mathcal {H}$ and then leveraging inner products in that space to solve linear problems in place of solving the nonlinear problem in the original space $\mathcal {X}$ by the mapping function $\phi ,$ expressed as, $$\phi : \mathcal {X} \to \mathcal {H}\tag{2.7}$$ Since most of the mapping functions cannot be explicitly computed, the kernel method uses a kernel function $K ( \cdot ) \mathrm{to}$ directly compute the inner product of two samples in $\mathcal {H}$ $$K ( x , y ) = \langle \phi ( x ) , \phi ( y ) \rangle\tag{2.8}$$ which represents the similarity between x and y.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. Inspired by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features present in the flow fields.
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
| Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. | 摘要/引言/结论候选 | 图：Fig. 1. Procedure of the proposed flow-field reconstruction method. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. | 摘要/引言/结论候选 | 图：Fig. 2. Visualizations of different kernel functions. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Inspired by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features pr | 摘要/引言/结论候选 | 图：Fig. 3. Training and testing samples in the M∞-α parameter space. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Then, we combine these coefficients and modes to achieve accurate recon struction of flow fields with discontinuities. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed flow-field reconstruction method is validated through the reconstruction of transonic flow fields over the RAE2822 airfoil. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Comparison results demonstrate that the method can achieve better reconstruction accuracy than the existing approaches. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 200.1, 690.38)]] * Corresponding authors | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Procedure of the proposed flow-field reconstruction method. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Visualizations of different kernel functions. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Training and testing samples in the M∞-α parameter space. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Relative reconstruction error and Rrs of the KRR-DCR through different ML methods (cubic polynomial kernel, γ =1). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 5. Relative reconstruction error and Rrs through different kernels. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 6. Flow-field reconstruction result through linear kernel with d = 35 at M∞= 0.758 and α = 4.169∘. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 7. Relative reconstruction error and Rrs under different degrees of the polynomial kernel (base-10 logarithmic coordinate). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 8. Flow-field reconstruction through the quartic kernel with d = 17 at M∞= 0.758 and α = 4.169∘. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Relative reconstruction error and Rrs under different λ. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. Relative reconstruction error and Rrs under different γ. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 11. Wall pressure comparison by different methods for the reconstruction samples. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. Comparison of the flow fields reconstructed by different methods at M∞= 0.755, α = 2.33∘. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. Comparison of the flow fields reconstructed by different methods at M∞= 0.758, α = 4.17∘. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 14. Comparison of the flow fields reconstructed by different methods at M∞= 0.804, α = 2.05∘. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 15. Comparison of the flow fields reconstructed by different methods at M∞= 0.827, α = 5.10∘. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 200.1, 690.38)]] * Corresponding authors. E-mail address: ch | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 332.73, 716.91)]] https://doi.org/10.1016/j.ast.2025.110549  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (205.85, 350.02, 232.53, 364.9)]] ) = γaT i bj | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (205.85, 319.18, 273.73, 333.22)]] ) = exp ( - γ ‖ ai - bj‖2 F | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (205.85, 328.93, 247.83, 343.86)]] ) = tanh ( γaT i bj | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (205.85, 340.27, 235.47, 355.15)]] ) = ( γaT i bj | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (37.59, 712.39, 290.98, 725.43)]] Y = f(X) (2.1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 6, bbox (306.59, 545.27, 532.51, 558.3)]] 2.2. KRR-based discontinuity-capturing reconstruction (K | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields. However, the reconstruction from low- dimensional manifold coordinates to high-dimensional flow fields often introduces considerable reconstruction errors, leading to inaccurate reconstruction in the location with nonlinear flow structures, especially the region with discontinuities. To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities. Inspired by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features present in the flow fields. Then, we combine these coefficients and modes to achieve accurate recon struction of flow fields with discontinuities. The proposed flow-field reconstruction method is validated through the reconstruction of transonic flow fields over the RAE2822 airfoil. Comparison results demonstrate that the method can achieve better reconstruction accuracy than the existing approaches. In comparison with POD, the modes obtained via the kernel ridge regression (KRR) appear to capture the local discontinuities more precisely. This work provides an effective and highly interpretable approach for enhancing the accuracy of nonlinear ROMs in the modeling of discontinuous flow fields.

### 7.4 摘要中文翻译

> 流形学习（ML）是最具代表性的非线性降阶模型（ROM）之一，可以有效捕获整个流场的非线性流动特性。然而，从低维流形坐标到高维流场的重建往往会引入相当大的重建误差，导致在具有非线性流结构的位置，尤其是不连续的区域重建不准确。为了解决这一挑战，提出了一种基于非线性ROM的新型重建方法，以提高重建不连续流场的精度。受本征正交分解（POD）的启发，我们引入核函数来获取非线性核空间中的模态系数，并执行岭回归来构造一组有效捕获流场中存在的不连续特征的模态。然后，我们结合这些系数和模式来实现具有不连续性的流场的精确重建。通过重建 RAE2822 机翼上的跨音速流场，验证了所提出的流场重建方法。对比结果表明，该方法比现有方法能够获得更好的重建精度。与 POD 相比，通过核岭回归 (KRR) 获得的模式似乎更精确地捕获局部不连续性。这项工作为提高非线性 ROM 在不连续流场建模中的准确性提供了一种有效且高度可解释的方法。

### 7.5 结论完整摘录

识别到的结论位置：4. Conclusion

> In this paper, a new reconstruction method KRR-DCR is proposed to enhance the reconstruction accuracy of the flow fields with discontinuities. The main conclusions are drawn as follows:
> 
> 1. After dimensionality reduction by ML, we introduce the KRR to construct a set of mode coefficients and modes to nonlinearly reconstruct the flow fields from manifold coordinates. It can significantly improve the reconstruction accuracy in the discontinuous regions in comparison with the POD and NPBM.
> 
> 2. The modes constructed by the KRR-DCR show strong physical interpretability, with each mode effectively capturing the discontinuity information of its corresponding training sample.
> 
> 3. The LLE is recommended for dimensionality reduction of flow fields in the KRR-DCR, and the quartic polynomial kernel function with $\lambda {=} 10 ^ {- 5}$ and $\gamma = 1.1$ are suitable for flow-field reconstruction of the RAE2822 airfoil to achieve the minimum reconstruction error.
> 
> 4. The analysis of applicability to time-dependent problems shows that main limitations of the current KRR-DCR method include kernel sensitivity, absence of physical constraints and extrapolation vulnerability.
> 
> 5. Future works include leveraging conservation laws or governing equations into the construction of the KRR-DCR modes and exploring the feasibility of the KRR-DCR modes for building intrusive ROMs.

### 7.6 结论中文翻译

> 本文提出了一种新的重建方法KRR-DCR来提高不连续流场的重建精度。主要结论如下： 1.通过ML降维后，引入KRR构造一组模态系数和模态，从流形坐标非线性地重构流场。与POD和NPBM相比，它可以显着提高不连续区域的重建精度。 KRR-DCR构建的模态具有很强的物理可解释性，每种模态都有效地捕获了相应训练样本的不连续性信息。 KRR-DCR 中推荐使用 LLE 对流场进行降维，$\lambda {=} 10 ^ {- 5}$ 和 $\gamma = 1.1$ 的四次多项式核函数适用于 RAE2822 翼型的流场重建，以实现最小的重建误差。对瞬态问题的适用性分析表明，当前 KRR-DCR 方法的主要局限性包括核敏感性、缺乏物理约束和外推漏洞。未来的工作包括利用守恒定律或控制方程构建 KRR-DCR 模式，并探索 KRR-DCR 模式构建侵入式 ROM 的可行性。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7460 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Methodology | 方法建构 | 873 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Dimensionality reduction based on ML | 对象/条件/子问题展开 | 1266 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. KRR-based discontinuity-capturing reconstruction (KRR-DCR) | 对象/条件/子问题展开 | 2966 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Kernel method | 方法建构 | 2535 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3. Method validation and parameter analysis | 方法建构 | 1656 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3.1. Dataset generation and accuracy evaluation criterion | 对象/条件/子问题展开 | 3086 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2. Flow-field reconstruction | 对象/条件/子问题展开 | 5976 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.3. Parametric analysis of λ and $\gamma$ | 结果验证/讨论 | 2318 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 10 | 3.4. Comparison with commonly-used reconstruction methods | 方法建构 | 13550 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 3.5. Applicability to time-dependent problems | 对象/条件/子问题展开 | 5390 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4. Conclusion | 主张回收/边界说明 | 1378 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 13 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 333 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(111)；flow(96)；reconstruction(96)；fields(74)；kernel(69)；samples(57)；krr-dcr(56)；pmb(55)；nonlinear(47)；modes(44)；discontinuities(43)；fig(41)；manifold(36)；accuracy(33)；pod(31)；mean(30)；flow-field(28)；reconstructed(27)；all(27)；sample(26)
- 高频学术名词/术语：reconstruction(96)；dimensionality(20)；discontinuity(19)；reduction(18)；capture(16)；characteristics(15)；pressure(15)；function(15)；information(14)；section(10)；similarity(9)；prediction(8)；intensity(8)；temperature(8)；distribution(7)
- 高频学术动词：compared(12)；constructed(10)；obtained(9)；presented(5)；developed(4)；introduced(4)；obtain(4)；construct(4)；validate(3)；demonstrate(3)；introduce(2)；compare(2)；predict(1)；indicated(1)；demonstrated(1)
- 高频形容词：local(22)；polynomial(17)；physical(16)；original(16)；global(15)；significant(12)；low-dimensional(11)；discontinuous(11)；high-dimensional(10)；coefficient(9)；transonic(8)；relative(8)；computational(7)；temporal(7)；static(6)
- 高频副词：accurately(10)；significantly(9)；effectively(6)；respectively(5)；gradually(4)；precisely(4)；especially(3)；randomly(3)；additionally(3)；particularly(2)；rapidly(2)；generally(2)
- 高频二词短语：flow fields(70)；mathrm mean(28)；mathrm max(23)；reconstruction accuracy(23)；pmb mathrm(21)；flow field(19)；dimensionality reduction(18)；manifold coordinates(17)；mathrm nonlinear(14)；training samples(14)；kernel function(13)；flow-field reconstruction(13)；pmb pmb(12)；fields discontinuities(11)；polynomial kernel(11)
- 高频三词短语：flow fields discontinuities(11)；mathrm mean mathrm(10)；mean mathrm max(10)；mathrm max mathrm(9)；flow fields reconstructed(8)；infty alpha circ(8)；high-dimensional flow fields(7)；pmb mathrm nonlinear(7)；pmb mathbb times(6)；reconstructed flow fields(5)；original flow fields(5)；pmb mathrm new(5)
- 被动语态估计：81
- `we + 动作动词` 主动句估计：4
- 一般现在时线索：215
- 一般过去时线索：215
- 现在完成时线索：1
- 情态动词线索：42

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Therefore, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dimensions.
  - 可迁移句型：{object}, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dimensions.
### gap/转折句
- 原句：However, the reconstruction from low- dimensional manifold coordinates to high-dimensional flow fields often introduces considerable reconstruction errors, leading to inaccurate reconstruction in the location with nonlinear flow structures, especially the region with discontinuities.
  - 可迁移句型：{object}, the reconstruction from low- dimensional manifold coordinates to high-dimensional flow fields often introduces considerable reconstruction errors, leading to inaccurate reconstruction in the location with nonlinear flow structures, especially the reg
- 原句：To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
  - 可迁移句型：{object} address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
- 原句：However, since the sharp gradients and nonlinear nature of discontinuities are poorly approximated by the smooth modes from POD or DMD, these POD-based or DMD-based methods often struggle to accurately capture the discontinuities in the flow fields.
  - 可迁移句型：{object}, since the sharp gradients and nonlinear nature of discontinuities are poorly approximated by the smooth modes from POD or DMD, these POD-based or DMD-based methods often struggle to accurately capture the discontinuities in the flow fields.
- 原句：However, since the increase in $R _ {\mathrm{rs}}$ from $\lambda {=} 10 ^ {- 4}$ to $10 ^ {- 5}$ is less than $10 ^ {- 5} ,$ it can be considered practically unchanged.
  - 可迁移句型：{object}, since the increase in $R _ {\mathrm{rs}}$ from $\lambda {=} 10 ^ {- 4}$ to $10 ^ {- 5}$ is less than $10 ^ {- 5} ,$ it can be considered practically unchanged.
### 方法提出句
- 原句：Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields.
  - 可迁移句型：{object} learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields.
- 原句：To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
  - 可迁移句型：{object} address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
- 原句：Inspired by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features present in the flow fields.
  - 可迁移句型：{object} by the proper orthogonal decomposition (POD), we introduce a kernel function to obtain the mode coefficients in the nonlinear kernel space, and perform ridge regression to construct a set of modes that effectively capture the discontinuity features pr
- 原句：The proposed flow-field reconstruction method is validated through the reconstruction of transonic flow fields over the RAE2822 airfoil.
  - 可迁移句型：{object} proposed flow-field reconstruction method is validated through the reconstruction of transonic flow fields over the RAE2822 airfoil.
### 结果证明句
- 原句：Then, we combine these coefficients and modes to achieve accurate recon struction of flow fields with discontinuities.
  - 可迁移句型：{object}, we combine these coefficients and modes to achieve accurate recon struction of flow fields with discontinuities.
- 原句：Comparison results demonstrate that the method can achieve better reconstruction accuracy than the existing approaches.
  - 可迁移句型：{object} results demonstrate that the method can achieve better reconstruction accuracy than the existing approaches.
- 原句：It replaces the Euclidean distance used in MDS with the geodesic distance, allowing it to achieve a low-dimensional manifold from high-dimensional nonlinear data while simultaneously preserving both local linear structures and global nonlinear structures.
  - 可迁移句型：{object} replaces the Euclidean distance used in MDS with the geodesic distance, allowing it to achieve a low-dimensional manifold from high-dimensional nonlinear data while simultaneously preserving both local linear structures and global nonlinear structures
- 原句：1 shows the main procedure of the reconstruction procedure, and the details are introduced as follows. a) $E _ {\mathrm{mean}}$ b) $E _ {\mathrm{max}}$ c) $R _ {\mathrm{rs}}$ During the construction of the mode matrix $W _ {\mathrm{nonlinear}}$ in the above section, we use a kernel function to project manifold space into the kernel inner product space.
  - 可迁移句型：1 shows the main procedure of the reconstruction procedure, and the details are introduced as follows. a) ${object} _ {\mathrm{mean}}$ b) $E _ {\mathrm{max}}$ c) $R _ {\mathrm{rs}}$ During the construction of the mode matrix $W _ {\mathrm{nonlinear}}$ in the a
### 贡献收束句
- 原句：Manifold learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields.
  - 可迁移句型：{object} learning (ML), one of the most representative nonlinear reduced-order models (ROMs), can effectively capture the nonlinear flow characteristics of the entire flow fields.
- 原句：To address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
  - 可迁移句型：{object} address this challenge, a novel reconstruction method based on nonlinear ROMs is proposed to enhance the accuracy of reconstructing flow fields with discontinuities.
- 原句：This work provides an effective and highly interpretable approach for enhancing the accuracy of nonlinear ROMs in the modeling of discontinuous flow fields.
  - 可迁移句型：{object} study provides an effective and highly interpretable approach for enhancing the accuracy of nonlinear ROMs in the modeling of discontinuous flow fields.
- 原句：Therefore, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dimensions.
  - 可迁移句型：{object}, the development of reduced-order models (ROMs) has been motivated in recent years, aiming to capture the essential characteristics of the flow fields using a significantlyreduced number of dimensions.
### 边界/谨慎句
- 原句：The ML assumes that high-dimensional data is distributed on a low-dimensional manifold, which can capture the intrinsic features and relationships between the data.
  - 可迁移句型：{object} ML assumes that high-dimensional data is distributed on a low-dimensional manifold, which can capture the intrinsic features and relationships between the data.
- 原句：It assumes that each sample in the high-dimensional space can be reconstructed by a linear combination of its neighboring samples, and such a linear relationship can be preserved in the low-dimensional manifold space.
  - 可迁移句型：{object} assumes that each sample in the high-dimensional space can be reconstructed by a linear combination of its neighboring samples, and such a linear relationship can be preserved in the low-dimensional manifold space.
- 原句：At last, the proposed KRR-DCR method is compared with 2 commonly-used reconstruction methods and the physical significance of the modes constructed by our method is explained.
  - 可迁移句型：{object} last, the proposed KRR-DCR method is compared with 2 commonly-used reconstruction methods and the physical significance of the modes constructed by our method is explained.
- 原句：Future works include leveraging conservation laws or governing equations into the construction of the KRR-DCR modes and exploring the feasibility of the KRR-DCR modes for building intrusive ROMs.
  - 可迁移句型：{object} works include leveraging conservation laws or governing equations into the construction of the KRR-DCR modes and exploring the feasibility of the KRR-DCR modes for building intrusive ROMs.

## 9. 引用风险层

- 正文引用簇估计：22
- 参考文献条数：36
- 可识别年份条目数：54
- 2021 年及以后参考文献数：29
- 2010 年以前经典文献数：14
- 高频来源粗略识别：Fluids(7)；Sci. Technol(4)；Fluid Mech(3)；Methods Appl. Mech. Eng(2)；Rev. Fluid Mech(1)；J. Comput. Fluid Dyn(1)；Numer. Math(1)；Comput. Phys(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] G. Berkooz, P. Holmes, J.L. Lumley, The proper orthogonal decomposition in the analysis of turbulent flows, Annu. Rev. Fluid Mech 25 (1993) 539–575, https://doi. org/10.1146/annurev.fl.25.010193.002543.
- [2] C. Cao, C. Nie, S. Pan, J. Cai, K. Qu, A constrained reduced-order method for fast prediction of steady hypersonic flows, Aerosp. Sci. Technol 91 (2019) 679–690, https://doi.org/10.1016/j.ast.2019.07.016.
- [3] P. Cook, M. Firmin, M. McDonald, AGARD Report AR 138, 1979.
- [4] K. Decker, N. Iyengar, C. Perron, D. Rajaram, D. Mavris, Nonlinear multi-fidelity reduced order modeling method using manifold alignment, in: AIAA AVIATION 2021 FORUM, 2021, https://doi.org/10.2514/6.2021-3050.
- [5] M. Dellacasagrande, D. Barsi, P. Bagnerini, D. Lengani, D. Simoni, Identification of coexisting dynamics in boundary layer flows through proper orthogonal decomposition with weighting matrices, Meccanica 56 (2021) 2197–2217, https:// doi.org/10.1007/s11012-021-01367-7.
- [6] A. Ehlert, C.N. Nayeri, M. Morzynski, B.R. Noack, Locally Linear Embedding For Transient Cylinder Wakes [WWW Document], arXiv.org, 2019. URL, https://arxiv. org/abs/1906.07822v1. accessed 2.14.25.
- [7] E. Farzamnik, A. Ianiro, S. Discetti, N. Deng, K. Oberleithner, B.R. Noack, V. Guerrero, From snapshots to manifolds – a tale of shear flows, J. Fluid Mech 955 (2023) A34, https://doi.org/10.1017/jfm.2022.1039.
- [8] R.W. Floyd, Algorithm 97: shortest path, Commun ACM 5 (1962) 345, https://doi. org/10.1145/367766.368168.
- [9] T. Franz, R. Zimmermann, S. G¨ortz, N. Karcher, Interpolation-based reduced-order modelling for steady transonic flows via manifold learning, Int. J. Comput. Fluid Dyn 28 (2014) 106–121.
- [10] B. García-Archilla, V. John, S. Katz, J. Novo, POD-ROMs for incompressible flows including snapshots of the temporal derivative of the full order solution: error bounds for the pressure, J. Numer. Math 32 (2024) 301–329, https://doi.org/ 10.1515/jnma-2023-0039.
- [11] D. Gottlieb, C.-W. Shu, On the Gibbs phenomenon and its resolution, SIAM Rev. 39 (1997) 644–668, https://doi.org/10.1137/S0036144596301390.
- [12] X. Hou, J. Zhang, L. Fang, Invertible neural network combined with dynamic mode decomposition applied to flow field feature extraction and prediction, Phys. Fluids 36 (2024) 095174, https://doi.org/10.1063/5.0221740.
- [13] L. Jacquin, P. Molton, S. Deck, B. Maury, D. Soulevant, Experimental study of shock oscillation over a transonic supercritical profile, AIAa J. 47 (2009) 1985–1994, https://doi.org/10.2514/1.30190.
- [14] X. Jia, C. Gong, W. Ji, C. Li, An accuracy-enhanced transonic flow prediction method fusing deep learning and a reduced-order model, Phys. Fluids 36 (2024) 056101, https://doi.org/10.1063/5.0204152.
- [15] X. Jia, C. Li, W. Ji, C. Gong, A hybrid reduced-order model combing deep learning for unsteady flow, Phys. Fluids 34 (2022) 097112, https://doi.org/10.1063/ 5.0104848.

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
