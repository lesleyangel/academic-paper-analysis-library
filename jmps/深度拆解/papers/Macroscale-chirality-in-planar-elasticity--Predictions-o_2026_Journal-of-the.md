# Macroscale chirality in planar elasticity: Predictions of granular micromechanics based extended micropolar model confirmed via classical micro finite element simulations

## 0. 读取说明
- 源 PDF：`jmps/文献/Macroscale-chirality-in-planar-elasticity--Predictions-o_2026_Journal-of-the.pdf`
- 源 TXT：`jmps/文本/txt/Macroscale-chirality-in-planar-elasticity--Predictions-o_2026_Journal-of-the.txt`
- 是否需要结合 PDF 图像核查：需要。位移场、微旋转场、边界层和 micro FE/micropolar 对比需结合 PDF。
- 本文类型：广义连续介质/力学超材料理论验证论文。

## 1. 基本信息与论文身份
- 题名：Macroscale chirality in planar elasticity: Predictions of granular micromechanics based extended micropolar model confirmed via classical micro finite element simulations
- 作者/机构：Nurettin Yilmaz, Luca Placidi, Anil Misra。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214 (2026) 106664。
- DOI：10.1016/j.jmps.2026.106664
- 关键词：Mechanical chirality; Granular micromechanics; Cosserat continua; Micropolar model; Granular motif
- 研究对象：平面弹性中由颗粒微结构诱导的宏观机械手性、负泊松效应和 micropolar/Cosserat 表征。
- 研究尺度：grain-pair 微结构、代表性材料点、宏观连续体位移/微旋转场、全场微 FE。
- 方法类型：granular micromechanics approach、extended 2D micropolar continuum、classical micro finite element simulation、参数研究。
- 证据类型：motif 设计、边界加载、网格收敛、反力-位移、位移场/微旋转场、micro FE 与 micropolar 对比、尺寸效应附录。
- 目标读者：Cosserat/micropolar 理论、颗粒微力学、力学超材料、均匀化和有限元读者。
- JMPS 风格定位：把广义连续体理论预测拉回微结构 FE 验证，是“理论-微结构-数值验证”型 JMPS。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先指出 classical Cauchy continuum 无法描述宏观手性；再说明 GMA 建立微-宏连接；随后用 granular motif 和 full-field micro FE 检验；最后强调 chiral effect 和 negative Poisson effect 可调。
- 背景句承担什么：说明宏观手性来自 stretch deformation 与 micro-rotation 的耦合。
- gap 句承担什么：这种宏观行为少见且 Cauchy 模型无法表示，需要高阶连续体和微结构验证。
- 方法句承担什么：GMA、extended micropolar model、micro FE 三者组成闭环。
- 结果句承担什么：micro FE 与 micropolar 预测在位移和旋转场上吻合，手性/auxetic 可调。
- 意义句承担什么：证明 extended micropolar model 对该 granular microstructure 高保真。
- 一句话主张：颗粒 motif 的特定 grain-pair 相互作用能在宏观平面弹性中产生手性和负泊松效应，且必须用 extended micropolar/Cosserat 模型而非 Cauchy 模型表征。
- 3-5 个核心关键词：mechanical chirality; granular motif; micropolar continuum; micro-rotation; auxetic response。

## 3. 选题层深拆
- 问题来源：经典 Cauchy 连续体没有微旋转自由度，无法描述某些颗粒/超材料微结构导致的宏观手性。
- 问题为什么重要：微结构设计可产生手性、负泊松效应和非标准耦合，是超材料设计的重要能力。
- 问题为什么现在值得做：广义连续体理论和 micro FE 验证工具成熟，可以检验 GMA 预测。
- 问题边界：二维 square granular motif；数值验证为主，未做物理实验制造验证。
- 选题的 JMPS 味道：用微结构机制证明高阶连续体不是数学装饰，而是必要模型。
- 选题可迁移性：适用于所有“经典连续体不足，需要广义自由度”的论文。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：Cosserat/micropolar 经典理论、颗粒微力学、chiral/auxetic metamaterials、tetrachiral lattices、微结构 FE 验证。
- 主要研究流派/方法路线：广义连续体理论、颗粒微力学、超材料设计、全场微 FE/homogenization。
- 每类研究解决了什么：Cosserat 提供微旋转；GMA 提供微-宏桥；超材料设计提供 motif；FE 提供验证。
- 每类研究留下什么不足：理论预测需要微观验证；Cauchy 模型无法表示微旋转；一些超材料缺少参数识别桥。
- 本文站在哪条线上：继承 Misra 等 GMA/micropolar granular continuum 路线，并用 micro FE 检验。
- 最接近前人工作：Cosserat 经典理论、Eringen microcontinuum、Misra 颗粒 micromechanics、chiral lattice 模型。
- 是否公平处理前人：文献处理是继承式，强调本文是验证和设计闭环。

