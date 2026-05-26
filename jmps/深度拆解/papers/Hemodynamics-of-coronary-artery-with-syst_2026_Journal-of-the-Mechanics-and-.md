# Hemodynamics of coronary artery with systolic luminal narrowing

## 0. 读取说明
- 源 PDF：`jmps/文献/Hemodynamics-of-coronary-artery-with-syst_2026_Journal-of-the-Mechanics-and-.pdf`
- 源 TXT：`jmps/文本/txt/Hemodynamics-of-coronary-artery-with-syst_2026_Journal-of-the-Mechanics-and-.txt`
- 是否需要结合 PDF 图像核查：需要。本文基于 TXT、metadata、章节树和图注拆解；速度场、相图颜色、箱线图分布和应力云图的视觉细节需结合 PDF。
- 本文类型：生物力学/血流动力学建模与理论分析论文。

## 1. 基本信息与论文身份
- 题名：Hemodynamics of coronary artery with systolic luminal narrowing
- 作者/机构：Zhi-Peng Wang 等；Beihang University、Fudan University、Imperial College London、Tsinghua University 等。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106683。
- DOI：10.1016/j.jmps.2026.106683
- 关键词：Coronary artery; Myocardial bridging; Morpho-hemodynamics; Blood pressure; Stress concentration
- 研究对象：心肌桥导致的冠状动脉收缩期管腔狭窄，重点是左前降支 LADA 的形态-血流-应力耦合。
- 研究尺度：血管几何尺度、心动周期时间尺度、管腔压力/流量尺度、动脉壁和周围心肌应力尺度。
- 方法类型：CFD、简化流体力学模型、各向异性软组织弹性模型、风险分类相图。
- 证据类型：患者/文献几何参数、数值模拟、理论-数值对比、RPD 相图、流量曲线、速度场、应力集中图。
- 目标读者：血管生物力学、计算流体力学、软组织力学、医学工程和 JMPS 机制建模读者。
- JMPS 风格定位：把临床形态问题改写成可推导的 morpho-hemodynamics 问题，是“医学现象 + 连续介质力学 + 风险图谱”的 JMPS 写法。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先说明 myocardial bridging 可能导致严重心血管事件，但其 biomechanical effects 仍不清楚；再提出流体模型和弹性模型；最后给出压缩率、狭窄长度、嵌入深度、桥位置、RPD、流量和应力集中之间的趋势。
- 背景句承担什么：把 MB 从解剖异常提升为有潜在严重后果的力学问题。
- gap 句承担什么：说明现有临床阈值或局部血流研究不足以解释“形态参数如何共同决定风险”。
- 方法句承担什么：交代 CFD 验证、细长分支管道压力模型、含任意孔洞和各向异性本构的应力模型。
- 结果句承担什么：压缩率、长度、嵌入深度增加 RPD；桥位置影响不明显；高压缩率增加应力集中；中等压缩但长狭窄段也可能严重。
- 意义句承担什么：把模型结果回收到预后评估和治疗策略。
- 一句话主张：心肌桥严重性不能只看压缩率，而应把狭窄长度、嵌入深度、压力降、流量和动脉壁应力集中纳入统一力学评价。
- 3-5 个核心关键词：myocardial bridging; relative pressure drop; compression ratio; narrowed length; stress concentration。

