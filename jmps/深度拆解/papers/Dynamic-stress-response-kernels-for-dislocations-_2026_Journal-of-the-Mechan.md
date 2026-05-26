# Dynamic stress response kernels for dislocations and cracks: Unified anisotropic Lagrangian formulation

## 0. 读取说明
- 源 PDF：`jmps/文献/Dynamic-stress-response-kernels-for-dislocations-_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/Dynamic-stress-response-kernels-for-dislocations-_2026_Journal-of-the-Mechan.txt`
- 辅助参考：上一轮标准拆解只用于核对主线，本稿重新依据全文、公式段和结论组织。
- 是否需要结合 PDF 图像核查：本文几乎无传统图像本体；重点需核查 PDF 中公式编号、符号、上下标、附录 Fourier convention 和排版。
- 本文类型：理论推导论文；各向异性弹性动力中裂纹/位错动态应力响应核统一公式化。

## 1. 基本信息与论文身份
- 题名：Dynamic stress response kernels for dislocations and cracks: Unified anisotropic Lagrangian formulation
- 作者/机构：Yves-Patrick Pellegrini, Marc Josien, Martin Chassard；CEA、Universite Paris-Saclay、Ecole Nationale des Ponts et Chaussees。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213, 2026, Article 106601。
- DOI：10.1016/j.jmps.2026.106601
- 关键词：Elastodynamics；Dislocations；Cracks；Anisotropic elasticity；Stroh formalism。
- 研究对象：各向异性介质中平面裂纹/位错的动态 traction/resolved-stress convolution kernel、instantaneous radiative term、prelogarithmic Lagrangian factor。
- 方法类型：Stroh formalism；Fourier/Fourier-Laplace treatment；causal limiting absorption principle；generalized functions；Green function eigendecomposition；Lagrangian/reactive stress kernel relation。
- 证据类型：公式推导、对称性证明、各向同性/Weertman/Dynamic Peierls 特殊情形还原、辐射项系数推导、数值实现前景论证。
- JMPS 风格定位：受众窄但理论贡献强的解析力学论文，用一个核心函数 L(v) 统一裂纹和位错动态核。

## 2. 摘要与核心信息提取
摘要先指出 Geubelle-Rice crack model 和 Dynamic Peierls Equation for dislocations 中都有相同的 space-time stress-response kernel，已知 isotropic 表达但 anisotropic 未知。随后给出本文答案：用 Stroh formalism 推导，Fourier representation 完全依赖 prelogarithmic Lagrangian factor L(v)，space-time form 依赖 p(v)=L'(v)。同时处理 radiative losses、causality、subsonic/intersonic/supersonic，并给未来 Fourier-Laplace 数值实现铺路。

一句话主张：各向异性弹性中裂纹和位错的动态应力响应核可以统一写成由 Stroh formalism 给出的 L(v) 及其导数 p(v) 控制的 Lagrangian/causal stress kernel。

核心关键词：L(v)；p(v)=L'(v)；radiative term；causality；Stroh eigenvalues；anisotropic elastodynamics。

## 3. 选题层深拆
问题来源：高速位错/裂纹的 intersonic/supersonic 运动已被原子模拟和实验确认，动态辐射、mobility law、equation of motion 重新受到关注。但很多理论仍在 isotropic elasticity 中完成，而真实晶体、界面和裂纹/位错系统需要 anisotropic elasticity。

为什么重要：cohesive-zone crack models 和 generalized Peierls-Nabarro dislocation models 都需要同类 stress-response kernel。若 anisotropic kernel 缺失，FFT/Laplace 数值求解、辐射损失和高速缺陷动力学都会停留在各向同性近似。

为何现在值得做：causal Stroh formalism 已成熟；Pellegrini/Josien 的 isotropic Fourier-Laplace 动态 Peierls 框架提供数值目标；L(v) 的 analytic continuation 和 radiative imaginary part 需要澄清。

问题边界：线弹性各向异性、平面缺陷、in-plane stress、同材质 half-spaces；不处理温度、晶格色散、核心非线性、具体 cohesive law 或完整数值实现。

## 4. 领域位置与文献版图
作者先引用高速缺陷实验/原子模拟，建立 intersonic/supersonic 的现实性。随后回到经典各向异性位错/裂纹理论：Bacon、Bullough/Bilby、Teutonico、Weertman、Barnett-Lothe、Stroh、Ting 等。第三条线是 L(v) 的历史作用和 analytic continuation。第四条线是 cohesive-zone/phase-field/FFT-Laplace numerical models。

