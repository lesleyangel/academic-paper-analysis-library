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

> 自动分析说明：以下基于 `jmps/文本/txt/hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science-.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

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
