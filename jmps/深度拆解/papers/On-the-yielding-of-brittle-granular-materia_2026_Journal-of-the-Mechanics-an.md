# On the yielding of brittle granular materials at elevated temperatures

## 0. 读取说明
- 源 PDF：`jmps/文献/On-the-yielding-of-brittle-granular-materia_2026_Journal-of-the-Mechanics-an.pdf`
- 源 TXT：`jmps/文本/txt/On-the-yielding-of-brittle-granular-materia_2026_Journal-of-the-Mechanics-an.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 可读出理论链、图题、结论和参数表线索，但 GSD 曲线、yield surface、实验-模型曲线吻合程度需结合 PDF 图像核查。
- 本文类型：矿物尺度热弱化机制 + 表面积破碎力学理论 + 颗粒材料屈服模型 + 实验数据验证。

## 1. 基本信息与论文身份
- 题名：On the yielding of brittle granular materials at elevated temperatures。
- 作者与机构：Yazeed Kokash、Richard Regueiro、Yida Zhang；University of Colorado Boulder。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106660。
- DOI：10.1016/j.jmps.2026.106660。
- 关键词：Granular materials；Yielding；Thermal weakening；Surface energy；Grain breakage。
- 研究对象：升温条件下 brittle granular materials，尤其 quartz-dominated sandstones 和 St. Peter sand 的屈服/破碎。
- 研究尺度：原子/矿物表面能 -> crack growth/fracture toughness -> grain crushing/specific surface area -> continuum yield surface。
- 方法类型：intermolecular potential/Morse potential 表面能模型 + surface-based breakage mechanics (SBM) + fractal GSD evolution + 实验数据验证。
- 证据类型：矿物 fracture toughness 数据、弹性参数温度变化、GSD 数据、sandstone/sand stress-strain 与 yield surface 对比、AE 数据对照。
- 目标读者：颗粒材料、岩土热-力耦合、破碎力学、热弱化建模和地质工程力学研究者。
- JMPS 风格定位：典型 bottom-up mechanistic modeling，从 mineral surface energy 出发推导 continuum yielding，而不是经验地让 yield/hardening parameters 随温度变化。

## 2. 摘要与核心信息提取
摘要开头把 temperature/humidity 对 geomaterials stiffness、strength、creep、time-to-failure 的影响放到 nuclear waste repositories、geothermal extraction、climate-resilient geostructures 等工程需求中。gap 不是“热效应无人研究”，而是现有 elastoplastic theories 多用经验温度依赖参数，缺少 micromechanical foundation 和 thermodynamic consistency。

方法句非常强：mechanistically link temperature-dependent macroscopic yielding to temperature dependence of surface energy of constituent solids。作者先用 intermolecular potential 建模 quartz 等矿物的 surface energy γ 随温度变化，再通过 surface-based breakage mechanics 上尺度到 brittle granular assemblies。关键选择是把 specific surface area As 作为唯一 internal state variable；As 与 γ 构成 thermodynamically conjugated pair，使 γ 显式进入 yield function。

一句话主张：在 20-150°C 范围内，quartz-dominated brittle granular materials 的热弱化可主要归因于矿物表面能/断裂韧性随温度降低，而不是 bulk elasticity 或 hardening parameters 的显著变化；specific surface area 作为内变量使这一矿物尺度机制自然进入连续体屈服模型。

核心关键词：surface energy γ；specific surface area As；surface-based breakage mechanics；fractal GSD；thermal weakening。

## 3. 选题层深拆
问题来源是工程热环境中的颗粒材料强度下降。地下核废料、深部地热、季节温度循环和岩石风化都需要理解 geomaterials 在温度变化下的屈服和破坏。已有实验显示 quartz、sandstone、sand 在升温后 fracture toughness、crack velocity、yield strength、creep rate 等发生明显变化。

问题重要性在于热-力模型通常需要预测 yield envelope，而不是只拟合一个温度点。经验参数法可以拟合数据，但缺乏机制：为什么温度会缩小 yield surface？是弹性模量变了、hardening 变了，还是颗粒破碎所需新表面能变了？本文选择第三条作为主假设。

为什么现在值得做：矿物 surface energy/fracture toughness 数据、grain size distribution 数据、X-ray tomography 支持的破碎统计、continuum breakage mechanics 已经为 bottom-up 模型提供基础。作者通过 SBM 重新定义内变量，使热依赖表面能能自然上尺度。

问题边界：结论主要针对 quartz-dominated granular materials 和 20-150°C 温度范围；高温相变、碳酸盐/更延性颗粒、湿度/化学溶解、塑性/黏塑性机制未完全纳入。边界明确让强 claim 更可信。

## 4. 领域位置与文献版图
文献版图分成四类。第一类是环境条件对 rock/sand 机械行为的实验研究，包括 triaxial compression、creep、fracture toughness、crack velocity。第二类是 empirical thermo-elastoplastic models，通过温度依赖 yield/hardening parameters 拟合热弱化。第三类是 continuum breakage mechanics，尤其 Einav 的 CBM，用 breakage internal variable 处理颗粒破碎。第四类是 mineral-scale surface energy/fracture toughness 与 GSD/fractal evolution 数据。

已有实验解决了“升温会弱化”的事实问题；经验模型解决了“怎么拟合”的工程问题；CBM 解决了“如何把颗粒破碎写入连续体”的理论问题；但尚缺一条热依赖 surface energy 到 macroscopic yield surface 的热力学一致链条。

本文站在 CBM 之后，但替换/改造内变量：用 specific surface area As 代替常规 breakage variable。这个选择的意义在于 As 与 γ 天然共轭，因此温度依赖的 γ 不再是外插参数，而是进入 free energy/dissipation/yield 的物理量。

对前人态度：作者承认经验模型能拟合，但指出 micromechanical foundation 和 second-law consistency 可能不足；承认 conventional breakage mechanics 有价值，但认为 surface-based formulation 更适合热弱化问题。

## 5. Gap 制造机制
显性 gap：现有热-力 elastoplastic theories 多以经验温度函数调整 yield/hardening parameters，缺少矿物尺度机制和热力学一致性。隐含 gap：传统 breakage variable 与 surface energy 的共轭关系不够直接，因此难以让 γ(T) 自然进入 yield function。

Gap 类型属于机制 gap + 热力学一致性 gap + 上尺度 gap。机制 gap 是宏观屈服为何随温度下降；热力学 gap 是能量耗散与第二定律；上尺度 gap 是 mineral surface energy 到 granular assembly yield。

Gap 证据来自实验对比：Darot 等 surface energy/fracture toughness 随温度变化；Karner、Jefferd、Heap 等砂岩/砂在升温下 yield、porosity reduction、AE、creep 变化；同时 E 与 ν 在测试温度范围变化很小，暗示 bulk elasticity 不是主要机制。

审稿人可能追问：温度影响 crack velocity、humidity、pressure solution、thermal expansion 等多个机制，为什么 surface energy 是主导？作者把结论限定在 quartz-dominated 和 20-150°C，并在结论承认更高温/更延性颗粒需引入 dislocation activity、plastic/viscoplastic flow、dissolution 等机制。

## 6. 创新性判断
作者声称贡献：提出 bottom-up approach；建立 surface energy γ 与 temperature 的 analytical model；把 γ(T) 集成到 thermodynamically consistent surface-based breakage mechanics；用 As 作为唯一内变量；用 evolving fractal dimension 表示 GSD；验证 sandstones 和 St. Peter sand 的温度依赖屈服。

真实创新集中在内变量选择和能量共轭。specific surface area As 作为唯一 internal state variable，使破碎程度、GSD 演化、表面能耗散和 yield surface 之间形成闭环。相较经验热弱化参数，这个框架能解释“为什么升温降低屈服强度”。

创新类型：理论机制强；热力学建模强；数据验证中等偏强；工程泛化中等。创新必要性很高，因为岩土热-力模型常被经验化，JMPS 读者会期待更深的 micromechanics。

容易被挑战处：Morse potential/surface energy 模型对真实矿物表面、湿度和缺陷的代表性；GSD fractal expression 的普适性；As 唯一内变量是否足以描述颗粒重排、形状、摩擦和接触演化；150°C 以上机制切换。

## 7. 论证链条复原
背景 -> 温度显著影响 geomaterials 强度、破碎、creep 和工程安全。
文献 -> 实验显示升温降低 fracture toughness/yield strength，经验模型能拟合但缺机制。
gap -> 需要从矿物 surface energy 上尺度到颗粒连续体屈服的热力学一致模型。
问题 -> 温度依赖 surface energy 是否足以解释 brittle granular materials 的 thermal weakening？
方法 -> 用 intermolecular potential 推导 γ(T)；建立 SBM，以 As 为内变量；用 fractal GSD law 描述破碎；推导 free energy、dissipation、flow rules、yield surface。
证据 -> fracture toughness dataset、GSD data、sandstone 和 St. Peter sand 的 stress-strain/yield surfaces/AE 对比。
发现 -> 仅考虑 quartz surface energy 的温度依赖即可自然再现实验中不同 confining pressure 下的热弱化；elastic properties 变化次要。
机制 -> 升温降低生成新表面的能量成本，促进 grain crushing，使 yield surface 和 hardening 演化发生变化。
意义 -> 为核废料、地热、坝工、湿热耦合和 pore-fluid chemistry 提供可扩展建模基础。

## 8. 方法/理论/模型细拆
Section 2 从 mineral scale 出发。2.1 讨论 crack growth thermodynamics；2.2 用 temperature-dependent surface energy 建模，借 Morse potential 把原子间势能、表面分离和温度联系；2.3 用 fracture toughness datasets 验证 γ(T) 或相关模型。

Section 3 是核心 SBM。3.1 写 grain crushing thermodynamics；3.2 建立 surface area-GSD relation，用 evolving fractal dimension 描述初始 GSD 到 ultimate GSD 的演化；3.3 写 Helmholtz free energy；3.4 推导 dissipation rate、flow rules 和 yield surface。关键在于 As 和 γ 是 thermodynamically conjugated pair。

Section 4 做 model performance：先验证 sandstones thermal weakening，再验证 St. Peter sand。作者不仅比 stress-strain，也比 p'-porosity change、yield surfaces、AE/cumulative parent grains 等，形成多证据链。

方法复杂度合理，因为它要跨四个尺度。可复现关键是公式、参数表、GSD 参数、surface energy calibration 和实验数据来源；这些需要核查 Tables 1-3 和 Appendix。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| thermal weakening 主要源于 constituent mineral surface energy 降低 | 摘要、6 | 仅用 quartz γ(T) 即可预测 sandstones/St. Peter sand 热弱化 | 模型-实验对比 | 强 | 仅限 quartz-dominated 与 20-150°C |
| As 是描述 grain crushing 的有效唯一内变量 | 摘要、3、6 | As-GSD relation、free energy/dissipation 推导、GSD 数据对比 | 理论 + 数据 | 中强 | 忽略形状/摩擦/重排细节 |
| γ 与 As 的共轭关系使 γ(T) 自然进入 yield function | 摘要、3.4、6 | Helmholtz free energy、dissipation rate、flow rule/yield surface | 热力学推导 | 强 | 公式细节需核查 |
| fractal-type GSD expression 优于线性插值，尤其 fine particles | 3.2、6 | carbonate sand、zeolite granules GSD 对比 | 数据拟合 | 中强 | 数据集有限 |
| bulk elastic properties 在测试范围变化次要 | 摘要、6 | E、ν 随温度数据与模型比较 | 文献数据 | 中强 | 不同矿物/高温可能不同 |
| 模型可预测 consolidated/unconsolidated sands 的 stress-strain 和 yield behavior | 4、6 | Bleursville、Locharbriggs、St. Peter sand 对比图 | 实验验证 | 强 | 参数校准独立性需核查 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | particle with crack in fluid/thermal environment | crack thermodynamics | 建立矿物尺度物理图像 | 是 |
| Fig. 2 | Morse potential 与 interatomic force | γ(T) 来源 | 把温度与表面能联系 | 是 |
| Fig. 3 | fracture toughness model vs data | surface energy model | 验证矿物尺度关系 | 是 |
| Fig. 4 | E、ν 随温度 | elasticity 次要 | 排除替代机制 | 是 |
| Table 1 | SBM 变量/参数 | 理论定义 | 保证符号可读 | 否 |
| Fig. 6-8 | GSD 与 fractal dimension/模型对比 | As-GSD law | 支撑内变量演化 | 是 |
| Table 2-3 | 材料/模型参数 | model performance | 支撑复现和校准 | 否 |
| Fig. 10、12、13 | sandstone/sand stress、porosity response | 热弱化预测 | 连接模型与实验 | 是 |
| Fig. 14 | St. Peter sand yield surfaces | γ(T) enters yield | 展示 yield surface shrink/shift | 是 |
| Fig. 15-16 | GSD probability/AE vs parent grains | breakage mechanism | 用破碎统计支撑宏观屈服 | 是 |

图表叙事是从原子势能到颗粒级 GSD 再到宏观屈服，尺度逐层放大。每一组图都对应论证链的一段，不是装饰性图表。

## 11. 章节结构与篇章布局
Abstract：工程背景 -> 机制目标 -> mineral surface energy -> SBM -> model validation -> 主结论。
Introduction：环境温度影响 -> 实验事实 -> 经验模型不足 -> breakage mechanics 机会 -> 本文贡献。
Section 2：矿物尺度热弱化，先 crack thermodynamics，再 γ(T)，再 fracture toughness data。
Section 3：surface-based breakage mechanics，建立连续体理论。
Section 4：model performance，分别验证 sandstones 和 St. Peter sand。
Section 5：讨论 rearrangement factor R 与 150°C 以上热弱化。
Section 6：结论，强调适用范围和未来湿热/化学扩展。

最值得模仿的是“底层物理 -> 内变量 -> 屈服面 -> 实验验证”的结构。它让理论模型不是从 yield function 突然出现，而是从表面能一步步上尺度。

结构风险：推导多且跨尺度，读者可能在 Section 2-3 之间迷失；图 3-4 的实验数据用于防守 surface energy 和 elasticity 机制，因此需要写得清楚。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/On-the-yielding-of-brittle-granular-materia_2026_Journal-of-the-Mechanics-an.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：14
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Thermal weakening at mineral scale | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Thermodynamics of crack growth | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Temperature-dependency of surface energy | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Comparing with fracture toughness dataset | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3 Surface-based breakage mechanics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Thermodynamics of grain crushing | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Helmholtz free energy | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Dissipation rate, flow rules, and yield surface | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Model performance | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Thermal weaking of sandstones | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Discussions | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1 The rearrangement factor R | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落推进：第一段工程需求；第二段实验证据；第三段模型不足；第四段 breakage mechanics 作为替代；最后提出 surface energy-SBM 框架。

Theory 段落推进：先给热力学量，再给几何统计量，再给自由能和耗散，最后给 flow/yield。这种写法让每个公式都有物理角色。

Model performance 段落推进：先说明材料和参数；再比较曲线；再解释为何温度影响在高 confining pressure 下更明显；最后用 yield surface 和 AE/parent grains 做交叉验证。

Discussion 段落推进：先处理 rearrangement factor R 这类模型内部参数，再讨论 150°C 以上机制变化，避免结论过度泛化。

可复用模板：`Empirical parameter dependence fits [phenomenon], but a bottom-up model can link [macroscopic response] to [microscale thermodynamic quantity].`

## 13. 文笔画像与语言习惯
语气是理论机制型，强调 “mechanistically link”“thermodynamically consistent”“sole internal state variable”“naturally form a conjugated pair”。作者善于把强理论 claim 与适用边界绑定。

问题表达常用 environmental conditions、thermal weakening、yielding behavior、micromechanical foundation。方法表达常用 bottom-up approach、upscale、surface-based breakage mechanics、fractal-type expression。机制表达常用 surface energy reduction、grain crushing、specific surface area、dissipation rate。

claim 强度在 20-150°C quartz-dominated 范围内较高；高温、ductile grains、humidity/chemistry 部分用 likely、promising direction 等谨慎语气。长句用于推导逻辑，短句用于结论边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：energy(94)；temperature(80)；surface(76)；granular(44)；grain(42)；quartz(34)；gsd(32)；data(29)；sand(29)；size(28)；thermal(28)；kokash(27)；model(27)；materials(26)；yield(26)；solid(26)；stress(26)；sandstone(26)；grains(25)；confining(24)
- 高频学术名词：energy(94)；temperature(80)；model(27)；materials(26)；stress(26)；dissipation(23)；pressure(21)；fracture(20)；parameters(19)；porosity(19)；strain(17)；function(14)；toughness(14)；relation(14)；system(13)；behavior(13)
- 高频学术动词：shows(9)；proposed(7)；shown(7)；predicted(6)；compared(5)；derived(5)；captured(4)；show(3)；propose(3)；investigated(3)；suggest(2)；capture(2)；evaluate(2)；demonstrated(2)；indicates(2)；estimate(2)
- 高频形容词：experimental(44)；elastic(38)；thermal(28)；effective(24)；different(21)；plastic(20)；initial(18)；total(17)；potential(14)；interatomic(14)；fractal(13)；mechanical(11)；temperature-dependent(11)；specific(11)；current(11)；parent(11)
- 高频副词/连接副词：respectively(24)；significantly(10)；assembly(10)；therefore(6)；however(5)；primarily(5)；essentially(5)；especially(5)；naturally(4)；accurately(4)；thermodynamically(3)；equivalently(3)；kelly(3)；directly(3)；relatively(3)；strongly(2)
- 高频二词短语：surface energy(39)；grain size(22)；granular materials(21)；free energy(21)；surface area(17)；thermal weakening(14)；fracture toughness(14)；confining pressure(13)；initial ultimate(13)；porosity change(12)；confining pressures(11)；specific surface(10)；helmholtz free(10)；bleursville sandstone(10)；locharbriggs sandstone(10)；parent grains(10)
- 高频三词短语：helmholtz free energy(10)；specific surface area(9)；brittle granular materials(8)；peter quartz sand(8)；initial ultimate gsds(8)；bleursville sandstone locharbriggs(8)；sandstone locharbriggs sandstone(8)；number parent grains(8)；internal state variable(5)；energy release rate(5)；modulus poisson ratio(5)；different confining pressures(5)

**主动、被动与句法**

- 被动语态估计次数：122
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：711
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：259
- 一般过去时线索：59
- 现在完成时线索：12
- 情态动词线索：63
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：granular(8)；surface(6)；energy(6)；materials(5)；temperature(5)；yielding(4)；boulder(4)；brittle(3)
- 1. Introduction：temperature(19)；energy(13)；surface(12)；granular(7)；yield(6)；materials(5)；creep(5)；zhang(5)
- 2. Thermal weakening at mineral scale：无明显高频项
- 2.1. Thermodynamics of crack growth：surf(18)；fluid(14)；energy(13)；surface(9)；temperature(8)；free(7)；crack(6)；system(6)
- 2.2. Temperature-dependency of surface energy：energy(14)；interatomic(14)；temperature(13)；solid(10)；surface(7)；potential(7)；force(7)；equilibrium(6)
- 2.3. Comparing with fracture toughness dataset：quartz(8)；temperatures(7)；various(5)；glass(5)；data(5)；values(5)；temperature(5)；fracture(4)
- 3. Surface-based breakage mechanics：无明显高频项
- 3.1. Thermodynamics of grain crushing：gsd(20)；grain(17)；energy(14)；surface(12)；ultimate(12)；size(11)；gsds(11)；volume(10)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
骨架：`While empirical temperature-dependent parameters can reproduce observations, they lack [micromechanical foundation] and may be inconsistent with [thermodynamic principle].`
中文启发：先承认经验模型有效，再指出理论合法性不足。

### 14.2 方法与框架表达
骨架：`We seek to mechanistically link [macroscopic behavior] to [temperature-dependent microscale property].`
中文启发：一句话把宏观和微观连接，是机制论文的核心句。

### 14.3 结果与趋势表达
骨架：`By considering only [microscale temperature dependence], the model naturally reproduces [macroscopic thermal weakening] under [conditions].`
中文启发：强调“only”可突出机制简洁性，但要有适用范围。

### 14.4 机制解释表达
骨架：`[Internal variable] and [energy quantity] form a thermodynamically conjugated pair, allowing [temperature-dependent property] to explicitly enter [yield/dissipation function].`
中文启发：热力学模型要写出共轭变量对。

### 14.5 贡献与意义表达
骨架：`The proposed theory provides a foundation for generalizations to [coupled effects], which frequently arise in [applications].`
中文启发：未来工作从当前理论自然延伸，而非另起炉灶。

### 14.6 局限与未来工作表达
骨架：`This conclusion is validated for [material class] in [temperature range]; for [other regimes], additional mechanisms such as [A/B/C] are likely important.`
中文启发：强结论后立刻写适用边界，是高可信写法。

## 15. 引用策略与文献使用
引用分工明确。工程背景引用 nuclear waste、geothermal、climate-resilient structures；实验事实引用 triaxial、creep、fracture toughness、crack velocity 数据；模型背景引用 empirical thermo-elastoplastic theories 和 continuum breakage mechanics；验证部分引用具体 sandstone/sand 数据集。

经典文献用于 CBM、surface energy、fracture mechanics；近年文献用于工程需求和最新实验。作者使用引用制造“事实-模型”落差：事实显示热弱化，模型多为经验调参，因此需要机制上尺度。

引用风险：矿物 surface energy 数据来源少且温度范围有限；GSD 数据来自不同材料，可能与验证材料不同。作者通过把 GSD relation 作为独立结构规律、把 quartz-dominated 作为适用范围来减小风险。

## 16. 审稿人视角风险
最大攻击面是单一机制主导性。温度会影响水化、湿度、亚临界裂纹、接触摩擦、热膨胀、孔隙流体和化学溶解；surface energy reduction 是否足以解释所有热弱化？本文只在 20-150°C quartz-dominated 条件下强 claim，这是必要防守。

第二风险是 As 作为唯一 internal variable。颗粒破碎还涉及颗粒形状、接触网络、重排和摩擦；rearrangement factor R 的处理可能被追问。第三风险是参数校准独立性：如果用同一数据调参再验证，预测性会降低。

第四风险是高温相变。quartz α-β phase transition 附近 surface energy 行为改变，本文结论不能外推。图表需核查：fracture toughness fit、E/ν 温度曲线、yield surface 对比和 AE 对照决定说服强度。

## 17. 可复用资产
可复用选题角度：把经验温度依赖参数替换为可上尺度的微观能量量。
可复用 gap 制造：模型能拟合但缺 micromechanical foundation 与 thermodynamic consistency。
可复用论证链：工程热环境 -> 实验热弱化 -> 经验模型不足 -> microscale γ(T) -> conjugate internal variable -> yield function -> 多数据验证。
可复用图表设计：微观机制示意、势能曲线、矿物数据验证、弹性替代机制排除、GSD 演化、宏观曲线、yield surface。
可复用段落结构：先提出可替代解释，再用数据排除或降级它。
可复用句型：`This choice is advantageous because [state variable] and [thermodynamic quantity] naturally form a conjugate pair.`
不宜直接模仿：在未限定材料和温度范围时声称单一机制主导。

## 18. 对我写论文的启发
写类似多尺度理论论文时，可以学习“变量选择即创新”。本文的 As 不是普通符号替换，而是让 surface energy γ(T) 合法进入耗散和屈服的关键。一个好的内变量能把微观机制、热力学和宏观响应连起来。

Introduction 可迁移写法：先列实验事实，再指出经验模型的哲学缺陷。Method 可迁移写法：从能量共轭关系出发，而不是从拟合公式出发。Results 可迁移写法：不仅验证目标曲线，还用弹性参数、GSD、AE 等旁证排除替代解释。

需要避免：bottom-up 叙事过长而没有回到工程数据；公式推导和参数表缺少物理解释；适用范围写得太晚。

## 19. 最终浓缩
这篇论文最值得学的是：把温度依赖颗粒屈服写成矿物表面能降低导致破碎耗散成本下降，并用 specific surface area 作为共轭内变量完成热力学上尺度。

最大风险是：surface energy 主导机制只在特定矿物和温度范围内被验证，高温、湿度、化学和延性颗粒会引入额外机制。

三个可迁移动作：1. 用经验模型不足引出机制模型；2. 选择能与微观能量共轭的内变量；3. 用多类数据验证并主动限定适用范围。
