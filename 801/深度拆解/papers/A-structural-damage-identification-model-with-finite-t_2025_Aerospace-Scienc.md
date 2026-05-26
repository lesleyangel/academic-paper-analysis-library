# A structural damage identification model with finite thermomechanical sensors of the re-entry module

## 0. 读取说明

本拆解基于 `801/文本/txt/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.txt` 和 metadata。文本能确认摘要、章节、流程、核心公式、表格数值和结论；但 re-entry module 结构图、热流/压力云图、温度/应力场、数据库扩展散点、训练曲线、误差直方图和残余能力云图均需 PDF 图像复核。该文抽取文本存在双栏交错，表格位置部分错位，数值以可读上下文中明确出现者为准。

## 1. 基本信息与论文身份

- 题名：A structural damage identification model with finite thermomechanical sensors of the re-entry module
- 作者：Xiao-Bing Ma, Rui Guo, Hua Su, Chun-Lin Gong, Jian-Jun Gou
- 期刊与年份：Aerospace Science and Technology, 161, 2025, 110150
- DOI：10.1016/j.ast.2025.110150
- 领域：再入舱结构健康监测、有限热-力传感器、损伤识别、Kriging 数据扩展、BPNN
- 类型：数据驱动方法 + 数值数据库 + 结构损伤评价模型
- 研究对象：参考 Orion 构型的 re-entry module，关注热防护壳/结构区域在 20-80 km 再入段的损伤状态。
- 方法组合：气动压力/热流计算、热-力耦合有限元、基于应变等效刚度折减的分区损伤模型、Kriging 数据扩展、BPNN 损伤识别、结构强度因子和损伤等级判定。

这篇论文的身份是“面向再入舱实时安全评估的数字模型 + 机器学习识别框架”。它不是单纯神经网络论文，而是把损伤数据库构造、扩增、识别和等级决策连成一条工程流程。

## 2. 摘要与核心信息提取

摘要分三步讲贡献：首先用热-力数值模拟和基于应变等效刚度折减的结构损伤模型建立原始损伤数据库；其次用 Kriging 代理模型把数据库扩展 10 倍且误差约 7%；第三以有限节点温度和应力为输入、结构损伤值为输出训练 BPNN，并构造损伤等级评价方程。

一句话主张：作者提出一种结合热-力仿真、Kriging 数据扩展和 BPNN 的再入舱结构损伤识别方法，可用有限温度/应力传感器估计分区残余能力并支持实时安全评估。

核心结果：

- 数据库扩展 10 倍，最大偏差约 7%。
- 数据扩展后，测试集识别误差降为未扩展数据的 40%，即约降低 60%。
- BPNN 训练 loss 约 0.0000926，整体平均误差约 0.0062。
- error threshold = 0.03 时整体识别准确率约 92.59%/92.6%，各区域准确率约 98%。
- 1% 随机传感器噪声下仍表现出较好抗干扰能力。

## 3. 选题层深拆

选题来自 reusable/re-entry module 的安全评估需求。再入舱在严酷气动加热和减速过载下可能出现结构损伤、性能退化甚至失效；如果能实时识别损伤状态，就可以调整任务策略、控制策略或再入轨迹，并降低复用维护成本。

作者把大问题收束为一个可训练的监督学习问题：给定有限节点温度、应力和飞行状态，预测若干结构分区的损伤/残余能力值，再用结构强度因子合成为整体损伤等级。

选题价值强在工程闭环：不是只定位裂纹，而是服务“剩余结构能力”和“是否能安全返回/复用”的决策。它也解决机器学习在结构损伤识别中的关键痛点：真实损伤数据不足，仿真数据昂贵，训练样本不足会过拟合。

## 4. 领域位置与文献版图

Introduction 的文献版图按 SDI 技术路线组织：

- 动态响应监测：基于模态、频率、波形等，能监控整体结构，但受环境干扰、高阶模态获取困难、多损伤识别效果有限。
- 静态响应监测：基于应力/应变等静态响应，计算成本低、物理意义强，但已有工作多关注局部或简单结构，缺少通用高效流程。
- 机器学习/深度学习：CNN、LSTM、Transformer、PINN、U-Net 等在图像、信号和结构损伤识别中有进展，但复杂结构、复杂变载和数据不足仍是问题。
- 代理模型/数据扩增：Kriging 等可降低仿真成本，支持大样本训练。

本文站位是“复杂再入舱 + 有限热力传感器 + 数据扩展 + BPNN 识别 + 损伤等级”。它和单纯视觉损伤识别不同，强调内部损伤/整体残余能力。

## 5. Gap 制造机制

作者制造 gap 的核心是“已有方法要么简单结构验证，要么缺足够数据，要么不能评价整体能力”。

具体 gap：

- 场景 gap：许多 ML-SHM 方法只在板、壳、翼等简单模型验证，复杂再入舱复杂热-力载荷下效果未知。
- 数据 gap：损伤数据通常只能通过数值仿真获得，成本高，样本不足导致 BPNN 过拟合。
- 决策 gap：许多损伤识别只关注位置/程度，不能直接给出整体残余结构能力和损伤等级。
- 传感器 gap：实际应用只能布置有限温度/应力节点，不能依赖全场数据。

gap 可信且工程导向强。风险是论文仍主要依赖数值仿真和代理扩展数据，真实损伤试验/飞行数据缺失，使“实时安全评估”仍是潜力而非已验证工程能力。

## 6. 创新性判断

