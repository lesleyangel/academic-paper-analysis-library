# Fluid-structure interaction of a vegetation canopy in the mixing layer

## 0. 读取说明

本拆解基于 `801/文本/txt/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.txt` 的全文抽取。文本抽取包含正文、公式、图题和结论，但不包含可直接判读的图像细节；涉及涡结构形态、颜色区域、参数图边界等视觉判断时，均按文本描述分析，细节标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：Introduction, Mathematical model, Results and discussion, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Fluid-structure interaction of a vegetation canopy in the mixing layer。
- 作者：Zhe Fang、Chunlin Gong、Alistair Revell、Joseph O'Connor。
- 期刊：Journal of Fluids and Structures，109，2022，103467。
- 领域：植被冠层流、流固耦合、混合层不稳定性、柔性结构动力学。
- 论文类型：数值模拟 + 机理解释型论文。
- 研究对象：浅淹没植被冠层与冠层顶部混合层之间的双向流固耦合。
- 主要方法：LBM 求解流场，非线性 FEM 求解植被梁变形，IBM 处理流固界面，强耦合 block Gauss-Seidel 隐式迭代稳定耦合。
- 核心变量：弯曲刚度 K、冠层密度 Phi、响应频率、KH 不稳定频率、自然频率、阻力系数、植被尖端偏转角。
- 目标读者：流固耦合数值模拟研究者、植被冠层流研究者、流动控制/生态流体力学读者。

## 2. 摘要与核心信息提取

论文的核心主张是：植被冠层的动态响应不是单纯由 KH 混合层不稳定性决定，也不是单纯由植被固有频率决定，而是由冠层密度、弯曲刚度、混合层强度和结构自然频率共同耦合产生；在 KH 频率与结构自然频率交叉区域会出现 lock-in，表现为混合层对植被摆动频率的“吸引”。

