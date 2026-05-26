# High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks

## 0. 读取说明

本拆解基于 `801/文本/txt/High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.txt` 的全文抽取。抽取文本包含公式、表格数值、图题和结论，但部分双栏文本顺序混杂；本拆解以可确认的正文叙述为准。压力云图、模态形状和误差分布的视觉细节标注“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks。
- 作者：Xuanhe Ding、Chunlin Gong、Hua Su、Chunna Li、Wei Li、Xuyi Jia。
- 期刊：Aerospace Science and Technology，176，2026，111927。
- 领域：非定常气动载荷建模、降阶模型、气动弹性、深度学习代理模型。
- 论文类型：方法提出 + 数值验证。
- 研究对象：结构振动诱导的高维非定常气动载荷分布。
- 主要方法：结构模态空间 + 气动 POD 模态空间耦合成 Dual Modal Space (DMS)，以 generalized aerodynamic forces 为中间变量，再用 LSTM 预测时序演化，并通过显式映射重构气动载荷。
- 对比基线：POD-LSTM、DMS-OpInf、POD-OpInf；三维翼算例中主要对比 DMS-LSTM 与 POD-LSTM。
- 核心指标：POD 系数 RMSE/NSE、升力系数 RMSE/NSE、表面压力系数重构误差、全局重构精度。

## 2. 摘要与核心信息提取

一句话主张：传统 POD-ROM 在结构振动条件下会遭遇模态混叠和高阶系数高频振荡，DMS 通过把气动载荷投影到结构模态空间，构造具有物理含义且更平滑的 generalized aerodynamic forces，从而让 LSTM 更准确、稳定地预测非定常气动载荷分布。

摘要的信息层次很完整：重要性是 aircraft performance evaluation and safety assurance；旧方法不足是 POD 系数难以从结构变形映射、模态混叠、高阶系数高频振荡；方法是 DMS + LSTM；机制解释是空间积分滤除与结构响应弱相关的小尺度高频流动结构；证据是二维 NACA65A004 和三维 AGARD445.6 翼，精度超过 97.2%，压力分布误差约降低 50%，升力误差在三维翼中最高改善约 80.7%。

## 3. 选题层深拆

选题来自航空结构轻量化和柔性化带来的强非定常气动问题。高保真 CFD 虽准，但长时间、变形边界模拟成本过高；数据驱动 ROM 可提速，却在结构振动场景下因为输入/输出物理空间不匹配而失稳。

作者没有把问题泛化成“深度学习预测气动载荷”，而是聚焦到一个更尖锐的建模矛盾：POD 模态是按气动能量排序的，结构振动输入却在结构模态空间中表达，两者直接映射会出现 modal mixing。这个问题定义很有效，因为它让 DMS 的必要性不是“换一种神经网络”，而是“换一个低维状态变量”。

选题价值在于：它同时面向工程效率、物理可解释性和模型泛化稳定性。对 AST 读者来说，单纯 LSTM 不够新，但“结构模态对齐的气动载荷降阶表示”更贴近气动弹性建模传统。

## 4. 领域位置与文献版图

文献版图分为四组。第一组是高保真 CFD 和气动弹性背景，用于说明准确预测载荷的重要性和成本瓶颈。第二组是黑箱数据驱动模型，如深度网络、operator learning，它们灵活但数据需求高、解释性弱。第三组是灰箱 ROM，尤其 POD-LSTM，它有能量最优基础但在结构振动条件下暴露 modal mixing。第四组是 SPOD、DMD、Koopman、physics-informed learning 等扩展方向，作者承认它们提供互补视角，但指出与结构对齐气动表示的结合仍是 open challenge。

本文站位是“不是发明更复杂的 surrogate，而是重构 surrogate 的状态空间”。这使得 DMS-LSTM 与普通 POD-LSTM 的差异更像物理表示差异，而非网络调参差异。

## 5. Gap 制造机制

Gap 的制造有两层。显性 gap：现有 POD-LSTM 在结构振动诱导的非定常气动载荷预测中困难显著，包括结构变形到 POD 系数映射困难、高阶系数高频振荡导致 surrogate 收敛和泛化问题。隐性 gap：许多数据驱动模型追求 latent complexity，但没有解决结构动力学与气动载荷之间的物理一致性。

