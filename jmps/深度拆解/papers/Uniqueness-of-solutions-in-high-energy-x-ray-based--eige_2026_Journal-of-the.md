# Uniqueness of solutions in high-energy x-ray based 'eigenstrain tomography' and other inverse eigenstrain problems: Counter examples and necessary conditions for well-posedness

## 0. 读取说明
- 源 PDF：`jmps/文献/Uniqueness-of-solutions-in-high-energy-x-ray-based--eige_2026_Journal-of-the.pdf`
- 源 TXT：`jmps/文本/txt/Uniqueness-of-solutions-in-high-energy-x-ray-based--eige_2026_Journal-of-the.txt`
- 辅助参照：上一轮标准拆解用于核对主线，本文件重新按深度模板展开。
- 是否需要结合 PDF 图像核查：需要。TXT 能读到数学论证、图注和结论，但 null field 的可视化、花形拟合图、边界示意图需看 PDF。
- 本文类型：逆问题理论 + 显式反例 + 唯一性充分条件 + eigenstrain 表示空间必要条件。它不是实验论文，图像主要是数学反例可视化。
- 阅读覆盖：摘要、Introduction、残余应力 eigenstrain 理论、一/二分量非适定性、剪切/法向三分量恢复、最小 eigenstrain 要求、Conclusions、附录证明。

## 1. 基本信息与论文身份
- 题名：Uniqueness of solutions in high-energy x-ray based 'eigenstrain tomography' and other inverse eigenstrain problems: Counter examples and necessary conditions for well-posedness
- 作者/机构：C.M. Wensrich, S. Holman, W.B.L. Lionheart, M. Courdurier, R.R. Jackson。完整机构以 PDF 为准。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 212 (2026) 106596。
- DOI：10.1016/j.jmps.2026.106596
- 关键词：Eigenstrain tomography；Residual stress；Eigenstrain method；Strain tomography；X-Ray diffraction；Poorly vector fields。
- 研究对象：高能 X 射线衍射应变测量结合 eigenstrain 方法反演三维残余应力的唯一性问题。
- 研究尺度：连续弹性体三维场；数学空间包括平衡应力场、弹性应变场、eigenstrain 表示空间。
- 方法类型：Hooke 各向同性弹性、平衡方程、零牵引边界、Maxwell potential、Fourier/cosine null fields、PDE 唯一性证明、弱形式论证。
- 证据类型：单/双分量测量非唯一的显式反例；三剪切分量或三对角分量足够恢复全应变的证明；任意残余应力可由对角 eigenstrain 生成；各向同性 eigenstrain 不完备。
- 目标读者：残余应力、X-ray diffraction tomography、逆问题、实验力学、计算重构算法读者。
- JMPS 风格定位：以严格数学判定约束一个热门实验-计算方法。它的价值在于“负结果 + 最低可行条件”。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先说明 eigenstrain tomography 的技术愿景；再指出唯一性尚未明确；随后构造单分量重构非唯一反例；接着给三分量充分条件；最后给一般 inverse eigenstrain 问题中的对角/各向同性 eigenstrain 结论。
- 背景句承担什么：把高能 X 射线测量与残余应力重构连接起来，说明这是工程上有吸引力的方法。
- gap 句承担什么：唯一性未建立，意味着数值优化给出的解可能只是正则化选择。
- 方法句承担什么：通过反例和证明处理 well-posedness，而不是提出更强正则化算法。
- 结果句承担什么：明确“一个或两个分量不够，三个合适分量够”；同时指出 eigenstrain 搜索空间可限于对角但不能限于 isotropic。
- 意义句承担什么：给出实验和计算最小要求，防止不适定重构被误用。
- 一句话主张：单/双应变分量的 eigenstrain tomography 本质上不唯一；要保证三维残余应力重构适定，至少需要三组合适应变分量，并且 eigenstrain 表示空间不能被过度限制为各向同性。
- 3-5 个核心关键词：non-uniqueness；null strain field；well-posedness；diagonal eigenstrain；minimum reconstruction requirements。

