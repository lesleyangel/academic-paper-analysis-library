# Evolving particle shape dispersion in crushable granular solids: A continuum breakage mechanics model

## 0. 读取说明
- 源 PDF：`jmps/文献/Evolving-particle-shape-dispersion-in-crushable-g_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/Evolving-particle-shape-dispersion-in-crushable-g_2026_Journal-of-the-Mechan.txt`
- 元数据：`jmps/文本/metadata/Evolving-particle-shape-dispersion-in-crushable-g_2026_Journal-of-the-Mechan.json`
- 读取范围：基于 TXT 中的题名、摘要、关键词、Introduction、方法/理论/模型、结果、讨论/结论、图题图注、附录与参考文献线索进行拆解。
- 图像核查：本文所有涉及曲线形状、图像纹理、颜色尺度、误差带、场分布细节的判断，均需后续结合 PDF 图像核查；本文件只基于 TXT 中可读图注和正文描述。
- 本文类型：连续介质破碎力学扩展论文。它把颗粒形状从平均值或定性描述提升为可演化的统计分布状态变量，并嵌入自由能、耗散势、屈服和压缩响应。

## 1. 基本信息与论文身份
- 题名：Evolving particle shape dispersion in crushable granular solids: A continuum breakage mechanics model
- 作者/机构：Divyanshu Lal; Yang Li; Giuseppe Buscarnera。机构为 Northwestern University 与 Kyushu University。
- 期刊/年份/卷页：Journal of the Mechanics and Physics of Solids, 214 (2026) 106651; DOI: 10.1016/j.jmps.2026.106651
- 关键词：Crushable granular materials; granular shape; shape indices
- 研究对象：可破碎颗粒材料在受限压缩/粉碎过程中粒径分布与形状分布的协同演化，重点是 flatness ratio 与 elongation ratio 的统计分布及其 attractor。
- 方法类型：Continuum Breakage Mechanics 扩展、Shape Evolution Index、形状分布 beta 拟合、自由能/耗散热力学、DEM 合成实验、室内一维压缩实验校准验证。
- 证据类型：Fig.1-4 给形状吸引子和指数定义；Fig.5-7 建立形状描述和强度图谱；Fig.9-10 展示形态和共演化速率对压缩响应/破碎的影响；Fig.12-15 用 DEM 与实验验证；Table 1-4 给符号、参数和校准信息。
- 目标读者：JMPS 的材料力学、连续介质力学、实验力学、计算力学或交叉方法读者；他们关心的不是单个现象是否有趣，而是现象能否被变量、方程、图表和边界条件闭合。
- JMPS 风格定位：这篇文章的价值不是把一个对象介绍一遍，而是把对象放进可验证的力学机制链条中。它具备 JMPS 偏好的三个要素：问题具体、变量可定义、证据能对应 claim。对于写作者而言，最值得关注的是作者如何把“现象”变成“可争辩但可检验的力学命题”。

## 2. 摘要与核心信息提取
- 摘要功能拆解：摘要先交代领域问题和旧方法不足，再用一两个方法动词声明本文做了什么，随后列出最能支撑贡献的结果，最后把意义回收到机制、预测或设计能力上。它不是背景综述式摘要，而是高度压缩的论证链。
- 背景句承担：把研究对象放到更大力学问题中，使读者知道这不是孤立算例。
- gap 句承担：指出已有知识、方法或实验中缺少的关键环节，通常是“已经能观察/模拟/讨论 A，但还不能解释/预测/量化 B”。
- 方法句承担：给出本文的身份标签，说明是实验、理论、数值、贝叶斯、热力学还是量子映射等哪类贡献。
- 结果句承担：用最少的变量表达最强发现，避免把所有图表结果平均铺开。
- 意义句承担：把发现从个案推回到机制理解、设计原则、可计算框架或实验判据。
- 一句话主张：颗粒破碎不仅改变粒径，也把形状分布推向统计吸引子；将形状分布作为连续状态变量嵌入 CBM 后，可以解释不同初始形态和形状共演化速率导致的非单调强度、刚度与耗散差异，并能拟合 DEM 与实验数据。
- 核心关键词：对象变量、状态变量、机制判据、验证闭环、适用边界。
- 摘要可学点：摘要中的强 claim 都有后文图表或公式对应；没有把“重要”写成口号，而是通过可测指标、可推导变量和对照组来体现重要性。

