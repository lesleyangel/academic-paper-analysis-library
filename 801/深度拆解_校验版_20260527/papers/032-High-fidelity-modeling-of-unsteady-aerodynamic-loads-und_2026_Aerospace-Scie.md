# 论文深度拆解：High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks

> 生成依据：`801/cleantext/032-High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`032-High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.pdf`
- 页数：20
- clean body 字符数：55202
- 摘要字符数：2269
- 参考文献条数：39
- 图题数：42
- 表题数：3
- 表格文件数：7
- 公式候选数：175
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "10 formula(s) need manual review."}]

## 1. 身份层

- 标题：High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks
- 年份：2026
- 期刊/来源：Aerospace Scie
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. Accurate and efficient prediction of these unsteady aerodynamic load 
- 主要方法：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynami
- 主要证据：图表 45 个标题、公式 175 个候选、参考文献 39 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, in”，可以通过“However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical i”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces. Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. Accurate and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [3,4].
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
- 作者声明或文本中可见 gap：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. However, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads. Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Data-driven approaches for unsteady aerodynamic modeling can generally be categorized as black-box or gray-box models [5,6].
- Black-box models, such as deep neural networks and operator-learning frameworks, aim to directly learn the mapping between structural motion and aerodynamic response from data [7–9].
- While flexible, these models typically require large training datasets and provide limited physical interpretability, which can reduce robustness and generalization capability under strongly coupled aeroelastic conditions [10–12].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces. As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed.
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
| This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized a | 摘要/引言/结论候选 | 图：Fig. 1. Schematic illustration of the DMS model integrating structural and aerodynamic modal spaces. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed. | 摘要/引言/结论候选 | 图：Fig. 2. Illustration of the structural-to-aerodynamic mesh projection procedure. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution. | 摘要/引言/结论候选 | 图：Fig. 3. Modeling framework of the DMS-LSTM model. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed model effectively mitigates the accuracy limitations of traditional POD-ROM under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic reg | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Lightweight and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [1,2]. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| This limitation restricts their applicability in iterative design processes and time-critical prediction scenarios, motivating the development of reduced-order models (ROMs) that balance efficiency and accuracy. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.3, 690.38)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic illustration of the DMS model integrating structural and aerodynamic modal spaces. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Illustration of the structural-to-aerodynamic mesh projection procedure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Modeling framework of the DMS-LSTM model. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. Prediction and reconstruction process of unsteady aerodynamic loads using the DMS-LSTM model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. First four structural modes of the NACA65A004 airfoil. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Aerodynamic computational mesh of the NACA65A004 airfoil. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. Steady-state pressure contour of the NACA65A004 airfoil at an angle of attack of 10◦. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Structural modal excitation signals for training set. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Structural modal excitation signals for test set. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. POD decomposition and generalized aerodynamic forces reduction of the NACA65A004 airfoil in time domain. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Predicted POD modal coefficients and corresponding absolute errors for the NACA65A004 airfoil using DMS-LSTM, DMS-OpInf, POD-LSTM and POD-OpInf. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. RMSE of predicted first 10 POD coefficients for the NACA65A004 airfoil. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 13. NSE of predicted first 10 POD coefficients for the NACA65A004 airfoil. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 14. Predicted lift coefficient for the NACA65A004 airfoil. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 15. Absolute error of predicted lift coefficient for the NACA65A004 airfoil. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.3, 690.38)]] * Corresponding author. E-mail address: leo | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 357.28, 716.91)]] https://doi.org/10.1016/j.ast.2026.111927  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (306.6, 339.73, 334.97, 357.06)]] F = ( ΦT s | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 529.84, 402.18, 543.69)]] Sp = [p1, p2, ..., pN] ∈Rna\timesN, | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (306.6, 606.25, 354.65, 622.59)]] Fi = [ Fx, Fy, Fz | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 680.19, 327.29, 704.11)]] F = 1 N | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (331.6, 697.48, 339.88, 705.95)]] i=1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (37.59, 712.4, 291.01, 725.43)]] M ¨X + C ˙X + KX = F (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by: Dr Qu Qiulin
> Rapid and accurate prediction of aerodynamic load distribution induced by structural vibrations is critical for aircraft performance evaluation and safety assurance. However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces. Since the generalized aerodynamic forces retain explicit physical property and are obtained through projection onto structural modes, the spatial integration filters out small-scale, high-frequency flow structures that are poorly correlated with structural responses. As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed. Combining DMS with Long Short-Term Memory (LSTM) neural networks yields an efficient surrogate model for predicting generalized aerodynamic forces under structural vibrations. Using the dual modal mapping matrix created in DMS, the aerodynamic load distributions can be precisely reconstructed from predicted generalized aerodynamic forces. Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution. Compared to traditional POD-LSTM models, prediction errors were reduced by 50.762 % for a 2D NACA65A004 airfoil, and 50.134 % for a 3D AGARD445.6 wing. The proposed model effectively mitigates the accuracy limitations of traditional POD-ROM under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic regime, within the tested parametric range.

### 7.4 摘要中文翻译

> 通讯人：曲秋林博士 快速、准确地预测结构振动引起的气动载荷分布对于飞机性能评估和安全保证至关重要。然而，对于这种强非定常流动预测问题，现有的基于适当正交分解（POD）的降阶模型（ROM）面临着重大挑战，包括由于模态混合现象而难以将物理输入（例如结构变形）映射到模态系数，以及由于高阶模态系数的高频振荡引起的代理建模中的收敛问题。本研究提出了一种双模态空间（DMS）模型，将结构模态和气动 POD 模态整合到统一的降维低维空间中，建立高维气动载荷场和低维广义气动力之间的映射。由于广义空气动力保留了明确的物理属性，并且是通过投影到结构模式上获得的，因此空间积分过滤掉了与结构响应相关性较差的小尺度、高频流动结构。结果，避免了模态混合现象，并且抑制了高阶气动 POD 系数中存在的高频振荡。将 DMS 与长短期记忆 (LSTM) 神经网络相结合，产生一个有效的代理模型，用于预测结构振动下的广义空气动力。使用 DMS 中创建的双模态映射矩阵，可以根据预测的广义气动力精确重建气动载荷分布。
> 
> 亚音速条件下的数值验证表明，DMS-LSTM对气动载荷分布的预测精度保持在97.2%以上。与传统的 POD-LSTM 模型相比，2D NACA65A004 翼型的预测误差减少了 50.762%，3D AGARD445.6 机翼的预测误差减少了 50.134%。所提出的模型有效地缓解了传统POD-ROM在结构振动条件下的精度限制，并且有可能在测试的参数范围内促进亚音速范围内规定结构运动的开环非定常气动载荷预测。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusion

> This paper presents a DMS-LSTM reduced-order modeling framework for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency.
> 
> The proposed Dual Modal Space (DMS) formulation couples structural modal bases with aerodynamic POD modes, enabling an explicit and bidirectional mapping between generalized aerodynamic forces and unsteady aerodynamic load distributions. By projecting aerodynamic loads onto the structural modal space, the formulation effectively mitigates modal mixing and provides a reduced representation that is well aligned with structural dynamics.
> 
> When integrated with LSTM networks, the DMS-based reduced representation facilitates efficient learning of the nonlinear temporal evolution of unsteady aerodynamic loads. Numerical investigations on a two-dimensional NACA65A004 airfoil and a three-dimensional AGARD445.6 wing demonstrate that the proposed DMS-LSTM model consistently outperforms conventional POD-LSTM approaches in both time-domain and frequency-domain metrics, achieving over 50 % reduction in surface pressure reconstruction error and up to 80.7 % improvement in lift coefficient prediction, while maintaining more than 97.2 % global reconstruction accuracy under broadband excitations and time-varying aerodynamic conditions.
> 
> The present study is limited to linear structural modal representations and open-loop aerodynamic load prediction driven by prescribed structural motions. Although nonlinear flow effects are implicitly captured through high-fidelity CFD data, the modal decompositions employed remain linear, and fully coupled aeroelastic feedback is not considered. Future work will focus on extending the proposed framework to nonlinear structural dynamics and fully coupled aeroelastic simulations, as well as incorporating adaptive modal representations and physics-informed learning strategies to enhance robustness and generalization under more complex flow conditions.

### 7.6 结论中文翻译

> 本文提出了一种 DMS-LSTM 降阶建模框架，用于预测结构振动引起的非定常气动载荷分布，并提高了准确性和物理一致性。所提出的双模态空间 (DMS) 公式将结构模态基础与气动 POD 模式耦合起来，从而实现广义气动力和非定常气动载荷分布之间的显式双向映射。通过将空气动力载荷投影到结构模态空间上，该公式有效地减轻了模态混合，并提供了与结构动力学良好一致的简化表示。当与 LSTM 网络集成时，基于 DMS 的简化表示有助于有效学习非定常空气动力载荷的非线性时间演化。对二维 NACA65A004 翼型和三维 AGARD445.6 机翼的数值研究表明，所提出的 DMS-LSTM 模型在时域和频域指标上始终优于传统的 POD-LSTM 方法，表面压力重建误差减少了 50% 以上，升力系数预测提高了 80.7%，同时在宽带激励和随时间变化的空气动力条件。目前的研究仅限于线性结构模态表示和由规定结构运动驱动的开环气动载荷预测。尽管非线性流动效应是通过高保真 CFD 数据隐式捕获的，但所采用的模态分解仍然是线性的，并且没有考虑完全耦合的气动弹性反馈。
> 
> 未来的工作将集中于将所提出的框架扩展到非线性结构动力学和全耦合气动弹性模拟，以及结合自适应模态表示和物理信息学习策略，以增强更复杂流动条件下的鲁棒性和泛化性。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6463 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Dual modal space model | 方法建构 | 561 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.1. Structural modal space | 对象/条件/子问题展开 | 4754 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.2. Aerodynamic modal space via POD | 对象/条件/子问题展开 | 3415 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. DMS by integrating structural and aerodynamic modes | 对象/条件/子问题展开 | 413 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | Step 1: Extraction and alignment of modal bases | 对象/条件/子问题展开 | 863 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | Step 2: Construction of the dual modal mapping | 对象/条件/子问题展开 | 2647 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3. DMS-LSTM surrogate modeling | 方法建构 | 7173 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4. Test case | 对象/条件/子问题展开 | 1483 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | generalized aerodynamic force | 对象/条件/子问题展开 | 62 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | aerodynamic modal space (POD components) | 对象/条件/子问题展开 | 531 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.1.1. Case setup | 对象/条件/子问题展开 | 1825 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1.2. Result and discussion | 结果验证/讨论 | 9152 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 4.1.3. Further analysis with complex excitation conditions | 结果验证/讨论 | 2194 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 15 | DMS-LSTM | 对象/条件/子问题展开 | 3205 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.2.1. Case setup | 对象/条件/子问题展开 | 1529 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 4.2.2. Result and discussion | 结果验证/讨论 | 5671 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 5. Conclusion | 主张回收/边界说明 | 1998 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 19 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 407 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(235)；phi(155)；aerodynamic(120)；structural(83)；modal(82)；pod(54)；fig(53)；generalized(48)；modes(46)；load(40)；modeling(39)；unsteady(38)；distribution(38)；times(37)；space(32)；prediction(30)；coefficients(28)；mathbb(28)；forces(26)；accuracy(26)
- 高频学术名词/术语：distribution(38)；prediction(30)；reconstruction(20)；vibration(18)；excitation(17)；pressure(16)；deformation(12)；dynamics(11)；representation(10)；performance(9)；decomposition(9)；section(9)；displacement(9)；formulation(8)；inference(7)
- 高频学术动词：predicted(11)；compared(9)；constructed(8)；obtained(7)；introduced(6)；evaluate(6)；presented(5)；evaluated(4)；demonstrate(4)；construct(3)；obtain(2)；demonstrated(1)；indicated(1)；indicate(1)；introduce(1)
- 高频形容词：aerodynamic(120)；structural(83)；modal(82)；physical(20)；coefficient(18)；temporal(14)；dominant(14)；three-dimensional(11)；computational(10)；dual(10)；two-dimensional(10)；dynamic(9)；numerical(9)；displacement(9)；table(9)
- 高频副词：significantly(10)；respectively(10)；directly(7)；consistently(6)；particularly(5)；separately(5)；approximately(5)；strongly(4)；effectively(4)；widely(3)；commonly(3)；typically(3)
- 高频二词短语：mathbf phi(130)；phi mathbf(126)；aerodynamic load(34)；generalized aerodynamic(28)；load distribution(28)；unsteady aerodynamic(25)；mathbf mathbf(25)；modal space(24)；aerodynamic forces(23)；structural modal(23)；fig fig(17)；mathbf mathbb(16)；mathbf tag(15)；aerodynamic force(14)；mathbb times(14)
- 高频三词短语：mathbf phi mathbf(119)；phi mathbf phi(117)；aerodynamic load distribution(27)；generalized aerodynamic forces(19)；unsteady aerodynamic load(15)；mathbf mathbf mathbf(11)；pod modal coefficients(10)；generalized aerodynamic force(9)；dual modal space(8)；phi mathbb times(7)；structural modal space(6)；dominant vibration modes(6)
- 被动语态估计：125
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：215
- 一般过去时线索：431
- 现在完成时线索：0
- 情态动词线索：14

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Communicated by: Dr Qu Qiulin Rapid and accurate prediction of aerodynamic load distribution induced by structural vibrations is critical for aircraft performance evaluation and safety assurance.
  - 可迁移句型：{object} by: Dr Qu Qiulin Rapid and accurate prediction of aerodynamic load distribution induced by structural vibrations is critical for aircraft performance evaluation and safety assurance.
- 原句：Accurate and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [3,4].
  - 可迁移句型：{object} and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [3,4].
- 原句：This limitation restricts their applicability in iterative design processes and time-critical prediction scenarios, motivating the development of reduced-order models (ROMs) that balance efficiency and accuracy.
  - 可迁移句型：{object} limitation restricts their applicability in iterative design processes and time-critical prediction scenarios, motivating the development of reduced-order models (ROMs) that balance efficiency and accuracy.
### gap/转折句
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  - 可迁移句型：{object}, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) t
- 原句：However, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads.
  - 可迁移句型：{object}, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads.
- 原句：Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
  - 可迁移句型：{object}, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
- 原句：Data-driven approaches for unsteady aerodynamic modeling can generally be categorized as black-box or gray-box models [5,6].
  - 可迁移句型：{object} approaches for unsteady aerodynamic modeling can generally be categorized as black-box or gray-box models [5,6].
### 方法提出句
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  - 可迁移句型：{object}, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) t
- 原句：This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
  - 可迁移句型：{object} study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generaliz
- 原句：As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed.
  - 可迁移句型：{object} a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed.
- 原句：Combining DMS with Long Short-Term Memory (LSTM) neural networks yields an efficient surrogate model for predicting generalized aerodynamic forces under structural vibrations.
  - 可迁移句型：{object} DMS with Long Short-Term Memory (LSTM) neural networks yields an efficient surrogate model for predicting generalized aerodynamic forces under structural vibrations.
### 结果证明句
- 原句：Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution.
  - 可迁移句型：{object} validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution.
- 原句：Although such POD–LSTM frameworks have shown promising performance in many unsteady flow problems, their limitations become particularly pronounced when structural vibration is involved.
  - 可迁移句型：{object} such POD–LSTM frameworks have shown promising performance in many unsteady flow problems, their limitations become particularly pronounced when structural vibration is involved.
- 原句：The illustration of the DMS model is shown in Fig.
  - 可迁移句型：{object} illustration of the DMS model is shown in Fig.
- 原句：The modeling framework shown in Fig.
  - 可迁移句型：{object} modeling framework shown in Fig.
### 贡献收束句
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  - 可迁移句型：{object}, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) t
- 原句：This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
  - 可迁移句型：{object} study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generaliz
- 原句：Compared to traditional POD-LSTM models, prediction errors were reduced by 50.762 % for a 2D NACA65A004 airfoil, and 50.134 % for a 3D AGARD445.6 wing.
  - 可迁移句型：{object} to traditional POD-LSTM models, prediction errors were reduced by 50.762 % for a 2D NACA65A004 airfoil, and 50.134 % for a 3D AGARD445.6 wing.
- 原句：Lightweight and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [1,2].
  - 可迁移句型：{object} and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [1,2].
### 边界/谨慎句
- 原句：High-fidelity computational fluid dynamics (CFD) simulations are commonly employed to resolve such fluid–structure interaction problems with high accuracy.
  - 可迁移句型：{object} computational fluid dynamics (CFD) simulations are commonly employed to resolve such fluid–structure interaction problems with high accuracy.
- 原句：While flexible, these models typically require large training datasets and provide limited physical interpretability, which can reduce robustness and generalization capability under strongly coupled aeroelastic conditions [10–12].
  - 可迁移句型：{object} flexible, these models typically require large training datasets and provide limited physical interpretability, which can reduce robustness and generalization capability under strongly coupled aeroelastic conditions [10–12].
- 原句：In contrast, gray-box ROMs embed physical knowledge into the modeling process, most commonly through modal decomposition.
  - 可迁移句型：{object} contrast, gray-box ROMs embed physical knowledge into the modeling process, most commonly through modal decomposition.
- 原句：For the threedimensional wing case, due to the significantly increased computational cost and model complexity, the comparison focuses on LSTMbased surrogate models only, namely DMS-LSTM and POD-LSTM.
  - 可迁移句型：{object} the threedimensional wing case, due to the significantly increased computational cost and model complexity, the comparison focuses on LSTMbased surrogate models only, namely DMS-LSTM and POD-LSTM.

## 9. 引用风险层

- 正文引用簇估计：5
- 参考文献条数：39
- 可识别年份条目数：53
- 2021 年及以后参考文献数：20
- 2010 年以前经典文献数：8
- 高频来源粗略识别：Fluids(4)；Rev. Fluid Mech(3)；Aerosp. Sci(2)；Fluid Mech(2)；Sci. Technol(2)；Fluids Struct(2)；Aircr(1)；The proposed Dual Modal Space(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] C. Herrmann, W. Dewulf, M. Hauschild, et al., Life cycle engineering of lightweight structures, Cirp Ann. 67 (2) (2018) 651–672, https://doi.org/10.1016/j. cirp.2018.05.008.
- 1. J058462.
- 1. J056060.
- [2] D P Wells, B L Horvath, L A McCullers, The Flight Optimization System Weights Estimation Method, National Aeronautics and Space Administration, 2017.
- [3] E. Livne, Future of airplane aeroelasticity, J. Aircr. 40 (6) (2003) 1066–1092, https://doi.org/10.2514/2.7218.
- [4] N F Giannelis, G A Vio, O. Levinski, A review of recent developments in the understanding of transonic shock buffet, Prog. Aerosp. Sci. 92 (2017) 39–84, https://doi.org/10.1016/j.paerosci.2017.05.004.
- 5. Conclusion This paper presents a DMS-LSTM reduced-order modeling frame work for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency. The proposed Dual Modal Space (DMS) formulation couples struc tural modal bases with aerodynamic POD modes, enabling an explicit and bidirectional mapping between generalized aerodynamic forces and unsteady aerodynamic load distributions. By projecting aerodynamic loads onto the str
- [5] J. Kou, W. Zhang, Data-driven modeling for unsteady aerodynamics and aeroelasticity, Prog. Aerosp. Sci. 125 (2021) 100725, https://doi.org/10.1016/j. paerosci.2021.100725.
- [6] J C Loiseau, B R Noack, S L Brunton, Sparse reduced-order modelling: sensor-based dynamics to full-state estimation, J. Fluid Mech. 844 (2018) 459–490, https://doi. org/10.1017/jfm.2018.147.
- [7] H. Bai, Z. Wang, X. Chu, et al., Data-driven modeling of unsteady flow based on deep operator network, Phys. Fluids 36 (6) (2024), https://doi.org/10.1063/ 5.0213233.
- [8] W. Ji, C. Gong, X. Jia, et al., Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning, Aerosp. Sci. Technol. 155 (2024) 109711, https://doi.org/10.1016/j.ast.2024.109711.
- [9] D. Massegur, A. Da Ronch, Recurrent graph convolutional multi-mesh autoencoder for unsteady transonic aerodynamics, J. Fluids Struct. 131 (2024) 104202, https:// doi.org/10.1016/j.jfluidstructs.2024.104202.
- [10] J. Liu, J. Liu, W. Du, et al., Performance analysis and characterization of training deep learning models on mobile device, in: 2019 IEEE 25th international conference on parallel and distributed systems (ICPADS), IEEE, 2019, pp. 506–515, https://doi.org/10.1109/ICPADS47876.2019.00077.
- [11] R W Kaszeta, T W Simon, D E Ashpis, Experimental investigation of transition to turbulence as affected by passing wakes, in: Turbo Expo: Power for Land, Sea, and Air. American Society of Mechanical Engineers 78521, 2001, https://doi.org/ 10.1115/2001-GT-0195. V003T01A069.
- [12] S. Taghizadeh, F D Witherden, Y A Hassan, et al., Turbulence closure modeling with data-driven techniques: Investigation of generalizable deep neural networks, Phys. Fluids 33 (11) (2021), https://doi.org/10.1063/5.0070890.

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
