# Unveiling scaling laws for wrinkling in compressed fiber-reinforced bilayers at any elastic mismatch

## 0. 读取说明
- 源 PDF：`jmps/文献/Unveiling-scaling-laws-for-wrinkling-in-compress_2026_Journal-of-the-Mechani.pdf`
- 源 TXT：`jmps/文本/txt/Unveiling-scaling-laws-for-wrinkling-in-compress_2026_Journal-of-the-Mechani.txt`
- 辅助参照：上一轮标准拆解用于核对主线，本文件重新按深度模板展开。
- 是否需要结合 PDF 图像核查：需要。TXT 可读到图注、参数趋势、标度律叙事和结论，但相图、极坐标图、误差图、regime transition 曲线必须看 PDF。
- 本文类型：理论标度律 + 渐近分析 + 参数图谱 + 3D 模型对照。没有直接实验验证。
- 阅读覆盖：摘要、Introduction、small-to-finite strain analytical model、film-mediated direct scaling laws、substrate-mediated dual scaling laws、Conclusions。

## 1. 基本信息与论文身份
- 题名：Unveiling scaling laws for wrinkling in compressed fiber-reinforced bilayers at any elastic mismatch
- 作者/机构：Andrea Mirandola, Angelo R. Carotenuto, Arsenio Cutolo, Stefania Palumbo, Massimiliano Fraldi, Luca Deseri。完整机构需以 PDF 为准。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 212 (2026) 106564。
- DOI：10.1016/j.jmps.2026.106564
- 关键词：Scaling laws for wrinkling；Wrinkling of fiber-reinforced bilayers；Regime-transition in wrinkling；Symmetry-breaking in wrinkling；Wrinkling instabilities。
- 研究对象：受压纤维增强基底-薄膜双层体系的起皱临界应变和临界波数，覆盖高到中低弹性失配。
- 研究尺度：连续体有限弹性 + 薄板/半无限基底分岔尺度；关注 onset，不追踪后皱折。
- 方法类型：Standard Reinforcing Model、small-on-large 分岔、可伸展弯曲薄板、Puiseux 渐近展开、direct/dual scaling laws、3D SRM/OGH 对比。
- 证据类型：临界应变/波数参数图、对称破缺、transition mismatch、direct 与 dual 标度律误差、板模型与 3D 模型对照。
- 目标读者：软材料起皱、纤维增强生物材料、薄膜-基底不稳定性、渐近分析和设计标度律读者。
- JMPS 风格定位：把复杂参数空间压缩成“regime + threshold + scaling law”的理论资产，是 JMPS 中很典型的可迁移理论写法。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先从自然和工程系统中的起皱应用切入；再指出各向同性 bilayer 标度律成熟，而纤维增强 bilayer 在任意失配下缺少关系；随后说明用小到有限应变分岔和渐近展开推导；最后给出 film-mediated 与 substrate-governed 两个 regime、阈值和标度律。
- 背景句承担什么：建立 wrinkling 的广泛物理和生物重要性。
- gap 句承担什么：将成熟的各向同性高失配理论与欠缺的纤维增强任意失配理论对比。
- 方法句承担什么：说明模型由可伸展薄板 film 和有限弹性 fiber-reinforced substrate 组成，并使用渐近展开。
- 结果句承担什么：给出两套标度律和 regime transition，而不是单一公式。
- 意义句承担什么：为复杂纤维增强体系提供可判断适用域的设计关系。
- 一句话主张：纤维增强双层起皱不能用一套高失配公式概括，而应根据 transition mismatch 判断 film-mediated direct scaling 或 substrate-governed dual scaling。
- 3-5 个核心关键词：wrinkling onset；elastic mismatch；fiber reinforcement；direct scaling laws；dual scaling laws。