作者声明的创新包括：分区刚度损失损伤模型、Kriging 数据库扩展、BPNN 损伤识别、结构损伤等级评价。

真实创新判断：

- 系统集成创新：较强。把数据库、扩展、识别和等级评价连成闭环。
- 方法创新：中等。Kriging 和 BPNN 成熟，创新在针对再入舱热-力传感器和分区残余能力的组合。
- 工程应用创新：较强。面向 re-entry module 复杂热-力环境。
- 理论创新：中等偏弱。刚度折减、Kriging、BPNN、F-test 都是已有工具，主要是工程适配。

最可信的创新是“数据扩展抑制过拟合”的证据；最容易被挑战的是“损伤等效为分区整体刚度折减”的简化，会牺牲裂纹类型和精确位置识别。

## 7. 论证链条复原

论证链条：

再入舱热-力环境严酷，损伤识别对安全和复用重要 -> 现有 SDI 方法在复杂结构、有限传感器和数据不足方面存在缺口 -> 建立再入舱数字模型和分区损伤模型 -> 在 20-80 km 再入段计算气动压力/热流并做热-力耦合仿真，形成原始损伤数据库 -> 用 Kriging 代理模型扩展数据库以降低仿真成本和缓解样本不足 -> 用 BPNN 从有限温度/应力传感器预测各分区残余能力 -> 用结构强度因子合成整体能力和损伤等级 -> 用训练/测试误差、置信区间、噪声干扰证明方法可行。

闭合度较高。最强环节是数据扩展前后对比，直接回应过拟合 gap。薄弱环节是仿真数据库到真实传感器应用之间的域差异。

## 8. 方法/理论/模型细拆

方法流程：

1. Re-entry module 建模：参考 Orion，建立结构 CAD 与返回轨迹。
2. 气动计算：在 20-80 km 关键再入段计算气动压力和热流，生成飞行工况。
3. 热-力耦合有限元：先热传导，后静力分析，得到温度和应力响应。
4. 分区损伤模型：按结构划分区域，用应变等效刚度折减表示损伤变量。
5. Kriging 数据扩展：为每个传感器建立代理模型，将随机/拉丁超立方生成的损伤数据映射为传感器响应，扩展数据库。
6. BPNN 损伤识别：输入传感器数据和飞行状态，输出各区域损伤值/残余能力。
7. 结构强度因子与损伤等级：按区域重要性权重计算整体结构能力 Cs，并据此分类。
8. 抗干扰验证：向传感器数据加入随机噪声，比较不同误差阈值下识别准确率。

关键假设：

- 某区域内所有损伤等效为该区域整体刚度降低。
- 代理扩展数据能代表真实仿真数据分布。
- 温度和应力有限节点足以反映分区损伤。
- 噪声以随机扰动表示。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 分区刚度损失模型可构造再入舱损伤数据库 | 2、3、结论 | 结构分区规则、热-力仿真，覆盖 20-80 km 再入段 | 中 | 损伤类型被等效为刚度折减，缺真实损伤校准 |
| Kriging 可低成本扩展数据库 | 摘要、3.3、6.2、结论 | 数据库扩展 10 倍，最大偏差约 7%；Fig. 10 原始/扩展数据趋势 | 强 | 扩展数据仍来自代理，不等于真实新仿真/实验 |
| 数据扩展能抑制 BPNN 过拟合 | 摘要、6.2、Fig. 11 | 未扩展训练出现严重过拟合；扩展后测试集识别误差为原始 40% | 强 | 对比基于 200 -> 2000 的子集实验，需更多随机种子复核 |
| BPNN 能高精度识别损伤值 | 6.3、Table 10/Table 11 | training loss 0.0000926，ravg_ov 0.0062；threshold 0.03 下整体准确率 92.59% | 强 | 数据均为仿真/扩展数据，真实域差未验证 |
| 模型具有抗噪声能力 | 6.4、Table 18-20、结论 | 1% 随机噪声下 threshold 0.03 总体准确率约 86.83%，区域准确率仍较高；误差变化有限 | 中 | 噪声模型简单，传感器失效/漂移未覆盖 |
| 损伤等级可服务任务决策 | 5、Table 17、结论 | 用结构强度因子计算样本整体残余能力 54.36%/71.06%/63.41%，对应 Level 4/Level 2/Level 4 | 中 | 等级阈值和工程决策规则需外部验证 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：本文方法流程图，承担总框架功能。
- Fig. 2：返回轨迹，说明热-力环境来源。
- Fig. 3-Fig. 4：再入舱结构和热防护壳网格，支撑几何/有限元建模。
- Table 1-Table 2：计算工况与典型飞行环境参数，为气动计算和热-力分析提供输入。
- Fig. 5：气动压力与热流，支撑环境载荷真实性；需要 PDF 图像复核。
- Table 3-Table 5：材料热/力物性，支撑热-力耦合模型。
- Fig. 7：数据扩展流程，解释 Kriging 如何扩展数据库。
- Fig. 8/Table 6：损伤识别模型构建和 BPNN 结构。
- Table 7：损伤等级分类，支撑工程决策输出。
- Fig. 9：典型工况温度和应力场，是传感器输入来源；需要 PDF 图像复核。
- Table 8：Kriging 拟合误差，支撑代理扩展可信度。
- Fig. 10-Fig. 11：原始/扩展数据与有无扩展训练效果，是数据 gap 的关键证据。
- Fig. 12-Fig. 13/Table 10-11：训练过程、误差分布和准确率，是模型性能核心证据。
- Fig. 14/Table 13-17：三种样本残余能力、置信区间和损伤等级，展示决策输出。
- Table 18-20：随机噪声下误差和准确率，支撑抗干扰。
- 公式：气动换热、热传导、静力平衡、Kriging 预测、BPNN 映射、MSE loss、结构能力 Cs 和 F-test 置信区间。公式链条从“环境载荷”一路到“损伤等级”。

