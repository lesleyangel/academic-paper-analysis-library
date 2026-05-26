# hp-Adaptive RPD based sequential convex programming for reentry trajectory optimization

## 0. 读取说明

本拆解基于 `801/文本/txt/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.txt` 的全文抽取。文本中公式、算法、表格和图题完整度较高；图中曲线形态与颜色区域仅根据正文描述分析，细节标注“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：hp-Adaptive RPD based sequential convex programming for reentry trajectory optimization。
- 作者：Tengfei Zhang、Hua Su、Chunlin Gong。
- 期刊：Aerospace Science and Technology，130，2022，107887。
- 领域：再入轨迹优化、序列凸规划、伪谱离散、最优控制。
- 论文类型：算法改进 + 典型再入算例验证。
- 研究对象：CAV-H 高超声速飞行器最大纵程再入轨迹优化。
- 主要方法：SCP + lossless convexification + hp-adaptive Legendre-Gauss-Radau/Radau pseudospectral discretization + 三阶段迭代。
- 核心贡献：用 hp 自适应 RPD 同时控制离散点数量和位置；用 constraint relaxation 稳住初期迭代；用 regularization 加速末期收敛。
- 对比方法：SCP with uniform discretization、SCP with hp RPD、GPOPS-II。

## 2. 摘要与核心信息提取

一句话主张：已有 SCP 再入轨迹优化方法的瓶颈不只在凸化，还在离散和迭代策略；将 hp-adaptive RPD 嵌入 SCP，并把迭代分成接近、网格更新、收敛三阶段，可以在保持精度的同时显著降低计算时间。

摘要压缩了完整贡献链：问题是 existing SCP 由于 oversimplified discretization and iteration 仍可提升；方法是 hp-adaptive RPD；机制是根据离散误差和状态曲率更新点数与位置；稳定性来自第一阶段约束松弛；收敛来自末阶段正则化；证据是典型再入算例中 CPU 时间比其他 SCP 方法少 40%-70%，约为 GPOPS-II 的 1/20。

## 3. 选题层深拆

选题来自工程实时性与精度的矛盾。再入参考轨迹需要快速、稳定、准确生成，尤其在 onboard optimal guidance 与地面轨迹优化边界变模糊的背景下，算法性能本身成为研究对象。

作者把问题从“求解再入轨迹”转为“如何让 SCP 在直接法框架下更有效”。这个切入很细：SCP 的核心通常被写成 convexification，但作者指出直接法还有同样关键的 discretization error；如果离散不合理，线性化迭代再好也会被低精度网格拖累。

选题价值包括：工程价值，减少 CPU 时间；方法价值，把自适应伪谱离散和 SCP 迭代阶段化结合；写作价值，把算法改进拆成三个可验证子贡献。

## 4. 领域位置与文献版图

文献版图先从 trajectory optimization 的 direct/indirect methods 展开，再转到 SCP 在 UAV、航天器、发射、再入中的应用，随后强调 lossless convexification 解决非凸控制约束，但“求解性能趋势”已经从能否求解转向稳定性、效率和精度。

本文位于 SCP 再入轨迹优化文献之后，同时借用 hp-adaptive pseudospectral 方法的离散优势。它与 GPOPS-II 不是同一类算法：GPOPS-II 是成熟的非线性规划伪谱工具，本文是序列凸规划路线下的自适应离散与迭代框架。

## 5. Gap 制造机制

Gap 的核心句是：现有 SCP 方法中 accuracy 由 linearization error 和 discretization error 共同决定，但常规方法通常只强调线性化迭代，对离散点位置、点数和迭代阶段处理较粗。这个 gap 很具体，后文也能一一对应。

作者将 gap 拆成三个子 gap：初始猜测远离真实轨迹时，严格微分约束会导致子问题不可行；中期固定网格或均匀网格无法把计算资源集中在轨迹变化剧烈处；末期相邻子问题差别很小，固定线搜索下容易振荡、收敛慢。

这种 gap 制造方式很强，因为每个不足都对应一个算法模块：relaxation、hp update、regularization。

## 6. 创新性判断

真实创新是“算法流程级整合”，不是单一数学工具发明。lossless convexification、Radau pseudospectral、hp-adaptive mesh、regularization 都有前史；本文的新意在于把它们放进 SCP 三阶段迭代，并用 differential error 和 state curvature 驱动网格更新。

