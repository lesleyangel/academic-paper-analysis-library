# Adaptive path following control for miniature unmanned aerial vehicle confined to three-dimensional Dubins path: From take-off to landing

## 0. 读取说明

本文拆解依据 `801/文本/txt/Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.txt` 的全文抽取。txt 中符号表、表格和公式有双栏交叉，Table 2/3 的完整内容、Fig. 8-19 曲线细节和控制框图需要 PDF 图像复核。以下以可稳定确认的研究问题、控制结构、仿真/飞行试验结果和结论为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 System model and problem description, 3 Methodology, 4 Performance evaluations and discussions, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Adaptive path following control for miniature unmanned aerial vehicle confined to three-dimensional Dubins path: From take-off to landing
- 作者：Weinan Wu, Jie Xu, Chunlin Gong, Naigang Cui
- 期刊：ISA Transactions, 143, 156-167
- 年份：2023
- 领域：小型固定翼无人机、3D Dubins path、向量场制导、自适应滑模控制、抗风扰路径跟随。
- 论文类型：控制方法论文 + 仿真 + 实飞验证。
- 研究对象：MAV 从起飞到降落全过程跟随 3D Dubins 路径，在模型不确定和风扰条件下保持路径跟踪。
- 方法：多层结构；guidance layer 用改进 VF-based 方法跟踪 straight-line、arc、helical path；control layer 用 adaptive SMC 管理风扰和模型不确定。
- 主要证据：Lyapunov 稳定性证明、仿真 3D Dubins 任务、风扰参数测试、Monte Carlo 算法比较、两架 MAV 实飞对比 ASMC/PID/LQR。
- 目标读者：无人机路径跟随与鲁棒控制研究者、工程飞控应用者、移动机器人 3D 路径规划/控制研究者。

## 2. 摘要与核心信息提取

一句话主张：将 3D Dubins 路径分解为可由向量场制导处理的路径段，并用自适应滑模控制补偿风扰和模型不确定，可让小型固定翼 MAV 从起飞到降落稳定跟随复杂三维任务路径。

