# Long-term irradiation transmutation promoted precipitation in tungsten: Multiscale models and new scaling law

## 0. 读取说明
- 源 PDF：`jmps/文献/Long-term-irradiation-transmutation-promoted-preci_2026_Journal-of-the-Mecha.pdf`
- 源 TXT：`jmps/文本/txt/Long-term-irradiation-transmutation-promoted-preci_2026_Journal-of-the-Mecha.txt`
- 是否需要结合 PDF 图像核查：需要。Re/缺陷场、微结构图、粗化指数拟合和机制谱需结合 PDF。
- 本文类型：辐照材料多尺度建模与尺度律论文。

## 1. 基本信息与论文身份
- 题名：Long-term irradiation transmutation promoted precipitation in tungsten: Multiscale models and new scaling law
- 作者/机构：Jia Chen, Aiya Cui, Yinan Cui；Tsinghua University。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106642。
- DOI：10.1016/j.jmps.2026.106642
- 关键词：Precipitation; Transmutation; Long-term irradiation; Kinetics; Multiscale
- 研究对象：中子辐照下钨中 Re 嬗变元素诱导 σ 相析出、点缺陷扩散和长时粗化。
- 研究尺度：MD 扩散、空间分辨 rate theory、相场微结构、年尺度辐照服役。
- 方法类型：phase-field、spatially-resolved rate theory、molecular dynamics diffusion coefficients、多尺度双向耦合、scaling law 拟合。
- 证据类型：解析应力验证、MD/文献扩散对比、Re/点缺陷分布实验对比、HFIR 微结构对比、粗化指数和机制图。
- 目标读者：核材料、相场、辐照缺陷动力学、多尺度模拟和材料性能退化读者。
- JMPS 风格定位：以长期服役问题为入口，用多尺度模型揭示机制并提出新尺度律。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先指出 transmutation-driven precipitate evolution 对长期辐照稳定性关键但少被量化；再提出 PF + SR rate theory + MD 的多尺度框架；随后说明模型与实验吻合；最后给出异质性成核、点缺陷加速和 n≈1.5 新粗化律。
- 背景句承担什么：把钨辐照嬗变与长期力学退化联系起来。
- gap 句承担什么：现有模型缺少 transmutation 与 displacement damage 的协同量化。
- 方法句承担什么：说明三个尺度模块及其耦合。
- 结果句承担什么：异质 Re 是成核前提，高密度缺陷加速扩散，嬗变率改变粗化机制。
- 意义句承担什么：为长期辐照材料性能理解和预测提供机制基础。
- 一句话主张：长时中子辐照下钨中析出由嬗变溶质持续注入与点缺陷增强扩散共同驱动，高嬗变率下粗化从经典 n=1/3 转向 n≈1.5 的溶质捕获-并合机制。
- 3-5 个核心关键词：transmutation; W-Re precipitation; phase-field; spatially-resolved rate theory; coarsening exponent。

## 3. 选题层深拆
- 问题来源：聚变/裂变环境下钨会产生 Re 等嬗变元素和辐照缺陷，导致 σ 相析出和微结构退化。
- 问题为什么重要：钨是聚变候选材料，析出和粗化会影响长期稳定性、脆化和机械性能。
- 问题为什么现在值得做：真实长时辐照实验昂贵且周期长，多尺度模型是预测服役行为的必要工具。
- 问题边界：聚焦 W-Re/σ 析出和点缺陷耦合；真实多元素和复杂缺陷谱仍被简化。
- 选题的 JMPS 味道：从服役问题出发，但落到可计算的微结构动力学和 scaling law。
- 选题可迁移性：适合迁移到其他长期不可直接实验的材料服役问题。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：钨辐照实验、W-Re 相图/σ 相、相场析出、rate theory 点缺陷、MD 扩散、Ostwald ripening。
- 主要研究流派/方法路线：实验表征、CALPHAD/热力学、相场微结构、缺陷动力学、MD 参数化、经典粗化理论。
- 每类研究解决了什么：实验提供现象和验证；相场给微结构演化；rate theory 给点缺陷浓度；MD 给扩散参数；粗化理论给基准指数。
- 每类研究留下什么不足：传统相场通常守恒组分；均匀 rate theory 无法解析局部缺陷；经典粗化律不含持续嬗变源。
- 本文站在哪条线上：相场析出和辐照缺陷动力学耦合，并用 MD 提供 diffusion input。
- 最接近前人工作：Cahn-Hilliard/Allen-Cahn 相场、SR rate theory、Hu/Lloyd 等 W-Re 辐照实验、LSW 粗化理论。
- 是否公平处理前人：整体是扩展式站位，承认经典理论并指出长时嬗变场景下机制改变。

