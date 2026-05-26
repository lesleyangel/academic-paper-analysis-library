# Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning

## 0. 读取说明

- 文本来源：`801/文本/txt/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.txt`，PyMuPDF 抽取，20 页。
- 抽取文本包含摘要、引言、DNN-TL 方法、CFD/RBD 样本生成、验证/插值/外推预测、轨迹仿真、附录和主要图表。
- 原文多处公式、表格和图题被双栏交错，本文依据上下文复原；DNN 结构图、CFD 网格、预测曲线和轨迹图均需 PDF 图像复核。

## 1. 基本信息与论文身份

- 题名：Unsteady aerodynamic modeling and flight trajectory simulation of dual-spin projectile based on DNN and transfer-learning。
- 作者：Wen Ji, Chunlin Gong, Xuyi Jia, Chunna Li, Gang Wang。
- 期刊：Aerospace Science and Technology, 155 (2024) 109711。
- 领域：非定常气动建模、双旋弹、CFD/RBD、深度神经网络、迁移学习、快速轨迹仿真。
- 论文类型：数据驱动代理模型 + 高保真 CFD/RBD 数据生成 + 对比验证 + 飞行动力学耦合仿真。
- 研究对象：带鸭舵 dual-spin projectile 在不同初始自旋状态下的气动力/力矩和飞行轨迹。
- 主要方法：用 coupled CFD/RBD 生成源域和目标域数据；构建带短期历史飞行状态和气动力历史输入的 DNN；用 pre-training/fine-tuning transfer learning 适应新初始条件；与 ARMA、LSTM/LSTM-TL 对比；最后替代 CFD 模块进行轨迹仿真。
- 论文身份判断：这是气动建模与工程仿真效率论文，核心贡献是让高保真 CFD/RBD 的非定常气动信息可迁移到秒级轨迹仿真。

## 2. 摘要与核心信息提取

本文核心主张是：dual-spin projectile 的非定常气动力受飞行状态、历史气动响应、Magnus effect 和弹体/鸭舵干扰影响，直接 CFD/RBD 计算精度高但成本极大；DNN-TL 可以利用源域 CFD/RBD 数据和少量目标域数据，在不同初始条件下快速准确预测气动力/力矩，并将轨迹仿真时间从约 20 小时降到几秒。

摘要强调三个技术点：输入特征包含当前与短期历史飞行状态、历史气动力/力矩；迁移学习用少量新工况数据 fine-tune 预训练模型；验证包含插值和外推预测，且优于 LSTM 和 ARMA。

一句话浓缩：本文用 DNN + transfer learning 替换双旋弹 CFD/RBD 轨迹仿真中的昂贵气动计算模块，在保持误差小于约 6%-8% 的同时获得三个数量级的效率提升。

## 3. 选题层深拆

选题来自制导双旋弹的工程仿真矛盾。双旋弹通过高速旋转保持陀螺稳定，同时用前体/鸭舵提供制导能力。其气动特性比普通非旋转飞行器复杂：aft body 高速旋转产生 Magnus effect，气动力/力矩不再只在攻角平面内；前体鸭舵和后体之间存在气动干扰；飞行速度、高度、角度在大包线内变化。

高保真 coupled CFD/RBD 能同时求解流场和刚体运动，避免传统气动插值表无法描述非定常效应的问题。但这种方法需要大量 CFD 计算，难以用于工程上的快速轨迹评估、控制律设计和多工况仿真。

作者把问题定义为：能否建立一个非定常气动代理模型，不仅在已有初始条件下准确，而且在初始自旋状态变化时通过少量目标数据快速迁移？这个定义使论文从普通神经网络回归变成“跨工况泛化”问题。

## 4. 领域位置与文献版图

文献版图分三类。第一类是双旋弹/旋转弹气动与飞行动力学研究，用于说明 Magnus effect、横纵耦合和强非定常干扰。第二类是高保真 CFD/RBD 联合仿真，用来建立精度标杆，但也暴露计算成本。第三类是非定常气动建模方法，包括白箱的 aerodynamic derivative、differential/integral equation、state-space model，以及黑箱的 Kriging、ARMA、LSTM、神经网络。

作者对前人评价比较明确：黑箱方法在纵向平面俯仰机动中已有较高精度，但 spinning projectile 的非定常气动建模和跨初始状态适用性仍不足。LSTM 能处理长历史序列，但本文认为引入过长历史会带来冗余；ARMA 计算快但非线性表达不足。

本文位于 data-driven unsteady aerodynamics 与 transfer learning 的交叉点。它不是提出新的 CFD 求解器，而是把 CFD/RBD 作为高保真数据源，构建可迁移的气动模型。

## 5. Gap 制造机制

本文 gap 是“高保真非定常气动与工程快速仿真之间的落差”。

第一层 gap：传统气动插值表不能准确反映双旋弹的非定常气动特性；CFD/RBD 能反映，但计算成本太高。第二层 gap：已有黑箱模型多用于固定工况或纵向机动，缺少对 dual-spin projectile 不同初始自旋状态的泛化能力。第三层 gap：LSTM 类模型虽然利用历史信息，但可能依赖长历史数据，计算与训练复杂度高；本文选择短期历史状态和气动响应作为输入，试图降低长期历史影响。