## 11. 章节结构与篇章布局

真实章节：1 Introduction -> 2 Re-entry module and structural damage model -> 3 Damage database and its expansion method -> 4 Damage identification model based on BPNN -> 5 Structural strength factor and definition of damage grade -> 6 Results and discussions -> 7 Conclusions。

结构非常工程流程化：先定义对象和损伤模型，再构建数据库，再构建识别模型，再定义等级，最后验证。这比把 BPNN 直接放在方法开头更好，因为读者先理解数据和标签如何产生。

标题命名偏流程型和对象型。第 3 节标题 `Damage database and its expansion method` 是最关键标题，直接暴露本文要解决机器学习数据不足问题。第 5 节把损伤识别连接到等级判定，是工程化亮点。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：4
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Re-entry module and structural damage model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Data expansion methodTable 5 | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Damage identification model based on BPNN | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5 Structural strength factor and definition of damage grade          the features of each sensor data, the data were normalized before data | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 先用 Columbia disaster 和 reusable vehicle 安全需求制造现实压力，再分类综述动态/静态/ML 损伤识别，最后指出复杂结构和数据不足。段落节奏是“事故/需求 -> 方法谱系 -> 数据瓶颈 -> 本文流程”。

方法段落按数据生产链推进：轨迹、气动、热传导、静力、损伤、扩展、BPNN、等级。结果段按验证问题推进：数据库是否够、扩展是否有效、BPNN 是否收敛、不同工况是否稳定、噪声是否影响。

可学习之处：机器学习论文没有把网络结构当成唯一主角，而是把“标签定义”和“数据扩增”作为核心章节，这对工程 ML 论文很重要。

## 13. 文笔画像与语言习惯

整体语气是工程安全和方法集成型。常用 `developed`, `established`, `proposed`, `expanded`, `identified`, `accuracy`, `residual capability`, `anti-interference`。claim 较强，但数值紧跟其后。

主动/被动：贡献句多用主动 `This work developed...`；仿真和训练多用被动 `was established`, `was expanded`, `was trained`。时态上，已有研究用过去时和现在完成时，方法定义用现在时，结果用一般现在时。

高频词集中于 `damage`, `identification`, `structural`, `module`, `sensor`, `database`, `accuracy`, `error`, `network`, `residual capability`。这些高频词高度对应论文贡献。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：damage(192)；model(126)；data(113)；identification(105)；structural(96)；error(80)；module(69)；re-entry(68)；method(68)；based(64)；area(59)；sensor(47)；training(44)；heat(44)；database(41)；accuracy(41)；structure(37)；temperature(34)；technology(33)；network(33)
- 高频学术名词：model(126)；identification(105)；structure(74)；method(68)；analysis(50)；simulation(42)；temperature(34)；function(29)；confidence(28)；material(27)；element(25)；calculation(23)；science(21)；capacity(21)；stress(20)；conditions(18)
- 高频学术动词：shown(27)；shows(13)；proposed(9)；predicted(8)；evaluate(5)；indicates(5)；developed(4)；simulate(3)；demonstrated(3)；compared(2)；show(2)；predict(2)；validated(2)；revealed(2)；estimate(2)；estimated(1)
- 高频形容词：structural(96)；aerodynamic(29)；neural(29)；elastic(28)；material(27)；element(25)；residual(23)；numerical(22)；thermal(22)；finite(21)；boundary(18)；static(16)；significant(16)；substantial(16)；interval(15)；experimental(14)
- 高频副词/连接副词：finally(15)；therefore(12)；respectively(12)；consequently(10)；however(8)；effectively(8)；fully(5)；significantly(4)；approximately(4)；extremely(4)；randomly(4)；furthermore(3)；mainly(3)；dynamically(3)；relatively(3)；typically(3)
- 高频二词短语：re-entry module(53)；damage identification(42)；structural damage(28)；identification error(23)；aerospace science(21)；science technology(21)；neural network(19)；sensor data(16)；finite element(16)；damage database(14)；identification accuracy(13)；residual capacity(13)；damage data(13)；identification model(11)；data expansion(11)；surrogate model(11)
- 高频三词短语：aerospace science technology(21)；damage identification model(11)；structural damage identification(8)；finite element model(8)；heat-force coupling analysis(7)；convective heat transfer(7)；area area area(7)；structural health monitoring(6)；kriging surrogate model(6)；model re-entry module(5)；sensor sensor area(5)；aerosp sci technol(5)

**主动、被动与句法**

- 被动语态估计次数：217
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：1193
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：276
- 一般过去时线索：110
- 现在完成时线索：11
- 情态动词线索：97
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：damage(126)；model(73)；data(73)；structural(68)；re-entry(57)；module(57)；method(51)；based(42)
- 5. Structural strength factor and definition of damage grade          the features of each sensor data, the data were normalized before data：identification(66)；damage(65)；error(56)；model(53)；data(37)；area(33)；structural(27)；accuracy(27)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

背景句：

- `The re-entry environment ... is extremely harsh...`
- 模仿：X 在极端 Y 环境下服役，其损伤状态识别对安全和复用评估至关重要。

Gap 句：

