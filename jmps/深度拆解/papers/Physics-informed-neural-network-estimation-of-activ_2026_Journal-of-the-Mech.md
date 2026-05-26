# Physics-informed neural network estimation of active material properties in time-dependent cardiac biomechanical models

## 0. 读取说明
- 源 PDF：jmps\文献\Physics-informed-neural-network-estimation-of-activ_2026_Journal-of-the-Mech.pdf
- 源 TXT：jmps\文本\txt\Physics-informed-neural-network-estimation-of-activ_2026_Journal-of-the-Mech.txt
- 是否需要结合 PDF 图像核查：需要。本文拆解基于 PyMuPDF 抽取文本、图注、公式附近文字和元数据；所有曲线形状、云图细节、误差空间分布和示意图视觉层次均需结合 PDF 图像核查。
- 本文类型：PINN 反演方法 + 心肌主动材料参数估计 + scar detection 数值验证。
- 读取边界：上一轮 `jmps/拆解/papers` 仅作为辅助索引；本文件按全文结构、摘要、章节、图注、附录和 references 线索重新组织。

## 1. 基本信息与论文身份
- 题名：Physics-informed neural network estimation of active material properties in time-dependent cardiac biomechanical models
- 作者/机构：Matthias Höfler; Francesco Regazzoni; Stefano Pagani; Elias Karabelas; Christoph Augustin; Gundolf Haase; Gernot Plank; Federica Caforio；University of Graz/NAWI Graz; Medical University of Graz; BioTechMed-Graz; Politecnico di Milano
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213 (2026) 106603. doi:10.1016/j.jmps.2026.106603
- DOI：10.1016/j.jmps.2026.106603
- 关键词：Physics-informed neural networks,Cardiac biomechanics,Parameter estimation,Active material properties,Scar detection
- 研究对象：时间依赖心脏生物力学模型中的 active stress/contractility 参数场，尤其是空间异质 scar 和 grey zone。
- 研究尺度：3D 软组织连续体、时间依赖主动应力、成像可观测位移/应变、参数场分类。
- 方法类型：总拉格朗日心肌力学、Guccione 被动模型、主动应力模型、PINN 反演、空间/时间解耦网络、adaptive weighting、residual-based attention、TV 正则、Fourier features、Pareto front 分析。
- 证据类型：均质 quasi-static 与 time-dependent 案例、单 scar + grey zone、双 scar、噪声/低分辨率/slice data、Appendix B-G 消融、超参数和运行时间。
- 目标读者：计算生物力学、PINN 反问题、个体化心脏建模和医学图像参数估计社区。
- JMPS 风格定位：复杂 PINN 方法论文：把训练技巧写成力学反问题的必要组成，而不是黑箱调参。 全文 32 页，抽取文本约 17923 个英文词，结构目录线索包括：Physics-informed neural network estimation of active material properties in time-dependent cardiac biomechanical models；1 Introduction；2 Methods；2.1 Parameter estimation with PINNs；2.1.1 Governing equations in cardiac biomechanics；2.1.2 Solving inverse problems in cardiac biomechanics with PINNs；2.2 Optimisation scheme；2.3 Regularisation；2.3.1 Weight decay；2.3.2 Regularisation for the active stress network；2.4 Hyperparameter tuning；2.4.1 Analysis of the apparent pareto fronts；2.4.2 Adaptive weighting；2.4.3 Residual-Based attention mechanism。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要采用“痛点 -> 方法分型/模型建立 -> 验证范围 -> 意义”的 JMPS 常见结构，不先铺过多背景，而是快速给出研究对象和方法承诺。
- 背景句承担什么：心肌主动收缩性质连接电生理与力学，是诊断和个体化治疗的重要参数。
- gap 句承担什么：临床难以直接测主动 contractility，只能从 MRI/超声等位移和应变数据间接估计；传统优化昂贵且常降维。
- 方法句承担什么：作者提出 PINN 框架，结合自适应权重、残差注意力、正则、Fourier features 和空间-时间网络来反演 active stress。
- 结果句承担什么：在均质、时间依赖和异质 scar 场景中，方法能在噪声和高空间分辨率下重构主动应力场，并用 Pareto front 分析权重影响。
- 意义句承担什么：为从成像数据识别心肌异质性和 scar 提供方法基础，但目前主要是 in silico 验证。
- 一句话主张：经过损失权重、边界、正则和频率特征专门设计的 PINN，可从有限位移/应变数据中反演时间依赖心肌主动应力参数场，并用于 scar detection。
- 3-5 个核心关键词：PINN；心脏生物力学；主动应力；参数反演；scar detection；Pareto front

