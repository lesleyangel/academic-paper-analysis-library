# Batch 14 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Torque-hyperuniformity-in-frictional-granula_2026_Journal-of-the-Mechanics-a.md`
- `jmps/深度拆解/papers/Twist-angle-dependence-of-the-out-of-plane_2026_Journal-of-the-Mechanics-and.md`
- `jmps/深度拆解/papers/Unraveling-microstructure-evolution-and-constitutive-beh_2026_Journal-of-the.md`

## 本批论文的共同特征
本批三篇都是典型 JMPS “机制闭环”论文，但入口不同。颗粒论文从理论必要条件出发，用实验确认 torque fluctuation hyperuniformity 的鲁棒性；MoS2 论文从直接测量难题出发，用 CR-AFM 零力点测量和 LJ 接触模型反演层间垂向刚度；AISI 9310 论文从声塑性机制争议出发，用实验、MD、NEB 和本构模型连接微结构演化与流动应力。

共同写法是：不满足于报告曲线，而是把现象压缩成一个可检验的内部变量或机制约束。第一篇的内部约束是每颗粒净 torque 为零导致边界贡献；第二篇的机制变量是 moiré stacking pattern、surface corrugation 和 effective local interfacial stiffness；第三篇的内部变量是 dislocation density、activation energy 和 acoustic stress/superposition。

## 本批最值得学习的 5 个写法
1. 把 gap 写成“理论/间接证据已存在，但真实直接验证不足”。颗粒论文验证理论条件，MoS2 论文补直接机械测量，AISI 论文补动态位错机制。
2. 用双重或三重证据证明强 claim：颗粒论文用 variance scaling + S(k)；MoS2 论文用 AFM + contact theory + MD；AISI 论文用实验曲线 + EBSD/SEM + MD/NEB + 本构。
3. 主动限定物理量：MoS2 的 Emm 是 supported TBLM 的 effective local stiffness，颗粒论文对剪切态各向同性失效保持谨慎，AISI 论文承认本构未包含 dislocation distribution 和 texture saturation。
4. 图表顺序服务论证链：先装置/定义，再核心趋势，再机制图，最后验证模型或外推。
5. Discussion 不只是重复结果，而是化解疑问：颗粒论文解释为什么 torque variance 是边界标度；MoS2 论文解释为什么与 interlayer shearing angle-independence 不矛盾；AISI 论文解释应力叠加为何不足以解释 residual softening。

## 本批最常见的审稿风险
- 外推风险：二维颗粒到三维摩擦物质、局部 TBLM stiffness 到 bulk C33、纳米晶铁 MD 到 AISI 9310 钢真实组织。
- 图像依赖：三篇都需回 PDF 核查关键图，尤其结构因子小 k、AFM/MD regime 图、EBSD/位错路径/断口图。
- 模型参数风险：MoS2 接触模型常数和 tip 校准、AISI 本构多参数拟合、颗粒力反演误差传播。
- claim 强度风险：direct evidence、extremely sensitive、accurately predict 等词都需要与证据范围匹配。
- 替代机制风险：颗粒中的有限尺寸/边界，MoS2 中污染和 tip contact，AISI 中温升/损伤/复杂合金相结构。

## 可沉淀到 JMPS 写作模板的规律
- 选题入口：`已有理论/间接观测/工艺现象 -> 关键机制变量尚未被直接验证或统一建模 -> 本文提供可测量/可计算闭环。`
- gap 表达：`A theoretical requirement does not guarantee that real systems satisfy it.` / `Indirect observables suggest X, but direct mechanical measurement of Y remains challenging.` / `Macroscopic curves alone cannot discern the underlying mechanism.`
- 方法表达：`We combine [direct measurement] with [physics-based model] and [simulation] to connect [local mechanism] with [macroscopic response].`
- 结果表达：`The response is controlled not only by [obvious variable], but also by [hidden structural/mechanistic variable].`
- 机制表达：`The robustness/anomaly can be traced to [local constraint or microstructural evolution], which changes [intermediate quantity] and thereby [global response].`
- 边界表达：`This quantity should be interpreted as [effective/local/in-range property], rather than [overgeneralized property].`

## 需要后续人工图像核查的内容
- 颗粒 torque hyperuniformity：Fig. 3-8 的方差斜率、S(k) 小 k 趋势、剪切下二维结构因子各向异性、Fig. 9 边界贡献示意。
- MoS2 垂向弹性：Fig. 1 样品清洁和 SHG、Fig. 2-3 CR-AFM 曲线与 mapping、Fig. 4 Emm-angle 散点和 regime 边界、Fig. 5 MD surface corrugation 与 modulus 对比。
- AISI 9310 UVAT：Fig. 3-4 应力降低曲线、Fig. 5-9 EBSD/KAM/IPF/Schmid factor、Fig. 10 断口形貌、Fig. 16/20 位错路径、Fig. 17-19 NEB 能垒、Fig. 27-28 本构拟合。

## 本批可复用句型骨架
- `The observed [macroscopic behavior] raises the question of whether it is specific to [idealized system] or persists under [broader conditions].`
- `To turn this theoretical condition into an experimentally testable quantity, we measure [observable A] and [observable B].`
- `This anomalous regime cannot be explained by [single-variable theory], indicating the role of [structural factor].`
- `The residual response after removing [external field] indicates that [internal variable] has been modified.`
- `The remaining discrepancy likely arises because [missing microstructural factor] is not explicitly included in the model.`