作者制造 gap 的方式很工程化：不是说神经网络没用，而是说固定训练集模型在新初始条件下会失效；不是说 CFD 不准，而是说它太慢。因此 DNN-TL 的必要性来自“精度”和“速度”两端夹逼。

## 6. 创新性判断

- 创新类型：气动代理模型结构 + 迁移学习跨工况泛化 + 轨迹仿真耦合。
- 真实创新点 1：构造输入 `S(t) = [x(t-2), x(t-1), x(t), y(t-2), y(t-1)]`，同时考虑当前/历史飞行状态和历史气动力/力矩。
- 真实创新点 2：用 source domain 预训练 DNN，再在 target domain 0-0.3 s 少量数据上 fine-tune，提高新初始条件下泛化能力。
- 真实创新点 3：在 validation、interpolation prediction、extrapolation prediction 三类测试中与 ARMA、LSTM/LSTM-TL 对比。
- 真实创新点 4：将 DNN-TL 气动模型耦合入飞行动力学方程，实现秒级轨迹仿真。
- 创新强度：中等偏强。DNN 和 transfer learning 本身不是新技术，但用于 dual-spin projectile 非定常气动和轨迹仿真的场景贡献明确。
- 可挑战之处：模型可解释性弱，训练数据仍来自昂贵 CFD/RBD，外推范围有限。

## 7. 论证链条复原

1. 双旋弹飞行性能评估需要准确气动力/力矩和轨迹仿真。
2. 气动插值表不能表达非定常特性；CFD/RBD 精确但计算昂贵。
3. 需要一个高精度、可迁移、快速的非定常气动模型。
4. DNN 可以拟合非线性输入输出关系，短期历史状态和历史气动力可捕捉 time-delay effects。
5. Transfer learning 可以利用源域预训练知识，用少量目标域数据适应新初始条件。
6. 通过 CFD/RBD 生成源域和目标域数据，并设置 validation、interpolation、extrapolation 三类工况。
7. 先调参确定 m = n = 2、隐藏层神经元数 200，再训练 DNN-TL。
8. 与 ARMA、LSTM/LSTM-TL 对比，DNN-TL 在三类工况下气动力/力矩误差最低。
9. 将 DNN-TL 模型耦合轨迹方程，轨迹状态误差小于 6%-8%，计算时间从约 20 小时降到几秒。
10. 结论回扣：DNN-TL 在双旋弹非定常气动建模中兼顾精度、泛化和效率。

## 8. 方法/理论/模型细拆

DNN 输入设计是方法核心。`x(t)` 包含速度分量、角速度、姿态角等飞行状态；`y(t)` 包含轴向力、法向力、侧向力、前体滚转力矩、后体滚转力矩、俯仰力矩和偏航力矩。最终选择 `m = n = 2`，即使用当前和前两步飞行状态，以及前两步气动力/力矩。

DNN 结构为全连接网络，文本显示采用 3 个隐藏层，每层神经元数经参数研究后设为 200。训练使用 Adam，硬件为 Nvidia GeForce RTX 3080。神经元数过少欠拟合，过多有过拟合风险。

迁移学习流程包括：用源域 CFD/RBD 数据训练预训练 DNN；冻结前 `l-1` 个隐藏层，随机初始化最后隐藏层；用目标域少量数据重训；再解冻所有层并以较小学习率 fine-tune。这个流程让低层特征保留源域气动知识，高层适应目标域初始条件。

数据生成来自 coupled CFD/RBD。文中 projectile 初始状态包括 H = 11 km、Ma = 0.723、θ = 16 deg、aft spin rate 等。Table 2 设置三类测试：validation、interpolation prediction、extrapolation prediction。插值/外推工况主要通过不同 `pf` 初始自旋状态和时间区间构造。

