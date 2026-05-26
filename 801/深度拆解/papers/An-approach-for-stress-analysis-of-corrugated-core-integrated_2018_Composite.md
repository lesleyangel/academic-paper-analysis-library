# An approach for stress analysis of corrugated-core integrated thermal protection system under thermal and mechanical environment 深度拆解

## 0. 读取说明

本文拆解基于 `801/文本/txt/An-approach-for-stress-analysis-of-corrugated-core-integrated_2018_Composite.txt` 的 26 页 PyMuPDF 文本抽取。抽取文本能确认题名、摘要、主要公式、章节顺序、算例设置、图题和结论，但无法直接复核曲线重合程度、云图颜色和局部应力集中细节；凡涉及图中局部峰值、边缘误差和曲线形态处，均需标注“需要 PDF 图像复核”。本文主体用中文分析，短引只保留必要关键词。

## 1. 基本信息与论文身份

- 题名：An approach for stress analysis of corrugated-core integrated thermal protection system under thermal and mechanical environment。
- 作者与机构：Chunlin Gong, Yifan Wang, Liangxian Gu, Shengbo Shi；Northwestern Polytechnical University。
- 期刊与年份：Composite Structures, 185, 2018, 1-26。
- 论文类型：工程结构力学方法论文，结合等效模型、高阶层合理论、结构力学和 3D FEM 验证。
- 研究对象：梯形波纹芯一体化热防护系统 ITPS，在机械横向压力、热载荷及热-机械耦合载荷下的应力分布。
- 核心方法：把离散波纹芯 ITPS 均匀化为等效夹层板，引入温度相关材料参数，基于 C0 高阶 layerwise theory 得到整体位移场，再用结构力学恢复波纹腹板、上面板、下面板中的局部应力。
- 主要证据：3 个载荷算例，压力、温度、压力加温度；与 Nastran 3D 壳单元模型对比，3D FEM 模型含 47474 节点和 37440 单元。

## 2. 摘要与核心信息提取

一句话主张：本文声称可以用一个比 3D FEM 更快的等效夹层板加局部应力恢复方法，较准确预测梯形波纹芯 ITPS 在热-机械环境下的面板和腹板应力。

摘要的卖点组织很直接：先说 ITPS 应力分布需要预测，再说明使用前期等效夹层模型；随后列出本文新增的 stress prediction 方法，即高阶层合理论、温度相关材料参数、面板曲率、上面板受压局部位移和下面板受腹板作用局部位移；最后用 3D FEM 验证“显著减少计算量且吻合较好”。核心信息不是新的 ITPS 概念，而是“等效模型如何重新恢复离散结构应力”。

最重要的隐含边界是：该方法不是完全替代 3D FEM，而是服务初步设计中的快速应力评估；其优势来自等效板低自由度，风险来自等效化后边缘、节点和应力集中区域的局部误差。

## 3. 选题层深拆

问题来源来自高超声速/可重复使用飞行器的 ITPS 设计瓶颈：热防护系统既要隔热又要承载，传统 TPS 不满足轻量化、维护性和重复使用要求。梯形波纹芯 ITPS 结构离散，直接做 3D FEM 可捕捉复杂几何和温度相关材料，但不适合初步设计反复迭代。

作者把大问题收束成一个很具体的工程问题：不再泛泛讨论 ITPS 性能，而是问“给定热载荷和机械载荷，如何快速得到波纹腹板、上面板、下面板的实际应力分布，尤其是表面应力而非中面应力”。这个问题的价值在于强度校核通常由最大应力控制，而薄面板弯曲使最大应力出现在表面，中面应力不足以判断安全性。

选题成立依赖三个必要性：第一，3D FEM 精确但慢；第二，既有均匀化模型能给位移却难给离散结构应力；第三，已有 stress recovery 多忽略温度相关参数、横向法向应变或腹板应力。

## 4. 领域位置与文献版图

文献版图分成四层。第一层是 ITPS 工程设计与 3D FEM 研究，包括 Bapanapalli、Sharma、Rajesh 等，用来证明问题重要且传统方法昂贵。第二层是波纹板/波纹芯等效刚度和均匀化方法，从 Seydel、Briassoulis 到 Bartolozzi、Mohammadi、Gu，说明等效夹层模型的理论来源。第三层是 layerwise plate/sandwich theory，如 Plagianakos、Pandey、Gu，提供厚芯夹层板位移场和横向法向应变处理。第四层是离散芯结构应力恢复，如 Romanoff、Martinez、He、Gu，用来制造本文 gap。

