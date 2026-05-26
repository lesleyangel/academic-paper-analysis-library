# A study of morphing aircraft on morphing rules along trajectory

## 0. 读取说明

本文拆解依据 `801/文本/txt/A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer.txt` 的全文抽取。txt 中双栏文本在 Introduction、Conclusions 和 References 处有交叉，图 1-18 的具体曲线与形状细节需要 PDF 图像复核。以下以文本可确认的任务设定、模型、表格数值与结论为主。

## 1. 基本信息与论文身份

- 题名：A study of morphing aircraft on morphing rules along trajectory
- 作者：Xiaoyu Chen, Chunna Li, Chunlin Gong, Liangxian Gu, Andrea Da Ronch
- 期刊：Chinese Journal of Aeronautics, 34(7), 232-243
- 年份：2021
- 领域：变体飞行器、气动代理模型、轨迹规划、低/高保真 CFD。
- 论文类型：方法应用型论文，结合多保真 Kriging、离线优化和轨迹规划。
- 研究对象：可变后掠角和翼身轴向位置的变体飞行器，在爬升巡航、下降巡逻、下降突防任务中的变形规律。
- 方法：Euler 低保真 CFD + Navier-Stokes 高保真 CFD 建立 MFK 模型；基于最大升阻比和压力中心限制做形状优化；再将最优气动表用于轨迹规划。
- 主要证据：240 个低保真数据、110 个高保真数据；MFK 留一交叉验证 RMSE/RRMSE；最优形状表；全轨迹和三阶段变形规律曲线；与传统轨迹优化计算量对比。
- 目标读者：变体飞行器气动/控制设计者、轨迹优化研究者、代理模型应用研究者。

## 2. 摘要与核心信息提取

一句话主张：将变体飞行器沿轨迹的变形规律研究转化为基于 MFK 代理模型的离线气动优化和轨迹规划问题，可以在保持较好气动性能的同时显著降低计算成本。

摘要中的核心卖点有三层。第一，研究对象不是单一飞行状态下的变形翼，而是整条任务轨迹中的 sweep angle 与 axial position 规律。第二，方法不是直接把变形变量塞进高维轨迹优化，而是先用多保真代理模型获得不同 Mach/攻角下的最优形状，再用于轨迹规划。第三，计算效率是主要证据：仅用 240 个低保真和 110 个高保真数据，较传统轨迹优化减少 86% 计算时间。

## 3. 选题层深拆

问题来源是变体飞行器的工程矛盾：变形翼可以在宽速度域内保持较好气动性能，但一旦把变形变量与轨迹规划同时考虑，CFD 调用和优化维度急剧增加。作者没有泛泛讨论“变体飞行器优化”，而是定义了一个更窄的问题：在给定任务和轨迹框架下，如何高效获得沿轨迹的变形规则。

问题定义包含明确边界：飞行器只考虑纵向平面质点动力学；变形变量只有后掠角与翼轴向位置；任务由爬升巡航、下降巡逻、下降突防构成；优化目标是最大升阻比并满足压力中心、后掠角和轴向位置限制。这个边界让文章从难以收敛的全变量最优控制问题转为可执行的离线流程。

选题价值主要是方法价值和工程价值。方法价值在于用 MFK 降低高保真 CFD 数量；工程价值在于给出沿任务阶段单调连续的 morphing rules，有利于机构实现。

## 4. 领域位置与文献版图

作者把已有研究组织成三类。

第一类是变体翼/变后掠翼气动和实验研究，包括 NASA 变后掠翼、风洞实验、减阻优化、变展长翼瞬态气动弹性等。这些研究说明变形可改善气动性能，但多数关注单点或气动特性本身。

第二类是变体飞行器轨迹优化方法，包括 indirect methods、shooting、PSO、collocation、伪谱方法、RPM 等。作者承认这些方法可以解轨迹问题，但强调初值敏感、收敛慢、依赖约束设置或对复杂问题不够高效。

第三类是代理模型，尤其是多保真 Kriging。作者从计算成本角度说明高保真 CFD 太贵，低保真 Euler 数据可提供全局趋势，高保真 N-S 数据可校正偏差。

本文位于“变体翼气动优化”和“轨迹规划”之间，试图跨越气动代理模型与任务轨迹设计。它不是提出新气动理论，而是提出一种离线工程流程。