## 5. Gap 制造机制
- 明示 gap：宏观平面机械手性的 micro-macro link 虽由 extended micropolar 模型预测，但需要 full-field classical micro FE 验证其有效性。
- 隐含 gap：如果只用 Cauchy 模型，即使 micro FE 显示手性，也无法在等效连续体中表达 micro-rotation 和 boundary layer。
- gap 类型：理论验证 gap、模型适用性 gap、设计机制 gap。
- gap 证据来自哪里：摘要、Introduction 对 Cauchy 局限的讨论、Fig. 8-12 的场变量对比。
- gap 是否足够窄：足够窄，限定到 square granular motif 的三种加载。
- gap 是否足够重要：重要，因为它决定是否需要 micropolar continuum。
- 如果我是审稿人会如何追问：结论是否依赖特定 motif？是否有实验验证？有限尺寸和边界层如何影响等效参数？

## 6. 创新性判断
- 作者声称的贡献：用 GMA 设计 granular motif；用 extended micropolar 模型预测宏观手性；用 classical micro FE 验证；展示 stiffness 调控。
- 我判断的真实创新：把微结构设计、等效 micropolar 参数和 full-field FE 验证串成闭环。
- 创新类型：理论验证创新 + 微结构设计创新 + 参数调控表达。
- 创新强度：中高。
- 创新必要性：必要，没有 micro FE 验证，高阶连续体预测容易显得抽象。
- 创新与证据匹配度：数值场对比强；实验和普适性证据不足。
- 容易被挑战的创新点：只验证一个设计 motif，泛化需要更多结构。

## 7. 论证链条复原
背景：Cauchy 模型缺少 micro-rotation，不能描述平面宏观手性。文献：Cosserat/micropolar 和 GMA 提供理论基础。gap：理论预测需要 micro FE 验证。问题：设计的 granular motif 是否真的表现出 micropolar 预测的 chiral/auxetic 响应？方法：GMA 推导 + extended micropolar continuum + micro FE。证据：网格收敛、反力-位移、位移场、微旋转场、grain count 收敛。发现：能量集中在连接，颗粒近似刚体；手性和负泊松可调；micro FE 与 micropolar 高度一致。机制：grain-pair 连接使伸长诱发旋转，微旋转与宏观应变耦合。意义：证明 micropolar continuum 对该类微结构必要。

