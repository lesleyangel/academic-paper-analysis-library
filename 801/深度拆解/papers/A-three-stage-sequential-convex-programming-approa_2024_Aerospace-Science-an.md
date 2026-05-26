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

> 自动分析说明：以下基于 `801/文本/txt/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

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

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.txt` 与 `801/文本/metadata/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 Problem formulation （方法/模型）
- L2 p.2: 3 Methodology （方法/模型）
  - L3 p.2: 3.1 Direct collocation method with hp RPD （方法/模型）
  - L3 p.3: 3.2 Fundamental of conventional SCP approach （对象/问题/模块）
  - L3 p.5: 3.3 Improved hp-Adaptive mesh refinement algorithm （对象/问题/模块）
  - L3 p.6: 3.4 The three-stage scp approach （对象/问题/模块）
- L2 p.7: 4 Simulations and discussion （结果/讨论/验证）
  - L3 p.7: 4.1 Reentry trajectory optimization with dual-channel control （对象/问题/模块）
  - L3 p.9: 4.2 Ascent trajectory optimization of launch vehicle （对象/问题/模块）
- L2 p.11: 5 Conclusions （结论）
- L2 p.11: Declaration of competing interest （对象/问题/模块）
- L2 p.11: Data availability （对象/问题/模块）
- L2 p.11: Acknowledgments （对象/问题/模块）
- L2 p.12: Appendix A Description of Eq. (28) （附录）
- L2 p.12: Appendix B Details of Reentry Example （附录）
- L2 p.14: Appendix C Details of Ascent Example （附录）
- L2 p.16: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Problem formulation | 2 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Methodology | 2 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Direct collocation method with hp RPD | 2 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Fundamental of conventional SCP approach | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Improved hp-Adaptive mesh refinement algorithm | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 The three-stage scp approach | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Simulations and discussion | 7 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Reentry trajectory optimization with dual-channel control | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Ascent trajectory optimization of launch vehicle | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 11 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 11 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 11 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 11 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix A Description of Eq. (28) | 12 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix B Details of Reentry Example | 12 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix C Details of Ascent Example | 14 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 16 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 最近，顺序凸规划（SCP）因其高效率而成为轨迹优化的潜在方法。为了提高稳定性和离散化精度，本文提出了一种基于hp自适应Radau伪谱离散化的三阶段SCP方法。在大多数情况下，由于未指定的初始猜测，初始子问题可能面临不可行的风险。因此，我们为SCP设计了一个约束松弛阶段，以尽可能增强子问题的可行性。一旦子问题可以直接求解，迭代进入第二阶段，在此阶段利用基于离散误差分析的网格细化算法将离散误差减小到容许范围内。最后阶段，在子问题的目标中引入阻尼项，以抑制解的振荡并加速收敛。以双通道控制再入轨迹优化和上升轨迹优化为例，仿真结果表明，该方法在精度和效率方面优于传统的SCP方法。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 本文针对一般轨迹优化问题提出了一种三阶段顺序凸规划方法。基于约束松弛、网格细化和迭代阻尼，有效改善了传统SCP方法迭代稳定性差、离散化误差大、收敛速度慢的问题。数值模拟结果表明，与其他SCP方法相比，该方法的精度（几乎相当于GPOPS-II）提高了2~4个数量级，并且CPU时间有一定程度的减少。本文的工作进一步增强了 SCP 方法在机载实时应用的潜力。此外，所提出的方法基于轨迹优化问题的一般形式，因此具有应用的普适性。所提出的方法仍然有一些局限性。一方面，为了进一步加快收敛速度​​，可以使用线搜索来确定迭代之间的步长。另一方面，使用二次函数来逼近非线性约束（需要使用BFPS等来逼近Hessian矩阵）可能比简单的线性化更有效。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：Indirect methods [9] have great advantages in solving simple problems, but they are difficult to imple ment when the control system is a little complicated.
- 本文解决方式：Recently, sequential convex programming (SCP) has become a potential approach in trajectory optimization because of its high efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
- 学术/工程增量：To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper. A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency. To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：57
- Introduction 引用簇数量（估计）：19
- References 条目数（解析）：34
- 可识别年份条目数：53
- 近五年/近年文献（2021+）数量：11
- 经典文献（2010年前）数量：9
- 同刊引用数量（按 subject 粗略匹配）：1
- 高频来源期刊（粗略）：Aerospace Science and Technology(1)
- 引用簇样例：[1,2], [7], [3], [10], [4,5], [6], [11,12], [7,8], [13], [14], [9], [1,19-21]

带引用的 gap/转折句样例：

- Over the last few years, many scholars proposed using sequence convex optimization (SCP) approaches to solve trajectory optimization problems [11,12].

References 解析样例（前12条）：

- [1] P. Lu, Entry guidance and trajectory control for reusable launch vehicle, J. Guidance, Control, Dyn. 20 (1) (1997) 143–149, https://doi.org/10.2514/ 2.4008.
- [2] D.B. Doman, M.W. Oppenheimer, M.A. Bolender, Progress in guidance and control research for space access and hypersonic vehicles, in: Proceedings of the 45th IEEE Conference on Decision and Control, 2006, https://doi.org/10.1109/ CDC.2006.377649.
- [3] P. Lu, Introducing computational guidance and control, J. Guidance, Control, Dyn. 40 (2) (2017) 193, https://doi.org/10.2514/1.G002745.
- [4] P. Sarmah, C. Chawla, R. Padhi, A nonlinear approach for re-entry guidance of reusable launch vehicles using model predictive static programming, in: 2008 16th Mediterranean Conference on Control and Automation, Ajaccio, Corsica, France, 2008, https://doi.org/10.1109/MED.2008.4602026.
- [5] B. Tian, W. Fan, R. Su, Q. Zong, Real-time trajectory and attitude coordination control for reusable launch vehicle in reentry phase, IEEE Trans. Ind. Electron. 62 (3) (2015) 1639–1650, https://doi.org/10.1109/TIE.2014.2341553.
- [6] Y. Shi, Z. Wang, A deep learning-based approach to real-time trajectory optimization for hypersonic vehicles, AIAA Scitech 2020 Forum, 2020, https://doi. org/10.2514/6.2020-0023.
- [7] R. Chai, A. Savvaris, A. Tsourdos, S. Chai, Y. Xia, A review of optimization techniques in spacecraft flight trajectory design, Prog. Aeosp. Sci. 109 (2019) 100543, https://doi.org/10.1016/j.paerosci.2019.05.003.
- [8] A.V. Rao, A survey of numerical methods for optimal control, Adv. Astronautical Sci. 135 (1) (2010) 497–528, https://doi.org/10.1166/1.6337.
- [9] E. Bryson, Applied optimal control: optimization, estimation and control, Taylor & Francis Group, New York, 1975.
- [10] M. Kelly, An introduction to trajectory optimization: how to do your own direct collocation, SIAM Rev 59 (4) (2017) 849–904, https://doi.org/10.1137/ 16M1062569.
- [11] R. Foust, S. Chung, F.Y. Hadaegh, Optimal guidance and control with nonlinear dynamics using sequential convex programming, J. Guidance, Control, Dyn. 43 (4) (2019) 633–644, https://doi.org/10.2514/1.G004590.
- [12] X. Liu, P. Lu, B. Pan, Survey of convex optimization for aerospace applications, Astrodynamics 1 (1) (2017) 23–40, https://doi.org/10.1007/s42064-017-0003-8.

### 20.9 常用词、词类、语态与时态

- 高频词：problem(25)；trajectory(20)；scp(20)；optimization(19)；control(17)；discretization(13)；points(13)；function(12)；constraints(12)；approach(11)；direct(9)；system(9)；programming(8)；stage(8)；approaches(8)；nlp(8)；convex(7)；flight(7)；initial(7)；objective(7)
- 高频名词化/学术名词：optimization(19)；discretization(13)；function(12)；solution(7)；guidance(6)；collocation(6)；transcription(6)；section(5)；science(4)；refinement(4)；convergence(4)；convexification(4)；dynamics(4)；relaxation(3)；iteration(3)
- 高频学术动词：compared(2)；indicate(2)
- 高频形容词：initial(7)；objective(7)；pseudospectral(6)；original(5)；sequential(4)；refinement(4)；optimal(4)；general(4)；dynamic(4)；boundary(4)；polynomial(4)；terminal(4)；hp-adaptive(3)；numerical(3)；iterative(3)
- 高频副词：directly(4)；typically(3)；respectively(3)；greatly(2)；successfully(2)；explicitly(2)；firstly(2)；finally(2)；recently(1)；quickly(1)；usually(1)；gradually(1)；mostly(1)；sufficiently(1)；early(1)
- 高频二词短语：trajectory optimization(13)；scp approaches(8)；scp approach(5)；direct collocation(5)；original problem(5)；aerospace science(4)；science technology(4)；sequential convex(4)；convex programming(4)；flight vehicle(4)；radau pseudospectral(4)；mesh refinement(4)
- 高频三词短语：aerospace science technology(4)；sequential convex programming(4)；radau pseudospectral discretization(3)；optimal control problem(3)；three-stage sequential convex(2)；approach trajectory optimization(2)；three-stage scp approach(2)；trajectory optimization problems(2)；page zhang aerospace(2)；zhang aerospace science(2)；initial terminal moments(2)；all knot points(2)
- 被动语态估计：27；`we + 动作动词` 主动句估计：0
- 一般现在时线索：59；一般过去时线索：86；现在完成时线索：0；情态动词线索：13

章节词频：

- Abstract: scp(4)；discretization(4)；approach(3)；trajectory(3)；optimization(3)；subproblem(3)；stage(3)；efficiency(2)
- Introduction: scp(16)；optimization(14)；problem(14)；trajectory(13)；discretization(10)；control(9)；stage(8)；approaches(8)
- Conclusion: approach(4)；problems(3)；scp(3)；approaches(3)；general(2)；trajectory(2)；optimization(2)；convergence(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：Indirect methods [9] have great advantages in solving simple problems, but they are difficult to imple ment when the control system is a little complicated.
  可迁移模板：Indirect methods [X] have great advantages in solving simple problems, but they are difficult to imple ment when the control system is a little complicated.
- 原句/结构：However, it is typically difficult to solve an NLP prob lem, and the performance of the direct method is mostly governed by the nonlinear programming solver.
  可迁移模板：However, it is typically difficult to solve an METHOD prob lem, and the performance of the direct method is mostly governed by the nonlinear programming solver.
- 原句/结构：The remainder of this paper is organized as follows.
  可迁移模板：The remainder of this paper is organized as follows.
#### 方法句
- 原句/结构：To improve stability and discretization accuracy, a three-stage SCP approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper.
  可迁移模板：To improve stability and discretization accuracy, a three-stage METHOD approach based on the hp-adaptive Radau pseudospectral discretization is proposed in this paper.
- 原句/结构：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
  可迁移模板：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional METHOD approaches in terms of accuracy and efficiency.
- 原句/结构：On the other hand, with the development of computational guidance and control [3] technology, the distinction between trajectory optimization and guidance is gradually blurring.
  可迁移模板：On the other hand, with the development of computational guidance and control [X] technology, the distinction between trajectory optimization and guidance is gradually blurring.
#### 结果句
- 原句/结构：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency.
  可迁移模板：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional METHOD approaches in terms of accuracy and efficiency.
- 原句/结构：Taking online optimization results as guidance instructions [4,5] or constructing a “guidance model” based on offline trajectory optimiza tion data [6] are the two main ways to realize advanced guidance.
  可迁移模板：Taking online optimization results as guidance instructions [X,X] or constructing a “guidance model” based on offline trajectory optimiza tion data [X] are the two main ways to realize advanced guidance.
- 原句/结构：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional SCP approaches in terms of accuracy and efficiency. improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly.
  可迁移模板：A dual-channel control reentry trajectory optimization and an ascent trajectory optimization are taken as examples, and the simulation results show that the proposed approach outperforms conventional METHOD approaches in terms of accuracy and efficiency. improvement of numerical optimization algorithms, it is possible to solve large-scale optimization problems quickly.
#### 贡献句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### 限制/边界句
- 原句/结构：In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.
  可迁移模板：In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.
- 原句/结构：Gong). https://doi.org/10.1016/j.ast.2024.109128 Received 23 May 2023; Received in revised form 16 August 2023; Accepted 5 April 2024 Available online 12 April 2024 1270-9638/© 2024 Elsevier Masson SAS.
  可迁移模板：Gong). https://doi.org/X/j.ast.XReceived XMay X; Received in revised form XAugust X; Accepted XApril XAvailable online XApril METHOD-X/© XElsevier Masson METHOD.
- 原句/结构：In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.
  可迁移模板：In most instances, the initial subproblem may risk infeasibility due to the undesignated initial guess.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
