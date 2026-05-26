# A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-heat-flux-distribution-prediction-method-for-hyperson_2025_Aerospace-Scien.txt` 的 PyMuPDF 全文抽取。由于 txt 由双栏 PDF 抽取得到，部分图表编号、表格内容和段落顺序存在串栏，涉及图像形态、曲线细节、热流分布云图和表格精确数值时均标注“需要 PDF 图像复核”。本文不复述长段原文，只抽取关键词和论证功能。

## 1. 基本信息与论文身份

- 题名：A heat flux distribution prediction method for hypersonic flight vehicle along trajectory based on POD and TSCN。
- 作者：Wenyu Huang, Chunna Li, Chunlin Gong, Xiaowei Wang。
- 期刊与年份：Aerospace Science and Technology, 2025, 163, 110283。
- 研究对象：高超声速再入飞行器沿轨迹的表面热流分布，验证对象为再入胶囊。
- 论文类型：数据驱动代理模型/降阶模型方法论文，带工程算例验证。
- 核心方法：POD 降维提取热流模态；TSCN 结合 TCN 与 CNN，分别处理近期飞行状态的时间特征和非均匀壁温的空间特征；与 CST 耦合替代 CHT 中的 CFD 计算。
- 主要证据：15 条可能轨迹训练、3 条测试轨迹、POD 模态数与历史输入长度分析、超参数搜索、消融对比、传统 HFDP 方法对比、DBA 预测区间。
- 目标读者：气动热/热防护仿真研究者、飞行器热管理设计人员、希望把 CFD/CST 耦合替换成 ROM 的工程应用者。

## 2. 摘要与核心信息提取

这篇论文的一句话主张是：沿轨迹热流分布不仅受当前飞行状态影响，还受近期飞行状态和壁温场影响，因此应把高维热流先用 POD 降到模态系数，再用能同时处理时间和空间信息的 TSCN 预测模态系数，从而在 CHT 分析中以约 200 倍效率替代 CFD。

摘要的信息组织很标准：先说“accurate and rapid determination”对高超声速飞行器很关键；再指出 transient CFD 使 CHT prohibitively expensive；随后提出 POD + TSCN；再说明 TSCN 输入来自 recent flight states 与 non-uniform wall temperatures；最后用再入胶囊算例给出小于 2% 平均相对误差和一小时内获得新轨迹热流分布的效率卖点。

核心信息不是“用了神经网络”，而是“把 CHT 中最耗时的 CFD 子环节替换为可迭代耦合的热流 ROM”。因此文章的工程价值比单点预测更强：它把预测模型放回 CST 迭代流程中，关注误差累积、轨迹边界、预测区间，而不只是离线拟合精度。

## 3. 选题层深拆

选题来源是典型工程瓶颈：高超声速飞行器沿轨迹飞行时，飞行状态快速变化，流场未必达到稳态，同时结构壁温又通过 CHT 反向影响气动加热。传统 CFD/CST 时间步耦合很慢，若每个时间步都跑 CFD，会使轨迹级热分析成本过高。

作者把大问题收束为一个可建模问题：给定近期飞行状态序列和上一时刻壁温分布，预测当前时刻表面热流分布。这个定义避免了泛泛地说“热流预测”，而是明确了输入、输出和耦合位置：输入是历史 flight states 与 wall temperature，输出是 heat flux distribution，应用场景是 CHT 时间推进。

选题价值分三层：工程上提高热防护设计与热管理效率；方法上处理瞬态轨迹热流预测中历史状态和空间壁温共同作用；系统上让气动 ROM 能与 CST 迭代稳定耦合。它不是单纯替代一次 CFD，而是替代整条轨迹上的重复 CFD。

## 4. 领域位置与文献版图

Introduction 将已有 heat flux prediction 分成三类：基于降维的建模、逐点建模、嵌入气动物理信息的建模。第一类能降低高维热流复杂度，但多数忽略瞬态 CHT 与壁温影响；第二类有局部适应性，但全局分布建模效率和泛化较弱；第三类借助边界层或流场特征增强泛化，但多基于稳态气动热数据。

作者又引入 transient aerodynamic modeling 文献作为方法借鉴，包括 ARMA、Volterra、Kriging、CNN、RNN、GRU、LSTM、CNN-LSTM、ConvLSTM 等。这一段的作用是把问题从“热流预测”扩展到“时间序列气动建模”，为 TCN/CNN 组合做铺垫。

本文站位是：继承 POD 降维的高维场压缩能力，吸收 TCN 处理历史输入的优势和 CNN 处理空间壁温分布的优势，把二者放进 CHT 迭代中。它与最接近工作的差异在于显式考虑 recent flight states、non-uniform wall temperature 和预测误差在 CST 耦合过程中的传播。

