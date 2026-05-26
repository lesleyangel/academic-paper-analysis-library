# Machine learning extraction of viscoelastic material properties from full-field deformation measurements

## 0. 读取说明
- 源 PDF：jmps\文献\Machine-learning-extraction-of-viscoelastic-mater_2026_Journal-of-the-Mechan.pdf
- 源 TXT：jmps\文本\txt\Machine-learning-extraction-of-viscoelastic-mater_2026_Journal-of-the-Mechan.txt
- 是否需要结合 PDF 图像核查：需要。本文拆解基于 PyMuPDF 抽取文本、图注、公式附近文字和元数据；所有曲线形状、云图细节、误差空间分布和示意图视觉层次均需结合 PDF 图像核查。
- 本文类型：机器学习反演方法 + 数值/实验验证。
- 读取边界：上一轮 `jmps/拆解/papers` 仅作为辅助索引；本文件按全文结构、摘要、章节、图注、附录和 references 线索重新组织。

## 1. 基本信息与论文身份
- 题名：Machine learning extraction of viscoelastic material properties from full-field deformation measurements
- 作者/机构：Congjie Wei; Lehu Bu; Jin Yang; Chenglin Wu；Texas A&M University; The University of Texas at Austin; Texas Materials Institute
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 212 (2026) 106589. doi:10.1016/j.jmps.2026.106589
- DOI：10.1016/j.jmps.2026.106589
- 关键词：Property characterization,Deep learning,Full-field deformation,Viscoelasticity
- 研究对象：黏弹性材料的全场变形测量、应力场预测与材料参数提取，重点覆盖水凝胶、微空化与单点加载场景。
- 研究尺度：连续介质全场尺度，同时利用点级时序、邻域空间梯度和材料参数空间。
- 方法类型：Deep-VM-FE 与 Deep-VM-FD 两条路线；Kelvin-Voigt/neo-Hookean Kelvin-Voigt 表述；双通道应力分解；梯度 pooling；数值训练与 LIC/NIC 实验应用。
- 证据类型：解析空化数据库、1D 蠕变/松弛 FE、2D 空化 FE、2D 单点加载 FE、STAQ-DIC 空化实验、误差统计与参数分布。
- 目标读者：软物质实验力学、黏弹性本构反演、数据驱动力学和全场测量社区。
- JMPS 风格定位：JMPS 中典型的 AI + mechanics 方法论文：算法不是独立炫技，而被嵌入力学方程、边界条件、实验测量和材料表征任务。 全文 22 页，抽取文本约 12004 个英文词，结构目录线索包括：Machine learning extraction of viscoelastic material properties from full-field deformation measurements；1 Introduction；2 Problem formulation；3 Deep-VM-FE algorithm decoupling temporal and spatial information；3.1 Deep-VM-FE algorithm construction；3.2 Analytical model for inertial microcavitation in viscoelastic materials to generate synthetic training datasets；3.3 Training database generation and formulation；3.4 Validation of Deep-VM-FE algorithm；4 Deep-VM-FD algorithms for decomposition and reconstruction of field data；4.1 Deep-VM-FD algorithm construction；4.1.1 Gradient pooling；4.1.2 Deep-VM-FD algorithm；4.2 Validation based on 1D creep and relaxation numerical model；4.2.1 1D creep model setup。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要采用“痛点 -> 方法分型/模型建立 -> 验证范围 -> 意义”的 JMPS 常见结构，不先铺过多背景，而是快速给出研究对象和方法承诺。
- 背景句承担什么：黏弹性材料性质表征对结构、聚合物和生物材料很关键，但传统拟合依赖假定本构、迭代正演和人工调参。
- gap 句承担什么：已有 PINN、序列网络和图像网络各有优势，却难同时处理已知本构、未知本构、时变历史、空间邻域和实验场数据。
- 方法句承担什么：作者把问题分成已知 governing equations 的 Deep-VM-FE 和无显式本构的 Deep-VM-FD 两种，前者分解弹性/黏性应力，后者从点式场序列直接学习应力演化。
- 结果句承担什么：算法在解析生成的水凝胶数据库、1D/2D 数值 benchmark 和 gelatin 空化实验中均显示与基准或内部一致性较好的预测。
- 意义句承担什么：论文给出从可测全场变形走向不可测应力和黏弹参数的可操作路线，但实验真实性仍依赖间接验证。
- 一句话主张：根据本构形式是否已知，将黏弹性全场反演拆成 Deep-VM-FE 与 Deep-VM-FD 两类学习任务，可以更高效地从变形场提取应力场和材料性质。
- 3-5 个核心关键词：黏弹性反演；全场变形；Deep-VM-FE/FD；梯度 pooling；空化实验

