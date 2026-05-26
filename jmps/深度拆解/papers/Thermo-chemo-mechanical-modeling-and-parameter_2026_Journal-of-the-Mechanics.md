# Thermo-chemo-mechanical modeling and parameter identification of epoxy resin curing

## 0. 读取说明
- 源 PDF：`jmps/文献/Thermo-chemo-mechanical-modeling-and-parameter_2026_Journal-of-the-Mechanics.pdf`
- 源 TXT：`jmps/文本/txt/Thermo-chemo-mechanical-modeling-and-parameter_2026_Journal-of-the-Mechanics.txt`
- 辅助参照：上一轮标准拆解用于校验论文主线，本文件重新基于全文目录、摘要、图注、实验和模型段落展开。
- 是否需要结合 PDF 图像核查：需要。TXT 可读出实验设计、图注、参数识别路径和验证叙事，但图中的拟合质量、误差条、DIC/红外热像场分布必须结合 PDF 核查。
- 本文类型：热-化-力耦合本构模型 + 参数识别方法 + 实验/有限元验证。它是工程本构长文，证据由实验矩阵、热力学推导、参数表和验证算例共同构成。
- 阅读覆盖：摘要、Introduction、拉伸/松弛/流变实验、自由能与 Clausius-Duhem 推导、演化方程、热传导方程、参数识别、热-力验证、Conclusions and outlook、附录。

## 1. 基本信息与论文身份
- 题名：Thermo-chemo-mechanical modeling and parameter identification of epoxy resin curing
- 作者/机构：Chris Leistner 等；完整作者与机构需以 PDF 首页为准，元数据仅记录第一作者。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106666。
- DOI：10.1016/j.jmps.2026.106666
- 关键词：Curing；Epoxy resin；Constitutive modeling；Parameter identification。
- 研究对象：环氧树脂体系在固化过程中和固化后的温度、固化度、黏塑性、松弛、滞回与热释放耦合行为。
- 研究尺度：材料点本构 + 试样实验尺度 + 有限元验证尺度；主要为小应变框架。
- 方法类型：热力学一致本构推导、Maxwell overstress、温度/固化度 shift 函数、多步非线性最小二乘参数识别、拉伸与流变实验、DIC/红外热像验证、有限元高阶自适应时间积分。
- 证据类型：单调拉伸、长时松弛、多步松弛、流变多波加载、参数唯一性/局部可识别性讨论、参数表、固化模具验证中温度/位移/应力演化对比。
- 目标读者：复合材料制造仿真、本构建模、固化残余应力、参数识别和有限元实现读者。
- JMPS 风格定位：典型“模型-参数-验证闭环”的本构论文。JMPS 味道在于热力学一致性和识别唯一性，而不只是拟合曲线。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先提出环氧树脂作为复合材料基体的重要性和热黏塑行为；再指出缺少描述固化过程热-化-力耦合性质的本构模型；随后说明本文发展热力学一致、温度与固化度相关模型；接着介绍实验表征和 overstress 参数识别；最后用全场实验和有限元验证能力。
- 背景句承担什么：把研究对象与纤维增强复合材料制造直接相连，说明不是孤立材料模型。
- gap 句承担什么：指出“固化过程 + 固化后 + 热力学一致 + 黏塑/松弛”尚未统一。
- 方法句承担什么：强调模型不仅依赖公式，还依赖可识别参数和实验矩阵。
- 结果句承担什么：宣称提出 novel parameter identification concept，并通过验证算例展示能力。
- 意义句承担什么：将模型定位为分析环氧树脂固化过程和制造残余应力的工具。
- 一句话主张：本文构建了一个热力学一致、温度和固化度依赖的环氧树脂热-化-力黏塑性本构模型，并通过多步实验识别策略使复杂 Maxwell overstress 参数可局部唯一确定。
- 3-5 个核心关键词：thermodynamic consistency；degree of cure；overstress；multi-step parameter identification；curing validation。

