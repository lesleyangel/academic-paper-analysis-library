# Real-time reconstruction of thermal fields from sparse sensors with a tensorized Fourier neural operator

## 0. 读取说明

本文拆解基于 `801/文本/txt/Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa.txt` 的 PyMuPDF 全文抽取，并参考 `801/文本/metadata/Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa.json` 中的题名、期刊、页码和目录信息。txt 存在双栏 PDF 抽取后的串栏现象，尤其是公式、表格和参考文献附近会把左右栏内容并排拼接；因此本文对图像形态、云图细节、表格完整数值和公式排版均标注“需要 PDF 图像复核”。主体使用中文分析，不长段复制原文，只保留少量关键词，如 TFNO、replication-masking、low-fidelity、recent measurements 等。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Problem description, 3 Methods, 4 Heat flux distribution reconstruction for a blunt cone, 5 Temperature distribution reconstruction for a C/SiC plate, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Real-time reconstruction of thermal fields from sparse sensors with a tensorized Fourier neural operator。
- 作者：Huang Wenyu, Li Chunna, Gou Jianjun, Ma Xiaobing, Gong Chunlin。
- 期刊与年份：International Journal of Heat and Fluid Flow, 120, 2026, Article 110341。
- DOI：10.1016/j.ijheatfluidflow.2026.110341。
- 关键词：Sparse sensor reconstruction；Tensorized Fourier neural operator；Multi-fidelity data fusion；Aerothermal prediction。
- 论文类型：面向高超声速热监测的机器学习反问题方法论文，带两类算例验证。
- 研究对象：从稀疏热流/温度传感器测量重构完整热场，包括钝锥 Mach 10.6 表面热流场和 C/SiC 板辐射加热瞬态温度场。
- 核心方法：TFNO 作为场重构主干；replication-masking 扩展传感器布局泛化；融合飞行状态、低保真热场和高保真稀疏传感器；瞬态场用最近历史测量增强输入。
- 主要证据：两类任务、不同传感器数量、不同输入组合、不同低保真质量、传统插值/神经网络/operator backbone 对比、已知/遮蔽传感点时程验证。
- 目标读者：高超声速热防护与热管理研究者、反热传导/稀疏测量重构研究者、神经算子在工程热流场中落地的读者。

这篇论文的身份不只是“一个新网络用于热场预测”，而是“将稀疏飞行传感、低保真物理先验和神经算子组合成实时机载热场重构框架”。它同时服务两个社区：一边是 inverse heat transfer 与 thermal monitoring，一边是 neural operator / multi-fidelity learning。文章的工程卖点是从 9-126 个传感器重构 2400-3700 节点场，平均相对误差低于 2% 或 1.5%，单场推理约 0.08 s。

## 2. 摘要与核心信息提取

一句话主张：高超声速飞行器关键热区难以密集布设传感器，本文用 TFNO 从少量、可变布局的传感器测量中实时重构完整热流/温度场，并通过 masking、多源融合和历史测量显著提升稀疏重构精度与时序一致性。

摘要的叙事是标准的“工程必要性 -> 观测受限 -> 方法增强 -> 双算例验证 -> 数值指标”。开头先说实时监测 heat flux 与 temperature 对 safety、control 和 thermal management 关键；随后指出飞行中只能布置 sparse sensors，leading edges 等极端区域甚至无法布设。接着方法不是单点抛出 TFNO，而是列出三个增强：随机遮蔽重复样本以缓解测量稀少；若有 state information，则连同 low-fidelity data 一起输入；若是 time-continuous reconstruction，则加入 recent measurement history。

最核心的信息有三层。第一层是反问题定义：从 J 个传感器读数映射到 P 个网格节点的完整场。第二层是物理/数据融合：低保真场不要求完全准确，但能提供空间形状先验，飞行状态能校准全局量级，高保真传感器约束局部真实值。第三层是实时约束：模型的价值不是离线重构一幅好看的云图，而是 0.08 s 左右的单场推理，使热管理或控制系统有在线更新可能。