## 5. Gap 制造机制
- 明示 gap：transmutation-driven precipitate evolution 对长期辐照稳定性关键，但在现有框架中很少被量化。
- 隐含 gap：如果不把 transmutation source 和点缺陷空间分布放进模型，就无法解释成核位置、加速动力学和异常粗化指数。
- gap 类型：多尺度耦合 gap、长时预测 gap、机制/尺度律 gap。
- gap 证据来自哪里：摘要、Nomenclature 后的 Introduction、模型验证和第 4 节参数研究。
- gap 是否足够窄：足够窄，限定在钨中 Re 嬗变诱导 σ 析出。
- gap 是否足够重要：重要，对聚变材料长期稳定性直接相关。
- 如果我是审稿人会如何追问：W-Re 简化能否代表真实多嬗变元素？n≈1.5 是否对源项、网格、初始波动和缺陷参数敏感？

## 6. 创新性判断
- 作者声称的贡献：发展 PF-SR rate-MD 多尺度框架；验证应力、扩散、缺陷和析出特征；揭示异质成核和点缺陷加速；提出嬗变率控制的新粗化律。
- 我判断的真实创新：把持续嬗变源项显式写入相场，并与空间分辨点缺陷动力学双向耦合，进而解释粗化指数从 1/3 到约 1.5。
- 创新类型：多尺度模型创新 + 机制发现 + 新 scaling law。
- 创新强度：高。
- 创新必要性：必要。无源项的守恒相场无法表示长期嬗变溶质增加。
- 创新与证据匹配度：模型验证链较完整；新尺度律仍需更多实验或独立模拟。
- 容易被挑战的创新点：新 scaling law 的普适性和高嬗变率现实性。

## 7. 论证链条复原
背景：钨长期辐照产生嬗变元素和点缺陷。文献：已有实验和模型分别处理析出、缺陷或扩散。gap：缺少 transmutation + displacement damage 的协同模型。问题：它们如何共同控制成核、增长和粗化？方法：phase-field + SR rate theory + MD diffusion + time-stepping coupling。证据：解析应力、实验 Re/缺陷/析出对比、参数研究。发现：Re 异质性成核，点缺陷加速扩散，高嬗变率改变粗化指数。机制：持续溶质注入 + 缺陷增强扩散 + cluster coalescence。意义：预测长期辐照微结构和性能退化。