## 3. 选题层深拆
- 问题来源：既有 CBM 成功描述粒径破碎能量，但多把形状作为平均指标或外部描述；已有形状研究又难进入连续本构。缺口是：形状分布如何作为状态变量进入自由能和耗散，并如何随粒径破碎共同演化。
- 为什么重要：该问题牵动的是“局部机制如何决定整体响应”或“复杂对象如何进入连续/可计算/可实验框架”的 JMPS 核心关切。如果不能解决，领域只能停留在经验描述、单次模拟或不可外推的观察。
- 为什么现在值得做：已有文献已经积累了足够的现象、工具和基准，使作者可以把问题收束到一个清晰缺口；同时实验、计算或理论手段已经成熟到足以提供证据闭环。
- 问题边界：本文没有试图解决整个领域全部问题，而是把边界限定在 可破碎颗粒材料在受限压缩/粉碎过程中粒径分布与形状分布的协同演化，重点是 flatness ratio 与 elongation ratio 的统计分布及其 attractor。。这种边界感很重要，因为它让最强结论有明确适用条件。
- JMPS 味道：选题不是“把新工具用到老问题”，而是工具和问题互相需要。方法的复杂度来自缺口本身，而不是为了制造高阶感。
- 可迁移性：如果自己的论文也有类似选题，可以学习其收束方式：先列出已有研究已经做到什么，再指出仍缺哪个变量、哪种边界条件、哪类观测或哪条机制链，最后把本文限定为补上这一个环节。
- 潜在审稿追问：这个 gap 是否真的没有被最近文献处理？本文边界是否过窄以至于意义不足？方法复杂度是否与问题难度匹配？

## 4. 领域位置与文献版图
文献版图先从天然极端破碎、断层 gouge、行星撞击引出 size/shape attractor，再接 Continuum Breakage Mechanics 的经典体系和扩展，最后转到颗粒形状影响宏观性质的相互矛盾证据。作者的站位是整合型：承认 CBM 的能量优势，也承认形状力学文献的丰富现象，但指出二者之间缺少分布层状态变量。

- 作者如何划分已有研究：通常不是按时间简单排队，而是按功能分组：提供基本理论的文献、提供现象证据的文献、提供方法工具的文献、提供最接近对照的文献。
- 每类研究解决了什么：基础理论给术语和守恒/本构/几何合法性；实验或模拟文献证明现象存在；方法文献提供可继承工具；最近工作制造本文 novelty 的直接参照。
- 每类研究留下什么不足：旧理论可能太理想，实验可能只能观察结果，数值可能缺解析或物理解释，跨领域工具可能没有纳入力学边界。
- 本文站在哪条线上：它不是推翻前人，而是在前人交叉处补一个缺少的中介变量、机制判据或可执行框架。
- 是否公平处理前人：从 TXT 可见作者总体采取温和姿态，先承认已有贡献，再指出“not yet address / remains unclear / limited by”这类边界。这样的写法比直接说前人错误更容易被 JMPS 审稿人接受。

## 5. Gap 制造机制
- 显式 gap：既有 CBM 成功描述粒径破碎能量，但多把形状作为平均指标或外部描述；已有形状研究又难进入连续本构。缺口是：形状分布如何作为状态变量进入自由能和耗散，并如何随粒径破碎共同演化。
- 隐含 gap：读者不仅需要知道“还没有人做”，还需要知道“为什么已有工具不能自然解决”。本文的隐含 gap 往往在于缺少能把观测、变量、理论和图表连接起来的中间层。
- gap 类型：方法 gap、机制 gap、尺度桥接 gap、验证 gap 或设计 gap 的组合。强度来自组合后仍然足够窄：它不是泛泛说领域复杂，而是锁定一个可处理的关键变量。
- gap 证据来源：引言中的文献分类、方法部分对旧框架边界的说明、结果部分与基线或对照组的差异共同支撑 gap。
- gap 是否足够窄：足够窄。作者没有声称解决所有材料/结构/算法/物理系统，而是围绕 可破碎颗粒材料在受限压缩/粉碎过程中粒径分布与形状分布的协同演化，重点是 flatness ratio 与 elongation ratio 的统计分布及其 attractor。 建立闭环。
- gap 是否足够重要：重要性来自该 gap 会影响解释、预测、设计或不确定性判断。如果没有本文补充，后续研究会缺少可复用判据或变量。
- 审稿人可能追问：最接近前人是谁？本文与它相比增量在哪里？这个 gap 是概念缺口、数据缺口还是实现缺口？如果只是组合已有工具，组合后的新知识是什么？

