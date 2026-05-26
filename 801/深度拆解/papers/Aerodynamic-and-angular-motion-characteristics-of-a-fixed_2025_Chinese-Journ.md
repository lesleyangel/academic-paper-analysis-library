# Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates

## 0. 读取说明

本文拆解依据 `801/文本/txt/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.txt` 的全文抽取。该文为 Chinese Journal of Aeronautics 2025 article-in-press/预印版本，txt 中图 1-16、附录网格/时间步验证表和若干公式存在排版错位，流场图、涡结构和曲线细节需要 PDF 图像复核。以下以文本可确认的模型、结果趋势和结论为主。

## 1. 基本信息与论文身份

- 题名：Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates
- 作者：Wen Ji, Chunlin Gong, Chunna Li, Gang Wang
- 期刊：Chinese Journal of Aeronautics, 2025, article in press, DOI 10.1016/j.cja.2025.103988
- 年份：2025
- 领域：双旋弹丸、非定常气动、CFD/RBD 耦合、角运动稳定性、前体旋转控制。
- 论文类型：数值模拟 + 机理分析 + 控制策略启示。
- 研究对象：固定鸭舵双旋弹丸在不同 forebody spinning rates 下的气动特性、角运动特性和稳定机制。
- 方法：基于 unsteady RANS 和滑移网格的固定轴旋转 CFD；HUNS3D 自研并行流场求解器；7-DOF RBD；CFD/RBD 耦合模拟；网格/时间步独立性和 ARL 弹丸验证。
- 主要证据：不同攻角/前体旋速下平均气动力和力矩；Q-criterion 涡结构；截面流线和压力系数；五种前体旋速飞行仿真；复攻角与合力矩投影；自由旋转验证。
- 目标读者：弹道/弹丸气动研究者、CFD/RBD 耦合模拟研究者、双旋弹丸控制系统设计者。

## 2. 摘要与核心信息提取

一句话主张：前体旋转通过改变左右鸭舵有效攻角和翼尖涡非对称性，显著影响双旋弹丸气动和角运动；合力矩在弹轴方向的投影是决定复攻角收敛或发散的关键机制。

摘要中的逻辑很集中：先用 RANS 非定常模拟分析固定轴旋转气动，发现前体旋转导致左右鸭舵有效攻角差异，进而产生非对称翼尖涡；再用 CFD/RBD 耦合分析飞行中的角运动，识别 resultant moment projection onto projectile axis 是主导因素；最后给出控制策略：为提高角运动稳定性，前体应反向旋转或保持静止。

## 3. 选题层深拆

问题来源是 fixed-canard dual-spin projectile 的精度和稳定性矛盾。双旋弹丸利用后体高速旋转提供陀螺稳定，同时通过前体鸭舵修正弹道。但前体/后体相对旋转使气动强非线性、非定常，并耦合横向和法向运动。

作者把问题收束为两个可研究对象：固定轴旋转下前体旋速如何改变气动特性；飞行中前体旋速如何改变角运动稳定性。进一步，文章把角运动机制收束到一个判据：resultant moment projection `M_R · e_Δ` 与复攻角幅值变化之间的关系。

选题价值主要是机理解释和控制设计启示。若能知道哪种前体旋转方向让复攻角收敛，就能为双旋弹丸控制系统提供简单而可操作的设计原则。

## 4. 领域位置与文献版图

文献版图分为三类。

第一类是带鸭舵/修正引信弹丸气动数值研究，说明 CFD 已用于预测 projectile aerodynamic coefficients 和 flow field structures，但多集中在稳态或特定参数。

第二类是旋转弹丸非定常气动研究，包括 sliding mesh、unsteady RANS 与理论公式对比。作者强调高速旋转时理论公式会有明显偏差，说明高保真 CFD 必要。

第三类是双旋弹丸角运动研究，包括气动插值表、线性化角运动微分方程、7-DOF 模型等。作者指出这些方法常忽略非定常气动效应和气动-飞行行为耦合。

本文站位是用 CFD/RBD 同时捕捉非定常气动和角运动，弥补仅靠插值表或线性化方程难以解释机制的问题。

## 5. Gap 制造机制

gap 的核心是“已有研究知道前体旋转影响气动，但不知道它如何通过流场和力矩机制影响角运动稳定性”。

- 机理 gap：生成 yawing moment 和 lateral force 的流动机制仍未充分理解。
- 方法 gap：角运动研究依赖气动插值表或线性化方程，忽略非定常气动与飞行行为耦合。
- 应用 gap：缺少将前体旋速方向和稳定控制策略直接关联的判据。

gap 的说服力较强，因为作者不仅说“需要 CFD/RBD”，还具体指出传统 CFD 难以模拟飞行动态过程，而 CFD/RBD 可以同步求解流场和飞行动力学。

## 6. 创新性判断

作者声明的贡献包括两点：分析不同前体旋速和攻角下鸭舵干扰效应对气动特性的影响；用 CFD/RBD 分析前体旋速对角运动和轨迹特性的影响，并揭示机制。

真实创新属于“非定常气动-角运动耦合机理识别”。最重要的创新不是使用 RANS 或 CFD/RBD 本身，而是提出 `M_R · e_Δ` 作为解释复攻角收敛/发散的关键物理量，并由此导出反向旋转或静止前体有利于稳定的控制策略。

创新强度为中等偏强。方法属于成熟高保真模拟，但机理提炼和控制启示比较清楚。若有风洞或飞行试验验证，创新可信度会更高。

## 7. 论证链条复原