## 5. Gap 制造机制

文章制造的 gap 有三个层次。第一是场景 gap：已有 HFDP 多面向稳态或轨迹点预测，缺少沿完整轨迹、含时间滞后效应的分布预测。第二是方法 gap：传统热流预测没有同时处理高维分布、历史飞行状态和非均匀壁温。第三是工程部署 gap：ROM 若要替代 CFD 参与 CHT，必须兼具精度、泛化性和稳定性，而现有方法尚不足。

这个 gap 的说服力较强，因为作者没有只说“计算慢”，而是解释了慢的物理原因：流场在快速变化的飞行状态下未充分稳定，当前热流仍受先前状态影响；同时壁温由上一时刻热流和 CST 更新而来，构成闭环。这使“时间-空间联合输入”变成必要选择。

可被审稿人追问的是：15 条轨迹是否足以覆盖“possible trajectories”；TSCN 的优势是否来自结构本身，还是来自更合适的输入组合；以及 transient CFD/CST 的基准设置是否足够代表真实高超声速任务。

## 6. 创新性判断

作者声明的贡献主要包括：用 POD+TSCN 替代 CFD 参与 CHT，使新轨迹热流分布在一小时内获得；TSCN 同时利用近期飞行状态和非均匀壁温，提高精度；用 DBA 给出预测区间以增强可靠性。

真实创新属于方法整合与工程流程创新。POD、CNN、TCN、dropout Bayesian approximation 都不是新概念，新意在于把它们组合成适合“轨迹级瞬态热流分布 + CHT 耦合”的模型结构，并证明模型在迭代使用时仍可控。

创新强度：中到强。强在场景定义和系统闭环，弱在深度学习模块本身并非原创。若审稿人强调算法原创性，文章可能被质疑为工程集成；但若从 Aerospace Science and Technology 的应用导向看，200 倍效率和低误差验证足以支撑贡献。

## 7. 论证链条复原

论证链条如下：

1. 高超声速飞行器热流时空变化强，热流分布对结构、材料、热防护和控制有直接影响。
2. 沿轨迹 CHT 需要 CFD 与 CST 紧耦合，CFD 时间成本使全轨迹分析昂贵。
3. 现有 HFDP 方法忽略历史飞行状态、壁温非均匀性或高维热流分布问题，不能稳定替代 CHT 中的 CFD。
4. 将热流分布用 POD 表示为低维模态系数，可降低输出维度和过拟合风险。
5. 用 TCN 提取近期飞行状态的时间特征，用 CNN 提取壁温空间特征，融合后预测 POD 系数。
6. 将预测热流作为 CST 边界条件，迭代推进整条轨迹。
7. 在再入胶囊与多轨迹数据集上验证误差、效率、消融和不确定性区间。

逻辑闭合度较高。最薄弱环节在于真实飞行适用性：模型训练数据来自数值仿真轨迹，若轨迹、几何、气体模型或壁温边界超出训练域，结论是否仍成立需要更多外推验证。

## 8. 方法/理论/模型细拆

方法结构可以拆成四步。第一步是 CHT 问题离散：连续时间离散为 K 个时间步，表面热流和壁温在 P 个气动网格节点上离散。第二步是 POD：把高维热流矩阵分解为模态和模态系数，用少数模态保留主要能量。第三步是 TSCN：TCN 分支输入 `[Xk, Xk-1, ...]` 形式的近期飞行状态，CNN 分支输入上一时刻壁温分布，融合后输出当前热流 POD 系数。第四步是耦合预测：系数乘以 POD 模态重构热流，送入 CST 得到下一时刻壁温，再进入下一次预测。

关键假设包括：近壁区域热流可由类似 Fourier law 的局部温度梯度关系描述；有限长度的近期状态足以代表主要历史影响；训练轨迹覆盖了测试轨迹的可行范围；POD 模态能以较少维度表达主要热流空间结构。

复现信息相对充分：给出了硬件软件环境、优化器、学习率、TCN/CNN 超参数候选、POD 模态选择、训练轨迹数量、评价指标和消融模型。但真实复现仍需要 CFD/CST 数据生成细节、网格、边界条件和训练集轨迹参数，txt 中部分表格需要 PDF 复核。

## 9. 证据系统与 Claim-Evidence 表

