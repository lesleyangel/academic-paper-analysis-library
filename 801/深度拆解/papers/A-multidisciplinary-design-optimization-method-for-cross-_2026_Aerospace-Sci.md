# A multidisciplinary design optimization method for cross-domain vehicles based on distributed-centralized augmented Lagrangian coordination

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.txt`。该文包含大量公式、流程图和表格，txt 抽取存在双栏串行问题；尤其是 ALC 数学推导、Algorithm、Table 1-6、Fig. 4-16 的流程和图像细节需要 PDF 图像复核。本文以可识别摘要、Introduction、方法章节、优化结果和结论为依据。

## 1. 基本信息与论文身份

- 题名：A multidisciplinary design optimization method for cross-domain vehicles based on distributed-centralized augmented Lagrangian coordination。
- 作者：Qi Liu, Hua Su, Songyu Liu, Shengyu Zeng, Chunlin Gong。
- 期刊与年份：Aerospace Science and Technology, 2026, 169, 111499。
- 研究对象：X37-like cross-domain vehicle，涉及 geometry、aerodynamics、trajectory、thermal protection、structure、mass 等学科。
- 论文类型：多学科设计优化方法论文，结合参数化建模、协调优化算法和飞行器算例。
- 核心方法：基于 3D CST 的几何/气动/结构一体化参数化建模；distributed-centralized augmented Lagrangian coordination（ALC）方法；自适应异步乘子/罚权更新；以 payload mass 最大化或质量优化为目标的嵌套 MDO 流程。
- 主要证据：数学例子比较 distributed、distributed parallel、centralized、dominant、distributed-centralized ALC；X37-like vehicle 优化前后对比；payload mass 增加 318.5 kg，即 70.2%；结构应力/变形和再入轨迹约束验证。

## 2. 摘要与核心信息提取

本文的一句话主张是：跨域飞行器的气动、结构、轨迹等高耗时强耦合学科导致传统串行/单一协调优化效率低，因此应结合 3D CST 联合建模与 distributed-centralized ALC，在保留并行求解效率的同时降低一致性约束和耦合误差。

摘要按“三步贡献”写：第一，提出 integrated geometric-aerodynamic-structural parametric modeling；第二，提出 distributed-centralized ALC 与 adaptive asynchronous multiplier update；第三，用 X37-like vehicle 完成 nested MDO，优化后 payload mass 增加 70.2%。这是一种典型工程方法论文摘要：方法架构 + 算法策略 + 工程指标。

核心信息不是单纯“优化了一个飞行器”，而是“解决高耗时学科强耦合 MDO 的协调效率问题”。X37-like 算例用于证明方法不是理论推导，而能嵌入 geometry/aero/structure/trajectory/TPS/mass 的工程流程。

## 3. 选题层深拆

选题来源是跨域飞行器设计复杂性。Cross-domain vehicles 同时具有航空和航天特征，覆盖在轨、再入、高超声速滑翔、近空间飞行等任务，构型复杂，气动、结构、轨迹和热防护强耦合且计算昂贵。

作者把大问题收束为两个可处理问题：第一，如何用统一参数化模型避免几何、气动、结构之间的数据转换和模型断裂；第二，如何用协调优化架构在强耦合 MDO 中兼顾并行性、收敛性和求解误差。

选题价值是工程设计效率和系统最优性。传统 discipline-decoupling 可能丢失协同效应，串行迭代求解又低效；本文试图通过 3D CST 和 ALC 架构把“联合建模”和“联合优化”连接起来。

## 4. 领域位置与文献版图

Introduction 先铺开跨域飞行器的工程背景，再引出传统多学科解耦方法的不足。随后将 MDO 协调方法分为 CO、CSSO、BLISS、ATC 和 ALC 等谱系。作者强调 ATC 有数学收敛支撑，ALC 通过 augmented Lagrangian relaxation 可处理层级和非层级问题，计算成本较低。

文章进一步细分 ALC：distributed ALC 不引入 master problem，但直接耦合限制并行；distributed parallel ALC 可并行但一致性约束过多、强耦合下难收敛；centralized ALC 可消除子问题间直接耦合，但 master problem 选择和耦合负担高；dominant ALC 在强耦合下仍可能一致性约束过多。

本文站位是：在 ALC 家族中提出 distributed-centralized 中间路线，试图兼顾 distributed 的并行和 centralized 的耦合削减；同时用 3D CST 解决跨域飞行器几何/气动/结构联合建模问题。

## 5. Gap 制造机制

本文 gap 包括两个层次。建模 gap：CAD-based parametric modeling 低效、成本高、难以支持大规模设计空间探索，也难以保证气动/结构拓扑同步变化。优化 gap：现有 ALC 变体在强耦合问题中不是并行性不足，就是一致性约束太多、乘子更新不匹配或 master problem 选择困难。

gap 的关键逻辑是：跨域飞行器的难点不是某个单学科模型，而是强耦合系统中“模型一体化 + 优化协调”的共同瓶颈。因此只改形状参数化或只改 ALC 都不够，需要联合解决。

该 gap 有较强工程说服力，但也有验证压力：如果算例只展示一个 X37-like vehicle，审稿人可能要求更多不同耦合结构或不同 master problem 选择下的鲁棒性证明。

## 6. 创新性判断

作者声明的创新主要包括：基于 3D CST 的几何/气动/结构联合参数化；distributed-centralized ALC 方法；adaptive asynchronous multiplier update；X37-like 跨域飞行器嵌套 MDO 实现。

真实创新类型是工程方法框架创新和协调算法改造。3D CST、ALC、MDO 都已有，本文的新意在于把它们组合成面向 cross-domain vehicle 的两层协调架构，并用 distributed-centralized 方式减少耦合变量和保持并行效率。

创新强度：中等偏强。强在系统集成和工程指标，弱在算法理论原创可能有限。若投工程设计类期刊，该贡献成立；若投优化理论期刊，可能需要更严格的收敛证明、复杂度分析和更多基准。

## 7. 论证链条复原

全文论证链条如下：

1. 跨域飞行器任务环境复杂、速度/空域范围大，必须同时考虑气动、结构、轨迹、热防护和质量。
2. 学科强耦合和高耗时求解导致传统解耦/串行优化效率低、可能损失全局最优。
3. 现有 ALC 方法在并行性、耦合变量、一致性约束和 master problem 选择之间存在权衡。
4. 先用 3D CST 统一几何/气动/结构参数，减少跨学科数据转换。
5. 再用 distributed-centralized ALC 构建两层协调优化，配合自适应异步乘子和罚权更新。
6. 用数学例子比较多种 ALC 方法的收敛效率和精度。
7. 用 X37-like vehicle 完成 MDO，payload mass 明显提升，同时满足热、翼展、应力、变形等约束。

逻辑闭合度较高。最薄弱环节在于：优化结果的改进有多少来自 3D CST 参数化设计空间，有多少来自 ALC 协调策略，文章需要消融或对照更清楚地区分。

## 8. 方法/理论/模型细拆

方法第一层是联合建模。3D CST 用 category function 和 shape function 表达截面与三维基本曲面；通过 ψ、η、τ 等非递减节点向量生成气动外形和结构网格。气动模型由几何参数化形状生成表面网格，结构模型基于气动模型在高度方向引入参数，避免 CAD/CAE 反复转换。

第二层是其他学科模型：trajectory 使用考虑地球自转和飞行器动力学的三自由度极坐标轨迹方程；thermal protection 估算再入热流影响下 TPS 质量；mass 模型整合结构质量、TPS 质量和 payload mass。

第三层是 distributed-centralized ALC。系统被分为 master problem 与若干 subproblems，放松 coupling constraints 和 consistency constraints，利用 augmented Lagrangian 形式协调。自适应异步更新策略根据一致性约束误差更新 Lagrange multipliers 与 penalty weights，试图避免罚权过大导致数值困难。

关键假设：3D CST 参数足以表达优化所需几何变化；气动/结构/轨迹/TPS 低阶或工程模型精度可接受；MDO 目标和约束代表任务需求；ALC 更新策略在所给耦合结构下稳定。

## 9. 证据系统与 Claim-Evidence 表

证据系统包括两部分：算法基准和工程应用。算法基准用数学例子展示不同 ALC 变体在迭代数、计算时间、一致性约束收敛上的差异；工程应用用 X37-like vehicle 展示优化目标和约束结果。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| distributed-centralized ALC 比 dominant/centralized ALC 更高效 | 结论、Fig. 7-9 | 数学例子中比较目标值、迭代次数、计算时间和一致性约束收敛 | 中强 | 数学例子规模和代表性需复核 |
| 相比 distributed/distributed parallel ALC，本文方法误差更小、局部最优风险更低 | 结论、算法比较 | 作者声称 solution errors 最小且对局部最优不敏感 | 中 | 需查看误差定义和多初值测试 |
| 3D CST 能实现几何/气动/结构联合参数化 | 2.2、Fig. 2、公式 | CST 表达截面、表面和结构节点，避免跨学科数据转换 | 中强 | 建模精度和适用构型范围需 PDF/代码复核 |
| X37-like vehicle 优化后 payload mass 增加 70.2% | 摘要、Table 5、4.4 | payload mass 从 454.0 kg 到 772.5 kg，增加 318.5 kg | 强 | 目标函数和 takeoff mass 固定条件需复核 |
| 优化后结构约束满足 | 4.1/4.4、Fig. 15 | 最大应力 5.914e7 Pa，最大变形 2.487e-3 m，未触及约束上限 | 中强 | 图像与约束限值需 PDF 复核 |
| 关键 CST 参数可通过多方法敏感性筛选 | 4.2、Fig. 10-11、Table 4 | correlation coefficient、regression、Sobol、neural network 给出综合敏感度 | 中 | 敏感性方法融合权重需复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 任务剖面 | 跨域飞行器多阶段任务复杂 | 在轨与再入/近空间飞行共同驱动多学科耦合 | 需要 PDF 图像复核 |
| Eq. (1)-(8) | 3D CST 几何表达 | 联合参数化可行 | 用 category/shape functions 和节点向量生成曲面 | 公式需 PDF 复核 |
| Fig. 2 | 初始结构参数化网格 | 几何/结构建模一致 | 结构网格随 CST 参数生成 | 需要 PDF 图像复核 |
| Eq. (14) | 轨迹动力学 | 轨迹学科纳入 MDO | 三自由度极坐标再入方程 | 公式需 PDF 复核 |
| Fig. 3 | design structure matrix | 学科耦合关系可视化 | 显示 geometry/aero/trajectory/TPS/structure/mass 之间耦合 | 需要 PDF 图像复核 |
| Fig. 4/Fig. 5 | distributed-centralized ALC 流程 | 协调架构 | 展示 master/subproblem 和更新过程 | 需要 PDF 图像复核 |
| Fig. 7-9 | ALC 方法对比 | 本文方法效率/收敛优势 | 不同收敛阈值下迭代数、时间和一致性约束 | 需要 PDF 图像复核 |
| Fig. 10-11 | 敏感性分析 | 设计变量筛选 | head-body joint shape factor、wing thickness 等影响大 | 需要 PDF 图像复核 |
| Fig. 12-13 | MDO 流程和目标历史 | 优化过程可收敛 | distributed-centralized ALC 后期目标更优 | 需要 PDF 图像复核 |
| Table 5/6 | 优化前后数值 | payload mass 提升 | 772.5 kg payload，结构质量下降，TPS 质量略增 | 表格需 PDF 复核 |
| Fig. 14-16 | CAD、结构和轨迹结果 | 工程约束满足 | 优化外形、应力/变形分布、再入轨迹变化 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

文章结构大致为：1 Introduction；2 Cross-domain vehicle，包括 mission requirements、3D CST joint modeling、trajectory/TPS/mass 等学科模型、design structure matrix；3 Distributed-centralized ALC method，包括数学公式、更新策略和收敛分析；4 Optimization design，包括 problem overview、sensitivity analysis、optimization process、optimization results；5 Conclusion。

结构采用“对象/学科模型 → 协调算法 → 算例验证”的顺序。与一般 MDO 论文不同，它先把 cross-domain vehicle 的工程对象讲清楚，再进入 ALC 算法，这有助于读者理解为什么需要 distributed-centralized 而不是抽象优化器。

标题偏工程描述型，如 “Joint geometric/aerodynamic/structural modeling based on the 3D CST method”“Design structure matrix”“Optimization results”。最值得模仿的是 design structure matrix 章节，它把复杂耦合关系从文字转成结构矩阵，是 MDO 论文非常有用的路线图。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：4
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结论/展望型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2.4 Design structure matrix | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Sensitivity analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Conclusion | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.3 Optimization methods and processes                                     centralized ALC, the proposed distributed-centralized ALC method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是：跨域飞行器价值 → 任务环境复杂 → 学科耦合和计算成本 → MDO 协调方法谱系 → 现有 ALC 变体不足 → 本文 distributed-centralized ALC。段落推进很像“工程痛点 + 方法谱系排除法”。

建模章节段落偏公式驱动，通常先给传统方法不足，再给 CST 表达式和节点参数，再说明避免数据转换。优化算法段落先抽象系统分解，再引入松弛和增广拉格朗日，最后给流程图。

结果段落先做敏感性筛选，再展示优化流程和结果。它的叙事重心是“目标提升是否满足约束”，因此 Table 5 和 Fig. 15/16 是核心证据。结论段落则回到效率、并行性、误差和工程应用指导意义。

## 13. 文笔画像与语言习惯

整体语气是工程优化型，常用 multidisciplinary、coupling、subproblems、consistency constraints、parallel、efficiency、payload mass、optimization。claim 强度较强，摘要和结论中使用 significantly improved、highest computational efficiency、smallest solution errors 等表达。

主动语态多用于本文贡献：“we propose”“we build”；被动语态用于模型和结果：“is proposed”“is established”“is shown”。名词化程度很高，如 coordination、parameterization、decomposition、convergence、optimization。

时态上，Introduction 用现在时描述跨域飞行器特点和方法谱系；方法章节用现在时定义公式；结果章节多用过去时或现在时解释图表。情态词常见 can、may，用于方法能力和潜在问题。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：method(156)；alc(153)；optimization(67)；problem(66)；distributed(63)；coupling(57)；subproblems(57)；design(54)；convergence(45)；master(44)；variables(43)；parallel(41)；mass(41)；distributed-centralized(40)；shown(38)；vehicle(36)；based(32)；methods(32)；centralized(29)；multidisciplinary(28)
- 高频学术名词：method(156)；optimization(67)；coupling(57)；solution(52)；structure(46)；convergence(45)；analysis(24)；science(22)；system(21)；results(18)；equation(18)；condition(18)；coordination(18)；iteration(18)；function(17)；model(12)
- 高频学术动词：shown(38)；proposed(18)；solve(13)；compared(11)；solved(8)；shows(3)；validated(2)；indicate(2)；estimated(1)；validate(1)；show(1)；evaluate(1)；simulate(1)；revealed(1)
- 高频形容词：dominant(48)；local(34)；multidisciplinary(28)；structural(28)；objective(23)；aerodynamic(22)；computational(19)；optimal(17)；analytical(16)；parametric(14)；geometric(11)；high(10)；dynamic(10)；low(9)；traditional(9)；thermal(9)
- 高频副词/连接副词：significantly(6)；respectively(6)；however(5)；mainly(5)；therefore(3)；finally(3)；directly(3)；early(3)；relatively(3)；usually(3)；theoretically(2)；strongly(2)；firstly(2)；widely(2)；tively(2)；continuously(2)
- 高频二词短语：alc method(101)；distributed-centralized alc(35)；master problem(27)；centralized alc(26)；distributed alc(25)；distributed parallel(22)；parallel alc(21)；dominant alc(20)；aerospace science(19)；science technology(19)；liu aerospace(17)；design optimization(15)；alc methods(15)；cross-domain vehicle(14)；updating strategy(13)；multidisciplinary design(12)
- 高频三词短语：distributed-centralized alc method(26)；aerospace science technology(19)；distributed parallel alc(18)；centralized alc method(18)；liu aerospace science(17)；distributed alc method(16)；dominant alc method(15)；parallel alc method(14)；multidisciplinary design optimization(9)；consistency constraint convergence(9)；alc method dominant(9)；augmented lagrangian coordination(8)

**主动、被动与句法**

- 被动语态估计次数：117
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：820
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：248
- 一般过去时线索：22
- 现在完成时线索：6
- 情态动词线索：45
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：method(33)；design(26)；problem(25)；vehicle(22)；optimization(20)；based(18)；coupling(17)；cos(17)
- 2.4. Design structure matrix：alc(126)；method(100)；distributed(52)；subproblems(44)；coupling(40)；problem(39)；convergence(36)；master(34)
- 4.3. Optimization methods and processes                                     centralized ALC, the proposed distributed-centralized ALC method：optimization(23)；method(22)；design(18)；alc(12)；multidisciplinary(12)；based(10)；mass(9)；shown(8)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频词/短语：distributed-centralized ALC、coupling variables、subproblems、master problem、consistency constraints、penalty weights、Lagrange multipliers、3D CST、cross-domain vehicle、payload mass。

可复用问题句：`There is a strong nonlinear coupling between different disciplines, and traditional decoupling design may lead to the loss of the overall optimal solution.`

可复用 gap 句：`Existing coordination methods face a trade-off between parallel solving efficiency and the number of consistency constraints.`

可复用方法句：`An integrated geometric-aerodynamic-structural parametric modeling method is developed to avoid tedious data conversion between disciplines.`

可复用贡献句：`The proposed coordination method balances computational efficiency and parallel scalability through an adaptive asynchronous multiplier update strategy.`

可复用结果句：`The optimized design increases the payload mass by X% while satisfying structural, trajectory and thermal protection constraints.`

## 15. 引用策略与文献使用

引用主要服务四个功能：跨域飞行器工程背景；传统飞行器/高超声速设计和 MDO 理论；CO、CSSO、BLISS、ATC、ALC 等协调方法谱系；CST 几何参数化和飞行器建模。作者引用姿态通常是“已有方法有用，但在强耦合高耗时场景下仍有不足”。

gap 与引用连接方式是多层排除：CO/CSSO/BLISS 有两层结构但收敛支撑不足；ATC 收敛支撑更强但成本高；ALC 更灵活，但 distributed/centralized/dominant 各有并行性和一致性约束问题。这样本文方法不是凭空提出，而是 ALC 谱系内部的一种折中改进。

引用风险：MDO 与 ALC 文献很广，若遗漏近期基于 ADMM、surrogate-assisted MDO、Bayesian optimization 或 gradient-based multidisciplinary feasible architectures 的工作，审稿人可能要求补充。

## 16. 审稿人视角风险

1. 算法创新与工程集成的边界需要清晰：distributed-centralized ALC 相对已有 ALC 的数学本质差异需充分证明。
2. X37-like 单一算例的优化改进可能依赖初始构型和参数化空间，泛化到其他 cross-domain vehicle 需要更多案例。
3. 70.2% payload mass 提升很强，需核查 takeoff mass 固定、约束设置、设计变量范围是否公平。
4. 气动模型精度、结构模型简化和 TPS 质量估算误差会传递到 MDO 结论。
5. 敏感性分析使用四种方法综合排序，但融合规则和样本量可能影响变量筛选。
6. 收敛分析在工程非凸问题中可能不足以保证全局最优，需谨慎表达。

## 17. 可复用资产

可复用选题套路：从“复杂工程系统强耦合 + 单学科高耗时”切入，提出同时解决建模一致性和优化协调效率的方法。

可复用论证链：工程对象复杂 → 学科耦合矩阵 → 现有协调方法对比 → 新协调策略 → 数学例子验证 → 工程算例验证 → 优化指标和约束复核。

可复用图表：任务剖面图；参数化网格图；design structure matrix；ALC 架构图；求解流程图；收敛/计算时间对比图；敏感性排序图；优化前后 CAD 和轨迹图。

可复用表达：`balances efficiency and parallel computation`, `adaptive asynchronous multiplier update`, `joint geometric/aerodynamic/structural modeling`, `nested multidisciplinary design optimization process`。

## 18. 对我写论文的启发

这篇论文值得学习的是用 design structure matrix 把复杂耦合关系可视化。MDO 论文如果只写“多学科耦合”，读者很难判断问题复杂度；矩阵能让 gap 更可信。

摘要的“三贡献 + 一个硬结果”也很实用：先说建模，再说算法，再说工程验证，最后给 70.2% 这种明确数字。工程期刊很吃这一套。

需要避免的是过强结果没有足够消融。自己的论文如果同时提出建模方法和优化算法，最好分别设计对照：只换建模、不换算法；只换算法、不换建模；二者都换。

## 19. 最终浓缩

本文最值得学的是：把 cross-domain vehicle MDO 的难点拆成联合参数化和协调优化两条主线，并用 3D CST + distributed-centralized ALC 形成工程闭环。

最大风险是：单一算例和强优化提升可能掩盖模型简化、参数空间与约束设置的敏感性，图表/公式细节需 PDF 复核。

可迁移的三件事：一是用学科耦合矩阵制造 MDO gap；二是用多种协调方法对比证明算法必要性；三是用优化前后任务、结构和质量指标共同支撑工程有效性。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.txt` 与 `801/文本/metadata/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 Cross-domain vehicle （对象/问题/模块）
  - L3 p.2: 2.1 Mission requirements （对象/问题/模块）
  - L3 p.3: 2.2 Joint geometric/aerodynamic/structural modeling based on the 3D CST method （方法/模型）
    - L4 p.3: 2.2.1 Geometry （对象/问题/模块）
    - L4 p.3: 2.2.2 Aerodynamics （对象/问题/模块）
    - L4 p.4: 2.2.3 Structure （对象/问题/模块）
  - L3 p.4: 2.3 Modeling in other disciplines （方法/模型）
    - L4 p.4: 2.3.1 Trajectory （对象/问题/模块）
    - L4 p.5: 2.3.2 Thermal protection （对象/问题/模块）
    - L4 p.5: 2.3.3 Mass （对象/问题/模块）
  - L3 p.5: 2.4 Design structure matrix （对象/问题/模块）
- L2 p.5: 3 Distributed-centralized ALC method （方法/模型）
  - L3 p.6: 3.1 Distributed-centralized ALC model （方法/模型）
  - L3 p.6: 3.2 Distributed-centralized ALC method-solving strategy （方法/模型）
  - L3 p.8: 3.3 Convergence analysis （对象/问题/模块）
  - L3 p.10: 3.4 Numerical case studies （结果/讨论/验证）
    - L4 p.10: 3.4.1 Definition of the problem （对象/问题/模块）
    - L4 p.13: 3.4.2 Problem-solving （对象/问题/模块）
    - L4 p.14: 3.4.3 Analysis of results （结果/讨论/验证）
- L2 p.16: 4 Multidisciplinary design optimization for the cross-domain vehicle （对象/问题/模块）
  - L3 p.17: 4.1 Overview of the optimization problem （对象/问题/模块）
  - L3 p.17: 4.2 Sensitivity analysis （对象/问题/模块）
  - L3 p.17: 4.3 Optimization methods and processes （方法/模型）
  - L3 p.17: 4.4 Optimization results （结果/讨论/验证）
- L2 p.17: 5 Conclusion （结论）
- L2 p.17: Funding （对象/问题/模块）
- L2 p.17: Replication of results （结果/讨论/验证）
- L2 p.17: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.17: Declaration of competing interest （对象/问题/模块）
- L2 p.18: Data availability （对象/问题/模块）
- L2 p.18: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Cross-domain vehicle | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Mission requirements | 2 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Joint geometric/aerodynamic/structural modeling based on the 3D CST method | 3 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.1 Geometry | 3 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.2 Aerodynamics | 3 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2.3 Structure | 4 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Modeling in other disciplines | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.1 Trajectory | 4 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.2 Thermal protection | 5 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.3 Mass | 5 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.4 Design structure matrix | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Distributed-centralized ALC method | 5 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Distributed-centralized ALC model | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Distributed-centralized ALC method-solving strategy | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Convergence analysis | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 Numerical case studies | 10 | 3 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4.1 Definition of the problem | 10 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4.2 Problem-solving | 13 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4.3 Analysis of results | 14 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Multidisciplinary design optimization for the cross-domain vehicle | 16 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Overview of the optimization problem | 17 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Sensitivity analysis | 17 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 Optimization methods and processes | 17 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.4 Optimization results | 17 | 3 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusion | 17 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Funding | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Replication of results | 17 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 18 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 18 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 针对跨域车辆配置的复杂性带来的气动、结构、轨迹等高耗时学科求解效率低下的问题，提出一种基于增强拉格朗日协调和几何/气动/结构学科联合建模的嵌套多学科设计优化方法。首先，提出基于3D CST方法的集成几何-气动-结构参数化建模，实现几何/气动/结构联合建模。其次，提出了一种平衡效率和并行计算的分布式集中式增强拉格朗日协调方法，并采用自适应异步乘子更新策略来更新惩罚权重。最后以跨域车辆中的类X37车辆为对象，建立其嵌套的多学科设计优化流程，以最优质量为目标进行优化设计。优化结果表明，在整个任务过程中，优化后的设计形状在初始形状的基础上增加了有效载荷质量70.2%，性能显着提升，验证了本文提出的分布式集中式增强拉格朗日协调多学科设计优化方法的有效性。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusion；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-multidisciplinary-design-optimization-method-for-cross-_2026_Aerospace-Sci.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 针对计算时间消耗大导致求解复杂跨域车辆配置计算效率低的问题，本文重点研究跨域车辆的学科耦合特性。基于3D CST方法，实现几何/气动/结构联合仿真。通过收敛分析，提出了一种分布式集中式ALC方法。通过数学公式，我们评估了分布式、分布式并行、集中式、主导式和分布式集中式 ALC 方法的计算效率、并行可扩展性和求解精度。结果表明，与主导 ALC 和集中式 ALC 相比，所提出的分布式集中式 ALC 方法最大限度地减少了耦合变量和解耦变量，同时实现了最高的计算效率。相对于分布式 ALC 和分布式并行 ALC，它产生最小的解误差，并且对局部最优的敏感性降低。最后，通过解决跨域飞机多学科优化问题，进一步验证了所提方法的可行性和有效性。研究成果为多学科设计优化提供了新见解，为工程实践应用提供了重要指导。

### 20.7 论文逻辑脉络复核

- 提出的问题：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem. The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
- 旧方法/已有研究不足：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem.
- 本文解决方式：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations. Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling. Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
- 学术/工程增量：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper. The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：68
- Introduction 引用簇数量（估计）：11
- References 条目数（解析）：39
- 可识别年份条目数：42
- 近五年/近年文献（2021+）数量：7
- 经典文献（2010年前）数量：16
- 同刊引用数量（按 subject 粗略匹配）：1
- 高频来源期刊（粗略）：Aerospace Science and Technology(1)
- 引用簇样例：[3], [4], [1,2], [5,6], [7,8], [9,10], [14], [21], [15], [19], [20], [22]

带引用的 gap/转折句样例：

- However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].
- Gui [19] et al. proposed a distributed parallel ALC method, using the coupling values obtained in the previous round of each subproblem for the next round of solving, which can realize the parallel solving of the subproblems, but all the subproblems are decoupled and solved in parallel, which leads to too many consistency constraints, and it is difficult to satisfy all the consistency constraints for the strongly coupled problems, which leads to the results failing to converge, and the study also shows that in the parallel solving, the efficiency of the current AL-AD algorithm, which has the best efficiency, will lead to information mismatch when updating the Lagrange multipliers, and the Lagrange multipliers may not be optimal; and the increase of the penalty weights leads to numerical difficulties when solving the optimization problem [20], which further aggravates the convergence difficulties.
- While Nie [21] et al. proposed the dominant ALC method, selecting a subproblem with the highest number of coupling quantities with other subproblems as the master problem can reduce the copy of coupling variables between the master problem and other subproblems, and achieve a balance between the coordination cost and parallelization, but for the strong coupling problem, selecting a discipline as the master problem will create the same problem as the distributed parallel ALC method, consistency constraints are too many and difficult to satisfy all of them, resulting in the results not converging.

References 解析样例（前12条）：

- [1] R. Hu, J.H. Meng, et al., Integrated structure/mechanism design of cross-domain wing-body fusion variant vehicle, Unmanned Sys. Technol. 7 (2) (2024) 51–64.
- [2] C.J. Li, F.C. Liu, N. Liu, et al., Design of inertial guidance device and anti-shock measurement method for cross-domain vehicle, Electron. Measure. Technol. 47 (5) (2024) 167–172.
- [3] S.B. Luo, Integrated Design of Airframe-Engine For Hypersonic Vehicle, Science Press, Beijing, 2018.
- [4] X., Q. Chen, et al., Multidisciplinary Design Optimization Theory and Application of Hypersonic Vehicle, Science Press, Beijing, 2020.
- [5] R. Balling, M.R. Rawlings, Collaborative optimization with disciplinary conceptual design, Struct. Multidisciplinary Opt. 20 (3) (2000) 232–241.
- [6] L.L. Yang, W.L. Li, X.L. Kong, H. Xu, Mixed uncertainty robust Cooperative optimization design method, Comp Integr Manuf Sys. 27 (11) (2021) 3282–3290.
- [7] R.D. Braun, A.A. Moore, I.M. Kroo, Collaborative approach to launch vehicle design, J. Spacecr. Rockets 34 (4) (1997) 478–486.
- [8] C. Ye, S.H. Miao, C. Li, W.C. Yang, D.D. Sun, Co-optimization of transmission and distribution grids based on improved parallel subspace algorithm, J. Electrotechnol. 33 (23) (2018) 5509–5522.
- [9] J. Sobieszczanski-Sobieski, S. Kodiyalam, BLISS/S: a new method for two-level structural optimization, Struct. Multidisciplinary Opt. 21 (1) (2001) 1–13.
- [10] P. Jiang, L. Kuang, X.Y. Shao, M. Xiao, An approximate model-based Cooptimization approach for two-stage integrated systems, China Mech. Eng. 23 (4) (2012) 395–402.
- [11] H.M. Kim, N.F. Michelena, P.Y. Papalambros, T. Jiang, Target cascading in optimal system design, in: ASME 2000 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference 12, 2020.
- [12] J. Sun, T. Qu, D.X. Nie, M. Thürer, C.D. Li, G.Q. Huang, Dual-channel multilevel distribution network location-inventory problem, Comp. Integr. Manuf.Sys. 27 (11) (2021) 3305–3317.

### 20.9 常用词、词类、语态与时态

- 高频词：alc(153)；problem(65)；distributed(63)；coupling(57)；subproblems(57)；optimization(54)；convergence(44)；master(44)；variables(43)；fig(41)；distributed-centralized(40)；parallel(40)；mass(40)；design(37)；vehicle(29)；centralized(29)；solving(28)；structural(27)；problems(27)；solution(26)
- 高频名词化/学术名词：optimization(54)；convergence(44)；solution(26)；structure(22)；science(20)；iteration(18)；coordination(17)；function(17)；relationship(15)；computation(11)；protection(9)；equation(9)；reference(9)；condition(9)；thickness(9)
- 高频学术动词：compared(11)；optimized(6)；validated(2)；indicate(2)；estimated(1)；revealed(1)；validate(1)
- 高频形容词：structural(27)；dominant(23)；objective(22)；multidisciplinary(20)；aerodynamic(20)；computational(19)；local(17)；table(17)；optimal(15)；geometric(11)；traditional(9)；thermal(9)；parametric(8)；adaptive(7)；initial(6)
- 高频副词：respectively(6)；mainly(5)；only(4)；finally(3)；significantly(3)；directly(3)；early(3)；relatively(3)；usually(3)；firstly(2)；widely(2)；tively(2)；continuously(2)；slightly(2)；fly(1)
- 高频二词短语：distributed-centralized alc(35)；master problem(27)；centralized alc(26)；distributed alc(25)；distributed parallel(22)；parallel alc(21)；dominant alc(20)；aerospace science(19)；science technology(19)；page liu(17)；liu aerospace(17)；alc distributed(17)
- 高频三词短语：aerospace science technology(19)；distributed parallel alc(18)；page liu aerospace(17)；liu aerospace science(17)；alc dominant alc(12)；science technology fig(10)；alc distributed parallel(9)；consistency constraint convergence(9)；augmented lagrangian coordination(8)；centralized alc dominant(8)；alc distributed-centralized alc(8)；multidisciplinary design optimization(7)
- 被动语态估计：94；`we + 动作动词` 主动句估计：0
- 一般现在时线索：242；一般过去时线索：452；现在完成时线索：1；情态动词线索：45

章节词频：

- Abstract: design(5)；optimization(5)；multidisciplinary(3)；augmented(3)；lagrangian(3)；coordination(3)；aerodynamic(3)；structural(3)
- Introduction: problem(21)；optimization(16)；coupling(15)；design(14)；solving(14)；subproblems(11)；alc(11)；parallel(10)
- Conclusion: alc(7)；computational(4)；distributed(4)；efficiency(3)；cross-domain(3)；parallel(3)；solving(2)；solution(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Distributed ALC does not eliminate the direct coupling variables between subproblems, and the direct coupling and coordination between each subproblem requires each subproblem to be solved consecutively, which restricts the parallel solution of the subproblems and leads to low efficiency of problem-solving.
  可迁移模板：Distributed METHOD does not eliminate the direct coupling variables between subproblems, and the direct coupling and coordination between each subproblem requires each subproblem to be solved consecutively, which restricts the parallel solution of the subproblems and leads to low efficiency of problem-solving.
- 原句/结构：The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
  可迁移模板：The research findings provide new insights for multidisciplinary design optimization and offer important guidance for engineering practice applications.
#### Gap句
- 原句/结构：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem.
  可迁移模板：However, since the flight of this type of vehicle covers both aerospace and aviation domains, the mission and flight environment are complex, and its multidisciplinary design needs to comprehensively consider the flight environment of in-orbit operation and re-entry flight, and the configuration is more complex, which will directly affect the aerodynamic, structural and trajectory disciplines with high timeconsumption and high computational cost, making it more difficult and longer to solve the problem.
- 原句/结构：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].
  可迁移模板：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [X].
- 原句/结构：Gui [19] et al. proposed a distributed parallel ALC method, using the coupling values obtained in the previous round of each subproblem for the next round of solving, which can realize the parallel solving of the subproblems, but all the subproblems are decoupled and solved in parallel, which leads to too many consistency constraints, and it is difficult to satisfy all the consistency constraints for the strongly coupled problems, which leads to the results failing to converge, and the study also shows that in the parallel solving, the efficiency of the current AL-AD algorithm, which has the best efficiency, will lead to information mismatch when updating the Lagrange multipliers, and the Lagrange multipliers may not be optimal; and the increase of the penalty weights leads to numerical difficulties when solving the optimization problem [20], which further aggravates the convergence difficulties.
  可迁移模板：Gui [X] et al. proposed a distributed parallel METHOD method, using the coupling values obtained in the previous round of each subproblem for the next round of solving, which can realize the parallel solving of the subproblems, but all the subproblems are decoupled and solved in parallel, which leads to too many consistency constraints, and it is difficult to satisfy all the consistency constraints for the strongly coupled problems, which leads to the results failing to converge, and the study also shows that in the parallel solving, the efficiency of the current METHOD algorithm, which has the best efficiency, will lead to information mismatch when updating the Lagrange multipliers, and the Lagrange multipliers may not be optimal; and the increase of the penalty weights leads to numerical difficulties when solving the optimization problem [X], which further aggravates the convergence difficulties.
#### 方法句
- 原句/结构：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations.
  可迁移模板：A nested multidisciplinary design optimization method based on augmented Lagrangian coordination and joint geometric/aerodynamic/structural disciplines modeling is proposed to address the problem of inefficient solving in high time-consuming disciplines such as aerodynamic, structural, and trajectory, brought by the complexity of the cross-domain vehicle configurations.
- 原句/结构：Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the 3D CST method is proposed to realize joint geometric/aerodynamic/structural modeling.
  可迁移模板：Firstly, integrated geometric-aerodynamic-structural parametric modeling based on the METHOD METHOD method is proposed to realize joint geometric/aerodynamic/structural modeling.
- 原句/结构：Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
  可迁移模板：Second, a distributed-centralized augmented Lagrangian coordination method that balances efficiency and parallel computation is proposed with an adaptive asynchronous multiplier update strategy to update the penalty weights.
#### 结果句
- 原句/结构：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.
  可迁移模板：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by X based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper.
- 原句/结构：Cross-domain vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in both military and civil fields, and thus have received extensive attention from scholars at home and abroad [1,2].
  可迁移模板：Cross-domain vehicles combine the typical features of aviation and space vehicles, can fly remotely in the atmosphere and transatmosphere, and have the characteristics of a large airspace and wide velocity domain, which have shown great application value in both military and civil fields, and thus have received extensive attention from scholars at home and abroad [X,X].
- 原句/结构：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by 70.2 % based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper. relationship is maintained [3].
  可迁移模板：The optimization results show that during the whole mission, the optimized design shape increases the payload mass by X based on the initial shape, and the performance is significantly improved, which verifies the effectiveness of the distributed-centralized augmented Lagrangian coordination multidisciplinary design optimization method proposed in this paper. relationship is maintained [X].
#### 贡献句
- 原句/结构：Finally, the X37-like vehicle in the cross-domain vehicle is taken as an object, and its nested multidisciplinary design optimization process is established to carry out the optimization design with the goal of optimal mass.
  可迁移模板：Finally, the X37-like vehicle in the cross-domain vehicle is taken as an object, and its nested multidisciplinary design optimization process is established to carry out the optimization design with the goal of optimal mass.
- 原句/结构：Finally, the X37-like vehicle in the cross-domain vehicle is taken as an object, and its nested multidisciplinary design optimization process is established to carry out the optimization design with the goal of optimal mass.
  可迁移模板：Finally, the X37-like vehicle in the cross-domain vehicle is taken as an object, and its nested multidisciplinary design optimization process is established to carry out the optimization design with the goal of optimal mass.
- 原句/结构：Tosserams [16–18] et al. proposed the method of introducing the master problem, which establishes the indirect coupling between the master problem and the subproblems, eliminates the direct coupling between the subproblems, and realizes the parallel solution of the problem.
  可迁移模板：Tosserams [X–X] et al. proposed the method of introducing the master problem, which establishes the indirect coupling between the master problem and the subproblems, eliminates the direct coupling between the subproblems, and realizes the parallel solution of the problem.
#### 限制/边界句
- 原句/结构：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [4].
  可迁移模板：However, there is a strong nonlinear coupling between different disciplines of the cross-domain vehicle, and the traditional discipline decoupling design method makes it difficult to consider the synergistic effect generated by the mutual coupling between disciplines, which may lead to the loss of the overall optimal solution of the system, thus reducing the overall performance of the vehicle [X].
- 原句/结构：Gui [19] et al. proposed a distributed parallel ALC method, using the coupling values obtained in the previous round of each subproblem for the next round of solving, which can realize the parallel solving of the subproblems, but all the subproblems are decoupled and solved in parallel, which leads to too many consistency constraints, and it is difficult to satisfy all the consistency constraints for the strongly coupled problems, which leads to the results failing to converge, and the study also shows that in the parallel solving, the efficiency of the current AL-AD algorithm, which has the best efficiency, will lead to information mismatch when updating the Lagrange multipliers, and the Lagrange multipliers may not be optimal; and the increase of the penalty weights leads to numerical difficulties when solving the optimization problem [20], which further aggravates the convergence difficulties.
  可迁移模板：Gui [X] et al. proposed a distributed parallel METHOD method, using the coupling values obtained in the previous round of each subproblem for the next round of solving, which can realize the parallel solving of the subproblems, but all the subproblems are decoupled and solved in parallel, which leads to too many consistency constraints, and it is difficult to satisfy all the consistency constraints for the strongly coupled problems, which leads to the results failing to converge, and the study also shows that in the parallel solving, the efficiency of the current METHOD algorithm, which has the best efficiency, will lead to information mismatch when updating the Lagrange multipliers, and the Lagrange multipliers may not be optimal; and the increase of the penalty weights leads to numerical difficulties when solving the optimization problem [X], which further aggravates the convergence difficulties.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
