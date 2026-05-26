# Mechanobiological morphomechanics of aneurysms

## 0. 读取说明
- 源 PDF：`jmps/文献/Mechanobiological-morphomechanics-o_2026_Journal-of-the-Mechanics-and-Physic.pdf`
- 源 TXT：`jmps/文本/txt/Mechanobiological-morphomechanics-o_2026_Journal-of-the-Mechanics-and-Physic.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 可读出理论结构、图题和结论，但相图边界、后屈曲形态、壁厚/损伤分布等视觉证据需要结合 PDF 图像核查。
- 本文类型：理论建模 + 线性稳定性分析 + 有限元数值验证的生物力学机制论文。

## 1. 基本信息与论文身份
- 题名：Mechanobiological morphomechanics of aneurysms。
- 作者与机构：Wei-Zhi Huang、Bo Li、Xi-Qiao Feng；Tsinghua University。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213 (2026) 106607。
- DOI：10.1016/j.jmps.2026.106607。
- 关键词：Aneurysm；Stress-modulated growth；Remodeling；Damage；Mechanobiological stability；Postbuckling evolution。
- 研究对象：动脉瘤形成中的动脉壁生长、胶原纤维重取向、基质损伤和残余伸长重塑。
- 研究尺度：组织层面圆柱动脉 -> 纤维增强复合材料本构 -> 线性稳定性 -> 有限元后屈曲形态。
- 方法类型：mechanobiological theory、linear stability analysis、phase diagrams、FEM postbuckling simulations。
- 证据类型：特征值/增长率、稳定/不稳定相图、轴对称与非轴对称 bulging 模拟、参数敏感性、初始损伤自愈模拟。
- 目标读者：生物组织力学、生长重塑理论、动脉瘤机制、软管屈曲稳定性和 JMPS 理论力学读者。
- JMPS 风格定位：把病理形态发生写成“主动生物组织的稳定性问题”，并与被动橡胶管式 mechanical bulging 区分。

## 2. 摘要与核心信息提取
摘要用一句临床定位开场：aneurysm is life-threatening。随后把传统“动脉瘤是局部扩张”升级为多过程耦合：tissue growth、collagen fiber reorientation、matrix damage、residual stretch remodeling，并强调这些过程由 mechanical stimuli 与 biochemical signals 调控。方法句提出集成 stress-modulated growth、remodeling、damage 的 mechanobiological theory。证据句分两层：linear stability analysis 解释 bulging bifurcation；FEM simulations 追踪 normal arteries 到 aneurysms 的 postbuckling evolution。

结果句有几个有辨识度的 claim：decreased circumferential homeostatic stress tends to stabilize arteries；internal pressure influence is small because long-term growth/remodeling compensates by wall thickening；bulging bifurcation 后出现 oscillations，但 matrix damage accumulation 使振荡衰减；aged smooth muscle mechanosensitivity reduction 可触发 instability；人工兔 AAA 的 self-healing 可由 non-aneurysmal arteries 的 mechanobiological stability 解释。

一句话主张：动脉瘤形成不是单纯被动材料在内压下的机械鼓胀，而是由应力调控生长、胶原重塑和基质损伤共同决定的 mechanobiological bulging bifurcation；这种主动适应机制解释了壁厚补偿、振荡衰减、老化诱发不稳定和初始损伤自愈等现象。

核心关键词：mechanobiological stability；stress-modulated growth；matrix damage；collagen residual stretch remodeling；postbuckling evolution。

## 3. 选题层深拆
问题来源是传统力学解释与临床/组织事实之间的矛盾。被动橡胶管模型预测局部鼓胀会伴随壁厚明显变薄，而真实动脉瘤平均壁厚常与健康动脉相近或仅略薄；临床和组织学还显示胶原取向改变、弹性层破坏、AAA 壁刚度增加。这些现象共同指向：动脉壁不是被动膜，而是会生长、重塑和损伤的活组织。

问题重要性由 aneurysm rupture 风险支撑，但作者并不急于做患者预测，而是抓住形态发生机制：为什么会出现局部 bulging，为什么内压不是唯一控制量，为什么损伤既可能诱发也可能被自愈响应抑制。这个问题适合 JMPS，因为它把医学现象转化为稳定性、分岔、后屈曲演化和本构耦合。

为什么现在值得做：已有 mechanical bulging bifurcation 文献较成熟，Cyron/Humphrey 等也发展了 mechanobiological stability 概念；作者团队已有 growing biological tissues 的理论方法。本文把这些基础合成到 aneurysm morphomechanics 中，并显式纳入 growth、remodeling、damage 三类过程。

问题边界：模型没有完整纳入血流、脉动压力、周围组织、血栓、炎症/生化网络等因素；它关注动脉壁本身在长期生长重塑中的稳定性与形态演化。边界清晰使理论可推导，但也决定其临床解释是机制层而非个体诊断层。

## 4. 领域位置与文献版图
作者把前人工作分成三条主线。第一条是临床/组织学观察：动脉瘤直径扩张、壁厚变化、胶原纤维取向分布、弹性层破坏、AAA 壁刚度等。第二条是被动 mechanical instability：把动脉视为 hyperelastic membrane tube，解释 bulging bifurcation。第三条是 mechanobiological stability/growth and remodeling：把 Lyapunov stability 与 mass turnover、growth、remodeling 结合。

每条线解决的问题不同。组织学线证明“形态变化不只是几何扩张”；被动力学线提供分岔工具；生物生长线提供主动适应框架。留下的问题是：这些线索尚未形成一个能同时解释 bulging onset、postbuckling evolution、damage feedback 和 self-healing 的统一理论。

本文站在被动动脉屈曲理论之后，又站在 mechanobiological stability 方法之内。它对前人不是替代，而是修正：被动模型能解释 latex-like bulging，但不能解释 in vivo aneurysm 的壁厚补偿和长期不可逆演化。

最接近前人包括 Rodriguez and Merodio、Fu 等被动管屈曲研究，以及 Cyron/Humphrey 的 growth-remodeling stability。本文差异在于将 matrix growth/damage、collagen reorientation、residual stretch remodeling 放在同一稳定性与 FEM 框架中。

## 5. Gap 制造机制
显性 gap：已有 mechanical bulging models 往往把 artery 作为 passive material，忽略 growth and remodeling，因此难以复制体内动脉瘤形态和长期演化。隐含 gap：已有 mechanobiological 研究虽然考虑质量更新或 prescribed elastin loss，但对 growth-remodeling-damage 耦合下的 bulging bifurcation、postbuckling oscillation 和 damage feedback 解释不足。

Gap 类型属于理论 gap + 机制 gap + 生物组织活性 gap。理论 gap 是 stability analysis 如何纳入主动生物过程；机制 gap 是动脉瘤形态如何由负反馈/正反馈交替生成；活性 gap 是被动材料类比不足。

Gap 证据来自临床/组织事实：真实 aneurysm 壁厚没有像橡胶管那样急剧变薄，胶原纤维取向更弥散，弹性层破坏，壁刚度反而提高。这些事实削弱了“单纯内压机械失稳”的解释力。

审稿人追问可能集中在生化过程简化：stress-modulated growth 是否足以代表真实 mechanobiological signaling？作者在局限段承认线性 stress-modulated effects 只适用于 homeostatic state 附近，未来需更精确非线性机制，这是必要的防守。

## 6. 创新性判断
作者声称贡献：提出整合 stress-modulated growth、remodeling、damage 的 mechanobiological theory；通过 linear stability analysis 揭示 mechanobiological bulging bifurcation；通过 FEM 追踪 postbuckling evolution；解释内压影响小、oscillation、damage accumulation、自愈和老化 mechanosensitivity 等现象。

真实创新在于将多个生物过程组织为稳定性问题，并用 phase diagrams 与后屈曲模拟共同说服。尤其是“internal pressure little influence because active growth/remodeling compensates wall thickening”与“damage turns compensatory oscillation into progressive dilation”两个机制，构成了区别于被动管模型的主要贡献。

创新类型：理论框架创新强；机制解释强；数值验证中等；临床应用推论中等。创新必要性高，因为动脉瘤领域容易停留在 phenomenological growth/remodeling 或纯机械屈曲，本文把两者以稳定性语言连接。

容易被挑战的创新点：参数较多、方程假设线性、growth/remodeling laws 的生理真实性；FEM 是否真正“验证”理论，还是在同一模型假设下的数值实现；非轴对称 aneurysm 的异质性设定是否过于理想化。

## 7. 论证链条复原
背景 -> aneurysm 是严重动脉疾病，真实形态涉及壁厚、纤维取向、损伤和刚度变化。
文献 -> 被动 hyperelastic tube bulging 已研究，但忽略活性生长重塑；mechanobiological stability 概念已有基础。
gap -> 需要能同时处理 growth、remodeling、damage 和 bulging bifurcation 的理论。
问题 -> 活性动脉在什么条件下发生 mechanobiological instability，并如何演化为 aneurysm-like bulges？
方法 -> 建立 fiber-reinforced artery theory，写入 matrix growth/damage、collagen reorientation/residual stretch remodeling，做线性稳定性和 FEM。
证据 -> normalized growth rate、phase diagrams、axisymmetric/non-axisymmetric postbuckling morphologies、initial damage simulations。
发现 -> circumferential homeostatic stress 和 mechanosensitivity 关键；内压被长期壁厚补偿削弱；damage 使振荡衰减并促进扩张。
机制 -> 生长重塑是负反馈，matrix damage 是正反馈；两者竞争决定形态演化。
意义 -> 解释自发 aneurysm、人工模型 self-healing 和老化相关风险，为 patient-specific assessment 提供机制框架。

薄弱环节是从理想圆柱/偏心动脉到临床复杂形态的跨度。作者通过讨论周围组织、血流、血栓、mechano-bio-chemical coupling 等未纳入因素，控制了外推。

## 8. 方法/理论/模型细拆
理论结构按章节搭建。2.1 Kinematics 定义 reference/current configurations、增长变形和几何变量。2.2 Growth of arteries 写入 matrix stress-modulated volumetric growth。2.3 Remodeling of arteries 处理 collagen fiber production、degradation、reorientation 和 residual stretch remodeling。2.4 Damage of arteries 引入 supra-physiological load induced matrix damage。2.5 Mechanobiological equilibrium 定义活组织长期平衡。2.6 Incremental mechanobiological deformation 为稳定性分析做增量方程。

关键变量包括 internal pressure、circumferential/axial homeostatic stresses、collagen stiffness 与 strain-stiffening parameters、growth parameters、damage parameters、residual stretch increase、mode number、normalized growth rate。Table 1 承担参数表功能。

方法步骤：先求 cylindrical mechanobiologically static state；再做 dimensional analysis；然后区分 mechanical stability 与 mechanobiological stability；再用 phase diagrams 扫描压力、homeostatic stress、collagen parameters、growth parameters、damage/residual stretch；最后以 FEM 追踪 axisymmetric bulging、initial damage-induced bulging 和 non-axisymmetric bulging。

核心假设：动脉可视为 fiber-reinforced composite；matrix 和 collagen 的主动过程可由应力调控律表达；稳定性可由线性增量和增长率判断；损伤在 matrix 应力超过生理域时积累。方法复杂度与问题匹配，但可复现需要完整方程、边界条件和参数值。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 动脉瘤形成可由 mechanobiological bulging bifurcation 解释 | 摘要、4-6 | 线性稳定性分析与 FEM 后屈曲形态吻合 | 理论 + 数值 | 强 | 依赖模型假设 |
| internal pressure 对主动动脉 bulging stability 影响较小 | 摘要、6 | phase diagrams 与讨论中对被动模型的对比 | 参数相图 | 中强 | 临床中脉动压力/血流未纳入 |
| 较大的 circumferential homeostatic stress 可使动脉失稳，降低该应力趋于稳定 | 摘要、4.3、6 | normalized growth rate 随 homeostatic stress 的相图变化 | 稳定性结果 | 强 | homeostatic stress 难直接测量 |
| bulging 后的振荡来自 growth/remodeling 负反馈，damage accumulation 使振荡衰减 | 摘要、5.2、6 | postbuckling morphology、wall thickness/time curves、damage evolution | FEM 时程 | 中强 | 振荡幅度临床不可见 |
| aged VSMC mechanosensitivity reduction 可触发 instability | 摘要、4.3/6 | growth parameter/ mechanosensitivity phase space | 参数机制推论 | 中 | 生理参数映射需实验证据 |
| 初始损伤下自愈行为可来自非动脉瘤动脉的 mechanobiological stability | 摘要、5.3、6 | initial prescribed damage FEM 与兔 AAA self-healing 对照 | 模拟 + 文献解释 | 中 | 动物模型机制可能更多元 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | artery reference/current configuration schematic | 理论变量定义 | 建立几何和变形分解 | 是 |
| Table 1 | 模型参数/无量纲量 | 方法可复现 | 支撑相图扫描 | 否，需核数值 |
| Fig. 2-3 | normalized growth rate 与 homeostatic stress/length | mechanobiological stability | 展示分岔前兆 | 是 |
| Fig. 4-8 | pressure、matrix stress、collagen parameters、growth/damage 的 phase diagrams | 参数控制稳定性 | 把理论结果可视化为稳定/不稳定区 | 是 |
| Fig. 10-11 | axisymmetric postbuckling morphology 与 wall thickness/time | aneurysm-like evolution、oscillation | 从线性分岔走到形态演化 | 是 |
| Fig. 12 | stable artery under initial prescribed damage | self-healing 解释 | 展示损伤不必然导致 aneurysm | 是 |
| Fig. 13-14 | mode number、eccentric artery、non-axisymmetric bulging | 真实异质性影响形态 | 扩展到非轴对称形态 | 是 |
| 方程组 2.1-2.6 | kinematics/growth/remodeling/damage/equilibrium/incremental deformation | 理论贡献 | 提供 JMPS 级力学骨架 | 否，但需核公式细节 |

图表叙事是：先定义几何，再用相图找失稳条件，再用 FEM 展示失稳后会长成什么样。相图承担“理论判据”，形态图承担“病理可解释性”。

## 11. 章节结构与篇章布局
Abstract：疾病重要性 -> 多过程耦合 -> 理论与 FEM -> 关键发现 -> 框架意义。
Introduction：临床定义与组织事实 -> 被动机械失稳文献 -> mechanobiological stability 文献 -> 本文贡献。
Theory：从 kinematics 到 growth/remodeling/damage/equilibrium/incremental deformation，层层铺垫。
Mechanobiologically static state：先建立基态，避免稳定性分析无根。
Linear stability analysis：区分 mechanical 与 mechanobiological，并用 phase diagrams 展开。
Numerical simulations：从 FEM 方法到轴对称、初始损伤、非轴对称形态。
Discussions and conclusions：与被动模型对比，解释机制，承认局限。

最值得模仿的是理论论文的“先基态、再稳定性、再后屈曲”的布局。标题也很稳：Theory、Mechanobiologically static state、Linear stability analysis、Numerical simulations，让读者知道每节的数学功能。

结构风险：理论部分参数和方程密集，非本领域读者可能难以跟上；但后续相图和形态模拟降低了理解门槛。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Mechanobiological-morphomechanics-o_2026_Journal-of-the-Mechanics-and-Physic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：26
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Kinematics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Growth of arteries | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Remodeling of arteries | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Damage of arteries | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Mechanobiological equilibrium | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.6 Incremental mechanobiological deformation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Mechanobiologically static state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Cylindrical mechanobiologically static state | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Dimensional analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Linear stability analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Mechanical stability analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Mechanobiological stability analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 第一段用临床与流行病学建立问题严重性；第二段列组织事实，制造被动模型解释不了的矛盾；第三段梳理 mechanical bulging bifurcation；第四段引入 mechanobiological stability；末段给出本文理论框架和目标。

Theory 段落节奏是“定义变量 -> 写过程律 -> 写平衡 -> 写增量”。每个小节只承担一个生物过程，避免 growth、remodeling、damage 混成一团。

Results/Simulation 段落常见模式：先给某参数的相图，再解释稳定/不稳定区变化，再与生理或病理现象对应。FEM 段落则先描述 morphology，再解释 wall thickness、growth、damage、residual stretch 的时间演化。

Conclusion 段落不是摘要式列表，而是讨论式收束：先重申框架，再与 passive model 对照，再解释 feedback，再写老化和自愈，最后承认局限和未来机制。

可复用段落模板：`Observed biological morphology conflicts with passive mechanical prediction -> introduce active adaptation variable -> stability analysis shows altered critical condition -> simulation recovers disease-like morphology.`

## 13. 文笔画像与语言习惯
语气是理论型、解释型、对比型。作者频繁使用 “different from previous studies”“in contrast”“this behavior results from”“contributes to”“promotes” 来区分主动组织与被动材料。

claim 强度较高，但通常绑定在“theoretical and numerical results reveal”之后；临床表达更谨慎，如 “may contribute”“future efforts are deserved”。

常用问题词：formation、development、morphogenesis、bulging bifurcation、mechanobiological instability。常用机制词：growth、remodeling、damage、residual stretch、homeostatic stress、mechanosensitivity、negative feedback、positive feedback。常用限定词：within the vicinity of homeostatic state、clinically imperceptible、many other factors。

长句用于理论过程和文献差异；短句用于结论中的关键判断。名词化程度高，符合 JMPS 理论论文风格。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：growth(144)；collagen(113)；matrix(113)；damage(108)；artery(91)；arteries(82)；fibers(73)；normalized(73)；mechanobiological(69)；stress(68)；stretch(60)；mechanobiologically(60)；aneurysms(58)；remodeling(56)；bulging(56)；mechanical(54)；residual(53)；homeostatic(50)；phase(47)；incremental(45)
- 高频学术名词：stress(68)；deformation(50)；analysis(40)；stability(37)；instability(32)；parameter(29)；thickness(29)；material(27)；bifurcation(27)；pressure(27)；formation(23)；evolution(22)；distribution(22)；configuration(21)；parameters(20)；solution(18)
- 高频学术动词：shown(22)；shows(14)；derived(7)；investigate(6)；reveal(6)；proposed(6)；show(6)；developed(5)；indicates(4)；investigated(4)；solve(4)；suggests(3)；simulate(3)；validate(2)；derive(2)；suggest(2)
- 高频形容词：unstable(84)；static(70)；mechanobiological(69)；critical(58)；mechanical(54)；residual(53)；homeostatic(50)；incremental(45)；circumferential(43)；local(34)；axial(27)；material(27)；internal(26)；theoretical(24)；stable(22)；variable(22)
- 高频副词/连接副词：mechanobiologically(60)；respectively(24)；generally(14)；significantly(12)；mechanically(11)；similarly(11)；family(10)；newly(9)；therefore(8)；slightly(8)；however(7)；numerically(6)；furthermore(5)；clinically(5)；initially(5)；locally(4)
- 高频二词短语：collagen fibers(73)；residual stretch(42)；growth remodeling(34)；collagen fiber(30)；matrix damage(30)；mechanobiologically static(30)；growth rate(29)；homeostatic stress(28)；static state(28)；mechanobiologically unstable(26)；normalized growth(24)；bulging bifurcation(22)；wall thickness(22)；internal pressure(20)；circumferential homeostatic(18)；mechanobiological bulging(18)
- 高频三词短语：mechanobiologically static state(28)；normalized growth rate(24)；circumferential homeostatic stress(17)；exp cos exp(14)；collagen fiber residual(13)；mechanobiologically unstable phase(13)；growth remodeling damage(12)；mechanobiological bulging bifurcation(12)；radial growth ratio(12)；growth rate function(11)；limit physiological domain(9)；fiber residual stretch(9)

**主动、被动与句法**

- 被动语态估计次数：141
- `we + 动作动词` 主动句估计次数：9
- 名词化表达估计次数：898
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：256
- 一般过去时线索：29
- 现在完成时线索：7
- 情态动词线索：90
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：mechanobiological(7)；growth(5)；damage(5)；aneurysms(4)；remodeling(4)；tsinghua(3)；university(3)；beijing(3)
- 1. Introduction：aneurysms(18)；growth(17)；damage(15)；collagen(13)；arteries(12)；aneurysm(11)；mechanical(11)；bulging(10)
- 2. Theory：无明显高频项
- 2.1. Kinematics：collagen(21)；fibers(18)；configuration(13)；time(11)；matrix(11)；stretch(10)；artery(9)；growth(8)
- 2.2. Growth of arteries：growth(9)；stress(6)；circumferential(5)；axial(5)；blood(4)；collagen(4)；fibers(4)；mass(4)
- 2.3. Remodeling of arteries：stretch(6)；residual(4)；stress(4)；cauchy(3)；principal(3)；mechanobiologically(3)；static(3)；state(3)
- 2.4. Damage of arteries：damage(7)；matrix(7)；arteries(5)；variable(5)；internal(4)；strain(3)；energy(3)；density(3)
- 2.5. Mechanobiological equilibrium：collagen(9)；equilibrium(8)；matrix(7)；fibers(7)；strain(6)；energy(6)；artery(6)；stress(4)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
骨架：`Although [passive/mechanical models] can explain [idealized instability], they cannot reproduce [in vivo morphology] because they neglect [active processes].`
中文启发：用真实现象与经典模型预测不一致制造强 gap。

### 14.2 方法与框架表达
骨架：`We propose a mechanobiological theory that integrates [process A], [process B], and [process C] to elucidate [morphogenesis/mechanism].`
中文启发：理论贡献句要列出被整合的过程，而不是只说“new model”。

### 14.3 结果与趋势表达
骨架：`Our results reveal that [parameter/process] tends to stabilize/destabilize [system], whereas [another factor] exerts limited influence due to [compensation mechanism].`
中文启发：对比两个因素的作用强弱，并给出补偿机制。

### 14.4 机制解释表达
骨架：`The local [morphological change] triggers [adaptive response], which acts as a negative feedback; once [damage threshold] is reached, [damage] becomes a positive feedback that accelerates [disease progression].`
中文启发：复杂生物过程可写成反馈竞争。

### 14.5 贡献与意义表达
骨架：`This framework provides a mechanobiological basis for analyzing [growth/damage/remodeling] in physiological and pathological contexts.`
中文启发：意义句要从具体疾病扩展到一类过程。

### 14.6 局限与未来工作表达
骨架：`The assumed linear stress-modulated effects are valid only near [state]; more precise nonlinear laws are required to address [regime].`
中文启发：局限要指出适用区间，而不是泛泛说模型简化。

## 15. 引用策略与文献使用
引用策略服务于“被动模型不足”。临床/组织引用用于证明真实 aneurysm 的形态和材料变化；Fu、Rodriguez、Topol 等用于代表 mechanical bulging bifurcation；Cyron、Humphrey 等用于 mechanobiological stability；兔 AAA 自愈实验用于支持 initial damage simulation 的讨论。

经典文献承担理论谱系：hyperelastic membrane tube、growth and remodeling、fiber-reinforced artery。近年文献承担临床/组织现象和 mechano-bio-chemical coupling 的边界。引用姿态总体克制：作者承认被动模型解释了某类 instability，但指出它对活组织形态不足。

gap 与引用关系：先用引用证明 passive model 的合理性，再用组织事实引用指出其偏差，最后引入 mechanobiological stability 文献作为桥梁。这样的 gap 不显得突兀。

引用风险：动脉瘤生物化学机制庞大，若审稿人来自血管生物学，可能认为引用过于力学化；作者通过 future work 提到 blood flow、ILT、mechano-bio-chemical coupling 来缓解。

## 16. 审稿人视角风险
最大攻击面是生物过程律的真实性。linear stress-modulated growth、collagen reorientation、residual stretch remodeling 和 damage law 是否有直接实验标定？如果参数可调范围很大，相图可能被认为是模型行为而非疾病机制。

第二个风险是“internal pressure little influence”的表述。临床读者可能认为压力当然重要；作者的意思是在长期主动生长重塑平衡下，内压效应被壁厚补偿弱化。写作上必须保留这个条件，避免被误读为内压无关。

第三个风险是 FEM 与理论并非独立验证，而是同一理论的数值实现。应把 FEM 称为 corroborate/trace postbuckling，而不是实验验证。

图表需核查：相图边界、颜色定义、mode number、时间归一化、damage 分布和壁厚曲线是说服关键，需结合 PDF 图像确认。

## 17. 可复用资产
可复用选题角度：用“经典被动力学预测与真实生物组织形态不一致”作为理论创新入口。
可复用 gap 制造：传统模型解释 instantaneous mechanical instability，但疾病形成是 progressive persistent mechanobiological process。
可复用论证链：组织事实 -> 被动模型不足 -> 主动过程建模 -> 稳定性判据 -> 后屈曲形态 -> 病理解释。
可复用图表设计：reference/current configuration schematic、phase diagrams、mode number maps、postbuckling morphology、time-evolution curves。
可复用段落结构：每个生物过程一个小节，最后在 equilibrium/incremental deformation 中合并。
可复用句型：`Unlike passive materials, active tissues can maintain [state] through long-term [growth/remodeling], thereby altering [stability condition].`
不宜直接模仿：没有实验标定时把 mechanobiological 参数解释成确定临床阈值。

## 18. 对我写论文的启发
写类似理论论文时，可以学习“矛盾事实驱动建模”：先列出被动模型解释不了的形态事实，再提出需要引入哪些物理/生物过程。Introduction 不要堆疾病背景，而要让每个背景事实都指向模型变量。

Method 可迁移写法：按过程分节，先各自定义，再在平衡和增量方程中耦合。Results 可迁移写法：相图回答“何时失稳”，后屈曲模拟回答“失稳后长成什么样”。Discussion 可迁移写法：把模型反馈机制与具体临床/动物实验现象对照，同时明确未纳入因素。

需要避免：参数多但缺少主线；相图很多但没有提炼稳定/失稳的生物解释；把模型推论写成临床事实。

## 19. 最终浓缩
这篇论文最值得学的是：把动脉瘤形态发生从被动 mechanical bulging 改写为主动 mechanobiological instability，并用 growth/remodeling 负反馈与 damage 正反馈解释长期演化。

最大风险是：生物调控律和参数缺乏直接个体化标定，真实 aneurysm 还受血流、周围组织、炎症、血栓和生化网络影响。

三个可迁移动作：1. 用真实现象反驳经典模型的关键预测；2. 用相图把理论判据可视化；3. 用后屈曲模拟把数学稳定性翻译成病理形态。