## 6. 创新性判断
- 作者声称的贡献：提出 Shape Evolution Index 衡量当前形状分布到 ultimate attractor 的距离，将 flatness/elongation 分布写入自由能与耗散势，并用 coevolution rate 控制形状演化相对于破碎的速度。创新不只在公式，而在把多源形状观测、热力学变量和宏观应力响应串成闭环。
- 我判断的真实创新：真实创新在于把一个分散问题重新组织成可检验结构，而不只是提出一个新名词。最有力的部分是 claim、变量、图表和边界条件之间能互相对上。
- 创新类型：理论/模型创新、方法工作流创新、实验可视化创新、机制判据创新或跨领域映射创新，具体取决于本文主题。
- 创新强度：中高。它不一定在每个子模块上都是世界首次，但在本文组合方式、论证闭环和写作定位上形成了清晰增量。
- 创新必要性：必要性由 gap 支撑。若不引入本文框架，旧研究要么只能给现象描述，要么只能给局部模拟，要么无法处理不确定性/应力/边界/分布等关键环节。
- 创新与证据匹配度：核心创新与图表、公式和验证基本匹配；更广泛的工程外推需要谨慎。
- 容易被挑战的创新点：如果审稿人认为最接近前人已包含类似变量或判据，作者必须证明本文在适用范围、可解释性、验证强度或实际可执行性上有实质增量。

## 7. 论证链条复原
背景：领域中存在一个已被广泛观察或迫切需要解决的力学问题。 -> 文献：已有理论、实验、模拟或算法分别解决了部分环节。 -> gap：既有 CBM 成功描述粒径破碎能量，但多把形状作为平均指标或外部描述；已有形状研究又难进入连续本构。缺口是：形状分布如何作为状态变量进入自由能和耗散，并如何随粒径破碎共同演化。 -> 问题：本文把这个缺口收束为 可破碎颗粒材料在受限压缩/粉碎过程中粒径分布与形状分布的协同演化，重点是 flatness ratio 与 elongation ratio 的统计分布及其 attractor。 的可研究命题。 -> 方法：Continuum Breakage Mechanics 扩展、Shape Evolution Index、形状分布 beta 拟合、自由能/耗散热力学、DEM 合成实验、室内一维压缩实验校准验证。 -> 证据：Fig.1-4 给形状吸引子和指数定义；Fig.5-7 建立形状描述和强度图谱；Fig.9-10 展示形态和共演化速率对压缩响应/破碎的影响；Fig.12-15 用 DEM 与实验验证；Table 1-4 给符号、参数和校准信息。 -> 发现：颗粒破碎不仅改变粒径，也把形状分布推向统计吸引子；将形状分布作为连续状态变量嵌入 CBM 后，可以解释不同初始形态和形状共演化速率导致的非单调强度、刚度与耗散差异，并能拟合 DEM 与实验数据。 -> 机制：作者把结果解释为变量、边界、几何、本构、能量、概率或流体反馈之间的耦合。 -> 意义：该框架为后续设计、预测、实验判据或跨领域计算提供可迁移模板。

这条链的优点是闭合度较高：方法不是孤立技术，图表也不是结果堆砌，而是逐一服务于主张。最薄弱环节通常在外推处：文内证据可以支撑特定对象和条件下的结论，但若推广到更复杂材料、真实工程系统或任意几何/边界，需要更多验证。

