# 论文深度拆解：The innovation of an aerodynamic-heat-harvest TEG considering multi-interface contact effect for a high-speed flight vehicle

> 生成依据：`801/cleantext/041-The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`041-The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.pdf`
- 页数：18
- clean body 字符数：46564
- 摘要字符数：1416
- 参考文献条数：48
- 图题数：20
- 表题数：13
- 表格文件数：14
- 公式候选数：113
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "14 formula(s) need manual review."}]

## 1. 身份层

- 标题：The innovation of an aerodynamic-heat-harvest TEG considering multi-interface contact effect for a high-speed flight vehicle
- 年份：2025
- 期刊/来源：Applied Ther
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：实验/测量 + 性能分析型
- 研究对象：Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.
- 主要方法：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified. Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topography [29]. In the authors’ previous works [30,31], an optical profiler is used to measure the 
- 主要证据：图表 33 个标题、公式 113 个候选、参考文献 48 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.”，可以通过“Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and vali”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively. Liu et al. [22] studied the TCR between bearing inner ring and shaft journal, and found that the interference fit reduces the TCR because the interference fit reduces the interfacial contact area. Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is affected by the material properties.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.
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
- 作者声明或文本中可见 gap：Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency. The TEG mainly consists of several couples of TE legs (N- and P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows. However, most published reports on contact effects focused on conventional metallic materials (e.g., Fe, Al, Cu, $\operatorname{Zn} ,$ and Mn) and their alloys, with fewer studies on the TCR and ECR of TE materials.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
- In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes one N- and P-type TE leg), totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured, leading to unaffordable cost.

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified. Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topography [29]. In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes The evaluation of TEG performance consists of two processes: microscale contact effects calculation and macro-scale performance analysis.
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
| Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated,  | 摘要/引言/结论候选 | 图：Fig. 1. Schematic diagram of TEGs for a high-speed flight vehicle. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is | 摘要/引言/结论候选 | 图：Fig. 2. Schematic diagram of the TEG and its components. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| (10) shows that the equivalent thermal conductance for the thermal radiation from A (source surface) to B (target surface) at T, equals to the heat flux of the thermal radiation. | 摘要/引言/结论候选 | 图：Fig. 3. Fabrication and assembly process of TEG. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| As shown in Table 9, the maximum differences $\mathrm {_ {d f}} \cdots \mathrm{E} - N ^ {\prime}$ and $\mathrm {^ {66}}$ are − 13.4 % and − 4.56 %, respectively. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The maximum deviation within 15 % (compared to similar literature data accuracy) and the trend is reasonable, which indicates the numerical model is highly reliable. | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The positive sign for the difference indicates that the measured value exceeds the numerically calculated value and vice versa. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 161.02, 426.05, 200.25)]] The innovation of an a | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. Schematic diagram of TEGs for a high-speed flight vehicle. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 2. Schematic diagram of the TEG and its components. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 3. Fabrication and assembly process of TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Measurement and reconstruction of rough surfaces. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. Meshed models of contacting pairs and TEG. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 6. Aerodynamic meshed model and external thermo-mechanical loads. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 7. Boundary conditions of contacting pairs and TEG. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Experimental measurements of TCR. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Experimental measurements of TEG performance. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Dimensionless real contact aera varied with loading pressure. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Stress distribution of rough surfaces for contacting pairs. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 12. TCRs between electrodes and TE legs. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. ECRs between electrodes and TE legs. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Comparison between equivalent model and micro-scale interfa- cial model. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 15. Temperature distribution under different clearances. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 8 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 9 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 10 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 161.02, 426.05, 200.25)]] The innovation of an aerodynamic-heat-harv | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 206.22, 463.46, 223.92)]] Shi-Yuan Chen a, Hai-Peng Chen b, Ge Gao a | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.63, 669.07, 202.04, 690.38)]] * Corresponding author. E-mail address: jj.gou@nwpu.edu. | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 346.33, 716.91)]] https://doi.org/10.1016/j.applthermaleng.2 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (378.76, 76.22, 414.77, 103.77)]] Specific heat capacity (J/(kg⋅K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (441.69, 76.22, 476.89, 103.77)]] Thermal conductivity (W/(m⋅K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (52.39, 165.94, 529.31, 185.46)]] Silver-epoxy adhesive 2.3 / / 0.34.50 \times 10-5504 / 1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (166.28, 225.04, 201.48, 252.59)]] Thermal conductivity (W/(m⋅K)) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> High-speed flight vehicles generate large amounts of aerodynamic heat during long-duration flights, so the aerodynamic heat harvest based on thermoelectric (TE) conversion is one of the most promising thermal man- agement techniques. In this work, a heat-harvest thermoelectric generator (TEG) is innovatively created and evaluated with the fully consideration of multiple heterogeneous interfaces effect. At first, a TEG including a force-bearing frame, twenty-seven couples of cylindrical TE legs, fifty-four couples of electrodes, two substrates, an insulation layer and two types of heterogeneous interfaces is designed and fabricated to possess the heat- harvest and force-bear functions simultaneously. Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified. Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively.

### 7.4 摘要中文翻译

> 高速飞行器在长时间飞行过程中会产生大量的气动热量，因此基于热电（TE）转换的气动热量收集是最有前途的热管理技术之一。在这项工作中，充分考虑多种异质界面效应，创新地创建和评估了热收集热电发电机（TEG）。首先，设计并制造了一个包含受力框架、27对圆柱形TE腿、54对电极、两个基板、绝缘层和两种异质界面的TEG，使其同时具有集热和受力功能。其次，基于接触式测量和W-M函数重建了TE腿和电极的表面形貌，通过间接实验测量建立并验证了热电阻和电接触电阻的数值模型，并阐明了压力、温度和间隙介质的影响。再次，考虑微尺度接触电阻，分析了发电机的TE传递和转换过程；对车辆典型气动条件下的TE和机械性能进行了数值和实验评估，得出TEG的最大电压和输出功率分别为6.978 V和12.41 W。

### 7.5 结论完整摘录

识别到的结论位置：6. Conclusion

> In this work, an aerodynamic-heat-harvest TEG is innovatively developed and evaluated based on the full consideration of the multiinterface contact effect. The TEG including a force-bearing frame, twenty-seven couples of cylindrical TE legs, fifty-four couples of electrodes, two substrates, an insulation layer and two types of heterogeneous interfaces is designed and fabricated. The TEG possess the heatharvest and force-bear functions simultaneously. The surface topography of TE legs and electrodes are reconstructed based on the contacttype measurement and W-M function, numerical models of thermal and electrical contact resistances are established and experimentally validated, and the influences of pressure, temperature and clearance medium are clarified. The performance of TEG considering micro-scale contact resistances is numerically and experimentally evaluated under the vehicle’s typical aerodynamic conditions. Some conclusions are obtained:
> 
> (a) Twenty-seven TE couples
> 
> (b) Force-bearing frame
> 
> (c) TE 1egs
> 
> (a) TE 1egs
> 
> (b) TEG
> 
> 1. The TCR and ECR decrease with the increase of loading pressure and average temperature of the interfaces, and they are reduced by the presence of clearance medium. When the loading pressure varies from 0.8179 to 3.041 MPa, the TCR decreases from $12.63 \times {{10} ^ {- 4}}$ to $2.920 \times 10 ^ {- 4} , 6.571 \times 10 ^ {- 4} {\mathrm{to}} 2.106 \times 10 ^ {- 4}$ and $3.377 \times 10 ^ {- 5}$ to $2.485 \times 10 ^ {- 5} ( \mathrm{K} {\cdot} \mathrm{m} ^ {2} ) / \mathrm{W}$ under vacuum, air and silver-epoxy adhesive clearance, respectively; the ECR varies from $17.20 \times 10 ^ {- 8}$ to $4.348 \times 10 ^ {- 8} , 8.151 \times 10 ^ {- 10} \mathrm {{t o}} 6.919 \times 10 ^ {- 10} \mathrm {{\Omega}} \Omega {\cdot} \mathrm {{m}} ^ {2}$ under air/ vacuum and silver-epoxy adhesive clearance, respectively.
> 
> 2. The TCR model is validated by indirect experimental measurements with the maximum deviation of 13.4 %.
> 
> 3. The fabricated TEG has the ability to capture aerodynamic heat to generate power with the maximum voltage, output power and conversion efficiency are 6.978 V, 12.41 W and 2.334 %, respectively (at 0.1 MPa and under the silver-epoxy adhesive clearance).
> 
> 4. The equivalent interfacial model can be used to evaluate the performance of the TEG under consideration of interfacial contact effects with a maximum model deviation of 0.444 %. The thermoelectric and mechanical performance are influenced by the loading pressure and the clearance medium, and the force-bearing frame has the highest Mises stress of 7.88 MPa under the silverepoxy adhesive clearance and 7.68 MPa under air clearance.
> 
> 5. Experimental measurements validated the TEG evaluation model with a maximum deviation in output voltage of − 19.69 %.

### 7.6 结论中文翻译

> 本工作在充分考虑多界面接触效应的基础上，创新性地开发和评估了气动热收集TEG。设计并制作了TEG，包括受力框架、27对圆柱形TE腿、54对电极、两个基板、绝缘层和两种异质界面。 TEG同时具备吸热和受力功能。基于接触式测量和W-M函数重建了TE腿和电极的表面形貌，建立了热和电接触电阻的数值模型并进行了实验验证，并阐明了压力、温度和间隙介质的影响。在车辆的典型空气动力学条件下，对考虑微尺度接触电阻的 TEG 性能进行了数值和实验评估。得到了一些结论： (a) 27 个 TE 力偶 (b) 受力框架 (c) TE 1egs (a) TE 1egs (b) TEG 1。TCR 和 ECR 随着加载压力和界面平均温度的增加而减小，并且由于间隙介质的存在而减小。
> 
> 当加载压力从0.8179变化到3.041 MPa时，TCR从$12.63 \times {{10} ^ {- 4}}$下降到$2.920 \times 10 ^ {- 4}、6.571 \times 10 ^ {- 4} {\mathrm{to}} 2.106 \times 10 ^ {- 4}$ 和 $3.377 \times 10 ^ {- 5}$ 到 $2.485 \times 10 ^ {- 5} ( \mathrm{K} {\cdot} \mathrm{m} ^ {2} ) / \mathrm{W}$ 分别在真空、空气和银环氧树脂粘合剂间隙下； ECR 的变化范围为 $17.20 \times 10 ^ {- 8}$ 到 $4.348 \times 10 ^ {- 8} 、 8.151 \times 10 ^ {- 10} \mathrm {{t o}} 6.919 \times 10 ^ {- 10} \mathrm {{\Omega}} \Omega {\cdot} \mathrm {{m}} ^ {2}$ 分别在空气/真空和银环氧树脂粘合剂间隙下。 TCR模型通过间接实验测量进行验证，最大偏差为13.4%。所制备的 TEG 能够捕获空气动力热量来发电，最大电压、输出功率和转换效率分别为 6.978 V、12.41 W 和 2.334%（在 0.1 MPa 和银环氧树脂粘合剂间隙下）。等效界面模型可用于评估考虑界面接触效应的TEG性能，最大模型偏差为0.444%。热电性能和机械性能受加载压力和间隙介质影响，受力框架在银胶间隙下具有最高Mises应力，为7.88 MPa，在空气间隙下为7.68 MPa。实验测量验证了 TEG 评估模型，输出电压的最大偏差为 − 19.69 %。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6519 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. The TEG with multi-interfaces | 对象/条件/子问题展开 | 5775 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Fabrication and assembly of TEGs | 实验或测量设定 | 1189 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. Rough surfaces measurement and reconstruction | 实验或测量设定 | 3158 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 5 | 3. Two-scale TEG evaluation model | 方法建构 | 262 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.1. Governing equations | 对象/条件/子问题展开 | 3241 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.2. Calculation method of TCR and ECR | 方法建构 | 1850 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 3.3. Equivalent interfacial layers in TEG | 对象/条件/子问题展开 | 1477 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.4. Meshed models | 方法建构 | 2238 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 10 | 3.5. Boundary conditions | 对象/条件/子问题展开 | 3692 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.1. TCR measurements under different pressure and temperature | 实验或测量设定 | 1550 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 12 | 4.2. Power supply measurement of TEG | 实验或测量设定 | 933 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 13 | 5.1.1. Contact mechanics | 对象/条件/子问题展开 | 1610 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 5.1.2. Thermal and electrical contact resistances | 对象/条件/子问题展开 | 1470 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 5.1.3. The comparison with experimental results | 结果验证/讨论 | 1823 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 16 | 5.2.1. Validation of the equivalent interfacial layers | 对象/条件/子问题展开 | 992 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 5.2.2. Thermo-mechanical performance | 结果验证/讨论 | 1997 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 18 | 5.2.3. TEG performance | 结果验证/讨论 | 1858 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 19 | 5.2.4. The comparison with experimental results | 结果验证/讨论 | 666 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 20 | 6. Conclusion | 主张回收/边界说明 | 2791 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 21 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 413 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

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

- 高频词：teg(73)；contact(61)；clearance(59)；legs(57)；temperature(53)；respectively(42)；partial(40)；fig(39)；surface(38)；surfaces(37)；pressure(35)；heat(34)；mathrm(34)；adhesive(31)；frac(30)；electrodes(29)；tcr(29)；silver-epoxy(29)；equivalent(27)；times(27)
- 高频学术名词/术语：clearance(59)；temperature(53)；pressure(35)；performance(21)；measurement(14)；compression(13)；deviation(13)；conversion(12)；distribution(12)；deformation(11)；difference(9)；insulation(9)；conduction(8)；function(8)；radiation(7)
- 高频学术动词：evaluated(4)；validated(4)；construct(2)；developed(2)；constructed(2)；evaluate(2)；obtained(2)；demonstrated(1)；obtain(1)；indicate(1)；compared(1)
- 高频形容词：partial(40)；adhesive(31)；equivalent(27)；thermal(26)；electrical(21)；real(20)；interfacial(19)；experimental(16)；table(15)；measurement(14)；aerodynamic(12)；fractal(9)；cylindrical(8)；heterogeneous(6)；hexahedral(6)
- 高频副词：respectively(42)；mainly(7)；numerically(7)；effectively(4)；assembly(4)；significantly(3)；accurately(3)；supply(3)；experimentally(3)；slightly(3)；directly(2)；indirectly(2)
- 高频二词短语：silver-epoxy adhesive(29)；adhesive clearance(24)；loading pressure(22)；frac partial(17)；real contact(15)；force-bearing frame(15)；air clearance(13)；contact effects(12)；contact area(12)；rough surfaces(12)；p-type legs(12)；equivalent interfacial(12)；clearance medium(11)；integrated electrode(11)；table lists(11)
- 高频三词短语：silver-epoxy adhesive clearance(22)；real contact area(11)；frac partial partial(9)；partial frac partial(8)；equivalent interfacial layers(7)；integrated electrode substrate(7)；air clearance silver-epoxy(7)；clearance silver-epoxy adhesive(7)；elements nodes elements(7)；nodes elements nodes(7)；twenty-seven couples cylindrical(6)；couples cylindrical legs(6)
- 被动语态估计：116
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：217
- 一般过去时线索：253
- 现在完成时线索：1
- 情态动词线索：31

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.
  - 可迁移句型：{object}, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles.
- 原句：Accurate characterization of the rough surface is a necessary prerequisite for the precise assessment of the contact effect.
  - 可迁移句型：{object} characterization of the rough surface is a necessary prerequisite for the precise assessment of the contact effect.
### gap/转折句
- 原句：Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
  - 可迁移句型：{object} thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency
- 原句：The TEG mainly consists of several couples of TE legs (N- and P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows.
  - 可迁移句型：{object} TEG mainly consists of several couples of TE legs (N- and P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electric
- 原句：However, most published reports on contact effects focused on conventional metallic materials (e.g., Fe, Al, Cu, $\operatorname{Zn} ,$ and Mn) and their alloys, with fewer studies on the TCR and ECR of TE materials.
  - 可迁移句型：{object}, most published reports on contact effects focused on conventional metallic materials (e.g., Fe, Al, Cu, $\operatorname{Zn} ,$ and Mn) and their alloys, with fewer studies on the TCR and ECR of TE materials.
- 原句：In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes The evaluation of TEG performance consists of two processes: microscale contact effects calculation and macro-scale performance analysis.
  - 可迁移句型：{object} the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in This study, the TEG consists of twenty-seven TE couples (one TE couple incl
### 方法提出句
- 原句：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
  - 可迁移句型：{object}, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurem
- 原句：Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topography [29].
  - 可迁移句型：{object} methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topog
- 原句：In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes The evaluation of TEG performance consists of two processes: microscale contact effects calculation and macro-scale performance analysis.
  - 可迁移句型：{object} the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in This study, the TEG consists of twenty-seven TE couples (one TE couple incl
- 原句：5(a) and (b) are the meshed models of contacting pairs and TEG, respectively.
  - 可迁移句型：5(a) and (b) are the meshed models of contacting pairs and {object}, respectively.
### 结果证明句
- 原句：Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively.
  - 可迁移句型：{object}, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated,
- 原句：Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is affected by the material properties.
  - 可迁移句型：{object} et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the T
- 原句：(10) shows that the equivalent thermal conductance for the thermal radiation from A (source surface) to B (target surface) at T, equals to the heat flux of the thermal radiation.
  - 可迁移句型：(10) shows that the equivalent thermal conductance for the thermal radiation from {object} (source surface) to B (target surface) at T, equals to the heat flux of the thermal radiation.
- 原句：As shown in Table 9, the maximum differences $\mathrm {_ {d f}} \cdots \mathrm{E} - N ^ {\prime}$ and $\mathrm {^ {66}}$ are − 13.4 % and − 4.56 %, respectively.
  - 可迁移句型：{object} shown in Table 9, the maximum differences $\mathrm {_ {d f}} \cdots \mathrm{E} - N ^ {\prime}$ and $\mathrm {^ {66}}$ are − 13.4 % and − 4.56 %, respectively.
### 贡献收束句
- 原句：Liu et al. [22] studied the TCR between bearing inner ring and shaft journal, and found that the interference fit reduces the TCR because the interference fit reduces the interfacial contact area.
  - 可迁移句型：{object} et al. [22] studied the TCR between bearing inner ring and shaft journal, and found that the interference fit reduces the TCR because the interference fit reduces the interfacial contact area.
- 原句：The TCR and ECR decrease with the increase of loading pressure and average temperature of the interfaces, and they are reduced by the presence of clearance medium.
  - 可迁移句型：{object} TCR and ECR decrease with the increase of loading pressure and average temperature of the interfaces, and they are reduced by the presence of clearance medium.
### 边界/谨慎句
- 原句：Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
  - 可迁移句型：{object} thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency
- 原句：In this study, the TCC for the real contact elements is assumed to be perfect and given as 1 $\times ~ 10 ^ {10} ~ \mathrm {W / ( m ^ {2} {\cdot} K )}$ .
  - 可迁移句型：{object} This study, the TCC for the real contact elements is assumed to be perfect and given as 1 $\times ~ 10 ^ {10} ~ \mathrm {W / ( m ^ {2} {\cdot} K )}$ .

## 9. 引用风险层

- 正文引用簇估计：26
- 参考文献条数：48
- 可识别年份条目数：48
- 2021 年及以后参考文献数：23
- 2010 年以前经典文献数：5
- 高频来源粗略识别：Therm. Eng(11)；J. Heat Mass Transf(10)；Energy(9)；Sci. Technol(2)；Tribol(2)；Pt. B-Eng(1)；Struct(1)；Energ. Fuels(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] X.F. Ma, P.X. Jiang, Y.H. Zhu, Dynamic simulation and analysis of transient characteristics of a thermal-to-electrical conversion system based on supercritical CO2 Brayton cycle in hypersonic vehicles, Appl. Energy 359 (2024).
- [2] J.J. Gou, Z.W. Yan, J.X. Hu, G. Gao, C.L. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021).
- [3] W.Z. Yang, X.Y. Zhang, Y. Cui, Z.T. Chen, Thermal and fracture analysis of collinear interface cracks in graded coating systems under ramp-type heating, Int. J. Heat Mass Transf. 216 (2023).
- [4] V.T. Le, N.S. Ha, N.S. Goo, Advanced sandwich structures for thermal protection systems in hypersonic vehicles: A review, Compos. Pt. B-Eng. 226 (2021).
- [5] G. Gao, D. Li, J.J. Gou, C.L. Gong, S.M. Li, A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations, Aerosp. Sci. Technol. 131 (2022) 107966.
- [6] G. Gao, J.J. Gou, C.L. Gong, J.X. Hu, R.C. Gao, A novel mechanical-thermal- electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962.
- [7] K.L. Cheng, J. Qin, D. Zhang, W. Bao, W.X. Jing, Performance evaluation for a combined power generation system of closed-Brayton-cycle and thermoelectric generator with finite cold source at room temperature on hypersonic vehicles, Energy 254 (2022).
- [8] K.L. Cheng, J. Qin, Y.G. Jiang, C.W. Lv, S.L. Zhang, W. Bao, Performance assessment of multi-stage thermoelectric generators on hypersonic vehicles at a large temperature difference, Appl. Therm. Eng. 130 (2018) 1598–1609.
- [9] W.J. Song, F.F. Bai, M.B. Chen, S.L. Lin, Z.P. Feng, Y.L. Li, Thermal management of standby battery for outdoor base station based on the semiconductor thermoelectric device and phase change materials, Appl. Therm. Eng. 137 (2018) 203–217.
- [10] S. Lan, R. Stobart, X.N. Wang, Matching and optimization for a thermoelectric generator applied in an extended-range electric vehicle for waste heat recovery, Appl. Energy 313 (2022).
- [11] B. Orr, A. Akbarzadeh, M. Mochizuki, R. Singh, A review of car waste heat recovery systems utilising thermoelectric generators and heat pipes, Appl. Therm. Eng. 101 (2016) 490–495.
- [12] J. Wei, J.W. Hui, T.T. Wang, Y. Wang, Y.P. Guo, S.Q. Zhang, Y.B. Zhang, X.Y. Qiao, A thermoelectric energy harvesting system for pavements with a fin cooling structure, Sustain. Energ. Fuels 7 (1) (2022) 248–262.
- [13] K. Li, G. Garrison, M. Moore, Y. Zhu, C. Liu, R. Horne, S. Petty, An expandable thermoelectric power generator and the experimental studies on power output, Int. J. Heat Mass Transf. 160 (2020).
- [14] H. Jing, Q.P. Xiang, R.D. Ze, X.X. Chen, J. Li, J.C. Liao, S.Q. Bai, A skutterudite thermoelectric module with high aspect ratio applied to milliwatt radioisotope thermoelectric generator, Appl. Energy 350 (2023).
- [15] W. Yang, H.P. Xie, L.C. Sun, C. Ju, B.X. Li, C.B. Li, H.Y. Zhang, H.T. Liu, An experimental investigation on the performance of TEGs with a compact heat exchanger design towards low-grade thermal energy recovery, Appl. Therm. Eng. 194 (2021).

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