作者用 generalized aerodynamic forces 填补 gap：它们由 CFD 载荷投影到结构模态基得到，每个力都对应特定结构振型贡献，因此比 POD 系数更有物理意义、更平滑，也更适合作为学习目标。

Gap 的可信度较强，因为后文不只说 POD 不好，而是在二维和三维算例中显示高阶 POD 系数的误差与频谱失真，并用 DMS 在不同 surrogate（LSTM 和 OpInf）中均改善来证明主要收益来自空间构造。

## 6. 创新性判断

作者声明的创新是 DMS 模型、DMS-LSTM 框架、generalized aerodynamic forces 中间表示、显式双向映射 Q-a-F，以及二维/三维验证。

真实创新属于“表示层创新 + 工程验证”。LSTM、POD、结构模态投影都不是新概念；新意在于把结构模态空间和气动 POD 空间通过 dual modal mapping matrix H 连接，使低维变量既能学习又能重构。这类创新的强度取决于是否能证明 DMS 比 POD 的优势来自物理空间对齐，而不是算例偶然性。论文通过 DMS-OpInf 的辅助对比增强了这一点。

容易被挑战的地方：DMS 要求结构模态数与 POD 模态数匹配，并依赖 H 的可逆/条件数；目前限于线性结构模态、开放环 prescribed structural motions、亚声速测试参数范围。

## 7. 论证链条复原

1. 柔性航空结构导致结构振动与气动载荷强耦合，高维非定常载荷需要快速准确预测。
2. CFD 成本高，POD-LSTM 等 ROM 是合理方向。
3. 但 POD 系数是气动能量模态，结构输入是结构模态，两者直接学习会 modal mixing，且高阶 POD 系数高频振荡难学。
4. 因此需要一个与结构动力学一致的低维气动表示。
5. generalized aerodynamic forces 由气动载荷投影到结构模态得到，保留物理含义，并滤除弱相关小尺度高频结构。
6. DMS 构造 H=Phi_A^T Phi_p，实现 Q 与 POD 系数 a 的显式映射，再由 a 重构载荷 F。
7. LSTM 学 q 和历史 Q 到当前 Q 的时序映射，降低直接预测高维 F 或高频 a 的难度。
8. 二维、复杂激励、三维算例均显示 DMS-LSTM 在 RMSE/NSE、升力和压力分布重构上优于 POD-LSTM。
9. 结论收束为：DMS 提升主要来自模态空间构造，并为后续非线性结构/闭环气动弹性扩展铺路。

## 8. 方法/理论/模型细拆

DMS 的输入是结构模态矩阵 Phi_s、映射到气动网格的结构模态 Phi_A、CFD 载荷快照 F、POD 气动模态 Phi_p。结构方程 M Xddot + C Xdot + KX = F 投影到结构模态，得到 generalized coordinate q 和 generalized aerodynamic force Q=Phi_s^T F；在气动网格上则用 Phi_A 表示结构模态。

气动 POD 对载荷快照去均值后构造协方差，保留 r 个主模态，得到 F(t)=Phi_p a(t)+F_bar。DMS 核心是把 Q 与 a 联系起来：Q-Q0=H a，其中 H=Phi_A^T Phi_p，Q0=Phi_A^T F_bar。预测时先由 LSTM 得到 Q，再 a=H^{-1}(Q-Q0)，最后 F=Phi_p a+F_bar。

LSTM 数据组织采用滑动窗口。输入包含过去和当前 generalized displacement q，以及过去 generalized aerodynamic forces Q；输出为当前 Q。二维 case 使用两层 64 hidden units，三维 case 使用两层 128 hidden units，窗口长度 W=2，Adam 学习率 0.001，RMSE loss。

