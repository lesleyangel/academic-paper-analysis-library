# Correlating dislocation waviness and strength with compositional heterogeneity via continuous dislocation dynamics with sub-core resolution

## 0. 读取说明
- 源 PDF：`jmps/文献/Correlating-dislocation-waviness-and-strength-with-co_2026_Journal-of-the-Me.pdf`
- 源 TXT：`jmps/文本/txt/Correlating-dislocation-waviness-and-strength-with-co_2026_Journal-of-the-Me.txt`
- 图像核查：txt 可读摘要、章节、正文和图题，但 Fig. 2-15 的颜色场、散点云和曲线形态需结合 PDF 图像核查。
- 论文类型：计算/理论方法论文，目标是在亚位错芯分辨率下解释 CCA 中 SFE 波动、位错波状化和 CRSS 增强之间的联系。

## 1. 基本信息与论文身份
- 作者：Mengzhen Cao, Yuqi Zhang, David J. Srolovitz, Alfonso H.W. Ngan。
- 期刊/年份：Journal of the Mechanics and Physics of Solids, 214, 2026, 106686。
- DOI：10.1016/j.jmps.2026.106686。
- 关键词：continuous dislocation dynamics；dislocation core；Peierls-Nabarro model；critical resolved shear stress；machine-learning molecular dynamics。
- 研究对象：复杂浓缩合金中由 fluctuating stacking fault energy landscape 诱导的 wavy dislocations。
- 方法类型：intensive CDD + P-N 位错芯描述 + 空间变化的 core-width landscape + 理想/随机景观参数扫描 + ML-MD 特征验证。
- 证据类型：方程推导、数值模拟、参数扫描、随机 rough surface、CRSS 统计、机器学习特征重要性。
- JMPS 定位：强机制建模论文，贡献不只是“模拟更细”，而是提出 `∂2γusf/∂y∂x` 作为形态与强度的统一控制量。

## 2. 摘要与核心信息提取
摘要按“现象已知但方法不足 -> 新框架 -> 参数化发现 -> 统一机制因子 -> 工具意义”推进。核心问题是 CCA 中 dislocations 会因 SFE 起伏产生波状形态并提高滑移阻力，但显式解析位错芯的动态模拟很少。作者提出 intensive CDD，把 P-N 型 core representation 和 chemical heterogeneity 放进同一框架。关键发现分三层：fluctuation amplitude 同时放大 waviness 与 CRSS；correlation length 存在临界峰值，因为位错芯应力会屏蔽过高频的 SFE variance；单向/理想景观揭示 `∂w/∂x` 及其沿位错线方向的变化是局部 curvature 的来源，最终收束到 `∂2γusf/∂y∂x`。
- 一句话主张：通过把 SFE 起伏映射为空间变化的位错芯宽度 `w`，intensive CDD 揭示了 CCA 中位错波状化和 intrinsic strengthening 的共同几何-能量控制量。
- 核心关键词：sub-core resolution；w landscape；SFE heterogeneity；CRSS；cross derivative；core shielding。
- 摘要写法可学处：把“随机化学环境”降解为可操控场变量，再用一个可计算指标重写复杂机制。

## 3. 选题层深拆
问题来源于 CCA/HEA 强化机制中的一个典型矛盾：MD 能看到位错在化学非均匀场中弯曲、迟滞和强化，但 MD 昂贵且不便任意控制 SFE 景观；DDD 把位错当奇异线，PFDD 常假定刚性芯或 quasi-static 能量最小化，都难以把 core structure evolution 本身纳入动态解释。本文把大问题缩窄为：若将 slip plane 上的 SFE 波动抽象成 `w(x,y)`，位错线形、局部速度差和 CRSS 如何响应？

选题价值在两个层面成立。材料层面，它回应 CCA 中 SRO/SFE fluctuation 与 strengthening 的机制争议；方法层面，它在 MD 和传统介观位错模型之间提供透明的可控模拟平台。边界也清楚：作者不声称模拟具体某一合金，而是研究 `γ0, Δγ, λ, ∂w/∂x, ∂2γusf/∂y∂x` 等统计/微分特征如何支配位错行为。

## 4. 领域位置与文献版图
作者把已有研究放在四条线上：CDD/DDD/PFDD 等位错模拟；Peierls-Nabarro 和 γ surface 位错芯理论；CCA/SRO 强化的 MD 或 atomistic studies；机器学习解释 MD 数据。CDD 能处理连续密度，但传统 interest 多在 extensive scale；P-N 能解析 core spreading 和 lattice misfit，但 γ surface 获取昂贵；DDD/PFDD/MD 都能解释部分现象，却在“显式位错芯 + 可控异质景观 + 动态滑移”三者上不同时满足。