本文站位：补上 anisotropic stress-response kernel 的统一表达，使裂纹与位错两个模型共享同一数学对象。作者不是提供一个应用案例，而是提供后续模型的 kernel infrastructure。

文献姿态：继承经典 formalism，指出 isotropic known/aniso unknown 的理论缺口。

## 5. Gap 制造机制
显式 gap：动态应力响应核和 instantaneous radiative term 在 isotropic elasticity 中已知，在 anisotropic elasticity 中缺少统一空间-时间和 Fourier 表达。

隐含 gap：L(v) 虽长期被视为 energetic factor，但它的 imaginary part、causal continuation 和 stress response/radiative losses 的关系尚未完全澄清。

gap 类型：理论公式 gap + 因果/辐射解释 gap + 数值实现前置 gap。

gap 是否窄：很窄。作者限定 planar defects、in-plane stress、Stroh eigenproblem，并明确 nonlinear pull-back/cohesive term 不在本文范围。

审稿人追问：各向异性分支切割、复杂根、isolated velocity degeneracies、generalized functions 的处理是否严谨；未来数值实现是否真可行。

## 6. 创新性判断
作者声明贡献：用 Stroh formalism 推导 anisotropic traction/resolved-stress kernel；证明 Fourier 表达由 L(v) 控制，space-time 由 p(v) 控制；推导 anisotropic radiative coefficient；覆盖 subsonic/intersonic/supersonic；支撑 FFT-Fast inverse Laplace 实现。

真实创新：第一，把裂纹 opening 和 dislocation slip 的 plane-source kernel 统一。第二，通过 v=omega/k+i0+ 和 limiting absorption principle 明确因果性。第三，说明 Lagrangian kernel 是 reactive part of stress response，retarded stress kernel 可由 L(omega+i0+) 得到。第四，把 Weertman steady stress kernel 首次写成 L(v) 形式。

创新类型：理论统一创新。创新强度：高但受众专业。

易被挑战：推导可读性和符号复杂度；数值 cuts in complex plane 留待未来；没有算例图。

## 7. 论证链条复原
高速 planar cracks/dislocations 需要动态 kernel 描述波传播和辐射 -> isotropic kernel 已知但各向异性真实材料需要 aniso kernel -> 设定两个同材质 anisotropic half-spaces，plane interface 位移跳跃 eta、traction 连续 -> 对 in-plane coordinates 做 Fourier transform，不对 z 做 transform -> Navier equation 变成依赖 omega/k 的 Stroh eigenproblem，并用 i0+ 实现因果性 -> 得到 traction 与 displacement discontinuity 的 kernel L(hat k, omega/k) -> 证明频率/波矢反演对称性和 radiative-loss tensor coefficient -> 对 straight 1D defect 推出 Fourier form、steady state、isotropic-like form、space-time kernel p(v) -> 从 Green function 能量积分区分 reactive/radiative part，说明 kinetic/elastic energies 在辐射区单独病态但 Lagrangian 差值良好 -> Lagrangian kernel 等于 stress response reactive part，补充 causal continuation 即得 retarded stress kernel -> 结论指向 anisotropic FFT-Laplace numerical implementation。

薄弱环节：从公式到实际算法的 complex-plane cuts 和 mixed representation 尚未完成。

## 8. 方法/理论/模型细拆
几何与边界条件：两个 anisotropic half-spaces 由 z=0 plane 分开，plane 是 crack plane 或 dislocation glide plane。位移不连续 eta(r,t) 表示 crack opening 或 slip；traction 在界面连续。crack 的 cohesive stress 或 dislocation gamma-surface pull-back 不进入 kernel 推导。

Stroh 推导：对 r=(x,y) 和 t 做 Fourier transform，引入 in-plane wavevector k、director hat k、ratio v=omega/k+i0+。Stroh eigenvalues p_alpha 和 eigenvectors A_alpha/L_alpha 解 6x6 spectral problem。PLA 使 kernel analytic in upper half-plane，保证 causality 和 outgoing radiation。

核心对象：Fourier kernel L(hat k,v) 将 traction 和 eta 关联；straight defects 中 prelogarithmic Lagrangian factor L(v) 进入 steady stress 和 dynamic response；space-time kernel 用 p(v)=L'(v) 表达。