创新强度中等偏强，优势在工程算法可用性。最强证据是与 UD、hp RPD、GPOPS-II 的 CPU/精度表格比较；最弱点是理论收敛性仍有限，结论也承认正则项没有改变线性收敛性质。

## 7. 论证链条复原

1. 再入轨迹优化需要高稳定性、高效率、高精度。
2. SCP 可把非凸问题转成一系列凸子问题，适合工程快速求解。
3. 原问题中控制归一化约束和运动方程非凸；控制约束可 lossless relaxation，运动方程可线性化。
4. 连续最优控制问题还必须离散，离散误差会显著影响精度和效率。
5. hp-adaptive RPD 可根据局部误差和曲率自适应布点，避免一开始就用大规模子问题。
6. 迭代初期用约束松弛保证可行，中期更新网格降低微分误差，末期固定网格用正则项抑制振荡。
7. CAV-H 算例显示轨迹积分误差小、控制松弛 lossless、初值不敏感。
8. 与 UD、hp RPD、GPOPS-II 对比显示 CPU 时间显著下降，精度可比。
9. 因此本文主张：SCP 性能提升必须同时处理凸化、离散和迭代。

## 8. 方法/理论/模型细拆

问题建模以负能量 E 为自变量，三自由度无动力再入方程省去速度状态，状态为径向距离、经度、纬度、航迹角、航向角。攻角剖面预先给定，主控制是倾侧角 sigma；通过 u1=cos sigma、u2=sin sigma 将非线性控制项转为线性输入，同时引入归一化约束 ||u||^2=1。

凸化分两步。运动方程在当前参考轨迹处 Taylor 线性化为 x'=Ax+Bu+c。控制归一化约束放松为 ||u||^2<=1，并通过最大值原理证明在最优解中仍满足等号，因此是 lossless convexification。

离散使用 hp-adaptive Radau pseudospectral discretization。能量区间分段，每段设置 LGR 点和终点，用 Lagrange 插值近似状态，导数由微分矩阵表达。离散后构成稀疏线性等式 F X = M[X,U]+O，配合状态边界、路径约束、信赖域和二阶锥控制约束形成凸子问题。

自适应机制用两个指标：differential error R 衡量插值导数和动力学导数差异；worst state curvature K 衡量局部状态曲率。若曲率分布均匀则增加该段多项式阶数 p；若不均匀则按曲率概率分布切分 h 段。

三阶段迭代是论文方法中心：approach stage 用粗网格和微分约束松弛逼近真实轨迹；hp update stage 更新离散点降低微分误差；convergence stage 不再更新网格，加入 Pe||X-Xref||^2 正则项加速收敛并抑制振荡。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 控制归一化约束可 lossless convexification | 3.1 | Hamiltonian、KKT/互补松弛、反证推导到 ||u||=1 | 中强 | 证明依赖特定再入问题结构 |
| hp-adaptive RPD 能用更少点获得高精度轨迹 | 5.1/5.3 | proposed method 403 点，误差与 dense UD/RPD、GPOPS-II 可比 | 强 | 仅 CAV-H 单一典型算例 |
| 三阶段迭代能从简单初值稳定逼近 | 5.2 | Fig. 7 轨迹更新，7+5+7 次迭代形成 approach/update/convergence | 强 | 曲线细节需 PDF 图像复核 |
| 正则化可抑制末期振荡并加快残差下降 | 5.2/5.3 | Fig. 8/11 残差历史，convergence stage 残差快速下降 | 中强 | 正则参数 Pe 选取敏感性未系统展开 |
| 算法对初值不敏感 | 5.2 | 1000 次 Monte Carlo 初值，迭代 16-22，CPU 1.68-3.461 s，结果标准差小 | 强 | 初值分布范围由作者设定 |
| 相比其他 SCP 方法 CPU 时间减少 40%-70% | 摘要/5.3 | Table 4：2.377 s vs UD800 8.071 s、RPD150 6.277 s | 强 | MATLAB/MOSEK/硬件条件影响绝对时间 |
| 相比 GPOPS-II 约为 1/20 时间 | 摘要/5.3 | Table 4：2.377 s vs 41.056 s | 强 | GPOPS-II 设置公平性需复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 定义坐标和状态变量 | 问题建模 | 再入状态符号清晰化 | 需要 PDF 图像复核 |
| Eq. 1-17 | 原始最优控制问题 | 研究对象可数学化 | 负能量自变量、路径约束、目标经度 | 文本可确认 |
| Eq. 18-26 | 凸化与 lossless 证明 | 非凸约束可转成凸约束 | 控制约束放松仍等号成立 | 文本可确认 |
| Fig. 2-3 | RPD 分段和微分矩阵稀疏性 | hp RPD 高效性 | 分段矩阵稀疏利于优化 | 需要 PDF 图像复核 |
| Eq. 39-46 | 微分误差、曲率和网格更新 | 自适应布点 | 按误差增阶或按曲率分段 | 文本可确认 |
| Algorithm 1-2 | 算法流程 | 方法可复现 | hp update 与 SCP 迭代过程明确 | 文本可确认 |
| Fig. 4-6 | 轨迹、地面航迹、倾侧角和控制误差 | 算法可行和 lossless | 轨迹与积分高度重合，控制误差多小于 1e-7 | 需要 PDF 图像复核 |
| Fig. 7-9 | 迭代过程、残差、点数和 CPU | 三阶段策略有效 | 点数逐步增加，末期残差下降 | 需要 PDF 图像复核 |
| Table 4/Fig. 10-11 | 方法对比 | 速度和精度优势 | 2.377 s，误差接近 dense/GPOPS-II | 文本可确认，曲线需复核 |

