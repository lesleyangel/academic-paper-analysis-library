# A variational phase-field model for anisotropic fracture accounting for multiple cohesive lengths

## 0. 读取说明
- 源 PDF：`jmps/文献/A-variational-phase-field-model-for-anisotropic-_2026_Journal-of-the-Mechani.pdf`
- 源 TXT：`jmps/文本/txt/A-variational-phase-field-model-for-anisotropic-_2026_Journal-of-the-Mechani.txt`
- 辅助参照：上一轮 `jmps/拆解/papers/A-variational-phase-field-model-for-anisotropic-_2026_Journal-of-the-Mechani.md` 仅用于校验方向，本稿按全文结构重新展开，没有直接复制其段落。
- 是否需要结合 PDF 图像核查：需要。当前依据 PyMuPDF 抽取的全文、图注、表格文字和公式上下文拆解；涉及云图、裂纹形貌、曲线拟合优劣、应力场细节和图像色标的判断均标注为需结合 PDF 图像核查。
- 本文类型：理论模型 + 解析性质 + 有限元验证论文。

## 1. 基本信息与论文身份
- 题名：A variational phase-field model for anisotropic fracture accounting for multiple cohesive lengths
- 作者/机构：Angela Maria Fajardo Lacave; Francesco Vicentini; Fabian Welschinger; Laura De Lorenzis。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 212 (2026) 106585; DOI: 10.1016/j.jmps.2026.106585
- DOI：见上方 subject 信息。
- 关键词：Phase-field fracture; Anisotropy; Cohesive models; Crack nucleation; Crack propagation
- 研究对象：各向异性材料相场断裂中的裂纹形核、方向强度面、裂纹扩展和层合结构偏转
- 研究尺度：小应变连续介质/相场尺度，覆盖 2D strength surface、3D 单轴拉伸和层合断裂算例
- 方法类型：单损伤变量 multi-cohesive phase-field model，主材料方向多 cohesive length，变分离散和 Abaqus 热传导类比实现
- 证据类型：SM/MDM/MCM 强度面解析比较、方向临界应力、二阶稳定性分析、2D/3D 数值裂纹扩展算例
- 目标读者：JMPS 的计算力学、材料力学、断裂/接触/生物力学模型研究者，以及需要把微观机制转译为可计算模型的工程力学读者。
- JMPS 风格定位：这不是单纯应用论文，而是把一个具体物理现象放入可推导、可计算、可验证的力学框架中；文章的价值主要来自“模型如何闭合机制”而不是只报告性能或现象。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要采用 JMPS 常见的“问题对象 -> 模型动作 -> 验证/结果 -> 物理意义”压缩方式。第一层交代研究对象和旧方法不足，第二层用方法动词建立本文身份，第三层给最核心的趋势或机制发现，最后把结果回收到领域意义。
- 背景句承担什么：背景句把 各向异性相场断裂的形核强度校准 写成一个需要定量模型的力学问题，使读者知道这不是孤立算例，而是材料/结构/生物系统中的普遍机制。
- gap 句承担什么：gap 句不是空泛地说“尚不清楚”，而是强调 标准单损伤各向异性模型主要控制 fracture energy 和裂纹扩展方向，对 crack nucleation 强度的方向性调节不够灵活；多损伤变量模型更灵活但成本和强度面光滑性存在代价。 这类具体缺口；它把本文方法复杂度合理化。
- 方法句承担什么：方法句用 单损伤变量 multi-cohesive phase-field model，主材料方向多 cohesive length，变分离散和 Abaqus 热传导类比实现 明确告诉读者本文提供的是“可计算框架”而非经验解释。
- 结果句承担什么：结果句服务于主张：在单相场变量框架中引入主方向不同 cohesive lengths，可比标准各向异性相场更灵活地校准裂纹形核强度，同时避免多损伤变量模型的计算和切换复杂性。
- 意义句承担什么：意义句通常回到 JMPS 读者关心的尺度桥接、机制解释、边界条件或可复现计算。
- 一句话主张：在单相场变量框架中引入主方向不同 cohesive lengths，可比标准各向异性相场更灵活地校准裂纹形核强度，同时避免多损伤变量模型的计算和切换复杂性。
- 3-5 个核心关键词：机制化建模；定量验证；尺度桥接；边界条件；可复用图表叙事。