本文站位是 P-N core physics、CDD dynamics 和 CCA heterogeneity 的交叉点。与前人相比，最关键差异是把 core-shielding factor 中的 `w` 从常数扩展为二维空间函数，使 dislocation line shape 与 core width 沿 slip plane 同时响应。

## 5. Gap 制造机制
- 显式 gap：缺少能在 sub-core resolution 下模拟 chemical heterogeneity 中 wavy dislocations 并直接关联 SFE statistics 与 CRSS 的模型。
- 隐含 gap：CCA 强化讨论常以“随机能量景观阻碍滑移”概括，但缺少能解释局部曲率和全局阻力的具体场特征。
- Gap 类型：方法 gap + 机制 gap + 尺度桥接 gap。
- Gap 证据：Introduction 对 CDD、P-N、γ surface、MD、DDD/PFDD 的综述；Discussion 对 DDD/PFDD/MD 的能力比较。
- 审稿追问：`w` 与真实 γ surface 的映射是否唯一？未指定具体材料时能否称为 CCA strengthening？ML-MD 数据是否足以验证因果而非相关？

## 6. 创新性判断
作者声称的贡献包括：提出 intensive CDD；通过 spatially varying `w` 纳入 SFE heterogeneity；揭示 amplitude/correlation length 对 waviness 和 CRSS 的竞争作用；发现 `∂2γusf/∂y∂x` 作为统一控制因子；用 ML-MD 分析确认该特征的重要性。真实创新强度中高：模型上是 CDD/P-N 的二维异质扩展，机制上则把“局部 SFE 波动”精炼成可微分、可统计、可预测的指标。最易被挑战的是 semi-phenomenological core-shielding 机制和未纳入 dynamic SRO、diffuse APB、edge/screw 差异、cross-slip/twinning 等真实材料细节。

## 7. 论证链条复原
背景：CCA 中化学/SFE 波动引发 wavy glide 和强化。  
文献：CDD、P-N、MD、DDD/PFDD 各有能力但不能同时解析动态位错芯和可控 2D 异质景观。  
Gap：缺少 transparent model 来拆分 SFE landscape 的统计/局部特征。  
方法：构建 intensive CDD，校准 `γusf-w` 关系，生成 idealized、unidirectional、random landscapes，统计 equilibrium shape 与 CRSS，并用 MD-ML 验证。  
证据：Fig. 2-3 建立芯结构与 γ surface 映射；Fig. 5-8 显示 waviness；Fig. 9-12 显示 CRSS；Fig. 13-15 收束到 cross derivative。  
结论：amplitude 增强 waviness/CRSS，correlation length 有峰值，`∂w/∂x` 控制一维阻力，`∂2γusf/∂y∂x` 统一解释二维线形和强度。

## 8. 方法/理论/模型细拆
方法总框架以 Nye/GND density tensor 的动态演化描述亚芯尺度位错内容，再用 P-N 型 lattice misfit 与 elastic interaction 的平衡控制 core spreading。core-shielding factor 中的 `w` 与 `n` 控制位错芯宽度和 dissociation tendency；当 `w` 变成 `w(x,y)` 时，SFE 起伏就以模型参数场形式进入 lattice misfit stress。

