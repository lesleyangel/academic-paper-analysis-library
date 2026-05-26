# Unit cells of composites with symmetric structures for the study of effective thermal properties

## 0. 读取说明

- 文本来源：`801/文本/txt/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.txt`，PyMuPDF 抽取，18 页。
- 抽取文本包含 highlights、摘要、引言、单胞构造规则、温度分布规则、UD 和 satin woven 算例、结论和主要图表标题。
- 原文双栏造成公式和表格有局部错行，本文按章节逻辑复原；温度云图、单胞几何边界、SUC/UC1/UC2 关系和实验对比表需要 PDF 图像复核。

## 1. 基本信息与论文身份

- 题名：Unit cells of composites with symmetric structures for the study of effective thermal properties。
- 作者：Jian-Jun Gou, Chun-Lin Gong, Liang-Xian Gu, Shuguang Li, Wen-Quan Tao。
- 期刊：Applied Thermal Engineering, 126 (2017) 602-619。
- 领域：复合材料有效热导率、对称结构、单胞方法、边界条件、织物增强复合材料。
- 论文类型：理论规则 + 单胞边界条件推导 + 数值验证 + 文献实验对比。
- 研究对象：具有平移、反射和 180°旋转对称性的复合材料，重点包括 UD 单向纤维复合材料和 4HS-8HS satin woven 织物复合材料。
- 主要方法：从宏观实验试样和热通量边界出发，定义 STS/ATS，推导对称节点温度关系；用 SIMP 以外的有限元热传导计算验证不同尺寸 UC 的有效热导率一致性。
- 论文身份判断：这是 2018 年热膨胀单胞论文的前序方法基础，主题是热传导/有效热导率中的 unit cell formulation，而不是热膨胀位移边界。

## 2. 摘要与核心信息提取

本文核心主张是：具有规则对称结构的复合材料，其有效热性质可以通过尺寸受限的 unit cell 高效计算；但单胞建立不只是选择一个重复几何单元，还包括根据平移、反射和 180°旋转对称下的温度分布规则推导正确热边界条件。

摘要强调两步：identify structure symmetries 建立几何模型，derive boundary conditions 赋予模型物理意义。作者把宏观实验中的热通量方向定义为 symmetric thermal stimulus (STS) 和 antisymmetric thermal stimulus (ATS)，并用两条温度关系式总结三类对称结构的边界推导依据。

一句话浓缩：本文把有效热导率单胞计算中的“如何缩小几何域、如何写热边界条件”整理成一套从宏观试样到多尺寸 UC 的通用路径。

## 3. 选题层深拆

选题来自复合材料热管理应用。高温飞行器、热防护结构和电子热控都需要有效热导率，但直接用宏观含微结构模型成本高。RVE/UC 可以降低计算成本，但只有在几何和边界条件都正确时才可靠。

作者把问题收束成一个方法学命题：对于有序复合材料，结构对称性不仅能决定几何单胞，还会决定单胞边界温度关系。以往很多研究使用 full unit cell 和周期边界，或直接套用简化边界；但在反射和 180°旋转对称性被用于缩小模型后，边界条件必须重新推导。

该选题非常适合作为方法论文，因为它不依赖某一种材料的独特性能，而是面向一类建模操作的普遍问题：单胞几何缩小越多，边界条件越复杂；若边界条件错误，计算结果即使偶然接近，也缺少物理正确性。

## 4. 领域位置与文献版图

文献版图首先区分无序复合材料和有序复合材料。无序材料 RVE 面临微结构随机性和代表尺寸问题；有序材料如纤维、织物、编织复合材料具有可利用的结构对称性，因此可以构造更精确的 UC。

其次，作者回顾有效热导率预测中的解析模型、数值模型和 unit cell 方法。Full unit cell 基于平移对称，是最常见做法；但许多织物结构还包含反射或旋转对称，理论上可进一步缩小 UC。此前关于 plain woven、3D braided 和 satin woven 的研究已有具体单胞，但 general rules and concepts 尚未澄清。

本文处在“具体单胞算例”之后、“通用单胞规则”之上。它不是单纯再算一个 satin 织物，而是把单胞 formulation 的流程和边界条件演化明确化。

## 5. Gap 制造机制

本文 gap 是“单胞 formulation rules 不清”。作者指出，已有研究虽然使用 unit cell，但很多工作只把注意力放在几何重复单元和有效热导率结果上，未系统讨论从宏观试样到 UC0、UC1、UC2、UC3 的路径，尤其没有把边界条件随对称性使用而演化的过程讲清楚。

另一个 gap 是“inappropriate BCs 有时给出近似正确结果”。这很危险，因为它会掩盖物理错误。作者用 UD 轴向导热算例展示，普通简化边界条件在某些长宽比下可能接近正确，但只有严格周期/对称节点温度关系才能保持与宏观热通量一致。

第三个 gap 是复杂 satin woven 结构的单胞研究不足。Satin 相比 plain woven 交织点少、结构更复杂，4HS-8HS 的对称路径不同，适合作为统一边界公式的验证对象。

