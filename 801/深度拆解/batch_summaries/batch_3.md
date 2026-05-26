# Batch 3 深度拆解总结

## 本批论文列表

1. `A-study-of-interfacial-electrical-contact-resistances-of-th_2022_Aerospace-S`
2. `A-study-of-morphing-aircraft-on-morphing-rules-a_2021_Chinese-Journal-of-Aer`
3. `A-thermal-contact-model-encompassing-near-field-e_2023_International-Journal`
4. `A-three-stage-sequential-convex-programming-approa_2024_Aerospace-Science-an`
5. `Adaptive-path-following-control-for-miniature-unmanned-aerial-v_2023_ISA-Tra`
6. `Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ`

## 共同主题和方法谱系

本批 6 篇都不是单纯“发现一个现象”的论文，而是围绕航空航天工程对象建立可验证的模型链条。共同主题包括：高超声速热管理中的界面效应、变体/轨迹优化中的计算降本、飞行器/无人机/弹丸控制中的非线性与耦合机制。

方法谱系可分为三类：

- 界面多物理建模：ECR 与 TCR/NFTR 两篇以真实粗糙形貌为入口，连接微观接触、实验验证和 TEG 系统性能。
- 轨迹与控制算法：MFK 变形规则、三阶段 SCP、MAV 3D Dubins 控制三篇都把复杂任务拆成可求解模块，并用对比实验证明效率/鲁棒性。
- 高保真气动机理：双旋弹丸论文用 unsteady CFD + CFD/RBD 把流场非对称和角运动稳定性联系起来。

## 常见 gap 类型

- 工程对象 gap：已有理论或方法存在，但没有用于高超声速 TEG、MAV 全流程、双旋弹丸等具体工程对象。
- 多尺度/多模块 gap：已有研究停留在局部模型，没有把微观界面参数映射到系统性能，或没有把制导/控制/路径几何同时处理。
- 计算成本 gap：直接高保真 CFD 或直接轨迹优化计算量过大，需要代理模型、自适应离散或分阶段算法。
- 机理解释 gap：已有仿真或插值表能给结果，但不能解释为什么气动/角运动会变化。
- 验证 gap：模型提出后缺少实验、实飞或成熟软件对比验证。

## 常见论证链

1. 工程背景很强：高超声速热、变体多任务、MAV 风扰、弹丸精度。
2. 指出已有方法有价值但在本文场景下不够：忽略界面、计算太贵、维度太高、耦合不足。
3. 建立一个可分解的方法框架：两尺度模型、MFK 离线流程、三阶段 SCP、多层 guidance/control、CFD/RBD。
4. 先验证子模型或程序可信度：交叉验证、公开文献对比、实验测量、网格/时间步独立性、成熟软件对比。
5. 再展示工程指标变化：输出功率、计算时间、跟踪误差、状态误差、复攻角收敛。
6. 最后把结果转成设计建议：使用高导电界面材料、考虑 NFTR、采用反向/静止前体、分阶段 SCP 适合实时应用。

## 高频写作套路

- “已有研究很多，但很少考虑 X 在 Y 场景下的影响。”
- “为降低计算成本，将原问题转化为离线代理/分阶段优化/等效界面层问题。”
- “Fig. X shows... As shown... In conclusion...” 的图驱动结果段。
- 用编号贡献或编号结论把 claim 与证据一一对应。
- 用对比表收束方法价值：实验-数值误差表、算法 CPU time 表、控制器实飞误差表。
- 结论中加入边界和未来工作，通常是更多变量、更多模型、line search、collision avoidance、长期可靠性等。

## 可迁移到自己论文写作的资产

- 选题资产：从一个大工程系统中抓住被理想化处理的“局部非理想因素”，再证明它对系统指标有显著影响。
- 方法资产：真实数据/形貌/路径/网格进入模型，比抽象理论更容易获得工程期刊认可。
- 证据资产：不要只给模型结果，最好有“模型验证 + 对比基线 + 系统级指标”三层证据。
- 图表资产：把局部变量和最终工程指标放在相邻结果节中，例如 ECR/TCR 到 TEG 输出功率，旋速到复攻角稳定。
- 文笔资产：claim 可以强，但要用条件和数值范围限制，如 “under vacuum clearance”, “at 0.1 MPa and 650 K”。

## 本批需要后续 PDF 图像复核的地方

- ECR 论文：Fig. 2 粗糙面重构、Fig. 7-13 应力/电势/电流密度云图、Fig. 19-21 内阻/功率曲线。
- Morphing 论文：Fig. 1-3 任务与流程，Fig. 8 最优形状，Fig. 9-18 三阶段轨迹与变形规则曲线。
- TCR/NFTR 论文：Eq. (10)-(14) 波动电动力学公式排版，Fig. 12-22 温度云图、TCR 曲线和 TEG 性能曲线。
- 三阶段 SCP 论文：Algorithm 1、Fig. 1-2、Fig. 4/7/8/11/12 迭代和网格演化曲线，公式矩阵排版。
- MAV 控制论文：Table 2/3 路径跟随规则、Fig. 5-6 框架、Fig. 8-12 仿真轨迹、Fig. 14/17/19 对比图。
- 双旋弹丸论文：Fig. 5-8 气动和流场图、Fig. 10-16 角运动/投影曲线，Appendix A/B 网格、时间步和验证图表。