## 3. 选题层深拆
- 问题来源：复合材料制造中的固化收缩、温升、玻璃化、残余应力和后固化力学性能都由树脂本构控制。已有模型常只覆盖热化学或固化后黏弹响应，难以同时处理固化中与固化后。
- 问题为什么重要：树脂是纤维复合材料基体，固化残余应力会影响翘曲、开裂、界面损伤和制造质量。若本构模型不能覆盖温度和固化度依赖，工艺仿真会失真。
- 问题为什么现在值得做：实验设备能同时提供拉伸松弛、流变和全场温度/位移数据；有限元时间积分和参数优化工具足以处理多 Maxwell 元件；工业上对工艺仿真的需求强。
- 问题边界：小应变；材料体系为特定 epoxy resin；验证主要是固化热-力过程，作者承认没有显式验证固化中外加机械载荷下的响应。
- 选题的 JMPS 味道：不是简单工程拟合，而是把热力学一致性、Clausius-Duhem 不等式、参数唯一性和实验验证一起写。
- 选题可迁移性：可以迁移为“复杂材料模型必须同时回答：物理一致吗？参数可识别吗？能在边值问题中验证吗？”

## 4. 领域位置与文献版图
- 作者如何划分已有研究：固化动力学和热模型；固化相关黏弹/黏塑本构；热力学一致自由能框架；拉伸/流变实验表征；Prony/Maxwell 参数识别和非线性最小二乘方法。
- 主要研究流派/方法路线：经验固化模型能拟合热释放；黏弹模型能描述松弛；热化学模型能描述温度和固化度；多场本构模型试图统一；参数识别文献处理非唯一性和过拟合。
- 每类研究解决了什么：提供固化度演化、温度依赖、固化后力学、松弛谱识别和有限元实现基础。
- 每类研究留下什么不足：通常不能同时适用于固化过程和固化后；多 Maxwell 元件参数存在非唯一；三维应力状态下用一维拉伸数据识别容易偏差；验证常停留在校准曲线。
- 本文站在哪条线上：整合本构模型和参数识别两条线，并把验证推进到全场固化实验。
- 最接近前人工作：作者团队先前热固化模型、固化动力学模型、黏弹/overstress 参数识别工作，以及环氧树脂固化实验文献。
- 是否公平处理前人：总体公平，语气以继承和补足为主，很少直接否定；gap 通过“尚未同时满足”构造。

## 5. Gap 制造机制
- 明示 gap：缺少一个能描述固化过程热-化-力耦合、又可在固化后继续适用的热力学一致环氧树脂本构模型。
- 隐含 gap：即使模型形式存在，如果参数不能唯一识别或只能在一维假设下拟合，也难以进入可靠有限元工艺模拟。
- gap 类型：模型整合 gap + 参数识别 gap + 验证 gap。
- gap 证据来自哪里：Introduction 长综述把已有模型、实验和识别方法分组；实验段展示材料有温度相关松弛与滞回；参数识别段说明 Maxwell 参数必须精细处理。
- gap 是否足够窄：相对宽，但被收束到一个材料体系、一个小应变本构框架和一套识别流程。
- gap 是否足够重要：重要。工程仿真常受材料参数质量限制，本文把参数识别作为核心贡献，而非附属步骤。
- 如果我是审稿人会如何追问：模型复杂度是否超过验证覆盖？Maxwell 元件数量如何选？滞回平衡应力的物理意义是否清楚？外部机械载荷固化中未验证是否削弱主张？作者在 conclusion 中承认最后一点。