## 3. 选题层深拆
- 问题来源：临床上 MB 常见，但不同患者风险差异很大；单一压缩率阈值无法解释所有严重病例。
- 问题为什么重要：MB 与缺血、冠脉痉挛、内皮功能障碍和潜在不良心血管事件相关，风险判断直接影响随访和干预。
- 问题为什么现在值得做：CTA/冠脉几何数据、CFD 和理论流体/弹性模型让形态指标可以转化为可量化力学指标。
- 问题边界：聚焦收缩期管腔狭窄下的 LADA 模型、RPD、主要出口流量、流型与周围组织应力，不做完整血流-血管壁-心肌强耦合 FSI。
- 选题的 JMPS 味道：临床问题只是入口，真正贡献在于把形态变量和力学后果联系起来。
- 选题可迁移性：可迁移为“从工程/医学现象中抽取少数几何和材料控制变量，建立可验证相图”的选题策略。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：临床 MB 诊断与阈值、冠脉 CFD、管道流动理论、软组织孔洞应力集中、心肌纤维化/功能异常关联。
- 主要研究流派/方法路线：单因素压缩率分类路线；患者特异 CFD 路线；理论血管流动阻力路线；血管嵌入软组织应力分析路线。
- 每类研究解决了什么：临床路线提供风险经验，CFD 路线提供局部血流细节，理论路线给可解释指标，弹性力学路线解释应力集中。
- 每类研究留下什么不足：单因素阈值忽略长度和深度；纯 CFD 不易形成快速分类图；血流指标和组织应力机制往往分开讨论。
- 本文站在哪条线上：站在血管生物力学和连续介质理论的交叉线上。
- 最接近前人工作：Javadzadegan 等 LADA 血流数据、Sharzehee 等 MB 几何分类、Bourassa 等临床压缩率阈值。
- 是否公平处理前人：整体是温和补充式写法，承认前人阈值有用，但指出其不能处理变量耦合。

## 5. Gap 制造机制
- 明示 gap：MB 的 biomechanical effects remain poorly understood，尤其缺少能同时解释形态、血流压力降和动脉壁应力的框架。
- 隐含 gap：单一 compression ratio 不能覆盖长度、嵌入深度和流体阻力；流量/压力模型也不能直接说明组织应力风险。
- gap 类型：机制 gap、方法 gap、分类 gap、临床转化 gap。
- gap 证据来自哪里：导言中的临床阈值文献、CFD 文献、患者图像和后文 RPD/纤维化分类比较。
- gap 是否足够窄：足够窄，集中在 systolic luminal narrowing 的 RPD、流量和 stress concentration。
- gap 是否足够重要：足够重要，因为它可能改变中等压缩但长桥患者的风险判断。
- 如果我是审稿人会如何追问：二因素相图是否有足够患者随访支撑？忽略血管顺应性、湍流和 FSI 是否会改变阈值？

## 6. 创新性判断
- 作者声称的贡献：建立经 CFD 验证的管腔压力理论模型；建立动脉嵌入心肌的弹性应力模型；提出基于 RPD 的风险分类。
- 我判断的真实创新：把 MB 风险从单一压缩率推进到压缩率-长度-RPD-应力耦合，并把结果压缩成分类相图。
- 创新类型：应用场景创新 + 理论简化模型 + 分类表达创新。
- 创新强度：中高。强在变量闭环完整；弱在临床外推仍需更多数据。
- 创新必要性：必要。若只用 CFD，难以形成可解释分类；若只用压缩率，容易误判长狭窄段。
- 创新与证据匹配度：压力和流量趋势证据强；纤维化分类和临床预后意义属于中强证据。
- 容易被挑战的创新点：RPD 阈值、纤维化分组、应力集中与内皮功能障碍之间的因果链仍需更大样本验证。

## 7. 论证链条复原
`背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义`：

1. 背景：MB 在收缩期压迫冠脉，可能造成血流异常和心肌风险。
2. 文献：已有临床阈值和 CFD 研究，但多以单因素或特定患者为主。
3. gap：尚缺一个能同时处理 η、l、λ、d、RPD 和应力的统一框架。
4. 问题：形态参数如何改变管腔压力、出口流量和动脉壁应力？
5. 方法：LADA CFD + 细长分支管道压力模型 + 含孔软组织弹性模型。
6. 证据：压力/流量/流型图、理论-数值对比、RPD phase diagram、应力相图。
7. 发现：η、l、d 增加 RPD；λ 影响弱；大 η 增加应力集中；中等 η + 长 l 也可能严重。
8. 机制：形态狭窄增加局部流动阻力，心肌收缩和血压共同导致孔边应力集中。
9. 意义：为 MB 预后预测和治疗策略提供力学依据。