轨迹仿真中，DNN-TL 模型替代 CFD 模块：每个时间步根据历史状态构造输入 S(t)，预测当前气动力/力矩 y(t)，再由飞行动力学方程更新状态。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| 短期历史输入能捕捉非定常气动 time-delay effects | Section 2/4 | m,n 参数研究显示 m=n=2 时预测误差最小 | 中强 | 只在本文数据上调参 |
| DNN-TL 在 validation case 精度高 | Table 3 | DNN-TL 最大 δe 为 Mxa 5.54%，其余多数低于 1.5%；优于 LSTM 和 ARMA | 强 | 表格错行需 PDF 复核 |
| DNN-TL 在 interpolation prediction 中泛化优于对比方法 | Table 4 | DNN-TL δe 最大约 3.49%，LSTM-TL 在 Fy/Fz 超 9%/14%，ARMA Fz 达 39.49% | 强 | 目标域只用 0-0.3 s 数据 |
| DNN-TL 在 extrapolation prediction 仍可用 | Table 5 | DNN-TL 最大 δe = 6.74%；LSTM-TL Fy 达 71.09%，ARMA Fy 达 43.59% | 强 | 外推误差高于插值，范围有限 |
| DNN-TL 比 ARMA/LSTM 更能处理跨初始条件变化 | Fig. 12-15 | 预测曲线更贴近 CFD/RBD，高误差不随时间快速积累 | 中强 | 曲线细节需 PDF 图像复核 |
| 代理模型轨迹仿真效率提升三个数量级 | Section 4.3 | DNN-TL 轨迹仿真几秒，coupled CFD/RBD 约 20 h | 强 | 前置训练/数据生成成本未计入 |
| 轨迹仿真误差保持工程可接受 | Table 6/7 | 插值 θ/α/β 误差约 0.12%、5.69%、1.31%；外推约 0.61%、7.65%、1.66%，均 <8% | 强 | 长时间误差积累仍需更多工况验证 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 2 DNN model | 展示输入历史状态/气动力与输出气动载荷的网络结构 | 方法定义 | 需要 PDF 图像复核 |
| Eq. 1 输入 S(t) | 把 time-delay effects 显式写进模型 | 非定常输入设计 | 文本可读 |
| Fig. 3 pre-training/fine-tuning | 展示迁移学习流程 | 跨工况泛化 | 需要 PDF 图像复核 |
| Algorithm 1 | 将 DNN-TL 训练流程步骤化 | 可复现性 | 文本可读 |
| Fig. 4 flowchart | 串联样本生成、预训练、迁移、预测 | 方法总览 | 需要 PDF 图像复核 |
| Fig. 5-7 projectile/坐标/CFD-RBD | 定义物理对象和高保真数据源 | 数据可信度 | 网格和流程需 PDF 复核 |
| Fig. 8-9 参数研究 | 证明 m,n 和神经元数选择合理 | 模型调参 | 曲线需 PDF 复核 |
| Table 3-5 | 三类工况误差对比 | DNN-TL 优于 ARMA/LSTM | 表格需 PDF 复核 |
| Fig. 10/12/14 | 预测值与 CFD/RBD 高保真值曲线对比 | 精度证据 | 需要 PDF 图像复核 |
| Algorithm 2 / Fig. 16 | 展示模型驱动轨迹仿真流程 | CFD 替代 | 文本可读，流程图需复核 |
| Fig. 17-18 / Table 6-7 | 轨迹仿真结果和状态误差 | 秒级仿真可行 | 轨迹图需 PDF 复核 |

结果叙事的安排是：先讲模型结构和迁移流程，再讲数据生成和参数选择，随后按 validation/interpolation/extrapolation 递进验证，最后升到轨迹仿真效率。

## 11. 章节结构与篇章布局

文章结构为 Introduction；Aerodynamic modeling method；Samples generation of aerodynamic modeling and prediction；Results and discussion；Conclusions，后附 CFD 网格、ARMA、LSTM 附录。

Introduction 很长，承担领域综述和 gap 建立。第二章专门讲 DNN、transfer learning 和 DNN-TL 流程，避免把机器学习方法混进结果。第三章讲样本如何从 coupled CFD/RBD 得来，保证数据源可信。第四章分成参数选择、气动预测和轨迹仿真，层级清楚。

标题命名偏工程方法型。最值得学习的是把“样本生成”单独成章，因为数据驱动论文最容易被质疑数据来源，单独说明 CFD/RBD 流程能增强可信度。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：7
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Aerodynamic modeling method                                  where, Fx,Fy, and Fz represent the axial force, normal force, and lateral | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.2 Transfer learning based on the pre-training | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3 Aerodynamic modeling method based on DNN-TL | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.2.3 Coupled CFD/RBD method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Generation of the unsteady aerodynamic dataset | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2.1 Result analysis of the validation case | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4.2.2 Result analysis of the interpolation prediction case | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 节奏是“飞行器需求-双旋弹复杂气动-CFD/RBD 精度与成本矛盾-已有气动模型分类-黑箱方法不足-本文贡献”。作者先把工程复杂性讲足，再引出数据驱动方法。

方法段落节奏是“定义变量-写公式-解释物理含义-给流程图/算法”。DNN 输入公式后紧跟对每个状态量和气动力矩的解释，减少黑箱感。

结果段落采用“先调参、再对比、再分析误差原因”的节奏。插值和外推段落结构几乎平行：说明训练数据，展示曲线，给误差表，解释 DNN-TL 为什么更好。

轨迹仿真段落先说明算法需要前几个 CFD/RBD 时间步初始化，再报告误差和时间。这个顺序避免读者误以为完全不需要高保真计算。

## 13. 文笔画像与语言习惯

本文语言是航空工程 + 机器学习混合风格。高频词包括 aerodynamic、model、method、flight、projectile、unsteady、prediction、simulation、DNN-TL、CFD/RBD、source domain、target domain。

语气偏强但以数值支撑。作者常用 “accurately predict”“enhance simulation efficiency”“better generalization capability” 等性能 claim，但紧跟误差表和对比图。

