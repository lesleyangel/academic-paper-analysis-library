# Couplant-free and high-purity excitation of unidirectional shear waves via a meta-exciter

## 0. 读取说明
- 源 PDF：`jmps/文献/Couplant-free-and-high-purity-excitation-of-uni_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps/文本/txt/Couplant-free-and-high-purity-excitation-of-uni_2026_Journal-of-the-Mechanic.txt`
- 图像核查：txt 可读 Fig. 1-11 与 Appendix 图题，但波场颜色、FFT 主峰、实验装置和 metasurface 单元需结合 PDF 图像核查。
- 论文类型：理论设计 + FEM 仿真 + 实验验证的弹性波/超材料方法论文。

## 1. 基本信息与论文身份
- 作者：Weijian Zhou, Muyang Li, Miao Yang, Yang Liu, He Sun, Zheng Zhong, Bin Wu, Weiqiu Chen。
- 期刊/年份：Journal of the Mechanics and Physics of Solids, 214, 2026, 106652。
- DOI：10.1016/j.jmps.2026.106652。
- 关键词：elastic metasurface；shear wave；wavefront engineering；meta-exciter；inverse design；normal-encoding principle。
- 研究对象：无需切向耦合剂、仅用法向接触激发高纯度定向 SV 剪切波。
- 方法类型：SV-Rayleigh wave interference theory；normal-encoding principle；PWE 快速前向模型；FEM 参数优化；铝板实验与 FFT 验证。
- 目标读者：弹性超材料、超声 NDT、波前调控、医学弹性成像研究者。
- JMPS 定位：从工程 trade-off 提炼新的边界编码机制，再以解析关系和实验验证闭环。

## 2. 摘要与核心信息提取
摘要开头把问题压缩为 fundamental trade-off：高 modal purity 需要刚性 tangential coupling，但 couplant/bonding 会限制扫描灵活性和 inline inspection throughput；EMAT 和 laser ultrasound 虽便携但效率低或多模态干扰强。本文提出 normal-encoding paradigm：利用 SV-Rayleigh standing wave nodes，在切向位移为零、法向位移仍有可设计相位分布的位置放置法向源阵列，以 phase gradient 合成定向 SV wavefield。结果包括解析角度-间距-相位梯度关系、PWE 快速计算、FEM 中 SV energy proportion 超过 90%、1 mm 铝板实验中 beam steering 偏差小于 1°。

## 3. 选题层深拆
选题来自 NDT 和 elastography 对高纯度剪切波的实际需求。SV 波对剪切模量敏感、波长短，适合细小缺陷和组织刚度表征；但传统压电换能器需要切向应力传递，导致粘接/耦合剂瓶颈。本文把问题收束为：能否只通过法向位移边界，在不传递切向应力的情况下，激发定向高纯度 SV 波？这个问题足够窄，且直接服务 inline inspection、复杂构件扫描和低频深部 elastography。

## 4. 领域位置与文献版图
文献被组织为四类：传统压电/相控阵，优点是能量高但依赖耦合剂；EMAT/laser ultrasound，优点是非接触但效率或纯度不足；elastic metasurfaces，具备相位和波前调控能力；NDT/医学应用，提供场景压力。本文站在 source design 与 metasurface wavefront engineering 的交界，差异不是“又一个超表面”，而是将剪切波源端机制从 tangential-pushing 改为 normal-encoding。

## 5. Gap 制造机制
- 显式 gap：现有高纯度 shear wave excitation 通常需要 tangential coupling，couplant-free 方法又牺牲效率和模态纯度。
- 隐含 gap：metasurface 研究多关注传播调制，较少从源端解决“法向接触产生纯 SV 波”的边界条件矛盾。
- Gap 类型：工程瓶颈 gap + 物理机制 gap + 逆设计 gap。
- 审稿追问：实验是否真正 dry contact？monolithic metasurface 是否等价于独立 phase-controlled vertical sources？1 mm 铝板 plane-stress 近似可否推广到厚板、曲面或复合材料？

