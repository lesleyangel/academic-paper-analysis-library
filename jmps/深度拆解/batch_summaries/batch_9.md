# Batch 9 深度拆解摘要

## 完成文件

1. `jmps/深度拆解/papers/Data-driven-material-identification-in-hete_2026_Journal-of-the-Mechanics-an.md`
2. `jmps/深度拆解/papers/Degradation-of-constitutive-response-to-mass-loss--Pr_2026_Journal-of-the-Me.md`
3. `jmps/深度拆解/papers/Dislocation-distribution-near-a-wall-within-the-f_2026_Journal-of-the-Mechan.md`
4. `jmps/深度拆解/papers/Dynamics-and-modal-energy-analysis-of-periodic-_2026_Journal-of-the-Mechanic.md`
5. `jmps/深度拆解/papers/Editorial-Board_2026_Journal-of-the-Mechanics-and-Physics-of-Solids.md`
6. `jmps/深度拆解/papers/Effect-of-discreteness-on-domain-wall-stability-i_2026_Journal-of-the-Mechan.md`

## 本批论文的共同特征

本批 5 篇研究论文都不是单纯“做仿真给结果”的文章，而是把一个复杂现象转化为可解释的力学结构：构成差距、反应程度、塑性势参数、模态能量分数、能量 landscape。它们共同体现 JMPS 的偏好：数据或有限元证据必须被理论变量组织起来，图表要服务于机制而不是只展示现象。

三篇论文有明显的“模型校准/验证”气质：数据驱动材料识别用 synthetic full-field displacement 验证反问题框架；水解 vitrimer 用 FTIR、拉伸、松弛、质量损失校准多物理本构；位错墙问题用 DDD 校准 continuum theory 参数。两篇结构论文则更偏“设计规则”：弹性铰结构通过 modal energy fraction 解释 ZGV，双稳态基底通过 P-N pinning 建立 domain wall 稳定准则。

`Editorial-Board` 是非研究性出版信息页，已按真实类型简化处理，保留 0-19 标题但不虚构研究问题、方法或结果。

## 本批最值得学习的 5 个写法

1. **把数据驱动方法物理化**：`Data-driven material identification...` 先定义相容、平衡和构成 gap，再引入 DDI/k-planes，避免算法像黑箱。
2. **用中心内部变量串起多尺度退化**：`Degradation of constitutive response...` 用 reaction extent 连接酯键衰减、BER 减弱、branch redistribution、质量损失和 void susceptibility。
3. **为复杂理论设计简单 benchmark**：`Dislocation distribution near a wall...` 用 impenetrable wall 产生可拟合密度分布，使 continuum dislocation theory 参数可校准。
4. **由模态形状提炼机制指标**：`Dynamics and modal energy analysis...` 从 FEA 模态观察到铰弯曲主导，再定义 torsional spring energy fraction，增强解释力。
5. **用能量地形统一多种形态演化**：`Effect of discreteness...` 把 expansion、shrinking、pinning 统一到 surface/bulk energy 与 P-N modulation 竞争中。

## 本批最常见的审稿风险

- 合成或数值数据强、真实实验验证弱：数据驱动识别和 domain wall stability 都主要依赖 synthetic/FEA。
- 模型边界较窄：线性黏弹、干态玻璃 vitrimer、单滑移位错、一维周期结构、小挠度板模型等，都需要避免标题或摘要过度泛化。
- 参数敏感性和唯一性风险：k-planes 初始化/相数、vitrimer 多参数演化、位错 continuum 参数、ROM 稳定范围都可能被追问。
- 图像证据依赖 PDF：空间分布图、色散图、FEA contour、显微图等从 txt 只能读图注，后续应结合 PDF 图像核查。
- “设计规则”泛化风险：elastic hinge 与 polygon domain wall 的规则在有限参数/有限样例中验证，不能直接声称适用于任意结构。

## 可沉淀到 JMPS 写作模板的规律

- **背景写法**：先承认领域已有进展，再指出“数据/结构/实验已具备，但缺少可解释框架”。
- **方法写法**：先给物理 admissible set 或能量函数，再给算法/降阶/有限元实现。
- **结果写法**：按难度递进案例展开，并在最难案例中展示方法模块的必要性。
- **机制写法**：用 competition、energy landscape、modal energy、internal variable、benchmark geometry 等概念组织结果。
- **局限写法**：具体列出模型假设、未建模机制和后续验证路径，不用泛泛说 “future work is needed”。

## 需要后续人工图像核查的内容

- 数据驱动识别：Figs. 3/7/10/11 点云和平面、Figs. 4/8/12 相分布、Table 1/2 误差与误分类。
- vitrimer：Figs. 7-11 曲线拟合偏差，Figs. 12-13 显微图与 simulated low-std contours 的定性对应。
- 位错墙：Figs. 4-6 和 8-10 中 2D/3D DDD 拟合质量，尤其近墙排除区域。
- 弹性铰结构：Fig. 4 实验色散与 FEA 叠合，Fig. 6 ZGV 局域，Figs. 7-10 energy fraction 与极限模型。
- 双稳态基底：Figs. 8-11 的 P-N local minima 与 FEA stable radii，Figs. 12-15 polygon/cat geometry 稳定演化。
- Editorial Board：如需精确人名/机构，应核查 PDF 分栏，避免 OCR 错配或特殊字符误读。
