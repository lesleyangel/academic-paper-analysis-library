# Asymptotic representation of frictional, non-conforming contact edges under general periodic loading

## 0. 读取说明
- 源 PDF：`jmps/文献/Asymptotic-representation-of-frictional--non-con_2026_Journal-of-the-Mechani.pdf`
- 源 TXT：`jmps/文本/txt/Asymptotic-representation-of-frictional--non-con_2026_Journal-of-the-Mechani.txt`
- 辅助参照：上一轮 `jmps/拆解/papers/Asymptotic-representation-of-frictional--non-con_2026_Journal-of-the-Mechani.md` 仅用于校验方向，本稿按全文结构重新展开，没有直接复制其段落。
- 是否需要结合 PDF 图像核查：需要。当前依据 PyMuPDF 抽取的全文、图注、表格文字和公式上下文拆解；涉及云图、裂纹形貌、曲线拟合优劣、应力场细节和图像色标的判断均标注为需结合 PDF 图像核查。
- 本文类型：解析接触力学/渐近理论论文。

## 1. 基本信息与论文身份
- 题名：Asymptotic representation of frictional, non-conforming contact edges under general periodic loading
- 作者/机构：J.R. Barber; D.A. Hills。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106650; DOI: 10.1016/j.jmps.2026.106650
- DOI：见上方 subject 信息。
- 关键词：Frictional contact; Fretting; Fretting fatigue; Partial slip; Contact mechanics
- 研究对象：非共形摩擦接触边缘在一般周期载荷下的分离、滑移、粘着、能量耗散和 T-stress
- 研究尺度：二维半平面/接触边缘小过程区尺度，链接有限元原型和可控实验接触
- 方法类型：接触边缘渐近场、KI/KII/T-stress 参数化、分段滑移构造、Coulomb 摩擦下耗散积分
- 证据类型：公式推导、加载相空间构造、分离/滑移/粘着区域图、耗散密度曲线、相位与 mode mixity 参数扫描
- 目标读者：JMPS 的计算力学、材料力学、断裂/接触/生物力学模型研究者，以及需要把微观机制转译为可计算模型的工程力学读者。
- JMPS 风格定位：这不是单纯应用论文，而是把一个具体物理现象放入可推导、可计算、可验证的力学框架中；文章的价值主要来自“模型如何闭合机制”而不是只报告性能或现象。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要采用 JMPS 常见的“问题对象 -> 模型动作 -> 验证/结果 -> 物理意义”压缩方式。第一层交代研究对象和旧方法不足，第二层用方法动词建立本文身份，第三层给最核心的趋势或机制发现，最后把结果回收到领域意义。
- 背景句承担什么：背景句把 fretting fatigue 中接触边缘裂纹形核的局部相似准则 写成一个需要定量模型的力学问题，使读者知道这不是孤立算例，而是材料/结构/生物系统中的普遍机制。
- gap 句承担什么：gap 句不是空泛地说“尚不清楚”，而是强调 已有 half-plane 或恒定法向载荷理论难处理一般原型、接触边移动以及 KI/KII 非同相变化；工程上又需要把复杂接触映射到可控实验。 这类具体缺口；它把本文方法复杂度合理化。
- 方法句承担什么：方法句用 接触边缘渐近场、KI/KII/T-stress 参数化、分段滑移构造、Coulomb 摩擦下耗散积分 明确告诉读者本文提供的是“可计算框架”而非经验解释。
- 结果句承担什么：结果句服务于主张：对一般周期载荷下光滑非共形摩擦接触边缘，可以用局部参数 LI、KI、KII 和 T-stress 建立与原型无关的渐近表示，并推断滑移范围、点态耗散和 fretting fatigue 过程区条件。
- 意义句承担什么：意义句通常回到 JMPS 读者关心的尺度桥接、机制解释、边界条件或可复现计算。
- 一句话主张：对一般周期载荷下光滑非共形摩擦接触边缘，可以用局部参数 LI、KI、KII 和 T-stress 建立与原型无关的渐近表示，并推断滑移范围、点态耗散和 fretting fatigue 过程区条件。
- 3-5 个核心关键词：机制化建模；定量验证；尺度桥接；边界条件；可复用图表叙事。

