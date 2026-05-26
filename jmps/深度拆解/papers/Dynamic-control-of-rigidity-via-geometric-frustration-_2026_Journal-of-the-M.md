# Dynamic control of rigidity via geometric frustration: Unifying central force network theory and responsive hyperelasticity for mechanical metamaterials

## 0. 读取说明
- 源 PDF：`jmps/文献/Dynamic-control-of-rigidity-via-geometric-frustration-_2026_Journal-of-the-M.pdf`
- 源 TXT：`jmps/文本/txt/Dynamic-control-of-rigidity-via-geometric-frustration-_2026_Journal-of-the-M.txt`
- 辅助参考：上一轮标准拆解只用于核对主线，本稿依据全文、图注、理论段和讨论重写。
- 是否需要结合 PDF 图像核查：需要。pentamode 单胞、FEM 应变场、band structure、modulus 曲线和附录图需结合 PDF 图像核查。
- 本文类型：理论设计 + 数值验证的机械超材料论文。

## 1. 基本信息与论文身份
- 题名：Dynamic control of rigidity via geometric frustration: Unifying central force network theory and responsive hyperelasticity for mechanical metamaterials
- 作者/机构：Santiago Gomez Melo, Falko Ziebert, Ulrich S. Schwarz；Heidelberg University/BioQuant。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214, 2026, Article 106661。
- DOI：10.1016/j.jmps.2026.106661
- 关键词：Rigidity transition；Mechanical metamaterial；Geometric frustration；Second order rigidity；Morphoelasticity；Band structure。
- 研究对象：由 stimuli-responsive constituent 构成的 pentamode/diamond lattice 机械超材料，如何通过几何挫折和自应力动态调控 shear modulus。
- 方法类型：central force network theory；rigidity matrix；Maxwell-Calladine；state of self-stress；responsive hyperelasticity；LCE/hydrogel constitutive actuation；FEM；band structure；variational ansatz；JAX point-particle simulations。
- 证据类型：网络理论推导、FEM 模量-控制参数曲线、LCE/hydrogel 两材料对比、band structure 零模抬升、点粒子解析/数值/FEM 标度比较。
- JMPS 风格定位：把抽象刚性理论、生物网络启发和响应超弹性材料转译成可制造单材料可变刚度超材料蓝图。

## 2. 摘要与核心信息提取
摘要先从 4D-printing 和 programmable metamaterials 的宏观性质控制切入，指出 variable stiffness 目前多依赖 multiphase 和大尺度单胞。然后给出本文方案：one material、micrometer unit cells、central force network theory + responsive hyperelasticity。核心物理机制是 geometric incompatibility 诱发 rigidity phase transition：responsive constituent 的本征变形被固定几何约束，产生 state of self-stress，进而通过 second order rigidity 消除 floppy modes，使 shear modulus 改变数个数量级。

一句话主张：把响应材料做成几何受限的 pentamode/diamond 网络，可以用本征收缩/膨胀制造几何不相容和边张力，从而动态抬升零模、切换刚度。

核心关键词：geometric incompatibility；state of self-stress；floppy modes；second order rigidity；responsive hyperelasticity；metastring。

## 3. 选题层深拆
问题来源：机械超材料已能通过几何和材料实现负泊松比、拓扑边界态、odd elasticity、strain-to-twist 等性质；4D printing 和 responsive materials 让性质随刺激改变成为可能。但可变刚度目前多靠 multiphase、melting/jamming/glass transition，单胞大且制造复杂。

为什么重要：如果单一响应材料和微米尺度单胞即可实现连续可调刚度，将为软机器人、微结构可编程材料和动态拓扑机械系统提供更简单路线。

为何现在值得做：LCE 和 hydrogel 可通过温度、pH 等刺激产生本征应变；two-photon laser printing 已能制造 LCE/hydrogel 微结构；rigidity theory 对 self-stress 如何消除 zero modes 有清晰预测。

问题边界：本文是理论与数值设计，尚无实验制造；主要关注 control parameter below unity 的正张力/收缩 rigidification，压缩/增长导致 buckling 的区域留作未来。

