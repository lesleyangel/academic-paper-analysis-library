# An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites

## 0. 读取说明

- 文本来源：`801/文本/txt/An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.txt`，PyMuPDF 抽取，22 页。
- 图表较多，且含图形摘要、随机孔隙 realizations、协方差/残差/相关矩阵图；本文拆解以文字和表格数值为主，所有图像空间形态均标注需要 PDF 图像复核。
- 这篇是 Batch 5 中方法论密度最高的一篇，重点不只是“孔隙降低刚度”，而是“怎样非侵入地把基体尺度随机孔隙传播到复合材料尺度刚度不确定性”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Inter-scale stiffness propagation method with stochastic porosity, 3 Matrix-scale RVE model of stochastic pores, 4 Statistical features and modeling of porosity field, 5 Statistical feature of matrix-scale effective properties, 6 Composite-scale FE model with nonintrusive pores, 7 Results and discussions, 8 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：An inter-scale stiffness propagation method with nonintrusive modeling of stochastic porosity in unidirectional composites。
- 作者：Yu-Cheng Yang, Zi-Qian Wang, Jian-Jun Gou, Xiao-Bing Ma, Chun-Lin Gong。
- 期刊：Computer Methods in Applied Mechanics and Engineering，452，2026，118720。
- 领域：复合材料多尺度力学、随机孔隙、RVE 均匀化、不确定性量化、非侵入式随机场建模。
- 论文类型：理论/方法建模 + 数值验证。
- 研究对象：UD 纤维增强复合材料中基体孔隙引起的刚度不确定性。
- 主要方法：Boolean germ-grain 孔隙模型、Poisson 点过程、截断 Gaussian 半径、Matérn 型协方差、FE 均匀化、功率律方差-体积标度、条件 Gaussian 映射、两阶段 Monte Carlo、非侵入式 FE 属性赋值。

## 2. 摘要与核心信息提取

本文的中心命题是：显式在复合材料尺度建模随机孔隙会导致不可承受的计算成本；如果先在基体尺度建立孔隙统计、孔隙-刚度联合分布和体积平均标度，再把统计一致的孔隙/刚度场非侵入地赋给复合材料尺度 FE 网格，就能高效传播孔隙导致的刚度不确定性。

