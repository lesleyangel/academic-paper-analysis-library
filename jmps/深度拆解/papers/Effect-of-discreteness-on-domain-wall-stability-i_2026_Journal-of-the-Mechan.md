# Effect of discreteness on domain wall stability in a plate coupled to a foundation of bistable elements

## 0. 读取说明

- 源 PDF：`jmps/文献/Effect-of-discreteness-on-domain-wall-stability-i_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/Effect-of-discreteness-on-domain-wall-stability-i_2026_Journal-of-the-Mechan.txt`
- 文本抽取：PyMuPDF，23 页。含理论模型、ROM、FEA、图注、表格、附录和 references；txt 中连字/公式有乱码。
- 是否需要结合 PDF 图像核查：需要。domain wall 形态、FEA contour、能量 landscape、phase diagram、polygon/cat geometry 等高度依赖图像，txt 只能确认功能与文字描述。
- 本文类型：多稳态可重构结构/弹性板-双稳态基底系统的理论与数值研究论文。

## 1. 基本信息与论文身份

- 题名：Effect of discreteness on domain wall stability in a plate coupled to a foundation of bistable elements
- 作者与机构：Dengge Jin、Samuele Ferracin、Vincent Tournat、Jordan R. Raney；University of Pennsylvania、LAUM/CNRS/Le Mans Université。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214, 2026, Article 106643。
- DOI：10.1016/j.jmps.2026.106643。
- 关键词：Reconfigurable surface；Multistability；Domain wall；Phase transition；Peierls-Nabarro effect。
- 研究对象：弹性柔顺板耦合二维双稳态单元阵列后形成的 closed domain walls，其扩张、收缩和亚稳 pinning。
- 研究尺度：连续板尺度、双稳态基底离散单元尺度、domain wall collective coordinate 尺度。
- 方法类型：Kirchhoff-Love plate、quartic bistable potential、collective coordinate reduced-order model、Peierls-Nabarro energy modulation、Abaqus FEA、polygon local stability criteria。
- 证据类型：ROM 能量 landscape、临界核化半径、动态相轨迹、FEA contour、稳定半径范围、凸/凹多边形稳定表格和示例形状。
- JMPS 风格定位：用简化理论模型解释复杂可重构形态稳定机制，并把结果转化为设计规则。

## 2. 摘要与核心信息提取

摘要先从 multistable/reconfigurable surfaces 的应用背景进入，强调无需持续驱动即可保持复杂形态。随后定义系统：compliant plate coupled to a two-dimensional foundation of bistable elements。核心现象是 domain walls 有三种行为：expansion、shrinking、metastable pinning。作者把三种行为归因于两个极限：continuum limit 中强耦合导致类似一阶相变的 global phase transition；anti-continuum/discrete limit 中 Peierls-Nabarro energy modulation 导致 pinning。方法句说明建立 reduced-order model 捕捉含 domain wall 构型的总势能，并用 FEA 验证。结果扩展到 axisymmetric 和 non-axisymmetric geometries，给出 phase diagrams 和局部几何稳定准则。

一句话主张：本文证明基底离散性通过 Peierls-Nabarro 型能量调制，在弹性板-双稳态基底系统中把本应扩张或收缩的 domain wall 钉扎为亚稳形态，并给出由 bistable asymmetry、discreteness 和几何边长共同决定的稳定设计规则。

核心关键词：domain wall；bistable foundation；discreteness ratio；critical nucleation radius；P-N pinning；reduced-order model；polygon stability。

## 3. 选题层深拆

问题来自可重构表面的一对矛盾：连续柔顺表面能提供平滑形态和长程弹性耦合，但常需持续驱动维持形状；双稳态单元能无源保持状态，但离散性和几何相互作用会决定哪些形态真正稳定。此前已有类似系统能形成多种稳定曲面，但 domain wall 为什么扩张、收缩或停在某个有限尺寸，缺少统一能量解释。

作者的关键选题动作是把“能否保持形状”转化为“closed domain wall 在能量 landscape 中有没有局部极小值”。这比直接仿真大量形状更可解释，也能导出设计准则。

为什么重要：如果想设计可重构表面、可编程形态或多稳态机械超材料，就必须知道施加多大 actuation area 会触发全局相变，何种离散单元间距能 pin 住目标形状，凸/凹角和边长如何影响稳定性。

