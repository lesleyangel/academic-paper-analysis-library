# The out-of-plane bifurcation and narrow stability interval of planar solutions in the Euler-Plateau problem

## 0. 读取说明
- 源 PDF：`jmps/文献/The-out-of-plane-bifurcation-and-narrow-stability_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/The-out-of-plane-bifurcation-and-narrow-stability_2026_Journal-of-the-Mechan.txt`
- 辅助参照：上一轮标准拆解仅用于校验主线，本文件重新按全文结构细拆。
- 是否需要结合 PDF 图像核查：需要。TXT 能读到图注、公式和部分图中趋势描述，但不能核查曲线形状、模态图、颜色标注和三维形态细节。
- 本文类型：理论稳定性分析 + 半解析数值求根 + 实验可观测性解释。它不是实验论文，证据主要来自二次变分、特征值求解、收敛性和能量分解。
- 阅读覆盖：摘要、Introduction、参数化、二次变分、稳定泛函最小化、无量纲化、平面分支几何、数值求临界值、实验含义、非凸性讨论、Summary、附录和参考文献线索。

## 1. 基本信息与论文身份
- 题名：The out-of-plane bifurcation and narrow stability interval of planar solutions in the Euler-Plateau problem
- 作者/机构：Sankalp Tiwari；Eliot Fried。机构包括 Indian Institute of Technology Delhi 与 Okinawa Institute of Science and Technology。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106657。
- DOI：10.1016/j.jmps.2026.106657
- 关键词：Elastic stability；Elastica；Minimal surface；Bifurcation；Variational mechanics。
- 研究对象：Euler-Plateau 问题中由极小曲面张成的不可伸长、无扭转、无自然曲率弹性闭环；重点是非圆平面分支何时发生出平面失稳。
- 研究尺度：连续体几何力学尺度；无微观材料结构，关键无量纲参数为 `nu = R^3 sigma / a`。
- 方法类型：变分力学、平面 elastica 参数化、二次变分稳定条件、约束稳定泛函最小化、Fourier/Bessel 型截断、非线性特征值求根。
- 证据类型：临界值 `nu_crit ≈ 3.7402`、截断阶数收敛、驻值分支交换、临界模态形状、能量项分解、与 Majid 数值估计 `4.3790` 的对比。
- 目标读者：稳定性理论、弹性曲线、极小曲面、软物质形态实验和变分力学读者。
- JMPS 风格定位：典型“精确修正一个领域认知”的理论论文。它的贡献不是提出一个宽泛模型，而是把一个实验-数值文献中悬置的临界点算清楚，并把数学临界值翻译成实验半径差。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先界定 Euler-Plateau 系统，再交代已知 `nu=3` 平面分岔和未知的平面分支出平面失稳；随后给方法，即基于已有二次变分条件最小化稳定泛函；最后给数值结果、与前人差异和实验后果。
- 背景句承担什么：把肥皂膜-弹性环问题压缩为“极小曲面表面张力 + 边界弹性弯曲”的耦合平衡问题，并指出稳定性只由 `nu` 控制。
- gap 句承担什么：强调圆形平面态在 `nu=3` 后转入非圆平面分支，但这些平面构型何时失稳此前没有解析研究，仅有 Majid 的全数值估计。
- 方法句承担什么：说明本文不从头做离散模拟，而是使用 Chen and Fried 的二次变分稳定条件，将问题化为带归一化约束的稳定泛函最小化。
- 结果句承担什么：给出 `nu_crit ≈ 3.7402`，并说明该值明显低于 `4.3790`；摘要在这里直接把贡献锚定为“纠正临界值”。
- 意义句承担什么：把数学结果转为实验语言：非圆平面分支只存在于 `3 < nu < nu_crit` 的窄区间；若通过增加半径提升 `nu`，两次分岔半径仅差约 7.6%。
- 一句话主张：Euler-Plateau 问题中的非圆平面分支并不是长区间稳定形态，而是在 `nu=3` 后很快于 `nu_crit≈3.7402` 发生出平面失稳，因此前人全数值临界值高估了稳定区间。
- 3-5 个核心关键词：second variation；nonlinear eigenvalue；narrow stability interval；out-of-plane bifurcation；solution landscape。

