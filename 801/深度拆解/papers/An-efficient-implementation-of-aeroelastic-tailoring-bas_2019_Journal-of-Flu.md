## 0. 读取说明

本文依据 `801/文本/txt/An-efficient-implementation-of-aeroelastic-tailoring-bas_2019_Journal-of-Flu.txt` 的全文抽取进行拆解。抽取文本包含摘要、引言、方法公式、AGARD 445.6 算例、表格数值与结论，能够支撑对方法链、证据链和写法的复原。部分图中曲线、网格局部形态和时间历程细节只能从图题与正文描述间接判断，涉及视觉细节处均标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：Introduction, Overview of traditional direct evaluation method, Approximate aeroelastic characteristics evaluation method, Numerical results and discussion, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：An efficient implementation of aeroelastic tailoring based on efficient computational fluid dynamics-based reduced order model
- 期刊：Journal of Fluids and Structures, 84 (2019) 182-198
- 作者：Dongfeng Li, Chunlin Gong, Andrea Da Ronch, Gang Chen, Yueming Li
- 机构：Xi’an Jiaotong University, Northwestern Polytechnical University, University of Southampton 等
- 关键词：Aeroelastic tailoring; Aeroelastic characteristics evaluation method; CFD-based POD/ROM; Structural dynamic reanalysis method

论文身份可以概括为：面向复合材料机翼气动弹性剪裁优化的“快速评估器”论文。它不是提出新的剪裁目标或新的复合材料力学模型，而是解决 CFD-based ROM 在结构参数反复变化时需要重复构造 ROM 的计算瓶颈。文章核心贡献是把结构动力学重分析方法嵌入 CFD-based POD/ROM，使基准结构的气动力 ROM 可以经由模态变换被近似迁移到修改结构上。

## 2. 摘要与核心信息提取

摘要的叙事非常清楚：先指出气动弹性剪裁优化需要反复评估结构变化后的响应与稳定性；再指出高保真 CFD 虽然准确但代价高，传统 CFD-based ROM 虽然快速但通常绑定某一结构模型；随后提出将结构动力学重分析用于更新结构模态并变换气动 ROM；最后用跨声速复合材料 AGARD 445.6 机翼验证精度和效率。

核心信息有三层：

1. 问题层：复合材料铺层参数变化会改变机翼刚度和模态，气动弹性剪裁优化需要大量重复评估。
2. 方法层：基准 CFD-based POD/ROM + 结构动力学重分析得到的模态变换矩阵 `Z` + 变换后的广义气动力模型。
3. 证据层：AGARD 445.6 标准翼验证基准 ROM 的跨声速颤振预测能力，再用三种复合材料铺层比例变化模型 A/B/C 验证近似更新精度和成本优势。