本文站位是“继承 Gu et al. 的温度相关等效刚度和 C0 高阶层合理论，但把它从位移/中面应力推进到离散腹板和面板表面应力恢复”。它不是完全新理论，而是将已有等效模型用于更接近强度设计的应力层级。

## 5. Gap 制造机制

作者制造 gap 的方式是逐步收窄已有方法的适用边界。3D FEM 可以算应力，但太耗时；均匀化夹层板可以算整体位移，但难恢复离散几何应力；Martinez 类方法能算热-机械应力，但没有横向法向应变和温度相关材料；He 的半解析方法可捕捉应力波动，但不能预测波纹腹板应力；Gu 的前期工作只给不同 sheet 中面的正应力，而实际最大应力常在薄板表面。

这个 gap 属于“方法 gap + 证据/设计使用 gap”。它不声称无人研究 ITPS，而是指出已有工作没有把“快速等效计算”和“工程需要的表面/腹板应力”同时满足。该 gap 与本文方法高度一致，因为全文的 4 节几乎都在把等效位移场转成腹板、上面板和下面板应力。

## 6. 创新性判断

作者声明的创新是提出一种快速准确的应力计算方法，考虑温度相关材料属性、面板曲率、横向压力导致的上面板局部变形，以及波纹腹板传力导致的下面板局部变形。

真实创新强度为中等偏强。强处在组合式工程化：不是单个公式，而是把均匀化、layerwise theory、Castigliano/结构力学、局部板梁模型串成完整 stress recovery 流程。弱处在理论基础多来自前期工作和经典结构力学，创新主要是“扩展到完整应力恢复和算例验证”。它容易被挑战的点是：局部应力集中、边界层误差、剪应力只保趋势等地方说明方法不是高保真替代。

## 7. 论证链条复原

论文论证链为：未来飞行器需要轻量、可重复使用 ITPS；梯形波纹芯 ITPS 的热-机械应力设计重要；3D FEM 精确但慢，均匀化模型快但不能直接给离散应力；因此需要一种基于等效夹层板的应力恢复方法；方法先对温度场和等效材料参数降维，再用 C0 高阶 layerwise theory 得到等效板位移与应变，随后分部件恢复波纹腹板、上面板、下面板的中面和表面正应力及面内剪应力；最后用压力、热载荷、热-机械耦合三类工况与 3D FEM 对比，证明总体吻合。

最薄弱环节是从等效夹层板位移场到离散局部应力的映射。作者通过局部曲率、连续板/梁假设和与 FEM 对比来补强，但边缘、腹板连接点和剪应力细节仍有明显不确定性。

## 8. 方法/理论/模型细拆

方法输入包括 ITPS 几何参数 `p, h1, h2, h3, tw, theta`，温度场、材料温度相关弹性模量与热膨胀系数、边界条件和外压。输出是腹板、上面板、下面板的正应力和面内剪应力分布。

第一步是温度场和材料参数均匀化。面板因薄而假设厚度方向温度均匀，波纹芯温度场按单胞几何简化为 `DeltaTr(x,z)`，然后推导温度相关的等效弹性模量、剪切模量和热膨胀系数。第二步是 C0 高阶 layerwise theory：中间厚芯层采用线性、二次、三次位移项并考虑横向法向应变，上下面薄层采用一阶面内位移场和厚度均匀横向位移。第三步是局部 stress recovery：腹板中面应变来自等效中层位移，表面应力通过全局弯曲曲率和剪切诱导曲率修正；上面板额外考虑外压下多跨连续/固支板局部弯曲；下面板额外考虑波纹腹板传递的局部力和弯矩。