摘要里的信息压缩方式很典型：先说现象，即 submerged vegetation canopy 的 waving motion 与冠层顶部 coherent vortices 相关；再制造不足，即此前多用显著建模假设简化系统，混合层与冠层的双向影响仍 underexplored；再给方法，即 fully coupled fluid-structure modeling；然后给结果分类，即 static、flapping、dual、regular waving、irregular waving 五种状态；最后给频率机制，即 lock-in 出现在混合层不稳定频率与植被自然频率 crossover region。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Fluid-structure-interaction-of-a-vegetation-canop_2022_Journal-of-Fluids-and.md`。

中文译文：

> 水下植被冠层的波动运动与冠层顶部相干涡流的产生有关，这是混合层不稳定性的表现。混合层上方的不稳定流之间的相互作用及其对植被冠层本身的影响仍然相对未得到充分探索，大多数先前的研究都采用重要的建模假设来简化系统。在本文中，采用完全耦合的流体-结构建模方法来研究植被冠层与其上方出现的混合层之间的相互作用机制。探讨了植被行为对弯曲刚度和冠层密度的依赖性，观察了植被的五种代表性行为状态：静态、扑动、双重、规则波动和不规则波动。比较了在与每个状态相关的混合层中观察到的涡流结构，并研究了冠层密度对混合层发展的影响，特别关注与植被相关的流动特征。此外，在混合层不稳定频率与植被固有频率的交叉区域观察到锁定效应，这表明混合层对植被波动频率的吸引作用。 © 2021 爱思唯尔有限公司
>
> 版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自两个交叉需求：一是生态/工程问题，植被冠层通过流固相互作用影响沉积物输运、作物损伤、空气/水质和栖息地；二是流体力学问题，冠层顶部速度剖面的拐点会诱发类似 mixing layer 的 KH 不稳定性，但柔性冠层又会反过来改变流场。

作者把大问题收束成一个可计算问题：在固定 Re=100、质量比 M=1 的二维浅淹没冠层中，系统改变弯曲刚度和冠层密度，观察行为图谱、涡结构、频率关系和 lock-in 机制。这个收束很稳，因为它避免了“真实植被太复杂”的泛化陷阱，把论文变成参数空间中的机理识别。

选题价值主要有三层：理论上解释混合层不稳定性和结构自然频率之间的控制权；方法上展示 fully coupled FSI 在冠层流中的作用；应用上把 flapping 状态中的垂向输运与沙化/风蚀联系起来，并提出混种不同刚度植被保护脆弱作物的初步策略。

## 4. 领域位置与文献版图

文献版图被组织成三条线。第一条是植被冠层流与 mixing layer 类比：Ghisalberti、Nepf、Raupach 等工作说明冠层顶部阻力不连续导致速度剖面拐点和 KH 不稳定。第二条是植被动力学：Finnigan、Py 等实验指出摆动频率接近植被自然频率，从而挑战“完全由 KH 控制”的解释。第三条是数值建模：早期连续冠层/刚体植被/分段线性速度剖面模型简化较多，近年的 O'Connor、Revell、Zhang 等 fully coupled FSI 模型更能解析单根植被柔性动力学。

本文的站位是“继承 mixing layer 模型，但修正其单向解释”。作者没有否定 KH 不稳定，而是把 KH 频率、真空/流体自然频率、实际摆动频率同时放进比较框架中，试图解释前人结论为什么不一致。

## 5. Gap 制造机制

作者制造 gap 的方式不是简单说“没人研究”，而是说已有研究的结论彼此冲突：有的认为 canopy waving 由 KH instability dominated，有的发现主频接近 free-vibration frequency，还有的 lock-in 解释依赖不同 KH 频率定义。冲突的根源又被追溯到模型假设差异：简化流场、连续冠层、刚体植被、少量 flap 等都可能改变频率关系。

真实 gap 是：缺少一个 fully coupled、能同时改变弯曲刚度和冠层密度、并把涡结构与频率响应连起来的参数化研究。这个 gap 是成立的，因为论文后文确实用行为图谱、涡结构、速度梯度、KH 频率估计和自然频率比较逐层回应。

风险在于：二维、Re=100、无重力/浮力/接触模型使 gap 的“真实植被适用性”被削弱；作者在讨论中承认了这些边界。

## 6. 创新性判断

作者声明的创新包括：使用直接流固耦合模型研究冠层与混合层相互作用；在弯曲刚度和冠层密度空间中识别五种行为状态；解释涡结构如何随状态改变；观察 lock-in，并将其解释为混合层对植被频率的吸引效应。

真实创新强度属于中高。方法本身是已有 LBM-IBM-FEM 框架的应用和组合，不是全新数值方法；但问题拆解和证据组织有新意，特别是把行为模式、涡中心位置、剪切载荷、KH 频率、自然频率放入一条机制链。

最可能被挑战的是“lock-in 机制解释”和“沙化/作物保护应用延伸”。前者依赖后验频率估计和二维模拟；后者从无颗粒、无重力/浮力模型外推到 sediment/sandification，启发性强但证据链偏间接。

## 7. 论证链条复原

论证链条如下：

1. 植被冠层流具有速度剖面拐点，可能产生 KH 型 mixing layer instability。
2. 柔性植被并非被动响应，植被自然频率和运动会反过来影响流场。
3. 既有研究对主导频率和 lock-in 的解释不一致，原因之一是模型简化不同。
4. 因此需要 fully coupled FSI 模型，在参数空间中同时考察弯曲刚度和冠层密度。
5. LBM-IBM-FEM 强耦合模型给出五种行为状态，并显示状态边界依赖 K 与 Phi。
6. 涡结构比较解释行为转换：涡中心低于植被尖端时产生 mode-two flapping；涡中心上移后转为 mode-one waving；生产/耗散失衡导致 irregular waving。
7. 冠层密度改变速度剖面拐点与速度梯度，从而改变混合层强度和不稳定性起始位置。
8. 频率比较显示 waving branch 近似一阶自然频率，flapping branch 近似二阶自然频率，KH 频率在交叉区吸引实际频率形成 lock-in。
9. 结论回扣开头：动态行为由混合层和结构属性耦合控制，而非单一机制。

薄弱环节是第 8 步：KH 频率由速度剖面和动量厚度估计，实际 lock-in 的因果证据还需要更多控制实验或 3D 验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services. Secondly, the fluid grid in the IBM does not need to conform to the structure boundary, so the grid generation in the present model becomes much faster than that of the traditional Arbitrary Lagrangian Eulerian (ALE) method (Peskin, 2002), and the flow governing equations are solved very efficiently on the fixed regular fluid grid. At each internal iteration, the displacement of structure is relaxed based on the previous iteration, given by ˜U = ωU + (1 −ω) ˜U k−1 (17) The Aitken’s ∆2 relaxation method (Kuttler and Wall, 2008) is adopted here to speed up the convergence rate of the above coupling scheme, in which the relaxation factor ω is calculated dynamically through: ⏐⏐rk −rk−1⏐⏐2 (18) rk = U k −˜U k−1 (19) Typically, a lower structure-to-fluid density ratio requires more sub-iterations to ensure the convergence of the coupling.
- 已有研究不足/GAP：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. However, for problems with a low structure-to-fluid density ratio, this coupling strategy can lead to a boundary condition mismatch at the fluid–structure interface, which can adversely impact the stability and accuracy of the solution.
- 本文解决方式：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system. In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it. The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
- 学术或工程增量：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004). In addition, a strong-coupling implicit scheme is also introduced in this model in order to improve the stability and accuracy of algorithm. The accuracy and reliability of the present model has also been demonstrated by these studies, mainly from the following three aspects: Firstly, the LBM used in the present model has been proven to be a feasible substitute over a Navier–Stokes (N–S) solver due to its simple formulations, high efficiency and high level of parallelizability (Shan et al., 2006).
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

模型由三部分组成。流场用 LBM-BGK 方程和 Guo forcing term，优势是规则网格、高并行性、适合与 IBM 耦合。结构用非线性 FEM，把每根植被离散为 Euler-Bernoulli 梁，用 Newmark-beta 与 Newton-Raphson 求解大变形动力学。界面用 IBM，在 Eulerian 流体点和 Lagrangian 结构标记点之间通过插值和 spreading 交换速度与力。

耦合策略是方法可信度的关键。作者指出低结构/流体密度比下显式 partitioned 方法会有界面边界条件 mismatch，因此加入强耦合 block Gauss-Seidel 隐式子迭代，并用 Aitken relaxation 动态调整松弛因子。这给“fully coupled”的说法提供了数值稳定性支撑。

参数设置上，通道高 H=3h，冠层长 Lc=64h，总长 Lt=104h，入口为无拐点抛物线速度剖面，用于观察混合层如何由冠层产生而不是入口预置。Re=100，M=1.0，K 取 12 个数量级分布值，Phi 取 0 到 0.1。每根植被 50 个 IBM markers、20 个 FEM elements，并附录做网格独立性。

方法边界：二维、浅淹没、无植被接触、无重力/浮力、固定 Re 和 M。作者用讨论小节主动限定这些条件，降低过度外推风险。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 冠层行为可分为 static、flapping、dual、regular waving、irregular waving 五类 | 4.1 | Fig. 3 快照、Fig. 4 参数图谱 | 强 | 状态分类依赖视觉判读，需要 PDF 图像复核 |
| 行为模式受弯曲刚度和冠层密度共同控制 | 4.1 | K0-K11 与 Phi0-Phi10 参数图，动态区集中在中间参数范围 | 强 | 参数范围固定于 Re=100、M=1 |
| flapping 中涡中心低于植被尖端，导致强剪切和 mode-two deformation | 4.2 | Fig. 5b 流线/竖向速度，Fig. 6 阻力系数，文字描述涡旋穿透冠层 | 中强 | 涡中心位置需 PDF 图像复核 |
| waving 中涡旋上移，植被由 mode-two 转为 mode-one | 4.2 | Fig. 5c-5e 与 Fig. 6，作者比较涡旋尺度和阻力幅值 | 中强 | mode 判别依赖形态图 |
| 冠层密度增加会降低冠层内外垂向交换、提高顶部速度梯度并提前 KH 不稳定起始 | 4.3 | Fig. 9-11，速度剖面和 ∂ux/∂y 随密度变化 | 强 | 速度剖面来自单一 x=26 静态区域 |
| 动态响应频率由结构自然频率主导，但受混合层 KH 频率吸引 | 4.4 | Fig. 12-14，一阶/二阶自然频率、KH 频率、实际频率平台 | 中强 | lock-in 因果性主要由相关趋势支持 |
| flapping 中存在冠层到混合层的自发垂向输运，可能关联沙化 | 4.2/结论 | Fig. 5b 中诱导涡上移描述 | 中 | 无颗粒输运、重力/浮力模型，应用外推较强 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 建立冠层速度剖面、混合层与 wavelike motion 的概念图 | 冠层顶部混合层驱动 monami/honami | 视觉化“速度拐点-涡-波动”链条 | 需要 PDF 图像复核 |
| Eq. 1-7 | 给出 LBM 流场控制与 forcing | 方法可解析受力流场 | 外力项进入动量更新 | 文本可确认 |
| Eq. 8-10 | 给出植被梁动力学与 Newmark 求解 | 单根植被柔性动力学被解析 | 内力、外力、质量矩阵闭合 | 文本可确认 |
| Eq. 11-16 | IBM 插值/扩散与界面力计算 | 流固界面数据交换 | Eulerian-Lagrangian 两套网格耦合 | 文本可确认 |
| Fig. 3-4 | 行为分类和参数图谱 | 五种行为状态 | dynamic/static 区域随 K、Phi 成带状分布 | 需要 PDF 图像复核 |
| Fig. 5-7 | 用涡结构、阻力和偏转角解释 flapping/waving | 涡中心位置决定变形模态 | flapping 有冠层穿透与 mode-two，应力更强 | 需要 PDF 图像复核 |
| Fig. 9-11 | 解释冠层密度对混合层起始的作用 | 密度调节速度梯度和不稳定性 | inflection point 上移，速度梯度峰值增大 | 需要 PDF 图像复核 |
| Eq. 25-28 | 估计自然频率和 KH 频率 | 频率竞争/lock-in | KH 与自然频率交叉区出现 plateau | 文本可确认 |
| Fig. 12-14 | 频率证据核心 | mixing layer 对频率有 attraction effect | waving branch 近一阶，flapping branch 近二阶 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节顺序是：Introduction -> Mathematical model -> Numerical settings and parameter space -> Results and discussion -> Conclusions。结构不是严格 IMRaD，而是“模型方法 + 参数空间 + 机理结果”型。

Introduction 先铺生态和冠层流背景，再引出 KH 不稳定与自然频率冲突，最后说明模型选择。Method 章节按 LBM、FEM、IBM、coupling 分模块展开，服务于“fully coupled”可信度。Numerical settings 把物理问题转为可扫参数的计算设计。Results 章节内部节奏清楚：先分类，再解释涡结构，再讨论冠层密度，再讨论 lock-in，最后讨论其他参数边界。Conclusion 三段回收：行为/涡结构、密度机制、频率机制，并附未来工作。

标题命名偏好是描述型，几乎每个小节直接暴露变量或机制，如 “The influence of canopy density on mixing layer instability” 和 “Lock in effect”。这种命名适合工程/流体期刊，因为读者能快速定位变量-现象关系。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: Introduction（背景定位/文献缺口）
- L2 p.3: Mathematical model（方法/模型/算法）
  - L3 p.3: Lattice Boltzmann method（方法/模型/算法）
  - L3 p.4: Finite element method（方法/模型/算法）
  - L3 p.4: Immersed boundary method（方法/模型/算法）
  - L3 p.5: Fluid–structure#xcoupling（对象/模块/过渡章节）
- L2 p.5: Numerical settings and parameter space（对象/模块/过渡章节）
- L2 p.6: Results and discussion（结果/验证/讨论）
  - L3 p.6: Dynamic behaviors of vegetation canopy（对象/模块/过渡章节）
  - L3 p.8: Vortical structures in different vegetation behaviors（对象/模块/过渡章节）
  - L3 p.12: The influence of canopy density on mixing layer instability（对象/模块/过渡章节）
  - L3 p.15: Lock in effect（对象/模块/过渡章节）
  - L3 p.18: Discussion on the effects of other parameters（结果/验证/讨论）
- L2 p.20: Conclusions（结论/贡献回收）
- L2 p.21: CRediT authorship contribution statement（尾部材料）
- L2 p.21: Declaration of competing interest（尾部材料）
- L2 p.21: Acknowledgments（尾部材料）
- L2 p.21: Appendix. Grid independence test（尾部材料）
- L2 p.22: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| Introduction | 1 | 2 | 背景定位/文献缺口 |
| Mathematical model | 3 | 2 | 方法/模型/算法 |
| Lattice Boltzmann method | 3 | 3 | 方法/模型/算法 |
| Finite element method | 4 | 3 | 方法/模型/算法 |
| Immersed boundary method | 4 | 3 | 方法/模型/算法 |
| Fluid–structure#xcoupling | 5 | 3 | 对象/模块/过渡章节 |
| Numerical settings and parameter space | 5 | 2 | 对象/模块/过渡章节 |
| Results and discussion | 6 | 2 | 结果/验证/讨论 |
| Dynamic behaviors of vegetation canopy | 6 | 3 | 对象/模块/过渡章节 |
| Vortical structures in different vegetation behaviors | 8 | 3 | 对象/模块/过渡章节 |
| The influence of canopy density on mixing layer instability | 12 | 3 | 对象/模块/过渡章节 |
| Lock in effect | 15 | 3 | 对象/模块/过渡章节 |
| Discussion on the effects of other parameters | 18 | 3 | 结果/验证/讨论 |
| Conclusions | 20 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 21 | 2 | 尾部材料 |
| Declaration of competing interest | 21 | 2 | 尾部材料 |
| Acknowledgments | 21 | 2 | 尾部材料 |
| Appendix. Grid independence test | 21 | 2 | 尾部材料 |
| References | 22 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是：生态功能 -> 冠层顶部混合层 -> 频率争议 -> 模型争议 -> 本文方案。每段末尾都有自然转折，通常用 “However” 或 “Considering” 把已有认识推向不足。

Results 的段落多采用“图示观察 -> 物理解释 -> 参数含义 -> 应用/机制外推”。例如 flapping 段先读 Fig. 5b，再解释涡旋穿透和剪切力，再联系 Fig. 6/7 的阻力与偏转，最后提出垂向输运和沙化启发。

Discussion on other parameters 的功能是控边界。作者没有把二维低 Re 结果硬推到真实冠层，而是分别讨论 Re、M、gravity/buoyancy、2D approximation，属于主动防审稿风险的段落。

## 13. 文笔画像与语言习惯

整体语气偏机制解释型，claim 强度中等偏强。作者喜欢用 “it can be seen/observed/indicated” 从图表引出结论，再用 “as a result/therefore/while” 给出因果链。强动词包括 investigate、explore、indicate、demonstrate、reveal、suppress、enhance、attract。

时态上，Introduction 综述用现在完成时和一般过去时；方法用一般现在时；结果读图常用一般现在时和被动结构；结论用一般现在时回收贡献。被动语态较多，如 “is solved by”、“is handled by”、“is observed”，但在机制解释处也会用主动结构，如 “the mixing layer acts to attract”。

形容词/副词习惯：coherent、dynamic、regular、irregular、representative、dominant、noticeable、spontaneous、gradually、slightly、significantly。作者会用 hedging 控制外推，如 “is expected to”、“may carry”、“one possible compromise”。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：24855
- 高频词：vegetation(85)；canopy(46)；fluid(39)；flow(28)；structure(23)；velocity(23)；density(21)；model(19)；frequency(18)；method(16)；aquatic(15)；represents(15)；terrestrial(14)；waving(13)；instability(12)；channel(12)；given(12)；element(12)；boundary(11)；canopies(10)
- 高频名词化/学术名词：vegetation(85)；structure(23)；velocity(23)；density(21)；instability(12)；element(12)；addition(7)；motion(7)；inflection(6)；expression(6)；influence(5)；function(5)；condition(4)；thickness(4)；relaxation(4)
- 高频学术动词：indicated(6)；predicted(4)；provide(3)；compared(2)；presented(2)；analyzed(2)；analyze(1)；estimated(1)；demonstrated(1)；validated(1)
- 高频形容词：aquatic(15)；terrestrial(14)；element(12)；boundary(11)；natural(9)；flexible(7)；different(7)；dynamic(6)；typical(6)；material(5)；dimensionless(5)；individual(4)；spatial(4)；external(4)；displacement(4)
- 高频副词：finally(3)；numerically(2)；briefly(2)；nonlinearly(2)；physically(2)；generally(2)；fully(2)；experimentally(1)；greatly(1)；synchronously(1)；recently(1)；partly(1)；relatively(1)；widely(1)；mainly(1)
- 高频二词短语：fluid structure(15)；vegetation canopy(11)；terrestrial vegetation(10)；aquatic vegetation(8)；mixing layer(7)；vegetation element(7)；vegetation canopies(6)；ghisalberti nepf(6)；inflection point(6)；frequency canopy(6)；natural frequency(5)；material properties(5)
- 高频三词短语：fluid structure model(5)；mass ratio vegetation(4)；aquatic vegetation terrestrial(4)；aquatic terrestrial vegetation(4)；waving frequency canopy(3)；natural frequency canopy(3)；mixing layer instability(3)；dimensionless mass ratio(3)；vegetation element discretized(3)；finite element method(3)；immersed boundary method(3)；canopies ghisalberti nepf(2)
- 被动语态估计：77；`we + 动作动词` 主动句估计：0
- 一般现在时线索：143；一般过去时线索：201；现在完成时线索：0；情态动词线索：21

分章节正文词频：

- Introduction: canopy(24)；flow(16)；frequency(15)；vegetation(13)；nepf(10)；waving(10)；canopies(9)；found(7)
- Mathematical model: fluid(1)；structure(1)；interaction(1)；described(1)；briefly(1)；case(1)；setup(1)；relevant(1)
- Results and discussion: vegetation(25)；canopy(6)；density(6)；aquatic(5)；terrestrial(5)；set(4)；typical(3)；values(3)
- Conclusions: vegetation(47)；fluid(33)；structure(20)；canopy(16)；method(16)；velocity(15)；density(14)；model(13)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：X are abundant in nature and play an important role in... 可复用为“对象广泛存在 + 功能重要”开场。
- Gap 句式：The interaction between X, as well as its influence on Y, remain relatively underexplored. 适合双向耦合类 gap。
- 冲突句式：This finding conflicted with the X model in which... 用于制造理论张力。
- 方法句式：A fully coupled fluid-structure modeling approach is used to investigate... 适合方法-问题直接对应。
- 结果句式：The behavior can be classified into five modes... 适合参数扫描后的分类贡献。
- 机制句式：This can be attributed to... / As a result... / On the one hand... on the other hand... 适合多因素竞争机制。
- 边界句式：Although further insight is obtained, several areas remain for further investigation. 适合结尾收束。

可复用关键词组：mixing layer instability、coherent vortices、bending rigidity、canopy density、dynamic response、lock-in effect、natural frequency、momentum thickness、vertical transport、parameter map。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
  可迁移模板：Vegetation canopies, such as seagrass meadow, crop field and dense forest, are abundant in nature and play an important role in a wide range of ecological services.
- 原句：In order to cover most of the parameter space that governs the behavior of both aquatic and terrestrial vegetation, twelve different values of K (K0 ∼K11) are tested in the following tests, which are distributed in powers of ten as Ki = 5 × 10−3+(2(i−1)/9), i = 0 ∼11 (22) Aside from the material properties of individual vegetation, the spatial density of the vegetation canopy is also an important parameter to be investigated.
  可迁移模板：In order to cover most of the parameter space that governs the behavior of both aquatic and terrestrial vegetation, twelve different values of K (K0 ∼K11) are tested in the following tests, which are distributed in powers of ten as Ki = X× X−X+(X(i−X)/X), i = X∼X(X) Aside from the material properties of individual vegetation, the spatial density of the vegetation canopy is also an important parameter to be investigated.
#### Gap/转折句
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  可迁移模板：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above METHOD instability will not be applicable anymore.
- 原句：However, in their study the natural frequency of the canopy was estimated in the fluid, which is smaller than the coupled KH frequency in the lock-in range.
  可迁移模板：However, in their study the natural frequency of the canopy was estimated in the fluid, which is smaller than the coupled METHOD frequency in the lock-in range.
- 原句：However, the frequency of KH instability was not considered in their study since the number of flaps was too few to generate the mixing boundary layer.
  可迁移模板：However, the frequency of METHOD instability was not considered in their study since the number of flaps was too few to generate the mixing boundary layer.
#### 方法提出句
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
- 原句：In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
  可迁移模板：In this paper a fully coupled fluid–structure modeling approach is used to investigate the interaction mechanism between the vegetation canopy and the mixing layer that arises above it.
- 原句：The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
  可迁移模板：The dependence of vegetation behavior on the bending rigidity and canopy density is explored and five representative behavior states of vegetation are observed: static, flapping, dual, regular waving and irregular waving.
- 原句：The vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation.
  可迁移模板：The vortical structures observed in the mixing layer associated with each state are compared, and the influence of canopy density on the mixing layer development is investigated, with a particular focus on flow features relevant to vegetation.
- 原句：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
  可迁移模板：The interaction between this unsteady flow above the mixing layer, as well as its influence on the vegetation canopy itself, remain relatively underexplored, with most prior studies employing significant modeling assumptions to simplify the system.
#### 结果呈现句
- 原句：In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, 2002).
  可迁移模板：In addition, such drag discontinuity also results in strong velocity shear at the top of the canopy, making the flow in this region roll up and form the coherent canopyscale vortices which propagate downstream through the canopy (Ghisalberti and Nepf, X).
- 原句：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. 1.
  可迁移模板：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. X.
- 原句：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
  可迁移模板：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
- 原句：The results indicated that the waving motion of these two plants always occurred near their own natural frequencies.
  可迁移模板：The results indicated that the waving motion of these two plants always occurred near their own natural frequencies.
- 原句：Recently, O’Connor and Revell (2019) numerically investigated the waving interactions of a flexible canopy with different material properties in an open channel flow, their results displayed a wide range of flap patterns of canopy and indicated that the lock-in effect occurred when the mean waving frequency of the canopy approached the coupled KH frequency.
  可迁移模板：Recently, O’Connor and Revell (X) numerically investigated the waving interactions of a flexible canopy with different material properties in an open channel flow, their results displayed a wide range of flap patterns of canopy and indicated that the lock-in effect occurred when the mean waving frequency of the canopy approached the coupled METHOD frequency.
#### 贡献/增量句
- 原句：These canopies can provide habitats for wildlife (Carpenter and Lodge, 1986), capture suspended sediment (Palmer et al., 2004), adjust temperature (Karlsson, 2000) and improve water/air quality (Moore, 2004).
  可迁移模板：These canopies can provide habitats for wildlife (Carpenter and Lodge, X), capture suspended sediment (Palmer et al., X), adjust temperature (Karlsson, X) and improve water/air quality (Moore, X).
- 原句：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. 1.
  可迁移模板：The wavelike motion of vegetation canopy, called honami in terrestrial flow or monami in aquatic flow, provides the striking visualization of such propagations, as shown in Fig. X.
- 原句：Ghisalberti and Nepf (2006) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.
  可迁移模板：Ghisalberti and Nepf (X) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.
- 原句：In order to further investigate the above lock-in mechanism, Gosselin and Langre (2009) improved the fluid model of Py et al. (2006, 2004) by removing the irrotationality assumption and investigated three different KH frequencies: the coupled KH frequency in flow with a flexible canopy, the pure KH frequency in flow without any canopy and the heavy KH frequency in flow with a still/rigid canopy.
  可迁移模板：In order to further investigate the above lock-in mechanism, Gosselin and Langre (X) improved the fluid model of Py et al. (X, X) by removing the irrotationality assumption and investigated three different METHOD frequencies: the coupled METHOD frequency in flow with a flexible canopy, the pure METHOD frequency in flow without any canopy and the heavy METHOD frequency in flow with a still/rigid canopy.
- 原句：In addition, a strong-coupling implicit scheme is also introduced in this model in order to improve the stability and accuracy of algorithm.
  可迁移模板：In addition, a strong-coupling implicit scheme is also introduced in this model in order to improve the stability and accuracy of algorithm.
#### 限制/边界句
- 原句：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above KH instability will not be applicable anymore.
  可迁移模板：However, it should be noted that when the vegetation canopy becomes sparse, the prominence of the inflection point in the mean velocity profile is reduced and the above METHOD instability will not be applicable anymore.
- 原句：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
  可迁移模板：This finding conflicted with the mixing layer model in which the main waving frequency of canopy should be dominated by the flow instability, and therefore indicated a noticeable influence of canopy motion on the flow dynamics.
- 原句：Ghisalberti and Nepf (2006) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.
  可迁移模板：Ghisalberti and Nepf (X) then performed a flume experiment with both rigid and flexible model canopies to study the structure of vegetated shear flow, they found the waving motion of canopy could improve the vertical momentum transport within the canopy and noted that the deflection of the canopy was more than just a passive response to the coherent vortices.
- 原句：In addition, it should be noted that the difference of conclusions among the above studies is partly due to the different modeling approaches they use.
  可迁移模板：In addition, it should be noted that the difference of conclusions among the above studies is partly due to the different modeling approaches they use.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是“综述背景 + 对立结论 + 模型选择背书”。生态功能引用用于证明问题重要；Ghisalberti/Nepf/Raupach 用于建立 mixing layer/KH 传统解释；Finnigan/Py/Gosselin/O'Connor/Zhang 用于建立频率解释冲突；LBM/IBM/FEM 相关文献用于证明数值框架可靠。

作者对前人态度比较克制：不是直接批判，而是说 simplified assumptions、differing conclusions、different modeling approaches。这样既保留前人贡献，又为 fully coupled 模型腾出必要性。

引用的 gap 制造方式很值得学：先展示 A 类文献认为 KH 控制，再展示 B 类文献认为自然频率重要，再说两类文献模型不同，所以本文要用更完整耦合模型统一解释。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：0
- Introduction 引文簇数量估计：0
- References 条目数：97
- 可识别年份条目数：54
- 2021 年及以后文献数：1
- 2010 年前经典文献数：34
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Journal of Fluids and Structures(1)
- 引文簇样例：未识别

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 2012. The wind in the willows: flows in forest canopies in complex terrain. Annu. Rev. Fluid Mech. 44,
479–
- 504. Belcher, S., Jerram, N., Hunt, J.,
- 2003. Adjustment of a turbulent boundary layer to a canopy of roughness elements. J. Fluid Mech. 488, 369–
- 398. Berry, P.M., Sterling, M., Spink, J.H., Baker, C.J., Sylvester-Bradley, R., Money, S.J., Tams, A.R., Ennos, A.R., Sparks, D.L.,
- 2004. Understanding and reducing
lodging in cereals. Adv. Agron. 84, 217–
- 271. Bhatnagar, P.L., Gross, E.P., Krook, M.,
- 1954. A model for collision processes in gases. I. Small amplitude processes in charged and neutral
one-component systems. Phys. Rev. 94 (3), 511–
- 525. Carpenter, S.R., Lodge, D.M.,
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 二维模型对真实冠层的外推有限，尤其在高 Re 下三维涡、横向 coherent vortices、kinking/pairing 可能改变结论。
2. Re=100 接近作者前作中能出现 waving instability 的低限，不代表自然水生/陆生冠层的典型范围。
3. lock-in 的“attraction effect”主要来自频率曲线对比，缺少更直接的因果干预，例如固定结构频率或人工改变速度剖面。
4. flapping 与沙化/风蚀联系没有颗粒输运模型支持，属于应用假说。
5. 混种不同刚度作物保护策略只做一个 preliminary test，缺少间距、比例、成本和真实植物参数敏感性。
6. 植被接触、碰撞、重力/浮力和三维渗透性均未进入主模型，可能影响高密度/大偏转区域。
7. 网格独立性有附录，但状态分类边界对数值分辨率和时间长度的敏感性仍需复核。

## 17. 可复用资产

- 选题套路：从“前人结论冲突”而不是“空白”切入，显得 gap 更真实。
- 参数图谱资产：用二维参数空间把复杂行为分类，是机制论文非常强的证据组织方式。
- 图表链条：行为快照 -> 参数 map -> 力/偏转量化 -> 速度剖面 -> 频率图，层层从现象推到机制。
- 讨论边界资产：单独设置 “effects of other parameters” 小节，主动处理 Re、mass ratio、gravity、2D approximation。
- 写法资产：每个结果小节都用“物理观察 + 量化指标 + 机制解释 + 更大意义”的节奏。

## 18. 对我写论文的启发

如果自己的研究也有“模型解释不一致”的领域，可以模仿本文：不要只宣称方法更复杂，而要说明复杂模型能解决哪个解释冲突。最值得迁移的是参数空间图和频率对照图：一个负责分类，一个负责机制。

另一个启发是，应用外推可以写，但要放在机制证据之后，并用谨慎措辞。本文把沙化和作物保护作为“indicates/inspired by/preliminary”的层级，而不是把它包装成已完成工程方案。

## 19. 最终浓缩

这篇论文的核心价值在于把植被冠层 waving/flapping 从单一 KH 不稳定解释推进到“混合层-结构属性耦合控制”解释。它最值得学习的是：用 fully coupled FSI 模型扫参数空间，用涡结构解释行为类别，用自然频率与 KH 频率比较解释 lock-in。最大风险是二维低 Re 结果和应用外推仍需 PDF 图像与更真实物理模型复核。
