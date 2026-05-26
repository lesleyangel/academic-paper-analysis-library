# JMPS 论文拆解批次 5 摘要

## 覆盖论文
1. Polymer necking revisited: A route to a new oriented material state in poly(ethylene terephthalate)
2. Programmable symmetry-breaking in folded elastic ribbons via tunable pitchfork bifurcations
3. Shear and compaction bands in porous rocks with a micromechanics-inspired non-local elastoplastic model
4. Symmetries of (quasi)periodic materials: Superposability vs. Indistinguishability
5. The mechanics and physics of tofu: Understanding hydrated soft solids through feature networks
6. The mechanics of the Less In More Out artificial heart: Modeling fabric-based soft robotic devices

## 批次总体画像
这一批 JMPS 论文的共同特征是：都不满足于描述现象，而是把现象重写成可计算、可控制或可复用的“状态/判据/框架”。PET 颈缩论文把不稳定视为材料状态转化；折叠 ribbon 论文把屈曲路径变成几何可编程稳定性景观；多孔岩石论文把剪切与压密带统一为微结构竞争；准周期材料论文把对称性从可叠合性扩展到不可区分性；豆腐论文把食品质构变成本构发现 benchmark；LIMO 人工心脏论文把器件实验转成局部应力和疲劳风险设计工具。

## 最强可复用套路
- 反转对象身份：把“失效/缺陷/日常对象”改写成“可利用状态/调谐器/benchmark”。PET、folded ribbon、tofu 都非常典型。
- 建立不可观测量：常规实验看不到颈缩区内禀响应、分岔稳定景观、岩石微结构演化、人工心脏内部应力场，于是论文价值来自“让不可见变可测/可算”。
- 竞争机制叙事：取向承载 vs 松弛流动、几何偏置 vs 全局失稳、孔裂成核 vs 孔隙塌陷、弹性 vs 非弹性、水含量调制不同网络项。
- 图表组合拳：基线对照 + 参数相图/敏感性 + 机制示意 + 设计/性能对比，是这一批最常见的说服结构。

## 写作与引用观察
- Introduction 通常先给大背景，再指出已有文献“研究了起始/全局/传统判据/经验指标”，最后收束到一个具体不可分辨的问题。
- Discussion 常用小标题直接写 claim，尤其 tofu 和 LIMO；这种写法适合机制多、结果多的论文。
- 引用姿态大多温和：承认经典模型或实验贡献，再说它们没有处理本文的边界条件、对象状态或可计算判据。
- 强 claim 往往配限定：`over the tested range`, `first-order`, `currently requires`, `single realization`, `room temperature` 等，审稿友好。

## 主要审稿风险类型
- 泛化风险：PET 只测一种材料；rock 模型主要验证 chalk；tofu 只有三种水含量；LIMO 是特定器件。
- 机制证据不足：PET 的链取向需要更多微观表征；rock 的随机孔隙场需要多 realization；tofu 的三维本构发现需要更多加载模式。
- 模型简化：folded ribbon toy model、LIMO 各向同性织物模型、quasiperiodic symmetry 的人工频率选择都可能被追问。
- 图像依赖：本批多篇核心证据在图像、相图、场图和图注中；txt 可读但图像本体不可读，关键图需结合 PDF 核查。

## 可迁移到自己论文的 6 件事
1. 用一个强基线对照定义贡献：初始 PET vs 颈缩 PET，pristine ribbon vs folded ribbon，实验全局 PV vs 仿真 full-field。
2. 把 gap 写成“旧方法看不到/分不开/不能统一”的问题，而不是泛泛说研究少。
3. 将图表功能前置设计：每张图承担一个 claim，不只是展示结果。
4. 主动给边界条件，反而增强可信度。
5. 如果方法复杂，增加 toy model、机制图或变量-机制映射降低黑箱感。
6. 让题目或摘要包含一个可记忆的概念反转：necking revisited、fold as tuner、tofu as benchmark、superposability vs indistinguishability。

## 异常与核查
- 原始 txt 存在 PDF 字符抽取乱码，如连字符、特殊符号和部分数学字符显示异常；不影响主旨判断，但公式细节需以 PDF 为准。
- 图像本体未在 txt 中呈现，所有涉及场图、相图、FFT peaks、网络权重热图、疲劳风险图的细节均应结合 PDF 图像核查。