双旋弹丸用于提高命中精度但角运动复杂 → 前体旋速过低/过高都会影响稳定和跟踪 → 现有气动和角运动研究对非定常耦合机制解释不足 → 本文用滑移网格 unsteady RANS 分析固定轴旋转气动 → 发现前体旋转造成左右鸭舵有效攻角差异和翼尖涡非对称 → 这种非对称改变 lateral force/yawing moment → 用 CFD/RBD 模拟不同前体旋速飞行 → 观察复攻角、俯仰/偏航、力矩随旋速变化 → 提出 `M_R · e_Δ` 判据解释角运动稳定性 → 自由旋转仿真进一步验证从发散到收敛的转变 → 得出前体反向旋转或静止可提高稳定性。

论证链条较完整。薄弱环节是缺少实验数据直接验证双旋弹丸流场和角运动，附录用 ARL spinning projectile 验证 CFD/RBD 方法，但对象不是同一构型。

## 8. 方法/理论/模型细拆

方法名称：unsteady CFD + 7-DOF RBD coupled simulation for dual-spin projectile。

输入：弹丸几何、惯量参数、飞行初始状态、Ma/Re/密度、后体旋速、前体旋速、攻角、计算网格和时间步。输出：气动力/力矩系数、流场涡结构、压力系数分布、复攻角和角运动响应。

关键方法：

1. CFD：自研 HUNS3D 并行流场求解器，采用 ALE 形式 unsteady RANS、improved LU-SGS、SA turbulence model，滑移网格处理前体/后体相对运动。
2. RBD：7-DOF 双旋弹丸动力学，包括质心平动、前体/后体滚转和俯仰/偏航角运动。
3. CFD/RBD 耦合：先求初始稳态，再在每个时间步把 CFD 气动力/力矩传给 RBD，更新状态、网格和新流场。
4. 固定轴气动分析：Ma 0.72，Re 8.45×10^5，攻角 0-25°，后体旋速 500π rad/s，前体旋速 -500π 到 500π rad/s。
5. 飞行角运动分析：五种前体旋速 case，观察复攻角和力矩投影；再做前体自由旋转 case 验证。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 前体旋转显著影响横向气动而非纵向气动 | 结果 4.1/Fig. 5 | 前体旋速变化对 lateral force/yawing moment 显著，对 longitudinal characteristics 有限 | 强 | 图 5 曲线细节需 PDF 复核 |
| 前体旋转造成左右鸭舵有效攻角差异 | 摘要/结果 4.1 | Fig. 6/7：不同旋速下左右翼尖涡强度不同 | 中-强 | 流场云图需 PDF 复核 |
| 翼尖涡非对称改变压力分布和偏航力矩 | 结果 4.1/Table 3/Fig. 8 | Cp 特征点 A/B 随旋速变化；前体同向旋转增强 Magnus effect | 强 | 截面位置和色标需 PDF 复核 |
| 同向旋转使角运动幅值增加，稳定性降低 | 结果 4.2/Fig. 10 | forebody 与 aft body 同向时 angle of attack 和 attitude angle 幅值增加 | 强 | 曲线细节需 PDF 复核 |
| 反向旋转或静止有利于复攻角收敛 | 结果 4.2/Fig. 10/13 | `M_R · e_Δ` 为负或非正时复攻角收敛 | 强 | 判据推导较经验化 |
| `M_R · e_Δ` 是影响角运动的关键因素 | 结果 4.2/Fig. 12/16 | 自由旋转中投影变化与复攻角先增后降一致，最终收敛 | 强 | 因果性仍主要由仿真关联支撑 |
| 数值方法具有一定可信度 | Appendix A/B | 网格/时间步独立性；ARL projectile CFD/RBD 验证 | 中 | 缺少本构型实验数据 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Eq. (1) ALE RANS | 给出非定常流场控制方程 | CFD 方法可信 | ALE 处理运动网格 | 公式排版需 PDF 复核 |
| Eq. (2)-(3) 7-DOF RBD | 建立双旋角运动模型 | CFD/RBD 耦合基础 | 前体/后体滚转与俯仰/偏航耦合 | 公式排版需 PDF 复核 |
| Algorithm 1/Fig. 2 耦合流程 | 说明流场与刚体动力学如何交互 | 方法闭环 | CFD loads → RBD states → grid update | 需要 PDF 图像复核 |
| Fig. 3-4 几何与网格 | 定义计算对象 | 数值模型边界 | 6.9 million cells，sliding interface | 需要 PDF 图像复核 |
| Fig. 5 气动力/力矩系数 | 第一核心结果 | 旋速影响横向气动 | 横向力和偏航力矩随前体旋速变化 | 曲线需 PDF 复核 |
| Fig. 6-7 涡结构/压力截面 | 解释气动变化机理 | 有效攻角差异 | 翼尖涡非对称、分离点偏移 | 需要 PDF 图像复核 |
| Table 3 Cp 特征点 | 量化压力不对称 | 压力分布影响力矩 | 左右点 Cp 随 pf 改变 | 可从 txt 确认 |
| Fig. 9-11 飞行状态与力矩 | 连接气动和角运动 | 旋速影响角运动 | 力/矩周期和幅值随旋速变 | 需要 PDF 图像复核 |
| Eq. (6)-(9) 复攻角和投影 | 机制判据 | `M_R · e_Δ` 控制稳定 | 复攻角定义与单位向量 | 公式排版需 PDF 复核 |
| Fig. 14-16 自由旋转验证 | 验证机制 | 复攻角由发散转收敛 | 1.8567 s 前后阶段变化 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Numerical method；3 Computational model；4 Results and discussion；5 Conclusions，并含 Appendix A/B。