关键变量包括 `w0, A, n, γusf, γssf, λ, Δγ, ∂w/∂x, ∂2γusf/∂y∂x, CRSS`。方法步骤是：均匀芯结构复现 -> 建立 `γusf-w` 反向关系 -> 构造正弦/线性/随机景观 -> 求 equilibrium density fields 和 Fourier-fitted line coordinates -> 施加应力得到 CRSS -> 用局部景观特征和 ML 分析解释结果。关键假设是 `w` 可代理局部 SFE 对位错芯的主效应，随机景观的均值/幅值/相关长度可概括 SRO 的一阶影响。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| intensive CDD 能合并 P-N 位错芯、动态位错和化学非均匀性 | 摘要、4.1 | Fig. 1 流程、方法方程、Fig. 2 芯结构 | 模型构建 | 强 | 与真实 γ surface 的映射半现象 |
| `w` 与 `γusf` 的关系可用于引入 SFE 起伏 | 3.1、结论(1) | Fig. 2-3 γ surface 与拟合 | 数值拟合 | 中强 | 材料/弛豫方案可能改变关系 |
| 波动幅值增加会增强 waviness 和 CRSS | 3.2-3.3 | Fig. 5-6、Fig. 9、Fig. 12 | 参数扫描 | 强 | 极端波动受数值稳定性限制 |
| correlation length 存在使 CRSS 峰值化的临界区 | 摘要、3.3 | random landscapes 与 CRSS statistics | 统计模拟 | 中强 | λ 需真实 SRO 校准 |
| `∂w/∂x` 在一维景观中主导 CRSS | 3.3.1 | Fig. 10-11 | 受控数值实验 | 强 | 一维结论向二维推广需谨慎 |
| `∂2γusf/∂y∂x` 关联 waviness 与 CRSS | 3.4、结论(4) | Fig. 13-15、ML-MD | 机制+外部验证 | 中强 | 相关与因果边界需说明 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | intensive CDD 流程 | 方法框架成立 | 给出初始化、景观和求解逻辑 | 是 |
| Fig. 2 | 均匀位错芯和 γ surface | `w/n` 控制 core structure | 建立物理可信度 | 是 |
| Fig. 3 | `γusf-w` 拟合与 w landscape | SFE 到参数场桥接 | 使异质性可操控 | 是 |
| Fig. 4-8 | 位错密度/线形随景观变化 | landscape 改变 waviness | 形态证据 | 是 |
| Fig. 9-12 | CRSS 与 w、λ、位置关系 | landscape 控制强度 | 强度证据 | 是 |
| Fig. 13 | w、γusf、交叉导数场 | 机制指标 | 把局部曲率可视化 | 是 |
| Fig. 14-15 | 特征预测、相关散点 | 统一指标 | 收束全文主张 | 是 |
| 演化方程 | density tensor dynamics | CDD 物理基础 | 避免经验拟合 | 否 |

## 11. 章节结构与篇章布局
Introduction 从 CDD 尺度讲到 P-N 位错芯，再进入 CCA/SRO 的 SFE 起伏，最后提出方法断层。Methods 以 intensive CDD、chemical heterogeneity、numerical scheme 三段组织。Results 的顺序非常值得学习：先均匀芯校准，再理想 landscape，再随机 landscape，再 CRSS，最后统一控制因子。Discussion 先讲 novelties，再讲 limitations and future prospect，主动限定半现象性、材料未指定和数值稳定性。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Correlating-dislocation-waviness-and-strength-with-co_2026_Journal-of-the-Me.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：18
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Intensive continuous dislocation dynamics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Effects of chemical heterogeneity | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Numerical scheme and simulation settings | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Equilibrium dislocation core shape | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Dislocation line configuration | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2.1 Idealized landscapes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2.2 Random landscapes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Critical resolved shear stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3.1 Idealized landscapes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3.2 Random landscapes | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Underlying factor governing dislocation waviness and strength | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 的段落功能是“工具谱系 -> 物理瓶颈 -> 材料现象 -> 本文变量”。Results 段落通常先说明景观设置，再报告趋势，最后给机制解释。Discussion 段落的亮点是与 DDD/PFDD/MD 逐一比较：DDD 缺显式芯，PFDD 偏 quasi-static，MD 透明度和可控性不足；因此本文的新意来自结构性能力差异，而非单纯精度宣称。