## 11. 章节结构与篇章布局

章节顺序是：Introduction -> Problem formulation -> Convexification and discretization -> Iterative algorithm -> Numerical simulations and discussion -> Conclusions。结构是算法论文标准范式：先给原问题，再给转化，再给算法，再给数值验证。

Introduction 先把轨迹优化放进 guidance/control 背景，再缩小到 SCP，最后指出 discretization and iteration 可改进。Section 2 让读者知道原问题是什么；Section 3 负责数学可解性；Section 4 负责算法可执行性；Section 5 负责工程性能。

标题命名高度功能化，如 “Choice of control variable”、“Differential error and state curvature”、“Comparison with other algorithms”。这类标题适合算法论文，读者能迅速定位推导组件。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Problem formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Motion equations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Choice of control variable | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Optimal control problem | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Discretization and approximation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Convex optimization subproblem | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Iterative algorithm | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Differential error and state curvature | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.3 Iteration process | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Numerical simulations and discussion | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1 Solve by the proposed algorithm | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.2 Convergence analysis of the proposed algorithm | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.3 Comparison with other algorithms | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

方法段落通常先说“为什么需要这个步骤”，再写公式，最后解释变量含义。例如引入 u1/u2 前先说明 sigma 使方程高度非线性；引入正则项前先说明末期子问题相近、解会波动。

结果段落的节奏是“图表观察 -> 定量误差 -> 算法机制解释”。例如 Fig. 7 不只是展示轨迹更新，而是被解释为三阶段功能分工；Fig. 9 不只是展示 CPU，而是支撑“子问题规模逐步增加”的设计合理性。

## 13. 文笔画像与语言习惯

文风直接、工程算法导向。高频词围绕 trajectory optimization、SCP、discretization、iteration、differential error、curvature、constraint relaxation、regularization、CPU time、accuracy。

作者常用 “it is necessary to”、“it can be seen”、“the main purpose of this stage is” 这类教学式句式。强 claim 多由表格支撑，语气比材料/流体机理论文更确定。

时态上，问题和算法用一般现在时；数值结果用一般过去时或现在时读图；结论用现在时总结。被动语态较多，如 “is transformed”、“is adopted”、“is solved by”。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：error(52)；iteration(49)；points(48)；optimization(44)；stage(41)；state(40)；trajectory(38)；discretized(38)；scp(37)；rpd(35)；discretization(35)；algorithm(35)；proposed(29)；differential(29)；number(28)；time(28)；control(27)；problem(27)；cos(25)；initial(24)
- 高频学术名词：iteration(49)；optimization(44)；discretization(35)；solution(22)；convergence(20)；method(18)；segment(18)；science(16)；relaxation(15)；reference(15)；results(12)；equation(12)；regularization(12)；energy(11)；parameters(10)；simulation(10)
- 高频学术动词：proposed(29)；shown(17)；solve(8)；shows(6)；compared(5)；solved(4)；evaluate(3)；indicates(2)；show(1)；evaluated(1)；demonstrate(1)；validated(1)；indicate(1)；capture(1)；developed(1)
- 高频形容词：differential(29)；initial(24)；segment(18)；optimal(16)；hp-adaptive(15)；relative(15)；terminal(15)；pseudospectral(11)；cient(10)；variable(10)；small(8)；numerical(8)；polynomial(8)；residual(8)；different(8)；dimensionless(7)
- 高频副词/连接副词：respectively(13)；gradually(10)；however(7)；generally(4)；directly(4)；therefore(3)；especially(3)；relatively(2)；nally(2)；partially(2)；rapidly(2)；slowly(2)；basically(2)；slightly(2)；cantly(2)；adaptively(1)
- 高频二词短语：discretized points(35)；cpu time(22)；proposed algorithm(20)；differential error(19)；trajectory optimization(18)；aerospace science(16)；science technology(16)；number discretized(15)；zhang gong(14)；gong aerospace(14)；cos cos(14)；hp-adaptive rpd(12)；scp methods(11)；iteration process(11)；xref xref(11)；convexi cation(10)
- 高频三词短语：aerospace science technology(16)；number discretized points(15)；zhang gong aerospace(14)；gong aerospace science(14)；trajectory optimization problem(7)；cos cos cos(7)；xref xref xref(7)；deg deg deg(7)；reentry trajectory optimization(6)；radau pseudospectral discretization(6)；sin cos cos(6)；cos cos sin(6)

