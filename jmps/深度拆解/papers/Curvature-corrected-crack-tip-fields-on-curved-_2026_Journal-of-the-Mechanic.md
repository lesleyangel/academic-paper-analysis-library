# Curvature-corrected crack-tip fields on curved manifolds: A geometric framework for fracture

## 0. 读取说明
- 源 PDF：`jmps/文献/Curvature-corrected-crack-tip-fields-on-curved-_2026_Journal-of-the-Mechanic.pdf`
- 源 TXT：`jmps/文本/txt/Curvature-corrected-crack-tip-fields-on-curved-_2026_Journal-of-the-Mechanic.txt`
- 图像核查：txt 可读理论叙述、图题、实验讨论和结论，但角函数曲线、裂纹路径 overlay、实验装置和材料表征图需结合 PDF 图像核查。
- 论文类型：理论推导 + 实验验证的几何断裂力学论文，目标是建立曲面流形上的曲率修正裂纹尖端场和 MTS 准则。

## 1. 基本信息与论文身份
- 作者：Mirmilad Mirsayar。
- 期刊/年份：Journal of the Mechanics and Physics of Solids, 214, 2026, 106667。
- DOI：10.1016/j.jmps.2026.106667。
- 关键词：non-Euclidean fracture；crack-tip asymptotic solution；manifold curvature；Laplace-Beltrami operator；differential geometry。
- 研究对象：曲面/非欧几里得流形上的裂纹尖端奇异场、角向应力函数和裂纹路径预测。
- 方法类型：differential geometry of manifolds；Laplace-Beltrami Airy stress function；perturbation analysis；Fredholm solvability；curvature-corrected MTS；橡胶曲面实验与 FE 增量裂纹模拟。
- 目标读者：断裂力学、壳膜力学、几何力学、柔性器件/生物膜失效研究者。
- JMPS 定位：强理论框架论文，用实验路径对比证明几何修正的工程必要性。

## 2. 摘要与核心信息提取
摘要从经典断裂力学的 flat Euclidean assumption 切入，指出许多自然和工程薄结构在曲面上失效，平面 near-tip fields 可能不完整。作者声称给出第一套直接在 curved manifold 上推导的 crack-tip asymptotic solution。方法链是 Airy stress function -> Laplace-Beltrami operator -> perturbation analysis -> Fredholm solvability。关键理论结果是：curvature preserves the universal `r^-1/2` stress singularity, while perturbing angular eigenfunctions and modifying near-tip stress distribution。实验表明曲率修正 MTS 能匹配曲面橡胶裂纹路径，而 flat-surface solution 会累积路径误差。

## 3. 选题层深拆
选题来自经典断裂力学平面假设与真实曲面薄结构之间的错位。薄膜、壳、柔性电子、生物膜等都在 curved surfaces 上工作或失效，但 Williams 型奇异场和经典 MTS 多默认平面欧氏域。曲率不是材料非均匀性，也不是外载梯度，而是由 metric 与 compatibility 进入控制方程的内禀几何场。本文的问题被收束为：曲率如何进入 crack-tip asymptotic fields？它是否改变奇异阶、角函数和裂纹路径？这个问题足够窄，且具有很强理论意义。

## 4. 领域位置与文献版图
文献版图包括经典 LEFM/Williams 奇异场、能量/应力/应变断裂准则、曲面膜/壳/表面弹性理论、薄壳裂纹路径数值/经验研究、差分几何与非欧弹性。作者强调壳膜理论擅长 smooth deformation and stress fields，但 crack 引入 singular perturbation，不能从光滑解直接推断尖端场。本文站在 differential geometry 与 crack-tip asymptotics 的交界，区别在于从 Laplace-Beltrami operator 和 curvature-corrected biharmonic equation 直接推导，而不是把曲率作为后处理修正。

## 5. Gap 制造机制
- 显式 gap：经典裂纹尖端场缺少 curved manifold 上的内禀推导；曲面裂纹研究多依赖数值或经验观察。
- 隐含 gap：如果把 curvature 当作 passive geometry，裂纹路径预测中的局部小误差会在传播中累积为显著偏差。
- Gap 类型：理论 gap + 准则 gap + 实验验证 gap。
- 审稿追问：一阶曲率扰动的适用范围多大？实验中摩擦、基底约束、材料非线性是否混入曲率效应？“first” claim 的文献覆盖是否充分？

