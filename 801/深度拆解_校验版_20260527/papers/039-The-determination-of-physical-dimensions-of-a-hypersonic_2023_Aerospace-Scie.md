# 论文深度拆解：039-The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie

> 生成依据：`801/cleantext/039-The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`039-The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie.pdf`
- 页数：15
- clean body 字符数：42691
- 摘要字符数：1681
- 参考文献条数：35
- 图题数：23
- 表题数：6
- 表格文件数：7
- 公式候选数：26
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "low_confidence_formulas", "severity": "medium", "message": "5 formula(s) need manual review."}]

## 1. 身份层

- 标题：039-The-determination-of-physical-dimensions-of-a-hypersonic_2023_Aerospace-Scie
- 年份：2023
- 期刊/来源：Aerospace Scie
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：工程应用 + 多物理场分析型
- 研究对象：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps. Accurate constraint conditions are essential to the structural mode analysis.
- 主要方法：Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance. The numerical models for each simulation are introduced below. 3(a) and (b) show the geometric and meshed models of CI, respectively.
- 主要证据：图表 29 个标题、公式 26 个候选、参考文献 35 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. However,”，可以通过“Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance. The numerical models for ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency. 3(a) and (b) show the geometric and meshed models of CI, respectively. The meshed model shown in Fig.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance. However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps. Accurate constraint conditions are essential to the structural mode analysis.
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
- 作者声明或文本中可见 gap：However, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of air intake system. However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps. The vehicle involved in this work has relatively large scale and thus corresponding experiment studies are difficult to carry on.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance. The numerical models for each simulation are introduced below. 3(a) and (b) show the geometric and meshed models of CI, respectively.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：工程应用 + 多物理场分析型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：工程应用 + 多物理场分析型
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
| Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance. | 摘要/引言/结论候选 | 图：Fig. 1. The hypersonic vehicle and its intake system. (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.) | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency. | 摘要/引言/结论候选 | 图：Fig. 2. Configurational parameters of the intake system. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15]. | 摘要/引言/结论候选 | 图：Fig. 3. Geometric model and meshed model of CI for mode analysis. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| 3(a) and (b) show the geometric and meshed models of CI, respectively. | 摘要/引言/结论候选 | 表：Table 2 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| 3(a), the six boundary planes are indicated by $P _ {x 0} , \ P _ {x 1} , \ P _ {y 0} , \ P _ {y 1} , \ P _ {z 0} ,$ and $P _ {z 1}$ . | 摘要/引言/结论候选 | 表：Table 4 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Such rivets are indicated by the red points in Fig. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 206.74, 422.48, 220.38)]] Jian-Jun Gou a,∗, Shu- | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The hypersonic vehicle and its intake system. (For interpretation of the colors in the figure(s), the reader is referred to the web version of this arti | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. Configurational parameters of the intake system. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 3. Geometric model and meshed model of CI for mode analysis. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 4. Computational region, mesh and information transfer. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 5. Pressure coefficient on the upper and lower walls (comparison with Refs. [22,32]). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 6. Displacement variation along with dynamic pressure (comparison with Refs. [23,34]). | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 7. Mode shape of CI under CoA. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Mode shape of CI under CoB. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Natural frequencies of different panel thicknesses for CI, CII and CIII. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. The panel stiffness along with panel thickness. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Displacement contours under aerodynamic force. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Pressure and velocity fields under CI vibration with 100 Hz and different amplitudes. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Fig. 13. Total pressure recovery and mass flow coefficients along with time (CI vi- bration with frequency of 100 Hz and amplitude of 50 mm). | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. Average values and fluctuation ranges of total pressure recovery and flow coefficients. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. Pressure and velocity fields under CI vibration with 0.05 m amplitude and different frequencies. | 结果呈现/机制解释 | 支撑方法、模型或结果可靠性 | 从标题看用于结果呈现/机制解释 | 是，图像细节需 PDF 核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 4 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 3 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 206.74, 422.48, 220.38)]] Jian-Jun Gou a,∗, Shu-Zhen Jia a, Jin-Xing | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.64, 687.49, 264.98, 714.35)]] * Corresponding authors. E-mail addresses: | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 2, bbox (306.63, 712.58, 557.7, 722.39)] [M]] {¨x} + [K]{x} = {0} (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.62; needs_review; source=equations; [page 4, bbox (46.73, 399.96, 288.71, 416.72)]] ∂t + div(ρUφ) = div(�gradφ) + Q s (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (209.58, 219.74, 456.19, 245.97)]] Inlet Ma=6, P=2971 Pa T =300 K Outlet P=0 Pa T =300 K W | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 14, bbox (37.64, 728.33, 291.37, 748.81)]] (5) For the design of thin-panel-structur | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] \left[ M \right] \left\{\ddot {x} \right\} + \left[ K \right] \left\{x \right\} = \left\{0 \right\}\ta | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] \mathrm {k g / m ^ {3}} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Communicated by Yu Lv
> The panel vibration of air intake system that excitated by fluid-structural interaction, engine thrust variation and noise has decisive influences on the performance of an air-breathing hypersonic vehicle. The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent. In this paper, an intake system with three-stage external compression ramps is designed under Mach number of 6 and flight altitude of 24 km, and the configurational parameters are determined based on the shock-on-lip criterion, Oswatitsch criterion and viscous effects modification. The mode vibration characteristics of external compression ramps with panel thicknesses of 0.002 to 0.03 m are analyzed, and appropriate natural frequencies are obtained by constraint conditions of fixed four side boundaries with an additional and more realistic constraint of strengthened internal boundary. The flow field of the intake system with forced panel vibrations of compression ramps is simulated, and the effects of vibration amplitude of 0 to 0.11 m and frequency of 10 to 250 Hz on the intake performance, i.e., total pressure recovery coefficient and mass flow coefficient are clarified. The vibration effects of hypersonic flow on the compression ramp structure and intake performance are studied by fluid-structural coupling simulations. Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance.

### 7.4 摘要中文翻译

> 吕宇 通讯 流固耦合、发动机推力变化和噪声激发的进气系统面板振动对吸气式高超声速飞行器的性能具有决定性影响。此类进气系统的设计应包含考虑流动和结构振动的结构参数和物理尺寸的确定，目前尚缺乏明确的设计路径。本文设计了马赫数为6、飞行高度为24 km的三级外压缩坡道进气系统，并根据唇上冲击准则、Oswatisch准则和粘性效应修正确定了构型参数。分析了面板厚度为0.002~0.03 m的外部压缩坡道的模态振动特性，通过固定四个侧边界的约束条件，并附加更真实的强化内部边界约束，获得了合适的固有频率。对压缩坡道强制面板振动的进气系统流场进行了仿真，明确了0～0.11 m振幅和10～250 Hz频率对进气性能即总压恢复系数和质量流量系数的影响。通过流固耦合仿真研究了高超声速流振动对压缩坡道结构和进气性能的影响。最后，确定了外部压缩坡道的可用物理尺寸，并通过考虑结构和进气性能来制定进气系统的设计路径。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> For an air-breathing hypersonic vehicle, the thin-panel structure is always adopted by the compression ramp of air intake system, the panel vibration that excitated by hypersonic flow, engine and noise has decisive effect on its performance. In this paper, a threestage compression intake system is designed under Mach number of 6 and flight altitude of 24 km. The mode vibration characteristics of compression ramps’ panels are obtained and the influence of panel vibration frequency and amplitude on the intake performance is clarified. The effect of fluid-structural interactions on the panel structure and intake performance is analyzed, and the available thicknesses are determined for the compression ramps. The design path of compression system is finally summarized. Some conclusions are obtained:
> 
> (1) In the mode analysis, higher and more appropriate natural frequency can be obtained by the clamped four side boundaries with additional strengthened internal boundary using certain number of rivets.
> 
> (a) CII panel thickness of 0.002 m
> 
> (b) CII panel thickness of 0.005 m
> 
> (c) ClI panel thickness of 0.010 m
> 
> (a) CllI panel thickness of 0.002 m
> 
> (b) CII panel thickness of 0.005 m 
> (c) CllI panel thickness of 0.010 m
> 
> (c) Fluid-structural interaction of CIlI
> 
> (2) For the three-stage compression ramps CI, CII and CIII, the natural frequency increases with the increase of panel thickness; the available upper bound of operational vibration frequencies in real conditions increases from 16.8 to 249 Hz, 17.76 to 259 Hz, and 17.12 to 251 Hz, respectively, when the panel thickness increases from 2 to 30 mm.
> 
> (3) The consideration of panels’ fluid-structural interaction will lead to the reduction and fluctuation of total pressure recovery and mass flow coefficients; the intake performance fluctuation range decreases with the increasing panel thickness and greater stiffness, and increases when the fluid-structural interaction source transfers from the fuselage leading edge to the intake lip.
> 
> (4) The natural frequency increases while the operational frequency decreases with the increase of panel thickness; the lower bound of panel thickness for CI, CII and CIII that studied in this work (two-dimensional intake system with three-stage compression ramps under Mach number of 6 and altitude of 24 km) can be considered as 5.5, 6.0 and 6.5 mm, respectively.
> 
> (5) For the design of thin-panel-structural compression system, the consideration of resonance limit is essential.

### 7.6 结论中文翻译

> 对于吸气式高超声速飞行器，进气系统压缩坡道多采用薄壁板结构，高超声速气流、发动机和噪声激发的壁板振动对其性能具有决定性影响。本文设计了马赫数6、飞行高度24km的三级压缩进气系统。获得了压缩坡道面板的模态振动特性，阐明了面板振动频率和振幅对进气性能的影响。分析了流体-结构相互作用对面板结构和进气性能的影响，并确定了压缩坡道的可用厚度。最后总结了压缩系统的设计路径。得到以下结论： (1)在模态分析中，采用一定数量的铆钉夹紧四个侧边界并附加加强内部边界，可以获得更高、更合适的固有频率。 (a) CII 面板厚度为 0.002 m (b) CII 面板厚度为 0.005 m (c) ClI 面板厚度为 0.010 m (a) CllI 面板厚度为 0.002 m (b) CII 面板厚度为 0.005 m (c) CllI 面板厚度为 0.010 m (c) CILI 的流固相互作用 (2) 对于三级压缩坡道CI、CII和CIII，固有频率随着面板厚度的增加而增加；当面板厚度从2毫米增加到30毫米时，实际条件下可用的工作振动频率上限分别从16.8赫兹增加到249赫兹、17.76赫兹增加到259赫兹、17.12赫兹增加到251赫兹。
> 
> (3)考虑面板的流固耦合会导致总压恢复和质量流量系数的降低和波动；进气性能波动范围随着面板厚度的增加和刚度的增大而减小，当流固耦合源从机身前缘转移到进气唇时，进气性能波动范围增大。 (4)随着面板厚度的增加，固有频率增加，而工作频率降低；本工作中研究的 CI、CII 和 CIII（马赫数为 6、高度为 24 km 时具有三级压缩斜坡的二维进气系统）的面板厚度下限可分别视为 5.5、6.0 和 6.5 mm。 (5)对于薄板结构受压系统的设计，必须考虑共振极限。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 6717 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2. The hypersonic vehicle and multi-stage compression system | 对象/条件/子问题展开 | 2552 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 3. Numerical models | 方法建构 | 284 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 3.1.1. Vibration differential equation | 对象/条件/子问题展开 | 379 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 5 | 3.1.2. Meshed models and constraint conditions | 方法建构 | 1810 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.2.1. Governing equations | 对象/条件/子问题展开 | 2034 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.2.2. Computational region, boundary conditions and mesh independence | 对象/条件/子问题展开 | 4248 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.2.3. Validation of the numerical method | 方法建构 | 2339 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.1. Mode analysis | 结果验证/讨论 | 3975 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 10 | 4.2.1. Effects of vibration amplitude | 对象/条件/子问题展开 | 4166 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2.2. Effects of vibration frequency | 对象/条件/子问题展开 | 2569 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.3. Fluid-structural interaction effects | 对象/条件/子问题展开 | 474 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.3.1. Structural vibration of compression ramps | 对象/条件/子问题展开 | 2240 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.3.2. Effects of vibration on the intake performance | 结果验证/讨论 | 1656 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 15 | 4.4. Design path of compression system | 对象/条件/子问题展开 | 3902 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 5. Conclusions | 主张回收/边界说明 | 2490 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：panel(85)；vibration(78)；intake(64)；flow(64)；compression(63)；fig(56)；thickness(51)；respectively(49)；cii(45)；ciii(42)；system(41)；frequency(41)；performance(40)；pressure(39)；work(36)；one(28)；ramps(27)；fluctuation(25)；fluid-structural(24)；recovery(24)
- 高频学术名词/术语：vibration(78)；compression(63)；thickness(51)；performance(40)；pressure(39)；fluctuation(25)；displacement(22)；interaction(19)；stiffness(14)；structure(11)；influence(11)；condition(11)；variation(9)；deformation(9)；section(8)
- 高频学术动词：obtained(22)；indicated(10)；indicate(4)；developed(3)；compared(3)；obtain(2)；evaluated(2)；presented(2)；introduced(1)；validate(1)；reveal(1)
- 高频形容词：fluid-structural(24)；coefficient(24)；total(22)；displacement(22)；hypersonic(21)；structural(21)；natural(16)；available(15)；table(15)；operational(12)；boundary(11)；internal(10)；numerical(10)；external(9)；real(9)
- 高频副词：respectively(49)；finally(7)；closely(2)；widely(2)；relatively(2)；commonly(1)；actually(1)；numerically(1)；uniformly(1)；specifically(1)；obviously(1)；sequentially(1)
- 高频二词短语：panel thickness(43)；cii ciii(39)；intake system(29)；intake performance(24)；compression ramps(23)；total pressure(21)；pressure recovery(19)；mass flow(19)；one find(19)；fluid-structural interaction(16)；flow field(15)；flow coefficient(13)；compression system(12)；flow coefficients(12)；panel thicknesses(12)
- 高频三词短语：total pressure recovery(19)；fig one find(10)；pressure recovery mass(9)；recovery mass flow(9)；mass flow coefficient(9)；pressure recovery coefficient(9)；mass flow coefficients(8)；cii ciii respectively(8)；increase panel thickness(8)；available panel thickness(6)；respectively fig one(6)；cii ciii vibrations(6)
- 被动语态估计：136
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：257
- 一般过去时线索：259
- 现在完成时线索：0
- 情态动词线索：78

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Thus, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance.
  - 可迁移句型：{object}, for the design of a compression system, it is essential to obtain vibration characteristics of compression ramps and clarify their effects on the intake performance.
- 原句：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
  - 可迁移句型：{object}, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
- 原句：Accurate constraint conditions are essential to the structural mode analysis.
  - 可迁移句型：{object} constraint conditions are essential to the structural mode analysis.
- 原句：(5) For the design of thin-panel-structural compression system, the consideration of resonance limit is essential.
  - 可迁移句型：(5) {object} the design of thin-panel-structural compression system, the consideration of resonance limit is essential.
### gap/转折句
- 原句：However, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of air intake system.
  - 可迁移句型：{object}, the thin-panel structure is liable to be excitated by various vibration sources such as hypersonic flow (fluid-structural interaction), engine (thrust variation) and noise, and the induced panel vibration has significant effect on the performance of 
- 原句：However, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
  - 可迁移句型：{object}, in real conditions, the viscous effect will lead to the reduction of intake performance, thus viscosity corrections by corresponding CFD simulations are essential subsequent steps.
- 原句：The vehicle involved in this work has relatively large scale and thus corresponding experiment studies are difficult to carry on.
  - 可迁移句型：{object} vehicle involved in This study has relatively large scale and thus corresponding experiment studies are difficult to carry on.
- 原句：The GK-01 wind-tunnel model of DLR [22,33] is adopted to verify the current method’s The vehicle involved in this work has relatively large scale and thus corresponding experiment studies are difficult to carry on.
  - 可迁移句型：{object} GK-01 wind-tunnel model of DLR [22,33] is adopted to verify the current method’s The vehicle involved in This study has relatively large scale and thus corresponding experiment studies are difficult to carry on.
### 方法提出句
- 原句：Finally, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance.
  - 可迁移句型：{object}, the available physical dimensions of external compression ramps are determined and a design path of intake system is developed by considering both the structural and intake performance.
- 原句：The numerical models for each simulation are introduced below.
  - 可迁移句型：{object} numerical models for each simulation are introduced below.
- 原句：3(a) and (b) show the geometric and meshed models of CI, respectively.
  - 可迁移句型：3(a) and (b) show the geometric and meshed models of {object}, respectively.
- 原句：The meshed model shown in Fig.
  - 可迁移句型：{object} meshed model shown in Fig.
### 结果证明句
- 原句：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
  - 可迁移句型：{object} “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
- 原句：3(a) and (b) show the geometric and meshed models of CI, respectively.
  - 可迁移句型：3(a) and (b) show the geometric and meshed models of {object}, respectively.
- 原句：3(a), the six boundary planes are indicated by $P _ {x 0} , \ P _ {x 1} , \ P _ {y 0} , \ P _ {y 1} , \ P _ {z 0} ,$ and $P _ {z 1}$ .
  - 可迁移句型：3(a), the six boundary planes are indicated by ${object} _ {x 0} , \ P _ {x 1} , \ P _ {y 0} , \ P _ {y 1} , \ P _ {z 0} ,$ and $P _ {z 1}$ .
- 原句：Such rivets are indicated by the red points in Fig.
  - 可迁移句型：{object} rivets are indicated by the red points in Fig.
### 贡献收束句
- 原句：The additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency.
  - 可迁移句型：{object} additional compression and turning processes in such three-dimensional intake system contribute to the improvement of compression efficiency.
- 原句：It shows that the CoB condition indicates noteworthy stiffness improvement.
  - 可迁移句型：{object} shows that the CoB condition indicates noteworthy stiffness improvement.
### 边界/谨慎句
- 原句：The design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
  - 可迁移句型：{object} design of such type of intake system should contain the determination of configurational parameters and physical dimensions by considering both flow and structural vibrations, and a clear design path is still absent.
- 原句：A compression system, take the multi-stage planar one for instance, is formed by several compression ramps, which commonly adopt thin-panel structures in consideration of the low-weight requirement.
  - 可迁移句型：{object} compression system, take the multi-stage planar one for instance, is formed by several compression ramps, which commonly adopt thin-panel structures in consideration of the low-weight requirement.
- 原句：The “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
  - 可迁移句型：{object} “shock-on-lip” criterion means all the shock waves are converged to the cowl lip with no spillage and indicates the maximum mass flow coefficient (should be 100%), while the Oswatitsch criterion indicates the maximum total pressure recovery [15].
- 原句：A great number of researches about complex fluid-structural phenomena, e.g., turbulent boundary layers [16,17], aeroelastic effects [18,19], dynamic aeroelastic effects [20,21], aerothermoelastic effects [22,23], shock-wave-boundarylayer In this work, three types of numerical simulations should be conducted: the mode analysis of compression ramps, the flow field analysis with vibrational structural boundaries, and the fluidstructural interaction analysis.
  - 可迁移句型：{object} great number of researches about complex fluid-structural phenomena, e.g., turbulent boundary layers [16,17], aeroelastic effects [18,19], dynamic aeroelastic effects [20,21], aerothermoelastic effects [22,23], shock-wave-boundarylayer In This study, 

## 9. 引用风险层

- 正文引用簇估计：36
- 参考文献条数：35
- 可识别年份条目数：37
- 2021 年及以后参考文献数：18
- 2010 年以前经典文献数：8
- 高频来源粗略识别：Sci. Technol(5)；Propuls. Power(4)；Fluids(2)；Aerosp. Eng(2)；Aerosp. Sci(1)；Platzer(1)；Aircr(1)；Fluid Mech(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] F-Y. Zuo, S. Mölder, Hypersonic wavecatcher intakes and variable-geometry tur- bine based combined cycle engines, Prog. Aerosp. Sci. 106 (2019) 108–144.
- [2] S. Luo, Y. Sun, J. Liu, J. Song, W. Cao, Performance analysis of the hypersonic vehicle with dorsal and ventral intake, Aerosp. Sci. Technol. 131 (2022) 107964.
- [3] O. Musa, G. Huang, Z. Yu, Assessment of new pressure-corrected design method for hypersonic internal waverider intake, Acta Astronaut. 201 (2022) 230–246.
- [4] E.T. Curran, Scramjet engines: the first forty years, J. Propuls. Power 17 (6) (2001) 1138–1148.
- [5] C.J. Trefny, J.M. Roche, Performance Validation Approach for the GTX Air- Breathing Launch Vehicle, NASA/TM–2002-211495, 2002.
- [6] U.B. Mehta, M.J. Aftosmis, J.V. Bowles, S.A. Pandya, Skylon aerodynamics and SABRE plumes, in: 20th AIAA International Space Planes and Hypersonic Sys- tems and Technologies Conference, American Institute of Aeronautics and As- tronautics, 2015.
- [7] J.A. Medina, H. Patel, B. Chudoba, Inlet sizing of hypersonic vehicles for con- ceptual design, in: ASCEND 2021, American Institute of Aeronautics and Astro- nautics, 2021.
- [8] C. Yunseok, M. Yost, E. Lerner, J.F. Driscoll, Model of a JP-7-fueled generic X- 51 vehicle: effects of varying scramjet flowpath, in: AIAA Scitech 2021 Forum, American Institute of Aeronautics and Astronautics, 2021.
- [9] Y. Choi, M.F. Yost, E.W. Lerner, J.F. Driscoll, Scramjet performance computed for a JP-7-fueled generic X-51 vehicle, J. Propuls. Power 38 (3) (2022) 348–358.
- [10] S.N.B. Murthy, E.T. Curran, Strutjet rocket-based combined-cycle engine, in: Scramjet Propulsion, American Institute of Aeronautics and Astronautics, 2001, pp. 697–755.
- [11] W.Y.K. Chan, D.J. Mee, M.K. Smart, J.C. Turner, Drag reduction by boundary- layer combustion: effects of flow disturbances from rectangular-to-elliptical- shape-transition inlets, J. Propuls. Power 31 (5) (2015) 1256–1267.
- [12] N.O.P. Raj, K. Venkatasubbaiah, A new approach for the design of hypersonic scramjet inlets, Phys. Fluids 24 (8) (2012) 086103.
- [13] P.P.B. Araújo, M.V.S. Pereira, G.S. Marinho, J.F.A. Martos, P.G.P. Toro, Optimiza- tion of scramjet inlet based on temperature and Mach number of supersonic combustion, Aerosp. Sci. Technol. 116 (2021) 106864.
- [14] K. Oswatitsch, Pressure recovery for missiles with reaction propulsion at high supersonic speeds (the efficiency of shock diffusers), in: W. Schnei- der, M. Platzer (Eds.), Contributions to the Development of Gasdynamics: Se- lected Papers, Translated on the Occasion of K. Oswatitsch’s 70th Birthday, Vieweg+Teubner Verlag, Wiesbaden, 1980, pp. 290–323.
- [15] M.K. Smart, Optimization of two-dimensional scramjet inlets, J. Aircr. 36 (2) (1999) 430–433.

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