问题边界：双稳态单元用通用 quartic potential 表示，不指定具体几何；板用 Kirchhoff-Love 小挠度弯曲为主；基底惯性忽略；plate-foundation coupling 只通过 out-of-plane displacement；ROM 用 circular/tanh domain wall profile，后续多边形准则是一阶近似。

## 4. 领域位置与文献版图

文献版图包括四组。第一组是表面形态与功能响应，如 mechanics、acoustics、optics、fluid dynamics 中曲率和周期性影响性能。第二组是 reconfigurable surfaces/structures，需要 on-demand tuning of shape。第三组是 mechanical bistability 和双稳态基底，能够无持续能量保持构型。第四组是 domain wall、phase transition、Peierls-Nabarro effect、φ4 lattice/kink motion 等离散非线性系统理论。

本文站在“连续板长程耦合 + 离散双稳态基底 + domain wall 能量地形”的交叉点。它不是单纯做有限元展示，而是借用 collective coordinate approximation 和 P-N effect 语言，把结构稳定性解释为连续能量背景与离散周期调制的竞争。

对前人关系处理方式：作者引用已有可重构表面和 bistable foundation 实验作为应用动机，引用 φ4 lattice 和 P-N 文献作为理论类比，再说明本文系统因为板的 biharmonic bending operator 和二维 hexagonal foundation 而有新问题。

## 5. Gap 制造机制

显式 gap：已有系统能形成复杂稳定形态，但离散性如何改变 domain wall energy landscape、何时导致 expansion/shrinking/pinning、何种非轴对称几何稳定，尚需定量设计规则。

隐含 gap：连续极限只给出临界核化尺寸，不能解释有限半径亚稳 pinning；纯离散仿真能看到 pinning，但缺少可迁移准则。本文用 ROM 把二者桥接。

gap 类型：机制 gap + 设计准则 gap + 几何泛化 gap。

gap 证据来源：Section 2 中 FEA 先展示同一系统会出现 shrink、expand、pin 三种行为；后续理论解释这些行为分别由 surface/bulk energy competition 和 P-N modulation 造成。

审稿人追问：ROM 的 circular tanh ansatz 对大 domain wall 或非圆形状是否可靠；P-N modulation 的计算是否依赖 hexagonal lattice；polygon stability 的 edge independence 假设何时失效。

## 6. 创新性判断

作者声称的贡献：建立适用于 continuum 与 discrete regimes 的 analytical ROM；给出 continuum limit 下 critical nucleation radius 和三相区；揭示 discreteness 超过临界值后产生 P-N local minima；用 FEA 验证 metastable radius range；把规则扩展到凸 120° 和凹 240° 多边形 domain walls，并展示 general geometries。

真实创新较强。它把一个可重构结构设计问题转化为 energy-landscape/P-N pinning 问题，并从轴对称推广到多边形几何准则。尤其是 concave angle 用 complementary bistable parameter α' = 1 - α 推断稳定性的写法，很有设计规则味道。

创新必要性高。没有 discreteness，连续模型只预测 expand/shrink；有离散性后才能保持 finite shape。理解离散性是设计稳定图案的关键。

容易被挑战：ROM 对大半径圆形 domain wall 低估稳定上界，因为 FEA 中形状会转为 lattice-conforming hexagon；general polygon criterion 是一阶近似，需要更多 FEA/实验验证；示例 cat-like geometry 带有展示性，不是严谨泛化证明。

## 7. 论证链条复原

背景 -> 多稳态可重构表面需要无持续驱动保持复杂形态。  
文献 -> 双稳态基底、domain wall、P-N pinning 和相变理论提供基础。  
gap -> 仍不清楚离散基底如何决定 closed domain wall 的扩张、收缩和亚稳钉扎。  
问题 -> 给定板、双稳态单元、离散间距、初始 domain wall，预测最终形态是否稳定。  
方法 -> 定义 quartic bistable potential、discreteness γ、characteristic length；构建 tanh-profile ROM 和势能；连续极限求临界半径；离散情形求 P-N local minima；FEA 验证；扩展到 polygon。  
证据 -> Fig. 1 三种行为；Fig. 5 临界半径和 FEA 相符；Fig. 7 动态轨迹相符；Figs. 8-11 pinning 范围相符；Tables 1-2 多边形稳定推断与 FEA 一致。  
发现 -> α、γ、rd 共同控制稳定；metastability 最先在连续 energy landscape 最平坦的 rcr 附近出现；稳定半径只在有限范围内存在；多边形稳定可由边长和局部角准则预测。  
意义 -> 为可重构表面设计提供 actuation size、foundation density 和 shape geometry 规则。

