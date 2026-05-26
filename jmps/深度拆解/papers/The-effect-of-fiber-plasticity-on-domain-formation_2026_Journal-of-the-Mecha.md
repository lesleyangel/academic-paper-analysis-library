# The effect of fiber plasticity on domain formation in soft biological composites—Part II: An imperfection analysis

## 0. 读取说明
- 源 PDF：`jmps/文献/The-effect-of-fiber-plasticity-on-domain-formation_2026_Journal-of-the-Mecha.pdf`
- 源 TXT：`jmps/文本/txt/The-effect-of-fiber-plasticity-on-domain-formation_2026_Journal-of-the-Mecha.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 214 (2026) 106645, DOI: 10.1016/j.jmps.2026.106645。
- 是否需要结合 PDF 图像核查：需要。本文关键证据是层合几何、domain 形貌、P21/P22 应力云图、accumulated plastic strain、stress-stretch 曲线、strain energy 曲线和不同缺陷幅值/波长的变形图；当前只据 txt 和图注拆解，所有 domain 位置、颜色、局部弯曲和图中线型需 PDF 核查。
- 本文类型：软生物复合材料理论/数值论文，是 Part I 完美层合板分岔分析的几何缺陷补充。

## 1. 基本信息与论文身份
- 题名：The effect of fiber plasticity on domain formation in soft biological composites—Part II: An imperfection analysis。
- 作者/机构：Dimitris Iordanidis, Michail Agoras, Nicholas Bouklas 等；txt 首屏显示通讯作者来自 University of Thessaly 和 Cornell University，完整机构需 PDF 核查。
- 关键词：Soft composites; Fiber plasticity; Loss of ellipticity; Domain formation; Tendon。
- 研究对象：two-phase laminate soft biological composites、stiff collagen-like fiber phase、compliant matrix phase、geometric crimp imperfection、finite-strain J2 plasticity。
- 研究尺度：mesoscopic laminate unit cell；从小幅 sinusoidal imperfection 到 layer-width 量级 crimp；单调压缩和拉伸-卸载-压缩非单调加载。
- 方法类型：finite-strain elastoplastic constitutive model + multiplicative decomposition + flow rule integration + periodic boundary conditions + nonlinear FE imperfection analysis。
- 证据类型：纯超弹性层合板中 domain formation 与 perfect laminate 的 LOE 一致；不同 imperfection 类型/波长/幅值影响；fiber yield limit 与 hardening 参数研究；非单调加载下大幅 crimp 可在宏观 tensile unloading 阶段形成 domains。
- 目标读者：软组织力学、tendon mechanics、有限变形塑性、loss of ellipticity、复合材料微结构失稳和生物启发材料读者。
- JMPS 风格定位：典型“companion theory + numerical imperfection validation”论文。JMPS 味道在于把 tendon chevron-like patterns 写成可由层合板失稳、fiber plasticity 和几何缺陷共同解释的力学问题。

## 2. 摘要与核心信息提取
摘要将本文明确定位为 Part II：Part I 分析完美平直层合板在 plane-strain 和 aligned non-monotonic loading 下的分岔；本文加入 soft biological materials 中不可避免的 crimp/geometric imperfection。摘要先指出 Part I 的 post-bifurcation solution 物理上对应垂直于加载轴的 twin lamellar domains，与 tendon 循环加载中的 chevron-like patterns 相似；随后说明真实 tendon 高度 imperfect，特别是 collagen fibers 的 crimp 需要纳入。

核心结果分两层：小初始缺陷下，数值结果与 Part I 完美几何分析完全一致，domains 在宏观压缩状态出现；当 imperfection amplitude 增大到 layer width 或更大时，domains 会在卸载过程的宏观拉应力下发展，这更符合 tendon/ligament 主要承受拉伸的生理事实。

一句话主张：collagen fiber plasticity 与几何 crimp imperfection 会共同控制软生物层合复合材料的 domain formation，小缺陷验证 Part I 的 LOE，大缺陷则打开 tensile unloading 中形成 domains 的机制路径。

## 3. 选题层深拆
问题来源：tendon 和 ligament 等软纤维组织在循环加载中会出现 localized kinks 和 repeating chevron-like patterns，这些模式会扰动 tenocyte microenvironment，被视为 tendinopathy 的早期标志。Part I 已在完美层合板中说明 fiber plasticity 可诱发 LOE 和 lamellar domains，但真实胶原纤维存在 crimp，不是理想平直层。

问题为什么重要：如果理论只在完美几何中成立，无法解释真实组织中的缺陷诱导模式；如果理论只预测宏观压缩下 domain formation，也难以对应 tendon 主要拉伸加载的事实。本文通过 imperfection analysis 连接理论分岔和真实组织形貌。

问题为什么现在值得做：已有 Part I 的解析基准、finite-strain plasticity 框架、周期性边界 FE 和 tendon crimp 生物观察。本文不是从零建模，而是检验一个完美理论在更真实几何下是否稳健，以及何时产生新机制。

问题边界：二维 plane strain laminate、理想周期边界、简化 crimp 几何、fiber phase plasticity、matrix 多为 elastic。真实 tendon 的三维纤维束、水合基质、残余应力、细胞耦合和损伤演化未完全纳入。

## 4. 领域位置与文献版图
文献版图连接三类对象。第一类是 tendon/ligament 生物力学：collagen fibers 可表现 ductile behavior，matrix deformation 多可恢复，组织能承受大量循环。第二类是 chevron folding/domain formation：tendon 中 kink patterns 与层状岩石、seashell patterns 有形式相似性。第三类是理论力学和复合材料失稳：Furer and Castañeda 的 hyperelastic laminate domain formation、d’Avila 等几何扰动、Part I 的 elastoplastic bifurcation theory。

本文站位：Part I 给完美 laminate 的 principal path、LOE 和 post-bifurcation；本文加入 imperfections，检验 LOE 预测的稳定性，并把大幅 crimp 与 tensile loading 中 domains 联系起来。

文献处理公平：作者承认 Part I 是直接基础，也承认已有纯超弹性层合板 domain theory；新意在 biological imperfection 和 fiber plasticity 的组合。

## 5. Gap 制造机制
明示 gap：Part I 的 perfect two-phase laminate 没有考虑几何缺陷，而 biological materials 在多尺度上高度 imperfect，尤其 collagen fiber crimp。隐含 gap：完美几何理论若只预测压缩 domain formation，不能充分解释 tendon 在 tensile cyclic loading 下观察到的 chevron-like patterns。

gap 类型：对象 gap + 几何 gap + 加载历史 gap。对象 gap 是从工程层合板走向 tendon-like soft composites；几何 gap 是从 flat layers 到 sinusoidal/decaying imperfections；加载历史 gap 是从 monotonic compression 到 tension-unloading-compression。

审稿人追问：crimp 初始状态是否 stress-free；二维层合板是否能代表真实 tendon fascicle；塑性参数是否来自实验；domain formation 与 actual damage/tendinopathy 的定量关系是否足够。

## 6. 创新性判断
创新不在于单独提出 finite-strain plasticity，而在于把 Part I 的完美分岔理论放到几何缺陷和非单调加载下检验。结果具有双重价值：小缺陷下理论稳健，onset 与 LOE 接近；大缺陷下理论边界打开，domains 可在宏观拉应力/卸载阶段出现。

创新类型：机制验证 + imperfection analysis + biological relevance。强度中高。本文把一个理论 companion paper 与真实组织形貌之间的距离缩短了，尤其是“tensile unloading 中 domain formation”这一点增强了 tendon 相关性。

容易被挑战处：几何缺陷幅值达到 layer width 是否真实；initial stress-free crimp 假设可能不符合 tendon；局部 bending/transition regions 的损伤解释需要实验验证。

## 7. 论证链条复原
背景：tendon/ligament 的 collagen fibers 在循环加载中形成 chevron-like domains，与早期损伤相关。 -> 文献：Part I 完美层合板预测 fiber plasticity 可导致 LOE 和 lamellar domains。 -> gap：真实组织存在 crimp，且主要承受 tensile loading。 -> 问题：几何缺陷如何改变 macroscopic response 和 domain onset。 -> 方法：finite strain elastoplastic laminate FE，sinusoidal/decaying imperfections，periodic boundary conditions，monotonic/non-monotonic loading。 -> 证据：纯超弹性 baseline 与 LOE 对照；wavelength/amplitude/geometry studies；yield limit/hardening studies；tension-unloading-compression 下大幅缺陷形成 domains。 -> 发现：小缺陷验证完美理论，大缺陷能解释 tensile unloading domains；transition regions 有强 bending 和局部塑性。 -> 意义：fiber plasticity 与 crimp 可能是真实 tendon domain evolution 的关键。

## 8. 方法/理论/模型细拆
材料为两相 laminate：stiff fiber phase 与 compliant matrix phase 周期交替。有限变形下采用 multiplicative decomposition F=FeFp，每相可写 elastoplastic，yield criterion 为 von Mises with isotropic hardening，内部变量为 accumulated plastic strain。

几何缺陷主要是 sinusoidal perturbation，参数为 amplitude α 和 wavelength w，动机来自 tendon crimp。另比较 d’Avila 等 decaying perturbation。周期性边界通过 homologous boundary points 施加，使 unit cell 代表无限层合材料。

数值研究分两大块。Section 3 先用 purely hyperelastic laminate 检查 imperfection 对 Part I/既有 domain theory 的影响，研究 baseline、另一类 perturbation 和 wavelength。Section 4 转向 elastoplastic laminate，考察 initial yield limit、hardening、以及 tension -> unloading -> compression 的非单调程序。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 小幅 sinusoidal imperfection 下 domain onset 与 perfect laminate LOE 基本一致 | Section 3/Fig.3-5 | 应力云图、stress-stretch response、LOE vertical marker | 数值+理论对照 | 强 | transition region 有 finite-size 偏离 |
| domain formation 后软化机制来自 stiff fiber rotation 与 matrix shear 增加 | Fig.4-5/Conclusion | phase response、P21 contour、matrix deformation | 机制图+能量解释 | 中强 | 三维纤维网络可能更复杂 |
| imperfection 类型会决定是否出现 rank-2-like domains | Fig.7-8 | sinusoidal 与 decaying perturbation 对比 | 数值对比 | 中 | 需 PDF 核查图像细节 |
| 波长/厚度/幅值会改变 transition regions 的能量代价和 onset | Fig.9-12/Appendix | 不同 wavelength 的形貌、应力-伸长、strain energy | 参数研究 | 中强 | 参数范围仍是理想 laminate |
| fiber yield limit 和 hardening 控制弹性/塑性竞争，进而影响 LOE 与 domains | Fig.13-16 | 不同 Σy/hardening 参数下 domain/no-domain 曲线 | 参数研究 | 强 | collagen plasticity law 需实验支持 |
| 大幅 crimp 可使 domains 在 tensile unloading 中出现 | Fig.17-20/Conclusion | 非单调加载、不同 imperfection amplitude、deformed configurations | 数值机制 | 中强 | 与真实 tendon 定量对应仍不足 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig.1-2 | two-phase laminate 和 perturbed unit cell | 问题定义 | 交代完美层合板与 crimp 缺陷 | 需结合 PDF 图像核查 |
| Fig.3-5 | 纯超弹性单调压缩中的 P22/P21 contour 与响应曲线 | LOE-onset claim | 证明小缺陷仍回收 Part I 结论 | 需结合 PDF 云图核查 |
| Fig.6 | 附加 shear 下 domain/mesolayer 演化 | 后分岔机制 | 展示 domain 可被剪切调控 | 需结合 PDF 图像核查 |
| Fig.7-8 | 两类几何扰动对比 | 缺陷类型 claim | 说明不是所有扰动都诱导同样 domains | 需结合 PDF 图像核查 |
| Fig.9-12 | wavelength 与 strain energy study | 尺度效应 claim | 显示 transition region 能量代价 | 需结合 PDF 曲线核查 |
| Fig.13-16 | yield limit/hardening 参数研究 | fiber plasticity claim | 区分 domain/no-domain 和局部塑性 | 需结合 PDF 图像核查 |
| Fig.17-20 | 非单调加载与缺陷幅值 | tensile-domain formation claim | 连接 tendon 拉伸情境 | 需结合 PDF 图像核查 |
| 公式组 | multiplicative decomposition、yield function、periodic BC、sinusoidal imperfection | 模型闭合 | 从材料、几何到边界条件 | 不涉及图像本体 |

## 11. 章节结构与篇章布局
Introduction 先讲 tendon damage cascade 和 chevron patterns，再连接 Part I。Theory and methodology 给 kinematics、constitutive theory、flow rule integration、FE implementation、periodic boundary conditions 和 nonlinear solution scheme。Section 3 研究 purely hyperelastic laminate，作为理论基准和缺陷效应分离。Section 4 研究 elastoplastic laminate，进入 fiber plasticity 的核心。Conclusion 汇总小缺陷、大缺陷、塑性和 tendon relevance。

最值得模仿的是“先纯弹性再弹塑性”的结构：先用简单材料剥离几何缺陷效应，再加入塑性解释真实现象。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-effect-of-fiber-plasticity-on-domain-formation_2026_Journal-of-the-Mecha.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：17
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Theory and methodology | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Kinematics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Constitutive theory | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Flow rule integration scheme | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Finite element implementation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Enforcement of periodic boundary conditions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.6 Nonlinear solution scheme | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Numerical investigation of a purely hyperelastic laminate | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Baseline case | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 An alternative type of geometric imperfection | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Wave length study | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Numerical investigation of an elastoplastic laminate | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Initial yield limit | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 节奏：软组织损伤重要 -> tendon chevron pattern 现象 -> Part I 理论基础 -> 真实 crimp 缺陷 -> 本文 imperfection analysis。Method 段落非常标准，先 kinematics 再 constitutive，再 numerical implementation。

Results 段落按“baseline -> alternative perturbation -> wavelength -> yield limit -> hardening -> nonmonotonic loading”推进，每一步只增加一个控制因素。这样的节奏适合复杂非线性问题，因为读者能区分几何、材料和加载历史的作用。

Conclusion 段落长但功能清楚：先回顾研究动机和简化，再分 hyperelastic 与 elastoplastic 两部分总结，最后强调大缺陷下 tensile domain formation 的生物意义。

## 13. 文笔画像与语言习惯
整体语气谨慎而机制感强。作者常用 “motivated from tendon”“consistent with Part I”“under the set of assumptions”“qualitative analysis” 等表达，提醒读者这是理想化机制模型，不是直接临床预测。

claim 强度有分层：与 Part I 一致的数值结果写得较强；解释 tendon 实际 domains 时用 “suggest strongly”“may play a key role” 这种有边界的表达。文笔中物理图像很丰富，如 rotation of stiff phase、increased shear in matrix、transition regions、intense bending。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：solution(77)；phase(65)；loading(57)；elastic(55)；response(54)；analytical(53)；compression(50)；formation(45)；results(44)；domains(43)；part(42)；domain(39)；laminates(39)；ber(38)；composite(36)；imperfection(34)；laminate(34)；monotonic(34)；plastic(34)；work(32)
- 高频学术名词：solution(154)；deformation(62)；response(54)；transition(46)；formation(45)；results(44)；analysis(36)；imperfection(34)；ellipticity(28)；material(27)；strain(26)；plasticity(25)；stress(23)；conditions(20)；section(20)；perturbation(19)
- 高频学术动词：shown(27)；indicates(16)；compared(9)；develop(7)；developed(4)；predicted(4)；indicate(4)；captured(3)；suggest(2)；suggests(2)；investigate(2)；compare(2)；proposed(2)；derived(2)；investigated(2)；validate(1)
- 高频形容词：elastic(110)；analytical(106)；plastic(68)；numerical(46)；monotonic(34)；macroscopic(30)；sinusoidal(28)；material(27)；elastoplastic(26)；local(20)；erent(20)；geometric(19)；initial(17)；boundary(17)；principal(16)；vertical(14)
- 高频副词/连接副词：purely(24)；approximately(14)；geometrically(9)；numerically(8)；cally(8)；respectively(8)；ciently(7)；experimentally(6)；additionally(6)；interestingly(5)；cantly(5)；strongly(4)；highly(4)；however(3)；macroscopically(3)；primarily(3)
- 高频二词短语：analytical solution(40)；domain formation(32)；monotonic compression(27)；loss ellipticity(22)；unit cell(20)；ber phase(18)；casta eda(18)；purely elastic(18)；transition regions(18)；matrix phase(15)；yield limit(14)；subjected monotonic(14)；indicates loss(14)；ellipticity analytical(14)；furer casta(12)；rank laminate(12)
- 高频三词短语：indicates loss ellipticity(14)；loss ellipticity analytical(14)；ellipticity analytical solution(14)；subjected monotonic compression(13)；furer casta eda(12)；elastic coe cients(12)；red line indicates(10)；line indicates loss(10)；initial yield limit(9)；laminates subjected monotonic(9)；vertical red line(9)；material properties laminates(8)

**主动、被动与句法**

- 被动语态估计次数：282
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：1068
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：392
- 一般过去时线索：136
- 现在完成时线索：30
- 情态动词线索：30
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：soft(5)；biological(5)；plasticity(4)；formation(4)；composites(4)；part(4)；work(4)；loading(4)
- 1. Introduction：macroscopic(13)；part(11)；ber(11)；composites(10)；response(9)；composite(9)；phase(9)；loading(9)
- 2. Theory and methodology：region(2)；material(1)；consideration(1)；two-phase(1)；laminate(1)；periodically(1)；alternating(1)；layers(1)
- 2.1. Kinematics：point(3)；gradient(3)；material(2)；deformation(2)；state(2)；positional(1)；vector(1)；current(1)
- 2.2. Constitutive theory：plastic(10)；elastic(6)；isotropic(5)；yield(5)；function(5)；hardening(4)；stress(4)；plasticity(3)
- 2.3. Flow rule integration scheme：step(3)；plastic(3)；results(3)；discrete(2)；steps(2)；time(2)；presented(2)；yields(2)
- 2.4. Finite element implementation：boundary(5)；virtual(4)；work(4)；problems(3)；body(3)；displacement(3)；prescribed(3)；equations(3)
- 2.5. Enforcement of periodic boundary conditions：boundary(7)；face(6)；points(5)；material(4)；unit(4)；cell(4)；conditions(4)；periodic(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：Although the perfect geometry reveals the bifurcation mechanism, real biological tissues contain imperfections across scales.
- 中文启发：用“完美理论已解释 A，但真实对象存在 B”制造 Part II gap。

### 14.2 方法与框架表达
- 骨架：We employ the same constitutive framework as Part I and introduce geometric imperfections motivated by X.
- 启发：companion paper 写法要强调继承与新增变量。

### 14.3 结果与趋势表达
- 骨架：For small imperfections, the onset coincides with the analytical LOE; for larger imperfections, the response deviates and domains emerge earlier/later.

### 14.4 机制解释表达
- 骨架：The post-bifurcation softening is accommodated by rotation of the stiff phase and shear deformation of the compliant matrix.

### 14.5 贡献与意义表达
- 骨架：The results suggest that plasticity and crimp-like imperfections jointly control domain evolution in tendon-like composites.

### 14.6 局限与未来工作表达
- 骨架：The unloaded crimp state is treated as stress-free, while real tissues may contain residual stresses that require future characterization.

## 15. 引用策略与文献使用
引用分工明确。tendon/ligament 文献用于证明现象和生物意义；Bigoni/Gourgiotis、layered rock/seashell 等用于扩大 pattern 类比；Furer and Castañeda、d’Avila、Part I 用于理论基准；有限变形塑性和周期性边界文献用于方法合法性。

gap 依靠 Part I 制造：Part I 越清楚，Part II 的新增变量越明确。引用风险是如果读者没读 Part I，本文需要足够自洽；当前通过摘要和引言解释了 Part I 的 principal path、LOE 和 post-bifurcation 含义。

## 16. 审稿人视角风险
最大攻击面：二维 laminate 对 tendon 的代表性；crimp 初始 stress-free 假设；塑性参数与真实 collagen 的对应；domain formation 与 actual damage 的因果关系；缺少直接实验图像对照。

claim 是否过强：生物解释部分应保持 “may” 和 “suggest” 级别。证据是否不足：数值机制丰富，但定量实验验证不够。替代解释：真实 tendon 的 fluid flow、cell-matrix interaction、fibril sliding 和 damage accumulation 都可能参与 chevron pattern。

## 17. 可复用资产
- 可复用选题角度：对 companion theory 做 imperfection robustness test。
- 可复用 gap：完美理论解释机制，真实几何缺陷决定 onset 和加载路径相关性。
- 可复用论证链：Part I 基准 -> 小缺陷验证 -> 大缺陷偏离 -> 塑性参数调控 -> 生物现象解释。
- 可复用图表：几何扰动图、LOE vertical marker、phase response、塑性云图、非单调加载形貌。
- 不宜直接模仿：没有实验支撑时，不要把 numerical domains 直接等同病理损伤。

## 18. 对我写论文的启发
这篇适合学习“理论续篇”怎么写：不是重复 Part I，而是用一个现实变量检验理论边界。若我要写类似论文，可以先建立一个完美模型，再系统加入 imperfection、noise、manufacturing defect 或 loading history，说明哪些结论稳健，哪些结论被真实因素改写。

Introduction 可迁移“真实对象不完美”写法；Results 可迁移“每次只引入一个复杂因素”的节奏；Conclusion 可迁移“理论一致性 + 新现象 + 真实意义”的三段式。

## 19. 最终浓缩
这篇论文最值得学：用小缺陷验证完美理论，用大缺陷解释真实 tendon 中拉伸加载下的 domain formation，把 Part I 的抽象分岔推向生物相关性。

这篇论文最大风险：理想二维层合板和真实 tendon 的距离仍大，特别是残余应力、三维结构和损伤演化未闭合。

三个可迁移动作：
1. 把 companion paper 的理论结果作为基准，而不是重新铺一遍。
2. 用 imperfection amplitude/type/wavelength 建立真实因素的参数地图。
3. 在结论中区分“理论上验证”和“对真实材料的启示”。
