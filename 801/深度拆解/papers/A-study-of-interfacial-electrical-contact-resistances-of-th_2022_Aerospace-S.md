# A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations

## 0. 读取说明

本文拆解依据 `801/文本/txt/A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.txt` 的全文抽取。由于抽取文本存在双栏串行、图表跨栏和公式错位，图像云图、色标、局部粗糙形貌与部分公式排版需要 PDF 图像复核。以下分析以可从 txt 稳定确认的信息为主。

## 1. 基本信息与论文身份

- 题名：A study of interfacial electrical contact resistances of thermoelectric generators for hypersonic vehicles by experimental measurements and two-scale numerical simulations
- 作者：Ge Gao, Dou Li, Jian-Jun Gou, Chun-Lin Gong, Shuang-Ming Li
- 期刊：Aerospace Science and Technology, 131, 107966
- 年份：2022
- 领域：高超声速飞行器热管理、热电发电器、界面电接触、电-热耦合仿真。
- 论文类型：实验测量 + 两尺度数值模拟 + 工程性能评估。
- 研究对象：高超声速飞行器用 TEG 中 TE legs 与 copper electrodes 之间四类电接触界面：E-N_l、E-N_u、E-P_l、E-P_u。
- 方法：真实粗糙表面测量与重构、微米尺度接触力学/电传导仿真、ECR 实验平台验证、毫米尺度 TEG 等效界面层模型。
- 主要证据：粗糙度测量、接触应力/真实接触面积、电势和电流密度云图、ECR 随温度/压力/间隙介质变化曲线、实验-仿真误差表、TEG 内阻与最大输出功率对比。
- 目标读者：高超声速热防护/热管理研究者、TEG 设计者、界面接触建模与实验测量研究者。

## 2. 摘要与核心信息提取

一句话主张：高超声速飞行器 TEG 中 TE legs 与电极之间的微米粗糙界面会产生显著 ECR，必须通过真实形貌两尺度模型和实验测量定量计入，否则会严重高估 TEG 输出功率。

核心问题不是“TEG 能否发电”，而是“界面电接触非理想性是否足以改变 TEG 性能评估”。摘要先把工程背景定为高超声速气动热回收，再把瓶颈压缩到微米尺度粗糙度导致的电流收缩，最后用两尺度模型把微观 ECR 映射到宏观 TEG 输出功率。关键结论包括：空气间隙下 ECR 会使 TEG 最大输出功率较完美接触降低约 83%；银环氧胶间隙下影响约 2.0%；实验与数值整体吻合，最大差异在四个接触对中为 13.2%、14.9%、38.9%、17.7%。

## 3. 选题层深拆

问题来源来自工程瓶颈：高超声速飞行器表面气动热巨大，传统热防护系统的重量和体积可能不可承受，TEG 被引入作为能量回收式热管理方案。但 TEG 不是理想多材料串联体，TE legs 与电极存在粗糙接触界面，真实接触区域极小，电流被迫收缩通过少量 asperity，从而产生 ECR。

作者的收束方式很清楚：从“飞行器热管理”收束到“高超声速 TEG”，再收束到“四个 TE leg-electrode 接触界面”，最后收束到 ECR 对最大输出功率的影响。这个选题的价值在于把一个常被等效忽略的界面参数变成可测、可算、可进入系统性能模型的工程量。

为什么现在值得研究：前文已有 TEG 高超声速应用、热电材料、ECR 理论/测量/预测模型，但这些研究要么不针对高超声速 TEG，要么粗糙形貌依赖假设，要么只定性说明 ECR 重要。本文的切入点是“真实形貌 + 实验验证 + TEG 性能降额”三件事同时完成。

## 4. 领域位置与文献版图

文献版图可分为四组。

第一组是高超声速 TEG 与热管理应用。作者先说明 aerodynamic heat、hot fuel、engine combustion heat 三类热源，并引用本团队和他人关于多级 TEG、scramjet、Brayton-cycle + TEG 的工作，证明 TEG 在高温差场景下有应用前景。

第二组是热电材料与 TEG 构型。CoSb3 基 skutterudite 被定位为 800 K 以下具有潜力的块体热电材料，这使本文选用 Yb0.29Co4Sb12 与 La0.1Ce0.8Fe3CoSb12 具有工程背景。