## 3. 选题层深拆
- 问题来源：fretting fatigue 中接触边缘裂纹形核的局部相似准则 中存在一个典型 JMPS 式张力：微观机制已被观察或假设，但宏观/中尺度响应需要更干净的定量解释。
- 问题为什么重要：如果不能解释 fretting fatigue 中接触边缘裂纹形核的局部相似准则，相关材料或系统的设计只能停留在经验层面；本文试图把现象转成可计算的变量、参数和图表证据。
- 问题为什么现在值得做：一方面已有文献积累到足以支撑模型假设，另一方面数值工具/实验观测/原子模拟数据已经允许作者把旧问题推进到更一般条件。
- 问题边界：本文的研究边界并不无限扩张，而是绑定在 二维半平面/接触边缘小过程区尺度，链接有限元原型和可控实验接触；超出这些假设的真实结构、复杂加载、材料散布或动态演化，需要后续验证。
- 选题的 JMPS 味道：JMPS 喜欢“现象 + 物理机制 + 数学/数值框架”的组合。本文不是把某个软件跑一遍，而是把 非共形摩擦接触边缘在一般周期载荷下的分离、滑移、粘着、能量耗散和 T-stress 中的核心驱动因素拆成可推导、可比较、可被图表支撑的 claims。
- 选题可迁移性：可迁移到任何“局部机制决定整体响应”的论文：先找到局部事件，再建立上层响应，再用图表证明局部事件如何改变整体曲线或形貌。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：文章通常把前人分成三类：基础物理/经典理论，数值或实验观测，最近的模型扩展。这样做的好处是 gap 不会变成“我没看到别人做”，而是“每类方法都解决了一部分，但组合起来仍缺本文这块”。
- 主要研究流派/方法路线：一类路线提供机理概念，一类路线提供可计算工具，一类路线提供可验证数据或图像。本文站在第二类和第三类之间，试图让概念能落到计算证据上。
- 每类研究解决了什么：经典理论提供术语和物理边界；数值/实验研究证明现象真实存在；近期模型展示了可行性或局部趋势。
- 每类研究留下什么不足：经典理论往往假设理想化，数值观测可能尺度小或难推广，实验图像可能只能观察结果而不能分解局部驱动力。本文的 gap 正是这些不足的交叉点。
- 本文站在哪条线上：创新是将非共形接触边缘写成 fracture mechanics 式的局部参数匹配问题，扩展到一般周期载荷相位；一个重要发现是最大摩擦耗散密度独立于 LI，只由 KII、mode mixity 参数和相位控制。
- 最接近前人工作：从文本看，作者通常会引用与方法最接近的模型或与现象最接近的实验/模拟，并把本文定位为扩展、整合或更一般化。
- 是否公平处理前人：整体较公平。文章没有简单否定旧方法，而是承认已有贡献，再指出其不适用条件或未覆盖变量。审稿时仍需检查是否遗漏最新相邻工作。

## 5. Gap 制造机制
- 明示 gap：已有 half-plane 或恒定法向载荷理论难处理一般原型、接触边移动以及 KI/KII 非同相变化；工程上又需要把复杂接触映射到可控实验。
- 隐含 gap：隐含缺口是“现象层证据”与“可预测模型”之间仍有距离。读者可能知道现象存在，但不知道在给定参数、几何、加载或材料条件下如何定量判断。
- gap 类型：方法 gap、机制 gap、尺度桥接 gap 和验证 gap 的组合；具体权重随本文主题而变。
- gap 证据来自哪里：来自引言中文献分类、方法部分对旧模型限制的说明、以及结果部分把基线和新框架并排比较的图表。
- gap 是否足够窄：足够窄。本文没有试图解决整个领域，而是围绕 非共形摩擦接触边缘在一般周期载荷下的分离、滑移、粘着、能量耗散和 T-stress 中一个可建模问题展开。
- gap 是否足够重要：重要，因为它影响模型可信度、设计准则或实验解释；若该 gap 不补，后续结论容易停留在经验或图像层面。
- 如果我是审稿人会如何追问：最可能追问 gap 是否真的没有被最近文献处理；如果只是组合已有工具，本文的新贡献是否超过实现层面；以及结论是否超出了本文假设范围。

