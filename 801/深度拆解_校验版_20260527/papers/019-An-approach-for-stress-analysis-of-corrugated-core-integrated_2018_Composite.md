# 论文深度拆解：An approach for stress analysis of corrugated-core integrated thermal protection system under thermal and mechanical environment

> 生成依据：`801/cleantext/019-An-approach-for-stress-analysis-of-corrugated-core-integrated_2018_Composite`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`019-An-approach-for-stress-analysis-of-corrugated-core-integrated_2018_Composite`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-approach-for-stress-analysis-of-corrugated-core-integrated_2018_Composite.pdf`
- 页数：26
- clean body 字符数：78933
- 摘要字符数：1063
- 参考文献条数：14
- 图题数：36
- 表题数：0
- 表格文件数：1
- 公式候选数：454
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "7 formula(s) need manual review."}]

## 1. 身份层

- 标题：An approach for stress analysis of corrugated-core integrated thermal protection system under thermal and mechanical environment
- 年份：2018
- 期刊/来源：Composite
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results. The characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design. In this section, the equivalent properties with temperature-dependent material properties needed to model a trapezoidal corrugated core are introduce
- 主要方法：The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017). The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets. The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
- 主要证据：图表 36 个标题、公式 454 个候选、参考文献 14 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results. The characteristic of fully reusable ”，可以通过“The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous s”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis. It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results. Until Briassoulis’s study [12] using Castigliano’s second theorem was developed, the precise of extensional and flexural rigidities of the corrugated plates was improved greatly.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results. The characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design. In this section, the equivalent properties with temperature-dependent material properties needed to model a trapezoidal corrugated core are introduced.
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
- 作者声明或文本中可见 gap：This means that the TPS not only withstands serious temperature induced by aero-heating during launch and re-entry process, but also should be required to be lightweight, easily maintained and fully reusable [3]. The 3D FEM not only captures the stress distribution accurately, but also is capable of taking into account the complicate boundary conditions and the effects of temperature-dependent material properties. However, the 3D FEM is time consuming for calculating the stress distribution of complicate geometrical structures, so that it is unable to satisfy the fast requirement of preliminary design.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017). The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets. The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
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
| The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets. | 摘要/引言/结论候选 | 图：Fig. 1. Trapezoidal corrugated core ITPS panel. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis. | 摘要/引言/结论候选 | 图：Fig. 2. Equivalent sandwich plate. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results. | 摘要/引言/结论候选 | 图：Fig. 3. The unit cell that build corrugated core. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The technology development conducts the future launch vehicle to be durable, operable and cost effective [2]. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 686.56, 293.2, 704.34)]] ⁎ Corresponding authors | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Because the traditional TPS is unable to satisfy the requirements, the integrated thermal protection system (ITPS) concept has been developed to meet these goals, which provides an integrated structural component for thermo-mechanical load bearing and thermal  | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 3, bbox (321.27, 185.6, 409.74, 200.66)]] ∫ ∫ = ⎛ | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The ITPS using metallic materials and trapezoidal corrugated cores is presented in this article. | 摘要/引言/结论候选 | 图：Fig. 1. Trapezoidal corrugated core ITPS panel. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Trapezoidal corrugated core ITPS panel. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Equivalent sandwich plate. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. The unit cell that build corrugated core. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. The deformation acting on corrugated web. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. The nomenclature of a half of unit cell and forces acting on the section. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The forces and moments acting on the bottom face sheet of two different unit cells. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Normal stresses in the mid-plane of corrugated webs subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Normal stresses in the top surface of corrugated webs subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Normal stresses in the bottom surface of corrugated webs subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. Normal stresses in the mid-plane of top face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 11. Normal stresses in the top surface of top face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. Normal stresses in the bottom surface of top face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. Normal stresses in the mid-plane of bottom face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. Normal stresses in the top surface of bottom face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Normal stresses in the bottom surface of bottom face sheet subjected to pressure loading. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (43.99, 686.56, 293.2, 704.34)]] ⁎ Corresponding authors. E-mail addresses:  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (321.27, 185.6, 409.74, 200.66)]] ∫ ∫ = ⎛ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.66, 215.47, 393.27, 234.9)]] = - E t p d C C C ( ( ) / ) y w | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (321.28, 244.98, 364.67, 259.18)]] = C | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (321.11, 274.52, 364.52, 288.72)]] = C | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (321.09, 310.02, 326.84, 318.0)]] = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.59, 435.65, 392.52, 447.35)]] where, = + ′ + z z z z | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 450.31, 391.27, 467.12)]] when ⩽ < + z z l z z (2) 2 l u (2) (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017). The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets. For the top face sheet of ITPS, the local displacement induced by out-of-plane pressure is taken into account in the prediction of stress. And for the bottom face sheet of ITPS, the local displacement induced by corrugated webs is also considered by treating the sheet as beams with proper dis- placement compatibility. The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis. It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.

### 7.4 摘要中文翻译

> （机器翻译失败，保留英文原文供复核。）The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017). The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets. For the top face sheet of ITPS, the local displacement induced by out-of-plane pressure is taken into account in the prediction of stress. And for the bottom face sheet of ITPS, the local displacement induced by corrugated webs is also considered by treating the sheet as beams with proper dis- placement compatibility. The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis. It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusions

> This paper deals with the stress analysis of trapezoidal corrugated core ITPS panel subjected to thermal and mechanical loads. The equivalent rigidities method with temperature-dependent material properties and the ${\mathsf{C}} ^ {0}$ higher-order layerwise theory for equivalent sandwich plate introduced in our previous study [1] are used in this paper. By combining the equivalent sandwich model with the principle of structural mechanics, the normal and in-plane shear stress in corrugated webs, top face sheet and bottom face sheet are calculated, respectively. And the stresses induced by local deformations are considered in the prediction of stress. The comparisons between the results obtained by the present method and the FEM results have shown that the present method gives acceptable results for stress of ITPS panel subjected to thermal and mechanical loads. Otherwise, the present method is simpler and accurately, which can give a further economy for predicting stress distribution of ITPS panel.
> 
> (b). σ×x=02m 
> (d). $\sigma _ {y y} ^ {\mathsf{m}} , \mathsf{x} {=} 0.2 \mathsf{m}$
> 
> (c). $\pmb {\sigma} _ {y y} ^ {z 1} , \pmb {x} {=} \pmb {0} . 4 \pmb {\mathrm{m}}$
> 
> (d). ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {Z 1} ,$ x=0.2m
> 
> (c). ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {z _ {2}} ,$ x=0.4m
> 
> (b). σx x=0.2m
> 
> (c). ${\sigma} _ {y y} ^ {m} ,$ x=0.4m
> 
> (c). $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$
> 
> (d). $\sigma _ {y y} ^ {z 1} , \kappa {=} 0.2 \ m$
> 
> (c). $\pmb {\sigma} _ {y y} ^ {z _ {2}} , \pmb {x} {=} \pmb {0.4 m}$
> 
> (d). $\sigma _ {\mathrm{yy}} ^ {z 2} , \kappa {=} 0.2 \ m$
> 
> (c). Bottom face sheet

### 7.6 结论中文翻译

> 本文研究了梯形波纹芯 ITPS 面板在热载荷和机械载荷下的应力分析。本文使用了具有与温度相关的材料特性的等效刚度方法和我们之前的研究[1]中介绍的等效夹层板的 ${\mathsf{C}} ^ {0}$ 高阶分层理论。将等效夹层模型与结构力学原理相结合，分别计算了波纹腹板、顶面板和底面板的法向剪应力和面内剪应力。在应力预测中考虑了局部变形引起的应力。通过本方法获得的结果与FEM结果之间的比较表明，本方法对于承受热载荷和机械载荷的ITPS面板的应力给出了可接受的结果。另外，本方法更加简单和准确，可以为预测ITPS面板的应力分布提供进一步的经济性。 （二）。 σ×x=02m(d)。 $\sigma _ {y y} ^ {\mathsf{m}} , \mathsf{x} {=} 0.2 \mathsf{m}$ (c)。 $\pmb {\sigma} _ {y y} ^ {z 1} , \pmb {x} {=} \pmb {0} 。 4 \pmb {\mathrm{m}}$ (d)。 ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {Z 1} ，$ x=0.2m (c)。 ${\mathfrak {o}} _ {\mathbf {y} \mathbf {y}} ^ {z _ {2}} ，$ x=0.4m (b)。 σx x=0.2m (c)。 ${\sigma} _ {y y} ^ {m} ，$ x=0.4m (c)。 $\sigma _ {y y} ^ {z 1} , x {=} 0.4 m$ (d)。 $\sigma _ {y y} ^ {z 1} , \kappa {=} 0.2 \ m$ (c)。 $\pmb {\sigma} _ {y y} ^ {z _ {2}} , \pmb {x} {=} \pmb {0.4 m}$ (d)。 $\sigma _ {\mathrm{yy}} ^ {z 2} , \kappa {=} 0.2 \ m$ (c)。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7617 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Homogenization method | 方法建构 | 1080 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Reduced temperature fields | 对象/条件/子问题展开 | 3085 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Equivalent elastic properties | 对象/条件/子问题展开 | 4877 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Equivalent coefficients of thermal expansion | 对象/条件/子问题展开 | 3118 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3. Layerwise theory | 对象/条件/子问题展开 | 5235 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.1. Strain-displacement relations | 对象/条件/子问题展开 | 2721 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2. Stress-strain relations | 对象/条件/子问题展开 | 5689 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.3. Finite element formulation | 方法建构 | 4898 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 3.4. Application cases | 对象/条件/子问题展开 | 1104 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4. Prediction of stress | 对象/条件/子问题展开 | 188 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.1. Stress calculation in corrugated webs of ITPS | 对象/条件/子问题展开 | 132 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1.1. Normal strain in the mid-plane of corrugated webs | 对象/条件/子问题展开 | 1673 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.1.2. Curvature in corrugated webs induced by global bending moment | 对象/条件/子问题展开 | 7690 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 4.1.3. Curvature in corrugated webs induced by transverse shear force | 对象/条件/子问题展开 | 2124 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.1.4. Shear strain in corrugated webs | 对象/条件/子问题展开 | 1180 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 4.1.5. Constitutive relationship in corrugated webs | 对象/条件/子问题展开 | 2784 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 4.2. Stress calculation in bottom and top face sheets of ITPS | 对象/条件/子问题展开 | 153 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 4.2.1. Normal strain in the mid-plane of bottom and top face sheets | 对象/条件/子问题展开 | 1015 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 4.2.2. Curvature in bottom face sheets | 对象/条件/子问题展开 | 3788 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 21 | 4.2.3. Curvature in top face sheets | 对象/条件/子问题展开 | 2179 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 22 | 4.2.4. Shear strain in bottom and top face sheets | 对象/条件/子问题展开 | 398 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 23 | 4.2.5. Constitutive relationship in bottom and top face sheets | 对象/条件/子问题展开 | 5261 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 24 | 5. Numerical examples | 对象/条件/子问题展开 | 278 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 25 | 5.1. Stress distributions of ITPS subjected to uniform transverse pressure | 对象/条件/子问题展开 | 2957 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 26 | 5.2. Stress distributions of ITPS subjected to thermal loads | 对象/条件/子问题展开 | 4769 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 27 | 6. Conclusions | 主张回收/边界说明 | 1630 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：frac(132)；array(130)；pmb(118)；delta(115)；theta(111)；tag(99)；mathrm(91)；corrugated(88)；face(87)；zeta(82)；sin(77)；sigma(75)；psi(74)；sheets(71)；end(69)；itps(66)；alpha(66)；begin(65)；bottom(61)；varepsilon(60)
- 高频学术名词/术语：temperature(32)；displacement(30)；curvature(28)；element(25)；distribution(21)；section(15)；deformation(13)；moment(13)；thickness(11)；direction(11)；y-direction(10)；pressure(9)；homogenization(8)；expansion(8)；x-direction(7)
- 高频学术动词：obtained(16)；derived(13)；presented(9)；developed(8)；predict(7)；introduced(6)；investigated(3)；investigate(1)；propose(1)；develop(1)；predicted(1)；obtain(1)；compared(1)
- 高频形容词：normal(42)；equivalent(39)；displacement(30)；thermal(26)；element(25)；leqslant(24)；partial(20)；moment(13)；trapezoidal(12)；material(12)；temperature-dependent(11)；mechanical(10)；structural(9)；local(9)；strain-displacement(7)
- 高频副词：respectively(29)；accurately(8)；simply(3)；currently(2)；easily(2)；fully(2)；rapidly(1)；greatly(1)；globally(1)；consequently(1)；effectively(1)；firstly(1)
- 高频二词短语：sin theta(77)；face sheets(66)；begin array(65)；end array(65)；pmb pmb(46)；top face(42)；corrugated webs(39)；bottom face(36)；theta sin(32)；frac sin(32)；theta frac(29)；alpha delta(29)；array tag(29)；normal stresses(25)；corrugated core(24)
- 高频三词短语：theta sin theta(32)；frac sin theta(32)；sin theta sin(31)；bottom face sheets(30)；end array tag(29)；pmb pmb pmb(28)；top face sheets(27)；sin theta frac(24)；theta frac sin(23)；top face sheet(15)；tag begin array(15)；array end array(13)
- 被动语态估计：150
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：235
- 一般过去时线索：376
- 现在完成时线索：2
- 情态动词线索：41

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
  - 可迁移句型：{object} has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
- 原句：The characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design.
  - 可迁移句型：{object} characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design.
- 原句：Therefore, homogenization technique of the corrugated panel is necessary to study.
  - 可迁移句型：{object}, homogenization technique of the corrugated panel is necessary to study.
### gap/转折句
- 原句：However, the 3D FEM is time consuming for calculating the stress distribution of complicate geometrical structures, so that it is unable to satisfy the fast requirement of preliminary design.
  - 可迁移句型：{object}, the 3D FEM is time consuming for calculating the stress distribution of complicate geometrical structures, so that it is unable to satisfy the fast requirement of preliminary design.
### 方法提出句
- 原句：The stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017).
  - 可迁移句型：{object} stress distributions in trapezoidal corrugated-core integrated thermal protection system (ITPS) under thermal and mechanical loads are predicted by employing the equivalent sandwich model introduced in our previous study (Gu et al., 2017).
- 原句：The method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets.
  - 可迁移句型：{object} method for prediction of stress based on high-order layerwise theory and the principle of structural mechanics is presented, which considers the effects of temperature-dependent material properties and curvature in sheets.
- 原句：The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
  - 可迁移句型：{object} accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
- 原句：It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
  - 可迁移句型：{object} has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
### 结果证明句
- 原句：The accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
  - 可迁移句型：{object} accuracy of the proposed method is verified by comparison with the results by three-dimensional (3D) finite element analysis.
- 原句：It has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
  - 可迁移句型：{object} has been shown that the proposed method requires sig- nificantly less computational effort and agrees well with the finite element results.
- 原句：1 and 2 shown, the ITPS panel is homogenized as an equivalent sandwich plate.
  - 可迁移句型：1 and 2 shown, the {object} panel is homogenized as an equivalent sandwich plate.
- 原句：1 shows a typical corrugated core panel with the key dimensions including the sheet thickness $h _ {1}$ and $h _ {3} ,$ the core sheet thickness $t _ {w} ,$ the core height $h _ {2} ,$ the web angle of the corrugation $\theta ,$ the core sheet spacing $p ,$ and the panel length and width a and b.
  - 可迁移句型：1 shows a typical corrugated core panel with the key dimensions including the sheet thickness $h _ {1}$ and $h _ {3} ,$ the core sheet thickness $t _ {w} ,$ the core height $h _ {2} ,$ the web angle of the corrugation $\theta ,$ the core sheet spacing $p ,$ an
### 贡献收束句
- 原句：Because the traditional TPS is unable to satisfy the requirements, the integrated thermal protection system (ITPS) concept has been developed to meet these goals, which provides an integrated structural component for thermo-mechanical load bearing and thermal protection function [4].
  - 可迁移句型：{object} the traditional TPS is unable to satisfy the requirements, the integrated thermal protection system (ITPS) concept has been developed to meet these goals, which provides an integrated structural component for thermo-mechanical load bearing and thermal
- 原句：Until Briassoulis’s study [12] using Castigliano’s second theorem was developed, the precise of extensional and flexural rigidities of the corrugated plates was improved greatly.
  - 可迁移句型：{object} Briassoulis’s study [12] using Castigliano’s second theorem was developed, the precise of extensional and flexural rigidities of the corrugated plates was improved greatly.
- 原句：Concerning the current ${\mathsf{C}} ^ {0}$ higher-order finite element, reduced integration was used for the shear terms and full integration for the in-plane terms in all cases studied.
  - 可迁移句型：{object} the current ${\mathsf{C}} ^ {0}$ higher-order finite element, reduced integration was used for the shear terms and full integration for the in-plane terms in all cases studied.
- 原句：No hourglassing modes were observed among the ones studied due to cubic approximation of the transverse displacement in the xy-plane for middle layer. $\textsf {A 3} \times 3$ Gauss-Legendre integration scheme for full integration and a $2 \times 2$ Gauss-Legendre integration scheme for reduced integration are required, respectively.
  - 可迁移句型：{object} hourglassing modes were observed among the ones studied due to cubic approximation of the transverse displacement in the xy-plane for middle layer. $\textsf {A 3} \times 3$ Gauss-Legendre integration scheme for full integration and a $2 \times 2$ Gaus
### 边界/谨慎句
- 原句：The technology development conducts the future launch vehicle to be durable, operable and cost effective [2].
  - 可迁移句型：{object} technology development conducts the future launch vehicle to be durable, operable and cost effective [2].
- 原句：Future space vehicles require more advanced thermal protection system (TPS) than the one currently used.
  - 可迁移句型：{object} space vehicles require more advanced thermal protection system (TPS) than the one currently used.
- 原句：This means that the TPS not only withstands serious temperature induced by aero-heating during launch and re-entry process, but also should be required to be lightweight, easily maintained and fully reusable [3].
  - 可迁移句型：{object} means that the TPS not only withstands serious temperature induced by aero-heating during launch and re-entry process, but also should be required to be lightweight, easily maintained and fully reusable [3].
- 原句：The characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design.
  - 可迁移句型：{object} characteristic of fully reusable is the key feature for the future vehicle, hence a precise and rapidly stress analysis of the ITPS under thermal and mechanical loads is important in the reliable design.

## 9. 引用风险层

- 正文引用簇估计：42
- 参考文献条数：14
- 可识别年份条目数：15
- 2021 年及以后参考文献数：1
- 2010 年以前经典文献数：11
- 高频来源粗略识别：Compos Struct(1)；J Spacecraft Rockets(1)；AIAA J(1)；Finite element analysis of doubly cor- rugated shells. J Struct Div ASCE(1)；Equivalent orthotropic properties of corrugated sheets. Comput Struct(1)；Transverse stiffness of a sinusoidally corrugated plate. Mech Struct Mach(1)；Finite element static and dynamic analyses of folded plates. Eng Struct(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Gu Liangxian, Wang Yifan, Shi Shengbo, Dai Cunxi. An approach for bending and transient dynamic analysis of integrated thermal protection system with tempera- ture-dependent material properties. Compos Struct 2017;159:128–43.
- [2] Blosser ML. Development of advanced metallic thermal-protection-system prototype hardware. J Spacecraft Rockets 2004;41(2):183–94.
- [3] Martinez OA, Sankar BV, Haftka RT. Micromechanical analysis of composite cor- rugated-core sandwich panels for integral thermal protection systems. AIAA J 2007;45(9):2323–36.
- [4] Martinez OA, Bapanapalli SK, Sankar BV. Micromechanical analysis of composite truss-core sandwich panels for integral thermal protection systems. In: 47th AIAA/ ASME/ASCE/AHS/ASC Structures, structural dynamics, and materials conference, Newport, Rhode Island, May. 1–4, 2006.
- [5] Bapanapalli SK. Analysis and design of corrugated-core sandwich panels for thermal protection system of space vehicles. In: 47th AIAA Structures, Structural Dynamics and Materials Conference, Newport, Rhode Island, May 1–4, 2006.
- [6] Sharma A. Multi-fidelity design of an integrated thermal protection system for spacecraft reentry. In: 49th AIAA Structures, Structural Dynamics and Materials Conference, Schaumburg, April 7–10; 2008.
- [7] Rajesh KB. Bending, vibration and vibro-acoustic analysis of composite sandwich plates with corrugated core. University of Michigan-Dearborn; 2014. [Ph.D. thesis].
- [8] Ravishankar B, Sankar BV, Haftka RT. Homogenization of integrated thermal pro- tection system with rigid insulation bars. In: 47th AIAA/ASME/ASCE/AHS/ASC Structures, structural dynamics, and materials conference, Orlando, Florida, April. 12–15; 2010.
- [9] Seydel EB. Schubknickversuchemit Wellblechtafeln, Jahrbuch d. Deutsch. Versuchsanstalltfür Luftfahrt. E.V. München und Berlin; 1931. p. 233–35.
- [10] McFarland DE. An investigation of the static stability of corrugated rectangular plates loaded in pure shear [PhD. thesis]. KS: University of Kansas, Lawrence; 1967.
- [11] Mang AH, Girya-Vallabhan VC, Smith HJ. Finite element analysis of doubly cor- rugated shells. J Struct Div ASCE 1976;102:2033–50.
- [12] Briassoulis D. Equivalent orthotropic properties of corrugated sheets. Comput Struct 1986;23(2):129–38.
- [13] Shimansky RA, Lele MM. Transverse stiffness of a sinusoidally corrugated plate. Mech Struct Mach 1995;23(3):439–51.
- [14] Samanta A, Mukhopadhyay M. Finite element static and dynamic analyses of folded plates. Eng Struct 1999;21:277–87.

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