## 5. Gap 制造机制

gap 的核心表述是：已有 morphing rules 研究多考虑气动特性，轨迹没有充分进入；已有轨迹优化方法可以处理控制变量，但变形变量引入后 CFD 计算量巨大，直接轨迹优化不经济。

具体 gap 包括：

- 场景 gap：只研究单状态或单气动特性，不能回答沿整条任务轨迹如何变形。
- 方法 gap：直接轨迹优化需要大量高保真 CFD 或密集插值表。
- 工程 gap：变形规则必须连续、单调、适合机构组织，而不仅是离散状态最优。
- 数据 gap：高保真数据少时，普通代理模型难以兼顾效率和准确度。

这个 gap 有说服力，因为作者在结果中用 Table 6 把计算代价从 18,000 h 降到 2,520 h。不过 gap 也带有前提：轨迹被给定/简化为几段任务，若进行真正闭环最优控制，本文流程可能不是全局最优。

## 6. 创新性判断

作者的创新在于把“沿轨迹变形规律”拆成两个相对简单的问题：基于 MFK 的离线形状优化，以及基于最优气动表的轨迹规划。这是流程创新和应用创新。

创新强度为中等。MFK 本身不是新方法，变后掠翼也不是新对象，轨迹规划也不是新理论；真正的新意在于把多保真气动代理作为中介，使 morphing rules 不再通过高维轨迹优化直接求解。

贡献写法很清楚：先提出方法，再证明模型准确，再给出轨迹规律，最后量化计算效率。最容易被挑战的是：作者把“study morphing rules”与“trajectory optimization”区别开来，但所得规则仍依赖预设任务和插值表，是否能代表最优轨迹需要谨慎。

## 7. 论证链条复原

变体飞行器需要适应多任务和宽速度域 → 变形会改变气动形状与压力中心 → 若在轨迹规划中直接调用 CFD，计算成本巨大 → 多保真代理模型可用大量低保真和少量高保真数据替代昂贵 CFD → 对不同 Mach/攻角建立升力、阻力、压力中心 MFK 模型 → 在变形范围和压力中心约束下求最大升阻比形状 → 建立最优气动性能插值表 → 进行分阶段轨迹规划 → 提取沿轨迹的后掠角和轴向位置变化规则 → 与传统轨迹优化比较计算成本。

链条闭合性较强，但“最优气动形状”与“最优轨迹”之间存在中间假设：局部最大升阻比被当作轨迹规划中合适的气动策略，而不是把燃耗、时间和姿态约束全部纳入统一优化。

## 8. 方法/理论/模型细拆

方法名称：基于 Multi-Fidelity Kriging 的离线变形规则学习流程。

输入：Mach number、angle of attack、sweep angle、axial wing position、低/高保真 CFD 气动数据、任务轨迹约束。输出：不同飞行状态下最优变形参数、沿轨迹的 sweep angle 和 wing axial position 变化。

关键模块：

1. 动力学模型：基于瞬时平衡假设，将飞行器视为可控质点，只研究纵向平面运动，状态包括速度、攻角、轨迹倾角、位置、质量。
2. MFK 模型：用自回归一阶模型 `y_high(x)=q(x)y_low(x)+d(x)`，低保真模型提供全局趋势，高保真模型校正误差。
3. 留一交叉验证：用 RMSE/RRMSE 评估升力、阻力、压力中心代理模型。
4. 形状优化：在 sweep angle、axial position、pressure centre 约束下最大化升阻比。
5. 轨迹规划：根据最优气动表规划爬升巡航、下降巡逻、下降突防，并提取变形规则。