## 3. 选题层深拆
- 问题来源：来自实验形态序列和理论临界值之间的空缺。Giomi and Mahadevan 的实验显示弹性环张成肥皂膜后会经历圆形、非平面鞍形、八字形等变化；已有理论知道圆形平面态在 `nu=3` 发生平面分岔，但“非圆平面分支何时出平面”一直没有解析答案。
- 问题为什么重要：临界值决定实验可见形态序列，也决定对平面分支的物理解释。如果真实临界值接近 3，那么非圆平面分支只是极窄过渡；如果接近 4.3790，则可能有相对宽的实验可观测窗口。
- 问题为什么现在值得做：前人 Chen and Fried 已给出完整变分稳定框架，Majid 又给出全数值估计但受到离散曲面、网格和稳定判据影响；理论工具和争议对象都已具备，适合做一次“解析化清算”。
- 问题边界：只处理平面非圆分支的线性出平面失稳临界点、临界模态和相关解景观；不完整追踪后分岔非平面稳定构型，也不直接复现实验。
- 选题的 JMPS 味道：JMPS 很偏爱这种“低维几何现象 + 变分原理 + 稳定性条件 + 清晰物理后果”的题型。问题小而硬，公式多但结论有可观测含义。
- 选题可迁移性：可迁移到其他领域的方式是：找一个被数值或经验接受的临界点，用更严格的稳定性条件重算，并说明重算结果改变了实验解释或设计窗口。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：第一类是实验和初始模型，代表 Giomi and Mahadevan；第二类是完整变分稳定理论，代表 Chen and Fried；第三类是全数值离散微分几何模拟，代表 Majid；第四类是更经典的平面 elastica 和环形稳定性分析，作为数学工具背景。
- 主要研究流派/方法路线：实验观察路线负责提出形态序列；受限 ansatz 路线能给直观但可能误判稳定；完整变分路线强调必须相对所有邻近构型稳定；离散数值路线能看非线性形态但临界判据受离散影响。
- 每类研究解决了什么：实验路线证明现象真实存在；Giomi-Mahadevan 模型给出基本能量；Chen-Fried 证明 `nu=6` 圆盘到鞍形说法不成立；Majid 给出一个可比较的出平面临界估计。
- 每类研究留下什么不足：实验缺少精确临界分辨；受限模型会错把某类构型内的极小当作全空间稳定；Chen-Fried 留下了具体平面分支临界值；Majid 的 `4.3790` 缺少解析稳定泛函支撑。
- 本文站在哪条线上：站在 Chen-Fried 变分条件之后，同时吸收经典平面 elastica 参数化，以 Majid 的数值值作为直接比较对象。
- 最接近前人工作：Majid 的离散数值求稳定出平面分岔，以及 Chen and Fried 的二次变分框架。本文与前者差异在临界判据和解析化程度；与后者差异在把一般稳定条件用于具体平面分支并求出临界值。
- 是否公平处理前人：总体公平。作者明确承认前人给出实验、模型和稳定条件，但也清楚指出受限构型、离散网格和数值阈值可能导致临界值偏差。

