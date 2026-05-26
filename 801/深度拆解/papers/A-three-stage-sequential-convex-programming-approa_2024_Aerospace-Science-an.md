# A three-stage sequential convex programming approach for trajectory optimization

## 0. 读取说明

本文拆解依据 `801/文本/txt/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.txt` 的全文抽取。该文公式、算法框和图注在 txt 中有部分跨栏错位，尤其是 SCP 子问题、mesh refinement 算法和 appendix 公式需要 PDF 复核。拆解重点放在问题链、三阶段算法设计、仿真实证和写作结构。

## 1. 基本信息与论文身份

- 题名：A three-stage sequential convex programming approach for trajectory optimization
- 作者：Tengfei Zhang, Hua Su, Chunlin Gong
- 期刊：Aerospace Science and Technology, 149, 109128
- 年份：2024
- 领域：飞行器轨迹优化、序列凸规划、hp-adaptive Radau pseudospectral discretization、在线制导潜力。
- 论文类型：算法方法论文 + 两个典型轨迹优化仿真验证。
- 研究对象：一般多阶段飞行器轨迹优化问题，包括双通道控制再入轨迹和运载火箭上升轨迹。
- 方法：基于 hp-adaptive RPD 的三阶段 SCP：constraint relaxation & result approaching、mesh refinement、fast convergence with damping。
- 主要证据：算法流程、误差/曲率驱动网格细化、与 ED/RPD/GPOPS-II 对比的迭代次数、CPU time、状态误差、终端误差。
- 目标读者：轨迹优化算法研究者、计算制导研究者、飞行器任务规划工程师。

## 2. 摘要与核心信息提取

一句话主张：通过把 SCP 迭代拆成约束松弛、网格细化和阻尼快速收敛三阶段，可以同时改善传统 SCP 的初始可行性、离散精度和收敛效率。

摘要中的三个关键词分别对应三类痛点。constraint relaxation 用于解决初始猜测不好导致子问题不可行；hp-adaptive mesh refinement 用于降低离散误差；damping term 用于抑制迭代振荡和加快收敛。两个示例证明其在准确性和效率上优于 conventional SCP approaches，并接近 GPOPS-II 精度但计算时间更短。

## 3. 选题层深拆

问题来源是轨迹优化在飞行器设计和计算制导中的双重需求：离线轨迹可用于总体设计评估，在线优化结果也可能直接作为制导指令，因此方法必须既准确又高效。

作者把宽泛的轨迹优化问题收束到 SCP 的三个具体瓶颈：初始值差导致子问题不可行；简单离散方案导致精度差；固定步长迭代出现振荡导致收敛慢。这个收束很适合方法论文，因为每个瓶颈都能对应一个算法组件。

选题价值来自方法价值和应用价值。方法上，三阶段设计比单一“加 penalty function”更可控；应用上，CPU time 降低和网格自适应增强了 onboard real-time application 的潜力。

## 4. 领域位置与文献版图

作者首先把轨迹优化放在 indirect methods 与 direct methods 的历史谱系中。Indirect methods 对简单问题有优势，但复杂控制系统实现困难；direct collocation 将最优控制转成 NLP，表达目标和约束更灵活，但依赖 NLP solver。

第二层是 SCP 文献。SCP 通过一系列凸子问题逼近原问题，已用于 rocket launch and landing、atmospheric reentry、missile flight 等。但早期 SCP 使用简单离散和低阶数值积分，精度不足；近期已有 hp-adaptive RPD 与 SCP 结合的尝试。

第三层是本文 gap：初始猜测影响迭代稳定性，常见 penalty function 会影响最优性、收敛慢且权重难选；同时已有 SCP 很难同时处理初始可行性、离散精度和最终快速收敛。

## 5. Gap 制造机制

gap 的核心是“三个局部问题没有被一个统一 SCP 流程同时解决”。

