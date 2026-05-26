# Batch 4 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Machine-learning-extraction-of-viscoelastic-mater_2026_Journal-of-the-Mechan.md`：Machine learning extraction of viscoelastic material properties from full-field deformation measurements
- `jmps/深度拆解/papers/Normal-contact-of-metainterfaces--The-roles-of_2026_Journal-of-the-Mechanics.md`：Normal contact of metainterfaces: The roles of finite size and microcontact interactions
- `jmps/深度拆解/papers/Nucleation-in-rank-one-gradient-plasticity--Exa_2026_Journal-of-the-Mechanic.md`：Nucleation in rank-one gradient plasticity: Exact solutions and geometry-dependent regimes
- `jmps/深度拆解/papers/On-rubber-elasticity-from-a-microscale-structur_2026_Journal-of-the-Mechanic.md`：On rubber elasticity from a microscale structural mechanics representation of polymer chains
- `jmps/深度拆解/papers/Physics-informed-neural-network-estimation-of-activ_2026_Journal-of-the-Mech.md`：Physics-informed neural network estimation of active material properties in time-dependent cardiac biomechanical models
- `jmps/深度拆解/papers/Plasticity--hysteresis--and-recovery-mecha_2026_Journal-of-the-Mechanics-and.md`：Plasticity, hysteresis, and recovery mechanisms in spider silk fibers

## 本批论文的共同特征
- 都是 JMPS 典型的“机制/模型/反问题”论文，选题不是泛泛应用，而是把一个不可直接观测或不可直接设计的变量变成可计算对象。
- 文献使用都采取功能分组：经典理论提供语言，近年方法提供技术可能，最近工作制造窄 gap。
- 证据链普遍采用由简单到复杂的递进：解析或基准 -> 数值/拟合 -> 实验或复杂几何/异质性。
- 作者都比较注意限定边界，但面向应用的意义句仍需读者警惕外推。

## 本批最值得学习的 5 个写法
1. 先承认前人有效，再审计其假设有效域。
2. 把复杂问题拆成可命名的 regime、网络、路线或状态。
3. 用 workflow/机制图先降低认知负荷，再进入公式或算法。
4. 用附录、参数表、消融或敏感性分析防御最可能的审稿问题。
5. 把结果转成机制、设计准则或反演流程，而不是只报告拟合好。

## 本批最常见的审稿风险
- 实验或真实应用缺少外部 ground truth 时，claim 容易过强。
- 后验拟合可能被质疑为参数自由度，而非机制验证。
- 数值 benchmark 的理想几何、边界和材料假设限制外推。
- 图像/曲线细节若只从 txt 图注判断，可能误读误差量级或空间分布。

## 可沉淀到 JMPS 写作模板的规律
- JMPS 写作可以沉淀为：重要现象/需求 -> 现有路线有效但有明确边界 -> 本文在一个窄问题上提供机制闭环。
- 图表叙事应至少包含对象图、方法图、基线图、核心证据图和风险防御图。
- 贡献句优先写成 establish/provide/identify/reveal，而不是笼统 improve。
- 局限句要对应方法假设，不能只写 future work will consider more cases。

## 需要后续人工图像核查的内容
- `Machine-learning-extraction-of-viscoelastic-mater_2026_Journal-of-the-Mechan`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
- `Normal-contact-of-metainterfaces--The-roles-of_2026_Journal-of-the-Mechanics`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
- `Nucleation-in-rank-one-gradient-plasticity--Exa_2026_Journal-of-the-Mechanic`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
- `On-rubber-elasticity-from-a-microscale-structur_2026_Journal-of-the-Mechanic`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
- `Physics-informed-neural-network-estimation-of-activ_2026_Journal-of-the-Mech`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
- `Plasticity--hysteresis--and-recovery-mecha_2026_Journal-of-the-Mechanics-and`：需核查所有主图的曲线量级、云图/示意图细节、误差空间分布和图注无法覆盖的视觉信息。