## 5. Gap 制造机制
- 明示 gap：平面非圆构型失去稳定性的 `nu` 值尚未被解析研究；已有数值估计与二次变分框架之间缺少连接。
- 隐含 gap：只知道一个临界数值还不够，还需要知道临界模态、分支交换、能量项如何导致失稳，以及为什么实验很难看到这段平面分支。
- gap 类型：理论 gap + 方法 gap + 解释 gap。理论 gap 是临界值未知；方法 gap 是缺少半解析稳定判据；解释 gap 是缺少对 Majid 高估值和实验不可见性的说明。
- gap 证据来自哪里：Introduction 中逐步回顾 `nu=3`、`nu=6` 被否定、Majid `4.3790` 的路径；正文第 8-10 节通过新临界值、收敛性和能量分解反证旧估计不足。
- gap 是否足够窄：非常窄，集中在一个临界点和一个分支稳定区间，避免了“全面解释所有肥皂膜形态”的过宽问题。
- gap 是否足够重要：重要，因为临界值从 4.3790 降到 3.7402，会显著改变稳定窗口和实验设计需求。
- 如果我是审稿人会如何追问：星形参数化是否排除了更早出现的非星形或自交扰动？截断空间是否足够捕捉全局最小模态？`nu_crit` 之后的稳定非平面分支是否一定与观察形态相关？这些问题中前两个作者用收敛和附录部分缓解，第三个留作后续。

## 6. 创新性判断
- 作者声称的贡献：解析确定平面分支的出平面临界值；得到临界模态；刻画 `nu=3` 与 `nu_crit` 之间的解景观；说明非圆平面分支的实验可见窗口很窄。
- 我判断的真实创新：最核心是把二次变分稳定条件转化为可求解的非线性特征值问题，并用收敛性证明 `nu_crit≈3.7402` 不是数值偶然。其次是把“稳定泛函最小值为零”与“驻值分支交换”和“能量项平衡”联系起来。
- 创新类型：理论校正、临界值重估、模态解释、实验后果重新解释。
- 创新强度：强。原因是它不是边际改进，而是直接改写前人临界数值并缩短稳定区间。
- 创新必要性：必要。若只接受 Majid 的数值值，实验者会寻找更宽的平面分支窗口；本文显示这个窗口很窄，实验控制精度要求更高。
- 创新与证据匹配度：临界值 claim 与稳定泛函、收敛图、附录替代表述匹配强；实验可观测 claim 是由参数换算推出，合理但不是直接实验验证。
- 容易被挑战的创新点：所有创新都建立在线性失稳和选定参数化上，若存在非线性亚临界路径或未覆盖扰动空间，可能影响“最先失稳”的解释。

## 7. 论证链条复原
背景：弹性环张成肥皂膜的形态由表面张力和弯曲能竞争决定，`nu` 是唯一控制参数。

文献：Giomi and Mahadevan 给出实验和早期模型，Chen and Fried 纠正了 `nu=6` 鞍形转变说法，Majid 用全离散数值估计出平面分岔。

gap：非圆平面分支失稳点缺少解析化确定；全数值值可能受离散和稳定判据影响。

问题：沿 `n=2` 平面分支，何时存在使二次变分为零的出平面扰动？

方法：参数化平面边界和跨膜曲面；整理二次变分；证明关键可化为横向扰动稳定泛函；施加归一化约束；用傅里叶/贝塞尔展开得到非线性特征值方程。

证据：最小根给 `nu_crit≈3.7402`；截断阶数和阈值变化下收敛；前四个驻值分支在临界附近交换；临界模态显示出平面失稳形状；能量分解揭示非凸区域对负贡献的作用。

发现：非圆平面分支稳定区间是 `3<nu<3.7402`，比 Majid 值暗示的区间窄得多。

机制：出平面失稳不是圆盘态在高 `nu` 处突然转变，而是平面非圆分支上稳定泛函最小驻值与另一个分支交换后穿零；非凸性和边界拉格朗日乘子分布改变能量平衡。

意义：实验上通过增大半径扫 `nu` 时，两次分岔半径差约 7.6%，需要非常精细的长度控制和轮廓测量才能分辨非圆平面阶段。