## 8. 方法/理论/模型细拆
- 方法总框架：用 GMA 从 grain-pair strain energy 推导 2D extended micropolar continuum；设计 duoskelion square motif；建立等效 continuum 和 micro FE；在拉伸、压缩、剪切下比较反力、位移、微旋转和 grain rigid body motion。
- 关键概念：Cosserat continuum、micropolar elasticity、granular micromechanics、grain-pair interaction、micro-rotation ψ、relative rotation γ、auxetic response。
- 关键变量/参数：u1/u2、ψ、γ、grain-pair stiffness、reaction force、specimen size、grain count、加载边界。
- 核心假设：颗粒近似刚体，能量主要集中在连接；二维平面模型足以描述目标机制；GMA 参数可代表等效 continuum。
- 边界条件：75×75 mm square specimen，拉伸/压缩/剪切，top/bottom micro-rotation constrained，left/right free。
- 方法步骤：GMA 推导 -> micropolar 建模 -> motif 设计 -> micro FE 网格收敛 -> 三种加载 -> 参数研究 -> 场变量对比 -> 尺寸效应。
- 复现信息：图注提供几何、边界和网格线索；参数表需 PDF 核查。
- 方法复杂度是否合理：合理，因为目标是证明 Cauchy 不足和 micropolar 必要。
- 方法与 gap 的对应关系：GMA 提供微-宏参数桥，micropolar 提供微旋转自由度，micro FE 提供验证。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| Cauchy 模型无法描述该宏观手性 | 摘要/结果 | Cauchy 与 micropolar 场对比 | 模型对比 | 强 | 特定 motif |
| GMA 可设计 chiral/auxetic granular motif | 2/结论 | grain-pair 机制和 motif 设计 | 理论+设计 | 强 | 无实验制造 |
| 变形能集中在连接，颗粒近似刚体 | 3/结论 | micro FE strain energy distribution | 数值场 | 中强 | 需图像核查 |
| 微刚度可调节手性和负泊松效应 | 3.2 | Fig. 5-7 | 参数模拟 | 强 | 参数范围代表性 |
| micropolar 与 micro FE 场一致 | 3.3 | Fig. 8-12 | 全场对比 | 强 | 边界层细节需核查 |
| 尺寸增加后行为趋于尺度无关 | Appendix | Fig. A.1-A.2 | 附录验证 | 中 | 仍是数值验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1-2 | 材料点微结构和 duoskelion motif | 微-宏连接对象 | 给理论预测实体化 | 是 |
| Fig. 3-4 | 加载边界和网格收敛 | 仿真可信度 | 消除数值离散疑问 | 是 |
| Fig. 5-7 | 反力和参数研究 | 可调手性/auxetic 响应 | 展示设计自由度 | 是 |
| Fig. 8-10 | Cauchy 与 micropolar 位移场对比 | Cauchy 不足 | 场变量证据 | 是 |
| Fig. 11-12 | 微旋转/相对旋转与 micro FE 对比 | micropolar 高保真 | 核心验证 | 是 |
| 关键公式组 | grain-pair energy、micropolar strain measures、micro-macro stiffness identification | 从微结构到连续体 | 建立参数桥 | 需核查公式排版 |

## 11. 章节结构与篇章布局
- Abstract：Cauchy 局限、GMA、micro FE 验证、可调手性。
- Introduction：经典连续体局限 -> 微旋转必要 -> GMA 和本文目标。
- Related Work/Background：嵌入 Introduction。
- Method/Theory/Model：2.1 GMA，2.2 extended micropolar，2.3 micro-macro identification。
- Results：3.1 micro FE，3.2 参数研究，3.3 场变量对比。
- Discussion：与 Results 合并。
- Conclusion：回收 motif 设计、能量集中、模型必要性和高保真。
- 章节之间如何过渡：理论推导 -> 数值设置 -> 参数研究 -> 模型对比。
- 哪一节最值得模仿：3.3 Comparison of calculated kinematic fields。
- 哪一节可能存在结构风险：参数表和图像证据需 PDF 才能完全理解。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Macroscale-chirality-in-planar-elasticity--Predictions-o_2026_Journal-of-the.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：6
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Mathematical model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Granular micromechanics approach | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Results and discussion | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Parametric study using extended micropolar continuum model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4 Conclusion | 结论/展望型 | 收束贡献、边界和未来工作 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：Cauchy 局限 -> 高阶自由度 -> 颗粒微结构 -> 本文验证。
- Method 段落推进：从 grain-pair 到 continuum，再到具体 motif。
- Results 段落推进：先收敛，再参数研究，最后核心对比。
- Discussion/Conclusion 段落推进：强调微结构能量分布、可调性和 micropolar 高保真。
- 常见段落开头方式：`Classical elasticity...`; `The granular microstructure consists...`; `The results show...`。
- 常见段落收束方式：指出 chiral effect、negative Poisson effect 或 micropolar necessity。
- 可复用段落模板：`A classical model fails to represent [field], whereas the enriched model captures [micro-kinematic feature].`