## 6. 创新性判断
- 作者声称的贡献：提出热力学一致温度/固化度依赖本构；发展新的参数识别概念；保证 overstress 参数唯一性；用全场实验和 FE 验证固化过程。
- 我判断的真实创新：最大贡献不是单个自由能项，而是“实验矩阵 + 多步识别 + 模型验证”流程。它将 fully cured tensile tests 和 curing rheometry 串起来，并在三维加载状态下修正一维参数识别偏差。
- 创新类型：本构整合、参数识别方法、工程验证。
- 创新强度：中强。物理机制多来自已有黏弹/固化理论，但组合的完整性和可复现路径有价值。
- 创新必要性：必要。若只给复杂模型而无唯一参数，模型无法用于预测；若只做实验拟合而无热力学一致性，难以说服 JMPS 读者。
- 创新与证据匹配度：参数识别和固化验证证据较充分；“固化中外部机械加载可预测”证据不足，作者没有过度展开。
- 容易被挑战的创新点：多步识别可能隐藏参数相关性；shift 函数形式可能经验化；模型在未测试工况下外推能力不明。

## 7. 论证链条复原
背景：环氧树脂固化控制复合材料制造质量，固化中材料从液态到固态并伴随热释放、收缩、玻璃化和黏塑响应。

文献：已有固化动力学、黏弹/黏塑和热化学模型分别覆盖部分过程，但很少同时满足热力学一致、固化后适用、参数可识别和边值验证。

gap：模型完整性与参数唯一性没有闭合。

问题：如何构建并识别一个可用于固化过程有限元模拟的热-化-力本构模型？

方法：设计 fully cured 拉伸/松弛和 rheometry 实验；从运动学、自由能和 Clausius-Duhem 不等式推导应力分解与演化方程；提出 reduced/multi-step 参数识别。

证据：参数表、拟合曲线、长时松弛外推、多步松弛、流变固化曲线、验证模具全场温度和位移。

发现：模型可同时捕捉温度依赖松弛、滞回平衡应力、固化相关流变演化和验证实验中的热-力响应。

机制：固化度通过 shift 函数、连接元件和内变量演化改变材料从液态到固态的承载路径；overstress Maxwell 元件描述长时间尺度松弛。

意义：为复合材料制造仿真提供更可靠材料模型，同时指出外加载固化验证仍需未来完成。