一句话浓缩：本文把“每次结构变化都重新建 CFD-ROM”的问题转成“基准 ROM 通过结构重分析矩阵快速更新”的问题。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/An-efficient-implementation-of-aeroelastic-tailoring-bas_2019_Journal-of-Flu.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-efficient-implementation-of-aeroelastic-tailoring-bas_2019_Journal-of-Flu.md`。

中文译文：

> 航空航天业当前和未来的趋势利用轻质材料提供的潜在优势，这些材料可以定制以在加载时实现所需的机械特性。对于飞机设计来说，对于任何可能的结构修改，需要重新计算空气动力场对基础结构特性的依赖性，这阻碍了气动弹性剪裁的部署。为了在这个方向上取得进展，这项工作提出了一种基于快速计算流体动力学的气动弹性工具，该工具是围绕空气动力学降阶模型构建的，该模型通过使用结构动力学再分析方法针对结构的任何修改进行更新。气动弹性剪裁工具在 AGARD 445.6 机翼的跨音速流中进行了演示，并使用复合材料进行了适当修改。结果发现，当结构从基线模型修改时，所提出的方法可以为气动弹性响应和稳定性提供准确的工程预测。 © 2018 Elsevier Ltd. 保留所有权利。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题抓住了气动弹性剪裁中的一个工程痛点：优化空间大、每个候选结构都需要气动弹性响应和颤振边界评估，而 CFD 级别的非定常气动模型昂贵。传统降阶模型的优势在于用一次训练换取多次快速响应，但它的隐含前提是结构模态基底不变。复合材料剪裁恰恰以改变刚度、模态和耦合特性为目标，于是 ROM 的“可复用性”与剪裁的“结构可变性”发生冲突。

这个选题的妙处在于没有直接挑战完整 CFD 优化，而是切入优化循环里最频繁、最耗时的一环：结构参数改变后的气动弹性特性评估。文章把宏大问题收缩成一个可验证的技术命题：当结构相对基准发生修改时，能否不重新生成 POD/ROM，而用结构动力学重分析构造近似模型，并保持工程可接受精度。

选题的应用场景非常明确：复合材料机翼铺层角、铺层比例、材料参数改变；气动弹性响应、稳定性和颤振速度反复计算；跨声速条件下需要 CFD 而非简单势流或 DLM 模型。它的目标读者不是单纯结构优化读者，而是关心高保真气动弹性分析如何进入优化内环的人。

## 4. 领域位置与文献版图

文章将文献版图分成三组：

第一组是气动弹性剪裁与复合材料机翼优化。这里强调复合材料通过铺层角、层合比例等参数改变弯扭耦合和气动弹性稳定边界，是主动利用结构各向异性来改善性能。

第二组是 CFD-based reduced order model。作者承认 POD/ROM、linearized CFD ROM、Volterra、ARX 等方法已经能显著降低非定常气动力计算成本，尤其在固定结构和固定飞行条件附近表现良好。

第三组是结构动力学重分析。Kirsch 类方法和组合近似方法能够在结构刚度或质量矩阵变化后快速估计修改结构的模态与频率，但这些方法通常服务于结构动力学本身，较少与 CFD-based 气动弹性 ROM 直接耦合。

因此本文位于三者交叉处：不是“又一个 ROM”，也不是“又一个结构重分析算法”，而是把结构重分析作为 ROM 可迁移机制，服务于气动弹性剪裁优化。

## 5. Gap 制造机制

本文的 gap 不是通过说现有方法“不准确”来制造，而是通过“准确但不可反复使用”来制造。

作者先承认 CFD-based ROM 在非定常气动力与气动弹性响应预测上已经有效；然后指出这些 ROM 通常围绕某一组结构模态建立。当复合材料剪裁改变刚度矩阵和模态形状时，原有 ROM 的广义坐标、气动力矩阵和结构方程不再直接匹配。

进一步，若每一个铺层设计都重新构造 CFD-based POD/ROM，则优化循环成本接近不可接受。文中用 Table 4 把这个 gap 数字化：直接方案对 1000 个结构变化、20 个动压点的估算成本达到 16009.72 h，而近似更新方案约 26.31 h。这个数量级差异使 gap 从“方法不够优雅”变成“优化流程难以落地”。

Gap 的逻辑链如下：

1. 高保真 CFD 是跨声速气动弹性分析所需。
2. CFD-based ROM 可以降低单个结构模型的分析成本。
3. 气动弹性剪裁会造成大量结构模型变化。
4. 现有 ROM 对结构变化缺乏快速更新机制。
5. 因此需要一种能在结构变化后复用基准 ROM 的快速气动弹性评估方法。

## 6. 创新性判断

创新性主要是系统集成型和计算流程型，而非单个物理模型原创。

强创新点：

- 把结构动力学重分析得到的模态变换矩阵 `Z` 用作 CFD-based POD/ROM 的结构更新桥梁。
- 将修改结构的广义位移映射回基准模态空间，使基准气动力 ROM 可以服务于结构变化后的气动弹性方程。
- 在跨声速 AGARD 445.6 复合材料机翼上同时展示响应、广义气动力、颤振速度和计算成本。

中等创新点：

- 将复合材料层合板理论、线性化 Euler CFD ROM 和扩展 Kirsch 重分析方法组装成面向优化内环的评估框架。
- 用固定铺层顺序但改变 0/45/-45/90 比例的 Model A/B/C 构造典型剪裁扰动。

创新边界：

- POD/ROM 本体和结构重分析方法并非从零提出。
- 优化本身没有完整展开，论文验证的是“快速评估工具”，不是端到端剪裁优化器。
- 结构修改假设相对基准模型，且文中主要处理质量不变、刚度变化的剪裁情形。

## 7. 论证链条复原

全文论证链条可以复原为七步：

1. 气动弹性剪裁需要大量结构候选方案的跨声速气动弹性分析。
2. 直接 CFD 耗时，固定结构的 CFD-based POD/ROM 虽快但难以处理结构参数变化。
3. 复合材料铺层变化可以通过层合板理论进入结构刚度矩阵，从而改变模态。
4. 修改结构的模态可以用结构动力学重分析从基准模态近似得到。
5. 若存在修改模态与基准模态之间的变换矩阵 `Z`，则广义位移和气动力 ROM 矩阵也可被相应变换。
6. 对 AGARD 445.6 标准翼，基准 CFD/ROM 能准确预测跨声速颤振边界，说明基准模型可信。
7. 对三种复合材料改型，近似方法在频率、MAC、广义气动力、响应和颤振速度上接近直接 ROM，且成本大幅降低。

这条论证的中心不是“模型更准确”，而是“相近精度下快得足以进入优化循环”。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：For aircraft design, the deployment of aeroelastic tailoring is hindered by the need to re-compute, for any possible modification of the structure, the dependence of the aerodynamic field on the underlying structural properties. For aircraft design, the deployment of aeroelastic tailoring is hindered by the need to re-compute, for any possible modification of the structure, the dependence of the aerodynamic field on the underlying structural properties. Efficiency evaluation of the aeroelastic characteristics evaluation method Our objective is to propose a new approximate aeroelastic characteristics evaluation method which is suitable for transonic aeroelastic tailoring, so the computational efficiency is one of the most important criteria of the proposed method for assess the aeroelastic stability in aeroelastic tailoring process.
- 已有研究不足/GAP：Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades. However the computational cost of the proposed approximate aeroelastic characteristics evaluation method is only 16 h × 1 + 0.74 s × 1000 + 1.82 s × 20 × 1000 = 26.31 h about which is only little more than one day. However, without the most expensive time-consuming reconstruction procedure, the computational cost of the proposed method is reduced obviously, especially after the POD/ROM for original structure was constructed.
- 本文解决方式：To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method. It was found that the proposed method provides accurate engineering predictions for the aeroelastic response and stability when the structure is modified from the baseline model. © 2018 Elsevier Ltd. To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method.
- 学术或工程增量：Current and future trends in the aerospace industry leverage on the potential benefits provided by lightweight materials that can be tailored to realize desired mechanical characteristics when loaded. The aeroelastic tailoring tool is demonstrated in transonic flow for the AGARD 445.6 wing, suitably modified with composite materials. It was found that the proposed method provides accurate engineering predictions for the aeroelastic response and stability when the structure is modified from the baseline model. © 2018 Elsevier Ltd.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法由三个模块构成。

第一，复合材料结构建模。文章使用经典层合板理论生成等效刚度，涉及 A/B/D 矩阵、铺层角和各层比例。铺层设计变量不直接出现在气动力模型中，而是通过改变结构刚度矩阵，进一步改变固有频率和模态。

第二，CFD-based POD/ROM。非定常气动力来自线性化 Euler 方程和 POD 降阶。基准模型先在选定结构模态下构造流场扰动快照，提取 POD 基，再建立低维气动状态方程。文中 Eq. 3-12 一类公式承担这个功能：把高维 CFD 离散系统压缩成可快速时域推进的广义气动力模型。

第三，结构动力学重分析。修改结构的模态不是重新完整求解，而是用扩展 Kirsch 组合近似方法由基准模态展开。对剪裁问题，作者采用质量矩阵不变或近似不变的设定，即 `Delta M = 0`，重点处理刚度变化。重分析产生变换矩阵 `Z`，使修改结构的模态坐标可以与基准结构 ROM 关联。

关键耦合步骤是：

- 修改结构广义位移 `u_b = Z u`；
- 气动力 ROM 中的矩阵按 `Z` 变换，例如 `G = ZG_b`、`E = ZE_b`、`C = ZC_b`；
- 最终形成修改结构的低维流固耦合方程。

这套模型的核心假设是：结构变化没有大到破坏基准气动降阶空间的表达能力；修改模态仍可由基准模态组合近似；跨声速小扰动附近的线性化 ROM 足够描述响应和稳定性。

## 9. 证据系统与 Claim-Evidence 表

| Claim | Evidence | 论证功能 | 潜在限制 |
|---|---|---|---|
| 基准 CFD/ROM 能可靠预测标准 AGARD 445.6 翼颤振边界 | 标准翼算例覆盖 Mach 0.499-1.141，颤振边界与 Yates 实验和全阶求解器吻合，并捕捉跨声速 dip | 先证明基准 ROM 不是弱模型 | 图中曲线精确偏差需要 PDF 图像复核 |
| 结构重分析能较准地预测剪裁后模态 | Table 2 中 Model A/B/C 频率误差最大约 3.838%，多数 MAC 接近 1，Model B 第四模态 MAC 0.9450 | 支撑 `Z` 矩阵可用于后续气动模型更新 | 只测试三种铺层比例变化 |
| 变换后的 ROM 能保留广义气动力时间历程 | Fig. 7 中 Model B 在 Ma=0.960、AOA=0 下广义气动力时域结果与直接方法一致 | 证明气动矩阵变换不仅结构正确，也能反映非定常气动力 | 曲线局部相位与峰值差异需要 PDF 图像复核 |
| 近似方法能预测稳定、临界和发散响应 | Figs. 8-10 展示不同动态压力下广义位移响应，近似方法与直接方法在衰减和发散趋势上吻合 | 说明方法可用于气动弹性稳定性判断 | 视觉曲线细节需复核，且只在示范工况验证 |
| 颤振速度误差在工程可接受范围内 | Table 3：Ma=0.960 下 Model A/B/C 直接法与近似法颤振速度误差分别为 0.481%、1.804%、1.970% | 将方法有效性落到剪裁最关心的指标 | 只报告单一 Mach 下三种模型 |
| 计算成本显著下降 | Table 4：1000 个结构变化、20 个动压点直接法约 16009.72 h，近似法约 26.31 h | 证明方法进入优化循环的价值 | 成本估算依赖具体硬件、实现和样本规模 |
| 方法适合复合材料铺层比例变化 | 改进 AGARD 翼将 0/45/-45/90 铺层比例设置为 Original 和 A/B/C 四组，模型 B 以 70% -45 层制造较强变化 | 将方法与 aeroelastic tailoring 场景绑定 | 未覆盖任意铺层顺序和质量变化 |

## 10. 图表、公式与结果叙事提取

| 类型 | 内容 | 论证功能 | 复核备注 |
|---|---|---|---|
| Fig. 1 类流程/模型图 | CFD-based ROM 与结构重分析耦合流程 | 帮读者理解“基准 ROM + 变换矩阵”的整体路径 | 需要 PDF 图像复核 |
| AGARD 445.6 几何图/网格图 | 45° 四分之一弦后掠、展弦比 1.6525、NACA65A004，CFD 网格 223,146 点 | 交代标准验证对象和计算可信度 | 网格局部质量需要 PDF 图像复核 |
| 层合板公式 | A/B/D 刚度矩阵与铺层角、层厚之间关系 | 将复合材料设计变量接入结构刚度 | 公式转写以原文为准 |
| CFD ROM 公式 Eq. 3-12 | 线性化 Euler 系统、POD 降维、广义气动力矩阵 | 建立高保真气动降阶模型 | 关键符号需与 PDF 核对 |
| 结构重分析公式 | 扩展 Kirsch 方法、模态组合、`Z` 变换矩阵 | 说明修改结构模态如何快速得到 | 组合近似阶数细节需按原文核对 |
| Eq. 31/Eq. 32 一类耦合方程 | 变换后的气动 ROM 与结构方程 | 全文方法落点，体现模型更新后的可求解系统 | 公式编号需 PDF 复核 |
| Table 2 | 三个改型的频率误差和 MAC | 验证结构重分析精度 | 数值来自文本抽取 |
| Fig. 7 | 广义气动力时间历程比较 | 验证气动 ROM 更新精度 | 曲线细节需要 PDF 图像复核 |
| Figs. 8-10 | 衰减/发散响应比较 | 验证稳定性预测 | 曲线细节需要 PDF 图像复核 |
| Table 3 | Ma=0.960 下 Model A/B/C 颤振速度误差 | 给出最终工程指标 | 数值来自文本抽取 |
| Table 4 | 直接法与近似法计算成本 | 强化效率主张 | 成本估算条件需要保留上下文 |

结果叙事节奏是：先标准翼证明 CFD/ROM 本身可信，再改型翼证明结构重分析可信，再时域气动力和响应证明耦合可信，最后用颤振速度和成本完成“准确 + 快”的双重闭环。

## 11. 章节结构与篇章布局

文章结构是典型计算方法论文：

1. Introduction：定义气动弹性剪裁的计算瓶颈，梳理 CFD ROM 和结构重分析文献，提出本文方案。
2. Formulation：分别给出复合材料层合板模型、CFD-based ROM、结构动力学重分析和耦合更新公式。
3. Numerical examples：先用标准 AGARD 445.6 验证基准方法，再构造复合材料改型并比较直接/近似方法。
4. Computational efficiency：用时间成本表格突出优化循环价值。
5. Conclusions：总结精度、效率和适用性。

布局上先“建工具”，再“证工具”，再“卖工具”。方法部分理论密度较高，但算例部分用大量表格和图把抽象公式落回频率、MAC、颤振速度、CPU 时间等可判断指标。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: Introduction（背景定位/文献缺口）
- L2 p.3: Overview of traditional direct evaluation method（方法/模型/算法）
  - L3 p.3: Mechanical model of composite laminates（方法/模型/算法）
  - L3 p.4: CFD-based reduced order model for aeroelastic system（方法/模型/算法）
- L2 p.5: Approximate aeroelastic characteristics evaluation method（方法/模型/算法）
  - L3 p.5: Structural dynamic reanalysis method（方法/模型/算法）
  - L3 p.7: Aeroelastic characteristics evaluation method for modified structure（方法/模型/算法）
- L2 p.8: Numerical results and discussion（结果/验证/讨论）
  - L3 p.8: POD/ROM solver validation（结果/验证/讨论）
  - L3 p.9: Accuracy evaluation of the structural dynamic reanalysis model（方法/模型/算法）
  - L3 p.10: Accuracy evaluation of the aeroelastic characteristics evaluation method（方法/模型/算法）
  - L3 p.12: Efficiency evaluation of the aeroelastic characteristics evaluation method（方法/模型/算法）
- L2 p.16: Conclusions（结论/贡献回收）
- L2 p.16: Acknowledgments（尾部材料）
- L2 p.16: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| Introduction | 1 | 2 | 背景定位/文献缺口 |
| Overview of traditional direct evaluation method | 3 | 2 | 方法/模型/算法 |
| Mechanical model of composite laminates | 3 | 3 | 方法/模型/算法 |
| CFD-based reduced order model for aeroelastic system | 4 | 3 | 方法/模型/算法 |
| Approximate aeroelastic characteristics evaluation method | 5 | 2 | 方法/模型/算法 |
| Structural dynamic reanalysis method | 5 | 3 | 方法/模型/算法 |
| Aeroelastic characteristics evaluation method for modified structure | 7 | 3 | 方法/模型/算法 |
| Numerical results and discussion | 8 | 2 | 结果/验证/讨论 |
| POD/ROM solver validation | 8 | 3 | 结果/验证/讨论 |
| Accuracy evaluation of the structural dynamic reanalysis model | 9 | 3 | 方法/模型/算法 |
| Accuracy evaluation of the aeroelastic characteristics evaluation method | 10 | 3 | 方法/模型/算法 |
| Efficiency evaluation of the aeroelastic characteristics evaluation method | 12 | 3 | 方法/模型/算法 |
| Conclusions | 16 | 2 | 结论/贡献回收 |
| Acknowledgments | 16 | 2 | 尾部材料 |
| References | 16 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

引言段落节奏为：应用动机 -> 高保真需求 -> ROM 进展 -> ROM 对结构变化不足 -> 结构重分析可补位 -> 本文贡献。每段都承担一个台阶，不急于提出公式。

方法段落的节奏是模块化的。复合材料、气动 ROM、结构重分析各自独立成块，最后在耦合小节合并。这种写法适合跨领域方法，因为读者可能熟悉其中一部分，不熟悉另一部分。

算例段落采用“标准基准 -> 修改模型 -> 多指标对比”的顺序。作者没有先直接宣称快，而是先确保读者相信近似结果。成本对比被放在方法可信性之后，因此效率主张更有说服力。

结论段落回收三个关键词：accurate、efficient、aeroelastic tailoring。没有扩展太多未来工作，收束较干净。

## 13. 文笔画像与语言习惯

本文英文风格偏工程计算论文：句子不追求修辞，重点在限定条件、模型动作和数值结果。常见表达包括：

- “An efficient implementation is proposed...”
- “The method is validated by...”
- “The results are compared with...”
- “Good agreement is observed...”
- “The computational cost is significantly reduced...”

文风特点是大量使用被动语态和名词化结构，例如 implementation, evaluation, modification, transformation, reanalysis。作者喜欢用 “basis model / modified model” 这样的成对术语组织全文，让复杂流程保持可跟踪。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：38204
- 高频词：aeroelastic(122)；method(61)；structural(59)；characteristics(45)；model(43)；evaluation(38)；composite(37)；tailoring(37)；structure(37)；approximate(36)；pod(34)；rom(27)；wing(24)；ply(23)；transonic(21)；computational(21)；global(21)；modified(20)；roms(18)；modeshapes(18)
- 高频名词化/学术名词：characteristics(45)；evaluation(38)；structure(37)；stiffness(13)；sequence(10)；variation(9)；section(7)；equation(7)；fraction(7)；modification(6)；performance(5)；function(5)；construction(5)；procedure(5)；description(4)
- 高频学术动词：demonstrated(8)；evaluated(7)；presented(5)；evaluate(4)；predicted(4)；compared(2)；achieve(2)；analyze(2)；predict(2)；construct(2)；propose(2)；indicated(2)；validated(2)；indicate(2)；constructed(2)
- 高频形容词：aeroelastic(122)；structural(59)；transonic(21)；computational(21)；global(21)；dynamic(15)；aerodynamic(14)；modal(12)；local(10)；different(10)；original(7)；basic(5)；potential(4)；mechanical(4)；important(4)
- 高频副词：ply(23)；commonly(4)；generally(4)；rapidly(4)；significantly(3)；accurately(3)；firstly(3)；finally(3)；successfully(2)；unfortunately(2)；increasingly(1)；simultaneously(1)；particularly(1)；highly(1)；formally(1)
- 高频二词短语：aeroelastic characteristics(41)；aeroelastic tailoring(36)；evaluation method(34)；characteristics evaluation(30)；approximate aeroelastic(26)；pod rom(16)；composite structure(13)；modified structure(12)；structural model(11)；structural parameters(11)；stacking sequence(10)；structural dynamic(10)
- 高频三词短语：aeroelastic characteristics evaluation(30)；characteristics evaluation method(29)；approximate aeroelastic characteristics(26)；aeroelastic tailoring process(9)；extended kirsch combined(9)；kirsch combined method(8)；cfd-based pod rom(6)；structural dynamic reanalysis(6)；structural parameter variation(6)；aeroelastic wing model(6)；fraction ply angles(6)；transonic aeroelastic tailoring(6)
- 被动语态估计：80；`we + 动作动词` 主动句估计：1
- 一般现在时线索：161；一般过去时线索：300；现在完成时线索：2；情态动词线索：33

分章节正文词频：

- Introduction: aeroelastic(32)；tailoring(13)；transonic(13)；composite(11)；structural(11)；roms(11)；aircraft(10)；model(10)
- Overview of traditional direct evaluation method: structural(4)；level(4)；global(4)；composite(3)；modifications(3)；local(3)；step(3)；mass(2)
- Approximate aeroelastic characteristics evaluation method: aeroelastic(32)；structural(24)；structure(23)；method(20)；pod(18)；modified(18)；matrix(15)；model(14)
- Numerical results and discussion: aeroelastic(15)；method(12)；approximate(11)；ply(11)；wing(10)；evaluation(9)；model(9)；modal(9)
- Conclusions: aeroelastic(42)；method(26)；characteristics(20)；evaluation(20)；approximate(17)；structural(12)；tailoring(10)；model(9)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用关键词：

- aeroelastic tailoring
- CFD-based reduced order model
- structural dynamic reanalysis
- generalized aerodynamic force
- basis model / modified model
- transformation matrix
- flutter boundary
- computational efficiency
- good agreement
- engineering prediction

可复用句式：

- “The main difficulty lies in the repeated construction of ... for each modified structure.”
- “To avoid rebuilding the reduced-order model, a transformation relationship is introduced between the basis and modified structural modes.”
- “The proposed approach decouples the expensive aerodynamic model construction from the repeated structural modifications.”
- “The accuracy of the approximation is assessed in terms of natural frequencies, MAC values, generalized aerodynamic forces and flutter speeds.”
- “Compared with the direct method, the proposed method reduces the computational cost by orders of magnitude while maintaining acceptable engineering accuracy.”

中文写作可借用的表达：

- “本文不是替代高保真 CFD，而是把高保真模型的一次性建模成本转化为可复用资产。”
- “该方法的关键在于把结构变化投影为模态空间的低维变换，而不是重新生成完整气动模型。”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：One of the important aspects of aeroelastic tailoring is to assess aeroelastic characteristics such as divergence and flutter for composite wing in the subsonic, transonic and supersonic flight regimes.
  可迁移模板：One of the important aspects of aeroelastic tailoring is to assess aeroelastic characteristics such as divergence and flutter for composite wing in the subsonic, transonic and supersonic flight regimes.
- 原句：Therefore, it is particularly important to analyze and assess the transonic aeroelastic characteristics of aircraft.
  可迁移模板：Therefore, it is particularly important to analyze and assess the transonic aeroelastic characteristics of aircraft.
- 原句：Efficiency evaluation of the aeroelastic characteristics evaluation method Our objective is to propose a new approximate aeroelastic characteristics evaluation method which is suitable for transonic aeroelastic tailoring, so the computational efficiency is one of the most important criteria of the proposed method for assess the aeroelastic stability in aeroelastic tailoring process.
  可迁移模板：Efficiency evaluation of the aeroelastic characteristics evaluation method Our objective is to propose a new approximate aeroelastic characteristics evaluation method which is suitable for transonic aeroelastic tailoring, so the computational efficiency is one of the most important criteria of the proposed method for assess the aeroelastic stability in aeroelastic tailoring process.
#### Gap/转折句
- 原句：Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades.
  可迁移模板：Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades.
- 原句：However, these full order models (FOMs), including finite element analysis (FEA) and CFD, require large computer memories and have high computational cost, making these methods impractical for routine use.
  可迁移模板：However, these full order models (FOMs), including finite element analysis (METHOD) and METHOD, require large computer memories and have high computational cost, making these methods impractical for routine use.
- 原句：However, the majority of previous work is only adequate for a fixed flight condition and a given structural model, i.e. changes to flight conditions (Mach number, angle of attack, etc.) and structural parameters (mass, etc.) are excluded.
  可迁移模板：However, the majority of previous work is only adequate for a fixed flight condition and a given structural model, i.e. changes to flight conditions (Mach number, angle of attack, etc.) and structural parameters (mass, etc.) are excluded.
- 原句：However, few studies has considered the aeroelastic response for variations in the structural parameters within a ROM.
  可迁移模板：However, few studies has considered the aeroelastic response for variations in the structural parameters within a METHOD.
- 原句：However the computational cost of the proposed approximate aeroelastic characteristics evaluation method is only 16 h × 1 + 0.74 s × 1000 + 1.82 s × 20 × 1000 = 26.31 h about which is only little more than one day.
  可迁移模板：However the computational cost of the proposed METHOD is only Xh × X+ Xs × X+ Xs × X× X= Xh about which is only little more than one day.
#### 方法提出句
- 原句：To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method.
  可迁移模板：To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method.
- 原句：To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method.
  可迁移模板：To make progress in this direction, the work presents a rapid computational fluid dynamics based aeroelastic tool which is built around a reduced order model for the aerodynamics that is updated for any modification of the structure by using the structural dynamics reanalysis method.
- 原句：Marques et al. (Marques et al., 2017) presented an investigation on the aeroelastic tailoring of stiffened laminate composite panels in supersonic flow to maximize the flutter non-dimensional dynamic pressure.
  可迁移模板：Marques et al. (Marques et al., X) presented an investigation on the aeroelastic tailoring of stiffened laminate composite panels in supersonic flow to maximize the flutter non-dimensional dynamic pressure.
- 原句：All these examples call for the development of an accurate and efficient approach to assess the aeroelastic characteristics (Cesnik et al., 1996).
  可迁移模板：All these examples call for the development of an accurate and efficient approach to assess the aeroelastic characteristics (Cesnik et al., X).
- 原句：For accurate aeroelastic predictions, a high-fidelity fluid model is highly needed.
  可迁移模板：For accurate aeroelastic predictions, a high-fidelity fluid model is highly needed.
#### 结果呈现句
- 原句：The aeroelastic tailoring tool is demonstrated in transonic flow for the AGARD 445.6 wing, suitably modified with composite materials.
  可迁移模板：The aeroelastic tailoring tool is demonstrated in transonic flow for the METHOD Xwing, suitably modified with composite materials.
- 原句：The aeroelastic tailoring tool is demonstrated in transonic flow for the AGARD 445.6 wing, suitably modified with composite materials.
  可迁移模板：The aeroelastic tailoring tool is demonstrated in transonic flow for the METHOD Xwing, suitably modified with composite materials.
- 原句：Sherrer et al. (Sherrer et al., 1981) demonstrated that aeroelastic tailoring can be used to increase the divergence speed of a composite forward swept wing through low-speed wind tunnel tests.
  可迁移模板：Sherrer et al. (Sherrer et al., X) demonstrated that aeroelastic tailoring can be used to increase the divergence speed of a composite forward swept wing through low-speed wind tunnel tests.
- 原句：Guo (Guo, 2007) demonstrated aeroelastic tailoring to significantly reduce the weight of aircraft structures and, at the same time, to increase up to 30% the flutter speed.
  可迁移模板：Guo (Guo, X) demonstrated aeroelastic tailoring to significantly reduce the weight of aircraft structures and, at the same time, to increase up to X the flutter speed.
- 原句：High-performance modern aircraft often cruises at transonic flow regime to achieve high performance (Rizk, 1981).
  可迁移模板：High-performance modern aircraft often cruises at transonic flow regime to achieve high performance (Rizk, X).
#### 贡献/增量句
- 原句：Current and future trends in the aerospace industry leverage on the potential benefits provided by lightweight materials that can be tailored to realize desired mechanical characteristics when loaded.
  可迁移模板：Current and future trends in the aerospace industry leverage on the potential benefits provided by lightweight materials that can be tailored to realize desired mechanical characteristics when loaded.
- 原句：In particular, the concept of aeroelastic tailoring using the directional stiffness properties of composite materials offers great potential for designers to improve aeroelastic performance.
  可迁移模板：In particular, the concept of aeroelastic tailoring using the directional stiffness properties of composite materials offers great potential for designers to improve aeroelastic performance.
- 原句：Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades.
  可迁移模板：Aeroelastic tailoring has been applied to improve aeroelastic characteristics in the aircraft structural design process over the past few decades.
- 原句：In computational fluid analysis, linear potential flow theory provides a low-cost and high efficiency way for subsonic and supersonic aeroelastic stability analysis.
  可迁移模板：In computational fluid analysis, linear potential flow theory provides a low-cost and high efficiency way for subsonic and supersonic aeroelastic stability analysis.
- 原句：It indicates again that the approximate aeroelastic characteristics evaluation method has good accuracy for aeroelastic response prediction of the improved AGARD 445.6 wing in a very large range of composite structural parameter variation, without reconstructing a new set of POD/ROMs basis corresponding to the new structural model.
  可迁移模板：It indicates again that the approximate aeroelastic characteristics evaluation method has good accuracy for aeroelastic response prediction of the improved METHOD Xwing in a very large range of composite structural parameter variation, without reconstructing a new set of METHOD/ROMs basis corresponding to the new structural model.
#### 限制/边界句
- 原句：Current and future trends in the aerospace industry leverage on the potential benefits provided by lightweight materials that can be tailored to realize desired mechanical characteristics when loaded.
  可迁移模板：Current and future trends in the aerospace industry leverage on the potential benefits provided by lightweight materials that can be tailored to realize desired mechanical characteristics when loaded.
- 原句：System identification and proper orthogonal decomposition (POD) are the two most commonly used ROMs for nonlinear aeroelastic analysis.
  可迁移模板：System identification and proper orthogonal decomposition (METHOD) are the two most commonly used ROMs for nonlinear aeroelastic analysis.
- 原句：However, the majority of previous work is only adequate for a fixed flight condition and a given structural model, i.e. changes to flight conditions (Mach number, angle of attack, etc.) and structural parameters (mass, etc.) are excluded.
  可迁移模板：However, the majority of previous work is only adequate for a fixed flight condition and a given structural model, i.e. changes to flight conditions (Mach number, angle of attack, etc.) and structural parameters (mass, etc.) are excluded.
- 原句：For every change of the composite structural model, both structural modeshapes and associated frequencies and the ROM around the new equilibrium position should be regenerated, and each of these regeneration cycles takes a considerable time, which jeopardize the computational efficiency.
  可迁移模板：For every change of the composite structural model, both structural modeshapes and associated frequencies and the METHOD around the new equilibrium position should be regenerated, and each of these regeneration cycles takes a considerable time, which jeopardize the computational efficiency.
- 原句：It should be note Parameter Flutter speed (m/s) Error (%) Direct method Approximate method Model A 208 209 0.481 Model B 249.5 245 1.804 Model C 203 207 1.970 that the flutter speed of Model A and C are very close.
  可迁移模板：It should be note Parameter Flutter speed (m/s) Error (%) Direct method Approximate method Model A XXXModel B XXXModel C XXXthat the flutter speed of Model A and C are very close.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略是“分领域建立合法性”。气动弹性剪裁部分用于说明应用需求；CFD ROM 部分用于说明降阶建模已成熟但有边界；结构动力学重分析部分用于引入可解决结构变化的工具。作者没有堆砌文献，而是让每组文献都服务于 gap 的一个环节。

值得注意的是，文献不是被用来证明“没人做过一切”，而是证明“已有方法分别解决了两个子问题，但还没有很好地组合到剪裁优化评估中”。这种引用方式对工程方法论文很稳妥：避免绝对化 novelty，同时突出集成价值。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：0
- Introduction 引文簇数量估计：0
- References 条目数：101
- 可识别年份条目数：57
- 2021 年及以后文献数：0
- 2010 年前经典文献数：29
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Composite Structures(2)；Journal of Fluids and Structures(1)
- 引文簇样例：未识别

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 2001. Fast exact linear and non-linear structural reanalysis and the Sherman–Morrison–Woodbury formulas.
Internat. J. Numer. Methods Engrg. 50, 1587–
- 1606. Alyanak, E.J., Pendleton, E.,
- 2017. Aeroelastic tailoring and active aeroelastic wing impact on a lambda wing configuration. J. Aircr. 54, 11–
- 19. Amsallem, D., Farhat, C., Lieu, T.,
- 2007. Aeroelastic analysis of F-16 and F −18/A configurations using adapted CFD-based reduced-order models. AIAA Pap.
2364, 23–
- 26. Bekemeyer, P., Timme, S.,
- 2017. Reduced Order Transonic Aeroelastic Gust Response Simulation of Large Aircraft. In: 35th AIAA Applied Aerodynamics
Conference, p.
- 4361. Beliveau, J.-G., Cogan, S., Lallement, G., Ayer, F.,
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 适用范围风险：方法依赖基准模态空间和结构变化相对温和。若铺层变化导致模态顺序交换、局部模态出现或气动非线性增强，`Z` 变换可能不足。
2. 质量矩阵假设风险：文中剪裁算例基本假设质量不变或变化可忽略，但真实铺层厚度、材料替换可能改变质量分布。
3. 气动模型风险：Euler/线性化 ROM 对粘性分离、激波强非线性和大幅响应的覆盖有限。
4. 验证范围风险：主要验证集中在 AGARD 445.6 和三种人为改型，尚缺真实优化过程中的大量随机结构样本。
5. 优化闭环风险：题目强调 tailoring，但文中展示的是评估方法，未真正运行完整 aeroelastic tailoring optimization。

## 17. 可复用资产

可复用问题表述：

- “在多次结构修改场景中，降阶模型的主要瓶颈不再是单次响应求解，而是模型重构本身。”
- “将高成本模型从优化内环移出，是使高保真方法进入工程优化的关键。”

可复用方法框架：

1. 为基准构型构造高保真 ROM。
2. 用低成本重分析方法预测修改构型的关键结构特征。
3. 构造基准与修改构型之间的低维变换。
4. 通过变换复用基准 ROM。
5. 用直接高保真或直接 ROM 对少量代表性构型验证精度。
6. 用大量候选估算展示效率收益。

可复用验证指标：

- natural frequency error
- MAC value
- generalized aerodynamic force history
- generalized displacement response
- flutter speed error
- CPU time / construction time / repeated-analysis time

## 18. 对我写论文的启发

这篇论文最大的启发是：工程计算论文可以把 novelty 放在“计算流程的可复用性”上，而不必每个底层模型都原创。只要能把应用痛点具体化，并用成本数量级差异证明必要性，集成型贡献也能很有力量。

第二个启发是验证顺序很重要。作者没有直接展示最终三种改型结果，而是先证明基准 CFD/ROM 能复现实验颤振边界。这个铺垫让后续近似更新结果更可信。

第三个启发是效率论文必须用场景化成本，而不是只报单次运行时间。Table 4 把 1000 个结构变化和 20 个动压点放进估算，立刻把方法价值从“快一点”提升为“优化可不可做”的层面。

## 19. 最终浓缩

本文提出一种面向复合材料机翼气动弹性剪裁的快速评估方法：先为基准结构建立 CFD-based POD/ROM，再用结构动力学重分析获得修改结构模态与基准模态之间的变换矩阵，从而快速更新广义气动力模型和气动弹性方程。AGARD 445.6 标准翼验证了基准模型可信，三种复合材料改型验证了近似方法在频率、广义气动力、响应和颤振速度上的精度。文章最强的价值不在单一公式，而在把高保真 CFD ROM 的一次性建模成本转化为可复用资产，使大量剪裁候选方案的气动弹性评估从数百天级缩短到约一天级。