## 6. 创新性判断

- 创新类型：单胞热边界条件理论澄清 + 复杂织物应用验证。
- 真实创新点 1：提出从宏观 UC0 到 UC1/UC2/UC3 的单胞构造流程，明确几何模型与 BC 的关系。
- 真实创新点 2：用 STS/ATS 统一描述平移、反射和 180°旋转对称结构中的温度分布规律。
- 真实创新点 3：通过 UD 轴向算例说明 derived BC 与不合适 BC 的物理差异。
- 真实创新点 4：对 4HS-8HS satin woven 构造 UC1/UC2，并以统一公式推导边界条件。
- 创新强度：中等偏强。贡献是方法规范化，不是新材料性能，但对热导率多尺度建模具有直接复用价值。
- 可挑战之处：验证主要基于理想几何和数值一致性，真实制造缺陷和温度依赖材料参数未纳入。

## 7. 论证链条复原

1. 复合材料有效热导率是热管理设计基础，宏观建模成本高。
2. 有序复合材料存在平移、反射和旋转对称，可用 unit cell 替代宏观试样。
3. 单胞必须包含两个要素：代表性几何和准确 BC。
4. 宏观实验热通量方向可视为 thermal stimulus，相对于对称面/轴分为 STS 和 ATS。
5. 三类对称结构中的对称节点温度关系可用 Eq. 3/4 等公式描述。
6. 这些温度关系可在边界节点上转化为 UC 的边界条件。
7. UD 轴向算例证明不合适 BC 会因长宽比和材料布置产生不可靠 DTD 分布。
8. UD 横向算例用四个不同大小 UC 得到一致热导率，验证推导流程。
9. 4HS-8HS satin woven 用 UC1/UC2 得到最大偏差仅约 0.19%，并与实验有一定一致性。
10. 结论回扣：每次利用对称性缩小单胞，都必须严格推导新边界条件。

## 8. 方法/理论/模型细拆

方法从 Fourier 热传导本构开始，以宏观有效热导率和宏观温度梯度的关系定义测量目标。宏观试样 UC0 具有真实实验边界：某一方向给定热通量，其他方向绝热。UC0 太大，因此通过结构对称性得到更小的 UC。

单胞构造流程是递进的：UC1 基于平移对称，获得 periodic BC；若 UC1 内部存在反射或 180°旋转对称，则可继续得到 UC2/UC3。作者强调，平移对称把无限结构变成有限尺寸，反射和旋转对称则通常把单胞减半；但每一次缩小都会引入新的边界条件。

STS/ATS 是方法关键。对于反射面或旋转轴，宏观热通量平行时为 STS，对称节点的相对温度关系同号；垂直时为 ATS，相对温度关系反号。对于平移结构，宏观热通量均可视为 STS。

数值模型中，UD 横向截面以六角纤维-基体排布构建四种 UC；satin woven 使用 4HS-8HS 织物，纤维为碳纤维，横向/轴向热导率分别约 0.84 和 8.4 W/(m K)，基体为酚醛树脂，热导率约 0.42 W/(m K)，纤维体积分数约 0.38。纱线起伏通过局部坐标系统处理。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| 几何 UC 和 BC 是单胞有效性的两个必要要素 | Section 2 | 作者明确区分 identification of symmetries 和 derivation of BCs | 强 | 属理论论证，需要算例支撑 |
| STS/ATS 可统一三类对称结构温度关系 | Section 2.2-2.3 | 平移、反射、180°旋转结构的温度场算例和 Table 3 汇总 | 强 | 图像温度场需 PDF 复核 |
| 不合适 BC 会影响计算物理机制 | Section 3 | UD 轴向算例比较 BC0/BC1 和 DTD，说明周期节点温度关系更严格 | 中强 | 具体误差随材料布置变化 |
| UD 横向四种 UC 的结果一致 | Section 4.1 | 有效横向热导率约 1.6503-1.6506 W/(m K)，与解析公式吻合，偏差 <0.02% | 强 | 理想六角排列 |
| Satin woven UC1/UC2 边界公式有效 | Section 4.2 | 4HS-8HS 的 UC1/UC2 有效热导率最大偏差 0.19% | 强 | 仅验证规则几何 |
| 综数增加使 in-plane k 增加、out-plane k 略减 | Table 8 | 4HS-8HS in-plane 从 2.037 增至 2.049，out-plane 从 0.5580 降至 0.5439 | 中强 | 依赖给定材料和几何参数 |
| 数值结果与实验有一定一致性 | Table 9 | C-phenolic KT 数值 2.35 vs 实验 2.79，差 15.8%；KA 数值 0.61 vs 实验 0.57，差 7.0% | 中 | KT 差异较大，实验条件可能不同 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 1 单胞形成过程 | 展示 UC0 到 UC1/UC2/UC3 的几何与 BC 演化 | 单胞流程 | 需要 PDF 图像复核 |
| Eq. 1 Fourier 有效导热关系 | 定义宏观热通量、温度梯度和有效热导率 | 研究对象 | 公式可读 |
| Eq. 2 宏观实验 BC | 把实验测量条件转化为模型基准 | BC 来源 | 公式排版需复核 |
| Fig. 2-8 三类对称结构温度场 | 验证 STS/ATS 温度关系 | 温度规则 | 需要 PDF 图像复核 |
| Table 3 STS/ATS 汇总 | 将宏观热流方向、对称面/轴和公式对应起来 | BC 推导工具 | 表格需 PDF 复核 |
| Fig. 9-11 UD 轴向模型/DTD | 说明不合适 BC 的物理差异 | BC 必要性 | 需要 PDF 图像复核 |
| Fig. 12-14 UD 横向 UC 和温度场 | 展示四个 UC 结果一致 | 多尺寸验证 | 温度云图需复核 |
| Fig. 15-20 satin 织物、UC、坐标和边界 | 展示复杂织物如何参数化 | 复杂结构应用 | 需要 PDF 图像复核 |
| Table 8 satin 有效热导率 | 用 UC1/UC2 偏差验证 BC | 数值证据 | 表格较清晰 |
| Table 9 实验对比 | 提供外部验证 | 方法可信度 | 实验条件需 PDF 复核 |