第三组是 ECR 理论、实验和数值预测。作者列举动态模型、体积接触理论、数字万用表测量、X-ray CT 间接测量、微接触模型、随机粗糙体模型等，指出许多数值模型在粗糙表面构造中采用假设，可靠性受限。

第四组是 ECR 对 TEG/TEC 性能影响。已有研究指出 ECR 可能严重影响 TEG/TEC 设计优化，但高超声速 TEG 很少考虑 ECR。因此本文站位不是从零提出 ECR，而是把 ECR 放入高超声速 TEG 的真实几何和任务温度范围。

## 5. Gap 制造机制

作者制造 gap 的方式是“已有研究重要，但缺一个可验证的工程闭环”。

- 对象 gap：已有 ECR 研究不一定覆盖高超声速飞行器 TEG 的 TE leg-electrode 异质界面。
- 方法 gap：许多数值模型用随机或理想化粗糙形貌，本文强调真实表面形貌测量与重构。
- 验证 gap：ECR 预测若没有实验平台支撑，难以用于设计。
- 系统 gap：已有 TEG 性能评估很少把四个 ECR 界面等效为宏观模型中的界面层。

这个 gap 基本真实且重要。最强的一点是作者没有只说“ECR 重要”，而是把其影响换算成最大输出功率下降 83%。最弱的一点是实验验证只在有限压力和 298 K 条件下直接测 ECR，高温条件的模型可信度主要来自材料参数和仿真推断。

## 6. 创新性判断

作者声明的贡献包括：建立高超声速 TEG；基于真实粗糙形貌建立微米尺度 ECR 预测模型；搭建 ECR 测量平台并验证模型；把 ECR 作为等效界面层纳入毫米尺度 TEG，评估输出功率影响。

真实创新更像“工程建模链条创新”而不是基础理论创新。它把表面测量、接触力学、电传导、实验标定和 TE 转换性能串成一条链。创新强度为中等偏强：单个模块并非全新，但组合后解决了高超声速 TEG 设计中一个具体且高影响的非理想因素。

可能被挑战的地方：银环氧胶间隙把 ECR 降低约 1000 倍，这个结论很工程有用，但长期高温、热循环、力学可靠性和界面老化没有展开；空气间隙下 83% 降额很强，但同时未计入 thermal contact resistance，因此系统级真实性仍需与热接触模型联用。

## 7. 论证链条复原

论证链条如下：

高超声速飞行器气动热管理困难 → TEG 有潜力回收热量并供电 → TEG 中 TE legs 与 electrodes 是串联电流路径的关键界面 → 微米粗糙度导致真实接触面积小、电流收缩和 ECR → 现有模型依赖粗糙面假设且高超声速 TEG 少有 ECR 定量 → 本文测量真实形貌并建立微尺度接触/电传导模型 → 用实验平台验证 ECR → 把 ECR 等效成 TEG 界面层 → 计算内阻和最大输出功率变化 → 得出 ECR 不能忽略，导电界面材料和预压可缓解。

闭合度较好。背景、gap、方法、证据、结论都能互相回扣。薄弱环节是实验工况覆盖范围窄于仿真工况，且污染膜/氧化膜未进模型，导致 E-P_l 最大差异达到 38.9%。

## 8. 方法/理论/模型细拆

方法名称：真实形貌驱动的两尺度 ECR-TEG 性能预测框架。

输入包括：TE legs 与 electrodes 的 3D 光学测量表面、材料物性、温度、加载压力、间隙介质、TEG 几何和边界温度。输出包括：四个接触对的 ECR、等效界面层电导率、TEG 内阻和最大输出功率。

关键步骤：

1. 用 Bruker Contour GT-K 测量 TE legs 与 electrodes 粗糙面，每个粗糙面约 7700 数据点，并在 CATIA 中重构。
2. 在 ABAQUS 中建立微米尺度接触对模型，先做接触力学，再导入变形后的模型做电传导分析。
3. 对 ECR 计算等效界面层电导率，界面层厚度取对应粗糙面的平均距离。
4. 在 ANSYS Multiphysics 中建立毫米尺度 TEG 模型，因为 ABAQUS 不能模拟 Seebeck effect。
5. 搭建 ECR 实验平台，用压力装置、电源、数据采集系统和电阻箱测量不同压力下 ECR。