摘要的核心信息有四层：孔隙是刚度不确定性源；显式建模太贵；局部体积效应决定量化精度；本文用 Poisson 球孔隙、Matérn 协方差、方差随体积衰减、负相关刚度-孔隙关系和 Monte Carlo 传播完成闭环。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-inter-scale-stiffness-propagation-method-with-_2026_Computer-Methods-in-A.md`。

中文译文：

> 文章信息
>
> 摘要
>
> 孔隙率是纤维增强复合材料中刚度不确定性的主要来源。然而，在复合尺度上使用规定的几何形状对孔隙进行显式建模会导致不确定性量化的计算成本过高。本研究提出了一种将矩阵尺度随机孔隙率与单向纤维增强（UD）复合材料的刚度不确定性联系起来的尺度间刚度传播方法。在这种非侵入式孔隙率建模中，局部体积效应强烈影响量化精度。基质中的孔隙被建模为通过泊松点过程分布的球体。它们的半径遵循截断高斯定律，导致孔隙率场的协方差遵循与局部体积无关的马特恩型形式。孔隙率方差随着体积尺寸的增加而衰减，归因于局部体积
>
> * 通讯作者。电子邮箱地址：jj.gou@nwpu.edu.cn（J.-J. Gou）。 https://doi.org/10.1016/j.cma.2025.118720 2025 年 10 月 28 日收到； 2025 年 12 月 15 日收到修订版； 2025 年 12 月 29 日接受
>
> 2026 年 1 月 6 日在线提供 0045-7825/© 2025 Elsevier B.V. 保留所有权利，包括文本和数据挖掘、人工智能培训和类似技术的权利。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自制造缺陷和结构可靠性之间的尺度错位。孔隙在基体尺度产生，但设计者关心的是复合材料尺度的等效刚度分布；直接把每个孔隙几何显式塞进大尺度 FE 会导致网格数量和 Monte Carlo 成本爆炸。

作者将问题收束为：在不修改确定性 FE 求解器的前提下，如何让孔隙空间相关、体积平均效应、孔隙-刚度耦合和多刚度分量相关性都能被保留。这个问题比单纯“孔隙率影响模量”更高级，因为它关注统计结构传播，而不是单个均值退化。

价值在于可靠性设计：对于实际生产中只能有限表征孔隙分布的 UD 复合材料，方法可以在有限体积、有限数据、有限网格成本下给出不确定性输入。

## 4. 领域位置与文献版图

Introduction 的文献地图组织得很完整：

- 制造缺陷背景：纤维排布不规则、基体孔隙会影响刚度、强度和损伤。
- RVE/SVE 尺寸效应：小体积有显著样本波动，大体积有 self-averaging，方差常呈反体积或功率律衰减。
- 分布/矩阵距离验证：Frobenius、谱范数、Bhattacharyya distance、KL divergence 用来验证联合统计结构。
- 随机场与空间相关：两点协方差、Karhunen-Loève 和谱方法用于随机场离散。
- micro-CT/image-based 方法：形貌真实但成本高、样本有限且带来 epistemic uncertainty。

本文的位置是“把 stochastic geometry、FE homogenization 和 nonintrusive random field assignment 接起来”。它不是单一孔隙模拟，也不是单纯 RVE 尺寸收敛，而是多尺度统计传播框架。

## 5. Gap 制造机制

gap 是由三重不足构成的：

1. 显式孔隙建模在复合材料尺度不可扩展，尤其 Monte Carlo 下成本过高。
2. 仅用平均孔隙率不能捕捉空间相关和局部体积平均导致的方差变化。
3. 已有随机缺陷均匀化多关注界面不规则或单尺度性质，缺少从基体孔隙到复合材料尺度刚度场的非侵入传播。

这个 gap 被大量引用支撑，并且和工程约束紧密绑定：实际制造不能对每个构件做高分辨 CT，也不能把超大 RVE 显式网格化。因此 gap 具有计算力和数据可得性双重现实基础。

## 6. 创新性判断

- 真实创新 1：用 Boolean 球孔隙模型推导孔隙局部平均的空间-体积协方差，并用 Matérn 核拟合。
- 真实创新 2：将刚度方差随 RVE 体积的功率律衰减与孔隙-刚度强负相关结合为 volume-adaptive joint model。
- 真实创新 3：非侵入地在复合材料 FE 网格单元层面采样孔隙和条件刚度张量，不改求解器。
- 创新强度：强。贡献体现在模型链条完整性，而非某个孤立公式。
- 可能被挑战：球形孔隙和均匀 Poisson 假设较理想；UD 体系验证强，但对织物复合材料、非球形/连通孔隙、孔隙各向异性仍需扩展。

## 7. 论证链条复原

背景：孔隙导致微观缺陷和宏观刚度随机性。

困难：显式建模孔隙太贵；有限 RVE 下方差不能忽略。

方法链：Poisson 球孔隙生成 Y(x) -> 局部平均孔隙 ϕV(x) -> 两点协方差与 Matérn 体积核 -> FE 均匀化得到 X(V) 与 ϕV 的联合统计 -> 功率律描述方差随体积衰减 -> 条件 Gaussian 映射 P(Xe|ϕe, Ve) -> 在复合材料尺度 FE 中 Monte Carlo 赋值。

验证链：孔隙半径/体积分布 -> 协方差拟合残差 -> 矩阵尺度方差-体积功率律和 LOOV -> 相关矩阵 Frobenius/谱误差 -> BD/KL 分布距离 -> 网格独立性 -> 复合材料尺度随机 FE 演示。

结论链：孔隙统计可拟合，刚度-孔隙负相关稳定，非侵入传播在复合材料尺度保留 self-averaging。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Quantifying this inherent sto chasticity is therefore essential for reliable prediction and design of composite structures.
- 已有研究不足/GAP：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. These results demonstrate that, once propagated to the composite scale, the stochastic porosity-stiffness fields remain statistically consistent and naturally reproduce the expected self-averaging behavior across increasing RVE sizes. The variance of stiffness components decays with increasing averaging volume following a power-law form, whereas the stiffness-porosity correlation remains strongly negative and nearly volume-invariant over the scales investigated.
- 本文解决方式：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification. This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites. In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
- 学术或工程增量：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification. Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2]. These results demonstrate that, once propagated to the composite scale, the stochastic porosity-stiffness fields remain statistically consistent and naturally reproduce the expected self-averaging behavior across increasing RVE sizes.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

基体尺度孔隙用 Boolean model：孔中心服从强度为 λp 的 homogeneous Poisson point process，孔半径 Ri 服从截断正态分布，孔隙相为球并集 B(ω)，指示场 Y(x,ω) 为 0/1。局部孔隙率是 ϕV(x,ω)=<Y>V。

统计层先给出平均孔隙率、two-point function S2(r)、indicator covariance CY(r)，再通过局部体积双重积分得到 Var[ϕV] 和 Cϕ(r;V1,V2)。作者把它拟合为 Matérn ν=3/2 核，并显式引入 V^-α 的体积衰减。

力学层通过 matrix-scale RVE 的 FE homogenization 得到有效属性 X(V)，发现均值近似体积不变、方差按 Var[Xi(V)]=Bi|V|^-αi 衰减、刚度与孔隙率强负相关且近似体积不变。由此构建 stiffness-porosity joint Gaussian model。

复合材料尺度实现是非侵入式：对每个 matrix-phase 单元在单元体积上采样局部孔隙 ϕe，再按条件分布 P(Xe|ϕe,Ve) 采样刚度张量 Xe。纤维确定，孔隙只进入基体区域。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| Boolean 孔隙模型可产生可控孔隙统计 | 3/7.1 | Fig. 5 半径和体积分布符合截断 Gaussian 输入 | 中强 | 球孔隙假设理想化，需要真实 micro-CT 对比 |
| 孔隙协方差可由 Matérn 核准确拟合 | 4.3/7.1 | Fig. 7 Monte Carlo 协方差，Table 3 A=483.0、α=1.33、ρ=3.75 μm；Fig. 8 残差无系统趋势 | 强 | 图中残差细节需要 PDF 图像复核 |
| 刚度和孔隙方差随体积呈 self-averaging | 5.3/7.2 | Table 4 COV 随 RVE 变大明显下降；Table 5 αi=0.93-0.98，R2 多数 >0.99 | 强 | 只覆盖设定孔隙分布和四个 RVE 尺寸 |
| 刚度-孔隙相关强负且体积近似不变 | 5.4/7.2 | Fig. 11 刚度分量与 Φ 强负相关，变化约 3-5%；Poisson 比波动被解释为数值敏感 | 强 | Poisson 比处理需要谨慎 |
| 模型联合分布与经验分布一致 | 7.2 | Frobenius/谱误差多在几个百分点，BD <0.2，KL 小 | 强 | Gaussian 假设可能掩盖尾部风险 |
| 非侵入传播在复合材料尺度保留体积标度 | 7.4 | Table 10 COV 从 RVEb3 到 RVEb1 降低；Table 11 α≈0.96-1.02，R2=0.99-1.00 | 强 | 复合材料尺度相关变弱，机制解释需更多材料体系验证 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 展示不同 λp/半径分布下孔隙 realizations | 随机几何生成器可控 | 孔隙密度和大孔概率随参数变化 | 需要 PDF 图像复核 |
| Eq. (1)-(6) | 定义 Poisson 孔中心、半径、孔隙相、局部平均孔隙 | 孔隙场有明确概率结构 | 从几何到 ϕV 的基础 | 文本足够 |
| Eq. (7)-(14) | 推导平均孔隙率、two-point covariance、variance-volume scaling | 方差随体积平均衰减 | Var[ϕV]≈Aϕ|V|^-αϕ | 文本足够 |
| Fig. 7/8 + Table 3 | 验证 Matérn 协方差模型 | 协方差模型准确 | α=1.33，ρ=3.75 μm，残差小 | 需要 PDF 图像复核 |
| Table 4/5 | 矩阵尺度统计和功率律拟合 | 刚度方差随体积下降 | COV 显著下降，α 近 1 | 文本足够 |
| Fig. 11/12/13 + Table 6/7 | 验证相关矩阵和联合分布 | 相关结构体积不变 | F-err/λ-err 几个百分点，BD/KL 小 | 需要 PDF 图像复核 |
| Table 8/9 | 排除网格离散影响 | 误差不是网格造成 | 5154 elements 已足够，E[Φ] 网格无关 | 文本足够 |
| Table 10/11 + Fig. 14/15 | 复合材料尺度演示 | 非侵入传播有效 | α≈1，负相关保留但幅值减弱 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节：1 Introduction；2 Inter-scale stiffness propagation method with stochastic porosity；3 Matrix-scale RVE model of stochastic pores；4 Statistical features and modeling of porosity field；5 Statistical feature of matrix-scale effective properties；6 Composite-scale FE model with nonintrusive pores；7 Results and discussions；8 Conclusion。

文章结构是“先总览流程，再分模块建模，再数值验证”的工程数学论文结构。第 2 章像路线图，把后文 Section 3-6 串成三步：空间统计和体积标度、孔隙-力学耦合、非侵入网格采样。第 7 章按方法模块逐一验证，避免读者只看到最终演示而不知道每个中间假设是否成立。

标题命名偏精确、模块化，适合 CMAE 风格；缺点是标题较长且抽象，读者需要先理解符号体系。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.2: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Inter-scale stiffness propagation method with stochastic porosity（方法/模型/算法）
- L2 p.3: 3 Matrix-scale RVE model of stochastic pores（方法/模型/算法）
- L2 p.5: 4 Statistical features and modeling of porosity field（方法/模型/算法）
  - L3 p.5: 4.1 Statistical features of pores field（对象/模块/过渡章节）
  - L3 p.5: 4.2 Statistical features of porosity field（对象/模块/过渡章节）
  - L3 p.7: 4.3 Statistical modeling of porosity field covariance（方法/模型/算法）
- L2 p.7: 5 Statistical feature of matrix-scale effective properties（对象/模块/过渡章节）
  - L3 p.7: 5.1 Stiffness and porosity sampling of RVE size（对象/模块/过渡章节）
  - L3 p.8: 5.2 FE-based homogenization procedure（对象/模块/过渡章节）
  - L3 p.8: 5.3 Stiffness and porosity variance decay with RVE size（对象/模块/过渡章节）
  - L3 p.9: 5.4 Joint distribution modeling of stiffness-porosity（方法/模型/算法）
- L2 p.9: 6 Composite-scale FE model with nonintrusive pores（方法/模型/算法）
  - L3 p.9: 6.1 Nonintrusive mesh-level sampling in composite scale（对象/模块/过渡章节）
  - L3 p.10: 6.2 Computational efficiency（对象/模块/过渡章节）
- L2 p.11: 7 Results and discussions（结果/验证/讨论）
  - L3 p.12: 7.1 Statistical features of pore and porosity（对象/模块/过渡章节）
  - L3 p.12: 7.2 Joint distribution of stiffness-porosity（对象/模块/过渡章节）
  - L3 p.17: 7.3 Mesh independence and correlation discretization effects（对象/模块/过渡章节）
  - L3 p.18: 7.4 Stochastic FE demonstration（对象/模块/过渡章节）
- L2 p.19: 8 Conclusion（结论/贡献回收）
- L2 p.20: CRediT authorship contribution statement（尾部材料）
- L2 p.20: Declaration of competing interest（尾部材料）
- L2 p.20: Data availability（尾部材料）
- L2 p.20: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 2 | 2 | 背景定位/文献缺口 |
| 2 Inter-scale stiffness propagation method with stochastic porosity | 3 | 2 | 方法/模型/算法 |
| 3 Matrix-scale RVE model of stochastic pores | 3 | 2 | 方法/模型/算法 |
| 4 Statistical features and modeling of porosity field | 5 | 2 | 方法/模型/算法 |
| 4.1 Statistical features of pores field | 5 | 3 | 对象/模块/过渡章节 |
| 4.2 Statistical features of porosity field | 5 | 3 | 对象/模块/过渡章节 |
| 4.3 Statistical modeling of porosity field covariance | 7 | 3 | 方法/模型/算法 |
| 5 Statistical feature of matrix-scale effective properties | 7 | 2 | 对象/模块/过渡章节 |
| 5.1 Stiffness and porosity sampling of RVE size | 7 | 3 | 对象/模块/过渡章节 |
| 5.2 FE-based homogenization procedure | 8 | 3 | 对象/模块/过渡章节 |
| 5.3 Stiffness and porosity variance decay with RVE size | 8 | 3 | 对象/模块/过渡章节 |
| 5.4 Joint distribution modeling of stiffness-porosity | 9 | 3 | 方法/模型/算法 |
| 6 Composite-scale FE model with nonintrusive pores | 9 | 2 | 方法/模型/算法 |
| 6.1 Nonintrusive mesh-level sampling in composite scale | 9 | 3 | 对象/模块/过渡章节 |
| 6.2 Computational efficiency | 10 | 3 | 对象/模块/过渡章节 |
| 7 Results and discussions | 11 | 2 | 结果/验证/讨论 |
| 7.1 Statistical features of pore and porosity | 12 | 3 | 对象/模块/过渡章节 |
| 7.2 Joint distribution of stiffness-porosity | 12 | 3 | 对象/模块/过渡章节 |
| 7.3 Mesh independence and correlation discretization effects | 17 | 3 | 对象/模块/过渡章节 |
| 7.4 Stochastic FE demonstration | 18 | 3 | 对象/模块/过渡章节 |
| 8 Conclusion | 19 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 20 | 2 | 尾部材料 |
| Declaration of competing interest | 20 | 2 | 尾部材料 |
| Data availability | 20 | 2 | 尾部材料 |
| References | 20 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 段落很像系统综述：每段引入一个挑战或工具，再说明它如何连接到本文。方法段落采用“定义符号 -> 给公式 -> 解释物理意义 -> 说明后续如何使用”的节奏。结果段落高度标准化：先说明图表目的，再描述数值趋势，随后给出方法论含义。

特别可学的是第 7 章每一小节都不是孤立展示图，而是回应前文一个建模假设：孔隙统计、方差标度、相关稳定、网格独立、复合尺度保真。这样读者会感觉整条模型链都被逐段加固。

## 13. 文笔画像与语言习惯

语言是高密度、公式驱动、验证导向。高频词包括 porosity、stiffness、covariance、volume、stochastic、correlation、RVE、Monte Carlo。常用动词是 represents、defines、captures、validates、confirms、enables。作者偏好名词化，如 variance-volume scaling、cross-property structure、volume-adaptive joint model。

语气强但不夸张：claim 通常由 “indicating/confirming/demonstrating” 连接证据；限制语包括 “nearly”“essentially”“over the scales investigated”。时态上，方法定义用现在时，数值结果用过去时/现在时混合，结论用 presents/offers/enables。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：56052
- 高频词：porosity(85)；stiffness(57)；model(49)；covariance(48)；stochastic(47)；volume(37)；pore(37)；local(34)；correlation(34)；matrix(31)；field(31)；spatial(29)；composite-scale(28)；rve(28)；pores(27)；monte(27)；carlo(27)；elements(26)；volumes(25)；statistics(25)
- 高频名词化/学术名词：porosity(85)；stiffness(57)；covariance(48)；correlation(34)；statistics(25)；section(23)；variance(21)；homogenization(20)；element(18)；structure(17)；realization(16)；distribution(14)；distance(14)；variability(13)；propagation(12)
- 高频学术动词：provide(9)；evaluated(5)；developed(4)；constructed(3)；identified(3)；evaluate(3)；demonstrate(3)；estimated(3)；compared(2)；validate(2)；reveal(2)；presented(2)；analyzed(2)；predicted(2)；indicate(2)
- 高频形容词：stochastic(47)；local(34)；spatial(29)；effective(21)；element(18)；consistent(17)；nonintrusive(16)；spherical(13)；statistical(12)；independent(12)；volume-invariant(11)；normal(11)；geometric(10)；conditional(9)；empirical(8)
- 高频副词：nearly(9)；statistically(9)；directly(8)；primarily(6)；strongly(5)；computationally(4)；empirically(4)；independently(4)；uniformly(4)；approximately(4)；fully(4)；spatially(3)；accurately(3)；identically(3)；numerically(3)
- 高频二词短语：monte carlo(27)；porosity field(13)；stochastic porosity(11)；composite scale(11)；variance-volume scaling(11)；effective properties(9)；boolean model(7)；spatial coherence(7)；local porosity(7)；correlation matrix(7)；rve size(6)；boundary conditions(6)
- 高频三词短语：monte carlo realization(5)；local average porosity(4)；carlo realization produces(4)；realization produces porosity(4)；produces porosity field(4)；porosity field statistically(4)；field statistically consistent(4)；statistically consistent multivariate(4)；consistent multivariate stiffness(4)；multivariate stiffness field(4)；stiffness field preserving(4)；field preserving spatial(4)
- 被动语态估计：128；`we + 动作动词` 主动句估计：2
- 一般现在时线索：231；一般过去时线索：385；现在完成时线索：4；情态动词线索：22

分章节正文词频：

- 1 Introduction: stochastic(9)；stiffness(8)；matrix(7)；properties(7)；homogenization(6)；porosity(6)；model(6)；rve(6)
- 2 Inter-scale stiffness propagation method with stochastic porosity: porosity(11)；stiffness(7)；stochastic(5)；field(5)；model(5)；spatial(5)；section(4)；local(4)
- 3 Matrix-scale RVE model of stochastic pores: porosity(16)；pore(16)；stochastic(10)；field(10)；pores(9)；stiffness(9)；model(8)；spatial(7)
- 4 Statistical features and modeling of porosity field: covariance(19)；local(10)；porosity(9)；distance(9)；volumes(9)；volume(8)；function(7)；overlap(7)
- 5 Statistical feature of matrix-scale effective properties: stiffness(11)；rve(10)；porosity(7)；matrix(7)；volume(7)；correlation(7)；shear(7)；pore(6)
- 6 Composite-scale FE model with nonintrusive pores: porosity(10)；composite-scale(8)；model(8)；stiffness(8)；mesh(7)；correlation(6)；monte(6)；carlo(6)
- 7 Results and discussions: porosity(20)；mesh(16)；elements(15)；covariance(15)；stochastic(13)；statistics(10)；model(10)；correlation(10)
- 8 Conclusion: porosity(6)；composite-scale(5)；stochastic(5)；method(4)；uncertainty(4)；stiffness(4)；scale(3)；statistically(3)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 问题句式：Explicitly modeling X at the Y-scale leads to prohibitive computational cost.
- 方法总述：This study proposes an inter-scale method linking X to Y.
- 体积效应句式：The variance decreases with increasing averaging volume following a power-law form.
- 验证句式：The close clustering along the 1:1 line demonstrates predictive consistency.
- 谨慎结论：The correlation remains strongly negative and nearly volume-invariant over the scales investigated.
- 复用模板：先构建可控随机几何输入，再用高保真小尺度模型标定联合统计，最后非侵入地传播到大尺度 FE。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：When the domain is below a critical threshold, statistical volume elements (SVEs) exhibit significant sample-to-sample variability; studies on carbon-fiber systems have identified the approximate critical RVE size [5].
  可迁移模板：When the domain is below a critical threshold, statistical volume elements (SVEs) exhibit significant sample-to-sample variability; studies on carbon-fiber systems have identified the approximate critical METHOD size [X].
- 原句：Beyond variance-volume scaling, it is also important to assess whether the statistical structure of the homogenized properties is preserved across different volumes.
  可迁移模板：Beyond variance-volume scaling, it is also important to assess whether the statistical structure of the homogenized properties is preserved across different volumes.
#### Gap/转折句
- 原句：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
  可迁移模板：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
- 原句：In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibi tive, particularly for architectures lacking clear scale separation [18].
  可迁移模板：In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibi tive, particularly for architectures lacking clear scale separation [X].
- 原句：These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].
  可迁移模板：These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [X].
- 原句：These results demonstrate that, once propagated to the composite scale, the stochastic porosity-stiffness fields remain statistically consistent and naturally reproduce the expected self-averaging behavior across increasing RVE sizes.
  可迁移模板：These results demonstrate that, once propagated to the composite scale, the stochastic porosity-stiffness fields remain statistically consistent and naturally reproduce the expected self-averaging behavior across increasing METHOD sizes.
- 原句：The variance of stiffness components decays with increasing averaging volume following a power-law form, whereas the stiffness-porosity correlation remains strongly negative and nearly volume-invariant over the scales investigated.
  可迁移模板：The variance of stiffness components decays with increasing averaging volume following a power-law form, whereas the stiffness-porosity correlation remains strongly negative and nearly volume-invariant over the scales investigated.
#### 方法提出句
- 原句：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
  可迁移模板：However, explicitly modeling pores with prescribed geometry at the composite-scale leads to prohibitive computational cost for uncertainty quantification.
- 原句：This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (UD) composites.
  可迁移模板：This study proposes an inter-scale stiffness propagation method linking matrix-scale stochastic porosity to stiffness uncertainty of unidirec tional fiber-reinforced (METHOD) composites.
- 原句：In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
  可迁移模板：In such nonintrusive modeling of porosity, the local volume effect strongly influences the quantification accuracy.
- 原句：Pores in the matrix are modeled as spheres distributed by a Poisson point process.
  可迁移模板：Pores in the matrix are modeled as spheres distributed by a Poisson point process.
- 原句：The stiffnessporosity joint distribution is then constructed by the conditional Gaussian mapping method.
  可迁移模板：The stiffnessporosity joint distribution is then constructed by the conditional Gaussian mapping method.
#### 结果呈现句
- 原句：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
  可迁移模板：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
- 原句：Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [1,2].
  可迁移模板：Fiber-reinforced composites achieve high specific stiffness and strength by embedding stiff fibers in matrix; yet microstructural variability - irregular fiber packing and matrix porosity - almost inevitably arises during manufacturing [X,X].
- 原句：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
  可迁移模板：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [X].
- 原句：Entropy-based distances of this type have also proved useful beyond homogenization; for instance, recent reliability analyses of telecommunication skeletal structures have shown that BD offers an efficient and robust probabilistic measure compared with KL divergence and classical First-Order Reliability Method-type indices, further highlighting the relevance of such metrics in characterizing stochastic response surfaces [28].
  可迁移模板：Entropy-based distances of this type have also proved useful beyond homogenization; for instance, recent reliability analyses of telecommunication skeletal structures have shown that METHOD offers an efficient and robust probabilistic measure compared with METHOD divergence and classical First-Order Reliability Method-type indices, further highlighting the relevance of such metrics in characterizing stochastic response surfaces [X].
- 原句：These results confirm that the classical V-1 self-averaging law persists at the composite scale.
  可迁移模板：These results confirm that the classical V-Xself-averaging law persists at the composite scale.
#### 贡献/增量句
- 原句：The variance of matrix stiffness is found to decrease with growing local volume size, and its consistent negative correlation with porosity is thereby established.
  可迁移模板：The variance of matrix stiffness is found to decrease with growing local volume size, and its consistent negative correlation with porosity is thereby established.
- 原句：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
  可迁移模板：The results show that the nonintrusive modeling of stochastic porosity enables reliable stiffness propagation and efficient pore-induced uncertainty quantification.
- 原句：By introducing explicit spatial correlation and scale dependence, the proposed method enables stochastic propagation from the matrix scale to the composite scale and complements existing approaches in this area.
  可迁移模板：By introducing explicit spatial correlation and scale dependence, the proposed method enables stochastic propagation from the matrix scale to the composite scale and complements existing approaches in this area.
- 原句：Distribution-based metrics provide a complementary viewpoint: the Bhatta charyya distance (BD) characterizes the overlap between multivariate distributions, while the Kullback-Leibler divergence (KL) quantifies their information discrepancy [24–26].
  可迁移模板：Distribution-based metrics provide a complementary viewpoint: the Bhatta charyya distance (METHOD) characterizes the overlap between multivariate distributions, while the Kullback-Leibler divergence (METHOD) quantifies their information discrepancy [X–X].
- 原句：This confirms that the proposed nonintrusive method enables physically consistent and computationally feasible uncertainty propagation from matrix-scale porosity to composite-scale effective properties.
  可迁移模板：This confirms that the proposed METHOD enables physically consistent and computationally feasible uncertainty propagation from matrix-scale porosity to composite-scale effective properties.
#### 限制/边界句
- 原句：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [4].
  可迁移模板：In particular, pores that form in the matrix regions between fibers can further reduce stiffness; studies on short-glass-fiber thermoplastics with random orientations have shown that even modest increases in porosity may lead to appreciable decreases in the effective Young’s modulus [X].
- 原句：A high-fidelity RVE model of a porous composite may contain hundreds of millions of elements, making it impractical for routine analysis [19].
  可迁移模板：A high-fidelity METHOD model of a porous composite may contain hundreds of millions of elements, making it impractical for routine analysis [X].
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用密度高，尤其 Introduction。作者不是罗列“孔隙影响材料性能”，而是把文献按方法问题组织：缺陷影响、RVE 尺寸、距离度量、随机场、micro-CT、UD 均匀化。每组文献先承认已有价值，再指出本文补的环节。

引用姿态总体中性：对 micro-CT 是“真实但昂贵”，对随机场是“统计上有用但需要结合孔隙空间相关与体积效应”，对已有缺陷模型是“有启发但对象不同”。gap 和贡献连接自然，因为每类文献都留下一个未闭合接口。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：71
- Introduction 引文簇数量估计：15
- References 条目数：46
- 可识别年份条目数：70
- 2021 年及以后文献数：29
- 2010 年前经典文献数：4
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：[1,2], [3], [4], [5], [5,6], [18], [19], [18], [20,21], [22,23], [27], [28]

带引文的 gap/转折句样例：

- In practice, RVEs cannot be enlarged indefinitely because high-fidelity simulations of very large domains are computationally prohibi tive, particularly for architectures lacking clear scale separation [18].
- These constraints highlight the need for variance-aware modeling strategies that remain accurate at finite, feasible volumes rather than relying on asymptotically large RVEs [18].

References 解析样例（前 8 条）：

- 15. Correlation between stiffness components and porosity ρ(Xi, Φ) versus sampling volume V for the composite-scale RVEs (Fisher 95 % confidence bands). The negative correlations persist but with reduced magnitude relative to matrix-scale RVEs, consistent with load sharing and averaging effects in the composite.
Yu-Cheng Yang: Writing – original draft, Software, Resources, Formal analysis, Data curation, Conceptualization. Zi-Qian Wang: Visualization, Data curation. Jian-Jun Gou: Writing – review & editing, Validation, Conceptualization. Xiao-Bing Ma: Supervision. Chun-Lin Gong: Validation, Supervision.
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
- [1] M. Mehdikhani, I. Straumit, L. Gorbatikh, S.V. Lomov, Detailed characterization of voids in multidirectional carbon fiber/epoxy composite laminates using X-ray micro-computed tomography, Compos. A: Appl. Sci. Manuf. 125 (2019) 105532, https://doi.org/10.1016/j.compositesa.2019.105532.
- [2] S.H.R. Sanei, E.J. Barsotti, D. Leonhardt, R.S. FertigIII, Characterization, synthetic generation, and statistical equivalence of composite microstructures, J. Compos. Mater. 51 (2017) 1817–1829, https://doi.org/10.1177/0021998316662133.
- [3] M. Petrolo, A. Pagani, M. Trombini, E. Carrera, Voids effect on micromechanical response of elastoplastic fiber-reinforced polymer composites using 1D higherorder theories, Mech. Mater. 184 (2023) 104747, https://doi.org/10.1016/j.mechmat.2023.104747.
- [4] Porous materials reinforced with short fibers: unbiased full-field assessment of several homogenization strategies in elasticity: mechanics of Advanced Materials and Structures: Vol 29, No 20 - Get Access, (n.d.). https://www.tandfonline.com/doi/full/10.1080/15376494.2021.1880674 (accessed September 12, 2025).
- [5] S.P. Shah, M. Maiarù, Effect of manufacturing on the transverse response of polymer matrix composites, Polymers 13 (2021) 2491, https://doi.org/10.3390/ polym13152491.
- [6] T. Kanit, S. Forest, I. Galliet, V. Mounoury, D. Jeulin, Determination of the size of the representative volume element for random composites: statistical and numerical approach, Int. J. Solids. Struct. 40 (2003) 3647–3679, https://doi.org/10.1016/S0020-7683(03)00143-4.
- [7] D. Savvas, G. Stefanou, M. Papadrakakis, Determination of RVE size for random composites with local volume fraction variation, Comput. Methods Appl. Mech. Eng. 305 (2016) 340–358, https://doi.org/10.1016/j.cma.2016.03.002.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

- 孔隙形状风险：球形孔隙与 Poisson 独立假设可能不适用于 elongated、coalesced 或制造过程相关孔隙。
- 分布假设风险：条件 Gaussian 映射对尾部和非线性退化的表现需要验证。
- 实验校准不足：文中主要是数值建模，没有真实 CT/实验模量不确定性闭环验证。
- UD 泛化风险：织物、编织、层合板多尺度几何更复杂，非侵入赋值可能需要改造。
- 相关削弱解释：复合尺度负相关幅值从约 0.9 降至约 0.35-0.55，解释合理但可能需要更多机制分析。
- 文本复杂度：公式、符号和表格密集，读者理解成本高，摘要中的“nonintrusive modeling”需要更早给直觉图解。

## 17. 可复用资产

- 论证链资产：随机几何 -> 统计量 -> 均匀化 -> 联合分布 -> 非侵入 FE -> Monte Carlo 验证。
- 图表资产：分布直方图、协方差核、残差诊断、log-log 方差标度、leave-one-out parity plot、相关矩阵距离图、网格独立表。
- 方法资产：把复杂微结构显式建模转化为统计一致的单元属性场。
- 写作资产：每个中间模型都配一个诊断图/表，避免最终 demo 显得黑箱。
- 适用迁移：任何“微观随机缺陷 -> 宏观等效性质不确定性”的问题都可参考此结构。

## 18. 对我写论文的启发

如果论文要提出多尺度方法，不要只展示最终尺度结果。本文非常值得学习的是“逐级验证模型链”：先验证随机输入，再验证协方差，再验证体积标度，再验证联合分布，再验证网格独立，最后才做应用。这种结构能显著降低审稿人对复杂模型的防御心理。

另一个启发是：非侵入式方法必须强调“兼容现有确定性求解器”，这比单纯说“高效”更能打动工程计算期刊。

## 19. 最终浓缩

本文最值得学的是把孔隙几何显式建模的高成本问题转化为统计一致的非侵入刚度场传播问题。最强证据是：孔隙协方差、刚度方差标度、刚度-孔隙负相关和复合材料尺度 self-averaging 都通过表格/图示逐层验证。最大风险是孔隙形貌和 Gaussian 假设偏理想，后续需要真实 CT/实验数据闭环和更复杂复合材料结构验证。
