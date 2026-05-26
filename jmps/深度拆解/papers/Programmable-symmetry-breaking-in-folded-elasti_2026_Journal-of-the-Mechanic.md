# Programmable symmetry-breaking in folded elastic ribbons via tunable pitchfork bifurcations

## 0. 读取说明
- 源 PDF：`jmps\文献\Programmable-symmetry-breaking-in-folded-elasti_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps\文本\txt\Programmable-symmetry-breaking-in-folded-elasti_2026_Journal-of-the-Mechanic.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 能支持全文语义、图注、章节和公式附近文字，但不能可靠判断曲线细节、误差条、颜色条、三维形态和局部图像。
- 本文类型：常规 JMPS 研究论文；本文件按 0-19 深度模板拆解。上一轮 `jmps/拆解/papers` 仅作为事实校验底稿，本轮重新组织为“细致拆解 + 写作素材”。

## 1. 基本信息与论文身份
- 题名：Programmable symmetry-breaking in folded elastic ribbons via tunable pitchfork bifurcations
- 作者/机构：Weicheng Huang 等；完整机构见 PDF 首页。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106654. doi:10.1016/j.jmps.2026.106654
- DOI：10.1016/j.jmps.2026.106654
- 关键词：Elastic ribbon,Pitchfork bifurcation,Programmable symmetry-breaking,Discrete simulation,Toy model
- 研究对象：带局部折痕的弹性 ribbon，在轴向压缩和横向剪切下的对称破缺/保持路径
- 研究尺度：从具体材料/结构/图像对象进入机制、模型或设计规则；章节标题包括：1. Introduction；2. Model and methodology；2.1. Problem setup；2.2. Experimental setup；2.3. Anisotropic rod model；2.4. Discrete diﬀerential geometry (DDG) framework；3. Results；3.1. Spontaneous symmetry-breaking in continuous ribbons；3.2. Programming bifurcations via a single fold；3.3. Interaction and complexity in multi-fold systems；4. Theoretical analysis: low-dimensional toy model；5. Discussion and conclusion；Appendix A. Symmetry of the two modes；Appendix B. Convergent study；Appendix C. Supplementary Video；References
- 方法类型：桌面实验、各向异性 rod model、离散微分几何 DDG 模拟、特征值稳定性分析、低维质量-弹簧 toy model
- 证据类型：图 1-10 的分岔图、稳定性景观、参数相图、双折痕协同效应与 toy model；补充视频和收敛附录；图像本体需结合 PDF/视频核查
- 目标读者：JMPS 中关注材料机制、本构建模、结构稳定性、图像判据、软物质或工程设计诊断的读者。
- JMPS 风格定位：这篇不是孤立应用报告，而是把一个具体对象提升为可验证的力学问题，并试图输出可迁移的 benchmark、机制解释、判据或设计规则。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要通常按“背景/传统理解 -> 未解决 gap -> 本文方法 -> 关键发现 -> 意义”推进。它的强处是让读者在第一页就知道本文改变了什么判断。
- 背景句承担什么：建立对象的重要性，给读者一个进入 JMPS 问题的理由，而不是泛泛科普。
- gap 句承担什么：指出现有测试、模型、判据或实验只能看到一部分，不能回答本文真正关心的状态、路径、局部场或统计性质。
- 方法句承担什么：说明作者如何隔离变量、构造模型、扫描参数或提取图像特征，使 gap 变成可回答问题。
- 结果句承担什么：用少量定量结果或清晰转变支撑主张，让 contribution 不停留在“提出方法”。
- 意义句承担什么：把结果翻译成更广义的本构、设计、分类或机制价值。
- 一句话主张：把实验演示、数值追踪和低维物理解释串成闭环。
- 3-5 个核心关键词：Elastic ribbon,Pitchfork bifurcation,Programmable symmetry-breaking,Discrete simulation,Toy model

## 3. 选题层深拆
- 问题来源：- 问题来源：细长结构的屈曲/分岔在功能结构中有用，但对称破缺常对微小扰动敏感，路径选择不可控。 - 为什么重要：软机器人、机械逻辑、可展开结构需要确定性形变，而不是“偶然屈曲”。 - 研究边界：弹性 ribbon，局部折痕角作为 tuner；主要讨论准静态平衡和形态路径，不是材料失效。 - JMPS 取向：把经典 pitchfork bifurcation 与可编程几何缺陷连接，强调稳定性拓扑而不只是形状演示。
- 问题为什么重要：重要性不只来自对象本身，还来自该对象暴露出的通用困难：常规实验混合多个过程，结构失稳路径难以控制，本构变量和微机制脱节，传统判据过强，或全局性能无法揭示局部风险。
- 问题为什么现在值得做：当前实验、数值、图像处理和物理约束学习工具足以把过去只能定性描述的现象转成可度量证据。
- 问题边界：边界被限定在本文材料、结构、加载、图像或数据窗口中。这个边界让证据链闭合，也意味着不能无条件外推到所有同类系统。
- 选题的 JMPS 味道：把一个具体系统写成“机制/模型/判据/设计规则”问题，而不是只报告工程性能。
- 选题可迁移性：可学的是重新切分对象和证据的动作：先找被传统观察遮蔽的层次，再设计能直接暴露该层次的实验或模型。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：- 既有版图：细长结构大变形、屈曲、origami 折痕力学、FEA/DDG 模拟、数值 continuation 和 reduced-order model。 - 作者制造的 gap：折痕常被作为铰链或折叠运动学元素研究，但“局部几何奇异性如何重塑全局分岔拓扑”研究不足。 - gap 类型：机制 gap + 控制策略 gap。 - gap 是否成立：成立。文献链从 instability-driven functionality 转到 deterministic control，再指出 creases 与 global stability landscape 的联系缺失。
- 主要研究流派/方法路线：可分为经典理论或经验观察、现代实验/数值/图像工具、以及应用牵引的设计或预测需求三类。
- 每类研究解决了什么：经典文献提供概念和基本方程；方法文献提供实现路径；近年应用文献提供为什么需要更强预测能力的动机。
- 每类研究留下什么不足：不足通常在交叉处：已有研究能解释现象 A 或预测量 B，但不能隔离本文关心的状态、局部场、相图边界、统计判据或 feature 依赖。
- 本文站在哪条线上：本文站在已有工具之后，强调把工具组织成一个能回答具体 gap 的闭环。
- 最接近前人工作：上一轮底稿指出了相邻经典和近年工作；深度阅读时应重点核查 Introduction 中最接近方法是否被公平比较。
- 是否公平处理前人：总体是“继承 + 补足”的写法，很少直接贬低前人，这符合 JMPS 对累积性贡献的偏好。

## 5. Gap 制造机制
- 明示 gap：折痕常被作为铰链或折叠运动学元素研究，但“局部几何奇异性如何重塑全局分岔拓扑”研究不足。
- 隐含 gap：如果不引入本文框架，读者只能得到现象描述或经验拟合，无法知道背后的状态变化、稳定性拓扑、微结构竞争、对称判据、成分调制或局部风险。
- gap 类型：对象 gap、机制 gap、方法 gap、数值 gap、判据 gap 或设计诊断 gap。
- gap 证据来自哪里：来自文献分组、baseline 对比、方法必要性和图表结果的递进。
- gap 是否足够窄：较窄；它被收束到具体材料、结构、参数、图像或器件，而非泛泛宣称领域空白。
- gap 是否足够重要：足够重要，因为解决后能产生可迁移的模型、实验基准、相图、图像指标或设计 workflow。
- 如果我是审稿人会如何追问：最可能追问最接近前人是否遗漏、参数窗口是否太小、机制证据是否直接、图像和误差是否支撑强 claim。

## 6. 创新性判断
- 作者声称的贡献：证明单折痕将超临界 pitchfork 转为 imperfect bifurcation；给出临界边界；双折痕以更小角度抑制对称破缺；toy model 提炼能量竞争。
- 我判断的真实创新：不是“折痕影响形状”本身，而是把折痕强度、稳定分支、特征值和相图合成一个可编程分岔语言。
- 创新类型：机制解释 + 设计规则 + 多方法验证。
- 创新强度：中高。对可编程结构设计有清晰迁移价值。
- 创新必要性：必要性来自 gap：没有本文的隔离、调谐、正则化、判据或局部场解析，就无法支撑主张。
- 创新与证据匹配度：核心 claim 有图表支撑；外推性意义需要按作者给出的边界理解。
- 容易被挑战的创新点：toy model 简化强；实验参数范围有限；DDG 与真实折痕材料非理想性之间仍有差距。

## 7. 论证链条复原
用 `背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义` 复原：可编程结构需要控制分岔路径 -> pristine ribbon 在压缩-剪切下出现 pitchfork，对称分支选择受扰动影响 -> 引入局部折痕作为几何偏置 -> 实验和 DDG 都显示分岔图由对称双分支变为主稳定分支，折痕足够大时全程保持构型旋转对称 -> 特征值与相图给出对称破缺/保持临界边界 -> 双折痕存在协同作用，更小折角即可稳定路径 -> toy model 说明本质是局部几何偏置与全局压缩失稳之间的能量竞争。

深度拆解看，这条链的关键是“每一步让下一步不可避免”。背景给重要性，文献给已有能力，gap 给必要性，方法给可验证路径，图表给证据，Discussion 再把证据转成机制或设计语言。写作时可以模仿这种递进，但不能省略 baseline，否则创新会显得悬空。

## 8. 方法/理论/模型细拆
- 方法总框架：实验平台记录 ribbon 形态；DDG 通过离散能量最小化捕捉大转动和局部弯曲奇异；稳定性通过 Hessian/eigenvalue 判断；toy model 用少量自由度解释分岔拓扑。
- 关键概念：Elastic ribbon,Pitchfork bifurcation,Programmable symmetry-breaking,Discrete simulation,Toy model
- 关键变量/参数：从 TXT 可见的变量包括章节标题、公式附近符号、图注中的控制参数和输出指标；完整符号表需结合 PDF 核查。
- 核心假设：折痕可用局部几何约束/角度参数代表；准静态平衡足以描述主要路径；DDG 能忠实捕捉 ribbon bending/twisting。
- 边界条件：本文只对其测试/模拟/图像/数据范围内的 claim 最可靠。
- 方法步骤：先定义对象和 baseline，再引入本文方法，随后做对比、参数扫描或验证，最后讨论机制与边界。
- 复现信息：TXT 足以提取方法逻辑，但完整复现需要 PDF 图、参数表、补充材料、代码/数据可用性说明。
- 方法复杂度是否合理：合理，因复杂度对应 gap；但写作时要防止公式或网络/数值细节压倒问题主线。
- 方法与 gap 的对应关系：本文方法不是装饰，而是为了看见传统路径看不到的那一层证据。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 把实验演示、数值追踪和低维物理解释串成闭环。 | 摘要/结论 | 摘要主张、核心图表、Discussion 收束共同支撑 | 综合证据 | 中强 | 折痕角、材料刚度、边界条件和摩擦等实验细节是否足够控制；fold “tuner strength”是否能推广。 |
| 不是“折痕影响形状”本身，而是把折痕强度、稳定分支、特征值和相图合成一个可编程分岔语言。 | Introduction/Results | 方法设计与 baseline 对比显示本文并非单纯重复已有工作 | 方法+对比 | 中强 | 需确认最接近前人是否充分比较 |
| 本文的结果链能够从现象推进到机制或设计规则 | Results/Discussion | 图表按 baseline、核心结果、参数/机制、意义展开 | 图表叙事 | 中强 | 机制有时是推断而非直接观测 |
| 方法复杂度与 gap 基本匹配 | Method/Theory | 实验、数值、理论或网络模块分别对应隔离、预测、分类、调谐或筛查任务 | 方法论证 | 中 | 参数与复现细节需查 PDF |
| 作者主动控制外推边界 | Discussion/Conclusion | 结尾列出材料、载荷、图像、模型或数据窗口限制 | 边界说明 | 强 | 摘要和标题的强表述仍需正文支撑 |
| 图表系统承担主要说服功能 | Figures/Tables | 图注和正文显示多图共同完成对象、方法、结果、机制、应用的分工 | 视觉证据 | 中强 | 图像本体必须核查 |

这张表说明：核心 claim 通常由多种证据共同支撑，而不是只靠一张图。写作时应避免把 Discussion 中的机制推断写成与实验观察同等强度的事实。

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig./Table | Fig. 1. Evolution of equilibrium conﬁgurations and bifurcation behaviour of a folded elastic ribbon. The mechanical transition proceeds through | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 2. Experimental platform and mathematical modeling of folded ribbons. (a) Experimental setup. The system comprises a folded elastic ribbon | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3. Spontaneous symmetry-breaking and supercritical pitchfork bifurcation in continuous ribbons. (a) Bifurcation diagram for a continuous | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 4. Imperfect bifurcation and deterministic path selection via a single fold. (a) Bifurcation diagram for a ribbon with a prescribed fold (𝜙= 30◦ at | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 5. Imperfect bifurcation and deterministic path selection via a single fold with a large angle. (a) Bifurcation diagram for a ribbon with a large | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6(d)). Since the maximum shear satisﬁes | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6. Global stability landscape and parameter phase diagram of a ribbon with a single fold. (a) 3D equilibrium conﬁguration surface showing | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 7. Bifurcation topology and path selection in a dual-fold system. (a) Bifurcation diagram for a ribbon featuring two prescribed folds (𝜙= 20◦ at | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 8. Bifurcation topology and path selection in a dual-fold system with increased fold angle. (a) Bifurcation diagram for a ribbon featuring | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 9. Global stability landscape and parameter phase diagram of a dual-fold ribbon system. (a) 3D equilibrium conﬁguration surface showing | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 10. Low-dimensional toy model and stability analysis. (a) Schematic representation of the mass-spring toy model. The system comprises a | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |

图表顺序服务于论证节奏：先交代对象和方法，再给 baseline，随后展示核心变化，最后用参数图、机制图、误差图或风险图把结果变成可复用规律。由于 TXT 只能读图注，涉及图像本体的判断必须回到 PDF。

## 11. 章节结构与篇章布局
- Abstract：压缩整篇论证，突出反转或新能力。
- Introduction：从广背景快速收束到具体 gap，文献按能力组织。
- Related Work/Background：若没有独立小节，则嵌入 Introduction 与 Method。
- Method/Theory/Model：承担“为什么本文能回答 gap”的技术可信度。
- Results：按 baseline、核心结果、参数/机制、意义推进。
- Discussion：- Abstract：高度概括“fold as geometric tuner”。 - Introduction：从细长结构和功能失稳切入，再聚焦 symmetry-breaking 的随机性，最后提出折痕-全局稳定性 gap。 - Method：先问题设置和实验，再 rod/DDG 数学模型。 - Results：按 pristine -> single fold -> dual fold 递进。 - Theory：toy model 不是主方法，而是解释层，用来把数值结果变成物理图像。 - Discussion/Conclusion：回到机械逻辑、软抓手、航空展开结构等应用。
- Conclusion：把发现收束成可迁移贡献，同时限制外推。
- 章节之间如何过渡：过渡靠问题链，而不是机械地介绍下一节。
- 哪一节最值得模仿：Results 到 Discussion 的转换最值得学，因为它把图表事实变成机制/设计语言。
- 哪一节可能存在结构风险：方法密集小节可能让非本领域读者失去主线，需要流程图和主题句。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Programmable-symmetry-breaking-in-folded-elasti_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：11
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Model and methodology | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Problem setup | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Experimental setup | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Anisotropic rod model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Spontaneous symmetry-breaking in continuous ribbons | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Programming bifurcations via a single fold | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Interaction and complexity in multi-fold systems | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Theoretical analysis: low-dimensional toy model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5 Discussion and conclusion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：对象重要性 -> 既有研究能力 -> 未解 gap -> 本文策略和贡献。
- Method 段落推进：对象定义 -> 变量/方程/实验/算法 -> 实现细节 -> 验证路线。
- Results 段落推进：每段围绕一个图或一个 claim，先给趋势，再给机制解释。
- Discussion/Conclusion 段落推进：先整合结果，再对照文献，最后给边界和迁移价值。
- 常见段落开头方式：`To isolate...`、`We first...`、`Having established...`、`These results suggest...`。
- 常见段落收束方式：用 `Together`、`This indicates`、`These findings` 把事实收束到机制。
- 可复用段落模板：`传统理解/基线 -> 本文操作 -> 图中差异 -> 机制解释 -> 对模型或设计的启发`。

## 13. 文笔画像与语言习惯
- 整体语气：- 整体语气：强机制、强设计导向，常把几何缺陷写成主动调控工具。 - 常用问题表达：`stochasticity`, `extreme sensitivity`, `deterministic control` - 常用贡献表达：`reshapes the stability topology`, `maps the global stability landscape` - 常用机制表达：`nonlinear coupling between localized geometric singularities and global buckling modes` - 常用限定表达：toy model 部分明确说 simplicity 是 strength 也是 limitation。 - 可复用句式：`X functions not merely as a defect but as an active tuner of Y.`
- claim 强度：核心范围内强，外推处谨慎。
- 谨慎表达：常用 `suggest`, `consistent with`, `over the explored range`, `relative`, `first-order`, `requires further validation`。
- 问题表达：强调“现有方法遮蔽/无法解析/判据不适用”，比简单说“缺少研究”更高级。
- 贡献表达：把贡献写成能力，如 isolate、recast、reshape、capture、detect、predict、screen、enable。
- 机制表达：常通过 transition、competition、coupling、state、landscape、hotspot、feature dependency 组织。
- 对比表达：baseline 对比是文笔骨架。
- 限定边界表达：Discussion/Conclusion 主动承认限制。
- 术语密度：高，但围绕少数核心术语重复。
- 长句/短句习惯：方法段长句多，结果主题句较短。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：ribbon(81)；bifurcation(64)；fold(60)；stability(56)；con(52)；system(41)；stable(40)；shear(39)；geometric(38)；huang(34)；experimental(32)；symmetry(32)；angle(30)；branch(29)；two(28)；continuous(26)；symmetry-breaking(25)；localized(25)；landscape(25)；boundary(25)
- 高频学术名词：bifurcation(64)；stability(56)；deformation(44)；system(41)；transition(40)；analysis(34)；model(24)；displacement(24)；guration(22)；energy(20)；parameter(14)；instability(14)；ness(14)；condition(12)；response(12)；solution(12)
- 高频学术动词：shown(7)；shows(5)；capture(3)；demonstrate(3)；develop(3)；indicates(3)；suggests(2)；captured(2)；compared(2)；developed(2)；solve(2)；indicate(2)；validated(1)；formulated(1)；derive(1)；investigate(1)
- 高频形容词：stable(80)；experimental(64)；numerical(46)；elastic(44)；unstable(40)；geometric(38)；critical(30)；global(28)；continuous(26)；boundary(25)；symmetric(25)；primary(24)；displacement(24)；deterministic(19)；asymmetric(19)；rotational(17)
- 高频副词/连接副词：ectively(9)；consequently(8)；fundamentally(6)；cantly(6)；initially(6)；highly(5)；however(4)；systematically(4)；finally(4)；audoly(4)；cally(4)；respectively(4)；rotationally(4)；strictly(4)；eventually(4)；merely(3)
- 高频二词短语：con guration(21)；stability landscape(19)；con gurations(18)；geometric bias(17)；pitchfork bifurcation(14)；sti ness(14)；rotational symmetry(13)；transverse shear(13)；experimental snapshots(13)；fold angle(12)；shear displacement(12)；bifurcation diagram(11)；single fold(11)；primary stable(10)；localized fold(9)；toy model(9)
- 高频三词短语：supercritical pitchfork bifurcation(8)；primary stable branch(7)；global stability landscape(7)；plotted against shear(6)；against shear displacement(6)；solid black lines(6)；stable branches gray(6)；con gurational rotational(5)；gurational rotational symmetry(5)；minimum eigenvalue min(5)；vertical displacement plotted(5)；displacement plotted against(5)

**主动、被动与句法**

- 被动语态估计次数：103
- `we + 动作动词` 主动句估计次数：9
- 名词化表达估计次数：860
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：185
- 一般过去时线索：14
- 现在完成时线索：12
- 情态动词线索：31
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：symmetry-breaking(5)；programmable(4)；bifurcation(4)；localized(4)；fold(4)；pitchfork(3)；stability(3)；geometric(3)
- 1. Introduction：huang(12)；bifurcation(9)；wang(7)；localized(7)；ribbon(6)；con(6)；elastic(5)；numerical(5)
- 2. Model and methodology：无明显高频项
- 2.1. Problem setup：ribbon(9)；symmetry(8)；fold(6)；con(4)；shear(4)；prescribed(3)；two(3)；guration(3)
- 2.2. Experimental setup：ribbon(5)；experimental(3)；precise(3)；elastic(3)；geometric(3)；platform(2)；two(2)；programmable(2)
- 2.3. Anisotropic rod model：ribbon(12)；boundary(12)；moment(7)；frame(7)；equilibrium(7)；equations(6)；huang(6)；elastic(5)
- 3. Results：bifurcation(3)；shear(3)；section(2)；numerical(2)；ribbon(2)；folds(2)；normalized(2)；present(1)
- 3.1. Spontaneous symmetry-breaking in continuous ribbons：con(7)；bifurcation(7)；ribbon(5)；experimental(4)；pitchfork(4)；stable(4)；stability(4)；numerical(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：先承认已有进展，再指出关键对象仍被混淆、不可测、不可控或判据不适用。
- 可复用句型骨架：`Although X has been extensively studied, Y remains unresolved because Z.`
- 中文写作启发：gap 要写“为什么现有方法看不到”，不要只写“研究较少”。
### 14.2 方法与框架表达
- 原文表达模式：`To decouple/capture/detect/control X, we combine A with B.`
- 可复用句型骨架：`We first establish a baseline, then introduce X to quantify Y.`
- 中文写作启发：方法模块要和 gap 一一对应。
### 14.3 结果与趋势表达
- 原文表达模式：先总体趋势，再关键定量，再与 baseline 比较。
- 可复用句型骨架：`Increasing X shifts the response from A to B, while C remains nearly unchanged.`
- 中文写作启发：结果要提炼成转变、边界或权衡。
### 14.4 机制解释表达
- 原文表达模式：`This behavior can be attributed to...` / `These observations suggest...`
- 可复用句型骨架：`The competition between X and Y governs the transition from A to B.`
- 中文写作启发：机制推断要和证据强度匹配。
### 14.5 贡献与意义表达
- 原文表达模式：贡献被写成新能力，而非仅“提出模型”。
- 可复用句型骨架：`This work recasts X from Y into Z and provides a framework for A.`
- 中文写作启发：让读者知道读完后能做什么。
### 14.6 局限与未来工作表达
- 原文表达模式：主动限定窗口、模型和数据。
- 可复用句型骨架：`The present study focuses on X; extending it to Y requires Z.`
- 中文写作启发：局限写得好，会保护主 claim。

## 15. 引用策略与文献使用
- 引用密度：- 引用密度：Introduction 高，Method 中引用 DDG/rod 模型，Discussion 引功能结构应用。 - 文献组织：细长结构经典力学 -> instability-driven applications -> symmetry-breaking control -> crease/origami mechanics -> DDG 与 reduced-order model。 - 引用姿态：对前人多为“奠基/提供工具”，gap 放在“crease 与 global stability landscape 交互未充分研究”。 - 引用偏好：经典书/综述与 2024-2026 近作并存，显得问题很前沿。
- 引用主要集中位置：Introduction、Method 选择依据和 Discussion 机制对照。
- 经典文献用途：建立概念合法性和理论基线。
- 近年文献用途：说明应用需求与当前技术窗口。
- 方法文献用途：支撑实验规范、数值方法、图像算法、网络结构或本构模型。
- 对比/批判性引用：多用温和转折，少用直接否定。
- gap 如何靠引用搭建：把已有研究分成“能解决什么/不能解决什么”。
- references 暗示的研究共同体：本文通常跨越固体力学、材料科学、计算方法和具体应用社群。
- 引用风险：若缺少最接近 competitor，审稿人会质疑 gap。

## 16. 审稿人视角风险
- 最大攻击面：- 最容易被质疑：折痕角、材料刚度、边界条件和摩擦等实验细节是否足够控制；fold “tuner strength”是否能推广。 - claim 与证据匹配：对本系统的路径控制证据充足；对“new generation of systems”属于展望。 - 方法风险：DDG 参数、折痕离散化、双折痕空间相互作用可能对结果敏感。 - 需进一步核查：图 4-9 的分岔分支和相图边界最好结合 PDF 图像确认；补充视频能支撑实验-模拟相似性。
- claim 是否过强：核心范围内可接受；标题和摘要中的广义意义需靠正文限定。
- 证据是否不足：宏观或数值证据较足，微观/真实工况/长期循环/多材料泛化可能不足。
- 方法是否可复现：需要 PDF、补充材料和参数表进一步核查。
- 对比是否充分：baseline 有，但最接近前人对比需重点检查。
- 边界条件是否清楚：正文通常清楚，摘要较强。
- 替代解释是否排除：部分机制仍可能存在替代解释。
- 图表是否需要进一步核查：需要，尤其所有图像本体。

## 17. 可复用资产
- 可复用选题角度：- 可复用选题角度：把不可控失稳改造成可编程稳定性景观。 - 可复用论证套路：经典分岔基线 -> 几何缺陷引入 -> 分岔拓扑改变 -> 参数相图 -> 低维模型解释。 - 可复用写法：用 `tuner`, `landscape`, `topological shift`, `energy competition` 把工程现象提升成力学机制。 - 可复用图表：分岔图 + 3D 稳定性景观 + 参数相图 + toy model 四件套。 - 不宜直接模仿：没有稳定性分析时，不要只凭形态照片宣称“重塑分岔拓扑”。
- 可复用 gap 制造方式：从传统方法遮蔽的层次入手。
- 可复用论证链：baseline -> intervention/framework -> evidence -> mechanism -> boundary。
- 可复用图表设计：对象图、方法图、核心曲线、参数/相图、机制示意、边界/风险图。
- 可复用段落结构：主题句 + 图中事实 + 机制解释 + 下一步引导。
- 可复用句型骨架：`X is often viewed as Y; here we show that Z.`
- 可复用引用组织：文献按能力分组。
- 不宜直接模仿之处：没有直接证据时不要模仿强反转标题。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：- 最值得学习：把实验演示、数值追踪和低维物理解释串成闭环。 - 最大风险：从特定 ribbon 折痕到普适结构设计的外推。 - 可迁移三件事：先建立无缺陷基线；用参数相图表达设计边界；用 toy model 给复杂模拟一个可讲的物理核。
- 可以迁移到 Introduction 的写法：先把大问题收窄到一个可测/可算/可判定 gap。
- 可以迁移到 Method 的写法：每个方法模块都对应一个 claim。
- 可以迁移到 Results/Discussion 的写法：Results 讲证据，Discussion 讲机制和边界。
- 需要避免的问题：不要把特定系统结论外推成普遍定律；不要让复杂方法掩盖问题链。

## 19. 最终浓缩
- 这篇论文最值得学：把实验演示、数值追踪和低维物理解释串成闭环。
- 这篇论文最大风险：从特定 ribbon 折痕到普适结构设计的外推。
- 三个可迁移动作：建立 baseline；设计直接对准 gap 的方法；把图表结果翻译成机制、判据或设计规则，并明确边界。
