# 论文深度拆解：Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates

> 生成依据：`801/cleantext/018-Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`018-Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.pdf`
- 页数：22
- clean body 字符数：31771
- 摘要字符数：2498
- 参考文献条数：38
- 图题数：0
- 表题数：0
- 表格文件数：8
- 公式候选数：75
- 提取质量分：0.93
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "7 formula(s) need manual review."}]

## 1. 身份层

- 标题：Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates
- 年份：2025
- 期刊/来源：Chinese Journ
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：工程应用 + 多物理场分析型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectil
- 主要证据：图表 0 个标题、公式 75 个候选、参考文献 38 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mech”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards. The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
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
- 作者声明或文本中可见 gap：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed. Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
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
| The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (42.52, 215.95, 330.44, 257.73)]] PII: S1000-9361(25)00594-1 DOI: http | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 11, bbox (119.73, 74.48, 257.0, 84.11)]] f (rad/s) p Point A (Le | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (42.52, 215.95, 330.44, 257.73)]] PII: S1000-9361(25)00594-1 DOI: http | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been de | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 11, bbox (119.73, 74.48, 257.0, 84.11)]] f (rad/s) p Point A (Le | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic char | 摘要/引言/结论候选 | 公式/模型：[confidence=0.92; source=equations; [page 1, bbox (42.52, 215.95, 330.44, 257.73)]] PII: S1000-9361(25)00594-1 DOI: http | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| With the continuous development of computer technology, Computational Fluid Dynamics (CFD) has broad applications in analysis of aeronautics and astronautics.7 Many researches7-11 have explored the aerodynamic characteristics of projectiles with canards. | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 11, bbox (119.73, 74.48, 257.0, 84.11)]] f (rad/s) p Point A (Le | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| 公式：[confidence=0.92; source=equations; [page 1, bbox (42.52, 215.95, 330.44, 257.73)]] PII: S1000-9361(25)00594-1 DOI: https://doi.org/10.1016/ | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 11, bbox (119.73, 74.48, 257.0, 84.11)]] f (rad/s) p Point A (Left) Point B (Right) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 14, bbox (321.32, 695.2, 546.81, 713.96)]]   2 ,  e =   (9) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 15, bbox (393.23, 547.03, 475.33, 556.62)]] f (rad/s) p 600π (free) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 19, bbox (79.1, 74.49, 281.6, 91.91)]] Direction Velocity (m/s) Attitude angular (^{\circ}) Angula | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 21, bbox (73.7, 369.98, 333.28, 406.34)]] 39. Sahu J. Time-accurate numerical predic | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] \mathsf{al.} ^ {29} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=body_inline] \frac {\partial} {\partial t} \iiint _ {\mathcal {Q}} \mathbf {d} \mathcal {Q} + \iint _ {\hat {c} \ma | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> In this paper, a numerical study is conducted on a fixed-canard dual-spin projectile to explore its aerodynamic and angular motion characteristics at different forebody spinning rates. Based on the Reynolds-averaged Navier–Stokes equations, unsteady simulations of the dual-spin projectile rotating around its longitudinal axis are performed to investigate its aerodynamic characteristics. The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards. This discrepancy, in turn, gives rise to an asymmetric wingtip vortex structure, which ultimately exerts significant influence on the aerodynamic characteristics of the dual- spin projectile. Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed. The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile. Among the underlying mechanisms, the projection of the resultant moment onto the projectile axis is identified as the dominant contributing factor. A non-positive projection induces convergence of the complex angle of attack, thereby enhancing stability of the spinning projectile. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
> Keywords: Dual-spin projectile; Unsteady aerodynamic characteristic; Angular motion; Coupled computational fluid dynamics and rigid body dynamics
> *Corresponding author. E-mail address: chunnali@nwpu.edu.cn
> 1. Introduction1
> Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1
> To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed. It utilizes the gyroscopic stability generated by the high-speed spinning of the aft body to maintain flight stability. Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3
> Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics,

### 7.4 摘要中文翻译

> 本文对固定鸭翼双自旋弹丸进行了数值研究，探讨其在不同前体旋转速率下的气动和角运动特性。基于雷诺平均纳维-斯托克斯方程，对双自旋弹丸绕纵轴旋转进行非定常模拟，研究其气动特性。结果表明，前体的旋转导致左右鸭翼的有效迎角存在差异。这种差异反过来又产生了不对称的翼尖涡结构，最终对双自旋弹丸的气动特性产生了重大影响。此外，基于计算流体动力学和刚体动力学耦合方法，研究了双自旋弹丸飞行过程中的气动和角运动特性，并分析了角运动机理。结果表明，前体旋转显着影响弹丸的气动特性和角运动特性。在潜在的机制中，合力在弹丸轴上的投影被认为是主要的影响因素。非正投影会引起复杂攻角的收敛，从而增强旋转射弹的稳定性。基于这些发现，提出了一种控制策略：为了提高角运动稳定性，驱动前体沿相反方向旋转或保持静止状态。关键词：双旋射弹；气动特性非定常；角运动；耦合计算流体动力学和刚体动力学 *通讯作者。
> 
> E-mail 地址：chunnali@nwpu.edu.cn 1. 引言1 自旋稳定弹近年来得到广泛应用，但其攻击精度仍然有限​​。1 为了提高命中精度，开发了一种弹道修正弹的固定鸭翼双自旋弹。它利用尾体高速旋转产生的陀螺稳定性来保持飞行稳定性。另外，它还可以通过控制前鸭翼的旋转来修正弹道，从而提高攻击精度。2,3由于后弹体的高速旋转，双旋弹弹表现出高度非线性和非定常的气动特性，

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this study, we investigate the aerodynamic and angular motion characteristics of a fixed-canard dualspin projectile at various forebody spinning rates through numerical simulations. The unsteady aerodynamic characteristics of the dual-spin projectile spinning around fixed axis are analyzed through unsteady CFD simulations. Further, coupled CFD/RBD simulations are conducted to study the angular motion and aerodynamic characteristics with the forebody respectively spinning at fixed rates and freely. The main conclusions of this work are summarized as follows:
> 
> (1) The forebody spinning influences the lateral aerodynamic characteristics of the dual-spin projectile. An increase in the opposite-direction spinning rate of the forebody leads to a higher lateral force coefficient, while simultaneously reducing the yawing moment coefficient. As the angle of attack increases, the impact of the forebody spinning on the lateral force and yawing moment coefficients becomes more significant.
> 
> (2) When the forebody spins, the effective angle of attack differs between the left and right canards, resulting in stronger vortices on the side with larger effective angle of attack. This results in asymmetry in the wingtip vortex structures, and changes its aerodynamic characteristics.
> 
> (3) The projection of the moment perpendicular to the body axis onto the projectile axis is a key factor influencing its angular motion. When the projection is larger than zero, the amplitude of the angular motion increases gradually.
> 
> (4) When the aft body and forebody of the dual-spin projectile spin in the same direction, the amplitude of angular motion increases, leading to reduced stability. By contrast, employing a control strategy in which the forebody spins in the opposite direction or remains stationary can reduce the projection of the moment onto the projectile’s axis, thereby enhancing the stability of its angular motion.

### 7.6 结论中文翻译

> 在这项研究中，我们通过数值模拟研究了固定鸭翼双旋射弹在不同前体旋转速率下的空气动力和角运动特性。通过非定常CFD仿真分析了双自旋弹丸绕定轴旋转的非定常气动特性。此外，还进行了CFD/RBD耦合仿真，研究了前体分别以固定速率和自由旋转时的角运动和气动特性。本工作的主要结论如下：（1）前体旋转影响双旋弹的横向气动特性。前体反方向旋转速率的增加导致侧向力系数更高，同时降低了偏航力矩系数。随着迎角增大，前体旋转对侧向力和偏航力矩系数的影响变得更加显着。 (2)前体旋转时，左右鸭翼的有效迎角不同，导致有效迎角较大一侧涡流较强。这导致翼尖涡结构不对称，并改变其空气动力特性。 (3)垂直于体轴的力矩在弹体轴上的投影是影响其角运动的关键因素。当投影大于零时，角运动的幅度逐渐增大。 (4)双自旋弹丸的后体和前体同向旋转时，角运动幅度增大，稳定性降低。
> 
> 相比之下，采用前体向相反方向旋转或保持静止的控制策略可以减少投射到弹丸轴上的力矩，从而增强其角运动的稳定性。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction1 | 问题引入/文献定位 | 6856 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. CFD method | 方法建构 | 1955 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. RBD method | 方法建构 | 2486 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. Coupled CFD/RBD method | 方法建构 | 788 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3. Computational model | 方法建构 | 560 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Computational grid | 对象/条件/子问题展开 | 945 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 7 | 4. Results and discussion | 结果验证/讨论 | 6537 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 8 | 4.2. Aerodynamic and angular motion characteristics analysis in flight | 结果验证/讨论 | 9404 | 该节承担“结果验证/讨论”功能，服务于从问题到证据的推进。 |
| 9 | 5. Conclusions | 主张回收/边界说明 | 1928 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |

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

- 高频词：mathrm(68)；forebody(65)；spinning(60)；projectile(59)；angle(52)；aerodynamic(45)；angular(41)；motion(39)；attack(38)；fig(38)；flight(36)；moment(34)；dual-spin(28)；characteristics(28)；coefficient(25)；rates(24)；body(23)；lateral(22)；cfd(22)；cdot(22)
- 高频学术名词/术语：motion(39)；moment(34)；characteristics(28)；direction(21)；stability(14)；velocity(13)；simulation(10)；pressure(10)；projection(8)；influence(6)；equation(6)；interference(5)；dynamics(4)；configuration(4)；reference(4)
- 高频学术动词：presented(9)；compared(6)；investigate(6)；predicted(3)；developed(2)；obtained(1)；indicate(1)
- 高频形容词：aerodynamic(45)；moment(34)；coefficient(25)；lateral(22)；negative(12)；numerical(9)；longitudinal(9)；table(7)；significant(6)；stationary(6)；positive(6)；dynamic(5)；computational(5)；total(5)；effective(5)
- 高频副词：respectively(6)；gradually(6)；conversely(4)；significantly(4)；additionally(2)；highly(2)；similarly(2)；simultaneously(2)；accurately(2)；freely(2)；widely(1)；excessively(1)
- 高频二词短语：forebody spinning(38)；angular motion(33)；angle attack(31)；dual-spin projectile(27)；spinning rates(23)；aft body(20)；mathrm cdot(19)；aerodynamic characteristics(18)；spinning rate(18)；complex angle(16)；cfd rbd(15)；mathrm mathrm(15)；coupled cfd(14)；flight states(13)；yawing moment(11)
- 高频三词短语：forebody spinning rates(21)；complex angle attack(16)；coupled cfd rbd(13)；forebody spinning rate(11)；flight states moments(11)；angular motion characteristics(8)；aerodynamic angular motion(7)；yawing moment coefficient(7)；lateral flight states(7)；mathrm cdot vardelta(7)；characteristics dual-spin projectile(6)；mathrm mathrm mathrm(6)
- 被动语态估计：51
- `we + 动作动词` 主动句估计：0
- 一般现在时线索：110
- 一般过去时线索：155
- 现在完成时线索：1
- 情态动词线索：14

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 原句：Conversely, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-depth investigation of the aerodynamic and angular motion characteristics of the dual-spin projectile is necessary.
  - 可迁移句型：{object}, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-dept
- 原句：The time-averaged aerodynamic coefficient is calculated by $$C _ {\mathrm{ave}} = \frac {\displaystyle \int _ {t} ^ {t + T} C ( t ) \mathrm{d} t} {T}\tag{4}$$ (a) Lift coefficient (c) Lateral force coefficient where T is the period of coefficient change; t represents time; C denotes the aerodynamic coefficient.
  - 可迁移句型：{object} time-averaged aerodynamic coefficient is calculated by $$C _ {\mathrm{ave}} = \frac {\displaystyle \int _ {t} ^ {t + T} C ( t ) \mathrm{d} t} {T}\tag{4}$$ (a) Lift coefficient (c) Lateral force coefficient where T is the period of coefficient change; 
### gap/转折句
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  - 可迁移句型：{object} on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句：Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：Introduction1 {object} projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed
- 原句：Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：{object}, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characte
- 原句：However, the flow mechanisms generating yawing moment and lateral force, which can lead to flight instability, remain not fully understood.
  - 可迁移句型：{object}, the flow mechanisms generating yawing moment and lateral force, which can lead to flight instability, remain not fully understood.
### 方法提出句
- 原句：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed.
  - 可迁移句型：{object}, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed.
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  - 可迁移句型：{object} on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句：Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：Introduction1 {object} projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed
- 原句：Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：{object}, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characte
### 结果证明句
- 原句：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
  - 可迁移句型：{object} results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
- 原句：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
  - 可迁移句型：{object} results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
- 原句：Liu et al.14 used the sliding mesh approach to study the influence of the spinning rate of the aft body, angle of attack, and Mach number, on the time-averaged aerodynamic characteristics of a dual-spin projectile through numerical simulation, revealing the underlying flow mechanisms.
  - 可迁移句型：{object} et al.14 used the sliding mesh approach to study the influence of the spinning rate of the aft body, angle of attack, and Mach number, on the time-averaged aerodynamic characteristics of a dual-spin projectile through numerical simulation, revealing t
- 原句：Yin et al.15 compared the aerodynamic coefficients of spinning projectiles using the unsteady Reynolds-Average Navier-Stokes (RANS) equation with the aerodynamic coefficients obtained from theoretical formulations, finding significant differences at high spinning rates, which indicates that the theoretical formulation method has limitations in calculating aerodynamic characteristics.
  - 可迁移句型：{object} et al.15 compared the aerodynamic coefficients of spinning projectiles using the unsteady Reynolds-Average Navier-Stokes (RANS) equation with the aerodynamic coefficients obtained from theoretical formulations, finding significant differences at high 
### 贡献收束句
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  - 可迁移句型：{object} on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句：Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：Introduction1 {object} projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed
- 原句：Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：{object}, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characte
- 原句：Conversely, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-depth investigation of the aerodynamic and angular motion characteristics of the dual-spin projectile is necessary.
  - 可迁移句型：{object}, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-dept
### 边界/谨慎句
- 原句：Introduction1 Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：Introduction1 {object} projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed
- 原句：Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, Spin-stabilized projectiles have been widely deployed in recent years, but their attack precision remains limited.1 To enhance hit accuracy, the fixed-canard dual-spin projectile, designed as a type of trajectory-corrected projectile, has been developed.
  - 可迁移句型：{object}, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characte
- 原句：Additionally, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characteristics, along with strong couplings between the motion of the lateral and normal axes.2,4 The projectile’s flight involves coupled angular motions—spin, precession, and nutation— resulting in highly complex dynamic behavior.5 When the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising flight stability.
  - 可迁移句型：{object}, it can correct the trajectory by controlling the rotation of the front canard, thereby improving attack precision.2,3 Due to the high-speed rotation of the aft body, the dual-spin projectile exhibits highly nonlinear and unsteady aerodynamic characte
- 原句：Conversely, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-depth investigation of the aerodynamic and angular motion characteristics of the dual-spin projectile is necessary.
  - 可迁移句型：{object}, when the spinning rate is too high, it may reduce trajectory-following stability, causing the projectile to experience an excessively large angle of attack during flight, which negatively affects the stability of its angular motion.6 Thus, an in-dept

## 9. 引用风险层

- 正文引用簇估计：0
- 参考文献条数：38
- 可识别年份条目数：44
- 2021 年及以后参考文献数：27
- 2010 年以前经典文献数：2
- 高频来源粗略识别：Chin J Aeronaut(5)；Aerosp Sci Technol(4)；AIAA SCITECH(3)；Proceedings of the(2)；J Spacecr Rockets(2)；Proc Inst Mech Eng Part G J Aerosp Eng(2)；Phys Fluids(2)；Def Technol(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- 1. Wang Y, Yu JY, Wang XM, et al. A guidance and control design with reduced information for a dual-spin stabilized projectile. Def Technol 2024;33:494–505.
- 3. Karimi J, Rajabi MR, Sadati SH, et al. Multidisciplinary design optimization of a dual-spin guided vehicle. Def Technol 2024;37:133–48.
- 4. Yin JT, Jiang SJ, Hu YW, et al. Aerodynamic characteristics and dynamic stability of coning motion of spinning finned projectile in supersonic conditions. Aerospace 2025;12(3):225.
- 5. Zhu Z, Shi L, He C, et al. Construction and kinematic performance analysis of a suspension support for wind tunnel tests of spinning projectiles based on wire-driven parallel robot with kinematic redundancy. Chin J Aeronaut 2024;37(12):404–15.
- 6. Wang G, Zhang RT, Lin HZ, et al. Study on influence of canard rotation speed on following stability of dual-spin projectile. Aero Weapon 2024;31(2):71–8 [Chinese].
- 7. Chen SS, Cai FJ, Xiang XH, et al. A low-diffusion robust flux splitting scheme towards wide-ranging Mach number flows. Chin J Aeronaut 2021;34(5):628–41.
- 8. Askary F, Soltani MR. Effects of Mach numbers on Magnus induced surface pressure. Chin J Aeronaut 2020;33(12):3058–72.
- 9. Zhao XX, Shi JG, Wang ZY, et al. Nonlinear aerodynamic modeling and analysis on body of fixed canard dual-spin projectiles. Proceedings of the 2nd international conference on mechanical system dynamics. Singapore: Springer Nature Singapore, 2024:3759–74.
- 10. Shen Q, Qiu LL, Pu WY, et al. Aerodynamic characteristics and characterization of the double spin structure of two-dimensional correction high-spin projectile. Trans Beijing Inst Technol 2024;44(4):359–68 [Chinese].
- 11. Pokela R, Kumar R, Vasile JD, et al. Aerodynamic characterization of a generic high-speed projectile configuration. J Spacecr Rockets 2024;61(3):741–56.
- 12. Li JM, He GL, Guo HY. A study on the aerodynamic characteristics for a two-dimensional trajectory correction fuze. Appl Mech Mater 2014;703:370–5.
- 13. Jaiswal R, Kothari M, Abhishek A. Design and aerodynamic characterization of canard guided fuze for dual-spin artillery projectiles. AIAA SCITECH 2024 forum. Reston: AIAA; 2024.
- 14. Liu XD, Wu XS, Yin JT. Aerodynamic characteristics of a dual-spin projectile with canards. Proc Inst Mech Eng Part G J Aerosp Eng 2019;233(12):4541–53.
- 15. Yin JT, Lei JM, Wu XS, et al. Aerodynamic characteristics of a spinning projectile with elastic deformation. Aerosp Sci Technol 2016;51:181–91.
- 16. Ji W, Gong CL, Jia XY, et al. Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning. Aerosp Sci Technol 2024;155:109711.

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