## 3. 选题层深拆
- 问题来源：高能 X 射线 diffraction 几何下，某一方向的应变分量较容易通过标量 tomography 得到；近期方法希望用 eigenstrain 和弹性平衡从单分量恢复完整残余应力。
- 问题为什么重要：若唯一性不成立，重构结果可能由正则化、基函数选择或先验假设决定，而非由测量数据决定。工程上这会导致看似物理合理但实际不可辨识的残余应力场。
- 问题为什么现在值得做：相关实验和算法已经出现，且有减少扫描次数的强需求；此时给出数学下限能及时规范方法发展。
- 问题边界：主要考虑均匀各向同性线弹性、无体力、零牵引边界、已知全场分量；真实 ray transform、噪声、各向异性和复杂边界属于后续问题。
- 选题的 JMPS 味道：用力学理论和逆问题数学澄清实验方法的最小可行条件，是 JMPS 偏好的“mechanics-informed measurement”题型。
- 选题可迁移性：所有数据驱动反演都可学习：先问唯一性和 null space，再谈算法精度。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：传统 diffraction strain tomography 可通过多个旋转轴得到完整张量；eigenstrain tomography 试图减少测量需求；residual stress/eigenstrain 方法提供计算框架；近期单分量实现引发唯一性问题。
- 主要研究流派/方法路线：测量几何路线关注可测分量；eigenstrain 反演路线用不相容应变源表示残余应力；数学逆问题路线关注唯一性、稳定性和 null space。
- 每类研究解决了什么：多轴测量可完整采样但实验成本高；eigenstrain 方法将场重构转成有限参数优化；残余应力理论给平衡和边界约束。
- 每类研究留下什么不足：少分量测量是否唯一不清；正则化可能隐藏不可观测自由度；过窄 eigenstrain 基底可能排除真实应力。
- 本文站在哪条线上：站在残余应力理论和逆问题唯一性分析线上，对近期单分量方法提出反例并给替代最低条件。
- 最接近前人工作：Uzun/Korsunsky 等高能 X-ray eigenstrain tomography 实现，Lionheart/Withers 等 diffraction tomography 理论，Eshelby/Mura/Korsunsky eigenstrain 基础。
- 是否公平处理前人：较直接但有建设性。作者明确指出近期方法的问题，同时给出三分量和对角 eigenstrain 作为可行路线。

## 5. Gap 制造机制
- 明示 gap：eigenstrain tomography 的重构唯一性尚未清楚建立，尤其是从一个测量分量恢复全场。
- 隐含 gap：数值正则化会选择某个解，但不会证明测量数据唯一决定该解；因此已有成功案例不能代替适定性证明。
- gap 类型：逆问题适定性 gap + 实验设计最低要求 gap + 计算基底约束 gap。
- gap 证据来自哪里：Introduction 介绍测量几何和近期方法；第 3 节构造满足平衡/边界且特定分量为零的非零场，直接证明不可观测自由度。
- gap 是否足够窄：窄而硬。围绕“几个应变分量足够”展开。
- gap 是否足够重要：非常重要。唯一性是反演方法可信性的前置条件。
- 如果我是审稿人会如何追问：证明中的“已知全场分量”与真实 X-ray ray transform 是否一致？噪声和离散化下三分量是否稳定？复杂几何是否仍成立？作者将部分问题留为 further questions。

## 6. 创新性判断
- 作者声称的贡献：给单/双分量 eigenstrain tomography 非唯一反例；证明三剪切或三法向分量可唯一恢复；证明任意 residual stress 可由 diagonal eigenstrain 生成而 isotropic eigenstrain 不足。
- 我判断的真实创新：把“少测几个分量”的工程愿望转化为严格数学边界，并用具象 null field 让不可观测空间可见。
- 创新类型：理论反例、唯一性证明、方法规范。
- 创新强度：强。因为它直接改变某类实验重构方法的可接受条件。
- 创新必要性：必要。没有唯一性，下游的误差、分辨率和算法优化都没有可靠意义。
- 创新与证据匹配度：反例和证明与 claim 高度匹配；实验实现层面的 claim 较谨慎。
- 容易被挑战的创新点：实际测量不是直接全场分量，三分量充分性到实验扫描设计还有一层算法距离。

## 7. 论证链条复原
背景：高能 X-ray diffraction 可以测局部弹性应变投影，并有潜力无损重构三维残余应力。

文献：传统方法需要多方向测量完整张量，eigenstrain tomography 试图利用弹性理论减少测量。

