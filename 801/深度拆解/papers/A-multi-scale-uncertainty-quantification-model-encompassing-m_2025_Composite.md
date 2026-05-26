# A multi-scale uncertainty quantification model encompassing minimum-size unit cells for effective properties of plain woven composites

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.txt`。该文图表和公式较多，txt 抽取存在明显串栏；尤其是边界条件公式、Table 1-14、Fig. 2-24 的几何/相关性/直方图细节需要 PDF 图像复核。本文依据可识别的摘要、Introduction、模型流程、单胞参数化、UQ 结果和 Conclusions 进行拆解。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Multi-scale uncertainty quantification model, 3 Minimum-size unit cells and model parameterizations, 4 Parameter uncertainty and propagation model, 5 Results and discussions, 6 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-multi-scale-uncertainty-quantification-model-encompassing-m_2025_Composite.md`。

中文译文：

> 不确定性量化对于复合材料有效性能的高精度预测至关重要。然而，多尺度参数的输入不确定性不明确、尺度间相关性的不确定性传播复杂以及大规模模拟的计算成本难以承受是目前的三个主要问题。在这项工作中，开发了一种具有高精度和可行成本的创新模型，用于平纹编织复合材料的机械性能预测，包括最小尺寸单元和多尺度不确定性量化。为了保持精度，建立了由溯源描述、尺度间传播和量化组成的不确定性分析流程。几何形状的不确定性分别通过纤维、纤维束和复合材料尺度的均匀分布来描述；成分性质的分布用纤维和基体的正态分布来描述，其向束和复合尺度的传播是通过考虑参数相关性的Nataf变换方法实现的。为了控制成本，通过对结构对称性的详尽分析来制定最小尺寸晶胞，以在不影响单次模拟精度的情况下降低计算成本，并获得与传统全尺寸晶胞相比的1/8和1/16晶胞。
>
> 最终获得有效属性​​统计不确定性的演化收敛，计算成本总共降低了89%。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6]. However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 本文解决方式：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present. In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale uncertainty quantification. The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Multi-scale uncertainty quantification model（方法/模型/算法）
- L2 p.2: 3 Minimum-size unit cells and model parameterizations（方法/模型/算法）
  - L3 p.2: 3.1 Constitutive equation and constituent parameters（对象/模块/过渡章节）
  - L3 p.3: 3.2 Unit cells and geometric parameters（对象/模块/过渡章节）
    - L4 p.3: 3.2.1 Translational symmetric structure（对象/模块/过渡章节）
    - L4 p.4: 3.2.2 Summary of symmetry（对象/模块/过渡章节）
  - L3 p.5: 3.3 Unit cells and their parameterization（对象/模块/过渡章节）
    - L4 p.5: 3.3.1 Microscale fiber bundle（对象/模块/过渡章节）
    - L4 p.8: 3.3.2 Mesoscale woven composite material（对象/模块/过渡章节）
- L2 p.10: 4 Parameter uncertainty and propagation model（方法/模型/算法）
  - L3 p.11: 4.1 Traceability description of parameter uncertainty（问题定义）
  - L3 p.11: 4.2 Inter-scale propagation model（方法/模型/算法）
    - L4 p.11: 4.2.1 Multiscale uncertainty propagation process（对象/模块/过渡章节）
    - L4 p.11: 4.2.2 The multivariate gaussian distribution（对象/模块/过渡章节）
    - L4 p.12: 4.2.3 Nataf transformation（对象/模块/过渡章节）
- L2 p.14: 5 Results and discussions（结果/验证/讨论）
  - L3 p.14: 5.1 Analysis of model accuracy and efficiency（方法/模型/算法）
  - L3 p.15: 5.2 Multiscale uncertainty analysis（对象/模块/过渡章节）
    - L4 p.15: 5.2.1 Microscale uncertainty analysis（对象/模块/过渡章节）
    - L4 p.19: 5.2.2 Mesoscale uncertainty analysis（对象/模块/过渡章节）