## 6. 创新性判断
- 作者声称的贡献：提出或扩展一个可计算/可解析框架，并用多组图表说明它能解释 fretting fatigue 中接触边缘裂纹形核的局部相似准则 中的关键现象。
- 我判断的真实创新：创新是将非共形接触边缘写成 fracture mechanics 式的局部参数匹配问题，扩展到一般周期载荷相位；一个重要发现是最大摩擦耗散密度独立于 LI，只由 KII、mode mixity 参数和相位控制。
- 创新类型：方法创新 + 机制解释 + 证据组织创新。个别文章还包含实验闭环或解析公式贡献。
- 创新强度：中高。创新强度不只来自“新公式”，还来自作者把一个复杂现象整理成可被验证的 claims，并逐一提供证据。
- 创新必要性：必要性由 gap 支撑；如果没有本文方法，关键问题要么只能被定性解释，要么只能在更窄条件下模拟。
- 创新与证据匹配度：核心方法 claim 与证据匹配较好；更宽泛的设计、普适性或预测性 claim 需要边界控制。
- 容易被挑战的创新点：如果最接近前人已经具备相似功能，本文需要强调差异在变量、边界、可复现性或解释能力上，而不是只换了实现平台。

## 7. 论证链条复原
背景：fretting fatigue 的寿命常由小接触边缘过程区中的裂纹形核控制。 -> 文献：Williams/Rice 裂纹渐近思想、Jäger/Ciavarella 接触解、作者前作的接触边缘相似。 -> gap：一般周期载荷下接触边移动和非同相法/切向扰动缺少统一局部表示。 -> 问题：如何从 FE 原型提取局部参数并推断真实接触中的滑移和耗散。 -> 方法：先固定接触边并强制 stick，计算 KI(t)、KII(t)、Δσ，再释放接触边运动与滑移，构造分段解。 -> 证据：同相和非同相载荷的解析表达、图形构造、耗散分布和总耗散。 -> 发现：耗散峰随 λ 和相位变化，部分区域可能只经历单向滑移或分离期补偿；T-stress 需要单独记录。 -> 机制：奇异场在真实接触中通过边缘运动和局部滑移被 relaxed out。 -> 意义：为原型-实验匹配和 fretting 疲劳过程区表征提供理论准则。

这条链条的优点是闭合度较高：问题不是凭空抛出，方法不是孤立技术，图表也不是装饰。最薄弱环节通常在“发现 -> 机制 -> 意义”的外推：模型内趋势是否能成为真实材料/系统规律，需要更强数据或实验验证。

