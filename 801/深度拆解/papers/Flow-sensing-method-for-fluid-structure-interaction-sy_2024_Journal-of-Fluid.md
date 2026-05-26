# Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition

## 0. 读取说明

- 文本来源：`801/文本/txt/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.txt`，PyMuPDF 抽取，34 页。
- 本文图非常多，包含模式、误差区域、流线、等值线、瞬态算例等；图像空间细节全部需要 PDF 图像复核。
- 这篇的重点是“用结构变形实时感知/预测复杂 FSI 流场”，核心技术是结构 POD + 流场 multilayer POD + DNN 系数映射。

## 1. 基本信息与论文身份

- 题名：Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition。
- 作者：Xuyi Jia, Chunlin Gong, Wen Ji, Chunna Li。
- 期刊：Journal of Fluids and Structures，124，2024，104023。
- 领域：流固耦合、流场感知、降阶模型、POD、多层 POD、深度神经网络、柔性丝/仿生传感。
- 论文类型：方法论文 + 数值算例验证。
- 研究对象：两个 FSI 系统：圆柱后夹持柔性丝绕流；二维多柔性丝阵列绕流。
- 方法组合：LBM 流体求解、FEM 结构求解、IBM 流固耦合、结构 POD、流场 multilayer POD、DNN 映射结构模态系数到流体模态系数。
- 目标输出：用结构变形实时 forecast 流场速度、压力、涡量等属性。

## 2. 摘要与核心信息提取

本文核心主张是：传统 POD 对复杂 FSI 流场的全域建模会在涡结构和柔性结构附近产生较大误差；通过 multilayer POD 逐层识别高误差区域并对残差流场再建模，再用 DNN 从结构模态系数预测各层流体模态系数，可以在复杂、多柔性结构和瞬态流入条件下实现稳定的流场感知。

摘要的逻辑是：FSI 多柔性结构带来复杂非定常流和大量传感器；结构变形可作为流场感知输入；POD 降维结构，multilayer POD 提升复杂局部流场建模精度，DNN 建立结构-流体系数映射；两个算例和恒定/瞬态来流验证空间-时间性能。

## 3. 选题层深拆

选题源于仿生流场感知和工程监测需求：很多系统无法直接获得全流场，只能通过结构/少量传感器测量推断流动。FSI 系统中结构运动和流场相互耦合，因此结构变形包含流场信息。但复杂 FSI 系统的流场高维、局部涡结构强、传感维度多，直接黑箱建模网络大且可解释性差。

作者把问题收束为：如何用灰箱模型减少数据维度，同时不牺牲局部复杂流场的精度。multilayer POD 的切入点很具体：第一层 POD 建模全域主模态，误差大的局部区域再用残差 POD 建模，直到误差满足阈值。

## 4. 领域位置与文献版图

Introduction 的文献组织很清晰：

- 流场感知的生物启发和工程应用：鱼侧线、柔性纤毛、压力重构、传感器优化。
- 流场建模三类方法：white-box 高保真但慢；black-box 快但网络复杂、解释性弱；gray-box ROM 兼顾降维和可解释。
- 稳态流/静结构非定常流已有 POD、DMD、LSTM、CNN 等研究。
- 移动结构/FSI 流场更复杂，已有研究多集中简单系统或局部气动力/压力，复杂多柔性结构全流场实时感知不足。

本文站在 gray-box 路线内：不是放弃 DNN，而是让 DNN 只学习低维模态系数映射，把复杂空间结构交给 POD/multilayer POD。

## 5. Gap 制造机制

gap 是由复杂 FSI 的局部非线性和高维数据共同制造：

1. black-box 直接从结构到全流场，维度高、网络大、解释性弱。
2. conventional POD 对全域建模，能抓主相干结构，但对柔性结构附近、尾迹和强涡局部误差大。
3. 现有 FSI flow sensing 多在简单系统上验证，对多柔性结构和 transient inflow 条件研究不足。

作者的 gap 有方法针对性：不是说 POD 不好，而是说单层全域 POD 不关心复杂局部区域，因此需要 residual/local multilayer strategy。

## 6. 创新性判断