gap：少分量测量是否唯一没有严格结论。

问题：从一个、两个或三个应变分量能否唯一恢复全弹性应变/残余应力？

方法：先构造满足平衡和零牵引的非零 null fields，使某些测量分量为零；再证明三剪切或三对角分量在边界条件下足够；最后分析 eigenstrain 表示空间。

证据：立方体上的 cosine null basis；`N=2` 简单反例；`N=8` 可拟合花形图案的巨大 null space；PDE 唯一性证明；对角 eigenstrain 和 isotropic eigenstrain 的构造/反构造。

发现：一/二分量不适定；三剪切或三对角分量可唯一恢复；对角 eigenstrain 足够生成任意 residual stress，isotropic eigenstrain 不足。

机制：不可观测场存在于测量算子的 null space 中，平衡和零牵引并不能消除它们；只有足够多独立分量才能关闭自由度。

意义：实验扫描方案和 eigenstrain 重构基底必须满足最低数学要求。

## 8. 方法/理论/模型细拆
- 方法总框架：将 residual stress 写成由 eigenstrain 诱导的自平衡应力；用 Hooke 定律联系应力和弹性应变；研究已知部分应变分量时其余分量是否被平衡和边界唯一确定。
- 关键概念：eigenstrain；elastic strain tensor；residual stress；zero-traction boundary；Maxwell potential；null field；well-posedness；diagonal/isotropic eigenstrain。
- 关键变量/参数：应力 `sigma_ij`、应变 `epsilon_ij`、eigenstrain、Poisson ratio、Young's modulus、Fourier/cosine 模式阶数 `N`、域 `Omega`。
- 核心假设：各向同性线弹性；无体力；边界零牵引；足够正则或弱意义；部分结论在凸域边界条件下成立。
- 边界条件：反例在立方体中满足零牵引；三分量恢复证明中利用任意凸域上法向和切向导数关系。
- 方法步骤：1. 定义 eigenstrain 残余应力理论；2. 构造一/二分量不可见的非零应力/应变场；3. 展示 null space 维数随 `N` 增长；4. 证明剪切分量恢复；5. 证明法向分量恢复；6. 分析 eigenstrain 搜索空间最低要求。
- 复现信息：数学构造和公式充分；图像复现需要生成 null basis 和 least-squares 拟合过程。
- 方法复杂度是否合理：合理。唯一性问题需要负例和正例并行，否则只批判不建设。
- 方法与 gap 的对应关系：gap 是 well-posedness 未知，方法直接输出非唯一反例和充分条件。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 单分量 eigenstrain tomography 非唯一 | 摘要、第 3 节 | 满足 `epsilon_33=0` 等条件的非零 null field | 显式反例 | 强 | 针对理想化全场分量 |
| 二分量重构也可非唯一 | 第 3 节 | 构造 `epsilon_22=epsilon_33=0` 但应力非零场 | 显式反例 | 强 | 域和材料假设 |
| 三剪切分量足以恢复全应变 | 摘要、第 4 节 | 从剪切分量推导其余分量的 PDE/边界唯一性 | 数学证明 | 强 | 实验能否测得三剪切另说 |
| 三对角分量足以恢复全应变 | 摘要、第 5 节 | 正常分量恢复和边界条件证明 | 数学证明 | 强 | 凸域/正则性条件需注意 |
| 任意残余应力可由对角 eigenstrain 生成 | 摘要、第 6 节 | 构造和证明 | 理论证明 | 强 | 数值表示效率另论 |
| isotropic eigenstrain 不能生成所有 residual stress | 摘要、第 6 节 | 反例/必要条件 | 理论证明 | 强 | 实际样品若近似 isotropic source 仍可能可用但不普适 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 高能 X-ray 测量几何 | 单次扫描得到有限应变信息 | 说明为什么少分量测量有诱惑 | 是 |
| eigenstrain 残余应力基本公式 | 理论基础 | 应力由 eigenstrain 诱导 | 建立反演问题 | 否 |
| null field 构造公式 | 非唯一反例 | 一/二分量不可唯一 | 数学上直接击穿方法 | 否 |
| Fig. 2 | `N=2` 简单 null field 可视化 | 非零场可在测量分量中不可见 | 让抽象反例可视化 | 是 |
| Fig. 3 | `N=8` null basis 拟合花形图案 | null space 很大 | 显示不适定不是小特例 | 是 |
| Fig. 4 | 边界条件示意 | 三分量恢复证明 | 帮助理解凸域边界约束 | 是 |
| 定理/猜想/附录证明 | 唯一性和 eigenstrain 表示 | 最低要求 | 把负结论变成建设性条件 | 否，需核对符号 |