## 8. 方法/理论/模型细拆
- 方法总框架：方法细拆：第一步用 LI 描述平均压力在接触边缘附近的平方根分布；第二步在平均接触尺寸下禁止滑移，施加振荡载荷并提取 KI(t)、KII(t)；第三步在真实接触中允许边缘移动和 Coulomb 滑移，利用局部条件消除奇异性，求得滑移带位置、速度和耗散密度；第四步引入 T-stress 以处理平行于边缘的应力。关键限制是相同材料或 Dundurs beta 近似为零、二维平面问题、接触边由局部曲率定义、过程区小于接触尺度、表面光滑且服从点态 Coulomb law。
- 关键概念：局部驱动因素、可计算状态变量、基线模型、对照参数、边界条件和验证指标。
- 关键变量/参数：从全文看，关键参数总是被设计成能直接改变主图趋势的变量，而不是只存在于公式中的符号。读者应重点追踪这些参数如何进入图表。
- 核心假设：每篇都依赖理想化假设，例如几何简化、材料模型、加载范围、尺度分离、局部均匀或统计代表性。好的地方是作者通常在方法或结论中承认这些边界。
- 边界条件：边界条件既包括数学边界，也包括物理适用范围。写作上值得学习的是：边界条件不是附属信息，而是 claim 能否成立的前提。
- 方法步骤：先定义对象，再建立控制方程或计算流程，再给参数，最后安排验证。这样的顺序能降低读者理解成本。
- 复现信息：总体上有较多参数、图注和公式可供复现；但图像本体、代码、补充材料和实验原始数据仍需进一步核查。
- 方法复杂度是否合理：合理。复杂度来自目标问题本身，而不是为了“显得高级”。不过，如果移植到自己的论文，需要确认数据量和验证强度能支撑同等级复杂度。
- 方法与 gap 的对应关系：方法中的每个模块都应能回答 gap 的一部分；如果某个模块不服务 claim，就会成为审稿风险。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 局部接触边缘可由 LI、KI、KII 参数化，而不必全局 half-plane 理想化 | 引言/接触分析 | Fig. 1-2 的非 Hertzian 原型示意和渐近压力/剪切表示 | 解析构造 | 强 | 只适用于光滑非共形接触边 |
| 真实接触中的边缘运动和滑移会消除固定 stick 分析中的奇异性 | Sections 1-2 | KI/KII 的符号、接触边移动和滑移区构造公式 | 理论推导 | 强 | 需要 FE 提取参数准确 |
| 同相载荷下最大耗散密度随 λ 变化且 LI 影响会抵消 | Section 3 | Fig. 5-6 的耗散密度与最大值曲线 | 解析积分 + 图形 | 强 | 理想 Coulomb 摩擦可能影响真实耗散 |
| 非同相载荷会改变分离、滑移和粘着区域时序，并造成单向滑移区域 | Section 4 | Fig. 7-11 的相位构造和耗散分布 | 解析构造 + 图示 | 中强 | 复杂分段推导对读者复现要求高 |
| T-stress 对 fretting fatigue 过程区匹配不可忽略 | Section 3.5/Appendix | 均值与振荡 T-stress 的推导，结论要求记录 Δσ | 理论推导 | 中 | 未做实验验证 |

这张表说明本文的证据组织不是平均铺开，而是围绕少数强 claim 逐层加固。最值得学习的是作者通常先建立 baseline，再展示新变量带来的差异，最后讨论边界。最需要警惕的是图像/曲线的视觉说服力可能强于统计说服力，因此涉及图像本体处都应回到 PDF 核查。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | Hertzian 与非 Hertzian 接触边示意 | 局部小区域可共享相同渐近场 | 用图降低抽象渐近理论门槛 | 是 |
| Fig. 2 | 非共形接触边剪切牵引表示 | 定义边缘局部载荷和剪切奇异项 | 承接 KI/KII 参数化 | 是 |
| Fig. 3-4 | 载荷椭圆和同相轨迹 | 说明 KI/KII 周期变化和摩擦锥关系 | 把时间问题转化为几何构造 | 是 |
| Fig. 5-6 | 同相载荷耗散密度和最大值 | 证明耗散峰与 λ 的关系 | 核心结果图，服务 fretting 风险判断 | 是 |
| Fig. 7-8 | 滑移区构造和分离/滑移/粘着区域 | 展示非同相路径下界面状态时序 | 让复杂分段解可视化 | 是 |
| Fig. 9-12 | 相位对点态/总耗散的影响 | 相位会改变耗散峰位置和总量 | 把理论结果转成实验设计参数 | 是 |
| Appendix T-stress formulas | 计算平行应力项 | 完善过程区应力匹配 | 服务实验原型等效 | 否 |

图表顺序整体服务一条递进叙事：先让读者相信对象和方法定义正确，再用基线图建立可比较坐标，随后逐个加入变量，最后用综合图或补充图说明边界。公式的作用不是堆砌推导，而是把物理机制转为可计算量；表格的作用是把参数暴露出来，增强复现性和审稿信任。