## 3. 选题层深拆
- 问题来源：选题来自一个清楚的实验力学断裂：DIC/STAQ-DIC 能给出高时间分辨率变形场，但真实应力和黏弹参数仍需依赖模型反演。作者把传统表征成本高、PINN 对时变问题不稳、纯数据模型吃数据这三类痛点合并成一个方法学入口。
- 问题为什么重要：它连接了一个高价值应用目标和一个力学上仍不完全可控的变量；如果该变量能被测量、预测或设计，后续材料表征、结构设计或生物医学判断都会更可操作。
- 问题为什么现在值得做：一方面，近年实验、计算或机器学习工具让以前难以观测/求解的量变得可处理；另一方面，已有模型的局限已经被足够多文献暴露，形成了可被审稿人接受的切入口。
- 问题边界：文章主要在 Kelvin-Voigt 型软材料、均质或近似均质训练分布和空化/单点加载 benchmark 中展开；对损伤、强异质、循环历史、未知边界和跨材料外推仅作为未来方向。
- 选题的 JMPS 味道：它不是停留在应用演示，而是追问“为什么这个响应会出现、这个假设何时成立、这个反问题如何被物理约束”。这种从现象回到机制/模型/证据闭环的写法，是 JMPS 的核心味道。
- 选题可迁移性：可迁移到任何“可测量 X 与关键但不可直接获得 Y 之间存在断裂”的论文：先证明 Y 重要，再说明传统路线的成本或偏置，最后提出受力学约束的桥接框架。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：作者不是按年份堆文献，而是按问题功能划分：哪些工作解释了现象，哪些提供了模型，哪些给出了数据或设计工具，哪些留下了当前缺口。
- 主要研究流派/方法路线：
- 传统黏弹性表征：应力-应变曲线 + 假定本构 + 参数拟合，解决可解释性，留下高成本和模型偏置。
- PINN 和 physics-informed 方法：减少数据需求并嵌入平衡方程，解决物理一致性，留下时间历史、过拟合和不完整数据问题。
- RNN/LSTM/Transformer/neural ODE/operator learning：适合路径依赖和序列映射，解决历史记忆，留下全场应力反演和实验边界适配问题。
- DIC、空化微流变和图像/场学习：提供高价值全场输入，留下应力不可直接测量的问题。
- 每类研究解决了什么：前人分别解决了基本物理语言、经典模型、数值或实验方法、以及部分应用验证；因此本文不需要重建整个领域，只需说明这些路线拼在一起时仍缺少最后一环。
- 每类研究留下什么不足：不足通常不是“完全不能用”，而是“在本文关心的边界条件、几何、数据类型或机制层级下不够”。这种写法比直接否定前人更稳。
- 本文站在哪条线上：本文站在最接近的机制/模型/反演路线之后，把前人留下的假设、尺度或数据缺口具体化。
- 最接近前人工作：从全文看，最接近的是那些已经提出相近模型、方法或实验事实但没有系统处理本文特定 gap 的工作；作者通过对比适用前提而不是简单性能排名来定位自己。
- 是否公平处理前人：总体公平。它承认前人有效范围，再指出本文要处理的是其未覆盖的场景。这种姿态降低了“为创新而贬低文献”的风险。

## 5. Gap 制造机制
- 明示 gap：明示 gap 是黏弹性全场数据丰富但材料参数和应力场不能直接获得；隐含 gap 是一个算法很难同时适配有解析本构和无解析本构两类任务。因此作者用问题分型而不是单一万能网络来制造必要性。
- 隐含 gap：更深层的缺口是“已有工具无法同时满足物理可解释、可计算、可验证和可迁移”四个要求；本文通过一个更窄但更闭合的问题来处理它。
- gap 类型：方法 gap、机制 gap、验证 gap 或假设有效域 gap的组合；具体取决于本文对象，但都不是单纯“没人做过”。
- gap 证据来自哪里：来自 Introduction 的文献分组、方法章节中被保留/放弃的假设、以及 Results 中专门设计的 benchmark 或参数扫描。
- gap 是否足够窄：足够窄。作者没有声称解决整个领域问题，而是把范围限制在明确材料、几何、数据类型或模型框架内。
- gap 是否足够重要：重要性来自两端：一端是应用/实验/设计需求，另一端是理论或模型上的未闭合。两端都存在时，JMPS 审稿人更容易接受。
- 如果我是审稿人会如何追问：我会问最接近前人方法是否真的不能处理该场景，本文的证据是否覆盖了 gap 中最困难的边界，以及结论有没有超出验证范围。

