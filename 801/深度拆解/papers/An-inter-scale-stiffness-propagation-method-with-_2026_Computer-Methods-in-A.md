# An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites

## 0. 读取说明

- 文本来源：`801/文本/txt/An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.txt`，PyMuPDF 抽取，22 页。
- 图表较多，且含图形摘要、随机孔隙 realizations、协方差/残差/相关矩阵图；本文拆解以文字和表格数值为主，所有图像空间形态均标注需要 PDF 图像复核。
- 这篇是 Batch 5 中方法论密度最高的一篇，重点不只是“孔隙降低刚度”，而是“怎样非侵入地把基体尺度随机孔隙传播到复合材料尺度刚度不确定性”。

## 1. 基本信息与论文身份

- 题名：An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites。
- 作者：Yu-Cheng Yang, Zi-Qian Wang, Jian-Jun Gou, Xiao-Bing Ma, Chun-Lin Gong。
- 期刊：Computer Methods in Applied Mechanics and Engineering，452，2026，118720。
- 领域：复合材料多尺度力学、随机孔隙、RVE 均匀化、不确定性量化、非侵入式随机场建模。
- 论文类型：理论/方法建模 + 数值验证。
- 研究对象：UD 纤维增强复合材料中基体孔隙引起的刚度不确定性。
- 主要方法：Boolean germ-grain 孔隙模型、Poisson 点过程、截断 Gaussian 半径、Matérn 型协方差、FE 均匀化、功率律方差-体积标度、条件 Gaussian 映射、两阶段 Monte Carlo、非侵入式 FE 属性赋值。

## 2. 摘要与核心信息提取

本文的中心命题是：显式在复合材料尺度建模随机孔隙会导致不可承受的计算成本；如果先在基体尺度建立孔隙统计、孔隙-刚度联合分布和体积平均标度，再把统计一致的孔隙/刚度场非侵入地赋给复合材料尺度 FE 网格，就能高效传播孔隙导致的刚度不确定性。

摘要的核心信息有四层：孔隙是刚度不确定性源；显式建模太贵；局部体积效应决定量化精度；本文用 Poisson 球孔隙、Matérn 协方差、方差随体积衰减、负相关刚度-孔隙关系和 Monte Carlo 传播完成闭环。

## 3. 选题层深拆

选题来自制造缺陷和结构可靠性之间的尺度错位。孔隙在基体尺度产生，但设计者关心的是复合材料尺度的等效刚度分布；直接把每个孔隙几何显式塞进大尺度 FE 会导致网格数量和 Monte Carlo 成本爆炸。

作者将问题收束为：在不修改确定性 FE 求解器的前提下，如何让孔隙空间相关、体积平均效应、孔隙-刚度耦合和多刚度分量相关性都能被保留。这个问题比单纯“孔隙率影响模量”更高级，因为它关注统计结构传播，而不是单个均值退化。

价值在于可靠性设计：对于实际生产中只能有限表征孔隙分布的 UD 复合材料，方法可以在有限体积、有限数据、有限网格成本下给出不确定性输入。

## 4. 领域位置与文献版图

Introduction 的文献地图组织得很完整：

- 制造缺陷背景：纤维排布不规则、基体孔隙会影响刚度、强度和损伤。
- RVE/SVE 尺寸效应：小体积有显著样本波动，大体积有 self-averaging，方差常呈反体积或功率律衰减。
- 分布/矩阵距离验证：Frobenius、谱范数、Bhattacharyya distance、KL divergence 用来验证联合统计结构。
- 随机场与空间相关：两点协方差、Karhunen-Loève 和谱方法用于随机场离散。
- micro-CT/image-based 方法：形貌真实但成本高、样本有限且带来 epistemic uncertainty。

本文的位置是“把 stochastic geometry、FE homogenization 和 nonintrusive random field assignment 接起来”。它不是单一孔隙模拟，也不是单纯 RVE 尺寸收敛，而是多尺度统计传播框架。

## 5. Gap 制造机制

gap 是由三重不足构成的：