## 11. 章节结构与篇章布局
- Abstract：压缩问题、方法、核心发现和意义，通常包含一两个强 claim。
- Introduction：先给领域背景，再把文献分组，最后制造具体 gap。优点是 gap 与方法天然连接。
- Related Work/Background：不一定单列章节，常嵌入 Introduction。文献不是逐篇罗列，而是按机制、尺度或方法功能组织。
- Method/Theory/Model：方法章先给可理解的对象定义，再逐步展开公式、参数和求解。这样的顺序让复杂理论不至于成为黑箱。
- Results：结果按“基线 -> 变量 -> 机制 -> 边界”的顺序推进，避免一开始就抛出最复杂图。
- Discussion：把结果放回机制语境，控制 claim 强度，承认方法尚不能处理的真实复杂性。
- Conclusion：重复最强贡献，但通常不引入新证据；边界和未来工作服务于审稿友好性。
- 章节之间如何过渡：过渡依赖“上一节证明了什么，因此下一节需要检查什么”。
- 哪一节最值得模仿：最值得模仿的是方法与结果之间的接口：作者会用图表或参数表明确告诉读者“现在开始验证哪一个 claim”。
- 哪一节可能存在结构风险：如果 Discussion 把模型内发现写成普适设计准则，或结果图没有足够对照，就会产生结构风险。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Asymptotic-representation-of-frictional--non-con_2026_Journal-of-the-Mechani.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：19
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 1.1 Half-plane formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 1.4 The T stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Contact analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Tangential loading | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 In-phase loading | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.1 Slip velocity | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.2 Dissipation rate | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Total dissipation in one cycle | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.4 Hysteretic damping | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5 Alternating T-stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5.1 Constant contact area | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Evolution of separation, slip and stick zones | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Unidirectional slip | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：第一段扩大问题重要性；第二段收束到具体物理对象；第三段分类前人；第四段指出缺口；最后一段声明本文方法和贡献。这个节奏适合 JMPS，因为它让方法复杂性看起来是问题逼出来的。
- Method 段落推进：先给全局框架，再给变量和公式；先讲已知部分，再讲本文新增部分；先说明假设，再说明求解和参数。每个段落都应回答“这个模块为什么存在”。
- Results 段落推进：通常以图开头，描述趋势，给物理解释，再说明该趋势支撑哪个 claim。好的结果段不会一次解释所有现象，而是逐图推进。
- Discussion/Conclusion 段落推进：从最稳的发现开始，再讲机制意义，最后承认局限并提出未来验证。语气从强到谨慎，避免结尾过度外推。
- 常见段落开头方式：`To investigate...`、`Figure X shows...`、`Compared with...`、`This suggests...`、`We emphasize that...`。
- 常见段落收束方式：回到 gap、引出下一参数、限定适用范围、强调机制解释或连接实验/文献。
- 可复用段落模板：`问题对象句 -> 前人已知句 -> 本文变量句 -> 方法动作句 -> 图表证据句 -> 机制解释句 -> 边界限定句`。