## 3. 选题层深拆
- 问题来源：各向同性薄膜-基底起皱已有经典标度律，但真实生物组织和工程软材料常含纤维增强、各向异性、纤维角度和有限应变；传统高失配公式不能解释中低失配和基底主导。
- 问题为什么重要：脑回、血管、叶片、组织生长、软传感和可编程表面都可能由纤维增强双层起皱控制。没有标度律，设计和解释只能依赖数值扫描。
- 问题为什么现在值得做：已有 finite elasticity 与 SRM/OGH 本构可表示纤维基底；作者前期研究已涉及小应变纤维增强起皱；渐近工具可系统推导而非经验拟合幂律。
- 问题边界：平面应变、完美粘结、半无限基底、起皱 onset；主要 SRM，OGH 用于对照；不包含实验验证和后屈曲形态。
- 选题的 JMPS 味道：从经典标度律出发，扩展到更复杂本构和更宽参数域，输出可用的阈值和公式。
- 选题可迁移性：任何复杂参数不稳定性问题都可学习：先识别旧标度律失效区，再构造 regime map。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：经典各向同性 bilayer wrinkling；高弹性失配标度律；有限应变/非线性基底；纤维增强和生物组织 wrinkling；近年特定纤维增强模型。
- 主要研究流派/方法路线：Biot/Allen/Cao-Hutchinson 类经典理论；small-on-large 分岔；薄板-基底降维模型；3D finite elasticity；生物材料 OGH/SRM 本构。
- 每类研究解决了什么：经典理论给高失配公式；3D 有限弹性能求精确 onset；纤维增强本构能表示角度和分散；薄板模型便于解析标度。
- 每类研究留下什么不足：高失配公式不适用所有 mismatch；3D 模型难给透明标度律；纤维增强研究缺统一 direct/dual regime 判据。
- 本文站在哪条线上：经典 bilayer 标度律之后，纤维增强有限弹性分岔之前/之中，目标是把数值可见趋势变成公式和阈值。
- 最接近前人工作：各向同性起皱标度律和作者前期 fiber-reinforced bilayer wrinkling 研究。
- 是否公平处理前人：总体公平。作者承认经典公式的有效域，并通过参数域扩展说明本文必要性。

## 5. Gap 制造机制
- 明示 gap：fiber-reinforced bilayers 在任意 elastic mismatch 下的临界应变和波数标度律仍 underexplored。
- 隐含 gap：旧公式不仅缺纤维项，还缺 regime 判断；中低失配时控制机制从 film 转向 substrate，变量应重新缩放。
- gap 类型：理论标度 gap + regime 分类 gap + 设计图谱 gap。
- gap 证据来自哪里：Introduction 对比各向同性高失配理论；Fig. 2-3 展示纤维角度和 mismatch 造成对称破缺；后文 direct laws 在低失配下失效，促成 dual laws。
- gap 是否足够窄：较宽但被“onset scaling laws at any mismatch”集中起来，边界清楚。
- gap 是否足够重要：重要。没有 regime 判据，工程使用者可能把 direct formula 用到错误区间。
- 如果我是审稿人会如何追问：SRM 能否代表真实纤维材料？OGH 对比覆盖是否充分？dual laws 对波数精度较弱如何解释？缺少实验是否削弱应用 claim？

## 6. 创新性判断
- 作者声称的贡献：推导适用于任意 mismatch 的起皱标度律；识别 film-mediated 和 substrate-governed regimes；给出 transition mismatch；揭示 symmetry breaking 和 isotropization。
- 我判断的真实创新：将“一个公式不够用”升级为“先判 regime 再用公式”的理论框架，并用 Puiseux 展开系统推导 direct/dual scaling。
- 创新类型：渐近理论创新、regime map、设计公式。
- 创新强度：强。尤其是 transition threshold 使理论可操作。
- 创新必要性：必要。纤维增强、角度和 elastic mismatch 共同作用会破坏经典幂律。
- 创新与证据匹配度：理论推导和 3D 模型对照支撑强；生物应用外推和真实材料适用性证据较弱。
- 容易被挑战的创新点：supplementary 中推导依赖大；dual regime 波数预测精度；压缩纤维是否承载的物理假设。

## 7. 论证链条复原
背景：起皱是薄膜-基底失配下常见分岔，经典各向同性高失配标度律已成熟。

文献：已有理论主要针对 isotropic bilayers 或特定极限；纤维增强 bilayers 的任意 mismatch relations 缺失。

gap：当纤维角度、分散、刚度比和中低 mismatch 同时存在，旧标度律无法判断临界应变/波数。

问题：如何推导覆盖 small-to-finite strain 和 any elastic mismatch 的 scaling laws？