**主动、被动与句法**

- 被动语态估计次数：160
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：555
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：304
- 一般过去时线索：32
- 现在完成时线索：9
- 情态动词线索：48
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：reentry(4)；scp(4)；aerospace(3)；sequential(3)；convex(3)；programming(3)；trajectory(3)；optimization(3)
- 1. Introduction：trajectory(15)；error(15)；methods(14)；discretization(14)；optimization(13)；scp(10)；control(8)；discretized(8)
- 2. Problem formulation：optimization(2)；constraints(2)；control(2)；variables(2)；section(1)；formulation(1)；original(1)；reentry(1)
- 2.1. Motion equations：cos(17)；sin(10)；angle(5)；energy(4)；coe(4)；reentry(3)；velocity(3)；system(3)
- 2.2. Choice of control variable：cos(8)；sin(4)；dimensionless(3)；form(3)；control(2)；follows(2)；although(1)；pro(1)
- 2.3. Optimal control problem：xref(16)；constraint(7)；constraints(5)；expressed(5)；optimization(5)；convexi(5)；cation(5)；according(5)
- 3.2. Discretization and approximation：points(6)；state(4)；segment(4)；polynomial(4)；discretized(4)；variables(3)；problem(3)；denoted(3)
- 3.3. Convex optimization subproblem：state(6)；matrix(5)；optimization(5)；terminal(4)；discretized(4)；points(4)；differentiation(4)；constraint(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- Gap 句式：Due to the oversimplified discretization and iteration, the accuracy and efficiency ... can be further improved.
- 方法句式：The iteration process is divided into three stages depending on the characteristics of subproblems.
- 机制句式：The scale of the subproblem gradually increases, thus improving the solving efficiency on the whole.
- 结果句式：With comparable or even higher accuracy, the CPU time reduced by...
- 边界句式：Although X is added..., its linear convergence property is not changed.
- 算法解释句：The main purpose of this stage is to...

可复用术语：lossless convexification、trust region constraint、differential error、state curvature、hp-adaptive RPD、approach stage、convergence stage、regularization term。

## 15. 引用策略与文献使用

引用从 broad trajectory optimization 逐渐收束到 SCP 和 lossless convexification，再到 hp pseudospectral/GPOPS-II。作者引用主要服务三件事：证明再入轨迹优化重要；证明 SCP 已被广泛用于航天工程；证明 hp pseudospectral 离散有成熟基础。

文献评价比较温和，使用 “have been developed”、“have been applied”、“can be further improved” 而非直接批判。这样写法适合算法改进论文，因为贡献是增量优化，不宜夸成完全替代。

## 16. 审稿人视角风险

1. 单一 CAV-H 算例不足以覆盖不同再入约束、目标函数和飞行器模型。
2. CPU 时间依赖 MATLAB、MOSEK、GPOPS-II 设置和硬件；公平性需要明确配置。
3. hp update 参数如 epsilon、zeta、pmin、Nmax、kappa 对性能影响未系统敏感性分析。
4. 正则化项 Pe 的选择可能影响终端经度损失和收敛速度。
5. 方法更偏离线优化，是否能满足 onboard 实时闭环约束还需更多实验。
6. lossless convexification 证明针对当前控制变量和目标，推广到复杂目标/约束未必直接成立。
7. GPOPS-II 的精度和网格设置可能有调参空间，不能简单用默认或单一设置下结论概括。

## 17. 可复用资产

- Gap 拆分资产：把“算法性能差”拆成初期可行性、中期离散误差、末期振荡三个可处理问题。
- 方法命名资产：approach stage / hp update stage / convergence stage，直接把算法流程变成贡献点。
- 证据链资产：先证明轨迹可行，再证明迭代过程，再证明初值鲁棒，最后与算法库对比。
- 表格资产：Table 4 同时列点数、迭代、CPU、终端经度和各状态误差，是算法比较的高密度证据表。
- 写作资产：承认正则项没有改变线性收敛性质，避免对理论贡献过度包装。

## 18. 对我写论文的启发

如果要写算法改进，不要只给“总算法更快”的结果，而要把算法分解成若干阶段，每一阶段对应一个痛点和一个图表证据。本文最值得学的是三阶段迭代的叙事：初期解决可行性，中期解决离散精度，末期解决收敛速度。

另一个启发是比较对象要有层次：简单基线、同类强基线、成熟工具都要有。这样读者能知道提升来自哪里，也能判断方法位置。

## 19. 最终浓缩

这篇论文把 SCP 再入轨迹优化的贡献从“凸化”扩展到“离散 + 迭代”。它提出 hp-adaptive RPD-SCP 三阶段算法，用约束松弛稳住初期、自适应网格降低离散误差、正则化加速末期收敛。最强证据是 CAV-H 中 2.377 s 的求解时间和与 dense/GPOPS-II 接近的精度；主要复核点是多算例泛化、参数敏感性和对比设置公平性。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.txt` 与 `801/文本/metadata/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 Problem formulation （方法/模型）
  - L3 p.2: 2.1 Motion equations （对象/问题/模块）
  - L3 p.3: 2.2 Choice of control variable （对象/问题/模块）
  - L3 p.4: 2.3 Optimal control problem （对象/问题/模块）
- L2 p.4: 3 Convexification and discretization （对象/问题/模块）
  - L3 p.4: 3.1 Convexification （对象/问题/模块）
  - L3 p.5: 3.2 Discretization and approximation （对象/问题/模块）
  - L3 p.6: 3.3 Convex optimization subproblem （对象/问题/模块）
- L2 p.7: 4 Iterative algorithm （对象/问题/模块）
  - L3 p.7: 4.1 Differential error and state curvature （对象/问题/模块）
  - L3 p.8: 4.2 hp-Adaptive RPD （对象/问题/模块）
  - L3 p.8: 4.3 Iteration process （对象/问题/模块）
- L2 p.10: 5 Numerical simulations and discussion （结果/讨论/验证）
  - L3 p.10: 5.1 Solve by the proposed algorithm （对象/问题/模块）
  - L3 p.11: 5.2 Convergence analysis of the proposed algorithm （对象/问题/模块）
  - L3 p.13: 5.3 Comparison with other algorithms （对象/问题/模块）
- L2 p.15: 6 Conclusions （结论）
- L2 p.15: Declaration of competing interest （对象/问题/模块）
- L2 p.15: Data availability （对象/问题/模块）
- L2 p.15: Acknowledgements （对象/问题/模块）
- L2 p.15: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Problem formulation | 2 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Motion equations | 2 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Choice of control variable | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Optimal control problem | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Convexification and discretization | 4 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Convexification | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Discretization and approximation | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Convex optimization subproblem | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Iterative algorithm | 7 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Differential error and state curvature | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 hp-Adaptive RPD | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 Iteration process | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Numerical simulations and discussion | 10 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.1 Solve by the proposed algorithm | 10 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2 Convergence analysis of the proposed algorithm | 11 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3 Comparison with other algorithms | 13 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6 Conclusions | 15 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 15 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 15 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 15 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 15 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 文章历史： 接收日期 2022年8月7日 收到修订版 2022年9月12日 接受日期 2022年9月18日 在线发布 2022年9月23日 詹兴群传播
> 
> 顺序凸规划（SCP）方法已被开发来解决再入轨迹优化问题。由于过于简化的离散化和迭代，现有SCP方法的准确性和效率可以进一步提高。本文提出了一种基于hpadaptive Radau伪谱离散化(RPD)的SCP算法。在该算法中，根据子问题的特点将迭代过程分为三个阶段。第一阶段应用约束松弛技术以确保迭代稳定。在第二阶段，离散点的数量和位置将根据离散化误差和状态曲率自适应更新。在最后阶段，通过多次迭代来减少线性化误差而不更新网格，并利用正则化技术来提高该过程的收敛速度。通过一个典型的重入示例对所提出的算法进行了验证和检验。在结果精度相当甚至更高的情况下，与其他 SCP 方法相比，CPU 时间减少了 40%-70%，仅为 GPOPS-II 的二十分之一。 © 2022 Elsevier Masson SAS。
> 
> 版权所有。

### 20.5 结论完整摘录（本地证据）

结论章节识别：6 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 6. 结论
> 
> 基于SCP的轨迹优化在航空航天领域得到广泛应用。 SCP的核心是凸化技术，
> 特别是关于非凸控制约束的无损凸化技术。不过由于SCP属于直接法
> 从本质上来说，离散化也是影响求解精度和效率的关键因素。主要贡献为
> 本文在离散化和迭代方面改进了现有的SCP方法，提出了hp自适应RPD的SCP。 hp自适应RPD的应用使得迭代过程中子问题的规模逐渐增大，从而提高了
> 整体解决效率。更重要的是，可以用更少的资源获得尽可能高精度的最优轨迹。
> 通过合理的网格更新离散化点。此外，还使用了约束松弛和正则化技术
> 分别在迭代开始和结束时，使所提出的算法对初始值不敏感，并在
> 结束。与其他方法相比，本文提出的算法具有很强的竞争力。虽然本文在优化目标中加入了正则化项来提高迭代的收敛速度
> 过程中，其线性收敛特性没有改变。
> 
> 此外，还使用了约束松弛和正则化技术
> 分别在迭代开始和结束时，使所提出的算法对初始值不敏感，并在
> 结束。与其他方法相比，本文提出的算法具有很强的竞争力。虽然本文在优化目标中加入了正则化项来提高迭代的收敛速度
> 过程中，其线性收敛特性没有改变。在未来的工作中，我们希望利用非线性函数的 Hessian 矩阵作为
> 正则化项的权重，这可能会进一步提高算法的性能。

### 20.7 论文逻辑脉络复核

- 提出的问题：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6]. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the eﬃciency. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating.
- 旧方法/已有研究不足：However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the eﬃciency. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating.
- 本文解决方式：Article history: Received 7 August 2022 Received in revised form 12 September 2022 Accepted 18 September 2022 Available online 23 September 2022 Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems. Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In this paper, a SCP algorithm based on the hpadaptive Radau pseudospectral discretization (RPD) is proposed.
- 学术/工程增量：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved. In the last stage, the linearization error is reduced by several iterations without updating mesh, and the regularization technique is utilized to improve the convergence rate of this process. Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：61
- Introduction 引用簇数量（估计）：9
- References 条目数（解析）：39
- 可识别年份条目数：55
- 近五年/近年文献（2021+）数量：8
- 经典文献（2010年前）数量：9
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Aerospace Science and Technology(1)
- 引用簇样例：[1], [2,3], [7], [14], [15], [16], [17], [18,19], [20,21], [17], [22], [28]

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- 11. Maximum residual history in different algorithms.
Trajectory optimization based on SCP is widely used in the aerospace community. The core of SCP is the convexification technology, especially the lossless convexification technology about non-convex control constraints. However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the efficiency. The main contribution of this paper is to improve the existing SCP method in terms of discretization and iteration, and the SCP with hp-adaptive RPD is proposed. The application of hp-adaptive RPD makes the scale of the subproblem in the iteration process gradually increase, thus improving the solving efficiency on the whole. More importantly, the optimal trajectory with as high precision as possible can be obtained with fewer discretized points through reasonable mesh updating. In addition, constraint relaxation and regularization techniques are used at the beginning and end of iteration, respectively, to make the proposed algorithm insensitive to initial values and achieve fast convergence at the end. Compared with other methods, the algorithm proposed in this paper has strong competitiveness.
Although the regularization term is added to the optimization objective in this paper to improve the convergence rate of the iteration process, its linear convergence property is not changed. In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
The present work was partially supported by the Defense Industrial Technology Development Program (Grant No. JCKY2020204B016).
- [1] B. Tian, W. Fan, R. Su, Q. Zong, Real-time trajectory and attitude coordination control for reusable launch vehicle in reentry phase, IEEE Trans. Ind. Electron. 62 (3) (2015) 1639–1650, https://doi .org /10 .1109 /TIE .2014 .2341553.
- [2] A.V. Rao, A survey of numerical methods for optimal control, Adv. Astronaut. Sci. 135 (1) (2010) 497–528, https://www.webofscience .com /wos /alldb /full -record /WOS : 000280501900030.
- [3] R. Chai, A. Savvaris, A. Tsourdos, S. Chai, Y. Xia, A review of optimization techniques in spacecraft flight trajectory design, Prog. Aerosp. Sci. 109 (2019) 100543, https:// doi .org /10 .1016 /j .paerosci .2019 .05 .003.
- [4] K.D. Mease, J. Kremer, Shuttle entry guidance revisited using nonlinear geometric methods, J. Guid. Control Dyn. 17 (6) (1994) 1350–1356, https://doi .org /10 .2514 /3 . 21355.
- [5] A. Caruso, A.A. Quarta, G. Mengali, M. Ceriotti, Shape-based approach for solar sail trajectory optimization, Aerosp. Sci. Technol. 107 (2020) 106363, https://doi .org /10 . 1016 /j .ast .2020 .106363.
- [6] Y. Zheng, X. Fu, M. Xu, Q. Li, M. Lin, Ascent trajectory design of small-lift launch vehicle using hierarchical optimization, Aerosp. Sci. Technol. 107 (2020) 106285, https:// doi .org /10 .1016 /j .ast .2020 .106285.
- [7] K. Mease, P. Teufel, H. Schoenenberger, D. Chen, S. Bharadwaj, Re-entry trajectory planning for a reusable launch vehicle, in: 24th Atmospheric Flight Mechanics Conference, Portland, OR, U.S.A., 1999.
- [8] D.A. Benson, G.T. Huntington, T.P. Thorvaldsen, A.V. Rao, Direct trajectory optimization and costate estimation via an orthogonal collocation method, J. Guid. Control Dyn. 29 (6) (2006) 1435–1440, https://doi .org /10 .2514 /1.20478.
- [9] S. Kameswaran, L.T. Biegler, Convergence rates for direct transcription of optimal control problems using collocation at Radau points, Comput. Optim. Appl. 41 (1) (2008) 81–126, https://doi .org /10 .1007 /s10589 -007 -9098 -9.
- [10] D. Garg, et al., A unified framework for the numerical solution of optimal control problems using pseudospectral methods, Automatica 46 (11) (2010) 1843–1851, https:// doi .org /10 .1016 /j .automatica .2010 .06 .048.
- [11] P. Lu, Entry guidance and trajectory control for reusable launch vehicle, J. Guid. Control Dyn. 20 (1) (1997) 143–149, https://doi .org /10 .2514 /2 .

