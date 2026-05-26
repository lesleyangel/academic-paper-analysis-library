# A novel mechanical-thermal-electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles

## 0. 读取说明

本拆解基于 `801/文本/txt/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.txt` 的全文抽取结果。抽取文本能确认题名、摘要、章节、材料、模型流程、主要数值结论和图表标题；但 Fig. 7-Fig. 16 中大量云图、曲线、节点位置和颜色分布只能从文字说明间接判断，涉及空间位置、色标和局部极值的细节均标注为“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：A novel mechanical-thermal-electrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles
- 作者：Ge Gao, Jian-Jun Gou, Chun-Lin Gong, Jia-Xin Hu, Rui-Chao Gao
- 期刊与年份：Composite Structures, 268, 2021, 113962
- 机构：Northwestern Polytechnical University, School of Astronautics
- 领域：高超声速飞行器热防护系统、多功能结构、热电转换、有限元多尺度分析
- 论文类型：工程概念设计 + 多尺度数值模拟 + 热-力-电性能评估
- 研究对象：安装在高超声速运载器二级压缩面的 MTPS，宏观为 8 块 MTPS plate，细观为 288 个 MTPS unit。
- 方法组合：整机载荷分析、MTPS 板级位移边界插值、MTPS 单元热-力耦合有限元、热电输出后处理。
- 主要证据：整机/板/单元三级应力云图，单元温度场，TE 材料节点温度与应力曲线，电性能曲线，质量与电输出表格。

这篇论文的身份不是单纯材料性能论文，而是“把热防护结构变成能承载、隔热、发电的系统方案”的工程构型论文。它的贡献重心在概念完整性和边界条件传递，而非单个热电材料性能刷新。

## 2. 摘要与核心信息提取

摘要的说服结构很清楚：先指出 MTPS 具有热电转换和承载附加功能；再说明该概念在宏观上是板、在细观上是单元；然后把单元拆成 TE module 与 gap TPS；最后用多尺度分析证明载荷边界准确性和三功能可行性。

一句话主张：作者提出一种包含两级 TE 层、承载框架、蜂窝芯、嵌入导电片和低模量胶层的机械-热-电一体化热防护系统，并用整机-板-单元多尺度有限元证明它可同时承担承载、隔热和供电功能。

核心信息：

- 问题：传统 TPS 只耗散或阻挡气动热，无法复用热能，且既有 TE-TPS 结构细节和气动力载荷考虑不足。
- 方法：将整机气动力/热流映射到 MTPS plate，再把 plate 位移边界传给 unit，形成更真实的单元级热-力边界。
- 创新：两级高温/中温 TE 层、细观结构完整化、热应力释放设计、多尺度位移边界传递。
- 主要结果：单元平均输出功率 0.88 W、平均转换效率 0.51%，整套 288 单元约 253.44 W；TE 转换效率相对前作从 0.237% 提高到 0.51%。

## 3. 选题层深拆

选题来自三个工程矛盾叠加。第一，Hypersonic launch vehicle 面临强气动热，TPS 是刚需；第二，传统 TPS 的热是被浪费的，从能源利用角度低效；第三，热电模块可以复用热，但如果直接贴到 TPS 上，会引入结构承载、热应力集中、边界条件失真等问题。

作者把大问题收束为一个可建模问题：在一个特定高超声速运载器二级压缩面上，设计一个可装配的 MTPS unit，并在整机真实载荷路径下验证它的机械、热和电性能。这个收束很有效，因为它避免泛泛讨论“热电热防护是否有前途”，而是把问题转成：几何、材料、边界、热流、应力、电输出能否闭合。

选题价值主要是工程价值和方法价值：工程上尝试把 TPS 从“被动防热”升级为“承载 + 防热 + 供电”；方法上强调多尺度边界传递，回应很多单胞分析只用简化边界的问题。它也有明显应用牵引：如果数百瓦级热电输出成立，可替代部分机载电源，节省内部空间。

## 4. 领域位置与文献版图

Introduction 的文献版图按系统类型组织，而不是按时间线组织：

- ITPS：能兼顾承载与热防护，但存在 thermal short-circuit effect。
- ATPS：主动冷却能力强，但需要冷却剂和复杂附属系统，成本高。
- UHTC：适合最严苛热载荷位置，但韧性不足。
- Ablative TPS：可带走热量，但一次性使用且改变外形。
- TE conversion/TE generator：可回收热能，已有多级 TE、三维耦合模型和高超声速应用探索。
- 作者前作：已有 TE module-based MTPS，但仅一级高温 TE、细节不足、热力分析未考虑气动力载荷。

本文站位是“继承前作 + 修正边界 + 完整化结构”。它不是推翻 ITPS/ATPS，而是把它们的不足转化为本文 gap：既有系统缺热复用，既有 TE-TPS 缺细观结构和真实载荷链。

## 5. Gap 制造机制