## 6. 创新性判断
作者贡献包括：提出 normal-encoding principle；推导 SV 角度与阵列间距/相位梯度关系；建立 PWE + FEM 设计流程；仿真 SV 能量占比 >90%；实验 beam direction 偏差 <1°。真实创新中高，最有辨识度的是 standing wave node 处“切向位移消失、法向位移编码”的物理构型。局限是实验仍为 proof-of-concept，独立相控阵列、真实干接触工程夹持和复杂介质尚待实现。

## 7. 论证链条复原
背景：SV 波在 NDT 和医学成像中有价值。  
文献：传统高纯度方法依赖切向耦合，非接触方法效率/纯度不足。  
Gap：缺少只靠法向接触的高纯度定向 SV source。  
方法：利用 SV-Rayleigh interference nodes，推导 phase gradient 与 radiation angle，构造 finite meta-exciter，PWE/FEM 计算并优化。  
证据：Fig. 1 概念，Fig. 2-3 理论模型，Fig. 4-8 FEM 和参数扫描，Fig. 9 metasurface 实现，Fig. 10-11 实验波场和 FFT。  
发现：法向阵列可激发约 38° 定向 SV，实验 FFT 主能量方向 37.91°，与仿真偏差小于 1°。

## 8. 方法/理论/模型细拆
方法核心是在弹性半空间中分析 obliquely incident SV wave 与 Rayleigh wave 的干涉，找到 tangential displacement vanish 的节点，再在节点处布置法向点源并赋予相位梯度。关键变量包括 SV radiation angle `α`、阵列间距 `d`、相位梯度 `Δϕ/d`、wave vector、SV/Rayleigh/longitudinal energy proportion、100 kHz 工作频率和 1 mm 铝板 plane-stress 参数。流程是理论推导 -> 有限源阵列 -> PWE 快速计算 -> PML FEM 验证 -> 参数扫描 -> metasurface 实现 -> 实验扫描和 FFT。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 传统剪切波存在纯度与扫描灵活性 trade-off | Introduction | 压电、EMAT、laser、phased array 文献比较 | 综述 | 强 | 场景依赖 |
| normal-encoding 可用法向位移合成定向 SV 波 | Section 2 | SV-Rayleigh 节点理论、Fig. 1-3 | 理论推导 | 强 | 节点条件对边界敏感 |
| 角度、间距、相位梯度可逆设计 | Section 2-3 | 解析关系、Fig. 6-7 | 公式+仿真 | 强 | 离散相位影响纯度 |
| FEM 中 SV 能量比例可超过 90% | Section 3 | Fig. 5-8 | 数值仿真 | 中强 | PML/材料假设需核查 |
| 实验实现约 38° 定向 SV 波 | Section 4 | Fig. 10-11，FFT 37.91° | 实验 | 强 | 扫描分辨率和杂散波影响波长 |
| 适合 inline NDT 和 elastography | Conclusion | 无耦合、方向可调、高纯度 | 应用推论 | 中 | 复杂介质未验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | tangential-pushing vs normal-encoding | 范式转换 | 一图说明创新 | 是 |
| Fig. 2 | 半空间 SV-Rayleigh 干涉 | 节点条件 | 理论来源 | 是 |
| Fig. 3 | 有限 nodal displacement 源阵列 | 理论到结构 | 工程化桥接 | 是 |
| Fig. 4 | PML 抑制 inter-cell coupling | FEM 可靠性 | 排除反射干扰 | 是 |
| Fig. 5 | FEM 单向 SV 波场 | 高纯度定向激发 | 直接性能证据 | 是 |
| Fig. 6-7 | 参数扫描/控制带 | 逆设计可操作 | 显示设计空间 | 是 |
| Fig. 8 | 时间域仿真 | 动态稳定性 | 补充频域证据 | 是 |
| Fig. 9 | metasurface 实现 | 可制备性 | 装置桥接 | 是 |
| Fig. 10-11 | 实验波场与 FFT | 实验验证 | 核心 validation | 是 |
| angle-phase relation | 逆设计公式 | 可编程设计 | 避免黑箱优化 | 否 |