- 创新类型：降阶建模策略 + FSI 应用验证。
- 真正创新：把 multilayer POD 用作流场局部残差建模，并与结构 POD 和 DNN 系数映射组合成完整 flow sensing pipeline。
- 创新强度：中等偏强。POD/DNN/FSI 都不是新概念，但“误差阈值驱动的多层局部 POD”在复杂 FSI 流场感知中有清晰价值。
- 可信度：两个算例、恒定与瞬态条件、多物理量展示较充分；但结果完全基于数值仿真，缺少实验传感噪声和真实测量验证。

## 7. 论证链条复原

背景：流场感知需要从结构/传感器测量恢复流场。

已有方法：黑箱可预测但维度大，灰箱 ROM 可解释但传统 POD 局部误差大。

方法：用结构 POD 得结构模态系数 as；用 multilayer POD 对流场逐层建模，第一层全域、后续层在误差超过阈值的局部区域建残差；用 DNN 学习 as -> af；预测时由结构快照得到 as，再预测各层流体系数并融合重构流场。

验证：在 case A 单柔性丝和 case B 51 根柔性丝阵列中，分别考察恒定来流和随机瞬态来流；对速度、压力、流线、RMSE 和层数影响进行比较。

结论：多层 POD 每增加一层流场重构误差近似降低一个数量级，预测误差不随时间累积，复杂涡结构区域也能保持较好空间预测。

## 8. 方法/理论/模型细拆

结构 POD：对结构变形快照 Ds 建模，获得结构模态 ξs 和系数 as；以最大重构误差 Es≤1.0×10^-3D 作为结构精度条件。Case A 选 10 个结构模态，前 4 个模态能量 99.96%。

流体 multilayer POD：第一层对全流场 Df 建 POD；计算平均重构误差 E1f；选取 E1f>σ 的网格区域作为下一层建模区域；下一层对残差流 D2f 建 POD；重复直到无超阈值区域。最终 Df 由各层流场逐元素相加重构。

DNN：输入结构 POD 系数，输出所有流体 multilayer POD 系数。DNN 只处理低维系数，空间复杂性由 POD 模式承载。

数值 FSI：流体用 LBM，结构用 FEM，耦合用 IBM。Case A 计算域 4.1D×25D，D=0.10 m；Case B 计算域 3h×90h，51 根柔性丝，间距 h。网格 Δs=0.02l，每根丝 20 个 FEM 单元。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 结构 POD 能高精度表达结构变形 | 4.2.1 | Case A 前 4 模态能量 99.96%；10 模态 Es=8.88×10^-4D，小于阈值 | 强 | 图 8/9 需 PDF 复核 |
| multilayer POD 能定位并降低局部流场误差 | 4.2.2/4.3.2 | Case A Vx 三层：8/27/54 模态，误差区域从 100% 到 63.19% 到 2.46% 再到 0%；Case B 类似降至 0% | 强 | 阈值 σ 选择敏感性有限 |
| 多层模型效率仍可接受 | 4.3.2 | Case B 第二层数据维度减少 71.62%、建模时间减少 78.75%；第三层维度减少 98.96%、时间减少 97.91% | 强 | 仅报告 Vx 示例 |
| DNN 系数映射能预测流场 | 4.2.3/4.3.3 | 预测速度、压力和流线与数值参考总体吻合，误差集中在尾迹/柔性丝附近 | 中强 | 图像定性证据多，需要 PDF 复核 |
| 预测误差不随时间累积 | 4.2.3/结论 | 不同时刻独立预测，RMSE 呈周期/随机波动但不累积 | 强 | 真实闭环在线预测可能不同 |
| 方法可处理瞬态流入 | 4.2.4/4.3.4 | Case A 测试含 Re 72-120 区间，Case B Re 137-162；总体仍匹配，但准确性低于恒定来流 | 中强 | 作者承认只适用于一定 Reynolds 数范围 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1/2 | DNN 与 flow sensing 架构 | 方法流程完整 | 建模阶段和预测阶段分开 | 需要 PDF 图像复核 |
| Eq. (4)-(17) | 数学定义 POD/multilayer POD/DNN 映射 | 方法可复现 | 残差流场、误差阈值、层融合 | 文本足够 |
| Fig. 3/4 + Eq. (31)-(35) | FSI 数值模型 | 验证场景可信 | LBM/FEM/IBM 和 Re/K/M 定义 | 需要 PDF 图像复核 |
| Fig. 8/9 | 结构 POD | 结构降维准确 | Case A 10 模态满足误差阈值 | 需要 PDF 图像复核 |
| Fig. 11/29 + Table 2/3 | 多层 POD 参数和误差区域 | 局部残差建模有效 | 每层模式数、区域比例、平均误差、时间 | 需要 PDF 图像复核 |
| Fig. 12-18/30-36 | 恒定来流预测 | 速度/压力/流线预测可用 | 误差集中在尾迹/丝附近，层数越多越准 | 需要 PDF 图像复核 |
| Fig. 19-25/37-41 | 瞬态来流预测 | 方法有 transient 能力 | 预测整体匹配但误差更大 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Flow sensing method；2.1 POD；2.2 DNN；2.3 Flow sensing model via multilayer POD；3 Numerical simulation methods and model description；4 Test cases；4.1 physical/numerical settings；4.2 Case A；4.3 Case B；5 Conclusions。