关键假设包括周期性单胞等效、面板薄板行为、局部结构力学边界简化、温度场在若干方向的简化、材料温度函数拟合。复现信息较足，公式和几何参数详细，但图中应力云图数值需要 PDF 图像复核。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 等效夹层模型可用于快速分析梯形波纹芯 ITPS | 摘要、2-3 节 | 温度场降维、等效刚度公式、C0 高阶层合理论 | 中 | 依赖前期 Gu et al. 工作，本文不是从零验证等效刚度 |
| 本文方法能恢复腹板、上面板、下面板应力 | 4 节 | 分别推导 corrugated webs、bottom/top face sheets 的正应力和剪应力 | 强 | 推导长且依赖局部结构力学假设 |
| 表面应力比中面应力更关键 | Introduction、4.1.2 | 薄板弯曲导致最大应力出现在 sheet 表面，作者专门引入曲率 | 中 | 未给独立实验，只用力学常识和 FEM 对比支撑 |
| 压力载荷下方法与 3D FEM 结果吻合 | 5.1 | Figs. 7-16 与 Nastran 壳单元模型对比，47474 节点、37440 单元 | 中强 | 边缘和连接点应力集中预测不足；需要 PDF 图像复核 |
| 热载荷下方法能捕捉主要正应力趋势 | 5.2 | Figs. 17-26，线性温度场 `50-250 C`，温度相关 PM2000 | 中 | 上面板外表面仅能捕捉趋势，局部差异较大 |
| 热-机械耦合下仍有较好一致性 | 5.3 | Figs. 27-36，压力 0.1 MPa 加相同线性温度场 | 中强 | “excellent agreement” 主要来自图形对比，缺少系统误差表 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核点 |
| --- | --- | --- | --- | --- |
| Fig. 1-2 | 给出真实波纹芯 ITPS 和等效夹层板的几何映射 | 离散结构可等效为夹层板 | 建立后续所有等效公式的几何基础 | 需要 PDF 图像复核几何标注 |
| Fig. 3, Eqs. 3-19 | 展示单胞、温度场降维、等效弹性/热膨胀系数 | 温度相关均匀化可行 | 把复杂三维温度场压缩到等效芯层参数 | 公式排版需 PDF 复核 |
| Eqs. 20-32 | 构造 layerwise 位移、应变、应力关系 | 等效板能给全局应变状态 | 中层高阶、面层一阶的混合位移假设 | 需核公式符号 |
| Eqs. 47-78 | 腹板应力恢复 | 能预测腹板中面、表面和剪应力 | 引入全局弯曲和剪切曲率 | 曲率推导复杂，建议复核 |
| Eqs. 79-99 | 面板应力恢复 | 能预测上下面板局部应力 | 上面板考虑压力局部弯曲，下面板考虑腹板传力 | 局部边界条件需复核 |
| Figs. 7-16 | 压力载荷验证 | 与 FEM 吻合 | 总体趋势和数量级一致 | 图像细节需要 PDF 图像复核 |
| Figs. 17-26 | 热载荷验证 | 温度相关材料下仍有效 | 边缘、上表面存在偏差 | 需要 PDF 图像复核 |
| Figs. 27-36 | 热-机械耦合验证 | 方法适用于组合载荷 | 整体 agreement 被用于结论收束 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实结构为：1 Introduction；2 Homogenization method，含 Reduced temperature fields、Equivalent elastic properties、Equivalent coefficients of thermal expansion；3 Layerwise theory，含 strain-displacement、stress-strain、finite element formulation、cases；4 Prediction of stress，分 corrugated webs 与 face sheets；5 Numerical examples；6 Conclusions；另有多个 Appendix。

结构策略是典型“前期模型继承 + 本文增量推导 + 多场景验证”。Introduction 的末段明确本文 objective 和方法构成，2-3 节把前期模型重新铺好，4 节才是本文真正贡献，5 节用大量图占据篇幅。标题偏描述型，几乎不提前透露结论，适合公式密集型力学论文。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/An-approach-for-stress-analysis-of-corrugated-core-integrated_2018_Composite.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：11
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结论/展望型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Homogenization method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Layerwise theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Strain-displacement relations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Application cases | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1.2 Curvature in corrugated webs induced by global bending moment | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Prediction of stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Stress calculation in corrugated webs of ITPS | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.1.1 Normal strain in the mid-plane of corrugated webs | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2.2 Curvature in bottom face sheets | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Numerical examples                                             lowing dimensions is analyzed: | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 6 Conclusions                                                        corrugated webs, top face sheet and bottom face sheet are calculated, | 结论/展望型 | 收束贡献、边界和未来工作 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 前半段承担工程背景和 ITPS 价值，随后密集综述 3D FEM、均匀化、layerwise、stress recovery，最后用“however”连续收束 gap。方法段落节奏是“先定义几何/变量，再给假设，再列公式，再解释符号”。结果段落节奏是“工况设置、FEM 模型、图组说明、一致性评价、差异解释”。这种写法并不追求叙事华丽，而是让读者沿公式编号和图号移动。