辐射与 Lagrangian：retarded Green function 的 radiative part 在 kinetic/elastic energy 中单独产生 distributional pathology，但在 Lagrangian K-S 中抵消。Lagrangian kernel等于 stress response 的 reactive part；用 L(omega+i0+) 可恢复 causal radiative stress。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| anisotropic traction/resolved-stress kernel 可由 Stroh formalism 得到 | Section 2 | half-space boundary problem、Stroh eigenproblem、Fourier kernel | 公式推导 | 强 | 退化速度态处理有限 |
| 因果性由 omega/k+i0+ 和 PLA 保证 | 2.2 | Paley-Wiener/Titchmarsh、outgoing radiation、Mach cones | 数学物理论证 | 强 | 分支选择复杂 |
| radiative-loss coefficient 可各向异性化 | 2.4 | k=0/|omega/k| -> infinity 极限 | 极限推导 | 中强 | 符号需核查 |
| straight defect steady stress 可写成 L(v) | 3.2 | Weertman model reformulation | 特殊情形还原 | 强 | 读者需跟公式 |
| space-time dynamic kernel 由 p(v)=L'(v) 控制 | 3.4 | Dynamic Peierls kernel 表达 | 公式推导 | 强 | generalized functions 门槛高 |
| Lagrangian kernel 与 reactive stress response 等价 | 4.3-4.4 | Green function energy integral，radiative singularity cancel，Eq. 76-79 | 理论统一 | 强 | 工程实现未展示 |
| 适合 FFT-Fast inverse Laplace 实现 | 5 | kernel 可在 Fourier grid/Laplace contours 预计算 | 实现前景 | 中 | cuts 数值重定义未完成 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需图像核查 |
| --- | --- | --- | --- | --- |
| Eq. 1-2 | 位移跳跃、traction 连续、Navier equation | 问题定义 | 统一 crack/dislocation | 公式核查 |
| Eq. 4-12 | Stroh eigenproblem 与 causal modes | kernel 推导 | 建立各向异性 formalism | 公式核查 |
| Section 2.3 | symmetry properties | kernel 可用性 | 保证数值/物理一致 | 公式核查 |
| Section 2.4 | radiative-loss coefficient | 辐射项 | 推导瞬时项 | 公式核查 |
| Eq. 35/48 等 | straight defect/L(v)/p(v) | 特殊情形还原 | 连接 DPE/Weertman | 公式核查 |
| Eq. 68-79 | energy/Lagrangian/stress response | reactive/radiative 关系 | 全文理论高潮 | 公式核查 |
| Appendices A-D | Fourier convention、eigenvalue perturbation、generalized functions | 严谨性 | 支撑主文推导 | PDF 核查 |

本文没有传统结果图；“结果”就是公式对象和等价关系。因此写作素材应重点学习符号导航和特殊情形还原。

## 11. 章节结构与篇章布局
Introduction：从高速缺陷现实需求切入，再定位 anisotropic kernel gap，最后逐节导读。Section 2：从一般 plane source 取 traction kernel，是全文最基础的推导。Section 3：收窄到 straight defects，给 steady state、isotropic-like form 和 space-time dynamic response。Section 4：从 Green function 和能量角度重新解释 L(v)、radiation 和 Lagrangian factor。Section 5：总结理论贡献、数值实现前景和未完成的 mixed representation。

最值得模仿：理论论文的章节不是按“方法/结果”传统格式，而是按“一般问题 -> 特殊情形 -> 物理解释”递进。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Dynamic-stress-response-kernels-for-dislocations-_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Traction and resolved-stress kernel from Stroh formalism | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Outline | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Two-dimensional in-plane derivation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Symmetry properties | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Straight defects (1D case): steady state and dynamics, in isotropic-like form | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 One-dimensional dynamic response in Fourier form, and prelogarithmic Lagrangian factor | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Steady state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Isotropic-like form | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Dynamical stress response in space-time form | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Prelogarithmic Lagrangian factor and radiation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.3 Integral form of kinetic and elastic energy densities | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.4 Lagrangian and stress response function | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.5 Prelogarithmic Lagrangian factor | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落功能：现实动机、各向异性必要性、L(v) 未解问题、本文贡献、应用目标、章节安排。推导段落节奏：先定义变量和空间，再说明物理意义，再给方程，再指出与经典情形的差别。Section 4 节奏：先暴露 kinetic/elastic energy 的病态，再说明 Lagrangian 差值消除病态，最后把它与 stress response 连接。

可复用段落模板：两个模型表面不同，但共享同一 kernel；已有 isotropic 表达成熟，而 anisotropic 中该对象未知；选择某成熟 formalism 后，先给一般 Fourier kernel，再通过特殊情形还原增强可信度。

## 13. 文笔画像与语言习惯
整体语气：高度技术化、精确、少修辞。作者不靠图像说服，而靠“known/unknown/derived/retrieved/explained”的公式链。

