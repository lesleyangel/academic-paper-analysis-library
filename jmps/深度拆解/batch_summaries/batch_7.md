# Batch 7 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/A-chemo-mechanical-model-coupling-damage-and-mech_2026_Journal-of-the-Mechan.md`
- `jmps/深度拆解/papers/Active-filament-dynamics-model-for-the-locomot_2026_Journal-of-the-Mechanics.md`
- `jmps/深度拆解/papers/Active-peridynamic-method-for-deformation--dama_2026_Journal-of-the-Mechanic.md`
- `jmps/深度拆解/papers/A-lightweight-compact-metastructure-for-simultaneous-_2026_Journal-of-the-Me.md`
- `jmps/深度拆解/papers/A-thermodynamic-framework-for-diffusive-shells-wi_2026_Journal-of-the-Mechan.md`
- `jmps/深度拆解/papers/A-unified-thermo-chemo-mechanical-framework-for-bul_2026_Journal-of-the-Mech.md`

## 本批论文的共同特征
本批 6 篇都不是单纯现象报告，而是把复杂耦合系统压缩为可计算框架。两篇以软材料/生物材料损伤为核心：mechanofluorescent elastomer 将链力、损伤和环开反应耦合；active peridynamics 将细胞界面键、catch-slip、本构断裂和生化反馈耦合。两篇以主动/多功能结构设计为核心：active filament 将线虫肌肉激活转译为 spontaneous curvature；PRHH 将声学耗散和力学承载做功能解耦。两篇是典型 JMPS 热力学理论：diffusive shell 做三维到中面降维，polymerization framework 做 stress-dependent kinetics 与 stress-free configuration evolution 的统一。

## 本批最值得学习的 5 个写法
1. 用“实验异常或工程冲突”制造模型必要性：循环荧光滞后、线虫频率-振幅适应、水下吸声与承载冲突、FP 拉伸熄灭。
2. 把复杂机制拆成状态变量：damage density、activated mechanophore concentration、CCIB damage/healing state、spontaneous curvature、chemical potential、transformation deformation。
3. 先建立一般框架，再做 reduced/specialized problem：球壳闭式解、一维窄反应区、单轴/孔洞/裂纹验证。
4. 用参数研究或相图把公式变成物理直觉：reaction rates、Flory parameters、rubber lining、heat loss/loading、active strain modes。
5. 在强 claim 后主动给边界：图像需核查、线性黏弹性/均匀化学势/一维近似/二维单层模型/缺原型实验等。

## 本批最常见的审稿风险
- 模型参数可识别性不足，尤其是 mechanophore kinetics、APD 生化参数、DNN/NSGA 目标权重、polymerization kinetic relation。
- 图像或曲线验证可能偏视觉一致，缺少误差指标、色标统一、统计显著性或真实原型实验。
- 简化假设决定适用边界：uniform chemical potential、single material point per cell、linear viscoelastic rubber、一维 narrow reaction zone、prescribed/optimized active curvature。
- 从计算演示外推到工程/生物应用时容易过强，需用 “potential / provides a framework / suggests” 控制语气。

## 可沉淀到 JMPS 写作模板的规律
- Introduction 可采用“应用/现象重要性 -> 前人分流派 -> 每类不足 -> 本文统一框架”的四段式。
- Method 可采用“物理对象 -> 状态变量 -> 守恒/热力学限制 -> 演化律 -> 输出 observable”的顺序。
- Results 可采用“基线验证 -> 参数解释 -> 核心预测 -> 复杂场景外推 -> 局限”的顺序。
- Discussion/Conclusion 最好回到机制词，而不是只复述性能：damage-fluorescence coupling、active strain-curvature mapping、functional decoupling、mid-surface reduction、generalized Zeldovich criterion。

## 需要后续人工图像核查的内容
- Mechanofluorescent elastomer：Fig. 19-22 荧光图像的色标、曝光、裂尖/孔边局部一致性。
- Active filament：Fig. 1 统计误差、Fig. 4-7 导航轨迹和壁面接触/几何尺度。
- Active peridynamics：Fig. 8-10 实验/模拟裂纹、dorsal closure 和病变皮肤曲率的定量一致性。
- PRHH metastructure：Fig. 5-7 吸声峰与耗散云图，Fig. 17-22 DNN/Pareto/benchmark 条件统一性。
- Diffusive shell：Fig. 10-13 参数曲线不连续点、Fig. 17 扩散/化学势图、极限退化曲线。
- Unified polymerization：Fig. 2-4 regime、phase diagram、velocity quenching 与 force-response 对照。