## 8. 方法/理论/模型细拆
- 方法总框架：构建 LADA 几何和不同 MB 参数组，先用 CFD 获得基准流体结果，再推导简化压力模型，并用弹性模型评估嵌入动脉周围组织应力。
- 关键概念：compression ratio η、narrowed length l、bridge location λ、embedded depth d、relative pressure drop、major outlet flow rate、von Mises stress。
- 关键变量/参数：η、l、λ、d、入口速度波形、Windkessel 出口压力、血液流量 q、心肌收缩力、各向异性模量比、孔洞长宽比。
- 核心假设：血管可简化为分支细长管；狭窄段截面可参数化；血流与组织应力分模块处理；材料参数部分取自文献。
- 边界条件：心动周期入口速度，主要出口 Windkessel 压力，收缩期/舒张期划分，不同 MB 几何组。
- 方法步骤：几何建模 -> CFD 验证 -> 理论压降模型 -> RPD 相图 -> 嵌入动脉弹性模型 -> 应力参数图。
- 复现信息：TXT 中包含章节、图注和部分公式线索；完整复现需核查 PDF 公式、表 1 参数、边界条件细节和网格设置。
- 方法复杂度是否合理：合理，流体模型回答压降，弹性模型回答应力，分类图回答应用转化。
- 方法与 gap 的对应关系：每个模型模块直接对应一个 gap：形态-压降、形态-流量、形态-应力、指标-风险分类。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| MB 风险不能只由压缩率判断 | 摘要/3.4 | RPD 相图与纤维化分组，二因素模型优于单因素阈值 | 相图/统计对比 | 强 | 样本量和临床随访不足 |
| η、l、d 增加会提高 RPD | 摘要/3.1/3.4 | CFD 曲线与理论模型参数分析 | 数值+理论 | 强 | 几何简化影响定量阈值 |
| 桥位置 λ 对 RPD 影响不明显 | Results | 不同 λ 模型压力/压降对比 | 参数研究 | 中 | 特定 LADA 几何下成立 |
| MB 降低主要出口流量并改变流型 | 3.2/3.3 | q-t 曲线、速度场、扰动图 | 数值模拟 | 强 | 流场细节需 PDF 核查 |
| 大压缩率显著增加动脉壁应力集中 | 3.5/Discussion | von Mises 应力曲线和相图 | 弹性模型 | 中强 | 材料参数和 FSI 简化 |
| 本文框架可辅助预后预测 | Conclusion | 分类模型和应力机制综合 | 应用推论 | 中 | 需临床验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1-3 | 定义 MB、LADA 几何、截面变化和分支流动问题 | 研究对象可力学化 | 把临床形态转为变量 | 是 |
| Fig. 5-8 | 展示压力、流量和流型响应 | MB 改变血流动力学 | 建立 CFD 证据链 | 是 |
| Fig. 11 | 数值与理论 RPD 对比 | 理论模型可预测压降趋势 | 降低模型黑箱感 | 是 |
| Fig. 12-13 | RPD 相图与纤维化分组 | 二因素分类优于单因素阈值 | 把结果转为风险工具 | 是 |
| Fig. 14-16 | 动脉壁应力和参数相图 | MB 诱发应力集中 | 支撑内皮/痉挛机制讨论 | 是 |
| 关键公式组 | 细长管压降、RPD、各向异性孔洞应力 | 压力和应力预测 | 连接变量与输出 | 需核查公式排版 |

图表顺序很清楚：对象图 -> 几何/边界 -> CFD 验证 -> 参数趋势 -> 分类相图 -> 应力机制。其写作价值是，每张图都对应一个 claim，而不是只展示“算了很多模型”。

