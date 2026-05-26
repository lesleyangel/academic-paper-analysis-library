# The mechanics and physics of tofu: Understanding hydrated soft solids through feature networks

## 0. 读取说明
- 源 PDF：`jmps\文献\The-mechanics-and-physics-of-tofu--Understandin_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps\文本\txt\The-mechanics-and-physics-of-tofu--Understandin_2026_Journal-of-the-Mechanic.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 能支持全文语义、图注、章节和公式附近文字，但不能可靠判断曲线细节、误差条、颜色条、三维形态和局部图像。
- 本文类型：常规 JMPS 研究论文；本文件按 0-19 深度模板拆解。上一轮 `jmps/拆解/papers` 仅作为事实校验底稿，本轮重新组织为“细致拆解 + 写作素材”。

## 1. 基本信息与论文身份
- 题名：The mechanics and physics of tofu: Understanding hydrated soft solids through feature networks
- 作者/机构：Birte Boes 等；完整机构见 PDF 首页。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213 (2026) 106632. doi:10.1016/j.jmps.2026.106632
- DOI：10.1016/j.jmps.2026.106632
- 关键词：Inelasticity,Viscoelasticity,Poroelasticity,Automated model discovery,Feature network,Food,Tofu
- 研究对象：silken、firm、extra-firm tofu 的非线性黏弹/孔黏弹行为及水含量依赖性
- 研究尺度：从具体材料/结构/图像对象进入机制、模型或设计规则；章节标题包括：1. Introduction；2. Mechanical testing；3. Physics-based model；4. Neural network model；5. Results；6. Discussion；Appendix A. Errors of discovered individual and uniﬁed models；Appendix B. Preliminary sensitivity analyses；References
- 方法类型：百余次压缩测试、三次压缩训练/双次压缩测试、有限黏弹理论、inelastic constitutive neural networks、feature network
- 证据类型：图 8-9 实验应变/应力历史；图 10、16 预测与实验对比；图 11-13 网络权重；图 14 弹性/非弹性分解；图 15 水含量调制；附录敏感性分析
- 目标读者：JMPS 中关注材料机制、本构建模、结构稳定性、图像判据、软物质或工程设计诊断的读者。
- JMPS 风格定位：这篇不是孤立应用报告，而是把一个具体对象提升为可验证的力学问题，并试图输出可迁移的 benchmark、机制解释、判据或设计规则。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要通常按“背景/传统理解 -> 未解决 gap -> 本文方法 -> 关键发现 -> 意义”推进。它的强处是让读者在第一页就知道本文改变了什么判断。
- 背景句承担什么：建立对象的重要性，给读者一个进入 JMPS 问题的理由，而不是泛泛科普。
- gap 句承担什么：指出现有测试、模型、判据或实验只能看到一部分，不能回答本文真正关心的状态、路径、局部场或统计性质。
- 方法句承担什么：说明作者如何隔离变量、构造模型、扫描参数或提取图像特征，使 gap 变成可回答问题。
- 结果句承担什么：用少量定量结果或清晰转变支撑主张，让 contribution 不停留在“提出方法”。
- 意义句承担什么：把结果翻译成更广义的本构、设计、分类或机制价值。
- 一句话主张：把“好玩对象”写成严肃本构 benchmark 的能力。
- 3-5 个核心关键词：Inelasticity,Viscoelasticity,Poroelasticity,Automated model discovery,Feature network,Food,Tofu

## 3. 选题层深拆
- 问题来源：- 问题来源：食品 texture profile analysis 常停留在经验指标，缺少材料科学意义上的可解释本构模型。 - 为什么重要：替代蛋白、食品质构设计、 hydrated soft solids 的本构发现都需要把成分和力学联系起来。 - 研究边界：主要是受限压缩；加载速率范围较小；水被作为单一标量 feature，未区分 bound/immobilized/free water。 - JMPS 取向：用看似日常的 tofu 承载严肃的非线性软物质本构问题，写法有强记忆点。
- 问题为什么重要：重要性不只来自对象本身，还来自该对象暴露出的通用困难：常规实验混合多个过程，结构失稳路径难以控制，本构变量和微机制脱节，传统判据过强，或全局性能无法揭示局部风险。
- 问题为什么现在值得做：当前实验、数值、图像处理和物理约束学习工具足以把过去只能定性描述的现象转成可度量证据。
- 问题边界：边界被限定在本文材料、结构、加载、图像或数据窗口中。这个边界让证据链闭合，也意味着不能无条件外推到所有同类系统。
- 选题的 JMPS 味道：把一个具体系统写成“机制/模型/判据/设计规则”问题，而不是只报告工程性能。
- 选题可迁移性：可学的是重新切分对象和证据的动作：先找被传统观察遮蔽的层次，再设计能直接暴露该层次的实验或模型。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：- 既有版图：食品科学有 texture profile analysis；软材料有黏弹/孔弹理论；数据驱动力学有 constitutive neural networks。 - 作者制造的 gap：食品实验指标不能解释底层机制；已有自动本构发现多集中于弹性，少有能处理 hydrated food 的非弹性、水含量调制统一模型。 - gap 类型：应用对象 gap + 方法扩展 gap + 可解释性 gap。 - gap 是否成立：成立。作者用豆腐的两成分简单性和十倍应力变化强化“成分-力学映射”问题。
- 主要研究流派/方法路线：可分为经典理论或经验观察、现代实验/数值/图像工具、以及应用牵引的设计或预测需求三类。
- 每类研究解决了什么：经典文献提供概念和基本方程；方法文献提供实现路径；近年应用文献提供为什么需要更强预测能力的动机。
- 每类研究留下什么不足：不足通常在交叉处：已有研究能解释现象 A 或预测量 B，但不能隔离本文关心的状态、局部场、相图边界、统计判据或 feature 依赖。
- 本文站在哪条线上：本文站在已有工具之后，强调把工具组织成一个能回答具体 gap 的闭环。
- 最接近前人工作：上一轮底稿指出了相邻经典和近年工作；深度阅读时应重点核查 Introduction 中最接近方法是否被公平比较。
- 是否公平处理前人：总体是“继承 + 补足”的写法，很少直接贬低前人，这符合 JMPS 对累积性贡献的偏好。

## 5. Gap 制造机制
- 明示 gap：食品实验指标不能解释底层机制；已有自动本构发现多集中于弹性，少有能处理 hydrated food 的非弹性、水含量调制统一模型。
- 隐含 gap：如果不引入本文框架，读者只能得到现象描述或经验拟合，无法知道背后的状态变化、稳定性拓扑、微结构竞争、对称判据、成分调制或局部风险。
- gap 类型：对象 gap、机制 gap、方法 gap、数值 gap、判据 gap 或设计诊断 gap。
- gap 证据来自哪里：来自文献分组、baseline 对比、方法必要性和图表结果的递进。
- gap 是否足够窄：较窄；它被收束到具体材料、结构、参数、图像或器件，而非泛泛宣称领域空白。
- gap 是否足够重要：足够重要，因为解决后能产生可迁移的模型、实验基准、相图、图像指标或设计 workflow。
- 如果我是审稿人会如何追问：最可能追问最接近前人是否遗漏、参数窗口是否太小、机制证据是否直接、图像和误差是否支撑强 claim。

## 6. 创新性判断
- 作者声称的贡献：百余次 controlled compression；发现三类 tofu 的稀疏非弹性本构；引入 water-content feature network；开源代码。
- 我判断的真实创新：把水含量作为调制网络权重的 feature，而不是简单体积分数线性加权；发现弹性由第二等容不变量主导，耗散由第二和第三偏应力不变量主导。
- 创新类型：实验基准 + physics-informed ML + 机制解释。
- 创新强度：中高。对象新颖但不是噱头，方法和解释能迁移到水合软材料。
- 创新必要性：必要性来自 gap：没有本文的隔离、调谐、正则化、判据或局部场解析，就无法支撑主张。
- 创新与证据匹配度：核心 claim 有图表支撑；外推性意义需要按作者给出的边界理解。
- 容易被挑战的创新点：压缩数据能否唯一识别三维本构；feature 只有三个水含量点；“discover”一词容易被认为过强。

## 7. 论证链条复原
用 `背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义` 复原：豆腐由大豆和水组成却表现复杂质构 -> 食品质构指标无法提供本构机制 -> 作者对三种水含量 tofu 做多速率多幅值压缩 -> 实验显示强非线性、应力松弛和水含量小变化导致十倍应力差 -> 物理约束非弹性网络拟合训练/测试数据并分解弹性与非弹性贡献 -> 稀疏网络显示三类 tofu 共享功能形式但参数随水含量变 -> feature network 学习水含量到网络权重的非线性映射 -> 统一模型预测不同 tofu，说明高度水合软固体需要非线性 poroviscoelastic 描述。

深度拆解看，这条链的关键是“每一步让下一步不可避免”。背景给重要性，文献给已有能力，gap 给必要性，方法给可验证路径，图表给证据，Discussion 再把证据转成机制或设计语言。写作时可以模仿这种递进，但不能省略 baseline，否则创新会显得悬空。

## 8. 方法/理论/模型细拆
- 方法总框架：机械测试 -> 物理本构设定 -> elastic/dissipative neural networks -> synthetic derivative training data -> individual models -> water-content unified feature model。
- 关键概念：Inelasticity,Viscoelasticity,Poroelasticity,Automated model discovery,Feature network,Food,Tofu
- 关键变量/参数：从 TXT 可见的变量包括章节标题、公式附近符号、图注中的控制参数和输出指标；完整符号表需结合 PDF 核查。
- 核心假设：非弹性变形各向同性且体积保持；体积变化属于弹性部分；压缩主导 chewing 相关行为；水含量可作为单标量特征。
- 边界条件：本文只对其测试/模拟/图像/数据范围内的 claim 最可靠。
- 方法步骤：先定义对象和 baseline，再引入本文方法，随后做对比、参数扫描或验证，最后讨论机制与边界。
- 复现信息：TXT 足以提取方法逻辑，但完整复现需要 PDF 图、参数表、补充材料、代码/数据可用性说明。
- 方法复杂度是否合理：合理，因复杂度对应 gap；但写作时要防止公式或网络/数值细节压倒问题主线。
- 方法与 gap 的对应关系：本文方法不是装饰，而是为了看见传统路径看不到的那一层证据。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 把“好玩对象”写成严肃本构 benchmark 的能力。 | 摘要/结论 | 摘要主张、核心图表、Discussion 收束共同支撑 | 综合证据 | 中强 | 仅靠压缩能否识别完整三维不变量依赖；三个水含量点支撑 feature network 是否偏少。 |
| 把水含量作为调制网络权重的 feature，而不是简单体积分数线性加权；发现弹性由第二等容不变量主导，耗散由第二和第三偏应力不变量主导。 | Introduction/Results | 方法设计与 baseline 对比显示本文并非单纯重复已有工作 | 方法+对比 | 中强 | 需确认最接近前人是否充分比较 |
| 本文的结果链能够从现象推进到机制或设计规则 | Results/Discussion | 图表按 baseline、核心结果、参数/机制、意义展开 | 图表叙事 | 中强 | 机制有时是推断而非直接观测 |
| 方法复杂度与 gap 基本匹配 | Method/Theory | 实验、数值、理论或网络模块分别对应隔离、预测、分类、调谐或筛查任务 | 方法论证 | 中 | 参数与复现细节需查 PDF |
| 作者主动控制外推边界 | Discussion/Conclusion | 结尾列出材料、载荷、图像、模型或数据窗口限制 | 边界说明 | 强 | 摘要和标题的强表述仍需正文支撑 |
| 图表系统承担主要说服功能 | Figures/Tables | 图注和正文显示多图共同完成对象、方法、结果、机制、应用的分工 | 视觉证据 | 中强 | 图像本体必须核查 |

这张表说明：核心 claim 通常由多种证据共同支撑，而不是只靠一张图。写作时应避免把 Discussion 中的机制推断写成与实验观察同等强度的事实。

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig./Table | Fig. 1. Five different types of tofu. Extra-ﬁrm, ﬁrm, medium, soft, and silken tofu illustrate how small changes in composition and processing | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Table 1 | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 2, right, illustrates a representative sample inside a cylindrical chamber, mounted in the rheometer, to perform compression tests | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 2. Mechanical testing. Preparation of cylindrical samples; triple compression test for training; double compression test for testing; and rheome- | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3 visualizes the architecture of both elastic networks that a priori satisfy the thermodynamic requirements of polyconvexity, | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3. Elastic networks. The elastic networks have two hidden layers with 5 and 9 nodes per layer. The feed forward networks take the invariants | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 4 visualizes the architecture of the dissipative network that a priori satisﬁes thermodynamic consistency by remaining | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 5 schematically visualizes the architecture of the feature network. To a priori ensures non-negative, non-zero-valued outputs | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6 illustrates the coupling between one of the three mechanical networks and the feature network. The mechanical networks | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 4. Dissipative network. The dissipative network has three hidden layers with 18, 8, and 8 nodes per layer. It take the invariants of the Mandel | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 5. Feature network. The feature network has three hidden layers with 𝑘× 4 nodes per layer. It takes the feature 𝛼, in our case the scalar-valued | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6. Coupling of mechanical and feature networks. The mechanical network from Figs. 3 or 4 receives a strain- or stress-like input 𝐀 and the | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |

图表顺序服务于论证节奏：先交代对象和方法，再给 baseline，随后展示核心变化，最后用参数图、机制图、误差图或风险图把结果变成可复用规律。由于 TXT 只能读图注，涉及图像本体的判断必须回到 PDF。

## 11. 章节结构与篇章布局
- Abstract：压缩整篇论证，突出反转或新能力。
- Introduction：从广背景快速收束到具体 gap，文献按能力组织。
- Related Work/Background：若没有独立小节，则嵌入 Introduction 与 Method。
- Method/Theory/Model：承担“为什么本文能回答 gap”的技术可信度。
- Results：按 baseline、核心结果、参数/机制、意义推进。
- Discussion：- Abstract：把文化/可持续背景与本构发现并置，记忆点强。 - Introduction：从 tofu 的社会意义到 texture analysis，再到材料建模与自动发现。 - Mechanical testing：清晰交代训练/测试压缩方案。 - Physics-based model 与 Neural network model：先给物理约束，再给可学习架构。 - Results/Discussion：按“实验现象 -> 模型发现 -> invariant 解释 -> water feature”推进。 - Conclusion：回到 tofu 作为 benchmark 和替代蛋白设计。
- Conclusion：把发现收束成可迁移贡献，同时限制外推。
- 章节之间如何过渡：过渡靠问题链，而不是机械地介绍下一节。
- 哪一节最值得模仿：Results 到 Discussion 的转换最值得学，因为它把图表事实变成机制/设计语言。
- 哪一节可能存在结构风险：方法密集小节可能让非本领域读者失去主线，需要流程图和主题句。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-mechanics-and-physics-of-tofu--Understandin_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Mechanical testing | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Physics-based model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Neural network model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 6 Discussion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

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
- 整体语气：- 整体语气：跨界但严肃，善用短句小标题直接给观点，如 `Tofu is a nonlinear viscoelastic material.` - 常用问题表达：`Can we characterize...`, `remains incompletely understood` - 常用贡献表达：`automated model discovery can identify`, `feature network reveals` - 常用机制表达：`autonomously separates elastic and inelastic mechanisms`, `dominated by the second isochoric invariant` - 常用限定表达：Limitations 单独列出五点，控制 ML claim。 - 可复用句式：用“简单材料 + 复杂响应”制造张力：“Made up of only X and Y, it nevertheless...”
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

- Top 高频词：tofu(178)；network(94)；model(89)；stress(72)；water(71)；data(71)；three(60)；dissipative(56)；potential(54)；networks(51)；inelastic(51)；elastic(51)；silken(50)；extra(48)；second(46)；models(44)；equilibrium(44)；feature(43)；neq(43)；content(41)
- 高频学术名词：model(89)；stress(72)；deformation(52)；feature(43)；behavior(37)；analysis(28)；strain(23)；activation(22)；parameters(19)；results(19)；material(17)；response(15)；sensitivity(15)；architecture(14)；regularization(14)；texture(11)
- 高频学术动词：predicted(10)；show(9)；shown(8)；shows(8)；capture(7)；suggest(5)；indicates(4)；indicate(4)；reveal(3)；evaluate(3)；demonstrate(3)；derive(2)；suggests(2)；predict(2)；compared(2)；propose(2)
- 高频形容词：elastic(102)；dissipative(56)；potential(54)；inelastic(51)；experimental(46)；content(41)；mechanical(31)；constitutive(31)；invariant(31)；individual(25)；erent(24)；neural(23)；total(19)；material(17)；viscoelastic(16)；deviatoric(14)
- 高频副词/连接副词：experimentally(20)；notably(12)；accurately(8)；computationally(7)；generally(6)；entirely(6)；cally(6)；autonomously(5)；directly(5)；freely(5)；importantly(4)；exclusively(4)；apply(4)；previously(4)；primarily(3)；highly(3)
- 高频二词短语：water content(40)；extra tofu(30)；dissipative potential(23)；tofu types(22)；right cauchy(19)；feature network(18)；cauchy green(18)；activation functions(18)；silken extra(17)；training data(16)；equilibrium non-equilibrium(16)；dissipative network(16)；model discovery(15)；second third(15)；three tofu(15)；silken tofu(15)
- 高频三词短语：right cauchy green(18)；cauchy green tensor(15)；three tofu types(14)；silken extra tofu(12)；slow medium fast(10)；individual tofu models(9)；second third deviatoric(8)；third deviatoric invariants(8)；neq neq neq(8)；non-equilibrium potential neq(8)；inelastic constitutive neural(7)；constitutive neural networks(7)

**主动、被动与句法**

- 被动语态估计次数：44
- `we + 动作动词` 主动句估计次数：21
- 名词化表达估计次数：673
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：170
- 一般过去时线索：19
- 现在完成时线索：17
- 情态动词线索：30
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：tofu(10)；water(4)；model(4)；hydrated(3)；soft(3)；feature(3)；university(3)；available(2)
- 1. Introduction：tofu(18)；water(12)；constitutive(11)；neural(10)；texture(9)；behavior(9)；models(9)；model(9)
- 2. Mechanical testing：test(9)；three(8)；tofu(8)；compression(7)；hold(7)；loading(6)；uid(6)；sample(6)
- 3. Physics-based model：neq(26)；inelastic(21)；tensor(19)；deformation(16)；elastic(16)；right(11)；cauchy(11)；green(11)
- 4. Neural network model：network(44)；networks(32)；layer(26)；feature(25)；data(24)；dissipative(21)；functions(19)；input(18)
- 5. Results：tofu(45)；silken(23)；stress(21)；extra(21)；model(19)；kpa(17)；potential(16)；three(14)
- 6. Discussion：tofu(76)；model(38)；water(34)；data(33)；stress(30)；network(27)；three(20)；behavior(20)

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
- 引用密度：- 引用密度：Introduction 高，Discussion 根据每个机制小标题引用食品、软组织、ML、本构理论。 - 文献组织：食品科学/TPA -> 软材料力学 -> 数据驱动本构 -> hydrated tissues/poroviscoelasticity。 - 引用姿态：把食品科学指标转译为力学问题，同时用软组织文献支撑方法迁移。 - 引用偏好：Kuhl 团队相关 constitutive ANN 文献较多，但也引用经典 Reese-Simo、Mow、Holzapfel 等。
- 引用主要集中位置：Introduction、Method 选择依据和 Discussion 机制对照。
- 经典文献用途：建立概念合法性和理论基线。
- 近年文献用途：说明应用需求与当前技术窗口。
- 方法文献用途：支撑实验规范、数值方法、图像算法、网络结构或本构模型。
- 对比/批判性引用：多用温和转折，少用直接否定。
- gap 如何靠引用搭建：把已有研究分成“能解决什么/不能解决什么”。
- references 暗示的研究共同体：本文通常跨越固体力学、材料科学、计算方法和具体应用社群。
- 引用风险：若缺少最接近 competitor，审稿人会质疑 gap。

## 16. 审稿人视角风险
- 最大攻击面：- 最容易被质疑：仅靠压缩能否识别完整三维不变量依赖；三个水含量点支撑 feature network 是否偏少。 - claim 与证据匹配：训练/测试数据拟合匹配；“universal across all three tofu types”仅限三类商品 tofu。 - 方法风险：假设体积变化只在弹性部分，未区分三态水；受限边界下流体迁移解释受限。 - 需进一步核查：图 10/16 的 R2、误差分布、图 11-13 权重可解释性需结合 PDF 图像确认。
- claim 是否过强：核心范围内可接受；标题和摘要中的广义意义需靠正文限定。
- 证据是否不足：宏观或数值证据较足，微观/真实工况/长期循环/多材料泛化可能不足。
- 方法是否可复现：需要 PDF、补充材料和参数表进一步核查。
- 对比是否充分：baseline 有，但最接近前人对比需重点检查。
- 边界条件是否清楚：正文通常清楚，摘要较强。
- 替代解释是否排除：部分机制仍可能存在替代解释。
- 图表是否需要进一步核查：需要，尤其所有图像本体。

## 17. 可复用资产
- 可复用选题角度：- 可复用选题角度：用一个低门槛但机制丰富的材料作为 benchmark。 - 可复用论证套路：实验现象强差异 -> 传统线性体积分数解释失败 -> 稀疏物理网络发现功能形式 -> feature network 统一材料族。 - 可复用写法：每个 Discussion 小节标题就是一个 claim，读者可快速抓住贡献。 - 可复用图表：测试流程图；物理约束网络架构图；权重热图；机制分解堆叠曲线；feature-to-weight 曲线。 - 不宜直接模仿：不要把 ML 拟合直接称为物理发现，除非有稀疏结构、物理约束、测试集和限制讨论。
- 可复用 gap 制造方式：从传统方法遮蔽的层次入手。
- 可复用论证链：baseline -> intervention/framework -> evidence -> mechanism -> boundary。
- 可复用图表设计：对象图、方法图、核心曲线、参数/相图、机制示意、边界/风险图。
- 可复用段落结构：主题句 + 图中事实 + 机制解释 + 下一步引导。
- 可复用句型骨架：`X is often viewed as Y; here we show that Z.`
- 可复用引用组织：文献按能力分组。
- 不宜直接模仿之处：没有直接证据时不要模仿强反转标题。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：- 最值得学习：把“好玩对象”写成严肃本构 benchmark 的能力。 - 最大风险：数据维度有限导致本构发现非唯一。 - 可迁移三件事：选择简单但可调的材料族；用 feature 表达成分变化；用 limitations 主动约束 discover 的含义。
- 可以迁移到 Introduction 的写法：先把大问题收窄到一个可测/可算/可判定 gap。
- 可以迁移到 Method 的写法：每个方法模块都对应一个 claim。
- 可以迁移到 Results/Discussion 的写法：Results 讲证据，Discussion 讲机制和边界。
- 需要避免的问题：不要把特定系统结论外推成普遍定律；不要让复杂方法掩盖问题链。

## 19. 最终浓缩
- 这篇论文最值得学：把“好玩对象”写成严肃本构 benchmark 的能力。
- 这篇论文最大风险：数据维度有限导致本构发现非唯一。
- 三个可迁移动作：建立 baseline；设计直接对准 gap 的方法；把图表结果翻译成机制、判据或设计规则，并明确边界。