## 3. 选题层深拆
- 问题来源：选题来自临床可观测量与关键材料参数之间的断裂：成像可给位移/应变，却不能直接给 active contractility。作者将这个医学难题翻译成受平衡方程、边界条件和参数正则约束的高维反问题。
- 问题为什么重要：它连接了一个高价值应用目标和一个力学上仍不完全可控的变量；如果该变量能被测量、预测或设计，后续材料表征、结构设计或生物医学判断都会更可操作。
- 问题为什么现在值得做：一方面，近年实验、计算或机器学习工具让以前难以观测/求解的量变得可处理；另一方面，已有模型的局限已经被足够多文献暴露，形成了可被审稿人接受的切入口。
- 问题边界：当前结果基于 FEM ground truth 和简化几何/边界，主要估计主动参数；被动参数、纤维方向、几何和边界压力大多被视作已知或可控。真实临床图像、配准误差和电-机械耦合是未来方向。
- 选题的 JMPS 味道：它不是停留在应用演示，而是追问“为什么这个响应会出现、这个假设何时成立、这个反问题如何被物理约束”。这种从现象回到机制/模型/证据闭环的写法，是 JMPS 的核心味道。
- 选题可迁移性：可迁移到任何“可测量 X 与关键但不可直接获得 Y 之间存在断裂”的论文：先证明 Y 重要，再说明传统路线的成本或偏置，最后提出受力学约束的桥接框架。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：作者不是按年份堆文献，而是按问题功能划分：哪些工作解释了现象，哪些提供了模型，哪些给出了数据或设计工具，哪些留下了当前缺口。
- 主要研究流派/方法路线：
- 数据同化和 PDE-constrained optimisation：可估计 contractility，但成本高、先验强、常用区域参数。
- 心肌主动应力和被动本构模型：提供物理方程与组织各向异性基础。
- PINN 和软组织反演：已有被动、2D 或简化超弹性问题，缺少 active/time-dependent/3D anisotropic 场景。
- PINN 训练改良技术：自适应权重、RBA、Fourier features、正则和 Pareto front 用于处理 loss 竞争、频谱偏置与不适定性。
- 每类研究解决了什么：前人分别解决了基本物理语言、经典模型、数值或实验方法、以及部分应用验证；因此本文不需要重建整个领域，只需说明这些路线拼在一起时仍缺少最后一环。
- 每类研究留下什么不足：不足通常不是“完全不能用”，而是“在本文关心的边界条件、几何、数据类型或机制层级下不够”。这种写法比直接否定前人更稳。
- 本文站在哪条线上：本文站在最接近的机制/模型/反演路线之后，把前人留下的假设、尺度或数据缺口具体化。
- 最接近前人工作：从全文看，最接近的是那些已经提出相近模型、方法或实验事实但没有系统处理本文特定 gap 的工作；作者通过对比适用前提而不是简单性能排名来定位自己。
- 是否公平处理前人：总体公平。它承认前人有效范围，再指出本文要处理的是其未覆盖的场景。这种姿态降低了“为创新而贬低文献”的风险。