## 8. 方法/理论/模型细拆
- 方法总框架：先把 Euler-Plateau 能量写成表面面积项与边界弯曲项；再沿已知平面 elastica 分支求边界、跨膜面和拉格朗日乘子；然后对完整曲面-边界系统做二次变分稳定性分析；最后求稳定泛函最小值何时从正变零。
- 关键概念：planar bifurcation；out-of-plane bifurcation；second variation；stationary mode；Lagrange multiplier；loss of convexity；loss of star shape；narrow stability interval。
- 关键变量/参数：`nu` 为分岔参数；`nu_crit` 为出平面临界值；`lambda` 是不可伸长约束相关乘子；`eta` 类参数进入径向特征方程；`N` 是展开截断阶数；非凸性量度 `m_nc` 用来诊断平面区域形状变化。
- 核心假设：边界不可伸长、无扭转、无自然曲率；膜为常表面张力极小曲面；所考察区间内平面区域可用所选参数化处理；临界由二次变分零化判定。
- 边界条件：边界闭合、长度固定、平面分支对称；扰动满足跨膜和边界耦合条件；最小化时加入归一化约束防止平凡解。
- 方法步骤：1. 复现平面非圆分支；2. 计算跨膜极小曲面及边界几何；3. 写出二次变分泛函；4. 通过展开求驻值方程；5. 对不同 `nu` 求最小驻值；6. 找到穿零点；7. 做截断和附录验证；8. 解释模态和能量。
- 复现信息：论文给出主要方程、数值求解思路、截断阶数和收敛检查；但实际代码、网格和求根容差若未公开，复现者仍需从公式重新实现。
- 方法复杂度是否合理：合理。问题本质是耦合曲面-弹性边界的稳定性，直接 3D 数值会引入离散不确定；半解析特征值方法恰好对准 gap。
- 方法与 gap 的对应关系：gap 是临界值和模态不清，方法直接输出临界根、临界模态、分支交换和能量分解，形成一一对应。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 非圆平面分支的出平面临界值为 `nu_crit≈3.7402` | 摘要、第 8 节、Summary | 稳定泛函最小驻值穿零；截断收敛；附录对 `eta<0` 情况处理 | 理论推导 + 数值求根 | 强 | 依赖参数化和截断空间完整性 |
| Majid 的 `4.3790` 高估了稳定区间 | 摘要、Introduction、结果讨论 | 本文临界值与前值直接比较，且有收敛验证 | 对比论证 | 中强 | 若前人定义的非平面出现判据不同，比较需谨慎 |
| 非圆平面分支只在 `3<nu<nu_crit` 窄区间稳定 | 摘要、第 9 节、Summary | `nu=3` 平面分岔已知；本文给出第二临界值 | 理论拼接 | 强 | 未讨论非线性亚临界构型是否可提前出现 |
| 实验中两次分岔半径差约 7.6% | 摘要、第 9 节 | `nu=R^3 sigma/a` 换算；`R_crit/R_planar=(nu_crit/3)^(1/3)` | 参数换算 | 中强 | 真实实验有材料参数漂移、膜张力变化和缺陷 |
| 临界出平面模态可被稳定泛函驻值分支交换解释 | 第 8 节 | 前四个 stationary modes 随 `nu` 变化图、能量曲线 | 模态分析 | 中强 | 图像细节需结合 PDF 核查 |
| 非凸性影响但不是简单等同于失稳点 | 第 6 和第 10 节 | `m_nc`、loss of convexity、loss of star shape 与 `nu_crit` 的相对位置 | 几何诊断 + 解释 | 中 | 非凸性量度和能量项关系需要读图核查 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| 公式 (1)-(3) 能量与无量纲参数 | 建立问题对象和控制参数 | 稳定性由 `nu` 控制 | 把实验半径、弯曲刚度、表面张力压成一个参数 | 否，公式可从 TXT 判断 |
| 二次变分相关公式组 | 稳定性判据核心 | 临界点来自二次变分零化 | 给出比全数值更可审计的理论基础 | 否，但符号排版需 PDF 核查 |
| Fig. 1 | 展示平面边界随 `nu` 变化及非凸性量度 | 平面分支几何会经历凸性丧失 | 把抽象分支可视化，并引入 `m_nc` | 是 |
| Fig. 2 | 展示星形性丧失判据 | 参数化适用边界与几何变化相关 | 说明 star-shaped 假设在较高 `nu` 才失效 | 是 |
| Fig. 3 | 展示拉格朗日乘子 `lambda(s)` 随 `nu` 的变化 | 边界约束场影响稳定能量 | 解释约束乘子从接近圆态到复杂分布的变化 | 是 |
| Fig. 4 | 最小驻值/特征根随 `nu` 的图 | `nu_crit` 的定位 | 直接给穿零临界点 | 是 |
| Fig. 5 | 收敛性图 | 临界值稳健 | 回应数值截断风险 | 是 |
| Fig. 6-7 | 驻值模态和临界形态 | 临界模态与分支交换 | 将特征值结果转为形态直觉 | 是 |
| Fig. 10-12 | 能量项分解与非凸区域贡献 | 失稳机制与非凸性 | 解释为什么某些区域提供负稳定贡献 | 是 |