结果叙事的核心是“先建立规则，再用越来越复杂的结构验证规则”。UD 先承担教学功能，satin woven 承担推广功能。

## 11. 章节结构与篇章布局

文章结构为 Introduction；Unit cell formulation rules in thermal calculations；Axial calculations of UD composites；Study of typical composites with symmetric structures；Conclusions。

第二章是全文的理论主体，先讲为什么需要 UC、如何从宏观试样走到 UC，再讲三类对称结构温度规则。第三章单独拿 UD 轴向做“边界条件必要性”演示。第四章再进入 UD 横向和 satin woven 的系统算例。

这种布局很有策略：作者没有直接把所有算例塞进 Results，而是用一个简单 UD 轴向问题专门教育读者“不合适 BC 的问题在哪里”。等读者接受这个逻辑后，再进入多尺寸 UC 验证。

标题命名偏方法流程型，信息密度主要在小节和图题中。最值得模仿的章节是 Section 3，因为它用一个简化反例说明方法必要性，比直接宣称“BC 很重要”更有说服力。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：10
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                speed aircraft, the surface temperature reaches a value of 1600 C | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 2 Unit cell formulation rules in thermal calculations                original structure UC0 provided that their thermal relations with | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Unit cells and thermal boundary conditions                        the decreasing of the unit cell size, the BCs become more compli- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Temperature disciplines in translational symmetric structures | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3.3 Temperature distribution disciplines in 180  rotational           which means the length-width ratio, a/b of the unit cell can be an | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Axial effective thermal conductivities | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 10 W/(m K), according to the classic Rule of Mixture which is | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Study of typical composites with symmetric structures | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Transverse thermal properties of UD composite                 ATS equations are used by each derivation step for each boundary | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2.5 Comparison with available experimental results                    International Joint Research of National Natural Science Founda- | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“复合材料热应用-有效性质预测-随机与有序结构差异-单胞两要素-本文目的”。作者不断提醒读者 BC 与几何同等重要。

理论段落遵循“宏观实验条件-对称关系-节点温度公式-边界条件”的推导节奏。每个公式前后都有物理含义解释，避免纯数学化。

UD 轴向段落节奏是“简单结构-两种 BC-长宽比/DTD 对比-物理机制总结”。这是全文最像“反例教学”的部分。

Satin 段落节奏是“织物结构介绍-单胞构造-坐标系统-边界公式-温度场/热导率-实验对比”。复杂结构被拆成有序步骤，降低阅读难度。

## 13. 文笔画像与语言习惯

本文语言克制、规范、流程感强。高频词包括 thermal、unit、boundary、symmetric、temperature、structure、effective、STS、ATS。术语场高度集中，服务于方法贡献。

作者常用 “should be”“can be”“is derived”“is formulated”“is validated” 等表达，强调规范性和可操作性。相比材料性能论文，本文几乎不靠 “significant enhancement” 类强修辞，而靠公式、图表和偏差数值说服读者。

被动语态占主导，尤其在方法定义和结果验证中。主动语态常出现在 “we need”“we can notice” 等导读句中，承担解释和转场作用。