验证设计有三层：二维 NACA65A004 常规多频激励，对比 DMS-LSTM/POD-LSTM/DMS-OpInf/POD-OpInf；二维复杂激励同时改变 Mach、攻角和宽带结构模态；三维 AGARD445.6 翼用 40 模态验证真实复杂度下的性能。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| POD-LSTM 在结构振动下的主要困难是 modal mixing 和高阶系数高频振荡 | Introduction/4.1/4.2 | Fig. 10、Fig. 35 中 POD 系数非线性增强，Fig. 11/36 高阶误差增大 | 强 | 高频结构视觉与频谱需 PDF 图像复核 |
| generalized aerodynamic forces 更平滑、更适合作为学习变量 | Section 2/4.1/4.2 | 投影定义 Q=Phi_A^T F，结果段称 DMS 空间线性可分性更好 | 中强 | 平滑性主要由图和定性描述支撑 |
| DMS-LSTM 在二维基准算例中优于 POD-LSTM | 4.1.2 | Table 2：升力 RMSE 1.844e-4 vs 4.151e-4，NSE 6.082e-3 vs 1.612e-2 | 强 | 训练随机性需多次运行统计，文中有 box plot |
| DMS 优势不是 LSTM 独有，而来自模态空间构造 | 4.1.2 | DMS-OpInf 也优于 POD-OpInf；作者明确比较两类 surrogate | 强 | OpInf 设置和正则化参数可能影响公平性 |
| 复杂激励下 DMS-LSTM 仍更稳 | 4.1.3 | Table 4：DMS-LSTM RMSE 4.87e-3，POD-LSTM 1.06e-2；box plot 离散度更小 | 强 | 仍是 interpolation within tested range |
| 三维翼中 DMS-LSTM 优势更明显 | 4.2 | Table 5：升力 RMSE 2.935e-5 vs 1.519e-4，误差降低 80.678% | 强 | 只对比 LSTM，未含 OpInf |
| DMS-LSTM 维持超过 97.2% 的全局重构精度 | Abstract/4.2 | 三维表面压力 RMSE 平均 1.485e-3，约低于 POD-LSTM 50.134% | 中强 | “global accuracy”具体定义需 PDF/公式复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | DMS 概念图 | 结构模态与气动 POD 可统一 | 给读者先验框架 | 需要 PDF 图像复核 |
| Eq. 1-5 | 结构模态空间和 generalized force 定义 | Q 有明确物理意义 | X=Phi_s q，Q=Phi_s^T F | 文本可确认 |
| Eq. 6-14 | POD 气动模态空间 | 传统气动降阶表示 | F=Phi_p a+F_bar | 文本可确认 |
| Eq. 15-18 | DMS 双向映射核心 | Q-a-F 可显式重构 | H=Phi_A^T Phi_p，a=H^-1(Q-Q0) | 文本可确认 |
| Fig. 3-4 | DMS-LSTM 训练和预测流程 | 模型闭环完整 | 数据生成、降维、LSTM、重构 | 需要 PDF 图像复核 |
| Fig. 10/35 | 对比 POD 系数与 generalized forces | DMS 表示更易学习 | 高阶 POD 非线性更明显 | 需要 PDF 图像复核 |
| Fig. 11-18 | 二维基准结果 | DMS-LSTM 减少模态和载荷误差 | 升力、压力分布双指标支持 | 需要 PDF 图像复核 |
| Fig. 19-28 | 复杂激励结果 | 非定常气动条件下仍稳定 | Mach/攻角/宽带结构输入同时变化 | 需要 PDF 图像复核 |
| Fig. 29-41 | 三维 AGARD 翼验证 | 复杂三维流中优势放大 | 高阶模式和压力重构改善 | 需要 PDF 图像复核 |
| Table 2-6 | 量化证据 | 误差降低百分比 | 50%+ 压力误差降低，三维升力 80.678% 改善 | 文本可确认 |

## 11. 章节结构与篇章布局

章节为：Introduction -> Dual modal space model -> DMS-LSTM surrogate modeling -> Test case -> Conclusion。结构是典型方法论文：先解释旧方法失效点，再建数学框架，再给学习流程，最后多算例验证。

Introduction 的说服节奏很清楚：航空轻量化背景 -> CFD 成本瓶颈 -> ROM 分类 -> POD-LSTM 局限 -> generalized forces/DMS 方案。Section 2 负责让读者相信 DMS 是物理上闭合的；Section 3 负责让读者相信 DMS 可被神经网络使用；Section 4 用层层加难的算例证明从二维到三维都有效。

标题偏方法型和算例型，如 “Dual modal space model”、“DMS-LSTM surrogate modeling”、“Case A/B”。小节标题不花哨，但变量暴露充分。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2.2 Aerodynamic modal space via POD | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2 Dual modal space model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Structural modal space                                                           all three Cartesian directions, yielding: | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Test case | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Case B: Three-dimensional wing | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2.1 Case setup | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