特别可学的是每个结果小节都先说明图组覆盖哪个部件和哪个厚度位置，再评价 agreement，最后主动承认边缘、连接点和剪应力趋势的问题。这使得 claim 不至于过强。

## 13. 文笔画像与语言习惯

整体语气保守、工程化、公式驱动。常用动词包括 predict, calculate, derive, obtain, consider, compare, verify。常用限定语包括 acceptable, agree well, trend and magnitude, unable to predict accurately。时态上，Introduction 用一般现在时描述领域事实和已有方法，方法推导用现在时，算例用过去时或现在时混合。

主动/被动方面，被动表达占多，如 “is homogenized”, “is derived”, “is compared”。作者较少用 “we”，更喜欢让方法和公式做主语。形容词多服务边界判断，如 accurate, fast, complicated, temperature-dependent, local。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：corrugated(111)；face(111)；bottom(81)；top(76)；stresses(74)；sheets(73)；itps(70)；normal(69)；stress(54)；webs(53)；temperature(50)；sheet(48)；sin(47)；method(45)；subjected(45)；shear(44)；equivalent(43)；distribution(39)；thermal(37)；panel(37)
- 高频学术名词：analysis(60)；stress(54)；temperature(50)；method(45)；distribution(39)；structures(35)；pressure(30)；displacement(29)；element(29)；curvature(27)；deformation(26)；properties(22)；model(19)；strain(17)；material(17)；section(16)
- 高频学术动词：shown(19)；derived(13)；show(9)；proposed(8)；predict(7)；developed(7)；shows(5)；investigated(3)；predicted(2)；captured(2)；compared(1)；formulated(1)；develop(1)；propose(1)；investigate(1)；formulate(1)
- 高频形容词：normal(69)；equivalent(43)；thermal(37)；local(34)；displacement(29)；element(29)；trapezoidal(20)；material(17)；structural(15)；static(12)；elastic(12)；moment(12)；present(12)；mechanical(11)；temperature-dependent(10)；linear(9)
- 高频副词/连接副词：respectively(27)；accurately(8)；however(5)；therefore(3)；simply(3)；consequently(2)；globally(2)；currently(2)；easily(2)；fully(2)；moreover(1)；cantly(1)；rapidly(1)；greatly(1)；tively(1)；spectively(1)
- 高频二词短语：face sheets(64)；top face(53)；corrugated webs(50)；normal stresses(49)；face sheet(42)；bottom face(42)；composite structures(27)；corrugated core(25)；gong composite(25)；temperature distribution(22)；stresses mid-plane(22)；sheet subjected(22)；bottom top(20)；subjected pressure(20)；itps panel(19)；trapezoidal corrugated(15)
- 高频三词短语：top face sheets(26)；top face sheet(25)；gong composite structures(25)；bottom face sheets(24)；face sheet subjected(22)；bottom face sheet(17)；normal stresses mid-plane(16)；mid-plane corrugated webs(15)；sheet subjected pressure(14)；composite structures normal(12)；structures normal stresses(12)；bottom top face(11)

**主动、被动与句法**