claim 强度：对推导结论强；对 numerical implementation 使用 well-suited、preliminary investigations indicate、falls outside scope。

问题表达：well-known for isotropic elasticity；for anisotropic elasticity they were unknown；needs further clarification；outside the scope。

贡献表达：we demonstrate；can be formulated exclusively in terms of；has been derived；physical origin clarified。

机制表达：radiative losses；causality constraint；reactive part；analytic continuation；prelogarithmic impulsion function。

限定表达：we do not further consider degeneracies；falls outside the present work；will be considered elsewhere。

写法特点：密集公式中穿插短解释句，保证读者知道每个对象的物理角色。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：pellegrini(38)；kernel(34)；stress(31)；function(30)；fourier(27)；plane(26)；response(23)；dislocations(23)；form(23)；radiative(22)；lagrangian(21)；equation(20)；anisotropic(19)；stroh(19)；dislocation(18)；functions(17)；section(16)；wave(15)；elasticity(15)；terms(15)
- 高频学术名词：equation(40)；stress(31)；function(30)；response(23)；dislocation(18)；section(16)；energy(15)；elasticity(15)；motion(15)；formalism(13)；model(11)；traction(11)；analysis(10)；condition(10)；velocity(10)；identity(10)
- 高频学术动词：derived(5)；formulated(2)；derive(2)；demonstrate(2)；shown(2)；solved(1)；evaluated(1)；proposed(1)；show(1)；shows(1)；solve(1)；indicate(1)
- 高频形容词：anisotropic(38)；elastic(28)；radiative(22)；real(14)；isotropic(13)；dynamic(12)；prelogarithmic(12)；supersonic(11)；numerical(10)；imaginary(10)；integral(10)；intersonic(9)；elastodynamic(8)；present(8)；reactive(7)；local(6)
- 高频副词/连接副词：consequently(8)；namely(5)；previously(5)；numerically(4)；respectively(4)；however(3)；exclusively(3)；vanishingly(3)；formally(3)；furthermore(2)；analytically(2)；therefore(2)；locally(2)；moreover(2)；fully(2)；precisely(2)
- 高频二词短语：stress response(11)；stroh formalism(11)；prelogarithmic lagrangian(10)；lagrangian factor(10)；isotropic elasticity(8)；complex plane(7)；green functions(7)；intersonic supersonic(6)；upper complex(6)；pellegrini josien(6)；stress kernel(6)；response function(6)；coe cients(6)；anisotropic elasticity(5)；equation motion(5)；wave speeds(5)
- 高频三词短语：prelogarithmic lagrangian factor(10)；upper complex plane(5)；stress response function(5)；intersonic supersonic regimes(4)；instantaneous radiative term(3)；continuation upper complex(3)；stress kernel weertman(3)；kernel weertman equation(3)；kinetic elastic energy(3)；elastic energy densities(3)；writing review editing(3)；review editing writing(3)

**主动、被动与句法**