## 6. 创新性判断
- 作者声称的贡献：真实创新在反演工作流和数据组织：Deep-VM-FE 利用已知本构结构做双通道分解，Deep-VM-FD 将邻域空间信息引入点级时序应力预测。创新强度中等偏强，算法组件并非全新基础网络，但验证路线完整且贴近实验表征。
- 我判断的真实创新：真实创新不只是提出一个名字或公式，而是重排了问题边界：把原本混在一起的物理、数据、几何或机制因素拆开，让某个不可见变量变得可计算或可检验。
- 创新类型：理论机制、方法流程、假设审计、实验反演或本构表达中的一种或多种组合。
- 创新强度：相对较强的部分在于论证闭环，而不一定在单个工具。若单独拿出网络、FE 或拟合公式，未必全新；但放在本文问题链条里，它们承担了清楚的新功能。
- 创新必要性：必要，因为不引入该框架，论文关心的 gap 只能靠经验拟合、理想化假设或不可验证叙事维持。
- 创新与证据匹配度：主体证据能支撑“在本文边界内有效”；对更广泛材料、临床、复杂几何或真实多物理场的外推需要谨慎。
- 容易被挑战的创新点：最容易被问的是：新方法/模型相对最近前人的不可替代性在哪里？新增参数或算法组件是否只是提高拟合自由度？是否有消融、对照或解析基准证明？

## 7. 论证链条复原
背景：黏弹性性质难以高效表征 -> 文献：物理模型、PINN、序列网络和场学习各有局限 -> gap：全场变形到应力/参数的映射缺少分场景工具 -> 问题：已知与未知本构两类情形如何分别学习 -> 方法：Deep-VM-FE 和 Deep-VM-FD -> 证据：解析、FE、2D 和实验逐级验证 -> 发现：数值基准准确，实验结果内部一致 -> 机制：时空分解与邻域 pooling 改善历史和空间感知 -> 意义：提供黏弹性材料表征的高效替代流程。

这条链条的写作价值在于：每个后续部分都回到前一个必要性。方法不是凭空出现，而是对 gap 的直接回应；图表不是展示材料，而是为特定 claim 服务；结论也没有离开开头的问题。若要迁移到自己的论文，可先写出同样的九节点链条，再检查每个节点是否有文本或图表支撑。