方法：建立 SRM fiber-reinforced substrate 与 extensible bending plate film；写分岔条件和最优波数条件；用 Puiseux 展开推导 direct laws；发现低失配 substrate-governed regime 后改变量纲得到 dual laws。

证据：参数图显示对称破缺；3D SRM/OGH 与板模型对照；direct laws 在高失配准确；transition mismatch 图给 regime 判据；dual laws 改善低失配。

发现：存在 film-mediated 和 substrate-governed 两个 regime；纤维可导致角度对称破缺和基底各向同性化；阈值 `rho*_ML` 决定公式选择。

机制：高失配时 film bending 与 substrate foundation 平衡；低失配时纤维增强基底自身支配临界，导致变量缩放对偶化。

意义：为纤维增强软材料起皱设计提供简化公式和适用域。

## 8. 方法/理论/模型细拆
- 方法总框架：将 film 降维为可伸展弯曲板，将 substrate 作为含两族 `±theta` 纤维的有限弹性半空间；在预压缩状态上做 small-on-large 扰动，求临界条件；通过渐近展开提取幂律。
- 关键概念：elastic mismatch；fiber dispersion；Standard Reinforcing Model；symmetry breaking；film-mediated regime；substrate-governed regime；transition mismatch；direct/dual scaling。
- 关键变量/参数：matrix/layer mismatch `rho_ML`、fiber/matrix stiffness `rho_FM`、fiber angle `theta`、dispersion `kappa`、critical strain `epsilon_cr`、critical wavenumber `kh_cr`、transition threshold `rho*_ML`。
- 核心假设：平面应变；完美粘结；基底远厚于 film；纤维在压缩时是否贡献需区分；SRM 可作为主本构；onset 前均匀变形。
- 边界条件：film-substrate 界面位移和牵引连续，基底远场衰减；临界扰动为周期性 wrinkle。
- 方法步骤：1. 建立双层几何和本构；2. 推导分岔方程；3. 在 high mismatch 下做 direct Puiseux expansion；4. 与 3D 模型对比；5. 识别 transition mismatch；6. 在 substrate-governed 区域重写 dual laws；7. 给误差和适用域图。
- 复现信息：主要公式和参数图充足，但完整推导可能依赖补充材料；复现需 PDF 和 supplementary。
- 方法复杂度是否合理：合理。目标是解析标度律，渐近复杂度与参数空间复杂度匹配。
- 方法与 gap 的对应关系：gap 是缺任意 mismatch 下公式和判据，方法直接输出 direct/dual laws 和 threshold。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 纤维增强 bilayer 起皱存在不同于各向同性的角度依赖和对称破缺 | Introduction、Section 2-3 | Fig. 2-3 极坐标/参数图 | 数值参数图 | 中强 | 需 PDF 核查图形 |
| high mismatch 下 direct scaling laws 有效 | Section 3 | Puiseux 推导、与 3D SRM/OGH 对比、误差图 | 渐近 + 数值对比 | 强 | 有效域需阈值限定 |
| 任意 mismatch 不能用 direct laws 一套公式 | Section 4 | transition mismatch、direct law 误差增大 | 参数图 + 机制分析 | 强 | 阈值定义依赖模型 |
| 存在 substrate-governed dual regime | Section 4 | dual scaling laws、Fig. 10 等 regime 图 | 渐近 + 对比 | 中强 | 波数预测精度较弱 |
| `rho*_ML` 可作为公式选择判据 | Section 4 | transition mismatch contour | 理论阈值 + 图谱 | 中强 | 真实材料参数估计误差影响判据 |
| 3D 模型对照支持薄板降维模型 | Section 3-4 | plate vs 3D SRM/OGH 曲线/误差 | 数值对比 | 中强 | 无实验验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 双层几何和纤维方向示意 | 模型设定 | 降低 SRM 和扰动理解成本 | 是 |
| 分岔方程与最优波数条件 | 理论核心 | onset 判定 | 连接本构与临界量 | 否，需核对排版 |
| Fig. 2 | 高到中 mismatch 的对称破缺 | 纤维角度影响临界 | 可视化新现象 | 是 |
| Fig. 3 | 参数 `rho_FM/kappa/rho_ML` 影响 | 本构参数改变临界量 | 展示复杂参数空间 | 是 |
| Fig. 4-5 | plate vs 3D onset | 降维模型可靠 | 支撑使用解析板模型 | 是 |
| Fig. 6-7 | direct laws 与 3D 对比 | direct scaling 有效域 | 给误差证据 | 是 |
| Fig. 8 | transition mismatch contour | regime 判据 | 全文核心设计图谱之一 | 是 |
| Fig. 10-12 | dual laws 和 regime transition | substrate-governed regime | 证明需要第二套公式 | 是 |

