# A mesomechanical model for predicting the degradation in stiffness of FRP composites subjected to combined thermal and mechanical loading

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material.txt`。该文页数较短，但 txt 抽取中公式、图表与正文有串栏，尤其是 Eq. (2)-(15)、Table 1/2 和 Fig. 4-10 的图像细节需要 PDF 图像复核。以下分析以全文抽取的摘要、Introduction、实验过程、模型章节、结果讨论和结论为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1. Introduction, 2. Experimental procedure, 3. Mesomechanical model for predicting the degraded stiffness properties, 4. Results and discussion, 5. Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A mesomechanical model for predicting the degradation in stiffness of FRP composites subjected to combined thermal and mechanical loading。
- 作者：Shengbo Shi, Liangxian Gu, Jun Liang, Guodong Fang, Chunlin Gong, Cunxi Dai。
- 期刊与年份：Materials and Design, 2016, 89, 1079-1085。
- 研究对象：高温和静态压缩载荷下 FRP 复合材料，实验材料为 silica fiber reinforced phenolic resin composite。
- 论文类型：热-力耦合材料退化模型论文，结合高温压缩实验验证。
- 核心方法：低于玻璃化转变温度用 tanh 函数描述热软化；高于玻璃化转变温度用介观多相模型描述树脂热分解、气相/炭相生成、硅纤维相变，并用 Eshelby-Mori-Tanaka 方法求有效刚度；引入孔隙气体压力对 bulk modulus 的影响。
- 主要证据：20-800 °C 多温度点压缩模量实验；相组分体积分数随温度变化；相组分弹性模量曲线；模型预测与实验温度-模量曲线对比；断口形貌；单侧加热压缩问题残余刚度随时间变化。

## 2. 摘要与核心信息提取

本文的一句话主张是：FRP 复合材料高温压缩刚度退化不能只用经验温度函数描述，应把热软化、树脂热分解、增强纤维相变和分解气体压力纳入介观模型，才能预测不同温度和热-力组合载荷下的刚度衰减。

摘要结构为：先指出机械性能随热暴露温度和时间降低；再提出 mesomechanical model；随后列出模型考虑的机制：matrix thermal softening、thermal decomposition、fiber phase transition、bulk modulus/internal pressure；再用高温压缩实验验证；最后给出刚度退化可粗分为三个阶段。

核心信息有两个：一是模型不是单一拟合曲线，而是把材料相组成变化与有效刚度联系起来；二是实验不是独立贡献，而是为模型提供温度-模量曲线验证和阶段划分依据。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-mesomechanical-model-for-predicting-the-degradation-in-stiff_2016_Material.md`。

中文译文：

> 文章历史记录： 2015年9月15日收到 2015年10月13日以修订形式收到 2015年10月14日接受 2015年10月19日在线提供
>
> 纤维增强聚合物 (FRP) 复合材料的机械性能随着热暴露温度和时间的增加而降低。提出了细观力学模型来预测高温下承受静态压缩载荷的 FRP 复合材料的退化行为。所开发的模型考虑了基体材料的热软化、热分解和增强纤维的相变​​，这些对复合材料的刚度性能产生不利影响。此外，为了评估高内压对刚度性能的影响，在数学模型的制定中应用了体积模量。进行高温压缩实验来测量与温度相关的弹性模量。通过比较模拟模量和实验模量进一步评估模型的准确性。通过分析预测的温度-模量曲线，FRP复合材料在高温下刚度性能的降低可大致分为三个阶段。 © 2015 Elsevier Ltd. 保留所有权利。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来源是热防护结构中的材料可靠性问题。FRP 复合材料因强度重量比、隔热性和成本优势用于飞行器热防护和固体火箭发动机喷管等高温环境，但在气动加热或火载荷下，树脂基体会热软化、裂解并产生孔隙/气体，导致刚度和强度退化。