情态动词 `should` 是重要风格标记：unit cell should contain、BCs should be derived、new boundary conditions should be derived strictly。这种语气适合写“方法规范”型论文。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：thermal(102)；unit(102)；symmetric(68)；temperature(61)；boundary(61)；structure(59)；structures(55)；cell(52)；bcs(52)；composites(48)；cells(47)；composite(46)；ber(42)；sts(40)；two(38)；direction(38)；model(37)；heat(37)；macroscopic(37)；respectively(37)
- 高频学术名词：structure(118)；temperature(61)；structures(55)；direction(38)；model(37)；conditions(31)；results(22)；conductivity(22)；distribution(22)；section(22)；equation(20)；equations(17)；derivation(16)；condition(14)；calculation(14)；gure(12)
- 高频学术动词：shown(31)；formulated(25)；derived(21)；shows(19)；formulate(8)；compared(7)；developed(6)；indicates(5)；investigated(5)；derive(4)；demonstrate(4)；revealed(4)；demonstrated(3)；validate(2)；indicate(2)；show(1)
- 高频形容词：thermal(102)；symmetric(68)；boundary(61)；effective(58)；macroscopic(37)；numerical(28)；translational(28)；rotational(27)；ectional(25)；different(23)；local(16)；typical(16)；axial(16)；relative(12)；physical(10)；periodic(10)
- 高频副词/连接副词：respectively(37)；however(11)；widely(4)；tively(4)；therefore(3)；july(3)；certainly(3)；experimentally(2)；especially(2)；nally(2)；clearly(2)；separately(2)；ciently(1)；rstly(1)；obviously(1)；closely(1)
- 高频二词短语：unit cell(48)；unit cells(44)；symmetric structures(28)；boundary conditions(26)；thermal conductivity(20)；applied thermal(19)；thermal engineering(18)；macroscopic heat(18)；cos tox(18)；tox sin(18)；sin toy(18)；effective thermal(17)；thermal conductivities(17)；symmetric nodes(17)；satin woven(16)；gou applied(16)
- 高频三词短语：applied thermal engineering(18)；cos tox sin(18)；gou applied thermal(16)；tox sin toy(16)；effective thermal conductivities(10)；satin woven composites(10)；rotational symmetric structures(6)；temperature distribution disciplines(6)；unidirectional ber reinforced(6)；ber reinforced composite(6)；translational symmetric structures(6)；sin toy cos(6)

**主动、被动与句法**

- 被动语态估计次数：199
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：411
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：348
- 一般过去时线索：44
- 现在完成时线索：1
- 情态动词线索：91
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：unit(13)；thermal(9)；cell(8)；symmetric(7)；boundary(7)；composites(6)；conditions(6)；engineering(5)
- 1. Introduction                                                speed aircraft, the surface temperature reaches a value of 1600 C：unit(22)；composites(18)；composite(15)；thermal(15)；bcs(14)；model(13)；cell(13)；structure(13)
- 2. Unit cell formulation rules in thermal calculations                original structure UC0 provided that their thermal relations with：unit(8)；cell(6)；bcs(5)；symmetries(5)；thermal(4)；based(4)；structures(4)；accurate(3)
- 2.1. Unit cells and thermal boundary conditions                        the decreasing of the unit cell size, the BCs become more compli-：symmetric(33)；thermal(27)；heat(27)；temperature(27)；structures(24)；macroscopic(22)；sts(22)；structure(20)
- 2.3.3. Temperature distribution disciplines in 180  rotational           which means the length-width ratio, a/b of the unit cell can be an：thermal(17)；symmetric(15)；boundary(15)；direction(11)；sts(11)；temperature(10)；structures(8)；structure(8)
- 4.1. Transverse thermal properties of UD composite                 ATS equations are used by each derivation step for each boundary：unit(36)；thermal(26)；cells(24)；ber(23)；cos(22)；sin(20)；satin(19)；composite(18)
- 4.2.5. Comparison with available experimental results                    International Joint Research of National Natural Science Founda-：although(1)；identical(1)；numerical(1)；result(1)；obtained(1)；multi-size(1)；tion(1)；china(1)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：unit cell, effective thermal conductivity, boundary conditions, symmetric structures, translational symmetry, reflectional symmetry, rotational symmetry, STS, ATS, macroscopic heat flux。

可复用 gap 句式：

- “The general rules and concepts are not yet clarified.”
- “The first step builds a geometric model while the later one endows the model physical meanings.”
- “Inappropriate BCs sometimes can lead to approximate accurate results.”

可复用方法句式：

- “The formulation of a unit cell can be summarized as...”
- “Each utilization of symmetries can create a new unit cell with smaller size.”
- “The corresponding boundary conditions should be derived based on temperature distribution disciplines.”

可复用结果句式：

- “Identical results with the maximum deviation of X are obtained by the two multi-size unit cells.”
- “The good agreement between numerical and analytic results confirms...”
- “The approach developed in this paper can be applied to...”

## 15. 引用策略与文献使用

引用策略主要有三类。第一类是应用和材料背景，如高温飞行器、热防护、复合材料有效热导率。第二类是 RVE/UC 和微观力学建模文献，用来说明单胞方法已有基础。第三类是具体织物复合材料热导率研究，包括 plain woven、3D braided、satin woven，用于说明本文对象具有延续性。

作者对前人采取“已有具体算例，但缺少通用规则”的评价方式。这样既承认已有单胞工作，也为本文的 general rule 留出贡献空间。