1. 显式孔隙建模在复合材料尺度不可扩展，尤其 Monte Carlo 下成本过高。
2. 仅用平均孔隙率不能捕捉空间相关和局部体积平均导致的方差变化。
3. 已有随机缺陷均匀化多关注界面不规则或单尺度性质，缺少从基体孔隙到复合材料尺度刚度场的非侵入传播。

这个 gap 被大量引用支撑，并且和工程约束紧密绑定：实际制造不能对每个构件做高分辨 CT，也不能把超大 RVE 显式网格化。因此 gap 具有计算力和数据可得性双重现实基础。

## 6. 创新性判断

- 真实创新 1：用 Boolean 球孔隙模型推导孔隙局部平均的空间-体积协方差，并用 Matérn 核拟合。
- 真实创新 2：将刚度方差随 RVE 体积的功率律衰减与孔隙-刚度强负相关结合为 volume-adaptive joint model。
- 真实创新 3：非侵入地在复合材料 FE 网格单元层面采样孔隙和条件刚度张量，不改求解器。
- 创新强度：强。贡献体现在模型链条完整性，而非某个孤立公式。
- 可能被挑战：球形孔隙和均匀 Poisson 假设较理想；UD 体系验证强，但对织物复合材料、非球形/连通孔隙、孔隙各向异性仍需扩展。

## 7. 论证链条复原

背景：孔隙导致微观缺陷和宏观刚度随机性。

困难：显式建模孔隙太贵；有限 RVE 下方差不能忽略。

方法链：Poisson 球孔隙生成 Y(x) -> 局部平均孔隙 ϕV(x) -> 两点协方差与 Matérn 体积核 -> FE 均匀化得到 X(V) 与 ϕV 的联合统计 -> 功率律描述方差随体积衰减 -> 条件 Gaussian 映射 P(Xe|ϕe, Ve) -> 在复合材料尺度 FE 中 Monte Carlo 赋值。

验证链：孔隙半径/体积分布 -> 协方差拟合残差 -> 矩阵尺度方差-体积功率律和 LOOV -> 相关矩阵 Frobenius/谱误差 -> BD/KL 分布距离 -> 网格独立性 -> 复合材料尺度随机 FE 演示。

结论链：孔隙统计可拟合，刚度-孔隙负相关稳定，非侵入传播在复合材料尺度保留 self-averaging。

## 8. 方法/理论/模型细拆

基体尺度孔隙用 Boolean model：孔中心服从强度为 λp 的 homogeneous Poisson point process，孔半径 Ri 服从截断正态分布，孔隙相为球并集 B(ω)，指示场 Y(x,ω) 为 0/1。局部孔隙率是 ϕV(x,ω)=<Y>V。

统计层先给出平均孔隙率、two-point function S2(r)、indicator covariance CY(r)，再通过局部体积双重积分得到 Var[ϕV] 和 Cϕ(r;V1,V2)。作者把它拟合为 Matérn ν=3/2 核，并显式引入 V^-α 的体积衰减。

力学层通过 matrix-scale RVE 的 FE homogenization 得到有效属性 X(V)，发现均值近似体积不变、方差按 Var[Xi(V)]=Bi|V|^-αi 衰减、刚度与孔隙率强负相关且近似体积不变。由此构建 stiffness-porosity joint Gaussian model。