被动语态用于方法和实验，如 “the model is trained”“samples are generated”；主动语态用于贡献总结，如 “we propose”。时态上，方法定义用一般现在时，结果分析用过去时和现在时混合。

情态动词较少，更多使用 can 表示能力。与生物论文不同，作者较少使用 may/potentially，因为结果主要是数值误差和仿真效率，claim 更直接。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：aerodynamic(123)；model(99)；method(85)；flight(56)；modeling(52)；projectile(51)；unsteady(48)；prediction(48)；simulation(45)；org(44)；dnn-tl(38)；dual-spin(37)；case(36)；based(35)；domain(34)；aerospace(30)；lstm(30)；layer(27)；trajectory(26)；cfd(25)
- 高频学术名词：model(99)；simulation(90)；method(85)；prediction(48)；analysis(28)；moment(23)；science(22)；comparison(20)；results(19)；validation(18)；interpolation(14)；extrapolation(14)；parameters(12)；equation(12)；equations(10)；velocity(10)
- 高频学术动词：shown(20)；proposed(20)；compared(13)；predicted(10)；predict(8)；shows(5)；indicates(3)；developed(3)；estimated(2)；solve(2)；solved(2)；indicate(2)；validate(1)；evaluate(1)；validated(1)；propose(1)
- 高频形容词：aerodynamic(123)；dynamic(24)；neural(23)；different(23)；moment(23)；initial(15)；nonlinear(12)；computational(10)；represent(10)；high(9)；lateral(7)；normal(6)；small(5)；current(5)；previous(5)；large(4)
- 高频副词/连接副词：respectively(18)；fully(8)；significantly(6)；however(6)；accurately(6)；commonly(5)；moreover(4)；greatly(3)；randomly(3)；therefore(2)；strongly(2)；mainly(2)；similarly(2)；finally(2)；primarily(2)；furthermore(1)
- 高频二词短语：aerodynamic modeling(33)；aerodynamic model(30)；dual-spin projectile(28)；unsteady aerodynamic(25)；aerospace science(21)；science technology(21)；forces moments(21)；source domain(20)；cfd rbd(19)；dnn-tl method(19)；trajectory simulation(18)；prediction case(18)；aerodynamic forces(16)；coupled cfd(15)；rbd method(12)；aft body(12)
- 高频三词短语：aerospace science technology(21)；aerodynamic forces moments(15)；coupled cfd rbd(14)；cfd rbd method(12)；unsteady aerodynamic modeling(11)；aerodynamic modeling method(8)；extrapolation prediction case(7)；aerosp sci technol(7)；flight trajectory simulation(6)；interpolation prediction case(6)；source domain target(5)；domain target domain(5)

**主动、被动与句法**

- 被动语态估计次数：105
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：632
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：198
- 一般过去时线索：41
- 现在完成时线索：4
- 情态动词线索：43
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：aerodynamic(44)；model(32)；flight(30)；method(25)；unsteady(18)；projectile(17)；modeling(16)；simulation(13)
- 2. Aerodynamic modeling method                                  where, Fx,Fy, and Fz represent the axial force, normal force, and lateral：aerodynamic(78)；model(67)；method(59)；prediction(46)；org(43)；case(36)；modeling(35)；projectile(34)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：unsteady aerodynamic modeling, dual-spin projectile, coupled CFD/RBD, deep neural network, transfer learning, source domain, target domain, aerodynamic forces and moments, trajectory simulation。

可复用 gap 句式：

- “However, the efficiency is compromised by the large number of CFD calculations required.”
- “There remains a need for ... particularly in model applicability for various flight states.”
- “To accelerate the flight trajectory simulation, the simulation driven by the aerodynamic model is of concern.”

可复用方法句式：

- “The time-delay effects both of flight states and aerodynamic forces and moments are considered in the inputs.”
- “We fine-tune the pre-trained model with a small amount of data when the initial flight states change.”
- “The established model is further used for fast and accurate flight trajectory simulations.”

可复用结果句式：

- “The predicted values remain close to the high-fidelity results.”
- “The errors accumulate and increase over time.”
- “The simulation efficiency can be increased by three orders of magnitude.”

## 15. 引用策略与文献使用

引用策略按问题链组织。首先引用双旋弹、制导弹和 Magnus effect 文献，证明对象复杂。其次引用 CFD/RBD 和高保真流固耦合/刚体动力学方法，说明精度基准。然后引用 white-box 和 black-box 非定常气动模型，包括 aerodynamic derivative、state-space、Kriging、ARMA、LSTM 和神经网络。

作者对前人评价有分寸：ARMA 快但非线性能力不足，LSTM 有历史建模能力但泛化不佳，CFD/RBD 精确但成本高。本文在这些方法之间找位置：用 CFD/RBD 做数据源，用 DNN 表达非线性，用 TL 解决跨工况。

附录中介绍 ARMA 和 LSTM，说明对比方法不是稻草人。这是机器学习工程论文中重要的审稿防御。

## 16. 审稿人视角风险