## 3. 选题层深拆
- 问题来源：各向异性相场断裂的形核强度校准 中存在一个典型 JMPS 式张力：微观机制已被观察或假设，但宏观/中尺度响应需要更干净的定量解释。
- 问题为什么重要：如果不能解释 各向异性相场断裂的形核强度校准，相关材料或系统的设计只能停留在经验层面；本文试图把现象转成可计算的变量、参数和图表证据。
- 问题为什么现在值得做：一方面已有文献积累到足以支撑模型假设，另一方面数值工具/实验观测/原子模拟数据已经允许作者把旧问题推进到更一般条件。
- 问题边界：本文的研究边界并不无限扩张，而是绑定在 小应变连续介质/相场尺度，覆盖 2D strength surface、3D 单轴拉伸和层合断裂算例；超出这些假设的真实结构、复杂加载、材料散布或动态演化，需要后续验证。
- 选题的 JMPS 味道：JMPS 喜欢“现象 + 物理机制 + 数学/数值框架”的组合。本文不是把某个软件跑一遍，而是把 各向异性材料相场断裂中的裂纹形核、方向强度面、裂纹扩展和层合结构偏转 中的核心驱动因素拆成可推导、可比较、可被图表支撑的 claims。
- 选题可迁移性：可迁移到任何“局部机制决定整体响应”的论文：先找到局部事件，再建立上层响应，再用图表证明局部事件如何改变整体曲线或形貌。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：文章通常把前人分成三类：基础物理/经典理论，数值或实验观测，最近的模型扩展。这样做的好处是 gap 不会变成“我没看到别人做”，而是“每类方法都解决了一部分，但组合起来仍缺本文这块”。
- 主要研究流派/方法路线：一类路线提供机理概念，一类路线提供可计算工具，一类路线提供可验证数据或图像。本文站在第二类和第三类之间，试图让概念能落到计算证据上。
- 每类研究解决了什么：经典理论提供术语和物理边界；数值/实验研究证明现象真实存在；近期模型展示了可行性或局部趋势。
- 每类研究留下什么不足：经典理论往往假设理想化，数值观测可能尺度小或难推广，实验图像可能只能观察结果而不能分解局部驱动力。本文的 gap 正是这些不足的交叉点。
- 本文站在哪条线上：真实创新是把 anisotropic nucleation calibration 放到 cohesive degradation/length scale 设计中，同时保留单变量相场；文章用强度面、方向临界应力和稳定性分析把贡献说清楚。
- 最接近前人工作：从文本看，作者通常会引用与方法最接近的模型或与现象最接近的实验/模拟，并把本文定位为扩展、整合或更一般化。
- 是否公平处理前人：整体较公平。文章没有简单否定旧方法，而是承认已有贡献，再指出其不适用条件或未覆盖变量。审稿时仍需检查是否遗漏最新相邻工作。

## 5. Gap 制造机制
- 明示 gap：标准单损伤各向异性模型主要控制 fracture energy 和裂纹扩展方向，对 crack nucleation 强度的方向性调节不够灵活；多损伤变量模型更灵活但成本和强度面光滑性存在代价。
- 隐含 gap：隐含缺口是“现象层证据”与“可预测模型”之间仍有距离。读者可能知道现象存在，但不知道在给定参数、几何、加载或材料条件下如何定量判断。
- gap 类型：方法 gap、机制 gap、尺度桥接 gap 和验证 gap 的组合；具体权重随本文主题而变。
- gap 证据来自哪里：来自引言中文献分类、方法部分对旧模型限制的说明、以及结果部分把基线和新框架并排比较的图表。
- gap 是否足够窄：足够窄。本文没有试图解决整个领域，而是围绕 各向异性材料相场断裂中的裂纹形核、方向强度面、裂纹扩展和层合结构偏转 中一个可建模问题展开。
- gap 是否足够重要：重要，因为它影响模型可信度、设计准则或实验解释；若该 gap 不补，后续结论容易停留在经验或图像层面。
- 如果我是审稿人会如何追问：最可能追问 gap 是否真的没有被最近文献处理；如果只是组合已有工具，本文的新贡献是否超过实现层面；以及结论是否超出了本文假设范围。

