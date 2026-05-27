# 论文深度拆解：The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests

> 生成依据：`801/cleantext/042-The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`042-The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.pdf`
- 页数：30
- clean body 字符数：83428
- 摘要字符数：1357
- 参考文献条数：42
- 图题数：24
- 表题数：5
- 表格文件数：10
- 公式候选数：295
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "45 formula(s) need manual review."}]

## 1. 身份层

- 标题：The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests
- 年份：2023
- 期刊/来源：International Journ
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Proper characterization of rough surfaces is essential for the accurate estimation of TCR. The essential assumptions involved in above characterizations weakens their accuracy. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
- 主要方法：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG. Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are th
- 主要证据：图表 29 个标题、公式 295 个候选、参考文献 42 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Proper characterization of rough surfaces is essential for the accurate estimation of TCR. The essential assumptions involved in above characterizations weakens their accuracy. 4 T”，可以通过“The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd. 2 shows the reconstructed rough surfaces and contacting model. As shown in the upper left part of Fig.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Proper characterization of rough surfaces is essential for the accurate estimation of TCR. The essential assumptions involved in above characterizations weakens their accuracy. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
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
- 作者声明或文本中可见 gap：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap. The study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15]. It should be noted that considering the lim- $$P _ {\operatorname* {m a x}} ^ {T \& E} = \frac {\left( U ^ {T \ : T R} \right) ^ {2}} {R _ {i} ^ {T \ : \mathrm{R} \ : E}} = \frac {\left( \int _ {T _ {p} ^ {h}} ^ {T _ {p} ^ {h}} \big | S _ {P} ( T ) \big | d T + \int _ {T _ {p} ^ {h}} ^ {T _ {h} ^ {h}} \big | S _ {N} ( T ) \big | d T \right) ^ {2}} {A \Bigg [ \frac {I} {A} ( \frac {1} {k _ {b} ( \frac {T _ {h} ^ {h} + T _ {e} ^ {h}} {2} )} + \frac {1} {k _ {b} ( \frac {T _ {h} ^ {h} + T _ {e} ^ {h}} {2} )} ) + R _ {E - P , u} ^ {c} ( T _ {p} ^ {h} ) + R _ {E - P , d} ^ {c} ( T _ {p} ^ {c} ) + R _ {E - N , u} ^ {c} ( T _ {N} ^ {h} ) + R _ {E - N , d} ^ {c} ( T _ {N} ^ {c} ) \Bigg ]}\tag{5}$$ where $P _ {\mathrm{max}} ^ {T 8 E}$ and $R _ {i} ^ {T \& E}$ are the maximum output power and internal electric resistance of the TEG with TCR and ECR, respectively.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG. Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
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
| The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. | 摘要/引言/结论候选 | 图：Fig. 1. Schematic figure of TEG and interfacial contact effects. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively | 摘要/引言/结论候选 | 图：Fig. 2. Reconstructed rough surfaces and contacting model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated. | 摘要/引言/结论候选 | 图：Fig. 3. Boundary conditions of contacting model and TEG model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Third, the TE conversion process of TEG is simulated with consider- ing the contact effects by equivalent layers, the TCR test platform is developed to measure the out power of TEG and the numerical models are then validated. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd. | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Aalilija et al. [9] proposed a numerical model based on the diffuse interface method, and the contact region is simulated by an intermediate thin material. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.61, 694.79, 292.16, 709.84)]] E-mail addresses: jj.g | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic figure of TEG and interfacial contact effects. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Reconstructed rough surfaces and contacting model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Boundary conditions of contacting model and TEG model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. Meshed models of contacting pairs and TEG. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. Test method for TCR between TE leg and electrodes. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 6. Experimental measurement platform for TCR. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Experimental measurements for ECR and power generation of TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Temperature nephogram of contacting pairs under different gap mediums. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Temperature nephogram of rough surfaces for TE legs under vacuum and air gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 10. Temperature and heat flux of rough surfaces for TE legs under silver-epoxy adhesive gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 11. Numerical results of influences of thermal radiation on TCR. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Numerical results of variation of TCR with interface temperature under vacuum gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. Numerical results of variation of TCR with interface temperature under air gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. Variation of TCR with loading pressure under vacuum and air gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Variation of TCR with loading pressure under silver-epoxy adhesive gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.61, 694.79, 292.16, 709.84)]] E-mail addresses: jj.gou@nwpu.edu.cn (J.-J | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (431.7, 486.63, 471.66, 510.25)]] Thermal conductivity (W/(m ·K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (368.51, 495.2, 425.14, 510.25)]] Specific heat capacity (J/(kg ·K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (337.82, 622.3, 421.54, 647.55)]] R PC i = (U PC P + U PC N ) 2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (306.6, 622.72, 357.25, 640.9)]] P PC max = (U PC ) 2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (366.8, 631.64, 439.72, 645.48)]] 4(R P (T ) + R N (T )) = | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 4, bbox (497.05, 630.84, 561.11, 654.05)]] k N ( T h E + T c E 2 ) ) (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (460.36, 636.02, 514.75, 654.05)]] k P ( T h E + T c E 2 ) + 1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG. First, the thermal and electrical contact resistances under different temperatures, pressures, gap mediums and thermal radia- tion conditions are predicted. Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated. Third, the TE conversion process of TEG is simulated with consider- ing the contact effects by equivalent layers, the TCR test platform is developed to measure the out power of TEG and the numerical models are then validated. Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd. All rights reserved.

### 7.4 摘要中文翻译

> 异质界面接触效应的精确定量描述是开发具有高超音速气动热收集潜力的热电发电机（TEG）的关键问题。本文通过基于实拓扑的数值预测和新颖的间接实验测试研究了热电（TE）腿和电极之间的热电接触效应，并提出了两个简化公式来定量表达它们对 TEG 的影响。首先，预测不同温度、压力、间隙介质和热辐射条件下的热接触电阻和电接触电阻。其次，开发了一种基于TE转换特性的新型间接热接触热阻（TCR）测试方法，建立了相应的平台并对数值模型进行了验证。第三，考虑等效层的接触效应，模拟了TEG的TE转换过程，开发了TCR测试平台来测量TEG的输出功率，并对数值模型进行了验证。最后推导了考虑接触效应的TEG最大输出功率预测的两个预测公式，与数值结果吻合较好，最大偏差为7.7%。 © 2022 爱思唯尔有限公司

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work, the thermal and electrical contact effects between the TE legs and electrodes of the TEG applied to hypersonic vehicles are studied by real-topology-based predictions and novel indirect tests, their influences on the TEG are clarified by corresponding simulations and measurements, and two prediction formulas are finally developed. To begin with, the thermal and electrical contact resistances are predicted based on the reconstructed rough surfaces, and the influences of temperature, loading pressure, gap medium and thermal radiation are analyzed. For another thing, a novel indirect TCR test approach is developed and a corresponding platform is established, and the TCR under different temperatures and loading pressures are measured and the numerical models are then validated. The platform is also altered to measure the ECR and power supply of the TEG. And thirdly, the heat transfer and conversion process of the TEG is simulated with considering the interfacial contact effects by equivalent layers, the electric power supply of the TEG under different temperatures are measured and the numerical models are then validated. Finally, two simplified formulas for the prediction of the maximum output power with considerations of thermal and thermal-electrical contact resistance of the TEG are established. The results show some conclusions:
> 
> 1 In the numerical prediction of the TCR, heat conduction and thermal radiation are considered, and the model is established based on the reconstructed real rough surface topographies of the TE legs and electrodes. The proposed approach can be used to predict the thermal contact resistance under different temperatures, loading pressures and gap mediums.
> 
> 2 The influence of thermal radiation on the TCR increases gradually with the rise of the average interface temperature under vacuum or air gap. When the gap medium is vacuum, the TCR is mainly affected by the thermal conductivity of the TE materials; while when the gap medium is air, the TCR decreases with the rise of the average interface temperature.
> 
> 3 The TCR decreases while the tendency slows down with the increase of the loading pressure. The TCR under air gap is about half of that under vacuum gap, and the TCR under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap.
> 
> 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes. The corresponding experimental platform can measure the TCR under different temperatures and loading pressures, and the experimental and numerical results have a relatively good agreement with the largest difference of -27.51%. The platform can also be altered to measure the ECR and power supply of the TEG.
> 
> 5 The negative influence of the ECR on the TEG is higher than that of the TCR under vacuum or air gap; while the TCR is slightly higher than that of the ECR under the silver-epoxy adhesive gap. The TE performance degradation of the TEG caused by contact effects under the silver-epoxy adhesive gap is no more than 4%; while that for air gap is over 96%.
> 
> 6 The proposed numerical model for evaluating the influence of contact effects on the TEG is validated by measuring the electric power supply of the TEG, and the largest difference is 8.73%.
> 
> 7 The prediction formulas for the maximum output power of the TEG with contact effects can be applicable for loading pressure from 0.104 to 0.187 MPa, temperature from 323 to 523 K, roughness from 3.55 to 32.53 μm and gap medium of vacuum, air and the silver-epoxy adhesive with the maximum deviation of 7.7%.

### 7.6 结论中文翻译

> 在这项工作中，通过基于真实拓扑的预测和新颖的间接测试，研究了应用于高超声速飞行器的TE腿和电极之间的热电接触效应，并通过相应的模拟和测量阐明了它们对TEG的影响，并最终提出了两个预测公式。首先，根据重建的粗糙表面预测热阻和电接触电阻，并分析温度、加载压力、间隙介质和热辐射的影响。另一方面，开发了一种新颖的间接TCR测试方法并建立了相应的平台，测量了不同温度和加载压力下的TCR并验证了数值模型。该平台还经过改造，可以测量 TEG 的 ECR 和电源。第三，考虑等效层界面接触效应，模拟了TEG的传热和转换过程，测量了TEG在不同温度下的供电情况，并对数值模型进行了验证。最后，考虑了 TEG 的热阻和热电接触电阻，建立了两个简化的最大输出功率预测公式。结果表明： 1 在TCR数值预测中，考虑了热传导和热辐射，并根据重建的TE腿和电极的真实粗糙表面形貌建立了模型。该方法可用于预测不同温度、负载压力和间隙介质下的接触热阻。
> 
> 2 热辐射对TCR的影响随着真空或气隙下平均界面温度的升高而逐渐增大。当间隙介质为真空时，TCR主要受TE材料导热系数的影响；而当间隙介质为空气时，TCR随着平均界面温度的升高而降低。 3 随着加载压力的增加，TCR降低，但趋势减慢。空气间隙下的TCR约为真空间隙下的一半，银胶间隙下的TCR约为真空间隙下的千分之一。 4 所开发的 TCR 测试方法对于获得包含一条 TE 腿和两个电极的测试样品的合理实验结果至关重要。相应的实验平台可以测量不同温度和加载压力下的TCR，实验结果与数值结果吻合较好，最大差异为-27.51%。该平台还可以进行更改以测量 TEG 的 ECR 和电源。 5 ECR对TEG的负面影响高于真空或气隙下TCR的负面影响；而在银环氧胶间隙下TCR略高于ECR。银环氧胶间隙下接触效应引起的TEG的TE性能下降不超过4%；而气隙则超过96%。 6 通过测量 TEG 的供电电源来验证所提出的评估接触效应对 TEG 影响的数值模型，最大差异为 8.73%。
> 
> 7 具有接触效应的TEG最大输出功率预测公式可适用于加载压力0.104~0.187 MPa、温度323~523 K、粗糙度3.55~32.53 μm、间隙介质为真空、空气、银环氧胶等情况，最大偏差为7.7%。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 7648 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The TEG and material properties | 对象/条件/子问题展开 | 4574 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Theoretical power generation of TEG with consideration of contact effects | 对象/条件/子问题展开 | 7861 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3. Numerical models | 方法建构 | 1221 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 2.3. Rough surfaces and contacting models | 方法建构 | 426 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.1. Governing equations | 对象/条件/子问题展开 | 337 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.1.1. Equilibrium equation | 对象/条件/子问题展开 | 906 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.1.2. Geometric equation | 对象/条件/子问题展开 | 787 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.1.3. Constitutive equations for elastic stage | 对象/条件/子问题展开 | 183 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.1.4. Constitutive equations for plastic stage | 对象/条件/子问题展开 | 1181 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3.2. Calculation methods of TCR and ECR | 方法建构 | 599 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 3.3. Boundary conditions | 对象/条件/子问题展开 | 2642 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 3.4. Meshed models | 方法建构 | 1336 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 14 | 4.1. Experimental method for TCR | 方法建构 | 3436 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 15 | 4.2. Experimental platform for TCR | 实验或测量设定 | 1119 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 16 | 4.3. Experimental measurements of ECR and power generation | 实验或测量设定 | 1495 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 17 | 5.1. Contact mechanics and heat transfer | 对象/条件/子问题展开 | 7267 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 18 | 5.2.1. The influence of thermal radiation | 对象/条件/子问题展开 | 2335 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 19 | 5.2.2. The influence of average interface temperature | 对象/条件/子问题展开 | 7164 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 20 | 5.2.3. The influence of loading pressure | 对象/条件/子问题展开 | 3461 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 21 | 5.2.4. The experimental results of thermal contact resistance | 结果验证/讨论 | 2672 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 22 | 5.2.5. Electrical contact resistance | 对象/条件/子问题展开 | 2104 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 23 | 5.3.1. Considering the impact of TCR | 对象/条件/子问题展开 | 10476 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 24 | 5.3.2. Considering the impact of both TCR and ECR | 对象/条件/子问题展开 | 7032 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 25 | 6. Conclusion | 主张回收/边界说明 | 3649 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 26 | Data availability statement | 对象/条件/子问题展开 | 138 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(335)；temperature(140)；tcr(135)；gap(134)；teg(105)；frac(102)；about(91)；contact(88)；leg(82)；fig(82)；times(75)；legs(70)；air(67)；increases(67)；electrodes(64)；ecr(64)；vacuum(62)；respectively(62)；heat(56)；thermal(54)
- 高频学术名词/术语：temperature(140)；pressure(41)；condition(39)；displacement(28)；difference(26)；compression(26)；resistance(23)；radiation(22)；measurement(20)；prediction(18)；conductivity(18)；conduction(16)；influence(16)；distribution(16)；performance(13)
- 高频学术动词：obtained(13)；compared(13)；developed(6)；predicted(5)；validated(5)；predict(5)；obtain(2)；indicate(2)；derived(2)；estimate(2)；indicated(1)
- 高频形容词：thermal(54)；adhesive(45)；partial(44)；electric(36)；experimental(29)；numerical(28)；displacement(28)；real(23)；potential(22)；electrical(20)；measurement(20)；material(18)；coefficient(11)；current(10)；table(10)
- 高频副词：respectively(62)；gradually(19)；mainly(14)；supply(7)；relatively(6)；significantly(5)；slightly(5)；finally(3)；greatly(2)；publicly(1)；widely(1)；firstly(1)
- 高频二词短语：mathrm mathrm(165)；loading pressure(39)；silver-epoxy adhesive(39)；air gap(35)；times mathrm(35)；legs electrodes(34)；maximum output(34)；interface temperature(34)；average interface(33)；n-type leg(32)；output power(31)；adhesive gap(30)；about times(29)；increases about(29)；vacuum gap(28)
- 高频三词短语：mathrm mathrm mathrm(76)；average interface temperature(33)；maximum output power(31)；silver-epoxy adhesive gap(25)；times mathrm cdot(18)；mathrm cdot mathrm(17)；cdot mathrm mathrm(16)；perfect contact condition(16)；varepsilon varepsilon varepsilon(16)；output power teg(15)；displaystyle frac partial(15)；absolute value compression(15)
- 被动语态估计：152
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：395
- 一般过去时线索：306
- 现在完成时线索：1
- 情态动词线索：64

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Proper characterization of rough surfaces is essential for the accurate estimation of TCR.
  - 可迁移句型：{object} characterization of rough surfaces is essential for the accurate estimation of TCR.
- 原句：The essential assumptions involved in above characterizations weakens their accuracy.
  - 可迁移句型：{object} essential assumptions involved in above characterizations weakens their accuracy.
- 原句：4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
  - 可迁移句型：4 {object} developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
### gap/转折句
- 原句：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  - 可迁移句型：{object} legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 原句：The study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15].
  - 可迁移句型：{object} study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15].
- 原句：In addition, compared with the public reports, there are fewer assumptions in the experimental method: the electrical resistance of TE materials, the ECRs between TE legs and electrodes are considered, and the TCRs and material parameters are change with temperature.
  - 可迁移句型：{object} addition, compared with the public reports, there are fewer assumptions in the experimental method: the electrical resistance of TE materials, the ECRs between TE legs and electrodes are considered, and the TCRs and material parameters are change with
### 方法提出句
- 原句：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
  - 可迁移句型：{object} precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
- 原句：In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG.
  - 可迁移句型：{object} This study, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantita
- 原句：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  - 可迁移句型：{object}, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句：Third, the TE conversion process of TEG is simulated with consider- ing the contact effects by equivalent layers, the TCR test platform is developed to measure the out power of TEG and the numerical models are then validated.
  - 可迁移句型：{object}, the TE conversion process of TEG is simulated with consider- ing the contact effects by equivalent layers, the TCR test platform is developed to measure the out power of TEG and the numerical models are then validated.
### 结果证明句
- 原句：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd.
  - 可迁移句型：{object}, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd.
- 原句：2 shows the reconstructed rough surfaces and contacting model.
  - 可迁移句型：2 shows the reconstructed rough surfaces and contacting model.
- 原句：As shown in the upper left part of Fig.
  - 可迁移句型：{object} shown in the upper left part of Fig.
- 原句：4 shows the meshed models of contacting pairs and TEG.
  - 可迁移句型：4 shows the meshed models of contacting pairs and {object}.
### 贡献收束句
- 未稳定识别，需从对应章节人工补充。
### 边界/谨慎句
- 原句：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  - 可迁移句型：{object} legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 原句：The study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15].
  - 可迁移句型：{object} study of TE materials is very limited, and the publicly reported studies mainly focus on the TCR between TEG and heat/cold sources [13–15].
- 原句：It should be noted that considering the lim- $$P _ {\operatorname* {m a x}} ^ {T \& E} = \frac {\left( U ^ {T \ : T R} \right) ^ {2}} {R _ {i} ^ {T \ : \mathrm{R} \ : E}} = \frac {\left( \int _ {T _ {p} ^ {h}} ^ {T _ {p} ^ {h}} \big | S _ {P} ( T ) \big | d T + \int _ {T _ {p} ^ {h}} ^ {T _ {h} ^ {h}} \big | S _ {N} ( T ) \big | d T \right) ^ {2}} {A \Bigg [ \frac {I} {A} ( \frac {1} {k _ {b} ( \frac {T _ {h} ^ {h} + T _ {e} ^ {h}} {2} )} + \frac {1} {k _ {b} ( \frac {T _ {h} ^ {h} + T _ {e} ^ {h}} {2} )} ) + R _ {E - P , u} ^ {c} ( T _ {p} ^ {h} ) + R _ {E - P , d} ^ {c} ( T _ {p} ^ {c} ) + R _ {E - N , u} ^ {c} ( T _ {N} ^ {h} ) + R _ {E - N , d} ^ {c} ( T _ {N} ^ {c} ) \Bigg ]}\tag{5}$$ where $P _ {\mathrm{max}} ^ {T 8 E}$ and $R _ {i} ^ {T \& E}$ are the maximum output power and internal electric resistance of the TEG with TCR and ECR, respectively.
  - 可迁移句型：{object} should be noted that considering the lim- $$P _ {\operatorname* {m a x}} ^ {T \& E} = \frac {\left( U ^ {T \ : T R} \right) ^ {2}} {R _ {i} ^ {T \ : \mathrm{R} \ : E}} = \frac {\left( \int _ {T _ {p} ^ {h}} ^ {T _ {p} ^ {h}} \big | S _ {P} ( T ) \big 
- 原句：It should be noted that $T _ {\mathrm{E1}}$ and $T _ {\mathrm{E} 2}$ are the temperatures for hot- and cold side of electrodes measured in the test, respectively.
  - 可迁移句型：{object} should be noted that $T _ {\mathrm{E1}}$ and $T _ {\mathrm{E} 2}$ are the temperatures for hot- and cold side of electrodes measured in the test, respectively.

## 9. 引用风险层

- 正文引用簇估计：38
- 参考文献条数：42
- 可识别年份条目数：81
- 2021 年及以后参考文献数：14
- 2010 年以前经典文献数：1
- 高频来源粗略识别：Therm. Eng(9)；J. Heat Mass Transf(7)；Energy(4)；J. Therm. Sci(3)；Manag(3)；Sci. Technol(2)；Commun. Heat Mass Transf(2)；J. Int. Meas. Confed(2)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] JJ Gou, JX Hu, ZW Yan, G Gao, CL. Gong, Effects of physical dimensions, temper- ature ranges and interfacial thermal contacts on the multi-stage thermoelectric generators for a hypersonic vehicle, Int. J. Energy Res. 46 (2022) 20 021–20 038, doi: 10.1002/er.7799 .
- [2] JJ Gou, ZW Yan, JX Hu, G Gao, CL. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cool- ing and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021) 106373, doi: 10.1016/j.ast.2020.106373 .
- [3] BX Shen, WQ. Liu, Insulating and absorbing heat of transpiration in a com- binational opposing jet and platelet transpiration blunt body for hyper- sonic vehicle, Int. J. Heat Mass Transf. 138 (2019) 314–325, doi: 10.1016/j. ijheatmasstransfer.2019.04.057 .
- [4] G Gao, J-J Gou, C-L Gong, J-X Hu, R-C. Gao, A novel mechanical-thermal- electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962, doi: 10.1016/j.compstruct.2021.113962 .
- [5] CL Gong, JJ Gou, JX Hu, F. Gao, A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470, doi: 10.1016/j.ast.2018.03.028 .
- [6] T Cui, Q Li, Y. Xuan, Characterization and application of engineered regular rough surfaces in thermal contact resistance, Appl. Therm. Eng. 71 (2014) 400– 409, doi: 10.1016/j.applthermaleng.2014.07.020 .
- [7] J Liu, C Ma, S Wang, S Wang, B. Yang, Thermal contact resistance between bearing inner ring and shaft journal, Int. J. Therm. Sci. 138 (2019) 521–535, doi: 10.1016/j.ijthermalsci.2019.01.022 .
- [8] PG Siddappa, A. Tariq, Contact area and thermal conductance estimation based on the actual surface roughness measurement, Tribol. Int. 148 (2020) 106358, doi: 10.1016/j.triboint.2020.106358 .
- [9] A Aalilija, C-A Gandin, E. Hachem, A simple and efficient numerical model for thermal contact resistance based on diffuse interface immersed boundary method, Int. J. Therm. Sci. 166 (2021) 106817, doi: 10.1016/j.ijthermalsci.2020. 106817 .
- [10] J-J Gou, X-J Ren, Y-J Dai, S. Li, Study of thermal contact resistance of rough surfaces based on the practical topography, Comput. Fluids 164 (2018) 2–11, doi: 10.1016/J.COMPFLUID.2016.09.018 .
- [11] YJ Dai, JJ Gou, XJ Ren, F Bai, WZ Fang, WQ. Tao, A test-validated predic- tion model of thermal contact resistance for Ti-6Al-4V alloy, Appl. Energy 228 (2018) 1601–1617, doi: 10.1016/j.apenergy.2018.06.134 .
- [12] XJ Ren, YJ Dai, JJ Gou, WQ. Tao, Numerical prediction of thermal contact resistance of 3D C/C-SiC needled composites based on measured practi- cal topography, Int. J. Heat Mass Transf. 131 (2019) 176–188, doi: 10.1016/j. ijheatmasstransfer.2018.08.137 .
- [13] B Beltrán-Pitarch, J Maassen, J. García-Cañadas, Comprehensive impedance spectroscopy equivalent circuit of a thermoelectric device which includes the internal thermal contact resistances, Appl. Energy 299 (2021) 117287, doi: 10. 1016/j.apenergy.2021.117287 .
- [14] S Wang, T Xie, H. Xie, Experimental study of the effects of the thermal contact resistance on the performance of thermoelectric generator, Appl. Therm. Eng. 130 (2018) 847–853, doi: 10.1016/j.applthermaleng.2017.11.036 .
- [15] B Beltrán-Pitarch, F Vidan, J. García-Cañadas, Thermal contact resistance eval- uation of a thermoelectric system by means of three I-V curves, Int. J. Heat Mass Transf. 173 (2021) 121247, doi: 10.1016/j.ijheatmasstransfer.2021.121247 .

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