1. 数据成本风险：轨迹仿真很快，但训练数据仍需 coupled CFD/RBD 生成，若新任务跨度很大，前置成本仍高。
2. 外推风险：extrapolation case 最大 δe 已升至 6.74%，更远离源域时性能可能快速下降。
3. 物理可解释性风险：DNN-TL 难以解释具体气动机理，可能被质疑可靠性和安全认证。
4. 初始化依赖风险：轨迹仿真仍需要前三个 CFD/RBD 时间步获得输入，完全替代程度有限。
5. 不确定性风险：文中主要给 MRE/δR，没有系统置信区间或不确定性传播。
6. 工况覆盖风险：只围绕特定弹型、Ma、高度和自旋状态，是否适用于大机动、不同攻角/舵偏仍需扩展。
7. 误差积累风险：轨迹仿真误差随时间增长，长时间飞行或闭环控制中可能放大。

## 17. 可复用资产

- 选题资产：从“高保真但太慢”与“快速但不准”之间建立方法需求。
- 方法资产：短期历史状态 + 历史气动力的输入构造，非常适合非定常代理建模。
- 迁移资产：source domain pre-training + target domain small-data fine-tuning 的跨工况写法。
- 验证资产：validation/interpolation/extrapolation 三层验证，比单一测试集更有说服力。
- 图表资产：DNN 输入结构图、迁移学习流程图、CFD/RBD 流程图、误差随参数变化图、预测曲线对比表、轨迹仿真结果图。
- 写作资产：把“效率提升”放在最终工程任务中，而不是只报告单步预测误差。

## 18. 对我写论文的启发

最值得学习的是验证层级设计。很多代理模型论文只做随机测试集误差，本文专门区分 validation、interpolation 和 extrapolation，让“泛化能力”不只是口号。

第二个启发是，数据驱动模型要交代数据源。作者详细说明 CFD/RBD、网格、飞行动力学和样本域，使读者知道网络学习的是高保真物理数据而非随意数据。

第三个启发是，工程价值最好落到最终任务。本文不仅预测气动力，还把模型放进轨迹仿真，报告从 20 小时到几秒的效率差，这比单独报告 δe 更能说服航空航天工程读者。

## 19. 最终浓缩

这篇论文的核心贡献是用 DNN-TL 为双旋弹建立可迁移的非定常气动代理模型：输入短期历史飞行状态和气动响应，用 CFD/RBD 数据预训练，再用少量新工况数据 fine-tune，在插值和外推初始条件下优于 ARMA 和 LSTM/LSTM-TL，并将轨迹仿真从约 20 小时加速到几秒。

最大风险是模型仍强依赖 CFD/RBD 数据域，外推范围、物理可解释性和长时间误差积累需要进一步验证。

可迁移到自己论文中的三件事：第一，把泛化问题拆成源域/目标域；第二，验证时区分插值和外推；第三，用最终工程流程的效率和误差证明代理模型价值。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.txt` 与 `801/文本/metadata/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 Aerodynamic modeling method （方法/模型）
  - L3 p.3: 2.1 Deep neural network for aerodynamic modeling （方法/模型）
  - L3 p.5: 2.2 Transfer learning based on the pre-training （对象/问题/模块）
  - L3 p.5: 2.3 Aerodynamic modeling method based on DNN-TL （方法/模型）
- L2 p.6: 3 Samples generation of aerodynamic modeling and prediction （方法/模型）
  - L3 p.6: 3.1 Computational model and simulation settings （方法/模型）
  - L3 p.6: 3.2 Numerical method （方法/模型）
    - L4 p.6: 3.2.1 Unsteady N-S equations （对象/问题/模块）
    - L4 p.9: 3.2.2 Flight dynamic equations （对象/问题/模块）
    - L4 p.9: 3.2.3 Coupled CFD/RBD method （方法/模型）
  - L3 p.9: 3.3 Generation of the unsteady aerodynamic dataset （对象/问题/模块）
- L2 p.9: 4 Results and discussions （结果/讨论/验证）
  - L3 p.9: 4.1 Parameter analysis of the DNN-TL （对象/问题/模块）
  - L3 p.12: 4.2 Aerodynamic modeling and results analysis （方法/模型）
    - L4 p.12: 4.2.1 Result analysis of the validation case （结果/讨论/验证）
    - L4 p.12: 4.2.2 Result analysis of the interpolation prediction case （结果/讨论/验证）
    - L4 p.15: 4.2.3 Result analysis of the extrapolation prediction case （结果/讨论/验证）
  - L3 p.15: 4.3 Flight trajectory simulation based on aerodynamic model （方法/模型）