## 6. 创新性判断
- 作者声称的贡献：提出或扩展一个可计算/可解析框架，并用多组图表说明它能解释 各向异性相场断裂的形核强度校准 中的关键现象。
- 我判断的真实创新：真实创新是把 anisotropic nucleation calibration 放到 cohesive degradation/length scale 设计中，同时保留单变量相场；文章用强度面、方向临界应力和稳定性分析把贡献说清楚。
- 创新类型：方法创新 + 机制解释 + 证据组织创新。个别文章还包含实验闭环或解析公式贡献。
- 创新强度：中高。创新强度不只来自“新公式”，还来自作者把一个复杂现象整理成可被验证的 claims，并逐一提供证据。
- 创新必要性：必要性由 gap 支撑；如果没有本文方法，关键问题要么只能被定性解释，要么只能在更窄条件下模拟。
- 创新与证据匹配度：核心方法 claim 与证据匹配较好；更宽泛的设计、普适性或预测性 claim 需要边界控制。
- 容易被挑战的创新点：如果最接近前人已经具备相似功能，本文需要强调差异在变量、边界、可复现性或解释能力上，而不是只换了实现平台。

## 7. 论证链条复原
背景：复合材料、陶瓷和生物材料的断裂具有方向相关 stiffness、toughness 和 strength。 -> 文献：标准各向异性相场、多损伤变量模型、cohesive phase-field。 -> gap：现有模型难同时兼顾形核校准灵活性、计算成本和光滑强度面。 -> 问题：能否在单相场变量中独立调节主方向 cohesive length。 -> 方法：提出 MCM，推导能量泛函、变分离散、不可逆约束和 admissible stress domain。 -> 证据：SM/MDM/MCM 强度面比较、数值验证、裂纹扩展算例。 -> 发现：MCM 强度面更灵活且光滑，可产生方向性形核和层合偏转。 -> 机制：cohesive length 调节局部强度尺度而不是只调 fracture energy。 -> 意义：为工程各向异性断裂标定提供更可控单变量模型。

这条链条的优点是闭合度较高：问题不是凭空抛出，方法不是孤立技术，图表也不是装饰。最薄弱环节通常在“发现 -> 机制 -> 意义”的外推：模型内趋势是否能成为真实材料/系统规律，需要更强数据或实验验证。

## 8. 方法/理论/模型细拆
- 方法总框架：方法总框架先定义三类模型：SM 使用单损伤变量与经典各向异性 fracture energy；MDM 使用多个损伤变量控制不同方向；MCM 保持单变量但在 asymptotically cohesive degradation 中引入不同 cohesive lengths。关键变量包括相场 d、regularization length、主材料方向结构张量、cohesive lengths、fracture toughness 和弹性张量。核心假设是小应变、正交各向异性、给定主材料方向、相场不可逆和非负约束。文章的可复现性较好：公式、时间离散、约束处理和数值算例参数都较完整；不足是缺少真实材料标定案例。
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
| MCM 比标准各向异性相场更灵活地校准多轴强度面 | Sections 2-3 | Fig. 4-6 的 admissible domain、strength surface 和数值标记验证 | 解析推导 + 数值验证 | 强 | 材料真实强度面是否光滑需实验支持 |
| MCM 保留单 damage variable，避免 MDM 的多变量成本和不连续切换 | 模型构建/结论 | SM/MDM/MCM 能量泛函对照，结论强调 single phase-field variable | 理论比较 | 中强 | 实际计算成本比较没有作为主图量化 |
| 不同 cohesive lengths 可控制方向临界应力 | Section 3.3 | 方向临界应力极坐标图和公式推导 | 解析公式 + 图示 | 强 | 受参数识别和材料对称性限制 |
| 各向异性对均匀解二阶稳定性有应力态依赖 | Appendix/结论 | 体积应力与单轴应力下 Rayleigh ratio/eigenvalue 分析 | 稳定性分析 | 中强 | 附录性质较强，正文读者可能不易消化 |
| MCM 能在 2D/3D 算例中产生方向性裂纹扩展和层合偏转 | Section 4 | Fig. 7-15 的单轴、compact tension、layered/laminate crack surfaces | 有限元算例 | 中 | 多为理想算例，缺少实验路径对比 |