## 8. 方法/理论/模型细拆

系统定义：弹性薄板厚度 h、弯曲刚度 B、密度 ρ，连接到 hexagonal honeycomb 排列的双稳态基底。单元势能是含 asymmetry parameter α 的 quartic potential。α 控制两个稳态的能量差；γ = lattice spacing / characteristic domain-wall width 表征离散性。

连续 PDE：采用 Kirchhoff-Love plate theory，axisymmetric deformation w(r,t) 受 biharmonic bending operator 和 bistable restoring force 控制。定义 characteristic time T 和 length L，将方程无量纲化。

Reduced-order model：用 hyperbolic tangent ansatz 表示 domain wall profile。Stage 1 中 domain wall 半径 rd 变化，高度保持 wb；Stage 2 中 wall 消失，高度 H 和 rd 同时变化。Collective coordinate method 将场问题降为 rd/H 的有效势能问题。

连续势能：总能量由 plate bending energy 与 foundation energy 组成。Stage 1 中势能包含 reciprocal term、linear surface energy term 和 quadratic bulk energy term。α < 0.5 时 bulk energy favor expansion，α > 0.5 时 favor shrinking。临界半径 rcr 是能量全局最大的位置。

动态方程：由 Lagrangian 得到 rd 的有效质量和运动方程。有效质量随 perimeter 缩放，因为 kinetic energy 局域在 domain wall 附近。ROM 能预测 shrink/expand 的速度趋势，但 FEA 中 phonon radiation 和 profile relaxation 会让运动更慢。

离散基底：foundation energy 不再积分，而是对单元求和。domain wall 移动时相对 lattice 的位置变化产生周期能量调制，即 P-N effect。局部能量 minima 对应 metastable pinned states。临界 γcr 以上才出现 local minima。

多边形准则：规则 hexagon 稳定范围可转成边长整数 nst 的稳定区间。凸 120° irregular hexagon 若每条边长都在稳定范围内，则推断整体稳定。凹 240° 角用 complementary regular hexagons 和 α' = 1 - α 判断；需要 convex 和 concave edges 同时满足稳定条件。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| domain wall 有 expansion、shrinking、pinning 三种行为 | Section 2, Fig. 1 | FEA 代表性演化图 | 数值观察 | 强 | 需图像核查 |
| continuum limit 中存在 critical nucleation radius | Section 4.1, Fig. 5 | ROM cubic equation 和 FEA expand/shrink 对比 | 理论+FEA | 强 | 依赖 ROM profile |
| ROM 可预测 domain wall 动态轨迹 | Section 4.1.2, Fig. 7 | ODE 与 FEA center position 对比 | 动态验证 | 中强 | FEA 慢于 ROM |
| discreteness 产生 P-N energy modulation 和 metastable radii | Section 4.2, Fig. 8 | 能量曲线周期振荡、local minima 和 energy barrier | ROM | 强 | 圆形假设 |
| FEA 验证稳定半径范围并显示大半径六边形化 | Figs. 9-11 | ROM minima 与 FEA stable radii 对比 | FEA 对比 | 中强 | ROM 低估上界 |
| polygon stability 可由边长/角度局部准则推断 | Section 5, Tables 1-2, Figs. 12-14 | irregular hexagon/octagon FEA 与 inferred stability 一致 | 设计规则验证 | 中强 | 一阶近似，样本有限 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 系统、势能、三种行为 | 问题定义与现象 | 开篇核心图 | 是 |
| Fig. 2 | P-N 能量调制示意 | 离散性机制 | 概念解释 | 是 |
| Eqs. (1)-(5) | 单元势能和板 PDE | 模型基础 | 理论严谨性 | 否 |
| Fig. 3 | tanh profile 与两阶段收缩 | ROM ansatz | 证明近似来源 | 是 |
| Eqs. (9)-(18) | 连续势能 | surface/bulk competition | 核心推导 | 否 |
| Fig. 5 | α regime 与 rcr | 临界核化尺寸 | 设计相图 | 是 |
| Fig. 7 | FEA 动态和 ROM 轨迹 | 动态预测 | 检验 ODE | 是 |
| Fig. 8 | γ 对 energy landscape 的影响 | P-N pinning | 机制核心证据 | 是 |
| Figs. 9-11 | stable radii 与演化历史 | ROM-FEA 验证 | 证明 metastability | 是 |
| Figs. 12-15, Tables 1-2 | 多边形和一般形状 | 几何设计规则 | 从圆到复杂形态 | 是 |

