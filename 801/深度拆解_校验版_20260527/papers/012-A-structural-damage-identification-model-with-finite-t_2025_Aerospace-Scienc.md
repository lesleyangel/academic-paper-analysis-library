# 论文深度拆解：A structural damage identification model with finite thermomechanical sensors of the re-entry module

> 生成依据：`801/cleantext/012-A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`012-A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.pdf`
- 页数：20
- clean body 字符数：72625
- 摘要字符数：1753
- 参考文献条数：44
- 图题数：14
- 表题数：17
- 表格文件数：21
- 公式候选数：213
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "11 formula(s) need manual review."}]

## 1. 身份层

- 标题：A structural damage identification model with finite thermomechanical sensors of the re-entry module
- 年份：2025
- 期刊/来源：Aerospace Scienc
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
- 主要方法：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules. Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
- 主要证据：图表 31 个标题、公式 213 个候选、参考文献 44 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].”，可以通过“This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. First, the primary damage ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- interference ability of 1 % sensor noise are exhibited for the model. Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4]. Based on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
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
- 作者声明或文本中可见 gap：Although this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitive to damage, and poor effect of multi-damage identification. The ablation effect of thermal protection materials is typically determined through experimental measurements; however, direct and accurate calculation remains challenging [42] . The model demonstrates a remarkable accuracy of 92.6 %, with an error threshold of 0.03, and exhibits notable anti-interference capabilities, with an error rate of <1 % in the presence of random sensor noise.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules. Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
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
| This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. | 摘要/引言/结论候选 | 图：Fig. 1. The flow chart of the proposed method. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules. | 摘要/引言/结论候选 | 图：Fig. 2. Return trajectory of the re-entry module. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error. | 摘要/引言/结论候选 | 图：Fig. 3. The re-entry module structure. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Third, the damage identification model was developed with inputs of the finite nodal temperature and stress and output of structural damage value based on the back propagation neural network, and a structural damage grade evaluation equation was finally formul | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- interfere | 摘要/引言/结论候选 | 表：Table 3 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of re- entry module. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 206.16, 377.52, 223.92)]] Xiao-Bing Ma a,b, Rui  | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The flow chart of the proposed method. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Return trajectory of the re-entry module. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. The re-entry module structure. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The mesh of the heat-proof shell. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. Aerodynamic pressure and heat flux. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. The meshed structural model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. Data expansion process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Damage identification model construction. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 9. Temperature and stress fields of typical conditions. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. The raw data and expanded data. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The Train effect with and without database expansion. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Network training process. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Error distribution histogram. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 14. The residual capacity recognition value of three cases. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 12 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 13 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 206.16, 377.52, 223.92)]] Xiao-Bing Ma a,b, Rui Guo a, Hua Su a, Chu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 204.14, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 357.56, 716.91)]] https://doi.org/10.1016/j.ast.2025.110150  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 404.29, 55.79, 418.2)]] ε = σ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (51.7, 404.29, 70.81, 425.63)]] E = σ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 488.23, 74.24, 512.15)]] λ = 1 - A A0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 555.43, 291.01, 576.27)]] σ = σ 1 -λ (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (37.59, 593.96, 291.01, 617.88)]] λ = 1 -E E (4) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The re-entry module encounters extremely harsh aerodynamic pressure and heating conditions, and the high- precision identification of the structural damage state is crucial to the flight and reuse performance evalua tion. The current techniques are mainly based on complex numerical simulations or indirect sensor measure ments of finite nodes in time or space dimensions, respectively. This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules. Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error. Third, the damage identification model was developed with inputs of the finite nodal temperature and stress and output of structural damage value based on the back propagation neural network, and a structural damage grade evaluation equation was finally formulated. The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- interference ability of 1 % sensor noise are exhibited for the model. The model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of re- entry module.

### 7.4 摘要中文翻译

> 再入舱面临极其恶劣的气动压力和加热条件，结构损伤状态的高精度识别对于飞行和再利用性能评估至关重要。当前的技术主要基于复杂的数值模拟或分别在时间或空间维度上有限节点的间接传感器测量。这项工作开发了一种损伤识别模型，其中包括数值模拟、传感器测量和额外的机器学习，以获得模块的结构损伤状态。首先，通过热机械数值模拟建立了初级损伤数据库，并根据基于应变当量的刚度折减方法和一定的结构划分规则提出了结构损伤模型。其次，提出了一种基于Kriging代理模型的精度更高的数据库扩展方法，将损伤数据库扩展了10倍，误差为7%。第三，基于反向传播神经网络，建立了以有限节点温度和应力为输入，输出结构损伤值的损伤识别模型，最终建立了结构损伤等级评估方程。结果表明，该模型充分抑制了过拟合，识别误差较未扩展的原始数据降低了60%，模型识别精度高达92.6%，误差阈值为0.03，具有良好的抗1%传感器噪声干扰的能力。该模型具有较高的结构剩余能力识别效率和准确性，为再入模块的实时安全评估带来了潜力。

### 7.5 结论完整摘录

识别到的结论位置：7. Conclusions

> In this study, a damage identification model was developed for a reentry module. This model incorporated numerical simulations, sensor measurements, and machine learning algorithms. The primary damage database is established by thermomechanical numerical simulations and the strain-equivalent-based stiffness reduction method. A database expansion method based on the Kriging agent model is proposed to expand the damage database, and a damage identification model with BPNN is developed. The following conclusions were obtained:
> 
> (1) It is demonstrated that the zonal stiffness loss model can be utilized to construct the damage model of the re-entry module. Through the implementation of numerical simulations, a damage database has been constructed within the altitude range of 20 km to 80 km, effectively characterizing the extreme conditions that the re-entry module experiences during its return.
> 
> (2) The proposed database expansion method has been shown to significantly reduce the thermomechanical numerical simulation cost. The database is expanded by a factor of ten, and the expanded data can effectively simulate the distribution trend of the original simulation data with a maximum deviation of 7 %, thereby demonstrating the reliability and accuracy of the expanded data. Meanwhile, the contrast experiment of BPNN model training with and without database expansion demonstrated that based on the same simulation damage data, the identification error of the model with data expansion in the test set is 40 % of the original. And the overfitting was avoided to the greatest extent with low identification error, which further reveals the effectiveness and superiority of the database expansion method.
> 
> (3) The damage identification model’s training loss is reduced to 0.0000926, accompanied by a substantial decrease in the identification error to 0.0062, which sufficiently substantiates the convergence of the model. The model’s superior identification performance in both the training and test sets further substantiates its exemplary generalization capability. The model demonstrates a remarkable accuracy of 92.6 %, with an error threshold of 0.03, and exhibits notable anti-interference capabilities, with an error rate of <1 % in the presence of random sensor noise.

### 7.6 结论中文翻译

> 在这项研究中，为再入舱开发了损伤识别模型。该模型结合了数值模拟、传感器测量和机器学习算法。通过热机械数值模拟和基于应变当量的刚度折减方法建立了初级损伤数据库。提出一种基于Kriging代理模型的数据库扩展方法来扩展损伤数据库，并建立了基于BPNN的损伤识别模型。得到以下结论： (1)证明了可利用区域刚度损失模型构建再入舱损伤模型。通过数值模拟，建立了20公里至80公里高度范围内的损伤数据库，有效表征了再入舱返回过程中所经历的极端条件。 (2)所提出的数据库扩展方法已被证明可以显着降低热机械数值模拟成本。数据库扩容了十倍，扩容后的数据能够有效模拟原始模拟数据的分布趋势，最大偏差为7%，从而证明了扩容后数据的可靠性和准确性。同时，对带数据库扩展和不带数据库扩展的BPNN模型训练对比实验表明，基于相同的模拟损伤数据，测试集中数据扩展后的模型识别误差为原始的40%。并且最大程度地避免了过拟合，识别误差低，进一步揭示了数据库扩展方法的有效性和优越性。
> 
> （3）损伤识别模型的训练损失降低至0.0000926，识别误差大幅降低至0.0062，充分证明了模型的收敛性。该模型在训练和测试集中的卓越识别性能进一步证实了其典型的泛化能力。该模型的准确度高达 92.6%，误差阈值为 0.03，并且具有显着的抗干扰能力，在随机传感器噪声存在的情况下，误差率 <1%。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9803 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. Re-entry module and structural damage model | 方法建构 | 8073 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 3. Damage database and its expansion method | 方法建构 | 937 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1. Aerodynamic calculation model | 方法建构 | 6358 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.2. Structural heat-force coupling analysis model | 方法建构 | 801 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.2.1. Heat conduction analysis | 结果验证/讨论 | 4512 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 7 | 3.2.2. Static analysis | 结果验证/讨论 | 4168 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 8 | 3.3. Data expansion method | 方法建构 | 8401 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4. Damage identification model based on BPNN | 方法建构 | 7208 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 5. Structural strength factor and definition of damage grade | 对象/条件/子问题展开 | 1015 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 6. Results and discussions | 结果验证/讨论 | 683 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 12 | 6.1. Primary construction of the damage database | 对象/条件/子问题展开 | 1220 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 6.2. Expansion of damage database | 对象/条件/子问题展开 | 2233 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 6.3. Training of the damage identification model | 方法建构 | 9454 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 6.4. Analysis of the anti-interference ability of the model | 方法建构 | 4361 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 16 | 7. Conclusions | 主张回收/边界说明 | 2288 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 17 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 354 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：damage(157)；data(114)；identification(81)；structural(67)；module(64)；re-entry(63)；frac(62)；partial(58)；tag(56)；error(54)；sigma(45)；training(43)；sensor(41)；database(40)；heat(39)；area(38)；temperature(36)；pmb(33)；big(32)；distribution(30)
- 高频学术名词/术语：identification(81)；temperature(36)；distribution(30)；structure(29)；function(27)；element(24)；simulation(23)；calculation(23)；expansion(22)；confidence(19)；stiffness(17)；ability(15)；section(15)；capacity(14)；performance(12)
- 高频学术动词：obtained(27)；obtain(14)；constructed(13)；predicted(9)；construct(7)；demonstrated(6)；evaluate(5)；presented(3)；optimize(3)；predict(2)；indicated(2)；estimate(2)；revealed(2)；validated(2)；developed(2)
- 高频形容词：structural(67)；partial(58)；aerodynamic(29)；element(24)；neural(21)；material(20)；thermal(17)；table(17)；internal(13)；elastic(12)；residual(12)；boundary(12)；coefficient(11)；real(10)；substantial(10)
- 高频副词：finally(14)；respectively(11)；effectively(8)；consequently(5)；fully(4)；randomly(4)；extremely(3)；significantly(3)；dynamically(3)；relatively(3)；typically(3)；timely(2)
- 高频二词短语：re-entry module(55)；damage identification(34)；frac partial(28)；pmb pmb(21)；identification error(20)；partial partial(19)；structural damage(18)；neural network(17)；finite element(17)；damage data(15)；sensor data(14)；damage database(14)；heat flux(13)；begin array(13)；end array(13)
- 高频三词短语：frac partial partial(19)；pmb pmb pmb(14)；frac partial sigma(9)；partial sigma partial(9)；partial frac partial(9)；end array tag(8)；convective heat transfer(8)；structural damage identification(6)；sigma partial frac(6)；big big big(6)；distribution internal cabin(6)；sensor sensor area(5)
- 被动语态估计：210
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：273
- 一般过去时线索：497
- 现在完成时线索：3
- 情态动词线索：97

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
  - 可迁移句型：{object} damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
### gap/转折句
- 原句：Although this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitive to damage, and poor effect of multi-damage identification.
  - 可迁移句型：{object} this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitiv
- 原句：The ablation effect of thermal protection materials is typically determined through experimental measurements; however, direct and accurate calculation remains challenging [42] .
  - 可迁移句型：{object} ablation effect of thermal protection materials is typically determined through experimental measurements; however, direct and accurate calculation remains challenging [42] .
### 方法提出句
- 原句：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module.
  - 可迁移句型：{object} study developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module.
- 原句：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules.
  - 可迁移句型：{object}, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strain- equivalent-based stiffness reduction method with certain structural partition rules.
- 原句：Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
  - 可迁移句型：{object}, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
- 原句：Third, the damage identification model was developed with inputs of the finite nodal temperature and stress and output of structural damage value based on the back propagation neural network, and a structural damage grade evaluation equation was finally formulated.
  - 可迁移句型：{object}, the damage identification model was developed with inputs of the finite nodal temperature and stress and output of structural damage value based on the back propagation neural network, and a structural damage grade evaluation equation was finally for
### 结果证明句
- 原句：The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- interference ability of 1 % sensor noise are exhibited for the model.
  - 可迁移句型：{object} result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- inte
- 原句：The model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of re- entry module.
  - 可迁移句型：{object} model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of re- entry module.
- 原句：1 shows the return trajectory of the re-entry module.
  - 可迁移句型：1 shows the return trajectory of the re-entry module.
- 原句：The aerodynamic heat flux is applied on the structural boundary (as shown in Eq.
  - 可迁移句型：{object} aerodynamic heat flux is applied on the structural boundary (as shown in Eq.
### 贡献收束句
- 原句：The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- interference ability of 1 % sensor noise are exhibited for the model.
  - 可迁移句型：{object} result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good anti- inte
- 原句：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
  - 可迁移句型：{object} technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
- 原句：Based on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].
  - 可迁移句型：{object} on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].
- 原句：The boundary conditions must be provided to solve the heat conduction problem.
  - 可迁移句型：{object} boundary conditions must be provided to solve the heat conduction problem.
### 边界/谨慎句
- 原句：If minor damage couldn’t be detected in time and adopt effective countermeasures, the likelihood of a catastrophic space incident is significantly high.
  - 可迁移句型：{object} minor damage couldn’t be detected in time and adopt effective countermeasures, the likelihood of a catastrophic space incident is significantly high.
- 原句：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
  - 可迁移句型：{object} technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
- 原句：Therefore, it’s crucial for the future development of intelligent aircraft.
  - 可迁移句型：{object}, it’s crucial for the future development of intelligent aircraft.
- 原句：Based on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].
  - 可迁移句型：{object} on the real-time structural capacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the spacecraft and improve the safety of manned space missions [6].

## 9. 引用风险层

- 正文引用簇估计：46
- 参考文献条数：44
- 可识别年份条目数：45
- 2021 年及以后参考文献数：28
- 2010 年以前经典文献数：3
- 高频来源粗略识别：Sci. Technol(6)；Sound. Vib(2)；Struct(1)；J. Heat. Mass Transf(1)；Eng. Mech(1)；J. Solids Struct(1)；Constr. Steel. Res(1)；Tech(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] H. Rocha, C. Semprimoschnig, P.N. Jo˜ao, Sensors for process and structural health monitoring of aerospace composites: a review, Eng. Struct. 237 (2021) 112231.
- [2] Hu Jia-Xin, Ai Li-Qiang, Liu Nan, Gou Jian-Jun, Gong Chun-Lin, Tolerance indicating models of non-thermal and thermal damages for a heat transport system, Int. J. Heat. Mass Transf. 224 (2024) 125360.
- [3] A. Rytter, M. Krawczuk, P.H. Kirkegaard, Experimental and numerical study of damaged cantilever, J. Eng. Mech. 126 (1) (2000) 60–65.
- [4] D.Y. Gao, Z.J. Wu, L. Yang, et al., Structural health monitoring for long-term aircraft storage tanks under cryogenic temperature, Aerosp. Sci. Technol. 92 (2019) 881–891.
- [5] Nakatani Scott, Timothy Sands, Simulation of spacecraft damage tolerance and adaptive controls, in: 2014 IEEE Aerospace Conference, 2014.
- [6] Nicholas Cholevas ad Konstantinos, N. Anyfantis, Crack identification in solid rocket motors through the Neyman-Peason detection theory, AIAA J. 5 (2023) 61.
- [7] Gou Jian-Jun, Jia Shu-Zhen, Tian Hai-Tao, Hu Jia-Xin, Gong Chun-Lin, An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths, Aerosp. Sci. Technol. 148 (2024) 109115.
- [8] S.P. Chandra, S.V. Nimje, S. Roy, Strain based structural health monitoring of stiffened composite plate, Mater. Today: Proceed. 72 (2023) 1631–1636.
- [9] Gou Jian-Jun, Jia Shu-Zhen, Li Jin-Xing, Xiao Shuang, Gong Chun-Lin, The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects, Aerosp. Sci. Technol. 140 (2023) 108431.
- [10] E. Esu Obukho, Wang Ying, K. Chryssanthopoulos Marios, Local vibration mode pairs for damage identification in axisymmetric tubular structures, J. Sound. Vib. 494 (2020) 115845.
- [11] C. Peng, C. Bei, Influence of the blade size on the dynamic characteristic damage identification of wind turbine blades, Nonlinear Eng. 12 (2023) 20220261.
- [12] M. Masoumi, M.R. Ashory, Damage identification from uniform load surface using continuous and stationary wavelet transforms, Latin Am. J. Solids Struct. 11 (5) (2014) 738–754.
- [13] M. Motlagh, A. Bahar, O. Bahar, Damage detection in a 3D wind turbine tower by using extensive multilevel 2D wavelet decomposition and heat map, including soil- structure interaction, Structures 31 (2021) 842–861.
- [14] C.A. Ahmet, Y.O. Fatih, K. Volkan, Automated model updating of multiple cracked cantilever beams for damage detection, J. Constr. Steel. Res. 138 (2017) 499–512.
- [15] M. Gunaydin, S. Adanur, A.C. Altunisik, et al., Dynamic characteristics monitoring changes of damaged and retrofitted RC buildings, Exp. Tech. 46 (3) (2022) 457–484.

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
