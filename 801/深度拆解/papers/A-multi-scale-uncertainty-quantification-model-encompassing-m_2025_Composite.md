# A multi-scale uncertainty quantification model encompassing minimum-size unit cells for effective properties of plain woven composites

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.txt`。该文图表和公式较多，txt 抽取存在明显串栏；尤其是边界条件公式、Table 1-14、Fig. 2-24 的几何/相关性/直方图细节需要 PDF 图像复核。本文依据可识别的摘要、Introduction、模型流程、单胞参数化、UQ 结果和 Conclusions 进行拆解。

## 1. 基本信息与论文身份

- 题名：A multi-scale uncertainty quantification model encompassing minimum-size unit cells for effective properties of plain woven composites。
- 作者：Yu-Cheng Yang, Jian-Jun Gou, Chun-Lin Gong, Yue-Er Sun, Shuguang Li。
- 期刊与年份：Composite Structures, 2025, 352, 118648。
- 研究对象：plain woven composites 的有效力学/热膨胀性质不确定性，包括 fiber、fiber bundle、composite 多尺度参数。
- 论文类型：多尺度有限元单胞建模 + 不确定性量化方法论文。
- 核心方法：用结构对称性穷尽分析构造 minimum-size unit cells；对几何参数用 uniform distributions，对 constituent properties 用 normal distributions；用 Nataf transformation 在尺度间传播相关不确定性；通过 Monte Carlo/统计收敛分析获得有效性质分布。
- 主要证据：fiber bundle 的 1/8 单胞、plain woven composite 的 1/16 单胞；不同尺寸单胞结果对比；均值/方差收敛曲线；输出分布直方图；输入-输出相关矩阵；总体计算成本降低 89%。

## 2. 摘要与核心信息提取

本文的一句话主张是：平纹织物复合材料有效性质的不确定性预测同时受多尺度输入不清、尺度间相关传播复杂和大规模仿真成本高三重限制；通过最小尺寸单胞和 Nataf 相关传播，可以在不牺牲单次仿真精度的前提下把整体 UQ 成本降低约 89%。

摘要首先给出三个痛点：unclear input uncertainties、complex uncertainty propagations、unaffordable computational cost。接着提出模型的两个支柱：accuracy holding 和 cost control。前者靠 traceability description、inter-scale propagation、quantification；后者靠 structural symmetries 推导 1/8 和 1/16 单胞。最后用 statistical uncertainties convergence 和 reduced computational cost 收束贡献。

核心信息不是“用了 Monte Carlo”，而是“从单次仿真成本入手降低 UQ 成本”。这和常见用 surrogate model 减少样本数的路线不同，作者明确说 surrogate 会带来精度折衷，而本文尝试缩小 unit cell 来降低每个样本的求解成本。

## 3. 选题层深拆

选题来源是复合材料制造不确定性。平纹织物复合材料的有效性质由织物几何、纤维/基体性质和多尺度结构共同决定；模具、尺寸加工和高温制造会引入几何和材料参数不确定性。若不量化这些不确定性，高精度性能预测就不可靠。

作者把问题收束为：如何在 fiber、fiber bundle、composite 多尺度上描述输入不确定性，保留尺度间输出参数相关性，并以可承受成本得到有效 elastic modulus、Poisson's ratio、shear modulus 和 thermal expansion coefficient 的统计分布。

选题价值包括：提高复合材料有效性质预测可信度；为多尺度可靠性/设计优化提供输入分布；用最小单胞降低仿真成本，避免仅靠 surrogate 减样本带来的精度损失。

## 4. 领域位置与文献版图

Introduction 将已有研究组织成三条线。第一条是不确定性分析方法：Monte Carlo 理论可靠但计算成本高；RBF、Gaussian processes、PCE 等 surrogate 可减少样本数但可能牺牲精度。第二条是复合材料有效性质计算：解析方法如 Mori-Tanaka 公式显式但局部细节不足，FEM 单胞精度高但成本大。第三条是尺度间相关传播：只描述 marginal distribution 不够，Rosenblatt、Nataf、copulas 可处理相关变量。

作者站位是：不与 surrogate 竞争样本数，而是在单胞尺寸和边界条件上做成本优化；不只输出边缘分布，还通过 Nataf 保留 bundle-to-composite 的相关结构。

文献版图还有一个隐含背景：Gou/Jian-Jun 团队此前在 unit cell method、thermal conductivity、thermal expansion 等方面已有一系列工作，本文延续“利用平移/反射/旋转对称减少单胞尺寸”的路线，并把它扩展到多尺度 UQ。

## 5. Gap 制造机制

本文 gap 由三个并列问题组成：多尺度输入不确定性来源不清；尺度间输出相关性传播复杂；大量有限元仿真成本不可承受。作者进一步指出，减少 Monte Carlo 样本数通常要借助 surrogate，但 surrogate 伴随精度折衷；因此有必要从单次仿真成本入手。

gap 类型包括数据/输入 gap、方法 gap 和计算成本 gap。最有说服力的是计算成本 gap，因为单胞尺寸与 FE 求解成本之间关系直观；通过更多结构对称性缩小单胞但保持边界条件严格推导，能直接回应“准确又便宜”的目标。

可被质疑的是：最小尺寸单胞的边界条件复杂度提高，实际建模和网格对称要求更高；如果自动化程度不足，工程部署成本可能转移到前处理上。

## 6. 创新性判断

作者声明的创新包括：建立 traceability-description/inter-scale-propagation/quantification 的多尺度 UQ 流程；用 uniform/normal distribution 描述不同尺度参数；用 Nataf transformation 传递参数相关性；通过结构对称性构造 fiber bundle 1/8 单胞和 plain woven composite 1/16 单胞，并实现 89% 总成本下降。

真实创新属于方法框架和工程效率创新。单胞对称性、Nataf 和 Monte Carlo 都已有，但组合到 plain woven composites 的多尺度 UQ 中，并把“最小单胞”作为降低 UQ 成本的主策略，是本文的新意。

创新强度：中等偏强。强在模型链条完整、成本收益明确、结论量化；弱在概率分布假设较常规，且不确定性输入来源主要来自假设/标准而非实测反演。

## 7. 论证链条复原

全文论证链条为：

1. 平纹织物复合材料性能受多尺度几何和组分参数影响，制造过程引入不确定性。
2. Monte Carlo 能可靠量化不确定性，但多尺度 FE 单胞仿真成本过高。
3. 与其减少样本数，不如减少每个样本的单胞尺寸，避免 surrogate 精度折衷。
4. 通过平移、反射、旋转/反旋转对称关系推导统一边界条件，构造最小尺寸单胞。
5. 在 fiber bundle 微尺度和 plain woven composite 介尺度分别参数化几何和材料参数。
6. 对微尺度输出有效性质，用 Nataf 保留相关性并传播到介尺度。
7. 用统计收敛、分布直方图和相关矩阵分析输出不确定性与主导参数。
8. 得到 1/8、1/16 单胞和 89% 总体成本下降，同时保持有效性质结果一致。

逻辑较完整，最薄弱环节是输入不确定性分布的真实性：几何参数统一用 ±25% uniform、组分性质用 normal，这些假设若缺少实测制造数据，会影响输出分布可信度。

## 8. 方法/理论/模型细拆

方法分为三大模块。第一是 minimum-size unit cell formulation：总结 translational symmetry、reflectional symmetry/antisymmetry、rotational symmetry/antisymmetry 等位移约束规则，将它们统一到边界条件表达中。fiber bundle 从 UC1 到 UC4 逐步利用对称性缩小到 1/8；plain woven composite 从全尺寸单胞缩小到 1/16。

第二是参数化与有效性质计算：对各单胞定义几何参数，如 fiber bundle 的宽、长、纤维半径，plain woven composite 的长度、半宽、半间隙、厚度和层间间隙；通过加载边界条件求 elastic modulus、Poisson's ratio、shear modulus、thermal expansion coefficient。

第三是不确定性传播：fiber/matrix 组分性质和几何参数采样后，先在 microscale 得到 fiber bundle effective properties；再用 Nataf transformation 将这些相关输出转成可用于 mesoscale 的联合分布样本；最后在 plain woven composite 单胞上得到输出统计量和输入-输出相关。

关键假设：几何参数服从均匀分布，材料组分性质服从正态分布；输出相关可由 Nataf 近似处理；样本量足以使均值/方差收敛；最小单胞边界条件严格等价于全尺寸单胞。

## 9. 证据系统与 Claim-Evidence 表

证据系统由“单胞等价验证 + 成本比较 + 统计收敛 + 分布形态 + 相关性解释”组成。它的强项是把效率和物理/统计解释放在同一条证据链上。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| fiber bundle 可用 1/8 最小单胞替代全尺寸单胞 | Conclusions、Fig. 6-8、Tables 1-3、Fig. 17 | UC4 基于三平移、两反射和一个 180° 旋转对称；与更大单胞最大偏差约 3.5%，成本降低 82% | 强 | 边界条件和偏差细节需 PDF 复核 |
| plain woven composite 可用 1/16 最小单胞 | Conclusions、Fig. 10-11、Fig. 18 | 基于三平移、两反射和两个 180° 旋转对称，成本降低 94% | 强 | 几何/网格对称要求需 PDF 复核 |
| 整体 UQ 效率提升 89% | 摘要、5.2.2、Conclusions | 结合两尺度样本数和最小单胞平均计算时间得到总成本下降 | 强 | 计算环境和时间统计口径需复核 |
| Nataf 能用于尺度间相关传播 | 2、4.2、Fig. 14 | 将 fiber bundle 输出有效性质的相关联合分布传播到 composite 尺度 | 中强 | Nataf 对非高斯/尾相关的适用性有限 |
| fiber bundle 输出中面外性质更受 fiber 输入影响，面内性质更受 matrix 影响 | 5.2.1、Fig. 21 | 输入-输出相关矩阵显示 Exb/Ezb、vxyb/vxzb、G、alpha 的主导来源不同 | 中 | 相关系数不等于因果；图像需 PDF 复核 |
| plain woven composite 的参数耦合更强 | 5.2.2、Fig. 24、Table 14 | 多尺度传播后 CV 增大，volume fraction vfp 相关性高 | 中强 | 分布假设和样本收敛影响结论 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 多尺度 UQ 总流程 | 方法框架完整 | microscale UQ → Nataf propagation → mesoscale UQ | 需要 PDF 图像复核 |
| Eq. (1)-(6) | 有效性质定义 | 输出物理量明确 | E、ν、G、α 由应力/应变/温差求得 | 公式需 PDF 复核 |
| Fig. 2-5 | 对称性与边界条件规则 | 最小单胞有数学基础 | 平移/反射/旋转关系转成位移约束 | 需要 PDF 图像复核 |
| Fig. 6-8 | fiber bundle 单胞与参数 | 1/8 单胞构造 | UC1-UC4 逐步缩小，参数化半径/尺寸 | 需要 PDF 图像复核 |
| Tables 1-3 | fiber bundle 边界条件 | 小单胞等价计算 | 不同加载下边界条件汇总 | 表格需 PDF 复核 |
| Fig. 10-11 | plain woven composite 几何和边界 | 1/16 单胞构造 | 参数化织物单胞尺寸和边界面 | 需要 PDF 图像复核 |
| Fig. 14 | 尺度间传播流程 | Nataf 传播相关性 | 微尺度输出转联合分布输入介尺度 | 需要 PDF 图像复核 |
| Fig. 17-18 | 不同单胞相对差异 | 精度不妥协 | 小单胞与 UC1 相比差异有限 | 需要 PDF 图像复核 |
| Fig. 19/22 | 均值方差随样本量收敛 | 样本量足够 | fiber bundle 和 composite 输出统计量收敛 | 需要 PDF 图像复核 |
| Fig. 20/23、Table 13/14 | 输出分布与统计指标 | UQ 结果可解释 | CV、skew、kurtosis 描述输出不确定性 | 表格需 PDF 复核 |
| Fig. 21/24 | 输入-输出相关 | 主导参数分析 | 区分 fiber-dominated、matrix-dominated、co-dominated | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

文章结构大致为：1 Introduction；2 Multi-scale uncertainty quantification model；3 Minimum-size unit cells and model parameterizations；4/5 不确定性参数描述、尺度间传播与多尺度不确定性分析；6 Conclusions。由于 txt 串栏，部分章节编号显示不完整，但主体逻辑清晰。

Introduction 是“问题三连击”：输入不确定性、相关传播、计算成本。Section 2 给总体流程，先把模型路线图交代清楚。Section 3 是全文最长、最技术的部分，逐步推导对称性和单胞边界条件。后续结果部分先验证单胞尺寸，再做 UQ 输出分析，最后在 Conclusions 中按 fiber bundle、plain woven composite、total efficiency、uncertainty findings 分点总结。

标题命名偏方法型和对象型，例如 “Minimum-size unit cells and model parameterizations”“Inter-scale propagation model”。优点是层级清楚；不足是结果章节标题在 txt 中不够清晰，若写作时可用 “Validation of minimum unit cells” 和 “Dominant uncertainty sources across scales” 强化论证功能。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：4
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3.2 Unit cells and geometric parameters | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.2.1 Translational symmetric structure | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Unit cells and their parameterization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3.1 Microscale fiber bundle | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 前两段从材料应用和制造不确定性切入，随后引入 Monte Carlo 成本问题，再转到 unit cell 尺寸对单次仿真成本的影响。这个转折很关键：它把文章从普通 UQ 论文变成“UQ 成本控制”论文。

方法段落节奏是“定义规则 → 图示对称性 → 给约束方程 → 应用到具体单胞”。虽然公式密集，但每组公式都服务于一个几何对称操作。参数化段落则从 microscale 到 mesoscale，保持尺度递进。

结果段落先讲收敛，再讲分布，再讲相关性，最后给物理解释：哪些输出由 fiber 主导，哪些由 matrix 主导，哪些共同主导。这种顺序非常适合 UQ 论文，因为它先确认统计结果可靠，再解释不确定性来源。

## 13. 文笔画像与语言习惯

整体语气是方法工程型，常用 uncertainty quantification、effective properties、unit cell、symmetry、correlation、distribution、computational cost。claim 强度偏强，尤其是 “without accuracy compromising”“reduced computational cost of 89%”，但在 Nataf 选择处有边界说明：输出参数没有显著非线性相关，因此采用 Nataf。

主动语态较少，多用被动和客观结构：“is developed”“is established”“is adopted”“can be calculated”。这让文本呈现公式/流程驱动的风格。

时态上，一般现在时用于模型定义和物理/数学事实；过去时较少，主要用于结果描述；将来/情态表达用于方法用途。名词化高，如 traceability description、inter-scale propagation、parameterization、transformation、quantification。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：fiber(141)；unit(109)；woven(76)；properties(75)；uncertainty(73)；composites(69)；plain(68)；composite(65)；boundary(64)；parameters(62)；cell(60)；conditions(53)；effective(52)；matrix(52)；bundles(51)；modulus(47)；displacement(47)；bundle(46)；cells(45)；analysis(44)
- 高频学术名词：analysis(88)；properties(75)；parameters(62)；conditions(53)；displacement(47)；distribution(39)；model(29)；structure(28)；simulation(26)；structures(24)；quantification(24)；correlation(22)；parameter(19)；method(18)；results(17)；transformation(17)
- 高频学术动词：shows(30)；compared(10)；shown(7)；indicates(7)；developed(6)；show(5)；formulated(4)；validated(3)；formulate(3)；develop(2)；derived(2)；derive(1)；predicted(1)；solve(1)；predict(1)；proposed(1)
- 高频形容词：effective(104)；boundary(64)；elastic(60)；displacement(47)；thermal(36)；symmetric(32)；normal(31)；geometric(30)；coefficient(30)；constituent(20)；different(20)；relative(15)；antisymmetric(15)；mechanical(14)；summary(14)；rotational(13)
- 高频副词/连接副词：strongly(26)；respectively(22)；therefore(8)；however(6)；normally(5)；finally(4)；relatively(4)；specifically(3)；similarly(3)；significantly(2)；substantially(2)；theoretically(2)；numerically(2)；widely(2)；mostly(2)；primarily(2)
- 高频二词短语：plain woven(64)；unit cell(58)；boundary conditions(51)；fiber bundles(46)；fiber bundle(42)；unit cells(41)；woven composites(39)；effective properties(34)；thermal expansion(31)；woven composite(27)；elastic modulus(25)；composite structures(23)；uniform range(23)；poisson ratio(22)；six surfaces(22)；displacement boundary(22)
- 高频三词短语：plain woven composites(34)；plain woven composite(23)；displacement boundary conditions(22)；boundary conditions six(21)；conditions six surfaces(21)；yang composite structures(20)；summary unit cell(12)；unit cell boundary(12)；cell boundary conditions(12)；fiber bundles uniform(12)；bundles uniform range(12)；thermal expansion coefficient(11)

**主动、被动与句法**

- 被动语态估计次数：146
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：685
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：304
- 一般过去时线索：38
- 现在完成时线索：3
- 情态动词线索：41
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：uncertainty(29)；unit(26)；cell(16)；quantification(14)；composites(14)；composite(13)；effective(13)；properties(12)
- 3.2. Unit cells and geometric parameters：无明显高频项
- 3.2.1. Translational symmetric structure：symmetry(19)；displacement(17)；direction(9)；surfaces(9)；average(8)；uoq(7)；surface(7)；points(7)
- 3.3. Unit cells and their parameterization：work(1)；plain(1)；woven(1)；composites(1)；fiber(1)；bundles(1)；considered(1)；meso-scale(1)
- 3.3.1. Microscale fiber bundle：fiber(127)；unit(76)；woven(64)；properties(62)；boundary(58)；plain(57)；parameters(55)；composites(54)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：uncertainty quantification、plain woven composites、effective properties、unit cell、minimum-size、structural symmetries、Nataf transformation、fiber bundle、correlation、computational cost。

可复用问题句：`The uncertainty quantification is crucial to the high-precision prediction of X. However, A, B, and C are three primary problems at present.`

可复用贡献句：`For accuracy holding, ...; for cost control, ...` 这个二分结构非常适合方法论文摘要，把贡献分成性能与成本两个维度。

可复用方法句：`The uncertainties of geometry are described by uniform distributions, while those of constituent properties are described by normal distributions.`

可复用结果句：`The evolution convergence for statistical uncertainties is finally obtained with a totally reduced computational cost of X%.`

可复用讨论句：`The relevant effects of input properties on effective properties can be categorized into fiber-dominated, matrix-dominated, and co-dominated.`

## 15. 引用策略与文献使用

引用策略主要按功能组织。背景引用支撑织物复合材料航空/汽车应用与制造不确定性；方法引用覆盖 Monte Carlo、surrogate models、analytical/numerical homogenization、unit cell boundary conditions、Nataf/copula 等相关技术；团队前期工作用于支撑反射/旋转对称单胞理论。

作者对 surrogate 文献的姿态是“认可但指出折衷”：它们能减少仿真数量，但可能牺牲精度。对 unit cell 文献的姿态是继承和扩展：全尺寸周期单胞已有，本文继续利用更多对称性形成最小单胞。对 Nataf/copula 的姿态是方法选择：copula 可处理尾依赖，但本文输出没有显著非线性相关，因此 Nataf 足够。

引用风险在于输入不确定性分布假设需要更多制造实测文献支撑；如果读者来自不确定性量化领域，可能希望看到对 Nataf 与 copula/非高斯方法的更系统比较。

## 16. 审稿人视角风险

1. 几何参数 ±25% uniform distribution 是否真实代表制造误差，可能需要实验测量或工艺统计支持。
2. Nataf transformation 对非正态和尾相关处理有限，若输出分布多峰或偏态明显，传播精度可能受影响。
3. 最小单胞边界条件复杂，网格必须满足严格对称关系，实际自动化建模难度可能被低估。
4. 文章强调“不牺牲精度”，但需要更清楚报告与 full-size unit cell 的误差指标和误差来源。
5. 成本降低百分比与硬件、网格密度、求解器设置相关，跨平台可比性有限。
6. 输出相关性解释主要基于 Pearson correlation，不能完全证明物理因果。

## 17. 可复用资产

可复用选题套路：当主流方法通过 surrogate 降低样本数时，换一个角度从单次仿真成本入手，形成差异化 gap。

可复用论证链：多尺度制造不确定性 → Monte Carlo 成本高 → 最小单胞降低单次成本 → Nataf 保留尺度间相关 → 统计收敛与相关矩阵解释输出。

可复用图表：多尺度流程图；对称性几何示意；单胞逐步缩小图；参数化示意；不同单胞误差对比；均值/方差收敛曲线；输出直方图；输入-输出相关热图。

可复用表达：`accuracy holding`, `cost control`, `traceability description`, `inter-scale propagation`, `without compromising accuracy`, `fiber-dominated/matrix-dominated/co-dominated`。

## 18. 对我写论文的启发

这篇论文最值得学的是贡献拆分方式：摘要中直接把问题分成三个痛点，再把解决方案分成“精度保持”和“成本控制”。这种结构非常适合复杂方法论文，可以让读者迅速理解贡献不是单点技巧，而是一套流程。

如果自己写多尺度/多模块论文，应该像本文一样先画总流程图，再进入每个模块公式。否则大量边界条件和参数化细节会让读者迷路。

需要避免的是输入分布假设太轻。如果自己有制造不确定性主题，应尽量用真实测量、工艺标准或文献统计支撑每个分布，而不是只写“commonly assumed”。

## 19. 最终浓缩

本文最值得学的是：用最小尺寸单胞降低多尺度 UQ 的单次仿真成本，同时用 Nataf 保留尺度间相关性，把“准确”和“便宜”放到同一框架中。

最大风险是：输入分布和 Nataf 相关传播的适用性需要更多实测支撑，边界条件与图表细节需要 PDF 复核。

可迁移的三件事：一是把 gap 写成多个并列痛点；二是把贡献分成 accuracy holding 与 cost control；三是用相关矩阵把 UQ 结果转化为可解释的主导机制。