图表顺序服务论证的方式：Fig. 1 说明实验问题，Fig. 2-3 把非唯一性从数学变成视觉冲击，Fig. 4 支撑正向唯一性证明。图少但功能集中。

## 11. 章节结构与篇章布局
- Abstract：直接给负结论、正条件和 eigenstrain 表示条件，信息密度高。
- Introduction：从测量几何和近期单分量方法切入，提出 central question。
- Related Work/Background：第 2 节回顾 eigenstrain theory of residual stress。
- Method/Theory/Model：第 3-6 节都是理论结果，但功能不同：反例、剪切恢复、法向恢复、最低 eigenstrain 要求。
- Results：数学论文中结果即 theorem/counterexample；图像只辅助理解。
- Discussion：第 7 节 Conclusions and further questions 把结果翻译成实验要求和未来问题。
- Conclusion：提出最小三分量要求，并提醒正则化不能修复本质非唯一。
- 章节之间如何过渡：先负后正：打破单分量方法，再给三分量可行路线，最后给计算 eigenstrain 基底建议。
- 哪一节最值得模仿：第 3 节。用显式反例批判方法，比抽象质疑更有杀伤力。
- 哪一节可能存在结构风险：第 5 节边界条件证明对非数学读者较难，需要图和符号表辅助。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Uniqueness-of-solutions-in-high-energy-x-ray-based--eige_2026_Journal-of-the.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：引用/附录型, 描述型, 方法/模型型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Eigenstrain theory of residual stress | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3 Ill-posedness of 1 and 2 component eigenstrain tomography | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2 See Appendix A for notation and spaces used throughout this paper | 引用/附录型 | 提供支撑材料、声明或文献来源 | 高 | 否 | 保留具体变量/对象 |
| 5.1 General solutions for (11) | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.2 Boundary conditions on an arbitrary convex domain | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 6 Minimum requirements of reconstructed eigenstrains | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 7 Conclusions and further questions on uniqueness | 结论/展望型 | 收束贡献、边界和未来工作 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：技术愿景 -> 测量几何 -> 近期方法 -> 唯一性质疑 -> 本文问题列表。
- Method 段落推进：定义空间和方程 -> 提出 question/remark/conjecture/theorem -> 给证明或反例 -> 解释对 tomography 的含义。
- Results 段落推进：每个数学结果后都有工程翻译，说明实验至少要测什么。
- Discussion/Conclusion 段落推进：从具体高能 X-ray 回到一般 inverse eigenstrain 问题。
- 常见段落开头方式：`We now show...`；`To summarise...`；`This poses a significant issue...`。
- 常见段落收束方式：以 well-posedness、minimum requirements 或 further questions 收束。
- 可复用段落模板：热门方法 claim -> 构造同测量数据下的两个不同物理场 -> 说明正则化只能选解不能保唯一 -> 给最低额外数据条件。