## 8. 方法/理论/模型细拆
- 方法总框架：实验先行，模型中场变量和参数都有实验来源；本构上采用小应变热黏塑框架，应力由弹性平衡、滞回平衡和 overstress 组成；热方程耦合固化放热。
- 关键概念：degree of cure；thermo-viscoplasticity；overstress；Maxwell elements；shift functions；Clausius-Duhem inequality；equilibrium hysteresis；local identifiability。
- 关键变量/参数：温度 `T`、固化度、应变及其分解、固体应变、黏性应变、滞回内变量、Maxwell 元件参数、固化动力学参数、热传导参数。
- 核心假设：小应变；各向同性或工程上可接受的简化；实验子集能分离参数组；长时松弛可外推平衡点；温度和固化度依赖可由 shift 函数表示。
- 边界条件：实验识别中有单轴拉伸、松弛保持、多步加载和流变剪切；验证中用铝模/树脂几何和热边界条件模拟固化。
- 方法步骤：1. 用单调拉伸确定载荷边界和速率效应；2. 用长时/多步松弛识别平衡与松弛；3. 用流变固化数据识别固化相关参数；4. 写自由能并由不等式推应力；5. 分组识别参数；6. 在 FE 中验证固化实验。
- 复现信息：论文给出实验加载路径、参数表、识别步骤和附录数据；真正复现仍需原始数据、优化权重、初值和代码。
- 方法复杂度是否合理：基本合理，因为研究目标是固化全过程；但复杂度与验证覆盖之间存在张力，是审稿风险。
- 方法与 gap 的对应关系：模型完整性对应热-化-力耦合；识别流程对应参数唯一性；验证算例对应工程可用性。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 环氧树脂固化需要热-化-力耦合本构 | Introduction、摘要 | 复合材料制造背景、温度/固化度/松弛实验现象 | 文献 + 实验 | 强 | 对特定树脂外推需谨慎 |
| 本文模型热力学一致 | 第 3 节 | 自由能结构、Clausius-Duhem 不等式评价、演化方程 | 理论推导 | 强 | 符号和假设需 PDF 核查 |
| overstress 参数需要精细识别以确保唯一性 | 摘要、第 4 节 | 多 Maxwell 元件、reduced approach、multi-step identification | 参数识别论证 | 中强 | 局部唯一不等于全局唯一 |
| 模型能拟合固化后温度相关松弛与滞回 | 第 2、4 节 | 单调拉伸、长时松弛、多步松弛曲线 | 实验拟合 | 中强 | 图中误差和外推需核查 |
| 模型可描述流变固化过程 | 第 2.2、4.2.2 | rheometry multiwave 测试、固化参数识别 | 实验拟合 | 中强 | 流变到三维固化应力的转化有假设 |
| FE 验证展示固化热-力响应能力 | 第 5 节 | 全场实验数据与 FE 温度/位移/应力演化对比 | 验证算例 | 中 | 未显式验证外部机械载荷固化中响应 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1-2 | 拉伸试样几何和加载路径 | 实验矩阵可复现 | 让参数识别来源清楚 | 是 |
| Fig. 3-4 | 长时/多步松弛数据 | 存在温度相关松弛与滞回 | 支撑 overstress 和 hysteresis 结构 | 是 |
| Fig. 5 及流变图 | rheometry loading | 固化过程剪切/流变参数来源 | 支撑固化相关参数识别 | 是 |
| 自由能公式组 | 热力学一致性 | 模型结构合理 | 从能量而非经验项出发 | 否，需核对符号 |
| Clausius-Duhem 推导 | 演化方程合法性 | 热力学一致 | 约束应力和内变量形式 | 否 |
| 表 4/5 类参数表 | 参数可复现 | 多步识别完整 | 给出工程可用模型 | 是，需核查表项 |
| Fig. 15-16 类拟合图 | 校准质量 | 模型捕捉实验响应 | 显示曲线拟合和偏差 | 是 |
| Fig. 18-21 类验证图 | 固化模具验证 | 模型可用于边值问题 | 连接材料点模型与 FE | 是 |

图表顺序服务论证的方式：先给实验路径和数据，说明模型不是凭空设定；中间用公式和表格建立可复现模型；后段用校准图和验证图逐步升级说服力。工程本构论文尤其依赖这种“数据-模型-参数-验证”的图表节奏。

## 11. 章节结构与篇章布局
- Abstract：按重要性、gap、模型、识别、验证五步组织。
- Introduction：长而密，按本构模型、实验表征、参数识别三条线组织文献，最后引出本文贡献。
- Related Work/Background：无独立章节，但 Introduction 实质上承担 Related Work。
- Method/Theory/Model：第 3 节是理论主体，从运动学到自由能、不等式、演化方程和热方程。
- Results：第 4 节参数识别是结果与方法混合章节；第 5 节是独立验证结果。
- Discussion：讨论分布在识别偏差、验证偏差和 Conclusion 中。
- Conclusion：回收模型能力，同时明确未来要验证固化中外加机械载荷。
- 章节之间如何过渡：实验章节为模型和参数服务；模型章节为参数识别服务；识别章节为验证服务。
- 哪一节最值得模仿：第 4 节。它把复杂参数识别拆成 reduced approach 和 multi-step workflow，是本构论文最容易被复用的部分。
- 哪一节可能存在结构风险：第 3 节符号密集，若读者只想看模型使用方法，阅读成本高。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Thermo-chemo-mechanical-modeling-and-parameter_2026_Journal-of-the-Mechanics.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：23
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Experiments | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Uniaxial tensile tests | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.1 Monotonic tensile tests | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.2 Long-term relaxation tests | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.3 Multi-step relaxation tests | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Rheometrical tests | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Constitutive modeling | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Kinematics and stress decomposition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Structure of free energy | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Evaluation of the Clausius-Duhem inequality | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.3.1 Spherical and deviatorical part of elastic equilibrium stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3.2 Hysteretic equilibrium stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3.3 Overstress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：工程背景 -> 现有模型类型 -> 实验表征需求 -> 参数识别难题 -> 本文贡献。每段通常以一类文献开头，以不足或本文需求收束。
- Method 段落推进：定义变量 -> 给自由能或演化方程 -> 由热力学约束解释其合理性 -> 说明参数如何识别。
- Results 段落推进：先给实验曲线或识别步骤，再讨论参数意义、唯一性或偏差来源。
- Discussion/Conclusion 段落推进：先总结模型覆盖能力，再主动承认验证尚未包含外部机械加载。
- 常见段落开头方式：`In order to...`；`Based on the experimental observations...`；`Special attention is paid to...`。
- 常见段落收束方式：以参数识别需求、模型模块选择或未来验证边界收束。
- 可复用段落模板：复杂模型段可写成“观察到 X 行为 -> 因此引入 Y 内变量/能量项 -> 热力学约束给出演化形式 -> 参数由 Z 实验识别”。