- L2 p.15: 5 Conclusions （结论）
- L2 p.17: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.17: Declaration of competing interest （对象/问题/模块）
- L2 p.17: Acknowledgments （对象/问题/模块）
- L2 p.17: Appendix A: Computational grids of the dual-spin projectile （附录）
- L2 p.18: Appendix B: ARMA method for aerodynamic modeling （方法/模型）
- L2 p.19: Appendix C: LSTM network for aerodynamic modeling （方法/模型）
- L2 p.19: datalink4 （对象/问题/模块）
- L2 p.19: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Aerodynamic modeling method | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Deep neural network for aerodynamic modeling | 3 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Transfer learning based on the pre-training | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Aerodynamic modeling method based on DNN-TL | 5 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Samples generation of aerodynamic modeling and prediction | 6 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Computational model and simulation settings | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Numerical method | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2.1 Unsteady N-S equations | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2.2 Flight dynamic equations | 9 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2.3 Coupled CFD/RBD method | 9 | 4 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Generation of the unsteady aerodynamic dataset | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Results and discussions | 9 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Parameter analysis of the DNN-TL | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Aerodynamic modeling and results analysis | 12 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.1 Result analysis of the validation case | 12 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.2 Result analysis of the interpolation prediction case | 12 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.3 Result analysis of the extrapolation prediction case | 15 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 Flight trajectory simulation based on aerodynamic model | 15 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 15 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix A: Computational grids of the dual-spin projectile | 17 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix B: ARMA method for aerodynamic modeling | 18 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix C: LSTM network for aerodynamic modeling | 19 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| datalink4 | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 19 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 为了评估双旋弹丸的飞行性能和气动特性，通常采用计算流体动力学和刚体动力学耦合（CFD/RBD）方法，该方法可以同时求解飞行力学和流场。然而，所需的大量 CFD 计算会影响效率。本文开发了一种结合深度神经网络和迁移学习的非定常空气动力学建模方法，可以准确预测不同初始条件下双自旋弹丸的非定常空气动力学。考虑到短期历史时刻飞行状态和气动数据的影响，我们将它们整合作为气动模型的输入特征，以减少长期历史数据的影响。为了增强不同初始条件下模型的泛化能力，我们通过迁移学习在新条件下使用少量数据对构建的空气动力学模型进行微调。分别通过内插和外推预测案例验证了所提出的方法。结果表明，该方法在双自旋弹丸非定常气动建模中比长短期记忆神经网络和自回归移动平均法具有更好的精度和泛化性。
> 
> 通过将飞行动力学方程与时域空气动力学模型耦合，飞行模拟只需几秒钟，与耦合的CFD/RBD方法相比，可以减少三个数量级的计算时间。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Unsteady-aerodynamic-modeling-and-flight-trajectory-simu_2024_Aerospace-Scie.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 本文提出了一种基于DNN和迁移学习的双旋弹丸非定常气动建模方法，并进行了三个测试用例来验证和评估该方法。此外，该方法构建的气动模型用于飞行轨迹仿真，以提高仿真效率。结论如下：
> 
> 参数δe/%
> 
> θ 0.12 α 5.69 β 1.31
> 
> (1)所提出的DNN-TL方法可以准确地模拟不同初始条件下双旋弹丸的气动特性，所有力和力矩的预测误差均小于6%，但所提出的方法的精度
> 
> W. Ji 等人。航天科技155(2024)109711
> 
> 当将该方法应用于外推预测时，该方法会减少。 (2)基于所建立的气动模型进行双自旋弹丸飞行轨迹仿真相比CFD/RBD耦合仿真能够显着提高仿真效率，δe < 8%。 (3)与常用的ARMA方法和LSTM网络相比，所提出的DNN-TL方法在预测气动力和力矩方面表现出更好的泛化能力和更高的精度。 (a) 相对于 t 的变化
> 
> 参数δe /%
> 
> θ 0.61 α 7.65 β 1.66

### 20.7 论文逻辑脉络复核

- 提出的问题：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the above parameters.
- 旧方法/已有研究不足：However, the efficiency is compromised by the large number of CFD calculations required. By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method. However, the efficiency is compromised by the large number of CFD calculations required.
- 本文解决方式：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simultaneously solve the flight mechanics and flow field. This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin projectiles under varying initial conditions. Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
- 学术/工程增量：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：79
- Introduction 引用簇数量（估计）：28
- References 条目数（解析）：45
- 可识别年份条目数：77
- 近五年/近年文献（2021+）数量：41
- 经典文献（2010年前）数量：2
- 同刊引用数量（按 subject 粗略匹配）：2
- 高频来源期刊（粗略）：Aerospace Science and Technology(2)
- 引用簇样例：[7], [1], [8], [9], [1,2], [10], [3], [11,12], [4,5], [6], [20], [21]

带引用的 gap/转折句样例：

- By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method. the angle of attack plane, leading to cross-coupling between longitudinal and lateral motions, and strong coupling among pitch, yaw, and roll motions [7].
- The black-box method is a data-driven modeling method, which can build an input-output mapping model directly by a surrogate model [15] or machine learning approach [14], providing more powerful nonlinear description capabilities.
- Recently, another type of white-box method building aerodynamic model by system identification with explicit expressions, such as Kriging [21] and autoregressive moving average (ARMA) [22] methods, have been developed and applied to unsteady aerodynamic modeling.
- Black-box methods, such as neural networks [25–27], can ignore physical features when constructing unsteady aerodynamic models.