图表顺序服务论证的方式：先用 Fig. 1-3 告诉读者平面分支本身如何变形，再用 Fig. 4-5 锁定临界值和稳健性，接着用 Fig. 6-7 解释临界模态，最后用能量分解图把“为什么失稳”讲成机制。这种顺序从几何对象、数值证据到物理解释逐级推进。

## 11. 章节结构与篇章布局
- Abstract：完整五步：对象、已知、未知、方法、临界值与实验后果。摘要非常像一段压缩版论证链。
- Introduction：从肥皂膜实验引入，随后回顾能量模型、`nu` 的物理含义、`nu=3` 平面分岔、`nu=6` 误判、Majid 数值估计，最后定位本文要做解析临界值。
- Related Work/Background：没有独立 Related Work，文献版图被嵌入 Introduction；这种做法适合理论短链条论文。
- Method/Theory/Model：第 2-5 节是方法主体，先参数化，再二次变分，再最小化，再无量纲化。该顺序体现“先把对象写清，再写稳定条件，再写求解形式”。
- Results：第 6-8 节从平面分支几何到数值临界值；第 8 节是最核心结果。
- Discussion：第 9-10 节讨论实验观察与非凸性作用，避免让文章停留在一个数字上。
- Conclusion：第 11 节 Summary 回收临界值、窄区间、实验意义和未来后分岔分析。
- 章节之间如何过渡：公式章节靠“为了求临界值必须先知道平面分支”过渡；结果到讨论靠“这个临界值对实验意味着什么”过渡。
- 哪一节最值得模仿：第 9 节。它把纯理论结果换算成实验半径差，显著提高论文的可读性和影响面。
- 哪一节可能存在结构风险：第 2-5 节公式密度高，若读者不熟悉 Chen-Fried 框架，会觉得进入核心结果前铺垫过长。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-out-of-plane-bifurcation-and-narrow-stability_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：11
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Parameterization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Second variation condition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Minimization of the second variation functional | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Nondimensionalization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6.2 Loss of convexity | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6.3 Loss of star shape | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 8.2 Convergence analysis of the numerical scheme | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 9 Implications for experimental observation of the noncircular planar branch | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 10 Characteristics of the critical bifurcation mode and the role of nonconvexity | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 11 Summary | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：实验现象段负责造问题；能量模型段负责给变量；前人临界争议段负责制造 gap；本文方法段负责给路线；章节安排段负责降低阅读成本。
- Method 段落推进：每段通常先给一个几何或变分对象，再给公式定义，随后说明该对象在后续稳定性求解中的作用。段落收束多是“因此可将问题化为……”。
- Results 段落推进：先描述图显示什么，再给关键数值，再解释其与前人或几何性质的关系。尤其在收敛性段落中，作者先展示阈值敏感性，再展示截断阶数稳定。
- Discussion/Conclusion 段落推进：先将 `nu_crit` 换算成实验半径，再讨论为什么很难观测；随后转入非凸性对临界模态的作用，最后承认后分岔分析是自然延伸。
- 常见段落开头方式：`It is known that...`；`To determine...`；`We observe from Fig....`；`A principal consequence is...`。
- 常见段落收束方式：给出一个数值、一个临界判断或一个下一节需要解释的问题。
- 可复用段落模板：现象/前人给出临界 A -> 另一路径给出临界 B -> 指出两者差异影响物理解释 -> 本文采用更严格条件重算 -> 后文用收敛性和模态证明该值。