复合材料尺度实现是非侵入式：对每个 matrix-phase 单元在单元体积上采样局部孔隙 ϕe，再按条件分布 P(Xe|ϕe,Ve) 采样刚度张量 Xe。纤维确定，孔隙只进入基体区域。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| Boolean 孔隙模型可产生可控孔隙统计 | 3/7.1 | Fig. 5 半径和体积分布符合截断 Gaussian 输入 | 中强 | 球孔隙假设理想化，需要真实 micro-CT 对比 |
| 孔隙协方差可由 Matérn 核准确拟合 | 4.3/7.1 | Fig. 7 Monte Carlo 协方差，Table 3 A=483.0、α=1.33、ρ=3.75 μm；Fig. 8 残差无系统趋势 | 强 | 图中残差细节需要 PDF 图像复核 |
| 刚度和孔隙方差随体积呈 self-averaging | 5.3/7.2 | Table 4 COV 随 RVE 变大明显下降；Table 5 αi=0.93-0.98，R2 多数 >0.99 | 强 | 只覆盖设定孔隙分布和四个 RVE 尺寸 |
| 刚度-孔隙相关强负且体积近似不变 | 5.4/7.2 | Fig. 11 刚度分量与 Φ 强负相关，变化约 3-5%；Poisson 比波动被解释为数值敏感 | 强 | Poisson 比处理需要谨慎 |
| 模型联合分布与经验分布一致 | 7.2 | Frobenius/谱误差多在几个百分点，BD <0.2，KL 小 | 强 | Gaussian 假设可能掩盖尾部风险 |
| 非侵入传播在复合材料尺度保留体积标度 | 7.4 | Table 10 COV 从 RVEb3 到 RVEb1 降低；Table 11 α≈0.96-1.02，R2=0.99-1.00 | 强 | 复合材料尺度相关变弱，机制解释需更多材料体系验证 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 展示不同 λp/半径分布下孔隙 realizations | 随机几何生成器可控 | 孔隙密度和大孔概率随参数变化 | 需要 PDF 图像复核 |
| Eq. (1)-(6) | 定义 Poisson 孔中心、半径、孔隙相、局部平均孔隙 | 孔隙场有明确概率结构 | 从几何到 ϕV 的基础 | 文本足够 |
| Eq. (7)-(14) | 推导平均孔隙率、two-point covariance、variance-volume scaling | 方差随体积平均衰减 | Var[ϕV]≈Aϕ|V|^-αϕ | 文本足够 |
| Fig. 7/8 + Table 3 | 验证 Matérn 协方差模型 | 协方差模型准确 | α=1.33，ρ=3.75 μm，残差小 | 需要 PDF 图像复核 |
| Table 4/5 | 矩阵尺度统计和功率律拟合 | 刚度方差随体积下降 | COV 显著下降，α 近 1 | 文本足够 |
| Fig. 11/12/13 + Table 6/7 | 验证相关矩阵和联合分布 | 相关结构体积不变 | F-err/λ-err 几个百分点，BD/KL 小 | 需要 PDF 图像复核 |
| Table 8/9 | 排除网格离散影响 | 误差不是网格造成 | 5154 elements 已足够，E[Φ] 网格无关 | 文本足够 |
| Table 10/11 + Fig. 14/15 | 复合材料尺度演示 | 非侵入传播有效 | α≈1，负相关保留但幅值减弱 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节：1 Introduction；2 Inter-scale stiffness propagation method with stochastic porosity；3 Matrix-scale RVE model of stochastic pores；4 Statistical features and modeling of porosity field；5 Statistical feature of matrix-scale effective properties；6 Composite-scale FE model with nonintrusive pores；7 Results and discussions；8 Conclusion。

文章结构是“先总览流程，再分模块建模，再数值验证”的工程数学论文结构。第 2 章像路线图，把后文 Section 3-6 串成三步：空间统计和体积标度、孔隙-力学耦合、非侵入网格采样。第 7 章按方法模块逐一验证，避免读者只看到最终演示而不知道每个中间假设是否成立。

标题命名偏精确、模块化，适合 CMAE 风格；缺点是标题较长且抽象，读者需要先理解符号体系。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：21
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Inter-scale stiffness propagation method with stochastic porosity | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Matrix-scale RVE model of stochastic pores | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4 Statistical features and modeling of porosity field | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Statistical features of pores field | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Statistical features of porosity field | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.3 Statistical modeling of porosity field covariance | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5 Statistical feature of matrix-scale effective properties | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Stiffness and porosity sampling of RVE size | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.2 FE-based homogenization procedure | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.3 Stiffness and porosity variance decay with RVE size | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.4 Joint distribution modeling of stiffness-porosity | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 6 Composite-scale FE model with nonintrusive pores | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 6.1 Nonintrusive mesh-level sampling in composite scale | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 段落很像系统综述：每段引入一个挑战或工具，再说明它如何连接到本文。方法段落采用“定义符号 -> 给公式 -> 解释物理意义 -> 说明后续如何使用”的节奏。结果段落高度标准化：先说明图表目的，再描述数值趋势，随后给出方法论含义。