## 4. 领域位置与文献版图
作者将背景分成四块：第一，mechanical metamaterials 的几何设计和 exotic properties；第二，生物系统如 actin cytoskeleton、ECM、epithelial monolayers 的 rigidity transitions 和 adaptability；第三，LCE/hydrogel 等 responsive materials 和 4D printing；第四，已有 variable stiffness metamaterials，如 melting filler、jamming、glass transition，多为 multiphase 且尺度较大。

本文站位：从生物网络和 vertex model 中借用 geometric incompatibility/self-stress 机制，把它放入合成 pentamode 超材料。它不是让材料本身相变变硬，而是让响应本征变形在固定单胞中变成 prestress。

文献姿态：complements earlier work，而非否定。作者强调实践优势：single constituent、low power actuation、micron-scale possibility。

## 5. Gap 制造机制
显式 gap：variable stiffness 多由多相材料和大单胞实现，缺少单材料、微尺度、可连续调控的刚度切换机制。

隐含 gap：responsive materials 常被用于 shape change，较少用于动态控制 rigidity；central force network theory 能解释 self-stress，但尚未和 responsive hyperelastic continuum 结合成可制造设计。

gap 类型：设计机制 gap + 理论整合 gap + 制造尺度 gap。

gap 是否窄：作者收束到 pentamode/diamond lattice、LCE/hydrogel 两类材料、shear modulus 控制和 positive tension regime。

审稿人追问：实际打印结构是否满足中心力网络近似；有限节点/腰部半径、粘弹性、缺陷、屈曲、材料损伤是否会破坏数量级刚度变化。

## 6. 创新性判断
作者声明贡献：统一 central force network theory 和 responsive hyperelasticity，提出由 geometric frustration 动态控制 rigidity 的 metamaterial blueprint。

真实创新：第一，把 LCE/hydrogel 的本征收缩转译为网络边张力。第二，用 second order rigidity 解释 underconstrained pentamode 如何在 self-stress 下 rigidify。第三，FEM 与 point-particle band structure 双层验证，既有工程几何又有解析机制。第四，把 pentamode 从 metafluid 重新比喻为 3D self-tensing metastring，直观解释 transverse modes 与 tension 的关系。

创新类型：理论机制创新 + 设计蓝图创新。创新强度：中高，受实验缺失限制。

## 7. 论证链条复原
机械超材料性质可由单胞几何和材料控制 -> 已有 variable stiffness 路线多相/大尺度/跳变式 -> responsive materials 可产生可调本征应变 -> 中心力网络理论表明 underconstrained networks 有 floppy modes，但 self-stress 可通过 prestress stability matrix 赋予二阶刚性 -> 若 pentamode 结构外边界固定，responsive bars 不能达到自由本征长度，产生 geometric incompatibility -> 所有边处于张力 self-stress -> zero modes 被抬升，shear modulus 从近零变为有限并随控制参数变化 -> FEM 对 LCE/hydrogel pentamode 显示模量提升 -> diamond lattice band structure 证明 transverse acoustic zero modes 被张力抬升 -> shear modulus 与 edge tension 呈幂律，点粒子接近线性，FEM 指数约 3/4 -> 该设计可由现有微打印材料实现，压缩/拓扑边界态等留作未来。

薄弱环节：FEM 和理论指数不完全一致，实际制造/耗散尚未验证。

## 8. 方法/理论/模型细拆
网络理论：节点-边图用 incidence matrix g 描述，edge length L_alpha 由节点位置和边界向量决定。rigidity matrix R 描述一阶边长变化；ker(R) 是 linear zero modes；ker(R^T) 是 states of self-stress。Maxwell-Calladine 给出自由度、约束、LZM 和 SSS 的计数关系。

几何不相容：若边势 U_alpha 的各自最小长度无法在允许 edge length space Omega 内同时实现，平衡点就带 self-stress。正张力下 prestress stability matrix 在非平凡 zero mode 子空间正定，产生 second order rigidity。

响应超弹性：LCE 用 nematic order/temperature 产生 anisotropic active strain；hydrogel 用 swelling/control parameter 产生 isotropic/volumetric response。FEM 中把 responsive constituent 做成 pentamode cube 并固定边界，测 shear modulus。