- 可行性 gap：初始 reference solution 与真实轨迹偏差大时，线性化后的子问题可能不可行。
- 精度 gap：SCP 仍属于 direct collocation，离散误差不处理会污染解质量。
- 收敛 gap：网格更新后若固定步长且无 line search，解可能振荡，拖慢收敛。

作者特别批评 penalty function 不是根本办法：它会带来权重选择困难、慢收敛和最优性损失。这个 gap 有针对性，因为后文第一阶段直接用约束松弛替代 penalty，第三阶段用 damping term 替代被动等待收敛。

## 6. 创新性判断

创新点可拆成三项：

1. 约束松弛阶段：把微分约束按 relaxation factor 放宽，逐步把 reference trajectory 拉近真实轨迹。
2. 网格细化阶段：基于离散误差和曲率比决定增加 LGR knot points 还是划分子段。
3. 快速收敛阶段：在目标中加入 `η||Z-Z_ref||^2` 阻尼项，抑制第三阶段数值振荡。

真实创新是算法流程设计和工程化整合。单个组件可能都有类似思想，但本文把它们组织成可解释的三阶段 SCP，并通过两个问题证明不同阶段各自承担功能。创新强度中等偏强，尤其适合 Aerospace Science and Technology 这类重视工程适用性的期刊。

## 7. 论证链条复原

轨迹优化需要高精度和高效率 → direct methods 进步但 NLP 难解 → SCP 通过凸子问题提升效率 → 现有 SCP 仍面临初始不可行、离散误差和迭代振荡 → 本文基于 hp-adaptive RPD 构建一般多阶段轨迹问题转录 → 先给 conventional SCP 子问题 → 增加 mesh refinement 算法评估离散误差 → 设计三阶段 SCP 流程 → 用再入和上升两个典型问题验证 → 与 ED/RPD/GPOPS-II 比较 CPU time、迭代次数和误差 → 得出准确性提高 2-4 个数量级、CPU time 降低且具有通用性。

链条闭合良好。最薄弱环节是方法仍在 MATLAB + MOSEK 桌面环境中验证，所谓 onboard potential 还不是真实机载实现。

## 8. 方法/理论/模型细拆

方法名称：Three-stage SCP with hp-adaptive Radau pseudospectral discretization (ARPD)。

输入：多阶段最优控制问题的状态、控制、动力学、路径约束、边界约束、初始/终端条件、初始网格和 reference solution。输出：满足终端和路径约束的优化轨迹、控制序列、自适应网格。

关键结构：