方法段落多采用“定义变量 -> 写公式 -> 解释物理意义 -> 指出计算优势”的节奏。结果段落常用“先分析 POD 现象 -> 再解释 DMS 优势 -> 最后给误差表”。

作者特别重视“隔离变量”的叙事：通过 DMS-OpInf vs POD-OpInf 说明不是 LSTM 技巧导致提升；通过复杂激励说明不是简单周期输入下偶然有效；通过三维翼说明高非线性场景中优势更明显。

结论段落非常标准：第一段概括框架，第二段概括 DMS 物理映射，第三段概括数值提升，第四段承认线性模态和开放环限制。

## 13. 文笔画像与语言习惯

文风是工程方法论文的“稳态推进”：术语密度高，句子偏长，名词化强。高频名词包括 generalized aerodynamic forces、modal coefficients、structural modes、POD modes、unsteady aerodynamic load distribution、surrogate model、reconstruction accuracy。

作者常用强解释动词：mitigate、suppress、retain、establish、reconstruct、outperform、facilitate、align。谨慎限定词包括 within the tested parametric range、open-loop、prescribed structural motions、subsonic conditions。这些限定词在摘要和结论中重复出现，用于防止模型泛化 claim 过强。

被动语态用于方法定义，如 “is computed as”、“is reconstructed using”；主动语态用于贡献表达，如 “the proposed model effectively mitigates”。时态上方法用现在时，算例结果用现在时/过去时混合，结论用现在时。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：aerodynamic(131)；structural(101)；modal(101)；pod(65)；model(56)；generalized(54)；modes(51)；modeling(50)；unsteady(49)；load(42)；models(38)；prediction(37)；distribution(36)；coefficient(36)；coefficients(35)；dms-lstm(35)；time(35)；org(34)；space(32)；airfoil(32)
- 高频学术名词：model(56)；prediction(37)；distribution(36)；analysis(34)；pressure(23)；deformation(22)；science(22)；excitation(22)；conditions(21)；vibration(21)；reconstruction(21)；decomposition(20)；framework(12)；results(12)；performance(12)；basis(12)
- 高频学术动词：predicted(31)；shown(19)；proposed(14)；compared(10)；evaluate(6)；evaluated(4)；demonstrate(4)；shows(3)；captured(2)；capture(2)；indicates(1)；indicate(1)；demonstrated(1)
- 高频形容词：aerodynamic(131)；structural(101)；modal(101)；coefficient(36)；dynamic(32)；dominant(28)；physical(22)；nonlinear(20)；numerical(20)；dual(15)；temporal(14)；linear(13)；computational(11)；three-dimensional(11)；global(10)；displacement(10)
- 高频副词/连接副词：significantly(20)；approximately(10)；respectively(9)；strongly(8)；directly(7)；however(6)；consistently(6)；effectively(5)；particularly(5)；separately(5)；commonly(3)；widely(3)；typically(3)；specifically(3)；inherently(3)；explicitly(3)
- 高频二词短语：aerodynamic load(35)；generalized aerodynamic(30)；unsteady aerodynamic(27)；structural modal(26)；naca airfoil(25)；aerodynamic forces(24)；lift coefficient(24)；load distribution(23)；aerospace science(21)；science technology(21)；modal space(20)；ding aerospace(19)；modal coefficients(17)；agard wing(17)；surface pressure(16)；rmse nse(16)
- 高频三词短语：aerospace science technology(21)；generalized aerodynamic forces(21)；aerodynamic load distribution(20)；ding aerospace science(19)；unsteady aerodynamic load(12)；predicted lift coefficient(12)；pod modal coefficients(10)；proper orthogonal decomposition(9)；dual modal space(8)；generalized aerodynamic force(8)；unsteady aerodynamic loads(7)；surface pressure coefficient(7)

**主动、被动与句法**