关键假设：闭合接触单元为 perfect contact；污染和氧化膜电阻不计；冷源假定为 kerosene，详细冷却过程不涉及；热接触电阻在本文 TEG 性能部分未考虑，主要考察 ECR 的电学影响。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 真实粗糙界面会显著限制实际电接触区域 | 方法与结果 5.1 | Fig. 2 重构粗糙面；Fig. 7/8 应力云图；真实接触面积在 0.3 MPa 以下最大小于 0.6% | 强 | 云图细节需 PDF 图像复核 |
| 加载压力增大可降低 ECR | 结果 5.3.2 | Fig. 15：四类接触对在空气与银环氧胶间隙下 ECR 随压力增大下降 | 强 | 压力范围有限，预压可靠性未评估 |
| 温度对 ECR 的影响依赖材料电导率变化 | 结果 5.3.1 | Fig. 14：N 型 ECR 随温度升高增加；P 型先增加后降低，解释为 TE 材料电导率变化 | 中-强 | 高温实验验证不足，主要来自仿真 |
| 银环氧胶间隙显著降低 ECR | 结果 5.2/5.3.2 | Fig. 10/13/15：银环氧胶提高非接触区电势与电流密度，ECR 约比空气小 1000 倍 | 强 | 长期服役、热循环和材料兼容性未展开 |
| 数值模型可预测不同环境下 ECR | 实验验证 5.3.3 | Table 4：四接触对实验-仿真最大差异 13.2%、14.9%、38.9%、17.7% | 中 | E-P_l 差异 38.9% 偏大，污染膜未建模 |
| ECR 会严重降低 TEG 最大输出功率 | 结果 5.4 | Fig. 19-21：空气间隙下 ECR 约为 TE 材料电阻 4 倍，最大输出功率降约 83% | 强 | 仅考察电接触，未和 TCR 同时耦合 |
| 高导电界面材料和适当预压可缓解负面影响 | 结论 | 银环氧胶条件功率仅降低约 2.0%，压力增大使 ECR 降低 | 中 | “适当预压”的结构安全边界需额外实验 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 TEG for hypersonic vehicles | 把宏观飞行器热管理问题收束到一个代表性 TEG 单元 | 研究对象具有工程真实性 | TEG 位于背风区，包含 substrates、TE legs、electrodes、PEEK shell | 需要 PDF 图像复核布局 |
| Table 1/2 材料物性 | 提供接触力学、电传导、TEG 仿真的参数基础 | 模型可复现 | 给出 TE 材料、铜、氧化铝、PEEK 的弹性、屈服、热/电导率 | 基本可从 txt 确认 |
| Fig. 2 粗糙面重构 | 支撑“真实形貌建模”创新 | 减少粗糙面假设 | 给出 N/P TE legs 与 electrode 的实测/重构表面 | 需要 PDF 图像复核粗糙面细节 |
| Fig. 3-5 模型和网格 | 说明两尺度模型如何连接 | 方法闭环 | 微尺度接触对与宏观 TEG 网格/界面层 | 需要 PDF 图像复核网格质量 |
| Eq. (12)-(13) TE 耦合控制方程 | 说明热、电、Seebeck/Peltier 耦合机制 | TEG 性能可计算 | 温度方程含 Joule/Peltier 项，电势方程含 Seebeck 项 | 公式排版需 PDF 复核 |
| Fig. 7-9 接触应力与面积 | 证明压力改变真实接触区域 | 压力降低 ECR 的物理原因 | 接触面积随压力近似线性增大 | 云图色标需 PDF 复核 |
| Fig. 10-13 电势/电流密度云图 | 揭示空气 vs 银环氧胶间隙的导电差异 | 高导电介质降低 ECR | 银环氧胶使非接触区电流显著增加 | 需要 PDF 图像复核 |
| Table 4 实验-数值 ECR | 验证模型可信度 | 模型可预测 ECR | 最大差异 38.9%，多数差异较小 | 可从 txt 确认 |
| Fig. 19-21 内阻与功率 | 将微观 ECR 转换为系统级输出降额 | ECR 不可忽略 | 空气间隙最大输出功率约为完美接触的 1/5 | 曲线细节需 PDF 复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The TEG and material properties of its components；3 Two-scale numerical model；4 Experimental measurement platform for ECR；5 Results and discussions；6 Conclusion，并含 Appendix A 材料制备与物性。

结构是典型工程建模论文：先立工程对象，再给材料和几何，再给模型，再给实验平台，最后结果分层展开。第 5 节内部顺序从 contact mechanics 到 electric conduction，再到 ECR 定量和 TEG performance，符合“微观机制 → 界面参数 → 系统性能”的推进逻辑。