特别可学的是第 7 章每一小节都不是孤立展示图，而是回应前文一个建模假设：孔隙统计、方差标度、相关稳定、网格独立、复合尺度保真。这样读者会感觉整条模型链都被逐段加固。

## 13. 文笔画像与语言习惯

语言是高密度、公式驱动、验证导向。高频词包括 porosity、stiffness、covariance、volume、stochastic、correlation、RVE、Monte Carlo。常用动词是 represents、defines、captures、validates、confirms、enables。作者偏好名词化，如 variance-volume scaling、cross-property structure、volume-adaptive joint model。

语气强但不夸张：claim 通常由 “indicating/confirming/demonstrating” 连接证据；限制语包括 “nearly”“essentially”“over the scales investigated”。时态上，方法定义用现在时，数值结果用过去时/现在时混合，结论用 presents/offers/enables。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：porosity(100)；stiffness(62)；covariance(59)；model(58)；volume(52)；stochastic(51)；pore(48)；correlation(45)；local(40)；volumes(37)；rve(36)；matrix(34)；rveb(34)；pores(32)；composite-scale(32)；engineering(31)；properties(29)；sampling(29)；field(28)；variance(28)
- 高频学术名词：porosity(100)；stiffness(62)；covariance(59)；model(58)；correlation(45)；structure(32)；properties(29)；field(28)；variance(28)；analysis(24)；scale(24)；homogenization(20)；distance(19)；section(19)；distribution(18)；variability(17)
- 高频学术动词：proposed(12)；shown(11)；evaluated(8)；show(6)；estimated(4)；compared(3)；predicted(3)；evaluate(3)；shows(3)；demonstrate(3)；developed(3)；validate(2)；formulated(2)；reveal(2)；indicate(2)；solved(1)
- 高频形容词：local(80)；stochastic(51)；effective(48)；spatial(24)；numerical(22)；consistent(21)；elastic(20)；small(17)；nonintrusive(17)；element(16)；statistical(16)；geometric(14)；independent(13)；spherical(12)；volume-invariant(12)；empirical(11)
- 高频副词/连接副词：strongly(14)；approximately(10)；nearly(10)；therefore(9)；directly(8)；statistically(7)；numerically(6)；primarily(6)；uniformly(5)；consistently(5)；consequently(4)；substantially(4)；computationally(4)；accurately(4)；independently(4)；highly(4)
- 高频二词短语：monte carlo(28)；computer methods(21)；methods applied(21)；applied engineering(21)；yang computer(19)；gpa gpa(14)；porosity field(13)；stochastic porosity(12)；poisson ratios(12)；composite scale(11)；variance-volume scaling(11)；rveb rveb(11)；effective properties(10)；mpa mpa(10)；rvem rvem(9)；covariance model(8)
- 高频三词短语：computer methods applied(21)；methods applied engineering(21)；yang computer methods(19)；gpa gpa gpa(13)；mpa mpa mpa(8)；rvem rvem rvem(6)；rveb rveb rveb(5)；mean standard deviation(5)；stochastic pore realizations(4)；elems elems elems(4)；inter-scale stiffness propagation(3)；poisson point process(3)

**主动、被动与句法**