## 13. 文笔画像与语言习惯
- 整体语气：工程化、严谨、流程感强。作者少用戏剧性语言，更多强调 consistency、identification、validation。
- claim 强度：对模型结构较强，对应用能力使用 `demonstrate the capabilities` 这类中等强度表述。
- 谨慎表达：`first validation`、`not explicitly validate`、`future work`、`can be caused by`。
- 问题表达：`has yet to be established`、`particularly challenging`、`must be performed meticulously`。
- 贡献表达：`we develop`、`we introduce`、`we validate`、`we discuss`。
- 机制表达：`temperature shift`、`curing shift`、`overstress`、`equilibrium hysteresis`、`degree of cure`。
- 对比表达：多用“与已有方法相比覆盖更完整”，较少尖锐批判。
- 限定边界表达：小应变、特定树脂、验证工况、未覆盖外加载等。
- 术语密度：很高，尤其第 3-4 节；术语跨热学、化学固化、黏塑性和数值积分。
- 长句/短句习惯：介绍模型和识别时长句多；结论列表和贡献表述较短。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：eqh(125)；eqe(106)；model(96)；temperature(96)；stress(94)；material(91)；curing(90)；part(83)；tests(79)；parameter(76)；relaxation(74)；strain(72)；equilibrium(72)；identi(70)；parameters(58)；leistner(55)；function(55)；experimental(52)；cation(51)；epoxy(49)
- 高频学术名词：model(96)；temperature(96)；stress(94)；material(91)；parameter(76)；relaxation(74)；strain(72)；transition(62)；parameters(58)；function(55)；cation(51)；behavior(49)；validation(42)；dependence(34)；simulation(32)；system(31)
- 高频学术动词：derived(13)；shown(11)；developed(8)；estimated(7)；investigated(5)；investigate(4)；propose(4)；estimate(4)；proposed(3)；evaluate(3)；show(3)；shows(3)；validate(2)；validated(2)；revealed(2)；compared(2)
- 高频形容词：experimental(104)；material(91)；elastic(60)；constitutive(43)；mechanical(40)；hysteretic(36)；thermal(30)；element(24)；viscoelastic(22)；deviatorical(19)；numerical(18)；viscous(18)；erent(17)；various(17)；axial(16)；chemical(16)
- 高频副词/连接副词：fully(17)；additionally(15)；consequently(12)；initially(11)；therefore(7)；however(6)；thermodynamically(6)；purely(6)；furthermore(4)；experimentally(4)；locally(4)；finally(4)；ciently(4)；subsequently(4)；analogously(4)；supply(3)
- 高频二词短语：identi cation(49)；equilibrium stress(48)；eqh eqh(48)；epoxy resin(40)；eqe eqe(37)；relaxation tests(32)；material parameters(29)；constitutive model(28)；experimental data(28)；degree cure(27)；resin system(24)；strain tensor(24)；tensile tests(24)；shift function(22)；free energy(22)；maxwell elements(21)
- 高频三词短语：eqh eqh eqh(26)；epoxy resin system(21)；parameter identi cation(20)；glass transition temperature(18)；eqe eqe eqe(17)；long-term relaxation tests(16)；hybrid free energy(14)；hysteretic equilibrium stress(14)；multi-step relaxation tests(14)；equilibrium stress part(13)；elastic equilibrium stress(11)；curing shift function(10)