摘要中可复用的贡献组织方式是“同一个框架，三个使用场景”：任意传感布局、低保真可用、时间连续监测。这样比单纯写“提出一种 TFNO 方法”更强，因为它把实际部署中会遇到的三个问题都提前放进框架。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Real-time-reconstruction-of-thermal-fields-from-sp_2026_International-Journa.md`。

中文译文：

> 实时监测高超音速飞行器的热通量和温度对于安全、控制和热管理至关重要。然而，在飞行中，传感通常仅限于稀疏分布的传感器，这会产生不完整的空间覆盖和不完整的信息。在极端环境中，例如前体前缘，情况变得更具挑战性，在这些环境中，传感器仪器不切实际，并且关键热区域仍然无法测量。为了解决这些问题，我们开发了一种基于张量傅里叶神经算子（TFNO）的增强方法，该方法可以从稀疏测量中重建完整的热场。首先，为了缓解测量的缺乏，我们提出了一种复制掩蔽策略，该策略通过随机遮挡重复副本中的一小部分传感器读数来扩展训练集。其次，如果状态信息可用，我们将其与相应的低保真数据一起输入模型以改进重建。第三，对于时间连续重建，我们用最近的测量历史来增加输入，以利用时间相干性。我们在两个任务上评估了所提出的方法：10.6 马赫高超音速流条件下的钝锥表面热通量重建和受辐射加热的 C/SiC 复合板的瞬态温度重建。
>
> 只需 9-126 个传感器，它就能在 2,400-3,700 个节点的网格上重建场，平均相对误差低于 2%，平均推理延迟约为 0.08 秒。 （续）
>
> BPNN 反向传播神经网络
>
> E 分解误差张量 F 傅里叶变换算子 J 传感器数量 j 传感器索引 K 时间步数 k 时间步长索引 L 张量维数 N 矩阵数量 P 网格节点数 p 节点索引 q 热通量 R 张量秩 R 模型参数 T 温度 t 时间 U 投影矩阵 v 特征表示
>
> （下一栏继续）
>
> （下页继续）
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自高超声速在线热监测的硬约束：全场热流/温度对结构安全、热防护、热管理和控制都重要，但真实飞行中不能像地面实验那样使用红外热成像或温敏涂料，也不能在前缘、烧蚀区和强热流区域密集埋设传感器。传感器布设本身会破坏表面光顺、结构强度和热防护完整性。因此，稀疏测量不是数据集不够大的偶然困难，而是飞行器应用场景内生的约束。

作者把大问题收束为三个可研究子问题。第一，从少量传感器读数重构完整场，这是空间反问题。第二，当飞行状态和低保真场可获得时，如何让这些不完全可靠的信息帮助高保真重构，这是多保真融合问题。第三，对于瞬态温度场，如何利用最近历史而不是把每一帧孤立重构，这是时序一致性问题。

选题价值也分三层。工程价值是实时热安全评估：如果能在飞行中从有限传感器恢复热场，就能服务热管理、故障诊断和控制。方法价值是为神经算子找到一个强需求场景：传统插值缺少物理结构，传统优化反演太慢，普通神经网络易产生局部伪影，FNO/TFNO 可通过频域全局卷积表达场的整体结构。写作价值是把“数据不足”转成“传感器布置可变、低保真可用、实时性严格”的具体工程约束。

论文切入点很聪明：没有把“传感器稀疏”写成简单的压缩感知，也没有把“高超声速热场”写成纯 CFD 替代，而是把传感、低保真物理模型和神经算子放在同一个在线重构流程里。这样可以同时吸收 inverse heat transfer、multi-fidelity modeling 和 neural operator 三组文献资源。

## 4. 领域位置与文献版图

Introduction 将已有热反问题方法分成三类：optimization-based、data-driven、physics-aware。优化类通过反复调整边界条件，使前向模型在传感点处匹配观测，优点是物理一致性强，缺点是在线速度慢、需要正则化且反复求解前向问题。数据驱动类用测量-场样本训练映射，在线速度快，但离线成本高，采样包络外泛化受限。physics-aware 类把方程残差、边界条件和数据误差放进训练目标，能降低数据需求，但训练慢、对架构和超参数敏感，场景变化时常需重训。

这三分类并不是平铺综述，而是逐步制造本文站位。作者先承认每类方法有效，再指出它们无法同时满足 real-time、high-definition 和 generalization from limited data。尤其对高超声速热管理而言，问题不是只要在传感点精确，而是要在未测热区也有空间连贯的全场重构；不是只要固定传感器布局可用，而是要面对任意或失效传感器布局。

在神经网络文献中，作者提及 BPNN、CNN、GAN、PINN、DeepONet、FNO 等，实际站位是“用 operator learning 做场到场映射，但通过 Tucker tensorization 控制参数规模，并用低保真/历史输入补足稀疏传感信息”。它继承 FNO 的全局谱卷积能力，也继承多保真建模的“粗场给空间先验、高保真传感器给局部校准”思路。

本文位于三个版图交叉处：inverse heat transfer 提供问题合法性；aerothermal prediction 提供工程场景；neural operator 提供模型工具。这个交叉定位很重要，因为单看神经算子，TFNO 未必是全新算法；但放到稀疏传感热场重构和机载实时热管理中，就形成了更明确的应用贡献。

## 5. Gap 制造机制

文章制造 gap 的方式不是“没人做过 TFNO”，而是“已有路线不能同时满足三项工程要求”。第一是实时性 gap：优化反演和物理约束反演往往要多次调用前向模型，难以在线。第二是场完整性 gap：许多方法只预测边界值、传感点附近值或简化形式的边界条件，不能恢复完整高分辨率空间场。第三是泛化 gap：纯数据驱动模型对固定传感器布局和训练包络依赖强，当传感器位置变化或部分失效时容易退化。

作者还把 gap 进一步具体化到高超声速场景：关键热区正是最不容易布设传感器的区域，导致观测区域与风险区域错位。这个设定让“从稀疏传感器外推到未测高热区”显得必要而非炫技。同时，低保真 CFD 或工程算法在实际系统中常常存在，虽然不够准确，却可提供热场形状。已有研究要么不用这类信息，要么没有系统判断低保真数据何时有用。

这个 gap 的可信度较强，因为作者用文献分类和问题描述双重支撑：文献分类指出传统方法的速度/泛化限制，问题描述指出飞行器传感布设的物理限制。可被追问之处是“arbitrary sensor layouts”的真实范围：论文通过 masking 和不同 meridian 遮蔽验证布局鲁棒性，但这不等于所有任意布局都可泛化；真实飞行传感器噪声、漂移和失效模式也比随机遮蔽复杂。

## 6. 创新性判断

作者声明的创新主要有三项。第一，提出 TFNO + replication-masking 的稀疏热场重构方法，用随机遮蔽重复样本增强对任意稀疏传感器布局的泛化。第二，提出多输入融合，把离散传感器、飞行状态和低保真场合并输入，显著降低钝锥热流重构误差。第三，提出历史测量增强策略，在 C/SiC 板瞬态温度重构中利用 recent measurements 提高时间连续性。

真实创新属于“场景化方法组合 + 部署问题解决”。TFNO、Tucker decomposition、masking、multi-fidelity fusion、history window 都不是单独的新概念；新意在于它们被组合进一个高超声速稀疏传感热场重构任务，并以两个不同热场任务验证。尤其是 low-fidelity usefulness 通过 random forest importance 做快速评估，这一点很实用：它承认低保真并非总是有益，给出是否纳入输入的决策依据。

创新强度：中到强。算法原理层面是中等，工程系统层面较强。对 IJHFF 的读者来说，关键不是神经算子是否首次提出，而是它是否能比 nearest-neighbor、RBF、BPNN、BPNN+POD、FNO、UNO、Kriging 等更稳地重构热场，并满足在线推理。文章的数据支持基本能支撑这一点。

潜在削弱点是：两类算例仍然是受控场景，一个是数值生成的钝锥热流，一个是实验/瞬态加热板。它们覆盖“气动热”和“结构温度”，但并不等于复杂真实飞行器全外形、真实飞行噪声和热防护损伤场景都已验证。

## 7. 论证链条复原

全文论证链可以复原为：

1. 高超声速飞行器需要实时掌握完整热流/温度场，以支持安全、控制和热管理。
2. 实际飞行只能布置有限传感器，且关键热区常不可测，因此完整热场重构是典型欠定反问题。
3. 传统优化反演慢，纯数据驱动泛化弱，物理约束方法训练和部署代价高；现有方法难以兼顾实时、高分辨率和有限数据泛化。
4. TFNO 可以在频域执行全局卷积，用较紧凑参数学习场的空间结构；Tucker 压缩降低参数量和过拟合风险。
5. replication-masking 通过随机遮蔽传感器读数，使模型见到多种传感布局，提升对传感器稀疏/失效/变布局的鲁棒性。
6. 飞行状态和低保真场分别提供全局状态与空间先验，与稀疏高保真测量互补。
7. 对瞬态温度场，最近历史测量提供时间趋势，能减少逐帧重构造成的不连续和局部错误。
8. 两个算例和多组消融/对比表明，模型在误差、空间连贯性和推理速度上优于传统方法。

这条链闭合度较高。最关键的转折在 Section 2：作者把问题写成从 `[y1k, ..., yJk]` 到 `[ŷ1k, ..., ŷPk]` 的函数映射，再扩展到包含状态、低保真场和历史窗口的形式。也就是说，方法结构不是凭空选择，而是从问题定义自然展开。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
- 已有研究不足/GAP：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information. The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured. Full-field measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
- 本文解决方式：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements. First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies. Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 学术或工程增量：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction. Yang et al. (Yang and Fu, 2010) and Zhao et al. (Zhao et al., 2014) applied Tikhonov regula rization to estimate boundary heat flux and demonstrated this stabili zation in practice. To handle high-dimensional spatiotemporal thermal fields efficiently, conjugate-gradient sequential estimation with an adjoint model provides efficient gradients and makes the optimization fast.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法由三段组成。第一段是低保真模型构建：当飞行状态可用时，先由 CFD、工程气动加热算法或其他低成本模型生成完整低保真热场。它不要求精确，但要提供大致空间分布。第二段是高保真数据预处理：传感器读数被组织成稀疏输入，并通过 replication-masking 在训练期间随机遮蔽部分读数，使模型学习“缺测情况下仍需重构完整场”。第三段是 TFNO 重构：输入经提升层变成特征表示，经过 Fourier neural operator 的谱卷积和 Tucker 分解压缩，最后投影回完整场输出。

TFNO 的方法必要性来自三个性质。第一，热场是连续空间场，局部插值容易产生块状、过冲或不连贯；频域全局卷积更适合捕捉整体场结构。第二，传感器稀疏导致欠定，模型需要强先验；谱截断、低保真场和历史输入共同起到正则化作用。第三，在线应用不能接受大模型慢推理；tensorization 用低秩分解压缩权重，有利于控制参数量。

钝锥热流案例中，输入组合包括离散测量、飞行状态、低保真 CFD 或工程预测。作者还人工构造不同失真强度的低保真 CFD 场，用随机森林 feature importance 评估低保真信息贡献，并观察低保真误差增大时重要性下降、重构误差上升。当 importance 低于约 0.17 时，低保真场不应继续作为输入。这是全文很可复用的工程判断机制。

C/SiC 板案例中，方法重点从“多保真”转为“时间历史”。通过加入三个 25 s 间隔的历史测量，模型将瞬态温度场平均相对误差降到 1.5% 以下；若不加入历史，误差约 6.4%。这说明同一个 TFNO 框架可以根据场景切换信息补偿方式：热流场依赖状态和低保真，温度场依赖最近历史。

## 9. 证据系统与 Claim-Evidence 表

证据系统分为五组：第一组是钝锥 CFD/工程算法热流场和不同传感器布局的可视化重构；第二组是输入消融，比较仅传感器、传感器+状态、传感器+低保真、状态+工程/CFD 等组合；第三组是低保真质量敏感性与 RF importance；第四组是与 nearest-neighbor、RBF、BPNN、BPNN+POD、FNO、UNO、Kriging 等基线比较；第五组是 C/SiC 板已知/遮蔽传感点时程验证。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| TFNO 能从少量传感器实时重构完整热场 | 摘要、结论、Sections 4-5 | 9-126 个传感器重构 2400-3700 节点，单场推理约 0.08 s | 双算例数值/实验验证 | 强 | 真实机载硬件、噪声和数据流延迟未充分验证 |
| replication-masking 提升任意/缺失传感器布局泛化 | 贡献 1、Fig. 3.2、Fig. 4.7 | 随机遮蔽训练、多 meridian 遮蔽测试仍保持较好空间重构 | 数据增强与消融 | 中强 | 随机遮蔽不完全等价真实传感器故障和布局优化 |
| 状态变量与低保真 CFD 融合能显著降低钝锥热流误差 | 贡献 2、Fig. 4.8-4.13、Table 4.7/4.8 | 传感器-only 误差约 27.5%，加入状态和低保真后低于 2%；CFD 低保真比工程场更有用 | 输入组合消融 | 强 | 表格串栏，完整指标需要 PDF 图像复核 |
| 低保真数据并非越多越好，需评估其可用性 | Section 4.3、Table 4.8 | 随失真参数增大，RF importance 下降，重构误差单调恶化；importance 约 0.17 是经验阈值 | 敏感性分析 | 中强 | 阈值可能只适用于本数据和模型 |
| 历史测量能显著改善瞬态 C/SiC 温度场重构 | 贡献 3、Section 5.3、Table 5.5 | 三个 25 s 历史测量将平均相对误差降至 1.491%，无历史约 6.4% | 时序消融 | 强 | 历史窗口长度和采样间隔对其他热惯性结构需重调 |
| TFNO 优于传统插值和普通神经网络/神经算子基线 | Fig. 4.14、Table 5.5 | TFNO 在温度案例 R2=0.996、RMSE=13.740 K、相对误差=1.491%；FNO/UNO/Kriging 更差 | 基线对比 | 强 | 钝锥部分基线完整数值需 PDF 表格复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核说明 |
| --- | --- | --- | --- | --- |
| Eq. (1) | 定义稀疏传感到完整场的基础映射 | 反问题可被学习成 operator mapping | 从 J 个传感器到 P 个节点 | 公式排版需 PDF 复核 |
| Eq. (2) | 扩展为多源融合 | 状态和低保真场可作为输入 | 输入包含 X、高保真传感子集和低保真全场 | 需 PDF 复核 |
| Eq. (3) | 扩展为历史增强 | recent measurements 提供时间趋势 | 输入短历史窗口 | 需 PDF 复核 |
| Fig. 3.1 | 总体流程图 | 方法不是单一网络，而是数据驱动重构流程 | 低保真构建、预处理、高保真重构串联 | 需要 PDF 图像复核 |
| Fig. 3.2 | 展示 replication-masking | 增强对传感布局变化的鲁棒性 | 随机遮蔽传感读数并重复样本 | 需要 PDF 图像复核 |
| Fig. 3.3/Fig. 3.4 | 解释 Tucker decomposition 与 TFNO | 压缩参数、全局谱卷积 | 神经算子主干的结构依据 | 需要 PDF 图像复核 |
| Fig. 4.1-Fig. 4.4 | 交代钝锥几何、网格和高/低保真热流 | 数据来源可靠性 | Mach 10.6 钝锥，CFD 与工程算法对比 | 云图细节需 PDF 复核 |
| Fig. 4.5-Fig. 4.13 | 展示不同输入组合下热流重构 | 多源输入提高精度和空间连贯性 | 仅传感器或工程场输入会有更大偏差；融合 CFD 最好 | 需要 PDF 图像复核 |
| Table 4.8 | 低保真质量与 RF importance | 低保真可用性需评估 | CFD 场 importance 0.284，工程场 0.151，失真增强则下降 | 表格串栏，需 PDF 复核 |
| Fig. 4.14/Table 4.9 | 与传统方法比较 | TFNO 优于 NN/RBF/BPNN/BPNN+POD | 插值有块状/过冲，普通网络有伪影 | 需要 PDF 图像复核 |
| Fig. 5.1-Fig. 5.4 | 展示 C/SiC 板几何、传感器和实验设置 | 第二任务数据基础 | 传感器布置、加热功率、热循环 | 需要 PDF 图像复核 |
| Fig. 5.5-Fig. 5.8/Table 5.5 | 温度场重构与时程验证 | 历史增强有效，TFNO 优于 FNO/UNO/Kriging | TFNO 相对误差 1.491%，Kriging 21.463% | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Problem description；3 Methods；4 Heat flux distribution reconstruction for a blunt cone；5 Temperature distribution reconstruction for a C/SiC plate；6 Conclusion。章节顺序体现“问题形式化 -> 方法框架 -> 两个代表性任务验证”的布局。

Introduction 是文献版图与 gap 制造的主场。它先按方法类别组织 inverse problem 文献，再指出速度、泛化和完整场重构的综合缺口，最后给出三项贡献。Problem description 起到数学收束作用，把工程需求写成函数映射，并逐步加入状态、低保真和历史项。Methods 不是长篇堆公式，而是围绕数据驱动重构流程、RM 和 TFNO 结构展开。Sections 4 和 5 的功能不同：Section 4 证明多源融合对气动热流场有效，Section 5 证明历史增强对瞬态温度场有效。

标题命名偏工程描述型，直接告诉读者任务对象和方法对象。例如 “Heat flux distribution reconstruction for a blunt cone” 比 “Case study 1” 更有效，因为它把热流、分布、钝锥都暴露出来。本文少有泛泛的 Discussion 独立章节，讨论嵌入结果段落中，这符合方法论文强调证据链推进的写法。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.2: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Problem description（问题定义）
- L2 p.4: 3 Methods（方法/模型/算法）
  - L3 p.4: 3.1 Data-driven reconstruction（对象/模块/过渡章节）
  - L3 p.5: 3.2 Tensorized Fourier neural operator（对象/模块/过渡章节）
- L2 p.7: 4 Heat flux distribution reconstruction for a blunt cone（对象/模块/过渡章节）
  - L3 p.7: 4.1 Physical model（方法/模型/算法）
  - L3 p.9: 4.2 TFNO model configuration and training（方法/模型/算法）
  - L3 p.10: 4.3 Results（结果/验证/讨论）
- L2 p.16: 5 Temperature distribution reconstruction for a C/SiC plate（对象/模块/过渡章节）
  - L3 p.16: 5.1 Physical model（方法/模型/算法）
  - L3 p.18: 5.2 TFNO model configuration and training（方法/模型/算法）
  - L3 p.19: 5.3 Results（结果/验证/讨论）
- L2 p.22: 6 Conclusion（结论/贡献回收）
- L2 p.22: CRediT authorship contribution statement（尾部材料）
- L2 p.22: Declaration of competing interest（尾部材料）
- L2 p.22: Acknowledgments（尾部材料）
- L2 p.22: Data availability（尾部材料）
- L2 p.22: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 2 | 2 | 背景定位/文献缺口 |
| 2 Problem description | 3 | 2 | 问题定义 |
| 3 Methods | 4 | 2 | 方法/模型/算法 |
| 3.1 Data-driven reconstruction | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Tensorized Fourier neural operator | 5 | 3 | 对象/模块/过渡章节 |
| 4 Heat flux distribution reconstruction for a blunt cone | 7 | 2 | 对象/模块/过渡章节 |
| 4.1 Physical model | 7 | 3 | 方法/模型/算法 |
| 4.2 TFNO model configuration and training | 9 | 3 | 方法/模型/算法 |
| 4.3 Results | 10 | 3 | 结果/验证/讨论 |
| 5 Temperature distribution reconstruction for a C/SiC plate | 16 | 2 | 对象/模块/过渡章节 |
| 5.1 Physical model | 16 | 3 | 方法/模型/算法 |
| 5.2 TFNO model configuration and training | 18 | 3 | 方法/模型/算法 |
| 5.3 Results | 19 | 3 | 结果/验证/讨论 |
| 6 Conclusion | 22 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 22 | 2 | 尾部材料 |
| Declaration of competing interest | 22 | 2 | 尾部材料 |
| Acknowledgments | 22 | 2 | 尾部材料 |
| Data availability | 22 | 2 | 尾部材料 |
| References | 22 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一组段落先陈述飞行热监测的约束：全场技术难以飞行部署，稀疏传感带来欠定反问题。第二组段落按三类方法综述，每类都遵循“可解决什么 -> 仍缺什么”的节奏。第三组段落把 gap 收束到 TFNO、RM、多源融合和历史输入。

方法段落节奏是“先问题映射，再数据流程，再模型结构”。这很适合 AI 工程论文，因为读者最怕先看到一个复杂网络却不知道为何必要。作者先用 Eq. (1)-(3) 让输入输出关系清楚，再解释为什么 spectral convolution、tensor compression 和 masking 能解决欠定、稀疏和布局变化问题。

结果段落通常围绕图表推进：先描述图/表呈现什么，再解释趋势，再回到 claim。比如低保真失真部分不是只报误差，而是用 RF importance 解释“低保真场对稀疏区域空间结构约束的贡献下降”。C/SiC 部分则先显示整场云图，再用已知/遮蔽传感点时程证明模型不仅拟合已知点，也能推断未知点。

## 13. 文笔画像与语言习惯

文章语言是典型的工程 AI 论文风格：高频词包括 real-time、sparse、reconstruction、full-field、low-fidelity、high-fidelity、fusion、thermal management、generalization、temporal coherence。语气较自信，但不是夸张式宣传；强 claim 后通常配指标，如 mean relative error、RMSE、R2、inference latency。

主动语态用于贡献声明和方法动作，如 “we develop”“we propose”“we evaluate”。被动语态用于实验设置和结果计算，如 “is reconstructed”“is modeled”“is compared”。时态上，文献综述用现在完成时和一般过去时，方法定义用一般现在时，结果用一般现在时描述图表趋势。

文笔的一个显著特点是“把正则化讲成工程结构”：不是只说加了 penalty，而是说 TFNO 的谱截断、多源输入和历史窗口共同形成 spatiotemporal priors，约束欠定反问题。这种写法把机器学习架构和物理直觉连接起来，能减轻“黑箱模型”的审稿压力。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：70299
- 高频词：model(65)；measurements(60)；sensor(56)；field(55)；temperature(47)；data(45)；low-fidelity(45)；error(43)；accuracy(39)；relative(38)；reconstruction(38)；tfno(38)；thermal(36)；sensors(36)；input(33)；points(30)；training(29)；fields(29)；spatial(27)；heat(26)
- 高频名词化/学术名词：temperature(47)；low-fidelity(45)；reconstruction(38)；measurement(17)；information(15)；function(14)；tion(14)；replication(14)；distribution(12)；smoothness(12)；validation(11)；prediction(10)；performance(10)；high-fidelity(9)；regularization(8)
- 高频学术动词：predicted(8)；evaluate(8)；predict(6)；provide(6)；evaluated(5)；optimized(4)；derived(4)；compare(4)；constructed(3)；indicate(3)；compared(3)；demonstrate(3)；estimate(2)；propose(2)；validated(2)
- 高频形容词：relative(38)；thermal(36)；spatial(27)；global(23)；neural(20)；spectral(18)；measurement(17)；physical(17)；transient(15)；boundary(13)；experimental(13)；local(10)；historical(10)；different(10)；consistent(9)
- 高频副词：effectively(7)；randomly(6)；significantly(6)；spatially(5)；primarily(4)；substantially(4)；tively(4)；physically(4)；subsequently(4)；consequently(4)；approximately(4)；conversely(4)；accurately(4)；closely(3)；simultaneously(3)
- 高频二词短语：relative error(29)；heat flux(20)；sensor locations(11)；mean relative(11)；rmse relative(11)；sparse sensor(9)；replication count(9)；low-fidelity cfd(9)；low-fidelity field(8)；sensor measurements(8)；masking ratio(8)；thermal field(7)
- 高频三词短语：rmse relative error(11)；mean relative error(8)；retained spectral modes(6)；sparse sensor measurements(4)；full set measurements(4)；neurons per fourier(4)；per fourier block(4)；boundary heat flux(3)；trained neural network(3)；fourier neural operator(3)；mean relative errors(3)；reduces mean relative(3)
- 被动语态估计：100；`we + 动作动词` 主动句估计：8
- 一般现在时线索：233；一般过去时线索：454；现在完成时线索：0；情态动词线索：28

分章节正文词频：

- 1 Introduction: sensor(13)；measurements(11)；fields(10)；heat(10)；boundary(9)；model(9)；data(9)；flux(9)
- 2 Problem description: measurements(6)；sensor(6)；data(5)；regularization(5)；state(4)；sensors(4)；field(4)；yjk(4)
- 3 Methods: model(17)；field(14)；measurements(13)；set(13)；input(13)；low-fidelity(12)；operator(12)；fourier(11)
- 4 Heat flux distribution reconstruction for a blunt cone: low-fidelity(25)；error(25)；cfd(21)；relative(21)；accuracy(19)；field(19)；model(18)；measurements(18)
- 5 Temperature distribution reconstruction for a C/SiC plate: temperature(30)；points(21)；model(16)；tfno(14)；thermal(13)；sensor(12)；surface(11)；sensors(11)
- 6 Conclusion: measurements(3)；model(3)；temperature(3)；tfno(2)；fields(2)；sparse(2)；discrete(2)；sensors(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：sparse measurements、full-field reconstruction、thermal monitoring、multi-fidelity data fusion、low-fidelity predictions、high-fidelity sensor data、replication-masking、temporal coherence、spectral domain、Tucker decomposition、operator backbone。

可复用问题句式：`Full-field measurement techniques are difficult to deploy in flight, so thermal assessments must be inferred from sparse sensors.` 可迁移到“不可全量观测，只能稀疏测量”的工程场景。

可复用 gap 句式：`Current methods still fail to balance real-time performance, high definition, and generalization from limited data.` 适合写三目标冲突型 gap。

可复用方法句式：`We incorporate auxiliary low-fidelity fields as spatial priors and sparse high-fidelity measurements as local constraints.` 适合多保真融合论文。

可复用贡献句式：`The method integrates (i) ..., (ii) ..., and (iii) ...`。它的好处是把框架贡献拆成部署问题，而不是拆成算法模块。

可复用结果句式：`Compared with traditional interpolants and conventional neural networks, the proposed model attains the best balance between accuracy and spatial coherence.` 这种句式不只说“最准确”，还强调空间连贯性这个场重构指标。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Real-time monitoring of the heat flux and temperature of hypersonic flight vehicles is critical for safety, control, and thermal management.
  可迁移模板：Real-time monitoring of the heat flux and temperature of TARGET SYSTEM is critical for safety, control, and thermal management.
- 原句：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
  可迁移模板：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
#### Gap/转折句
- 原句：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
  可迁移模板：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
- 原句：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
  可迁移模板：The situation becomes more challenging in extreme environments such as forebody leading edges, where sensor instrumentation is impractical and critical thermal regions remain unmeasured.
- 原句：Full-field measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
  可迁移模板：Full-field measurement techniques such as infrared thermography and temperature-sensitive paint are difficult to deploy in flight because of accuracy limits and the requirement for ground-based systems.
- 原句：As a result, thermal assessments are usually inferred from a few sensors placed in less extreme regions such as nonleading-edge areas.
  可迁移模板：As a result, thermal assessments are usually inferred from a few sensors placed in less extreme regions such as nonleading-edge areas.
- 原句：Reconstructing a global thermal field (i.e., distri bution) from such limited sparse measurements constitutes an inverse problem.
  可迁移模板：Reconstructing a global thermal field (i.e., distri bution) from such limited sparse measurements constitutes an inverse problem.
#### 方法提出句
- 原句：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (TFNO) that reconstructs full thermal fields from sparse measurements.
  可迁移模板：To address these issues, we develop an enhanced method based on the tensorized Fourier neural operator (METHOD) that reconstructs full thermal fields from sparse measurements.
- 原句：First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies.
  可迁移模板：First, to mitigate the paucity of measurements, we propose a replication-masking strategy that expands the training set by randomly occluding a fraction of sensor readings in repeated copies.
- 原句：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
  可迁移模板：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 原句：We evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach 10.6 hypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating.
  可迁移模板：We evaluate the proposed method on two tasks: blunt-cone surface heat-flux reconstruction under Mach Xhypersonic flow conditions and transient temperature reconstruction for a C/SiC composite plate subjected to radiant heating.
- 原句：The first is optimization-based: boundary conditions are iteratively adjusted so that the forward model's predictions at the sensor locations match the measurements as closely as possible, thereby yielding the boundary-condition distribution or field solution that best explains the observed data.
  可迁移模板：The first is optimization-based: boundary conditions are iteratively adjusted so that the forward model's predictions at the sensor locations match the measurements as closely as possible, thereby yielding the boundary-condition distribution or field solution that best explains the observed data.
#### 结果呈现句
- 原句：Yang et al. (Yang and Fu, 2010) and Zhao et al. (Zhao et al., 2014) applied Tikhonov regula rization to estimate boundary heat flux and demonstrated this stabili zation in practice.
  可迁移模板：Yang et al. (Yang and Fu, X) and Zhao et al. (Zhao et al., X) applied Tikhonov regula rization to estimate boundary heat flux and demonstrated this stabili zation in practice.
- 原句：They showed that near-boundary sensors carry the greatest value and that inference can be performed in milliseconds without repeatedly solving the for ward model, though strongly nonlinear or non-unique problems may still demand more data or richer architectures.
  可迁移模板：They showed that near-boundary sensors carry the greatest value and that inference can be performed in milliseconds without repeatedly solving the for ward model, though strongly nonlinear or non-unique problems may still demand more data or richer architectures.
- 原句：There is a need for an approach that incorporates physical information and still achieves high-accuracy, real-time recon struction when measurements are taken at arbitrary locations.
  可迁移模板：There is a need for an approach that incorporates physical information and still achieves high-accuracy, real-time recon struction when measurements are taken at arbitrary locations.
- 原句：By repeatedly and randomly masking subsets of sensor readings during training, the model achieves strong generalization to arbitrary sensor layouts, learning to faithfully reconstruct global fields from sparse, irregular inputs while effectively expanding the small measurement dataset.
  可迁移模板：By repeatedly and randomly masking subsets of sensor readings during training, the model achieves strong generalization to arbitrary sensor layouts, learning to faithfully reconstruct global fields from sparse, irregular inputs while effectively expanding the small measurement dataset.
- 原句：Sections 4 and 5 report results for the blunt-cone heat-flux and composite-plate temperature reconstructions, respectively, including comparisons to alternative methods.
  可迁移模板：Sections Xand Xreport results for the blunt-cone heat-flux and composite-plate temperature reconstructions, respectively, including comparisons to alternative methods.
#### 贡献/增量句
- 原句：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
  可迁移模板：Second, if state information is available, we feed it into the model together with the corresponding low-fidelity data to improve the reconstruction.
- 原句：To handle high-dimensional spatiotemporal thermal fields efficiently, conjugate-gradient sequential estimation with an adjoint model provides efficient gradients and makes the optimization fast.
  可迁移模板：To handle high-dimensional spatiotemporal thermal fields efficiently, conjugate-gradient sequential estimation with an adjoint model provides efficient gradients and makes the optimization fast.
- 原句：Once trained, it provides fast, accurate on line estimates, but the offline cost is high and generalization beyond the sampled envelope is limited.
  可迁移模板：Once trained, it provides fast, accurate on line estimates, but the offline cost is high and generalization beyond the sampled envelope is limited.
- 原句：Tamaddon et al. (Tamaddon-Jahromi et al., 2020) established a back-propagation neural network (BPNN) model from discrete temperatures to boundary temperatures for multiple conduction and convection problems and sensor layouts.
  可迁移模板：Tamaddon et al. (Tamaddon-Jahromi et al., X) established a back-propagation neural network (METHOD) model from discrete temperatures to boundary temperatures for multiple conduction and convection problems and sensor layouts.
- 原句：In the C/SiC plate temperature-field task, using three historical measurements at a 25-s interval reduces the mean relative error from ≈6.4% (no history) to below 1.5%, and markedly improves spatial smooth ness in the reconstructed fields.
  可迁移模板：In the C/SiC plate temperature-field task, using three historical measurements at a X-s interval reduces the mean relative error from ≈X (no history) to below X, and markedly improves spatial smooth ness in the reconstructed fields.
#### 限制/边界句
- 原句：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
  可迁移模板：In flight, however, sensing is typically limited to sparsely distributed sensors, which yields incomplete spatial coverage and incomplete information.
- 原句：Reconstructing a global thermal field (i.e., distri bution) from such limited sparse measurements constitutes an inverse problem.
  可迁移模板：Reconstructing a global thermal field (i.e., distri bution) from such limited sparse measurements constitutes an inverse problem.
- 原句：To ensure solution stability, these methods are commonly combined with regularization.
  可迁移模板：To ensure solution stability, these methods are commonly combined with regularization.
- 原句：Once trained, it provides fast, accurate on line estimates, but the offline cost is high and generalization beyond the sampled envelope is limited.
  可迁移模板：Once trained, it provides fast, accurate on line estimates, but the offline cost is high and generalization beyond the sampled envelope is limited.
- 原句：They showed that near-boundary sensors carry the greatest value and that inference can be performed in milliseconds without repeatedly solving the for ward model, though strongly nonlinear or non-unique problems may still demand more data or richer architectures.
  可迁移模板：They showed that near-boundary sensors carry the greatest value and that inference can be performed in milliseconds without repeatedly solving the for ward model, though strongly nonlinear or non-unique problems may still demand more data or richer architectures.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是“分类铺路 + 近邻对比”。作者没有把所有文献堆成一串，而是按 optimization-based、data-driven、physics-aware 分类。每类都列出代表性工作，再指出其不足。这种组织方式让 gap 更自然：不是某篇文章没做，而是整类方法在实时性、泛化或高分辨率完整场方面有结构性不足。

第二类引用是方法近邻，用 DeepONet、FNO、UNO、PINN 等说明神经算子和物理知情网络已用于科学计算与热问题。这里的引用作用是降低 TFNO 的陌生感，同时给出为什么选神经算子而不是普通 BPNN/CNN 的理由。

第三类引用是本团队/近领域延续，例如 2025 年 POD+TSCN 轨迹热流预测和 2024 年随机森林反热传导方法。这使本文看起来像连续研究路线的一环：从热流预测、反热传导到稀疏传感重构。风险是团队自引较集中，但由于领域交叉明显，整体引用版图仍较充分。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：0
- Introduction 引文簇数量估计：0
- References 条目数：65
- 可识别年份条目数：43
- 2021 年及以后文献数：22
- 2010 年前经典文献数：4
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：未识别

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 2001. Random forests. Mach. Learn. 45 (1), 5–
- 32. Cai, S., Wang, Z., Wang, S., et al.,
- 2021. Physics-informed neural networks for heat transfer problems. J. Heat Transfer 143 (6),
- 060801.
H. Wenyu et al. International Journal of Heat and Fluid Flow 120 (2026) 110341
Chanda, S., Balaji, C., Venkateshan, S.P., et al.,
- 2017. Estimation of principal thermal conductivities of layered honeycomb composites using ANN-GA based inverse technique. Int. J. Therm. Sci. 111, 423–
- 436. Chen, H., Yu, B., Zhou, H., et al.,
- 2018. Identification of transient boundary conditions with improved cuckoo search algorithm and polynomial approximation. Eng. Anal. Bound. Elem. 95, 124–
- 141. Cleary, J.W.,
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 真实飞行泛化风险：钝锥和 C/SiC 板是代表性场景，但真实飞行器几何、气体非平衡、材料退化、烧蚀和传感器漂移更复杂。
2. 传感器布局风险：replication-masking 可模拟随机缺失，但不等同最优传感器布置、系统性失效或热区完全无传感的极端场景。
3. 低保真依赖风险：低保真 CFD 或工程算法若偏差结构与训练不同，可能误导模型；RF importance 阈值是否可迁移仍需验证。
4. 指标风险：平均相对误差可能掩盖关键热区峰值误差；需要进一步报告峰值热流、热点位置和安全裕度误差。
5. 数据泄露/分布风险：若训练/测试状态分布相近，泛化结论可能偏乐观；需要更明确的外推测试。
6. 物理一致性风险：TFNO 输出空间连贯，但不一定严格满足热传导方程或能量守恒；physics-guided 的表述需避免被理解成强物理约束。
7. 表格与图像复核风险：txt 抽取中表格串栏较明显，关键对比数值需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把“传感器稀疏”写成飞行器结构/热防护不可避免的工程约束，而不是数据不足借口。
- Gap 资产：使用“三目标无法同时满足”制造 gap，即实时性、高分辨率、有限数据泛化。
- 方法资产：低保真场作为空间先验，高保真传感器作为局部约束，状态变量作为全局校准，历史测量作为时间先验。
- 证据资产：不仅给整体误差，还做输入消融、低保真质量敏感性、传统方法对比、遮蔽传感点验证。
- 图表资产：用一组图展示同一测试案例在不同输入组合下的云图差异，直观说明每类输入的作用。
- 写作资产：把架构组件对应到实际部署问题，例如 RM 对应传感布局变化，multi-source fusion 对应数据不足，history window 对应瞬态连续性。

## 18. 对我写论文的启发

如果自己写工程 AI 论文，不要把创新只放在“换了一个更强模型”。更好的写法是先定义部署场景中的硬约束，然后让每个模型模块都回应一个真实约束。本文的 TFNO、RM、低保真融合、历史输入之所以可信，是因为它们分别对应场结构、稀疏布局、物理先验和时间连续性。

另一个启发是对低保真信息要有“纳入/舍弃”的判据。很多多保真论文默认低保真一定有用，本文用 RF feature importance 给出快速评估，虽然阈值还需验证，但这种思路很适合工程设计：不要盲目融合，先判断它是否提供互补结构。

第三个启发是结果叙事要同时有数值和视觉。场重构问题只报 RMSE 不够，必须展示空间云图、热点区域、未知点时程和失效布局。因为真正的使用者关心的是“模型是否在未测关键区域胡编”。

## 19. 最终浓缩

这篇论文的核心贡献是：把高超声速热场稀疏传感重构写成一个在线多源 operator learning 问题，用 TFNO 学全场结构，用 replication-masking 处理可变传感布局，用低保真场和飞行状态补充空间/状态先验，用历史测量保证瞬态连续性。它的新意不在单个算法组件，而在把这些组件组织成可部署的热监测框架，并用钝锥热流与 C/SiC 板温度两个任务证明低误差和实时性。最值得学习的是它的 gap 制造方式和证据链：每个方法模块都有清楚的工程痛点，每个强 claim 都有消融、对比或遮蔽验证支撑。需要后续 PDF 复核的重点是所有云图细节、低保真对比表、传感器布局图和公式排版。