- 被动语态估计次数：165
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：530
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：231
- 一般过去时线索：36
- 现在完成时线索：9
- 情态动词线索：44
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：corrugated(34)；equivalent(28)；core(24)；stress(23)；itps(23)；temperature(21)；method(19)；thermal(17)
- 3. Layerwise theory：layer(17)；element(15)；displacement(10)；eld(8)；middle(8)；matrix(8)；jth(8)；plate(6)
- 3.4. Application cases：corrugated(9)；integration(6)；webs(5)；shear(4)；web(3)；bending(3)；reduced(3)；due(3)
- 4. Prediction of stress：stresses(3)；webs(2)；section(2)；itps(2)；curvatures(2)；occurs(1)；easy(1)；corrugated(1)
- 4.1. Stress calculation in corrugated webs of ITPS：corrugated(3)；along(3)；webs(2)；studied(2)；curvature(2)；induced(1)；itps(1)；bending(1)
- 4.1.1. Normal strain in the mid-plane of corrugated webs：face(52)；sheets(37)；bottom(35)；corrugated(31)；top(31)；normal(27)；itps(22)；curvature(21)
- 5. Numerical examples                                             lowing dimensions is analyzed:：stresses(37)；face(34)；normal(23)；subjected(22)；sheets(22)；surface(22)；panel(21)；mid-plane(18)
- 6. Conclusions                                                        corrugated webs, top face sheet and bottom face sheet are calculated,：sin(30)；tan(19)；corrugated(15)；sandwich(15)；struct(14)；analysis(13)；cos(12)；diw(12)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：Future vehicles require X not only to..., but also to...
- gap 句式：However, the method is incapable of solving the problem with...
- 方法句式：By combining A with B, the stresses in C are calculated.
- 结果句式：The stresses obtained by the present method agree well with those given by 3D finite element analysis.
- 限定句式：Only the trend and magnitude can be captured by the present method.
- 可迁移表达：`temperature-dependent material properties`, `equivalent sandwich model`, `local deformation`, `stress concentration`, `preliminary design`。

## 15. 引用策略与文献使用

引用主要服务三件事：证明 ITPS 工程重要性，铺垫等效刚度和 layerwise theory 的合法性，制造应力恢复 gap。作者对前人多采用“继承加转折”的姿态，很少强批判。典型路径是先承认 3D FEM 的精确性，再指出其 time consuming；承认 homogenization 能预测 displacement，再指出难得 discrete stress distribution；承认已有 stress analysis 方法，再指出未考虑温度相关、横向法向应变或表面最大应力。

文献覆盖从经典波纹板到近期 ITPS 方法，但最近文献比例受 2018 年发表时间限制。引用密度集中在 Introduction，方法和算例引用较少，说明本文把可信度主要建立在“公式推导 + FEM 对比”而非大量讨论文献上。

## 16. 审稿人视角风险

第一，最强 claim 是“accurate and fast”，但文中主要是图形对比，缺少系统误差统计和计算时间表。第二，边界和腹板-面板连接处的应力集中不能捕捉，这对强度设计可能正是危险位置。第三，剪应力部分作者承认只能捕捉 trend and magnitude，若用于失效准则需谨慎。第四，算例几何、材料和边界条件较单一，尚未证明对不同波纹角、芯高、热梯度和约束形式都稳健。第五，方法依赖前期等效刚度模型，若等效刚度本身误差较大，stress recovery 会叠加误差。

## 17. 可复用资产

可复用选题套路：把“高保真但慢”的 3D 模型压缩成“初步设计可用”的等效模型，再针对高保真模型中最关键的工程输出做局部恢复。可复用论证链：3D FEM 精确但慢；等效模型快但输出不足；本文补齐输出；用少数代表性载荷工况与 3D FEM 对比。可复用图表设计：真实结构图、等效结构图、单胞图、局部受力图、分部件分层应力图组。可复用风险写法：主动承认边缘和应力集中区域偏差，把方法定位为 fast preliminary design tool。

## 18. 对我写论文的启发

如果自己的论文也做工程快速模型，不必把贡献包装成“完全替代高保真”，而应明确服务场景：初步设计、参数扫描、快速评估。更重要的是要说明“快模型原本缺什么输出”，然后把贡献放在这个缺口上。本文还提示，结果图组不要只给最终指标，可以按部件、位置、载荷类型系统铺开，让审稿人看到方法在不同结构区域的表现。

## 19. 最终浓缩

这篇论文的核心是：用等效夹层板获得 ITPS 全局响应，再用结构力学把离散波纹芯和面板的实际应力恢复出来，从而在比 3D FEM 更经济的框架下支持热-机械强度初步设计。最值得学的是 gap 的精确收束和 stress recovery 的分部件推导；最大风险是局部应力集中、边缘效应和误差统计不足，图像细节需要 PDF 图像复核。