## 5. Gap 制造机制
- 明示 gap：明示 gap 是尚缺少用于 active cardiac biomechanics 参数估计的 ML/PINN 方法；隐含 gap 是 vanilla PINN 不足以解决这个问题，因为观测损失、PDE 残差、边界条件和参数正则之间存在强烈权衡。
- 隐含 gap：更深层的缺口是“已有工具无法同时满足物理可解释、可计算、可验证和可迁移”四个要求；本文通过一个更窄但更闭合的问题来处理它。
- gap 类型：方法 gap、机制 gap、验证 gap 或假设有效域 gap的组合；具体取决于本文对象，但都不是单纯“没人做过”。
- gap 证据来自哪里：来自 Introduction 的文献分组、方法章节中被保留/放弃的假设、以及 Results 中专门设计的 benchmark 或参数扫描。
- gap 是否足够窄：足够窄。作者没有声称解决整个领域问题，而是把范围限制在明确材料、几何、数据类型或模型框架内。
- gap 是否足够重要：重要性来自两端：一端是应用/实验/设计需求，另一端是理论或模型上的未闭合。两端都存在时，JMPS 审稿人更容易接受。
- 如果我是审稿人会如何追问：我会问最接近前人方法是否真的不能处理该场景，本文的证据是否覆盖了 gap 中最困难的边界，以及结论有没有超出验证范围。

## 6. 创新性判断
- 作者声称的贡献：创新中等偏强。PINN 不是新概念，贡献在于面向主动心肌反演的整套训练系统：空间/时间解耦、Pareto 权重分析、scar 参数场正则、Fourier features 和分类阈值评估共同构成可审稿的方法学。
- 我判断的真实创新：真实创新不只是提出一个名字或公式，而是重排了问题边界：把原本混在一起的物理、数据、几何或机制因素拆开，让某个不可见变量变得可计算或可检验。
- 创新类型：理论机制、方法流程、假设审计、实验反演或本构表达中的一种或多种组合。
- 创新强度：相对较强的部分在于论证闭环，而不一定在单个工具。若单独拿出网络、FE 或拟合公式，未必全新；但放在本文问题链条里，它们承担了清楚的新功能。
- 创新必要性：必要，因为不引入该框架，论文关心的 gap 只能靠经验拟合、理想化假设或不可验证叙事维持。
- 创新与证据匹配度：主体证据能支撑“在本文边界内有效”；对更广泛材料、临床、复杂几何或真实多物理场的外推需要谨慎。
- 容易被挑战的创新点：最容易被问的是：新方法/模型相对最近前人的不可替代性在哪里？新增参数或算法组件是否只是提高拟合自由度？是否有消融、对照或解析基准证明？

## 7. 论证链条复原
背景：精密医学需要 patient-specific contractility -> 文献：传统优化和数据同化已有但昂贵/降维 -> gap：主动、3D、各向异性、时间依赖的 PINN 反演缺位 -> 问题：如何从稀疏位移/应变重构 Sa 场 -> 方法：PINN loss + 正则 + 权重/注意力 + Fourier features -> 证据：均质、时间依赖、单 scar、双 scar 和附录消融 -> 发现：适当训练策略可重构参数并检测 scar -> 机制：物理残差约束 admissibility，观测损失提供数据锚，正则/频率特征控制空间细节 -> 意义：通向临床成像反演。

这条链条的写作价值在于：每个后续部分都回到前一个必要性。方法不是凭空出现，而是对 gap 的直接回应；图表不是展示材料，而是为特定 claim 服务；结论也没有离开开头的问题。若要迁移到自己的论文，可先写出同样的九节点链条，再检查每个节点是否有文本或图表支撑。