实验对比引用放在后段，用来增加外部可信度。但作者也很清楚主要验证仍来自多尺寸 UC 一致性，因此结论更强调方法可参考，而不是宣称完全替代实验。

## 16. 审稿人视角风险

1. 理想对称性风险：真实织物存在纱线偏移、孔隙、局部压实和制造误差，对称性可能不严格。
2. 边界条件泛化风险：STS/ATS 规则适合稳态导热和宏观热通量设定，复杂瞬态、非线性或接触热阻场景未覆盖。
3. 材料参数简化：碳纤维/酚醛树脂参数固定，未考虑温度依赖和界面热阻。
4. 实验对比差异：C-phenolic 横向/轴向热导与实验存在 15.8% 和 7.0% 差异，说明模型仍受几何/材料输入影响。
5. 拟合/验证范围风险：多尺寸 UC 一致性证明 BC 自洽，但不等于真实材料准确。
6. 图像依赖风险：温度场和 DTD 论证需要看图，需 PDF 图像复核。

## 17. 可复用资产

- 选题资产：从“几何单胞与物理边界条件不等价”切入。
- 方法资产：UC0-UC1-UC2-UC3 的路径叙述适合各种周期结构论文。
- 概念资产：STS/ATS 把复杂边界条件推导变成可查规则。
- 验证资产：用简单算例展示错误 BC 的后果，再用复杂算例证明统一规则。
- 图表资产：单胞缩小流程图、对称结构温度场、DTD 图、有效热导率对比表、实验对比表。
- 表达资产：把“model physical meanings”作为边界条件的重要性表述，非常适合多尺度建模论文。

## 18. 对我写论文的启发

最重要的启发是：方法论文要回答“为什么不能用旧方法”。本文不是直接提出新 UC，而是先证明不合适 BC 可能带来物理机制问题，这让新规则显得必要。

第二个启发是，通用规则最好从简单结构推导。三类基本对称结构就像“语法规则”，UD 和 satin 是“应用句子”。这种写法能让复杂工程问题变得可学。

第三个启发是，外部验证和内部一致性可以组合使用。多尺寸 UC 一致性验证边界条件，文献实验对比验证模型现实性，两者功能不同，写作时应明确区分。

第四个启发是，结果表格最好服务于一个方法判断，而不是只服务于性能展示。Table 8 的意义并不是告诉读者 4HS 到 8HS 的热导率各是多少，而是证明 UC1 和 UC2 在同一物理边界下给出一致结果。也就是说，表格中的 deviation 是论证主角，热导率数值反而是支撑材料。写自己的方法论文时，可以有意识地把“误差/偏差/一致性”设计成表格中心。

第五个启发是，概念名词要少而稳定。本文反复使用 STS、ATS、UC0、UC1、BC0、BC1 这几个符号，读者一旦掌握，就能跟随作者处理更复杂的 satin woven 结构。复杂论文不是靠不断发明新符号显得高级，而是靠少量稳定符号贯穿多个场景。

## 19. 最终浓缩

这篇论文最值得学习的是它把有效热导率单胞建模从“选一个重复几何”提升为“识别对称性、推导温度边界、验证多尺寸一致性”的规范流程。它用 STS/ATS 统一平移、反射和 180°旋转对称结构中的温度关系，并在 UD 与 satin woven 复合材料中证明规则可用。

最大风险是理想对称几何和简化材料参数限制了真实工程外推，尤其对非理想织物和温度依赖材料还需要扩展。

可迁移到自己论文中的三件事：第一，把几何代表性和边界条件代表性分开论证；第二，用反例展示旧边界条件的问题；第三，用多尺寸模型一致性作为方法正确性的核心证据。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.txt` 与 `801/文本/metadata/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 Unit cell formulation rules in thermal calculations （方法/模型）
  - L3 p.3: 2.1 Unit cells and thermal boundary conditions （对象/问题/模块）
  - L3 p.3: 2.2 Temperature disciplines in translational symmetric structures （对象/问题/模块）
  - L3 p.4: 2.3 Temperature disciplines in reflectional and 180° rotational symmetric structures （对象/问题/模块）
    - L4 p.4: 2.3.1 Two thermal stimuli definition （对象/问题/模块）
    - L4 p.6: 2.3.2 Temperature distribution disciplines in reflectional structures （对象/问题/模块）
    - L4 p.6: 2.3.3 Temperature distribution disciplines in 180° rotational structures （对象/问题/模块）
- L2 p.6: 3 Axial calculations of UD composites （对象/问题/模块）
  - L3 p.6: 3.1 Unit cell and boundary conditions （对象/问题/模块）
  - L3 p.7: 3.2 Axial effective thermal conductivities （对象/问题/模块）