图表顺序服务论证的方式：先给模型图，再展示旧直觉无法解释的角度/对称破缺，随后证明简化模型可靠，接着给 direct laws，最后指出其失效并引入 transition/dual laws。顺序是“旧公式扩展 -> 发现失效 -> 建立双 regime”。

## 11. 章节结构与篇章布局
- Abstract：应用背景、gap、方法、两套 law、transition threshold，一次性说明贡献。
- Introduction：非常长，先铺 wrinkling 广泛性，再进入经典标度律和 fiber-reinforced 缺口。
- Related Work/Background：Introduction 承担文献版图，按领域和公式发展组织。
- Method/Theory/Model：第 2 节建模，是后续所有渐近的地基。
- Results：第 3 节 film-mediated direct laws，第 4 节 substrate-mediated dual laws。
- Discussion：结果章节内嵌讨论，尤其是 validity、误差和物理解释。
- Conclusion：用编号式主结论概括，适合公式密集论文。
- 章节之间如何过渡：从模型到 direct laws，再由 direct laws 的有效域限制过渡到 dual laws。
- 哪一节最值得模仿：第 4 节。它不是硬扩展公式，而是在失效处重构变量和 regime。
- 哪一节可能存在结构风险：推导依赖补充材料，正文读者可能只能接受结论而难以审计全部细节。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Unveiling-scaling-laws-for-wrinkling-in-compress_2026_Journal-of-the-Mechani.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：3
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：结论/展望型, 背景/引言型, 问题/机制型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Fiber-reinforced substrate-mediated wrinkling: isotropization and dual scaling laws | 问题/机制型 | 围绕变量关系或机制问题组织读者预期 | 高 | 是 | 保留具体变量/对象 |
| 5 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：广泛现象 -> 经典公式 -> 纤维增强复杂性 -> 本文问题 -> 本文贡献。
- Method 段落推进：几何/本构定义 -> 扰动形式 -> 界面条件 -> 分岔方程。
- Results 段落推进：先给趋势图或公式，再解释参数作用，最后给误差或适用域。
- Discussion/Conclusion 段落推进：把许多公式压缩成“何时用 direct，何时用 dual”。
- 常见段落开头方式：`We now consider...`；`The comparison shows...`；`This suggests the occurrence of two regimes...`。
- 常见段落收束方式：以 threshold、validity range 或 deviation from 3D model 收束。
- 可复用段落模板：经典标度律 -> 新参数导致偏离 -> 渐近展开给修正 -> 3D 模型检验误差 -> 用阈值定义适用域。