References 解析样例（前12条）：

- [1] Y. Wang, J. Yu, X. Wang, et al., A guidance and control design with reduced information for a dual-spin stabilized projectile [J], Defence Techn. 33 (2024) 494–505, https://doi.org/10.1016/j.dt.2023.07.007.
- [2] J. Norris, A. Hameed, J. Economou, et al., A review of dual-spin projectile stability [J], Defence Techn. 16 (1) (2020) 1–9, https://doi.org/10.1016/j.dt.2019.06.003.
- [3] J. Karimi, M.R. Rajabi, S.H. Sadati, et al., Multidisciplinary design optimization of a dual-spin guided vehicle [J], Defence Techn. 37 (2023) 133–148, https://doi.org/ 10.1016/j.dt.2023.11.025.
- [4] Q. Chen, T. Hu, P. Liu, et al., The dynamic vortical flow behaviour on a coplanar canard configuration during large-amplitude-pitching [J], Aerosp. Sci. Technol. 112 (2021) 106553, https://doi.org/10.1016/j.ast.2021.106553.
- [5] T. Hu, Y. Zhao, P. Liu, et al., Investigation on lift characteristics of a double-delta wing pitching in various reduced frequencies [J], J. Aerospace Eng. 235 (14) (2021) 2081–2094, https://doi.org/10.1177/0954410021992201.
- [6] F. Askary, M.R Soltani, Effects of mach numbers on magnus induced surface pressure [J], Chin. J. Aeronautics 33 (12) (2020) 3058–3072, https://doi.org/ 10.1016/j.cja.2020.04.027.
- [7] K. Shi, M. Liu, Trajectory analysis of a dual-spin-stabilized projectile with fixedcanards for the precision guidance kit [J], J. Aerospace Eng. 236 (13) (2022) 2620–2632, https://doi.org/10.1177/
- 09544100211064759.
W. Ji et al. Aerospace Science and Technology 155 (2024) 109711
Fig. C1. Architecture of an LSTM network.
LSTM layer 200 Relu layer / Fully connected layer 1 200 Fully connected layer 2 200 Fully connected layer 3 200 Training algorithm Adam Initial learning rate 0.001 Training epochs 2000 Batch size 128
- [8] X. Zhao, J. Shi, Z. Wang, et al., Nonlinear aerodynamic modeling and analysis on body of fixed canard dual-spin projectiles [C], in: International Conference on Mechanical System Dynamics, Singapore, Springer Nature Singapore, 2023, pp. 3759–3774, https://doi.org/10.1007/978-981-99-8048-2_263.
- [9] F. Seve, S. Theodoulis, P. Wernert, et al., Flight dynamics modeling of dual-spin guided projectiles [J], IEEE Trans. Aerosp. Electron. Syst. 53 (4) (2017) 1625–1641, https://doi.org/10.1109/TAES.2017.2667820.
- [10] F. Nicolosi, A. De Marco, V. Sabetta, et al., Roll performance assessment of a light aircraft: flight simulations and flight tests [J], Aerosp. Sci. Technol. 76 (2018) 471–483, https://doi.org/10.1016/j.ast.2018.01.041.
- [11] L. Yan, X. Chang, N. Wang, et al., Aerodynamic identification and control law design of a missile using machine learning [J], AIAA J. 61 (7) (2023) 2998–3018, https://doi.org/10.2514/1.J062801.

### 20.9 常用词、词类、语态与时态

- 高频词：aerodynamic(106)；flight(49)；projectile(45)；fig(45)；prediction(42)；simulation(40)；modeling(39)；dnn-tl(38)；case(36)；unsteady(34)；dual-spin(34)；domain(34)；lstm(29)；layer(27)；dnn(24)；cfd(24)；moments(24)；arma(24)；moment(23)；trajectory(22)
- 高频名词化/学术名词：prediction(42)；simulation(40)；moment(23)；science(21)；interpolation(14)；extrapolation(13)；dynamics(10)；velocity(10)；aerodynamics(9)；validation(9)；high-fidelity(6)；equation(6)；section(6)；characteristics(5)；generalization(5)
- 高频学术动词：compared(13)；predicted(10)；predict(8)；developed(3)；presented(3)；indicate(2)；estimated(2)；validated(1)；propose(1)；showed(1)；validate(1)
- 高频形容词：aerodynamic(106)；moment(23)；table(20)；neural(15)；initial(15)；computational(10)；represent(10)；dynamic(8)；lateral(7)；normal(6)；current(5)；previous(5)；historical(4)；total(4)；available(3)
- 高频副词：respectively(18)；fully(8)；accurately(6)；commonly(5)；only(3)；greatly(3)；randomly(3)；significantly(3)；mainly(2)；similarly(2)；finally(2)；primarily(2)；neously(1)；highly(1)；ally(1)
- 高频二词短语：aerodynamic modeling(27)；dual-spin projectile(27)；forces moments(21)；aerospace science(20)；science technology(20)；source domain(20)；page aerospace(19)；unsteady aerodynamic(18)；cfd rbd(18)；prediction case(18)；aerodynamic forces(16)；trajectory simulation(15)
- 高频三词短语：aerospace science technology(20)；page aerospace science(19)；aerodynamic forces moments(15)；coupled cfd rbd(14)；unsteady aerodynamic modeling(8)；science technology fig(7)；extrapolation prediction case(7)；interpolation prediction case(6)；flight trajectory simulation(5)；source domain target(5)；domain target domain(5)；rolling moment aft(5)
- 被动语态估计：88；`we + 动作动词` 主动句估计：1
- 一般现在时线索：200；一般过去时线索：304；现在完成时线索：2；情态动词线索：43

