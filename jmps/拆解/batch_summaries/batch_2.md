# JMPS 论文拆解批次 2 摘要

## 批次范围
本批次覆盖 6 篇 2026 年 JMPS 论文：

1. `Constitutive-parameter-inference-using-physics-infor_2026_Journal-of-the-Mec`
2. `Crack-tip-deformation-transitions-and-fracture-mecha_2026_Journal-of-the-Mec`
3. `Deformation-induced-domains-in-sili_2026_Journal-of-the-Mechanics-and-Physic`
4. `Design-of-a-specimen-to-train-path-dependent-deep-learnin_2026_Journal-of-th`
5. `Dynamic-control-of-rigidity-via-geometric-frustration-_2026_Journal-of-the-M`
6. `Dynamic-stress-response-kernels-for-dislocations-_2026_Journal-of-the-Mechan`

## 总体画像
这一批的共同特征是“把不可见的内部机制变成可计算/可识别对象”。肩袖肌腱论文用全体积 MRI 位移场识别内部本构机制；玻璃态聚合物论文用 FE-MD 耦合解析裂尖附近分子机制；硅橡胶论文用 CT/DVC 与移动相模型解释变形诱导畴；试样设计论文把试样几何变成深度材料模型的数据生成器；超材料论文把响应材料的本征变形变成几何挫折和自应力；动态核论文把裂纹/位错的各向异性动态响应统一为 Lagrangian 核函数。

## 可学习的 JMPS 写法
- 选题不只说“更准确”，而是指出传统观测/模型缺少哪个内部变量、空间场或数学核。
- 方法论文通常需要双重证据：先证明方法对象合理，再用下游任务或特殊情形还原证明它有用。
- 图表承担强论证功能：全场误差图、相图、阶段演化图、路径覆盖图、band structure 或公式推导都不是展示附属品，而是 claim 的骨架。
- Discussion 常把不足转化为下一代模型需求，例如体积项误差、真实实验闭环、制造缺陷、数值分支切割等。

## 六篇的核心资产
- 肩袖肌腱：全场测量 + 物理约束反演 + 候选本构模型比较。
- 玻璃态聚合物裂尖：阶段机制链，`plastic activation -> coalescence -> necking -> disentanglement fracture`。
- 硅橡胶畴：异常实验现象 + tracer 证据 + 内部变量模型 + 相图统一。
- 单试样训练深度材料模型：strain diversity 熵目标 + 拓扑优化 + 下游 GRU 泛化验证。
- 几何挫折刚度控制：central force network 的 self-stress 机制转译为响应超材料设计。
- 各向异性动态核：用 L(v) 和 p(v) 统一裂纹/位错动态应力响应。

## 主要审稿风险共性
- 数据/模型外推：动物肌腱到人体、粗粒化聚合物到真实材料、数值试样到真实实验、理论超材料到制造样品。
- 内部变量可观测性：硅橡胶 mobile phase/nematic domain、玻璃态聚合物缠结断裂、肌腱纤维方向场都需要图像或额外实验支撑。
- 方法复杂度与必要性：越是复杂工作流，越需要明确说明传统方法为何不够，以及新增复杂度带来什么不可替代的信息。
- 边界和实现问题：MRI 分辨率、FE-MD 边界、DVC 平滑、mesh/filter 依赖、超材料缺陷、各向异性核的数值分支切割。

## 可迁移到自己论文的套路
1. 用“传统方法看不见/生成不了/统一不了 X”制造 gap，而不是泛泛说精度不足。
2. 把核心贡献压缩成一个可命名对象：全体积反演框架、阶段机制链、相图、strain-diversity specimen、geometric-frustration switch、Lagrangian kernel。
3. 让图表按论证顺序排布：概念图 -> 方法/变量定义 -> 关键结果 -> 对比/敏感性 -> 局限或未来闭环。
4. 在结论中同时给出强 claim 和清楚边界，避免把数值可行性、理论推导或动物模型直接写成工程/临床成熟方案。

## 异常与核查说明
- 本批次拆解基于 `jmps/文本/txt` 的全文抽取文本，并结合 references 和 figure captions。
- 多篇论文的关键图像本体无法从 txt 中完整读取；涉及空间分布、形貌、曲线数量级和附录图细节处，已在对应拆解中注明“需结合 PDF 图像进一步核查”。