结构是典型高保真数值机理论文：Introduction 制造机理 gap；Section 2 说明 CFD、RBD、耦合流程；Section 3 给几何、网格和验证；Section 4 分固定轴气动与飞行角运动两部分；Conclusion 以四条结论收束。

结果节布局非常关键：先在固定轴条件下解释“气动为什么变”，再在飞行耦合中解释“角运动为什么变”。这种先局部机理后系统动态的顺序值得学习。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：7
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 2 Numerical method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Coupled CFD/RBD method | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 9 Integrate the aerodynamic loads to updata aerodynamic forces and moments, | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Geometric configuration | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Computational grid | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Results and discussion                             The parameter settings for the numerical simulations | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 15 Throughout the entire flight, the variation trends of | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 前半段说明双旋弹丸应用和旋速稳定性矛盾，中段综述 CFD 与角运动研究，后段指出插值表/线性化方程不够，最后列贡献。节奏是从工程痛点到方法必要性。

方法段落偏硬技术叙述：每个模块先给求解器和方程，再解释变量。Results 段落图驱动明显，通常先描述图中趋势，再给流动机理解释，再连接到稳定性。

结论四条非常对应正文：气动影响、涡结构机理、力矩投影机制、控制策略。这种“每条结论都是一个 claim”很适合模仿。

## 13. 文笔画像与语言习惯

文笔偏机理型 CFD 论文，常用词包括 unsteady aerodynamic characteristics, angular motion characteristics, forebody spinning rate, wingtip vortex, effective angle of attack, resultant moment projection, complex angle of attack。

语气较强，常用 “significantly affects”, “dominant contributing factor”, “key factor”, 但通常由仿真图支撑。方法部分被动语态多；贡献和结论中主动句较多。

时态：摘要和结论用现在时陈述普遍发现；方法用过去/现在混合；结果解读用现在时。作者常用 “Compared to...”, “Conversely...”, “As the spinning rate increases...” 来组织对比。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：projectile(91)；spinning(84)；aerodynamic(77)；forebody(77)；angular(54)；motion(54)；angle(48)；characteristics(47)；dual-spin(46)；flight(45)；attack(38)；rates(34)；moment(33)；cfd(32)；different(29)；coupled(29)；rad(29)；rbd(27)；chinese(26)；aeronautics(26)
- 高频学术名词：motion(54)；simulation(40)；moment(33)；direction(23)；analysis(22)；method(22)；stability(21)；simulations(16)；velocity(15)；equation(12)；results(11)；pressure(11)；projection(10)；influence(9)；solution(8)；validation(8)
- 高频学术动词：shown(18)；investigate(7)；compared(6)；indicates(5)；simulate(5)；shows(4)；predicted(3)；developed(3)；indicate(2)；formulated(1)；evaluate(1)；demonstrate(1)；investigated(1)；validated(1)；proposed(1)；capture(1)
- 高频形容词：aerodynamic(77)；numerical(36)；moment(33)；different(29)；coefficient(24)；dynamic(20)；lateral(17)；initial(16)；significant(14)；computational(13)；effective(12)；negative(12)；experimental(8)；longitudinal(7)；stationary(7)；resultant(6)
- 高频副词/连接副词：significantly(14)；respectively(7)；gradually(6)；however(4)；conversely(4)；furthermore(3)；accurately(3)；freely(3)；generally(2)；moreover(2)；early(2)；additionally(2)；highly(2)；similarly(2)；simultaneously(2)；therefore(1)
- 高频二词短语：forebody spinning(47)；angular motion(42)；dual-spin projectile(37)；spinning rates(31)；angle attack(29)；cfd rbd(24)；chinese aeronautics(23)；aerodynamic characteristics(21)；spinning rate(20)；coupled cfd(19)；aft body(18)；different forebody(16)；motion characteristics(13)；complex angle(13)；yawing moment(12)；aerodynamic angular(10)
- 高频三词短语：forebody spinning rates(27)；coupled cfd rbd(18)；different forebody spinning(16)；angular motion characteristics(12)；complex angle attack(11)；forebody spinning rate(11)；aerodynamic angular motion(10)；characteristics dual-spin projectile(8)；cfd rbd method(8)；yawing moment coefficient(7)；effective angle attack(6)；fixed-canard dual-spin projectile(5)

**主动、被动与句法**

- 被动语态估计次数：63
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：603
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：161
- 一般过去时线索：20
- 现在完成时线索：6
- 情态动词线索：19
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：aerodynamic(33)；projectile(30)；motion(27)；characteristics(25)；angular(24)；spinning(22)；dual-spin(18)；forebody(15)
- 2. Numerical method：cfd(7)；aerodynamic(6)；moments(6)；coupled(6)；rbd(6)；initial(6)；represents(5)；angle(4)
- 3.1. Geometric configuration：projectile(6)；dual-spin(5)；grid(5)；study(3)；computational(3)；mesh(3)；elements(3)；forebody(2)
- 4. Results and discussion                             The parameter settings for the numerical simulations：forebody(48)；spinning(46)；rad(27)；angle(27)；projectile(22)；rates(21)；coefficient(19)；moment(19)
- 15. Throughout the entire flight, the variation trends of：projectile(30)；aerodynamic(24)；spinning(15)；flight(14)；characteristics(14)；dual-spin(14)；grid(14)；wang(13)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`To enhance hit accuracy, the fixed-canard dual-spin projectile... has been developed.`
- Gap 句式：`the flow mechanisms ... remain not fully understood.`
- 方法句式：`The coupled CFD/RBD method simultaneously solves...`
- 贡献句式：`The main contributions of this work are summarized as follows:`
- 机理句式：`This discrepancy, in turn, gives rise to...`
- 对比句式：`Conversely, when ..., the ...`
- 结果句式：`As the angle of attack increases, the impact ... becomes more significant.`
- 控制启示句式：`Based on these findings, a control strategy is proposed...`