作者把大问题收束为：在静态压缩载荷与高温暴露共同作用下，如何预测 FRP 复合材料的有效压缩刚度随温度退化。这个边界很明确：关注 stiffness properties，而不是全强度失效；关注高温压缩，而不是所有力学载荷；关注 silica/phenolic 复合材料，但模型形式试图对 FRP 有一般意义。

选题价值主要是工程可靠性：若能预测高温下刚度退化，就能支撑热防护结构设计、完整性评价和可靠性分析。方法价值在于把热化学相变与介观力学模型连接，而不是依赖少量实验温度点插值。

## 4. 领域位置与文献版图

Introduction 的文献版图围绕高温 FRP 退化展开。第一类是关于低温到玻璃化转变附近热软化和粘弹性蠕变的实验/模型研究；第二类是 Dimitrienko、Liang 等热-力多层结构模型，描述 composite stiffness/strength 随温度退化；第三类是 Bai and Keller 等基于 Arrhenius 或关键温度点的温度相关模量模型；第四类是 fire-under-compression 的压缩强度、失效时间和热分解模型。

作者的站位是继承前人热-力模型和 Mori-Tanaka/Eshelby 介观方法，但修正一个被忽略的机制：聚合物热分解产生孔隙、渗透性和内部高孔压，这会影响复合材料 bulk modulus；已有工作很少考虑温度升高导致的压缩刚度损失与气体压力效应。

文献组织不是按材料类型细分，而是按退化机制和模型能力推进：已有模型可描述热软化/热分解，但对 polymer decomposition 引起的 compressive stiffness loss 与 pore pressure 处理不足。

## 5. Gap 制造机制

本文 gap 的核心句意是：当 FRP 暴露于高温时，树脂热裂解导致孔隙和分解气体积累，固体骨架刚度急剧降低，内部孔压又会影响 bulk modulus；但已有研究对随温度升高、由聚合物分解导致的压缩刚度损失信息较少，也没有考虑气体压力对刚度的影响。

这个 gap 属于机制 gap 和模型 gap。机制 gap 是刚度退化不仅由热软化决定，还由热分解相变、残炭、气相和纤维相变共同控制。模型 gap 是缺少能把这些机制转成有效刚度预测的介观数学模型。

gap 说服力较强，因为它直接指向已有模型在物理机制上的遗漏。但它也有边界：本文实验主要是不同温度点的压缩模量，孔压效应并非通过原位压力测量直接验证，而是通过模型引入和估计。

## 6. 创新性判断

作者声明的贡献是建立介观数学模型预测高温刚度退化，并考虑热软化、粘弹性蠕变、基体热分解、纤维相变和内部气体压力，随后用高温压缩实验验证。

真实创新类型为理论/模型整合创新。tanh 热软化函数、Mori-Tanaka 方法、相变体积分数模型都不是完全新工具；新意在于把它们组织成面向高温压缩刚度退化的分阶段模型，并引入 pore pressure/bulk modulus 对有效刚度的影响。

创新强度：中等。文章篇幅短，模型推导和实验规模有限，但对于材料设计类期刊，能够把物理退化机制和实验验证闭合，贡献是成立的。最容易被挑战的是孔压效应的定量验证不足和材料体系外推性。

## 7. 论证链条复原

论证链条如下：

1. FRP 复合材料用于热防护结构，但高温下刚度/强度退化会威胁结构可靠性。
2. 低温段热软化和粘弹性会降低刚度；高于玻璃化转变温度后，树脂热分解和纤维相变导致进一步退化。
3. 已有模型对热分解导致的压缩刚度损失和分解气体孔压效应考虑不足。
4. 本文建立介观模型：低温段用 tanh 函数，高温段用多相介质与 Eshelby-Mori-Tanaka，加入内部压力对 bulk modulus 的影响。
5. 通过高温压缩实验获得 20-800 °C 的模量数据。
6. 模型预测曲线与实验数据合理一致，并可把刚度退化分成三个阶段。
7. 进一步用单侧加热压缩算例展示残余刚度随时间衰减。