作者制造 gap 的方式很典型：先列出传统 TPS 类型并逐项指出局限，再转向 TE 技术的机会，最后回到作者前作的三个不足。

关键 gap：

- 功能 gap：现有 TPS 多数只防热或冷却，不能复用气动热。
- 结构 gap：前作三层结构只示意，没有导电片、承载框、蜂窝芯、胶层等可装配细节。
- 性能 gap：单级高温 TE 层导致转换效率偏低。
- 边界 gap：前作热机械分析只考虑热应力，没有考虑气动力载荷及其从整机到单元的传递。

这个 gap 比较可信，因为作者没有只说“缺少 MTPS”，而是把“为什么前作还不够”拆成结构、效率、载荷三个可验证维度。风险在于文献对“最接近的多功能 TPS/TE-TPS”覆盖可能仍偏向作者团队体系，需复核是否遗漏同期多级 TE/TPS 方案。

## 6. 创新性判断

作者声明的创新主要有三项：两级 TE 层提高效率；细观结构细节被纳入；嵌入导电片和低模量胶层等热应力释放设计。另一个隐含创新是多尺度边界传递方法。

真实创新判断：

- 构型创新：中等偏强。把 TE layer、load-bearing frame、honeycomb cores、gap TPS、adhesives 组合成可分析单元。
- 方法创新：中等。整机-板-单元的边界传递更像工程建模策略，不是新的数学方法，但对该问题必要。
- 证据创新：中等。给出 21 页较完整的有限元链条，但缺实验验证。
- 应用创新：较强。把热电转换放入高超声速运载器局部热防护板，面向明确工况。

创新可信度来自与作者前作的直接对比：平均转换效率由 0.237% 到 0.51%，且在结构中引入两级 TE 和缓释应力设计。但它仍容易被审稿人追问：额外质量 1156.97 g/单元是否抵消供电收益？理想 Tie 约束是否高估结构可靠性？

## 7. 论证链条复原

论文论证链条如下：

高超声速气动热严重，传统 TPS 低效且不能热复用 -> TE 转换可利用温差发电，但需要和 TPS、承载结构集成 -> 作者前作存在一级 TE、结构示意化、缺气动力载荷三个不足 -> 本文提出两级 TE MTPS unit，并部署到具体运载器二级压缩面 -> 用整机分析获取气动力和位移边界，用 plate 分析传递到 unit，用 unit 分析验证热-力-电性能 -> 得出 MTPS 可承载、防热并输出电能。

逻辑闭合度较高。最强环节是“gap 对方法”的对应：每个前作不足都有结构或分析上的补丁。最薄弱环节是“数值可行性到工程可用性”的跳跃：装配、疲劳、热循环、界面退化、TE 材料长期高温稳定性没有充分证据。

## 8. 方法/理论/模型细拆

方法是三级多尺度数值链：

1. Vehicle scale：用 MSC Patran/Nastran 分析整机在典型轨迹上的气动力作用，提取二级压缩面的载荷和位移。
2. Plate scale：建立 1 m2 MTPS plate，使用整机位移插值作为板边界，确定局部 MTPS 单元的结构设计点。
3. Unit scale：基于 CAD 的 MTPS unit 模型，在 ABAQUS 中用 C3D8T 热-力耦合单元分析温度场和应力场，再由 TE 材料温差和 Seebeck 系数计算电性能。

关键模型假设：

- 焊接和胶接界面用 Tie 约束模拟，认为界面理想。
- 气动热流沿用作者前作数据，机械载荷由整机/板传递。
- 热-力耦合考虑材料非线性和热边界非线性，但电性能更多是后处理计算。
- 位移边界通过非线性插值获取，强调边界比简化周期/固定边界更合理。