- 被动语态估计次数：152
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：1143
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：246
- 一般过去时线索：65
- 现在完成时线索：11
- 情态动词线索：24
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：porosity(10)；stiffness(6)；uncertainty(6)；modeling(5)；volume(5)；engineering(4)；stochastic(4)；composites(4)
- 1. Introduction：stochastic(13)；stiffness(8)；variability(8)；porosity(8)；properties(8)；matrix(7)；pore(7)；pores(7)
- 2. Inter-scale stiffness propagation method with stochastic porosity：porosity(10)；stiffness(6)；field(5)；model(5)；spatial(5)；stochastic(4)；section(4)；local(4)
- 3. Matrix-scale RVE model of stochastic pores：pore(11)；matrix(5)；boolean(5)；defined(5)；pores(4)；model(4)；centers(4)；process(3)
- 4. Statistical features and modeling of porosity field：covariance(21)；local(14)；distance(12)；volumes(12)；porosity(10)；volume(10)；averaging(8)；model(7)
- 5. Statistical feature of matrix-scale effective properties：rve(6)；matrix(6)；pore(6)；realizations(5)；volume(4)；four(4)；rves(4)；pores(4)
- 5.2. FE-based homogenization procedure：stiffness(9)；normal(8)；macroscopic(6)；loading(6)；shear(6)；model(6)；correlation(6)；rve(5)
- 6. Composite-scale FE model with nonintrusive pores：无明显高频项

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 问题句式：Explicitly modeling X at the Y-scale leads to prohibitive computational cost.
- 方法总述：This study proposes an inter-scale method linking X to Y.
- 体积效应句式：The variance decreases with increasing averaging volume following a power-law form.
- 验证句式：The close clustering along the 1:1 line demonstrates predictive consistency.
- 谨慎结论：The correlation remains strongly negative and nearly volume-invariant over the scales investigated.
- 复用模板：先构建可控随机几何输入，再用高保真小尺度模型标定联合统计，最后非侵入地传播到大尺度 FE。

## 15. 引用策略与文献使用

引用密度高，尤其 Introduction。作者不是罗列“孔隙影响材料性能”，而是把文献按方法问题组织：缺陷影响、RVE 尺寸、距离度量、随机场、micro-CT、UD 均匀化。每组文献先承认已有价值，再指出本文补的环节。

引用姿态总体中性：对 micro-CT 是“真实但昂贵”，对随机场是“统计上有用但需要结合孔隙空间相关与体积效应”，对已有缺陷模型是“有启发但对象不同”。gap 和贡献连接自然，因为每类文献都留下一个未闭合接口。

## 16. 审稿人视角风险

- 孔隙形状风险：球形孔隙与 Poisson 独立假设可能不适用于 elongated、coalesced 或制造过程相关孔隙。
- 分布假设风险：条件 Gaussian 映射对尾部和非线性退化的表现需要验证。
- 实验校准不足：文中主要是数值建模，没有真实 CT/实验模量不确定性闭环验证。
- UD 泛化风险：织物、编织、层合板多尺度几何更复杂，非侵入赋值可能需要改造。
- 相关削弱解释：复合尺度负相关幅值从约 0.9 降至约 0.35-0.55，解释合理但可能需要更多机制分析。
- 文本复杂度：公式、符号和表格密集，读者理解成本高，摘要中的“nonintrusive modeling”需要更早给直觉图解。

## 17. 可复用资产

- 论证链资产：随机几何 -> 统计量 -> 均匀化 -> 联合分布 -> 非侵入 FE -> Monte Carlo 验证。
- 图表资产：分布直方图、协方差核、残差诊断、log-log 方差标度、leave-one-out parity plot、相关矩阵距离图、网格独立表。
- 方法资产：把复杂微结构显式建模转化为统计一致的单元属性场。
- 写作资产：每个中间模型都配一个诊断图/表，避免最终 demo 显得黑箱。
- 适用迁移：任何“微观随机缺陷 -> 宏观等效性质不确定性”的问题都可参考此结构。

## 18. 对我写论文的启发

如果论文要提出多尺度方法，不要只展示最终尺度结果。本文非常值得学习的是“逐级验证模型链”：先验证随机输入，再验证协方差，再验证体积标度，再验证联合分布，再验证网格独立，最后才做应用。这种结构能显著降低审稿人对复杂模型的防御心理。

另一个启发是：非侵入式方法必须强调“兼容现有确定性求解器”，这比单纯说“高效”更能打动工程计算期刊。

## 19. 最终浓缩

本文最值得学的是把孔隙几何显式建模的高成本问题转化为统计一致的非侵入刚度场传播问题。最强证据是：孔隙协方差、刚度方差标度、刚度-孔隙负相关和复合材料尺度 self-averaging 都通过表格/图示逐层验证。最大风险是孔隙形貌和 Gaussian 假设偏理想，后续需要真实 CT/实验数据闭环和更复杂复合材料结构验证。