## 13. 文笔画像与语言习惯
- 整体语气：精确、克制、纠错型。作者不会用夸张词汇包装，而是让“显著低于前值”和“窄区间”承担冲击力。
- claim 强度：对临界值、收敛性和稳定区间使用强 claim；对实验可观测性和未来后分岔使用较谨慎 claim。
- 谨慎表达：常用 `suggesting`、`within numerical resolution`、`most likely`、`would require` 来控制边界。
- 问题表达：偏好 `has not been studied analytically`、`the discrepancy stems from`、`determine the critical value`。
- 贡献表达：偏好 `we determine`、`we obtain`、`we characterize`、`we conclude`。
- 机制表达：`loss of convexity`、`loss of star shape`、`exchange of minimizers`、`negative contribution to the functional`。
- 对比表达：用 `substantially smaller than`、`in contrast to`、`consistent with` 建立与前人和内部结果的关系。
- 限定边界表达：用 `for the considered range`、`to numerical accuracy`、`within the framework of the free-energy`。
- 术语密度：高，但集中在几何变分和分岔稳定性术语；没有跨太多学科词。
- 长句/短句习惯：公式前后的解释句较长，结论句较短而明确，形成“推导复杂、判断清楚”的节奏。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：crit(115)；loop(82)；value(78)；planar(64)；section(62)；bifurcation(53)；dimensionless(51)；mode(51)；critical(49)；fried(47)；condition(45)；branch(42)；corresponding(41)；panel(41)；con(38)；values(35)；variation(34)；solution(33)；numerical(32)；second(31)
- 高频学术名词：condition(90)；solution(66)；section(62)；bifurcation(53)；variation(34)；analysis(30)；contribution(20)；equation(18)；normalization(18)；guration(17)；curvature(17)；displacement(16)；solutions(14)；continuation(14)；stability(13)；dependence(13)
- 高频学术动词：shown(12)；show(11)；indicates(4)；demonstrate(3)；derived(3)；estimate(3)；predicted(3)；formulated(2)；investigate(2)；proposed(2)；estimated(2)；solve(2)；solved(1)；capture(1)；captured(1)；reveal(1)
- 高频形容词：critical(98)；numerical(64)；dimensionless(51)；experimental(32)；boundary(28)；stable(22)；qualitative(18)；lineal(18)；small(17)；interval(17)；functional(17)；consistent(16)；displacement(16)；stationary(16)；areal(15)；integral(14)
- 高频副词/连接副词：approximately(34)；therefore(21)；furthermore(17)；respectively(17)；ciently(13)；monotonically(12)；consequently(10)；nearly(9)；however(8)；substantially(8)；accordingly(7)；finally(7)；fully(5)；sharply(5)；weakly(4)；analytically(4)
- 高频二词短语：bounding loop(29)；second variation(25)；tiwari fried(23)；value crit(22)；giomi mahadevan(21)；chen fried(19)；con gurations(18)；left panel(18)；out-of-plane bifurcation(17)；con guration(17)；variation condition(16)；critical mode(16)；lagrange multiplier(15)；critical value(11)；spanning surface(11)；bifurcation mode(11)
- 高频三词短语：second variation condition(16)；continuation cos mode(10)；second variation functional(8)；critical bifurcation mode(8)；planar con gurations(7)；spanning surface bounding(7)；surface bounding loop(7)；out-of-plane bifurcation occurs(6)；total dimensionless energy(6)；critical value crit(5)；noncircular planar con(5)；planar non-planar bifurcations(5)

**主动、被动与句法**