- `Insufficient training samples will lead to serious overfitting...`
- 模仿：由于高保真损伤数据获取成本高，训练样本不足会导致模型过拟合并削弱泛化能力。

方法句：

- `This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings...`
- 模仿：本文构建了一个融合数值仿真、有限传感器测量和机器学习的识别框架。

结果句：

- `The model overfitting is fully suppressed and the identification error is reduced...`
- 模仿：扩展数据库显著抑制过拟合，使测试集误差降至未扩展方案的 X%。

局限句：

- `this method can only evaluate the overall stiffness capacity...`
- 模仿：该等效损伤模型能够评估区域整体残余能力，但尚不能识别细小损伤的精确位置和类型。

## 15. 引用策略与文献使用

引用策略服务三个目标：

1. 现实重要性：再入舱热-力环境、Columbia disaster、reusable vehicle 安全。
2. 方法版图：动态响应、静态响应、FBG、ML、CNN、LSTM、Transformer、PINN 等。
3. 数据瓶颈：深度学习需要大数据，复杂结构仿真代价高，代理模型可缓解。

作者评价前人较平衡：动态方法能监测整体，但受环境干扰；静态方法物理意义强，但通用流程不足；视觉深度学习有效，但难以理解内部微观损伤和整体能力。这些评价自然引出本文“有限热力传感器 + 数据扩展 + 残余能力”的位置。

风险：引用面很广但有些方向只点名，若目标是 SHM 顶刊，可能需要更深入比较 physics-informed SHM、domain adaptation 和 uncertainty quantification 文献。

## 16. 审稿人视角风险

- 仿真域差：训练/验证主要来自数值仿真和 Kriging 扩展，缺真实再入舱或部件试验数据。
- 损伤简化：区域内所有损伤等效为整体刚度降低，无法识别裂纹、腐蚀、烧蚀等具体类型。
- 传感器布置：有限节点选择依据、数量和位置优化不如 2025 多源重构论文充分。
- 数据扩展偏差：Kriging 扩展数据若带偏，会让 BPNN 学到代理模型偏差。
- 抗干扰简化：随机噪声不等于真实传感器失效、漂移、热迟滞和同步误差。
- 决策等级：损伤等级阈值和结构强度因子需要工程标准或专家依据。
- 表达风险：`real-time safety assessment` 是潜力表述，若缺计算时延和在线部署测试，不能写成已实现。

## 17. 可复用资产

- 选题资产：从极端服役环境和安全事故切入，强调实时损伤识别对任务决策的价值。
- Gap 资产：把 ML-SHM 的数据不足和复杂结构适用性作为核心缺口。
- 方法资产：仿真数据库 -> Kriging 扩展 -> BPNN 识别 -> 残余能力等级。
- 图表资产：流程图、轨迹图、载荷云图、数据扩展散点、训练曲线、误差直方图、损伤等级表。
- 结果资产：用 loss、平均误差、阈值准确率、置信区间和噪声鲁棒性多指标证明模型。
- 局限表达资产：主动承认只能评估区域整体刚度，不能精确定位细小损伤。

## 18. 对我写论文的启发

工程 ML 论文要把数据来源讲清楚，否则网络再复杂也没有说服力。本文最好的地方是先定义损伤模型和数据库，再训练 BPNN，使标签和输入具有物理来源。

另一个启发是机器学习结果最好落到工程决策量。这里的结构强度因子和 damage grade 把预测值转成任务可用语言，比只报 MSE 更有应用价值。

如果模仿，需要加强真实验证或 domain gap 讨论，尤其是仿真数据训练的模型如何迁移到真实传感器。

## 19. 最终浓缩

最值得学习：把再入舱损伤识别写成从热-力仿真数据库到 BPNN 残余能力等级的完整工程闭环。

最大风险：方法主要由仿真和代理扩展数据验证，真实损伤类型、传感器误差和实验验证不足。

可迁移三点：

1. 在 ML 论文中优先解释数据和标签如何物理产生。
2. 用数据扩展前后对比直接证明过拟合问题被解决。
3. 把预测结果转化为残余能力和损伤等级，连接到工程决策。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.txt` 与 `801/文本/metadata/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 Re-entry module and structural damage model （方法/模型）
- L2 p.4: 3 Damage database and its expansion method （方法/模型）
  - L3 p.4: 3.1 Aerodynamic calculation model （方法/模型）
  - L3 p.6: 3.2 Structural heat-force coupling analysis model （方法/模型）
    - L4 p.6: 3.2.1 Heat conduction analysis （对象/问题/模块）
    - L4 p.6: 3.2.2 Static analysis （对象/问题/模块）
  - L3 p.8: 3.3 Data expansion method （方法/模型）
- L2 p.10: 4 Damage identification model based on BPNN （方法/模型）
- L2 p.15: 5 Structural strength factor and definition of damage grade （对象/问题/模块）
- L2 p.15: 6 Results and discussions （结果/讨论/验证）
  - L3 p.15: 6.1 Primary construction of the damage database （对象/问题/模块）
  - L3 p.15: 6.2 Expansion of damage database （对象/问题/模块）
  - L3 p.17: 6.3 Training of the damage identification model （方法/模型）
  - L3 p.18: 6.4 Analysis of the anti-interference ability of the model （方法/模型）