## 13. 文笔画像与语言习惯
- 整体语气：理论验证型、较直接。
- claim 强度：对“需要 micropolar 模型”表达强。
- 谨慎表达：specific motif 和 simulation-based evidence 是隐含边界。
- 问题表达：cannot be modeled using classical Cauchy continuum。
- 贡献表达：investigates the efficacy of theoretical micro-macro linkages。
- 机制表达：coupling of stretching deformations and micro-rotation。
- 对比表达：micro finite element model vs micropolar model。
- 限定边界表达：2D microstructure, square pattern, selected loading tests。
- 术语密度：中高，围绕 chirality/micropolar/granular。
- 长句/短句习惯：摘要长句较多，结论句更清楚。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：model(127)；micropolar(74)；continuum(59)；granular(42)；displacement(42)；nite(41)；extension(41)；element(40)；grain(40)；grains(35)；shear(34)；given(34)；strain(32)；micro(31)；energy(30)；case(30)；loading(30)；parameters(29)；compression(28)；extended(27)
- 高频学术名词：model(127)；deformation(46)；displacement(42)；element(40)；strain(32)；energy(30)；parameters(29)；behavior(26)；micro-rotation(23)；results(22)；direction(21)；rotation(20)；ness(18)；response(17)；cation(16)；coupling(15)
- 高频学术动词：predicted(18)；shown(13)；show(7)；simulated(5)；shows(4)；predict(3)；evaluated(3)；derived(3)；indicates(3)；capture(2)；compare(2)；compared(2)；demonstrated(2)；validated(1)；formulated(1)；investigate(1)
- 高频形容词：displacement(42)；element(40)；relative(21)；chiral(18)；boundary(17)；numerical(14)；elastic(14)；material(14)；classical(12)；kinematic(12)；negative(12)；mechanical(11)；uniaxial(11)；normal(11)；anisotropic(10)；apparent(9)
- 高频副词/连接副词：respectively(14)；experimentally(10)；generally(4)；systematically(4)；clearly(4)；directly(4)；nearly(3)；appropriately(3)；finally(3)；strongly(2)；furthermore(2)；notably(2)；consequently(2)；however(2)；extremely(2)；particularly(2)
- 高频二词短语：micropolar model(38)；nite element(38)；continuum model(34)；micro nite(30)；element model(27)；strain energy(24)；extended micropolar(21)；micropolar continuum(19)；extension compression(18)；sti ness(16)；granular motif(15)；energy density(15)；simple shear(14)；identi cation(14)；shear loading(14)；based upon(11)
- 高频三词短语：micro nite element(30)；nite element model(27)；micropolar continuum model(16)；strain energy density(14)；extended micropolar model(9)；extended micropolar continuum(9)；simple shear loading(9)；extension compression simple(7)；compression simple shear(7)；obtained micro nite(7)；negative poisson ect(7)；micro-scale nite element(6)

**主动、被动与句法**

- 被动语态估计次数：159
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：613
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：203
- 一般过去时线索：68
- 现在完成时线索：16
- 情态动词线索：41
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：model(8)；granular(7)；continuum(6)；based(5)；chirality(4)；extended(4)；micropolar(4)；classical(4)
- 1. Introduction：model(20)；misra(16)；micropolar(13)；granular(12)；continuum(11)；extended(9)；gma(7)；chiral(6)
- 2. Mathematical model：无明显高频项
- 2.1. Granular micromechanics approach：strain(21)；energy(18)；relative(17)；grain(16)；continuum(15)；grains(14)；follows(14)；grain-pair(13)
- 3. Results and discussion：model(11)；mesh(11)；elements(10)；domain(8)；grains(7)；boundary(7)；user-controlled(7)；specimen(6)
- 3.2. Parametric study using extended micropolar continuum model：model(62)；micropolar(40)；extension(31)；loading(27)；case(26)；shear(25)；compression(22)；micro(21)
- 4. Conclusion：model(14)；size(12)；specimen(11)；micropolar(9)；grain(7)；apparent(7)；continuum(6)；behavior(6)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 骨架：`Classical [model] does not possess the capability to describe [emergent behavior].`
- 启发：模型必要性可从“缺少自由度”切入。

### 14.2 方法与框架表达
- 骨架：`We utilize [micro-mechanics approach] to link [micro-scale] and [macro-scale].`
- 启发：micro-macro 论文要明确连接桥。

### 14.3 结果与趋势表达
- 骨架：`The comparison strongly indicates the need for [higher-order model].`
- 启发：结果句服务于模型选择。

### 14.4 机制解释表达
- 骨架：`The emergent response is caused by coupling between [deformation mode] and [micro-kinematic variable].`
- 启发：宏观异常行为要回到微观运动。

### 14.5 贡献与意义表达
- 骨架：`The model represents the behavior of [microstructure] with high fidelity.`
- 启发：验证型论文可把 high fidelity 作为结论关键词。