逻辑闭合度中等偏高。实验验证支撑温度-模量趋势，但对每个微观机制的单独验证较弱，因此机制解释更像“物理合理的模型归因”，不是严格解耦实验证明。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：However, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6].
- 本文解决方式：A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures. The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material. Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formulation of the mathematical model.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

模型分为两个温度域。低于玻璃化转变温度时，使用 hyperbolic tanh function 描述 Young's modulus 从 room temperature 到 glass transition 附近的平滑下降，参数包括室温模量、玻璃化转变温度处模量、Tg 和控制过渡宽度的 η。

高于 Tg 时，树脂基体被视为 virgin phase、new solid/char phase 和 gas phase 构成的多相介质；硅纤维在更高温区发生 amorphous-to-crystalline phase transition。模型通过相体积分数随温度/时间变化描述材料组成演化，再借助 Eshelby-Mori-Tanaka 计算相组分有效弹性性质，最后求复合材料有效刚度。

关键输入包括：纤维/基体体积分数、各相弹性模量、Poisson 比、bulk modulus、Tg、分解/相变体积分数函数、内部孔压。边界条件/实验条件包括静态压缩载荷、温度均匀假设、特定升温/浸泡时间。复现难点在于部分相变体积分数和压力模型来自作者前期工作，txt 中公式和参数表抽取不完整，需要 PDF 复核。

## 9. 证据系统与 Claim-Evidence 表

证据系统以实验-模型对照为主，辅以相组分演化图、断口形貌和一维单侧加热算例。它不像机器学习论文那样有大规模数据，而是通过物理模型解释少量关键实验点。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| FRP 压缩模量随温度升高明显降低 | 摘要、4.1、Fig. 3、Table 1 | 20-800 °C 多温度点压缩实验，3 或 5 个试样平均 | 强 | 温度场均匀性和试样重复性需 PDF/实验细节复核 |
| 刚度退化可分为三个阶段 | 摘要、Fig. 7 附近 | 65-180 °C 快速热软化，180-500 °C 逐渐热分解，500 °C 后基体强分解与纤维相变导致进一步下降 | 中强 | 阶段边界对材料体系敏感 |
| 介观模型能较好预测温度相关模量 | 摘要、Fig. 7、结论 | 模型预测曲线与实验模量点合理一致 | 中强 | 缺少误差指标和统计置信区间 |
| 树脂热分解导致相组成变化并降低基体刚度 | 3.2、4.1、Fig. 4/6 | phenolic resin 体积分数从 polymer 转 char/gas，基体模量在 400-650 °C 快速下降 | 中 | 相体积分数模型来自前期工作，需参数复核 |
| 硅纤维在高温相变导致增强相刚度降低 | 3.2、4.1、Fig. 5/6 | silica fiber 在约 500-600 °C 发生相变，模量下降 | 中 | 纤维相变证据主要为模型/文献支撑 |
| 单侧加热下残余刚度随加热时间降低 | 4.3、Fig. 9/10 | 热-力算例通过厚度积分计算 residual stiffness | 中 | 属于模型应用展示，缺少对应实验验证 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 实验装置图 | 高温压缩实验可靠性 | 三段环形炉、温控系统与试样温度测量 | 需要 PDF 图像复核 |
| Eq. (1) | 低温热软化函数 | Tg 附近模量快速下降 | 用 tanh 表达平滑退化 | 公式需 PDF 复核 |
| Fig. 2 | 介观物理模型 | 基体/纤维相变可建模 | matrix 与 silica fiber 的多相结构示意 | 需要 PDF 图像复核 |
| Eq. (2)-(15) | 多相介观有效刚度推导 | 热分解/孔压进入刚度预测 | Eshelby-Mori-Tanaka 与静力平衡关系 | 公式串栏严重，需 PDF 复核 |
| Table 1/Fig. 3 | 实验模量数据 | 模量随温度降低 | 温度-压缩模量曲线是核心验证 | 需要 PDF 复核 |
| Fig. 4/Fig. 5 | 树脂/纤维相体积分数 | 热分解和相变机制 | polymer 转 char/gas，fiber amorphous 转 crystalline | 需要 PDF 图像复核 |
| Fig. 6 | 相组分弹性模量 | 各相刚度随温度变化 | phenolic resin 和 silica fiber 高温模量下降 | 需要 PDF 图像复核 |
| Fig. 7 | 模型-实验对比 | 模型预测有效 | 预测曲线与实验点合理一致，并显示三阶段 | 需要 PDF 图像复核 |
| Fig. 8 | 断口形貌 | 高温后材料形貌变化 | 不同温度下失效模式相似，颜色和纤维暴露变化 | 需要 PDF 图像复核 |
| Fig. 9/Fig. 10 | 单侧加热压缩算例 | 模型可用于热-力问题 | residual stiffness 随 heating time 下降 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