关键参数和数据：Mach 选择 {0.35, 0.5, 0.65, 0.8, 0.95}，攻角 {0,2,4,6,8}；后掠角限制 [0,43]，轴向位置 [2235,2600] mm，压力中心 [2760,2920] mm。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| MFK 适合少量高保真数据的气动建模 | 方法 3.3/结果 4.2 | 240 低保真 + 110 高保真数据；Table 1/2 给出 RMSE/RRMSE，多数相对误差较小 | 强 | 只展示有限状态验证，外推风险存在 |
| 直接 CFD 轨迹优化计算量不可承受 | Introduction/4.4 | 传统轨迹优化至少需要 1500 高保真数据，约 18,000 h | 强 | 传统方案的网格密度设定可能影响比较 |
| 本文方法显著降低计算成本 | 结果 4.4/Table 6 | Proposed method 2520 h，trajectory optimization 18,000 h，减少 86% | 强 | 计算时间依赖硬件和 CFD 设置 |
| 沿轨迹变形规律具有单调性和连续性 | 结果 4.4 | Fig. 12/15/18：每个任务阶段后掠角与轴向位置随速度变化单调连续 | 中-强 | 曲线细节需 PDF 图像复核 |
| 最优形状随速度增加趋向更大后掠和更前翼位 | Table 3/结果 4.3 | Ma=0.35 时 (0,2600)，Ma=0.95 时多为 (43,2235) | 强 | 取决于压力中心和结构限制 |
| 复杂轨迹可以利用变形保持较好气动性能 | 摘要/结果 4.4 | 三个任务阶段均给出对应轨迹、速度曲线和 morphing rules | 中 | 未与固定翼或全局最优控制做性能收益对比 |
| 方法可扩展到更多变形变量 | 结论未来工作 | 作者指出 MFK 下变量增加的数据增量小于轨迹优化 | 弱-中 | 维数灾难仍可能出现，需要实证 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 任务轨迹示意 | 定义场景边界 | 研究沿轨迹变形规则 | 起飞、巡航、巡逻、突防等阶段 | 需要 PDF 图像复核 |
| Fig. 2 变形位置俯视图 | 说明变形变量 | 后掠角与轴向位置可控 | 最小/最大后掠和翼前后移动 | 需要 PDF 图像复核 |
| Fig. 3 流程图 | 展示方法闭环 | 离线代理 + 优化 + 轨迹规划 | CFD 数据、MFK、最优输入、轨迹规划 | 需要 PDF 图像复核 |
| Eq. (1)-(2) 质点动力学 | 把轨迹规划压缩到纵向模型 | 方法可计算 | 速度、航迹倾角、位置、质量随时间变化 | 公式排版需 PDF 复核 |
| Eq. (3)-(6) MFK 与误差指标 | 支撑代理模型可信度 | MFK 可用少量高保真数据 | 高/低保真关系，RMSE/RRMSE | 可从 txt 确认 |
| Eq. (7) 形状优化 | 把变形规则转成约束优化 | 最大升阻比形状 | 约束后掠角、轴向位置、压力中心 | 可从 txt 确认 |
| Table 1/2 交叉验证 | 证明代理精度 | MFK 模型足够准确 | RRMSE 多在工程可接受范围 | 可从 txt 确认 |
| Table 3-5 最优形状与气动表 | 连接代理模型与轨迹规划 | 最优气动表可用于轨迹 | 不同 Ma/攻角下变形参数、升力、阻力 | 可从 txt 确认 |
| Fig. 9-18 轨迹与变形规则 | 展示结果叙事 | 规则单调连续 | 三阶段速度、轨迹、后掠角、翼位变化 | 需要 PDF 图像复核 |
| Table 6 计算成本对比 | 最强效率证据 | 减少 86% 计算时间 | 240/110 数据 vs 1500 高保真数据 | 可从 txt 确认 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Problem description；3 Methods；4 Results and discussion；5 Conclusions。方法节下含 morphing rules 方法、动力学模型、MFK、交叉验证、形状优化。结果节下含气动仿真、MFK 建模、优化结果、沿轨迹变形规则。

结构简洁，像一篇工程应用方法论文。Introduction 负责说明为什么直接轨迹优化困难；Problem description 明确任务、限制和几何；Methods 给出代理建模和优化；Results 先验证模型，再展示轨迹规则，最后做效率对比。最值得模仿的是结果节顺序：模型可信度在前，应用结果在后，效率收益收尾。

标题命名偏流程型而非结论型，例如 `Results of MFK modeling`、`Results of optimization`。优点是清楚；弱点是读者需进入正文才知道最强结论。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                         on constraints when used to solve trajectory optimization | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 2 Problem description | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Method of studying morphing rules along trajectory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4 Results and discussion | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Results of MFK modeling | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 0.35 Ma, the aircraft is always in the optimal shape with sweep | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Conclusions                                                  References | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段先说明变体翼优势和已有研究，第二段转向轨迹优化方法局限，第三段提出本文离线轨迹规划方法。节奏是“价值 → 难点 → 方法”。