解析 band structure：diamond lattice nearest-neighbor model，控制参数 chi/lambda/phi 进入 edge tension f(chi)。当 chi=1，transverse acoustic modes 是 flat zero bands；chi<1 产生张力，bands lifted，density of states 的 zero peak broadened，shear modulus 近似 proportional to f。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| geometric incompatibility 可生成 self-stress 并消除 floppy modes | 2.1 | rigidity matrix、prestress stability matrix、Maxwell-Calladine 推导 | 理论 | 强 | 中心力假设理想化 |
| responsive pentamode 可由 LCE/hydrogel 控制 shear modulus | 3.1 | Fig. 3-5 FEM，lambda/phi 变化下 modulus 提升 | FEM 数值 | 中强 | 制造和材料耗散未验证 |
| zero modes 在张力下被 band structure 抬升 | 3.2 | Fig. 6，transverse acoustic flat bands 在 chi<1 后 lift | 谱分析 | 强 | 点粒子近似 |
| shear modulus 与 edge tension 呈幂律 | 3.2 | Fig. 7，解析/点粒子/FEM 对比；点粒子近线性，FEM 约 3/4 | 标度对比 | 中强 | FEM 指数不同 |
| 单材料微尺度实现有现实可能 | Discussion | LCE 20% strain、hydrogel 45% shrinkage、two-photon printing 文献 | 文献可行性 | 中 | 尚无样机 |
| 控制可连续调节，不同于 melting/jamming 跳变 | Discussion | control parameter 可连续调 lambda/phi | 理论/材料特性 | 中 | 实验控制精度未知 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1/Eq. 1-4 | central force network 定义 | 理论基础 | 建立 R、SSS、Maxwell-Calladine | 是/公式 |
| Fig. 2 | 设计概念图 | responsive pentamode | 把抽象机制可视化 | 是 |
| Fig. 3 | 单胞和 FEM cube | 几何实现 | 说明仿真对象 | 是 |
| Fig. 5 | LCE/hydrogel shear modulus | 动态刚度控制 | 核心 FEM 证据 | 是 |
| Fig. 6/Eq. 21-22 | band structure 与 dispersion | 零模抬升 | 机制解释 | 是/公式 |
| Fig. 7/Eq. 23 | modulus vs control/tension | 标度律 | 连接解析/数值/FEM | 是/公式 |
| Fig. C.8 | Cauchy strain tensor | 局部应变分布 | 附录支持 | 是 |

结果叙事先 FEM 证明“能变硬”，再 band structure 解释“为什么变硬”，最后讨论制造和未来拓展。

## 11. 章节结构与篇章布局
Introduction：先铺超材料设计空间，再借生物系统引出可适应和刚性转变，随后介绍 responsive materials，最后制造 variable stiffness gap。Methods：网络理论、网络模量、响应连续体三块并列。Results：3.1 用 FEM 给设计验证；3.2 用 band structure 给解析机制。Discussion：把本文机制与 melting/jamming/glass transition 区分，讨论 LCE/hydrogel 可制造性、连续调控、无上界张力控制、耗散假设、压缩/拓扑未来方向。

最值得模仿：抽象理论论文用“设计概念图 + FEM 实例 + 简化解析模型”三层证据，降低跳跃感。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Dynamic-control-of-rigidity-via-geometric-frustration-_2026_Journal-of-the-M.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Theory of mechanical networks | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Elastic moduli of mechanical networks | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Continuum theory for responsive elastic media | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Analytical modulus calculation from the band structure | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Discussion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落从宏观愿景到具体 gap。Methods 段落先定义数学对象，再马上解释物理意义，如 ker(R) 是 zero modes、ker(R^T) 是 self-stress。Results 段落常用“this confirms/demonstrates”把图与理论命题绑定。Discussion 段落先总结机制，再与已有路线比较，再评估实现性。

可复用段落模板：已有路线通过材料相变改变 stiffness；本文路线通过几何约束把响应应变转化为 self-stress；self-stress 改变 zero modes 的能量代价，因此改变宏观模量。

## 13. 文笔画像与语言习惯
整体语气：理论设计型，表达自信，善于把数学对象变成物理图像。claim 强度对理论和数值较强，对制造用 expect/envision。

问题表达：variable stiffness has been so far only achieved；meaningful exploration remains a challenge；dynamical control of rigidity。

贡献表达：we suggest an alternative strategy；unifying central force network theory and responsive hyperelasticity；blueprint of a single-phase metamaterial。