- L2 p.19: 7 Conclusions （结论）
- L2 p.19: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.19: Declaration of competing interest （对象/问题/模块）
- L2 p.19: Data availability （对象/问题/模块）
- L2 p.19: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Re-entry module and structural damage model | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Damage database and its expansion method | 4 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Aerodynamic calculation model | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Structural heat-force coupling analysis model | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2.1 Heat conduction analysis | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2.2 Static analysis | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Data expansion method | 8 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Damage identification model based on BPNN | 10 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Structural strength factor and definition of damage grade | 15 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6 Results and discussions | 15 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6.1 Primary construction of the damage database | 15 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6.2 Expansion of damage database | 15 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6.3 Training of the damage identification model | 17 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6.4 Analysis of the anti-interference ability of the model | 18 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 7 Conclusions | 19 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 19 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 再入舱面临极其恶劣的气动压力和加热条件，结构损伤状态的高精度识别对于飞行和再利用性能评估至关重要。当前的技术主要基于复杂的数值模拟或分别在时间或空间维度上有限节点的间接传感器测量。这项工作开发了一种损伤识别模型，其中包括数值模拟、传感器测量和额外的机器学习，以获得模块的结构损伤状态。首先，通过热机械数值模拟建立了初级损伤数据库，并建立了基于应变当量的刚度折减方法和一定结构分区规则的结构损伤模型。其次，提出了一种基于Kriging代理模型的精度更高的数据库扩展方法，将损伤数据库扩展了10倍，误差为7%。第三，基于反向传播神经网络，建立了以有限节点温度和应力为输入，输出结构损伤值的损伤识别模型，最终建立了结构损伤等级评估方程。
> 
> 结果表明，该模型充分抑制了过拟合，识别误差较未扩展的原始数据降低了60%，识别精度高达92.6%，误差阈值为0.03，并且具有良好的抗1%传感器噪声干扰的能力。该模型具有较高的结构剩余能力识别效率和准确性，为再入舱实时安全评估带来了潜力。监控结构状况并实时进行损伤检测、定位和评估。通过应用结构损伤识别，可以实时监测返回舱的结构损伤状态。然后根据损伤状况评估结构的能力。最后，根据结构状况，动态调整任务策略和再入轨迹，最大程度保证安全。这种技术为显着降低维护成本并提高未来可重复使用车辆的安全性提供了可能性[4]。因此，这对于智能飞行器的未来发展至关重要。通过将结构损伤识别应用于载人航天器，再入舱可以监测航天器的结构状态。
> 
> 基于实时的结构能力，飞行器可以动态调整其任务策略、控制策略[5]或再入轨迹，以确保航天器安全返回，提高载人航天任务的安全性[6]。

### 20.5 结论完整摘录（本地证据）