## 13. 文笔画像与语言习惯
- 整体语气：理论雄心强，常用 unified、full spectrum、any mismatch 等高定位。
- claim 强度：对公式推导较强，对实验/生物应用较谨慎。
- 谨慎表达：`for the sake of illustration`、`within the range`、`with less accuracy`、`as long as`。
- 问题表达：`widely underexplored`、`no such relations exist`、`regime change is expected`。
- 贡献表达：`we derive`、`we identify`、`we provide`、`we demonstrate`。
- 机制表达：`film-mediated`、`substrate-governed`、`symmetry breaking`、`isotropization`、`transition mismatch`。
- 对比表达：`relative to the neo-Hookean case`、`compared with the 3D formulation`。
- 限定边界表达：admissibility of compressed fibers、SRM/OGH comparison、onset only。
- 术语密度：很高，参数符号和公式多。
- 长句/短句习惯：Introduction 长句多，Conclusion 以编号结论降低复杂度。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：strain(125)；wrinkling(116)；critical(110)；scaling(109)；mismatch(86)；laws(85)；substrate(82)；bilayers(77)；bers(76)；wavenumber(70)；onset(69)；one(61)；model(59)；case(59)；supplementary(58)；elastic(55)；obtained(55)；bilayer(54)；ber(52)；ber-reinforced(49)
- 高频学术名词：strain(125)；analysis(82)；transition(76)；model(59)；material(46)；section(37)；condition(36)；solution(36)；hence(24)；deformation(22)；behavior(21)；reinforcement(18)；bifurcation(17)；equation(16)；ness(16)；parameters(15)
- 高频学术动词：shown(26)；shows(16)；derived(13)；show(9)；evaluated(5)；capture(4)；indicates(4)；proposed(3)；compared(3)；developed(3)；derive(2)；solved(2)；compare(2)；predicted(2)；investigated(2)；suggest(1)
- 高频形容词：critical(220)；elastic(110)；supplementary(58)；material(46)；asymptotic(38)；isotropic(30)；relative(29)；dual(22)；high(19)；small(18)；reinforcement(18)；erent(16)；biological(15)；present(15)；anisotropic(14)；homogeneous(14)
- 高频副词/连接副词：fully(25)；namely(15)；therefore(12)；furthermore(11)；family(11)；analytically(10)；moreover(9)；directly(9)；approximately(8)；highly(8)；slightly(8)；however(7)；respectively(7)；finally(7)；obviously(7)；cantly(6)
- 高频二词短语：scaling laws(76)；critical strain(72)；supplementary material(35)；elastic mismatch(31)；onset wrinkling(29)；ber-reinforced bilayers(26)；plate model(25)；scaling law(24)；strain wavenumber(19)；ber angle(17)；cos cos(17)；sti ness(16)；wrinkling onset(14)；elastic mismatches(13)；wrinkling features(13)；worth noting(13)
- 高频三词短语：critical strain wavenumber(18)；cos cos cos(12)；italian ministry university(9)；ministry university research(9)；dual scaling laws(8)；scaling laws obtained(7)；university research mur(7)；scaling laws critical(6)；obtained scaling laws(6)；explicit scaling law(6)；writing review editing(6)；scaling laws wrinkling(5)

**主动、被动与句法**

- 被动语态估计次数：240
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：1376
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：465
- 一般过去时线索：96
- 现在完成时线索：40
- 情态动词线索：86
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：wrinkling(11)；scaling(6)；bilayers(6)；laws(5)；elastic(5)；ber-reinforced(4)；mismatches(4)；university(3)
- 1. Introduction：wrinkling(80)；strain(74)；critical(68)；scaling(65)；substrate(54)；mismatch(52)；laws(52)；bilayers(48)
- 4. Fiber-reinforced substrate-mediated wrinkling: isotropization and dual scaling laws：strain(44)；critical(37)；one(30)；mismatch(28)；scaling(26)；value(23)；bers(23)；bilayer(22)
- 5. Conclusions：grant(12)；scaling(11)；laws(11)；bilayers(11)；italian(11)；wrinkling(10)；analysis(10)；ber-reinforced(10)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`corresponding relations for fiber-reinforced bilayers remain comparatively underexplored.`
- 可复用句型骨架：`While scaling laws for the isotropic/high-contrast limit are well established, corresponding relations for X across the full mismatch range remain unavailable.`
- 中文写作启发：用成熟极限与缺失全域公式形成 gap。

### 14.2 方法与框架表达
- 原文表达模式：film as axially deformable elastic plate, substrate by SRM within finite elasticity。
- 可复用句型骨架：`The upper layer is reduced to an extensible bending plate, whereas the substrate is modeled as a fiber-reinforced finite elastic half-space.`
- 中文写作启发：降维与完整模型的分工要一开始说清。

### 14.3 结果与趋势表达
- 原文表达模式：two distinct sets of scaling laws reveal two regimes。
- 可复用句型骨架：`The asymptotic expansion reveals two distinct regimes, each governed by a different balance and therefore by a different scaling law.`
- 中文写作启发：标度律论文要强调“平衡机制不同，所以公式不同”。

### 14.4 机制解释表达
- 原文表达模式：transition mismatch indicates when control passes from film to substrate。
- 可复用句型骨架：`The transition threshold marks the point at which the dominant balance switches from film bending to substrate reinforcement.`
- 中文写作启发：阈值的意义要写成机制转移，而非纯数学边界。