## 8. 方法/理论/模型细拆
- 方法总框架：相场描述 BCC 基体到 σ precipitate 的 order parameter 和组分演化；SR rate theory 计算 vacancy/SIA 空间分布；MD 给出 W/Re 扩散参数；两模块通过缺陷增强扩散、析出 sink 和 cross-diffusion 双向耦合。
- 关键概念：transmutation source、σ precipitate、phase-field order parameter、SR rate theory、point defects、vacancy/SIA、coarsening exponent。
- 关键变量/参数：cRe、φj、cv、ci、transmutation rate、diffusion coefficient、precipitate radius、area fraction、density、scaling exponent n。
- 核心假设：Re 是主要嬗变溶质代表；源项可按给定速率注入；MD 扩散参数可传递到相场尺度。
- 边界条件：900°C HFR/HFIR 条件，不同 dpa/温度，不同 transmutation rates。
- 方法步骤：自由能和 mobility -> Cahn-Hilliard 源项 -> SR rate theory -> MD 扩散 -> 时间步耦合 -> 验证 -> 机制研究 -> 粗化指数。
- 复现信息：公式、参数表和图注较丰富；需核查 PDF 中 Table 1/2 和公式。
- 方法复杂度是否合理：合理，长期辐照本身是多尺度问题。
- 方法与 gap 的对应关系：相场管微结构，rate theory 管缺陷，MD 管扩散输入，source term 管嬗变。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 嬗变驱动析出需显式量化 | 摘要/导言 | 多尺度框架建立 | 问题+方法 | 强 | 真实多元素复杂性 |
| 模型能捕捉应力场、Re 分布和析出特征 | 第 3 节 | Fig. 5-7 与解析/实验对比 | 验证 | 强 | 实验数据有限 |
| Re 空间异质性是成核前提 | 4.1.1 | Fig. 8 HF/QH 对比 | 机制模拟 | 强 | 初始波动敏感 |
| 点缺陷高浓度显著加速析出 | 4.1.2 | Fig. 9 irradiation-enhanced vs equilibrium | 参数对照 | 强 | 缺陷参数不确定 |
| 嬗变率控制粗化机制 | 4.2 | Fig. 10-11 | 参数研究 | 强 | 高源项现实性 |
| 高嬗变率下出现 n≈1.5 新尺度律 | 摘要/4.2/结论 | log(r)-log(t) 斜率和机制谱 | 尺度律 | 中强 | 普适性需验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1/4 | 多尺度耦合框架与时间步策略 | 模型能处理 PF-rate 双向耦合 | 方法可信度 | 是 |
| Fig. 2-3 | 相变自由能和扩散参数 | 热力学与动力学输入 | 支撑模型参数 | 是 |
| Fig. 5-7 | 应力、缺陷/组分、实验微结构验证 | 模型预测可信 | 三层验证 | 是 |
| Fig. 8-9 | 异质性成核和点缺陷加速 | 机制来源 | 对照清晰 | 是 |
| Fig. 10-13 | 嬗变率、粗化指数和机制谱 | 新 scaling law | 核心贡献压缩 | 是 |
| 关键公式组 | Cahn-Hilliard/Allen-Cahn、source term、rate equations、diffusion mobility | 多尺度耦合 | 连接辐照源项与微结构 | 需核查公式排版 |

## 11. 章节结构与篇章布局
- Abstract：gap、框架、验证、机制、新尺度律。
- Introduction：聚变钨服役 -> 嬗变和位移损伤 -> 模型缺口。
- Related Work/Background：嵌入 Introduction。
- Method/Theory/Model：第 2 节按 basic framework、phase-field、SR rate、MD diffusion、implementation 展开。
- Results：第 3 节验证，第 4 节机制和新 scaling law。
- Discussion：与 Results 合并。
- Conclusion：列出四条关键发现。
- 章节之间如何过渡：先模型，再验证，再机制，再尺度律。
- 哪一节最值得模仿：4.2 Transmutation controlled new coarsening kinetics。
- 哪一节可能存在结构风险：模块多，读者需依赖框架图理解信息流。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Long-term-irradiation-transmutation-promoted-preci_2026_Journal-of-the-Mecha.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：22
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Precipitation model considering transmutation and displacement damage | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Basic framework | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Phase-field model for precipitation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.1 Basic formulations without transmutation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.2 Extension to transmutation-driven precipitation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Spatially-resolved rate theory for point defect kinetics | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.4 Determination of diffusion coefficients via molecular dynamics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.5 Numerical implementation and time-stepping strategy | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Model verification | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Stress field verification of spherical inclusion | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Verification of transmutation element and point defect distributions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Verification of precipitate features | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Precipitate evolution under neutron irradiation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：材料服役需求 -> 现有模型局限 -> 多尺度框架必要性。
- Method 段落推进：先总体，再逐模块，再耦合策略。
- Results 段落推进：先验证模型，再分析成核和扩散，最后提出粗化律。
- Discussion/Conclusion 段落推进：以 i)-iv) 方式压缩主要发现。
- 常见段落开头方式：`To disclose...`; `The model couples...`; `It is found that...`。
- 常见段落收束方式：以 mechanism 或 scaling exponent 收束。
- 可复用段落模板：`The transition from regime A to B is controlled by the increasing contribution of mechanism C.`