可复用表达：把复杂动态机制浓缩为一个投影量或判据，是机理论文非常有力的写法。

## 15. 引用策略与文献使用

引用策略先按对象后按方法。对象文献包括 spin-stabilized projectiles、canard-controlled projectiles、dual-spin projectiles；方法文献包括 CFD、unsteady RANS、sliding mesh、CFD/RBD、7-DOF 和线性化角运动方程。

作者对前人评价有两类：对 CFD 气动研究表示继承，对插值表和线性化角运动模型指出局限。引用不是为了罗列，而是为了证明“必须用 CFD/RBD 耦合方法研究气动-角运动耦合”。

gap 连接方式是：前人知道前体旋转影响气动，但机制不清；前人研究角运动，但忽略非定常气动耦合；因此本文同时分析流场结构和飞行动态。

## 16. 审稿人视角风险

1. 主要证据来自数值模拟，缺少本构型风洞、自由飞或弹道实验验证。
2. RANS/SA 模型对复杂分离、旋转涡结构的预测精度可能受限。
3. ARL 弹丸验证对象与 fixed-canard dual-spin projectile 不同，只能说明 CFD/RBD 流程可信，不能完全验证本文构型。
4. `M_R · e_Δ` 判据的因果性主要来自仿真相关和物理解释，缺少严格解析推导。
5. 控制策略“反向旋转或静止”未考虑执行机构能耗、响应速度和制导任务需求。
6. 文章为 article in press，版式和细节可能在最终 Version of Record 中调整。

## 17. 可复用资产

- 选题套路：从工程稳定性问题进入，找一个可解释的物理判据连接流场和运动。
- 证据套路：固定轴气动机制 → 飞行耦合响应 → 自由旋转验证，三步递进。
- 图表资产：涡结构和压力截面用于解释力矩变化，复攻角和投影曲线用于解释稳定性。
- 写法资产：用 `Compared to`/`Conversely` 组织旋转方向影响，读者很容易跟踪正负旋速差异。
- 结论资产：把机理直接转成控制策略，是工程 CFD 论文很好的收束方式。

## 18. 对我写论文的启发

如果我写数值机理论文，不能只展示“参数变化导致结果变化”，还要像本文一样找一个中间机制变量：这里是有效攻角差异、翼尖涡不对称、`M_R · e_Δ`。这样论文才从参数扫描变成机理解释。

同时，要尽量补强验证链。本文有网格/时间步独立性和外部构型验证，但如果能增加本构型实验，审稿风险会明显降低。自己的论文也应提前设计“验证对象与研究对象一致性”的证据。

## 19. 最终浓缩

本文的核心贡献是解释 fixed-canard dual-spin projectile 中前体旋速如何通过鸭舵有效攻角差异、非对称翼尖涡和合力矩投影影响角运动稳定性。最强可复用点是将复杂角运动浓缩为 `M_R · e_Δ` 判据，并导出“前体反向旋转或静止更稳定”的控制启示。最大风险是数值模拟主导、实验验证不足。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.txt` 与 `801/文本/metadata/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.12: 0 Table 5 Initial forebody spinning rates （对象/问题/模块）
  - L3 p.8: 0.72 The forebody spinning has a limited impact on （对象/问题/模块）
- L2 p.3: 1. Introduction1 transonic and supersonic regimes （背景/领域定位）
- L2 p.19: 1. Wang Y, Yu JY, Wang XM, et al （对象/问题/模块）
- L2 p.4: 2. Numerical method （方法/模型）
- L2 p.19: 2. Norris J, Hameed A, Economou J, et al （对象/问题/模块）
  - L3 p.4: 2.2. RBD method （方法/模型）
  - L3 p.5: 2.3. Coupled CFD/RBD method （方法/模型）
- L2 p.6: 3. Computational model Fig （方法/模型）
- L2 p.19: 3. Karimi J, Rajabi MR, Sadati SH, et al （对象/问题/模块）
  - L3 p.6: 3.1. Geometric configuration （对象/问题/模块）
  - L3 p.7: 3.2. Computational grid （对象/问题/模块）
- L2 p.7: 4. Results and discussion The parameter settings for the numerical （结果/讨论/验证）
- L2 p.19: 4. Yin JT, Jiang SJ, Hu YW, et al （对象/问题/模块）
  - L3 p.7: 4.1. Aerodynamic characteristics analysis in fixed-axis and the reference area is 0 （参考文献）
  - L3 p.11: 4.2. Aerodynamic and angular motion characteristics Table 4 Initial states for numerical （对象/问题/模块）