篇章布局很工程化：先把工具链讲完，再讲 FSI 求解器，再用两个 case 做层层验证。第 4 章结构重复性强：POD for structure -> multilayer POD for fluid -> training and forecasting -> transient conditions。这种重复让读者能直接比较 case A/B。

标题命名偏功能型，不结果前置。Case B 标题“Flow past 2D flexible filament set”直接暴露复杂性，是很好的应用小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：25
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 The multilayer POD model is raised to enhance the modeling accuracy of unsteady flow with little increase of modeling data and | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 The proposed flow sensing method can handle flow sensing problems with transient flow conditions, and its suitability and spatial- | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2 Flow sensing method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Proper orthogonal decomposition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Deep neural network | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Flow sensing model via multilayer POD | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Numerical simulation methods and model description of the FSI systems | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Lattice Boltzmann method for fluid | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Finite element method for structure | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Immersed boundary method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Test cases | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Physical models and numerical settings of the FSI systems | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Case A: 2D flow past a flexible filament clamped behind a cylinder | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 是典型“方法谱系筛选”：先列 white/black/gray box，再逐渐排除 black-box 的高维缺点，保留 gray-box + DNN 的组合。方法段节奏是公式密集型：每一步定义快照矩阵、模态、系数、误差、阈值和重构。

结果段按图推进：先描述模式和误差区域，再报告训练/测试集长度，随后展示单时刻结果、流线、时间 RMSE、不同层数对比。它不是只报平均误差，而是不断指向“复杂局部区域”的改善。

## 13. 文笔画像与语言习惯

语言偏应用计算流体论文，常用 forecasted/reference/reconstruction error/modeling region/layer/modes。claim 通常用 “agree well”“stable temporal performance”“forecasting error is mainly remained in...”。

主动语态较多，尤其 “we propose/establish/define/select”。时态上方法定义用现在时，实验设置和结果描述用现在时与过去时混合。副词常用 mainly、generally、obviously、basically，强调图像观察。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：flow(215)；pod(199)；case(87)；error(78)；model(75)；modeling(73)；fluid(67)；structure(64)；velocity(62)；sensing(59)；method(55)；field(54)；region(52)；filament(52)；forecasted(50)；modes(48)；multilayer(47)；set(44)；structures(43)；structural(43)
- 高频学术名词：structure(128)；model(75)；velocity(62)；method(55)；field(54)；filament(52)；deformation(46)；structures(43)；simulation(42)；conditions(39)；results(36)；reconstruction(30)；performance(26)；pressure(25)；system(24)；condition(22)
- 高频学术动词：shown(34)；proposed(33)；shows(21)；compared(8)；predicted(6)；solved(6)；predict(4)；indicates(3)；validated(3)；validate(2)；evaluate(2)；investigated(2)；propose(2)；indicate(2)；show(1)；capture(1)
- 高频形容词：filament(52)；structural(43)；numerical(42)；transient(33)；flexible(26)；different(13)；dynamic(12)；significant(12)；temporal(12)；boundary(11)；static(10)；local(10)；real(10)；constant(9)；moment(9)；stable(8)
- 高频副词/连接副词：respectively(27)；significantly(10)；generally(10)；specifically(10)；therefore(8)；however(8)；approximately(6)；mainly(6)；gradually(6)；furthermore(5)；widely(5)；similarly(5)；consequently(4)；greatly(4)；relatively(4)；usually(3)
- 高频二词短语：flow sensing(56)；multilayer pod(41)；flow field(39)；fluids structures(34)；jia fluids(32)；pod model(30)；flow conditions(29)；transient flow(25)；test set(25)；mode coefficients(24)；structural deformation(23)；forecasting error(22)；sensing method(20)；fsi system(19)；numerical simulation(18)；reconstruction error(18)
- 高频三词短语：jia fluids structures(32)；transient flow conditions(25)；flow sensing method(19)；case transient flow(15)；proposed flow sensing(12)；multilayer pod fluid(11)；multilayer pod model(10)；flow sensing model(10)；numerical simulation results(10)；flow field structural(9)；field structural deformation(9)；test set case(9)