## 13. 文笔画像与语言习惯
- 整体语气：机制导向、模型密集、结果有强压缩。
- claim 强度：对模型机制较强，对长期性能用 deepen understanding 控制。
- 谨慎表达：available experimental data, direct validation limited 等。
- 问题表达：pivotal, rarely quantified, synergy of transmutation and displacement damage。
- 贡献表达：developed a novel multiscale framework。
- 机制表达：prerequisite, accelerate, controlled by, shifts from。
- 对比表达：classical Ostwald ripening vs new regime。
- 限定边界表达：specific irradiation conditions, available data。
- 术语密度：很高，集中在辐照、相场、缺陷。
- 长句/短句习惯：摘要长句压缩，结论条目清楚。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：precipitate(110)；transmutation(103)；diffusion(85)；concentration(84)；rate(79)；irradiation(68)；point(67)；cre(62)；evolution(58)；energy(53)；matrix(51)；model(50)；defect(48)；def(42)；precipitation(40)；coarsening(40)；theory(38)；nucleation(38)；high(36)；precipitates(35)
- 高频学术名词：transmutation(103)；concentration(84)；irradiation(68)；evolution(58)；energy(53)；model(50)；precipitation(40)；nucleation(38)；mechanism(36)；simulation(36)；condition(32)；field(32)；element(32)；system(30)；parameters(25)；conditions(24)
- 高频学术动词：simulated(17)；capture(10)；developed(9)；shows(7)；shown(6)；derived(6)；compared(5)；solved(4)；demonstrate(4)；indicate(4)；validate(3)；investigate(3)；simulate(3)；show(3)；indicates(3)；predicted(3)
- 高频形容词：experimental(44)；elastic(44)；local(40)；high(36)；critical(34)；element(32)；coefficient(26)；spatial(25)；thermodynamic(19)；classical(18)；exponent(18)；total(17)；microstructural(16)；atomic(15)；dynamic(14)；interstitial(14)
- 高频副词/连接副词：significantly(26)；approximately(22)；respectively(22)；consequently(14)；experimentally(8)；however(7)；directly(7)；fully(7)；notably(6)；therefore(6)；spatially(5)；accurately(5)；gradually(5)；strongly(4)；locally(4)；numerically(4)
- 高频二词短语：point defect(34)；transmutation rate(28)；rate theory(25)；point defects(25)；free energy(24)；diffusion coefficients(22)；transmutation element(21)；neutron irradiation(18)；cre cre(18)；matrix precipitate(17)；number density(16)；scaling exponent(15)；precipitate evolution(13)；diffusion coefficient(13)；phase-field model(13)；precipitate nucleation(12)
- 高频三词短语：matrix precipitate respectively(9)；gibbs free energy(9)；transmutation rate strans(7)；cre cre cre(7)；point defect concentration(7)；ele atom-def pair(6)；point defect concentrations(6)；spatially-resolved rate theory(5)；classical ostwald ripening(5)；def def vacancy(5)；def vacancy interstitial(5)；fraction number density(5)

**主动、被动与句法**