### 14.6 局限与未来工作表达
- 骨架：`Further experimental validation is needed for manufactured specimens and broader motif classes.`
- 启发：缺实验时要主动承认。

## 15. 引用策略与文献使用
- 引用密度：Introduction 高，方法和结果中等。
- 引用主要集中位置：Cosserat/micropolar 理论、颗粒微力学、chiral metamaterials。
- 经典文献用途：Cosserat、Mindlin、Eringen、Germain。
- 近年文献用途：chiral lattice、granular continuum、metamaterials。
- 方法文献用途：GMA 和 micro-macro identification。
- 对比/批判性引用：Cauchy 局限作为主要批判对象。
- gap 如何靠引用搭建：经典模型缺少微旋转 -> 现代超材料出现手性 -> 需要验证高阶模型。
- references 暗示的研究共同体：广义连续体、颗粒力学、超材料。
- 引用风险：需覆盖更多 homogenization 和实验 chiral metamaterial 文献。

## 16. 审稿人视角风险
- 最大攻击面：结论对特定 duoskelion motif 是否普适。
- claim 是否过强：对该 motif 强，对广泛颗粒材料需限定。
- 证据是否不足：无物理实验。
- 方法是否可复现：几何和参数需 PDF 核查。
- 对比是否充分：Cauchy/micropolar 对比强，与其他高阶模型比较少。
- 边界条件是否清晰：加载边界清楚。
- 替代解释是否排除：有限尺寸和边界效应可能影响场。
- 图表是否需要进一步核查：需要。

## 17. 可复用资产
- 可复用选题角度：用微结构验证一个高阶连续体自由度的必要性。
- 可复用 gap 制造方式：`The behavior is predicted by enriched theory, but requires full-field micro-scale confirmation.`
- 可复用论证链：理论预测 -> motif 设计 -> micro FE -> 场变量对比 -> 尺寸收敛。
- 可复用图表设计：motif 图、边界图、收敛图、场变量对比图。
- 可复用段落结构：先证明数值可信，再证明模型必要。
- 可复用句型骨架：`The enriched model captures the micro-rotation field that is absent in the classical model.`
- 可复用引用组织：经典理论 + 作者前作 + 现代超材料。
- 不宜直接模仿之处：没有微结构验证时，不要强行声称高阶模型必要。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学：用一个设计良好的微结构作为理论检验平台。
- 可迁移到 Introduction：从 classical model limitation 切入。
- 可迁移到 Method：先 micro-macro bridge，再 numerical validation。
- 可迁移到 Results/Discussion：用场变量而非单一曲线证明模型必要。
- 需要避免的问题：不要只比较反力曲线，忽略位移/旋转场。

## 19. 最终浓缩
- 这篇论文最值得学：如何证明高阶连续体模型不是数学奢侈品，而是描述微结构手性的必要工具。
- 这篇论文最大风险：缺少物理实验和更多 motif 泛化。
- 三个可迁移动作：
  1. 先展示 classical model 缺少什么自由度。
  2. 用 micro FE 场变量验证 enriched model。
  3. 用参数研究证明微结构响应可设计。

最终判断：这篇论文适合学习 micro-macro 论文的写法：从微结构机制定义问题，用广义连续体预测，再用全场数值场证明经典模型不够。

补充写作素材：本文的强写法是“先证明经典模型缺什么，再展示高阶模型多了什么”。如果写类似广义连续体论文，不要一开始就说自己的模型更先进，而应先让读者看到 classical model 无法表达的场变量，如 micro-rotation、relative rotation、boundary layer 或 couple-stress。这样高阶自由度的必要性会自然出现。

图表设计也可迁移：motif 图负责说明微结构，边界条件图负责说明实验/仿真可重复，收敛图负责排除数值误差，场变量对比图负责证明理论必要性，appendix 尺寸效应图负责防守 RVE/尺度问题。这个图序非常适合超材料、晶格、颗粒或 architected materials 论文。

审稿防守要点：如果没有真实实验，应明确本文验证的是“theoretical micro-macro linkage”而不是制造可行性；如果只有一种 motif，应把结论限定为“given class of granular motif”，再把泛化留给未来工作。这样可以保持 claim 强度而不显得过度外推。