## 8. 方法/理论/模型细拆
- 方法总框架：总拉格朗日心肌力学、Guccione 被动模型、主动应力模型、PINN 反演、空间/时间解耦网络、adaptive weighting、residual-based attention、TV 正则、Fourier features、Pareto front 分析。
- 关键概念：PINN；心脏生物力学；主动应力；参数反演；scar detection；Pareto front。这些概念不是名词列表，而是构成论证的“承重墙”：去掉任何一个，问题边界都会改变。
- 关键变量/参数：全文围绕可观测量、内部变量、材料/几何参数、损失或能量项、以及输出指标组织。具体变量需结合原文公式逐项核查。
- 核心假设：当前结果基于 FEM ground truth 和简化几何/边界，主要估计主动参数；被动参数、纤维方向、几何和边界压力大多被视作已知或可控。真实临床图像、配准误差和电-机械耦合是未来方向。 这些假设使问题可解，也限定了结论外推。
- 边界条件：文本给出了对应几何、加载、数据或模型边界；涉及图像、曲线和场分布处需结合 PDF 核查。
- 方法步骤：
- PINN 同时逼近位移场和主动参数，loss 包含观测、PDE 残差、边界条件、初始/约束和正则项。
- 时间依赖问题采用空间网络与时间网络解耦，避免直接在高维时空中训练一个过重网络。
- Pareto front 用于解释损失权重权衡；TV/边界正则与 Fourier features 用于 scar 场的锐界和高频结构识别。
- 复现信息：元数据、章节标题、图注、表格、附录和参数表均提供复现线索。若要真正复现，应回到 PDF 中的公式编号、网格/训练/拟合参数和附录表。
- 方法复杂度是否合理：合理。复杂度与 gap 的难度相匹配；论文也通过对照、基准或参数扫描证明复杂度不是纯装饰。
- 方法与 gap 的对应关系：方法中的每个关键模块都对准一个缺口：物理约束对准不适定性，参数扫描对准假设有效域，微观模型对准机制解释，实验/数值 benchmark 对准可验证性。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 主动 contractility 可从位移/应变数据通过 PINN 间接反演 | Sections 2-3 | 均质 quasi-static 和 time-dependent FEM 案例 | in silico 反演 | 强 | 临床真实数据尚未验证 |
| loss 权重选择是重构质量的关键 | Section 2.4/Fig. 4 | apparent Pareto fronts 展示 OBS 与 PDE 的 trade-off | 超参数分析 | 强 | Pareto 外观依赖采样和训练设置 |
| 自适应权重和 RBA 能提升训练稳定性 | Methods + Appendix B | 不同 weighting/RBA 结果比较 | 消融 | 中-强 | 需要看附录图确认量级 |
| 主动应力正则对 scar 场重构必要 | Section 2.3/Appendix C | 无正则与有正则重建对比 | 消融 | 强 | 正则系数可能影响边界厚度 |
| Fourier features 改善空间异质 scar 识别 | Appendix G | 不同频率参数下单 scar/双 scar 误分类变化 | 消融 | 中 | 过高频可能引入噪声或伪影 |
| 方法可用于 tissue inhomogeneity 和 scar detection | Section 3.2 | 单 scar + grey zone、双 scar 阈值化重建 | 应用验证 | 中 | 阈值、噪声和真实图像域差距是风险 |

证据链的总体特点是“先建立基线，再展示新增能力或失效边界”。强证据通常来自解析解、受控数值或明确对照；中等证据来自后验拟合、实验可行性展示或无外部 ground truth 的内部一致性。阅读时应特别区分“证明模型在本框架内成立”和“证明真实材料/临床/工程场景普遍成立”。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 2 | 均质测试的 FEM 位移 ground truth | 反演输入来自可观测位移 | 建立 benchmark | 是 |
| Fig. 3 | 训练/测试 loss 演化 | 训练过程可收敛并需观察 OBS/PDE | 支持方法稳定性 | 是 |
| Fig. 4 | apparent Pareto fronts | 权重选择决定数据拟合与物理残差平衡 | 全文方法可信度核心图 | 是 |
| Fig. 5 | 时间依赖 PINN 解的时间演化 | 方法能处理 time-dependent active stress | 从 quasi-static 推进到动态 | 是 |
| Fig. 6 | one-scar FEM ground truth 位移 | 异质性重建输入 | 为 scar 场验证铺垫 | 是 |
| Fig. 7 | single scar + grey zone 主动应力重建 | 能识别组织异质性 | 应用价值核心 | 是 |
| Fig. 8-9 | two-scar 位移 ground truth 与阈值重建 | 多病灶场景可检测 | 提高复杂性 | 是 |
| Appendix B-G/Figs. B.10-G.21 | 权重、正则、边界、阈值和 Fourier features 消融 | 训练组件并非随意堆叠 | 防御审稿质疑 | 是 |
| 核心公式 | 力平衡、主动应力、PINN loss、正则和约束 | 物理与学习耦合 | 避免黑箱 | 否 |
| Appendix H-I | 超参数和硬件运行时间 | 可复现性和成本透明 | 工程可信度 | 否 |