结论章节识别：7 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-structural-damage-identification-model-with-finite-t_2025_Aerospace-Scienc.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项研究中，为再入舱开发了损伤识别模型。该模型结合了数值模拟、传感器测量和机器学习算法。通过热机械数值模拟和基于应变当量的刚度折减方法建立了初级损伤数据库。提出一种基于Kriging代理模型的数据库扩展方法
> 
> [7] 苟建军，贾淑珍，田海涛，胡家新，龚春林，径向力传递路径舵结构多层次变量集成优化方法，Aerosp。科学。技术。 148 (2024) 109115。 [8] S.P.钱德拉，S.V. Nimje, S. Roy，基于应变的加筋复合板结构健康监测，Mater。今天：继续。 72（2023）1631-1636。 [9] 苟建军，贾淑珍，李金星，肖爽，龚春林，考虑面板振动效应的高超声速三级压缩系统物理尺寸的确定，Aerosp.科学。技术。 140 (2023) 108431。 [10] E. Esu Obukho、Wang Ying、K. Chryssanthopoulos Marios，用于轴对称管状结构损伤识别的局部振动模式对，J. Sound。振动。 494 (2020) 115845. [11] 彭晨，贝晨，叶片尺寸对风电机组叶片动态特性损伤识别的影响，非线性工程。 494 (2020) 115845. 12 (2023) 20220261。 [12] M. Masoumi，M.R.
> 
> Ashory，使用连续和平稳小波变换从均匀负载表面进行损伤识别，拉丁美洲。 J.固体结构。 11（5）（2014）738-754。 [13] M. Motlagh、A. Bahar、O. Bahar，通过使用广泛的多级 2D 小波分解和热图（包括土壤结构相互作用）进行 3D 风力涡轮机塔架损伤检测，Structures 31 (2021) 842–861。 [14] C.A.艾哈迈德，Y.O. Fatih, K. Volkan，用于损伤检测的多个裂纹悬臂梁的自动模型更新，J. Constr。钢。资源。 138（2017）499-512。 [15] M. Gunaydin、S. Adanur、A.C. Altunisik 等人，监测受损和改造 RC 建筑变化的动态特性，Exp。技术。 46（3）（2022）457-484。 [16] R.Z.崔泽峰王志刚宋，基于模糊C均值和频率响应函数曲率法的旋转叶片损伤识别，Int。 J.航空航天工程。 (2023) 011397。 [17] Timothy Sands，灵活空间机器人的鞭打补偿的优化出处，航空航天 6 (9) (2019) 93。 [18] N. Cholevas, K.N. Anyfantis, G. Mussbach 等人，通过 Neyman-Pearson 检测理论识别固体火箭发动机中的裂纹，AIAA J. 61 (5) (2023) 2241–2254。 [19] P. Hajela，F.J. Soeiro，基于静态和模态分析的结构损伤检测，AIAA J. 6 (28) (1990) 1110–1115。
> 
> [20] Dimitrios P Milanoski、Loutas 等人，基于应变的健康指标，用于加强复合材料板的结构健康监测，J. Intell。马特。系统。结构。 32（3）（2021）255-266。 [21] S.P.钱德拉，S.V. Nimje, S. Roy，基于应变的加筋复合板结构健康监测，今日材料：Proc。 72（2023）1631-1636。 [22] Young-Jin Cha、Rahmat Ali、John Lewis 等人，基于深度学习的结构健康监测，Autom。构造。 161 (2024) 105328。 [23] A. Sofi、J. Regita、B. Rane 等人，使用无线智能传感器网络进行结构健康监测 - 概述，Mech。系统。信号。过程。 163 (2022) 108113。 [24] L. Mainini, K. Willcox，支持实时结构评估和决策的代理建模方法，见：Aiaa 多学科设计优化会议，2014 年。 [25] Y.M. YE、Q. Yang、F. Yang 等，可重复使用航天器结构健康管理的数字孪生：案例研究，Eng。断裂机械。 234（2020）107076.X.-B。马等人。航天科技161(2025)110150
> 
> [26] Anna Arcaro、Bozhou Zhuang、Bora Gencturk 等人，使用多任务机器学习分类器对密封乏核燃料干式储存罐进行损坏检测和定位，Reliab。工程师。系统。安全 252 (2024) 110446。 [27] C. Yang, L. Yang, W.
> 
> 郭等人，基于深度学习的地铁枕梁应变场结构损伤识别，亚历山大工程公司。 J.81（2023）264-283。 [28] 硕士巴科达里，D.J.阿玛加尼，P.G. Asteris，使用集成深度卷积神经网络模型进行结构损伤识别，计算机模型。工程师。科学。 134（2）（2023）835–855。 [29] X.J.关子佳Wan 等人，利用上下文编码器神经网络对飞机发动机进行智能损伤检测，J. Aerospace Inf。系统。 18（11）（2021）803-812。 [30] Singh Abhaya Pal、Romanov Dmytro、Misimi Ekrem、Mason Alex，基于视觉机器人应用的基于曲线拟合的变形跟踪，Int。 J.机械。工程师。机器人。资源。 13（2）（2024）190-195。 [31] Q. Tang，J. Zhou，J. Xin，等，使用卷积神经网络的基于自回归模型的结构损伤识别和定位，KSCE J. Civil Eng。 24（7）（2020）2173–2185。 [32] 张文超，苏晨辉，张艳玲等，基于兰姆波和一维CNN的蜂窝夹层结构损伤识别，Mater.今天通讯。 40（2024）109717。 [33]尚成，孙，J.X.刘，等，基于深度学习的航空发动机叶片原位损伤检测内窥镜图像处理，Aerosp。科学。技术。 (2022) 107473。 [34] P. Iannelli, F. Angeletti, P.
> 
> Gasbarri 等人，基于深度学习的大型空间天线损伤检测结构健康监测，Acta Astronaut。 193（2022）635–643。 [35] 陆永辉，唐立群，刘泽佳等，基于 BiLSTM 网络和概率分布模型的无监督定量结构损伤识别方法，J. Sound。振动。 590 (2024) 118597。 [36] Xingxian Bao，Jianghao Li，Meng Liu 等，利用变压器神经网络和变分模态分解进行热塑性复合管的损伤识别，海洋工程。 311 (2024) 118852。 [37] Houwald Benedict von、A. Ali Sarhadi、Eitzinger Christian 等人，通过残余 U 网从热图像逐层重建复合材料中的疲劳损伤，Compos。科学。技术。 255 (2024) 110712。 [38] Timothy Sands，确定性人工智能，IntechOpen，2020。 [39] Timothy Sands，无人水下航行器 (UUV) 确定性人工智能的开发，J. Mar. Sci。工程师。 8 (8) (2020) 578。 [40] Wilt Evan, Timothy Sands，使用确定性人工智能的微卫星不确定性控制，传感器 22 (22) (2022) 8723。 [41] C. Wang, L. Yang, W.Guo, et al.，基于深度学习的地铁枕梁应变场结构损伤识别，Alexandria Eng。 J.81（2023）264-283。 [42] Y.Q.王，K.里什蒂莫西，H.
> 
> Koo Joseph，酚醛浸渍碳烧蚀剂的一维有限元炭化烧蚀材料响应模型的评估，Aerosp。科学。技术。 91（2019）301-309。 [43] S.B.史斌雷, M.Y. LI 等人，硅橡胶热防护涂层复合材料的热分解行为：实验和建模，Prog。组织。外套。 143（2020）105609。[44]洛帕文，H.B. Nielsen, Jscob S.，“DACE MATLAB 克里金工具箱”，2002 年。

### 20.7 论文逻辑脉络复核