- L2 p.19: 6 Conclusions（结论/贡献回收）
- L2 p.21: CRediT authorship contribution statement（尾部材料）
- L2 p.21: Declaration of competing interest（尾部材料）
- L2 p.21: Acknowledgements（尾部材料）
- L2 p.21: datalink4（对象/模块/过渡章节）
- L2 p.21: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Multi-scale uncertainty quantification model | 2 | 2 | 方法/模型/算法 |
| 3 Minimum-size unit cells and model parameterizations | 2 | 2 | 方法/模型/算法 |
| 3.1 Constitutive equation and constituent parameters | 2 | 3 | 对象/模块/过渡章节 |
| 3.2 Unit cells and geometric parameters | 3 | 3 | 对象/模块/过渡章节 |
| 3.2.1 Translational symmetric structure | 3 | 4 | 对象/模块/过渡章节 |
| 3.2.2 Summary of symmetry | 4 | 4 | 对象/模块/过渡章节 |
| 3.3 Unit cells and their parameterization | 5 | 3 | 对象/模块/过渡章节 |
| 3.3.1 Microscale fiber bundle | 5 | 4 | 对象/模块/过渡章节 |
| 3.3.2 Mesoscale woven composite material | 8 | 4 | 对象/模块/过渡章节 |
| 4 Parameter uncertainty and propagation model | 10 | 2 | 方法/模型/算法 |
| 4.1 Traceability description of parameter uncertainty | 11 | 3 | 问题定义 |
| 4.2 Inter-scale propagation model | 11 | 3 | 方法/模型/算法 |
| 4.2.1 Multiscale uncertainty propagation process | 11 | 4 | 对象/模块/过渡章节 |
| 4.2.2 The multivariate gaussian distribution | 11 | 4 | 对象/模块/过渡章节 |
| 4.2.3 Nataf transformation | 12 | 4 | 对象/模块/过渡章节 |
| 5 Results and discussions | 14 | 2 | 结果/验证/讨论 |
| 5.1 Analysis of model accuracy and efficiency | 14 | 3 | 方法/模型/算法 |
| 5.2 Multiscale uncertainty analysis | 15 | 3 | 对象/模块/过渡章节 |
| 5.2.1 Microscale uncertainty analysis | 15 | 4 | 对象/模块/过渡章节 |
| 5.2.2 Mesoscale uncertainty analysis | 19 | 4 | 对象/模块/过渡章节 |
| 6 Conclusions | 19 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 21 | 2 | 尾部材料 |
| Declaration of competing interest | 21 | 2 | 尾部材料 |
| Acknowledgements | 21 | 2 | 尾部材料 |
| datalink4 | 21 | 2 | 对象/模块/过渡章节 |
| References | 21 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 前两段从材料应用和制造不确定性切入，随后引入 Monte Carlo 成本问题，再转到 unit cell 尺寸对单次仿真成本的影响。这个转折很关键：它把文章从普通 UQ 论文变成“UQ 成本控制”论文。

方法段落节奏是“定义规则 → 图示对称性 → 给约束方程 → 应用到具体单胞”。虽然公式密集，但每组公式都服务于一个几何对称操作。参数化段落则从 microscale 到 mesoscale，保持尺度递进。

结果段落先讲收敛，再讲分布，再讲相关性，最后给物理解释：哪些输出由 fiber 主导，哪些由 matrix 主导，哪些共同主导。这种顺序非常适合 UQ 论文，因为它先确认统计结果可靠，再解释不确定性来源。

## 13. 文笔画像与语言习惯

整体语气是方法工程型，常用 uncertainty quantification、effective properties、unit cell、symmetry、correlation、distribution、computational cost。claim 强度偏强，尤其是 “without accuracy compromising”“reduced computational cost of 89%”，但在 Nataf 选择处有边界说明：输出参数没有显著非线性相关，因此采用 Nataf。

主动语态较少，多用被动和客观结构：“is developed”“is established”“is adopted”“can be calculated”。这让文本呈现公式/流程驱动的风格。

