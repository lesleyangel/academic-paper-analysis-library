# Batch 12 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Mechanistic-origins-of-toughness-in-rando_2026_Journal-of-the-Mechanics-and-.md`
- `jmps/深度拆解/papers/Mechanobiological-morphomechanics-o_2026_Journal-of-the-Mechanics-and-Physic.md`
- `jmps/深度拆解/papers/Microporosity-as-key-driver-of-the-in-situ-prope_2026_Journal-of-the-Mechani.md`
- `jmps/深度拆解/papers/Non-Hermitian-dynamic-modeling-of-electrical-wi_2026_Journal-of-the-Mechanic.md`
- `jmps/深度拆解/papers/On-the-yielding-of-brittle-granular-materia_2026_Journal-of-the-Mechanics-an.md`
- `jmps/深度拆解/papers/Preface-to-the-65th-anniversary-issue-of-JMPS_2026_Journal-of-the-Mechanics-.md`

## 本批论文的共同特征
本批 5 篇常规研究论文都具有明显 JMPS 机制化写法：不是只报告性能或曲线，而是把一个复杂现象压缩成可解释的核心机制。fibrin 网络论文用 deformational freedom 统一 junction density、crack length、W/L ratio 和 tortuosity；aneurysm 论文用 mechanobiological stability 和 growth/remodeling/damage feedback 区分主动组织与被动管屈曲；LPBF-AlSi10Mg 论文用 defect-aware I-DVC 证明 microporosity 驱动 in-situ matrix properties；non-Hermitian WET 论文用 Hamiltonian symmetry 把能量传输变成设计原则；granular yielding 论文用 surface energy 和 specific surface area 的共轭关系解释热弱化。

`Preface` 是非标准研究论文，主要功能是学术传记和专刊致敬，不适合完整研究论文模板。已按真实出版类型简化，并保留 0-19 标题结构。

## 本批最值得学习的 5 个写法
1. 用一个“统一机制词”组织多参数结果：deformational freedom、mechanobiological instability、microporosity-driven properties、PT/anti-PT symmetry、surface-based breakage mechanics。
2. 把传统模型的不足写成“能描述但不能设计/能拟合但缺机制/能解释被动材料但不能解释活组织”。这种 gap 比简单说“研究不足”更有说服力。
3. 图表顺序服务于论证链：先定义对象和方法，再给代表现象，再给统计/相图/反演/验证，最后回到机制。
4. 强 claim 和边界条件搭配使用：在模型或实验范围内强，在临床、工程器件、高温/湿热等外推处谨慎。
5. 结论段用主题化条目回收结果，而不是按图重复。尤其 fibrin 和 aneurysm 两篇把复杂结果整理成机制标签，适合沉淀为写作模板。

## 本批最常见的审稿风险
- 模型代表性：fibrin 网络缺血细胞/流体，aneurysm 模型缺复杂生化与血流，non-Hermitian WET 缺实物实验。
- 参数与数据可比性：LPBF 论文的 bulk literature data、granular 论文的矿物表面能与宏观砂岩参数都需要严格对应。
- 图像证据依赖：裂纹路径、应变带、相图边界、yield surface 和 efficiency maps 需要结合 PDF 图像核查。
- 外推边界：从单试样、单温度范围、selected parameter robustness 或纯仿真结果推广到工程/临床时必须谨慎。
- 术语强度：complete transfer、key driver、unifying principle、most accurate 等强词需要与证据范围匹配。

## 可沉淀到 JMPS 写作模板的规律
- 选题入口：真实工程/临床现象 -> 经典模型解释不足 -> 新机制变量或新理论框架。
- 方法表达：`We develop [model/workflow] that captures [microstructural or multiphysics variation] during [process].`
- gap 表达：`Existing approaches can capture [A], but they do not explain/predict/design [B], which is critical for [application].`
- 机制表达：`The observed transition can be traced to [micro-scale variable], which controls [local event] and thereby [global response].`
- 边界表达：`This conclusion is validated for [material/system] in [range]; beyond this range, additional mechanisms such as [X] may become important.`
- 图表配置：workflow/schematic + representative fields + parameter maps/statistics + validation/comparison + uncertainty/limitations。

## 需要后续人工图像核查的内容
- fibrin 网络：Fig. 3-11 中 rupture snapshots、crack/connect zone、segment strain distribution、tortuosity 对 rupture sequence 的视觉证据。
- aneurysm：Fig. 2-14 中 phase diagram 边界、normalized growth rate、mode number、axisymmetric/non-axisymmetric morphology、damage/wall-thickness time evolution。
- LPBF-AlSi10Mg：SEM、fractured surface、DVC strain maps、damaged mesh element removal 区域、χ plots、uncertainty 图。
- non-Hermitian WET：eigenfrequency real/imaginary curves、efficiency maps、frequency spectra、loss/no-loss 对比、steel/aluminum systems 的参数标注。
- granular yielding：Morse potential 图、fracture toughness 拟合、GSD/fractal plots、stress-strain/yield surface/AE 对比图。
- Preface：无研究图像需要核查；如需归档质量，可核作者署名、机构和特殊字符。