## 11. 章节结构与篇章布局
Introduction 先讲 SV 应用价值，再讲 trade-off，再引出 metasurface。Section 2 标题直接写出 normal-encoding principle 和 theoretical foundation，降低读者进入门槛。Section 3 做 FEM 设计和参数分析，Section 4 做实验验证，Conclusion 则按范式、理论关系、仿真/实验指标、应用和局限展开。最值得学的是“概念图 + 解析关系 + 参数扫 + 实验 FFT”的证据顺序。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Couplant-free-and-high-purity-excitation-of-uni_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：9
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 The normal-encoding principle: standing wave nodal excitation and its theoretical foundation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1 SV-Rayleigh wave interference theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Finite structure meta-exciter model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Design and parameter analysis of meta-exciter via FEM simulations | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Meta-exciter for unidirectional and high-purity SV wave | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 SV wave meta-exciter optimization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Experimental validation | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
问题段用对比式节奏：traditional transducers 高纯但不灵活，EMAT/laser 便携但低效/多模态。方法段从节点物理解释到 finite source array。实验段先报方向和波长，再主动解释 33 mm 与理论 31 mm 的差异来自 1 mm 扫描分辨率和 spurious components。这种主动误差解释能减轻审稿质疑。

## 13. 文笔画像与语言习惯
整体语气工程承诺较强，但结果指标明确。常用问题词：fundamental trade-off, bottleneck, low efficiency, multimodal interference。方法词：normal-encoding, phase gradient, inverse design, PWE, meta-exciter。结果词：exceeding 90%, deviation less than 1°, concentrated around 100 kHz。限定词：proof-of-concept, homogeneous or weakly stratified media, future phase control, practical coupling methods。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：wave(129)；excitation(51)；waves(50)；surface(46)；shear(45)；phase(42)；displacement(37)；normal(26)；array(25)；plane(23)；field(23)；longitudinal(22)；zhou(21)；metasurface(21)；design(21)；gradient(21)；angle(21)；beam(21)；tangential(20)；boundary(20)
- 高频学术名词：excitation(51)；displacement(37)；mechanism(26)；simulation(26)；condition(24)；field(23)；analysis(20)；stress(19)；model(18)；energy(16)；conditions(16)；solution(16)；interference(16)；equation(14)；results(14)；interface(13)
- 高频学术动词：shows(11)；shown(7)；proposed(6)；demonstrate(5)；derived(5)；indicate(4)；compared(3)；indicates(3)；validate(2)；reveal(2)；developed(2)；solved(1)；suggest(1)；develop(1)
- 高频形容词：displacement(37)；theoretical(32)；experimental(26)；normal(26)；longitudinal(22)；gradient(21)；tangential(20)；boundary(20)；elastic(18)；directional(18)；high(14)；nodal(14)；periodic(14)；incident(11)；couplant(10)；continuous(10)
- 高频副词/连接副词：therefore(9)；approximately(6)；consequently(6)；fundamentally(6)；obliquely(6)；however(5)；purely(5)；weakly(4)；notably(4)；significantly(4)；inherently(4)；moreover(3)；effectively(3)；inversely(3)；mathematically(3)；perfectly(3)
- 高频二词短语：shear wave(15)；phase gradient(14)；plane stress(13)；wave excitation(12)；normal displacement(11)；shear waves(10)；longitudinal waves(10)；boundary conditions(10)；standing wave(8)；tangential displacement(8)；surface wave(8)；wave field(8)；phase distribution(7)；rayleigh wave(7)；periodic boundary(7)；unit spacing(7)
- 高频三词短语：shear wave excitation(7)；obliquely incident wave(6)；writing review editing(6)；spacing phase gradient(5)；tangential displacement vanishes(4)；any tangential traction(4)；plane stress plane(4)；stress plane strain(4)；periodic boundary conditions(4)；shear wave beam(4)；normal surface contact(3)；surface contact eliminating(3)

**主动、被动与句法**