## 13. 文笔画像与语言习惯
整体语气技术密集、机制导向。强 claim 词包括 `reveals`, `unveiling`, `governing`, `dominant`; 局限部分则用 `may`, `could`, `depending on`, `for now` 降低外推。常用问题表达是 “limited to very few approaches”；贡献表达是 “merge A, B and C in one framework”；机制表达是 “originate from”, “boil down to”, “dominant role”。中文写作可学其“强机制 + 强边界”的搭配。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：dislocation(297)；crss(99)；core(86)；usf(80)；dislocations(66)；sfe(59)；landscape(55)；waviness(54)；line(53)；landscapes(50)；cdd(47)；stress(44)；local(43)；slip(38)；ccas(37)；random(37)；density(36)；along(34)；sro(33)；fluctuation(31)
- 高频学术名词：dislocation(297)；waviness(54)；stress(44)；simulation(40)；density(36)；fluctuation(31)；equation(30)；structure(30)；direction(30)；energy(28)；relation(26)；correlation(25)；velocity(24)；heterogeneity(23)；model(19)；position(18)
- 高频学术动词：shown(15)；indicate(5)；revealed(4)；demonstrated(4)；compared(3)；shows(3)；simulated(3)；suggest(2)；capture(2)；proposed(2)；evaluate(2)；derived(2)；indicates(2)；predicted(2)；investigated(2)；validated(1)
- 高频形容词：local(86)；elastic(34)；critical(30)；intensive(30)；different(26)；gradient(23)；numerical(20)；present(18)；chemical(13)；sinusoidal(13)；homogeneous(12)；intrinsic(12)；positive(12)；periodic(12)；previous(12)；dynamic(10)
- 高频副词/连接副词：respectively(13)；therefore(10)；purely(10)；essentially(9)；especially(7)；moreover(6)；furthermore(5)；however(5)；effectively(5)；generally(4)；consequently(4)；namely(4)；accordingly(4)；arbitrarily(3)；wiggly(3)；directly(3)
- 高频二词短语：dislocation core(54)；dislocation line(37)；dislocation waviness(29)；slip plane(27)；intensive cdd(23)；along dislocation(22)；core width(18)；dislocation density(17)；core structure(14)；equilibrium dislocation(14)；lattice misfit(13)；waviness crss(13)；dislocation velocity(13)；sfe landscape(12)；local dislocation(11)；zhang ngan(11)
- 高频三词短语：along dislocation line(14)；dislocation core width(12)；resolved shear stress(7)；dislocation core structure(7)；dislocation line direction(7)；stacking fault energy(6)；across slip plane(6)；dislocation waviness crss(6)；continuous dislocation dynamics(5)；lattice misfit stress(5)；equilibrium dislocation core(5)；dislocation core structures(5)

**主动、被动与句法**

- 被动语态估计次数：149
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：1426
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：269
- 一般过去时线索：52
- 现在完成时线索：7
- 情态动词线索：75
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：dislocation(13)；core(6)；dynamics(5)；sfe(4)；crss(4)；usf(4)；waviness(3)；heterogeneity(3)
- 1. Introduction：dislocation(51)；core(18)；dislocations(14)；ngan(14)；cdd(13)；ccas(13)；sfe(12)；zhang(10)
- 2. Methods：dislocation(37)；stress(13)；core(12)；direction(11)；line(9)；elastic(9)；landscape(9)；slip(8)
- 2.3. Numerical scheme and simulation settings：dislocation(17)；density(9)；flux(7)；stress(7)；kalaei(6)；pixel(6)；direction(6)；slip(5)
- 3. Results：无明显高频项
- 3.1. Equilibrium dislocation core shape：dislocation(15)；usf(14)；core(11)；dissociation(5)；relation(5)；equilibrium(4)；density(4)；stacking(4)
- 3.2. Dislocation line configuration：无明显高频项
- 3.2.1. Idealized landscapes：dislocation(35)；waviness(15)；line(8)；landscape(8)；valley(8)；positions(7)；usf(5)；equilibrated(5)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
`Although X has been observed in Y, simulative reproduction with explicit Z remains limited.`  
启发：不要只说研究少，要说“已观察到的现象缺少某种必要分辨率/自由度的复现”。

### 14.2 方法与框架表达
`Here, we devise a framework integrating A, B and C for dynamic simulation of D.`  
`The extension from a constant to a spatial function critically allows the framework to address heterogeneous systems.`

### 14.3 结果与趋势表达
`Results reveal that increased X amplifies both Y and Z, while Z peaks at a critical length scale due to competing effects.`

### 14.4 机制解释表达
`These scenarios lead to the emergence of variation in A along B as the driver of C.`

### 14.5 贡献与意义表达
`The framework serves as an analytical tool to unfold mechanisms overlooked in previous simulations.`

### 14.6 局限与未来工作表达
`The present semi-phenomenological mechanism suffices to capture A, nevertheless it falls short of representing B.`

## 15. 引用策略与文献使用
Introduction 高密度引用三类文献：CDD/DDD/PFDD 方法，P-N/γ surface 位错芯理论，CCA/SRO 强化和 MD 研究。经典文献服务于概念合法性，近年文献服务于前沿性和 gap。Discussion 的引用功能更强：逐类比较 DDD、PFDD、MD 的模型边界。风险是若审稿人认为已有 PFDD 或 atomistic-informed DDD 已处理类似问题，作者必须强调“explicit core structure evolution under dynamic heterogeneous lattice misfit”的差异。