文章结构是典型短篇材料模型论文：1 Introduction；2 Experimental procedure；3 Mesomechanical model for predicting degraded stiffness properties；4 Results and discussion；5 Conclusions。Results 内含 stiffness degradation、fracture morphology、compression modeling under one-sided heating。

它的章节顺序不是先模型后实验，而是先说明实验过程，再给模型。这种安排服务于 Materials and Design 读者：先建立数据来源和材料对象，再进入公式推导。模型章节按温度区间分段，低于 Tg 与高于 Tg 的处理不同，使“退化三阶段”在结构上提前埋下伏笔。

标题偏描述型，功能清晰但信息量一般。可模仿的是 “Mesomechanical model for predicting...” 这种标题直接暴露方法与目标；不太可模仿的是 Results 小节标题较宽泛，若改成 “Three-stage stiffness degradation and model validation” 会更有论证力度。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1. Introduction（背景定位/文献缺口）
- L2 p.2: 2. Experimental procedure（结果/验证/讨论）
- L2 p.3: 3. Mesomechanical model for predicting the degraded stiffness properties（方法/模型/算法）
  - L3 p.3: 3.1. Degraded stiffness properties at temperatures lower than glass transition temperature（对象/模块/过渡章节）
  - L3 p.3: 3.2. Degraded stiffness properties at temperatures higher than glass transition temperature（对象/模块/过渡章节）
    - L4 p.3: 3.2.1. Stiffness properties of matrix materials and reinforced fibers（对象/模块/过渡章节）
    - L4 p.4: 3.2.2. Stiffness properties of FRP composites（对象/模块/过渡章节）
- L2 p.4: 4. Results and discussion（结果/验证/讨论）
  - L3 p.4: 4.1. Stiffness degradation of matrix, fiber and silica/phenolic composites（对象/模块/过渡章节）
  - L3 p.6: 4.2. Fracture morphology analysis（对象/模块/过渡章节）
  - L3 p.6: 4.3. Compression modeling of silica/phenolic composite exposed to one-sided heating（方法/模型/算法）
