# Batch 10 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Enhanced-Poynting-effect-in-torsion-of-a-polyd_2026_Journal-of-the-Mechanics.md`（约 13796 字符）
- `jmps/深度拆解/papers/Evolving-particle-shape-dispersion-in-crushable-g_2026_Journal-of-the-Mechan.md`（约 14228 字符）
- `jmps/深度拆解/papers/Finite-deformation-theory-for-growth-inspired-co_2026_Journal-of-the-Mechani.md`（约 14163 字符）
- `jmps/深度拆解/papers/Fluid-mediated-process-zone-coalescence-drives_2026_Journal-of-the-Mechanics.md`（约 13847 字符）
- `jmps/深度拆解/papers/Frequency-domain-Bayesian-inference-for-identifying-_2026_Journal-of-the-Mec.md`（约 14092 字符）
- `jmps/深度拆解/papers/Hamiltonian-simulation-of-elastodynamics-on-a-q_2026_Journal-of-the-Mechanic.md`（约 14606 字符）


## 本批论文的共同特征
本批 6 篇覆盖实验机制、连续介质本构、有限变形几何设计、贝叶斯反问题和量子计算映射。共同点是都把复杂现象压缩为少数可追踪变量：应力比、形状分布指数、QC dilatation/areal stretch、process-zone coalescence、DCT 低频系数、能量范数。JMPS 的味道不在“题材新”，而在每篇都努力把新题材变成可推导、可测量、可对照、可限定的力学命题。

## 本批最值得学习的 5 个写法
1. 先排除直觉解释，再提出真正机制：LCE 论文用简单剪切不增强来凸显扭转几何的重要性。
2. 把平均变量升级为分布变量：颗粒破碎论文用 shape dispersion 和 attractor 距离重构 CBM。
3. 用双不变量组织复杂设计：贴合理论用 K 与 A 管几何，用相图管应力可靠性。
4. 用多观测通道锁定机制：流体裂纹论文把轨迹、压力、速度、荧光和 DIC 同步使用。
5. 把两个瓶颈对应两个技术模块：频域贝叶斯用 DCT 解决维度，用可微分编程解决梯度；量子弹性动力学用能量守恒解决 Hermitian 映射。

## 本批最常见的审稿风险
- 外推过宽：实验类比、理想几何、低频表示、保守线性系统都不能无条件推广。
- 参数/图像依赖：颜色场、相图边界、误差带、硬件噪声和拟合曲线均需 PDF 图像核查。
- 最接近前人比较：每篇都依赖“比已有工作多补一个环节”，若漏引近邻工作会削弱 novelty。
- 复现信息：TXT 可支撑拆解，但代码、补充材料、图像细节和原始数据仍需进一步核查。

## 可沉淀到 JMPS 写作模板的规律
高水平 JMPS 论文常按“现象/需求 -> 已有框架 -> 具体缺口 -> 新变量或新映射 -> 基线对照 -> 多图验证 -> 机制解释 -> 边界限制”推进。最强的图表不是最复杂的图，而是能把一个 claim 固定住的图。最稳的贡献不是“我们首次提出”，而是“我们把此前分散的对象、变量、证据和边界闭合起来”。

## 需要后续人工图像核查的内容
- LCE：应力比曲线、误差带、内变量径向分布和理论-实验拟合。
- 颗粒破碎：shape attractor 数据源标记、强度图谱颜色尺度、DEM/实验拟合。
- 贴合理论：graded-QC 曲线、增长场、界面牵引/膜张力相图边界。
- 流体裂纹：荧光染料 process zones 合并图像、DIC 应变场、轨迹与压力同步点。
- 频域贝叶斯：误差图、标准差图、空间域比较条件和表格硬件环境。
- 量子弹性动力学：3D 场图、边界离散失败/成功对比、Trotter 误差、量子硬件误差条。