## 8. 方法/理论/模型细拆
- 方法总框架：Deep-VM-FE 与 Deep-VM-FD 两条路线；Kelvin-Voigt/neo-Hookean Kelvin-Voigt 表述；双通道应力分解；梯度 pooling；数值训练与 LIC/NIC 实验应用。
- 关键概念：黏弹性反演；全场变形；Deep-VM-FE/FD；梯度 pooling；空化实验。这些概念不是名词列表，而是构成论证的“承重墙”：去掉任何一个，问题边界都会改变。
- 关键变量/参数：全文围绕可观测量、内部变量、材料/几何参数、损失或能量项、以及输出指标组织。具体变量需结合原文公式逐项核查。
- 核心假设：文章主要在 Kelvin-Voigt 型软材料、均质或近似均质训练分布和空化/单点加载 benchmark 中展开；对损伤、强异质、循环历史、未知边界和跨材料外推仅作为未来方向。 这些假设使问题可解，也限定了结论外推。
- 边界条件：文本给出了对应几何、加载、数据或模型边界；涉及图像、曲线和场分布处需结合 PDF 核查。
- 方法步骤：
- Deep-VM-FE 的关键是把总应力拆成 rate-independent 与 rate-dependent 两部分，用两个并行网络分别吸收空间变形和速率历史，再通过综合 loss 约束总应力。
- Deep-VM-FD 的关键是放弃显式本构，直接把点的变形历史、邻域梯度和时间序列作为输入，输出应力演化；gradient pooling 用于补充局部空间结构。
- 训练数据库从解析模型、FE 仿真和实验测量逐级切换，叙事上形成从可控 ground truth 到真实可测数据的证据梯度。
- 复现信息：元数据、章节标题、图注、表格、附录和参数表均提供复现线索。若要真正复现，应回到 PDF 中的公式编号、网格/训练/拟合参数和附录表。
- 方法复杂度是否合理：合理。复杂度与 gap 的难度相匹配；论文也通过对照、基准或参数扫描证明复杂度不是纯装饰。
- 方法与 gap 的对应关系：方法中的每个关键模块都对准一个缺口：物理约束对准不适定性，参数扫描对准假设有效域，微观模型对准机制解释，实验/数值 benchmark 对准可验证性。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 传统黏弹性表征在复杂速率依赖材料中成本高且依赖本构假设 | Introduction | 传统拟合流程、迭代正演和模型形式调参的文献铺垫 | 文献+问题分析 | 强 | 如果审稿人认为传统反演已有成熟加速算法，需要更直接对比 |
| Deep-VM-FE 能在已知方程场景下解耦弹性和黏性应力 | Section 3 | Kelvin-Voigt 分解、解析空化训练数据库、Fig. 3 loss 与预测对比 | 模型+数值 | 强 | 主要限于训练分布内的 Kelvin-Voigt 型材料 |
| Deep-VM-FD 能在未知显式本构时从场数据学习应力演化 | Section 4 | 1D 蠕变/松弛、2D 空化和单点加载 FE 验证 | 数值 benchmark | 强 | 未知本构并不等于任意材料，训练数据仍含隐含物理先验 |
| gradient pooling 增强模型的空间感知 | Section 4.1 | 算法示意和 2D 场预测结果中局部区域误差控制 | 算法设计+对比 | 中 | 缺少独立消融时，作用量级需核查 |
| 实验 LIC/NIC 数据可用于提取 gelatin 的应力场和材料性质 | Section 5 | STAQ-DIC 位移/应变输入、Fig. 12-15 应力预测和误差统计 | 实验应用 | 中 | 没有外部真实应力 ground truth，主要证明可用性和内部一致性 |
| 两套框架构成黏弹性表征的高效替代方案 | Conclusion | 多场景验证和计算流程展示 | 综合论证 | 中 | 对异质、损伤和复杂加载外推时 claim 需收窄 |

证据链的总体特点是“先建立基线，再展示新增能力或失效边界”。强证据通常来自解析解、受控数值或明确对照；中等证据来自后验拟合、实验可行性展示或无外部 ground truth 的内部一致性。阅读时应特别区分“证明模型在本框架内成立”和“证明真实材料/临床/工程场景普遍成立”。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 定义 forward/inverse 问题与全场反演任务 | 为什么需要从变形反推应力/参数 | 把问题视觉化，是整篇方法路线的入口 | 是 |
| Fig. 2 | Deep-VM-FE/FD 选择流程和总体 workflow | 已知/未知本构应分场景处理 | 降低双算法结构的认知成本 | 是 |
| Table 1-2 | 材料参数、训练数据库或模型配置 | 训练覆盖多个水凝胶和加载条件 | 增强复现性 | 否 |
| Fig. 3 | Deep-VM-FE loss 与应力/材料参数预测验证 | 已知方程场景可学习黏弹参数 | 承担第一条算法正确性证据 | 是 |
| Fig. 4 | Deep-VM-FD stress prediction 框架 | 点式场序列加邻域信息可替代显式本构 | 解释输入输出和 pooling | 是 |
| Fig. 5-6 | 1D 蠕变与松弛模型验证 | FD 算法能处理典型黏弹历史 | 用简单 benchmark 建立可信度 | 是 |
| Fig. 7-8 | 2D 空化与单点加载场景 | 算法能扩展到非均匀二维场 | 从 1D 推进到复杂空间场 | 是 |
| Fig. 9-11 | LIC/NIC 实验装置和 DIC 场数据 | 实验输入不是理想合成数据 | 连接真实测量 | 是 |
| Fig. 12-15 | 实验应力预测、误差和材料性质统计 | 框架可用于 gelatin 空化实验表征 | 承担应用价值证据 | 是 |
| 核心公式 | 平衡方程、Kelvin-Voigt 应力分解、loss 和 pooling 表述 | 物理结构进入网络训练 | 防止论文沦为纯黑箱 | 否 |