复现信息较充分：给出几何尺寸、材料选择、质量、软件、网格规模、关键方程和边界传递流程。缺口是材料温度依赖参数、界面失效准则和 TE 电路连接细节仍需 PDF/附表复核。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 多尺度分析对获得准确机械边界是必要的 | 摘要、4.2、结论 | 整机应力、plate 位移插值、unit 边界传递；Fig. 7-Fig. 10 | 中-强 | 缺少与简化边界的系统误差量化，图像细节需要 PDF 图像复核 |
| 两级 TE 层比前作单级结构更高效 | 摘要、4.3.2、结论 | 平均功率 0.88 W，效率 0.51%；前作效率 0.237%；同一结构中若中温层使用高温材料则 0.82 W/0.45% | 中 | 对比不一定完全等工况；TE 性能计算依赖材料参数 |
| 嵌入导电片和低模量胶可缓解热应力集中 | 2、4.3.1、结论 | 结构设计解释；TE 材料和胶层应力被控制，结论称承载部件 <650 MPa、TE 材料 <150 MPa | 中 | Tie 约束和理想界面可能低估真实界面应力 |
| MTPS 具有承载、防热、供电三功能 | 摘要、结论 | 温度场最高 927/665/368 K 时序，应力场在可承受范围，电输出曲线和 Table 6 | 中-强 | 没有实验、疲劳和寿命验证 |
| 整套 MTPS 可提供约 253.44 W 平均功率 | 4.3.2 | 单元平均 0.88 W × 288 units | 中 | 串联电路、负载匹配、实际热流非均匀、电接触损失需复核 |
| 该构型的质量仍需后续优化 | 2 | MTPS unit 1156.97 g，其中 TE module 904.10 g，TE layer 733.0 g | 强 | 该风险被作者承认，但未纳入性能-质量权衡指标 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：整机与 MTPS 布置，承担“应用场景落地”功能，说明不是孤立单胞。需要 PDF 图像复核。
- Fig. 2：MTPS unit 的 CAD、截面和 3D 打印模型，是全文最关键结构证据，支撑“细节完整化”和“可装配性”。需要 PDF 图像复核。
- Table 1：单元质量分解，支撑工程可行性和重量风险讨论。
- Table 2：相关材料物性，支撑热-力电多材料建模；需复核温度依赖参数是否完整。
- Fig. 3：整机-板-单元分析流程，承担方法框架图功能。
- Fig. 4-Fig. 6：三级模型、网格、边界和载荷，支撑复现性。
- Fig. 7/Table 5：整机应力分布和二级压缩面最大应力，说明设计点选择依据。
- Fig. 8-Fig. 10：plate 位移边界与 unit 位移边界，支撑“多尺度边界传递”的核心 claim。
- Fig. 11-Fig. 13：温度场、应力场和节点曲线，构成热-力安全性主证据。云图色标和局部集中位置需要 PDF 图像复核。
- Fig. 14-Fig. 16/Table 6：TE 材料选择、温度分布、电性能、输出功率/效率，构成发电能力证据。
- 公式 (1)-(4)：平衡方程、应变-位移关系、热弹性方程和本构方程，作用是把 ABAQUS 热-力耦合问题放到连续介质力学框架中。

## 11. 章节结构与篇章布局

真实章节顺序：1 Introduction -> 2 The vehicle and the MTPS -> 3 Numerical model -> 4 Results and discussions -> 5 Conclusion。

结构不是标准 IMRaD 的实验论文，而是“背景/gap -> 工程对象与构型 -> 多尺度模型 -> 分尺度结果 -> 结论”。第 2 节先给 vehicle 和 MTPS，避免方法节悬空；第 3 节再给控制方程和三级模型；第 4 节按 vehicle、plate、unit 递进，和方法尺度一一对应。

标题命名偏好是描述型和对象型：Vehicle、MTPS plate、MTPS unit、Thermal-mechanical performance、Electrical performance。优点是路线清楚；弱点是标题不直接暴露发现，例如 `4.2 MTPS plate` 可改成 `Boundary transfer and stress response of MTPS plate`，信息量更高。

章节推进节奏：

- Introduction：大背景 -> TPS 类型分类 -> TE 技术机会 -> 作者前作不足 -> 本文目标。
- Section 2：先宏观部署，再细观结构，再材料和质量。
- Section 3：从通用方程到整机、板、单元模型。
- Section 4：从整机边界来源到板级筛选，再到单元热力电性能。
- Conclusion：按边界、多级 TE、应力缓解、结构尺寸和整体功率收束。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：5
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                     designed a novel ITPS, which was consisted of C/SiC composite corru- | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 3.3 MTPS plate | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.4 MTPS unit | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Vehicle | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 段落节奏是“问题分类 + 局限递进 + 本文补位”。第一段用高超声速气动热和能量浪费提出工程压力；第二段列 ITPS/ATPS/UHTC/ablative TPS；第三段逐项说局限；第四段转向 TE conversion；第五段承认作者前作不足；最后一段给本文任务。

方法段落节奏偏工程说明：先给模型对象，再给边界条件，再给软件与网格，最后给方程。结果段落常以 `Fig. X is/shows...` 起手，随后按时间点或部件列数值，最后提炼一句机制或设计含义。

可学习的段落套路：在复杂工程构型论文中，作者没有一上来堆公式，而是先把对象和结构讲清楚，再让公式服务模型。这种“构型先行、方程后置”的顺序适合多功能结构设计类论文。

## 13. 文笔画像与语言习惯

整体语气是工程可行性证明型。强 claim 使用 `developed`, `essential`, `multi effective functions`；结果描述大量使用 `maximum`, `average`, `respectively`, `reaches`，强调数值边界。谨慎性主要体现在承认质量较高、实验研究有限和进一步优化空间。

主动/被动偏好：贡献和设计动作多用主动 `we developed`, `we established`；模型和仿真步骤多用被动或无主句，如 `is used`, `is established`, `is assumed`。时态上，引言综述用现在完成时和一般过去时，方法用一般现在时，结果用一般现在时描述图表、过去时描述建模操作。