1. 问题转录：用 LGR collocation points 将连续 Bolza 问题转成 NLP，再在线性化 reference solution 周围构造 second-order cone programming 子问题。
2. lossless convexification：控制方向余弦/幅值约束用二阶锥形式 `||u_1:K-1||_2 <= u_K`。
3. mesh refinement：用新增 LGR 点违反微分方程的程度定义 discretization error；用 curvature ratio 判定加阶还是分段。
4. 第一阶段：松弛微分约束，若不可解则倍增 relaxation factor，步长小以避免发散。
5. 第二阶段：可直接求解后进入网格细化，同时更新 reference solution。
6. 第三阶段：离散误差达到阈值后加入阻尼项，减小振荡并加速收敛。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 约束松弛能缓解初始不可行 | 方法 3.4/再入示例 | 再入问题前几次迭代需第一阶段使子问题结果接近收敛值 | 中-强 | 缺少单独消融表，仅从迭代过程间接体现 |
| 阻尼项可抑制第三阶段振荡 | 结果 4.1/Fig. 4 | 无阻尼第三阶段 38 次迭代且振荡；有阻尼 9 次收敛且无振荡 | 强 | 只展示一个状态 ψ 的例子 |
| ARPD 在再入问题中速度明显优于 GPOPS-II | Table 2 | SCP(ARPD) CPU 6.640 s，GPOPS-II 78.375 s，终端经度接近 | 强 | GPOPS-II 设置参数可能影响公平性 |
| ARPD 再入精度接近 GPOPS-II | Table 3 | 状态/终端误差与 GPOPS-II 同量级，明显优于 ED/RPD | 强 | 需 PDF 复核表格完整列 |
| ARPD 上升轨迹收敛快且网格少 | Table 5/Fig. 11-12 | SCP(ARPD) 52 knot points、13 iterations、0.338 s；GPOPS-II 69 nodes、11.105 s | 强 | MATLAB/MOSEK 桌面环境不等于机载环境 |
| ARPD 上升问题精度比简单 SCP 高 1-2 个数量级 | Table 6 | ARPD 最大状态误差接近 GPOPS-II，ED/RPD 误差更大 | 强 | 部分误差数值需 PDF 复核 |
| 方法具有一般多阶段轨迹优化适用性 | 结论/两示例 | 再入双通道控制 + 运载火箭两阶段上升均验证 | 中 | 仍只有两个航空航天示例，复杂路径约束覆盖有限 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Eq. (1)-(2) 一般多阶段问题 | 定义适用范围 | 方法通用性 | 多阶段 Bolza 目标、动力学、路径/边界约束 | 公式排版需 PDF 复核 |
| Eq. (10)-(27) conventional SCP 转录 | 交代基线方法 | 三阶段改进有基础 | NLP 到 SOCP 子问题 | 公式排版需 PDF 复核 |
| Fig. 1 hp RPD 示意 | 解释离散方案 | ARPD 精度来源 | segment、polynomial order、LGR points | 需要 PDF 图像复核 |
| Algorithm 1 mesh refinement | 说明自适应网格规则 | 降低离散误差 | 依据 error 和 curvature ratio 加点/分段 | 需要 PDF 复核算法框 |
| Fig. 2 三阶段流程图 | 展示方法全貌 | 三瓶颈三组件 | constraint relaxation、mesh refinement、fast convergence | 需要 PDF 图像复核 |
| Fig. 4 阻尼效果 | 支撑第三阶段必要性 | 阻尼减少迭代 | 38 次 vs 9 次 | 曲线需 PDF 复核 |
| Table 2/3 再入对比 | 核心性能证据 | ARPD 快且准 | CPU 6.640 s，对比 GPOPS-II 78.375 s | 表格可从 txt 确认 |
| Fig. 7/8 再入误差与网格演化 | 解释为什么快 | 自适应网格有效 | 子段平均配点约 4 | 需要 PDF 图像复核 |
| Table 5/6 上升对比 | 第二任务验证 | 方法泛化 | ARPD 0.338 s，精度接近 GPOPS-II | 表格可从 txt 确认 |
| Fig. 11/12 上升误差与网格演化 | 展示收敛和网格更新 | 平滑变量只需增点 | 3 次 mesh refinement 降至容差 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Problem formulation；3 Methodology；4 Simulations and discussion；5 Conclusions。方法节内部依次是 direct collocation with hp RPD、conventional SCP、mesh refinement、three-stage SCP。

结构是标准算法论文：先定义一般问题，再复现基线方法，再嵌入改进组件，最后用两个案例对比验证。一个优点是作者没有直接抛出三阶段算法，而是先把 conventional SCP 写清楚，让读者知道改进发生在哪里。

结果节安排也有层次：第一个再入问题非线性强，证明第一阶段和第三阶段有用；第二个上升问题较平滑，证明网格细化和效率优势。两例互补。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：5
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                 improvement of numerical optimization algorithms, it is possible to | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Fundamental of conventional SCP approach | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Simulations and discussion | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Reentry trajectory optimization with dual-channel control | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Ascent trajectory optimization of launch vehicle | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“轨迹优化应用重要 → 方法谱系 → SCP 优势 → SCP 问题 → 本文三阶段方案”。它没有过多铺历史，而是服务于三个痛点。