机制表达：geometric incompatibility；state of self-stress；eliminates zero modes；second order rigidity；self-tensing metastring。

限定表达：we expect；poses an interesting perspective；falls in the regime of positive tension；computationally challenging。

写法特点：常用对比句，明确区分“材料相变变硬”和“几何挫折引发自应力变硬”。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：modulus(49)；modes(47)；nodes(36)；tension(36)；control(35)；mechanical(35)；system(33)；given(32)；parameter(32)；edge(31)；strain(30)；hydrogel(30)；zero(29)；rigidity(28)；network(28)；order(28)；case(28)；energy(28)；lce(27)；shear(26)
- 高频学术名词：structure(48)；transition(38)；system(33)；parameter(32)；strain(30)；energy(28)；rigidity(28)；solution(20)；condition(18)；function(18)；material(15)；incompatibility(15)；actuation(15)；direction(15)；deformation(14)；model(13)
- 高频学术动词：shown(12)；proposed(7)；show(6)；compared(5)；demonstrated(5)；predicted(5)；suggest(4)；simulated(4)；derive(2)；captured(2)；compare(2)；propose(2)；shows(2)；indicates(2)；demonstrate(1)；estimated(1)
- 高频形容词：elastic(40)；mechanical(35)；geometric(25)；optical(20)；acoustic(20)；metamaterial(19)；crystal(19)；linear(17)；analytical(16)；responsive(15)；material(15)；displacement(13)；constituent(12)；capable(11)；constant(11)；erent(10)
- 高频副词/连接副词：analytically(10)；consequently(8)；experimentally(8)；numerically(8)；therefore(7)；furthermore(6)；finally(6)；additionally(5)；respectively(5)；locally(4)；theoretically(4)；dynamically(4)；connelly(4)；mainly(3)；necessarily(3)；essentially(3)
- 高频二词短语：control parameter(23)；shear modulus(20)；gomez melo(19)；zero modes(17)；geometric incompatibility(14)；lce hydrogel(12)；edge tension(10)；con guration(9)；diamond lattice(9)；point particles(8)；dispersion relation(8)；geometric frustration(7)；sti ness(7)；phase transition(7)；liquid crystal(7)；case lce(7)
- 高频三词短语：linear zero modes(5)；central force network(4)；rest con guration(4)；control parameter above(4)；nearest neighbour interaction(4)；control parameter below(4)；force network theory(3)；network theory responsive(3)；theory responsive hyperelasticity(3)；variable sti ness(3)；rst order rigid(3)；states self stress(3)

**主动、被动与句法**

- 被动语态估计次数：152
- `we + 动作动词` 主动句估计次数：3
- 名词化表达估计次数：688
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：279
- 一般过去时线索：44
- 现在完成时线索：26
- 情态动词线索：78
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：rigidity(5)；metamaterials(5)；geometric(4)；frustration(3)；mechanical(3)；one(3)；dynamic(2)；control(2)
- 1. Introduction：mechanical(11)；metamaterials(9)；design(7)；materials(7)；properties(6)；rigidity(6)；via(6)；responsive(6)
- 2. Methods：无明显高频项
- 2.1. Theory of mechanical networks：network(13)；edge(13)；rigid(12)；rst(7)；rigidity(7)；order(7)；zero(7)；system(7)
- 2.2. Elastic moduli of mechanical networks：network(4)；pentamode(4)；prestress(4)；mechanical(3)；moduli(3)；structure(3)；min(3)；metamaterial(3)
- 2.3. Continuum theory for responsive elastic media：energy(9)；bar(9)；hydrogel(7)；case(7)；given(6)；tensor(6)；lce(5)；factor(5)
- 3. Results：nodes(14)；bars(13)；strain(13)；shear(12)；modulus(12)；hydrogel(11)；lce(10)；parameter(10)
- 3.2. Analytical modulus calculation from the band structure：modes(23)；tension(17)；transverse(16)；parameter(15)；acoustic(13)；optical(12)；given(11)；control(11)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：Existing strategies typically require A, whereas here we propose B.
- 启发：设计论文要把实践优势写具体：single constituent、micron scale、continuous control。

### 14.2 方法与框架表达
- 骨架：We combine theory X with material model Y to propose a blueprint for Z.
- 启发：跨理论整合要说明两个理论各自贡献。

