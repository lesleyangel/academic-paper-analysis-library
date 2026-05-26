# Batch 13 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Pretrain-finite-element-method--A-pretraining-and-w_2026_Journal-of-the-Mech.md`：Pretrain finite element method: A pretraining and warm-start framework for PDEs via physics-informed neural operators。
- `jmps/深度拆解/papers/Prony-series-expansion-of-fractional-operators_2026_Journal-of-the-Mechanics.md`：Prony series expansion of fractional operators in viscoelastic fractal ladder models。
- `jmps/深度拆解/papers/Steady-state-crack-growth-in-viscoelastic-solids--F_2026_Journal-of-the-Mech.md`：Steady state crack growth in viscoelastic solids: Full-field analysis for the strip geometry with finite damage zone。
- `jmps/深度拆解/papers/The-effect-of-fiber-plasticity-on-domain-formation_2026_Journal-of-the-Mecha.md`：The effect of fiber plasticity on domain formation in soft biological composites—Part II: An imperfection analysis。
- `jmps/深度拆解/papers/Theory-guided-design-of-continuous-gradient-archit_2026_Journal-of-the-Mecha.md`：Theory-guided design of continuous-gradient architected materials: Trapping impact energy via impedance valley。
- `jmps/深度拆解/papers/Three-dimensional-third-medium-contact-model-for-_2026_Journal-of-the-Mechan.md`：Three-dimensional third medium contact model for hyperelastic contact and pneumatically actuated systems。

## 本批论文的共同特征
本批 6 篇都属于 JMPS 中“机制/方法闭合”很强的一类：不是只报告性能，而是把一个边界条件下的困难转化为可推导、可计算、可验证的框架。PFEM 和 third-medium contact 是计算方法型，Prony 和 steady-state crack growth 是理论推导型，fiber plasticity 与 impedance valley 是机制/设计型。共同点是：都先承认已有方法有效，再选择一个旧方法处理不好的场景作为切入点。

另一个共同点是图表叙事完整：概念图定义问题，公式/模型图定义方法，主结果图验证 claim，参数图说明边界，结论回到适用范围。除 Prony 偏理论外，其余论文都高度依赖云图、曲线和示意图；当前拆解已在每篇中标注需结合 PDF 图像核查。

## 本批最值得学习的 5 个写法
1. PFEM 的写法：把 AI 方法写成经典求解器的加速器，而不是替代者，降低计算力学审稿人的防御性。
2. Prony 论文的写法：把经验分数阶行为还原为微结构固定点，再转成 Prony 展开，完成物理来源与计算效率的双闭合。
3. 黏弹裂纹论文的写法：在经典问题中引入有限 damage zone 参数，用极限情形回收旧理论，同时解释新边界。
4. Fiber plasticity 论文的写法：用 companion paper 的完美理论作基准，再通过 imperfection analysis 检验理论稳健性和真实材料相关性。
5. Impedance valley 论文的写法：将结构设计概念写成“传统单调梯度副作用 -> 非单调阻抗谷 -> 能量陷阱 -> 实验验证”的清晰链条。

## 本批最常见的审稿风险
主要风险包括模型边界过窄、参数选择依赖、图像或实验细节需要回 PDF/原始数据核查、benchmark 与真实工况之间仍有距离。计算方法论文会被追问与最接近 baseline 的公平比较；理论论文会被追问假设是否过强；设计论文会被追问制造误差、材料率效应和实验样本量。

具体到单篇：PFEM 风险在训练成本与分布外泛化；Prony 风险在理想自相似和线性假设；黏弹裂纹风险在 Mode III/linear/DB cohesive zone 理想化；fiber plasticity 风险在二维 laminate 与真实 tendon 的距离；impedance valley 风险在一维等效模型和有限 shock-tube 载荷；third-medium contact 风险在 third medium 区域预定义和正则化参数敏感性。

## 可沉淀到 JMPS 写作模板的规律
规律一：Introduction 最有效的 gap 往往不是“没人做”，而是“已有 A、B、C，但在 D 边界下无法闭合”。规律二：Method 章节要先讲模块功能，再讲公式。规律三：Results 章节按 claim 组织，而不是按实验/推导流水账组织。规律四：Discussion 要主动给出适用边界，这在 JMPS 中常常增强而不是削弱可信度。

可沉淀的通用模板：背景需求 -> 经典路线 -> 最近进展 -> 边界缺口 -> 本文框架；模型定义 -> 关键变量 -> 假设边界 -> 实现细节；baseline -> 参数变化 -> 极限/边界 -> 机制图 -> 讨论风险。

## 需要后续人工图像核查的内容
所有文件均基于 txt 和图注完成；云图颜色、局部形貌、曲线坐标、实验照片、结构示意、应力/应变集中位置、图中标记点、误差色标和表格排版需结合 PDF 图像核查。

重点核查项：PFEM 的误差云图和迭代曲线；Prony 的收敛/成本图和 fractal cell 拓扑；裂纹论文的耗散云图和 hysteresis loops；fiber plasticity 的 domain 形貌、transition regions 和 accumulated plastic strain；impedance valley 的能量热图、阻抗演化和 shock-tube 曲线；third-medium contact 的自接触/气动执行器变形图和 gap 表格。