主要证据系统由五类组成：POD 模态数和轨迹样本量的参数分析；TSCN 超参数调优；TCN/CNN/FCL/LSTM/GRU/RNN 等消融对比；三条测试轨迹上的时空误差分布；DBA 预测区间可靠性。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| POD+TSCN 可在 CHT 中替代耗时 CFD | 摘要、结论、4.3 | 单时间步预测约 0.035 s，新轨迹热流分布约一小时完成，传统 CHT 约慢 200 倍 | 强 | 传统 CHT 基准和硬件/软件条件需 PDF 与设置复核 |
| TSCN 沿轨迹热流预测平均相对误差低于 2% | 摘要、结论、Fig. 11/12、表格 | 3 条测试轨迹的预测热流与 CFD/CST 计算热流对比 | 强 | 误差定义、空间平均方式和关键点误差需 PDF 图像复核 |
| 近期飞行状态是必要输入 | Introduction、Table 4 | 消融对比显示仅壁温 CNN 精度最低，TCN 处理 recent states 优于 LSTM/GRU/RNN/FCL | 中强 | 模型容量是否一致、训练公平性需复核 |
| 非均匀壁温空间特征需要 CNN 分支 | 3.2、4.2、Table 4 | CNN 分析 wall temperature 优于 FCL，联合输入获得最高精度 | 中强 | 壁温场网格排列和 CNN 一维卷积方式需图/代码复核 |
| 15 条轨迹训练可获得较高精度 | Table 1 附近 | 训练轨迹数从 3 到 15 时误差降低，15 条时相对误差约 3% 或更低 | 中 | 训练轨迹采样覆盖边界有限；外推风险较大 |
| DBA 可给出覆盖大部分真实热流的预测区间 | Fig. 13、4.3 | dropout 测试 50/200/800 次形成预测区间，并覆盖关键热流持续时间 | 中 | 区间校准、置信水平和覆盖率定义需要 PDF/代码复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 展示传统 CHT 中 CFD 与 CST 耦合关系 | CFD 是瓶颈 | 每个时间步需 CFD 更新热流，再交给 CST | 需要 PDF 图像复核 |
| Fig. 3/Fig. 4 | 展示 HFDP+CSS/TSCN 替代流程 | ROM 可嵌入 CHT | 预测热流替代 CFD，形成迭代闭环 | 需要 PDF 图像复核 |
| Eq. (1)-(2) | 定义热流/壁温离散和近壁热流关系 | 热流受壁温与近壁温度影响 | 把物理量转成模型输入输出 | 公式抽取有串栏，需 PDF 复核 |
| POD 相关公式 | 高维热流降维 | 输出降维可提高建模稳定性 | 模态系数作为 TSCN 输出 | 需 PDF 复核符号 |
| Fig. 5/Fig. 6 | 展示 TCN 与 CNN 模块 | TSCN 能处理时间和空间特征 | 因果膨胀卷积处理历史状态，CNN 处理壁温分布 | 需要 PDF 图像复核 |
| Table 1 | 训练轨迹数量敏感性 | 数据覆盖改善精度 | 3 条轨迹已可用，15 条更稳定 | 表格串栏，需 PDF 复核 |
| Fig. 11/Fig. 12 | 时空热流预测误差验证 | 平均误差低、关键时刻可用 | 误差在高热流区域和后期积累更明显 | 云图细节需 PDF 复核 |
| Table 6 | 与传统方法对比 | TSCN 优于不考虑历史状态的方法 | POD+BPNN、point-by-point MLP 不及 TSCN | 表格需 PDF 复核 |
| Fig. 13 | DBA 预测区间 | 模型可输出可靠区间 | 测试次数越多区间越稳定 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节大致为：1 Introduction；2 Problem description；3 Heat flux distribution prediction method，其中含 POD 与 TSCN；4 Numerical/validation 部分，含 physical model and dataset sampling、modelling、discussion；5 Conclusion。结构是“问题物理定义 → 方法流程 → 算例验证 → 工程讨论”的工程方法论文布局。

Introduction 不是简单综述，而是按方法流派拆分 HFDP，并逐步指出它们为何不能处理轨迹瞬态。Problem description 把 CHT、时间离散、空间离散和热流/壁温关系形式化，是全文最关键的转折：它把选题从工程痛点变成可学习映射。Method 先降维再网络建模，保证读者理解为什么输出不是直接高维场。Validation 从数据集、参数选择、消融、误差分布到不确定性，证据顺序较完整。