## 8. 方法/理论/模型细拆
- 方法总框架：方法的核心是用概率密度 p(si) 表示形状描述符的当前分布，并定义 Shape Evolution Index 为当前分布到 ultimate 分布距离相对于 initial-to-ultimate 距离的归一化度量。自由能由弹性应变能、破碎相关能量和形状相关能量构成；耗散率包含破碎、形状、体积塑性、偏塑性等分量。形状演化通过 c_phi、c_eta 等 coevolution rates 与破碎指数 B 关联，使模型能表达“粒径变化很快但形状变化慢”或相反情形。验证上，作者用 DEM bonded agglomerates 表示不同初始形态，再用实验 rod/plate 系统做校准检验。
- 关键概念：研究对象、状态变量、控制参数、基线模型、对照条件、响应指标和适用边界。
- 关键变量/参数：来自正文的核心变量通常会直接进入图表，而不是只停留在公式中。阅读时应追踪每个变量是否出现在结果图、敏感性分析或验证表中。
- 核心假设：包括材料模型、几何边界、加载方式、统计表示、噪声模型、守恒条件或实验类比条件。假设是本文 claim 成立的地基，不能只当方法细节。
- 边界条件：本文对边界条件的处理决定了结果能否外推。边界越理想化，结论越应写成机制启发而不是工程定律。
- 方法步骤：先定义对象和指标，再建立理论/实验/算法框架，然后设置基线与对照，最后通过多组图表验证主张。
- 复现信息：TXT 中可读出较多样品、参数、算法或公式信息，但完整复现仍需核查 PDF、补充材料、代码/数据可用性以及图像细节。
- 方法复杂度是否合理：总体合理，因为复杂度直接服务于 gap；若移植到自己论文，应确保每个模块都能服务一个明确 claim。
- 方法与 gap 的对应关系：本文最可学的是每个方法模块都有任务分工：有的解决定义问题，有的解决验证问题，有的解决对照问题，有的解决边界问题。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 形状分布在多种破碎场景下趋向共同吸引子 | 引言/2.1 | Fig.1-3 多源数据和 Li et al. 实验 | 中强 | 多源数据可比性和测量方法一致性需审查 |
| Shape Evolution Index 能概括分布到吸引子的演化程度 | 2.2 | Fig.4 定义和双向收敛示意 | 中 | 指数可能压缩分布细节 |
| 形状演化导致 crushing strength 非单调依赖初始形态和吸引子距离 | 摘要/3 | Fig.7 的强度图谱 | 中强 | 预测依赖形状能量函数和参数 |
| 细长/片状密集分布可增强刚度和能量耗散 | 摘要/3.5 | Fig.9-10 和自由能形状项 | 中 | 实验覆盖形态有限 |
| 模型能同时捕捉粒径/形状指标演化和应力-应变响应 | 3.6 | DEM Fig.12-13，实验 Fig.14-15 | 强 | 校准参数数量和泛化性需说明 |
| 形状分布可作为连续状态变量服务颗粒材料设计 | 结论/讨论 | 热力学框架 + 验证案例 | 中 | 工程设计外推仍需更多材料体系 |

- 证据系统总评：本文证据不是单一类型，而是由定义、公式、实验/模拟、参数对照、图表和讨论共同构成。强 claim 通常有多重证据；较弱 claim 多出现在意义外推或工程启发处。
- 证据链写法：先给基线，再给新方法/新现象，再解释差异，最后回到机制。这样的顺序可以避免读者觉得结果只是偶然图形。
- 需要特别警惕：如果某个 claim 只由一张图支持，且该图依赖图像颜色或复杂曲线，则必须在后续 PDF 核查中确认图像本体。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig.1-2 | 多源形状吸引子证据 | 把形状 attractor 从概念变成可视化事实，为状态变量建立必要性 | 需核查不同数据源标记和坐标 |
| Fig.3-4 | 分布收敛和 Shape Evolution Index | 定义本文最关键的中介变量 | 需核查指数计算示意 |
| Fig.5-6 | MVB 形状测量和表面积函数 | 说明 flatness/elongation 如何进入能量函数 | 公式曲面需结合 PDF |
| Fig.7 | crushing strength 在形态平面的预测 | 支撑非单调强度和最佳形状属性 claim | 需核查颜色尺度 |
| Fig.9-10 | 不同形态和共演化速率下的应力、破碎、形状指数 | 展示模型能区分 sphere/rod/plate/blade 响应 | 需核查曲线差异 |
| Fig.12-15 | DEM 和实验验证 | 将理论状态变量落到可观测数据上 | 需核查拟合误差和校准/验证划分 |

