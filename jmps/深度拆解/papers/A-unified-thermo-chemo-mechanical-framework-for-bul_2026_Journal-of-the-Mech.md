# A unified thermo-chemo-mechanical framework for bulk and frontal polymerization: Coupled kinetics and front stability

## 0. 读取说明
- 源 PDF：`jmps/文献/A-unified-thermo-chemo-mechanical-framework-for-bul_2026_Journal-of-the-Mech.pdf`
- 源 TXT：`jmps/文本/txt/A-unified-thermo-chemo-mechanical-framework-for-bul_2026_Journal-of-the-Mech.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 214 (2026) 106681, DOI: 10.1016/j.jmps.2026.106681。
- 是否需要结合 PDF 图像核查：需要。本文核心图含 deformation gradient decomposition、bulk/frontal regimes、velocity/stability phase diagram、force-response experimental comparison，当前仅根据 txt 与图注分析，需 PDF 核查曲线、相图分区、实验几何和力学对比。
- 本文类型：聚合/前沿聚合的三维热-化-力统一理论论文，含一维窄反应区解析、稳定性判据和实验趋势对照。

## 1. 基本信息与论文身份
- 题名：A unified thermo-chemo-mechanical framework for bulk and frontal polymerization: Coupled kinetics and front stability。
- 作者/机构：Xuanhe Li; Tal Cohen。机构为 MIT Mechanical Engineering / Civil and Environmental Engineering。
- 关键词：Polymerization; Frontal polymerization; Thermo-chemo-mechanics; Transformation deformation。
- 研究对象：bulk polymerization 与 frontal polymerization 中的温度、转化率、应力、残余变形、前沿传播和稳定性。
- 研究尺度：有限变形连续体、局部反应动力学、前沿 traveling wave、一维拉伸实验、三维理论框架。
- 方法类型：second-law thermodynamic framework + stress-dependent reaction kinetics + multiplicative decomposition + transformation deformation flow rule + narrow reaction zone approximation + traveling wave solution + perturbation stability analysis + force response comparison。
- 证据类型：理论推导、governing equations summary、bulk/frontal regime 数值模拟、传播速度闭式预测、generalized Zeldovich stability criterion、phase diagram、uniaxial displacement-control experiment 质性对照。
- 目标读者：聚合制造、frontal polymerization、热-化-力耦合、残余应力、有限变形本构、稳定性分析和 additive manufacturing 读者。
- JMPS 风格定位：强理论机制论文。它把聚合从工艺问题写成“反应动力学受应力调制，固化过程又演化无应力构型”的双向耦合热力学系统。

## 2. 摘要与核心信息提取
摘要从 polymerization 的工业基础性出发，指出 monomer mixture 转为 cross-linked polymer chains 时温度、密度、刚度改变，会诱导 residual stress 和 warping。随后区分 bulk polymerization 和 frontal polymerization：前者依赖持续能量输入，后者由自持放热反应前沿传播，更高效但伴随 abrupt spatial variations，放大 thermo-chemo-mechanical coupling。本文的核心动作是建立 generalized thermodynamically consistent framework，同时包含 local stress 对 reaction kinetics 的影响，以及 curing 中 stress-free configuration 的演化。后者借鉴 plasticity，建立 irreversible deformations 的 kinetic relation/flow rule。然后特化到 FP：用窄反应区近似得传播速度闭式预测，比较 residual stress，做 perturbation stability analysis，得到 generalized Zeldovich number 和 phase diagram。

一句话主张：聚合过程中的前沿传播、熄灭、失稳和残余应力可由一个热力学一致的大变形 thermo-chemo-mechanical 框架统一解释，其中应力改变反应驱动力，固化又通过 transformation deformation 演化改变应力自由构型。

核心关键词：stress-dependent kinetics；transformation deformation；frontal polymerization；narrow reaction zone；front stability；generalized Zeldovich criterion；residual stress。

## 3. 选题层深拆
问题来源是聚合制造中长期存在的残余应力、翘曲、脱粘、裂纹和前沿稳定性问题。传统热固化或光聚合依赖持续外部能量，frontal polymerization 更快更节能，但 localized reaction front 使温度、转化率、刚度和体积变化高度集中，耦合效应更强。

问题重要性：工业上，风机叶片、航空构件、涂层、3D 打印和复合材料都需要低缺陷、低残余应力的聚合件；理论上，front propagation 的速度、quenching 和 pulsating instability 不能只看热-化学，还要纳入力学载荷。

为什么现在值得做：作者/领域已有实验观察到 tensile stress 可 slow down or quench FP front；已有工作处理 stress-free configuration evolution，但缺少同时包含 stress-dependent kinetics 和 transformation deformation evolution 的统一热力学框架。

问题边界：总体框架是三维大变形，但详细解析和实验对照聚焦一维前沿传播与单轴 displacement-control force response；复杂几何、多轴应力、真实工业过程和三维数值实现是未来工作。

选题可迁移性：强。它是典型“工艺现象 -> 热力学驱动力 -> 稳定性判据 -> 制造控制”的 JMPS 论文路径。

## 4. 领域位置与文献版图
作者将文献分为几条线：thermo-chemical coupling、体积变化与 residual stress、frontal polymerization/Zeldovich stability、mechanical stress 对 reaction kinetics 的影响、以及 stress-free configuration evolution。本文站位是把后两条线同时纳入同一 thermodynamic framework：一方面 stress 进入 chemical driving force，另一方面 curing 通过 transformation deformation 更新 stress-free configuration。最接近前人包括 Zeldovich/combustion stability、Pojman/Lloyd FP instability、Kumar/Wijaya 等 stress-free configuration models，以及 Li and Cohen 2024 tensile stress-quenching experiments。作者承认前人贡献和自己前作证据，新意写在“unified, thermodynamically consistent framework capable of capturing two-way coupling”。

## 5. Gap 制造机制
明示 gap：现有 polymerization frameworks 尚未同时包含 local stress 对 reaction kinetics 的影响，以及 stress-free configuration 在 curing 中的演化；FP 中 abrupt front 放大耦合，尤其需要统一处理。

隐含 gap：经典 Zeldovich criterion 适用于 adiabatic, stress-free limit，不能解释机械加载和 heat loss 共同作用下的 stable/unstable/quenching regimes。

gap 类型：机制 gap + 理论一致性 gap + 稳定性 gap + 制造控制 gap。机制上是 two-way coupling；理论上需 second-law consistency；稳定性上需 generalized criterion；制造上需 residual stress management。

gap 证据来自引言中两个 coupling mechanisms 的分段铺垫：stress modifies kinetics；stress-free configuration evolves after gelation。作者将两者并列后自然推出 unified framework。

审稿追问：stress-dependent kinetics 的 thermodynamic driving force 是否可实验标定；flow rule for transformation deformation 是否唯一；窄反应区近似对实际 FP 是否足够；一维 phase diagram 对三维制造的预测性如何。

## 6. 创新性判断
作者声称的贡献是 fully coupled, large-deformation thermo-chemo-mechanical framework for polymerization，并特化到 FP 的 propagation dynamics 和 force response。真实创新包括：1. 从 second law/free energy imbalance 定义 reaction driving force；2. 用该 driving force 建立 thermodynamically consistent chemical kinetic relation，使 stress 可调控 reaction；3. 用 multiplicative decomposition `F=Fe Fi` 且 `Fi=F* Fv` 描述体积变化与 transformation deformation；4. 将 transformation deformation evolution 写成类似 plasticity flow rule；5. 窄反应区下推导 propagation velocity 和 critical load quenching；6. 稳定性判据推广 classical Zeldovich number；7. 用 shock-like transition 模型解释 front propagation 中 axial force/residual stress 演化。

创新类型：理论框架 + 解析机制 + 稳定性判据 + 实验趋势解释。强度高。尤其“generalized Zeldovich condition incorporating mechanical effects”是很清晰的 JMPS 级贡献表达。

创新必要性：强。没有 stress-dependent kinetics，无法解释拉伸导致 FP front slowdown/quenching；没有 transformation deformation，无法解释固化中应力自由构型演化和残余应力。

容易被挑战处：flow rule 类比 plasticity 是否物理唯一；kinetic relation 形式是否过于特定；实验比较是 qualitative agreement 而非全面定量；一维推导是否能代表三维复杂工艺。

## 7. 论证链条复原
背景：polymerization 是现代制造基础，但 curing 中温度、转化率、刚度和体积变化耦合会产生 residual stress、warping 和 failure。 -> 文献：thermo-chemical coupling、frontal polymerization、Zeldovich stability、stress-free configuration evolution 和 stress-modulated reaction 各自已有研究。 -> gap：缺少统一热力学框架同时处理应力调反应和固化无应力构型演化。 -> 问题：如何预测 bulk-to-frontal transition、front velocity、quenching/stability 和 force response。 -> 方法：构建 second-law framework、multiplicative decomposition、reaction driving force、flow rule、governing equations；特化为一维 FP，采用 narrow reaction zone，推导 traveling wave velocity 与 stability；比较单轴 force response。 -> 证据：Fig. 1 kinematics；Fig. 2 bulk/frontal regimes；Fig. 3 heat loss/mechanical loading 对 velocity 和 stability phase diagram 的影响；Fig. 4 experimental setup 与 force comparison。 -> 发现：mechanical loading 可导致 velocity 突然降为零，解释 binary response；stability criterion generalizes Zeldovich number；front 可像 shock-like transition 一样积累 stress。 -> 意义：指导 FP 制造中 front control 和 residual stress mitigation。

最强环节是 theory-to-criterion：从热力学推导到速度和稳定性判据。薄弱处是实验验证范围较窄。

## 8. 方法/理论/模型细拆
总体理论采用 multiplicative decomposition：`Fe` 表示 elastic deformation，`Fi` 表示 inelastic deformation；`Fi` 再分为 volume change tensor `Fv` 和 transformation deformation `F*`，从而分离 chemical shrinkage/thermal expansion 与 stress-free configuration evolution。质量守恒、机械平衡、energy balance 和 entropy imbalance 共同限制本构；free energy imbalance 定义 polymerization reaction 的 thermodynamic driving force，使局部应力可进入 kinetics。transformation deformation 借鉴 plasticity flow rule，描述固化中新链沉积导致的不可逆无应力构型演化。FP 特化中，一维窄反应区把 front 视为局部 transition，推得 traveling wave velocity、heat loss/loading 影响和 stability phase diagram；displacement-control force response 则被解释为 material properties 与 transformation deformation 的 shock-like transition。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| polymerization 需要同时考虑 thermo-chemical 和 mechanical coupling | Introduction | residual stress、warpage、delamination、FP front gradients 文献 | 文献 + 物理论证 | 强 | 工艺依赖性强 |
| stress 可通过 thermodynamic driving force 调控 reaction kinetics | Theory | second-law/free energy imbalance 导出 driving force 和 kinetic relation | 理论推导 | 强 | 需实验标定 kinetic parameters |
| transformation deformation flow rule 可描述 stress-free configuration evolution | Theory/Fig. 1 | multiplicative decomposition 与 plasticity analogy | 本构构造 | 中强 | flow rule 形式非唯一 |
| heat loss 和 mechanical loading 控制 front velocity，超过阈值可 quench | Section 3/Fig. 3 | closed-form velocity、critical threshold、前作实验 binary response | 解析 + 对照 | 强 | 一维/窄反应区适用范围 |
| stability criterion generalizes Zeldovich number | Section 3.5/Fig. 3 | perturbation analysis，adiabatic stress-free limit 退化为 classical Zeldovich | 理论判据 | 强 | 推导细节需核查 |
| phase diagram 可区分 stable/unstable/impossible FP | Fig. 3 | heat loss 和 loading 参数空间分区 | 理论结果 | 中强 | 需实验相图验证 |
| force evolution 可由 shock-like front transition 解释 | Section 4/Fig. 4 | displacement-control setup 与实验 force trend qualitative agreement | 解析 + 实验对照 | 中 | 定量精度有限 |

证据系统主要是理论与解析验证，实验只支撑关键机制趋势。写作上高明之处是把自己前作实验作为 gap 证据，又不把本文写成实验论文。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | `F=Fe Fi`, `Fi=F* Fv` decomposition | 无应力构型和体积变化分离 | 建立理论图像 | 是 |
| Fig. 2 | bulk vs frontal regimes 数值模拟 | 框架覆盖两种聚合模式 | 展示统一性 | 是 |
| Fig. 3 | heat loss/loading 对 velocity 和 stability 的影响，相图 | generalized front dynamics | 核心理论结果 | 是 |
| Fig. 4 | experimental setup 和 force comparison | 力学响应/残余应力机制 | 与实验连接 | 是 |
| Balance laws/equations summary | governing equations | 框架完整性 | 复现基础 | 否 |
| Reaction driving force equation | stress-dependent kinetics | stress 调反应 | 热力学核心 | 否 |
| Transformation flow rule | stress-free configuration evolution | 固化不可逆变形 | 本构核心 | 否 |
| Stability criterion | generalized Zeldovich | stable/unstable/quench 分区 | 理论卖点 | 否 |

图表少但功能强。每张图对应一个层级：Fig. 1 是 kinematics，Fig. 2 是 regime，Fig. 3 是 criterion/phase diagram，Fig. 4 是 experiment。理论论文不需要很多图，但每张图都要担任论证节点。

## 11. 章节结构与篇章布局
- Abstract：工业问题、耦合机制、统一框架、FP 速度和稳定性、phase diagram、制造意义。
- Introduction：polymerization 应用 -> thermo-chemo-mechanical coupling -> FP 效率与前沿问题 -> stress-dependent kinetics -> stress-free configuration evolution -> 本文贡献。
- Theory：从 kinematics 到 balance laws、energy、entropy、constitutive relations、response functions、transformation deformation、governing equations，结构非常系统。
- Coupling mechanism I: Propagation dynamics：bulk/frontal regimes、narrow reaction zone、traveling wave、velocity、stability。
- Coupling mechanism II: Force response：实验设置、解析 formulation、与实验对比。
- Conclusion：先复述需求，再总结框架和两个机制，最后指出未来三维复杂应力状态和数值实现。
- Appendices：处理 incompressibility stress、thermodynamic consistency、general r、heat equation 和 Zeldovich relation。

最值得模仿的是两个 results 章节标题：`Coupling mechanism I` 和 `Coupling mechanism II`。它们不是普通 Results，而是把结果直接组织为“两个耦合机制”。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-unified-thermo-chemo-mechanical-framework-for-bul_2026_Journal-of-the-Mech.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：20
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Kinematics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Balance laws | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Energy balance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Entropy imbalance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Constitutive relations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.6 Constitutive response functions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.7 Evolution of transformation deformation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.8 Summary of governing equations | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Coupling mechanism I: Propagation dynamics | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Characteristic regimes of polymerization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Narrow reaction zone assumption | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Traveling wave solution | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 节奏非常清楚：先写 polymerization 的广泛性和制造要求，再写 curing 的耦合源，接着写 FP 的优势和局部前沿问题，再分两段介绍本文要处理的两个 coupling mechanisms。最后一段贡献预告与章节安排。

Theory 段落遵循“定义 -> 守恒 -> 不等式 -> 本构限制 -> 响应函数 -> 控制方程汇总”。这是热力学框架论文的标准节奏，能让读者相信模型不是随便拼接。

Propagation dynamics 段落由简单到复杂：先区分 regimes，再提出窄反应区假设，求 traveling wave，再讨论 velocity，最后做 stability。这个顺序符合读者认识过程。

Force response 段落先给实验设置与 key observations，再给 analytical formulation，最后比较实验。这样能避免解析模型脱离现象。

可复用模板：`We first formulate the general three-dimensional theory. We then specialize it to a reduced setting in which the essential coupling mechanism can be isolated analytically. This specialization yields [closed-form result/criterion], which is then compared with [observation].`

## 13. 文笔画像与语言习惯
文笔理论感强但应用动机明确。高频表达包括 thermodynamically consistent, generalized framework, seamlessly captures, driving force, transformation deformation, narrow reaction zone, propagation velocity, stability criterion, phase diagram, residual stress。

claim 强度较高但有边界：作者明确说 examples focus on 1D configurations to isolate essential features，future work should handle multi-axial stress states and 3D simulations。这种先强贡献、后清边界的写法很稳。

动词习惯：develop, formulate, incorporate, define, introduce, derive, obtain, reveal, generalize, reduce, construct。理论结果常用 “shown to be a generalization of...” 这种句式，强调与经典判据关系。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：polymerization(117)；front(87)；stress(81)；deformation(70)；temperature(70)；reaction(68)；evolution(66)；propagation(63)；heat(57)；energy(55)；velocity(54)；transformation(51)；mechanical(49)；relation(48)；chemical(45)；process(43)；material(40)；condition(40)；gradient(40)；elastic(38)
- 高频学术名词：deformation(140)；polymerization(117)；stress(81)；condition(80)；temperature(70)；reaction(68)；evolution(66)；propagation(63)；energy(55)；velocity(54)；transformation(51)；solution(50)；relation(48)；material(40)；equation(36)；analysis(36)
- 高频学术动词：derived(12)；shown(11)；show(10)；proposed(9)；develop(6)；investigate(5)；capture(5)；indicates(5)；shows(4)；developed(4)；solve(3)；evaluated(2)；compared(2)；evaluate(2)；demonstrated(2)；predicted(2)
- 高频形容词：elastic(76)；mechanical(49)；chemical(45)；theoretical(40)；material(40)；gradient(40)；frontal(35)；experimental(34)；analytical(32)；thermal(25)；local(24)；stable(22)；constitutive(21)；critical(20)；numerical(20)；constant(18)
- 高频副词/连接副词：fully(14)；consequently(10)；cally(10)；thermodynamically(10)；directly(9)；however(7)；commonly(7)；explicitly(7)；accordingly(6)；therefore(5)；newly(5)；approximately(4)；experimentally(4)；locally(4)；theoretically(4)；recently(4)
- 高频二词短语：transformation deformation(36)；frontal polymerization(35)；deformation gradient(23)；con guration(21)；polymerization process(21)；mechanical loading(18)；free energy(18)；propagation velocity(17)；temperature eld(16)；heat loss(15)；volume change(14)；degree curing(13)；constitutive relation(13)；elastic stretch(13)；elastic deformation(12)；velocity gradient(12)
- 高频三词短语：stress-free con guration(11)；evolution transformation deformation(8)；temperature degree curing(7)；evolution stress-free con(7)；per unit mass(7)；narrow reaction zone(6)；heat loss mechanical(6)；loss mechanical loading(6)；thermal expansion chemical(6)；expansion chemical shrinkage(6)；transformation deformation gradient(6)；volume change ratio(6)

**主动、被动与句法**

- 被动语态估计次数：163
- `we + 动作动词` 主动句估计次数：20
- 名词化表达估计次数：1663
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：266
- 一般过去时线索：62
- 现在完成时线索：20
- 情态动词线索：101
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：polymerization(12)；frontal(6)；front(5)；reaction(5)；bulk(4)；material(4)；propagation(4)；framework(3)
- 1. Introduction：polymerization(26)；process(12)；reaction(10)；deformation(10)；stress(9)；polymer(8)；gradient(8)；transformation(6)
- 2. Theory：无明显高频项
- 2.1. Kinematics：gradient(16)；deformation(10)；con(8)；guration(8)；velocity(8)；polymer(6)；network(6)；elastic(6)
- 2.2. Balance laws：mass(3)；conservation(2)；density(2)；body(2)；work(2)；thermal(2)；expansion(2)；gurtin(2)
- 2.3. Energy balance：energy(9)；internal(4)；heat(4)；balance(4)；unit(3)；polymerization(2)；per(2)；mass(2)
- 2.4. Entropy imbalance：stress(7)；power(6)；energy(4)；term(4)；heat(4)；second(3)；law(3)；free(3)
- 2.5. Constitutive relations：energy(12)；term(9)；free(7)；deformation(6)；constitutive(5)；transformation(5)；based(4)；network(4)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 句型骨架：`[Process] inherently involves the interplay of [physics A], [physics B], and [physics C].`
- 句型骨架：`A unified, thermodynamically consistent framework capable of capturing [coupling mechanisms] is critically needed.`

### 14.2 方法与框架表达
- 句型骨架：`The constitutive model is derived from the second law of thermodynamics by constructing a free energy imbalance, from which [driving force] is defined.`
- 句型骨架：`We introduce a multiplicative decomposition of [field] and define [internal variable] whose evolution follows a rate-form flow rule inspired by [theory].`

### 14.3 结果与趋势表达
- 句型骨架：`Closed-form expressions were obtained for [quantity], revealing how [factor A] and [factor B] influence [dynamics].`
- 句型骨架：`The theory predicts a sudden drop to zero in [velocity] once [loading] exceeds [critical threshold].`

### 14.4 机制解释表达
- 句型骨架：`By modeling the reaction front as a shock-like transition in material properties, we derive [response] as the front propagates.`

### 14.5 贡献与意义表达
- 句型骨架：`This criterion generalizes the classical [criterion] by incorporating [new effect], and reduces to [classical limit] under [limit].`

### 14.6 局限与未来工作表达
- 句型骨架：`While the examples focus on [reduced configurations] to isolate [features], future work should investigate [complex states] and develop [robust numerical implementations].`

## 15. 引用策略与文献使用
引用策略按工艺和机制分组。应用文献支撑 polymerization 在 biomedical devices、protective coatings、wind blades、aircraft wings 和 3D printing 中的重要性。thermo-chemical coupling 文献支撑 reaction-temperature feedback。residual stress 文献支撑 warpage/delamination/failure。FP 文献支撑 energy efficiency、self-sustaining fronts、pulsating instabilities 和 Zeldovich number。相变/增长/断裂文献支撑 stress-modulated transformations。最后引用 stress-free configuration evolution 模型，为 transformation deformation flow rule 铺路。

引用姿态非常有层次：不是罗列，而是每组文献都对应一个机制模块。gap 由两个“尚未统一”的机制组合产生。

引用风险：FP 稳定性和 Zeldovich 文献很经典，推导必须准确；polymer curing residual stress 模型很多，本文需说明与 viscoelastic cure models 的关系；stress-dependent reaction evidence 目前较少，可能需要更多实验支撑。

## 16. 审稿人视角风险
最大攻击面：一维窄反应区近似。它有助于解析，但实际 FP 可能有二维/三维热损失、边界、氧阻聚、材料非均匀、凝胶点和多轴应力。

第二风险：stress-dependent kinetics 的具体形式和参数标定。热力学一致只说明方向合法，不保证反应速率形式唯一或参数易测。

第三风险：transformation deformation flow rule 的物理基础。类比 plasticity 很有力，但 polymer chain deposition 的微观机制可能更复杂，尤其在粘弹性、凝胶化、交联密度演化中。

claim 是否过强：framework “seamlessly captures both bulk and frontal polymerization” 在理论上成立，但实际验证主要在一维 FP，bulk polymerization 和复杂几何仍需更多 examples。

替代解释：front quenching 可能受 heat loss、氧阻聚、材料边界、样品厚度影响，不只是 tensile stress；本文 phase diagram 有助于区分，但实验仍需更多维度。

## 17. 可复用资产
- 可复用选题角度：将制造工艺中的缺陷问题上升为热-化-力双向耦合机制。
- 可复用 gap 制造：已有研究分别处理 A 和 B，但缺少 thermodynamically consistent unified framework。
- 可复用论证链：工业动机 -> 两个 coupling mechanisms -> second-law framework -> reduced analytical problem -> velocity/stability criterion -> experiment comparison -> future 3D implementation。
- 可复用图表设计：kinematics schematic + regime map + phase diagram + experimental comparison，是理论机制论文的强组合。
- 可复用句型：`The latter is developed in analogy to [classical theory] to establish [kinetic relation], akin to [known rule].`
- 不宜直接模仿处：不要在只有一维解析和质性对比时过度承诺复杂工业工艺预测。

## 18. 对我写论文的启发
写热力学框架论文时，可以学它把复杂工艺拆成两个清楚的 coupling mechanisms。这样的拆法让 Introduction、Theory 和 Results 都有统一骨架：先一般框架，再分别分析 propagation dynamics 和 force response。

Introduction 可迁移：先写工艺需求，再写耦合物理，再指出现有模型缺少哪个方向的反馈。Method 可迁移：用 second law 给本构和动力学合法性，而不是直接假设经验式。Results 可迁移：用 reduced analytical setting 提炼判据，再承认未来要做 3D 数值。

需要避免的问题：不要把热力学一致性等同于实验正确性；不要把 generalized criterion 写成所有条件通用；不要忽略参数标定与复杂边界。

## 19. 最终浓缩
这篇论文最值得学的是：如何把 polymerization 的 stress-dependent kinetics 与 stress-free configuration evolution 统一到 second-law consistent finite-deformation framework，并从中推出 front velocity、quenching 和 generalized Zeldovich stability criterion。

最大风险是：核心解析结果基于一维和窄反应区近似，真实三维制造、多轴应力和复杂热边界仍需数值与实验验证。

三个可迁移动作：1. 将复杂工艺拆成两个耦合机制分别论证；2. 用经典理论类比塑造新内部变量的合法性；3. 用“退化到经典极限”提升新稳定性判据可信度。