### 20.9 常用词、词类、语态与时态

- 高频词：trajectory(17)；optimization(15)；error(11)；scp(10)；discretization(7)；control(7)；programming(6)；reentry(6)；algorithm(6)；aerospace(5)；sequential(5)；convex(5)；cient(5)；technology(4)；problems(4)；accuracy(4)；radau(4)；pseudospectral(4)；number(4)；state(4)
- 高频名词化/学术名词：optimization(15)；discretization(7)；reference(4)；science(3)；iteration(3)；curvature(3)；linearization(3)；guidance(3)；regularization(2)；performance(2)；cation(2)；motion(2)；equation(2)；destination(2)；extraction(1)
- 高频学术动词：developed(1)；validated(1)；compared(1)
- 高频形容词：sequential(5)；cient(5)；pseudospectral(4)；optimal(4)；differential(4)；dimensionless(3)；available(2)；hp-adaptive(2)；recent(2)；cial(2)；lossless(2)；polytechnical(1)；adaptive(1)；stable(1)；several(1)
- 高频副词：only(2)；adaptively(1)；especially(1)；gradually(1)；apply(1)；precisely(1)；directly(1)；ciently(1)
- 高频二词短语：trajectory optimization(11)；sequential convex(5)；convex programming(5)；radau pseudospectral(4)；coe cient(4)；aerospace science(3)；science technology(3)；optimization problems(3)；discretization error(3)；linearization error(3)；reentry trajectory(2)；pseudospectral discretization(2)
- 高频三词短语：sequential convex programming(5)；aerospace science technology(3)；radau pseudospectral discretization(2)；elsevier masson sas(2)；masson sas all(2)；sas all rights(2)；all rights reserved(2)；trajectory optimization problems(2)；lossless convexi cation(2)；form state control(2)；discrete motion equation(2)；source pdf hp-adaptive-rpd-based-sequential-convex-programming-(1)
- 被动语态估计：17；`we + 动作动词` 主动句估计：0
- 一般现在时线索：18；一般过去时线索：46；现在完成时线索：0；情态动词线索：3