- 提出的问题：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
- 旧方法/已有研究不足：需结合 Introduction 的文献转折句复核。
- 本文解决方式：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module. First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules. Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
- 学术/工程增量：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4]. Based on the real-time structural ca pacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the space craft and improve the safety of manned space missions [6]. The following conclusions were obtained: (1) It is demonstrated that the zonal stiffness loss model can be uti lized to construct the damage model of the re-entry module.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：89
- Introduction 引用簇数量（估计）：40
- References 条目数（解析）：46
- 可识别年份条目数：47
- 近五年/近年文献（2021+）数量：30
- 经典文献（2010年前）数量：3
- 同刊引用数量（按 subject 粗略匹配）：2
- 高频来源期刊（粗略）：Aerospace Science and Technology(2)
- 引用簇样例：[1], [2], [4], [5], [6], [3], [23], [24], [25], [26], [27], [28]

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- 7. Conclusions
In this study, a damage identification model was developed for a reentry module. This model incorporated numerical simulations, sensor measurements, and machine learning algorithms. The primary damage database is established by thermomechanical numerical simulations and the strain-equivalent-based stiffness reduction method. A database expansion method based on the Kriging agent model is proposed to
X.-B. Ma et al. Aerospace Science and Technology 161 (2025) 110150
expand the damage database, and a damage identification model with BPNN is developed. The following conclusions were obtained:
(1) It is demonstrated that the zonal stiffness loss model can be uti
lized to construct the damage model of the re-entry module. Through the implementation of numerical simulations, a damage database has been constructed within the altitude range of 20 km to 80 km, effectively characterizing the extreme conditions that the re-entry module experiences during its return. (2) The proposed database expansion method has been shown to significantly reduce the thermomechanical numerical simulation cost. The database is expanded by a factor of ten, and the expanded data can effectively simulate the distribution trend of the original simulation data with a maximum deviation of 7 %, thereby demonstrating the reliability and accuracy of the expanded data. Meanwhile, the contrast experiment of BPNN model training with and without database expansion demon strated that based on the same simulation damage data, the identification error of the model with data expansion in the test set is 40 % of the original. And the overfitting was avoided to the greatest extent with low identification error, which further re veals the effectiveness and superiority of the database expansion method. (3) The damage identification model’s training loss is reduced to 0.0000926, accompanied by a substantial decrease in the iden tification error to 0.0062, which sufficiently substantiates the convergence of the model. The model’s superior identification performance in both the training and test sets further sub stantiates its exemplary generalization capability. The model demonstrates a remarkable accuracy of 92.6 %, with an error threshold of 0.03, and exhibits notable anti-interference capa bilities, with an error rate of <1 % in the presence of random sensor noise.
CRediT authorship contribution statement
Xiao-Bing Ma: Writing – original draft, Visualization, Validation, Methodology, Data curation, Conceptualization. Rui Guo: Writing – original draft, Visualization, Validation, Methodology. Hua Su: Super vision, Methodology. Chun-Lin Gong: Writing – review & editing, Su pervision. Jian-Jun Gou: Writing – review & editing, Supervision, Funding acquisition.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
Data availability
Data will be made available on request.
References
- [1] H. Rocha, C. Semprimoschnig, P.N. Jo˜ao, Sensors for process and structural health monitoring of aerospace composites: a review, Eng. Struct. 237 (2021) 112231.
- [2] Hu Jia-Xin, Ai Li-Qiang, Liu Nan, Gou Jian-Jun, Gong Chun-Lin, Tolerance indicating models of non-thermal and thermal damages for a heat transport system, Int. J. Heat. Mass Transf. 224 (2024) 125360.
- [3] A. Rytter, M. Krawczuk, P.H. Kirkegaard, Experimental and numerical study of damaged cantilever, J. Eng. Mech. 126 (1) (2000) 60–65.
- [4] D.Y. Gao, Z.J. Wu, L. Yang, et al., Structural health monitoring for long-term aircraft storage tanks under cryogenic temperature, Aerosp. Sci. Technol. 92 (2019) 881–891.
- [5] Nakatani Scott, Timothy Sands, Simulation of spacecraft damage tolerance and adaptive controls, in: 2014 IEEE Aerospace Conference, 2014.
- [6] Nicholas Cholevas ad Konstantinos, N. Anyfantis, Crack identification in solid rocket motors through the Neyman-Peason detection theory, AIAA J. 5 (2023) 61.
- [7] Gou Jian-Jun, Jia Shu-Zhen, Tian Hai-Tao, Hu Jia-Xin, Gong Chun-Lin, An integrated optimization method of multi-hierarchy variables for rudder structures with radial force transfer paths, Aerosp. Sci. Technol. 148 (2024) 109115.
- [8] S.P. Chandra, S.V. Nimje, S. Roy, Strain based structural health monitoring of stiffened composite plate, Mater. Today: Proceed. 72 (2023) 1631–1636.
- [9] Gou Jian-Jun, Jia Shu-Zhen, Li Jin-Xing, Xiao Shuang, Gong Chun-Lin, The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects, Aerosp. Sci. Technol. 140 (2023) 108431.
- [10] E. Esu Obukho, Wang Ying, K. Chryssanthopoulos Marios, Local vibration mode pairs for damage identification in axisymmetric tubular structures, J. Sound. Vib. 494 (2020) 115845.
- [11] C. Peng, C. Bei, Influence of the blade size on the dynamic characteristic damage identification of wind turbine blades, Nonlinear Eng. 12 (2023) 20220261.

### 20.9 常用词、词类、语态与时态

