# 论文深度拆解：Real-time reconstruction of thermal fields from sparse sensors with a tensorized Fourier neural operator

> 生成依据：`801/cleantext/037-Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`037-Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa.pdf`
- 页数：23
- clean body 字符数：75018
- 摘要字符数：3247
- 参考文献条数：32
- 图题数：29
- 表题数：30
- 表格文件数：16
- 公式候选数：142
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "13 formula(s) need manual review."}]

## 1. 身份层

- 标题：Real-time reconstruction of thermal fields from sparse sensors with a tensorized Fourier neural operator
- 年份：2026
- 期刊/来源：International Journa
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies. Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 主要证据：图表 59 个标题、公式 142 个候选、参考文献 32 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. First, to mitigate the paucity of measurements”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction. (Zhao et al., 2014) applied Tikhonov regularization to estimate boundary heat flux and demonstrated this stabilization in practice. (Huang and He, 2022) perturbed the unknown heat flux and solved a linearized form of the governing equations to obtain temperature-to-heat-flux sensitivities and compute search step sizes, which reduced the cost of evaluating high-dimensional gradients.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
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
- 作者声明或文本中可见 gap：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information. The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured. Full-field measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies. Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
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
| To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. | 摘要/引言/结论候选 | 图：Fig. 3.1. Data-driven method for complete thermal field reconstruction. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies. | 摘要/引言/结论候选 | 图：Fig. 3.2. Illustration of replication-masking strategy. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction. | 摘要/引言/结论候选 | 图：Fig. 3.3. Schematic of Tucker tensor decomposition. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| We evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach 10.6 hypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating. | 摘要/引言/结论候选 | 表：Table 4.1 Grid independence study for the blunt-cone CFD. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Abbreviations BPNN Back-propagation neural network CFD Computational fluid dynamics CNN Convolutional neural network FCL Fully connected layer RBF Radial basis function RM Replication-masking TFNO Tensorized Fourier neural operator PINN Physics-informed neural | 摘要/引言/结论候选 | 表：Table 4.2 Reconstruction accuracy at different masking ratios (replication count = 10). | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| (Zhao et al., 2014) applied Tikhonov regularization to estimate boundary heat flux and demonstrated this stabilization in practice. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 369.07, 716.91)]] https://doi.org/10.101 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 3.1. Data-driven method for complete thermal field reconstruction. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 3.2. Illustration of replication-masking strategy. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3.3. Schematic of Tucker tensor decomposition. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3.4. Schematic of the TFNO model. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4.2. CFD computational mesh for the blunt cone. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4.1. Geometry of the blunt cone. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4.3. Heat flux distribution calculated by CFD for three test conditions. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4.4. Heat flux distribution calculated by the engineering algorithm for three test conditions. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4.7 presents the reconstructed heat flux fields for the three test states using manually specified masked measurements. This scenario was generated by mask | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 4.5. Predicted distributions for three test cases using discrete measurements, flight-state, and low-fidelity predictions. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4.6. Comparison of predictions using all inputs for the three test cases. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4.7. Reconstruction results under different masking meridians and test cases (a1–a3: 0◦, b1–b3: 90◦, c1–c3: 180◦; columns correspond to Test cases 1–3). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4.8. Heat-flux predicted using discrete measurements. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4.9. Heat-flux predicted using discrete measurements and state. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4.10. Heat-flux predicted using discrete measurements and CFD predictions. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Table 4.1 Grid independence study for the blunt-cone CFD. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.2 Reconstruction accuracy at different masking ratios (replication count = 10). | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.5 Hyperparameters of the TFNO. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.3 Reconstruction accuracy at different replication counts (masking ratio = 10%). | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.4 Reconstruction accuracy with different numbers of experimental samples. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.6 Performance evaluation of the low-fidelity RF model on different datasets. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.7 Model performance under different combinations of input types. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.8 Reconstruction accuracy and effect of different low-fidelity fields. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.9 Reconstruction accuracy of heat flux distributions across different methods. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4.10 Reconstruction accuracy of different output formulations. | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 369.07, 716.91)]] https://doi.org/10.1016/j.ijheatfluidflow. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (352.01, 437.02, 400.96, 456.67)]] H Pk] = F(X, {yH j,τ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 204.14, 560.02, 217.17)] [̂y1k, ̂y2k, ..., ̂yPk]] = F([y1k, y2k, ..., yJk]) (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (352.01, 352.5, 560.01, 367.55)]] H Pk] = F(X, [yH 1k, yH 2k, ..., yH Jk], [ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (406.83, 442.65, 442.81, 459.84)]] j=1,τ=k-d, [̂y | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 4, bbox (352.01, 390.2, 560.01, 405.3)]] L Pk] = F(X) (5) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (417.15, 56.34, 557.66, 73.71)]] j=1,τ=k-d as inputs to observe the recon | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (423.72, 118.37, 559.99, 135.68)]] j=1,τ=k-d as inputs. The thermal field | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Real-time monitoring of the heat flux and temperature of hypersonic flight vehicles is critical for safety, control, and thermal management. In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information. The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured. To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies. Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction. Third, for time-continuous reconstruction, we augment the inputs with recent measurement history to exploit temporal coherence. We evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach 10.6 hypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating. From just 9–126 sensors, it reconstructs fields on grids of 2,400–3,700 nodes with a mean relative error under 2% and an average inference latency of approximately 0.08 s.
> Abbreviations
> BPNN Back-propagation neural network
> CFD Computational fluid dynamics CNN Convolutional neural network FCL Fully connected layer RBF Radial basis function RM Replication-masking TFNO Tensorized Fourier neural operator PINN Physics-informed neural network POD Proper orthogonal decomposition RMSE Root-mean-square error Nomenclature (Latin) B Input function space b Input function C Core tensor C Fully connected layer D Spatial domain d Duration of recent measurements
> (continued on next column)
> (continued)
> BPNN Back-propagation neural network
> E Decomposition error tensor F Fourier transform operator J Number of sensors j Sensor index K Number of time steps k Time step index L Tensor dimension N Number of matrices P Number of mesh nodes p Node index q Heat flux R Tensor rank R Model parameters T Temperature t Time U Projection matrices v Feature representation
> (continued on next page)
> ☆This article is part of a special issue entitled: ‘AI-FDHT-2025’ published in International Journal of Heat and Fluid Flow.
> * Corresponding author. E-mail addresses: huangwenyu@mail.nwpu.edu.cn (H. Wenyu), chunnali@nwpu.edu.cn (L. Chunna), jj.gou@nwpu.edu.cn (G. Jianjun), maxiaobing501@163. com (M. Xiaobing), leonwood@nwpu.edu.cn (G. Chunlin).
> https://doi.org/10.1016/j.ijheatfluidflow.2026.110341 Received 15 November 2025; Received in revised form 28 January 2026; Accepted 28 February 2026
> (continued)
> BPNN Back-propagation neural network
> X Tensor X State x Input Y Output function space y Target/output Z Number of layers z Layer index Nomenclature (Greek) ​α Regularization weight δ Relative error ε Root-mean-square error φ Circumferential angle λ Distortion intensity σ Standard deviation ϖ Random noise

### 7.4 摘要中文翻译

> 实时监测高超音速飞行器的热通量和温度对于安全、控制和热管理至关重要。然而，在飞行中，传感通常仅限于稀疏分布的传感器，这会产生不完整的空间覆盖和不完整的信息。在极端环境中，例如前体前缘，情况变得更具挑战性，在这些环境中，传感器仪器不切实际，并且关键热区域仍然无法测量。为了解决这些问题，我们开发了一种基于张量傅里叶神经算子（TFNO）的增强方法，该方法可以从稀疏测量中重建完整的热场。首先，为了缓解测量的缺乏，我们提出了一种复制掩蔽策略，该策略通过随机遮挡重复副本中的一小部分传感器读数来扩展训练集。其次，如果状态信息可用，我们将其与相应的低保真数据一起输入模型以改进重建。第三，对于时间连续重建，我们用最近的测量历史来增加输入，以利用时间相干性。我们在两个任务上评估了所提出的方法：10.6 马赫高超音速流条件下的钝锥表面热通量重建和受辐射加热的 C/SiC 复合板的瞬态温度重建。只需 9-126 个传感器，它就能在 2,400-3,700 个节点的网格上重建场，平均相对误差低于 2%，平均推理延迟约为 0.08 秒。
> 
> 缩写 BPNN 反向传播神经网络 CFD 计算流体动力学 CNN 卷积神经网络 FCL 全连接层 RBF 径向基函数 RM 复制掩蔽 TFNO 张量傅里叶神经算子 PINN 物理信息神经网络 POD 正确正交分解 RMSE 均方根误差 命名法（拉丁文） B 输入函数空间 b 输入函数 C 核心张量 C 全连接层 D 空间域 d 持续时间BPNN 反向传播神经网络 E 分解误差张量 F 傅里叶变换算子 J 传感器数量 j 传感器索引 K 时间步数 k 时间步长索引 L 张量维数 N 矩阵数量 P 网格节点数 p 节点索引 q 热通量 R 张量秩 R 模型参数 T 温度 t 时间 U 投影矩阵 v 特征表示（下页继续） ☆本文是题为： “AI-FDHT-2025”发表在《国际热与流体流杂志》上。 * 通讯作者。电子邮箱地址： huangwenyu@mail.nwpu.edu.cn（H.文宇）、ch​​unnali@nwpu.edu.cn（L.春娜）、jj.gou@nwpu.edu.cn（G.建军）、maxiaobing501@163。 com（M.小兵），leonwood@nwpu.edu.cn（G.春林）。 https://doi.org/10.1016/j.ijheatfluidflow.2026.110341 2025 年 11 月 15 日收到； 2026 年 1 月 28 日收到修订版； 2026 年 2 月 28 日接受（续） BPNN 反向传播神经网络 X 张量 X 状态 x 输入 Y 输出函数空间 y 目标/输出 Z 层数 z 层索引 命名法（希腊语）​α 正则化权重 δ 相对误差 ε 均方根误差 φ 圆周角 λ 畸变强度 σ 标准偏差 ϖ 随机噪声

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work we formulated a physics-guided, data-driven inversion framework based on a TFNO for reconstructing complete thermal fields of hypersonic configurations from sparse measurements. The method integrates (i) replication-masking to harden the model against arbitrary sparse sensor layouts, (ii) multi-input fusion of discrete sensors with flight-state variables and low-fidelity (CFD) predictions for aerodynamic heating on a blunt cone, and (iii) short historical measurements to recover transient temperature fields on a radiatively heated C/SiC plate. Validation across these two representative scenarios demonstrates realtime inference and consistent improvements over traditional interpolants, conventional neural networks, and other operator backbones. The main conclusions are as follows:
> 
> • On the blunt-cone heat-flux case, fusing discrete measurements, flight-state variables, and low-fidelity CFD yields a mean relative error below 2%, and ablation studies confirm the contribution of each component.
> 
> • On the C/SiC plate temperature case, using three recent measurements at 25 s intervals reduces the mean relative error in transient temperature reconstruction to below 1.5%, whereas omitting history raises it to about 6.4%.
> 
> • The trained model infers one field in about 0.08 s, enabling online updates that meet real-time requirements. Compared with nearestneighbor interpolation, RBF interpolation, BPNN, BPNN + POD, and alternative backbones, TFNO attains the best balance between accuracy and spatial coherence on both tasks. Repeated tests with a fixed masking ratio show that the model remains accurate even when some sensors fail or at unsensed locations.

### 7.6 结论中文翻译

> 在这项工作中，我们制定了一个基于 TFNO 的物理引导、数据驱动的反演框架，用于根据稀疏测量重建高超声速配置的完整热场。该方法集成了（i）复制掩蔽以针对任意稀疏传感器布局强化模型，（ii）离散传感器与飞行状态变量的多输入融合和钝锥体上空气动力学加热的低保真度（CFD）预测，以及（iii）简短的历史测量以恢复辐射加热的 C/SiC 板上的瞬态温度场。这两个代表性场景的验证表明了实时推理以及相对于传统插值器、传统神经网络和其他算子主干的持续改进。主要结论如下： • 在钝锥体热通量情况下，融合离散测量、飞行状态变量和低保真度CFD 产生的平均相对误差低于2%，并且消融研究证实了每个组件的贡献。 • 在C/SiC 板温度情况下，以25 秒为间隔使用最近的三个测量值可将瞬态温度重建的平均相对误差降低至1.5% 以下，而忽略历史记录则将其提高至约6.4%。 • 训练后的模型在约0.08 秒内推理出一个字段，从而实现满足实时要求的在线更新。与最近邻插值、RBF 插值、BPNN、BPNN + POD 和替代骨干网络相比，TFNO 在两项任务上都实现了准确性和空间一致性之间的最佳平衡。使用固定掩蔽比的重复测试表明，即使某些传感器发生故障或位于未感测的位置，该模型仍然准确。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 11549 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Problem description | 对象/条件/子问题展开 | 4829 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3.1. Data-driven reconstruction | 对象/条件/子问题展开 | 8915 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3.2. Tensorized Fourier neural operator | 对象/条件/子问题展开 | 6326 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 4.1. Physical model | 方法建构 | 5898 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 4.2. TFNO model configuration and training | 方法建构 | 1785 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | Table 4.5 | 对象/条件/子问题展开 | 2483 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 4.3. Results | 结果验证/讨论 | 15455 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 9 | 5. Temperature distribution reconstruction for a C/SiC plate | 对象/条件/子问题展开 | 68 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 5.1. Physical model | 方法建构 | 3134 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 11 | 5.2. TFNO model configuration and training | 方法建构 | 1611 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | Table 5.3 | 对象/条件/子问题展开 | 1143 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.3. Results | 结果验证/讨论 | 9349 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 14 | 6. Conclusion | 主张回收/边界说明 | 1685 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 15 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 224 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(89)；measurements(64)；sensor(56)；field(54)；temperature(53)；data(46)；low-fidelity(44)；reconstruction(43)；widehat(40)；tfno(38)；thermal(36)；sensors(36)；accuracy(36)；input(32)；pmb(32)；fig(32)；points(30)；fields(29)；training(27)；error(27)
- 高频学术名词/术语：temperature(53)；low-fidelity(44)；reconstruction(43)；information(19)；distribution(16)；measurement(14)；smoothness(13)；prediction(12)；function(12)；replication(12)；validation(11)；performance(10)；regularization(9)；conduction(9)；generalization(9)
- 高频学术动词：predicted(8)；evaluate(8)；introduce(7)；predict(6)；evaluated(5)；obtain(4)；optimized(4)；derived(4)；compare(4)；constructed(3)；indicate(3)；compared(3)；demonstrate(3)；estimate(2)；propose(2)
- 高频形容词：thermal(36)；spatial(27)；global(23)；relative(22)；table(21)；neural(20)；mathcal(19)；physical(17)；transient(16)；measurement(14)；boundary(13)；experimental(13)；spectral(13)；available(11)；local(10)
- 高频副词：respectively(14)；effectively(8)；randomly(6)；significantly(6)；primarily(5)；spatially(5)；consequently(5)；substantially(4)；physically(4)；subsequently(4)；approximately(4)；conversely(4)
- 高频二词短语：heat flux(21)；widehat mathrm(15)；sensor locations(13)；relative error(13)；pmb mathrm(12)；mathrm widehat(12)；mean relative(10)；mathrm mathrm(10)；sparse sensor(9)；widehat pmb(9)；low-fidelity cfd(9)；sensor measurements(8)；varphi circ(8)；mathrm pmb(8)；thermal field(7)
- 高频三词短语：widehat mathrm widehat(10)；mathrm widehat mathrm(10)；mean relative error(7)；pmb mathrm pmb(6)；widehat pmb mathrm(6)；mathrm mathrm mathrm(5)；left tau mathrm(5)；tau mathrm right(5)；mathrm right tau(5)；left widehat right(5)；sum sum left(5)；sparse sensor measurements(4)
- 被动语态估计：104
- `we + 动作动词` 主动句估计：8
- 一般现在时线索：234
- 一般过去时线索：459
- 现在完成时线索：0
- 情态动词线索：28

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Real-time monitoring of the heat flux and temperature of hypersonic flight vehicles is critical for safety, control, and thermal management.
  - 可迁移句型：{object} monitoring of the heat flux and temperature of hypersonic flight vehicles is critical for safety, control, and thermal management.
- 原句：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
  - 可迁移句型：{object} situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
### gap/转折句
- 原句：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
  - 可迁移句型：{object} flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
- 原句：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
  - 可迁移句型：{object} situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
- 原句：Full-field measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
  - 可迁移句型：{object} measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
- 原句：As a result, thermal assessments are usually inferred from a few sensors placed in less extreme regions such as nonleading-edge areas.
  - 可迁移句型：{object} a result, thermal assessments are usually inferred from a few sensors placed in less extreme regions such as nonleading-edge areas.
### 方法提出句
- 原句：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements.
  - 可迁移句型：{object} address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements.
- 原句：First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies.
  - 可迁移句型：{object}, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies.
- 原句：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
  - 可迁移句型：{object}, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 原句：We evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach 10.6 hypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating.
  - 可迁移句型：{object} evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach 10.6 hypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating.
### 结果证明句
- 原句：(Zhao et al., 2014) applied Tikhonov regularization to estimate boundary heat flux and demonstrated this stabilization in practice.
  - 可迁移句型：({object} et al., 2014) applied Tikhonov regularization to estimate boundary heat flux and demonstrated this stabilization in practice.
- 原句：The profiles reproduce the near-stagnation peak and the subsequent axial decay, remain smooth, and show effective suppression of nonphysical oscillations.
  - 可迁移句型：{object} profiles reproduce the near-stagnation peak and the subsequent axial decay, remain smooth, and show effective suppression of nonphysical oscillations.
- 原句：The 180◦ meridian shows a middle level of percentage error due to its larger amplitudes and stronger gradients near the nose.
  - 可迁移句型：{object} 180◦ meridian shows a middle level of percentage error due to its larger amplitudes and stronger gradients near the nose.
- 原句：Taken together, the close match in both level and slope demonstrates that the model captures the axial attenuation law and the azimuthal redistribution of heating, rather than merely fitting sensor points.
  - 可迁移句型：{object} together, the close match in both level and slope demonstrates that the model captures the axial attenuation law and the azimuthal redistribution of heating, rather than merely fitting sensor points.
### 贡献收束句
- 原句：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements.
  - 可迁移句型：{object} address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements.
- 原句：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
  - 可迁移句型：{object}, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 原句：To handle high-dimensional spatiotemporal thermal fields efficiently, conjugate-gradient sequential estimation with an adjoint model provides efficient gradients and makes the optimization fast.
  - 可迁移句型：{object} handle high-dimensional spatiotemporal thermal fields efficiently, conjugate-gradient sequential estimation with an adjoint model provides efficient gradients and makes the optimization fast.
- 原句：(Huang and He, 2022) perturbed the unknown heat flux and solved a linearized form of the governing equations to obtain temperature-to-heat-flux sensitivities and compute search step sizes, which reduced the cost of evaluating high-dimensional gradients.
  - 可迁移句型：({object} and He, 2022) perturbed the unknown heat flux and solved a linearized form of the governing equations to obtain temperature-to-heat-flux sensitivities and compute search step sizes, which reduced the cost of evaluating high-dimensional gradients.
### 边界/谨慎句
- 原句：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
  - 可迁移句型：{object} flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
- 原句：Reconstructing a global thermal field (i.e., distribution) from such limited sparse measurements constitutes an inverse problem.
  - 可迁移句型：{object} a global thermal field (i.e., distribution) from such limited sparse measurements constitutes an inverse problem.
- 原句：To ensure solution stability, these methods are commonly combined with regularization.
  - 可迁移句型：{object} ensure solution stability, these methods are commonly combined with regularization.
- 原句：The physical model is a spherical-nose cone with a half-cone angle of 15◦, a base shoulder angle of 75◦, and a base radius of 152.4 mm (Cleary, 1969).
  - 可迁移句型：{object} physical model is a spherical-nose cone with a half-cone angle of 15◦, a base shoulder angle of 75◦, and a base radius of 152.4 mm (Cleary, 1969).

## 9. 引用风险层

- 正文引用簇估计：29
- 参考文献条数：32
- 可识别年份条目数：41
- 2021 年及以后参考文献数：20
- 2010 年以前经典文献数：4
- 高频来源粗略识别：Int. J. Heat Mass Transf(7)；Random forests. Mach. Learn(1)；Physics-informed neural networks for heat transfer problems. J. Heat Transfer(1)；Int. J. Therm. Sci(1)；Eng. Anal. Bound. Elem(1)；Phys. Eng. Sci(1)；Appl. Therm. Eng(1)；J. Aerosp. Eng(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Breiman, L., 2001. Random forests. Mach. Learn. 45 (1), 5–32.
- Cai, S., Wang, Z., Wang, S., et al., 2021. Physics-informed neural networks for heat transfer problems. J. Heat Transfer 143 (6), 060801. historical data entirely caused the reconstruction relative error to surge from 1.495% to 6.443%, highlighting the critical role of temporal context in solving this transient problem.
- Chanda, S., Balaji, C., Venkateshan, S.P., et al., 2017. Estimation of principal thermal conductivities of layered honeycomb composites using ANN-GA based inverse technique. Int. J. Therm. Sci. 111, 423–436.
- Chen, H., Yu, B., Zhou, H., et al., 2018. Identification of transient boundary conditions with improved cuckoo search algorithm and polynomial approximation. Eng. Anal. Bound. Elem. 95, 124–141.
- Cleary, J.W., 1969. Effects of angle of attack and bluntness on laminar heating-rate distributions of a 15 cone at a mach number of 10.6. Natl. Aeronaut. Space Administ. Faroughi S A, Pawar N, Fernandes C, et al.
- Physics-guided, physics-informed, and physics-encoded neural networks in scientific computing. arXiv preprint arXiv: 2211.07377, 2022.
- Forrester, A.I.J., S´obester, A., Keane, A.J., 2007. Multi-fidelity optimization via surrogate modelling. Proc. Royal Soc. A: Math. Phys. Eng. Sci. 463 (2088), 3251–3269. Fort S, Brock A, Pascanu R, et al. Drawing multiple augmentation samples per image during training efficiently decreases test error. arXiv preprint arXiv:2105.13343, 2021.
- Gu, J., Hong, M., Yang, Q., et al., 2023. A fast inversion approach for the identification of highly transient surface heat flux based on the generative adversarial network. Appl. Therm. Eng. 220, 119765.
- Huang, W., Gong, C., Li, C., et al., 2024. Real-time data-driven inverse heat conduction method for a reentry flight vehicle based on the random forest algorithm. J. Aerosp. Eng. 37 (1), 04023091.
- Huang, C.H., He, K.J., 2022. A steady-state inverse heat conduction-convection conjugated problem in determining unknown spatially dependent surface heat flux. Case Stud. Therm. Eng. 39, 102411.
- Huang, W., Li, C., Gong, C., et al., 2025. A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN. Aerosp. Sci. Technol. 110283.
- Islam, M.S., Dutta, P., 2025. Machine learning assisted inverse heat transfer problem to find heat flux in ablative materials. Mater. Today Commun. 45 (C).
- Jiang, X., Wang, X., Wen, Z., et al., 2023. Practical uncertainty quantification for space- dependent inverse heat conduction problem via ensemble physics-informed neural networks. Int. Commun. Heat Mass Transfer 147, 106940.
- Kong, F.J., Liu, B.R., Wang, L., et al., 2020. Comparative analysis of calculation methods for heat flux field of the quartz lamp radiant heater. Spacecraft Environ. Eng. 37 (1), 47–53.
- Koric, S., Abueidda, D.W., 2023. Data-driven and physics-informed deep learning operators for solution of heat conduction equation with parametric heat source. Int. J. Heat Mass Transf. 203, 123809. Kossaifi J, Kovachki N, Azizzadenesheli K, et al. Multi-grid tensorized fourier neural operator for high-resolution pdes. arXiv preprint arXiv:2310.00120, 2023. Li Z, Kovachki N, Azizzadenesheli K, et al. Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010

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