图表顺序非常适合学习：先展示现象，再给概念机制，再推导模型，再用相图和 FEA 验证，最后展示设计扩展。

## 11. 章节结构与篇章布局

Introduction：可重构表面背景、domain wall 和离散性问题、本文贡献。  
Section 2：系统设定和三种 domain wall 行为。  
Section 3：理论模型，含 PDE、ROM、连续/离散势能。  
Section 4：轴对称 domain walls，先连续临界半径和动态，再离散 pinning 和 FEA 对比。  
Section 5：一般 polygon domain walls，分凸 120°、凹 240° 和 general geometries。  
Section 6：总结机制、设计规则和局限。  
Appendices：势能和动能推导。

最值得模仿的是 Section 2 的“先展示三种行为”。作者没有一上来推公式，而是先让读者看到同一系统能有三种结果，从而自然需要理论解释。

结构风险：Section 5 从规则圆/六边形跳到 irregular polygon 和 cat-shaped geometry，展示性强，严格性略弱。作者用 Tables 1-2 和 FEA 弥补。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Effect-of-discreteness-on-domain-wall-stability-i_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：16
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Expansion, shrinking, or metastable pinning of a domain wall | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3 Theoretical model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Reduced-order model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Potential energy for continuous foundation case | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Potential energy for discrete foundation case | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Axisymmetric domain walls | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Continuum limit | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1.1 Critical nucleation size | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1.2 Equation of motion: Dynamic domain wall motion | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Transition from continuum limit to discrete case | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 4.2.1 ROM prediction | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2.2 Comparison between ROM and FEA | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5 General polygon domain walls | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段从 surface morphology 功能讲到 reconfigurable surfaces，再强调 bistability 可无持续驱动保持状态。第二段引入 plate + bistable foundation 系统及 domain wall。随后明确两个问题：离散性如何重塑能量 landscape；哪些 domain-wall geometry 稳定。

Section 2 的段落先定义系统和 FEA 步骤，再解释三种行为的能量尺度：surface energy ~ perimeter，bulk energy ~ area。接着引入 P-N effect 解释 pinning。这种“现象 -> 尺度分析 -> 离散机制”的节奏很强。

Theory 段落中，作者先承认 PDE 无闭式解，再引入 tanh ansatz 和 collective coordinate ROM。这个“承认难点 -> 采用降阶”写法让近似更可接受。

Conclusion 不只总结结果，还列出四个限制：只考虑 out-of-plane coupling、忽略基底动力学、固定 circular/tanh profile、polygon stability 是一阶近似。这种局限写得具体且不伤主结论。

可复用段落模板：  
“In the continuum limit, the evolution is governed by a competition between surface energy, which scales with the perimeter, and bulk energy, which scales with the enclosed area. In the discrete regime, the same smooth energy landscape is modulated by the lattice periodicity, creating local minima that can pin the domain wall.”

## 13. 文笔画像与语言习惯

文风兼具机制解释和设计导向。常用词：expansion、shrinking、metastable pinning、energy landscape、critical nucleation size、Peierls-Nabarro modulation、stable range、local criterion、design rules。

claim 强度较明确，但局限写得充分。作者敢于说 “establishes governing principles”，因为有 ROM 和 FEA 支撑；同时承认 ROM 是 first-order approximation。

段落中大量使用 “we consider”、“we define”、“we show”、“we infer”、“we validate”。理论推导处用 “follows from”、“is given by”、“can be normalized”；设计规则处用 “we expect”、“we infer”，体现推断性质。