## 11. 章节结构与篇章布局
- Abstract：背景、gap、双模型、核心趋势、应用意义。
- Introduction：临床重要性 -> MB 形态特征 -> 现有阈值与血流研究不足 -> 本文贡献。
- Related Work/Background：嵌入 Introduction，没有单列综述。
- Method/Theory/Model：2.1 冠脉几何；2.2 CFD；2.3 流体和弹性理论模型。
- Results：3.1 压力；3.2 流量；3.3 流型；3.4 分类模型；3.5 应力。
- Discussion：把 RPD、纤维化、应力集中与临床风险联系，并承认局限。
- Conclusion：回收二因素分类和应力风险。
- 章节之间如何过渡：从临床对象过渡到模型，再从模型验证过渡到分类和机制。
- 哪一节最值得模仿：3.4 Classification model，把曲线结果压缩成可用相图。
- 哪一节可能存在结构风险：Discussion 的临床外推需要更多真实数据支撑。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Hemodynamics-of-coronary-artery-with-syst_2026_Journal-of-the-Mechanics-and-.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Materials and methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Coronary arteries | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Fluid dynamics analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Models | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3.1 Fluid mechanics model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3.2 Elastic mechanics model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Luminal pressure | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Flow rate | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Flow pattern | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Classification model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5 Stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Discussions | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：先讲 MB 的医学后果，再讲诊断阈值和力学机制不足，最后宣布“计算 + 理论”的策略。
- Method 段落推进：几何定义先行，边界条件次之，模型推导最后出现。
- Results 段落推进：先验证模型，再按压力、流量、流型、分类、应力逐层增强。
- Discussion/Conclusion 段落推进：先解释分类为何优于单因素，再讨论应力集中可能导致内皮功能障碍和痉挛。
- 常见段落开头方式：`To investigate...`; `The results show...`; `Comparison between...`; `It is found that...`。
- 常见段落收束方式：用趋势或机制句收束，如“therefore, length and compression ratio should be considered together”。
- 可复用段落模板：问题段“X is clinically important, but Y remains mechanically unclear”；结果段“Changing P affects Q, while R has a weaker influence, suggesting S”。

## 13. 文笔画像与语言习惯
- 整体语气：技术克制，偏工程生物力学。
- claim 强度：对参数趋势较强，对临床转化用 may/contribute 控制外推。
- 谨慎表达：承认需要更多临床 follow-up 和更强 FSI 模型。
- 问题表达：`remain poorly understood`、`may lead to serious events`。
- 贡献表达：`computational and theoretical efforts are combined`、`a model is developed/proposed`。
- 机制表达：`leads to higher RPD`、`could increase the risk of...`。
- 对比表达：二因素模型 vs 单因素模型，理论结果 vs 数值结果。
- 限定边界表达：模型忽略完整心肌-血管-血流相互作用，未来可改进。
- 术语密度：中高，但围绕 MB、RPD、flow rate、stress concentration 集中。
- 长句/短句习惯：方法段长句较多，结论段用短句列结果。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：model(65)；arterial(54)；flow(53)；blood(45)；ratio(42)；respectively(42)；stress(39)；segment(39)；compression(38)；pressure(37)；lada(34)；coronary(33)；artery(31)；myocardial(30)；myocardium(28)；embedded(27)；section(26)；length(25)；wall(23)；wang(22)
- 高频学术名词：model(65)；stress(39)；segment(39)；pressure(37)；section(26)；analysis(20)；results(17)；velocity(16)；function(13)；moment(12)；simulation(10)；classification(10)；cross-section(10)；concentration(9)；location(8)；contractility(8)
- 高频学术动词：compared(10)；predict(9)；shown(7)；proposed(5)；investigate(3)；develop(3)；developed(3)；predicted(3)；validate(2)；solved(2)；revealed(2)；show(2)；propose(2)；validated(1)；suggest(1)；estimated(1)
- 高频形容词：arterial(54)；segment(39)；coronary(33)；theoretical(30)；numerical(30)；myocardial(30)；elastic(24)；luminal(21)；cross-sectional(16)；volumetric(14)；clinical(12)；elliptical(12)；represent(12)；end-systolic(12)；moment(12)；large(10)
- 高频副词/连接副词：respectively(42)；significantly(20)；approximately(10)；therefore(7)；gradually(7)；however(6)；strongly(4)；notably(4)；substantially(4)；arbitrarily(3)；uniformly(3)；consequently(2)；theoretically(2)；anomaly(2)；intramurally(2)；closely(2)
- 高频二词短语：compression ratio(35)；arterial wall(19)；embedded depth(18)；blood flow(17)；major outlet(15)；flow rate(15)；luminal pressure(14)；narrowed section(14)；volumetric flow(14)；coronary artery(12)；fluid model(11)；elastic model(11)；length narrowed(11)；arterial segment(11)；lada models(11)；end-systolic moment(11)
- 高频三词短语：length narrowed section(11)；von mises stress(10)；volumetric flow rate(8)；larger compression ratio(8)；maximum von mises(7)；compression ratio length(6)；tunneled arterial segment(6)；large compression ratio(6)；ratio length narrowed(5)；university beijing china(4)；luminal pressure distributions(4)；relative pressure drop(4)