这张表说明本文的证据组织不是平均铺开，而是围绕少数强 claim 逐层加固。最值得学习的是作者通常先建立 baseline，再展示新变量带来的差异，最后讨论边界。最需要警惕的是图像/曲线的视觉说服力可能强于统计说服力，因此涉及图像本体处都应回到 PDF 核查。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Table 1 | 材料和模型参数设置 | 给出强度面/算例基准 | 保证模型比较可追踪 | 否 |
| Fig. 1 | 方向相关 Young 模量 | 定义各向异性背景 | 让读者看到材料方向性输入 | 是 |
| Fig. 2-3 | SM 与 MDM strength surface 和 directional critical stress | 现有模型的灵活性与局限 | 为提出 MCM 铺垫对照 | 是 |
| Fig. 4-5 | MCM admissible domain、strength surface 和极坐标强度 | MCM 可调且光滑 | 核心理论图 | 是 |
| Fig. 6 | MCM 强度面数值验证 | 解析 strength surface 与数值形核一致 | 封闭理论-计算链条 | 是 |
| Fig. 7-15 | 3D 单轴、compact tension、layered/laminate 裂纹路径 | 模型能处理复杂方向性裂纹扩展 | 把解析模型推向可用算例 | 是 |
| Fig. B.16-B.17 | 均匀解稳定性补充 | cohesive length/各向异性影响稳定性 | 解释模型边界和数值行为 | 是 |

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