## 13. 文笔画像与语言习惯
- 整体语气：数学审稿人式，冷静但锋利。
- claim 强度：对证明结果使用强 claim；对实验实践使用条件化表达。
- 谨慎表达：`provided that`、`in the weak sense`、`under these assumptions`、`further questions`。
- 问题表达：`central question`、`minimum requirements`、`well-posedness`、`non-uniqueness`。
- 贡献表达：`we demonstrate`、`we prove`、`we construct`、`we conclude`。
- 机制表达：`null space`、`regularisation`、`zero-traction boundary`、`diagonal eigenstrain`。
- 对比表达：`Conversely`、`notwithstanding`、`while this may be feasible`。
- 限定边界表达：材料、域、边界和测量分量条件都限定清楚。
- 术语密度：高，但以数学和弹性理论术语为主。
- 长句/短句习惯：证明段长句多；结论句短且硬。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：components(60)；eigenstrain(48)；strain(44)；diagonal(40)；stress(39)；elds(36)；any(35)；form(33)；boundary(29)；elastic(24)；three(22)；wensrich(21)；residual(20)；component(20)；tensor(19)；follows(19)；vector(18)；process(18)；eld(17)；solution(17)
- 高频学术名词：strain(44)；stress(39)；solution(34)；condition(32)；analysis(12)；conditions(12)；approach(11)；solutions(11)；hence(11)；question(10)；function(10)；raction(9)；reconstruction(9)；direction(9)；equations(7)；method(7)
- 高频学术动词：shown(10)；solve(5)；demonstrate(3)；show(2)；shows(2)；suggest(1)；demonstrated(1)
- 高频形容词：elastic(48)；diagonal(40)；boundary(29)；residual(20)；component(20)；general(16)；numerical(14)；isotropic(12)；arbitrary(12)；possible(11)；normal(11)；homogeneous(8)；experimental(6)；measurement(6)；tomographic(6)；perspective(6)
- 高频副词/连接副词：poorly(10)；uniquely(9)；however(7)；cally(6)；generally(4)；approximately(4)；directly(3)；actually(3)；imply(3)；similarly(3)；explicitly(3)；furthermore(2)；numerically(2)；clearly(2)；commonly(2)；additively(2)
- 高频二词短语：diagonal components(22)；residual stress(20)；elastic strain(19)；eigenstrain tomography(12)；boundary condition(11)；shear components(9)；every point(9)；boundary conditions(9)；vector elds(8)；stress eld(8)；killing elds(8)；eigenstrain problems(7)；components zero(7)；inverse eigenstrain(6)；x-ray raction(6)；three diagonal(6)
- 高频三词短语：inverse eigenstrain problems(6)；residual stress elds(5)；three diagonal components(5)；zero-traction boundary condition(5)；residual stress eld(5)；killing conformal killing(5)；writing review editing(5)；review editing writing(5)；editing writing original(5)；writing original draft(5)；investigation formal analysis(5)；conformal killing elds(5)

**主动、被动与句法**

- 被动语态估计次数：69
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：401
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：184
- 一般过去时线索：30
- 现在完成时线索：11
- 情态动词线索：64
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：eigenstrain(10)；tomography(5)；strain(4)；stress(4)；x-ray(3)；inverse(3)；university(3)；residual(3)
- 1. Introduction：strain(11)；elastic(9)；raction(6)；sample(6)；rotation(5)；high-energy(4)；uzun(4)；korsunsky(4)
- 2. Eigenstrain theory of residual stress：eigenstrain(9)；elastic(6)；body(6)；strain(6)；stress(5)；problem(5)；approach(4)；eld(4)
- 3. Ill-posedness of 1 and 2 component eigenstrain tomography：components(25)；boundary(16)；stress(14)；strain(14)；diagonal(13)；form(12)；shear(9)；eld(8)
- 5.1. General solutions for (11)：functions(4)；form(3)；arbitrary(3)；notation(3)；general(3)；solution(3)；provides(2)；note(2)
- 5.2. Boundary conditions on an arbitrary convex domain：components(7)；boundary(6)；condition(6)；follows(6)；proof(5)；general(4)；any(4)；point(4)
- 6. Minimum requirements of reconstructed eigenstrains：eigenstrain(12)；stress(8)；diagonal(8)；any(7)；form(7)；eigenstrains(6)；residual(6)；components(6)
- 7. Conclusions and further questions on uniqueness：elds(21)；diagonal(15)；any(14)；components(13)；killing(13)；vector(11)；writing(10)；eigenstrain(9)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`the uniqueness of such reconstructions has not yet been clearly established.`
- 可复用句型骨架：`Despite successful demonstrations, the uniqueness of the underlying inverse problem remains unresolved.`
- 中文写作启发：评价反演方法先问“底层问题”而非“案例效果”。

### 14.2 方法与框架表达
- 原文表达模式：构造 explicit counterexamples demonstrating non-uniqueness。
- 可复用句型骨架：`We construct explicit null fields that satisfy all governing equations and boundary conditions while remaining invisible to the measured components.`
- 中文写作启发：负结果最好可构造、可视化，而不是只说“不稳定”。

### 14.3 结果与趋势表达
- 原文表达模式：三剪切或三对角分量足以唯一恢复。
- 可复用句型骨架：`Uniqueness is recovered once three mutually independent components, such as A or B, are prescribed throughout the domain.`
- 中文写作启发：批判后必须给可执行替代条件。