- 被动语态估计次数：141
- `we + 动作动词` 主动句估计次数：12
- 名词化表达估计次数：943
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：313
- 一般过去时线索：50
- 现在完成时线索：6
- 情态动词线索：32
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：stability(6)；planar(6)；loop(6)；surface(4)；value(4)；bifurcation(3)；interval(3)；problem(3)
- 1. Introduction：section(21)；loop(18)；bifurcation(17)；solution(13)；con(12)；planar(12)；fried(11)；circular(10)
- 2. Parameterization：consistent(5)；parameterization(4)；symmetry(4)；planar(3)；admits(3)；polar(3)；representation(3)；since(3)
- 3. Second variation condition：second(9)；variation(8)；condition(8)；integral(7)；follows(6)；thus(6)；ned(4)；furthermore(4)
- 4. Minimization of the second variation functional：condition(12)；variation(6)；consider(4)；fried(4)；integral(4)；given(4)；rule(4)；boundary(4)
- 5. Nondimensionalization：dimensionless(22)；loop(14)；bounding(10)；values(9)；ned(8)；fried(8)；curvature(8)；planar(8)
- 6.2. Loss of convexity：convex(6)；length(5)；boundary(5)；hull(5)；observe(2)；panel(2)；loses(2)；convexity(2)
- 6.3. Loss of star shape：value(22)；crit(21)；section(15)；problem(13)；numerical(13)；corresponding(11)；left(10)；panel(9)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`The value at which ... has not been studied analytically but has been estimated through numerical simulations.`
- 可复用句型骨架：`The critical condition for X has been estimated numerically, but an analytic stability-based determination remains unavailable.`
- 中文写作启发：不要只说“缺少研究”，要说缺少哪一种更可信的确定方式。

### 14.2 方法与框架表达
- 原文表达模式：基于已有二次变分条件，通过最小化相关稳定泛函并加入归一化约束，将问题降为非线性特征值方程。
- 可复用句型骨架：`By minimizing the stability functional subject to a normalization constraint, the onset condition reduces to a nonlinear eigenvalue problem.`
- 中文写作启发：方法句要同时交代“用什么已有理论”“做了什么变换”“输出什么可计算问题”。

### 14.3 结果与趋势表达
- 原文表达模式：`the smallest root yields ... a value substantially smaller than ...`
- 可复用句型骨架：`The smallest admissible root gives X, which is substantially lower than the previously reported value Y.`
- 中文写作启发：结果句最好带对比对象，否则一个数字没有说服力。

### 14.4 机制解释表达
- 原文表达模式：稳定区间窄、模态分支交换、非凸段贡献共同解释失稳。
- 可复用句型骨架：`The loss of stability can be interpreted as an exchange of the minimizing mode, amplified by the changing sign/weight of selected energy contributions.`
- 中文写作启发：理论论文的机制解释不一定来自实验因果，可以来自泛函项、模态和约束的相互作用。

### 14.5 贡献与意义表达
- 原文表达模式：把 `nu` 临界值换算为半径差，说明实验控制要求。
- 可复用句型骨架：`In experimental protocols where X is varied through Y, the two thresholds differ by only Z%, implying that resolving the intermediate branch requires fine control of Y.`
- 中文写作启发：抽象无量纲参数最好转回实验可测变量。

### 14.6 局限与未来工作表达
- 原文表达模式：自然延伸是研究后分岔非线性稳定形态和更完整的解景观。
- 可复用句型骨架：`A natural extension is to continue the bifurcating branch beyond the onset and assess its nonlinear stability.`
- 中文写作启发：未来工作不要泛泛而谈，应紧接当前分析边界。

## 15. 引用策略与文献使用
- 引用密度：Introduction 密集，方法和结果部分引用少而精。正文靠公式自洽而不是靠大量文献背书。
- 引用主要集中位置：前两页用于搭建实验、模型和争议；后文只在与经典 elastica、前人数值和稳定框架相关处引用。
- 经典文献用途：经典 elastica 和变分稳定文献提供方法地基。
- 近年文献用途：Majid 和相关新近数值工作提供直接比较对象。
- 方法文献用途：Chen and Fried 的二次变分条件几乎是本文方法入口。
- 对比/批判性引用：对 Giomi-Mahadevan 的 `nu=6` 解释和 Majid 的临界值不是简单否定，而是说明其方法限制。
- gap 如何靠引用搭建：先引用实验说明现象重要，再引用完整变分框架说明稳定性条件已有，最后引用数值估计说明具体临界值仍可疑。
- references 暗示的研究共同体：弹性曲线、极小曲面、肥皂膜实验、变分稳定性、小规模但高度相关的共同体。
- 引用风险：若遗漏更近的后分岔数值或实验验证，审稿人可能要求补充；不过就 TXT 所见，本文聚焦的核心前作覆盖较完整。