时态上，一般现在时用于模型定义和物理/数学事实；过去时较少，主要用于结果描述；将来/情态表达用于方法用途。名词化高，如 traceability description、inter-scale propagation、parameterization、transformation、quantification。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：48671
- 高频词：fiber(93)；uncertainty(57)；unit(55)；matrix(45)；properties(43)；displacement(37)；boundary(35)；cell(34)；modulus(34)；effective(32)；parameters(32)；analysis(31)；bundle(30)；conditions(30)；bundles(29)；normal(28)；surfaces(28)；distribution(27)；woven(25)；uniform(25)
- 高频名词化/学术名词：displacement(37)；distribution(27)；expansion(22)；correlation(21)；transformation(17)；quantification(15)；function(13)；propagation(12)；simulation(11)；direction(11)；calculation(9)；structure(8)；computation(7)；difference(6)；sub-figure(6)
- 高频学术动词：compared(6)；developed(5)；develop(2)；constructed(2)；analyzed(2)；provide(1)；predicted(1)；achieved(1)；derived(1)；estimate(1)；derive(1)；validated(1)
- 高频形容词：displacement(37)；boundary(35)；effective(32)；normal(28)；thermal(21)；coefficient(21)；elastic(20)；geometric(17)；constituent(14)；symmetric(13)；computational(12)；rotational(10)；different(9)；translational(9)；directional(8)
- 高频副词：strongly(9)；finally(4)；mostly(3)；widely(2)；specifically(2)；primarily(2)；positively(2)；mainly(2)；totally(1)；theoretically(1)；computationally(1)；surely(1)；numerically(1)；typically(1)；solely(1)
- 高频二词短语：unit cell(34)；fiber bundle(29)；boundary conditions(29)；fiber bundles(29)；uniform range(23)；plain woven(22)；thermal expansion(21)；effective properties(19)；elastic modulus(19)；six surfaces(18)；displacement boundary(18)；poisson ratio(17)
- 高频三词短语：displacement boundary conditions(18)；boundary conditions six(17)；conditions six surfaces(17)；six surfaces follows(16)；surfaces follows displacement(13)；follows displacement boundary(13)；plain woven composites(12)；fiber bundles uniform(12)；bundles uniform range(12)；plain woven composite(9)；gap fiber bundles(9)；thermal expansion coefficient(8)
- 被动语态估计：88；`we + 动作动词` 主动句估计：0
- 一般现在时线索：193；一般过去时线索：203；现在完成时线索：2；情态动词线索：24

分章节正文词频：

- 1 Introduction: uncertainty(17)；unit(14)；method(11)；cost(11)；computational(10)；composites(9)；fiber(9)；properties(9)
- 2 Multi-scale uncertainty quantification model: uncertainty(12)；unit(9)；cell(8)；size(7)；quantification(6)；cost(4)；analysis(4)；conditions(3)
- 3 Minimum-size unit cells and model parameterizations: displacement(36)；boundary(29)；surfaces(28)；conditions(23)；ras(23)；unit(21)；ros(21)；follows(20)
- 4 Parameter uncertainty and propagation model: fiber(41)；normal(26)；uniform(24)；range(23)；distribution(21)；uncertainty(20)；matrix(20)；bundles(19)
- 5 Results and discussions: fiber(23)；matrix(17)；modulus(15)；properties(15)；effective(14)；bundle(12)；parameters(12)；analysis(10)
- 6 Conclusions: unit(4)；developed(3)；minimum(3)；quantification(2)；model(2)；accuracy(2)；cost(2)；plain(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：uncertainty quantification、plain woven composites、effective properties、unit cell、minimum-size、structural symmetries、Nataf transformation、fiber bundle、correlation、computational cost。

可复用问题句：`The uncertainty quantification is crucial to the high-precision prediction of X. However, A, B, and C are three primary problems at present.`

可复用贡献句：`For accuracy holding, ...; for cost control, ...` 这个二分结构非常适合方法论文摘要，把贡献分成性能与成本两个维度。

可复用方法句：`The uncertainties of geometry are described by uniform distributions, while those of constituent properties are described by normal distributions.`

可复用结果句：`The evolution convergence for statistical uncertainties is finally obtained with a totally reduced computational cost of X%.`

可复用讨论句：`The relevant effects of input properties on effective properties can be categorized into fiber-dominated, matrix-dominated, and co-dominated.`

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
  可迁移模板：Thus, for plain woven composites with uncertainties of at least three scales, i.e., composite, fiber bundle, fiber, and matrix, the primary challenge in uncertainty quantification by Monte Carlo method is the unaffordable computational burden.
- 原句：Thus, an exhaustive analysis of structural symmetries to formulate unit cells with minimum size is essential to obtain a balance between the computation cost and accuracy.
  可迁移模板：Thus, an exhaustive analysis of structural symmetries to formulate unit cells with minimum size is essential to obtain a balance between the computation cost and accuracy.
#### Gap/转折句
- 原句：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
  可迁移模板：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 原句：However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6].
  可迁移模板：However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [X,X].