## 6. 创新性判断
作者贡献包括：直接在 curved manifold 上推导 crack-tip asymptotic solution；证明曲率保持 `r^-1/2` 奇异阶但修正 angular eigenfunctions；得到 closed-form Mode I/II fields；构造 curvature-dependent MTS；用曲面橡胶实验和 FE 路径预测验证。真实创新高，理论命题明确且实验对比直接。易被挑战的是实验是否能独立分离 curvature 与 global boundary effect，以及一阶曲率修正对高曲率或大变形材料的适用边界。

## 7. 论证链条复原
背景：经典 fracture mechanics 依赖平面欧氏域，真实薄结构常在曲面上断裂。  
文献：壳/膜几何力学成熟，但裂纹奇异场不足；已有路径研究多为数值或经验。  
Gap：缺少曲面流形上的 singular fields 和相应传播准则。  
方法：用 Laplace-Beltrami operator 构造 Airy stress function，推导 curvature-corrected biharmonic equation，Fredholm solvability 处理 eigenproblem，得 Mode I/II fields，构造 curvature-corrected MTS，并用实验/FE 验证。  
证据：Fig. 2 angular functions；Fig. 3 fracture parameters；Fig. 4-5 setup/material；Fig. 6 Griffith length/kink angle；Fig. 7 crack patterns；Fig. 8 flat vs curvature-corrected path。  
结论：曲率不改 leading singular exponent，但会改变角向应力结构；mixed-mode 情况差异最大；忽略曲率会产生累积路径误差。

## 8. 方法/理论/模型细拆
方法从曲面 metric、covariant derivatives 和 Laplace-Beltrami operator 出发，以替代平面 Laplacian；对 Airy stress function 建立曲率修正 biharmonic equation；在 crack-tip local polar coordinates 中进行渐近展开，将曲率作为扰动；通过 Fredholm solvability 获得 angular eigenfunction correction；再将应力场放入 MTS 准则求 kink angle。实验中，合成橡胶 sheet conform to 3D-printed curved substrate，材料用 Neo-Hookean 拟合，FE 中每一步提取 SIF，按 `Δa=0.2 mm` 增量推进并更新局部曲率。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 曲率通过 metric/covariant operators 进入 crack-tip problem | Sections 2-3 | Laplace-Beltrami biharmonic equation | 理论推导 | 强 | 推导细节需审查 |
| 曲率不改变 leading `r^-1/2` 奇异阶 | Abstract、Conclusion | perturbation/Fredholm solvability | 渐近分析 | 强 | 高曲率边界 |
| 曲率扰动 angular eigenfunctions | Sections 4-5 | Mode I/II fields、Fig. 2 | 理论+图示 | 强 | 图示需核查 |
| 曲率修正 MTS 改善 kink angle 预测 | Sections 6-7 | Fig. 3、Fig. 6 | 准则+实验 | 中强 | 边界效应可能混入 |
| flat MTS 误差随传播累积 | Section 7 | Fig. 8 增量路径对比 | 数值+实验 | 强 | 路径匹配需视觉核查 |
| 曲率是 fracture control parameter | Conclusion | 理论与实验闭环 | 综合推论 | 中强 | 适用范围需限定 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 2 | 曲率修正 angular functions 随 Q 变化 | 角函数被扰动 | 理论可视化 | 是 |
| Fig. 3 | kink angle/fracture loci 与 Q | MTS 受曲率影响 | 连接公式与预测量 | 是 |
| Fig. 4 | 实验装置 | 曲面裂纹实验 | validation 基础 | 是 |
| Fig. 5 | 材料表征/曲率分布 | 材料和几何输入 | 排除参数任意性 | 是 |
| Fig. 6 | Griffith length/kink angle | 实验量化 | 支撑 curvature criterion | 是 |
| Fig. 7 | 不同 β 裂纹路径 | 曲率诱导偏折 | 直观证据 | 是 |
| Fig. 8 | flat vs curvature-corrected overlay | 主验证 | 证明路径累积差异 | 是 |
| Laplace-Beltrami biharmonic equation | 控制方程 | 理论框架 | 从根部修正平面假设 | 否 |
| Fredholm solvability/eigenproblem | 处理曲率扰动 | 保持奇异阶、修正角函数 | 数学可信度 | 否 |