## 13. 文笔画像与语言习惯
- 整体语气：成熟、克制、机制导向。方法 claim 往往写得清楚，机制 claim 用 suggest/indicate 控制强度。
- claim 强度：标题和摘要可能较强；正文结果通常通过图表和限定语削弱绝对性。
- 谨慎表达：常见 `qualitatively`, `suggests`, `may`, `within the investigated range`, `limited to`, `beyond the scope`。
- 问题表达：问题不是“缺研究”，而是“现有模型不能在某些条件下解释/预测某个关键量”。
- 贡献表达：偏好 `develop`, `propose`, `formulate`, `demonstrate`, `reveal`, `establish`。
- 机制表达：偏好 `attributed to`, `governed by`, `driven by`, `redistribution`, `interaction`, `competition`。
- 对比表达：大量使用 baseline、existing model、homogeneous case、in contrast、compared with。
- 限定边界表达：结论前后常给出条件，如加载范围、几何假设、材料模型或数据来源。
- 术语密度：术语密度高，但通常围绕少数核心概念重复，降低读者记忆负担。
- 长句/短句习惯：方法段长句多，结果段较多短句；图注信息量大，承担半个方法说明功能。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：contact(159)；slip(81)；edge(60)；sin(48)；loading(47)；dissipation(42)；stress(37)；region(36)；load(35)；barber(31)；zone(29)；shear(28)；small(26)；but(25)；hills(24)；normal(24)；phase(23)；case(22)；area(22)；maximum(22)
- 高频学术名词：dissipation(42)；analysis(40)；stress(37)；pressure(18)；friction(16)；energy(14)；distribution(14)；element(13)；traction(13)；interface(12)；nucleation(11)；intensity(11)；separation(11)；method(8)；solution(8)；position(8)
- 高频学术动词：shown(14)；show(9)；shows(9)；compared(7)；develop(4)；developed(4)；capture(3)；captured(2)；suggests(1)；investigate(1)；evaluated(1)；solve(1)
- 高频形容词：small(26)；normal(24)；dimensionless(20)；frictional(19)；local(16)；constant(15)；extent(14)；element(13)；elastic(12)；periodic(12)；tangential(11)；total(10)；positive(8)；cient(8)；asymptotic(7)；component(7)
- 高频副词/连接副词：therefore(14)；generally(10)；approximately(6)；apply(6)；however(5)；usually(5)；clearly(5)；locally(4)；relatively(4)；ciently(4)；actually(4)；easily(3)；respectively(3)；weakly(2)；potentially(2)；rigorously(2)
- 高频二词短语：contact edge(40)；barber hills(19)；slip zone(19)；sin sin(17)；contact area(15)；contact pressure(14)；normal load(13)；nite element(12)；dimensionless dissipation(12)；stress intensity(11)；shear tractions(11)；shear traction(10)；dissipation rate(10)；edge contact(9)；contacting bodies(9)；mean load(9)
- 高频三词短语：stress intensity factors(7)；sin sin sin(7)；dissipation per unit(6)；per unit area(6)；contact pressure distribution(5)；fretting fatigue cracks(4)；energy dissipated friction(4)；nite element analysis(4)；dashed lines slope(4)；coe cient friction(4)；extent slip zone(4)；dimensionless dissipation per(4)

**主动、被动与句法**