章节词频：

- Abstract: aerodynamic(7)；flight(5)；dual-spin(3)；dynamics(3)；cfd(3)；unsteady(3)；conditions(3)；data(3)
- Introduction: aerodynamic(40)；flight(26)；unsteady(16)；projectile(14)；modeling(13)；dual-spin(11)；simulation(11)；neural(10)
- Conclusion: aerodynamic(5)；simulation(5)；projectile(3)；flight(2)；trajectory(2)；enhance(2)；efficiency(2)；parameter(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [3], and we can assess the flight performance of the projectile based on the above parameters.
  可迁移模板：Accurate predictions of aerodynamic characteristics and flight trajectory of the projectile are essential to obtain flight states, impact point distribution, and flight stability [X], and we can assess the flight performance of the projectile based on the above parameters.
#### Gap句
- 原句/结构：However, the efficiency is compromised by the large number of CFD calculations required.
  可迁移模板：However, the efficiency is compromised by the large number of METHOD calculations required.
- 原句/结构：However, the efficiency is compromised by the large number of CFD calculations required.
  可迁移模板：However, the efficiency is compromised by the large number of METHOD calculations required.
- 原句/结构：However, the high computational cost of the CFD simulations makes the method unsuitable for engineering applications.
  可迁移模板：However, the high computational cost of the METHOD simulations makes the method unsuitable for engineering applications.
#### 方法句
- 原句/结构：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.
  可迁移模板：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (METHOD/METHOD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.
- 原句/结构：This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin projectiles under varying initial conditions.
  可迁移模板：This paper develops an unsteady aerodynamic modeling method that combines deep neural networks and transfer learning, which can accurately predict unsteady aerodynamics of dual-spin projectiles under varying initial conditions.
- 原句/结构：Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
  可迁移模板：Considering the influence of flight state and aerodynamic data from short-term historical moments, we integrate them as input features of the aerodynamic model to reduce the impact of long-term historical data.
#### 结果句
- 原句/结构：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
  可迁移模板：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
- 原句/结构：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
  可迁移模板：The results indicate that the proposed method can achieve better accuracy and generalizability than long short-term memory neural networks and autoregressive moving average method in unsteady aerodynamic modeling of the dual-spin projectile.
- 原句/结构：The coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
  可迁移模板：The coupled METHOD/METHOD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [X,X], thus it can achieve high-fidelity.
#### 贡献句
- 原句/结构：The coupled CFD/RBD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [11,12], thus it can achieve high-fidelity.
  可迁移模板：The coupled METHOD/METHOD method can provide both the unsteady aerodynamics characteristics and the flight dynamics characteristics in an integrated manner without using a database [X,X], thus it can achieve high-fidelity.
- 原句/结构：The white-box method usually establishes a mathematical model with a known structure and parameters, thus it has good interpretability.
  可迁移模板：The white-box method usually establishes a mathematical model with a known structure and parameters, thus it has good interpretability.
- 原句/结构：Bagherzadeh et al. [34] used a neural network to establish an aerodynamic model based on flight testing data for aircraft maneuvering at a high angle of attack, which can greatly enhance model accuracy in comparison with the traditional dynamic derivative model.
  可迁移模板：Bagherzadeh et al. [X] used a neural network to establish an aerodynamic model based on flight testing data for aircraft maneuvering at a high angle of attack, which can greatly enhance model accuracy in comparison with the traditional dynamic derivative model.
#### 限制/边界句
- 原句/结构：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.
  可迁移模板：To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (METHOD/METHOD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.
- 原句/结构：By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled CFD/RBD method.
  可迁移模板：By coupling the flight dynamics equations with the aerodynamic model in the time domain, the flight simulation only takes a few seconds, which can reduce computing time by three orders of magnitude compared to the coupled METHOD/METHOD method.
- 原句/结构：Aerospace Science and Technology 155 (2024) 109711 Contents lists available at ScienceDirect Aerospace Science and Technology journal homepage: www.elsevier.com/locate/aescte To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (CFD/RBD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.
  可迁移模板：Aerospace Science and Technology X(X) XContents lists available at ScienceDirect Aerospace Science and Technology journal homepage: www.elsevier.com/locate/aescte To evaluate flight performance and aerodynamic characteristics of a dual-spin projectile, the coupled computational fluid dynamics and rigid body dynamics (METHOD/METHOD) method is commonly used, which can simultaneously solve the flight mechanics and flow field.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