## 11. 章节结构与篇章布局
Introduction：经典平面假设 -> 曲面结构普遍性 -> curvature as active mechanical role -> singular field gap。Section 2-4 逐步搭建微分几何、控制方程和可解性；Section 5 给 Mode I/II stress fields；Section 6 构造 MTS；Section 7 用实验和 FE 讨论；Conclusion 回收理论、实验、意义和未来扩展。结构很像“数学构件逐级装配”，适合理论论文。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Curvature-corrected-crack-tip-fields-on-curved-_2026_Journal-of-the-Mechanic.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：12
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Differential geometry of curved cracked manifolds | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Fredholm solvability and curvature-corrected eigenproblem | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Curvature-corrected crack-tip stress fields | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1 Mode I stress fields | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.2 Mode II stress fields | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6 Curvature-corrected maximum tangential stress criterion | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 7 Experimental analysis and discussion | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 7.1 Testing setup | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 7.2 Material characterization | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 7.3 Prediction of the crack propagation path | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 8 Conclusions | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 具有强概念表达，例如把 geometry 从 passive container 提升为 active control parameter。理论段落按定义、算子、方程、可解性、应力场、准则推进。实验段落从材料/装置到 kink angle，再到全路径。Fig. 8 后的讨论强调小的 local curvature corrections 会在传播中累积，这使“次阶项”变成工程上不可忽略的路径误差。

## 13. 文笔画像与语言习惯
整体语气理论雄心强，概念化语言鲜明。强词包括 first, intrinsic, unified framework, first-class control parameter。问题表达常用 flat Euclidean domains, structural deficiency, geometry-mediated instability。方法表达常用 intrinsic formulation, covariant operators, perturbation analysis, solvability。结果表达常用 preserves singularity, perturbs angular eigenfunctions, accumulates path errors。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：curvature(121)；crack(109)；stress(98)；fracture(68)；cos(59)；mode(53)；crack-tip(52)；angular(49)；fields(48)；curved(41)；operator(41)；sin(40)；local(39)；geometric(33)；curvature-corrected(31)；mirsayar(28)；classical(27)；asymptotic(27)；material(26)；metric(26)
- 高频学术名词：curvature(121)；stress(98)；fracture(68)；fields(48)；equation(42)；structure(36)；solution(34)；analysis(30)；material(26)；propagation(24)；function(21)；conditions(19)；field(16)；framework(15)；correction(13)；parameter(12)
- 高频学术动词：shows(7)；predicted(7)；shown(6)；derived(6)；predict(5)；evaluated(5)；show(4)；demonstrate(4)；developed(4)；capture(3)；derive(2)；reveal(2)；compared(2)；estimated(2)；indicates(2)；validate(1)
- 高频形容词：local(78)；experimental(34)；geometric(33)；elastic(32)；classical(27)；asymptotic(27)；homogeneous(26)；material(26)；metric(26)；theoretical(20)；critical(16)；biharmonic(16)；exponent(16)；component(16)；present(15)；kic(14)
- 高频副词/连接副词：locally(20)；therefore(18)；experimentally(18)；consequently(14)；systematically(14)；approximately(10)；directly(8)；explicitly(7)；generally(6)；however(6)；asymptotically(5)；fundamentally(5)；family(4)；intrinsically(3)；independently(3)；geometrically(3)
- 高频二词短语：cos cos(33)；sin sin(23)；crack tip(22)；stress fields(21)；beltrami operator(13)；mts criterion(13)；laplace beltrami(12)；gaussian curvature(12)；crack-tip stress(10)；stress function(10)；airy stress(10)；biharmonic equation(10)；synthetic rubber(10)；crack paths(9)；singular exponent(9)；boundary conditions(9)
- 高频三词短语：cos cos cos(19)；sin sin sin(14)；laplace beltrami operator(10)；airy stress function(8)；crack-tip stress fields(7)；linear elastic fracture(6)；near crack tip(5)；maximum tangential stress(4)；geodesic polar coordinates(4)；traction-free boundary conditions(4)；stress intensity factor(4)；angular stress distribution(4)