- 被动语态估计次数：125
- `we + 动作动词` 主动句估计次数：4
- 名词化表达估计次数：674
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：276
- 一般过去时线索：26
- 现在完成时线索：11
- 情态动词线索：62
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：contact(10)；frictional(5)；engineering(5)；edge(5)；slip(5)；stress(5)；life(4)；fretting(4)
- 1. Introduction：contact(13)；crack(13)；hills(6)；edge(5)；stress(5)；must(5)；small(4)；fatigue(4)
- 1.1. Half-plane formulation：contact(69)；edge(29)；small(15)；load(15)；slip(15)；shear(15)；half-plane(12)；pressure(12)
- 1.4. The T stress：stress(8)；contact(8)；surface(4)；fatigue(4)；element(4)；analysis(4)；mean(4)；parallel(3)
- 2. Contact analysis：sin(4)；time(3)；frictional(2)；contact(2)；consider(1)；case(1)；varies(1)；sinusoidally(1)
- 2.1. Tangential loading：loading(6)；contact(5)；zone(5)；slip(4)；barber(3)；coordinate(3)；point(3)；entire(3)
- 3. In-phase loading：slip(16)；contact(7)；zone(6)；point(5)；load(4)；area(4)；region(4)；case(3)
- 3.1.1. Slip velocity：slip(5)；rate(4)；velocity(4)；respect(4)；tangential(4)；region(2)；therefore(2)；displacement(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

### 14.1 问题与 gap 表达
- 原文表达模式：先确认 `fretting fatigue 中接触边缘裂纹形核的局部相似准则` 的领域重要性，再用 `however/despite/current models` 把问题收束到具体模型缺口。gap 不写成泛泛的“研究不足”，而是绑定到某个旧框架不能解释、不能预测或不能经济计算的对象。
- 可复用句型骨架：`Despite extensive work on X, the way in which Y controls Z remains unresolved under A conditions.`；`Existing models capture A, but they do not provide a tractable route to B.`
- 中文写作启发：缺口句最好同时说明“已有研究已经解决什么”和“仍缺哪一个可验证环节”。不要只说“缺少研究”，而要说“缺少哪种变量、哪种尺度、哪种边界条件下的定量解释”。

### 14.2 方法与框架表达
- 原文表达模式：用 `we develop/propose/formulate` 声明方法，再用一组名词短语交代组成模块：控制方程、变量、求解器、参数、验证算例。方法句追求输入、输出、物理对象清楚，而不是追求漂亮修辞。
- 可复用句型骨架：`To address this issue, we formulate a framework that couples A with B and evaluates C under D.`；`The proposed model consists of three ingredients: A, B, and C.`
- 中文写作启发：复杂方法要先给总框架句，再进入公式。总框架句应回答“为什么这个方法刚好对应 gap”。

### 14.3 结果与趋势表达
- 原文表达模式：结果句常以 `Fig. X shows/indicates` 或 `The results show that` 起手，然后接趋势、对照和限定条件。强结论之前常加 `within the investigated range` 或 `qualitatively`。
- 可复用句型骨架：`As A increases, B first changes in direction C and then saturates/deviates when D becomes dominant.`；`Compared with the baseline case, the proposed setting leads to E, indicating F.`
- 中文写作启发：图表结果不要只复述横纵轴；每一句都要说明这个趋势支撑哪个 claim。

### 14.4 机制解释表达
- 原文表达模式：机制句多用 `suggest/indicate/can be attributed to/arises from`，避免把模型内解释写成绝对因果。机制解释围绕局部变量如何重分配能量、应力、驱动力或概率展开，同时承认 `最大攻击面是理想条件：二维、同材料、光滑、Coulomb 摩擦、接触边由曲率定义、过程区足够小。真实粗糙表面、磨屑、摩擦系数演化和 3D 边缘可能改变耗散。图像需核查耗散峰位置、非同相区域划分和 λ<1/full stick 特例。` 可能限制外推。
- 可复用句型骨架：`This behavior can be attributed to A, which redistributes B and therefore changes C.`；`The observed trend suggests that A rather than B dominates in this regime.`
- 中文写作启发：机制段要区分“观察到什么”“可能说明什么”“还不能说明什么”。

### 14.5 贡献与意义表达
- 原文表达模式：贡献不是单点炫技，而是“提出框架 + 证明可用 + 解释现象 + 给出边界”。意义句一般回到 JMPS 关心的力学机制、尺度桥接或可计算预测。
- 可复用句型骨架：`The framework provides a quantitative route for linking A-scale mechanisms to B-scale response.`；`These results establish a connection between X and Y without requiring Z.`
- 中文写作启发：贡献句最好是可检验的动作，不要写成抽象口号。

### 14.6 局限与未来工作表达
- 原文表达模式：局限放在假设、参数、加载条件、几何理想化和验证范围上。好的局限不是自我削弱，而是告诉读者“本结论在什么范围内可信”。
- 可复用句型骨架：`The present analysis is limited to A and does not yet account for B.`；`Future work should test whether the same mechanism persists when C is relaxed.`
- 中文写作启发：局限段应给出下一步可执行的验证方向，而不是只说“未来需要更多研究”。


## 15. 引用策略与文献使用
- 引用密度：引言最高，方法基础和讨论次之；结果段引用较少，主要靠本文图表说话。
- 引用主要集中位置：背景重要性、经典理论、最接近模型、参数来源、实验/模拟对照。
- 经典文献用途：提供理论合法性和术语来源，使本文不显得从零发明。
- 近年文献用途：证明问题仍在前沿，并说明最新方法还没有完全覆盖本文 gap。
- 方法文献用途：为求解器、势函数、相场、构型力、接触渐近或生物电模型提供继承关系。
- 对比/批判性引用：作者多采用温和转折，不轻易否定前人，而是写成“有价值但不覆盖本文条件”。
- gap 如何靠引用搭建：先列已有成果，再指出每类成果的边界，最后把本文问题放在边界交叉处。
- references 暗示的研究共同体：通常混合经典力学、计算方法、材料/生物/接触具体领域和最新实验/数值工作。
- 引用风险：如果最接近的反例或同类模型未被充分讨论，会削弱 novelty；如果只引用作者自有工作，也可能被质疑闭环过窄。

## 16. 审稿人视角风险
- 最大攻击面：最大攻击面是理想条件：二维、同材料、光滑、Coulomb 摩擦、接触边由曲率定义、过程区足够小。真实粗糙表面、磨屑、摩擦系数演化和 3D 边缘可能改变耗散。图像需核查耗散峰位置、非同相区域划分和 λ<1/full stick 特例。
- claim 是否过强：核心方法 claim 基本可接受；普适性、设计准则或预测性 claim 需要加限定语。
- 证据是否不足：主要不足不是“没有证据”，而是证据范围有限，常集中于理想化算例、少量样本或模型内参数扫描。
- 方法是否可复现：公式和参数较充分，但代码、网格、图像判读和实验原始数据仍可能影响复现。
- 对比是否充分：与最接近前人的对比是审稿关键；若只有定性对照，建议后续增加同条件基准。
- 边界条件是否清楚：多数边界在方法和结论中有说明，但读者需要把这些边界与每个 claim 对应起来。
- 替代解释是否排除：模型通常能解释现象，但未必排除所有替代机制。Discussion 需要保持“解释力”而非“唯一因果”。
- 图表是否需要进一步核查：需要。所有云图、裂纹形貌、拟合曲线、能量路径、滑移区域和构型力方向都应结合 PDF 图像核查。

## 17. 可复用资产
- 可复用选题角度：可复用的是“工程复杂性 -> 局部渐近降维 -> 明确适用限制 -> 提供实验匹配参数”的理论写法。图表可学：加载相空间椭圆、摩擦线构造、滑移/粘着时序图、无量纲耗散曲线。不宜模仿的是没有足够解析基础时用大量符号推导代替物理解释。
- 可复用 gap 制造方式：把旧模型的适用边界写清楚，再把本文变量放在该边界之外。
- 可复用论证链：`现象/工程痛点 -> 经典理论或旧模型 -> 具体 gap -> 新框架 -> 基线验证 -> 参数扫描 -> 机制解释 -> 边界控制`。
- 可复用图表设计：基线图、模型示意图、参数扫描图、核心机制图、补充边界图。
- 可复用段落结构：主题句先告诉读者本段要证明什么，中间用图表/公式推进，结尾回到 claim 或引出下一变量。
- 可复用句型骨架：`To isolate the role of X, we compare A with B under otherwise identical conditions.`；`The observed transition from A to B indicates that C becomes dominant.`；`This result should be interpreted within the limits of D.`
- 可复用引用组织：经典理论用于合法性，近期文献用于前沿性，最接近前作用于 novelty，应用文献用于意义。
- 不宜直接模仿之处：如果没有相当强的图表证据和边界说明，不宜模仿强标题、复杂模型或跨尺度外推。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：写类似理论论文可以学习开篇列限制条件的诚实做法；Method 可迁移“先冻结边界计算奇异参数，再释放真实机制”的分步思想；Results 可将公式转成无量纲图；Discussion 要主动说真实粗糙和 3D 效应尚未包括。
- 可以迁移到 Introduction 的写法：先把问题讲成“旧模型边界内的未解变量”，再给本文可解决的窄问题。
- 可以迁移到 Method 的写法：先给框架图或总公式，再逐步解释变量、假设和求解流程。
- 可以迁移到 Results/Discussion 的写法：每个结果小节只服务一个 claim；讨论中把机制解释和局限分开写。
- 需要避免的问题：不要让方法复杂度超过证据强度；不要把模型内趋势写成真实世界普适规律；不要遗漏最接近对照。

## 19. 最终浓缩
- 这篇论文最值得学：本文最值得学的是把 fretting contact 写成类似 fracture mechanics 的局部相似问题，让复杂原型能被少量参数控制。
- 这篇论文最大风险：模型或证据的适用边界被读者忽略，导致结论外推过度。
- 三个可迁移动作：
  1. 用一个清晰 baseline 让新方法的增量可见。
  2. 把每张关键图绑定到一个明确 claim，而不是把图当作结果陈列。
  3. 在结论中主动说清楚哪些发现稳、哪些只是模型内启发、哪些需要 PDF 图像或后续实验核查。