> 自动分析说明：以下基于 `jmps/文本/txt/A-variational-phase-field-model-for-anisotropic-_2026_Journal-of-the-Mechani.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：24
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Energy density functional | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.1 Energy density functional of the SM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1.2 Energy density functional of the MDM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1.3 Energy density functional of the proposed MCM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Time-discrete variational formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Irreversibility and non-negativity constraints | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Admissible strain and stress domains, strength surfaces | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.5 Directional critical stress under uniaxial conditions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Standard model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.1 Strength surface of the SM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1.2 Directional critical stress of the SM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Multi-damage model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2.1 Strength surfaces of the MDM | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

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

- Top 高频词：stress(85)；damage(68)；model(61)；fracture(57)；eld(56)；strength(53)；cohesive(52)；phase-(50)；crack(48)；models(46)；ratio(46)；material(44)；energy(40)；homogeneous(40)；tensor(40)；solution(39)；anisotropic(37)；critical(37)；erent(36)；degradation(31)
- 高频学术名词：stress(85)；solution(78)；model(61)；fracture(57)；material(44)；energy(40)；degradation(31)；strain(30)；stability(29)；direction(28)；analysis(26)；structure(24)；nucleation(23)；function(23)；mechanism(22)；conditions(22)
- 高频学术动词：proposed(26)；investigate(9)；shows(8)；derive(7)；shown(5)；propose(4)；demonstrate(3)；predict(2)；compared(2)；show(2)；demonstrated(2)；capture(1)；compare(1)；evaluated(1)；developed(1)；investigated(1)
- 高频形容词：homogeneous(80)；anisotropic(74)；critical(74)；elastic(54)；cohesive(52)；material(44)；local(38)；erent(36)；variable(27)；numerical(24)；directional(23)；uniaxial(21)；admissible(20)；volumetric(18)；unstable(16)；structural(15)
- 高频副词/连接副词：however(11)；numerically(10)；purely(10)；respectively(10)；ciently(7)；consequently(6)；moreover(6)；finally(6)；independently(5)；apply(5)；generally(4)；analytically(4)；rely(4)；asymptotically(4)；easily(4)；therefore(3)
- 高频二词短语：phase- eld(50)；homogeneous solution(34)；strength surface(30)；critical stress(28)；fajardo lacave(27)；energy density(20)；cohesive lengths(19)；directional critical(19)；tension test(19)；rayleigh ratio(18)；degradation function(13)；stress state(13)；eld models(12)；strength surfaces(12)；zolesi maurini(12)；damage variable(12)
- 高频三词短语：directional critical stress(16)；phase- eld models(12)；stability homogeneous solution(11)；admissible strain stress(10)；strain stress domains(10)；single-edge notched tension(10)；notched tension test(10)；phase- eld variable(9)；critical stress components(7)；variational phase- eld(6)；phase- eld model(6)；multiple damage variables(6)

**主动、被动与句法**

- 被动语态估计次数：98
- `we + 动作动词` 主动句估计次数：18
- 名词化表达估计次数：736
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：196
- 一般过去时线索：19
- 现在完成时线索：7
- 情态动词线索：19
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：anisotropic(7)；fracture(7)；phase-(5)；eld(5)；model(5)；crack(5)；cohesive(4)；nucleation(4)
- 1. Introduction：models(26)；model(22)；fracture(20)；phase-(16)；eld(16)；anisotropic(15)；damage(14)；variable(11)
- 2.1. Energy density functional：energy(4)；density(4)；eld(4)；damage(4)；functional(3)；generalized(3)；phase-(3)；array(3)
- 2.1.1. Energy density functional of the SM：function(5)；tensor(4)；fracture(3)；model(3)；energy(3)；sti(3)；ness(3)；degradation(3)
- 2.1.2. Energy density functional of the MDM：bleyer(4)；alessi(4)；mechanisms(4)；fracture(3)；damage(3)；energy(3)；function(3)；phase-(2)
- 2.1.3. Energy density functional of the proposed MCM：degradation(11)；tensor(6)；single(4)；functions(4)；model(3)；phase-(3)；eld(3)；variable(3)
- 2.2. Time-discrete variational formulation：time(10)；damage(7)；conditions(6)；variables(4)；boundary(4)；variational(3)；elds(3)；eld(3)
- 2.3. Irreversibility and non-negativity constraints：eld(5)；phase-(4)；conditions(3)；kkt(2)；variables(2)；penalty(2)；term(2)；set(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

### 14.1 问题与 gap 表达
- 原文表达模式：先确认 `各向异性相场断裂的形核强度校准` 的领域重要性，再用 `however/despite/current models` 把问题收束到具体模型缺口。gap 不写成泛泛的“研究不足”，而是绑定到某个旧框架不能解释、不能预测或不能经济计算的对象。
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
- 原文表达模式：机制句多用 `suggest/indicate/can be attributed to/arises from`，避免把模型内解释写成绝对因果。机制解释围绕局部变量如何重分配能量、应力、驱动力或概率展开，同时承认 `最大攻击面是参数增加后的实验标定问题：如果没有多轴强度数据，cohesive lengths 的物理唯一性可能被质疑。另一个风险是理想算例多、真实材料验证少。图像需核查强度面差异、裂纹路径是否确实沿材料方向偏折以及层合算例边界条件。` 可能限制外推。
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
- 最大攻击面：最大攻击面是参数增加后的实验标定问题：如果没有多轴强度数据，cohesive lengths 的物理唯一性可能被质疑。另一个风险是理想算例多、真实材料验证少。图像需核查强度面差异、裂纹路径是否确实沿材料方向偏折以及层合算例边界条件。
- claim 是否过强：核心方法 claim 基本可接受；普适性、设计准则或预测性 claim 需要加限定语。
- 证据是否不足：主要不足不是“没有证据”，而是证据范围有限，常集中于理想化算例、少量样本或模型内参数扫描。
- 方法是否可复现：公式和参数较充分，但代码、网格、图像判读和实验原始数据仍可能影响复现。
- 对比是否充分：与最接近前人的对比是审稿关键；若只有定性对照，建议后续增加同条件基准。
- 边界条件是否清楚：多数边界在方法和结论中有说明，但读者需要把这些边界与每个 claim 对应起来。
- 替代解释是否排除：模型通常能解释现象，但未必排除所有替代机制。Discussion 需要保持“解释力”而非“唯一因果”。
- 图表是否需要进一步核查：需要。所有云图、裂纹形貌、拟合曲线、能量路径、滑移区域和构型力方向都应结合 PDF 图像核查。

## 17. 可复用资产
- 可复用选题角度：可复用的是“先把已有模型并排定义 -> 推出新模型 -> 用解析强度面而非只用算例证明差异 -> 再展示复杂算例”的理论论文结构。图表可学：强度面、极坐标临界应力、解析-数值标记重合图、层合裂纹路径图。不宜直接模仿的是没有解析性质时只堆裂纹路径算例。
- 可复用 gap 制造方式：把旧模型的适用边界写清楚，再把本文变量放在该边界之外。
- 可复用论证链：`现象/工程痛点 -> 经典理论或旧模型 -> 具体 gap -> 新框架 -> 基线验证 -> 参数扫描 -> 机制解释 -> 边界控制`。
- 可复用图表设计：基线图、模型示意图、参数扫描图、核心机制图、补充边界图。
- 可复用段落结构：主题句先告诉读者本段要证明什么，中间用图表/公式推进，结尾回到 claim 或引出下一变量。
- 可复用句型骨架：`To isolate the role of X, we compare A with B under otherwise identical conditions.`；`The observed transition from A to B indicates that C becomes dominant.`；`This result should be interpreted within the limits of D.`
- 可复用引用组织：经典理论用于合法性，近期文献用于前沿性，最接近前作用于 novelty，应用文献用于意义。
- 不宜直接模仿之处：如果没有相当强的图表证据和边界说明，不宜模仿强标题、复杂模型或跨尺度外推。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：写类似论文可以学如何把模型贡献转换为可视化强度面；Introduction 可迁移“标准模型不足 + 多变量模型代价 + 本文折中”的三段逻辑；Method 要交代变量与约束；Results 要先证明模型性质再给漂亮裂纹图；避免缺少最接近模型的公平对比。
- 可以迁移到 Introduction 的写法：先把问题讲成“旧模型边界内的未解变量”，再给本文可解决的窄问题。
- 可以迁移到 Method 的写法：先给框架图或总公式，再逐步解释变量、假设和求解流程。
- 可以迁移到 Results/Discussion 的写法：每个结果小节只服务一个 claim；讨论中把机制解释和局限分开写。
- 需要避免的问题：不要让方法复杂度超过证据强度；不要把模型内趋势写成真实世界普适规律；不要遗漏最接近对照。

## 19. 最终浓缩
- 这篇论文最值得学：本文最值得学的是把“可调参数”写成“可校准物理量”，并用解析图形证明它不是任意复杂化。
- 这篇论文最大风险：模型或证据的适用边界被读者忽略，导致结论外推过度。
- 三个可迁移动作：
  1. 用一个清晰 baseline 让新方法的增量可见。
  2. 把每张关键图绑定到一个明确 claim，而不是把图当作结果陈列。
  3. 在结论中主动说清楚哪些发现稳、哪些只是模型内启发、哪些需要 PDF 图像或后续实验核查。