- 被动语态估计次数：182
- `we + 动作动词` 主动句估计次数：3
- 名词化表达估计次数：1397
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：313
- 一般过去时线索：80
- 现在完成时线索：6
- 情态动词线索：10
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：precipitate(19)；energy(19)；def(14)；ele(12)；free(10)；matrix(10)；rate(9)；coefficient(9)
- 1. Introduction：irradiation(14)；transmutation(11)；fusion(9)；point(8)；neutron(7)；damage(7)；high(6)；however(6)
- 2. Precipitation model considering transmutation and displacement damage：无明显高频项
- 2.1. Basic framework：model(10)；phase-field(7)；rate(6)；theory(6)；diffusion(6)；module(6)；point(6)；precipitate(6)
- 2.2.1. Basic formulations without transmutation：cre(31)；precipitate(20)；energy(20)；matrix(19)；free(15)；parameters(13)；strain(12)；phase(11)
- 2.2.2. Extension to transmutation-driven precipitation：diffusion(14)；def(11)；rate(9)；defect(8)；transmutation(7)；precipitate(7)；total(7)；point(7)
- 2.4. Determination of diffusion coefficients via molecular dynamics：diffusion(16)；atoms(8)；dele(7)；coefficients(7)；simulations(6)；atomic(5)；def(5)；sia(5)
- 2.5. Numerical implementation and time-stepping strategy：point(19)；defect(18)；def(11)；rate(10)；diffusion(10)；evolution(9)；cre(9)；phase-field(8)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：`X is pivotal to long-term Y, yet it has rarely been quantified within existing frameworks.`
- 启发：长期服役问题可用“重要但难以量化”开场。

### 14.2 方法与框架表达
- 骨架：`We developed a multiscale framework that couples A, B and C.`
- 启发：多尺度方法句要说明每个尺度模块。

### 14.3 结果与趋势表达
- 骨架：`Increasing P shifts the kinetics from regime A to regime B.`
- 启发：参数研究最好写成机制转变。

### 14.4 机制解释表达
- 骨架：`A is a prerequisite for B, while C accelerates D.`
- 启发：把成核和长大机制分开写。

### 14.5 贡献与意义表达
- 骨架：`These findings deepen our understanding of [material performance] over long timescales.`
- 启发：材料服役意义可强调 long timescales。

### 14.6 局限与未来工作表达
- 骨架：`Further validation is needed under [irradiation condition] and [alloy complexity].`
- 启发：局限应指向真实辐照条件和多元素复杂性。

## 15. 引用策略与文献使用
- 引用密度：Introduction、参数来源、验证和讨论处高。
- 引用主要集中位置：W-Re 实验、扩散数据、相场/粗化理论、辐照缺陷。
- 经典文献用途：Cahn-Hilliard、Allen-Cahn、Ostwald/LSW、CALPHAD。
- 近年文献用途：聚变钨、HFIR/HFR 实验、FISPACT 和最新核材料研究。
- 方法文献用途：phase-field、SR rate theory、MD potential 和 diffusion 参数。
- 对比/批判性引用：经典粗化律作为 n=1/3 基准。
- gap 如何靠引用搭建：从实验现象到模型不足，再到需耦合嬗变和缺陷。
- references 暗示的研究共同体：核材料、相场、MD、辐照缺陷、粗化理论。
- 引用风险：需覆盖 cluster dynamics 和更复杂 W-Re-Os 模型。

## 16. 审稿人视角风险
- 最大攻击面：n≈1.5 新尺度律的普适性。
- claim 是否过强：特定模型内强，普适材料规律需谨慎。
- 证据是否不足：高嬗变率长期实验验证有限。
- 方法是否可复现：参数多，需补充材料和表格。
- 对比是否充分：与经典粗化对比强，与其他辐照模型 benchmark 可加强。
- 边界条件是否清晰：条件列得较清楚。
- 替代解释是否排除：多缺陷 sink、多元素效应可能改变机制。
- 图表是否需要进一步核查：需要。