高频术语集中在 `MTPS`, `stress`, `materials`, `unit`, `heat`, `layer`, `load-bearing`, `boundary`, `power`，说明语言中心与贡献中心一致。形容词多为工程限定词：`multi-functional`, `high-temperature`, `low-modulus`, `non-uniform`, `accurate`。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：mtps(128)；temperature(118)；mpa(85)；stress(78)；materials(77)；maximum(75)；vehicle(72)；unit(71)；thermal(67)；heat(64)；respectively(64)；load(52)；layer(51)；high(43)；system(39)；bearing(38)；shown(38)；analysis(37)；nodes(36)；plate(35)
- 高频学术名词：temperature(118)；stress(78)；materials(77)；analysis(74)；structure(48)；system(39)；protection(32)；performance(31)；model(28)；structures(26)；conditions(24)；electricity(21)；energy(15)；insulation(15)；displacement(11)；properties(10)
- 高频学术动词：shown(38)；proposed(9)；developed(9)；show(7)；evaluated(7)；shows(7)；compared(3)；investigated(3)；simulate(3)；simulated(1)；derive(1)；predicted(1)；solved(1)；indicates(1)；derived(1)；investigate(1)
- 高频形容词：thermal(67)；high(43)；mechanical(33)；aerodynamic(33)；ceramic(32)；boundary(26)；numerical(20)；local(20)；hypersonic(20)；thermoelectric(19)；electrical(19)；low(13)；structural(12)；resistant(11)；displacement(11)；dynamic(10)
- 高频副词/连接副词：respectively(64)；rapidly(20)；gradually(17)；mainly(12)；however(5)；supply(5)；notably(2)；ciently(2)；actively(2)；tively(2)；relatively(2)；severely(2)；obviously(2)；extremely(1)；especially(1)；widely(1)
- 高频二词短语：mtps unit(64)；load bearing(32)；mtps plate(32)；high temperature(29)；bearing frame(28)；mpa mpa(28)；thermal protection(24)；alumina ceramic(24)；mpa respectively(24)；composite structures(22)；temperature materials(21)；boundary conditions(20)；gao composite(20)；mid temperature(19)；electricity conducting(17)；maximum value(17)
- 高频三词短语：load bearing frame(25)；gao composite structures(20)；mpa mpa respectively(17)；electricity conducting plates(13)；thermal protection system(11)；second stage compression(11)；alumina ceramic layer(10)；alumina ceramic layers(10)；mid temperature materials(10)；high temperature materials(9)；stage compression surface(9)；aerosp sci technol(8)

**主动、被动与句法**

- 被动语态估计次数：138
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：507
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：317
- 一般过去时线索：39
- 现在完成时线索：5
- 情态动词线索：47
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：thermal(6)；mtps(5)；protection(4)；concept(4)；vehicle(4)；load(4)；bearing(4)；multi(4)
- 1. Introduction                                                     designed a novel ITPS, which was consisted of C/SiC composite corru-：mtps(52)；vehicle(45)；temperature(28)；materials(25)；heat(23)；tps(23)；thermal(22)；high(20)
- 3.3. MTPS plate：heat(13)；plane(11)；system(8)；aerodynamic(7)；considered(6)；mtps(6)；boundaries(6)；mechanical(5)
- 3.4. MTPS unit：temperature(86)；mpa(85)；maximum(74)；stress(68)；mtps(63)；respectively(58)；materials(49)；unit(45)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

可复用问题句：

- `Although the above TPS have their own advantages, some limitations have to be stated...`
- 模仿：虽然已有 X 方案分别解决了 A/B/C，但在 Y 维度仍留下不可忽略的工程缺口。

可复用 gap 句：

- `This leaves some rooms for this work.`
- 模仿：这些不足为本文在结构细节、边界条件和性能验证方面的进一步推进留下空间。

可复用方法句：

- `The mechanical-thermal-electrical performance is evaluated based on the multi-scale analysis of...`
- 模仿：本文基于系统级、部件级和单元级的多尺度分析评估 X 的耦合性能。

可复用结果句：

- `The results show that the multi-scale analysis is essential to ensure...`
- 模仿：结果表明，若不显式传递上级边界，单元级响应会失去工程可信度。

常用词组：`load bearing`, `thermal protection`, `power supply`, `aerodynamic heat`, `thermal stress concentration`, `displacement boundary conditions`, `TE conversion efficiency`。

## 15. 引用策略与文献使用

引用主要服务四个功能：

1. 背景合法化：用 [1-8] 支撑 hypersonic heating 和 TPS 重要性。
2. 类型分类：用 ITPS、ATPS、UHTC、ablative TPS 文献构造领域版图。
3. 技术转向：用 TE materials、TE generator、热电耦合模型文献说明热复用可行。
4. 前作衔接：用作者前作 [38] 制造最直接 gap，并提供热流数据来源。