- 图表顺序如何服务论证：前几张图通常建立对象、装置、基线或概念；中间图承担模型/机制推导；后几张图负责验证、比较或相图总结。这种排序使读者先相信问题存在，再相信方法必要，最后相信结论有边界。
- 公式功能：公式不是为了展示数学复杂度，而是定义变量、约束边界、连接能量/应力/概率/几何或给出可计算判据。拆解时应问：该公式是否最终进入某张图或某个 claim？如果没有，它可能只是铺垫。
- 结果叙事：结果段落通常不复述图面细节，而是告诉读者图中哪一类趋势支持哪一个 claim。可迁移写法是“Fig. X shows A; compared with B, this indicates C under condition D”。

## 11. 章节结构与篇章布局
文章结构属于“证据先行的模型扩展”：先用 Fig.1-2 证明形状吸引子不是作者自造概念，再提出指数，再嵌入热力学，再给性能预测，最后验证。章节标题从 shape-enhanced breakage mechanics 到 model performance 再到 discussion，逻辑上把“为什么需要形状分布”放在“如何写本构”之前。

- Abstract：问题-方法-结果-意义四段压缩，避免过多背景。
- Introduction：用文献分类制造缺口，而不是简单堆引用。
- Method/Theory/Model：先给框架和变量，再进入公式或实验细节。
- Results：围绕少数核心 claim 排图，每个小节最好只服务一个主张。
- Discussion/Conclusion：把最稳的结果写成结论，把外推写成启发，把未覆盖内容写成未来工作或边界。
- 章节之间如何过渡：作者常用“having established / to address / we next / finally”等阶段性句子，让读者知道论证推进到哪一层。
- 最值得模仿的章节：引言中的 gap 收束和结果中的图表分工。最可能存在结构风险的是方法细节多、跨领域术语多时，读者可能在进入核心 claim 前被公式消耗。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Evolving-particle-shape-dispersion-in-crushable-g_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Shape-enhanced breakage mechanics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Evidence of shape attractor distributions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.2 A shape evolution index for tracking particle shape distributions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Free energy | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Thermodynamic framework | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4.1 Dissipation rates and shape coevolution | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Mathematical description of the particle shape | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Statistical homogenization with shape descriptors | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.5 Post-yielding response | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.6 Calibration and validation | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.6.1 DEM synthetic experiments | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.6.2 Laboratory experiments | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Discussion and future directions | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
引言长但功能清晰：第一段定义受限粉碎，第二段用自然极端和 attractor 制造物理动机，第三段定位 CBM，第四段指出 shape dispersion 缺口，最后给路线图。方法段落高度名词化，依靠符号表降低负担。结果段落多采用“形态类别 + 共演化速率 + 宏观响应”的并列句式，适合复杂参数论文。

- Introduction 段落推进：背景段负责扩大意义，文献段负责分类，gap 段负责收束，贡献段负责声明本文做什么，路线图段负责降低阅读成本。
- Method 段落推进：定义对象和变量，再解释参数、边界、假设和流程。好的方法段不是实验记录或公式清单，而是告诉读者为什么这些设置足以回答问题。
- Results 段落推进：每段开头通常点名本段要验证的 claim，中间引用图表和对照，结尾解释趋势的机制含义或引出下一变量。
- Discussion/Conclusion 段落推进：先重述最稳结论，再说明机制意义，最后写边界和未来工作。
- 常见段落开头方式：To investigate..., To quantify..., Having established..., Compared with..., These results suggest...。
- 常见段落收束方式：回到核心变量、指出机制、标注边界或引出下一节。
- 可复用段落模板：背景事实 2-3 句 -> 已有方法 2 句 -> 具体不足 1 句 -> 本文动作 1 句 -> 可验证贡献 1 句。

## 13. 文笔画像与语言习惯
文笔是热力学本构论文的厚重型：大量使用 dispersion、attractor、coevolution、dissipation、state variable 等名词，把新变量包装成不可缺少的状态描述。claim 强度较高，但经常用 dependent on、tend to、underpins 控制因果范围。

