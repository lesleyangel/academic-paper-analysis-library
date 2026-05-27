# 论文深度拆解：Adaptive path following control for miniature unmanned aerial vehicle confined to three-dimensional Dubins path: From take-off to landing

> 生成依据：`801/cleantext/017-Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`017-Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.pdf`
- 页数：12
- clean body 字符数：42347
- 摘要字符数：869
- 参考文献条数：31
- 图题数：19
- 表题数：3
- 表格文件数：6
- 公式候选数：203
- 提取质量分：0.96
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "34 formula(s) need manual review."}]

## 1. 身份层

- 标题：Adaptive path following control for miniature unmanned aerial vehicle confined to three-dimensional Dubins path: From take-off to landing
- 年份：2023
- 期刊/来源：ISA Tra
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7
- 主要方法：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
- 主要证据：图表 22 个标题、公式 203 个候选、参考文献 31 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins pat”，可以通过“This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty an”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. In general, methods in the current vector-field methodology serve as sources of motivation for researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7]. However, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.
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
- 作者声明或文本中可见 gap：However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7]. Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8]. In addition, the available literature addressing the path-following problem focuses primarily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
- Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
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
| This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind distur | 摘要/引言/结论候选 | 图：Fig. 1. The system model. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. | 摘要/引言/结论候选 | 图：Fig. 3. The planar projection of the involved trajectories generated by a 3D Dubins-based path planner. . (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. | 摘要/引言/结论候选 | 图：Fig. 4. Sketch map of the problem. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| In general, methods in the current vector-field methodology serve as sources of motivation for researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16]. | 摘要/引言/结论候选 | 表：Table 5 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Han [17] presented a controller for the active rejection of disturbances (ADRC) based on the extended state observer, which was proved to be applicable to various engineering problems. | 摘要/引言/结论候选 | 表：Table 6 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Thus, ADRC served as motivation for researchers wishing to improve this strategy. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.35, 690.38)]] * Corresponding author | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The system model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. The planar projection of the involved trajectories generated by a 3D Dubins-based path planner. . (For interpretation of the references to color in this | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 4. Sketch map of the problem. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 2. The complete flight process of MAV. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 5. The multi-layer framework. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. Flow diagram of the VF-based guidance layer and adaptive SMC control layer. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 7. Description of helical path. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 9. Results of the helical ascending path segment. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 10. Results of the cruising path segment at an altitude of 1500 m. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. Multiple 3D Dubins paths by the path planner. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. Results of the cruising path segment at altitudes 1500 m to 40 m. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 12. Results of the cruising path segment at an altitude of 400 m and attack path segment. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. P.C./104 computer. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The comparison result. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 15. The involved MAV in the experiment. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 5 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 6 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 7 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (42.63, 669.07, 214.35, 690.38)]] * Corresponding author. E-mail address: wu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (37.59, 695.66, 346.85, 716.91)]] https://doi.org/10.1016/j.isatra.2023.09.0 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (306.6, 81.95, 354.86, 100.81)]] ε = {xg, yg, zg | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 2, bbox (317.93, 410.86, 333.84, 419.39)]] = (τ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (314.99, 229.35, 562.35, 257.43)]] ˙x = Vucosγcosψ ˙y = Vucosγsinψ ˙z = -Vusinγ (1) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (45.98, 54.68, 100.24, 83.5)]] ˙x = Vucosγccosψ ˙y = Vucosγcsinψ ˙z = -Vusinγc | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (45.98, 83.25, 95.23, 93.02)]] ˙ψ = gtanϕc/Vu | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 4, bbox (37.59, 554.71, 163.35, 573.52)]] error is represented as ε = {xg, yg, zg | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. We provide a multilayered structure that incorporates both guiding and control at the same time. In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties. Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach.

### 7.4 摘要中文翻译

> 本研究提出了一种方法，用于解决在使用具有不确定性的模型和经历外部风扰动时沿着预定的三维（3D）杜宾斯路径控制微型固定翼无人机（MAV）的挑战。我们提供同时结合引导和控制的多层结构。在引导层中，提出了一种改进的基于矢量场的方法，使 MAV 能够遵循 3D Dubins 路径，包括具有三种不同类型航段的起飞、巡航和着陆过程。然后，使用自适应滑模控制器来分析和管理风扰动和系统不确定性。最后，模拟场景和飞行试验都证明了该方法的适用性和所提出方法的效率。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> This study investigated the path-following control issue for a MAV constrained to a 3D Dubins route with wind disturbance and model uncertainty. This was accomplished by introducing an adaptive sliding model control technique based on a vector-field. The technique was characterized by the incorporation of a multilayered structure to handle the guidance and control levels. In comparison to the previous vectorfield-based guiding legislation, the incorporation of the 3D Dubins route makes it more applicable to real-world situations. Furthermore, both wind disturbances and system uncertainties were explicitly analyzed and managed through the implementation of an adaptive sliding model controller. Simulation results demonstrated that the proposed controller provides effective tracking control. The efficacy and usefulness of this strategy have been demonstrated by a real-world flight test.
> 
> It should be noted that the suggested control strategy was developed without considering unknown observer factors. Thus, uncertain observer parameters should be addressed a future work. Future efforts should incorporate collision avoidance in order to meet the prerequisites for complex tasks involving multiple MAVs.

### 7.6 结论中文翻译

> 本研究研究了受风扰动和模型不确定性限制的 3D Dubins 路线的 MAV 的路径跟踪控制问题。这是通过引入基于矢量场的自适应滑动模型控制技术来实现的。该技术的特点是采用多层结构来处理引导和控制级别。与之前基于矢量场的指导立法相比，3D Dubins 路线的纳入使其更适用于现实世界的情况。此外，通过实施自适应滑动模型控制器，对风扰动和系统不确定性进行了明确的分析和管理。仿真结果表明，所提出的控制器提供了有效的跟踪控制。该策略的有效性和实用性已通过实际飞行测试得到证明。应该指出的是，所建议的控制策略是在没有考虑未知观察者因素的情况下制定的。因此，不确定的观察者参数应该在未来的工作中解决。未来的工作应该包括避免碰撞，以满足涉及多个微型飞行器的复杂任务的先决条件。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9453 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. System model | 方法建构 | 2147 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Problem description | 对象/条件/子问题展开 | 2984 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 3. Methodology | 方法建构 | 1309 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. VF-based path following | 对象/条件/子问题展开 | 581 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 6 | 3.1.1. Straight-line following | 对象/条件/子问题展开 | 837 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 3.1.2. Arc paths following | 对象/条件/子问题展开 | 869 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 8 | 3.1.3. Helical paths following | 对象/条件/子问题展开 | 3240 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 9 | 3.2. Adaptive sliding mode control | 对象/条件/子问题展开 | 1695 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 3.2.1. SMC of path following under wind disturbance | 对象/条件/子问题展开 | 5261 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 3.2.2. SMC of path following under model uncertainty | 方法建构 | 4253 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 12 | 4. Performance evaluations and discussions | 结果验证/讨论 | 558 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 13 | 4.1. Simulation case | 对象/条件/子问题展开 | 3974 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.2. Real flight experiment | 实验或测量设定 | 3400 | 该节承担“实验或测量设定”功能，服务于从问题到证据的推进。 |
| 15 | 5. Conclusions | 主张回收/边界说明 | 1215 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：pmb(110)；path(81)；mav(59)；dot(57)；control(50)；gamma(39)；following(37)；theta(36)；controller(30)；array(30)；psi(27)；tag(27)；wind(25)；infty(24)；disturbances(23)；adaptive(22)；helical(21)；left(21)；right(21)；omega(21)
- 高频学术名词/术语：guidance(17)；section(16)；disturbance(15)；performance(11)；dynamics(8)；velocity(8)；function(8)；mechanism(7)；addition(5)；location(5)；position(5)；direction(5)；experiment(5)；presence(4)；literature(4)
- 高频学术动词：presented(11)；developed(7)；demonstrated(5)；compared(5)；obtained(3)；validate(3)；develop(2)；estimate(2)；derive(2)；evaluate(2)；introduced(1)；demonstrate(1)；construct(1)；evaluated(1)；reveal(1)
- 高频形容词：adaptive(22)；helical(21)；table(11)；actual(10)；stable(8)；nominal(7)；cal(7)；instructive(6)；effective(5)；dynamic(5)；general(5)；experiment(5)；instructional(5)；external(4)；environmental(4)
- 高频副词：respectively(14)；consequently(9)；asymptotically(5)；finally(4)；primarily(3)；thoroughly(2)；accurately(2)；significantly(2)；evidently(2)；similarly(2)；apply(1)；extensively(1)
- 高频二词短语：pmb pmb(29)；pmb theta(19)；path following(16)；helical path(16)；sliding mode(15)；begin array(15)；gamma psi(15)；end array(15)；dot pmb(15)；path-following control(11)；pmb omega(11)；control law(10)；wind disturbance(10)；dot dot(10)；pmb eta(10)
- 高频三词短语：left begin array(9)；end array right(9)；sliding mode control(8)；array right tag(8)；pmb pmb pmb(8)；widetilde pmb theta(8)；mav path following(6)；path following control(6)；begin array dot(6)；pmb eta pmb(6)；dot pmb omega(6)；gamma psi gamma(6)
- 被动语态估计：97
- `we + 动作动词` 主动句估计：1
- 一般现在时线索：161
- 一般过去时线索：322
- 现在完成时线索：1
- 情态动词线索：34

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Table 6 displays the findings regarding the effects of $k _ {o r b i t}$ on the following error.
  - 可迁移句型：{object} 6 displays the findings regarding the effects of $k _ {o r b i t}$ on the following error.
- 原句：However, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.
  - 可迁移句型：{object}, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.
### gap/转折句
- 原句：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
  - 可迁移句型：{object} study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind di
- 原句：However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
  - 可迁移句型：{object}, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underlying modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
- 原句：Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].
  - 可迁移句型：{object} to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].
- 原句：Therefore, the MAV’s kinematic model is as follows: $$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma ^ {c} c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma ^ {c} s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma ^ {c}} \\ {\dot {\psi} = g t a n \phi ^ {c} / V _ {u}} \end{array} \right.\tag{2}$$ However, the attainable bank and flight-path angles should be limited within thresholds $\overline {{\phi}}$ and $\bar {\gamma}$ due to the physical abilities of the MAV.
  - 可迁移句型：{object}, the MAV’s kinematic model is as follows: $$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma ^ {c} c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma ^ {c} s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma ^ {c}} \\ {\dot {\psi} = g t a n \phi
### 方法提出句
- 原句：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
  - 可迁移句型：{object} study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind di
- 原句：In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
  - 可迁移句型：{object} the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
- 原句：Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
  - 可迁移句型：{object}, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach.
  - 可迁移句型：{object}, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach.
### 结果证明句
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach.
  - 可迁移句型：{object}, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach.
- 原句：The actual path with wind disturbance and the instructional path are shown in Figs.
  - 可迁移句型：{object} actual path with wind disturbance and the instructional path are shown in Figs.
- 原句：Table 6 indicates that as $k _ {o r b i t}$ increases, the tracking error of tests 1 and 2 decreases steadily.
  - 可迁移句型：{object} 6 indicates that as $k _ {o r b i t}$ increases, the tracking error of tests 1 and 2 decreases steadily.
- 原句：Simulation results demonstrated that the proposed controller provides effective tracking control.
  - 可迁移句型：{object} results demonstrated that the proposed controller provides effective tracking control.
### 贡献收束句
- 原句：We provide a multilayered structure that incorporates both guiding and control at the same time.
  - 可迁移句型：{object} provide a multilayered structure that incorporates both guiding and control at the same time.
- 原句：In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
  - 可迁移句型：{object} the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
- 原句：In general, methods in the current vector-field methodology serve as sources of motivation for researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
  - 可迁移句型：{object} general, methods in the current vector-field methodology serve as sources of motivation for researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
- 原句：Thus, ADRC served as motivation for researchers wishing to improve this strategy.
  - 可迁移句型：{object}, ADRC served as motivation for researchers wishing to improve this strategy.
### 边界/谨慎句
- 原句：In addition, the available literature addressing the path-following problem focuses primarily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks.
  - 可迁移句型：{object} addition, the available literature addressing the path-following problem focuses primarily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks.
- 原句：1 illustrates a fixed-wing MAV flying with velocity $V _ {u} ,$ angle of heading $\psi ,$ and angle of flight-path $\gamma$ Defining the inertial location of MAV as $[ x ( k ) , y ( k ) , z ( k ) ] ^ {T}$ , the bank angle as $\phi ,$ and the kinematics can be calculated as: $$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma} \end{array} \right.\tag{1}$$ where $V _ {u}$ is the magnitude of $V _ {u}$ Similar to the coordinated turn requirement stated in [30], the connection between ψ and ϕ may be signified as $\dot {\psi} = g t a n \phi / V _ {u}$ With the assumption of the engaged MAV’s dynamics being sufficiently fast, γ and ϕ are respectively restricted to the command angle $\gamma ^ {c}$ and $\phi ^ {c}$ by a low-level autopilot embedded in the control layer.
  - 可迁移句型：1 illustrates a fixed-wing {object} flying with velocity $V _ {u} ,$ angle of heading $\psi ,$ and angle of flight-path $\gamma$ Defining the inertial location of MAV as $[ x ( k ) , y ( k ) , z ( k ) ] ^ {T}$ , the bank angle as $\phi ,$ and the kinematics ca
- 原句：Therefore, the MAV’s kinematic model is as follows: $$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma ^ {c} c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma ^ {c} s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma ^ {c}} \\ {\dot {\psi} = g t a n \phi ^ {c} / V _ {u}} \end{array} \right.\tag{2}$$ However, the attainable bank and flight-path angles should be limited within thresholds $\overline {{\phi}}$ and $\bar {\gamma}$ due to the physical abilities of the MAV.
  - 可迁移句型：{object}, the MAV’s kinematic model is as follows: $$\left\{\begin{array} {l l} {\dot {x} = V _ {u} c o s \gamma ^ {c} c o s \psi} \\ {\dot {y} = V _ {u} c o s \gamma ^ {c} s i n \psi} \\ {\dot {z} = - V _ {u} s i n \gamma ^ {c}} \\ {\dot {\psi} = g t a n \phi
- 原句：However, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.
  - 可迁移句型：{object}, it is essential to note that $k _ {o r b i t}$ should be constrained to a threshold level.

## 9. 引用风险层

- 正文引用簇估计：26
- 参考文献条数：31
- 可识别年份条目数：39
- 2021 年及以后参考文献数：4
- 2010 年以前经典文献数：9
- 高频来源粗略识别：Aerosp. Sci. Technol(2)；IEEE Trans. Control Syst. Technol(2)；IEEE Trans. Ind. Electron(2)；ISA Trans(2)；J Intell Robot Syst(1)；J. Field Robotics(1)；UAV formation control via the virtual structure approach. J. Aerosp. Eng(1)；Path planning for solar-powered UAV in urban environment. Neurocomputing(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- [1] Maza I, Caballero F, Capit´an J, et al. Experimental results in multi-UAV coordination for disaster management and civil security applications. J Intell Robot Syst 2011;61(1):563–85.
- [2] Schmale Iii DG, Dingus BR, Reinholtz C. Development and application of an autonomous unmanned aerial vehicle for precise aerobiological sampling above agricultural fields. J. Field Robotics 2008;25(3):133–47.
- [3] Sujit PB, Kingston D, Beard R. Cooperative forest fire monitoring using multiple UAVs. In: 2007 46th IEEE conference on decision and control. IEEE; 2007. p. 4875–80.
- [4] Frew EW, Argrow B. Embedded reasoning for atmospheric science using unmanned aircraft systems. In: 2010 AAAI spring symposium series. 2010.
- [5] Askari A, Mortazavi M, Talebi HA. UAV formation control via the virtual structure approach. J. Aerosp. Eng. 2015;28(1):04014047.
- [6] Su Z, Wang H, Yao P, et al. Back-stepping based anti-disturbance flight controller with preview methodology for autonomous aerial refueling. Aerosp. Sci. Technol. 2017;61:95–108.
- [7] Wu J, Wang H, Li N, et al. Path planning for solar-powered UAV in urban environment. Neurocomputing 2018;275:2055–65.
- [8] Muniraj D, Palframan MC, Guthrie KT, et al. Path-following control of small fixed- wing unmanned aircraft systems with H∞ type performance. Control Eng. Pract. 2017;67:76–91.
- [9] Goncalves VM, Pimenta LCA, Maia CA, et al. Vector fields for robot navigation along time-varying curves in n-dimensions. IEEE Trans. Robot. 2010;26(4):647–59.
- [10] Zhu M, Tian Y, Chen T, et al. Spacial vector field path following for a stratospheric airship. In: 2016 35th Chinese control conference (CCC). IEEE; 2016. p. 10801–6.
- [11] Kapitanyuk YA, Proskurnikov AV, Cao M. A guiding vector-field algorithm for path-following control of nonholonomic mobile robots. IEEE Trans. Control Syst. Technol. 2017;26(4):1372–85.
- [12] Beard RW, Ferrin J, Humpherys J. Fixed wing UAV path following in wind with input constraints. IEEE Trans. Control Syst. Technol. 2014;22(6):2103–17.
- [13] Chitsaz H, LaValle SM. Time-optimal paths for a dubins airplane. In: 2007 46th IEEE conference on decision and control. IEEE; 2007. p. 2379–84.
- [14] Fari S, Wang X, Roy S, et al. Addressing unmodeled path-following dynamics via adaptive vector field: a UAV test case. IEEE Trans. Aerosp. Electron. Syst. 2019;56 (2):1613–22.
- [15] Rezende AMC, Gonçalves VM, Raffo GV, et al. Robust fixed-wing UAV guidance with circulating artificial vector fields. In: 2018 IEEE/RSJ international conference on intelligent robots and systems (IROS). IEEE; 2018. p. 5892–9.

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