- 原句：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
  可迁移模板：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 原句：However, this approach involves a significant amount of computationally intensive simulations to explore the entire uncertainty space.
  可迁移模板：However, this approach involves a significant amount of computationally intensive simulations to explore the entire uncertainty space.
- 原句：However, they incur higher costs in terms of model construction and solving numerous equations.
  可迁移模板：However, they incur higher costs in terms of model construction and solving numerous equations.
#### 方法提出句
- 原句：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
  可迁移模板：However, the unclear input uncertainties of multiscale parameters, complex uncertainty propagations of interscale correlations, and unaffordable computational cost of massive simulations are three primary problems at present.
- 原句：In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale uncertainty quantification.
  可迁移模板：In this work, an innovative model with high accuracy and feasible cost for the mechanical property prediction of plain woven composites is developed encompassing minimum-size unit cells and multi-scale uncertainty quantification.
- 原句：The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations.
  可迁移模板：The uncertainties of geometry are described by uniform distributions for fiber, fiber bundle and composite scales, respectively; that of constituent properties is described by normal distributions for fiber and matrix, and its propagations to bundle and composite scales are realized by Nataf transformation methods with the consideration of parameter correlations.
- 原句：Such type of material is developed by embedding fabric fibers into resin or ceramic matrix to take advantages of both the fiber and matrix.
  可迁移模板：Such type of material is developed by embedding fabric fibers into resin or ceramic matrix to take advantages of both the fiber and matrix.
- 原句：The mostly used method in uncertainty * Corresponding author.
  可迁移模板：The mostly used method in uncertainty * Corresponding author.
#### 结果呈现句
- 原句：Such method tend to outcome true results as the number of simulations increases [16].
  可迁移模板：Such method tend to outcome true results as the number of simulations increases [X].
- 原句：Based on the fullsize unit cell, the reflectional and rotational symmetries are further utilized to reduce the unit cell size in our previous works, it is found that the smaller size unit cell will obtain the same results and great reduction of computation cost, and the only disadvantage is the complicated boundary conditions [34–38].
  可迁移模板：Based on the fullsize unit cell, the reflectional and rotational symmetries are further utilized to reduce the unit cell size in our previous works, it is found that the smaller size unit cell will obtain the same results and great reduction of computation cost, and the only disadvantage is the complicated boundary conditions [X–X].
#### 贡献/增量句
- 原句：For the accuracy holding, an uncertainty analysis process consists of the traceability description, inter-scale propagation and quantification is established.
  可迁移模板：For the accuracy holding, an uncertainty analysis process consists of the traceability description, inter-scale propagation and quantification is established.
- 原句：For the accuracy holding, an uncertainty analysis process consists of the traceability description, inter-scale propagation and quantification is established.
  可迁移模板：For the accuracy holding, an uncertainty analysis process consists of the traceability description, inter-scale propagation and quantification is established.
- 原句：Theoretically, executing a sufficient number of Monte Carlo samples can provide a reliable measure of uncertainty.
  可迁移模板：Theoretically, executing a sufficient number of Monte Carlo samples can provide a reliable measure of uncertainty.