图表顺序服务于递进论证：先给对象/几何/框架图，让读者知道问题如何被建模；再给基线或网格/训练验证，防御方法可信度；然后给核心结果图，证明新机制或新能力；最后用误差、参数、附录或对比图处理审稿人最可能追问的稳健性。由于 txt 只能读取图注和附近文字，所有颜色、曲线交叉、云图局部特征、误差热区和示意图箭头含义均需结合 PDF 图像核查。

## 11. 章节结构与篇章布局
- Abstract：压缩呈现问题、gap、方法、验证和意义，承担“让读者立刻知道为什么这篇是 JMPS”的功能。
- Introduction：先建立领域重要性，再分组处理前人，最后把 gap 收窄到本文可解决的问题。
- Related Work/Background：若没有独立 Related Work，则 Introduction 和理论背景共同承担；文献不是按年份铺陈，而是按功能服务 gap。
- Method/Theory/Model：总拉格朗日心肌力学、Guccione 被动模型、主动应力模型、PINN 反演、空间/时间解耦网络、adaptive weighting、residual-based attention、TV 正则、Fourier features、Pareto front 分析。
- Results：按由简单到复杂、由受控到真实或由解析到数值的顺序展开，保证每一步只增加一个主要困难。
- Discussion：把结果翻译成机制、设计准则、方法边界或未来任务，而不是重复曲线。
- Conclusion：回到一开始的 gap，并主动承认外推边界。
- 章节之间如何过渡：结构偏方法手册：Section 2 非常长，先定义方程和 PINN，再给优化、正则、权重、实现细节；Section 3 结果从均质到异质；Section 4 讨论边界和临床前景；附录承担大量消融。最值得模仿的是把训练技巧放在 Methods 中解释失败模式，而不是在 Results 中临时补救。结构风险是组件太多，若没有附录消融会显得像调参堆叠。
- 哪一节最值得模仿：最值得模仿的是把复杂方法与具体 gap 一一对应的章节，而不是单纯公式或算法细节。
- 哪一节可能存在结构风险：风险通常出现在证据弱于 claim 的部分，例如实验外推、临床意义、普适机制或复杂几何结论。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Physics-informed-neural-network-estimation-of-activ_2026_Journal-of-the-Mech.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：27
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Parameter estimation with PINNs | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.1 Governing equations in cardiac biomechanics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.1.2 Solving inverse problems in cardiac biomechanics with PINNs | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Optimisation scheme | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Regularisation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3.1 Weight decay | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3.2 Regularisation for the active stress network | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.4 Hyperparameter tuning | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4.1 Analysis of the apparent pareto fronts | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.4.2 Adaptive weighting | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4.3 Residual-Based attention mechanism | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Implementation details | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：Introduction 从 precision medicine 到 contractility，再综述传统估计和 PINN 文献，最后列出本文比被动/2D/线性反演更复杂。Method 段落每引入一个技巧，都说明其解决的优化病症。Results 段落先展示 ground truth，再展示重建，再讨论噪声、分辨率或阈值。可复用模板是：反问题不是一个 loss 最小化问题，而是数据保真和物理可容许性的权衡问题。
- Method 段落推进：先定义对象和变量，再写假设与方程/算法，随后说明为什么这样处理能消除某个不适定或机制不明问题。
- Results 段落推进：先交代测试条件，再报告趋势，再解释趋势对应的力学机制，最后说明该结果支撑哪个 claim。
- Discussion/Conclusion 段落推进：把“结果是什么”转成“因此该领域可以怎么理解/设计/反演”，同时给出边界。
- 常见段落开头方式：`To address this limitation...`、`We first consider...`、`The results show...`、`This behavior suggests...`。
- 常见段落收束方式：回到 gap、指出适用条件、引出下一组更复杂验证。
- 可复用段落模板：先写“已有方法在 A 条件下有效”，再写“但在 B 条件下缺少 C”，接着写“本文通过 D 将问题转化为 E”，最后用“这使得 F 可被验证/设计/估计”收束。