图表顺序服务于递进论证：先给对象/几何/框架图，让读者知道问题如何被建模；再给基线或网格/训练验证，防御方法可信度；然后给核心结果图，证明新机制或新能力；最后用误差、参数、附录或对比图处理审稿人最可能追问的稳健性。由于 txt 只能读取图注和附近文字，所有颜色、曲线交叉、云图局部特征、误差热区和示意图箭头含义均需结合 PDF 图像核查。

## 11. 章节结构与篇章布局
- Abstract：压缩呈现问题、gap、方法、验证和意义，承担“让读者立刻知道为什么这篇是 JMPS”的功能。
- Introduction：先建立领域重要性，再分组处理前人，最后把 gap 收窄到本文可解决的问题。
- Related Work/Background：若没有独立 Related Work，则 Introduction 和理论背景共同承担；文献不是按年份铺陈，而是按功能服务 gap。
- Method/Theory/Model：Deep-VM-FE 与 Deep-VM-FD 两条路线；Kelvin-Voigt/neo-Hookean Kelvin-Voigt 表述；双通道应力分解；梯度 pooling；数值训练与 LIC/NIC 实验应用。
- Results：按由简单到复杂、由受控到真实或由解析到数值的顺序展开，保证每一步只增加一个主要困难。
- Discussion：把结果翻译成机制、设计准则、方法边界或未来任务，而不是重复曲线。
- Conclusion：回到一开始的 gap，并主动承认外推边界。
- 章节之间如何过渡：章节按问题分型展开：Section 2 先定义反问题；Section 3 专讲 Deep-VM-FE；Section 4 专讲 Deep-VM-FD 并从 1D 到 2D 验证；Section 5 才进入实验。最值得模仿的是先拆场景再设计算法，结构风险是实验部分的真实应力验证弱于数值部分。
- 哪一节最值得模仿：最值得模仿的是把复杂方法与具体 gap 一一对应的章节，而不是单纯公式或算法细节。
- 哪一节可能存在结构风险：风险通常出现在证据弱于 claim 的部分，例如实验外推、临床意义、普适机制或复杂几何结论。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Machine-learning-extraction-of-viscoelastic-mater_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：23
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Problem formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Deep-VM-FE algorithm decoupling temporal and spatial information | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Deep-VM-FE algorithm construction | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Analytical model for inertial microcavitation in viscoelastic materials to generate synthetic training datasets | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Training database generation and formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.4 Validation of Deep-VM-FE algorithm | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4 Deep-VM-FD algorithms for decomposition and reconstruction of field data | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Deep-VM-FD algorithm construction | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1.1 Gradient pooling | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1.2 Deep-VM-FD algorithm | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Validation based on 1D creep and relaxation numerical model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.2.2 Creep model training database generation and formulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.2.3 Creep model simulation results | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：Introduction 的段落推进是传统表征痛点 -> PINN 进展 -> 序列模型 -> 场/图像学习 -> 本文两条算法。Method 段落常以输入、网络结构、loss、训练数据库、验证目标为单位。Results 段落先报误差/一致性，再解释失败或偏差来源。可复用模板是：先说明某类数据为什么不足，再引入一个针对性网络组件，最后用 benchmark 显示该组件的必要性。
- Method 段落推进：先定义对象和变量，再写假设与方程/算法，随后说明为什么这样处理能消除某个不适定或机制不明问题。
- Results 段落推进：先交代测试条件，再报告趋势，再解释趋势对应的力学机制，最后说明该结果支撑哪个 claim。
- Discussion/Conclusion 段落推进：把“结果是什么”转成“因此该领域可以怎么理解/设计/反演”，同时给出边界。
- 常见段落开头方式：`To address this limitation...`、`We first consider...`、`The results show...`、`This behavior suggests...`。
- 常见段落收束方式：回到 gap、指出适用条件、引出下一组更复杂验证。
- 可复用段落模板：先写“已有方法在 A 条件下有效”，再写“但在 B 条件下缺少 C”，接着写“本文通过 D 将问题转化为 E”，最后用“这使得 F 可被验证/设计/估计”收束。