**主动、被动与句法**

- 被动语态估计次数：187
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：833
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：384
- 一般过去时线索：56
- 现在完成时线索：6
- 情态动词线索：62
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：flow(17)；sensing(6)；multilayer(6)；structures(5)；systems(5)；fsi(5)；model(5)；method(4)
- 1. Introduction：flow(68)；sensing(22)；methods(21)；pod(18)；unsteady(17)；method(14)；model(14)；field(13)
- 2. The multilayer POD model is raised to enhance the modeling accuracy of unsteady flow with little increase of modeling data and：time(1)；superior(1)；pod(1)
- 3. The proposed flow sensing method can handle flow sensing problems with transient flow conditions, and its suitability and spatial-：section(4)；paper(2)；model(2)；method(2)；temporal(1)；performance(1)；verified(1)；organized(1)
- 2. Flow sensing method：无明显高频项
- 2.1. Proper orthogonal decomposition：pod(9)；structure(5)；flow(4)；fluid(4)；represents(4)；standard(4)；described(3)；modeling(3)
- 2.2. Deep neural network：dnn(8)；coefficients(5)；layer(4)；output(4)；mode(4)；model(3)；input(3)；hidden(3)
- 2.3. Flow sensing model via multilayer POD：pod(53)；flow(19)；modeling(13)；fpod(12)；model(11)；fluid(11)；coefficients(10)；structural(9)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- gap 句式：The conventional POD approach typically models the entire flow field without specifically focusing on regions with variations.
- 方法句式：The region that satisfies E>σ is taken as the modeling region for the next layer.
- 结果句式：The forecasted results agree well with the numerical simulation results in general.
- 局限句式：The method is only suitable for a certain range of Reynolds numbers.
- 对比句式：With an increase in the number of layers, the forecasting error gradually decreases.
- 可复用模板：全域低阶模型捕捉主结构，局部残差模型补偿复杂区域，低维神经网络只学习模态系数映射。

## 15. 引用策略与文献使用

引用按流场感知对象和建模方法双轴组织：稳态流、静结构非定常流、移动结构/FSI；白箱、黑箱、灰箱。作者大量引用 DMD/LSTM/CNN/POD 等方法，让自己的路线看起来是综合而非孤立。

gap 前的引用策略很有效：先承认 black-box 和 gray-box 都能处理 flow sensing，再指出 black-box 高维、conventional POD 局部精度不足。这样 multilayer POD 的必要性自然出现。

## 16. 审稿人视角风险

- 数据全来自数值仿真，缺少真实传感器噪声、测量误差和实验流场验证。
- DNN 架构细节、超参数和泛化能力若不足，可能影响复现。
- transient 条件只在一定 Re 范围内有效，外推能力有限。
- multilayer POD 阈值 σ 的选择对层数、效率和精度影响很大，敏感性可进一步展开。
- 压力场在柔性丝附近存在 Gibbs/非平滑问题，说明线性 POD 对强非线性跳变仍有局限。
- Case B 多丝系统复杂，但仍是二维数值模型，三维真实 FSI 需验证。

## 17. 可复用资产

- 方法资产：POD 降维 + error-threshold local residual POD + DNN coefficient mapping。
- 图表资产：模型架构图、误差区域图、层数-时间误差图、不同层数等值线对比、恒定/瞬态来流对比。
- 论证资产：不仅展示预测好，还展示为什么单层 POD 不好、多层如何逐步修补。
- 写作资产：用两个 case 复用完全一致的小节结构，增强可比性。
- 局限表达资产：明确承认 transient forecasting 只在一定 Re 范围内适用。