### 14.5 贡献与意义表达
- 原文表达模式：simple calculation of threshold permits choosing scaling law。
- 可复用句型骨架：`A simple evaluation of the transition parameter determines which scaling law should be used in a given material system.`
- 中文写作启发：理论贡献最好转化为“使用步骤”。

### 14.6 局限与未来工作表达
- 原文表达模式：实验验证和更真实纤维本构是后续方向。
- 可复用句型骨架：`Experimental validation and extension to more realistic fiber constitutive responses are required before direct application to specific biological tissues.`
- 中文写作启发：生物材料外推要格外谨慎。

## 15. 引用策略与文献使用
- 引用密度：Introduction 很高，正文公式部分引用少。
- 引用主要集中位置：wrinkling 应用、经典标度律、有限弹性、生物组织纤维本构。
- 经典文献用途：Biot/Allen/Cao-Hutchinson 等用于建立标度律传统。
- 近年文献用途：纤维增强、生物 wrinkling、作者前期工作和 OGH/SRM 对比。
- 方法文献用途：small-on-large、薄板模型、有限弹性本构。
- 对比/批判性引用：主要是扩展而非否定经典理论。
- gap 如何靠引用搭建：先证明 wrinkling 广泛，再证明 isotropic 公式成熟，最后证明 fiber-reinforced 任意 mismatch 公式缺失。
- references 暗示的研究共同体：软材料不稳定性、非线性弹性、生物力学、薄膜/基底设计。
- 引用风险：应用面广容易漏掉某些生物/工程实验文献；但理论主线清晰。

## 16. 审稿人视角风险
- 最大攻击面：无实验验证，且 SRM 简化未必代表真实纤维网络。
- claim 是否过强：理论公式 claim 强；生物/工程应用 claim 需保持“可用于指导”而非“已验证”。
- 证据是否不足：对 direct/dual 公式有 3D 对照；对真实材料缺实验。
- 方法是否可复现：需要 supplementary 和公式细节；正文可能不足以复现所有 Puiseux 系数。
- 对比是否充分：与 3D SRM/OGH 对比是强项；与实验和其他本构较少。
- 边界条件是否清楚：onset、平面应变、完美粘结、半无限基底清楚。
- 替代解释是否排除：未讨论后屈曲模式竞争或缺陷敏感性。
- 图表是否需要进一步核查：Fig. 2-12 均需 PDF，尤其误差和 transition 图。

## 17. 可复用资产
- 可复用选题角度：把旧理论的“有效极限”扩展成“全参数域 regime map”。
- 可复用 gap 制造方式：`经典公式成熟 -> 新材料参数破坏假设 -> 中低参数区出现 regime switch -> 需要新标度律`。
- 可复用论证链：建模 -> exact/3D benchmark -> direct asymptotics -> validity map -> dual asymptotics。
- 可复用图表设计：极坐标角度图、误差热图、transition contour、direct/dual 对比图。
- 可复用段落结构：先讲物理平衡，再给公式，再给适用域。
- 可复用句型骨架：`The threshold allows one to identify the governing regime before applying the scaling law.`；`The classical scaling is recovered as a limiting case.`
- 可复用引用组织：从经典极限文献铺到最新复杂材料文献。
- 不宜直接模仿之处：缺实验时不要写得像已验证设计准则；supplementary 依赖不能过重到正文不可审计。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：公式多的理论论文要把结论组织成 regime、threshold 和使用规则。
- 可以迁移到 Introduction 的写法：先承认经典理论成熟，再指出新对象让经典假设失效。
- 可以迁移到 Method 的写法：降维模型必须用更完整模型对照，否则容易被认为过度简化。
- 可以迁移到 Results/Discussion 的写法：不要只给新公式，要给何时用旧公式、何时用新公式。
- 需要避免的问题：对真实生物材料的 claim 要留足本构和实验边界。

## 19. 最终浓缩
- 这篇论文最值得学：如何把复杂起皱分岔参数空间整理成可使用的双 regime 标度律。
- 这篇论文最大风险：SRM/板模型和真实纤维组织之间的距离，以及缺少实验验证。
- 三个可迁移动作：1. 先画适用域；2. 用完整模型 benchmark 降维模型；3. 把公式变成“先判 regime 再应用”的写作结构。