标题命名偏好偏描述型和方法型，例如 “Problem description”“Temporal-spatial convolution”“Physical model and dataset sampling”。优点是工程读者易定位；不足是部分标题不提前暴露结论，如“Discussion”较泛，若改成“Efficiency and uncertainty of TSCN-CST coupling”会更有信息量。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-heat-flux-distribution-prediction-method-for-hyperson_2025_Aerospace-Scien.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：2
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：章节标题数量较少，难以判断并列性。
- 章节名主要风格：描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Problem description | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Modelling | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段承担背景和工程必要性，先讲热流对 geometry、structure、materials、thermal protection 和 control 的影响，再指出 CFD/CST 成本。第二组段落做文献分类，每类都是“能解决什么 → 忽略什么”。第三组段落引入瞬态气动建模，完成从 HFDP 到 TCN/CNN 的方法迁移。

方法段落节奏是“先定义物理量，再压缩输出，再说明网络输入，再说明闭环使用”。这种节奏适合写代理模型论文：先让读者相信输出变量和物理过程清楚，再引入机器学习，否则容易显得黑箱。

结果段落通常从表/图起手：“Table/Figure shows...”，然后解释趋势，例如训练轨迹越多误差越低、历史序列过短/过长都有问题、误差在热流峰值后积累。讨论段落把数值误差解释为 CHT 迭代传播，是比普通结果描述更有说服力的地方。

## 13. 文笔画像与语言习惯

整体语气是工程应用型，强调 accurate、rapid、efficient、prediction、trajectory、distribution、CHT、CFD。claim 强度较强，常用 “effectively replaces”“achieving”“outperforming”“efficiency increase”，但在误差积累、轨迹边界、DBA 区间处又会用 “likely”“suggests” 控制解释边界。

主动语态多用于贡献声明，如 “we propose”“we developed”；被动语态多用于模型训练、数据采样和结果计算，如 “was employed”“was configured”。时态上，一般现在时用于物理事实和图表解释，过去时用于算例设置和实验结果，现在完成时用于文献综述。

名词化程度高：prediction、distribution、reconstruction、dimensionality reduction、generalization、stability。形容词集中在 transient、non-uniform、time-consuming、high-dimensional、spatio-temporal。副词多为 efficiently、accurately、significantly，基本都有数值证据支撑。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：heat(148)；flux(129)；distribution(61)；prediction(58)；model(58)；time(49)；trajectory(42)；trajectories(39)；wall(39)；temperature(39)；flight(37)；along(37)；error(37)；method(36)；states(36)；cfd(31)；convolution(29)；cnn(27)；cht(23)；pod(22)
- 高频学术名词：distribution(61)；model(58)；prediction(58)；temperature(39)；analysis(36)；method(36)；convolution(29)；field(17)；results(16)；condition(14)；validation(14)；science(14)；dimensionality(12)；duration(12)；simulations(10)；decomposition(9)
- 高频学术动词：predicted(21)；proposed(13)；shown(11)；predict(8)；compared(7)；derived(5)；capture(5)；indicate(4)；developed(3)；validate(2)；reveal(2)；shows(2)；demonstrate(2)；propose(2)；demonstrated(2)；simulated(1)
- 高频形容词：temporal(21)；spatial(20)；transient(17)；relative(17)；aerodynamic(17)；neural(17)；boundary(16)；recent(15)；convolutional(13)；traditional(13)；thermal(13)；causal(13)；hypersonic(12)；historical(11)；dynamic(10)；critical(10)
- 高频副词/连接副词：respectively(13)；spatially(8)；fully(8)；consequently(6)；typically(6)；furthermore(5)；however(5)；subsequently(5)；temporally(5)；additionally(5)；efficiently(4)；accurately(4)；highly(4)；specifically(4)；therefore(3)；extremely(3)
- 高频二词短语：heat flux(123)；flux distribution(48)；wall temperature(23)；flight states(16)；aerospace science(13)；science technology(13)；flux prediction(13)；flow field(13)；cht analysis(12)；tscn model(12)；re-entry capsule(12)；neural network(12)；huang aerospace(11)；prediction method(10)；relative error(10)；distribution prediction(9)
- 高频三词短语：heat flux distribution(47)；aerospace science technology(13)；heat flux prediction(13)；huang aerospace science(11)；calculated heat flux(9)；predicted heat flux(8)；flux distribution prediction(7)；proper orthogonal decomposition(7)；conjugate heat transfer(7)；averaged absolute error(7)；flux distribution along(6)；aerosp sci technol(6)

**主动、被动与句法**

- 被动语态估计次数：104
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：767
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：108
- 一般过去时线索：97
- 现在完成时线索：1
- 情态动词线索：27
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：heat(47)；flux(39)；distribution(25)；flight(17)；trajectory(15)；network(15)；wall(14)；along(13)
- 2. Problem description：heat(101)；flux(90)；model(49)；prediction(48)；time(41)；distribution(36)；trajectories(35)；error(33)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频领域词：heat flux、distribution、trajectory、wall temperature、flight states、CHT、CFD、POD、TSCN、TCN、CNN、relative error。