标题命名偏好偏描述型，少用结论型标题。好处是稳健、工程论文可接受；缺点是标题本身不暴露最强发现，例如 `5.4 TE performance` 可以更有力地写成 “ECR-induced internal resistance dominates power degradation under air gaps”。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3.4.2 Heat conduction and TE conversion processes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Contact mechanics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.4 TE performance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 7 For the TEG applied to hypersonic vehicles, the negative in- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 1 The numerical models of the ECR prediction are established      Ge Gao: Data curation, Methodology, Software, Validation, Writ- | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2 The  contact  area  increases approximately  linear with the     ization, Investigation, Methodology, Project administration, Super- | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 With the growth of temperature, the ECRs between the N- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“高超声速热管理压力 → TEG 前景 → TEG 材料和结构 → 接触界面 ECR → 已有 ECR 研究 → 高超声速 TEG 未充分考虑 → 本文做什么”。每段都承担一个收束功能，没有长时间停留在大背景。

方法段落多采用“先给图，再解释图中的对象和参数，再说明软件/边界条件”的顺序。结果段落则经常以 “Fig. X shows...” 开头，然后分 a/b/c/d 子图逐一描述，最后用一句 “In short / Overall / In conclusion” 收束规律。

叙事节奏偏密集数据型。优点是证据充分；缺点是段落中数值很多，读者需要图表配合才能抓住主线。可学习的是每个结果小节都回到一个物理解释：接触面积、材料电导率、间隙介质导电性、内阻。

## 13. 文笔画像与语言习惯

整体语气谨慎但工程判断明确。高频表达包括 “It should be noted that”, “As shown in Fig.”, “In short”, “Overall”, “it can be found that”。作者很少用夸张形容词，更多用数值和趋势支撑判断。

时态上，背景和一般规律用一般现在时；实验和本文操作用一般过去时或现在完成时；图表解读用一般现在时。主动语态与被动语态混用，方法部分被动多，如 “is established”, “is simulated”, “is measured”；贡献陈述和结论中主动性较强，如 “we can conclude”。

情态动词使用克制，常用 “can be”, “should be”, “may”。名词化程度高：constriction, electrical contact resistance, compression displacement, equivalent interfacial layers, thermoelectric conversion process。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：contact(114)；teg(99)；ecr(85)；surface(74)；temperature(71)；leg(69)；electrical(58)；respectively(58)；loading(54)；heat(53)；gap(53)；legs(51)；about(50)；resistance(50)；org(49)；electric(47)；shown(47)；p-type(46)；rough(46)；surfaces(45)
- 高频学术名词：temperature(71)；resistance(50)；pressure(40)；model(37)；analysis(36)；conductivity(36)；materials(35)；stress(33)；performance(27)；material(26)；displacement(25)；condition(22)；science(22)；density(21)；properties(19)；energy(19)
- 高频学术动词：shown(47)；shows(21)；show(14)；developed(8)；simulated(7)；predicted(3)；validated(3)；compared(2)；predict(2)；simulate(2)；proposed(2)；evaluated(1)；solved(1)；indicates(1)；indicate(1)；compare(1)
- 高频形容词：electrical(58)；electric(47)；potential(44)；numerical(42)；thermal(41)；hypersonic(37)；experimental(30)；thermoelectric(30)；current(28)；elastic(26)；material(26)；displacement(25)；real(24)；adhesive(24)；cient(22)；interfacial(17)
- 高频副词/连接副词：respectively(58)；gradually(12)；mainly(8)；supply(7)；cantly(6)；spectively(5)；relatively(4)；slightly(4)；directly(3)；generally(2)；approximately(2)；numerically(2)；greatly(2)；usually(2)；evenly(2)；basically(2)
- 高频二词短语：rough surfaces(32)；loading pressure(32)；n-type leg(28)；p-type leg(26)；upper surface(26)；legs electrodes(22)；aerospace science(21)；science technology(21)；coe cient(21)；electrical conductivity(21)；electrical contact(20)；contact resistance(20)；gao gou(20)；compression displacement(20)；gou aerospace(19)；real contact(19)
- 高频三词短语：aerospace science technology(21)；gao gou aerospace(19)；gou aerospace science(19)；electrical contact resistance(15)；surface n-type leg(15)；surface p-type leg(15)；rough surfaces legs(13)；seebeck coe cient(13)；maximum output power(13)；output power teg(12)；internal electric resistance(10)；real contact area(10)