- 被动语态估计次数：87
- `we + 动作动词` 主动句估计次数：6
- 名词化表达估计次数：574
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：143
- 一般过去时线索：20
- 现在完成时线索：18
- 情态动词线索：23
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：dislocations(5)；cracks(4)；anisotropic(4)；france(4)；cea(3)；elasticity(3)；dynamic(2)；stress(2)
- 1. Introduction：pellegrini(9)；dislocations(7)；radiative(7)；josien(6)；function(6)；stress(6)；section(6)；lagrangian(5)
- 2. Traction and resolved-stress kernel from Stroh formalism：无明显高频项
- 2.1. Outline：plane(6)；vector(4)；model(3)；material(3)；crack(3)；stress(3)；conditions(3)；dislocations(3)
- 2.2. Two-dimensional in-plane derivation：lothe(6)；plane(5)；matrix(5)；solutions(5)；one(5)；wave(4)；direction(4)；real(4)
- 2.3. Symmetry properties：limit(5)；tensor(4)；lim(4)；real(3)；wave(3)；pellegrini(3)；complex(2)；straightforward(2)
- 3. Straight defects (1D case): steady state and dynamics, in isotropic-like form：josien(3)；model(2)；weertman(2)；rosakis(2)；framework(1)；peierls-nabarro(1)；steady(1)；state(1)
- 3.1. One-dimensional dynamic response in Fourier form, and prelogarithmic Lagrangian factor：function(5)；kernel(3)；dislocation(3)；vector(3)；expression(3)；dislocations(3)；resolved(3)；stress(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：These objects are well-known for X; for Y they were unknown.
- 启发：理论 gap 可以非常直接，前提是对象足够具体。

### 14.2 方法与框架表达
- 骨架：We revisit the classical calculation using A while explicitly accounting for B.
- 启发：继承经典 formalism 时，强调新增处理点。

### 14.3 结果与趋势表达
- 骨架：The entire theory can be formulated exclusively in terms of X and its derivative.
- 启发：理论统一论文需要一个核心对象叙事。

### 14.4 机制解释表达
- 骨架：The causal stress-response kernel differs from the Lagrangian kernel only by its radiative part.
- 启发：把数学差异解释成物理部分的差异。

### 14.5 贡献与意义表达
- 骨架：This formulation lends itself naturally to future Fourier-Laplace implementations.
- 启发：纯理论论文也要说明下游可用性。

### 14.6 局限与未来工作表达
- 骨架：The numerical implementation details fall outside the scope of the present work and will be considered elsewhere.
- 启发：理论边界要明确，否则审稿人会要求算法。

## 15. 引用策略与文献使用
引用密度高，且经典文献占比大。高速缺陷实验/原子模拟用于说明问题现实性；Stroh/Barnett-Lothe/Ting/Mura/Willis/Weertman 等构成理论谱系；Geubelle-Rice、Dynamic Peierls、cohesive-zone/FFT/Laplace 文献说明本文 kernel 的应用场景。

引用姿态：继承和补全。作者没有批判前人，而是说各向同性成熟、各向异性缺口存在。经典文献用于合法性，近年文献用于说明高速缺陷和数值实现需求。

gap 与引用关系：通过“两个模型共享 kernel + isotropic known + anisotropic unknown”三步构建，引用不是罗列，而是围绕核心对象 L(v) 服务。

引用风险：若有近年 anisotropic cohesive-zone kernel 实现未覆盖，本文 novelty 会受影响；理论论文尤其需保证引用谱系完整。

## 16. 审稿人视角风险
- 最大攻击面：复杂根、branch cuts、isolated velocity states、non-semisimple Stroh matrix 的处理是否完整。
- 方法风险：generalized functions 和 radiative singularities 的处理需要极高严谨性。
- claim 风险：well-suited to numerical implementation 仍是前景，实际 cuts in complex plane 尚未实现。
- 范围风险：只处理线弹性、平面缺陷、同质 half-spaces，不含 core nonlinearity、temperature、lattice dispersion。
- 可读性风险：符号密度极高，若公式编号或符号不一致会严重影响说服。
- 图像核查：主要核查公式、附录和排版，不涉及视觉图像。

## 17. 可复用资产
- 选题角度：从两个物理模型共享同一数学核切入，做统一理论。
- gap 制造方式：已知 isotropic -> unknown anisotropic -> realistic applications require anisotropy。
- 论证链：一般边界问题 -> formalism 推导 -> 对称性/因果性 -> 特殊情形还原 -> 能量/Lagrangian 解释 -> 数值实现前景。
- 图表/公式设计：理论论文可无图，但必须有清晰符号、公式编号、附录 convention。
- 段落结构：每个推导段先给物理对象，再给数学定义，再说明与前人差异。
- 句型骨架：The apparent difference between A and B disappears once both are expressed in terms of the kernel X.
- 不宜模仿：若目标期刊/读者不是专业理论力学，过高符号密度会损害可读性。

## 18. 对我写论文的启发
第一，理论统一论文必须抓住一个“核心对象”。本文的 L(v) 和 p(v) 就是导航锚点，所有章节都围绕它们展开。第二，特殊情形还原非常重要：Weertman、Dynamic Peierls、isotropic-like form 都用来证明新公式不是孤立推导。第三，纯理论论文也要写清应用前景，但边界要守住：数值实现细节留给后续，就不能在正文中暗示已经完成。

可迁移到 Introduction：用“同一 kernel 出现在两个模型中”制造统一价值。可迁移到 Method：因果性和边界条件要在最前面说清。可迁移到 Conclusion：总结理论对象、应用前景和未完成的算法。

需要避免：符号未定义、公式编号混乱、把 future implementation 写成 already implemented。

## 19. 最终浓缩
最值得学习：用 L(v) 与 p(v) 两个核心函数统一 anisotropic cracks/dislocations 的动态 stress-response kernel，并解释辐射项和因果性。

最大风险：推导复杂且应用实现尚未展示，数值分支切割和 mixed representation 是后续关键。

三个可迁移动作：
1. 从多个模型共享的数学对象切入，建立统一理论贡献。
2. 用特殊情形还原增强可信度。
3. 明确区分本文完成的 kernel derivation 和未来要做的 numerical implementation。