引用姿态整体温和：对前人先承认优势，再列局限。最有力的引用策略是把“传统 TPS 的局限”和“作者前作的局限”分开，前者说明研究方向重要，后者说明本文改进必要。

风险：文献图谱较偏工程系统与作者团队技术线，若目标期刊审稿人来自热电材料方向，可能会要求更系统比较多级 TE generator 和高温 TE 材料长期稳定性。

## 16. 审稿人视角风险

- 实验缺失：3D 打印模型只验证装配理性，不能验证热-力-电性能。
- 界面理想化：Tie 约束忽略胶层老化、脱粘、接触热阻和电接触损失。
- 重量收益比：单元质量 1156.97 g，整机 288 单元质量显著，需和 253.44 W 平均功率做系统权衡。
- 电性能后处理：实际串联、电阻、负载匹配、温度非均匀、导线可靠性没有充分展开。
- 载荷覆盖有限：典型轨迹和特定二级压缩面不能代表更宽 flight envelope。
- 强 claim 风险：`power supply` 容易被理解为独立供电，实际上更像部分替代或补充供电。
- PDF 复核点：所有云图最大值位置、节点曲线、导电片嵌入几何和色标需要复核。

## 17. 可复用资产

- 选题套路：从“传统系统低效”切入，再引入“多功能集成”作为改进方向。
- Gap 套路：先列已有类型优缺点，再列自己前作不足，形成双层 gap。
- 方法套路：整机级载荷 -> 板级边界 -> 单元级性能，适合任何多尺度工程结构分析。
- 图表资产：构型图 + 分析流程图 + 网格边界图 + 分尺度结果云图 + 关键性能表。
- 结果表达：把最大值、平均值、对比前作提升和工程尺寸放在同一结论中。
- 风险控制：主动承认质量偏大和需要进一步结构优化，降低审稿人对过度乐观的反感。

## 18. 对我写论文的启发

如果写多功能结构或热管理论文，可以学习它的“工程对象具体化”：不要只说提出一种结构，而要马上说明安装位置、面积、单元数量、尺寸、质量和载荷来源。

另一个启发是 contribution 要和前作缺陷一一对应。本文前作有三点不足，本文正好给三项改进，这会让审稿人很容易判断“为什么需要这篇新论文”。

需要谨慎模仿的是数值证明的强度。没有实验时，最好在标题、摘要和结论里用 `concept`, `evaluation`, `potential` 控制边界，不要把仿真可行性写成工程成熟度。

## 19. 最终浓缩

这篇论文最值得学习的是：把一个多功能热防护概念拆成可部署、可建模、可计算的三级工程系统，并用前作不足驱动结构改进。

最大风险是：结论依赖理想界面和数值仿真，真实装配、热循环、界面退化和质量收益比尚未被实验闭合。

可迁移的三件事：

1. 用“现有系统功能缺失 + 前作模型不足”制造强 gap。
2. 用“整机-部件-单元”的多尺度链条提高边界条件可信度。
3. 用图表顺序还原设计逻辑：应用场景、结构细节、分析流程、边界传递、性能结果。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.txt` 与 `801/文本/metadata/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 The vehicle and the MTPS （对象/问题/模块）
- L2 p.3: 3 Numerical model （方法/模型）
  - L3 p.3: 3.1 Governing and constitutive equations （对象/问题/模块）
  - L3 p.3: 3.2 Vehicle （对象/问题/模块）
  - L3 p.5: 3.3 MTPS plate （对象/问题/模块）
  - L3 p.7: 3.4 MTPS unit （对象/问题/模块）
- L2 p.7: 4 Results and discussions （结果/讨论/验证）
  - L3 p.7: 4.1 Vehicle （对象/问题/模块）
  - L3 p.9: 4.2 MTPS plate （对象/问题/模块）
  - L3 p.9: 4.3 MTPS unit （对象/问题/模块）
    - L4 p.9: 4.3.1 Thermal-mechanical performance （对象/问题/模块）
    - L4 p.17: 4.3.2 Electrical performance （对象/问题/模块）