- 高频词：damage(171)；data(112)；identification(91)；structural(80)；error(80)；module(68)；re-entry(67)；area(59)；sensor(45)；training(44)；heat(41)；accuracy(40)；database(39)；structure(36)；fig(34)；table(34)；temperature(33)；technology(32)；network(31)；process(30)
- 高频名词化/学术名词：identification(91)；structure(36)；temperature(33)；function(28)；confidence(28)；element(24)；expansion(23)；calculation(23)；capacity(21)；science(20)；simulation(20)；ability(17)；stiffness(16)；distribution(15)；performance(13)
- 高频学术动词：predicted(8)；developed(3)；demonstrated(3)；presented(3)；optimize(3)；compared(2)；indicated(2)；predict(2)；estimate(2)；revealed(2)；validated(2)；indicate(1)；estimated(1)；demonstrate(1)
- 高频形容词：structural(80)；table(34)；aerodynamic(29)；material(26)；neural(25)；element(24)；residual(22)；thermal(18)；boundary(18)；interval(15)；elastic(14)；coefficient(12)；real(11)；internal(9)；signal(9)
- 高频副词：finally(15)；respectively(12)；effectively(8)；fully(5)；consequently(5)；extremely(4)；only(4)；randomly(4)；mainly(3)；dynamically(3)；relatively(3)；typically(3)；significantly(2)；timely(2)；apply(2)
- 高频二词短语：re-entry module(53)；damage identification(33)；structural damage(23)；identification error(23)；aerospace science(20)；science technology(20)；page aerospace(19)；neural network(17)；sensor data(16)；finite element(15)；damage database(13)；identification accuracy(13)
- 高频三词短语：aerospace science technology(20)；page aerospace science(19)；science technology fig(8)；convective heat transfer(7)；area area area(7)；structural damage identification(6)；sensor sensor area(5)；structure re-entry module(4)；science technology table(4)；value sensor data(4)；linear relu hidden(4)；relu hidden layer(4)
- 被动语态估计：188；`we + 动作动词` 主动句估计：0
- 一般现在时线索：277；一般过去时线索：527；现在完成时线索：4；情态动词线索：97

章节词频：

- Abstract: structural(15)；damage(14)；identification(7)；re-entry(5)；module(5)；state(4)；real-time(4)；numerical(3)
- Introduction: damage(50)；structural(42)；identification(23)；data(16)；technology(15)；re-entry(11)；module(10)；error(10)
- Conclusion: damage(8)；database(8)；identification(6)；expansion(5)；data(5)；error(5)；numerical(4)；module(3)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [3].
  可迁移模板：Structural damage identification is an essential online structural health management technology based on sensor system and evaluation algorithm [X].
#### Gap句
- 原句/结构：Although this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitive to damage, and poor effect of multi-damage identification.
  可迁移模板：Although this type of method can monitor the entire structural state, its application is limited due to the susceptibility of the structural natural frequency to environmental interference, difficulty to obtain the high-order natural frequency that is sensitive to damage, and poor effect of multi-damage identification.
- 原句/结构：However, neither study established a universal and efficient structural damage state identification process, which made it difficult to apply those methods in complex structural systems.
  可迁移模板：However, neither study established a universal and efficient structural damage state identification process, which made it difficult to apply those methods in complex structural systems.
- 原句/结构：However, these studies on damage iden tification were only verified in simple plate and shell models.
  可迁移模板：However, these studies on damage iden tification were only verified in simple plate and shell models.
#### 方法句
- 原句/结构：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module.
  可迁移模板：This work developed a damage identification model that included numerical simulations, sensor measurements, and additional machine learnings to obtain the structural damage state of the module.
- 原句/结构：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
  可迁移模板：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
- 原句/结构：Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by 10 times with 7 % error.
  可迁移模板：Second, a database expan sion method with higher accuracy based on the Kriging agent model was proposed, the damage database was expanded by Xtimes with X error.
#### 结果句
- 原句/结构：The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good antiinterference ability of 1 % sensor noise are exhibited for the model.
  可迁移模板：The result shows that the model overfitting is fully suppressed and the identification error is reduced by X compared with the original data without expansion, and great identification accuracy of X with error threshold of Xand good antiinterference ability of X sensor noise are exhibited for the model.
- 原句/结构：The model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of reentry module. monitor the structural condition and perform damage detection, local ization, and assessment in real-time.
  可迁移模板：The model holds higher recognition effi ciency and accuracy of structural residual capacity and indicates potentials for real-time safety assessment of reentry module. monitor the structural condition and perform damage detection, local ization, and assessment in real-time.
- 原句/结构：The result shows that the model overfitting is fully suppressed and the identification error is reduced by 60 % compared with the original data without expansion, and great identification accuracy of 92.6 % with error threshold of 0.03 and good antiinterference ability of 1 % sensor noise are exhibited for the model.
  可迁移模板：The result shows that the model overfitting is fully suppressed and the identification error is reduced by X compared with the original data without expansion, and great identification accuracy of X with error threshold of Xand good antiinterference ability of X sensor noise are exhibited for the model.
#### 贡献句
- 原句/结构：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
  可迁移模板：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
- 原句/结构：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
  可迁移模板：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [X].
- 原句/结构：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
  可迁移模板：First, the primary damage database was established by thermo mechanical numerical simulations and a structural damage model, which was proposed based on the strainequivalent-based stiffness reduction method with certain structural partition rules.
#### 限制/边界句
- 原句/结构：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [4].
  可迁移模板：Such technology provides the possibility to significantly reduce the maintenance costs and improve the security for future reusable vehicles [X].
- 原句/结构：Therefore, it’s crucial for the future development of intelligent aircraft.
  可迁移模板：Therefore, it’s crucial for the future development of intelligent aircraft.
- 原句/结构：Based on the real-time structural ca pacity, the aircraft could dynamically adjust its mission strategy, control strategy [5] or re-entry trajectory to ensure a safe return of the space craft and improve the safety of manned space missions [6].
  可迁移模板：Based on the real-time structural ca pacity, the aircraft could dynamically adjust its mission strategy, control strategy [X] or re-entry trajectory to ensure a safe return of the space craft and improve the safety of manned space missions [X].

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