**主动、被动与句法**

- 被动语态估计次数：116
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：809
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：187
- 一般过去时线索：75
- 现在完成时线索：5
- 情态动词线索：35
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：curved(5)；stress(5)；crack-tip(4)；fields(4)；fracture(4)；curvature(3)；crack(3)；curvature-corrected(2)
- 1. Introduction：fracture(17)；stress(15)；curvature(15)；crack(14)；curved(12)；geometric(11)；fields(9)；material(7)
- 2. Differential geometry of curved cracked manifolds：curvature(29)；metric(18)；gij(16)；operator(13)；crack(12)；tip(11)；geometric(10)；expansion(10)
- 4. Fredholm solvability and curvature-corrected eigenproblem：angular(18)；cos(18)；mode(15)；operator(14)；curvature(14)；exponent(11)；williams(9)；lnr(9)
- 5. Curvature-corrected crack-tip stress fields：modes(4)；conditions(3)；solution(3)；homogeneous(3)；kernel(3)；asymptotic(2)；stress(2)；must(2)
- 5.1. Mode I stress fields：cos(14)；mode(4)；sin(4)；krp(3)；curvature-corrected(2)；angular(2)；function(2)；stress(2)
- 5.2. Mode II stress fields：sin(27)；cos(16)；curvature(14)；stress(13)；mode(10)；angular(7)；component(7)；fields(7)
- 6. Curvature-corrected maximum tangential stress criterion：fracture(13)；curvature(13)；crack(10)；stress(9)；kic(9)；mode(7)；mixed-mode(7)；mts(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
`Classical X assumes Y. However, many systems fail under Z, where Y-based fields become insufficient.`

### 14.2 方法与框架表达
`Starting from A, we construct B using C and expand it asymptotically via D.`

### 14.3 结果与趋势表达
`Curvature preserves A while perturbing B and modifying C.`

### 14.4 机制解释表达
`Small local corrections accumulate during propagation and produce substantial long-range deviations.`

### 14.5 贡献与意义表达
`These results establish X as a quantifiable control parameter in Y.`

### 14.6 局限与未来工作表达
`The formulation provides a natural foundation for future extensions to anisotropy, spatially varying curvature, and multiphysics fracture.`

## 15. 引用策略与文献使用
引用层次清楚：Williams/LEFM 和传统断裂准则定义平面基线；薄膜、壳、生物膜、柔性器件文献证明曲面结构普遍；壳膜几何力学文献证明 curvature 进入应力是有理论基础的；曲面裂纹数值/经验文献制造 singular field gap。风险是 “first” claim 必须对相关 shell fracture asymptotics 文献覆盖充分。

## 16. 审稿人视角风险
最大攻击面是实验中曲率效应是否与摩擦、基底约束、厚度效应和材料非线性混淆。第二是 theoretical boundary：一阶曲率扰动、薄结构和各向同性条件限制适用范围。第三是 pure Mode I/II leading order 不受曲率影响，实验 β 必须覆盖 mixed-mode 区间才有说服力。Fig. 8 是全文胜负手，必须结合 PDF 核查。

## 17. 可复用资产
- 选题角度：识别经典理论的隐含几何假设，并在 governing-equation 层面修正。
- 论证链：几何定义 -> 控制方程 -> 渐近场 -> 准则 -> 实验路径。
- 图表设计：理论角函数图与实验路径图配套。
- 句型骨架：`preserves the universal singularity while perturbing angular eigenfunctions`。
- 不宜直接模仿：强概念词必须有严密推导和实验闭环。

## 18. 对我写论文的启发
本文示范了理论论文如何讲大问题：先指出经典理论的隐含世界观，再把缺失变量提升为控制参量。写类似论文时可问：已有模型是否在控制方程层面排除了重要因素？如果是，贡献就不是经验修正，而是框架重写。结果中要说明为什么小修正重要，例如路径误差的传播累积。

## 19. 最终浓缩
最值得学：从 Laplace-Beltrami 控制方程出发把曲率纳入裂纹尖端场。最大风险：一阶曲率、材料和边界条件的适用范围需严控。三个可迁移动作：找出经典隐含假设；在方程层面引入缺失变量；用累积误差证明次阶修正的重要性。

补充写作素材库：本文适合提取“理论框架重写”的表达。问题词包括 flat Euclidean domains、classical crack-tip fields、structural deficiency、passive container、geometry-mediated instability。方法词包括 intrinsic formulation、surface metric、covariant operators、Laplace-Beltrami operator、curvature-corrected biharmonic equation、Fredholm solvability、angular eigenfunctions。结果词包括 preserves the singular exponent、redistributes near-tip stresses、curvature-informed MTS、cumulative path deviation、geometry-guided failure control。边界词包括 leading order、first-order correction、pure-mode limits、spatially varying curvature、anisotropic extension。

可迁移段落 1：Introduction 的强写法是“经典理论不是错，而是在控制方程层面排除了某个现实变量”。可迁移骨架为：“The classical framework has provided remarkable clarity and effectiveness. Yet its governing equations assume A, thereby excluding B from the outset. This is not a minor correction but a structural deficiency when systems operate under C.” 这种写法尊重经典理论，同时制造必要的理论缺口。

可迁移段落 2：理论结果的表达要区分“不改变什么”和“改变什么”。本文说 curvature does not change the leading singular exponent, but perturbs angular eigenfunctions。这个句型非常稳：先保留经典理论的 universal part，再指出新变量改变 directional distribution。类似地，其他理论论文也可写“X preserves the scaling law but modifies the prefactor/localization/path selection”。

可迁移段落 3：实验验证的说服力来自对照准则，而不是只展示曲面裂纹。Fig. 8 同时给 flat MTS 和 curvature-corrected MTS，使读者看到如果不用新理论会错在哪里。可迁移策略是：每个新准则都要和最强 baseline 在同一实验路径上对比，最好展示误差随传播/时间/循环数累积。

可迁移段落 4：局部小修正的重要性可通过“accumulation”论证。很多理论修正初看是高阶项，审稿人会问工程意义。本文的回答是：每一步路径偏差小，但裂纹传播中不断更新局部曲率，误差会积累成长期路径偏离。这个逻辑可用于疲劳损伤、相场演化、波传播相位误差和多步优化算法。

可迁移段落 5：未来工作表达也很具体：anisotropic materials、spatially varying curvature、coupled multiphysics fracture。它们不是随便列，而是沿着“材料复杂性、几何复杂性、物理场复杂性”三个维度展开。自己的论文也可按这三类组织未来扩展。

审稿回复策略：若被质疑曲率效应与全局边界效应混淆，可强调曲率修正是在 local crack-tip stress field 和 MTS criterion 中逐步更新，而不是对全局路径做经验拟合；flat 和 curvature-corrected 两种准则在同一 FE/实验几何上对比，差异主要来自 near-tip angular stress redistribution。若被质疑一阶扰动适用性，可承认高曲率、大变形或强各向异性需要扩展，但本文的贡献是建立 leading-order geometric correction，并证明即使 modest correction 也会因路径传播而累积。

模板化句群：`The new term does not destroy the universal singular structure; it modifies the angular distribution that controls path selection.` 这句话适合任何“保留经典标度、修正方向/幅值/路径”的理论论文。`The importance of the correction is revealed not at a single step, but through its accumulated effect during evolution.` 可用于解释小修正为何有工程意义。

最终使用提醒：这篇最适合沉淀到“经典理论隐含假设重写模板”。模仿时不要只说“考虑了曲率/温度/梯度”，而要说清楚该变量是在哪一级进入理论：边界条件、控制方程、能量泛函、渐近场，还是后处理准则。进入层级越靠前，理论贡献越强。

入库标签：非欧断裂；控制方程修正；曲率作为控制参量；渐近场；路径误差累积。

进一步可迁移提醒：这篇的贡献表达有一个隐藏技巧：先承认经典奇异阶仍成立，再说明角向函数改变。这样既不推翻经典，又证明新增变量必要。理论写作中，这种“保留核心、修正关键”的姿态很稳。

补充标签：Laplace-Beltrami；Fredholm solvability；curvature-informed MTS；mixed-mode path prediction。