- L2 p.7: 5. Conclusions（结论/贡献回收）
- L2 p.7: Acknowledgements（尾部材料）
- L2 p.7: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1. Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2. Experimental procedure | 2 | 2 | 结果/验证/讨论 |
| 3. Mesomechanical model for predicting the degraded stiffness properties | 3 | 2 | 方法/模型/算法 |
| 3.1. Degraded stiffness properties at temperatures lower than glass transition temperature | 3 | 3 | 对象/模块/过渡章节 |
| 3.2. Degraded stiffness properties at temperatures higher than glass transition temperature | 3 | 3 | 对象/模块/过渡章节 |
| 3.2.1. Stiffness properties of matrix materials and reinforced fibers | 3 | 4 | 对象/模块/过渡章节 |
| 3.2.2. Stiffness properties of FRP composites | 4 | 4 | 对象/模块/过渡章节 |
| 4. Results and discussion | 4 | 2 | 结果/验证/讨论 |
| 4.1. Stiffness degradation of matrix, fiber and silica/phenolic composites | 4 | 3 | 对象/模块/过渡章节 |
| 4.2. Fracture morphology analysis | 6 | 3 | 对象/模块/过渡章节 |
| 4.3. Compression modeling of silica/phenolic composite exposed to one-sided heating | 6 | 3 | 方法/模型/算法 |
| 5. Conclusions | 7 | 2 | 结论/贡献回收 |
| Acknowledgements | 7 | 2 | 尾部材料 |
| References | 7 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一段先交代 FRP 的工程应用和高温风险，第二段归纳已有研究对热软化、Tg、热分解等现象的认识，第三段集中指出孔隙/气体压力和压缩刚度损失的不足，最后一句引出本文模型和实验验证。

实验段落节奏非常工程化：装置 → 材料组成 → 制备过程 → 试样尺寸 → 加载方向 → 温度点 → 浸泡时间 → 数据处理。这种顺序适合材料实验论文，最大优点是复现路径清楚。

模型段落按物理机制推进：先低温热软化，再高温多相相变，再求复合材料等效性质。结果段落则按“实测总体趋势 → 组分机制解释 → 模型对比 → 形貌观察 → 应用算例”推进，形成从宏观曲线到介观机制再到工程应用的节奏。

## 13. 文笔画像与语言习惯

整体语气是传统材料力学论文风格，强度适中，常用 “can be”“is assumed”“it is observed”“reasonably good”“satisfactorily predict”。相比 2025 年机器学习论文，本文更少使用 aggressive claim，更多用机制解释和实验对比来建立可信度。

主动语态较少，作者动作多用被动：“experiments were conducted”“model was presented”“accuracy was assessed”。这是材料实验/模型论文常见写法，把主语让给 specimen、modulus、phase、temperature。

时态方面，Introduction 用现在时描述 FRP 应用和高温退化的一般事实，用过去时回顾前人；Experiment/Results 多用过去时；Conclusion 用一般现在时和过去时混合总结模型能力。

高频概念包括 stiffness、modulus、temperature、matrix、fiber、thermal decomposition、phase transition、compression、FRP composites。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：23685
- 高频词：phase(55)；temperature(51)；properties(37)；material(36)；modulus(34)；composites(28)；thermal(25)；frp(24)；temperatures(23)；transition(21)；model(21)；silica(20)；stiffness(19)；phenolic(19)；polymer(18)；gas(18)；volume(18)；matrix(17)；high(16)；resin(16)
- 高频名词化/学术名词：temperature(51)；transition(21)；stiffness(19)；decomposition(14)；compression(14)；pressure(14)；inclusion(10)；degradation(8)；reaction(7)；ablation(6)；direction(6)；elasticity(5)；experiment(4)；fraction(4)；density(4)
- 高频学术动词：predict(5)；presented(3)；predicted(2)；developed(2)；compared(2)；provided(2)；achieved(1)；evaluated(1)；validate(1)；estimated(1)
- 高频形容词：material(36)；thermal(25)；phenolic(19)；elastic(14)；effective(12)；compressive(10)；internal(9)；mechanical(8)；temperature-dependent(8)；constant(7)；component(6)；residual(6)；experimental(5)；equivalent(5)；thermo-mechanical(4)
- 高频副词：drastically(4)；sufficiently(3)；additionally(3)；significantly(2)；relatively(2)；early(2)；similarly(2)；accordingly(2)；practically(2)；reasonably(1)；basically(1)；experimentally(1)；actually(1)；separately(1)；kindly(1)
- 高频二词短语：frp composites(20)；stiffness properties(13)；phenolic resin(12)；glass transition(11)；gas phase(11)；high temperatures(10)；properties frp(10)；transition temperature(10)；elastic modulus(10)；bulk modulus(9)；silica fiber(9)；solid phase(9)
- 高频三词短语：glass transition temperature(10)；properties frp composites(9)；silica phenolic composites(5)；degraded stiffness properties(4)；stiffness properties frp(4)；thermal response model(4)；char phase gas(4)；phase component materials(4)；mechanical properties frp(3)；ablation phase transition(3)；matrix materials reinforced(3)；materials reinforced fibers(3)
- 被动语态估计：94；`we + 动作动词` 主动句估计：0
- 一般现在时线索：65；一般过去时线索：234；现在完成时线索：0；情态动词线索：36