- 原句：This enables examination of a wider range of parameters and more complex systems.
  可迁移模板：This enables examination of a wider range of parameters and more complex systems.
#### 限制/边界句
- 原句：Based on the fullsize unit cell, the reflectional and rotational symmetries are further utilized to reduce the unit cell size in our previous works, it is found that the smaller size unit cell will obtain the same results and great reduction of computation cost, and the only disadvantage is the complicated boundary conditions [34–38].
  可迁移模板：Based on the fullsize unit cell, the reflectional and rotational symmetries are further utilized to reduce the unit cell size in our previous works, it is found that the smaller size unit cell will obtain the same results and great reduction of computation cost, and the only disadvantage is the complicated boundary conditions [X–X].
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略主要按功能组织。背景引用支撑织物复合材料航空/汽车应用与制造不确定性；方法引用覆盖 Monte Carlo、surrogate models、analytical/numerical homogenization、unit cell boundary conditions、Nataf/copula 等相关技术；团队前期工作用于支撑反射/旋转对称单胞理论。

作者对 surrogate 文献的姿态是“认可但指出折衷”：它们能减少仿真数量，但可能牺牲精度。对 unit cell 文献的姿态是继承和扩展：全尺寸周期单胞已有，本文继续利用更多对称性形成最小单胞。对 Nataf/copula 的姿态是方法选择：copula 可处理尾依赖，但本文输出没有显著非线性相关，因此 Nataf 足够。

引用风险在于输入不确定性分布假设需要更多制造实测文献支撑；如果读者来自不确定性量化领域，可能希望看到对 Nataf 与 copula/非高斯方法的更系统比较。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：69
- Introduction 引文簇数量估计：11
- References 条目数：47
- 可识别年份条目数：50
- 2021 年及以后文献数：10
- 2010 年前经典文献数：18
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Composite Structures(2)
- 引文簇样例：[15], [16], [11], [12], [13], [5,6], [17], [39], [40], [41], [42], [18,21,23,30,32,34,35,36,38,43]

带引文的 gap/转折句样例：

- However, the mold making, dimensional processing and high temperature in the composite manufacturing bring about various uncertainties of geometric and constituent parameters in multiple scales, thus, it is crucial to quantify these uncertainties to hold the prediction accuracy of composites properties [5,6].

References 解析样例（前 8 条）：

- [1] ˙Inal O, Katnam KB, Potluri P, Soutis C. Progress in interlaminar toughening of aerospace polymer composites using particles and non-woven veils. Aeronaut J 2022;126:222–48.
- [2] Amraei J, Rogala T, Katunin A, Premanand A, et al. Thermomechanical fatigue behavior of CF/PEKK composite under low and ultrasonic frequencies. Compos B Eng 2024;281:111539.
- [3] Abtew MA. A comprehensive review on advancements, innovations and applications of 3D warp interlock fabrics and its composite materials. Compos B Eng 2024;278:111395.
- [4] Ivanov DS, Lomov SV. 2 - Modelling the structure and behaviour of 2D and 3D woven composites used in aerospace applications. In: Irving PE, Soutis C, editors. Polymer Composites in the Aerospace Industry. Woodhead Publishing; 2015. p. 21–52.
- [5] Potter, K. D., Understanding the origins of defects and variability in composites manufacture. In International conference on composite materials (ICCM)-17, Edinburgh, UK (2009): p. 18.
- [6] Mesogitis TS, Skordos AA, Long AC. Uncertainty in the manufacturing of fibrous thermosetting composites: A review. Compos A Appl Sci Manuf 2014;57:67–75.
- [7] Greene MS, Xu H, Tang S, Chen W, Liu WK. A generalized uncertainty propagation criterion from benchmark studies of microstructured material systems. Comput Methods Appl Mech Eng 2013;254:271–91.
- [8] Fang G, Wang B, Liang J. A coupled FE-FFT multiscale method for progressive damage analysis of 3D braided composite beam under bending load. Compos Sci Technol 2019;181:107691.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

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