**主动、被动与句法**

- 被动语态估计次数：158
- `we + 动作动词` 主动句估计次数：4
- 名词化表达估计次数：491
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：255
- 一般过去时线索：31
- 现在完成时线索：4
- 情态动词线索：53
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：university(6)；china(6)；engineering(5)；coronary(4)；institute(4)；beijing(4)；model(4)；luminal(3)
- 1. Introduction：coronary(9)；arterial(7)；vessels(6)；myocardial(6)；section(6)；morphologies(5)；blood(5)；arteries(5)
- 2. Materials and methods：无明显高频项
- 2.1. Coronary arteries：lada(9)；segment(6)；models(6)；cross-section(4)；length(4)；group(4)；includes(4)；three(4)
- 2.2. Fluid dynamics analysis：blood(13)；model(10)；lada(7)；flow(7)；arterial(6)；velocity(5)；segment(5)；pressure(4)
- 2.3. Models：无明显高频项
- 2.3.1. Fluid mechanics model：segment(19)；respectively(14)；model(12)；blood(12)；lpd(12)；flow(11)；eqs(11)；pressure(10)
- 3. Results：无明显高频项

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`X may lead to serious events; however, the biomechanical effects remain poorly understood.`
- 可复用句型骨架：`Although X is clinically/engineeringly important, the coupled effects of A and B on Y remain unclear.`
- 中文启发：先给现实后果，再限定未解机制。

### 14.2 方法与框架表达
- 原文表达模式：`computational and theoretical efforts are combined to investigate...`
- 可复用句型骨架：`We combine [simulation] and [theory] to quantify [mechanical response] under [condition].`
- 中文启发：方法句要说明组合带来的能力。

### 14.3 结果与趋势表达
- 原文表达模式：`increasing P leads to higher Q and lower R.`
- 可复用句型骨架：`An increase in P amplifies Q, whereas R remains weakly affected by S.`
- 中文启发：把强影响和弱影响放在同一句中，便于形成机制判断。

### 14.4 机制解释表达
- 原文表达模式：`stress concentration may increase the risk of endothelial dysfunction and coronary spasm.`
- 可复用句型骨架：`The localized increase in [mechanical quantity] provides a plausible pathway toward [biological/engineering consequence].`
- 中文启发：用 plausible pathway 控制因果强度。

### 14.5 贡献与意义表达
- 原文表达模式：`This work may elucidate... and contribute to...`
- 可复用句型骨架：`This framework provides a quantitative basis for [classification/prediction/design].`
- 中文启发：意义要落到“定量依据”。

### 14.6 局限与未来工作表达
- 原文表达模式：`clinical follow-up studies are needed`; `more accurate predictions might be obtained if...`
- 可复用句型骨架：`Further validation using [data] is needed to test the proposed criterion.`
- 中文启发：局限句应指向下一步验证，而不是泛泛道歉。