分章节正文词频：

- 1. Introduction: temperature(11)；properties(10)；frp(9)；composites(9)；model(9)；high(8)；thermal(6)；stiffness(6)
- 2. Experimental procedure: temperature(19)；specimen(12)；furnace(7)；material(7)；temperatures(6)；specimens(6)；three(5)；compression(5)
- 3. Mesomechanical model for predicting the degraded stiffness properties: phase(33)；material(16)；properties(14)；kvirg(14)；gas(13)；transition(10)；temperature(10)；materials(10)
- 4. Results and discussion: phase(20)；modulus(16)；silica(14)；phenolic(14)；temperature(10)；resin(10)；fiber(9)；composites(8)
- 5. Conclusions: properties(5)；temperatures(4)；thermal(4)；frp(4)；composites(4)；model(3)；stiffness(3)；matrix(3)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用背景句结构：`FRP composites are favored in X due to Y. However, there is a serious concern for degradation under high temperatures.` 适合“材料优势 + 极端环境风险”的开头。

可复用 gap 句结构：`However, less information exists on A. Also, the effect of B has not been considered.` 这是经典短篇论文 gap 句，直接、清楚、不铺张。

可复用方法句结构：`A mesomechanical model was developed to predict A, in which B, C and D were considered.` 可以迁移到模型整合类论文。

可复用结果句结构：`It can be seen that X decreases with increasing Y, which is caused by Z.` 适合实验曲线解释。

可复用阶段划分句：`The reduction in stiffness properties can be roughly divided into three stages.` 这种句式能把连续曲线转成可讨论的机制阶段。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
#### Gap/转折句
- 原句：However, less information exists on the loss in compressive stiffness properties with increasing temperature due to the polymer decomposition.
  可迁移模板：However, less information exists on the loss in compressive stiffness properties with increasing temperature due to the polymer decomposition.
#### 方法提出句
- 原句：A mesomechanical model was presented to predict the degraded behavior of FRP composites supporting a static compressive loading under high temperatures.
  可迁移模板：A mesomechanical model was presented to predict the degraded behavior of METHOD composites supporting a static compressive loading under high temperatures.
- 原句：The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material.
  可迁移模板：The thermal softening, thermal decomposition of the matrix material and phase transition of the reinforced fibers were considered in the developed model, which adversely affect the stiffness properties of the composite material.
- 原句：Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formulation of the mathematical model.
  可迁移模板：Also, in order to evaluate the effect of high internal pressure on stiffness property, the bulk modulus was applied in the formulation of the mathematical model.
- 原句：The accuracy of the model was further assessed by comparing simulated and experimental modulus.
  可迁移模板：The accuracy of the model was further assessed by comparing simulated and experimental modulus.
- 原句：Dimitrienko [13–15] defined two degradation functions to describe the temperature dependence of elastic characteristics, stiffness and strength properties, and established a structural thermo-mechanical model of composite materials at high temperatures.
  可迁移模板：Dimitrienko [X–X] defined two degradation functions to describe the temperature dependence of elastic characteristics, stiffness and strength properties, and established a structural thermo-mechanical model of composite materials at high temperatures.
