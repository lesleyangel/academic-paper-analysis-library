# 论文深度拆解：013-A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S

> 生成依据：`801/cleantext/013-A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`013-A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.pdf`
- 页数：20
- clean body 字符数：62079
- 摘要字符数：1737
- 参考文献条数：48
- 图题数：21
- 表题数：3
- 表格文件数：5
- 公式候选数：170
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "14 formula(s) need manual review."}]

## 1. 身份层

- 标题：013-A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S
- 年份：2022
- 期刊/来源：Aerospace S
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography. An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
- 主要证据：图表 24 个标题、公式 170 个候选、参考文献 48 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography. An ECR measurement”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The thermoelectric (TE) conversion techniques can convert the aerodynamic heat and engine combustion heat into electrical power, the thermal protection system that is integrated with TE generators (TEG) [4–7] has potential efficiency improvement in heat management and is one of the most prospective techniques for the heat management of hypersonic vehicles. A TEG should consist of the N- and P -type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation. CoSb3 [16–18] based skutterudites are narrow bandgap semiconductors having high electrical conductivity and Seebeck coefficient, and the TE performance of bulk CoSb3 has been greatly improved by filling [19], doping [20] and nano-crystallization techniques [21,22].
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
- 作者声明或文本中可见 gap：However, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited. It should be noted that the thicknesses of the four equivalent interface layers are equal to the average distances of the corresponding four pairs of rough surfaces. The two-scale numerical simulation is carried out by commercial software and self-programming, in which the ECR prediction of the micrometer-scale contacting pairs model is simulated by ABAQUS, the material properties of the equivalent interface layers are calculated by self-programming, and the TE conversion process of the millimeter-scale TEG model is simulated by ANSYS Multiphysics (ABAQUS cannot simulate the Seebeck effects).
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography. An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
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
| An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. | 摘要/引言/结论候选 | 图：Fig. 1. TEG for hypersonic vehicles. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [2]. | 摘要/引言/结论候选 | 图：Fig. 2. Reconstruction of rough surfaces. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Thus, new heat management techniques [3] with potential high efficiency should be developed. | 摘要/引言/结论候选 | 图：Fig. 3. Geometric and mesh models of contact pairs. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The thermoelectric (TE) conversion techniques can convert the aerodynamic heat and engine combustion heat into electrical power, the thermal protection system that is integrated with TE generators (TEG) [4–7] has potential efficiency improvement in heat manage | 摘要/引言/结论候选 | 表：Table 1 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The conversion efficiency of TE materials is usually measured by dimensionless TE merit $\begin{array} {r} {Z T = \frac {S ^ {2} k} {\lambda} T} \end{array}$ , where S represents Seebeck coefficient, k electrical conductivity, λ thermal conductivity, T absolut | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| CoSb3 [16–18] based skutterudites are narrow bandgap semiconductors having high electrical conductivity and Seebeck coefficient, and the TE performance of bulk CoSb3 has been greatly improved by filling [19], doping [20] and nano-crystallization techniques [21 | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (306.63, 651.03, 520.73, 663.11)]] usually measured by dimensionless T | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. TEG for hypersonic vehicles. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Reconstruction of rough surfaces. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Geometric and mesh models of contact pairs. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. Analysis method, boundary conditions and contact properties. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Geometric and mesh models of TEG. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. Experimental measurement platform for ECR. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Stress cloud of rough region for TE legs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 8. Contact stress cloud of rough surfaces for TE legs. (For interpretation of the colors in the figure(s), the reader is referred to the web version of thi | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 9. Dimensionless real contact area varied with loading pressure. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Potential cloud of contact pairs under different gap mediums. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Potential cloud of rough surfaces for TE legs under air gap. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Current density cloud of rough surfaces for TE legs under air gap. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. Potential and current density of rough surfaces for TE legs under silver-epoxy adhesive gap. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Variation of ECR with temperature under air gap. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 15. Variation of ECR with loading pressure. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (306.63, 651.03, 520.73, 663.11)]] usually measured by dimensionless TE merit ZT = S2k | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 687.49, 264.98, 714.35)]] * Corresponding authors. E-mail addresses: | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (399.28, 80.84, 439.76, 107.12)]] Specific heat capacity (J/(kg·K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 7, bbox (37.64, 484.92, 78.64, 500.87)]] ECR = �U | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 8, bbox (37.8, 320.61, 288.71, 331.0)]] U = \|SN�T N\| + \|S P�T P\| (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 8, bbox (101.0, 482.09, 151.4, 498.41)]] ∂z + Fx = 0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 8, bbox (102.17, 507.44, 154.03, 523.75)]] ∂z + F y = 0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 8, bbox (102.08, 532.78, 151.36, 549.11)]] ∂z + Fz = 0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Jang-Kyo Kim
> An enormous amount of aerodynamic heat is produced on the surface of hypersonic vehicles, and the thermoelectric generator (TEG) technique holds the potential to convert aerodynamic heat into electric energy. In a TEG, the micrometer-scale roughness on TE legs and electrodes surfaces leads to the constriction of interfacial electric current and brings about electrical contact resistance (ECR). The heat transfer and conversion processes of a TEG are greatly influenced by such type of ECR. In this work, a TEG includes two ceramic substrates and a middle TE layer is established, and the TE layer consists of insulation material, N- and P-type TE legs and electrodes to connect the TE legs. The ECR and its effects on the TEG performance are studied by two-scale numerical simulations and experimental measurements. First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography. An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively. The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements. Second, the TE conversion process of TEG is simulated by a millimeter-scale model including insulation materials, TE legs, electrodes, and equivalent interfacial layers of ECR. The influence of ECR on the TE performance of TEG for the hypersonic vehicle is thus clarified.

### 7.4 摘要中文翻译

> 高超音速飞行器表面会产生大量的气动热，而热电发电机（TEG）技术具有将气动热转化为电能的潜力。在 TEG 中，TE 腿和电极表面的微米级粗糙度会导致界面电流收缩并产生接触电阻 (ECR)。 TEG 的传热和转换过程很大程度上受此类 ECR 的影响。在这项工作中，TEG包括两个陶瓷基板，并建立了中间TE层，TE层由绝缘材料、N型和P型TE腿以及连接TE腿的电极组成。通过两尺度数值模拟和实验测量研究了 ECR 及其对 TEG 性能的影响。首先，测量TE腿和电极粗糙表面的实际形貌，并基于重建的形貌建立微米级ECR预测数值模型。开发了ECR测量平台，该平台由压力装置、电源和数据采集系统组成，分别用于提供加载压力、电压以及电流和电压信号的采集。然后预测不同温度、加载压力和间隙介质下的 ECR，并通过一系列测量验证数值模型。其次，通过毫米级模型模拟TEG的TE转换过程，该模型包括绝缘材料、TE腿、电极和ECR的等效界面层。由此阐明了ECR对高超声速飞行器TEG TE性能的影响。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work, a TEG for hypersonic vehicles is established, and the influences of ECR on the TE conversion process and TE performance evaluation are studied by two-scale numerical simulations and experimental measurements. The practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction models are established based on the reconstructed topography. An experimental apparatus for ECR measurement under different loading pressures is developed. The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements. The TE conversion process of TEG is simulated by a millimeter-scale model, and the influence of ECR on the TE performance of the TEG for the hypersonic vehicle is thus clarified. The results show some conclusions:
> 
> 1. The numerical models of the ECR prediction are established based on the measured practical topography of rough surfaces for TE legs and electrodes, and the proposed approach can be used to predict the electrical contact resistance under different temperatures, loading pressures and gap mediums.
> 
> 2. The contact area increases approximately linear with the growth of loading pressure, while the maximum dimensional real contact area is less than 0.6% when the pressure is below 0.3 MPa.
> 
> 3. With the growth of temperature, the ECRs between the Ntype TE leg and electrodes gradually increase, and the ECRs between the P -type TE leg and electrodes first increase and then decrease, which is mainly affected by the variation law of the electrical conductivity of the TE materials.
> 
> 4. The ECR decreases while the tendency slows down with the growth of loading pressure. The ECR obtained in the silverepoxy adhesive condition (about $8.96 ~ \times ~ 10 ^ {- 10}$ to 10.2 × $1 {\dot {0}} ^ {- 1 {\dot {0}}} ~ \Omega \cdot \mathrm{m} ^ {2}$ at 400 K and 0.1 MPa) is much smaller and also less sensitive to the variation of loading pressure than that of air gap condition (about $2.70 \times 10 ^ {- 7} \mathrm {{\ t o \ 1.06 \times 10 ^ {- 6} \Omega ^ {.} m ^ {2}}}$ at 400 K and 0.1 MPa).
> 
> 5. The developed experimental apparatus can measure ECRs under different loading pressures. The experimental and numerical results have a relatively good agreement with largest differences of 13.2%, 14.9%, 38.9% and 17.7% for “E-N\_l”, “E-N\_u”, $\ " \mathrm{E} \ / - \ : P \_ {\mathrm{l}} \ "$ and $\ " \mathrm{E} - P \_ \mathrm{u"}$ , respectively.
> 
> 6. The influence of ECR on the TE conversion process of the TEG cannot be ignored. The ECR reduces the maximum output power of the TEG by increasing the internal electric resistance, and it decreases by about 83% and 2.0% under air and the silver-epoxy adhesive condition, respectively.
> 
> 7. For the TEG applied to hypersonic vehicles, the negative influence of the ECR between TE legs and electrodes can be significantly reduced by using interfacial materials with high electrical conductivity, and can be slightly reduced by applying an appropriate pre-compressed force.

### 7.6 结论中文翻译

> 本工作建立了高超声速飞行器TEG，通过两尺度数值模拟和实验测量研究了ECR对TE转换过程和TE性能评估的影响。测量了TE腿和电极粗糙表面的实际形貌，并基于重建形貌建立了微米级ECR预测模型。研制了不同加载压力下ECR测量的实验装置。然后预测不同温度、加载压力和间隙介质下的 ECR，并通过一系列测量验证数值模型。通过毫米级模型模拟了TEG的TE转换过程，明确了ECR对高超声速飞行器TEG TE性能的影响。结果显示出一些结论：1.基于测量的TE腿和电极粗糙表面的实际形貌，建立了ECR预测的数值模型，该方法可用于预测不同温度、加载压力和间隙介质下的电接触电阻。接触面积随加载压力的增长近似线性增加，而当压力低于0.3 MPa时，最大尺寸实际接触面积小于0.6%。随着温度的升高，N型TE脚与电极之间的ECR逐渐增大，P型TE脚与电极之间的ECR先增大后减小，这主要受TE材料电导率变化规律的影响。随着加载压力的增加，ECR降低，但趋势减慢。
> 
> 在银环氧树脂粘合剂条件下获得的 ECR（在 400 K 和 0.1 MPa 下约为 $8.96 ~ \times ~ 10 ^ {- 10}$ 至 10.2 × $1 {\dot {0}} ^ {- 1 {\dot {0}}} ~ \Omega \cdot \mathrm{m} ^ {2}$）要小得多，并且对加载压力的变化也比空气更不敏感间隙条件（约 $2.70 \times 10 ^ {- 7} \mathrm {{\ t o \ 1.06 \times 10 ^ {- 6} \Omega ^ {.} m ^ {2}}}$ 在 400 K 和 0.1 MPa 下）。所开发的实验装置可以测量不同加载压力下的ECR。实验和数值结果具有较好的一致性，“E-N\_l”、“E-N\_u”、$\ " \mathrm{E} \ / - \ : P \_ {\mathrm{l}} \ "$ 和 $\ " \mathrm{E} - P \_ \mathrm{u"}$ 的最大差异为 13.2%、14.9%、38.9% 和 17.7%，分别。 ECR对TEG的TE转化过程的影响不可忽视。 ECR通过增加内电阻降低了TEG的最大输出功率，在空气和银环氧树脂粘合剂条件下分别降低了约83%和2.0%。对于应用于高超声速飞行器的TEG，通过使用高导电率的界面材料可以显着降低TE腿与电极之间ECR的负面影响，并且通过施加适当的预压缩力可以稍微降低。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 8349 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The TEG for hypersonic vehicles | 对象/条件/子问题展开 | 3097 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Physical properties of materials | 对象/条件/子问题展开 | 1652 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3. Two-scale numerical model | 方法建构 | 2072 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. Rough surfaces | 对象/条件/子问题展开 | 1114 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.2.1. Model formation and meshing | 方法建构 | 2831 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3.2.2. Analysis method and boundary conditions | 方法建构 | 4239 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.3. TE conversion performance evaluation | 结果验证/讨论 | 2687 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 9 | 3.4.1. Mechanical contact process | 对象/条件/子问题展开 | 4789 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.4.2. Heat conduction and TE conversion processes | 对象/条件/子问题展开 | 951 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4. Experimental measurement platform for ECR | 实验或测量设定 | 2572 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 12 | 5.1. Contact mechanics | 对象/条件/子问题展开 | 4884 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 5.2. Electric conduction | 对象/条件/子问题展开 | 5425 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.3.1. The influence of temperature | 对象/条件/子问题展开 | 4161 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.3.2. The influence of loading pressure | 对象/条件/子问题展开 | 2389 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5.3.3. The experimental measurement results and the validation of numerical models | 方法建构 | 1867 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 17 | 5.4. TE performance | 结果验证/讨论 | 4451 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 6. Conclusion | 主张回收/边界说明 | 3089 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 19 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 438 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(224)；fig(95)；contact(86)；teg(78)；times(72)；ecr(71)；surface(71)；leg(67)；temperature(54)；respectively(52)；about(49)；loading(48)；gap(45)；legs(41)；type(40)；partial(40)；rough(38)；surfaces(38)；potential(36)；electrodes(36)
- 高频学术名词/术语：temperature(54)；pressure(35)；resistance(30)；compression(30)；displacement(28)；conversion(20)；conductivity(20)；distribution(16)；density(16)；influence(13)；performance(12)；conduction(12)；mechanics(10)；variation(10)；simulation(9)
- 高频学术动词：developed(7)；obtained(5)；validated(3)；predict(2)；predicted(2)；indicated(2)；compared(2)；optimized(1)；presented(1)；evaluated(1)；obtain(1)；compare(1)
- 高频形容词：partial(40)；potential(36)；electric(34)；displacement(28)；electrical(26)；hypersonic(25)；adhesive(25)；current(22)；real(22)；material(19)；numerical(17)；equivalent(15)；interfacial(15)；thermal(14)；internal(13)
- 高频副词：respectively(52)；gradually(12)；mainly(8)；significantly(6)；supply(5)；relatively(4)；slightly(4)；directly(3)；usually(2)；basically(2)；similarly(2)；greatly(1)
- 高频二词短语：mathrm mathrm(133)；loading pressure(32)；n-type leg(30)；type leg(30)；upper surface(29)；rough surfaces(28)；compression displacement(26)；times times(25)；legs electrodes(21)；contacting pairs(21)；lower surface(21)；real contact(20)；fig shows(20)；silver-epoxy adhesive(20)；frac partial(20)
- 高频三词短语：mathrm mathrm mathrm(100)；surface n-type leg(19)；omega cdot mathrm(19)；surface type leg(18)；times omega cdot(17)；maximum output power(15)；rough surfaces legs(14)；output power teg(13)；times times omega(12)；real contact region(11)；upper surface n-type(11)；upper surface type(11)
- 被动语态估计：117
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：308
- 一般过去时线索：238
- 现在完成时线索：4
- 情态动词线索：59

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：The management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [2].
  - 可迁移句型：{object} management of such a large amount of heat is one of the most critical issues to be solved for the development of hypersonic engineering [2].
### gap/转折句
- 原句：However, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.
  - 可迁移句型：{object}, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.
### 方法提出句
- 原句：First, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography.
  - 可迁移句型：{object}, the practical topography of rough surfaces for TE legs and electrodes is measured, and the micrometer-scale ECR prediction numerical models are established based on the reconstructed topography.
- 原句：An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
  - 可迁移句型：{object} ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
- 原句：The ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
  - 可迁移句型：{object} ECRs under different temperatures, loading pressures and gap mediums are then predicted and the numerical models are validated by a series of measurements.
- 原句：Second, the TE conversion process of TEG is simulated by a millimeter-scale model including insulation materials, TE legs, electrodes, and equivalent interfacial layers of ECR.
  - 可迁移句型：{object}, the TE conversion process of TEG is simulated by a millimeter-scale model including insulation materials, TE legs, electrodes, and equivalent interfacial layers of ECR.
### 结果证明句
- 原句：3 shows the geometric model and the mesh model of the contacting pairs.
  - 可迁移句型：3 shows the geometric model and the mesh model of the contacting pairs.
- 原句：For the convenience of description, the four contacting pairs are indicated as “E-N\_l” (the contacting pair composed of the electrode and Fig.
  - 可迁移句型：{object} the convenience of description, the four contacting pairs are indicated as “E-N\_l” (the contacting pair composed of the electrode and Fig.
- 原句：4 shows the analysis method, boundary conditions and contact properties of the contact pairs.
  - 可迁移句型：4 shows the analysis method, boundary conditions and contact properties of the contact pairs.
- 原句：4 (a) shows the surface definition, where RP is a reference point directly above the center of surface P 1, $P _ {\mathrm{r}} 1$ is the rough surface of TE legs, and $P _ {\Gamma} 2$ is the rough surface of electrodes.
  - 可迁移句型：4 (a) shows the surface definition, where {object} is a reference point directly above the center of surface P 1, $P _ {\mathrm{r}} 1$ is the rough surface of TE legs, and $P _ {\Gamma} 2$ is the rough surface of electrodes.
### 贡献收束句
- 原句：An ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
  - 可迁移句型：{object} ECR measurement platform is developed and the platform consists of a pressure device, power supply and data acquisition system which are used to provide loading pressures, voltage, and acquisition of electric current and voltage signals, respectively.
- 原句：The thermoelectric (TE) conversion techniques can convert the aerodynamic heat and engine combustion heat into electrical power, the thermal protection system that is integrated with TE generators (TEG) [4–7] has potential efficiency improvement in heat management and is one of the most prospective techniques for the heat management of hypersonic vehicles.
  - 可迁移句型：{object} thermoelectric (TE) conversion techniques can convert the aerodynamic heat and engine combustion heat into electrical power, the thermal protection system that is integrated with TE generators (TEG) [4–7] has potential efficiency improvement in heat m
- 原句：A TEG should consist of the N- and P -type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
  - 可迁移句型：{object} TEG should consist of the N- and P -type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
- 原句：CoSb3 [16–18] based skutterudites are narrow bandgap semiconductors having high electrical conductivity and Seebeck coefficient, and the TE performance of bulk CoSb3 has been greatly improved by filling [19], doping [20] and nano-crystallization techniques [21,22].
  - 可迁移句型：CoSb3 [16–18] based skutterudites are narrow bandgap semiconductors having high electrical conductivity and {object} coefficient, and the TE performance of bulk CoSb3 has been greatly improved by filling [19], doping [20] and nano-crystallization techniques [2
### 边界/谨慎句
- 原句：In traditional design, the vehicle’s structure is insulated from most of the aerodynamic heat by thermal protection systems, whose weight and size could be unaffordable under hypersonic conditions.
  - 可迁移句型：{object} traditional design, the vehicle’s structure is insulated from most of the aerodynamic heat by thermal protection systems, whose weight and size could be unaffordable under hypersonic conditions.
- 原句：Thus, new heat management techniques [3] with potential high efficiency should be developed.
  - 可迁移句型：{object}, new heat management techniques [3] with potential high efficiency should be developed.
- 原句：A TEG should consist of the N- and P -type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
  - 可迁移句型：{object} TEG should consist of the N- and P -type TE legs to convert heat into electricity by Seebeck effect, the electrodes to connect TE legs and form an electric current path, and the insulation materials to reduce the thermal radiation.
- 原句：However, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.
  - 可迁移句型：{object}, due to the low working temperature of the substrate material, the use of the film-shaped TE materials in hypersonic vehicles is limited.

## 9. 引用风险层

- 正文引用簇估计：37
- 参考文献条数：48
- 可识别年份条目数：84
- 2021 年及以后参考文献数：23
- 2010 年以前经典文献数：6
- 高频来源粗略识别：Sci. Technol(7)；Therm. Eng(5)；Mater. Chem. A(2)；Phys. Lett(2)；Alloys Compd(2)；Funct. Mater(2)；J. Heat Mass Transf(2)；Manag(2)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] K. An, Z yun Guo, X ping Xu, W Huang, A framework of trajectory design and optimization for the hypersonic gliding vehicle, Aerosp. Sci. Technol. 106 (2020) 106110, https://doi .org /10 .1016 /j .ast .2020 .106110.
- [2] W. Chen, R. Wang, X. Li, S. Lu, X. Fang, Study of the heat transfer design of an integrated thermal management system for hypersonic vehicles using su- percritical nitrogen as expendable coolant, Aerosp. Sci. Technol. 123 (2022) 107440, https://doi .org /10 .1016 /j .ast .2022 .107440.
- [3] P. Fernández-Yáñez, V. Romero, O. Armas, G. Cerretti, Thermal management of thermoelectric generators for waste energy recovery, Appl. Therm. Eng. (2021) 196, https://doi .org /10 .1016 /j .applthermaleng .2021.117291.
- [4] G. Gao, J.J. Gou, C.L. Gong, J.X. Hu, R.C. Gao, A novel mechanical-thermal- electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962, https://doi .org /10 .1016 /j .compstruct .2021.113962.
- [5] K. Cheng, J. Qin, H. Sun, C. Dang, S. Zhang, X. Liu, et al., Performance as- sessment of an integrated power generation and refrigeration system on hy- personic vehicles, Aerosp. Sci. Technol. 89 (2019) 192–203, https://doi .org /10 . 1016 /j .ast .2019 .04 .006.
- [6] K. Cheng, J. Qin, Y. Jiang, C. Lv, S. Zhang, W. Bao, Performance assessment of multi-stage thermoelectric generators on hypersonic vehicles at a large temperature difference, Appl. Therm. Eng. 130 (2018) 1598–1609, https:// doi .org /10 .1016 /j .applthermaleng .2017.11.057.
- [7] K. Cheng, D. Zhang, J. Qin, S. Zhang, W. Bao, Performance evaluation and com- parison of electricity generation systems based on single- and two-stage ther- moelectric generator for hypersonic vehicles, Acta Astronaut. 151 (2018) 15–21, https://doi .org /10 .1016 /j .actaastro .2018 .05 .033.
- [8] H.T. Zhu, J. Luo, J.K. Liang, Synthesis of highly crystalline Bi2Te3 nanotubes and their enhanced thermoelectric properties, J. Mater. Chem. A 2 (2014) 12821–12826, https://doi .org /10 .1039 /c4ta02532f.
- [9] X. Shi, H. Kong, C.P. Li, C. Uher, J. Yang, J.R. Salvador, et al., Low thermal conductivity and high thermoelectric figure of merit in n-type Bax Yby Co4 Sb12 double-filled skutterudites, Appl. Phys. Lett. 92 (2008) 90–93, https:// doi .org /10 .1063 /1.2920210.
- [10] L. Zhang, X. Chen, Y. Tang, L. Shi, G.J. Snyder, J.B. Goodenough, et al., Thermal stability of Mg2Si0.4Sn0.6 in inert gases and atomic-layer-deposited Al2O3 thin film as a protective coating, J. Mater. Chem. A 4 (2016) 17726–17731, https:// doi .org /10 .1039 /c6ta07611d.
- [11] B. Yang, S. Li, X. Li, Z. Liu, H. Zhong, S. Feng, Ultralow thermal conductiv- ity and enhanced thermoelectric properties of SnTe based alloys prepared by melt spinning technique, J. Alloys Compd. 837 (2020) 155568, https:// doi .org /10 .1016 /j .jallcom .2020 .155568.
- [12] Z. Soleimani, S. Zoras, B. Ceranic, Y. Cui, S. Shahzad, A comprehensive review on the output voltage/power of wearable thermoelectric generators concerning their geometry and thermoelectric materials, Nano Energy 89 (2021) 106325, https://doi .org /10 .1016 /j .nanoen .2021.106325.
- [13] L. Liang, M. Wang, X. Wang, P. Peng, Z. Liu, G. Chen, et al., Initiating a stretch- able, compressible, and wearable thermoelectric generator by a spiral archi- tecture with ternary nanocomposites for efficient heat harvesting, Adv. Funct. Mater. 32 (2022) 1–11, https://doi .org /10 .1002 /adfm .202111435.
- [14] C. Du, M. Cao, G. Li, Y. Hu, Y. Zhang, L. Liang, et al., Toward precision recognition of complex hand motions: wearable thermoelectrics by synergis- tic 2D nanostructure confinement and controlled reduction, Adv. Funct. Mater. 2206083 (2022) 1–9, https://doi .org /10 .1002 /adfm .202206083.
- [15] G. Rogl, A. Grytsiv, P. Rogl, E. Bauer, M. Hochenhofer, R. Anbalagan, et al., Nanostructuring of p- and n-type skutterudites reaching figures of merit of ap- proximately 1.3 and 1.6, respectively, Acta Mater. 76 (2014) 434–448, https:// doi .org /10 .1016 /j .actamat .2014 .05 .051.

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