## 18. 对我写论文的启发

如果提出“深度学习 + ROM”的方法，最好像本文一样把深度网络限制在低维系数空间，而不是直接预测高维场。这样既能减少网络复杂度，也能保留 ROM 的可解释性。

另外，结果展示要围绕失败区域展开。本文不断指出误差集中在尾迹、柔性丝附近、压力突变区，然后证明 multilayer POD 对这些区域有改进，这比只报全域 RMSE 更有说服力。

## 19. 最终浓缩

本文最值得学的是用误差阈值驱动的 multilayer POD 修补传统 POD 对复杂局部流场的弱点，再用 DNN 学结构-流体系数映射。最强证据是两个 FSI 算例中多层 POD 使重构误差近似逐层数量级下降，且预测误差不随时间积累。最大风险是完全数值验证、阈值敏感和瞬态 Re 范围有限，后续应加入实验噪声和三维场景验证。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.txt` 与 `801/文本/metadata/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 Flow sensing method （方法/模型）
  - L3 p.3: 2.1 Proper orthogonal decomposition （对象/问题/模块）
  - L3 p.4: 2.2 Deep neural network （对象/问题/模块）
  - L3 p.5: 2.3 Flow sensing model via multilayer POD （方法/模型）
- L2 p.6: 3 Numerical simulation methods and model description of the FSI systems （方法/模型）
  - L3 p.6: 3.1 Lattice Boltzmann method for fluid （方法/模型）
  - L3 p.8: 3.2 Finite element method for structure （方法/模型）
  - L3 p.8: 3.3 Immersed boundary method （方法/模型）
- L2 p.9: 4 Test cases （结果/讨论/验证）
  - L3 p.9: 4.1 Physical models and numerical settings of the FSI systems （方法/模型）
  - L3 p.12: 4.2 Case A: 2D flow past a flexible filament clamped behind a cylinder （结果/讨论/验证）
    - L4 p.12: 4.2.1 POD for structure （对象/问题/模块）
    - L4 p.13: 4.2.2 Multilayer POD for fluid （对象/问题/模块）
    - L4 p.19: 4.2.3 Training and forecasting （对象/问题/模块）
    - L4 p.23: 4.2.4 Case A study with transient flow conditions （结果/讨论/验证）
  - L3 p.26: 4.3 Case B: Flow past 2D flexible filament set （结果/讨论/验证）
    - L4 p.26: 4.3.1 POD for structure （对象/问题/模块）
    - L4 p.26: 4.3.2 Multilayer POD for fluid （对象/问题/模块）
    - L4 p.28: 4.3.3 Training and forecasting （对象/问题/模块）
    - L4 p.30: 4.3.4 Case B study with transient flow conditions （结果/讨论/验证）
