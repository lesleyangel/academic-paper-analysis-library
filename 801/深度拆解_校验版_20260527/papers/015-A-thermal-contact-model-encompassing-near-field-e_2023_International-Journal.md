# 论文深度拆解：A thermal contact model encompassing near-field effects of multi-interface TEGs in hypersonic conditions

> 生成依据：`801/cleantext/015-A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`015-A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal.pdf`
- 页数：21
- clean body 字符数：69879
- 摘要字符数：1698
- 参考文献条数：48
- 图题数：24
- 表题数：5
- 表格文件数：6
- 公式候选数：222
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "23 formula(s) need manual review."}]

## 1. 身份层

- 标题：A thermal contact model encompassing near-field effects of multi-interface TEGs in hypersonic conditions
- 年份：2023
- 期刊/来源：International Journal
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：The proper characterization of rough surface is essential in accurately estimating the TCR. 3 The NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfaces of TEGs.
- 主要方法：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions. First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements. Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
- 主要证据：图表 29 个标题、公式 222 个候选、参考文献 48 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“The proper characterization of rough surface is essential in accurately estimating the TCR. 3 The NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfac”，可以通过“In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively; and the maximum output power of the TEG increases by about 8.02% and 1.29% under vacuum and air clearance (0.1 MPa, 650 K), respectively. As shown in Table $^ {5 ,}$ the largest differences between the experimental and numerical results of the $\mathrm {^ {* *} S - E ^ {*}} ,$ the “E-$N _ - \mathrm{l} ^ {\prime} \mathrm{\Omega}$ , the $\tilde {\mathrm{~\varepsilon~}} _ {\mathrm{E} - N _ - \mathrm{u}} ,$ the “E-P\_l” and the $\mathrm {\bf {\ddot {E}}} {\bf -} P _ - \mathrm {\bf {u}} ^ {\mathrm {\tiny {\ '}}}$ are about $6.07 \% , \ : - 6.00 \%$ $- 5.76 \% ,$ 6.56% and $6.13 \% ,$ respectively. 21 shows the temperature contour of the TEG in considering of the solid conduction, the far- and the near-filed thermal radiation under vacuum and air clearance.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：The proper characterization of rough surface is essential in accurately estimating the TCR. 3 The NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfaces of TEGs.
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
- 作者声明或文本中可见 gap：Actually, substrates, electrodes and TE legs have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact clearance. However, the above researches mainly concentrated in the effect of solid conduction on the heat transfer process, and few of them consider the far-field thermal radiation (FFTR) effect. The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
- Most of the current work involved in TEGs [34,36,37] are measured the TCR between the TEG and cold/- heat source, and only a few focused on the heterogeneous interfaces inside of the TEG.
- For the influence of the TCR on the TEG, a lot of works in theoretical analysis [38] and numerical simulations [39–42] are carried, but lack of complete and reliable data on the TCRs of the heterogeneous interfaces inside of TEGs.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions. First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements. Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
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
| First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct | 摘要/引言/结论候选 | 图：Fig. 1. Schematic figure of thermal contact model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, r | 摘要/引言/结论候选 | 图：Fig. 2. Measured and reconstructed rough surfaces of contacting pairs in TEG. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Frekers et al. [13] proposed a micro-scale numerical method to predict the contact heat transfer based on the generation model of optical profiler. | 摘要/引言/结论候选 | 图：Fig. 3. Comparison of calculation results for thermal radiation effect with publicly reported literatures. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Dai et al. [15] and Ren et al. [16] developed the method from rectangle-like cross section contacting model to the circular ones. | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| As shown in Table $^ {5 ,}$ the largest differences between the experimental and numerical results of the $\mathrm {^ {* *} S - E ^ {*}} ,$ the “E-$N _ - \mathrm{l} ^ {\prime} \mathrm{\Omega}$ , the $\tilde {\mathrm{~\varepsilon~}} _ {\mathrm{E} - N _ - \mathr | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| 21 shows the temperature contour of the TEG in considering of the solid conduction, the far- and the near-filed thermal radiation under vacuum and air clearance. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 205.75, 443.68, 223.92)]] Ge Gao a, Shi-Yuan Che | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic figure of thermal contact model. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Measured and reconstructed rough surfaces of contacting pairs in TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Comparison of calculation results for thermal radiation effect with publicly reported literatures. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 4. Equivalent thermal contact conductance of thermal radiation. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Real model and CAD model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. Meshed models of contacting pairs and TEG. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. Boundary conditions of contacting pairs and TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Experimental measurement platform for TCR of TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Dimensionless real contact aera varied with loading pressure. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Mises stress contour of rough surfaces. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 11. Temperature contour of contacting pairs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. Temperature contour of rough surfaces under different heat transfer forms (I: solid conduction; II: solid conduction and far-field radiation; III: soli | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. Temperature contour of rough surfaces in negative heat transfer path. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 14. Influence of thermal radiation on TCRs between TE legs and electrodes under vacuum clearance. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Influence of thermal radiation on TCRs between TE legs and electrodes under air clearance. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 205.75, 443.68, 223.92)]] Ge Gao a, Shi-Yuan Chen a, Li-Qiang Ai b,  | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 206.24, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 324.91, 716.91)]] https://doi.org/10.1016/j.ijheatmasstransf | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (307.96, 123.32, 332.58, 137.88)]] εx = ∂u | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (307.96, 147.13, 334.06, 162.43)]] γyz = ∂v | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (307.96, 170.94, 334.79, 186.24)]] γxy = ∂u | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 5, bbox (313.0, 389.06, 357.85, 414.59)]] ∂t = div ( λ cp | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 5, bbox (313.51, 419.96, 356.28, 445.13)]] ∂t = div (k | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> High efficiency heat harvest of hypersonic vehicles claims elaborate design of thermoelectric (TE) conversion process. A thermoelectric generator (TEG) contains multi-interfaces in the heat transfer path and the interfacial thermal contacts with certain amount of nanoscale effects have significant influence on its TE conversion process. In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions. First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements. Second, the effects of average interfacial temperature, clearance distance and opposite heat transfer paths on the thermal radiation are analyzed, and the influences of average interfacial temperature, loading pressure and clearance mediums on the TCR are then clarified. Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted. The result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively; and the maximum output power of the TEG increases by about 8.02% and 1.29% under vacuum and air clearance (0.1 MPa, 650 K), respectively.

### 7.4 摘要中文翻译

> 高超音速飞行器的高效热收集需要精心设计的热电（TE）转换过程。热电发电机（TEG）在传热路径中包含多个界面，具有一定纳米级效应的界面热接触对其TE转换过程有显着影响。本文建立了一个热接触模型，该模型涵盖了基板、电极和 TE 腿之间具有异质界面的 TEG 的近场热辐射 (NFTR) 效应，并在高超声速条件下进行了实验验证。首先，建立了基于真实拓扑的热接触热阻（TCR）预测模型，并通过波动电动力学考虑异质界面的远场和近场辐射传热，并通过直接和间接实验测量验证了该模型。其次，分析了平均界面温度、间隙距离和相对传热路径对热辐射的影响，明确了平均界面温度、加载压力和间隙介质对TCR的影响。第三，在TEG性能评估模型中等效考虑TCR，并定量计算NFTR效应。结果表明：在考虑NFTR的情况下，TE腿与电极、基板与电极之间的TCR在真空间隙下分别降低了约3.90%~17.0%和0.510%~6.40%，在空气间隙下分别降低了1.30%~5.50%和0.220%~2.00%；在真空和空气间隙（0.1 MPa，650 K）下，TEG的最大输出功率分别增加了约8.02%和1.29%。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of thermoelectric generators (TEGs)
> 
> with heterogeneous interfaces between substrates, electrodes and thermoelectric (TE) legs is established and experimentally validated in hypersonic conditions. To begin with, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements. For another thing, the effects of average interfacial temperature, clearance distance and opposite heat transfer paths on the thermal radiation are analyzed, and the influences of average interfacial temperature, loading pressure and clearance mediums on the TCR are then clarified. And thirdly, the TCR is equivalently considered in a TEG performance evaluation model and the NFTR effects is quantitatively counted. The results show some conclusions:
> 
> 1 In the numerical prediction of the TCR, the thermal analysis is completed by considering of the solid conduction, the far- and the near-field thermal radiation between the real-topology-based rough surfaces. The proposed approach can be used to predict the TCR with thermal radiation effect under different temperatures, loading pressures and clearance mediums.
> 
> 2 The thermal radiation effect has an enormous contribution to the heat transfer between the rough surfaces of the TE legs and the electrodes under vacuum clearance. The contribution of the thermal radiation to the total heat flux of “E-N\_l”, “E-N\_u”, “E-P\_l” and “E-P\_u” reached about 48.9%, 46.6%, 71.4% and 81.6% at 725 K, respectively; in which the contribution of the NFTR is about 20.9%, 20.0%, 29.3% and 34.2%, respectively.
> 
> 3 The NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfaces of TEGs. With the consideration of the NFTR effect, the TCRs between the TE legs and the electrodes, the substrates and the electrodes reduced by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively.
> 
> 4 It is necessary to consider the heat transfer path when the equivalent thermal contact conductance of the NFTR effect for two materials has large difference in magnitude. The TCR of the “S-E” reached a maximum difference of about 10.0% at 480 K in different heat transfer paths under vacuum clearance.
> 
> 5 The TCR prediction model is validated by direct and indirect experimental measurements under different temperatures and loading pressures, and the experimental and numerical results have a relatively good agreement with the largest differences of about 6.07%, − 6.00%, − 5.76%, 6.56% and 6.13% for the “S-E”, “E-N\_l”, “E-N\_u”, “E-P\_l” and “E-P\_u”, respectively.
> 
> 6 For a TEG containing about 8 heterogeneous interfaces, it is crucial to consider the NFTR effect for accurate evaluating its TE performance. The maximum output power of the TEG increases by about 0.883% to 8.02% with the consideration of the NFTR effect.

### 7.6 结论中文翻译

> 在这项工作中，建立了一个热接触模型，该模型包含热电发生器（TEG）的近场热辐射（NFTR）效应，该模型具有基板、电极和热电（TE）腿之间的异质界面，并在高超声速条件下进行了实验验证。首先，建立了基于真实拓扑的热接触热阻（TCR）预测模型，并通过波动电动力学考虑异质界面的远场和近场辐射传热，并通过直接和间接实验测量验证了该模型。另一方面，分析了平均界面温度、间隙距离和相对传热路径对热辐射的影响，明确了平均界面温度、加载压力和间隙介质对TCR的影响。第三，在TEG性能评估模型中等效考虑TCR，并定量计算NFTR效应。结果表明： 1 在TCR数值预测中，考虑了真实拓扑粗糙表面之间的固体传导、远场和近场热辐射，完成了热分析。该方法可用于预测不同温度、加载压力和间隙介质下具有热辐射效应的TCR。 2 热辐射效应对真空间隙下 TE 腿的粗糙表面与电极之间的传热有巨大贡献。
> 
> 在725 K时，热辐射对“E-N\_l”、“E-N\_u”、“E-P\_l”和“E-P\_u”总热通量的贡献分别达到约48.9%、46.6%、71.4%和81.6%；其中NFTR的贡献分别约为20.9%、20.0%、29.3%和34.2%。 3 NFTR 效应对于精确评估 TEG 异质界面处的 TCR 至关重要。考虑到NFTR效应，TE腿与电极之间、基板与电极之间的TCR在真空间隙下分别降低了约3.90%至17.0%和0.510%至6.40%，在空气间隙下分别降低了1.30%至5.50%和0.220%至2.00%。 4 当两种材料的NFTR效应的等效接触热导幅度相差较大时，需要考虑传热路径。在真空间隙下不同传热路径中，“S-E”的TCR在480 K时达到约10.0%的最大差异。 5 通过不同温度和加载压力下的直接和间接实验测量验证了TCR预测模型，实验和数值结果具有较好的一致性，“S-E”、“E-N\_l”、“E-N\_u”、“E-P\_l”和“S-E”、“E-N\_l”、“E-N\_u”、“E-P\_l”的最大差异约为6.07%、−6.00%、−5.76%、6.56%和6.13%。分别为“E-P\_u”。 6 对于包含约 8 个异构接口的 TEG，考虑 NFTR 效应对于准确评估其 TE 性能至关重要。考虑NFTR效应后，TEG的最大输出功率增加了约0.883%至8.02%。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6961 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The multi-interface TEG and TCR | 对象/条件/子问题展开 | 4372 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Rough surfaces | 对象/条件/子问题展开 | 1964 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3. Numerical models | 方法建构 | 656 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. Governing equations | 对象/条件/子问题展开 | 3287 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Calculation method of TCR | 方法建构 | 3085 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Evaluation of radiative heat transfer | 对象/条件/子问题展开 | 6327 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.4. Model and meshed model | 方法建构 | 5017 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 3.5. Boundary conditions | 对象/条件/子问题展开 | 2824 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4. Experimental measurement platform for TCR | 实验或测量设定 | 1942 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 11 | 5.1. Contact mechanics and heat transfer | 对象/条件/子问题展开 | 6903 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 5.2.1. The quantitative description of thermal radiation | 对象/条件/子问题展开 | 9757 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.2.2. The influence of heat transfer path | 对象/条件/子问题展开 | 2172 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.2.3. The influence of average interfacial temperature | 对象/条件/子问题展开 | 2208 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.2.4. The influence of loading pressure | 对象/条件/子问题展开 | 2961 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5.2.5. The comparison with experimental results | 结果验证/讨论 | 1903 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 17 | 5.3. The evaluation of thermal radiation on TEG performance | 结果验证/讨论 | 2941 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 6. Conclusion | 主张回收/边界说明 | 3159 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 19 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 540 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(227)；about(124)；clearance(123)；times(113)；heat(100)；fig(80)；thermal(76)；tcr(72)；transfer(69)；temperature(68)；respectively(67)；vacuum(60)；cdot(56)；radiation(54)；surface(53)；air(52)；contact(50)；contacting(47)；nftr(44)；tcrs(43)
- 高频学术名词/术语：clearance(123)；temperature(68)；radiation(54)；pressure(33)；conduction(26)；displacement(24)；compression(23)；reduction(22)；influence(19)；distance(16)；calculation(13)；performance(11)；contribution(11)；roughness(10)；difference(9)
- 高频学术动词：compared(8)；validated(5)；developed(3)；predict(2)；predicted(2)；investigated(2)；obtained(2)；indicate(2)；derived(1)；estimated(1)；evaluated(1)；evaluate(1)
- 高频形容词：thermal(76)；partial(40)；interfacial(26)；displacement(24)；equivalent(20)；real(19)；radiative(18)；five(17)；total(11)；hexahedral(11)；positive(10)；tetrahedral(10)；heterogeneous(9)；dimensionless(9)；experimental(8)
- 高频副词：respectively(67)；mainly(9)；significantly(5)；quantitatively(3)；relatively(3)；obviously(3)；gradually(3)；accurately(2)；experimentally(2)；equivalently(2)；exponentially(2)；generally(2)
- 高频二词短语：mathrm mathrm(70)；times mathrm(68)；heat transfer(66)；vacuum clearance(51)；air clearance(48)；thermal radiation(46)；mathrm cdot(42)；cdot mathrm(42)；mathrm times(37)；about times(35)；loading pressure(32)；contacting pairs(26)；solid conduction(22)；fig shows(22)；compression displacement(22)
- 高频三词短语：mathrm cdot mathrm(38)；times mathrm cdot(33)；cdot mathrm mathrm(33)；mathrm times mathrm(31)；times mathrm times(29)；about times mathrm(22)；reduction rate about(20)；decreases about times(19)；average interfacial temperature(17)；big big big(17)；mathrm mathrm mathrm(16)；heat transfer path(16)
- 被动语态估计：106
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：293
- 一般过去时线索：256
- 现在完成时线索：0
- 情态动词线索：46

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The proper characterization of rough surface is essential in accurately estimating the TCR.
  - 可迁移句型：{object} proper characterization of rough surface is essential in accurately estimating the TCR.
- 原句：3 The NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfaces of TEGs.
  - 可迁移句型：3 {object} NFTR effect is essential for precisely evaluate the TCRs at heterogeneous interfaces of TEGs.
- 原句：4 It is necessary to consider the heat transfer path when the equivalent thermal contact conductance of the NFTR effect for two materials has large difference in magnitude.
  - 可迁移句型：4 {object} is necessary to consider the heat transfer path when the equivalent thermal contact conductance of the NFTR effect for two materials has large difference in magnitude.
### gap/转折句
- 原句：Actually, substrates, electrodes and TE legs have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact clearance.
  - 可迁移句型：{object}, substrates, electrodes and TE legs have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact clearance.
- 原句：However, the above researches mainly concentrated in the effect of solid conduction on the heat transfer process, and few of them consider the far-field thermal radiation (FFTR) effect.
  - 可迁移句型：{object}, the above researches mainly concentrated in the effect of solid conduction on the heat transfer process, and few of them consider the far-field thermal radiation (FFTR) effect.
- 原句：The near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
  - 可迁移句型：{object} near-field thermal radiative heat flux between two planes separated by a nanoscale vacuum clearance can exceed several orders of magnitude of the blackbody limit [19] and even reach a similar order of magnitude of heat conduction [20,21].
- 原句：It should be noted that considering the limited influence of the temperature on the contact state, it is reasonable to adopt step-by-step coupling method.
  - 可迁移句型：{object} should be noted that considering the limited influence of the temperature on the contact state, it is reasonable to adopt step-by-step coupling method.
### 方法提出句
- 原句：In this paper, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions.
  - 可迁移句型：{object} This study, a thermal contact model encompassing near-field thermal radiation (NFTR) effects of TEGs with heterogeneous interfaces between substrates, electrodes and TE legs is established and experimentally validated in hypersonic conditions.
- 原句：First, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by direct and indirect experimental measurements.
  - 可迁移句型：{object}, a real-topology-based thermal contact resistance (TCR) prediction model is developed and the far- and near-field radiative heat transfer at heterogeneous interfaces is considered by the fluctuational electrodynamics, and the model is validated by dir
- 原句：Third, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
  - 可迁移句型：{object}, the TCR is equivalently considered in a TEG perfor mance evaluation model and the NFTR effects is quantitatively counted.
- 原句：The rough surface can be reconstructed based on GW statistical model [7], Weierstrass–Mandelbrot fractal ones [8], Euclidean geometric statistical ones [9], facial ones [10], and semi-deterministic-based approach [11].
  - 可迁移句型：{object} rough surface can be reconstructed based on GW statistical model [7], Weierstrass–Mandelbrot fractal ones [8], Euclidean geometric statistical ones [9], facial ones [10], and semi-deterministic-based approach [11].
### 结果证明句
- 原句：The result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively; and the maximum output power of the TEG increases by about 8.02% and 1.29% under vacuum and air clearance (0.1 MPa, 650 K), respectively.
  - 可迁移句型：{object} result shows that: with the consideration of the NFTR, the TCRs between TE legs and electrodes, substrates and electrodes decrease by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearan
- 原句：As shown in Table $^ {5 ,}$ the largest differences between the experimental and numerical results of the $\mathrm {^ {* *} S - E ^ {*}} ,$ the “E-$N _ - \mathrm{l} ^ {\prime} \mathrm{\Omega}$ , the $\tilde {\mathrm{~\varepsilon~}} _ {\mathrm{E} - N _ - \mathrm{u}} ,$ the “E-P\_l” and the $\mathrm {\bf {\ddot {E}}} {\bf -} P _ - \mathrm {\bf {u}} ^ {\mathrm {\tiny {\ '}}}$ are about $6.07 \% , \ : - 6.00 \%$ $- 5.76 \% ,$ 6.56% and $6.13 \% ,$ respectively.
  - 可迁移句型：{object} shown in Table $^ {5 ,}$ the largest differences between the experimental and numerical results of the $\mathrm {^ {* *} S - E ^ {*}} ,$ the “E-$N _ - \mathrm{l} ^ {\prime} \mathrm{\Omega}$ , the $\tilde {\mathrm{~\varepsilon~}} _ {\mathrm{E} - N _ - 
- 原句：21 shows the temperature contour of the TEG in considering of the solid conduction, the far- and the near-filed thermal radiation under vacuum and air clearance.
  - 可迁移句型：21 shows the temperature contour of the {object} in considering of the solid conduction, the far- and the near-filed thermal radiation under vacuum and air clearance.
- 原句：The relatively small deviations indicate mesh-independence of the mesh size.
  - 可迁移句型：{object} relatively small deviations indicate mesh-independence of the mesh size.
### 贡献收束句
- 原句：In fact, when the separation between two objects is comparable to or below the dominant emitted wavelength, the net radiative heat flux can be enhanced [18], and that is so-called the near-field thermal radiation (NFTR) effect.
  - 可迁移句型：{object} fact, when the separation between two objects is comparable to or below the dominant emitted wavelength, the net radiative heat flux can be enhanced [18], and that is so-called the near-field thermal radiation (NFTR) effect.
- 原句：With the consideration of the NFTR effect, the TCRs between the TE legs and the electrodes, the substrates and the electrodes reduced by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance, respectively.
  - 可迁移句型：{object} the consideration of the NFTR effect, the TCRs between the TE legs and the electrodes, the substrates and the electrodes reduced by about 3.90% to 17.0% and 0.510% to 6.40% under vacuum clearance, 1.30% to 5.50% and 0.220% to 2.00% under air clearance
### 边界/谨慎句
- 原句：In traditional thermal protection system (TPS), the heat is mainly dissipated by the thermal radiation of the insulated structure, whose size and weight could be unaffordable under hypersonic conditions [2,3].
  - 可迁移句型：{object} traditional thermal protection system (TPS), the heat is mainly dissipated by the thermal radiation of the insulated structure, whose size and weight could be unaffordable under hypersonic conditions [2,3].
- 原句：Actually, substrates, electrodes and TE legs have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact clearance.
  - 可迁移句型：{object}, substrates, electrodes and TE legs have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact clearance.
- 原句：It should be noted that considering the limited influence of the temperature on the contact state, it is reasonable to adopt step-by-step coupling method.
  - 可迁移句型：{object} should be noted that considering the limited influence of the temperature on the contact state, it is reasonable to adopt step-by-step coupling method.
- 原句：It should be noted that $\mathrm{T} _ {E 1}$ and $\mathrm{T} _ {E 2}$ are the measured temperatures for the hot- and the cold-side of the sample in the experiment, respectively.
  - 可迁移句型：{object} should be noted that $\mathrm{T} _ {E 1}$ and $\mathrm{T} _ {E 2}$ are the measured temperatures for the hot- and the cold-side of the sample in the experiment, respectively.

## 9. 引用风险层

- 正文引用簇估计：48
- 参考文献条数：48
- 可识别年份条目数：85
- 2021 年及以后参考文献数：19
- 2010 年以前经典文献数：13
- 高频来源粗略识别：J. Heat Mass Transf(10)；Therm. Eng(10)；Sci. Technol(3)；J. Energy Res(2)；J. Therm. Sci(2)；Energy(2)；Commun. Heat Mass Transf(2)；Struct(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] J.J. Gou, J.X. Hu, Z.W. Yan, G. Gao, C.L. Gong, Effects of physical dimensions, temperature ranges and interfacial thermal contacts on the multi-stage thermoelectric generators for a hypersonic vehicle, Int. J. Energy Res. (2022) 1–18, https://doi.org/10.1002/er.7799.
- [2] J.J. Gou, Z.W. Yan, J.X. Hu, G. Gao, C.L. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021), 106373, https://doi. org/10.1016/j.ast.2020.106373.
- [3] B.X. Shen, W.Q. Liu, Insulating and absorbing heat of transpiration in a combinational opposing jet and platelet transpiration blunt body for hypersonic vehicle, Int. J. Heat Mass Transf. 138 (2019) 314–325, https://doi.org/10.1016/j. ijheatmasstransfer.2019.04.057.
- [4] G. Gao, J.J. Gou, C.L. Gong, J.X. Hu, R.C. Gao, A novel mechanical-thermal- electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021), 113962, https://doi.org/10.1016/j.compstruct.2021.113962.
- [5] C.L. Gong, J.J. Gou, J.X. Hu, F. Gao, A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470, https://doi.org/10.1016/j.ast.2018.03.028.
- [6] K. Cheng, J. Qin, Y. Jiang, C. Lv, S. Zhang, W. Bao, Performance assessment of multi-stage thermoelectric generators on hypersonic vehicles at a large temperature difference, Appl. Therm. Eng. (2018) 1598–1609, https://doi.org/ 10.1016/j.applthermaleng.2017.11.057.
- [7] J.A. Greenwood, J.B.P. Williamson, Contact of nominally flat surfaces, Proc. R. Soc. Lond. Ser. A Math. Phys. Sci. 295 (1966) 300–319, https://doi.org/10.1098/ rspa.1966.0242.
- [8] M.V. Berry, Z.V Lewis, On the Weierstrass-Mandelbrot fractal function, Proc. R. Soc. Lond. A Math. Phys. Sci. 370 (1980) 459–484, https://doi.org/10.1098/ rspa.1980.0044.
- [9] T. Cui, Q. Li, Y. Xuan, Characterization and application of engineered regular rough surfaces in thermal contact resistance, Appl. Therm. Eng. 71 (2014) 400–409, https://doi.org/10.1016/j.applthermaleng.2014.07.020.
- [10] J. Liu, C. Ma, S. Wang, S. Wang, B. Yang, Thermal contact resistance between bearing inner ring and shaft journal, Int. J. Therm. Sci. 138 (2019) 521–535, https://doi.org/10.1016/j.ijthermalsci.2019.01.022.
- [11] P.G. Siddappa, A. Tariq, Contact area and thermal conductance estimation based on the actual surface roughness measurement, Tribol. Int. 148 (2020), 106358, https://doi.org/10.1016/j.triboint.2020.106358.
- [12] G. Gao, D. Li, J.J. Gou, C.L. Gong, S.M. Li, A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations, Aerosp. Sci. Technol. 131 (2022), 107966, https://doi.org/10.1016/j.ast.2022.107966.
- [13] Y. Frekers, T. Helmig, E.M. Burghold, R. Kneer, A numerical approach for investigating thermal contact conductance, Int. J. Therm. Sci. 121 (2017) 45–54, https://doi.org/10.1016/j.ijthermalsci.2017.06.026.
- [14] J.J. Gou, X.J. Ren, Y.J. Dai, S. Li, Study of thermal contact resistance of rough surfaces based on the practical topography, Comput. Fluids 164 (2018) 2–11, https://doi.org/10.1016/J.COMPFLUID.2016.09.018.
- [15] Y.J. Dai, J.J. Gou, X.J. Ren, F. Bai, W.Z. Fang, W.Q. Tao, A test-validated prediction model of thermal contact resistance for Ti-6Al-4 V alloy, Appl. Energy 228 (2018) 1601–1617, https://doi.org/10.1016/j.apenergy.2018.06.134.

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