机制语言偏尺度分析：surface energy scales as O(rd)，bulk energy scales as O(rd^2)，P-N modulation scales with perimeter。这样的尺度词非常值得学习。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：domain(164)；wall(139)；energy(123)；foundation(77)；stable(69)；bistable(62)；fea(54)；rom(53)；stability(51)；plate(47)；system(45)；discreteness(40)；potential(40)；range(35)；walls(34)；size(34)；con(33)；metastable(31)；landscape(29)；angles(28)
- 高频学术名词：energy(123)；foundation(77)；stability(51)；system(45)；transition(42)；discreteness(40)；analysis(26)；displacement(25)；results(23)；model(23)；evolution(23)；motion(22)；section(20)；parameter(19)；equation(18)；condition(18)
- 高频学术动词：shown(17)；show(11)；shows(8)；predicted(6)；validate(5)；compared(5)；validated(3)；reveal(3)；derived(3)；predict(2)；develop(2)；investigated(2)；indicate(2)；derive(1)；investigate(1)；capture(1)
- 高频形容词：stable(138)；bistable(62)；local(54)；critical(46)；elastic(46)；potential(40)；global(32)；metastable(31)；initial(27)；hexagonal(26)；displacement(25)；dynamic(22)；continuous(22)；unstable(16)；small(16)；large(14)
- 高频副词/连接副词：approximately(10)；however(10)；therefore(8)；ciently(8)；previously(7)；strongly(6)；generally(6)；consequently(6)；primarily(6)；substantially(4)；elastically(4)；naturally(4)；relatively(4)；nearly(4)；respectively(4)；quantitatively(3)
- 高频二词短语：domain wall(130)；domain walls(34)；potential energy(29)；energy landscape(28)；con gurations(16)；bistable foundation(15)；fea results(15)；stable range(14)；phase transition(13)；bistable units(13)；critical nucleation(13)；con guration(12)；elastic energy(11)；reduced-order model(10)；out-of-plane displacement(10)；fea simulations(10)
- 高频三词短语：critical nucleation size(10)；potential energy landscape(9)；stage domain wall(9)；tanh tanh tanh(8)；domain wall expands(7)；initial domain wall(7)；domain wall size(7)；stable con gurations(6)；domain wall radius(6)；evolution domain wall(6)；sech sech tanh(6)；stable domain wall(6)

**主动、被动与句法**