### 14.3 结果与趋势表达
- 骨架：Lowering the control parameter induces tension, lifts the zero modes, and increases the modulus.
- 启发：把控制参数、微观谱、宏观模量串在一句里。

### 14.4 机制解释表达
- 骨架：The modulus is controlled by edge tension in the same way a string's transverse modes are controlled by tension.
- 启发：好比喻能让复杂 band structure 可理解。

### 14.5 贡献与意义表达
- 骨架：This strategy complements earlier work in which stiffness is tuned through material transitions.
- 启发：用 complements 避免过度贬低前人。

### 14.6 局限与未来工作表达
- 骨架：The true limit will be set by experimental parameters such as damage tolerance and actuation strength.
- 启发：理论无上界时必须马上给实验边界。

## 15. 引用策略与文献使用
引用分布：Introduction 引用超材料、4D printing、生物网络、responsive materials、variable stiffness routes；Methods 引用 rigidity theory、Maxwell-Calladine、second order rigidity；Discussion 引用可制造 LCE/hydrogel、rheology、topological modes。

经典文献用途：Maxwell/Calladine 与 rigidity theory 赋予理论合法性。近年文献用途：微打印、LCE/hydrogel actuation 和 variable stiffness 当前路线。

gap 搭建：用多篇 multiphase/jamming/melting/glass-transition 文献证明已有路线存在，但强调本文是 alternative/complementary。

引用风险：实验可制造性完全基于文献推断，需避免写成已实现。

## 16. 审稿人视角风险
- 最大攻击面：理论中心力网络与实际连续体 pentamode 的差异。
- 证据风险：FEM 指数约 3/4 与理论线性不一致，需要解释 finite node size、evanescent modes、finite size。
- 实验风险：打印精度、节点固定、粘弹性、响应速度、疲劳、prestress damage。
- 边界风险：固定外节点或 rigid bars 的实现会影响模量。
- claim 风险：new class of dynamic metamaterials 是蓝图，不是实验验证。
- 替代解释：局部 buckling 或 bending stiffness 可能参与 FEM 模量提升。
- 图像核查：Fig. 5/7 数量级变化和 Fig. 6 band lifting 需 PDF 核查。

## 17. 可复用资产
- 选题角度：把生物/网络中的自应力刚化机制迁移到可制造超材料。
- gap 制造方式：已有路线复杂/大尺度/跳变 -> 单材料/微尺度/连续控制需求。
- 论证链：rigidity theory -> responsive material -> geometric frustration -> FEM -> band structure -> manufacturing discussion。
- 图表设计：网络定义图、概念设计图、FEM 几何图、modulus-control 曲线、band structure、标度律。
- 段落结构：先机制，后实例，再标度，最后工程边界。
- 句型骨架：The constituent does not become intrinsically stiffer; the structure becomes stiffer because actuation generates self-stress.
- 不宜模仿：没有实验时，不要把 blueprint 写成材料已实现。

## 18. 对我写论文的启发
第一，理论设计论文要给“区别于已有路线”的一句话机制。本文最可学的是：材料并非相变变硬，而是响应变形被几何约束转化为 self-stress。第二，复杂理论要有简化模型解释 FEM，否则 FEM 曲线只是数值现象。第三，Discussion 可以非常具体地谈制造参数和材料响应幅度，让理论看起来可落地。

可迁移到 Introduction：先讲设计空间难以探索，再提出物理机制导向的设计原则。可迁移到 Results：用 band structure 解释模量曲线。可迁移到 Discussion：比较前人路线时强调 complement。

需要避免：过度依赖类比；忽视实际固定边界；在理论标度和 FEM 不一致时含糊处理。

## 19. 最终浓缩
最值得学习：把 self-stress/second-order rigidity 这类抽象网络理论，翻译成 LCE/hydrogel pentamode 的动态刚度开关设计。

最大风险：实验制造、耗散、缺陷和 buckling 尚未验证，FEM 与点粒子理论存在标度差异。

三个可迁移动作：
1. 明确区分本文机制与已有材料相变/堵塞路线。
2. 用 FEM 展示可行性，用 band structure 解释机制。
3. 在 Discussion 中把理论无上界说法转化为由 actuation strength 和 damage tolerance 限定的工程边界。
