# Adaptive path following control for miniature unmanned aerial vehicle confined to three-dimensional Dubins path: From take-off to landing

## 0. 读取说明

本文拆解依据 `801/文本/txt/Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.txt` 的全文抽取。txt 中符号表、表格和公式有双栏交叉，Table 2/3 的完整内容、Fig. 8-19 曲线细节和控制框图需要 PDF 图像复核。以下以可稳定确认的研究问题、控制结构、仿真/飞行试验结果和结论为主。

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

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 结论/展望型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2.2 Problem description | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.2 Arc paths following | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Adaptive sliding mode control | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 The multiple 3D Dubins paths consist of a helical ascending path, three | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Real flight experiment | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是：MAV 应用和难点 → 3D path following 研究总览 → 控制抗扰文献 → 制导/VF 文献 → Dubins path 和 take-off/landing gap → 本文贡献。每段既综述又制造缺口。

方法段落节奏是先讲框架，再讲路径段，再讲控制器。三类路径段的写法是“定义路径数学形式 → 说明目标 → 给 guidance equation”。控制部分是“定义不确定 → 设计控制律 → 定理证明”。

结果段落先展示一个复杂任务场景，再做参数影响，再做算法对比，最后实飞。这个顺序从可行性、敏感性、相对优势、真实验证逐步加强说服力。

## 13. 文笔画像与语言习惯

文笔偏控制论文常见风格，术语密集：path-following control, wind disturbances, model uncertainty, vector-field-based, adaptive SMC, asymptotically stable, Lyapunov candidate function。

作者喜欢用 “This study...” 开头总结本文动作；贡献句使用编号；结果解释中常用 “it is evident that”, “demonstrating that”, “Consequently”。语气较强，但通常搭配仿真或实飞数据。

时态方面，文献综述用过去时和现在完成时混合，方法描述用现在时，实验结果用过去时。主动/被动混合，理论证明部分形式化被动较多。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：path(117)；mav(77)；control(76)；following(47)；helical(34)；controller(32)；wind(31)；model(31)；tracking(29)；disturbances(26)；guidance(25)；adaptive(24)；dubins(24)；angle(24)；method(23)；error(23)；flight(23)；system(21)；sliding(20)；path-following(20)
- 高频学术名词：model(31)；guidance(25)；method(23)；system(21)；disturbance(20)；parameters(18)；section(16)；velocity(15)；mechanism(12)；experiment(12)；performance(11)；results(10)；position(10)；analysis(8)；equation(8)；structure(8)
- 高频学术动词：proposed(15)；shown(8)；developed(7)；compared(5)；demonstrated(5)；simulated(3)；validate(3)；derive(2)；evaluate(2)；develop(2)；estimate(2)；reveal(1)；evaluated(1)；indicates(1)；demonstrate(1)；investigated(1)
- 高频形容词：helical(34)；adaptive(24)；stable(16)；aerial(11)；actual(11)；dynamic(10)；robust(8)；effective(8)；nominal(8)；integral(7)；constant(7)；significant(6)；autonomous(6)；current(6)；experiment(6)；instructive(6)
- 高频副词/连接副词：respectively(14)；consequently(12)；therefore(9)；however(8)；finally(5)；asymptotically(5)；significantly(4)；quently(3)；globally(2)；approximately(2)；primarily(2)；accurately(2)；thoroughly(2)；evidently(2)；similarly(2)；furthermore(1)
- 高频二词短语：helical path(28)；path following(21)；sliding mode(15)；isa transactions(13)；path-following control(13)；tracking error(13)；wind disturbance(11)；dubins path(10)；control law(9)；following control(8)；unmanned aerial(8)；take-off landing(8)；wind disturbances(8)；ieee trans(8)；mode control(7)；actual value(7)
- 高频三词短语：sliding mode control(7)；path following control(6)；unmanned aerial vehicle(4)；fixed-wing unmanned aerial(4)；mav path following(4)；integral tracking error(4)；adaptive sliding mode(4)；korbit korbit korbit(4)；three-dimensional dubins path(3)；unmanned aerial vehicles(3)；actual value autopilot(3)；value autopilot parameters(3)

**主动、被动与句法**

- 被动语态估计次数：108
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：611
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：162
- 一般过去时线索：34
- 现在完成时线索：7
- 情态动词线索：36
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：path(32)；control(23)；mav(22)；disturbances(19)；model(17)；angle(15)；tracking(13)；helical(13)
- 2.2. Problem description：path(35)；mav(25)；helical(17)；following(15)；guidance(10)；layer(9)；angle(9)；point(8)
- 3.2. Adaptive sliding mode control：path(33)；mav(20)；wind(15)；control(14)；disturbance(12)；following(12)；test(12)；korbit(12)
- 4.2. Real flight experiment：control(32)；path(17)；ieee(16)；controller(12)；trans(11)；following(10)；mav(10)；flight(7)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

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

## 15. 引用策略与文献使用

引用策略是双谱系组织：控制文献和制导文献分开评价。控制文献主要服务于风扰和模型不确定的必要性；制导文献主要服务于 VF 和 3D path 的可行性；Dubins path 文献作为桥梁，把路径规划器和 MAV 任务连接起来。

作者评价前人时常用“有效但不覆盖本文场景”的姿态，例如 quadrotor/AUV/airship 结果有效，但 small-sized MAV、3D Dubins、wind disturbance、take-off/landing 同时出现时仍不足。这种引用策略避免了“所有前人都不行”的夸张。

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