- L2 p.30: 5 Conclusions （结论）
- L2 p.32: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.32: Declaration of Competing Interest （对象/问题/模块）
- L2 p.32: Data availability （对象/问题/模块）
- L2 p.32: Acknowledgments （对象/问题/模块）
- L2 p.32: Appendix A. Algorithms for POD （附录）
- L2 p.33: Appendix B. Validation of Grid independence （结果/讨论/验证）
- L2 p.33: Appendix C. Numerical simulation results （结果/讨论/验证）
- L2 p.33: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Flow sensing method | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Proper orthogonal decomposition | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Deep neural network | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Flow sensing model via multilayer POD | 5 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Numerical simulation methods and model description of the FSI systems | 6 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Lattice Boltzmann method for fluid | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Finite element method for structure | 8 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Immersed boundary method | 8 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Test cases | 9 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Physical models and numerical settings of the FSI systems | 9 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Case A: 2D flow past a flexible filament clamped behind a cylinder | 12 | 3 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.1 POD for structure | 12 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.2 Multilayer POD for fluid | 13 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.3 Training and forecasting | 19 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2.4 Case A study with transient flow conditions | 23 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 Case B: Flow past 2D flexible filament set | 26 | 3 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.1 POD for structure | 26 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.2 Multilayer POD for fluid | 26 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.3 Training and forecasting | 28 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.4 Case B study with transient flow conditions | 30 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 30 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 32 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of Competing Interest | 32 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 32 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 32 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix A. Algorithms for POD | 32 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix B. Validation of Grid independence | 33 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix C. Numerical simulation results | 33 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 33 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 流量传感广泛用于预测流固耦合（FSI）系统中的流场。具有多种柔性结构的FSI系统通常涉及复杂的非定常流动和大量的传感器，这使得流量传感变得困难。在本研究中，提出了一种通过多层本征正交分解（POD）的 FSI 系统流量传感方法，以利用结构变形实现流场的实时预测。首先，我们建立了结构变形的POD模型。为了提高流场模型的精度，我们提出了多层POD模型，主要关注流场结构复杂的区域的局部建模精度。然后，建立流场的多层模型。此外，采用深度神经网络模型将结构的模态系数映射到多层POD的所有模态系数。所提出的方法应用于两个 FSI 系统，包括流过夹在圆柱体后面的柔性细丝的流动和流过柔性细丝组的流动。恒定流入和瞬态流动条件均被考虑。结果表明，所提出的流量传感方法表现出优异的时空性能，流特性预测准确，适用于相干涡等复杂流结构的FSI系统。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项工作中，提出了一种通过多层 POD 进行 FSI 系统的流量传感方法。进行了两次应用来验证和评估所提出的方法。结论如下：
> 
> X.贾等人。流体与结构学报124(2024)104023
> 
> X.贾等人。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing. The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 本文解决方式：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD model of structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 学术/工程增量：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures. In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：0
- Introduction 引用簇数量（估计）：0
- References 条目数（解析）：93
- 可识别年份条目数：78
- 近五年/近年文献（2021+）数量：36
- 经典文献（2010年前）数量：4
- 同刊引用数量（按 subject 粗略匹配）：2
- 高频来源期刊（粗略）：Journal of Fluids and Structures(2)
- 引用簇样例：未识别

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- 2021. Deep learning to replace, improve, or aid CFD analysis in built environment applications: a review. Build. Environ. 206, 108315 https:// doi.org/10.1016/j.buildenv.2021.
- 108315. Castellanos, R., Cornejo Maceda, G.Y., De La Fuente, I., Noack, B.R., Ianiro, A., Discetti, S.,
- 2022. Machine-learning flow control with few sensor feedback and measurement noise. Phys. Fluids 34, 047118. https://doi.org/10.1063/5.
- 0087208. Chen, S., Doolen, G.D.,
- 1998. Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech. 30 (1), 329–364. https://doi.org/10.1146/annurev.fluid.30.1.
- 329. Connor, J.O., Revell, A.,
- 2019. Dynamic interactions of multiple wall-mounted flexible flaps. J. Fluid Mech. 870, 189–216. https://doi.org/10.1017/jfm.2019.
- 266. Dang, F., Nasreen, S., Zhang, F.,
- 2021. DMD-based background flow sensing for AUVs in flow pattern changing environments. IEEE Robot. Autom. Lett. 6 (3), 5207–5214. https://doi.org/10.1109/LRA.2021.
- 3072570. Dubois, P., Gomez, T., Planckaert, L., Perret, L.,
- 2022. Machine learning for fluid flow reconstruction from limited measurements. J. Comput. Phys. 448, 110733
https://doi.org/10.1016/j.jcp.2021.
- 110733. Fang, Z., Gong, C., Revell, A., O’Connor, J.,

### 20.9 常用词、词类、语态与时态