- 被动语态估计次数：120
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：793
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：198
- 一般过去时线索：35
- 现在完成时线索：2
- 情态动词线索：38
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：wave(5)；excitation(4)；shear(4)；tangential(4)；couplant-free(3)；china(3)；nodes(3)；phase(3)
- 1. Introduction：wave(14)；shear(10)；surface(9)；excitation(8)；tangential(8)；scanning(7)；displacement(7)；mode(6)
- 2. The normal-encoding principle: standing wave nodal excitation and its theoretical foundation：surface(3)；wave(3)；normal-encoding(2)；waves(2)；normal(2)；introduce(1)；theoretically(1)；validate(1)
- 2.1. SV-Rayleigh wave interference theory：wave(42)；surface(19)；displacement(15)；boundary(12)；nodal(10)；half-space(9)；periodic(9)；plane(9)
- 3. Design and parameter analysis of meta-exciter via FEM simulations：model(3)；waves(3)；wave(2)；excited(2)；pwe(2)；design(2)；framework(2)；meta-exciter(2)
- 3.1. Meta-exciter for unidirectional and high-purity SV wave：waves(15)；wave(14)；excitation(12)；region(10)；surface(8)；phase(7)；longitudinal(7)；unit(5)
- 3.2. SV wave meta-exciter optimization：wave(20)；waves(11)；excitation(10)；region(9)；regions(9)；beam(7)；phase(6)；angle(6)
- 4. Experimental validation：shear(12)；metasurface(10)；wave(10)；waves(7)；displacement(7)；phase(6)；substrate(6)；interface(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
`Traditional X faces a fundamental trade-off: A requires B, limiting C.`

### 14.2 方法与框架表达
`This work proposes a Y paradigm that enables A using only B.`

### 14.3 结果与趋势表达
`Finite-element simulations indicate an energy proportion exceeding X%; experiments demonstrate beam steering within Y.`

### 14.4 机制解释表达
`At these nodes, tangential displacement vanishes while normal displacement exhibits a prescribed phase distribution.`

### 14.5 贡献与意义表达
`This shifts excitation from tangential-pushing to normal-encoding.`

### 14.6 局限与未来工作表达
`While the proof-of-concept demonstrates the core mechanism, engineering applications require systematic investigation of practical coupling methods.`

## 15. 引用策略与文献使用
引用集中在 Introduction，用 NDT/医学文献证明 SV 波重要性，用压电/EMAT/laser/phased array 文献建立 trade-off，用 metasurface 文献铺垫波前调控。理论和结果部分主要依赖本文推导和仿真。风险是若已有 dry-contact shear source 或法向激发技术，作者必须突出“standing-node phase encoding + high-purity directional SV”的组合新意。

## 16. 审稿人视角风险
最大攻击面是实验尚未实现真正独立相控法向源阵列；monolithic metasurface 可能仍引入界面剪切。第二，proof-of-concept 在 1 mm 铝板上完成，复杂层状介质、厚板、曲面和真实缺陷检测未验证。第三，摘要中 “eliminating tangential stress transmission” 与正文中 perfect-bond/weak-bond、interface shear 的讨论要保持措辞一致。Fig. 10-11 必须结合 PDF 核查波束清晰度和杂散波。

## 17. 可复用资产
- 选题角度：把工程 trade-off 表述为边界条件矛盾，再提出新的编码自由度。
- 论证链：物理节点原理 -> 解析逆设计 -> FEM 优化 -> 实验 FFT。
- 图表设计：概念对比图非常关键。
- 句型骨架：`shifting from A to B`, `using only normal surface contact`, `analytical relation linking X to Y`。
- 不宜直接模仿：应用外推不能超过实验边界。

## 18. 对我写论文的启发
本文示范了如何把装置创新前移成物理原则创新。写类似论文时，Introduction 要先讲无法同时满足的 trade-off；Method 要给出可逆设计关系；Results 中仿真和实验指标要互补，仿真证明纯度上限，实验证明核心机制可实现。

## 19. 最终浓缩
最值得学：将剪切波激发从切向应力传递改写为法向相位编码，是清晰的边界条件范式转换。最大风险：真正 dry-contact、可编程和复杂介质应用尚未闭环。三个可迁移动作：用 trade-off 定义问题；用概念图表达范式转换；用解析关系、FEM、实验三层证据支撑 claim。

补充写作素材库：本文的词汇系统非常适合工程方法论文迁移。问题词包括 fundamental trade-off、modal purity、scanning flexibility、throughput bottleneck、multimodal interference、spherical spreading、signal-to-noise ratio。方法词包括 normal-encoding paradigm、standing wave nodes、phase-gradient metasurface、normally oriented point-source array、plane wave expansion、finite structure model、PML boundary。性能词包括 SV energy proportion、beam steering、radiation angle deviation、dominant energy direction、frequency concentration。局限词包括 proof-of-concept validation、monolithic metasurface、independent phase control、practical coupling methods、homogeneous or weakly stratified media。

可迁移段落 1：如果写一个工程瓶颈型 Introduction，可以采用本文的三段式。第一段先说明目标波/目标功能的不可替代价值，例如“SV 波对剪切模量敏感、波长短、适合缺陷检测”。第二段制造 trade-off：“高性能方案需要某种苛刻边界条件，而该条件破坏目标应用场景。”第三段引入新平台：“超表面提供波前设计自由度，但已有工作尚未在源端解除边界条件矛盾。”这种写法比直接说“本文提出一种新装置”更有说服力。

可迁移段落 2：方法段的关键是把装置功能还原为物理原则。本文不是先画 metasurface 单元，而是先说节点处 tangential displacement vanishes、normal displacement carries phase。这个顺序值得模仿：先证明边界条件中存在未被利用的自由度，再把结构设计描述为该自由度的实现。这样即使具体装置未来改变，principle 仍然站得住。

可迁移段落 3：实验段的误差解释很有价值。作者没有只报“实验符合仿真”，而是解释 measured wavelength 与理论值差异来自扫描分辨率、峰间距测量和 spurious components。可迁移骨架是：“The discrepancy is mainly due to A. Specifically, B introduces measurement errors; additionally, C contributes to inaccuracy. These factors reasonably account for the observed difference.” 这能避免审稿人把小误差放大成机制失败。

可迁移段落 4：应用展望的边界控制也值得学。作者把 NDT、complex structures 和 elastography 都列为潜力，但又承认 layered structures 会引入额外波现象，dry-contact engineering 还需 magnetic attraction、vacuum chucking 或 elastomer layers。应用论文最怕“实验小、愿景大”，本文通过 proof-of-concept 和 future practical coupling methods 把愿景落回可执行路线。

图表写法补充：Fig. 1 承担“范式转换”；Fig. 2-3 承担“理论可行”；Fig. 5-8 承担“仿真性能”；Fig. 10-11 承担“实验验证”。如果模仿，可避免每张图都只展示结果，而应让每张图对应一个审稿问题：为什么需要？为什么可行？性能多好？实验是否成立？误差在哪里？

审稿回复策略：若审稿人质疑实验并非真正 dry contact，可承认当前实验是 normal-encoding principle 的 proof-of-concept，而非最终工程封装；随后指出 weak-bond/perfect-bond 对比显示界面 shear strain 只起次要作用，核心方向性来自相位编码。若审稿人质疑 1 mm 铝板太理想，可强调理论关系在 half-space、plane stress、plane strain 中通过替换波速保持适用，但复杂层状结构确需未来纳入 mode conversion 和 dispersion。若审稿人质疑 SV purity，可把 FEM 的 mode proportion、time-domain wavefield 和 FFT direction 作为三重证据，而不只依赖单张波场图。

模板化句群：`The proposed mechanism does not rely on shear-stiff coupling at the interface; instead, it encodes the desired shear-wave phase through the normal displacement component at interference nodes.` 这句话可迁移到所有“用非传统边界自由度实现目标模态”的论文。`The current implementation validates the physical principle, while future programmable arrays will address practical deployment.` 这句话可用于 proof-of-concept 到 engineering prototype 的过渡。

最终使用提醒：这篇最适合沉淀到“工程 trade-off 破解模板”。它的真正亮点不是装置形状，而是把原先必须依赖切向耦合的功能改成法向边界编码。以后遇到类似问题，可优先问：目标功能是否真的需要传统输入通道？是否存在另一个边界自由度可以编码同一物理量？这类问题往往能生成强 Introduction 和强概念图。

入库标签：工程 trade-off；边界条件重写；法向编码；源端超表面；proof-of-concept 到工程封装。

进一步可迁移提醒：若未来写类似 NDT/波动控制论文，最好同时准备“性能指标图”和“误差来源段”。性能指标图回答能否工作，误差来源段回答为什么没有完全理想。二者组合能显著降低实验型审稿风险。

补充标签：相位梯度；法向接触；剪切波纯化；在线检测。

最后备注：适合与超声检测、声弹性、柔性传感论文互相对照。

可入库。

补充：可作为“源端机制创新”的案例，后续主线程可与其他 metasurface 论文横向比较。