## 16. 审稿人视角风险
最大攻击面是 `w` landscape 对真实 SRO 的简化。作者已承认 dynamic SRO creation/destruction、diffuse APB、edge/screw 差异、cross-slip/twinning/martensitic transformation 未纳入。第二个风险是数值稳定性：高频/强波动下 divergence-free condition 和 core integrity 可能受有限差分误差影响。第三个风险是 ML-MD 只能增强相关性证据，未必完全证明因果。

## 17. 可复用资产
- 选题角度：把复杂材料随机异质性转写成可控统计场，再寻找统一微分指标。
- 论证链：均匀校准 -> 理想景观 -> 随机景观 -> CRSS 统计 -> 统一控制量 -> 外部数据验证。
- 图表设计：示意流程、参数扫图、散点/ML 重要性图逐层收束。
- 段落模板：已有方法各自能做什么 -> 结构性缺什么 -> 本文框架如何补上。
- 不宜直接模仿：没有材料级校准时，不宜过度使用 `governing intrinsic strengthening`。

## 18. 对我写论文的启发
写类似论文时，方法创新要找到一个可操控变量，如本文的 `w(x,y)`，而不是只说模型更细。结果设计应先用理想化场拆因果，再用随机场证明稳健性。Discussion 应主动列出真实材料中未纳入的机制，这能提高而不是削弱模型可信度。

## 19. 最终浓缩
最值得学：用亚芯 CDD 把 CCA 中难解释的波状位错与强化转化为可参数化、可微分、可统计的景观问题。最大风险：`w/SFE` 映射和 SRO 简化不足以代表具体合金。三个可迁移动作：构造可控代理场；用理想场拆因果、随机场验稳健；在讨论中明确材料校准和未来扩展路径。

补充写作素材库：本文可迁移的关键词组可以分为四组。对象词包括 heterogeneous slip plane、dislocation core structure、SFE landscape、random rough surface、short-range order；方法词包括 intensive CDD、core-shielding factor、FFT-enabled correlation、Fourier-fitted line coordinates、machine-learning analysis；机制词包括 core stress shielding、velocity gradient、local curvature、intrinsic strengthening、competing fluctuation effects；边界词包括 semi-phenomenological、no specific material assigned、dynamic SRO creation/destruction、numerical stability、material calibration。若用于自己的论文，可把这些词组改写成“异质场 -> 可控参数 -> 局部梯度 -> 全局性能”的叙事模板。

可迁移段落 1：背景段可写成“在复杂材料中，宏观性能常由局部能量景观的统计起伏控制；然而，直接原子模拟难以系统改变景观的均值、幅值和相关长度，而传统介观模型又缺少显式缺陷芯结构。因此，需要一个能在中尺度上保留核心物理、同时允许景观可控变化的模型。”这个骨架适合位错、相界、裂纹、孪晶和界面迁移问题。

可迁移段落 2：结果段可写成“理想化景观用于隔离单一变量的因果效应，随机景观用于检验该效应在复杂统计条件下是否仍然成立。前者解释为什么，后者解释是否稳健。”本文的 Results 正是这样安排：从 sinusoidal/linear landscape 到 random landscape，再到 ML-MD 验证，避免直接在随机系统里寻找机制导致解释混乱。

可迁移段落 3：局限段可学习其分层方式。第一层承认代理变量的物理不完整性；第二层说明具体材料应用需要 atomistic calibration；第三层指出数值格式的稳定性边界；第四层提出未来可扩展现象，如 dynamic SRO、cross-slip、twinning。这样的局限不是泛泛说“未来需更多研究”，而是把模型缺口转化为下一轮研究路线图。

审稿回复策略：若被质疑“`∂2γusf/∂y∂x` 只是相关指标”，可用本文式回答：理想化景观提供因果拆解，随机景观提供统计稳健性，MD-ML 提供外部一致性，三者共同支持该指标的机制意义，但仍不把它说成所有 CCA 强化的唯一来源。若被质疑没有具体材料，可强调本文目标是建立 mechanism-resolving analytical tool，具体 alloy application 需要后续从 atomistic simulation 提取 `γ0, Δγ, λ` 和 `w/n` 校准范围。

最终使用提醒：这篇最适合沉淀到“复杂能量景观论文模板”。不要只学习 CDD 细节，更要学习它如何把随机、不可控、原子级的 SRO 问题翻译成均值、幅值、相关长度和局部导数。真正可复用的是这个翻译动作。

入库标签：异质能量景观；亚芯分辨率；可控随机场；机制指标提炼；MD-介观桥接。

补充标签：SRO 代理建模；参数场机制化。
