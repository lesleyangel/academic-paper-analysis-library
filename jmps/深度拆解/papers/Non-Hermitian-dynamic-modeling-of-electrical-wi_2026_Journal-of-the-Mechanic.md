# Non-Hermitian dynamic modeling of electrical wireless energy transfer through elastic waves

## 0. 读取说明
- 源 PDF：`jmps/文献/Non-Hermitian-dynamic-modeling-of-electrical-wi_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps/文本/txt/Non-Hermitian-dynamic-modeling-of-electrical-wi_2026_Journal-of-the-Mechanic.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 可读出模型、章节和图题，但 eigenvalue 曲线、efficiency maps、结构示意与材料/厚度参数的图像细节需结合 PDF 图像核查。
- 本文类型：理论建模 + 非厄米 Hamiltonian 框架 + 弹性波无线能量传输设计 + 数值仿真验证。

## 1. 基本信息与论文身份
- 题名：Non-Hermitian dynamic modeling of electrical wireless energy transfer through elastic waves。
- 作者与机构：Linlin Geng、Jinbo Yuan、Ziqi Zhong、Baoming Bi、Lei Zhang、Guoliang Huang、Xiaoming Zhou；Beijing Institute of Technology 与 Peking University。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106644。
- DOI：10.1016/j.jmps.2026.106644。
- 关键词：Elastic waves；Electrical wireless energy transfer；Non-Hermitian theory；PT symmetry；Anti-PT symmetry。
- 研究对象：通过金属/弹性结构传播弹性波实现 electrical wireless energy transfer 的系统。
- 研究尺度：电端口、压电换能器、弹性中间层、 resonant states、Hamiltonian eigenvalues 和能量传输效率。
- 方法类型：general non-Hermitian model、generalized Hamilton principle、Schrödinger-like equation、PT/anti-PT symmetry design、有限元/仿真对比。
- 证据类型：特征频率实部/虚部、power transfer efficiency maps、frequency spectra、loss/no-loss comparison、参数鲁棒性、不同材料结构仿真。
- 目标读者：弹性波、声/弹性超材料、非厄米物理、无线能量传输、压电结构设计研究者。
- JMPS 风格定位：将量子/非厄米理论语言迁移到经典弹性波能量传输，并把模型写成可设计原则而非只描述频响。

## 2. 摘要与核心信息提取
摘要开头先给应用需求：elastic-wave-based WET 可为 metallic sealed vessels 内部设备供能，避免电磁屏蔽导致的传统方法失效。gap 句指出 classical elastodynamic theory 往往描述 transfer behavior，却缺少高效率和鲁棒设计原则。方法句提出 non-Hermitian dynamic theory，rooted in quantum mechanics，用于 modeling and inverse design。

核心方法包括 general non-Hermitian model，捕捉 resonant states 与 electrical energy channels 的耦合；通过 piezoelectric composite structure 物理实现；将 coupled electro-elastic dynamics 写成 Schrödinger-like formulation 中的 non-Hermitian Hamiltonian。

结果句分两层：two-state PT-symmetric model 在 purely real eigenvalue states 实现 complete power transfer；three-state anti-PT-symmetric system 实现近完全且对选定参数 robust 的能量传输。意义句把框架定位为 elastic-wave WET design route 和 non-Hermitian elastic-wave phenomena platform。

一句话主张：通过把压电-弹性-电路耦合系统映射为非厄米 Hamiltonian，并工程化 PT/anti-PT symmetry，可为金属屏蔽环境中的 elastic-wave wireless energy transfer 提供高效率、鲁棒且可逆向设计的原则。

核心关键词：non-Hermitian Hamiltonian；Schrödinger-like equation；PT symmetry；anti-PT symmetry；elastic wave WET。

## 3. 选题层深拆
问题来源是应用约束与理论工具之间的错位。WET 在普通环境下可用电磁近场/远场方法，但 metallic sealed enclosures、armor、spacecraft、nuclear reactors、hazardous containers 等场景中电磁屏蔽使电磁 WET 失效。弹性波可穿过金属结构，因此成为替代路径。但弹性波 WET 涉及电端口、压电换能、结构振动、波传播和负载耦合，传统 elastodynamic modeling 更多是 forward analysis，不足以给出高效鲁棒设计规律。

问题重要性由“无物理穿线供电”支撑，尤其是封闭金属容器中的无线传感和供能。JMPS 价值则来自跨域理论迁移：非厄米理论、PT symmetry 和 anti-PT symmetry 原本常见于量子/波物理，本文把它们转译为经典 electro-elastic energy transfer 的设计变量。

为什么现在值得做：非厄米波物理已经在 optics/acoustics/mechanics 中积累了 exceptional points、gain/loss engineering、PT/anti-PT symmetry 等工具；压电结构又天然连接 mechanical energy channel 和 electrical port。两者结合可把“能量传输效率”写入 eigenvalue/eigenmode 设计。

问题边界：本文主要是理论与仿真设计，没有实物实验；系统基于 realistic materials，作者声称 experimentally feasible，但尚未直接制造验证。WET 效率和鲁棒性主要在选定参数空间中展示。

## 4. 领域位置与文献版图
文献版图包括三条线。第一条是 WET 发展：Tesla coil、radiative microwave/laser、near-field magnetic resonance coupling。第二条是 elastic wave WET：通过压电 transmitter/receiver 让能量穿过金属壁。第三条是 non-Hermitian wave theory：PT symmetry、anti-PT symmetry 和 Hamiltonian 表述为波系统设计提供新自由度。

前两条解决了应用和传统实现，第三条提供设计语言。已有 elastodynamic models 能描述 port behavior、vibration modes 和 wave propagation，但它们通常没有给出“在哪些 eigenvalue 条件下可实现 complete transfer/robust transfer”的简洁原则。

本文站在 non-Hermitian elastic/acoustic wave physics 与 piezoelectric WET 之间。创新不是简单说“非厄米也可用于弹性波”，而是建立 physical system 与 non-Hermitian model 的 quantitative correspondence，并分别构造 PT 和 anti-PT 对称 WET 系统。

对前人姿态温和：传统 elastodynamics 是基础，但缺少 inverse design clarity；非厄米理论是来源，但需要被翻译成实际压电-弹性结构。

## 5. Gap 制造机制
显性 gap：classical elastodynamic theory describes transfer behavior rather than offering clear design principles for high efficiency and robustness。隐含 gap：现有 elastic-wave WET 设计缺少把电端口 gain/loss、结构耦合和负载变化统一起来的 Hamiltonian 级框架。

Gap 类型属于设计原则 gap + 跨域理论迁移 gap。设计原则 gap 是“能算”不等于“会设计”；跨域 gap 是 non-Hermitian theory 尚未充分用于 elastic-wave WET 的 inverse design。

Gap 证据来自应用复杂性：能量传输机制包含 electrical port behavior、structural vibration modes、elastic wave propagation；参数变化和 material loss 会影响效率。因此需要一个能把这些耦合压缩成 eigenvalue/eigenstate 条件的模型。

审稿人可能追问：非厄米模型是否只是重新包装等效电路/模态耦合？作者的防守点在于 PT/anti-PT symmetry 给出 complete transfer 和 robustness 的明确条件，并通过物理结构对应和仿真展示差异。

## 6. 创新性判断
作者声称贡献：开发 general non-Hermitian model；从 generalized Hamilton principle 推导各元素动力学并组合成 Schrödinger-like equation；构造 two-state PT-symmetric WET 实现 complete transfer；构造 three-state anti-PT-symmetric WET 实现对 load resistance 等参数不敏感的 near-complete transfer；提出 realistic materials 下的可实现系统。

真实创新在“设计语言”而非单个结构。它把 source state、receiver state、intermediate state 和 coupling 写成通用模块，让弹性波 WET 可通过 Hamiltonian symmetry 设计。two-state 与 three-state 不是简单多一个 resonator，而是分别承担 efficiency 与 robustness 的机制展示。

创新类型：理论框架强；跨域迁移强；工程验证中等；实验数据弱。创新必要性高，因为封闭金属环境 WET 的关键不是只提升某个样机效率，而是找到可推广设计原则。

容易被挑战处：gain 的物理实现、loss 的处理、材料阻尼与电路非理想性、频率偏移、制造误差、带宽等；anti-PT symmetry 是否在真实结构中只是 approximate；complete transfer 是否对未扫参数仍鲁棒。

## 7. 论证链条复原
背景 -> WET 重要，但金属封闭环境中电磁方法受屏蔽限制。
文献 -> elastic wave WET 可穿透金属，但传统模型偏描述，缺少高效鲁棒设计原则。
gap -> 需要可把电-弹耦合转为可设计 eigenvalue 条件的统一框架。
问题 -> 如何用 non-Hermitian theory 设计 elastic-wave WET，使其达到 complete/robust energy transfer？
方法 -> 定义 source、receiver、intermediate states 和 coupling；用 generalized Hamilton principle 推导动力学；构建 non-Hermitian Hamiltonian。
证据 -> two-state PT eigenvalues、power transfer efficiency、loss comparison；three-state anti-PT eigenvalues、load/geometry/material 参数鲁棒性。
发现 -> PT-symmetric phase mode 可 complete transfer；anti-PT three-state system 对 load resistance 等变化更鲁棒。
机制 -> 电输入等效 gain，负载/损耗等效 loss；通过 symmetry condition 使能量在目标通道高效交换。
意义 -> 为 elastic-wave WET 提供 inverse design route，也为非厄米弹性波现象提供平台。

薄弱环节是实验缺失。作者用 realistic materials 和 simulation support 降低风险，但最终还需 prototype 验证。

## 8. 方法/理论/模型细拆
方法总框架包含四个模块：source state、receiver state、intermediate state、state coupling。source 和 receiver 通过压电材料与电端口交换能量；intermediate state 由弹性固体承担，既可作为电屏蔽屏障，也允许弹性波传播；coupling 描述状态之间的能量交换。

2.1 先提出 general non-Hermitian model。2.2 分别推导 source、receiver、intermediate 和 coupling 的 dynamic equations。关键写法是将经典 electro-elastic system 组织为类似 Schrödinger equation 的形式，并用 non-Hermitian Hamiltonian 表征能量传输。

3.1 构造 two-state PT-symmetric system，通过调节 source/load impedance 等使 effective Hamiltonian 满足 PT symmetry；在 PT-symmetric phase，eigenvalues 为实，从而实现 complete power transfer。3.2 构造 three-state anti-PT-symmetric system，加入 intermediate state 使 transfer 对 selected parameters 更不敏感。

方法与 gap 的对应：gap 是设计原则，方法就提供 symmetry condition；gap 是鲁棒性，方法就从 PT 扩展到 anti-PT；gap 是物理可实现，方法就用 piezoelectric composite structure 和 realistic materials 映射。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| elastic-wave WET 可写成 non-Hermitian Hamiltonian | 2、结论 | source/receiver/intermediate/coupling 动力学推导与 Schrödinger-like formulation | 理论推导 | 强 | 模态截断和等效参数需核查 |
| two-state PT-symmetric WET 可实现 complete energy transfer | 摘要、3.1、4.1 | eigenfrequency 实/虚部、power transfer efficiency map、frequency spectra | 理论 + 仿真 | 强 | 对损耗和失配敏感性需关注 |
| electric input 可作为 effective gain 构造 PT symmetry | 3.1、结论 | Hamiltonian 中 gain/loss 对应关系 | 模型解释 | 中强 | 实际电源稳定性/非线性未实验验证 |
| three-state anti-PT system 对 load resistance 变化更鲁棒 | 摘要、3.2、4.2 | Fig. 6-8 中 anti-PT eigenvalues 与效率随 Z0/h1 变化 | 参数仿真 | 强 | “selected parameters” 范围有限 |
| realistic materials 下系统 experimentally feasible | 结论、Fig. 10 | steel/aluminum systems、材料损耗仿真 | 工程仿真 | 中 | 仍缺样机实验 |
| non-Hermitian framework 可作为 elastic-wave phenomena platform | 摘要、结论 | PT/anti-PT 两类系统展示 | 理论外推 | 中 | 平台价值需更多现象支持 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | general non-Hermitian WET model 与 physical realization | 模型-物理对应 | 建立抽象状态与结构部件关系 | 是 |
| Fig. 2 | piezoelectric transmitter/receiver、coupling layer、电路模型 | 动力学推导基础 | 说明电-弹耦合来源 | 是 |
| Section 2 equations | source/receiver/intermediate/coupling dynamics | Hamiltonian 框架 | 提供理论核心 | 否，需核公式 |
| Fig. 3 | PT eigenfrequencies 与 theoretical transfer | PT complete transfer | 显示 real eigenvalue phase 与传输关系 | 是 |
| Fig. 4 | PT system efficiency map/frequency spectra | 数值验证 | 展示高效点和频率响应 | 是 |
| Fig. 5 | with/without material loss | 损耗影响 | 检查现实性 | 是 |
| Fig. 6 | anti-PT eigenfrequencies/theoretical transfer | anti-PT robustness | 展示三态机制 | 是 |
| Fig. 7-8 | Z0、h1 参数下效率图 | 鲁棒设计 | 证明 selected parameter insensitivity | 是 |
| Fig. 9-10 | loss 与 steel/aluminum systems | 实际材料可行性 | 扩展到不同材料/厚度 | 是 |

图表叙事是从“模型示意”到“对称性条件”再到“仿真效率图”。效率图是工程说服，eigenvalue 图是物理机制说服。

## 11. 章节结构与篇章布局
Abstract：应用需求 -> 传统理论不足 -> 非厄米框架 -> PT/anti-PT 设计 -> 意义。
Introduction：WET 技术谱系 -> 金属屏蔽问题 -> elastic wave WET -> modeling challenge -> non-Hermitian theory 机会。
Section 2：general model 和 element-wise dynamic equations。
Section 3：设计两个代表系统：two-state PT 与 three-state anti-PT。
Section 4：结果与讨论，分别验证 PT 和 anti-PT 系统的 transfer behavior。
Conclusion：回收四模块模型、Hamiltonian 表述、PT complete transfer、anti-PT robustness 和实验可行性。

最值得模仿的是“先 general model，再 two design cases”的布局。它让论文既有普适框架，又有具体演示。小节标题清楚区分 PT 与 anti-PT，读者容易跟踪。

结构风险：理论迁移跨度大，如果 Introduction 对 non-Hermitian 背景铺垫不足，传统力学读者可能觉得符号突然；但 physical/electrical circuit models 缓解了这个问题。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Non-Hermitian-dynamic-modeling-of-electrical-wi_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：14
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 A general non-Hermitian model for elastic wave wireless energy transfer | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.1 Non-Hermitian models of elastic wave WET systems | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.2.1 Source state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.2 Receiver state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.3 Intermediate state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.4 State coupling | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Elastic wave WET systems with the PT and anit-PT symmetry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Two-state WET system with the PT symmetry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Three-state WET system with the anti-PT symmetry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Energy transfer behavior in two-state PT-symmetric systems | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Energy transfer behavior in three-state anti-PT-symmetric systems | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Conclusion | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落推进：先讲 WET 的历史和主流方法；再指出金属屏蔽场景的特殊难题；再引入 elastic wave WET 的可行性；随后指出经典模型缺少 design principles；最后提出 non-Hermitian dynamic modeling。

Theory 段落推进：先抽象状态，再逐个写物理元素方程，最后合并为 Hamiltonian。这个节奏避免一开始就堆 Hamiltonian，让 reader 先看到对应的电路/结构部件。

Results 段落推进：对每个系统先看 eigenvalues，再看 power transfer maps，再看损耗和参数变化。也就是说，先证明对称性机制，再证明工程指标。

Conclusion 段落推进：以 general model 四部件开头，重申 source/receiver 的压电实现和 intermediate 的弹性屏障功能，再收束到 PT 与 anti-PT 的不同设计价值。

可复用模板：`Classical model describes [response], but design requires [principle]; by mapping [physical system] to [abstract operator], [symmetry/condition] yields [target performance].`

## 13. 文笔画像与语言习惯
语气是跨域理论型，常用 “rooted in quantum mechanics”“powerful framework”“quantitative correspondence”“Schrödinger-like formulation”。作者用较强词汇包装理论迁移，但在物理实现处强调 realistic materials 和 experimentally feasible。

claim 强度高：complete power transfer、robust to variations、superior design flexibility。但这些 claim 绑定在特定 PT/anti-PT 系统与 selected parameters 下，写作时应保持条件。

常用问题词：wireless energy transfer、metallic sealed vessels、electromagnetic shielding、coupled electro-elastic dynamics。常用机制词：gain、loss、coupling、eigenfrequency、Hamiltonian、PT symmetry、anti-PT symmetry。常用结果词：complete transfer、near-complete transfer、robustness、efficiency map。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：transfer(87)；energy(84)；non-hermitian(66)；systems(58)；system(51)；elastic(49)；piezoelectric(45)；transmission(44)；ciency(42)；wet(38)；power(33)；state(33)；wave(32)；receiver(32)；sin(31)；design(29)；symmetry(29)；model(29)；displacement(27)；coupling(24)
- 高频学术名词：energy(84)；system(51)；model(29)；condition(28)；displacement(27)；equation(26)；simulation(24)；coupling(24)；behavior(22)；thickness(21)；material(19)；results(19)；distribution(17)；validation(14)；excitation(14)；structure(12)
- 高频学术动词：shows(7)；proposed(6)；shown(5)；developed(5)；derived(4)；compared(3)；demonstrate(3)；demonstrated(3)；formulated(2)；validate(1)；derive(1)；reveal(1)；evaluated(1)；develop(1)；propose(1)；indicates(1)
- 高频形容词：elastic(98)；piezoelectric(45)；dynamic(40)；displacement(27)；theoretical(24)；electric(24)；real(23)；electrical(21)；wireless(19)；material(19)；resonant(18)；anti-pt-symmetric(14)；pt-symmetric(14)；structural(13)；erent(12)；cient(11)
- 高频副词/连接副词：respectively(15)；consequently(10)；potentially(4)；notably(4)；purely(4)；typically(3)；highly(3)；nearly(3)；primarily(3)；slowly(3)；clearly(3)；furthermore(2)；therefore(2)；experimentally(2)；recently(2)；rstly(2)
- 高频二词短语：energy transfer(49)；transfer ciency(28)；elastic wave(27)；non-hermitian model(21)；wave wet(19)；wireless energy(17)；wet systems(17)；power transfer(15)；power transmission(15)；sin sin(14)；anti-pt symmetry(12)；piezoelectric transmitter(12)；non-hermitian models(12)；results power(12)；simulation results(12)；resonant states(11)
- 高频三词短语：elastic wave wet(19)；wireless energy transfer(17)；wave wet systems(12)；power transfer ciency(11)；simulation results power(10)；complete energy transfer(9)；energy transfer behavior(9)；piezoelectric transmitter receiver(9)；axial displacement amplitude(9)；displacement amplitude distribution(9)；sin sin sin(6)；results power transfer(6)

**主动、被动与句法**

- 被动语态估计次数：173
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：549
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：207
- 一般过去时线索：21
- 现在完成时线索：16
- 情态动词线索：66
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：non-hermitian(9)；transfer(6)；design(6)；energy(5)；electrical(4)；wireless(4)；beijing(4)；wet(4)
- 1. Introduction：energy(24)；transfer(20)；systems(19)；non-hermitian(18)；wet(16)；elastic(14)；wave(10)；ciency(8)
- 2. A general non-Hermitian model for elastic wave wireless energy transfer：无明显高频项
- 2.1. Non-Hermitian models of elastic wave WET systems：energy(8)；non-hermitian(7)；model(6)；elastic(6)；states(6)；state(6)；resonant(5)；coupling(5)
- 2.2.1. Source state：electric(8)；piezoelectric(7)；cylinder(6)；transmitter(6)；coupling(5)；source(4)；state(4)；given(4)
- 2.2.2. Receiver state：receiver(6)；state(4)；piezoelectric(3)；given(3)；same(2)；source(2)；electrical(2)；electrode(2)
- 2.2.3. Intermediate state：cylinder(6)；state(3)；intermediate(2)；elastic(2)；mass(2)；density(2)；element(2)；mode(2)
- 2.2.4. State coupling：coupling(2)；resonant(2)；states(2)；elastic(2)；layer(2)；mode(2)；displacement(2)；eld(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
骨架：`Classical [theory] typically describes [behavior] rather than offering clear design principles for achieving [performance] and [robustness].`
中文启发：用“描述 vs 设计”的对比制造方法 gap。

### 14.2 方法与框架表达
骨架：`We develop [theory], rooted in [field], as a framework for modeling and inverse design of [system].`
中文启发：跨域方法要交代来源领域和目标任务。

### 14.3 结果与趋势表达
骨架：`By engineering [symmetry] in an effective [operator], [target performance] becomes achievable at [eigenvalue/eigenstate condition].`
中文启发：结果句可把设计动作、数学条件和工程性能放在同一句。

### 14.4 机制解释表达
骨架：`The coupled [physical] dynamics can be represented using [operator] within a [formulation], where [parameter] acts as [gain/loss/coupling].`
中文启发：映射类论文要明确“谁对应谁”。

### 14.5 贡献与意义表达
骨架：`The proposed framework provides an effective route to design [devices] and offers a versatile platform for exploring [phenomena].`
中文启发：贡献可以双重定位：工程设计 + 基础物理平台。

### 14.6 局限与未来工作表达
骨架：`Although the designed systems are based on realistic materials, experimental validation is required to assess [loss/tolerance/nonlinearity].`
中文启发：理论仿真论文要主动留下实验验证接口。

## 15. 引用策略与文献使用
引用从 WET 历史开始，用 Tesla、microwave、laser、magnetic resonance coupling 建立技术谱系。随后引用金属屏蔽场景和 elastic wave transfer 工作，说明弹性波路径的必要性。非厄米理论引用服务于引入 PT/anti-PT symmetry 的设计语言。

经典引用用于 WET 基础和非厄米概念，近年引用用于现代 WET devices、elastic wave systems 和 non-Hermitian wave phenomena。引用姿态是“继承 + 转译”：传统 WET 解决常规场景，弹性波解决金属屏蔽，非厄米理论解决设计原则。

gap 借引用形成：电磁 WET 文献说明为什么不够；elastic WET 文献说明替代方案存在；非厄米文献说明有新理论工具；本文填补的是两者之间的建模-设计桥梁。

引用风险：若非厄米 elastic/acoustic WET 已有相似工作，需明确本文 general model 与 physical correspondence 的新意；此外 PT/anti-PT 概念需要引用权威基础文献。

## 16. 审稿人视角风险
最大攻击面是实验缺失。complete/near-complete transfer 和 robustness 目前来自理论与 simulation，真实压电材料、粘接层、边界、温度、非线性和电路噪声可能降低效率。

第二风险是“gain/loss”物理实现。电输入作为 effective gain 的稳定性、能耗和控制实现需要工程说明。第三风险是 robustness 范围：anti-PT 对 selected parameters 鲁棒，不代表对所有制造误差和环境扰动鲁棒。

第四风险是模型降阶/模态截断。如果 physical system 到 Hamiltonian 的 quantitative correspondence 忽略了重要高阶模态或耗散通道，设计点可能偏移。

图表核查：efficiency maps、frequency spectra、eigenvalue real/imaginary parts 和材料损耗对比必须结合 PDF 图像核查，TXT 无法判断峰值宽度、颜色范围和参数扫描密度。

## 17. 可复用资产
可复用选题角度：把某领域“能描述但难设计”的模型升级为“可逆向设计”的 operator/symmetry 框架。
可复用 gap 制造：传统理论可 forward simulate，但缺少 high-efficiency and robustness design principles。
可复用论证链：应用限制 -> 传统方法失效 -> 替代物理通道 -> 抽象 Hamiltonian -> 对称性设计 -> 仿真验证。
可复用图表设计：general model schematic、physical circuit mapping、eigenvalue plots、efficiency maps、loss comparison、robustness scans。
可复用段落结构：先讲物理元件，再讲数学映射，再讲设计条件。
可复用句型：`By establishing a quantitative correspondence between [abstract model] and [physical system], [complex dynamics] can be represented as [compact formulation].`
不宜直接模仿：没有工程验证时过度承诺 device performance。

## 18. 对我写论文的启发
写跨域理论迁移论文时，要避免只搬术语。本文值得学的是先把 source、receiver、intermediate 和 coupling 映射到实物，再引入 Hamiltonian；这样非厄米语言不是装饰，而成为设计工具。

Introduction 可迁移写法：先说明传统路径为何在特定场景失效，再引入新物理通道。Method 可迁移写法：分模块推导，最后合并成统一方程。Results 可迁移写法：数学条件图和工程性能图成对出现，让机制与指标互相支撑。

需要避免：只展示高效率点而不展示参数鲁棒性；只谈 symmetry 而不说明可调物理参数；把 approximate anti-PT 写成严格物理实现。

## 19. 最终浓缩
这篇论文最值得学的是：用 non-Hermitian Hamiltonian 把复杂电-弹耦合 WET 系统转化为可设计的对称性问题，并用 PT/anti-PT 两个案例分别展示效率和鲁棒性。

最大风险是：目前主要是理论和仿真，真实器件中的损耗、制造误差和控制电路可能改变设计点。

三个可迁移动作：1. 用“描述不足以设计”制造方法 gap；2. 明确抽象模型和物理部件的一一对应；3. 用 eigenvalue 图与性能图双重证明设计原则。