摘要抓住两个痛点：MAV 体量小，更易受风扰影响，且精确动力学模型和扰动参数难获得；已有路径跟随研究多看 tracking performance，而较少考虑路径本身在真实任务中的多段特性。本文用 multi-layered structure 同时处理 guidance 和 control，并通过仿真与 in-flight trials 证明适用性。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.md`。

中文译文：

> 本研究提出了一种方法，用于解决在使用具有不确定性的模型和经历外部风扰动时沿着预定的三维（3D）杜宾斯路径控制微型固定翼无人机（MAV）的挑战。我们提供同时结合引导和控制的多层结构。在引导层中，提出了一种改进的基于矢量场的方法，使 MAV 能够遵循 3D Dubins 路径，包括具有三种不同类型航段的起飞、巡航和着陆过程。然后，使用自适应滑模控制器来分析和管理风扰动和系统不确定性。最后，模拟场景和飞行试验都证明了该方法的适用性和所提出方法的效率。研究人员希望改进这一策略，因为它们过去已被用于各种自动驾驶车辆类型 [9-16]。
>
> 目前，一些相关的优秀工作有多种扩展，主要有两种类型：一种侧重于控制机制，旨在管理干扰的影响和系统不准确的模型；另一种侧重于制导技术，旨在更有效地根据任务自适应地跟踪不同类型的参考路径。在控制相关领域，研究人员试图减轻模型不精确和环境干扰的影响。 Han[17]提出了一种基于扩展状态观测器的主动抗扰控制器（ADRC），该控制器被证明适用于各种工程问题。因此，ADRC 成为希望改进这一策略的研究人员的动力。 Mokhtari [18]、Shao [19] 和 Ma [20] 通过用重新设计的线性观测器代替扩展状态观测器来改进 Han 的基于观测器的控制器。随后证实，这款新观察器在同轴旋翼无人机、四旋翼直升机和高超音速再入飞行器中工作得非常成功，但不适用于微型飞行器。 Son [21] 和 Kim [22] 中使用了比例积分观测器，因为它能够消除稳态误差。
>
> 根据他们的发现，提出并实施了一种使用双一阶观测器的实用控制结构，用于稳健的速度控制问题或电力电子应用。其他启发式算法被应用于无人机的跟踪控制
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

问题来源是小型固定翼 MAV 的真实任务需求。MAV 要执行侦察、打击、验证等连续任务，路径不只是平面直线或圆，而包括起飞、巡航、降落、不同高度和 helical segment。与此同时，MAV 对风扰更敏感，模型参数又难精确。

作者把问题定义为：给定 instructive 3D Dubins path，设计 guidance/control，使 MAV 质心收敛到路径参考点且速度方向与路径切向一致，并在风扰和 autopilot 参数不确定下保证跟踪误差收敛。

选题价值主要是工程应用价值。它不只是提出一个控制器，而是把路径规划、三维路径几何、抗扰控制和实飞验证连接起来，强调 “from take-off to landing”。

## 4. 领域位置与文献版图

作者把文献分成两条线。

第一条是 control-related fields：ADRC、extended state observer、PI observer、heuristic algorithms、fuzzy logic、SMC 等，用来处理模型不准和外部扰动。作者指出这些方法在 quadrotor、vessel、常规 UAV 等对象上有效，但对 small-sized MAV 的实际有效性和可行性仍需展示。

第二条是 guidance-related fields：vector-field path following 在机器人/UAV 中应用广泛，但多数集中在 2D 或未充分考虑风扰和模型不确定；3D VF 方法、smooth curve following、Dubins airplane path 相关工作为本文提供基础。

本文的位置在两条线交叉处：用 3D Dubins path 让路径具有任务可解释性，用 VF guidance 适配不同路径段，用 adaptive SMC 处理控制层不确定。

## 5. Gap 制造机制

gap 的制造依赖三点：

- 对象 gap：MAV 比普通 UAV 更容易受扰，已有对 quadrotor/airship/AUV 的结果不能直接迁移。
- 路径 gap：很多研究只重跟踪误差，不考虑路径本身的任务几何和 take-off/landing 过程。
- 扰动 gap：已有 3D Dubins airplane 或 VF 方法往往忽略 wind disturbances 或只处理模型不确定。

作者将 gap 从“控制性能不足”升级为“路径特性与控制鲁棒性未同时考虑”。这点比较有说服力，因为后文确实把 straight-line、arc、helical 三类路径段分开设计 guidance。

## 6. 创新性判断

作者声明的贡献有两项：其一，构建 multi-layered framework，让 VF-based guiding 和 adaptive SMC 分别处理外部路径制导和内部扰动/模型不确定；其二，从路径规划器视角考察 3D Dubins path 对跟踪效果的影响，使方法更工程化。

真实创新属于“控制架构集成 + 工程验证”。VF、SMC、Dubins path 都不是新概念，但将它们用于 MAV 全流程 3D Dubins 路径，并做仿真、Monte Carlo、实飞三重验证，贡献是较强的应用型控制论文。

创新强度为中等偏强。强在实飞对比和完整任务场景，弱在理论层面主要是常规 Lyapunov 稳定性证明，没有提出全新的控制理论。

## 7. 论证链条复原

MAV 任务需要稳定高效 3D 路径跟随 → MAV 小、易受风扰且模型参数不准 → 现有方法要么偏控制抗扰、要么偏路径几何，难覆盖真实 3D Dubins 任务全过程 → 本文建立多层结构 → guidance layer 根据 straight-line、arc、helical path 生成 heading/altitude/speed commands → control layer 用 adaptive SMC 将 guidance commands 转为控制量并补偿 wind/model uncertainty → 用 Lyapunov 证明闭环稳定 → 用仿真验证风扰下可跟踪 → 用 Monte Carlo 与 Carrot、NLGL、PLOS、LQR 比较 → 用两架 MAV 实飞验证 ASMC 优于 PID/LQR → 得出方法适合真实 MAV 任务。

链条完整。薄弱点是理论证明依赖简化 MAV 模型和低层 autopilot 足够快假设，实飞结果证明实用性但没有展开统计显著性。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7]. Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].
- 本文解决方式：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances. In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
- 学术或工程增量：We provide a multilayered structure that incorporates both guiding and control at the same time. In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments. Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法名称：VF-based guidance + adaptive sliding mode control 的多层路径跟随框架。

输入：3D Dubins path、MAV 当前状态、路径参考点、风扰、低层 autopilot 参数估计。输出：heading、altitude、velocity guidance commands，以及 speed/flight-path/bank angle control commands。

Guidance layer：

1. Straight-line following：用起点和方向向量定义直线路径，VF 生成 heading instruction，使 lateral error 收敛。
2. Arc path following：用圆心、半径和旋转方向定义圆弧路径，控制距离和航向。
3. Helical path following：用半径、爬升率、中心点和方向定义螺旋路径，生成水平航向与垂直航迹角。

Control layer：

1. 建立含风扰的 MAV 运动方程，实际速度为机体速度加 wind disturbance。
2. 定义 tracking deviation、sliding mode function `s = dot(xi)+Λxi`。
3. 在已知参数下设计 SMC，并用 Lyapunov 证明全局渐近稳定。
4. 在 autopilot 参数不确定时，引入自适应律估计参数，并再次用 Lyapunov/Barbalat 证明收敛。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 多层结构能把路径几何和控制抗扰解耦 | 方法 3/Fig. 5-6 | guidance layer 输出 `[χ, hd, va]`，control layer 用 ASMC 处理扰动 | 中-强 | 框图细节需 PDF 复核 |
| 闭环系统在风扰下渐近稳定 | Theorem 1 | Lyapunov 函数 `L1=1/2 s^T s`，证明 `dot L1 <= -s^T K s` | 强（理论内） | 依赖扰动导数有界等假设 |
| 模型不确定下自适应 SMC 仍收敛 | Theorem 2 | 引入参数估计与自适应律，证明 `lim s=0` 并得到跟踪误差收敛 | 强（理论内） | 参数可辨识性和噪声影响讨论不足 |
| 仿真中方法可跟踪复杂 3D Dubins 路径 | 结果 4.1/Fig. 8-12 | 风速 7 m/s 时最大跟踪误差约 27 m，10 m/s 时约 35 m | 中-强 | 曲线细节需 PDF 图像复核 |
| 增大 korbit 可降低跟踪误差 | Table 6 | Test 1 从 22 m 降至 9 m；Test 2 从 36 m 降至 10 m | 强 | 作者也指出 korbit 需受阈值限制 |
| VF+ASMC 综合性能优于常见算法 | Monte Carlo/Fig. 14 | 与 Carrot、NLGL、PLOS、LQR 比较，权重范围内总体分数更好 | 中-强 | 性能分数权重 Γ 选择影响结论 |
| 实飞中 ASMC 比 PID/LQR 更准确高效 | Table 7/Fig. 19 | MAV1/2 take-off/cruise/landing 误差多数低于 PID/LQR，转场时间约 3.32/3.9 s | 强 | 实飞样本规模有限，环境条件未充分统计 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 系统模型 | 定义 MAV 运动变量 | 建模基础 | 速度、航向角、航迹角、位置 | 需要 PDF 图像复核 |
| Fig. 2 完整飞行过程 | 强化 from take-off to landing 场景 | 真实任务路径 | 起飞、任务执行、降落 | 需要 PDF 图像复核 |
| Fig. 3/4 3D Dubins 路径和问题示意 | 将路径规划任务可视化 | 路径 gap | 多目标任务与跟踪误差定义 | 需要 PDF 图像复核 |
| Fig. 5/6 多层框架 | 展示方法结构 | guidance/control 解耦 | VF guidance + adaptive SMC | 需要 PDF 图像复核 |
| Eq. (1)-(2) MAV kinematics | 建立控制对象 | 路径跟随模型 | 位置、航向、航迹角变化 | 公式排版需 PDF 复核 |
| Eq. (3)-(7) 路径段制导 | 覆盖直线/圆弧/螺旋路径 | 3D Dubins 适配 | 不同段生成 guidance commands | 公式和表格需 PDF 复核 |
| Eq. (12)-(23) SMC 与自适应律 | 理论稳定性核心 | 抗扰和模型不确定 | sliding surface、controller、adaptive law | 公式需 PDF 复核 |
| Fig. 8-12 仿真轨迹 | 证明复杂任务可跟踪 | 方法有效 | 最大误差 27 m/35 m | 曲线需 PDF 复核 |
| Fig. 14 Monte Carlo 对比 | 综合效率与准确性比较 | VF+ASMC 优势 | 多算法随 Γ 变化评分 | 需要 PDF 图像复核 |
| Table 7 实飞对比 | 工程验证 | ASMC 优于 PID/LQR | 误差和平均转场时间 | 可从 txt 确认 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 System model and problem description；3 Methodology；4 Performance evaluations and discussions；5 Conclusions。

结构很清晰：Introduction 负责双线文献和 gap；Section 2 先定义 MAV 模型和任务路径；Section 3 分 guidance 和 control 两层；Section 4 先仿真后实飞；Section 5 总结并给未来工作。

章节标题大多是功能型标题。Methodology 中 `VF-based path following` 与 `Adaptive sliding mode control` 是并列模块，符合多层结构。Results 中 `Simulation case` 和 `Real flight experiment` 分开，使“理论-仿真-实飞”的证据阶梯明显。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 System model and problem description（方法/模型/算法）
  - L3 p.3: 2.1 System model（方法/模型/算法）
  - L3 p.4: 2.2 Problem description（问题定义）
- L2 p.4: 3 Methodology（方法/模型/算法）
  - L3 p.5: 3.1 VF-based path following（对象/模块/过渡章节）
    - L4 p.5: 3.1.1 Straight-line following（对象/模块/过渡章节）
    - L4 p.5: 3.1.2 Arc paths following（对象/模块/过渡章节）
    - L4 p.5: 3.1.3 Helical paths following（对象/模块/过渡章节）
  - L3 p.7: 3.2 Adaptive sliding mode control（对象/模块/过渡章节）
    - L4 p.7: 3.2.1 SMC of path following under wind disturbance（对象/模块/过渡章节）
    - L4 p.8: 3.2.2 SMC of path following under model uncertainty（方法/模型/算法）
- L2 p.8: 4 Performance evaluations and discussions（结果/验证/讨论）
  - L3 p.8: 4.1 Simulation case（结果/验证/讨论）
  - L3 p.11: 4.2 Real flight experiment（结果/验证/讨论）
- L2 p.11: 5 Conclusions（结论/贡献回收）
- L2 p.12: Declaration of competing interest（尾部材料）
- L2 p.12: Acknowledgment（尾部材料）
- L2 p.12: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 System model and problem description | 3 | 2 | 方法/模型/算法 |
| 2.1 System model | 3 | 3 | 方法/模型/算法 |
| 2.2 Problem description | 4 | 3 | 问题定义 |
| 3 Methodology | 4 | 2 | 方法/模型/算法 |
| 3.1 VF-based path following | 5 | 3 | 对象/模块/过渡章节 |
| 3.1.1 Straight-line following | 5 | 4 | 对象/模块/过渡章节 |
| 3.1.2 Arc paths following | 5 | 4 | 对象/模块/过渡章节 |
| 3.1.3 Helical paths following | 5 | 4 | 对象/模块/过渡章节 |
| 3.2 Adaptive sliding mode control | 7 | 3 | 对象/模块/过渡章节 |
| 3.2.1 SMC of path following under wind disturbance | 7 | 4 | 对象/模块/过渡章节 |
| 3.2.2 SMC of path following under model uncertainty | 8 | 4 | 方法/模型/算法 |
| 4 Performance evaluations and discussions | 8 | 2 | 结果/验证/讨论 |
| 4.1 Simulation case | 8 | 3 | 结果/验证/讨论 |
| 4.2 Real flight experiment | 11 | 3 | 结果/验证/讨论 |
| 5 Conclusions | 11 | 2 | 结论/贡献回收 |
| Declaration of competing interest | 12 | 2 | 尾部材料 |
| Acknowledgment | 12 | 2 | 尾部材料 |
| References | 12 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是：MAV 应用和难点 → 3D path following 研究总览 → 控制抗扰文献 → 制导/VF 文献 → Dubins path 和 take-off/landing gap → 本文贡献。每段既综述又制造缺口。

方法段落节奏是先讲框架，再讲路径段，再讲控制器。三类路径段的写法是“定义路径数学形式 → 说明目标 → 给 guidance equation”。控制部分是“定义不确定 → 设计控制律 → 定理证明”。

结果段落先展示一个复杂任务场景，再做参数影响，再做算法对比，最后实飞。这个顺序从可行性、敏感性、相对优势、真实验证逐步加强说服力。

## 13. 文笔画像与语言习惯

文笔偏控制论文常见风格，术语密集：path-following control, wind disturbances, model uncertainty, vector-field-based, adaptive SMC, asymptotically stable, Lyapunov candidate function。

作者喜欢用 “This study...” 开头总结本文动作；贡献句使用编号；结果解释中常用 “it is evident that”, “demonstrating that”, “Consequently”。语气较强，但通常搭配仿真或实飞数据。

时态方面，文献综述用过去时和现在完成时混合，方法描述用现在时，实验结果用过去时。主动/被动混合，理论证明部分形式化被动较多。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：33460
- 高频词：path(84)；mav(61)；control(47)；helical(31)；model(30)；following(30)；wind(29)；controller(26)；disturbances(23)；adaptive(22)；tracking(22)；angle(21)；method(18)；sliding(18)；dubins(17)；guidance(17)；disturbance(16)；route(16)；system(16)；flight(16)
- 高频名词化/学术名词：guidance(17)；disturbance(16)；section(15)；velocity(14)；performance(8)；reference(8)；position(8)；direction(8)；dynamics(8)；function(8)；location(7)；distance(7)；addition(5)；mechanism(5)；experiment(5)
- 高频学术动词：presented(12)；developed(6)；demonstrated(5)；provide(4)；compared(3)；enable(2)；develop(2)；estimate(2)；derive(2)；validate(2)；evaluate(2)；demonstrate(1)；construct(1)；evaluated(1)；reveal(1)
- 高频形容词：helical(31)；adaptive(22)；actual(11)；nominal(8)；stable(7)；constant(7)；current(6)；instructive(6)；external(5)；dynamic(5)；experiment(5)；aerial(4)；general(4)；integral(4)；logic(4)
- 高频副词：consequently(5)；asymptotically(5)；finally(4)；quently(3)；thoroughly(2)；accurately(2)；evidently(2)；similarly(2)；underly(1)；marily(1)；apply(1)；extensively(1)；currently(1)；primarily(1)；adaptively(1)
- 高频二词短语：helical path(26)；sliding mode(15)；path following(14)；wind disturbance(11)；control law(10)；path-following control(9)；wind disturbances(9)；tracking error(9)；nominal value(8)；autopilot parameters(8)；model uncertainty(8)；adaptive sliding(7)
- 高频三词短语：sliding mode control(7)；mav path following(6)；path following control(6)；mode control law(5)；value autopilot parameters(4)；sliding mode controller(4)；adaptive sliding mode(4)；theorem closed-loop system(4)；miniature fixed-wing unmanned(3)；fixed-wing unmanned aerial(3)；unmanned aerial vehicles(3)；adaptive sliding model(3)
- 被动语态估计：89；`we + 动作动词` 主动句估计：1
- 一般现在时线索：142；一般过去时线索：292；现在完成时线索：1；情态动词线索：30

分章节正文词频：

- 1 Introduction: path(29)；control(19)；disturbances(18)；mav(16)；tracking(13)；helical(13)；model(11)；method(11)
- 2 System model and problem description: mav(10)；model(6)；kinematic(4)；vucos(4)；system(3)；motion(3)；problem(3)；control(3)
- 3 Methodology: path(28)；mav(26)；following(16)；helical(15)；control(14)；value(13)；given(11)；controller(11)
- 4 Performance evaluations and discussions: path(24)；test(9)；case(8)；mav(8)；korbit(8)；flight(7)；wind(7)；control(6)
- 5 Conclusions: control(5)；model(3)；should(3)；dubins(2)；route(2)；wind(2)；adaptive(2)；sliding(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`MAVs have emerged in recent years for a variety of applications.`
- 问题句式：`poses a significant challenge for the control strategy.`
- Gap 句式：`the literature rarely considers the adaptability of the path-following method to the path itself.`
- 贡献句式：`This study provides the following contributions:`
- 框架句式：`a multi-layered framework is developed based on...`
- 稳定性句式：`The closed-loop system ... is asymptotically stable.`
- 结果句式：`the maximum tracking error is ..., which is less than...`
- 局限句式：`It should be noted that the suggested control strategy was developed without considering...`

可复用表达：将路径类型写成 “SL trajectories, CS trajectories, and helical trajectories” 这种枚举，可把复杂任务拆成可控模块。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
  可迁移模板：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (METHOD) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
- 原句：However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
  可迁移模板：However, navigating the MAVs along a predetermined threedimensional (METHOD) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [X–X].
#### Gap/转折句
- 原句：However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
  可迁移模板：However, navigating the MAVs along a predetermined threedimensional (METHOD) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [X–X].
- 原句：Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].
  可迁移模板：Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [X].
- 原句：However, the path of the stratospheric airship was constrained in the 2D plane.
  可迁移模板：However, the path of the stratospheric airship was constrained in the METHOD plane.
- 原句：However, this study did not consider external distur bances and only considered the uncertainty of the dynamic model.
  可迁移模板：However, this study did not consider external distur bances and only considered the uncertainty of the dynamic model.
- 原句：However, when it comes to VF-based literature, most studies focus on 2D settings, while attempting to manage 3D scenarios with wind disturbances and improve the tracking efficiency of VF-based algorithms, the literature rarely considers the adaptability of the path-following method to the path itself, which limits the algorithm to a single scenario.
  可迁移模板：However, when it comes to METHOD-based literature, most studies focus on METHOD settings, while attempting to manage METHOD scenarios with wind disturbances and improve the tracking efficiency of METHOD-based algorithms, the literature rarely considers the adaptability of the path-following method to the path itself, which limits the algorithm to a single scenario.
#### 方法提出句
- 原句：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (3D) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
  可迁移模板：This study proposes a method for resolving the challenge of controlling miniature fixed-wing unmanned aerial vehicles (MAVs) along a predetermined three-dimensional (METHOD) Dubins path while using models with uncertainty and when experiencing external wind disturbances.
- 原句：In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
  可迁移模板：In the guidance layer, a modified vector-field-based approach is presented to enable the METHOD to follow a METHOD Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
- 原句：Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
  可迁移模板：Then, an adaptive sliding model controller is used for the analysis and man agement of both wind disturbances and system uncertainties.
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
  可迁移模板：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [X–X].
- 原句：Currently, there are several extensions in some related outstanding works, which are primarily of two types: one focuses on control mechanism and is designed to manage both the effects of disturbances and the system’s inaccurate model, while the other focuses on guidance technique and is designed to adaptively track different types of reference paths in accordance with missions in a more efficient manner.
  可迁移模板：Currently, there are several extensions in some related outstanding works, which are primarily of two types: one focuses on control mechanism and is designed to manage both the effects of disturbances and the system’s inaccurate model, while the other focuses on guidance technique and is designed to adaptively track different types of reference paths in accordance with missions in a more efficient manner.
#### 结果呈现句
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
  可迁移模板：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [X–X].
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
  可迁移模板：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [X–X].
- 原句：In addition, the applicability and superiority of the presented method are thoroughly demonstrated by presenting both simulation scenarios and a real-world flying experiment.
  可迁移模板：In addition, the applicability and superiority of the presented method are thoroughly demonstrated by presenting both simulation scenarios and a real-world flying experiment.
- 原句：Simulation results demonstrated that the pro posed controller provides effective tracking control.
  可迁移模板：Simulation results demonstrated that the pro posed controller provides effective tracking control.
- 原句：The efficacy and usefulness of this strategy have been demonstrated by a real-world flight test.
  可迁移模板：The efficacy and usefulness of this strategy have been demonstrated by a real-world flight test.
#### 贡献/增量句
- 原句：We provide a multilayered structure that incorporates both guiding and control at the same time.
  可迁移模板：We provide a multilayered structure that incorporates both guiding and control at the same time.
- 原句：In the guidance layer, a modified vector-field-based approach is presented to enable the MAV to follow a 3D Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
  可迁移模板：In the guidance layer, a modified vector-field-based approach is presented to enable the METHOD to follow a METHOD Dubins path, including the takeoff, cruise, and landing processes with three different types of route segments.
- 原句：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [9–16].
  可迁移模板：Finally, both simulated scenarios and in-flight trials demonstrate the applicability of the methodology and the efficiency of the proposed approach. researchers wishing to improve this strategy, as they have been utilized in the past for a variety of autonomous vehicle types [X–X].
- 原句：Thus, ADRC served as motivation for researchers wishing to improve this strategy.
  可迁移模板：Thus, METHOD served as motivation for researchers wishing to improve this strategy.
- 原句：Mokhtari [18], Shao [19], and Ma [20] improved Han’s observer-based controller by substituting the extended state observer with a redesigned linear observer.
  可迁移模板：Mokhtari [X], Shao [X], and Ma [X] improved Han’s observer-based controller by substituting the extended state observer with a redesigned linear observer.
#### 限制/边界句
- 原句：In addition, the available literature addressing the path-following problem focuses pri marily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks.
  可迁移模板：In addition, the available literature addressing the path-following problem focuses pri marily on path-tracking performance rather than the characteristics of the involved path, which may not apply to real-world tasks.
- 原句：However, this study did not consider external distur bances and only considered the uncertainty of the dynamic model.
  可迁移模板：However, this study did not consider external distur bances and only considered the uncertainty of the dynamic model.
- 原句：It should be noted that the suggested control strategy was developed without considering unknown observer factors.
  可迁移模板：It should be noted that the suggested control strategy was developed without considering unknown observer factors.
- 原句：Thus, uncertain observer parameters should be addressed a future work.
  可迁移模板：Thus, uncertain observer parameters should be addressed a future work.
- 原句：Future efforts should incorporate collision avoidance in order to meet the prerequisites for complex tasks involving multiple MAVs.
  可迁移模板：Future efforts should incorporate collision avoidance in order to meet the prerequisites for complex tasks involving multiple MAVs.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是双谱系组织：控制文献和制导文献分开评价。控制文献主要服务于风扰和模型不确定的必要性；制导文献主要服务于 VF 和 3D path 的可行性；Dubins path 文献作为桥梁，把路径规划器和 MAV 任务连接起来。

作者评价前人时常用“有效但不覆盖本文场景”的姿态，例如 quadrotor/AUV/airship 结果有效，但 small-sized MAV、3D Dubins、wind disturbance、take-off/landing 同时出现时仍不足。这种引用策略避免了“所有前人都不行”的夸张。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：57
- Introduction 引文簇数量估计：23
- References 条目数：32
- 可识别年份条目数：40
- 2021 年及以后文献数：5
- 2010 年前经典文献数：9
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：[17], [18], [19], [8], [20], [21], [22], [23], [24], [23], [24], [25]

带引文的 gap/转折句样例：

- However, navigating the MAVs along a predetermined threedimensional (3D) path in the presence of uncertainty in the underly ing modeling parameters and external disturbances poses a significant challenge for the control strategy [5–7].
- Due to their size, however, MAVs are more susceptible to environmental disturbances than typical UAVs, despite the fact that both the precise dynamic model of MAVs and the disturbance parameters are difficult to establish [8].

References 解析样例（前 8 条）：

- [1] Maza I, Caballero F, Capit´an J, et al. Experimental results in multi-UAV coordination for disaster management and civil security applications. J Intell Robot Syst 2011;61(1):563–85.
- [2] Schmale Iii DG, Dingus BR, Reinholtz C. Development and application of an autonomous unmanned aerial vehicle for precise aerobiological sampling above agricultural fields. J. Field Robotics 2008;25(3):133–47.
- [3] Sujit PB, Kingston D, Beard R. Cooperative forest fire monitoring using multiple UAVs. In: 2007 46th IEEE conference on decision and control. IEEE; 2007. p. 4875–80.
- [4] Frew EW, Argrow B. Embedded reasoning for atmospheric science using unmanned aircraft systems. In: 2010 AAAI spring symposium series. 2010.
- [5] Askari A, Mortazavi M, Talebi HA. UAV formation control via the virtual structure approach. J. Aerosp. Eng. 2015;28(1):04014047.
- [6] Su Z, Wang H, Yao P, et al. Back-stepping based anti-disturbance flight controller with preview methodology for autonomous aerial refueling. Aerosp. Sci. Technol. 2017;61:95–108.
- [7] Wu J, Wang H, Li N, et al. Path planning for solar-powered UAV in urban environment. Neurocomputing 2018;275:2055–
- 65.
ISA Transactions 143 (2023) 156–167
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. MAV 动力学模型较简化，低层 autopilot “sufficiently fast” 假设可能掩盖实际执行器动态。
2. Lyapunov 证明依赖扰动导数有界和参数估计结构，实飞噪声下鲁棒性未深入理论化。
3. Monte Carlo 的综合评分由 Γ 加权，权重选择可能影响算法排名。
4. 实飞实验样本量和环境条件描述有限，统计普遍性不足。
5. 3D Dubins path 的生成器本身不是本文重点，路径规划质量对控制结果的影响未充分隔离。
6. collision avoidance 被列为未来工作，多 MAV 复杂任务还不完整。

## 17. 可复用资产

- 选题套路：把“控制器鲁棒性”与“路径几何适配性”同时作为 gap。
- 方法资产：guidance layer/control layer 分层写法，适合任何“路径规划 + 飞控执行”论文。
- 证据资产：理论证明 + 仿真 + Monte Carlo + 实飞，这四层证据非常完整。
- 图表资产：Table 7 用同一飞行阶段比较 ASMC/PID/LQR 的误差和效率，便于审稿人快速判断优势。
- 句式资产：贡献中避免泛泛说 improved performance，而是说明谁处理外部环境、谁处理内部扰动。

## 18. 对我写论文的启发

若写控制/算法应用论文，最好像本文一样把“工程场景完整性”作为卖点：不仅展示巡航段，还覆盖起飞、任务、降落；不仅仿真，还做实飞；不仅单次曲线，还做算法对比。

同时要警惕：方法组合型论文很容易被质疑“只是拼接”。本文通过稳定性证明和实飞验证增强可信度。如果我采用类似结构，应增加模块消融，证明 VF、ASMC、自适应律各自贡献。

## 19. 最终浓缩

本文把小型固定翼 MAV 的 3D Dubins 路径跟随写成“路径几何 + 抗扰控制 + 实飞验证”的完整工程问题。最强证据是 ASMC 在实飞中将误差控制到约 7 m 以下，并比 PID/LQR 有更快转场响应。最可复用的是多层框架和四层证据链；最大风险是模型简化和实飞统计覆盖不足。