Problem description 通过任务约束 A-E 把模糊任务变成可规划问题。Methods 部分多以“为什么需要这个模块”开头，再给公式，例如先解释 CFD 计算量巨大，再引入 surrogate models 和 MFK。Results 的段落节奏以表格和图为中心：每个图表前说明设置，后解释规律。

结论先复述方法，再列三条结论，最后给未来工作。未来工作承认本文只考虑机翼变形变量和一种 MFK 模型，这种局限写法较稳健。

## 13. 文笔画像与语言习惯

语气偏工程实用，claim 强度主要围绕 “efficient”“reduce computational cost”“sufficient precision”。作者常用 “to alleviate computational cost”, “to improve efficiency”, “it can be seen that”, “it is obvious that”。

时态上，方法介绍用一般现在时，具体本文操作用一般过去时，结果解释用一般现在时。主动语态较多，尤其是 “we propose”, “we select”, “we build”。被动语态用于 CFD 设置和数据生成。

形容词/副词常见：efficient, optimum, huge, expensive, sufficient, monotonously, continuously。风险是 “obvious” 出现较多，若无图表支撑容易显得主观；本文大多配有表图。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：morphing(89)；trajectory(72)；aircraft(61)；wing(51)；delity(50)；optimization(48)；angle(41)；model(40)；method(39)；aerodynamic(36)；sweep(36)；data(35)；rules(33)；ight(30)；mfk(29)；position(25)；models(25)；stage(25)；high-(23)；axial(22)
- 高频学术名词：delity(50)；optimization(48)；model(40)；method(39)；position(25)；velocity(19)；performance(16)；acceleration(14)；pressure(11)；validation(10)；simulations(9)；tion(9)；simulation(8)；limitation(8)；results(7)；analysis(6)
- 高频学术动词：shown(15)；proposed(13)；solve(3)；compared(2)；predicted(2)；evaluate(2)；shows(2)；indicate(2)；simulated(1)；predict(1)；investigated(1)
- 高频形容词：aerodynamic(36)；axial(22)；cient(20)；descent(15)；low(10)；computational(10)；optimal(9)；variable(9)；experimental(8)；dynamic(8)；numerical(8)；different(7)；small(6)；global(6)；less(6)；initial(6)
- 高频副词/连接副词：respectively(10)；however(6)；accordingly(4)；directly(3)；greatly(3)；totally(3)；globally(2)；generally(2)；moreover(2)；finally(2)；commonly(2)；sharply(2)；usually(2)；tively(2)；specially(2)；actively(1)
- 高频二词短语：morphing rules(29)；sweep angle(29)；morphing aircraft(23)；delity data(23)；axial position(20)；high- delity(20)；trajectory optimization(17)；trajectory planning(15)；mfk models(14)；position wing(14)；aerodynamic performance(13)；low- delity(13)；aircraft morphing(12)；angle axial(12)；chin aeronaut(11)；study morphing(10)
- 高频三词短语：high- delity data(15)；sweep angle axial(12)；angle axial position(12)；axial position wing(11)；morphing aircraft morphing(8)；low- delity data(8)；study morphing aircraft(7)；aircraft morphing rules(7)；morphing rules along(7)；rules along trajectory(7)；studying morphing rules(7)；acceleration climbing stage(5)

**主动、被动与句法**