## 13. 文笔画像与语言习惯
- 整体语气：文笔是工程方法型，claim 强度偏积极但在结论中会主动降级。常见词组包括 efficient alternative、full-field deformation、rate-dependent behavior、spatial awareness、ground truth data、regulated stress。谨慎表达常用 feasibility、reasonable、future development。长句多用于罗列验证场景，短句用于给算法命名和定义适用条件。
- claim 强度：主体发现表达坚定，但常在范围上加限定；这种“结论强、边界清”的写法值得学习。
- 谨慎表达：常通过 within this framework、in the considered cases、suggest、potentially、future work 等词控制外推。
- 问题表达：偏好把困难写成 computationally expensive、not fully understood、remains challenging、assumptions may fail、direct measurement is not feasible 等可审稿的困难。
- 贡献表达：偏好 framework、exact solution、guideline、mechanism、benchmark、predictive foundation 等名词，而不是单纯 better。
- 机制表达：使用 attributed to、governed by、controlled by、results from、indicates a transition 等结构。
- 对比表达：通过 classical vs proposed、reference vs variant、affine vs non-affine、homogeneous vs heterogeneous、known vs unknown 等二元结构降低复杂度。
- 限定边界表达：作者通常会在 Discussion/Conclusion 把未覆盖的材料、几何、数据、物理过程或临床条件说清楚。
- 术语密度：较高，但术语会围绕少数主轴反复出现，而不是不断引入新概念。
- 长句/短句习惯：长句用于列举文献、条件和验证场景；短句用于命名贡献、定义 regime 或强调结论。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：stress(114)；material(104)；data(98)；fields(65)；viscoelastic(60)；model(58)；time(57)；displacement(53)；training(53)；validation(43)；properties(42)；algorithm(40)；learning(38)；deformation(35)；spatial(32)；cavitation(31)；loss(30)；models(29)；loading(29)；deep(28)
- 高频学术名词：stress(114)；material(104)；validation(86)；deformation(70)；fields(65)；model(58)；displacement(53)；properties(42)；analysis(38)；simulation(34)；cavitation(31)；conditions(25)；field(25)；materials(23)；relaxation(23)；results(20)
- 高频学术动词：shown(22)；developed(15)；predicted(15)；validated(7)；proposed(7)；demonstrate(7)；predict(6)；formulated(5)；capture(5)；demonstrated(4)；captured(3)；revealed(3)；compared(3)；show(3)；propose(3)；indicates(3)
- 高频形容词：viscoelastic(120)；material(104)；displacement(53)；experimental(40)；spatial(32)；elastic(30)；numerical(24)；constitutive(21)；lic(20)；boundary(19)；temporal(19)；neural(17)；gradient(17)；local(14)；rate-dependent(14)；nic(14)
- 高频副词/连接副词：directly(14)；respectively(13)；experimentally(10)；significantly(8)；physically(7)；specifically(5)；notably(4)；approximately(4)；consequently(4)；computationally(4)；accurately(4)；solely(4)；subsequently(4)；initially(4)；furthermore(3)；efficiently(3)
- 高频二词短语：stress fields(43)；material properties(32)；viscoelastic material(30)；deep learning(22)；time steps(15)；ground truth(13)；shear modulus(13)；boundary conditions(12)；agarose agarose(12)；displacement stress(12)；neural network(11)；deep-vm-fd algorithm(11)；time step(11)；loss function(10)；field data(10)；material model(10)
- 高频三词短语：viscoelastic material properties(8)；agarose agarose agarose(8)；viscoelastic material modeling(7)；viscoelastic material model(7)；displacement stress fields(7)；needle-induced cavitation nic(7)；deep learning viscoelastic(6)；learning viscoelastic material(6)；ground truth data(6)；deep learning algorithms(6)；shear modulus viscosity(6)；shear modulus kpa(6)

**主动、被动与句法**