- 被动语态估计次数：122
- `we + 动作动词` 主动句估计次数：10
- 名词化表达估计次数：862
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：250
- 一般过去时线索：54
- 现在完成时线索：8
- 情态动词线索：52
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：domain(8)；walls(6)；discreteness(5)；stability(4)；coupled(4)；foundation(4)；phase(4)；bistable(3)
- 1. Introduction：system(10)；units(8)；bistable(7)；plate(7)；foundation(7)；transition(7)；domain(7)；domain-wall(7)
- 2. Expansion, shrinking, or metastable pinning of a domain wall：domain(29)；wall(29)；energy(20)；foundation(16)；unit(16)；bistable(15)；plate(13)；displacement(12)
- 3. Theoretical model：foundation(7)；domain(5)；wall(5)；plate(4)；bistable(4)；small(3)；force(3)；energy(3)
- 3.1. Reduced-order model：tanh(5)；domain(5)；wall(5)；model(4)；plate(4)；stage(4)；rom(3)；height(3)
- 3.2. Potential energy for continuous foundation case：energy(17)；wall(10)；stage(9)；domain(8)；potential(7)；term(7)；point(6)；foundation(5)
- 3.3. Potential energy for discrete foundation case：foundation(7)；energy(4)；ned(4)；bistable(4)；unit(4)；continuous(4)；case(3)；same(3)
- 4. Axisymmetric domain walls：section(4)；domain(4)；wall(4)；rom(4)；fea(3)；erent(3)；comparison(2)；continuous(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

### 14.1 问题与 gap 表达

- 骨架：While [system] can realize [stable configurations], the mechanisms determining whether [interface/domain wall] expands, shrinks, or pins remain unclear.
- 启发：把复杂形态问题转化为界面运动三分类。

### 14.2 方法与框架表达

- 骨架：We develop a reduced-order model based on [collective coordinate/ansatz] to capture the total potential energy of configurations with [domain wall].
- 启发：ROM 的功能是捕捉能量，不一定复现所有场细节。

### 14.3 结果与趋势表达

- 骨架：The model yields phase diagrams identifying regimes of [A], [B], and [C] as functions of [parameters].
- 启发：结果句要明确相图变量和分类。

### 14.4 机制解释表达

- 骨架：Metastability arises from the competition between [global energetic drive] and [discreteness-induced local modulation].
- 启发：用“competition between”组织机制。

### 14.5 贡献与意义表达

- 骨架：These results provide predictive design rules linking [material parameter], [discreteness], and [geometry] to [shape stability].
- 启发：把理论参数转化为设计规则。

### 14.6 局限与未来工作表达

- 骨架：The stability inference should be regarded as a first-order approximation because adjacent edges and angles are geometrically and elastically coupled.
- 启发：几何规则类论文要承认局部独立假设。

## 15. 引用策略与文献使用

Introduction 用宽引用铺可重构表面应用：mechanics、acoustics、optics、fluid dynamics、morphing structures。然后用 bistability 文献说明无持续驱动保持形态的机制。再用 φ4 lattice、P-N effect、kink motion 文献建立理论类比。

方法引用精确：Kirchhoff-Love plate theory 用 Timoshenko；collective coordinate 用 Gervais and Sakita、Takyi and Weigel；P-N effect 用 Kevrekidis/Weinstein、Truskinovsky/Vainchtein；phonon radiation 用 Peyrard/Kruskal 和作者近期 beam-bistable work。

gap 与引用关系：引用不是为了说“没人做过”，而是把 plate-bistable foundation 置于多个成熟理论旁边，说明本文把这些理论迁移到二维可重构表面 domain wall stability。

引用风险：实验文献和理论类比多，但本文自身没有物理实验，只是 FEA。若未来投稿相近题目，应尽量补实验验证。

## 16. 审稿人视角风险

最大攻击面是 ROM 近似。Circular tanh profile 对小/中等轴对称 domain wall 有效，但大半径 FEA 会转为 hexagonal lattice-conforming shape，导致 ROM 低估稳定上界。

polygon stability 的 local criterion 是一阶近似。相邻边和角之间有几何/弹性耦合，不能完全独立。Tables 1-2 的 FEA 验证有限，无法覆盖所有复杂形状。

基底动力学被忽略。若真实双稳态单元有显著质量或内部自由度，domain wall transient 会改变，尽管静态 energy landscape 可能仍保留。

plate-foundation coupling 只考虑 out-of-plane displacement，不含 axial strain、大变形和非理想连接。实验实现时可能偏离。

图像核查重点：Fig. 8 local minima 是否确实随 γ 增强；Fig. 9 ROM 与 FEA 稳定半径差异；Figs. 12-14 polygon 推断与 FEA 是否一致；Fig. 15 eye domain wall 消失与 outline 稳定是否清楚。

## 17. 可复用资产

- 可复用选题角度：研究离散性不是数值误差，而是能创造稳定形态的设计资源。
- 可复用 gap 制造：连续模型解释相变，离散模型解释 pinning，二者缺少统一能量地形。
- 可复用论证链：现象三分类 -> 能量尺度分析 -> ROM -> 相图 -> FEA 验证 -> 几何设计规则。
- 可复用图表设计：系统示意、行为三联图、P-N 概念图、势能 landscape、临界半径相图、FEA 动态图、多边形稳定表。
- 可复用段落结构：先定性 scaling，再定量推导，再用 FEA 验证。
- 可复用句型骨架：`The discreteness-induced modulation creates local minima in an otherwise smooth energy landscape, thereby pinning the domain wall at metastable radii.`
- 可复用引用组织：应用背景 + 非线性格点理论 + 降阶方法 + 板理论。
- 不宜直接模仿：不要用少量 FEA 就宣称任意几何稳定；不要忽略实际基底惯性和连接非理想性。

## 18. 对我写论文的启发

如果写类似可重构/多稳态结构论文，最值得学的是用 energy landscape 统一行为。扩张、收缩、钉扎看似不同，但都能由势能斜率和局部极小解释。这样论文不会变成一堆仿真案例。

Introduction 可迁移写法：从应用需求进入，但尽快收束到一个可分析的 mechanics question，例如 domain wall stability。

Method 可迁移写法：复杂 PDE 无闭式解时，用 ansatz + collective coordinate 做 ROM，但要说明 ansatz 来自 FEA 或已知 kink solution。

Results 可迁移写法：用连续极限建立 baseline，再引入离散修正。这样读者能清楚看到离散性新增了什么。

需要避免：展示性形状（如 cat geometry）要放在设计示例位置，不要让它承担主要证明；主要证明仍应来自相图、表格和系统 FEA。

## 19. 最终浓缩

这篇论文最值得学的是：把“离散性”从通常被视为近似误差的因素，转化为可设计的 Peierls-Nabarro pinning 机制。连续极限解释全局相变，离散调制解释亚稳保持，多边形规则则把机制转成形状设计语言。

最大风险是：ROM 和多边形稳定准则都是一阶近似，真实实验、大变形、基底动力学和复杂连接尚未验证。

三个可迁移动作：
1. 用 surface energy 与 bulk energy 的尺度竞争解释界面扩张/收缩。
2. 用离散诱导的能量局部极小解释 metastability，而不只报告仿真稳定。
3. 把轴对称结果转化为边长/角度规则，形成可操作设计准则。