- L2 p.8: 4 Study of typical composites with symmetric structures （对象/问题/模块）
  - L3 p.9: 4.1 Transverse thermal properties of UD composite （对象/问题/模块）
    - L4 p.9: 4.1.1 Unit cells and boundary conditions （对象/问题/模块）
    - L4 p.12: 4.1.2 Temperature fields and effective thermal conductivities （对象/问题/模块）
  - L3 p.12: 4.2 Satin woven composites （对象/问题/模块）
    - L4 p.12: 4.2.1 Unit cells formulation （方法/模型）
    - L4 p.14: 4.2.2 Coordinate systems （对象/问题/模块）
    - L4 p.14: 4.2.3 Boundary conditions （对象/问题/模块）
    - L4 p.15: 4.2.4 Temperature fields and effective thermal conductivities （对象/问题/模块）
    - L4 p.17: 4.2.5 Comparison with available experimental results （结果/讨论/验证）
- L2 p.17: 5 Conclusions （结论）
- L2 p.17: Acknowledgment （对象/问题/模块）
- L2 p.17: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Unit cell formulation rules in thermal calculations | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Unit cells and thermal boundary conditions | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Temperature disciplines in translational symmetric structures | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Temperature disciplines in reflectional and 180° rotational symmetric structures | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.1 Two thermal stimuli definition | 4 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.2 Temperature distribution disciplines in reflectional structures | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3.3 Temperature distribution disciplines in 180° rotational structures | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Axial calculations of UD composites | 6 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Unit cell and boundary conditions | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Axial effective thermal conductivities | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Study of typical composites with symmetric structures | 8 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Transverse thermal properties of UD composite | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1.1 Unit cells and boundary conditions | 9 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1.2 Temperature fields and effective thermal conductivities | 12 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Satin woven composites | 12 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.1 Unit cells formulation | 12 | 4 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.2 Coordinate systems | 14 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.3 Boundary conditions | 14 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.4 Temperature fields and effective thermal conductivities | 15 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.5 Comparison with available experimental results | 17 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 17 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgment | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 17 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 具有对称结构的宏观复合材料的有效热性能可以通过尺寸有限的代表性晶胞来有效计算。在本文中，开发了这种晶胞公式的一般规则。其中涉及结构对称性识别和边界条件推导两个关键步骤，第一步建立几何模型，第二步赋予模型物理意义以表示原始结构。阐明了从实验样本到晶胞模型的路线，特别是相关边界条件的演变。实验中的宏观热通量通过其方向定义为对称和反对称的热刺激。对于三种典型的平移、反射和180°旋转对称结构，揭示了不同宏观热刺激下的温度分布规律并总结为两个方程，可用于推导晶胞的边界条件。对单向纤维增强复合材料进行轴向研究，以从物理机制的角度证明导出的边界条件和不适当的边界条件之间的差异。
> 
> 对于复合材料的横向，建立了四种尺寸减小的晶胞模型，阐述了晶胞公式和边界条件推导的基本过程。然后，对于更复杂的缎纹机织复合材料，研究了4、5、6、7和8综织物中所示的结构对称性，制定了两个不同尺寸的晶胞并以统一的形式推导了相应的边界条件，并且通过多尺寸晶胞获得的相同结果验证了晶胞和边界条件。本文开发的方法可应用于具有相关结构对称性的任何其他复合材料的热研究。 �2017 Elsevier Ltd. 保留所有权利。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Unit-cells-of-composites-with-symmetric-structures-for-_2017_Applied-Thermal.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 本文提出了用于对称结构复合材料热计算的晶胞公式的一般规则。该规则基于宏观实验样本和测量条件。实验中的宏观热通量根据平移、反射和180°旋转对称结构的方向分别定义为对称热刺激（STS）和反对称热刺激（ATS）。不同对称结构中的温度分布规律由相应的方程描述并通过典型计算得到证实，可用于推导晶胞的边界条件。以单向纤维增强复合材料的轴向研究为例，说明导出边界条件的必要性；通过横向研究，介绍晶胞公式化和边界条件推导的基本过程；然后，对于更复杂的4、5、6、7、8综丝缎纹编织复合材料，制定两个不同尺寸的晶胞，以统一的形式导出相应的边界条件，并通过相同的结果和实验结果对数值模型进行验证。参考。本文开发的方法可以被任何其他具有对称结构的复合材料的热计算所参考。
> 
> 可以得出结论：
> 
> 1. 具有对称结构的复合材料的有效热性能可以通过晶胞模型有效计算，该模型应根据结构中所示的对称性进行制定，并应根据本工作阐明的温度分布规律推导相应的边界条件。 2、晶胞表述的基本过程有四个步骤：结构对称性的识别、几何构型的建立、q0方向的确定和边界条件的推导。 3、每次利用对称性都会产生一个尺寸更小的新晶胞，新的边界条件必须严格推导，不合适的边界条件会影响计算精度。 4. 对于所研究的缎纹编织复合材料，随着复合材料硬度的增加，面内热导率增加，而面外热导率则略有下降。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 本文解决方式：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell. In this paper, a general rule of such unit cell formulation is developed. Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
- 学术/工程增量：For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells. An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view. For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：53
- Introduction 引用簇数量（估计）：12
- References 条目数（解析）：38
- 可识别年份条目数：34
- 近五年/近年文献（2021+）数量：0
- 经典文献（2010年前）数量：14
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Applied Thermal Engineering(1)
- 引用簇样例：[1], [2,3], [4,5], [13], [6,7], [8], [14], [8,26], [9], [27,28], [29,30], [12]