#### 结果呈现句
- 原句：Thus, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points.
  可迁移模板：Thus, temperature-dependent E-modulus was described as stepped functions achieved by connecting experimentally key points.
- 原句：High temperature compression experiment was carried out to validate the proposed model through comparing numerical results with corresponding experimental results.
  可迁移模板：High temperature compression experiment was carried out to validate the proposed model through comparing numerical results with corresponding experimental results.
- 原句：Comparing the numerical and experimental results of elastic modulus, the proposed model can satisfactorily predict the temperature-dependent effective properties of FRP composites.
  可迁移模板：Comparing the numerical and experimental results of elastic modulus, the proposed METHOD composites.
#### 贡献/增量句
- 原句：Dimitrienko [13–15] defined two degradation functions to describe the temperature dependence of elastic characteristics, stiffness and strength properties, and established a structural thermo-mechanical model of composite materials at high temperatures.
  可迁移模板：Dimitrienko [X–X] defined two degradation functions to describe the temperature dependence of elastic characteristics, stiffness and strength properties, and established a structural thermo-mechanical model of composite materials at high temperatures.
- 原句：The mathematical formulas for the mesomechanical model were established to predict the degraded stiffness properties at high temperatures.
  可迁移模板：The mathematical formulas for the mesomechanical model were established to predict the degraded stiffness properties at high temperatures.
#### 限制/边界句
- 原句：The conclusions could be summarized from the reported literatures as follows: in the lower temperature range, thermal softening and viscoelastic creep can cause the reduction in the mechanical properties of FRP composite, while, when the temperature reaches and exceeds the glass transition temperature, the elastic modulus and strength drops significantly increase [9–12].
  可迁移模板：The conclusions could be summarized from the reported literatures as follows: in the lower temperature range, thermal softening and viscoelastic creep can cause the reduction in the mechanical properties of METHOD composite, while, when the temperature reaches and exceeds the glass transition temperature, the elastic modulus and strength drops significantly increase [X–X].
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用主要服务三类功能：支持 FRP 在热防护结构中的应用；说明高温退化已有认识，包括热软化、Tg、热分解、DMA 关键点模型；支撑具体模型选择，如 Dimitrienko 多级结构模型、Bai/Keller 温度相关模量模型、Gibson/Feih/Mouritz/Kim 的 fire-under-compression 研究。

作者引用姿态以继承和补充为主。对前人不是强批判，而是指出“已有模型考虑了许多热-力退化，但孔压和由聚合物分解引起的压缩刚度损失还不够”。这让文章看起来像在一个成熟模型谱系中补齐机制，而不是推翻前人。

引用风险是：由于文章 2016 年发表，近年多尺度热化学/损伤模型当然不在其中；若作为当下写作模板，需要更新近五年复合材料高温退化、热解-孔压耦合和多尺度模拟文献。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：71
- Introduction 引文簇数量估计：8
- References 条目数：37
- 可识别年份条目数：37
- 2021 年及以后文献数：0
- 2010 年前经典文献数：19
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Composite Structures(1)
- 引文簇样例：[16,17], [5,6], [18,19], [19], [7,8], [20], [21], [22], [29], [30], [31], [32]

带引文的 gap/转折句样例：

- However, there is a serious concern for the degradation-tofailure of FRP composite structures at high temperatures associated with aerodynamic heating when spacecraft flies at supersonic [5,6].

References 解析样例（前 8 条）：