### 14.4 机制解释表达
- 原文表达模式：正则化隐式选择不可观测 null components。
- 可复用句型骨架：`Regularisation may select one member of the admissible family, but it cannot make the data determine that member uniquely.`
- 中文写作启发：这是所有正则化反演论文都可复用的审稿句型。

### 14.5 贡献与意义表达
- 原文表达模式：establish rigorous minimum experimental and computational requirements。
- 可复用句型骨架：`These results establish minimum measurement and representation requirements for a well-posed reconstruction.`
- 中文写作启发：理论论文的意义可写成“最低要求”。

### 14.6 局限与未来工作表达
- 原文表达模式：further questions on uniqueness。
- 可复用句型骨架：`The present uniqueness result addresses the ideal full-field setting; stability under noisy line-integral data remains an open question.`
- 中文写作启发：区分 uniqueness 和 stability，显得专业。

## 15. 引用策略与文献使用
- 引用密度：Introduction 集中，正文证明自足。
- 引用主要集中位置：X-ray diffraction tomography、eigenstrain theory、近期单分量方法。
- 经典文献用途：残余应力和 eigenstrain 基础。
- 近年文献用途：提供被审视的最新方法和实验动机。
- 方法文献用途：逆问题和 tomography 理论背景。
- 对比/批判性引用：对近期方法明确指出“可能物理可行但无理由认为为真”这类尖锐判断。
- gap 如何靠引用搭建：用近期实现说明问题迫切，用经典理论说明分析工具成熟。
- references 暗示的研究共同体：实验力学、残余应力、数学 tomography、弹性理论。
- 引用风险：直接批评近期工作，需要确保描述准确；若该方法另有隐含先验，需公平讨论。

## 16. 审稿人视角风险
- 最大攻击面：理想全场分量与真实高能 X-ray 数据采集之间的差距。
- claim 是否过强：对数学 setting 不过强；若读作所有实验流程都已解决则过强。
- 证据是否不足：对噪声稳定性、有限视角和离散算法没有充分证据。
- 方法是否可复现：反例和证明可复现；图像生成需代码。
- 对比是否充分：对单分量方法足够直接；对其他正则化/先验方法可能未穷尽。
- 边界条件是否清楚：清楚，但技术性强。
- 替代解释是否排除：正则化作为替代被指出不能提供唯一性。
- 图表是否需要进一步核查：Fig. 2-4 需 PDF，尤其花形 null field 的说明。

## 17. 可复用资产
- 可复用选题角度：热门反演方法先做适定性审计。
- 可复用 gap 制造方式：`方法已演示 -> 唯一性未证明 -> 构造 null space -> 提出最低数据要求`。
- 可复用论证链：实验几何 -> 数学模型 -> 反例 -> 充分条件 -> 计算基底建议。
- 可复用图表设计：用具象图案拟合展示 null space 巨大。
- 可复用段落结构：Question/Remark/Theorem/Consequence 的理论组织方式。
- 可复用句型骨架：`Regularisation cannot remove non-uniqueness inherent in the data.`；`Minimum requirements are therefore...`。
- 可复用引用组织：以最新争议方法为入口，向经典理论回溯。
- 不宜直接模仿之处：直接点名批评需要硬证明；否则容易引发审稿冲突。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：负结果论文要给反例，也要给建设性替代条件。
- 可以迁移到 Introduction 的写法：从实验便利性诱惑切入，再指出便利性可能以唯一性为代价。
- 可以迁移到 Method 的写法：先定义 ideal problem，再明确证明只在该 setting 下成立。
- 可以迁移到 Results/Discussion 的写法：每个 theorem 后都翻译成实验/算法要求。
- 需要避免的问题：不要把 uniqueness、stability、algorithmic convergence 混成一个概念。

## 19. 最终浓缩
- 这篇论文最值得学：如何用显式 null field 把“反演不适定”讲得既数学严格又直观。
- 这篇论文最大风险：理论 setting 与真实 X-ray 数据流程之间仍有距离。
- 三个可迁移动作：1. 先找 null space；2. 负结论后给最低可行条件；3. 用图像把抽象不可辨识性可视化。