## 15. 引用策略与文献使用
- 引用密度：Introduction 和 Discussion 较密，方法参数和临床阈值处也有引用。
- 引用主要集中位置：MB 临床后果、已有压缩率阈值、入口速度/出口模型、患者图像、纤维化/痉挛机制。
- 经典文献用途：支撑 MB 临床认识、血管流动模型和软组织力学背景。
- 近年文献用途：说明 MB 仍是活跃医学/力学问题。
- 方法文献用途：提供速度波形、Windkessel、患者几何和已有阈值。
- 对比/批判性引用：用两个单因素模型作为本文二因素模型对比。
- gap 如何靠引用搭建：先引用 MB 风险，再引用单因素诊断，最后指出需要形态-血流耦合。
- references 暗示的研究共同体：血管外科、心血管流体力学、软组织力学、形态发生/生物力学。
- 引用风险：若最新临床指南已有多因素评分，需更明确比较。

## 16. 审稿人视角风险
- 最大攻击面：二因素 RPD 分类图与真实临床结局之间的因果和统计关联。
- claim 是否过强：模型趋势 claim 可支撑；临床预后 claim 需谨慎。
- 证据是否不足：流体和应力证据较强，纤维化分组的临床证据较弱。
- 方法是否可复现：参数表和公式需 PDF 核查，理论模型可复现性较好。
- 对比是否充分：与两个单因素阈值比较清楚，但与多因素临床评分或 FSI 模型比较不足。
- 边界条件是否清晰：心动周期和几何参数较清楚；材料参数和组织边界仍可加强。
- 替代解释是否排除：纤维化和严重程度可能受其他病理因素影响。
- 图表是否需要进一步核查：需要，尤其 Fig. 12-16。

## 17. 可复用资产
- 可复用选题角度：从临床形态异常切入，建立力学风险指标。
- 可复用 gap 制造方式：`已有单因素阈值有用，但无法解释 A 与 B 的耦合效应。`
- 可复用论证链：几何模型 -> CFD 验证 -> 理论压降 -> 风险相图 -> 应力机制。
- 可复用图表设计：对象示意图、参数表、压力/流量曲线、理论-数值对比、风险相图、应力相图。
- 可复用段落结构：每个结果段都回答一个变量对一个力学量的影响。
- 可复用句型骨架：`The dependence of X on Y is weak compared with that on Z.`
- 可复用引用组织：临床事实引用在前，方法参数引用在中，风险解释引用在后。
- 不宜直接模仿之处：不要在没有患者数据时直接使用类似临床风险结论。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学：把应用问题转为形态参数和力学指标之间的可验证关系。
- 可迁移到 Introduction：用“单因素指标不足”制造清晰 gap。
- 可迁移到 Method：先定义几何变量，再定义输出指标，最后推导模型。
- 可迁移到 Results/Discussion：先做模型验证，再做相图或分类。
- 需要避免的问题：不要让临床意义超过数据支撑；不要只展示 CFD 彩图而缺少理论解释。

## 19. 最终浓缩
- 这篇论文最值得学：如何把临床 MB 形态转化为 RPD 分类相图和应力机制。
- 这篇论文最大风险：二因素分类的临床验证还不够充分。
- 三个可迁移动作：
  1. 用多变量耦合替代单一阈值。
  2. 用理论模型解释数值模拟趋势。
  3. 用相图把参数研究压缩成可用判断工具。

最终判断：这是一篇适合作为“医学问题力学化”的样本论文。它的问题入口应用性强，但真正的说服力来自形态变量、流体压降和组织应力之间的闭环。

补充写作素材：如果借鉴本文写 Introduction，可以把第一段写成“临床现象及后果”，第二段写成“已有指标如何工作但为什么不够”，第三段写成“本文把指标扩展为耦合力学变量”。如果借鉴 Results，可以学习“先给单变量趋势，再给二维相图”的节奏：单变量曲线负责解释，二维相图负责决策。审稿防守时，最应提前准备的是参数敏感性、患者样本量和 FSI 简化的解释；这些不是小问题，但可以通过把 claim 限定为“力学机制和风险分层辅助指标”来降低风险。
