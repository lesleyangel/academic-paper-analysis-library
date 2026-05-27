# 论文深度拆解：An enhanced temperature field inversion model by POD-BPNN-GA method for a 3D wing with limited sensors

> 生成依据：`801/cleantext/024-An-enhanced-temperature-field-inversion-model-_2025_International-Communicat`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`024-An-enhanced-temperature-field-inversion-model-_2025_International-Communicat`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\An-enhanced-temperature-field-inversion-model-_2025_International-Communicat.pdf`
- 页数：19
- clean body 字符数：65960
- 摘要字符数：1379
- 参考文献条数：65
- 图题数：21
- 表题数：8
- 表格文件数：9
- 公式候选数：171
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "6 formula(s) need manual review."}]

## 1. 身份层

- 标题：An enhanced temperature field inversion model by POD-BPNN-GA method for a 3D wing with limited sensors
- 年份：2025
- 期刊/来源：International Communicat
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4]. Since the inversion results of $\mathbf {T} _ {\mathrm{d}}$ and $\mathbf {T} _ {\mathbf {u}}$ need to be compared and analyzed in the subsequent study, it is necessary to standardize the number of reconstruction modes.
- 主要方法：In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality. The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 主要证据：图表 29 个标题、公式 171 个候选、参考文献 65 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature”，可以通过“In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. The model is trained by the Back Propagation Neural Network method wit”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise. The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods. With the development of artificial intelligence, machine learning methods such as Neural Networks (NN) and Random Forest (RF) have shown great potential in the TFI problem due to their capability to effectively characterize complex nonlinear relationships [13–15].
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4]. Since the inversion results of $\mathbf {T} _ {\mathrm{d}}$ and $\mathbf {T} _ {\mathbf {u}}$ need to be compared and analyzed in the subsequent study, it is necessary to standardize the number of reconstruction modes.
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
- 作者声明或文本中可见 gap：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors. The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9]. Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4].
- The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
- Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
- Lu et al. [4] proposed a 3D TFI model based on NN to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality. The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
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
| In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. | 摘要/引言/结论候选 | 图：Fig. 1. The wing model with HT paths. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy | 摘要/引言/结论候选 | 图：Fig. 2. Conceptual flow for solution of the TFI problem. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient regio | 摘要/引言/结论候选 | 图：Fig. 3. Max reconstruction error of temperature data by POD. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison  | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations. | 摘要/引言/结论候选 | 表：Table 3 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the development of artificial intelligence, machine learning methods such as Neural Networks (NN) and Random Forest (RF) have shown great potential in the TFI problem due to their capability to effectively characterize complex nonlinear relationships [13– | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.16, 242.49, 223.92)]] Jia-Xin Hu , Jian-Jun Gou *, Chun-Li | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The wing model with HT paths. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 2. Conceptual flow for solution of the TFI problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Max reconstruction error of temperature data by POD. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4. Basic temperature and first 5 POD modes of and. The unit is K. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 5. The performance of TFI models with different max epochs. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. Distributions and errors of Tu. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 7. Box plots of performance with different widths and depths. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Box plots of performance with different dimensionalities of input and output. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. The optimization process of sensor layout. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. The sensor layouts of the effective individuals. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Box plots of performance with different numbers of regression trees. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Box plots of performance with different minimum leaf sizes. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Box plots of performance with different dimensionalities of input. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The optimization result by RF method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Performance of Sample 1 in Case 1 (POD-BPNN-GA model). | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 206.16, 242.49, 223.92)]] Jia-Xin Hu , Jian-Jun Gou *, Chun-Lin Gong | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 202.04, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (37.59, 695.66, 226.03, 707.39)]] https://doi.org/10.1016/j.icheatmasstransfer.2025.108778 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 3, bbox (38.95, 491.58, 117.95, 519.83)]] Min : Tgeoav = ( 1 \|Ω\| | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (77.78, 519.06, 121.87, 539.72)]] ki∇TidΩ = ∫ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (306.6, 372.41, 557.68, 385.44)]] T ≈Tθ = fθ(Ts) (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (307.96, 491.41, 410.54, 533.12)]] find θ, xs, ys, zs min ‖Tθ(xs, ys, zs, Ts) -Tori ‖1 s.t | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 655.08, 60.9, 678.99)]] T0 = 1 n | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors. In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality. The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise. A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient region. The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.

### 7.4 摘要中文翻译

> 由于真实数据只能通过非常有限的本地传感器获取，全球温度的准确反演对于高速飞行器的状态评估至关重要。在这项工作中，针对具有热传输路径的 3D 飞机机翼结构开发了结合真实传感器数据的温度场反演模型。该模型通过反向传播神经网络方法进行训练，并使用优化的关键超参数，即最大历元、宽度、深度和数据维度。预先生成的样本温度场被完全分解为适当的正交模式，提取主要特征以形成匹配的数据维度，模型构建效率显着提高，而精度损失很小。综合考虑反演误差和成本，提出了一种混合遗传算法来同时优化传感器位置和数量，通过将传感器聚集到高温梯度区域，模型性能大大提高。测试结果表明，平均相对反演误差、平均绝对反演误差和传感器数量分别减少了0.063%、0.496K和60%，TFI模型具有良好的性能，并通过与随机森林、径向基函数神经网络和卷积神经网络方法的比较验证了TFI模型的优势。

### 7.5 结论完整摘录

识别到的结论位置：7. Conclusions

> In this work, the TFI model based on POD-BPNN-GA method is constructed to invert the temperature field of a 3D wing with HT paths. The POD method is introduced to project the sample data into proper orthogonal modes, and the principal features are extracted to reduce the data dimensionality. The BPNN method is used to realize the inversion of temperature field, and the efficiency is improved with the reducedorder samples. A hybrid optimization approach based on GA is developed to optimize the sensors numbers and locations simultaneously, and the optimal layout obtains better performance with the sensors gathering to high temperature gradient region. Compared with models based on RF, RBFNN and CNN methods, the TFI model proposed in this paper obtains superior performance.
> 
> The conclusions are as follows:
> 
> (1) The POD method effectively converts high-dimensional temperature data into low-dimensional modal coefficients, simplifying analysis while retaining the principal features of data. The dimensionality of temperature field data in this paper is reduced from 1920 to 12, with an absolute error of less than 2.5 K and a relative error of less than 1 %.
> 
> (2) For the initial layout with 60 sensors and the input dimensionality of $^ {5 ,}$ the performances of POD-BPNN model are m-MREs of 0.015 % and 0.068 %, m-MAEs of 0.103 K and 0.560 K for $\mathbf {T _ {d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively. The performances of POD-RF model are m-MREs of 2.535 % and 3.208 %, m-MAEs of 13.96 K and 20.35 K for $\mathbf {T} _ {\mathrm{d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively.
> 
> (3) The optimal layout obtained by GA includes 24 sensors gathering to high temperature and high gradient regions. For the RF method, the top 24 sensors ranked by importance are concentrated in the regions with maximum and minimum temperatures.
> 
> (4) With the optimal parameters and sensors, the performances of POD-BPNN-GA model are m-MREs of 0.014 % and 0.063 $^ {\% ,}$ m-MAEs 0.091 K and 0.496 K for $\mathbf {T _ {d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively. The performances of POD-RF model are m-MREs of 0.601 % and 1.205 $^ {\% ,}$ m-MAEs of 4.600 K and 11.47 K for $\mathbf {T _ {d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively.

### 7.6 结论中文翻译

> 在这项工作中，构建了基于POD-BPNN-GA方法的TFI模型来反演具有HT路径的3D机翼的温度场。引入POD方法将样本数据投影到适当的正交模式，并提取主要特征以降低数据维度。采用BPNN方法实现温度场反演，通过降阶样本提高效率。提出了一种基于遗传算法的混合优化方法来同时优化传感器数量和位置，并且随着传感器聚集到高温梯度区域，最佳布局获得了更好的性能。与基于RF、RBFNN和CNN方法的模型相比，本文提出的TFI模型获得了优越的性能。结论如下：（1）POD方法有效地将高维温度数据转换为低维模态系数，在简化分析的同时保留了数据的主要特征。本文温度场数据的维数由1920年降为12维，绝对误差小于2.5 K，相对误差小于1%。 (2) 对于具有 60 个传感器的初始布局和输入维度 $^ {5 ,}$，POD-BPNN 模型的性能为 $\mathbf {T _ {d}}$ 和 $\mathbf {T} _ 的 m-MRE 为 0.015 % 和 0.068 %，m-MAE 为 0.103 K 和 0.560 K分别为 {\mathrm{u}} ,$ 。对于 $\mathbf {T} _ {\mathrm{d}}$ 和 $\mathbf {T} _ {\mathrm{u}} ,$，POD-RF 模型的性能分别为 2.535 % 和 3.208 % 的 m-MRE、13.96 K 和 20.35 K 的 m-MAE。 (3) 遗传算法得到的最优布局包括24个传感器聚集到高温高梯度区域。
> 
> （机器翻译失败，保留英文原文供复核。）For the RF method, the top 24 sensors ranked by importance are concentrated in the regions with maximum and minimum temperatures. (4) With the optimal parameters and sensors, the performances of POD-BPNN-GA model are m-MREs of 0.014 % and 0.063 $^ {\% ,}$ m-MAEs 0.091 K and 0.496 K for $\mathbf {T _ {d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively. The performances of POD-RF model are m-MREs of 0.601 % and 1.205 $^ {\% ,}$ m-MAEs of 4.600 K and 11.47 K for $\mathbf {T _ {d}}$ and $\mathbf {T} _ {\mathrm{u}} ,$ respectively.

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7983 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The wing with HT paths and initial sensor layout | 对象/条件/子问题展开 | 4906 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Mathematical description of TFI problem | 对象/条件/子问题展开 | 2374 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. POD-based data dimensionality reduction | 对象/条件/子问题展开 | 4312 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.2. BPNN-based temperature field inversion | 对象/条件/子问题展开 | 2591 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.3. GA-based sensor layout optimization | 对象/条件/子问题展开 | 4044 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4.1. ROMs of temperature field data with POD method | 方法建构 | 3071 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 4.2. TFI model construction with POD-BPNN method | 方法建构 | 1150 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.2.1. The determination of max epochs | 对象/条件/子问题展开 | 4043 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.2.2. The determination of width and depth | 对象/条件/子问题展开 | 1325 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2.3. The determination of data dimensionality | 对象/条件/子问题展开 | 3272 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. Sensor layout optimization by GA | 对象/条件/子问题展开 | 3574 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.1. RF-based temperature field inversion method | 方法建构 | 5131 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 14 | 5.2. The construction of POD-RF model | 方法建构 | 885 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 5.2.1. The determination of regression trees | 对象/条件/子问题展开 | 1222 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5.2.2. The determination of minimum leaf size | 对象/条件/子问题展开 | 833 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 5.2.3. The determination of data dimensionality | 对象/条件/子问题展开 | 2515 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 5.2.4. Sensor layout optimization | 对象/条件/子问题展开 | 1180 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 6.1. Comparison of performance | 结果验证/讨论 | 2860 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 20 | 6.2. Performance of POD-BPNN-GA model | 方法建构 | 3392 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 21 | 6.3. Performance of POD-RF model | 方法建构 | 1515 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 22 | 7. Conclusions | 主张回收/边界说明 | 2258 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 23 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 274 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathbf(239)；mathrm(153)；data(82)；temperature(80)；inversion(75)；performance(70)；sensor(62)；fig(57)；layout(48)；optimization(42)；training(41)；pod(41)；dimensionality(37)；case(36)；field(34)；tfi(34)；sensors(33)；number(33)；input(32)；pmb(32)
- 高频学术名词/术语：temperature(80)；inversion(75)；performance(70)；optimization(42)；dimensionality(37)；regression(22)；importance(22)；reduction(21)；influence(16)；feature(15)；generation(12)；information(11)；reconstruction(10)；section(10)；distribution(9)
- 高频学术动词：obtained(26)；introduced(11)；constructed(8)；construct(8)；developed(5)；optimize(5)；indicate(5)；compared(5)；optimized(4)；obtain(4)；reveal(3)；evaluate(3)；compare(3)；predict(1)；derive(1)
- 高频形容词：initial(22)；optimal(19)；relative(14)；table(12)；high-dimensional(10)；computational(10)；thermal(9)；variable(9)；objective(8)；total(8)；original(8)；independent(8)；coefficient(7)；represent(7)；principal(6)
- 高频副词：respectively(31)；slightly(6)；significantly(6)；relatively(4)；especially(4)；similarly(4)；additionally(4)；randomly(4)；effectively(3)；simultaneously(3)；generally(3)；approximately(3)
- 高频二词短语：mathbf mathbf(63)；mathbf mathrm(49)；mathrm mathrm(42)；sensor layout(36)；temperature field(30)；box plots(25)；inversion performance(20)；initial sensor(16)；dimensionality reduction(15)；sensor data(14)；pmb varphi(14)；mathrm mathbf(13)；test set(13)；training time(13)；tfi problem(12)
- 高频三词短语：mathrm mathrm mathrm(17)；mathbf mathbf mathbf(15)；initial sensor layout(14)；mathbf mathrm respectively(9)；sensor layout optimization(8)；temperature field data(8)；mathbf mathbf mathrm(8)；mathbf mathrm mathbf(8)；minimum leaf size(8)；mathrm mathbf mathrm(6)；box plots time(6)；plots time box(6)
- 被动语态估计：159
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：352
- 一般过去时线索：335
- 现在完成时线索：1
- 情态动词线索：73

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
  - 可迁移句型：{object} model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
- 原句：Since the inversion results of $\mathbf {T} _ {\mathrm{d}}$ and $\mathbf {T} _ {\mathbf {u}}$ need to be compared and analyzed in the subsequent study, it is necessary to standardize the number of reconstruction modes.
  - 可迁移句型：{object} the inversion results of $\mathbf {T} _ {\mathrm{d}}$ and $\mathbf {T} _ {\mathbf {u}}$ need to be compared and analyzed in the subsequent study, it is necessary to standardize the number of reconstruction modes.
### gap/转折句
- 原句：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
  - 可迁移句型：{object} inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
- 原句：The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4].
  - 可迁移句型：{object} extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4].
- 原句：The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
  - 可迁移句型：{object} TFI problem studied in This study focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
- 原句：Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
  - 可迁移句型：{object} et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in 
### 方法提出句
- 原句：In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths.
  - 可迁移句型：{object} This study, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths.
- 原句：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
  - 可迁移句型：{object} model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
- 原句：The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
  - 可迁移句型：{object} pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little acc
- 原句：A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient region.
  - 可迁移句型：{object} hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradien
### 结果证明句
- 原句：The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.
  - 可迁移句型：{object} test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the compar
- 原句：With the development of artificial intelligence, machine learning methods such as Neural Networks (NN) and Random Forest (RF) have shown great potential in the TFI problem due to their capability to effectively characterize complex nonlinear relationships [13–15].
  - 可迁移句型：{object} the development of artificial intelligence, machine learning methods such as Neural Networks (NN) and Random Forest (RF) have shown great potential in the TFI problem due to their capability to effectively characterize complex nonlinear relationships 
- 原句：The number of POD modes affects the accuracy of reconstruction results, and Fig.
  - 可迁移句型：{object} number of POD modes affects the accuracy of reconstruction results, and Fig.
- 原句：3 shows the maximum relative error with different number of modes.
  - 可迁移句型：3 shows the maximum relative error with different number of modes.
### 贡献收束句
- 原句：The pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
  - 可迁移句型：{object} pre-generated sample temperature fields are fully decom- posed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little acc
- 原句：A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient region.
  - 可迁移句型：{object} hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradien
- 原句：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
  - 可迁移句型：{object} present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
- 原句：Niu et al. [17] proposed an approach of light field compression and noise reduction to extract the main features of the projection matrix and improve the performance of 3D temperature field reconstruction.
  - 可迁移句型：{object} et al. [17] proposed an approach of light field compression and noise reduction to extract the main features of the projection matrix and improve the performance of 3D temperature field reconstruction.
### 边界/谨慎句
- 原句：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
  - 可迁移句型：{object} inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
- 原句：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
  - 可迁移句型：{object} present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
- 原句：The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
  - 可迁移句型：{object} TFI problem studied in This study focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
- 原句：Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
  - 可迁移句型：{object} et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in 

## 9. 引用风险层

- 正文引用簇估计：33
- 参考文献条数：65
- 可识别年份条目数：65
- 2021 年及以后参考文献数：43
- 2010 年以前经典文献数：8
- 高频来源粗略识别：J. Heat Mass Transf(8)；Sci. Technol(3)；Appl. Artif. Intell(2)；Commun. Heat Mass Transf(2)；Therm. Eng(1)；Elect. Public Opin. Parties(1)；Turbul(1)；The dimensionality of temperature field data in this paper is reduced from(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Uyanna, H.
- Najafi, Thermal protection systems for space vehicles: a review on technology development, current challenges and future prospects, Acta Astronaut. 176 (2020), https://doi.org/10.1016/j.actaastro.2020.06.047. [2] G. Lu, Z. Shi, R. Zhang, Y. Li, K.
- Zhang, Probabilistic design and optimization of thermal protection system with variable thickness based on non-uniform aerodynamic heating, Int. J. Heat Mass Transf. 225 (2024), https://doi.org/ 10.1016/j.ijheatmasstransfer.2024.125386. [3] J.-J. Gou, S.-Z. Jia, J.-X.
- Li, S.
- Xiao, C.-L.
- Gong, The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects, Aerosp. Sci. Technol. 140 (2023) 108431, https://doi.org/ 10.1016/j.ast.2023.108431. [4] D.
- Lu, C.
- Wang, Three-dimensional temperature field inversion calculation based on an artificial intelligence algorithm, Appl. Therm. Eng. 225 (2023), https://doi. org/10.1016/j.applthermaleng.2023.120237. [5] M.T. Hughes, G. Kini, S. Garimella, Status, challenges, and potential for machine learning in understanding and applying heat transfer phenomena, J. Heat Transf. 143 (2021), https://doi.org/10.1115/1.4052510. [6] S.L. Brunton, J.N. Kutz, K. Manohar, A.Y. Aravkin, K. Morgansen, J. Klemisch, N. Goebel
- Liu, H.
- Zhou, Predicting the temperature field of thermal cloaks in homogeneous isotropic multilayer materials based on deep learning, Int. J. Heat Mass Transf. 219 (2024), https://doi.org/10.1016/j. ijheatmasstransfer.2023.124849. [8] X.
- Liu, W.
- Peng, Z.
- Gong, W.
- Zhou, W.
- Yao, Temperature field inversion of heat- source systems via physics-informed neural networks, Eng. Appl. Artif. Intell. 113 (2022), https://doi.org/10.1016/j.engappai.2022.104902. [9] M.S.

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