带引用的 gap/转折句样例：

- Textile reinforced composite is another typical orderedstructure composite with extensive applications in aerospace industry [12].

References 解析样例（前12条）：

- 5. Conclusions
In this paper, a general rule of unit cell formulation for thermal calculation of composites with symmetric structures is developed. The rule is based on the macroscopic experimental specimen and measurement conditions. The macroscopic heat flux in experiment is defined as symmetric thermal stimuli (STS) and antisymmetric thermal stimuli (ATS) by its directions for translational, reflectional and 180�rotational symmetric structures, respectively. The temperature distribution disciplines in different symmetric structures are described by corresponding equations and confirmed by typical calculations, and can be used to derive boundary conditions of unit cells. A case of axial study of unidirectional fiber reinforced composite is conducted to show the necessity of derived boundary conditions, and a transverse study is presented to introduce the basic process of unit cell formulations and boundary conditions derivation, and then for more complex 4-, 5-, 6-, 7- and 8-harness satin woven composites, two unit cells of different sizes are formulated, the corresponding boundary conditions are derived in a unified form, and the numerical models are validated by the identical results and also the experimental results available in reference. The approach developed in this paper can be referenced by thermal calculations of any other composites with symmetric structures. It can be concluded that:
- 1. Effective thermal properties of composites with symmetric structures can be efficiently calculated by a unit cell model, which should be formulated based on the symmetries indicated in the structures, and the corresponding boundary conditions should be derived based on temperature distribution disciplines clarified in this work.
- 2. The basic process of the formulation of a unit cell has four steps: the identification of structure symmetries, the establishment of geometric configuration, the determination of q0 direction and the derivation of boundary conditions.
- 3. Each utilization of symmetries can create a new unit cell with smaller size, and new boundary conditions should be derived strictly since inappropriate boundary conditions will affect the calculation accuracy.
- 4. For the studied satin woven composites, the in-plane thermal conductivity increases, while the out-plane one decreases very slightly with the increasing harness of composites.
Acknowledgment
This study is supported by the Fundamental Research Funds for the Central Universities (3102017OQD068) and the Key Project of
kt (Num.) (W/(m�K)) kt (Exp.) (W/(m�K)) Diff. (%) ka (Num.) (W/(m�K)) ka (Exp.) (W/(m�K)) Diff. (%)
International Joint Research of National Natural Science Foundation of China (51320105004).
References
- [1] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [2] J. Xie, J. Liang, G. Fang, Z. Chen, Effect of needling parameters on the effective properties of 3D needled C/C-SiC composites, Compos. Sci. and Technol. 117 (2015) 69–77.
- [3] W.Z. Fang, J.J. Gou, H. Zhang, Q. Kang, W.Q. Tao, Numerical predictions of the effective thermal conductivity for needled C/C-SiC composite materials, Numer. Heat Transf. Part A: Appl. 70 (10) (2016) 1101–1117.
- [4] L. Chen, H.-B. Luan, Y.-L. He, W.-Q. Tao, Pore-scale flow and mass transport in gas diffusion layer of proton exchange membrane fuel cell with interdigitated flow fields, Int. J. Therm. Sci. 51 (2012) 132–144.
- [5] X. He, Y. Guo, M. Li, N. Pan, M. Wang, Effective gas diffusion coefficient in fibrous materials by mesoscopic modeling, Int. J. Heat Mass Transf. 107 (2017) 736–746.
- [6] M. Wang, N. Pan, Modeling and prediction of the effective thermal conductivity of random open-cell porous foams, Int. J. Heat Mass Transf. 51 (5–6) (2008) 1325–1331.
- [7] P. Ranut, On the effective thermal conductivity of aluminum metal foams: review and improvement of the available empirical and analytical models, Appl. Therm. Eng. 101 (2016) 496–524.

### 20.9 常用词、词类、语态与时态