- 被动语态估计次数：146
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：868
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：221
- 一般过去时线索：42
- 现在完成时线索：3
- 情态动词线索：16
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：aerodynamic(45)；structural(38)；modal(35)；pod(18)；generalized(16)；unsteady(14)；space(13)；modeling(12)
- 2. Dual modal space model：aerodynamic(86)；modal(65)；structural(63)；pod(47)；model(45)；modes(45)；generalized(38)；modeling(38)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- Gap 句式：Existing POD-based ROMs face significant challenges, including... 可复用为“列举式方法不足”。
- 方法定位句：This study proposes a DMS model that integrates X and Y into a unified reduced low-dimensional space.
- 物理解释句：Since Q retains explicit physical property..., the spatial integration filters out...
- 对比句：Compared to traditional POD-LSTM models, prediction errors were reduced by...
- 限定句：The present work focuses on open-loop prediction with prescribed structural vibrations...
- 机制归因句：The improvement mainly stems from the modal space construction rather than the specific surrogate modeling technique.
- 未来工作句：Future work will focus on extending the proposed framework to...

可复用短语：physically interpretable representation、bidirectional mapping、modal mixing phenomenon、high-frequency oscillations、surface pressure reconstruction、time-domain and frequency-domain metrics、global reconstruction accuracy。

## 15. 引用策略与文献使用

引用按功能分布：前几篇用于轻量化/气动弹性背景；CFD 和 ROM 文献用于说明效率瓶颈；POD-LSTM 文献用于建立主流基线；Taira、Berkooz、Lumley 等用于 POD/模态分析理论背书；Kramer、Koopman、SPOD、DeepONet 等用于显示作者知道最新 ROM 生态；Bisplinghoff/Ashley 等气动弹性经典用于 generalized aerodynamic force 的物理基础。

引用姿态偏中性补充，不尖锐批判。作者通常说现有方法 “shown promising performance”，随后用 “however” 指出在 structural vibration 场景下局限突出。这样的写法能避免把 gap 写成稻草人。

## 16. 审稿人视角风险

1. DMS 依赖线性结构模态；大变形、非线性结构、模态耦合强时可能失效。
2. 当前是 prescribed structural motions 的开放环预测，没有完全闭合 FSI/aeroelastic feedback。
3. H 矩阵可逆性和条件数在更复杂构型中可能成为稳定性瓶颈。
4. 结构模态数与 POD 模态数匹配的策略可能不总是最优，缺少模态数敏感性。
5. LSTM 超参数、训练集规模和数据划分对结果影响需要更系统报告。
6. 三维算例只与 POD-LSTM 对比，没有保留 DMS-OpInf/POD-OpInf 或其他深度模型对比。
7. “高保真”依赖 CFD 数据，但实验验证缺失；湍流模型、网格和动态网格误差可能传递到训练标签。
8. 泛化范围被限定为 tested parametric range，外推到跨 Mach、跨攻角、跨结构参数仍待证明。

## 17. 可复用资产

- 表示创新套路：不要先换网络，先重定义物理一致的低维变量。
- 贡献验证套路：同一表示配两个 surrogate，证明收益来自表示；同一 surrogate 配两个表示，证明 DMS 优势。
- 指标组合：RMSE 管时间域，NSE 管频域，再用 lift coefficient 和 pressure distribution 连接工程量。
- 限定写法：在摘要和结论中主动写 open-loop、prescribed motion、subsonic、tested range，降低过度承诺。
- 图表组织：概念图 -> 数学流程图 -> 训练/预测流程 -> modal coefficient 对比 -> 物理量重构。

## 18. 对我写论文的启发

如果自己的方法是“模型 + AI”，最怕被审稿人认为只是把神经网络套上去。本文的启发是：把创新点放在物理表示上，再让 AI 成为自然使用该表示的工具。这样贡献从“拟合器更准”升级成“状态变量更对”。

另外，DMS-OpInf 的设置非常值得学。它相当于一个消融实验，用来证明 DMS 不是 LSTM 特例，而是对多种 surrogate 都有帮助。

## 19. 最终浓缩

这篇论文提出 DMS-LSTM，把结构模态和气动 POD 模态连接起来，用 generalized aerodynamic forces 替代直接 POD 系数作为学习目标，从而缓解模态混叠和高阶高频振荡。最值得学习的是 gap 定义精确、方法变量有物理意义、对比实验能隔离创新来源。主要复核点是三维图像细节、H 矩阵稳定性、开放环预测向闭环气动弹性的扩展。