- 被动语态估计次数：219
- `we + 动作动词` 主动句估计次数：6
- 名词化表达估计次数：1041
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：176
- 一般过去时线索：189
- 现在完成时线索：6
- 情态动词线索：28
- 时态判断：过去时相对突出，说明文本中实验/仿真步骤和已完成操作占比较高；现在时仍用于图表说明和一般性判断。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：viscoelastic(7)；material(6)；data(6)；learning(4)；texas(4)；austin(4)；materials(4)；deep(4)
- 1. Introduction：data(20)；material(18)；viscoelastic(15)；algorithms(10)；constitutive(9)；learning(9)；neural(9)；complex(8)
- 2. Problem formulation：material(18)；stress(11)；boundary(8)；deformation(7)；learning(7)；problem(6)；constitutive(6)；function(6)
- 3. Deep-VM-FE algorithm decoupling temporal and spatial information：algorithm(2)；material(2)；section(1)；proposes(1)；deep(1)；learning-based(1)；deep-vm-fe(1)；extract(1)
- 3.1. Deep-VM-FE algorithm construction：stress(13)；loss(12)；network(9)；learning(7)；elastic(7)；viscoelastic(6)；kelvin(5)；voigt(5)
- 3.2. Analytical model for inertial microcavitation in viscoelastic materials to generate synthetic training datasets：deformation(9)；tensor(7)；material(5)；model(5)；gradient(4)；bound(4)；agarose(4)；time(3)
- 3.3. Training database generation and formulation：agarose(12)；material(6)；system(6)；bound(6)；model(4)；qkv(4)；training(4)；tensor(3)
- 3.4. Validation of Deep-VM-FE algorithm：validation(6)；bd-(6)；system(5)；training(4)；set(3)；referred(3)；three-unknown-parameter(3)；cases(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：从 `黏弹性反演` 所在领域的可测/不可测、已知/未知或经典/未解矛盾切入。
- 可复用句型骨架：Despite extensive work on X, Y remains difficult to quantify because Z.
- 中文启发：先承认已有研究有效，再把缺口收窄到“特定场景下仍无法可靠完成的任务”。
### 14.2 方法与框架表达
- 原文表达模式：we propose/develop/formulate 后紧跟方法名称、适用前提和解决的具体困难。
- 可复用句型骨架：For cases where A is available, we use B; when A is unavailable, we instead construct C.
- 中文启发：方法不要只写工具名，要写清楚它接管了哪一段论证链。
### 14.3 结果与趋势表达
- 原文表达模式：results first confirm baseline validity, then reveal conditions/parameters under which new behavior appears.
- 可复用句型骨架：The results agree with the reference in regime A, whereas systematic deviations emerge when parameter B exceeds C.
- 中文启发：结果叙事按“先稳住基线，再展示偏离或新增机制”最容易说服审稿人。
### 14.4 机制解释表达
- 原文表达模式：This behavior can be attributed to / is governed by / results from 后接可解释机制。
- 可复用句型骨架：The transition from X to Y indicates that Z, rather than W, controls the observed response.
- 中文启发：机制句要避免只复述图中趋势，应指出哪个变量成为控制量。
### 14.5 贡献与意义表达
- 原文表达模式：This work provides/establishes/demonstrates 后接 framework、benchmark、guideline 或 foundation。
- 可复用句型骨架：The proposed framework establishes a link between measurable X and otherwise inaccessible Y.
- 中文启发：贡献最好写成“建立连接”“给出基准”“识别边界”，比泛泛说提高准确性更稳。
### 14.6 局限与未来工作表达
- 原文表达模式：future work should address / remains to be validated / within the present framework。
- 可复用句型骨架：The present results are confined to X; extending the approach to Y will require Z.
- 中文启发：局限要和方法边界对应，不能只写万能的更多实验。

## 15. 引用策略与文献使用
- 引用密度：引用集中在 Introduction 和实验技术铺垫，按传统表征、PINN、序列模型、operator learning、DIC/空化技术分组。经典文献用于奠定黏弹性和空化基础，近年文献用于证明 AI 力学路线活跃。引用风险在于 ML 文献覆盖广但直接对比有限，若强调算法优越性，最好补充运行时间、数据需求或消融对照。
- 引用主要集中位置：Introduction、理论背景、方法来源和实验/数据来源处最密；核心推导或结果解释处引用相对减少，以突出本文自洽证据。
- 经典文献用途：提供领域语言、经典模型、长期难题或物理来源。
- 近年文献用途：证明问题仍活跃、技术条件成熟、本文 gap 不是旧问题重复。
- 方法文献用途：说明工具来源和已知能力，避免把通用方法误写成本文独创。
- 对比/批判性引用：批评通常集中在适用范围、数据需求、成本、假设和验证不足，而不是否认前人贡献。
- gap 如何靠引用搭建：先展示已有路线已经覆盖了很多内容，再指出这些路线在本文边界下无法同时满足要求。
- references 暗示的研究共同体：该文献表明论文试图同时对力学核心社区和相邻应用/算法社区说话。
- 引用风险：若引用只证明“大背景重要”而不支撑“本文 gap 真实”，审稿人会要求更直接的最近工作对比。

## 16. 审稿人视角风险
- 最大攻击面：claim 的外推范围。审稿人会检查结果是否只在本文设定内成立，却被写成普适结论。
- claim 是否过强：主体 claim 基本可接受，但所有涉及工程、临床、跨材料或普适机制的表述都应保留限定。
- 证据是否不足：强证据部分通常足够；较弱部分多出现在真实实验 ground truth、微观机制直接观测、复杂几何普适性或临床域迁移。
- 方法是否可复现：需要回到公式、参数表、附录、训练设置、网格或数据处理细节；仅凭正文叙事不可完全复现。
- 对比是否充分：最接近前人工作是否被公平比较，是潜在审稿问题。
- 边界条件是否清楚：边界写得越清楚，文章越稳；若边界埋在方法细节里，读者容易误解贡献。
- 替代解释是否排除：需关注是否存在其他机制、其他网络组件、其他参数组合也能解释结果。
- 图表是否需要进一步核查：
- 实验中缺少独立全场真实应力，regulated stress 的一致性不能完全替代外部验证。
- 训练分布与实验材料同源性较强，跨材料、强非线性或损伤问题的泛化还未证明。
- gradient pooling 和网络结构的单独贡献需要结合 PDF 图和原文消融核查。
- 未知本构场景仍有隐含数据生成假设，审稿人可能要求说明 inverse mapping 的唯一性。

## 17. 可复用资产
- 可复用选题角度：
- 把一个大反问题拆成“已知物理”和“未知物理”两条路线。
- 用 workflow 图先告诉读者什么时候用哪个算法。
- 用解析/数值/实验三级证据分别承担正确性、复杂性和可用性。
- 把图像测量和应力反演之间的断裂作为 Introduction 的核心 gap。
- 可复用 gap 制造方式：承认前人有效，再锁定前人在某一数据类型、几何、尺度、机制或假设上的空白。
- 可复用论证链：背景 -> 文献分组 -> gap -> 方法/模型 -> 基线验证 -> 核心结果 -> 边界/风险。
- 可复用图表设计：对象示意图、方法 workflow、基线/对照图、核心结果图、误差/参数/敏感性图、附录消融或参数表。
- 可复用段落结构：一个段落只承担一个功能：造 gap、定义方法、解释机制、报告结果或限定边界。
- 可复用句型骨架：`We first establish a reference case...`; `We then systematically vary...`; `This comparison isolates...`; `The observed trend indicates...`; `The present framework is limited to...`。
- 可复用引用组织：按问题功能分组引用，而不是按时间线堆叠。
- 不宜直接模仿之处：如果没有同等强度的对照、解析、实验或附录消融，不宜模仿本文较强的 framework/benchmark/foundation 表述。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：写类似论文时，可以学习它如何把 AI 组件逐一绑定到力学困难：时间历史对应序列学习，空间非均匀对应邻域 pooling，已知方程对应物理分解，未知方程对应数据驱动。要避免的是在没有外部实验 ground truth 时把实验 claim 写得过强。
- 可以迁移到 Introduction 的写法：先写领域重要性，再写前人有效范围，最后用一个窄而硬的 gap 收束。
- 可以迁移到 Method 的写法：让每个方法模块对应一个明确困难，不要堆工具。
- 可以迁移到 Results/Discussion 的写法：先证明基线可信，再逐步增加复杂度；讨论时把结果转成机制、准则或边界。
- 需要避免的问题：避免过度复制原文句子；避免把拟合成功写成机制唯一；避免把数值/合成数据结果直接写成真实应用已解决。

## 19. 最终浓缩
- 这篇论文最值得学：最值得学的是问题分型和证据分层；最大风险是实验应力验证的间接性；三个动作是画 forward/inverse 对照、把算法适用条件写进缩写或流程图、用数值和真实实验分别支撑正确性与可用性。
- 这篇论文最大风险：最危险的是证据强度与结论外推不匹配；只要守住“本文边界内”的表达，论文说服力会强很多。
- 三个可迁移动作：第一，写出九节点论证链；第二，为每个核心 claim 配一张图或一个公式/表格；第三，在 Discussion 中主动写清楚不能外推到哪里。
