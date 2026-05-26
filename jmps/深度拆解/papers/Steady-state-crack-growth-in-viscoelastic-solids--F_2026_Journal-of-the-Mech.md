# Steady state crack growth in viscoelastic solids: Full-field analysis for the strip geometry with finite damage zone

## 0. 读取说明
- 源 PDF：`jmps/文献/Steady-state-crack-growth-in-viscoelastic-solids--F_2026_Journal-of-the-Mech.pdf`
- 源 TXT：`jmps/文本/txt/Steady-state-crack-growth-in-viscoelastic-solids--F_2026_Journal-of-the-Mech.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 214 (2026) 106662, DOI: 10.1016/j.jmps.2026.106662。
- 是否需要结合 PDF 图像核查：需要。本文核心证据包括 Mode III strip 示意、damage zone 长度曲线、stress/strain streamline 分布、toughness-velocity 曲线、hysteresis loops 和 dissipation power density 云图；当前拆解依据 txt、图注和公式上下文，图像色标、曲线坐标和局部耗散位置需 PDF 核查。
- 本文类型：经典断裂力学/线性黏弹性理论论文，强调 exact full-field solution 和 finite damage zone。

## 1. 基本信息与论文身份
- 题名：Steady state crack growth in viscoelastic solids: Full-field analysis for the strip geometry with finite damage zone。
- 作者/机构：Chung-Yuen Hui, Rong Long；Cornell University、Hokkaido University、University of Colorado Boulder。
- 关键词：Steady state crack growth; Viscoelasticity; Fracture toughness; Damage zone; Creep function; Viscoelastic dissipation。
- 研究对象：Mode III steady-state crack growth in an infinite strip, Dugdale-Barenblatt cohesive/damage zone, linear viscoelastic solids。
- 研究尺度：strip half-height h、damage zone length lc、creep time tc、crack velocity v；从 small-scale damage (SSD) 到 large-scale damage (LSD)。
- 方法类型：移动坐标系 steady-state formulation + complex stress analytic solution + creep-function strain field + crack shearing displacement criterion + energy balance/hysteresis/free-energy dissipation density。
- 证据类型：应力/应变全场解析表达；标准固体和 power-law creep solid 的 toughness-velocity 曲线；dimensionless damage parameter 控制 SSD/LSD；streamline hysteresis loops；dissipation power density contour。
- 目标读者：黏弹性断裂、软材料裂纹、凝胶/橡胶韧性、cohesive zone model 和经典解析力学读者。
- JMPS 风格定位：典型理论力学论文。它回到经典 steady-state crack growth 问题，用有限 damage zone 重新整理速度依赖 toughness 与耗散全场，而不是只做数值模拟。

## 2. 摘要与核心信息提取
摘要直接宣布 exact full-field analysis：对象是 long strip 中 Mode III crack steady-state growth；材料为 linear viscoelastic solid，exponential 和 power-law creep functions 只是展示，理论可适用于所有线性黏弹性体；裂尖前方用 Dugdale-Barenblatt cohesive zone 表示材料损伤。

摘要最关键的 claim 有三层。第一，结果覆盖 SSD 到 LSD 全范围，提出一个 0-1 的新 dimensionless damage parameter 控制过渡。第二，在 SSD 中 fracture toughness 随 crack velocity 增加，并达到由 instantaneous/long-term moduli ratio 决定的平台，回收既有理论。第三，在 LSD 中 toughness 仍随速度增加，但被 damage parameter 给出的上界截断，超过上界就不存在 steady-state crack growth 解。

一句话主张：本文给出 Mode III 黏弹性 strip 中带有限 DB damage zone 的 steady-state crack growth 全场解，说明 toughness 随速度上升但在大尺度损伤时受 damage parameter 上界限制，并揭示损伤区增大反而会降低同速黏滞耗散。

核心关键词：Mode III strip；DB cohesive zone；finite damage zone；SSD/LSD transition；creep compliance；viscoelastic dissipation。

## 3. 选题层深拆
问题来源：稳态黏弹性裂纹增长是经典基本问题。Knauss、Schapery、de Gennes、Persson-Brener 等都认识到必须引入长度尺度，否则黏弹性耗散会出现速度无关的悖论。过程区或 cohesive zone 是自然长度尺度，但许多理论主要在 small-scale damage 或渐近条件下工作。

问题为什么重要：软凝胶、橡胶和黏弹性聚合物的裂纹韧性常随速度变化。若只用小尺度过程区公式，无法解释 damage zone 与试样高度相当甚至更大时 toughness、strain field 和 dissipation region 如何改变。工程上，有限样品可能在还没达到理想 steady state 前就被裂纹穿透，因此全场和尺度边界很关键。

问题为什么现在值得做：经典解析工具和 cohesive zone 模型已成熟，线性黏弹性 creep function 可一般表示，且近年软材料实验能够测量变形场和耗散。本文把这些基础重新组合，给出 strip geometry 的 exact full-field solution。

问题边界：Mode III、linear viscoelasticity、DB constant cohesive stress、infinitely wide strip、fixed displacement 和 relaxed far field。迁移到 Mode I、有限变形、非线性黏弹性或真实三维裂纹，需要谨慎。

## 4. 领域位置与文献版图
作者把论文放在 steady-state viscoelastic fracture 的经典谱系里。Knauss 和 Schapery 代表力学传统，de Gennes 和 Persson-Brener 代表物理传统。这些工作共同认识到裂尖附近的长度尺度决定 velocity-dependent dissipation。

本文站位不是推翻旧理论，而是扩展其适用范围：当 damage zone 有限且可很大时，stress field、strain field、Γ-v 关系和 dissipation distribution 需要重新计算。它还通过 SSD 极限回收旧结论，让新理论和经典理论连续。

文献组织方式值得学习：开头先把问题抬到“classic and fundamental”，再说明悖论和长度尺度，最后指出本文通过 finite damage zone full-field analysis 补上缺口。

## 5. Gap 制造机制
明示 gap：有限 damage zone 的 full-field steady-state solution 不足，特别是从 SSD 到 LSD 的过渡缺少统一参数。隐含 gap：许多 toughness-velocity 关系只给整体能量或渐近结论，不能告诉 stress、strain 和 dissipation 在空间中如何分布。

gap 类型：理论 gap + 尺度 gap + 全场证据 gap。理论 gap 是 crack velocity 与 energy release rate 的完整关系；尺度 gap 是 damage zone size 相对 h 的变化；全场 gap 是应力、应变、hysteresis 和 dissipation power density 的空间定位。

审稿人会追问：DB cohesive stress constant 是否过于理想；fully relaxed far field 在实验中能否达到；finite sample width 如何影响 steady state；free energy density 定义不唯一是否改变局部耗散解释。

## 6. 创新性判断
创新点一：给出 Mode III strip 中带 DB damage zone 的 exact stress field，并说明 normalized stress 只由 G∞γ∞/τc 控制，不直接依赖黏弹性参数或 crack velocity。创新点二：通过 crack shearing displacement criterion 建立 Γ/Γ0 与 V 的完整关系，引入 dimensionless damage parameter 控制 SSD/LSD。创新点三：用 hysteresis loops 和 dissipation power density 两种方式解释能量耗散。

创新强度：理论上强，尤其是有限 damage zone 全场解和 LSD 上界。它不是靠复杂数值求解取胜，而是靠解析结构和无量纲参数组织取胜。

创新必要性：强。没有 finite damage zone，速度依赖韧性会被限制在小尺度过程区；没有全场解，无法判断耗散是否局限于裂尖、是否出现长尾 creep recovery 区。

## 7. 论证链条复原
背景：稳态黏弹性裂纹增长是经典问题，必须引入长度尺度。 -> 文献：已有理论多关注 small-scale damage 或渐近 toughness。 -> gap：有限 damage zone 与 strip height 可比时，缺少 full-field solution 和统一过渡参数。 -> 问题：如何描述 stress、strain、Γ-v 和 dissipation 随 velocity、creep function、damage parameter 的变化。 -> 方法：Mode III strip 移动坐标系；DB cohesive zone；complex stress solution；creep compliance 得 strain；crack shearing displacement criterion；energy balance 与 hysteresis。 -> 证据：Fig.2-16 从 damage length、stress、toughness、strain、hysteresis 到 dissipation contour。 -> 发现：SSD 回收经典平台；LSD 受 damage parameter 上界限制；damage zone 变大可降低同速耗散；stress concentration 是耗散必要条件。 -> 意义：为软黏弹性材料裂纹实验和理论解释提供全场基准。

## 8. 方法/理论/模型细拆
模型几何：高度 2h、水平和出平面方向无限的 strip；裂纹位于中面，以速度 v 向右传播；移动坐标系原点放在 damage zone tip。Mode III 反平面剪切使位移只有 w(x,y)，应力只有 τ1、τ2。

边界条件：上下边界施加 ±Δ；damage zone 前方满足 DB cohesive traction τc；裂纹面 beyond crack tip traction-free；critical shearing displacement δc 决定 crack growth criterion。材料模型通过 creep compliance C(t/tc) 表示，standard solid 和 power-law creep solid 用于展示。

方法核心：stress field 由解析复函数给出，形式与 stationary elastic strip 相同，但 damage zone length 由 far-field stress 控制。strain field 则依赖 crack velocity 和 creep function，因为材料点沿 streamline 经历不同加载历史。能量部分一方面用 stress-strain hysteresis loop 计算 dissipated energy，另一方面定义 Helmholtz free energy density 得 dissipation power density contour。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Mode III strip 的 steady-state stress field 可给出 exact analytic expression | Section 3.1/Fig.2-3 | complex stress function、crack line 和 upper edge stress distribution | 解析推导 | 强 | 依赖理想无限 strip 与 Mode III 假设 |
| damage zone length 由 far-field strain 控制，并有 SSD/LSD 过渡 | Section 3.2-3.4/Fig.2 | ε=πlc/h 与 G∞γ∞/τc 的关系、SSD series approximation | 公式+图 | 强 | 真实裂纹模式更复杂 |
| SSD 中 toughness 随速度上升并达到 modulus ratio 平台 | Fig.4-5 | standard solids 与 power-law creep solids 的 Γ/Γ0-V 曲线 | 数值解析 | 强 | 仅在线性黏弹与小损伤尺度下直接对应经典结论 |
| LSD 中 toughness 被 damage parameter 上界限制，超过临界无 steady-state 解 | Fig.6 | δc 与 λ 的关系、ε→∞ envelope | 参数图 | 强 | 实验有限样品可能先失效 |
| 应变场依赖 crack velocity 和 creep function，快裂纹产生长尾 creep recovery 区 | Fig.7-9 | 不同 V 下 streamline strain distributions | 全场计算 | 中强 | 图像细节需 PDF 核查 |
| stress concentration 是黏弹耗散的必要条件之一 | Fig.10-16/Conclusion | hysteresis loops 与 dissipation power density contour | 能量分析 | 中强 | free energy density 定义不唯一 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig.1 | Mode III strip、DB cohesive zone、creep function | 问题定义 | 把几何、过程区和材料函数绑定 | 需结合 PDF 图像核查 |
| Fig.2 | damage zone length 与 normalized stress 关系 | SSD/LSD 过渡 claim | 显示小尺度近似何时失效 | 需结合 PDF 曲线核查 |
| Fig.3 | 不同 streamline 上 stress distribution | 全场应力 claim | 说明 stress concentration 和 damage zone 空间结构 | 需结合 PDF 图像核查 |
| Fig.4-6 | toughness-velocity 与 damage zone size | 速度依赖 toughness claim | 主结果图组 | 需结合 PDF 曲线核查 |
| Fig.7-9 | strain distributions along streamlines | 黏弹时程效应 claim | 展示慢/快裂纹下 strain tail | 需结合 PDF 图像核查 |
| Fig.10-13 | hysteresis loops | 能量耗散 claim | 把耗散解释为 material point history loop | 需结合 PDF 曲线核查 |
| Fig.14-16 | dissipation power density contour | 耗散空间定位 claim | 揭示裂尖与 creep recovery 区贡献 | 需结合 PDF 色标核查 |
| 核心公式 | complex stress、damage parameter、Γ/Γ0-V、free energy | 理论闭合 | 从场解到能量关系 | 不涉及图像本体 |

## 11. 章节结构与篇章布局
Introduction 提出经典问题、长度尺度悖论和本文贡献。Problem definition 交代 strip geometry、DB cohesive zone、material creep model 和 energy release rate。Solutions 是全文主体，逐步列出 stress field、damage zone length、damage parameter、SSD condition、streamline stress/strain、crack growth criterion 和 Γ-v 关系。Energy dissipation 以 hysteresis 和 dissipation power density 两条线解释耗散。Conclusions 回收假设、主要发现和实验边界。

结构特点：公式密集但章节标题非常清楚，读者可沿“场 -> 判据 -> 能量 -> 耗散”推进。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Steady-state-crack-growth-in-viscoelastic-solids--F_2026_Journal-of-the-Mech.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：19
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Problem definition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Strip geometry for Mode III steady state crack growth | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Material model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Energy release rate | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Solutions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Stress field | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Length of damage zone | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Condition for Small-Scale Damage (SSD) | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.5 Stress distribution along streamlines | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.6 Strain field | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.7 Strain fields for slow and fast crack growth | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.8 Crack shearing displacement and crack growth criterion | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.9 Relation between crack velocity and energy release rate | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 节奏：经典问题 -> 先前认识 -> 悖论 -> 需要长度尺度 -> 本文 full-field finite damage zone。Problem definition 主要是清空歧义：坐标、边界、符号和无量纲量定义非常细。

Solutions 段落常采用“直接列公式 + 讨论物理含义”模式。因为推导复杂，作者把详细 derivations 放到 SI，正文保留结果和解释。Energy dissipation 段落先承认线性黏弹中 dissipated energy 定义不唯一，再选择可闭合的 hysteresis 和 free-energy 路径。

可复用段落模板：`Since derivations are complicated, we directly list the solution and discuss its physical implications.` 中文写作中可用“推导见附录，正文强调结果的物理含义”。

## 13. 文笔画像与语言习惯
整体语气经典、严谨、边界感强。作者常用 “strictly speaking”“in theory”“in experiments, ... approximated by...” 管理理想模型和实验现实之间的距离。claim 很强，但总是被 Mode III、linear viscoelastic、fixed displacement、relaxed far field 等条件限定。

术语密度高且符号系统完整。List of symbols 放在前面，降低长理论论文阅读成本。中文写作可学习这一点：理论模型符号多时，先给符号表或在拆解中明确变量含义。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：crack(219)；damage(140)；zone(123)；velocity(91)；stress(87)；strain(86)；normalized(72)；viscoelastic(71)；ssd(70)；energy(66)；dissipation(64)；creep(49)；growth(47)；fracture(47)；material(44)；solution(44)；state(42)；tip(41)；function(39)；section(39)
- 高频学术名词：velocity(91)；solution(88)；stress(87)；strain(86)；energy(66)；dissipation(64)；condition(56)；fracture(47)；material(44)；function(39)；section(39)；assumption(36)；field(33)；toughness(32)；analysis(30)；parameter(26)
- 高频学术动词：shown(23)；show(12)；shows(11)；capture(3)；reveal(3)；indicates(3)；solved(2)；suggests(2)；compare(2)；compared(2)；derived(2)；derive(1)；suggest(1)；predict(1)；captured(1)；evaluate(1)
- 高频形容词：viscoelastic(142)；material(44)；cohesive(33)；small(27)；different(27)；elastic(20)；displacement(20)；critical(18)；linear(16)；experimental(16)；analytical(12)；large(12)；dimensionless(12)；external(12)；instantaneous(11)；constant(11)
- 高频副词/连接副词：therefore(21)；however(15)；specifically(11)；monotonically(10)；fully(10)；numerically(8)；experimentally(6)；infinitely(5)；respectively(5)；extremely(5)；especially(5)；notably(4)；consequently(4)；locally(4)；moreover(4)；finally(4)
- 高频二词短语：damage zone(105)；crack velocity(80)；crack growth(46)；crack tip(32)；steady state(30)；hui long(26)；energy release(26)；release rate(26)；state crack(23)；zone length(23)；viscoelastic dissipation(22)；creep function(22)；zone size(21)；stress strain(19)；cohesive zone(16)；power-law creep(15)
- 高频三词短语：energy release rate(26)；damage zone length(23)；steady state crack(22)；damage zone size(20)；state crack growth(19)；normalized damage zone(13)；normalized crack velocity(13)；dissipation power density(11)；stress strain fields(10)；viscoelastic fracture theories(8)；fast crack growth(8)；ahead crack tip(7)

**主动、被动与句法**

- 被动语态估计次数：180
- `we + 动作动词` 主动句估计次数：18
- 名词化表达估计次数：979
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：383
- 一般过去时线索：37
- 现在完成时线索：14
- 情态动词线索：86
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：crack(13)；damage(9)；viscoelastic(7)；zone(7)；velocity(7)；dissipation(5)；steady(4)；state(4)
- 1. Introduction：crack(40)；damage(34)；viscoelastic(25)；zone(25)；fracture(20)；velocity(15)；ssd(15)；stress(14)
- 2. Problem definition：crack(10)；zone(9)；strip(7)；damage(7)；tip(5)；displacement(5)；steady(4)；state(4)
- 2.2. Material model：creep(9)；function(7)；viscoelastic(4)；shear(3)；power-law(3)；material(2)；property(2)；normalized(2)
- 2.3. Energy release rate：energy(7)；strain(5)；crack(4)；material(4)；cohesive(3)；growth(2)；shear(2)；property(2)
- 3. Solutions：stress(10)；crack(9)；field(4)；two(4)；velocity(3)；components(3)；tan(3)；boundary(3)
- 3.2. Length of damage zone：damage(8)；zone(7)；solution(7)；ssd(6)；stress(5)；parameter(5)；crack(5)；limit(5)
- 3.4. Condition for Small-Scale Damage (SSD)：damage(18)；zone(17)；crack(14)；ssd(13)；stress(10)；length(9)；k-field(8)；small(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 模式：A classic and fundamental problem is...
- 骨架：X 是 Y 领域中的经典基本问题，但当 Z 尺度不再可忽略时，现有渐近理论不足。

### 14.2 方法与框架表达
- 模式：We consider an ideal strip geometry where steady state can theoretically occur.
- 骨架：为获得可解析解，本文考虑一个理想几何，在该几何下核心机制可被清晰分离。

### 14.3 结果与趋势表达
- 模式：If δc ≤ λ, the curve resembles the SSD solution...
- 骨架：当控制参数处于 A 区间时，结果回收经典极限；当进入 B 区间时，出现由新参数控制的上界。

### 14.4 机制解释表达
- 模式：This is because material points do not instantly recover...
- 骨架：该长尾区域源于材料点的历史响应滞后，恢复尺度由 vtc 控制。

### 14.5 贡献与意义表达
- 骨架：本文提供了一个 full-field benchmark，使整体 toughness、局部 strain history 和空间耗散可以在同一框架下计算。

### 14.6 局限与未来工作表达
- 骨架：严格 steady state 只在无限宽和充分 relaxed far field 下成立，有限样品实验只能近似实现。

## 15. 引用策略与文献使用
引用集中在 Introduction，用少量重量级经典文献建立问题权威性。Knauss/Schapery 负责力学谱系，de Gennes/Persson-Brener 负责物理谱系。正文推导很少再引用，因为证据主要来自作者自己的解析结果。

gap 不是靠堆引用，而是靠“经典理论在小尺度/渐近条件下有效，但 finite damage zone full-field 仍未完成”的逻辑。引用策略适合理论论文：少而重，先定问题，再让公式说话。

风险：若有近年数值或实验论文已经处理 finite process zone，需在引言中更精确区分本文 exact Mode III strip solution 的新意。

## 16. 审稿人视角风险
最大攻击面：Mode III 与真实 Mode I/混合模式裂纹的距离；DB cohesive zone 的 constant traction 简化；linear viscoelasticity 对软材料大变形的限制；fully relaxed far field 和 infinite strip 的实验不可达；free energy density 的非唯一性。

claim 是否过强：只要限定在模型假设内，强 claim 可接受。证据是否不足：理论场解丰富，但直接实验验证少。替代解释是否排除：在理想模型内排除较充分，真实材料中损伤、非线性、孔洞和有限尺寸都可能改变耗散。

## 17. 可复用资产
- 可复用选题角度：经典问题在有限尺度下重新求解。
- 可复用 gap：小尺度过程区理论不能覆盖 damage zone 与结构尺度可比的情形。
- 可复用论证链：理想几何 -> 全场解 -> 无量纲参数 -> 极限回收 -> 新边界预测 -> 能量耗散图。
- 可复用图表：几何示意、尺度参数曲线、streamline 场分布、toughness-velocity、hysteresis、dissipation contour。
- 不宜直接模仿：没有严密边界时，不要把理想模型结论直接写成实验规律。

## 18. 对我写论文的启发
如果写理论力学论文，可以学习本文如何把经典问题重新做深：不是换花哨方法，而是找到旧理论未覆盖的尺度区间，提出一个能贯通旧极限和新边界的无量纲参数。

Introduction 可学习其“经典问题 + 悖论 + 长度尺度”结构；Method 可学习其“正文列结果，推导放 SI”；Discussion 可学习其主动说明实验近似条件。

## 19. 最终浓缩
这篇论文最值得学：用 finite damage zone 把经典黏弹性裂纹的速度依赖 toughness、全场应变和耗散空间统一起来，并通过 SSD 极限回收旧理论。

这篇论文最大风险：理想 Mode III/线性/无限 strip 假设强，真实软材料断裂外推需谨慎。

三个可迁移动作：
1. 从经典理论的尺度盲区切入选题。
2. 用无量纲参数组织从旧极限到新现象的过渡。
3. 不只给整体曲线，还给 full-field 和耗散位置，增强机制说服力。