- 高频词：thermal(102)；unit(102)；symmetric(68)；fig(62)；temperature(61)；boundary(61)；structure(59)；structures(55)；cell(52)；bcs(52)；composites(48)；cells(47)；composite(46)；ber(42)；sts(40)；two(38)；direction(38)；heat(37)；macroscopic(37)；respectively(37)
- 高频名词化/学术名词：temperature(61)；structure(59)；direction(38)；conductivity(22)；distribution(22)；section(22)；derivation(16)；calculation(14)；gure(12)；ection(10)；rotation(10)；equation(10)；translation(9)；tion(8)；formulation(7)
- 高频学术动词：derived(21)；indicated(9)；compared(7)；developed(6)；presented(5)；revealed(4)；derive(4)；demonstrate(4)；demonstrated(3)；validate(2)；indicate(2)；validated(1)；develop(1)
- 高频形容词：thermal(102)；symmetric(68)；boundary(61)；macroscopic(37)；effective(29)；translational(28)；rotational(27)；ectional(25)；table(19)；typical(16)；axial(16)；numerical(14)；relative(12)；physical(10)；periodic(10)
- 高频副词：respectively(37)；widely(4)；tively(4)；july(3)；certainly(3)；only(3)；especially(2)；nally(2)；clearly(2)；separately(2)；ciently(1)；rstly(1)；obviously(1)；closely(1)；likely(1)
- 高频二词短语：unit cell(48)；unit cells(44)；symmetric structures(28)；boundary conditions(26)；thermal conductivity(20)；applied thermal(19)；thermal engineering(18)；macroscopic heat(18)；cos tox(18)；tox sin(18)；sin toy(18)；effective thermal(17)
- 高频三词短语：applied thermal engineering(18)；cos tox sin(18)；page gou applied(16)；gou applied thermal(16)；tox sin toy(16)；effective thermal conductivities(10)；satin woven composites(10)；rotational symmetric structures(6)；temperature distribution disciplines(6)；unidirectional ber reinforced(6)；ber reinforced composite(6)；translational symmetric structures(6)
- 被动语态估计：188；`we + 动作动词` 主动句估计：0
- 一般现在时线索：354；一般过去时线索：432；现在完成时线索：0；情态动词线索：91

章节词频：

- Abstract: unit(9)；boundary(7)；conditions(7)；cell(6)；thermal(4)；structure(4)；composites(3)；symmetric(3)
- Introduction: unit(29)；composites(24)；thermal(19)；cell(19)；composite(17)；symmetries(17)；structure(15)；structures(14)
- Conclusion: conditions(9)；boundary(8)；unit(7)；thermal(6)；composites(6)；symmetric(6)；structures(6)；cell(5)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Therefore, an RVE model should contain two essential elements, representative geometric structures and accurate BCs.
  可迁移模板：Therefore, an METHOD model should contain two essential elements, representative geometric structures and accurate BCs.
#### Gap句
- 原句/结构：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  可迁移模板：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句/结构：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  可迁移模板：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句/结构：For such composites, the reproduce of the real random multiphase microstructure is the first challenge in RVE model establishment.
  可迁移模板：For such composites, the reproduce of the real random multiphase microstructure is the first challenge in METHOD model establishment.
#### 方法句
- 原句/结构：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  可迁移模板：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句/结构：In this paper, a general rule of such unit cell formulation is developed.
  可迁移模板：In this paper, a general rule of such unit cell formulation is developed.
- 原句/结构：Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
  可迁移模板：Two key steps are involved, the identification of structure symmetries and the derivation of boundary conditions, in which the first step build a geometric model while the later one endows the model physical meanings to represent the original structure.
#### 结果句
- 原句/结构：An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
  可迁移模板：An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
- 原句/结构：Then, for more complex satin woven composites, structure symmetries indicated in the 4-, 5-, 6-, 7- and 8-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary conditions are derived in a unified form, and the identical results obtained by multi-size unit cells validate the unit cell and the boundary conditions.
  可迁移模板：Then, for more complex satin woven composites, structure symmetries indicated in the X-, X-, X-, X- and X-harness textiles are investigated, two unit cells of different sizes are formulated and the corresponding boundary conditions are derived in a unified form, and the identical results obtained by multi-size unit cells validate the unit cell and the boundary conditions.
- 原句/结构：An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
  可迁移模板：An axial study of unidirectional fiber reinforced composite is conducted to demonstrate the difference between the derived and the inappropriate boundary conditions in the physical mechanism point of view.
#### 贡献句
- 原句/结构：For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells.
  可迁移模板：For three typical translational, reflectional and X�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells.
- 原句/结构：For the transverse direction of the composite, four unit cell models of reducing sizes are established, and the basic process of unit cell formulations and boundary conditions derivations is stated.
  可迁移模板：For the transverse direction of the composite, four unit cell models of reducing sizes are established, and the basic process of unit cell formulations and boundary conditions derivations is stated.
- 原句/结构：For three typical translational, reflectional and 180�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells.
  可迁移模板：For three typical translational, reflectional and X�rotational symmetric structures, the temperature distribution disciplines under different macroscopic thermal stimuli are revealed and summarized as two equations, and can be used to derive boundary conditions of unit cells.
#### 限制/边界句
- 原句/结构：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  可迁移模板：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句/结构：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
  可迁移模板：Effective thermal properties of macro composites with symmetric structures can be efficiently calculated by a size-limited representative unit cell.
- 原句/结构：Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost.
  可迁移模板：Such a model should contain adequate information of both macro and micro characteristics, like the macroscopic model size and the microscopic geometric structure, and thus needs considerable computational cost.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