方法段落密集公式化，每段先说明工程/数值含义，再给数学形式。比如 mesh refinement 先解释离散误差由网格决定，再定义 error 和 curvature ratio。三阶段段落用清晰的命名把算法功能直接暴露：result approaching、mesh refinement、fast convergence。

结果段落遵循“设置 → 对比对象 → 图表观察 → 表格量化 → 解释原因”的顺序。结论短而集中，同时承认 line search 和 nonlinear constraints quadratic approximation 是未来改进方向。

## 13. 文笔画像与语言习惯

文笔偏算法工程，常用词包括 feasibility, discretization accuracy, convergence speed, reference solution, subproblem, trust region, damping term, mesh refinement。claim 强度适中，常用 “effectively improved”, “significant advantages”, “almost equivalent to GPOPS-II”。

语态上，方法定义多用被动和形式主语，如 “is defined by”, “is utilized”, “it can be observed”。贡献段用主动 “we design”, “we propose”。时态稳定：方法用一般现在时，仿真结果用一般过去/现在混合。

作者喜欢给算法阶段命名并加括号解释，这是方法论文中很好的读者导航方式。抽象术语较多，但通过两个示例拉回工程可读性。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：scp(72)；control(61)；cos(53)；optimization(50)；trajectory(49)；problem(49)；sin(44)；stage(40)；constraints(35)；org(32)；mesh(30)；points(30)；discretization(29)；iteration(28)；constraint(28)；error(26)；follows(24)；convex(23)；state(23)；approach(22)
- 高频学术名词：optimization(50)；solution(44)；discretization(29)；iteration(28)；approach(22)；guidance(21)；method(20)；function(19)；equation(18)；reference(18)；science(17)；refinement(17)；convergence(17)；system(14)；comparison(13)；results(11)
- 高频学术动词：shown(13)；solve(12)；proposed(12)；shows(6)；solved(6)；compared(5)；show(4)；indicates(3)；indicate(2)；compare(2)；formulated(1)；evaluate(1)；propose(1)
- 高频形容词：initial(17)；refinement(17)；numerical(16)；optimal(15)；nonlinear(14)；terminal(14)；linear(13)；dynamic(12)；pseudospectral(12)；objective(12)；sequential(10)；different(9)；significant(8)；hp-adaptive(8)；segment(8)；coefficient(8)
- 高频副词/连接副词：respectively(9)；directly(8)；generally(6)；finally(6)；however(5)；therefore(4)；greatly(3)；typically(3)；firstly(3)；anomaly(3)；significantly(2)；weakly(2)；notably(2)；moreover(2)；successfully(2)；explicitly(2)
- 高频二词短语：trajectory optimization(27)；cos cos(21)；cos sin(19)；sin cos(18)；aerospace science(17)；science technology(17)；mesh refinement(16)；zhang aerospace(15)；knot points(14)；scp approaches(13)；sin sin(13)；optimal control(12)；convex programming(11)；discretization error(11)；ref ref(11)；sequential convex(10)
- 高频三词短语：aerospace science technology(17)；zhang aerospace science(15)；sequential convex programming(10)；sin cos cos(9)；sin sin cos(9)；ref ref ref(8)；cos cos sin(8)；cos sin sin(8)；cos cos cos(7)；mesh refinement algorithm(6)；reentry trajectory optimization(6)；deg deg deg(6)

**主动、被动与句法**