**主动、被动与句法**

- 被动语态估计次数：320
- `we + 动作动词` 主动句估计次数：8
- 名词化表达估计次数：1380
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：356
- 一般过去时线索：71
- 现在完成时线索：4
- 情态动词线索：36
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：epoxy(6)；constitutive(6)；model(6)；identi(5)；curing(5)；parameter(4)；cation(4)；resin(4)
- 1. Introduction：curing(33)；part(26)；material(25)；behavior(22)；model(20)；relaxation(18)；temperature(16)；tensor(16)
- 2. Experiments：resin(3)；parts(3)；epoxy(2)；system(2)；tests(2)；araldite(2)；weight(2)；order(1)
- 2.1. Uniaxial tensile tests：tensile(2)；tests(2)；plates(2)；out(2)；experimental(2)；uniaxial(1)；thickness(1)；produced(1)
- 2.1.1. Monotonic tensile tests：tensile(3)；strains(3)；temperatures(3)；axial(3)；stress(3)；monotonic(2)；tests(2)；strain(2)
- 2.1.2. Long-term relaxation tests：tests(7)；relaxation(6)；long-term(4)；times(4)；temperatures(4)；holding(3)；erent(3)；axial(3)
- 2.1.3. Multi-step relaxation tests：relaxation(7)；stress(6)；tests(6)；temperatures(6)；equilibrium(5)；hysteresis(4)；loading(4)；results(4)
- 2.2. Rheometrical tests：shear(4)；strain(4)；tests(3)；behavior(3)；plate(3)；frequency(3)；individual(3)；amplitude(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`Despite this, a constitutive model describing X has yet to be established.`
- 可复用句型骨架：`Despite extensive work on the individual mechanisms, a unified constitutive description of X under Y remains unavailable.`
- 中文写作启发：复杂模型论文要强调“单个机制已有，但统一框架缺失”。

### 14.2 方法与框架表达
- 原文表达模式：`we develop a thermodynamically consistent, temperature- and curing-dependent constitutive model...`
- 可复用句型骨架：`We formulate a thermodynamically consistent model in which A, B, and C enter through coupled internal variables.`
- 中文写作启发：方法句要列出依赖维度，体现模型覆盖范围。

### 14.3 结果与趋势表达
- 原文表达模式：实验显示长时间保持后仍未完全松弛，需要外推平衡状态。
- 可复用句型骨架：`The material does not reach equilibrium within the experimental time window; therefore, an extrapolation procedure is introduced to estimate the equilibrium response.`
- 中文写作启发：把实验限制转化为方法需求。

### 14.4 机制解释表达
- 原文表达模式：温度和固化度 shift 函数调节 Maxwell 元件和固体连接。
- 可复用句型骨架：`The transition from A to B is represented by a curing-dependent shift/connectivity function that progressively activates the load-bearing network.`
- 中文写作启发：用“逐步激活承载网络”解释固化本构很直观。

### 14.5 贡献与意义表达
- 原文表达模式：`we demonstrate the capabilities of the newly developed constitutive model for analyzing curing...`
- 可复用句型骨架：`The validation example demonstrates the capability of the model to reproduce coupled field evolutions in a process-relevant boundary-value problem.`
- 中文写作启发：验证算例的意义在于“过程相关边值问题”，不是单纯拟合。

### 14.6 局限与未来工作表达
- 原文表达模式：未来需验证固化过程中外加机械载荷下的模型响应。
- 可复用句型骨架：`Although the present validation addresses X, direct validation under Y remains necessary and is left for future work.`
- 中文写作启发：结论中明确“已验证”和“未验证”会提升可信度。

## 15. 引用策略与文献使用
- 引用密度：Introduction 极高，模型和识别章节中等，验证章节较低。
- 引用主要集中位置：本构模型类型、固化动力学、参数识别方法和实验表征。
- 经典文献用途：热力学、本构、Maxwell/Prony 识别和固化动力学基础。
- 近年文献用途：说明复合材料制造仿真、固化模型和参数识别仍活跃。
- 方法文献用途：支撑非线性最小二乘、时间积分、DIC/红外或流变实验方法。
- 对比/批判性引用：多数为温和转折：“已有方法有价值，但不覆盖本文全部目标”。
- gap 如何靠引用搭建：通过三个文献组分别证明模型、实验和识别各有局限，最后合成一个“完整闭环缺失”的 gap。
- references 暗示的研究共同体：复合材料工艺、本构理论、实验力学、数值材料建模。
- 引用风险：文献跨度大，容易被审稿人要求补充某类最新固化本构或不确定性识别文献。

## 16. 审稿人视角风险
- 最大攻击面：模型复杂而验证覆盖有限，尤其没有固化中外加载机械响应验证。
- claim 是否过强：若只说“用于分析固化过程”较稳；若外推到所有热-化-力加载，则过强。
- 证据是否不足：参数识别充分，但独立验证场景数量有限。
- 方法是否可复现：参数表和流程有帮助；原始数据和优化细节若不可得，会影响复现。
- 对比是否充分：与已有模型的定量对比不一定充分，更多是功能覆盖对比。
- 边界条件是否清楚：小应变、特定树脂、具体 cure schedule 较清楚。
- 替代解释是否排除：滞回和黏塑分解可能有其他模型形式，本文未穷尽比较。
- 图表是否需要进一步核查：所有拟合图、参数表和验证场图都需 PDF 核查。

## 17. 可复用资产
- 可复用选题角度：把“本构模型”与“参数唯一性”绑定，而不是只提出一个更复杂模型。
- 可复用 gap 制造方式：`已有模型覆盖 A/B/C 的部分组合，但缺少 A+B+C+可识别参数+边值验证`。
- 可复用论证链：实验观察 -> 热力学模型 -> 参数识别流程 -> 校准曲线 -> 独立验证。
- 可复用图表设计：加载路径图、长时松弛图、识别依赖流程图、参数表、校准/验证对比图。
- 可复用段落结构：每一类实验先说明目的，而不是先堆设备参数。
- 可复用句型骨架：`Special attention is paid to...`；`To ensure a locally unique parameter set...`；`This deviation can be attributed to...`。
- 可复用引用组织：复杂工程模型 Introduction 可按“模型-实验-识别”三组文献组织。
- 不宜直接模仿之处：多参数模型需要足够实验矩阵支撑；否则容易显得过拟合。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：复杂模型论文的贡献必须不止公式，还要有参数识别和验证闭环。
- 可以迁移到 Introduction 的写法：把文献不足分成模型不足、实验不足、识别不足三类，最后自然引出本文三项贡献。
- 可以迁移到 Method 的写法：从热力学约束出发，避免经验项堆砌。
- 可以迁移到 Results/Discussion 的写法：在结果中主动讨论参数唯一性、拟合偏差和未验证边界。
- 需要避免的问题：不要让模型能力超过验证；越复杂的模型越需要清楚说明哪些参数由哪些实验识别。

## 19. 最终浓缩
- 这篇论文最值得学：如何把本构模型、参数识别和有限元验证写成一个工程可用的闭环。
- 这篇论文最大风险：模型复杂度与验证覆盖面之间的张力。
- 三个可迁移动作：1. 贡献按 thermodynamics、identification、validation 分层；2. 参数识别写出唯一性/局部可识别性；3. 结论主动标注未验证工况。