- 被动语态估计次数：95
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：657
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：190
- 一般过去时线索：44
- 现在完成时线索：0
- 情态动词线索：57
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：morphing(13)；trajectory(9)；aircraft(6)；aerodynamic(6)；chinese(5)；aeronautics(5)；delity(5)；data(5)
- 1. Introduction                                         on constraints when used to solve trajectory optimization：morphing(25)；wing(19)；trajectory(17)；aircraft(17)；method(17)；rules(10)；sweep(9)；ight(9)
- 3. Methods：无明显高频项
- 3.1. Method of studying morphing rules along trajectory：model(26)；delity(15)；data(13)；low-(10)；ylow(9)；trajectory(8)；simulations(7)；high-(7)
- 4. Results and discussion：unstructured(5)；mesh(5)；meshes(4)；symmetrical(3)；plane(3)；ight(3)；delity(3)；structured(3)
- 4.2. Results of MFK modeling：aircraft(17)；stage(16)；morphing(14)；cient(13)；ight(12)；trajectory(12)；shapes(11)；wing(11)
- 0.35 Ma, the aircraft is always in the optimal shape with sweep：angle(9)；delity(9)；trajectory(9)；sweep(7)；data(7)；optimization(7)；method(7)；high-(6)
- 5. Conclusions                                                  References：morphing(27)；optimization(27)；trajectory(15)；chinese(15)；aeronaut(15)；aircraft(13)；design(12)；delity(12)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`Morphing aircraft can meet requirements of multi-mission during the whole flight due to...`
- Gap 句式：`However, trajectory planning considering morphing variables requires a huge number of expensive CFD computations...`
- 方法句式：`To alleviate computational cost and improve ..., an offline optimization method is proposed based on ...`
- 代理模型句式：`many low-fidelity data and few high-fidelity data are used to build...`
- 验证句式：`leave-one-out cross validation is taken to verify the accuracy of the models.`
- 结果句式：`It can be seen that the sweep angle begins to...`
- 效率句式：`the former can reduce 86% of computing time than the latter.`
- 局限句式：`However, the morphing parts ... are mainly the wings...`

可复用表达：把“计算成本”写成具体数据组合，即 low-fidelity/high-fidelity 数量 + 单次耗时 + 总耗时 + 百分比降低。

## 15. 引用策略与文献使用

引用集中在 Introduction 和 MFK 方法介绍。变体翼文献用于证明研究对象已有基础；轨迹优化文献用于划分 indirect/direct/PSO/collocation/RPM 等方法谱系；多保真建模文献用于支撑 MFK 选择。

作者评价前人较直接但不攻击：NASA 和风洞研究“only considered aerodynamic characteristics”；RPM 对简单问题有效，但复杂问题需要高维插值且依赖约束。这种写法先肯定已有方法，再指出本文场景下的不足。

gap 与引用的关系是：引用建立“变形有用”和“轨迹优化常用”，再指出两者结合时计算成本太高，由此引入 MFK。

## 16. 审稿人视角风险

1. 纵向质点模型和瞬时平衡假设忽略姿态、控制动态和变形过程气动迟滞。
2. 研究目标是沿给定任务提取规则，不是严格全局最优轨迹；“best aerodynamic performance”主要指局部升阻比。
3. MFK 验证是留一交叉验证，缺少外部测试点或风洞/飞行验证。
4. 计算效率对比依赖传统轨迹优化中离散点数量设定，可能被认为不完全公平。
5. 变形机构动力学、执行器约束、变形速率和结构载荷没有纳入。
6. 高/低保真数据的误差来源和一致性分析较少，Euler 与 N-S 的偏差可能在跨声速状态更复杂。

## 17. 可复用资产

- 选题角度：把“变量太多导致轨迹优化太贵”转化为“先离线学习规则，再规划轨迹”的工程降维问题。
- 方法链：低保真全局趋势 + 高保真校正 + 交叉验证 + 局部形状优化 + 轨迹应用。
- 图表资产：用 Table 6 做计算成本对比，是工程方法论文很强的收束图表。
- 写法资产：在摘要中同时报数据数量和效率收益，让方法贡献一眼可见。
- 结果叙事：按任务阶段解释规则，使曲线不仅是数学结果，也对应飞行任务语义。

## 18. 对我写论文的启发

当研究对象复杂、直接联合优化困难时，可以学习本文的“先建立状态-最优参数映射，再在系统流程中调用”的写法。它适用于变形结构、热管理、控制参数调度等问题。

如果我要写类似论文，最好补上两类增强证据：一是和固定形态/直接轨迹优化的性能指标对比，而不仅是计算时间；二是引入执行器约束，证明规则不只是连续，还能被机构实际跟踪。

## 19. 最终浓缩

本文的核心贡献是用 MFK 离线代理模型把变体飞行器沿轨迹变形规则从高维昂贵优化中解耦出来。最强证据是 240 个低保真 + 110 个高保真数据即可得到规则，并比传统轨迹优化减少 86% 计算时间。最值得复用的是“计算昂贵问题 → 多保真代理 → 交叉验证 → 工程规则”的论文生产路径；最大风险是动力学和机构实现被简化。
