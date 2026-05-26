# Torque hyperuniformity in frictional granular matter - theory and experiments

## 0. 读取说明
- 源 PDF：`jmps/文献/Torque-hyperuniformity-in-frictional-granula_2026_Journal-of-the-Mechanics-a.pdf`
- 源 TXT：`jmps/文本/txt/Torque-hyperuniformity-in-frictional-granula_2026_Journal-of-the-Mechanics-a.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 213 (2026) 106621, DOI: 10.1016/j.jmps.2026.106621。
- 是否需要结合 PDF 图像核查：需要。当前拆解依据 txt、图注和正文叙述；Fig. 1 的装置照片、Fig. 3-8 的曲线斜率、二维结构因子颜色/方向性、Fig. 9 的示意图细节均需回 PDF 核查。
- 本文类型：理论预测的实验确认与扩展论文，兼具短综述、实验报告和机制讨论。它不是从零推导理论，而是把 frictional granular matter 中 torque fluctuation hyperuniformity 的条件放到真实光弹颗粒实验中检验。

## 1. 基本信息与论文身份
- 题名：Torque hyperuniformity in frictional granular matter - theory and experiments。
- 作者/机构：Jin Shang、Jie Zhang、Itamar Procaccia；北航杭州国际创新研究院、上海交通大学、North University of China、Weizmann Institute 等。
- 关键词：Granular matter; Hyperuniformity; Elastic theory。
- 研究对象：二维摩擦颗粒堆积，包括圆盘在各向同性压缩、圆盘在纯剪切、椭圆颗粒在各向同性压缩三类体系。
- 研究尺度：接触力层面的 torque/pressure 定义，窗口积分方差，傅里叶结构因子，小波数极限，大尺度应力相关。
- 方法类型：光弹颗粒实验 + 接触力反演 + 统计窗口采样 + 结构因子分析 + 理论物理解释。
- 证据类型：方差随窗口半径 R 的标度、S(k) 在 k -> 0 的行为、剪切下二维结构因子的各向异性、椭圆体系中法向力也产生 torque 的对照。
- 目标读者：无序固体、颗粒物理、弹性理论、超均匀性、非哈密顿摩擦体系中的应力统计研究者。
- JMPS 风格定位：典型“理论约束 -> 可测条件 -> 多实验场景验证 -> 机制解释 -> 维度推广”的短而硬论文。最强贡献不是装置创新，而是把抽象条件“torque fluctuations must be hyperuniform”变成可观测统计事实。

## 2. 摘要与核心信息提取
摘要采用“问题-理论状态-实验缺口-本文验证-物理解释”的结构。开头把问题提升到基本层面：摩擦颗粒集合是否会呈现由弹性 Green 函数控制的长程各向异性应力自相关。随后区分 Hamiltonian central-force 系统和 frictional 系统：前者在力学平衡、材料各向同性和压力涨落 normal 的条件下，应力相关由压力相关决定；后者因为摩擦破坏局部应力对称性，必须额外引入 torque autocorrelation。摘要的关键句法不是“我们发现了新现象”，而是“理论上已经指出条件，实际材料是否普遍满足需要实验确认”。

一句话主张：二维摩擦颗粒体系中，扭矩涨落在圆盘各向同性压缩、圆盘剪切和椭圆颗粒压缩中都表现为超均匀；这种边界主导的 R 标度使 torque 对长程应力相关的贡献在大尺度上次要，从而支持摩擦颗粒中 elastic-like stress correlation 的理论条件。

摘要中的功能分工：
- 背景句：用 amorphous solids、granular matter、stress autocorrelations 建立领域重要性。
- gap 句：理论提出 pressure + torque 两个标量函数决定摩擦体系应力相关，但真实实验是否满足 torque hyperuniformity 未充分确认。
- 方法句：使用可测接触力的二维光弹颗粒体系，比较圆盘各向同性加载、圆盘剪切和椭圆颗粒加载。
- 结果句：三类体系中 torque variance 随 R 线性增长，S_tau(k) 在小 k 消失；pressure 在剪切时可偏离 normal。
- 意义句：给出直观解释，并预测 d 维中 torque variance 随 R^(d-1) 增长。

核心关键词：torque hyperuniformity; pressure normal fluctuations; stress autocorrelation; frictional granular packing; structure factor; boundary contribution。

## 3. 选题层深拆
问题来源不是工程性能，而是理论物理中的一个未闭合条件：长程应力相关是否是无序固体的普遍弹性后果，还是只在特定玻璃制备条件下出现。此前在 Hamiltonian amorphous solids 中，应力自相关的远场形式可由 mechanical balance、material isotropy、normal pressure fluctuations 推出。但摩擦颗粒不满足局部应力对称性，接触力含切向摩擦，局部 torque 不可忽略，理论结构变成 pressure 与 torque 两个自相关函数共同决定。

为什么重要：如果应力相关具有幂律衰减，远距离区域并不独立，这会影响热力学极限、力链统计、颗粒材料的宏观响应和无序固体 relaxation 的理解。对颗粒物来说，sand、soils、powders 都属于摩擦体系，不能直接沿用 central-force 玻璃的结论。

为什么现在值得做：近期理论工作已经把摩擦体系的条件说清楚，即 pressure 要 normal，torque 要 hyperuniform。理论命题的自然下一步就是实验检验。作者的实验系统恰好能通过光弹技术反演每个接触的法向/切向力，从而直接计算 torque 与 pressure，而不是只测宏观应力。

问题边界很清楚：二维光弹颗粒；准静态加载；圆盘和椭圆；窗口积分与结构因子；关注 torque fluctuations 是否 hyperuniform，不试图完整测量所有 stress autocorrelation 分量。剪切实验还主动承认材料各向同性条件会被破坏，因此主要用来测试 torque hyperuniformity 的鲁棒性，而不是证明剪切态仍满足完整 elastic-like stress correlation 条件。

JMPS 味道在于它把抽象场论条件转换为可观测尺度律：variance grows like R 而不是 R^2；structure factor vanishes at k=0。选题不是“颗粒实验又测了一次力链”，而是“实验是否确认理论要求的统计约束”。

## 4. 领域位置与文献版图
作者将文献组织成三条线。第一条是 amorphous solids 的宏观力学难题：塑性变形、Boson peak、拓扑转变、剪切带和断裂等，说明无序固体不能简单套用经典弹性介质。第二条是 inherent state stress correlations：超冷液体、局部重排和弹性应变印记导致的长程相关，说明该问题跨越固体和液体 relaxation。第三条是理论约束线：Hamiltonian systems 的 stress autocorrelation 由 pressure autocorrelation 决定；frictional systems 需要 torque autocorrelation，并要求 torque hyperuniform。

代表性文献功能：
- Henkes and Chakraborty、Lemaitre 系列：作为 stress correlation 理论基础。
- Torquato and Stillinger：定义 hyperuniformity 的概念源头。
- Shang et al. 2026：圆盘各向同性压缩中已经宣布的确认结果，是本文的前置实验。
- Majmudar and Behringer、Wang 等：力反演算法与光弹颗粒实验方法基础。
- Lemaître et al. 2021b/2021c：摩擦颗粒理论与剪切导致 pressure hyperfluctuation 的解释背景。

本文站在“已有理论之后、已有单一圆盘实验之后”。它的增量是把确认从一个最干净的圆盘各向同性体系扩展到两个更难体系：各向异性剪切态，以及椭圆中法向力也能产生 torque 的非圆形接触几何。这个定位很稳，因为它没有冒充全新理论，而是强调“theoretical discovery required experimental confirmation”。

是否公平处理前人：总体公平。作者承认 Hamiltonian 情况已被较充分解决，也承认圆盘各向同性压缩结果已近期报道。潜在不足是文献版图偏向同一理论共同体，对颗粒力链、剪切诱导各向异性、非圆颗粒统计的实验文献展开不多。

## 5. Gap 制造机制
显式 gap：理论指出摩擦颗粒中 torque fluctuations 必须 hyperuniform 才能使其对应力自相关的贡献在大尺度次要，但真实摩擦物质是否普遍服从这一条件，需要实验确认。

隐含 gap：已有确认主要针对 isotropically loaded frictional disks，圆盘中 torque 只来自切向摩擦力；如果换成剪切加载或椭圆颗粒，体系的各向同性、接触几何和 torque 来源都会改变，原结论是否仍成立并不显然。

gap 类型：理论验证 gap + 对象扩展 gap + 鲁棒性 gap。它不是“没人研究过椭圆颗粒”这类对象 gap，而是“理论条件在更一般摩擦接触几何下是否仍成立”的机制 gap。

gap 证据来自三层：
- 理论层：friction breaks Hamiltonian symmetry，stress correlation matrix 不再只由 pressure 决定。
- 方法层：必须测到每个接触的法向和切向力，实验选择受限。
- 现象层：剪切会破坏 isotropy，椭圆会让 normal force contribute to torque，这些都是对理论条件的压力测试。

如果我是审稿人会追问：三类二维体系是否足以支持“generic”或“universally obeyed”的语气？剪切态中 pressure 已偏离 normal 时，torque hyperuniformity 对完整应力相关的意义是否应更谨慎？椭圆实验的粒子数、独立样本数和边界剔除是否足够支撑小 k 外推？

## 6. 创新性判断
作者声明的贡献：回顾圆盘各向同性压缩结果，并新增圆盘剪切与摩擦椭圆压缩实验，确认 torque fluctuation hyperuniformity；给出物理解释，并预测 d 维推广。

真实创新有三点。第一，实验确认创新：把抽象 torque field 的超均匀条件用光弹颗粒接触力直接验证。第二，鲁棒性创新：在剪切破坏 pressure normality 和椭圆增加 normal-force torque 的条件下，torque hyperuniformity 仍成立。第三，解释创新：用“颗粒净 torque 为零导致窗口内部联系抵消，只有边界接触贡献”的图像解释为什么 variance 与周长而不是面积成比例。

创新强度：中高。理论本身不是本文原创，圆盘各向同性结果也不是完全新，但“同一条件在更复杂摩擦体系中仍成立”的实验支撑对 JMPS 读者有价值。尤其 Fig. 9 的边界解释使结论不只是经验拟合。

创新必要性强。没有实验，理论条件只是形式要求；没有剪切/椭圆扩展，读者可能认为 torque hyperuniformity 是圆盘、各向同性或切向摩擦特殊性造成的。

容易被挑战之处：二维系统能否代表三维；剪切态下 material isotropy 失效后，作者仍如何界定 elastic-like decay 的适用；小 k 极限受有限尺寸和窗口重叠影响；椭圆系统压力范围与圆盘不同，材料也不同，直接比较应谨慎。

## 7. 论证链条复原
背景 -> 无序固体的长程应力相关影响力学响应和热力学极限。

文献 -> Hamiltonian central-force 系统中，机械平衡、各向同性和 normal pressure fluctuations 足以推出 elastic-like stress correlation。

gap -> 摩擦颗粒破坏局部应力对称性，理论要求 pressure 与 torque 两个场共同决定应力相关，其中 torque 必须 hyperuniform；真实体系是否满足未知。

问题 -> 在可反演接触力的光弹颗粒体系中，直接测量 pressure 与 torque fluctuations 的尺度律和结构因子。

方法 -> 定义接触层面的 torque field 与 pressure field；随机圆窗积分，计算方差随 R 的标度；计算结构因子 S(k) 并做角向平均；比较圆盘各向同性、圆盘剪切、椭圆压缩。

证据 -> 圆盘压缩中 torque variance ~ R，pressure variance ~ R^2，S_tau(k->0)=0；剪切下 pressure 出现 hyperfluctuation 和各向异性，但 torque 仍在各方向小 k 消失；椭圆中两种 aspect ratio 均显示 torque hyperuniformity。

发现 -> torque hyperuniformity 对加载方式和颗粒形状鲁棒；pressure 的 normality 依赖 isotropy，但 torque 的边界约束更基本。

机制 -> 每个颗粒的合 torque 为零，窗口内完整包含的接触对贡献抵消，只有被窗口边界切割的接触贡献，数量随边界长度增长，因此二维 variance ~ R。

意义 -> 预测 d 维 torque variance ~ R^(d-1)，为摩擦无序固体中的 elastic-like stress correlations 提供实验支撑，并建议三维数值模拟检验。

链条最强处是理论命题与可测标度的闭合。最弱处是从“这些实验体系”到“generically obeyed”的外推，需要谨慎措辞。

## 8. 方法/理论/模型细拆
核心概念一：normal fluctuations。对 d 维球半径 R 内的积分量 Q，若方差随 R^d 增长，即体积标度，则称 normal。压力场在各向同性圆盘压缩中表现为 normal。

核心概念二：hyperuniformity。若积分方差增长慢于 R^d，等价地结构因子在 k -> 0 消失，则为 hyperuniform。二维 torque variance ~ R 是边界标度，满足超均匀。

实验流程：制备双分散光弹圆盘或椭圆；准静态压缩或纯剪切；用偏振光成像获得力链图；通过 force-inversion algorithm 重构接触力；计算每个接触贡献的 torque 与 pressure；剔除边界若干层；随机采样圆窗 4000 次计算积分方差；对 30 个独立样本求结构因子平均。

关键变量/参数：
- r_i：颗粒中心或几何中心位置。
- r_ij：从颗粒中心到接触点的矢量。
- f_ij：接触力。
- tau：r_ij x f_ij 的面外分量。
- p：接触力沿接触几何方向的压力式标量。
- R：随机窗口半径。
- S_tau(k), S_p(k)：torque/pressure 的结构因子。
- phi、gamma、p_bar：填充率、剪切应变、平均压力。

方法与 gap 的对应：理论 gap 要求知道 torque autocorrelation，实验就必须重构接触力；鲁棒性 gap 要求改变加载和形状，实验就安排剪切圆盘与椭圆；小波数条件要求直接看 S(k->0)，所以作者同时给 real-space 方差和 Fourier-space 结构因子。

复现信息较好：粒子数量、尺寸、加载速率、填充率、压力窗口、采样次数、边界剔除、结构因子定义均有说明。但复现仍需要原始图像、接触力反演代码、误差处理和具体样本数量的完整数据。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 摩擦颗粒的应力相关由 pressure 和 torque 两个各向同性函数决定 | Introduction | Lemaitre et al. 理论结果回顾 | 理论文献 | 中强 | 本文未重新完整推导 |
| 圆盘各向同性压缩中 torque fluctuations hyperuniform | Section 3.3 / Fig. 3 | torque variance 随 R 线性增长，S_tau(k->0) 消失 | 实验统计 + 结构因子 | 强 | 需 PDF 核查拟合区间和误差条 |
| 圆盘压缩中 pressure fluctuations normal | Section 3.3 / Fig. 3 | pressure variance ~ R^2，S_p(k) 小 k 不消失 | 实验统计 | 强 | 有限尺寸大 R 偏离 |
| 纯剪切破坏 pressure normality，但 torque hyperuniformity 仍保持 | Section 3.5 / Fig. 4-6 | pressure 出现 R^2.5 和小 k 发散趋势；S_tau 在各方向小 k 消失 | 剪切实验 + 二维结构因子 | 中强 | 剪切态各向异性下角向平均解释需谨慎 |
| 椭圆颗粒中即使法向力也贡献 torque，torque 仍 hyperuniform | Section 4.3 / Fig. 8 | 两种 aspect ratio 椭圆体系 torque variance 近似 R，S_tau 小 k 趋零 | 形状对照实验 | 中强 | 椭圆材料/压力范围不同，需看样本统计 |
| torque hyperuniformity 的物理原因是单颗粒净 torque 为零导致窗口内抵消、边界贡献主导 | Section 5 / Fig. 9 | 窗口内接触对抵消，边界切割接触数随周长增长 | 机制解释 | 强 | 对非平衡、强体力矩或三维复杂接触需进一步验证 |
| d 维中 torque variance 预计随 R^(d-1) 增长 | Section 5 | 边界贡献从周长推广到表面积 | 理论外推 | 中 | 需三维数值或实验确认 |

证据链的特点是“双指标互证”：real-space 的方差标度负责给直观尺度律，Fourier-space 的 S(k) 负责对应超均匀定义。剪切案例进一步用二维 S(kx, ky) 避免仅靠角向平均掩盖各向异性。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Eq. (1) | 定义 hyperuniformity 的方差判据 | 方差增长慢于 R^d | 给全文统计标准 | 否 |
| Eq. (2) | 给出 S(k->0)=0 的等价判据 | 结构因子小 k 消失 | 连接 real-space 与 Fourier-space | 否 |
| Fig. 1 | 展示圆盘光弹实验装置和力链图 | 接触力可被实验测量 | 方法可信度入口 | 是 |
| Fig. 2 | 定义 r_i、r_ij、f_ij | torque/pressure 可计算 | 避免抽象变量悬空 | 是 |
| Eq. (3)-(4) | 定义 torque field 和 pressure field | 可从接触力构造基础场 | 方法核心公式 | 否 |
| Eq. (5) | 定义窗口积分 torque 方差 | 检验 hyperuniformity | 把理论条件变成统计量 | 否 |
| Fig. 3 | 圆盘各向同性压缩的方差和 S(k) | torque hyperuniform、pressure normal | 核心正例 | 是 |
| Eq. (6) | 定义结构因子 | S_tau(k->0) 为超均匀证据 | 第二判据 | 否 |
| Fig. 4 | 剪切下不同 gamma/phi 的方差和 S(k) | torque 对剪切鲁棒，pressure 改变 | 压力和扭矩形成对比 | 是 |
| Fig. 5 | 二维结构因子 S(kx, ky) | 剪切引入各向异性但 torque 小 k 仍消失 | 防止角向平均误导 | 是 |
| Fig. 6 | 固定 phi 下随应变演化 | 小应变到剪切态的连续演化 | 解释剪切影响不是单点偶然 | 是 |
| Fig. 7 | 椭圆接触几何定义 | normal force 也产生 torque | 强化椭圆案例的必要性 | 是 |
| Fig. 8 | 椭圆的 variance 和 S(k) | 椭圆两种 aspect ratio 均超均匀 | 形状鲁棒性证据 | 是 |
| Fig. 9 | 边界贡献示意 | 单颗粒 torque balance 解释 R 标度 | 物理解释收束全文 | 是 |

图表顺序很值得学：先定义概念，再定义实验变量，再给最干净体系的标度结果，再给扰动体系，再用机制图解释。这种安排让读者先相信数据，再接受直观解释。

## 11. 章节结构与篇章布局
- Abstract：压缩理论背景、实验缺口和三组验证结果，结尾预告物理解释与 d 维推广。
- Introduction：从无序固体应力相关的广泛意义进入，再讲 Hamiltonian 理论已解决什么，最后指出 frictional packing 需要 torque 条件和实验确认。
- Section 2：为不熟悉 normal/hyperuniform fluctuation 的读者补定义，是降低跨领域门槛的“概念教学”章节。
- Section 3：圆盘实验。先回顾各向同性压缩装置和已报道结果，再新增纯剪切数据。
- Section 4：椭圆实验。通过接触几何变化强化 torque 来源不止切向摩擦。
- Section 5：总结与讨论。不是重复图，而是给出边界贡献机制，并外推 d 维。

章节间过渡自然：理论需要实验 -> 实验需要定义统计量 -> 最简单圆盘体系确认 -> 剪切破坏各向同性仍确认 -> 椭圆改变 torque 来源仍确认 -> 机制解释为什么如此鲁棒。

最值得模仿的是 Section 2 的短教学章节。它把 hyperuniformity 的定义、方差判据和结构因子判据先讲清楚，后文所有图都不需要反复解释。结构风险是 Introduction 较长且理论共同体引用密集，对纯实验读者可能门槛偏高。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Torque-hyperuniformity-in-frictional-granula_2026_Journal-of-the-Mechanics-a.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：12
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 机制/讨论型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Experiments with disks | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Experimental setup for isotropic compression | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Data analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.4 Exprimemtal setup for pure shear | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 3.5 Data analysis and results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4 Experiments with ellipses | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.1 Experimental setup | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.2 Data analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5 Summary and discussion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落推进：
1. 无序固体需要新概念，先铺领域复杂性。
2. 外部应力响应和 inherent states 引出长程应力相关。
3. 超冷液体 relaxation 说明该问题不仅限于颗粒。
4. Hamiltonian central-force 系统条件已被理论解决。
5. friction breaks stress symmetry，理论 gap 出现。
6. 实验可行性与本文贡献：光弹颗粒、圆盘剪切、椭圆。
7. 章节安排。

Method/Results 段落节奏：每次先说明实验设置，再给统计定义，再描述图中趋势，再解释偏离或有限尺寸影响。作者不会过度堆图，几乎每张图都服务于一个 claim。

Discussion 段落节奏：先总结数据事实，再提出需要解释的鲁棒性，再用单颗粒 torque balance 图像解释，再回应统计独立性疑问，最后维度推广。这一节有很强的“审稿人预答复”功能。

可复用段落模板：`The theory predicts condition X, but this condition need not be automatically satisfied in real material Y. To test its robustness, we examine systems in which assumption A is weakened and mechanism B is added. We quantify X using both real-space scaling and reciprocal-space spectra, and then interpret the observed scaling through a local conservation constraint.`

## 13. 文笔画像与语言习惯
整体语气：理论自信、实验谨慎、解释直观。强 claim 常用 direct evidence、robust、strictly valid、confirmed，但在剪切 pressure 和三维推广处用 possibly、may require、expected to 这类谨慎词。

问题表达偏高层：`A question of fundamental importance is whether...`、`It is crucial to assess whether...`。这种开头把一个具体颗粒统计问题提升为无序固体普遍问题。

贡献表达偏“确认理论”：review、report confirmation、test whether these conditions are generically obeyed。作者不抢理论优先权，而是强调实验确认的必要性。

机制表达偏物理图像：`results from the constraint...`、`only contribution comes from contacts adjacent to the boundary`。不是只给数学证明，而是用窗口边界解释读者能直观看到的 R 标度。

术语密度适中。核心词反复出现：frictional granular packings, stress autocorrelation, pressure fluctuations, torque fluctuations, hyperuniformity, normality, structure factor, isotropy, mechanical balance。重复服务于概念稳定，不显啰嗦。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：torque(46)；pressure(41)；uctuations(40)；stress(23)；results(19)；systems(17)；normal(17)；frictional(16)；isotropic(16)；disks(16)；variance(16)；experimental(15)；shear(15)；shang(14)；forces(14)；packing(14)；hyperuniformity(13)；one(12)；two(11)；data(11)
- 高频学术名词：pressure(41)；stress(23)；results(19)；variance(16)；analysis(14)；structure(14)；hyperuniformity(13)；system(10)；experiments(9)；section(8)；university(7)；auto-correlation(7)；pure(7)；conditions(6)；question(6)；contribution(6)
- 高频学术动词：shown(7)；shows(6)；show(3)；predict(2)；captured(2)；derive(1)；compare(1)；evaluate(1)；demonstrated(1)
- 高频形容词：experimental(30)；normal(17)；local(16)；frictional(16)；isotropic(16)；elastic(14)；anisotropic(10)；small(10)；plastic(10)；erent(10)；large(9)；theoretical(8)；amorphous(8)；initial(7)；homogeneous(6)；mechanical(6)
- 高频副词/连接副词：approximately(8)；recently(6)；fully(4)；respectively(4)；therefore(3)；strongly(2)；generally(2)；notably(2)；consequently(2)；spatially(2)；nearly(2)；consistently(2)；cantly(2)；randomly(2)；however(1)；moreover(1)
- 高频二词短语：torque uctuations(17)；pressure uctuations(9)；lema tre(7)；isotropic compression(7)；pure shear(7)；packing fraction(6)；pressure torque(5)；hyperuniformity torque(5)；variance torque(5)；torque pressure(5)；frictional granular(4)；mechanical balance(4)；balance material(4)；material isotropy(4)；stress auto-correlation(4)；stress correlations(4)
- 高频三词短语：hyperuniformity torque uctuations(5)；mechanical balance material(4)；balance material isotropy(4)；shanghai jiao tong(3)；jiao tong university(3)；material isotropy demand(3)；isotropy demand stress(3)；stress auto-correlation matrix(3)；matrix fully determined(3)；local pressure uctuations(3)；writing review editing(3)；review editing writing(3)

**主动、被动与句法**

- 被动语态估计次数：61
- `we + 动作动词` 主动句估计次数：2
- 名词化表达估计次数：291
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：116
- 一般过去时线索：36
- 现在完成时线索：2
- 情态动词线索：16
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：torque(6)；frictional(6)；china(5)；stress(5)；university(4)；shanghai(4)；pressure(4)；uctuations(4)
- 1. Introduction：stress(15)；uctuations(13)；forces(9)；torque(9)；normal(8)；local(7)；correlations(7)；frictional(7)
- 3. Experiments with disks：pure(3)；shear(3)；isotropic(2)；compression(2)；results(2)；studied(1)；assemblies(1)；frictional(1)
- 3.1. Experimental setup for isotropic compression：disks(6)；pressure(5)；isotropic(4)；glass(4)；packing(4)；polarizer(4)；torque(4)；circular(3)
- 3.2. Data analysis：pressure(4)；torque(3)；elds(2)；window(2)；radius(2)；expressed(1)；nitions(1)；variables(1)
- 3.3. Results：torque(4)；pressure(3)；uctuations(3)；spectrum(3)；structure(3)；factors(3)；shown(2)；like(2)
- 3.4. Exprimemtal setup for pure shear：initial(4)；shear(3)；pressure(3)；experimental(2)；section(2)；packing(2)；fractions(2)；strains(2)
- 3.5. Data analysis and results：pressure(9)；uctuations(9)；packing(4)；shear(3)；signi(3)；systems(3)；system(3)；fraction(3)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文模式：`A question of immediate interest is whether X is specific to Y or should be found under broader conditions.`
- 可复用骨架：`A central question is whether [observed behavior] is specific to [well-studied system] or persists under [broader/less idealized conditions].`
- 中文启发：把 gap 写成“特殊性 vs 普遍性”的判断题，比单纯说“缺少研究”更有张力。

### 14.2 理论条件表达
- 原文模式：`Mechanical balance and material isotropy demand...`
- 可复用骨架：`Under [constraints A and B], [quantity] is fully determined by [minimal set of variables].`
- 中文启发：用“约束迫使变量简化”制造理论力量。

### 14.3 实验验证表达
- 原文模式：`The theoretical statement does not mean that actual matter will always bow to this requirement.`
- 可复用骨架：`A theoretical requirement does not by itself guarantee that real systems satisfy it; experimental tests are therefore needed.`
- 中文启发：承认理论和真实材料之间有距离，能自然引出实验。

### 14.4 结果与趋势表达
- 原文模式：`The vanishing of the spectrum at k -> 0 is direct evidence of hyperuniformity.`
- 可复用骨架：`The [limiting behavior] of [observable] provides direct evidence for [mechanism/condition].`
- 中文启发：每个统计图都要明确它证明哪个条件。

### 14.5 机制解释表达
- 原文模式：`The reason is quite intuitive, and results from the constraint...`
- 可复用骨架：`The robustness can be understood from a local constraint: [constraint], which makes [bulk contribution] cancel and leaves [boundary contribution].`
- 中文启发：把复杂标度归因于局部守恒/平衡约束，是 JMPS 很爱的一类解释。

### 14.6 边界与未来工作表达
- 原文模式：`While it seems difficult to confirm experimentally in 3D, it appears worthwhile to test in numerical simulations.`
- 可复用骨架：`Although direct experimental confirmation in [hard regime] is challenging, the prediction can be tested in [tractable platform].`
- 中文启发：未来工作要给出可执行路径，而不是泛泛“需要更多研究”。

## 15. 引用策略与文献使用
引用密度最高在 Introduction 和 Section 2。Introduction 中引用承担三类功能：先用无序固体、玻璃、剪切带等文献扩大问题背景；再用 inherent-state stress correlation 文献说明现象已被观察；最后用 Lemaitre 等理论文献定位本文的直接前件。Section 2 中 Torquato and Stillinger 作为概念定义源头，随后列举 solid state physics、cosmology、biology 等跨领域应用，提升 hyperuniformity 的普遍性。

经典文献用途：定义 hyperuniformity、建立 Hamiltonian stress correlation 理论、提供光弹颗粒 force inversion 方法。

近年文献用途：支持 frictional amorphous solids 的 pressure+torque 理论、圆盘各向同性实验的前置结果、剪切 pressure hyperfluctuation 的解释。

gap 如何靠引用搭建：先引用 Hamiltonian 情况已解决，说明不是所有 stress correlation 问题都未知；再引用 frictional theory 指出新条件；最后指出理论条件需要实验确认。这个 gap 有“前人越强，本文越必要”的效果。

引用风险：理论共同体集中，可能遗漏更多颗粒实验、非圆颗粒 jammed packing、剪切力链统计的相关工作；如果审稿人来自颗粒实验方向，可能要求更多实验文献比较。

## 16. 审稿人视角风险
- 最大攻击面：普遍性措辞。三类二维体系很有说服力，但“universally”或“generically”仍应限定为当前实验范围。
- claim 是否过强：torque hyperuniformity 的证据强；elastic-like stress autocorrelation 的完整结论在剪切态下较弱，因为 material isotropy 失效且 pressure 已 hyperfluctuating。
- 证据是否不足：小 k 行为容易受有限尺寸、边界剔除和窗口重叠影响；需要 PDF 图和原始数据确认误差。
- 方法可复现性：force inversion algorithm 的误差传播、接触识别阈值、摩擦系数和光弹材料校准未在主文充分展开。
- 对比是否充分：椭圆和圆盘压力范围、材料、jamming 点不同，直接比较 fluctuation magnitude 时应注意。
- 替代解释：边界贡献解释很强，但对有体力矩、颗粒非刚性扭转、三维非平面接触或强非平衡加载是否仍成立，需要边界说明。
- 图表核查：Fig. 3-8 的斜率、线性区间和小 k 外推必须结合 PDF 图像核查。

## 17. 可复用资产
- 可复用选题角度：理论模型给出了必要条件，但真实材料是否满足，尤其在非理想条件下是否鲁棒。
- 可复用 gap 制造方式：`central-force/Hamiltonian systems are understood; friction breaks the symmetry and introduces an additional field.`
- 可复用论证链：理论约束 -> 可测标量 -> 最简单实验 -> 扰动实验 -> 几何变化实验 -> 局部平衡解释 -> 维度推广。
- 可复用图表设计：定义示意图 + 方差标度图 + 结构因子图 + 二维各向异性谱图 + 机制示意图。
- 可复用段落结构：先承认前人理论，再说理论条件“不自动等于真实材料服从”，进而提出实验检验。
- 可复用句型骨架：`The robustness of X can be traced to the local constraint that Y must vanish on each element.`
- 不宜直接模仿之处：若自己的研究没有明确理论预测，不宜强行写成“confirmation of theory”；若无法直接测量微观力，不宜使用同样强的“direct evidence”语气。

## 18. 对我写论文的启发
如果写类似论文，可以学三点。第一，用理论中“必要但未验证”的条件作为选题入口，比单纯报告新实验更有 JMPS 价值。第二，将统计判据成对呈现：一个实空间尺度律，一个倒空间极限行为，使结论不依赖单一可视化。第三，在 Discussion 中用一个局部约束解释所有实验体系的共同标度，能让“多个案例”变成“一个机制”。

可以迁移到 Introduction 的写法：先问“现象是特殊材料导致，还是普遍约束导致”，再用文献说明一个理想体系已解决，最后指出真实非理想体系缺少验证。

可以迁移到 Method 的写法：给出变量定义示意图，让每个统计量都能从实验对象直接计算。

可以迁移到 Results/Discussion 的写法：不要只说三组数据都相同，而要解释为什么相同；把鲁棒性从经验观察升级为约束结果。

需要避免的问题：不要把有限二维实验过度外推到所有维度和所有加载；不要只凭图形线性说超均匀，必须说明小 k 与窗口方差两个判据。

## 19. 最终浓缩
这篇论文最值得学的是：把“摩擦破坏 Hamiltonian 对称性后新增的 torque 条件”转化为可测的超均匀统计，并通过圆盘压缩、圆盘剪切、椭圆压缩三类实验建立鲁棒性。

最大风险是：二维有限尺寸实验对“普遍性”和“三维推广”的支撑仍有限，剪切态下完整 elastic-like stress correlation 的条件也不能和各向同性态混为一谈。

三个可迁移动作：
1. 在选题中寻找“理论条件尚未被真实系统验证”的入口。
2. 用 real-space scaling 与 reciprocal-space spectra 双重证明一个统计 claim。
3. 在 Discussion 中用局部平衡/守恒约束解释宏观标度，而不是停留在曲线拟合。