## 16. 审稿人视角风险
- 最大攻击面：稳定性分析的 admissible perturbation space 是否完整，尤其是星形参数化和截断展开是否可能排除更危险的扰动。
- claim 是否过强：临界值 claim 强但有证据；实验难观测 claim 应理解为由理想参数换算得到，不宜读成已实验验证。
- 证据是否不足：对后分岔形态和真实实验噪声没有直接证据；这不是主 claim，但会影响物理外推。
- 方法是否可复现：公式和收敛信息较充分；若无代码，独立复现仍有门槛。
- 对比是否充分：与 Majid 数值值对比充分；与可能的其他模拟路线对比有限。
- 边界条件是否清楚：理论边界清楚，包括不可伸长、无扭转、常张力、平面分支。
- 替代解释是否排除：对 `nu=4.3790` 的替代解释主要通过新稳定判据排除；实验中看不到平面分支还可能来自缺陷和动力学路径，作者只给一个强解释。
- 图表是否需要进一步核查：需要。尤其 Fig. 4-7、Fig. 10-12 的曲线、模态和能量分区必须看 PDF。

## 17. 可复用资产
- 可复用选题角度：修正一个广为引用但主要数值支持的临界值；把“精确临界点”作为理论贡献。
- 可复用 gap 制造方式：`前人有实验现象 -> 前人有完整理论条件 -> 前人有数值估计 -> 缺少解析化临界值和模态解释`。
- 可复用论证链：能量模型 -> 无量纲参数 -> 前人临界争议 -> 二次变分 -> 特征值 -> 收敛性 -> 实验变量换算。
- 可复用图表设计：几何分支图、非凸性量度图、临界根图、收敛图、模态图、能量项分解图。
- 可复用段落结构：每个结果段都采用“图显示趋势 -> 数值定位 -> 与前人/机制关系 -> 下一步问题”。
- 可复用句型骨架：`This value is substantially smaller than...`；`This narrow interval may explain why...`；`The discrepancy stems from restricting the minimization to...`。
- 可复用引用组织：小共同体论文适合少量强相关引用，不需要铺满大综述。
- 不宜直接模仿之处：如果自己的问题没有同等严格的变分条件，不宜模仿这种“纠正前人值”的强姿态；否则容易被认为只是数值差异。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：把理论工作写成“改变可观测窗口”的故事，而不是只堆公式。
- 可以迁移到 Introduction 的写法：先讲现象，再讲模型参数，再讲前人临界点冲突，最后给本文要算的单一问题。
- 可以迁移到 Method 的写法：每引入一个复杂泛函，都要说明它最终服务于哪个稳定判据。
- 可以迁移到 Results/Discussion 的写法：结果不止给数字，还给收敛、模态、能量解释和实验换算。
- 需要避免的问题：不要让前五节公式把读者淹没；可以在每节末尾加一句“本节为临界值求解准备了什么”。

## 19. 最终浓缩
- 这篇论文最值得学：如何用严格稳定性条件把一个模糊的数值临界点变成可信的物理结论，并把抽象参数换算成实验控制要求。
- 这篇论文最大风险：临界分析和参数化空间的边界若被挑战，`nu_crit` 的“最早失稳”解释会承压。
- 三个可迁移动作：1. 用前人冲突值制造清晰 gap；2. 对核心数值结果做截断/阈值收敛检查；3. 把无量纲结论转写成实验者能理解的尺度差。