- L2 p.18: 5 Conclusion （结论）
- L2 p.20: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.20: Declaration of Competing Interest （对象/问题/模块）
- L2 p.20: Acknowledgements （对象/问题/模块）
- L2 p.20: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 The vehicle and the MTPS | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Numerical model | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Governing and constitutive equations | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Vehicle | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 MTPS plate | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 MTPS unit | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Results and discussions | 7 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Vehicle | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 MTPS plate | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 MTPS unit | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.1 Thermal-mechanical performance | 9 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.2 Electrical performance | 17 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusion | 18 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of Competing Interest | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 20 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 本文为高超音速运载火箭开发了一种具有热电（TE）转换和承载附加功能的多功能热保护系统（MTPS）概念。这个概念是宏观尺度上的板块和中尺度上的单位。介观单元由TE模块和TPS间隙组成。 TE模块由氧化铝陶瓷层和纤维隔热层组成，用于消散一定量的气动热；高温和中温TE层，用于将气动热有效地转化为电能；承载框架和蜂窝芯，以提高承载能力；TE材料中嵌入导电板和低模量高温粘合剂，以缓解热应力。基于飞行器、MTPS板和MTPS单元的多尺度分析，评估了MTPS的机械热电性能，并建立了不同尺度之间机械边界条件的传递方法。结果表明，多尺度分析对于保证边界条件的准确性至关重要，所开发的MTPS概念具有承载、热防护和供电等多重有效功能。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusion；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-novel-mechanical-thermal-electrical-thermal-protection-syste_2021_Composit.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项工作中，我们开发了一种集承载、热保护和供电于一体的多功能TPS概念，该概念在宏观尺度上包含8个MTPS板，在介观尺度上包含288个MTPS单元。设计了导电板、承载框架、蜂窝芯材、粘合层等细节，研究了它们对结构机械热电性能的影响，开发了一种获取精确机械边界条件的多尺度方法。结果显示了一些结论：
> 
> G.高等人。复合结构 268 (2021) 113962
> 
> 对流系数(W/(m2·K)) 输出功率(W) TE转换效率(%)
> 
> 10 14.42 0.88 11.12 0.51
> 
> 最大平均 最大平均
> 
> G.高等人。复合结构 268 (2021) 113962
> 
> 分别为1156.97克、904.10克、733.0克和252.87克。当假设MTPS单位为车辆二级压缩面的TPS时，平均输出功率和TE转换效率分别为0.88 W和0.51%。 5. 对于本工作中提出的MTPS，它在宏观尺度上包含8个MTPS板，在介观尺度上包含288个MTPS单元。 MTPS内壁最高温度为360 K，平均输出功率为253.44 W。

### 20.7 论文逻辑脉络复核

- 提出的问题：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. The structural design points of the MTPS unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. 2.
- 旧方法/已有研究不足：需结合 Introduction 的文献转折句复核。
- 本文解决方式：In this paper, a multifunctional thermal protection system (MTPS) concept with additional functions of thermoelectric (TE) conversion and load bearing is developed for a hypersonic launch vehicle. The mechanical‐thermal‐electrical performance of the MTPS is evaluated based on the multi‐scale analysis of the flight vehicle, MTPS plate and MTPS unit, and the transfer method of mechanical boundary conditions between different scales is developed. The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
- 学术/工程增量：The TE module consists of an alumina ceramic layer and a fiber insulation layer to dissipate certain amount of the aerodynamic heat, a high‐temperature and a mid‐temperature TE layers to efficiently convert aerodynamic heat into electric energy, a load‐bearing frame and honeycomb cores to improve the load bearing capacity, embedded electricity conducting plates in TE materials and low‐modulus high‐temperature adhesives to alleviate the thermal stress. The improvement of the TPS and the development of heat reusing technologies become the key points of thermal management of hypersonic vehicles. Lin et al. [9] proposed a series of ITPS with different gradient hollows to improve the structural efficiency.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：85
- Introduction 引用簇数量（估计）：26
- References 条目数（解析）：51
- 可识别年份条目数：56
- 近五年/近年文献（2021+）数量：2
- 经典文献（2010年前）数量：12
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Composite Structures(1)
- 引用簇样例：[13], [14], [15], [16], [17], [9], [18], [10], [19], [11], [12], [20]

带引用的 gap/转折句样例：

- With the development of hypersonic engineering, thermal protection system (TPS) [5–8] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus TPS is low‐efficiency.
- The authors also proposed a TE module based on the MTPS concept and evaluated its mechanical‐thermoelectric performance in [38], however, the three limitations of the structure and analysis should be mentioned here: 1st, the structure has only one TE stage of high‐temperature TE materials, which leads to low TE conversion efficiency; 2nd, the three‐layer structure is only schematically described and no more details are involved; 3rd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.

References 解析样例（前12条）：