可复用问题句结构：`Accurate and rapid determination of X is essential for Y. However, Z is time-consuming, making A prohibitively expensive.` 可迁移为“先把 X 的工程必要性抬高，再用 Z 的成本制造 gap”。

可复用 gap 句结构：`Existing methods fail to account for both historical states and spatially non-uniform boundary conditions.` 适合用于多源耦合预测问题。

可复用方法句结构：`The high-dimensional field is first reduced to low-dimensional coefficients, which are then predicted by a network designed to extract temporal and spatial features.` 适合 POD/ROM + 神经网络论文。

可复用结果句结构：`The proposed method achieves an average relative error below X and reduces the computational time by Y compared with the traditional workflow.` 这是典型 Aerospace 工程论文的“精度 + 效率”双指标卖点。

## 15. 引用策略与文献使用

引用主要服务三件事：证明高超声速热流预测的重要性；把 HFDP 文献分为降维、逐点和物理嵌入三类；为 TSCN 借用瞬态气动建模中的神经网络方法提供依据。作者对前人多采取“认可价值 + 指出边界”的姿态，不强批判。

gap 与引用的连接方式很清楚：先列已有降维方法能降低复杂度，再指出忽略 wall temperature 和 transient CHT；再列 point-by-point 方法有局部适应性，但全局建模效率不足；再列 physics-embedded 方法可泛化，但多为 steady-state。最后自然推出“trajectory with time-varying flight states”尚未解决。

引用风险在于最接近工作的公平对比需要进一步核查，尤其是已有 ConvLSTM/时序流场模型是否可直接迁移到热流分布；如果审稿人认为 TCN/CNN 组合只是已有时空网络的一种，文章需要依靠 CHT 闭环验证来稳住创新。

## 16. 审稿人视角风险

1. 训练轨迹数量有限，15 条 possible trajectories 是否足以覆盖真实任务空间，尤其是边界轨迹和异常姿态。
2. 误差小于 2% 的统计口径需要核查，是空间平均、时间平均还是全局平均；峰值局部误差可能被平均指标掩盖。
3. CHT 闭环误差会累积，文章虽讨论了滞后峰值，但缺少更长任务或更强非线性工况下稳定性证明。
4. TSCN 与 LSTM/GRU/RNN/FCL 的消融是否参数量公平、训练预算一致，需要代码或附录复核。
5. POD 模态基于训练数据，若出现训练集中没有的热流空间结构，重构上限会受限。
6. DBA 预测区间属于近似不确定性，不能等同严格置信区间，需谨慎使用。

## 17. 可复用资产

可复用选题套路：从“高保真耦合仿真太慢”切入，但不止于加速，而是指出为什么现有代理模型不能进入闭环工程流程。

可复用方法套路：高维场输出先 ROM 降维，再用专门结构预测低维系数，最后回到物理求解器闭环验证。

可复用证据套路：参数敏感性 → 消融 → 与传统方法对比 → 关键时间/空间点可视化 → 不确定性区间。这个顺序很适合机器学习工程代理模型论文。

可复用图表：传统流程与替代流程对照图；网络结构图；训练样本空间覆盖图；关键时刻场分布对比图；误差随时间和空间分布图；预测区间覆盖图。

## 18. 对我写论文的启发

如果写工程代理模型论文，最重要的不是说“模型准确”，而是说清楚模型插在原工作流的哪个位置、替代了什么成本、会不会破坏后续物理耦合。本文的强项正是把 ML 模型从离线预测器提升为 CHT 流程的一部分。

Introduction 可以学习它的“方法流派分类 + 每类不足 + 本文跨越”的写法。Results 可以学习它不只给平均误差，还讨论误差峰值滞后和轨迹边界影响，这让结果更像工程分析而非 leaderboard。

需要避免的是过度依赖平均相对误差。自己的论文若有场预测，应同时报告峰值误差、局部关键区域误差、外推工况误差和闭环稳定性。

## 19. 最终浓缩

本文最值得学的是：把高超声速轨迹热流预测问题拆成“POD 降维 + TSCN 时空特征提取 + CST 闭环耦合”，并用精度、效率、消融和预测区间共同支撑工程可用性。

最大风险是：训练轨迹覆盖和局部峰值误差可能限制真实任务外推，图表与表格细节需要 PDF 图像复核。

可迁移的三件事：一是用现有方法分类制造 gap；二是用流程图说明代理模型替代位置；三是用“平均误差 + 关键点误差 + 消融 + 效率提升”组成完整证据链。
