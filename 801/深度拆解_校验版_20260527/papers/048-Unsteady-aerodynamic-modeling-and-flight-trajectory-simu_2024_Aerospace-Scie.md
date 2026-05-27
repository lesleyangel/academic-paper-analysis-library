# 论文深度拆解：Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning

> 生成依据：`801/cleantext/048-Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`048-Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.pdf`
- 页数：20
- clean body 字符数：38195
- 摘要字符数：1556
- 参考文献条数：50
- 图题数：23
- 表题数：6
- 表格文件数：8
- 公式候选数：137
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "16 formula(s) need manual review."}]

## 1. 身份层

- 标题：Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning
- 年份：2024
- 期刊/来源：Aerospace Scie
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：模型/预测 + 对比验证型
- 研究对象：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the above parameters.
- 主要方法：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow field. This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions. Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical dat
- 主要证据：图表 29 个标题、公式 137 个候选、参考文献 50 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [”，可以通过“To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously s”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data. The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile. By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the above parameters.
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
- 作者声明或文本中可见 gap：However, the efficiency is compromised by the large number of CFD calculations required. By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method. The trajectory simulation using the traditional aerodynamic interpolation table is not sufficient to meet high-fidelity simulation requirements, as it cannot accurately reflect unsteady aerodynamic characteristics.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The black-box method is a data-driven modeling method, which can build an input-output mapping model directly by a surrogate model [15] or machine learning approach [14], providing more powerful nonlinear description capabilities.
- Black-box methods, such as neural networks [25–27], can ignore physical features when constructing unsteady aerodynamic models.
- Commonly used black-box methods include radial basis function (RBF) neural networks [28,29], convolutional neural networks [30], and long short-term memory (LSTM) neural networks [31,32], etc.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow field. This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions. Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
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
| This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions. | 摘要/引言/结论候选 | 图：Fig. 1. The architecture of DNN. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed method is validated through interpolated and extrapolated prediction cases, respectively. | 摘要/引言/结论候选 | 图：Fig. 2. DNN model for aerodynamic modeling. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile. | 摘要/引言/结论候选 | 图：Fig. 3. Procedure of the pre-training and fine-tuning. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To maintain gyro stabilization while improving attack precision, the dual-spin projectile with guidance, navigation, and control (GNC) devices is developed [1,2]. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity. | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Input: training samples from the source domain and target domain Output: the DNN-TL model 1: Obtain the source domain $\mathcal {D} s = \{\pmb {x} _ {i} , \pmb {y} _ {i} \} , i = 1 , 2 , \cdots , i$ n and target domain $\mathcal {D} _ {T} = \{{\boldsymbol {x}} | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 198.0, 690.38)]] * Corresponding author. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The architecture of DNN. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. DNN model for aerodynamic modeling. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Procedure of the pre-training and fine-tuning. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The flowchart of the DNN-TL method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. The configuration of the canard dual-spin projectile. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Coordinate systems of the projectile. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Flowchart of the coupled CFD/RBD method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Variation in the error of pitching moment with respect to m and n. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 9. Variation in the prediction error of lateral force with respect to the number of neurons. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. Comparison between the predicted and high-fidelity values for the validation case. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. (continued). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Comparison of the δe by different methods for the validation case. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. Comparison of prediction results of different methods and high-fidelity results for the interpolation prediction case. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. (continued). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Comparison of δe by different methods for the interpolation predic- tion case. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 198.0, 690.38)]] * Corresponding author. E-mail address: chu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 337.94, 716.91)]] https://doi.org/10.1016/j.ast.2024.109711  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (307.96, 641.18, 346.3, 660.93)]] z(l+1) i = ∑ k | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (347.64, 646.34, 390.59, 662.16)]] W(l) ij a(l) j + b(l) i | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (336.36, 658.81, 344.68, 667.28)]] j=1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (339.59, 666.8, 359.06, 684.06)]] ( z(l+1) i | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (307.96, 669.47, 339.36, 684.06)]] a(l+1) i = σ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.59, 406.36, 557.68, 419.96)]] S(t) = [x(t -m), ..., x(t -1), x(t), y(t -n), ..., y(t  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow field. However, the efficiency is compromised by the large number of CFD calculations required. This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions. Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data. To enhance the model generalization under varying initial conditions, we fine-tune the built aerodynamic model using small amounts of data under new conditions by transfer learning. The proposed method is validated through interpolated and extrapolated prediction cases, respectively. The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile. By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.

### 7.4 摘要中文翻译

> 为了评估双旋射弹的飞行性能和气动特性，通常采用计算流体动力学和刚体动力学耦合（CFD/RBD）方法，该方法可以同时求解飞行力学和流场。然而，所需的大量 CFD 计算会影响效率。本文开发了一种结合深度神经网络和迁移学习的非定常空气动力学建模方法，可以准确预测不同初始条件下双自旋弹丸的非定常空气动力学。考虑到短期历史时刻飞行状态和气动数据的影响，我们将它们整合作为气动模型的输入特征，以减少长期历史数据的影响。为了增强不同初始条件下模型的泛化能力，我们通过迁移学习在新条件下使用少量数据对构建的空气动力学模型进行微调。分别通过内插和外推预测案例验证了所提出的方法。结果表明，该方法在双自旋弹丸非定常气动建模中比长短期记忆神经网络和自回归移动平均法具有更好的精度和泛化性。通过将飞行动力学方程与时域空气动力学模型耦合，飞行模拟只需几秒钟，与耦合的CFD/RBD方法相比，可以减少三个数量级的计算时间。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this work, an unsteady aerodynamic modeling method for dualspin projectile based on DNN and transfer learning is proposed, and three test cases are carried out to validate and assess the proposed method. Further, the aerodynamic models constructed by the proposed method are employed in flight trajectory simulation to enhance simulation efficiency. Conclusions are drawn as follows:
> 
> (a) Variation of the θ with respect to t
> 
> (b) Variation of the α with respect to t
> 
> (c) Variation of the β with respect to t
> 
> (d) Coining motion
> 
> (1) The proposed DNN-TL method can accurately model the aerodynamic characteristics of the dual-spin projectile under different initial conditions, with prediction errors of all the forces and moments smaller than 6%, but the accuracy of the proposed method decreases when applied the method to extrapolation prediction.
> 
> (2) The flight trajectory simulation of the dual-spin projectile based on the established aerodynamic model can significantly enhance simulation efficiency compared to the coupled CFD/RBD simulation, with $\delta _ {e} < 8 \%$
> 
> (3) In comparison with the commonly used ARMA method and LSTM networks, the proposed DNN-TL method exhibits a better generalization capability and higher accuracy in predicting aerodynamic forces and moments.
> 
> (a) Variation of the with respect to t
> 
> (b) Variation of the with respect to t
> 
> (c) Variation of the with respect to t
> 
> (d) Coining motion

### 7.6 结论中文翻译

> 本文提出了一种基于DNN和迁移学习的双旋弹丸非定常气动建模方法，并进行了三个测试用例来验证和评估该方法。此外，该方法构建的气动模型用于飞行轨迹仿真，以提高仿真效率。结论如下： (a) θ 相对于 t 的变化 (b) α 相对于 t 的变化 (c) β 相对于 t 的变化 (d) Coining 运动 (1) 所提出的 DNN-TL 方法可以准确地模拟不同初始条件下双自旋弹丸的气动特性，所有力和力矩的预测误差均小于 6%，但应用该方法时，该方法的精度有所下降外推预测。 (2) 基于所建立的气动模型进行双自旋弹丸飞行轨迹仿真，与耦合CFD/RBD仿真相比，仿真效率显着提高，$\delta _ {e} < 8 \%$ (3) 与常用的ARMA方法和LSTM网络相比，所提出的DNN-TL方法在预测气动力和力矩方面表现出更好的泛化能力和更高的精度。 (a) 相对于 t 的变化 (b) 相对于 t 的变化 (c) 相对于 t 的变化 (d) 铸造运动

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6874 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | Algorithm 1 | 方法建构 | 1892 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2. Aerodynamic modeling method | 方法建构 | 235 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.1. Deep neural network for aerodynamic modeling | 方法建构 | 3719 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 2.2. Transfer learning based on the pre-training | 对象/条件/子问题展开 | 1625 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 2.3. Aerodynamic modeling method based on DNN-TL | 方法建构 | 2581 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3. Samples generation of aerodynamic modeling and prediction | 方法建构 | 292 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.1. Computational model and simulation settings | 方法建构 | 922 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 3.2.1. Unsteady N-S equations | 对象/条件/子问题展开 | 1568 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.2.2. Flight dynamic equations | 对象/条件/子问题展开 | 2994 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3.2.3. Coupled CFD/RBD method | 方法建构 | 1040 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 3.3. Generation of the unsteady aerodynamic dataset | 对象/条件/子问题展开 | 909 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.1. Parameter analysis of the DNN-TL | 结果验证/讨论 | 2893 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 4.2. Aerodynamic modeling and results analysis | 方法建构 | 501 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 4.2.1. Result analysis of the validation case | 结果验证/讨论 | 1459 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 16 | 4.2.2. Result analysis of the interpolation prediction case | 结果验证/讨论 | 1835 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 17 | 4.2.3. Result analysis of the extrapolation prediction case | 结果验证/讨论 | 1509 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 4.3. Flight trajectory simulation based on aerodynamic model | 方法建构 | 447 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 19 | Algorithm 2 | 方法建构 | 1997 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 20 | 5. Conclusions | 主张回收/边界说明 | 1432 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 21 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 449 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：aerodynamic(89)；pmb(82)；simulation(38)；projectile(34)；dnn-tl(34)；flight(33)；domain(31)；prediction(30)；modeling(29)；psi(29)；unsteady(28)；moment(23)；mathrm(22)；case(22)；dual-spin(21)；accuracy(21)；fig(21)；varphi(21)；trajectory(20)；cfd(20)
- 高频学术名词/术语：simulation(38)；prediction(30)；moment(23)；velocity(10)；interpolation(10)；aerodynamics(8)；extrapolation(8)；characteristics(6)；dynamics(6)；generalization(6)；section(6)；variation(6)；equation(5)；function(5)；generation(5)
- 高频学术动词：compared(12)；obtain(9)；predicted(9)；predict(6)；obtained(5)；constructed(4)；introduced(4)；presented(4)；developed(3)；propose(1)；introduce(1)；investigate(1)；indicate(1)；estimated(1)；validate(1)
- 高频形容词：aerodynamic(89)；moment(23)；neural(12)；initial(12)；table(11)；mathcal(10)；represent(10)；lateral(7)；computational(7)；partial(5)；current(4)；axial(4)；normal(4)；vary(3)；general(3)
- 高频副词：respectively(17)；accurately(5)；commonly(4)；fully(4)；greatly(3)；randomly(3)；significantly(3)；mainly(2)；similarly(2)；finally(2)；primarily(2)；highly(1)
- 高频二词短语：pmb pmb(42)；aerodynamic modeling(19)；source domain(19)；dual-spin projectile(18)；unsteady aerodynamic(16)；cfd rbd(16)；forces moments(15)；trajectory simulation(15)；coupled cfd(15)；aerodynamic forces(14)；aft body(13)；target domain(11)；flight trajectory(10)；psi pmb(10)；prediction case(10)
- 高频三词短语：pmb pmb pmb(22)；coupled cfd rbd(15)；aerodynamic forces moments(13)；psi pmb pmb(10)；unsteady aerodynamic modeling(7)；cfd rbd simulation(7)；flight trajectory simulation(6)；rolling moment aft(6)；moment aft body(6)；end array right(6)；force lateral force(5)；aft body pitching(5)
- 被动语态估计：86
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：179
- 一般过去时线索：255
- 现在完成时线索：1
- 情态动词线索：33

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the above parameters.
  - 可迁移句型：{object} predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the abov
- 原句：To address the above issues, it is necessary to replace the CFD module in the coupled simulation with an efficient and high-accuracy aerodynamic Input layer Hidden layers Output layer model.
  - 可迁移句型：{object} address the above issues, it is necessary to replace the CFD module in the coupled simulation with an efficient and high-accuracy aerodynamic Input layer Hidden layers Output layer model.
### gap/转折句
- 原句：However, the efficiency is compromised by the large number of CFD calculations required.
  - 可迁移句型：{object}, the efficiency is compromised by the large number of CFD calculations required.
- 原句：By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
  - 可迁移句型：{object} coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
- 原句：However, the high computational cost of the CFD simulations makes the method unsuitable for engineering applications.
  - 可迁移句型：{object}, the high computational cost of the CFD simulations makes the method unsuitable for engineering applications.
- 原句：In general, unsteady aerodynamic modeling methods are categorized into two types: the white-box method and the black-box method.
  - 可迁移句型：{object} general, unsteady aerodynamic modeling methods are categorized into two types: the white-box method and the black-box method.
### 方法提出句
- 原句：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow field.
  - 可迁移句型：{object} evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow
- 原句：This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions.
  - 可迁移句型：{object} study develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin pro- jectiles under varying initial conditions.
- 原句：Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
  - 可迁移句型：{object} the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
- 原句：To enhance the model generalization under varying initial conditions, we fine-tune the built aerodynamic model using small amounts of data under new conditions by transfer learning.
  - 可迁移句型：{object} enhance the model generalization under varying initial conditions, we fine-tune the built aerodynamic model using small amounts of data under new conditions by transfer learning.
### 结果证明句
- 原句：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
  - 可迁移句型：{object} results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
- 原句：The coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
  - 可迁移句型：{object} coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
- 原句：The general architecture of a DNN [37] is shown in Fig.
  - 可迁移句型：{object} general architecture of a DNN [37] is shown in Fig.
- 原句：It indicates that incorporating more historical data into modeling will reduce model accuracy.
  - 可迁移句型：{object} indicates that incorporating more historical data into modeling will reduce model accuracy.
### 贡献收束句
- 原句：Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
  - 可迁移句型：{object} the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
- 原句：To enhance the model generalization under varying initial conditions, we fine-tune the built aerodynamic model using small amounts of data under new conditions by transfer learning.
  - 可迁移句型：{object} enhance the model generalization under varying initial conditions, we fine-tune the built aerodynamic model using small amounts of data under new conditions by transfer learning.
- 原句：By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
  - 可迁移句型：{object} coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
- 原句：The coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
  - 可迁移句型：{object} coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
### 边界/谨慎句
- 原句：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow field.
  - 可迁移句型：{object} evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled compu- tational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simulta- neously solve the flight mechanics and flow
- 原句：By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
  - 可迁移句型：{object} coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
- 原句：Commonly used white-box models include aerodynamic derivative models [16,17], differential and integral equation models [18,19], and state-space models [20].
  - 可迁移句型：{object} used white-box models include aerodynamic derivative models [16,17], differential and integral equation models [18,19], and state-space models [20].
- 原句：(3) In comparison with commonly-used LSTM networks and ARMA method, the accuracy and generalization of the proposed DNN-TL method can be obviously improved.
  - 可迁移句型：(3) {object} comparison with commonly-used LSTM networks and ARMA method, the accuracy and generalization of the proposed DNN-TL method can be obviously improved.

## 9. 引用风险层

- 正文引用簇估计：34
- 参考文献条数：50
- 可识别年份条目数：77
- 2021 年及以后参考文献数：40
- 2010 年以前经典文献数：2
- 高频来源粗略识别：Sci. Technol(6)；Fluids. Struct(2)；J. Aeronautics(1)；Aerosp. Electron. Syst(1)；Intell. Systems(1)；Aircr(1)；Build. Eng(1)；Comput. Phys(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Wang, J.
- Yu, X.
- Wang, et al., A guidance and control design with reduced information for a dual-spin stabilized projectile [J], Defence Techn. 33 (2024) 494–505, https://doi.org/10.1016/j.dt.2023.07.007. [2] J.
- Norris, A.
- Hameed, J.
- Economou, et al., A review of dual-spin projectile stability [J], Defence Techn. 16 (1) (2020) 1–9, https://doi.org/10.1016/j.dt.2019.06.003. [3] J.
- Karimi, M.R.
- Rajabi, S.H.
- Sadati, et al., Multidisciplinary design optimization of a dual-spin guided vehicle [J], Defence Techn. 37 (2023) 133–148, https://doi.org/ 10.1016/j.dt.2023.11.025. [4] Q.
- Chen, T.
- Hu, P.
- Liu, et al., The dynamic vortical flow behaviour on a coplanar canard configuration during large-amplitude-pitching [J], Aerosp. Sci. Technol. 112 (2021) 106553, https://doi.org/10.1016/j.ast.2021.106553. [5] T. Hu, Y. Zhao, P. Liu, et al., Investigation on lift characteristics of a double-delta wing pitching in various reduced frequencies [J], J. Aerospace Eng. 235 (14) (2021) 2081–2094, https://doi.org/10.1177/0954410021992201. [6] F.
- Askary, M.R Soltani, Effects of mach numbers on magnus induced surface pressure [J], Chin. J. Aeronautics 33 (12) (2020) 3058–3072, https://doi.org/ 10.1016/j.cja.2020.04.027. [7] K. Shi, M. Liu, Trajectory analysis of a dual-spin-stabilized projectile with fixed- canards for the precision guidance kit [J], J. Aerospace Eng. 236 (13) (2022) 2620–2632, https://doi.org/10.1177/09544100211064759. Table C1 Hyper-parameters of the LSTM network Hyper-parameter Value LSTM layer 200 Relu layer / Fully c
- Seve, S.
- Theodoulis, P.

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