- [1] L. Bian, J. Xiao, J. Zeng, et al., Microstructural interpretation of the ablative properties of phenolic-quartz hybrid fabric reinforced phenolic resin composites, Mater. Des. 62 (2014) 424–429.
- [2] N. Guermazi, N. Haddar, K. Elleuch, H.F. Ayedi, Investigations on the fabrication and the characterization of glass/epoxy, carbon/epoxy and hybrid composites used in the reinforcement and the repair of aeronautic structures, Mater. Des. 56 (2014) 714–724.
- [3] P.R.S. Reddy, T.S. Reddy, V. Madhu, et al., Behavior of E-glass composite laminates under ballistic impact, Mater. Des. 84 (2015) 79–86.
- [4] P. Luangtriratana, B.K. Kandola, P. Myler, Ceramic particulate thermal barrier surface coatings for glass fibre-reinforced epoxy composites, Mater. Des. 68 (2015) 232–244.
1085 S. Shi et al. / Materials and Design 89 (2016) 1079–1085
- [5] E. Kandare, B.K. Kandola, P. Myler, G. Edwards, Thermo-mechanical responses of fiber-reinforced epoxy composites exposed to high temperature environments. Part I: experimental data acquisition, J. Compos. Mater. 44 (2010) 3093–3114.
- [6] A.M. Coppola, A.S. Griffin, N.R. Sottos, S.R. White, Retention of mechanical performance of polymer matrix composites above the glass transition temperature by vascular cooling, Compos. Part A 78 (2015) 412–423.
- [7] K. Wei, R. He, X. Cheng, et al., A lightweight, high compression strength ultra high temperature ceramic corrugated panel with potential for thermal protection system applications, Mater. Des. 66 (2015) 552–556.
- [8] B. Yu, V. Kodur, Effect of temperature on strength and stiffness properties of nearsurface mounted FRP reinforcement, Compos. Part B 58 (2014) 510–517.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 孔压效应是本文 gap 的关键，但实验中没有直接测量内部 pore pressure，定量支撑偏弱。
2. 温度均匀性假设依赖试样小尺寸和浸泡时间，真实热防护结构中温度梯度更强。
3. 模型参数较多，部分来自文献或前期工作，可能存在参数可辨识性问题。
4. 实验只覆盖 silica/phenolic 一种体系，推广到碳纤维/环氧、陶瓷基或其他 FRP 需要谨慎。
5. 预测与实验“reasonable agreement”缺少系统误差指标、置信区间和残差分析。
6. 强度失效和损伤演化不是本文重点，但工程应用中刚度退化与破坏往往耦合。

## 17. 可复用资产

可复用选题套路：从极端环境应用中的材料优势切入，再指出该优势会被特定退化机制削弱，最后提出能够显式包含机制的模型。

可复用论证链：工程应用 → 高温退化现象 → 已有经验/半经验模型 → 被忽略机制 → 介观模型 → 实验温度点验证 → 阶段划分与应用算例。

可复用图表：实验装置图；介观相组成示意图；相体积分数随温度变化图；组分模量随温度变化图；预测-实验曲线对比；断口形貌；残余刚度随时间变化图。

可复用表达：`thermal softening`, `thermal decomposition`, `phase transition`, `effective properties`, `reasonably good agreement`, `roughly divided into three stages`。

## 18. 对我写论文的启发

这篇论文最值得学的是如何把一个复杂高温退化问题拆成温度区间和机制模块。它没有直接写“建立一个复杂模型”，而是先告诉读者低温段和高温段物理机制不同，因此需要不同建模策略。

自己的论文若涉及多机制耦合，可以学习这种“分阶段建模 + 合并预测”的写法。特别是把结果曲线解释成阶段，可以显著增强 Discussion 的可读性。

需要避免的是只用“吻合较好”替代量化误差。现代论文最好补充 RMSE、相对误差、参数敏感性、不确定性范围和独立验证工况。

## 19. 最终浓缩

本文最值得学的是：把 FRP 高温刚度退化从经验曲线拆成热软化、热分解、纤维相变和孔压影响，并用介观模型连接到有效压缩模量。

最大风险是：关键机制尤其孔压缺少直接实验验证，且单一材料体系限制外推。

可迁移的三件事：一是按温度/机制分段建立模型；二是用实验曲线支撑阶段划分；三是用介观示意图和相体积分数图把复杂材料退化讲清楚。