- 整体语气：克制、机制导向、证据优先。即使题材新，也尽量通过变量和图表表达新意，而不是形容词堆叠。
- claim 强度：核心结果处用 demonstrate/show/reveal，机制解释处常用 suggest/indicate/can be attributed to，外推处使用 may/could/potentially 控制范围。
- 谨慎表达：作者会在实验条件、模型假设、参数范围、类比系统或硬件噪声处主动加限定。
- 问题表达：常见模式是“X is important, but Y remains unresolved because Z”。
- 贡献表达：常见模式是“we develop/formulate/introduce/demonstrate a framework that...”。
- 对比表达：常用 in contrast、compared with、at variance with、unlike prior approaches。
- 术语密度：较高，但术语围绕核心变量聚集；没有明显为了显得高深而引入无关术语。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：shape(227)；evolution(103)；particle(92)；initial(58)；breakage(50)；energy(49)；model(46)；distributions(46)；coevolution(43)；size(39)；distribution(39)；index(39)；particles(38)；ultimate(37)；atness(34)；dissipation(33)；attractor(33)；elongation(33)；ratio(28)；con(27)
- 高频学术名词：evolution(103)；energy(49)；model(46)；coevolution(43)；distribution(39)；atness(34)；dissipation(33)；elongation(33)；parameters(26)；response(23)；stress(22)；analysis(22)；validation(22)；framework(22)；function(21)；parameter(20)
- 高频学术动词：proposed(16)；shown(13)；derived(7)；validated(5)；capture(5)；compared(5)；formulated(4)；show(4)；indicates(4)；indicate(4)；developed(3)；predicted(3)；suggests(2)；captured(2)；revealed(2)；evaluated(2)
- 高频形容词：initial(58)；experimental(32)；lal(25)；critical(24)；elastic(24)；plastic(24)；statistical(21)；mechanical(21)；thermodynamic(17)；relative(15)；represent(13)；principal(13)；macroscopic(13)；constitutive(12)；spherical(12)；theoretical(10)
- 高频副词/连接副词：explicitly(13)；however(11)；respectively(9)；assembly(7)；highly(7)；cally(7)；finally(5)；strictly(5)；initially(5)；strongly(4)；potentially(4)；notably(4)；consequently(4)；systematically(4)；thermodynamically(4)；successfully(4)
- 高频二词短语：shape evolution(51)；particle shape(31)；free energy(23)；shape distributions(23)；particle size(19)；initial ultimate(15)；initial shape(15)；crushing strength(14)；shape coevolution(14)；atness elongation(14)；coevolution rates(14)；breakage index(13)；shape dispersion(12)；granular materials(12)；dissipation rate(12)；sti ness(11)
- 高频三词短语：initial shape distributions(8)；shape evolution index(7)；ratio elongation ratio(6)；helmholtz free energy(6)；particle shape distributions(6)；particle size shape(5)；shape evolution indices(5)；atness ratio elongation(5)；initial shape distribution(5)；probability density functions(5)；free energy formulation(5)；sphere rod plate(5)

**主动、被动与句法**