## 17. 可复用资产
- 可复用选题角度：长期不可直接实验的问题，用多尺度模型和有限实验验证切入。
- 可复用 gap 制造方式：`Existing models capture A or B separately, but not their synergy under C.`
- 可复用论证链：多尺度框架 -> 多角度验证 -> 机制对照 -> scaling law。
- 可复用图表设计：框架图、参数输入图、验证图、机制对照图、尺度律图。
- 可复用段落结构：每个机制都用对照实验/模拟证明。
- 可复用句型骨架：`The dominant mechanism shifts from M1 to M2 with increasing P.`
- 可复用引用组织：经典理论作为基线，最新实验作为验证。
- 不宜直接模仿之处：不要在缺少长时验证时声称普适 scaling law。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学：先验证模型，再提出新机制或新尺度律。
- 可迁移到 Introduction：把“长期服役难以实验”写成模型必要性。
- 可迁移到 Method：用框架图解释多模块耦合。
- 可迁移到 Results/Discussion：用机制谱压缩复杂参数研究。
- 需要避免的问题：参数太多时必须有清晰 sensitivity 或验证链。

## 19. 最终浓缩
- 这篇论文最值得学：多尺度模型如何服务一个可记忆的新 scaling law。
- 这篇论文最大风险：新粗化指数的普适性和实验验证不足。
- 三个可迁移动作：
  1. 用源项打破守恒模型，贴合真实服役环境。
  2. 用实验/解析/参数对照三层验证模型。
  3. 用机制谱把多个 regime 压缩成一张图。

最终判断：这篇论文最强资产是“多尺度耦合 -> 验证 -> 机制 -> 新尺度律”的闭环。

补充写作素材：本文的 Introduction 可以拆成一个很清楚的四步模板：第一步，说明材料服役场景的不可替代性；第二步，说明长期辐照会引入持续变化的内部源项；第三步，指出传统模型通常分别处理析出、缺陷和扩散；第四步，提出必须耦合 transmutation、point defects 和 precipitation。这个模板非常适合写核材料、腐蚀、老化、疲劳等长时过程论文。

Results 的最大可学之处是“验证和发现分开”。作者没有一开始就宣布新尺度律，而是先用应力场、扩散、实验微结构对模型做背书。只有模型可信之后，后面的机制对照和粗化指数才显得有分量。写类似论文时，可以把每个验证图的功能写在图题里：验证应力、验证组分、验证析出特征，而不是笼统叫 simulation results。

审稿人最可能追问 scaling law 的稳健性，因此后续若扩写，应增加三类防守：不同初始 Re fluctuation 的指数稳定性；不同网格/维度下的指数稳定性；不同 transmutation source 和 sink strength 下的 regime boundary。这样新指数就不只是某一次拟合，而更像机制区间。

可复用句型：`The classical coarsening law is recovered in the low-source regime, whereas sustained solute injection drives the system into a non-equilibrium regime characterized by...`。这个句型适合把经典理论和新机制放在同一个连续谱里。

进一步可学的是“把新规律放回经典规律旁边”。作者没有把 n≈1.5 写成孤立发现，而是先保留 n=1/3 的经典 Ostwald ripening 作为低源项基线，再引入 solute capture 的中间 regime，最后进入 solute injection + coalescence 的高源项 regime。这样新结论不是推翻经典理论，而是说明经典理论在某个条件下退化为更一般机制谱的一端。这个写法很适合高水平期刊，因为它既尊重已有理论，又能凸显新贡献。

图表叙事上，Fig. 13 的机制谱是全文“收口图”。如果写类似论文，建议最后一定做一张 regime map 或 mechanism spectrum，把前面分散的参数研究统一起来。否则多尺度模型容易给人“算了很多但没有一句话结论”的感觉。

审稿防守还可以增加“经典极限回收”表述：当 transmutation source 很低、缺陷增强扩散弱、溶质近似守恒时，模型应能回到经典粗化指数；当源项持续增强时，才进入非平衡机制。能回收经典极限，是新模型获得信任的重要方式。

这一点尤其适合写在 Discussion。