- 高频词：flow(203)；pod(187)；fig(100)；case(75)；error(74)；modeling(71)；fluid(66)；structure(64)；velocity(60)；sensing(56)；field(52)；region(52)；forecasted(50)；filament(47)；multilayer(45)；structural(42)；structures(41)；set(41)；modes(41)；where(36)
- 高频名词化/学术名词：structure(64)；velocity(60)；filament(47)；reconstruction(27)；performance(25)；pressure(25)；deformation(23)；prediction(18)；simulation(18)；dimension(15)；moment(9)；motion(9)；distribution(8)；proportion(8)；density(8)
- 高频学术动词：compared(8)；predicted(6)；predict(4)；validated(3)；propose(2)；indicate(2)；validate(2)；optimize(1)；developed(1)；presented(1)
- 高频形容词：filament(47)；structural(42)；journal(34)；transient(28)；flexible(24)；numerical(18)；temporal(11)；boundary(11)；real(10)；constant(9)；moment(9)；coherent(8)；table(8)；external(8)；neural(7)
- 高频副词：respectively(26)；specifically(8)；mainly(6)；only(6)；gradually(6)；widely(5)；generally(5)；similarly(5)；significantly(5)；relatively(4)；usually(3)；accurately(3)；directly(3)；especially(3)；approximately(3)
- 高频二词短语：flow sensing(53)；multilayer pod(39)；flow field(37)；journal fluids(33)；fluids structures(33)；page jia(31)；jia journal(31)；flow conditions(27)；structures fig(26)；structural deformation(23)；transient flow(23)；test set(23)
- 高频三词短语：journal fluids structures(33)；page jia journal(31)；jia journal fluids(31)；fluids structures fig(26)；transient flow conditions(23)；case transient flow(17)；multilayer pod fluid(11)；flow field structural(9)；field structural deformation(9)；test set case(9)；forecasted velocity isolines(7)；set includes snapshot(7)
- 被动语态估计：136；`we + 动作动词` 主动句估计：4
- 一般现在时线索：354；一般过去时线索：391；现在完成时线索：1；情态动词线索：55

章节词频：

- Abstract: flow(15)；fsi(5)；sensing(4)；field(4)；systems(4)；multilayer(4)；pod(4)；flexible(3)
- Introduction: flow(80)；sensing(24)；pod(20)；field(17)；unsteady(17)；modeling(13)；fsi(12)；systems(10)
- Conclusion: flow(5)；transient(3)；conditions(3)；journal(2)；fluids(2)；structures(2)；case(2)；validate(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
  可迁移模板：The METHOD system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 原句/结构：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
  可迁移模板：The METHOD system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 原句/结构：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
  可迁移模板：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., X; Zhang et al., X).
#### 方法句
- 原句/结构：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句/结构：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
- 原句/结构：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  可迁移模板：To improve model accuracy for flow field, we propose the multilayer METHOD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
#### 结果句
- 原句/结构：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句/结构：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices. https://doi.org/10.1016/j.jfluidstructs.2023.104023 Received 12 May 2023; Received in revised form 4 October 2023; Accepted 6 November 2023 Available online 24 November 2023 0889-9746/© 2023 Elsevier Ltd.
  可迁移模板：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for METHOD systems with complex flow structures such as coherent vortices. https://doi.org/X/j.jfluidstructs.XReceived XMay X; Received in revised form XOctober X; Accepted XNovember XAvailable online XNovember METHOD-X/© XElsevier Ltd.
- 原句/结构：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  可迁移模板：In this study, a flow sensing method for METHOD systems via multilayer proper orthogonal decomposition (METHOD) is proposed to achieve real-time forecast of flow field using structural deformation.
#### 贡献句
- 原句/结构：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
- 原句/结构：Then, we establish the multilayer model of flow field.
  可迁移模板：Then, we establish the multilayer model of flow field.
- 原句/结构：First, we establish the POD model of structural deformation.
  可迁移模板：First, we establish the METHOD model of structural deformation.
#### 限制/边界句
- 原句/结构：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices. https://doi.org/10.1016/j.jfluidstructs.2023.104023 Received 12 May 2023; Received in revised form 4 October 2023; Accepted 6 November 2023 Available online 24 November 2023 0889-9746/© 2023 Elsevier Ltd.
  可迁移模板：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for METHOD systems with complex flow structures such as coherent vortices. https://doi.org/X/j.jfluidstructs.XReceived XMay X; Received in revised form XOctober X; Accepted XNovember XAvailable online XNovember METHOD-X/© XElsevier Ltd.
- 原句/结构：In above studies, many deep learning algorithms are used in the black-box methods, but only POD is used in the gray-box methods.
  可迁移模板：In above studies, many deep learning algorithms are used in the black-box methods, but only METHOD is used in the gray-box methods.
- 原句/结构：Li et al. (2019) used LSTM to forecast unsteady aerodynamics of airfoil pitching and plunging system under different flow conditions, but this study only focused on predicting aerodynamic coefficients.
  可迁移模板：Li et al. (X) used METHOD to forecast unsteady aerodynamics of airfoil pitching and plunging system under different flow conditions, but this study only focused on predicting aerodynamic coefficients.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