章节词频：

- Abstract: scp(4)；september(3)；discretization(3)；iteration(3)；algorithm(3)；stage(3)；received(2)；reentry(2)
- Introduction: trajectory(15)；optimization(11)；scp(8)；algorithm(6)；control(6)；discretization(5)；programming(4)；reentry(4)
- Conclusion: scp(5)；iteration(4)；regularization(3)；algorithm(3)；convergence(3)；trajectory(2)；optimization(2)；convexi(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Trajectory optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [1].
  可迁移模板：Trajectory optimization plays a key role with regard to improved guidance and control for the reusable vehicle, especially in the reentry phase [X].
- 原句/结构：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [4–6].
  可迁移模板：Considering the high flight safety requirements and unpredictable flight states, improving the performance of trajectory optimization, including stability, computational efficiency, and result accuracy, is very important [X–X].
- 原句/结构：The rapid generation of an accurate reference trajectory plays a crucial role in guidance effects and flight safety [11–13].
  可迁移模板：The rapid generation of an accurate reference trajectory plays a crucial role in guidance effects and flight safety [X–X].
#### Gap句
- 原句/结构：However, since SCP belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the eﬃciency.
  可迁移模板：However, since METHOD belongs to the direct method category, essentially, discretization is also a crucial factor affecting the accuracy of the solution and the eﬃciency.
#### 方法句
- 原句/结构：Article history: Received 7 August 2022 Received in revised form 12 September 2022 Accepted 18 September 2022 Available online 23 September 2022 Communicated by Xingqun Zhan Sequential convex programming (SCP) methods have been developed to solve reentry trajectory optimization problems.
  可迁移模板：Article history: Received XAugust XReceived in revised form XSeptember XAccepted XSeptember XAvailable online XSeptember XCommunicated by Xingqun Zhan Sequential convex programming (METHOD) methods have been developed to solve reentry trajectory optimization problems.
- 原句/结构：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing SCP methods can be further improved.
  可迁移模板：Due to the oversimplified discretization and iteration, the accuracy and efficiency of the existing METHOD methods can be further improved.
- 原句/结构：In this paper, a SCP algorithm based on the hpadaptive Radau pseudospectral discretization (RPD) is proposed.
  可迁移模板：In this paper, a METHOD algorithm based on the hpadaptive Radau pseudospectral discretization (METHOD) is proposed.
#### 结果句
- 原句/结构：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II. © 2022 Elsevier Masson SAS.
  可迁移模板：With comparable or even higher results accuracy, the METHOD time reduced by X-X when compared to other METHOD methods, and is only twentieth of that of METHOD. © XElsevier Masson METHOD.
- 原句/结构：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II. © 2022 Elsevier Masson SAS.
  可迁移模板：With comparable or even higher results accuracy, the METHOD time reduced by X-X when compared to other METHOD methods, and is only twentieth of that of METHOD. © XElsevier Masson METHOD.
- 原句/结构：In addition, constraint relaxation and regularization techniques are used at the beginning and end of iteration, respectively, to make the proposed algorithm insensitive to initial values and achieve fast convergence at the end.
  可迁移模板：In addition, constraint relaxation and regularization techniques are used at the beginning and end of iteration, respectively, to make the proposed algorithm insensitive to initial values and achieve fast convergence at the end.
#### 贡献句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### 限制/边界句
- 原句/结构：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II. © 2022 Elsevier Masson SAS.
  可迁移模板：With comparable or even higher results accuracy, the METHOD time reduced by X-X when compared to other METHOD methods, and is only twentieth of that of METHOD. © XElsevier Masson METHOD.
- 原句/结构：With comparable or even higher results accuracy, the CPU time reduced by 40%-70% when compared to other SCP methods, and is only twentieth of that of GPOPS-II. © 2022 Elsevier Masson SAS.
  可迁移模板：With comparable or even higher results accuracy, the METHOD time reduced by X-X when compared to other METHOD methods, and is only twentieth of that of METHOD. © XElsevier Masson METHOD.
- 原句/结构：In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.
  可迁移模板：In future work, we want to utilize the Hessian matrix of nonlinear functions as the weight of the regularization item, which may boost the algorithm’s performance even more.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