## 13. 文笔画像与语言习惯
- 整体语气：文笔方法推进型，常用 robust and accurate reconstruction、limited displacement and strain data、spatially-varying active properties、clinical setting、to the best of our knowledge。claim 在方法上较强，在临床上用 potentially、opens a pathway 等谨慎词。
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

- Top 高频词：network(114)；parameter(99)；active(90)；displacement(84)；test(83)；data(82)；case(77)；stress(74)；boundary(69)；pde(64)；loss(61)；training(49)；tissue(47)；eld(46)；error(45)；seeds(45)；fourier(43)；points(43)；phase(43)；pinn(42)
- 高频学术名词：parameter(99)；displacement(84)；stress(74)；solution(70)；section(42)；results(41)；analysis(40)；estimation(39)；regularisation(36)；condition(34)；method(32)；reconstruction(32)；conditions(30)；strain(28)；performance(28)；approach(24)
- 高频学术动词：shows(26)；shown(12)；show(11)；evaluated(10)；proposed(8)；estimate(8)；indicates(7)；compare(5)；evaluate(5)；derived(5)；indicate(5)；compared(4)；predicted(4)；investigate(3)；capture(3)；demonstrated(3)
- 高频形容词：active(90)；displacement(84)；boundary(69)；homogeneous(44)；relative(40)；neural(37)；heterogeneous(34)；erent(30)；time-dependent(28)；quasi-static(23)；total(21)；constant(17)；additional(17)；adaptive(15)；computational(15)；clinical(14)
- 高频副词/连接副词：respectively(25)；however(19)；potentially(10)；notably(10)；particularly(9)；approximately(8)；therefore(7)；exactly(7)；randomly(7)；typically(6)；accurately(6)；incorrectly(6)；weakly(4)；consequently(4)；finally(4)；cantly(4)
- 高频二词短语：active stress(68)；test case(44)；test cases(31)；relative error(31)；displacement network(29)；stress network(28)；boundary conditions(24)；fourier features(23)；adam phase(22)；neural network(21)；dirichlet boundary(21)；phase avg(21)；fourier feature(20)；network fourier(20)；displacement data(18)；data points(18)
- 高频三词短语：active stress network(28)；avg time one(12)；epoch phase avg(12)；phase avg total(12)；avg total training(12)；total training time(12)；shows relative error(11)；displacement data points(11)；network layer widths(10)；network fourier features(10)；network fourier feature(10)；learning rate adam(10)

**主动、被动与句法**