- 被动语态估计次数：102
- `we + 动作动词` 主动句估计次数：5
- 名词化表达估计次数：623
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：199
- 一般过去时线索：21
- 现在完成时线索：7
- 情态动词线索：42
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：trajectory(5)；optimization(5)；approach(4)；scp(4)；discretization(4)；aerospace(3)；sequential(3)；convex(3)
- 1. Introduction                                                 improvement of numerical optimization algorithms, it is possible to：problem(34)；constraints(22)；control(21)；scp(21)；trajectory(19)；stage(19)；mesh(18)；discretization(17)
- 4. Simulations and discussion：means(2)；mesh(2)；matlab(2)；optimization(2)；initial(2)；obtained(2)；result(2)；following(1)
- 4.1. Reentry trajectory optimization with dual-channel control：cos(53)；scp(47)；sin(44)；control(37)；org(31)；optimization(26)；trajectory(24)；stage(18)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`Both ... and ... greatly benefit from trajectory optimization.`
- Gap 句式：`Initial value guessing is a significant aspect that affects...`
- 方法句式：`To make the SCP method more stable and efficient, we divided the iterative process into three stages...`
- 阶段命名句式：`The first stage (...): ...`
- 对比句式：`For comparison, we use ... to solve the problem.`
- 结果句式：`It can be seen from Fig. X that...`
- 精度句式：`has similar accuracy to that of GPOPS-II`
- 局限句式：`The proposed approach still has some limitations. On the one hand... On the other hand...`

可复用表达：把算法贡献映射到痛点的写法非常值得学，如 “poor iteration stability, large discretization error, and slow convergence speed” 对应三阶段。

## 15. 引用策略与文献使用

引用策略按方法谱系组织。早期最优控制、indirect/direct methods 说明历史背景；direct collocation 文献说明 transcription 进步；SCP 文献说明应用范围；hp-adaptive RPD 文献说明本文基底；MOSEK/GPOPS-II 用作工具和对比基准。

作者对前人态度是“承认优势 + 指出局部问题”。例如 direct collocation 有表达约束的优势，但受 NLP solver 支配；SCP 避免复杂 NLP，但仍有初值和离散问题。引用不是堆算法名，而是服务于本文三段式 gap。

## 16. 审稿人视角风险

1. 缺少系统消融实验：单独去掉 constraint relaxation、mesh refinement、damping term 的量化对比不够完整。
2. 与 GPOPS-II 的 CPU time 比较依赖软件参数、容差、硬件和实现语言，需谨慎解读。
3. MATLAB + MOSEK 桌面仿真不能直接证明 onboard real-time application。
4. 动力学线性化和二阶锥松弛的适用边界需要在更复杂非凸约束问题中验证。
5. 初始猜测采用端点线性插值，极端不良初值或复杂路径约束下可行性还需测试。
6. 对 line search 的缺失在结论中承认，但固定步长策略仍可能影响普适收敛性。

## 17. 可复用资产

- 选题套路：把一个成熟算法的痛点拆成三个可命名、可验证的小问题。
- 方法资产：阶段命名 + 每阶段对应一个数学子问题，是算法论文的清晰结构。
- 证据资产：同时报告 knot points、iterations、CPU time、state error、terminal error，比只报目标值更有说服力。
- 图表资产：用误差-迭代曲线证明收敛，用网格特征演化图解释自适应机制。
- 写作资产：结论中用“2-4 orders of magnitude”概括精度提升，但正文表格给出细节。

## 18. 对我写论文的启发

如果我做算法改进，最重要的是不要只说“更快更准”，而要先拆清楚旧方法慢/不准/不稳分别来自哪里。本文的写法说明：一个好算法贡献最好有“痛点-模块-证据”的一一对应。

结果对比也值得学习：既与简单基线比，证明改进必要；又与成熟软件比，证明工程竞争力。对自己论文而言，可以增加消融表，让每个模块的贡献更难被审稿人质疑。

## 19. 最终浓缩

本文将 SCP 的初始可行性、离散精度和后期收敛三个痛点，分别交给 constraint relaxation、hp-adaptive mesh refinement 和 damping term 处理。最强证据是两个典型轨迹优化案例中，ARPD 精度接近 GPOPS-II 而 CPU time 显著更低。最可复用的是“问题拆解式算法设计”；最大风险是缺少更系统的模块消融和真实机载验证。