- [1] Qu F, Chen J, Sun Di, Bai J, Zuo G. A grid strategy for predicting the space plane’s hypersonic aerodynamic heating loads. Aerosp Sci Technol 2019;86:659–70.
- [2] Xiao H, He QJ. Aero-heating in hypersonic continuum and rarefied gas flows. Aerosp Sci Technol 2018;82-83:566–74.
- [3] Shahverdi H, Khalafi V. Bifurcation analysis of FG curved panels under simultaneous aerodynamic and thermal loads in hypersonic flow. Compos Struct 2016;146:84–94.
- [4] Uyanna O, Najafi H. Thermal protection systems for space vehicles: A review on technology development, current challenges and future prospects. Acta Astronaut 2020;176:341–56.
- [5] Blosser ML, Chen RR, Schmidt IH, Dorsey JT, Poteet CC, Bird RK. Advanced metallic thermal protection system development. 40th AIAA Aerosp Sci Meet Exhib 2002.
- [6] Pichon T, Barreteau R, Soyris P, Foucault A, Parenteau JM, Prel Y, et al. CMC thermal protection system for future reusable launch vehicles: Generic shingle technological maturation and tests. Acta Astronaut 2009;65(1-2):165–76.
- [7] Behrens B, Müller M. Technologies for thermal protection systems applied on reusable launcher. Acta Astronaut 2004;55(3-9):529–36.
- [8] Glass DE. Ceramic matrix composite (CMC) thermal protection systems (TPS) and hot structures for hypersonic vehicles. 15th AIAA Int Sp Planes Hypersonic Syst Technol Conf 2008::1–36.
- [9] Lin K, Hu K, Gu D. Metallic integrated thermal protection structures inspired by the Norway spruce stem: Design, numerical simulation and selective laser melting fabrication. Opt Laser Technol 2019;115:9–19.
- [10] Wei K, Cheng X, Mo F, Wen W, Fang D. Design and analysis of integrated thermal protection system based on lightweight C/SiC pyramidal lattice core sandwich panel. Mater Des 2016;111:435–44.
- [11] Wang X, Wei K, Tao Y, Yang X, Zhou H, He R, et al. Thermal protection system integrating graded insulation materials and multilayer ceramic matrix composite cellular sandwich panels. Compos Struct 2019;209:523–34.
- [12] Li Y, Zhang Lu, He R, Ma Y, Zhang K, Bai X, et al. Integrated thermal protection system based on C/SiC composite corrugated core sandwich plane structure. Aerosp Sci Technol 2019;91:607–16.

### 20.9 常用词、词类、语态与时态

- 高频词：mtps(102)；mpa(83)；stress(77)；temperature(70)；vehicle(67)；fig(66)；heat(58)；respectively(55)；unit(51)；maximum(50)；load(48)；layer(46)；materials(45)；thermal(39)；plate(35)；bearing(34)；nodes(33)；aerodynamic(30)；high(30)；stresses(30)
- 高频名词化/学术名词：temperature(70)；structure(21)；performance(17)；electricity(17)；compression(17)；insulation(14)；protection(12)；displacement(10)；conversion(9)；position(8)；concentration(8)；distribution(8)；direction(7)；equipment(7)；ture(6)
- 高频学术动词：developed(7)；optimized(2)；compared(2)；derived(1)；derive(1)
- 高频形容词：thermal(39)；aerodynamic(30)；mechanical(29)；ceramic(28)；boundary(24)；table(12)；hypersonic(11)；resistant(11)；structural(11)；displacement(10)；numerical(7)；adhesive(7)；equipment(7)；sic(6)；previous(6)
- 高频副词：respectively(55)；mainly(12)；rapidly(12)；gradually(11)；only(8)；supply(4)；tively(2)；relatively(2)；severely(2)；ciently(1)；extremely(1)；especially(1)；widely(1)；actively(1)；usually(1)
- 高频二词短语：mtps unit(46)；mtps plate(32)；load bearing(30)；mpa mpa(28)；bearing frame(27)；alumina ceramic(24)；mpa respectively(23)；high temperature(20)；composite structures(18)；boundary conditions(18)；page gao(16)；gao composite(16)
- 高频三词短语：load bearing frame(25)；mpa mpa respectively(17)；page gao composite(16)；gao composite structures(16)；composite structures fig(13)；electricity conducting plates(11)；alumina ceramic layer(10)；alumina ceramic layers(10)；second stage compression(10)；stage compression surface(9)；maximum stresses them(7)；modulus high temperature(6)
- 被动语态估计：107；`we + 动作动词` 主动句估计：0
- 一般现在时线索：257；一般过去时线索：249；现在完成时线索：1；情态动词线索：41

章节词频：

- Abstract: mtps(5)；load(4)；bearing(4)；thermal(3)；concept(3)；developed(3)；unit(3)；heat(3)
- Introduction: tps(17)；thermal(16)；heat(16)；mtps(12)；temperature(11)；hypersonic(10)；protection(10)；aerodynamic(9)
- Conclusion: mtps(14)；unit(8)；power(5)；average(5)；tps(4)；load(4)；bearing(4)；thermal(4)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
- 原句/结构：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. designed a novel ITPS, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply. designed a novel METHOD, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
- 原句/结构：The structural design points of the MTPS unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. 2.
  可迁移模板：The structural design points of the METHOD unit are obtained based on the analysis of the whole vehicle, and the proper displacement boundary conditions are essential to obtaining reasonable results. X.
#### Gap句
- 原句/结构：With the development of hypersonic engineering, thermal protection system (TPS) [5–8] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus TPS is low‐efficiency.
  可迁移模板：With the development of hypersonic engineering, thermal protection system (METHOD) [X–X] encounters great challenges, especially from the point of view of energy utilization, the large amount of aerodynamic heat is wasted by the heat resistant and dissipation technologies and thus METHOD is low‐efficiency.