- 被动语态估计次数：134
- `we + 动作动词` 主动句估计次数：18
- 名词化表达估计次数：1313
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：273
- 一般过去时线索：62
- 现在完成时线索：11
- 情态动词线索：47
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：active(7)；cardiac(6)；stress(4)；biomechanics(4)；physics-informed(3)；neural(3)；graz(3)；austria(3)
- 1. Introduction：data(17)；active(13)；properties(11)；estimation(10)；cardiac(9)；based(8)；contractility(7)；models(6)
- 2. Methods：tissue(3)；describe(2)；active(2)；cardiac(2)；estimation(2)；designed(2)；section(1)；comprehensive(1)
- 2.1. Parameter estimation with PINNs：work(1)；adopt(1)；pinn(1)；framework(1)；estimate(1)；active(1)；stress(1)；parameters(1)
- 2.1.1. Governing equations in cardiac biomechanics：consider(7)；stress(6)；active(6)；tissue(5)；model(5)；formulation(4)；point(4)；tensor(4)
- 2.1.2. Solving inverse problems in cardiac biomechanics with PINNs：pde(17)；obs(13)；bcn(13)；bcd(12)；parameter(8)；loss(7)；case(6)；max(5)
- 2.2. Optimisation scheme：adam(4)；bfgs(4)；optimisation(3)；iterations(3)；eqs(2)；perform(2)；optimiser(2)；followed(2)
- 2.3. Regularisation：network(2)；regularisation(1)；applied(1)；displacement(1)；active(1)；stress(1)；depending(1)；test(1)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：从 `PINN` 所在领域的可测/不可测、已知/未知或经典/未解矛盾切入。
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
- 引用密度：引用覆盖临床 contractility 估计、MRI/echo 数据同化、PDE-constrained optimisation、PINN 基础与软组织反演、训练稳定技术。gap 通过“现有方法多为被动、2D、线性或标准超弹性”搭建。风险是 PINN 文献更新快，类似论文应确认最新方法和 benchmark。
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
- 从 FEM 合成数据到真实医学图像存在域差距，包括噪声、配准、边界和几何误差。
- 被动参数和纤维方向若未知，会与主动参数发生可辨识性耦合。
- scar 阈值和 TV 正则可能影响 grey zone 边界，分类指标需谨慎解释。
- 训练成本不低，临床实时性 claim 需有运行时间和硬件支持。

## 17. 可复用资产
- 可复用选题角度：
- 用 Pareto front 解释 PINN loss 权重，而不是只报最佳参数。
- 把反演参数场进一步转为 scar detection 下游任务。
- 用附录系统防御训练组件：权重、正则、边界、Fourier features、阈值。
- 将临床不可测量转化为 physics-informed inverse problem。
- 可复用 gap 制造方式：承认前人有效，再锁定前人在某一数据类型、几何、尺度、机制或假设上的空白。
- 可复用论证链：背景 -> 文献分组 -> gap -> 方法/模型 -> 基线验证 -> 核心结果 -> 边界/风险。
- 可复用图表设计：对象示意图、方法 workflow、基线/对照图、核心结果图、误差/参数/敏感性图、附录消融或参数表。
- 可复用段落结构：一个段落只承担一个功能：造 gap、定义方法、解释机制、报告结果或限定边界。
- 可复用句型骨架：`We first establish a reference case...`; `We then systematically vary...`; `This comparison isolates...`; `The observed trend indicates...`; `The present framework is limited to...`。
- 可复用引用组织：按问题功能分组引用，而不是按时间线堆叠。
- 不宜直接模仿之处：如果没有同等强度的对照、解析、实验或附录消融，不宜模仿本文较强的 framework/benchmark/foundation 表述。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：写复杂 PINN 论文时，要把每个 trick 写成对不适定性的回应：权重解决 loss 竞争，正则解决参数场不唯一，Fourier features 解决频谱偏置，精确边界解决边界伪差。没有消融就不要堆组件。
- 可以迁移到 Introduction 的写法：先写领域重要性，再写前人有效范围，最后用一个窄而硬的 gap 收束。
- 可以迁移到 Method 的写法：让每个方法模块对应一个明确困难，不要堆工具。
- 可以迁移到 Results/Discussion 的写法：先证明基线可信，再逐步增加复杂度；讨论时把结果转成机制、准则或边界。
- 需要避免的问题：避免过度复制原文句子；避免把拟合成功写成机制唯一；避免把数值/合成数据结果直接写成真实应用已解决。

## 19. 最终浓缩
- 这篇论文最值得学：最值得学的是把训练工程写成可解释方法学；最大风险是真实临床域差距；三个动作是做 Pareto 权重图、做组件消融、把参数反演连接到下游诊断任务。
- 这篇论文最大风险：最危险的是证据强度与结论外推不匹配；只要守住“本文边界内”的表达，论文说服力会强很多。
- 三个可迁移动作：第一，写出九节点论证链；第二，为每个核心 claim 配一张图或一个公式/表格；第三，在 Discussion 中主动写清楚不能外推到哪里。