- L2 p.1: 5 June 2025 （对象/问题/模块）
- L2 p.17: 5. Conclusions （结论）
- L2 p.19: 5. Zhu Z, Shi L, He C, et al （对象/问题/模块）
- L2 p.19: 6. Wang G, Zhang RT, Lin HZ, et al （对象/问题/模块）
- L2 p.19: 7. Chen SS, Cai FJ, Xiang XH, et al （对象/问题/模块）
- L2 p.6: 8. Calculate the new flow field x (t （对象/问题/模块）
- L2 p.19: 8. Askary F, Soltani MR （对象/问题/模块）
- L2 p.1: 9 September 2025 （对象/问题/模块）
- L2 p.6: 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments, （对象/问题/模块）
- L2 p.19: 9. Zhao XX, Shi JG, Wang ZY, et al （对象/问题/模块）
- L2 p.6: 10. Update the time instant, t （对象/问题/模块）
- L2 p.19: 10. Shen Q, Qiu LL, Pu WY, et al （对象/问题/模块）
- L2 p.19: 11. Pokela R, Kumar R, Vasile JD, et al （对象/问题/模块）
- L2 p.19: 12. Li JM, He GL, Guo HY （对象/问题/模块）
- L2 p.20: 13. Jaiswal R, Kothari M, Abhishek A （对象/问题/模块）
- L2 p.20: 14. Liu XD, Wu XS, Yin JT （对象/问题/模块）
- L2 p.16: 15. Throughout the entire flight, the variation trends of （对象/问题/模块）
- L2 p.20: 15. Yin JT, Lei JM, Wu XS, et al （对象/问题/模块）
- L2 p.17: 16. Both the complex angle of attack and M R （对象/问题/模块）
- L2 p.20: 16. Ji W, Gong CL, Jia XY, et al （对象/问题/模块）
- L2 p.20: 17. Raza A （对象/问题/模块）
- L2 p.20: 18. Yan XY, Yang SX, Zhang C （对象/问题/模块）
- L2 p.1: 19 October 2025 （对象/问题/模块）
- L2 p.20: 19. Hu X, Yang SX （对象/问题/模块）
- L2 p.20: 20. Zhang LP, Chang XH, Ma R, et al （对象/问题/模块）
- L2 p.20: 21. Shi K, Liu MB （对象/问题/模块）
- L2 p.20: 22. Wang C, Ding LB, Feng Y, et al （对象/问题/模块）
- L2 p.20: 23. Lu TY, Wu XS, Lei JM, et al （对象/问题/模块）
- L2 p.20: 24. Sahu J, Burchett B, Gruenwald B （对象/问题/模块）
- L2 p.20: 25. Saini D, Shafei B （对象/问题/模块）
- L2 p.20: 26. Burchett BT, Sahu J, Gruenwald BC （对象/问题/模块）
- L2 p.20: 27. Ernst Z, Drosendahl M, Robertson BE, et al （对象/问题/模块）
- L2 p.20: 28. Yan L, Chang XH, Wang NH, et al （对象/问题/模块）
- L2 p.20: 29. Yan L, Chang XH, Wang NH, et al （对象/问题/模块）
- L2 p.20: 30. Silton SI, Sahu J, Fresconi F （对象/问题/模块）
- L2 p.20: 31. Liu Y, Wang G, Ye ZY （对象/问题/模块）
- L2 p.20: 32. Wang G, Zeng Z, Suo Q （对象/问题/模块）
- L2 p.20: 33. Pang C, Gao ZH, Yang H, et al （对象/问题/模块）
- L2 p.20: 34. Wang G, Ye ZY （对象/问题/模块）
- L2 p.21: 35. Wang G, Jiang YW, Ye ZY （对象/问题/模块）
- L2 p.21: 36. Seve F, Theodoulis S, Wernert P, et al （对象/问题/模块）
- L2 p.21: 37. Jin CH, Wang G, He R, et al （对象/问题/模块）
- L2 p.21: 38. Lin TY, Zhang TY, Wang G （对象/问题/模块）
- L2 p.21: 39. Sahu J （对象/问题/模块）
- L2 p.19: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 0 Table 5 Initial forebody spinning rates | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 0.72 The forebody spinning has a limited impact on | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 1. Introduction1 transonic and supersonic regimes | 3 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 1. Wang Y, Yu JY, Wang XM, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2. Numerical method | 4 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2. Norris J, Hameed A, Economou J, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2. RBD method | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3. Coupled CFD/RBD method | 5 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3. Computational model Fig | 6 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3. Karimi J, Rajabi MR, Sadati SH, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1. Geometric configuration | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2. Computational grid | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4. Results and discussion The parameter settings for the numerical | 7 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4. Yin JT, Jiang SJ, Hu YW, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1. Aerodynamic characteristics analysis in fixed-axis and the reference area is 0 | 7 | 3 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2. Aerodynamic and angular motion characteristics Table 4 Initial states for numerical | 11 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 June 2025 | 1 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5. Conclusions | 17 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5. Zhu Z, Shi L, He C, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6. Wang G, Zhang RT, Lin HZ, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 7. Chen SS, Cai FJ, Xiang XH, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 8. Calculate the new flow field x (t | 6 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 8. Askary F, Soltani MR | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 9 September 2025 | 1 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments, | 6 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 9. Zhao XX, Shi JG, Wang ZY, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 10. Update the time instant, t | 6 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 10. Shen Q, Qiu LL, Pu WY, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 11. Pokela R, Kumar R, Vasile JD, et al | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 12. Li JM, He GL, Guo HY | 19 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 13. Jaiswal R, Kothari M, Abhishek A | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 14. Liu XD, Wu XS, Yin JT | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 15. Throughout the entire flight, the variation trends of | 16 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 15. Yin JT, Lei JM, Wu XS, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 16. Both the complex angle of attack and M R | 17 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 16. Ji W, Gong CL, Jia XY, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 17. Raza A | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 18. Yan XY, Yang SX, Zhang C | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 19 October 2025 | 1 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 19. Hu X, Yang SX | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 20. Zhang LP, Chang XH, Ma R, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 21. Shi K, Liu MB | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 22. Wang C, Ding LB, Feng Y, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 23. Lu TY, Wu XS, Lei JM, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 24. Sahu J, Burchett B, Gruenwald B | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 25. Saini D, Shafei B | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 26. Burchett BT, Sahu J, Gruenwald BC | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 27. Ernst Z, Drosendahl M, Robertson BE, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 28. Yan L, Chang XH, Wang NH, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 29. Yan L, Chang XH, Wang NH, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 30. Silton SI, Sahu J, Fresconi F | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 31. Liu Y, Wang G, Ye ZY | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 32. Wang G, Zeng Z, Suo Q | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 33. Pang C, Gao ZH, Yang H, et al | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 34. Wang G, Ye ZY | 20 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 35. Wang G, Jiang YW, Ye ZY | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 36. Seve F, Theodoulis S, Wernert P, et al | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 37. Jin CH, Wang G, He R, et al | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 38. Lin TY, Zhang TY, Wang G | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 39. Sahu J | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 19 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 本文对固定鸭翼双旋弹丸进行了数值研究，探讨其气动性能和
> 不同前体旋转速率下的角运动特性。基于雷诺平均纳维-斯托克斯
> 方程，对双自旋弹丸绕其纵轴旋转的非定常模拟进行
> 研究其空气动力特性。结果表明，前体的旋转引起了差异
> 左右鸭翼之间的有效迎角。这种差异反过来又导致了不对称
> 翼尖涡结构，最终对双翼飞机的气动特性产生重大影响
> 旋转弹丸。此外，基于耦合计算流体动力学和刚体动力学方法，
> 研究了双自旋弹丸飞行过程中的气动和角运动特性，并
> 分析了角运动的机理。结果表明，前体旋转显着影响
> 弹丸的空气动力特性和角运动特性。其中底层
> 机制中，合力在弹丸轴上的投影被确定为主要贡献
> 因素。
> 
> 非正投影会导致复杂攻角的收敛，从而增强稳定性
> 旋转的射弹。基于这些发现，提出了一种控制策略：为了提高角运动稳定性，
> 前体要么被驱动向相反方向旋转，要么保持静止状态。关键词：双旋射弹；气动特性非定常；角运动；耦合计算流体动力学
> 和刚体动力学
> 
> *通讯作者。邮箱地址：chunnali@nwpu.edu.cn
> 
> 航空学报·2·
> 
> 1. 简介1 跨音速和超音速流态。 Liu 等人 14 使用
> 滑动网格方法研究的影响
> 自旋稳定弹在后体旋转速度、攻角和马赫数方面得到了广泛的应用
> 近年来，但它们的攻击精度仍然有限。1 数字，关于时间平均空气动力学
> 为了提高命中精度，双旋转弹丸的固定鸭翼双旋转特性通过
> 射弹，设计为一种轨迹校正数值模拟，揭示了底层的流动
> 弹丸，已经研制出来。它利用陀螺仪机制。 Yin等人15比较了空气动力学
> 使用非定常旋转射弹的尾部系数高速旋转所产生的稳定性
> 机身保持飞行稳定。
> 
> 此外，它还可以用雷诺平均纳维斯托克斯 (RANS) 方程表示
> 通过控制理论得到的气动系数的旋转来修正轨迹
> 前鸭翼，从而提高攻击精度。2,3配方，在高处发现显着差异
> 旋转速率，这表明理论
> 由于尾体高速旋转，该公式计算存在局限性
> 双旋射弹表现出高度非线性和空气动力学特性。综上所述，前言
> 不稳定的空气动力学特性以及旋转会显着影响空气动力学
> 横向运动与双旋转射弹特性之间的强耦合。然而，
> 法向轴。2,4 弹丸的飞行涉及耦合流动机制，产生偏航力矩和
> 角运动——自旋、进动和章动——可能导致飞行不稳定的侧向力仍然存在
> 导致高度复杂的动态行为。5 当未完全理解时。弹丸的旋转速度相当低，可能会导致
> 陀螺仪稳定性不足，从而损害了大多数关于角运动的研究
> 飞行稳定性。
> 
> 相反，当自旋速率太大时，双自旋弹丸的特性依赖于
> 高，可能会降低轨迹跟踪稳定性，空气动力插值表，16,17 忽略
> 导致弹丸受到过大的非定常空气动力效应。同样，研究
> 飞行过程中的迎角会对角运动产生负面影响，通常使用线性化角运动
> 其角运动的稳定性。6 因此，深入的微分方程，18,19 引入了过多的
> 研究空气动力学和角运动的假设和简化。此外，当
> 双旋射弹的特性是必要的。埃罗德

### 20.5 结论完整摘录（本地证据）

结论章节识别：5. Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项研究中，我们通过数值模拟研究了固定鸭翼双旋射弹在不同前体旋转速率下的空气动力和角运动特性。通过非定常CFD仿真分析了双自旋弹丸绕定轴旋转的非定常气动特性。此外，还进行了CFD/RBD耦合仿真，研究了前体分别以固定速率和自由旋转时的角运动和气动特性。这项工作的主要结论总结如下：
> 
> (1)前体自旋影响双自旋弹丸的横向气动特性。前体反方向旋转速率的增加导致侧向力系数更高，同时降低了偏航力矩系数。随着迎角增大，前体旋转对侧向力和偏航力矩系数的影响变得更加显着。 (2)前体旋转时，左右鸭翼的有效迎角不同，导致有效迎角较大一侧涡流较强。这导致翼尖涡结构不对称，并改变其空气动力特性。
> 
> (3)垂直于体轴的力矩在弹体轴上的投影是影响其角运动的关键因素。当投影大于零时，角运动的幅度逐渐增大。 (4)双自旋弹丸的后体和前体同向旋转时，角运动幅度增大，稳定性降低。相比之下，采用前体向相反方向旋转或保持静止的控制策略可以减少投射到弹丸轴上的力矩，从而增强其角运动的稳定性。致谢
> 
> 该研究得到国家自然科学基金项目（No. U2141254）的资助。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed. However, the normal axes.2,4 The projectile’s flight involves coupled flow mechanisms generating yawing moment and angular motions—spin, precession, and nutation— lateral force, which can lead to flight instability, remain resulting in highly complex dynamic behavior.5 When not fully understood. the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising Most studies carried out on angular motion flight stability.
- 本文解决方式：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
- 学术/工程增量：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：0
- Introduction 引用簇数量（估计）：0
- References 条目数（解析）：39
- 可识别年份条目数：45
- 近五年/近年文献（2021+）数量：27
- 经典文献（2010年前）数量：2
- 同刊引用数量（按 subject 粗略匹配）：3
- 高频来源期刊（粗略）：Chinese Journal of Aeronautics(3)
- 引用簇样例：未识别

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- 1. Wang Y, Yu JY, Wang XM, et al. A guidance and control design with reduced information for a dual-spin stabilized projectile. Def Technol 2024;33:494–505. Chinese Journal of Aeronautics · 18 ·
- 2. Norris J, Hameed A, Economou J, et al. A review of dual-spin projectile stability. Def Technol 2020;16(1):1– 9.
- 3. Karimi J, Rajabi MR, Sadati SH, et al. Multidisciplinary design optimization of a dual-spin guided vehicle. Def Technol 2024;37:133–48.
- 4. Yin JT, Jiang SJ, Hu YW, et al. Aerodynamic characteristics and dynamic stability of coning motion of spinning finned projectile in supersonic conditions. Aerospace 2025;12(3):225.
- 5. Zhu Z, Shi L, He C, et al. Construction and kinematic performance analysis of a suspension support for wind tunnel tests of spinning projectiles based on wire-driven parallel robot with kinematic redundancy. Chin J Aeronaut 2024;37(12):404–15.
- 6. Wang G, Zhang RT, Lin HZ, et al. Study on influence of canard rotation speed on following stability of dual-spin projectile. Aero Weapon 2024;31(2):71–8 [Chinese].
- 7. Chen SS, Cai FJ, Xiang XH, et al. A low-diffusion robust flux splitting scheme towards wide-ranging Mach number flows. Chin J Aeronaut 2021;34(5):628–41.
- 8. Askary F, Soltani MR. Effects of Mach numbers on Magnus induced surface pressure. Chin J Aeronaut 2020;33(12):3058–72.
- 9. Zhao XX, Shi JG, Wang ZY, et al. Nonlinear aerodynamic modeling and analysis on body of fixed canard dual-spin projectiles. Proceedings of the 2nd international conference on mechanical system dynamics. Singapore: Springer Nature Singapore, 2024:3759–74.
- 10. Shen Q, Qiu LL, Pu WY, et al. Aerodynamic characteristics and characterization of the double spin structure of two-dimensional correction high-spin projectile. Trans Beijing Inst Technol 2024;44(4):359–68 [Chinese].
- 11. Pokela R, Kumar R, Vasile JD, et al. Aerodynamic characterization of a generic high-speed projectile configuration. J Spacecr Rockets 2024;61(3):741–56.
- 12. Li JM, He GL, Guo HY. A study on the aerodynamic characteristics for a two-dimensional trajectory correction fuze. Appl Mech Mater 2014;703:370–5.

### 20.9 常用词、词类、语态与时态

- 高频词：projectile(79)；spinning(79)；forebody(77)；aerodynamic(68)；angular(53)；motion(50)；angle(48)；fig(45)；characteristics(41)；dual-spin(40)；attack(38)；flight(35)；rates(34)；moment(33)；cfd(31)；rad(29)；coupled(26)；body(26)；rbd(26)；journal(24)
- 高频名词化/学术名词：motion(50)；characteristics(41)；moment(33)；aeronautics(23)；direction(23)；stability(19)；velocity(15)；simulation(12)；pressure(11)；projection(10)；dynamics(9)；influence(8)；equation(6)；reference(5)；version(5)
- 高频学术动词：presented(12)；compared(6)；developed(3)；predicted(3)；indicate(2)；demonstrate(1)；validated(1)
- 高频形容词：aerodynamic(68)；moment(33)；journal(24)；coefficient(24)；table(21)；lateral(17)；initial(16)；numerical(13)；negative(12)；computational(10)；significant(7)；stationary(7)；longitudinal(6)；effective(6)；resultant(6)
- 高频副词：significantly(7)；respectively(7)；gradually(6)；conversely(4)；only(4)；accurately(3)；freely(3)；early(2)；additionally(2)；highly(2)；similarly(2)；simultaneously(2)；apply(1)；ultimately(1)；widely(1)
- 高频二词短语：forebody spinning(47)；angular motion(42)；dual-spin projectile(34)；spinning rates(31)；angle attack(29)；cfd rbd(23)；chinese journal(20)；journal aeronautics(20)；spinning rate(20)；aerodynamic characteristics(19)；coupled cfd(19)；aft body(18)
- 高频三词短语：forebody spinning rates(27)；chinese journal aeronautics(20)；coupled cfd rbd(18)；page chinese journal(17)；angular motion characteristics(12)；complex angle attack(11)；forebody spinning rate(11)；aerodynamic angular motion(10)；characteristics dual-spin projectile(7)；yawing moment coefficient(7)；effective angle attack(6)；fixed-canard dual-spin projectile(5)
- 被动语态估计：59；`we + 动作动词` 主动句估计：0
- 一般现在时线索：144；一般过去时线索：223；现在完成时线索：1；情态动词线索：17

章节词频：

- Abstract: projectile(17)；aerodynamic(15)；angular(12)；motion(12)；characteristics(12)；spinning(11)；dual-spin(10)；stability(8)
- Conclusion: forebody(8)；angular(6)；motion(6)；projectile(6)；spinning(6)；aerodynamic(5)；characteristics(5)；axis(4)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  可迁移模板：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句/结构：Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
  可迁移模板：Liu et al.Xused the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.Xnumber, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
- 原句/结构：However, the normal axes.2,4 The projectile’s flight involves coupled flow mechanisms generating yawing moment and angular motions—spin, precession, and nutation— lateral force, which can lead to flight instability, remain resulting in highly complex dynamic behavior.5 When not fully understood. the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising Most studies carried out on angular motion flight stability.
  可迁移模板：However, the normal axes.X,XThe projectile’s flight involves coupled flow mechanisms generating yawing moment and angular motions—spin, precession, and nutation— lateral force, which can lead to flight instability, remain resulting in highly complex dynamic behavior.XWhen not fully understood. the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising Most studies carried out on angular motion flight stability.
#### 方法句
- 原句/结构：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  可迁移模板：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句/结构：Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
  可迁移模板：Liu et al.Xused the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.Xnumber, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
- 原句/结构：Additionally, it can Reynolds-Average Navier-Stokes (RANS) equation with correct the trajectory by controlling the rotation of the the aerodynamic coefficients obtained from theoretical front canard, thereby improving attack precision.2,3 formulations, finding significant differences at high spinning rates, which indicates that the theoretical Due to the high-speed rotation of the aft body, the formulation method has limitations in calculating dual-spin projectile exhibits highly nonlinear and aerodynamic characteristics.
  可迁移模板：Additionally, it can Reynolds-Average Navier-Stokes (METHOD) equation with correct the trajectory by controlling the rotation of the the aerodynamic coefficients obtained from theoretical front canard, thereby improving attack precision.X,Xformulations, finding significant differences at high spinning rates, which indicates that the theoretical Due to the high-speed rotation of the aft body, the formulation method has limitations in calculating dual-spin projectile exhibits highly nonlinear and aerodynamic characteristics.
#### 结果句
- 原句/结构：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
  可迁移模板：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
- 原句/结构：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
  可迁移模板：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
- 原句/结构：Additionally, it can Reynolds-Average Navier-Stokes (RANS) equation with correct the trajectory by controlling the rotation of the the aerodynamic coefficients obtained from theoretical front canard, thereby improving attack precision.2,3 formulations, finding significant differences at high spinning rates, which indicates that the theoretical Due to the high-speed rotation of the aft body, the formulation method has limitations in calculating dual-spin projectile exhibits highly nonlinear and aerodynamic characteristics.
  可迁移模板：Additionally, it can Reynolds-Average Navier-Stokes (METHOD) equation with correct the trajectory by controlling the rotation of the the aerodynamic coefficients obtained from theoretical front canard, thereby improving attack precision.X,Xformulations, finding significant differences at high spinning rates, which indicates that the theoretical Due to the high-speed rotation of the aft body, the formulation method has limitations in calculating dual-spin projectile exhibits highly nonlinear and aerodynamic characteristics.
#### 贡献句
- 原句/结构：Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
  可迁移模板：Liu et al.Xused the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.Xnumber, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
#### 限制/边界句
- 原句/结构：Liu et al.14 used the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.1 number, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
  可迁移模板：Liu et al.Xused the sliding mesh approach to study the influence of the Spin-stabilized projectiles have been widely deployed in spinning rate of the aft body, angle of attack, and Mach recent years, but their attack precision remains limited.Xnumber, on the time-averaged aerodynamic To enhance hit accuracy, the fixed-canard dual-spin characteristics of a dual-spin projectile through projectile, designed as a type of trajectory-corrected numerical simulation, revealing the underlying flow projectile, has been developed.
- 原句/结构：However, the normal axes.2,4 The projectile’s flight involves coupled flow mechanisms generating yawing moment and angular motions—spin, precession, and nutation— lateral force, which can lead to flight instability, remain resulting in highly complex dynamic behavior.5 When not fully understood. the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising Most studies carried out on angular motion flight stability.
  可迁移模板：However, the normal axes.X,XThe projectile’s flight involves coupled flow mechanisms generating yawing moment and angular motions—spin, precession, and nutation— lateral force, which can lead to flight instability, remain resulting in highly complex dynamic behavior.XWhen not fully understood. the projectile’s spinning rate is quite low, it may lead to insufficient gyroscopic stability, thereby compromising Most studies carried out on angular motion flight stability.
- 原句/结构：Conversely, when the spinning rate is too characteristics of dual-spin projectiles rely on high, it may reduce trajectory-following stability, aerodynamic interpolation tables,16,17 neglecting the causing the projectile to experience an excessively large unsteady aerodynamic effects.
  可迁移模板：Conversely, when the spinning rate is too characteristics of dual-spin projectiles rely on high, it may reduce trajectory-following stability, aerodynamic interpolation tables,X,Xneglecting the causing the projectile to experience an excessively large unsteady aerodynamic effects.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