**主动、被动与句法**

- 被动语态估计次数：154
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：771
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：396
- 一般过去时线索：61
- 现在完成时线索：8
- 情态动词线索：64
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：contact(87)；surface(69)；ecr(69)；leg(62)；teg(60)；temperature(48)；legs(45)；respectively(45)
- 5.4. TE performance：org(48)；teg(39)；contact(27)；thermal(26)；electrical(26)；resistance(25)；temperature(23)；power(23)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`For hypersonic vehicles, ... is one of the most critical issues...`
- Gap 句式：`reported research ... rarely considered the influence of ... Thus, this leaves some room for this work.`
- 方法句式：`The whole process contains three steps: first..., second..., third...`
- 图表句式：`Fig. X shows the variation of Y with Z under ...`
- 结果句式：`with the increase of ..., the ... decreases/increases gradually.`
- 验证句式：`The experimental and numerical results have a relatively good agreement.`
- 边界句式：`It should be noted that ... is not considered.`
- 结论句式：`The influence of X on Y cannot be ignored.`

可复用表达策略：少用“novel”堆叠，用“rarely considered”“based on measured practical topography”“validated by a series of measurements”把创新落到可验证动作上。

## 15. 引用策略与文献使用

引用密度最高在 Introduction。作者先用高超声速热管理与 TEG 应用文献建立问题重要性，再用 TE 材料文献证明材料选择合理，随后集中引用 ECR 理论、实验和数值预测文献，最后引用 ECR 对 TEG/TEC 性能影响的研究来铺垫本文必要性。

引用姿态以继承和补充为主，批判较温和。作者不直接否定前人，而说已有模型“adopted some assumptions”或高超声速 TEG “rarely considered” ECR。这种写法适合工程应用论文：避免过度对立，同时明确留白。

gap 与引用的连接方式是：已有 TEG 应用证明重要性；已有 ECR 研究证明问题存在；已有 ECR 影响研究证明后果严重；但高超声速 TEG 真实界面缺验证模型，所以本文进入。

## 16. 审稿人视角风险

1. 实验验证温度主要在 298 K 和有限压力下，仿真拓展到 325-725 K 的可信度依赖材料参数与模型假设。
2. E-P_l 最大实验-数值差异 38.9%，虽然作者解释污染膜/氧化膜，但模型未纳入这一机制。
3. 闭合接触单元 perfect contact、污染膜不计、间隙介质理想化，可能低估真实 ECR。
4. 只讨论 ECR 对 TEG 电性能影响，没有与 TCR、热辐射、机械热循环等联立。
5. 银环氧胶作为缓解方案，需要耐高温、热膨胀失配、老化、脱粘等长期可靠性评估。
6. 冷源 kerosene 只是设定，没有展开燃油冷却系统边界，系统级应用仍是局部模型。

## 17. 可复用资产

- 选题套路：从宏观工程系统中挑一个被理想化忽略的界面非理想因素，证明其对系统性能有数量级影响。
- 方法套路：真实形貌测量 → 微尺度接触模型 → 实验验证 → 宏观等效层 → 系统性能降额。
- 证据套路：先机制云图，再参数曲线，再实验对比表，最后系统级性能图。
- 图表套路：用 Fig. 19-21 把局部界面电阻变成 TEG 内阻和输出功率，避免停留在局部现象。
- 写法套路：每一小节用 “As shown in Fig.” 展示，再用 “In short” 收束规律。

## 18. 对我写论文的启发

如果我的论文想研究工程系统中的局部界面/连接/接触问题，可以学习本文的“局部参数系统化”方法：不要只证明局部现象存在，而要把它等效进入整体模型，并用整体性能指标证明其不可忽略。

Introduction 可借鉴其渐进收束：大工程痛点不必展开太久，尽快进入具体部件和界面。Results 可借鉴其层层递进：几何/力学证据解释为什么有接触电阻，电学证据量化接触电阻，系统证据说明工程后果。

## 19. 最终浓缩

本文最值得学习的是把 ECR 这个微尺度接触问题写成了高超声速 TEG 设计必须考虑的系统级问题。最强证据是空气间隙下最大输出功率降低约 83%，最强写作资产是“两尺度模型 + 实验验证 + 等效界面层”的论证链。最大风险是高温、污染膜、热循环和热接触效应尚未完全纳入，适合与后续 TCR/NFTR 工作联读。