- 被动语态估计次数：154
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：1054
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：168
- 一般过去时线索：78
- 现在完成时线索：11
- 情态动词线索：33
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：shape(17)；particle(9)；granular(7)；dispersion(6)；crushable(4)；continuum(4)；size(4)；evolution(4)
- 1. Introduction：shape(24)；particle(16)；kpa(13)；ratio(11)；size(8)；buscarnera(8)；stress(7)；ultimate(7)
- 2. Shape-enhanced breakage mechanics：shape(5)；particle(3)；prior(2)；buscarnera(2)；towards(2)；studies(1)；explored(1)；coupling(1)
- 2.1. Evidence of shape attractor distributions：shape(15)；ultimate(7)；initial(7)；particle(7)；attractor(6)；distribution(6)；crushing(3)；particles(3)
- 2.2. A shape evolution index for tracking particle shape distributions：shape(13)；evolution(7)；particle(6)；ultimate(6)；index(6)；breakage(5)；distribution(4)；descriptor(4)
- 2.3. Free energy：shape(19)；energy(15)；free(7)；evolution(7)；size(6)；particle(5)；density(5)；distribution(5)
- 2.4. Thermodynamic framework：rate(4)；dissipative(4)；dissipation(3)；rates(3)；rate-independent(2)；total(2)；strain(2)；free(2)
- 2.4.1. Dissipation rates and shape coevolution：shape(23)；dissipation(18)；evolution(16)；rate(11)；coevolution(9)；particle(7)；law(6)；proposed(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
以下只提取短语和句式骨架，不大段复制原文。

- **问题/gap**：`Although size dispersion has been central to CBM, the statistical dispersion of particle shape remains largely absent from continuum descriptions.`  中文启发：用 although 建立旧框架价值，再指出缺席变量。
- **方法**：`We introduce a state variable that measures the distance between the current shape distribution and an attractor distribution.`  中文启发：适合任何“分布到目标态距离”变量。
- **结果**：`The model predicts non-monotonic strength trends controlled by both initial morphology and the rate of coevolution.`  中文启发：把复杂结果压缩成两个控制因子。
- **验证**：`Predictions are assessed against particle-scale simulations and laboratory measurements.`  中文启发：双验证句，避免只靠数值自洽。
- **未来**：`Future extensions should incorporate additional descriptors that capture angularity, roughness, and fabric anisotropy.`  中文启发：把局限转化为清晰扩展。

### 14.1 问题与 gap 表达
- 骨架：`Despite extensive studies on X, how Y controls Z under A remains unclear.`
- 中文启发：不要只说“研究不足”，而要说哪个控制关系、哪个条件、哪个尺度或哪个观测仍未闭合。

### 14.2 方法与框架表达
- 骨架：`To address this gap, we combine A with B to construct C.`
- 中文启发：方法句要同时交代输入、核心动作和输出，不要只报工具名。

### 14.3 结果与趋势表达
- 骨架：`Compared with the baseline, the proposed/observed system shows A, indicating B.`
- 中文启发：图表结果要和 baseline 绑定，否则趋势没有解释力。

### 14.4 机制解释表达
- 骨架：`This behavior can be attributed to A, which modifies B and thereby changes C.`
- 中文启发：机制句最好是三段式：原因、作用对象、宏观后果。

### 14.5 贡献与意义表达
- 骨架：`The framework provides a quantitative route for linking A-scale mechanisms to B-scale response.`
- 中文启发：贡献要写成可检验动作或能力，而不是抽象价值。

### 14.6 局限与未来工作表达
- 骨架：`The present analysis is limited to A; future work should examine whether B persists when C is relaxed.`
- 中文启发：局限不是自我削弱，而是告诉读者结论在哪里可靠、下一步如何扩展。

## 15. 引用策略与文献使用
引用策略很有层级：Sammis/Einav 等为破碎和 CBM 奠基，Domokos/Tsuchiyama/Seo/Li 等支撑形状吸引子，Radjai/Goldenberg/Cho 等说明形状影响宏观性质但结论分散，DEM 与实验文献为验证数据提供合法性。文献不是罗列，而是被分配到三个功能：证明现象存在、证明旧框架可继承、证明 gap 重要。

- 引用密度：引言最高，方法基础次之，结果段最低。这样的分布符合 JMPS 常见写法：先用文献建立问题位置，后用本文证据推进主张。
- 经典文献用途：提供术语、守恒律、本构、几何、贝叶斯或断裂理论的合法性。
- 近年文献用途：说明问题仍在前沿，制造与本文最接近工作的差异。
- 方法文献用途：证明工具不是凭空发明，并交代为什么旧工具仍不够。
- 对比/批判性引用：语气通常温和，强调“valuable but limited under...”而非直接否定。
- gap 如何靠引用搭建：先说明已有研究解决 A，再说明 B 仍缺，最后把本文放在 A 与 B 的交界处。
- 引用风险：若遗漏最接近的竞争工作，novelty 会被直接挑战；若过多自引或只引支持文献，gap 会显得人为。

## 16. 审稿人视角风险
第一，flatness/elongation 是否足够描述真实颗粒形状，尤其角度、粗糙度和表面纹理可能缺失。第二，Shape Evolution Index 把分布差异压缩成单指标，可能丢失多峰或尾部分布。第三，能量修正函数和 coevolution rates 的物理可辨识性需要更多实验。第四，DEM 合成颗粒与真实破碎机制仍有尺度差异。

- 最大攻击面：核心 claim 是否被足够多条件验证，或者是否只是特定设置下成立。
- claim 是否过强：文内最强结论通常可接受，但摘要和结论中的广泛意义需要限定在研究对象和方法假设内。
- 证据是否不足：主要不足往往不是没有证据，而是证据覆盖的参数、几何、材料或样本范围有限。
- 方法是否可复现：TXT 提供了公式和部分参数，但完整复现仍需 PDF、补充材料、代码/数据或实验细节。
- 对比是否充分：审稿人会要求与最接近前人同条件比较，而不是只和弱基线比较。
- 边界条件是否清晰：需要把每个主要 claim 与材料、几何、加载、噪声、守恒或类比条件绑定。
- 替代解释是否排除：若机制解释存在其他可能，需要用对照、消融、敏感性分析或谨慎措辞处理。
- 图表是否需进一步核查：需要。尤其是颜色场、误差带、图像序列、相图边界、硬件噪声和拟合曲线均应结合 PDF 图像核查。

## 17. 可复用资产
可复用的是“把平均变量升级为分布状态变量”的写法。先用跨尺度证据证明分布收敛，再定义一个距离指标，再把指标嵌入能量/耗散，最后用合成数据和真实实验双验证。图表设计也可迁移：概念证据图、变量定义图、参数响应图、验证图四类图分工明确。

- 可复用选题角度：从一个被观察到但未被机制闭合的现象切入，或从一个被使用但未被充分验证的工具切入。
- 可复用 gap 制造方式：承认旧研究贡献，指出其边界，再把本文变量放在边界之外但仍可验证的位置。
- 可复用论证链：背景 -> 文献分类 -> 具体 gap -> 新变量/框架 -> 基线验证 -> 对照/参数扫描 -> 机制解释 -> 边界。
- 可复用图表设计：概念/装置图、变量定义图、基线对照图、参数响应图、验证图、相图或流程图。
- 可复用段落结构：主题句先提出本段 claim，中间用图表和公式支撑，结尾解释对主线的意义。
- 可复用句型骨架：`To isolate the role of X, we compare A and B under otherwise identical conditions.`；`The observed transition from A to B indicates that C becomes dominant.`；`This result should be interpreted within the limits of D.`
- 可复用引用组织：经典文献管合法性，最新文献管前沿性，最接近文献管 novelty，应用文献管意义。
- 不宜直接模仿之处：若自己没有同等强度的图表、实验、推导或对照，不宜模仿过强标题和广泛外推。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学习：把贡献写成“补上某个闭环”，而不是“提出一个方法”。闭环包括变量定义、方法执行、证据验证、机制解释和边界控制。
- 可迁移到 Introduction 的写法：先把领域问题讲成读者关心的力学矛盾，再用文献分类制造窄 gap，最后明确本文只解决其中一个可验证问题。
- 可迁移到 Method 的写法：先讲总体框架和变量，后讲公式/实验/算法细节；让方法复杂度与 gap 一一对应。
- 可迁移到 Results/Discussion 的写法：每张关键图服务一个 claim；先说明图证明了什么，再解释为什么能支持机制。
- 需要避免的问题：不要让图表变成结果清单；不要在摘要中许诺正文没有验证的普适性；不要把模型内趋势写成真实世界定律；不要让引用只证明自己想证明的 gap。
- 对中文论文写作的启发：中文写作容易把“意义”写大，把“边界”写弱。本文提醒我们，高水平论文的可信度常来自主动限定条件，而不是无条件扩大贡献。

## 19. 最终浓缩
- 这篇论文最值得学：这篇最值得学的是如何让一个新状态变量显得必要：先证明旧变量解释不了分布效应，再让新变量进入热力学闭环。最大风险是形状描述符过少和参数可辨识性。三个可迁移动作：用多源证据制造变量需求，用归一化距离定义变量，用合成与实验双验证减少模型自说自话。
- 最核心的一句话：颗粒破碎不仅改变粒径，也把形状分布推向统计吸引子；将形状分布作为连续状态变量嵌入 CBM 后，可以解释不同初始形态和形状共演化速率导致的非单调强度、刚度与耗散差异，并能拟合 DEM 与实验数据。
- 最大风险：文内证据支撑特定对象和条件下的结论，但外推到更复杂系统时需要额外验证。
- 三个可迁移动作：
  1. 把 gap 写成具体变量、机制或边界缺口，而不是泛泛的“研究不足”。
  2. 让每个方法模块对应一个 claim，让每张图表承担明确说服功能。
  3. 在结论中区分“本文已经证明的”“本文提示的”“需要后续核查的”。
- 后续人工核查：应结合 PDF 检查图像本体、曲线尺度、误差带、颜色场、公式编号和补充材料；TXT 足以支持结构和写作拆解，但不应替代视觉核查。