- 原句/结构：The authors also proposed a TE module based on the MTPS concept and evaluated its mechanical‐thermoelectric performance in [38], however, the three limitations of the structure and analysis should be mentioned here: 1st, the structure has only one TE stage of high‐temperature TE materials, which leads to low TE conversion efficiency; 2nd, the three‐layer structure is only schematically described and no more details are involved; 3rd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.
  可迁移模板：The authors also proposed a METHOD module based on the METHOD concept and evaluated its mechanical‐thermoelectric performance in [X], however, the three limitations of the structure and analysis should be mentioned here: Xst, the structure has only one METHOD stage of high‐temperature METHOD materials, which leads to low METHOD conversion efficiency; Xnd, the three‐layer structure is only schematically described and no more details are involved; Xrd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.
#### 方法句
- 原句/结构：In this paper, a multifunctional thermal protection system (MTPS) concept with additional functions of thermoelectric (TE) conversion and load bearing is developed for a hypersonic launch vehicle.
  可迁移模板：In this paper, a multifunctional thermal protection system (METHOD) concept with additional functions of thermoelectric (METHOD) conversion and load bearing is developed for a hypersonic launch vehicle.
- 原句/结构：The mechanical‐thermal‐electrical performance of the MTPS is evaluated based on the multi‐scale analysis of the flight vehicle, MTPS plate and MTPS unit, and the transfer method of mechanical boundary conditions between different scales is developed.
  可迁移模板：The mechanical‐thermal‐electrical performance of the METHOD is evaluated based on the multi‐scale analysis of the flight vehicle, METHOD plate and METHOD unit, and the transfer method of mechanical boundary conditions between different scales is developed.
- 原句/结构：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
#### 结果句
- 原句/结构：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply.
- 原句/结构：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed MTPS concept has multi effective functions of load bearing, heat protection and power supply. designed a novel ITPS, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
  可迁移模板：The results show that the multi‐scale analysis is essential to ensure the accuracy of boundary conditions, and the developed METHOD concept has multi effective functions of load bearing, heat protection and power supply. designed a novel METHOD, which was consisted of C/SiC composite corrugated core sandwich plane and insulated aerogel.
- 原句/结构：The results show some conclusions: 1.
  可迁移模板：The results show some conclusions: X.
#### 贡献句
- 原句/结构：TE conversion technology [24] is a promising technology in energy reusing, by integrating TE module into TPS, a MTPS [25] can be established.
  可迁移模板：METHOD conversion technology [X] is a promising technology in energy reusing, by integrating METHOD module into METHOD, a METHOD [X] can be established.
- 原句/结构：Xiao et al. [29] established a TE module based on low‐temperature and mid‐temperature TE materials.
  可迁移模板：Xiao et al. [X] established a METHOD module based on low‐temperature and mid‐temperature METHOD materials.
- 原句/结构：Chen et al. [30] established a two‐ stage semiconductor TE generator model with external heat exchange and analyzed the performance of the generator.
  可迁移模板：Chen et al. [X] established a two‐ stage semiconductor METHOD generator model with external heat exchange and analyzed the performance of the generator.
#### 限制/边界句
- 原句/结构：Although the above TPS have their own advantages, some limitations have to be stated: for ITPS, it has thermal short‐circuit effect; for ATPS, it needs additional complicated system to supply consuming coolant and has high‐cost; for UHTC, it has low toughness; for ablative TPS, it can only be used once and has the problem of aerodynamic shape change after ablation.
  可迁移模板：Although the above METHOD have their own advantages, some limitations have to be stated: for METHOD, it has thermal short‐circuit effect; for METHOD, it needs additional complicated system to supply consuming coolant and has high‐cost; for METHOD, it has low toughness; for ablative METHOD, it can only be used once and has the problem of aerodynamic shape change after ablation.
- 原句/结构：The authors also proposed a TE module based on the MTPS concept and evaluated its mechanical‐thermoelectric performance in [38], however, the three limitations of the structure and analysis should be mentioned here: 1st, the structure has only one TE stage of high‐temperature TE materials, which leads to low TE conversion efficiency; 2nd, the three‐layer structure is only schematically described and no more details are involved; 3rd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.
  可迁移模板：The authors also proposed a METHOD module based on the METHOD concept and evaluated its mechanical‐thermoelectric performance in [X], however, the three limitations of the structure and analysis should be mentioned here: Xst, the structure has only one METHOD stage of high‐temperature METHOD materials, which leads to low METHOD conversion efficiency; Xnd, the three‐layer structure is only schematically described and no more details are involved; Xrd, in the thermo‐ mechanical analysis, only the thermal stress is simulated, and the influence of aerodynamic force loads is not considered.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
