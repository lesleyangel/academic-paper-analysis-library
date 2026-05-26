# 研究轨迹与方向矩阵：基于 801 样本的团队画像

> 说明：以下分析只基于 `801/深度拆解/README.md`、9 个 `batch_summaries`、抽查的单篇深拆文件和 `801/文本/_manifest.json`。团队边界、核心 PI、作者角色如果没有直接证据，不做强判断；本文统一称为“基于 801 样本的团队画像”。

## 1. 样本范围和证据可信度

| 项目 | 观察 | 证据强度 |
| --- | --- | --- |
| 样本规模 | 深度拆解总览显示 49 篇 PDF、49/49 文本抽取、49/49 深度拆解、9/9 批次总结完成。 | 强 |
| 年份范围 | 文件名和 manifest 覆盖 2016-2026，近期集中在 2024-2026。 | 强 |
| 主要作者群体 | 单篇深拆作者行中 Chunlin Gong 反复出现，Jianjun Gou、Chunna Li、Hua Su、Jiaxin Hu、Ge Gao、Xuyi Jia、Xiaobing Ma 等构成多条方向的稳定合作者。 | 中 |
| 机构边界 | 多篇明确出现 Northwestern Polytechnical University / 西北工业大学航天学院，但不是每篇都有完整机构行；不能据此断定全部论文来自同一固定行政团队。 | 中 |
| 研究对象 | 高超声速/再入飞行器、热防护与热管理、复合材料单胞、热电器件、气动/轨迹/控制、稀疏传感场重构、不确定性传播反复出现。 | 强 |
| 连续升级关系 | 多个单篇深拆直接提到“团队前期工作”或“延续某路线”，批次摘要也显示 unit cell、热管理/TEG、场重构、SCP/制导等链条。 | 中-强 |
| 作者角色与团队分工 | 现有材料主要有作者列表，缺少全量通讯作者/贡献声明汇总；不判断个人分工和性格。 | 不可判断 |

可信度结论：方向、年份、期刊、方法类型的判断可信度高；“团队生产线”与“资源复用链”可信度中到高；核心 PI、作者具体分工、合作网络功能只能作为推断或不判断。

## 2. 按年份/阶段划分研究轨迹

### 阶段一：2016-2018，热-材料-单胞基础资产期

关键词：高温复合材料、热响应实验、unit cell、边界条件、初代 TE-TPS、代理可靠性。

代表论文包括：2016 FRP 高温刚度退化模型、2016 太阳辐照高热流实验装置、2017 对称复合材料热性质 unit cell、2018 热膨胀 unit cell、2018 TE-material TPS、2018 corrugated-core ITPS 应力分析、2018 RBF 序贯代理可靠性。

这一阶段的主要贡献不是单一系统，而是建立可复用“基础砖块”：热-力材料退化模型、单胞对称性/边界条件规则、高热流实验验证、热电防热概念和低成本可靠性代理。证据强度：强。

### 阶段二：2019-2021，系统级热管理与工程流程期

关键词：whole-vehicle thermal management、active cooling network、heat dissipation-transport-reuse、multi-functional TPS、morphing rules、ROM。

代表论文包括：2019 active cooling networks 热管理系统、2019 aeroelastic tailoring ROM、2021 heat dissipation-transport-reuse 管理框架、2021 mechanical-thermal-electrical TPS、2021 变体飞行器规则。

这一阶段从“材料/局部结构”上升到“飞行器系统设计”。典型动作是提出能贯穿多模块的中间变量或系统框架，例如 overall equivalent HTC、heat reuse proportion、整机-板-单元边界传递。证据强度：强。

### 阶段三：2022-2023，界面非理想因素与算法部署期

关键词：TCR/ECR、近场热辐射、真实粗糙拓扑、hp-adaptive SCP、MAV 路径跟随、压缩系统尺寸。

代表论文包括：2022 interfacial electrical contact resistance、2022 hp-adaptive RPD-SCP、2023 thermal contact model with near-field effects、2023 quantitative interfacial contact effects、2023 hypersonic compression system physical dimensions、2023 MAV path following。

这一阶段的共同变化是把以前可能被当作“误差项”的因素变成主变量：界面接触阻抗、壁板厚度/振动、传感器/路径约束、离散误差。论文开始更明显地面向部署边界：真实接触、真实结构厚度、在线/高效求解。证据强度：强。

### 阶段四：2024-2026，数据驱动中间表示与在线智能期

关键词：POD/ROM、TFNO、DNN-transfer learning、sparse sensors、multi-fidelity、uncertainty propagation、MDO、WAPE-NMPG。

代表论文包括：2024/2025/2026 场重构与热场反演、2025 POD+TSCN 热流预测、2025 多源传感物理场重构、2026 TFNO 稀疏传感热场重构、2024/2025/2026 不确定性传播与多尺度 UQ、2025 WAPE-assisted ET-NMPG、2026 cross-domain vehicle MDO、2026 dual modal spaces + LSTM。

这一阶段最显著的升级是：从“离线设计模型”走向“有限传感、低保真/高保真融合、在线推理、任务闭环”。AI/ROM 不是单独炫技，而是嵌入热管理、气动建模、损伤识别、制导和设计优化流程。证据强度：强。

## 3. 长期母题与核心矛盾

| 长期母题 | 样本中的表现 | 核心矛盾 | 证据强度 |
| --- | --- | --- | --- |
| 用中间表示降低复杂系统成本 | unit cell、POD、ROM、Kriging/RBF、SCP、TFNO、等效层、heq、Nataf 传播反复出现。 | 高保真模型可信但太慢；工程设计/在线运行需要快。 | 强 |
| 把局部非理想因素映射到系统指标 | TCR/ECR、粗糙接触、近场热辐射、孔隙、单胞边界、壁板振动、传感器稀疏。 | 微观/局部因素复杂，但最终要影响功率、热安全、刚度、轨迹或可靠性。 | 强 |
| 热从“负担”变成“可管理资源” | TPS、active cooling、heat dissipation-transport-reuse、TEG、aerodynamic heat harvest。 | 高热流既威胁结构，又可能被转运和复用。 | 强 |
| 有限数据/观测下的全场判断 | 稀疏传感热场重构、物理场重构、温度场反演、损伤识别、在线参数估计。 | 真实飞行不可全量测量，但决策需要全场或系统状态。 | 强 |
| 多尺度/多学科耦合的可解释压缩 | 微-介-宏单胞，热-电-力 TEG，气动-结构-轨迹 MDO，不确定性跨学科传播。 | 耦合系统不可直接全量求解，必须压缩但不能丢掉关键物理。 | 强 |

核心矛盾可以概括为：航空航天复杂系统要求物理可信、场景真实、约束完整；但论文和工程流程都要求计算可承受、数据可获得、结果可解释、指标可决策。801 样本的生产方式，就是持续寻找“中间层”：等效变量、单胞、模态、代理模型、传感器映射、参数化指标，让复杂对象进入可计算、可验证、可发表的形式。

## 4. 方向矩阵

| 方向 | 代表论文 | 对象 | 方法 | 贡献 | 期刊 | 阶段 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 高超声速热防护/热管理/热复用 | 2018 TE-TPS；2019 active cooling TMS；2021 heat dissipation-transport-reuse；2021 MTPS | 高超声速/可重复使用飞行器、TPS、ACN、TE-AFRSI | 等效热平衡、overall HTC、系统 roadmap、多尺度边界传递 | 把局部防热扩展为全机热管理与热复用框架 | Aerospace Science and Technology；Applied Thermal Engineering；Composite Structures | 2018-2021，延续到 2025 | 强 |
| TEG 界面接触与热电器件 | 2022 ECR；2023 quantitative contact effects；2023 NFTR TCR；2025 multi-layer TEG；2025 aerodynamic-heat-harvest TEG | 热电器件、多异质界面、粗糙表面、RTG/高速飞行器 TEG | W-M 粗糙面、真实拓扑、TCR/ECR 等效层、压力/温度/介质扫描、实验验证 | 将界面损失从误差项变成设计变量，推进到器件级验证 | IJHMT；Applied Thermal Engineering；Aerospace Science and Technology | 2022-2025 | 强 |
| 复合材料单胞、多尺度有效性质与 UQ | 2016 FRP 退化；2017 unit cell 热导；2018 thermal expansion UC；2025 plain woven multi-scale UQ；2026 stochastic porosity stiffness propagation | 织物/单向复合材料、FRP、孔隙、有效热/力性质 | 对称性单胞、边界条件推导、Nataf、多尺度传播、非侵入建模 | 从规则澄清到不确定性传播，形成材料多尺度资产链 | Applied Thermal Engineering；Composite Structures；CMAME | 2016-2026 | 强 |
| 稀疏传感、热/物理场重构与健康监测 | 2025 POD+TSCN 热流预测；2025 multi-source physical field reconstruction；2025 damage identification；2025 POD-BPNN-GA 温度反演；2026 TFNO | 再入舱/钝锥/翼结构/热场/压力场/损伤状态 | POD、RBFNN、BPNN、GA/DE、Kriging、TFNO、multi-fidelity、history window | 从有限传感器恢复全场，服务在线热管理、安全评估和损伤识别 | Aerospace Science and Technology；IJHFF；ICHMT | 2025-2026 | 强，上升 |
| ROM/AI 气动与流场建模 | 2025 KRR-DCR；2024 DNN-TL 双旋弹；2026 dual modal spaces + LSTM；2024 FSI flow sensing | 流场、非定常气动载荷、双旋弹、FSI 系统 | KRR、nonlinear ROM、DNN/TL、LSTM、POD 局部残差 | 替代高成本 CFD/RBD，连接场预测与轨迹/结构任务 | Aerospace Science and Technology；Journal of Fluids and Structures | 2024-2026 | 中-强，上升 |
| 轨迹优化、制导控制与 MDO | 2021 morphing rules；2022 hp-adaptive SCP；2024 three-stage SCP；2025 WAPE ET-NMPG；2026 cross-domain MDO | 变体飞行器、再入轨迹、跨介质飞行器、MAV | MFK、多阶段 SCP、事件触发 NMPG、在线参数估计、分布式-集中式协调 | 把复杂优化拆成阶段化、可在线或可协调求解流程 | Aerospace Science and Technology；CJA；ISA Transactions | 2021-2026 | 强 |
| 可靠性与不确定性传播 | 2018 SSRM；2024 HABMPPT；2024 P-box nonlinear dynamics；2025 multidisciplinary UP；2025 multi-scale UQ | 极限状态函数、随机过程、火箭系统、多尺度材料 | RBF/代理模型、BMPP trajectory、Chebyshev/CADET、相关变量传播、Nataf | 降低 Monte Carlo/高保真调用成本，并保留相关性/分布不确定性 | Structural and Multidisciplinary Optimization；PEM；CJA；Composite Structures | 2018-2025 | 强 |
| 结构/热/力优化与气动弹性 | 2018 corrugated-core ITPS；2019 aeroelastic tailoring；2024 rudder hierarchy optimization；2025 wing thermal force-path optimization | ITPS、机翼、舵结构、气动弹性剪裁 | 等效夹芯、layerwise theory、CFD-based ROM、层级变量、混合 GA | 将结构拓扑/力路径/气动弹性纳入高效设计循环 | Composite Structures；Journal of Fluids and Structures；AST | 2018-2025 | 中 |
| 热电材料与高熵陶瓷 | 2018 Ca-Co-O；2024 non-equimolar high-entropy titanate；2024 CEJ textured ceramics；2026 GO-driven high-entropy titanate | 钙钛矿/钛酸盐/陶瓷热电材料 | 高熵、微结构调控、缺陷/第二相、XRD/SEM/TEM/XPS 等表征 | 为 TEG/热复用方向提供材料性能支撑，但与飞行器系统链条的耦合强弱不一 | Results in Physics；JAC；CEJ；JECS | 2018，2024-2026 | 中，上升 |
| 跨学科探索：微重力生物学 | 2024 simulated microgravity microglia transcriptome | BV2 细胞、转录组、微重力神经风险 | RNA-seq、DEGs、GO/KEGG、qPCR | 航天环境健康方向的合作/试探性扩展 | Acta Astronautica | 2024 | 弱 |

## 5. 主方向、副方向、试探方向、上升方向与可能继续发展方向

主方向：

1. 高超声速热防护、热管理、热电复用与界面效应。证据强：2018-2025 多篇连续出现，且从概念结构、系统框架、接触模型推进到器件验证。
2. 复合材料/多尺度单胞/有效性质与不确定性。证据强：2016-2026 跨多年持续升级，单胞规则被后续 UQ/刚度传播复用。
3. 面向飞行器复杂场的高效预测、重构、优化。证据强且正在上升：2024-2026 集中爆发，POD/ROM/AI/稀疏传感/在线制导成为共同工具箱。

副方向：

- 轨迹优化、制导控制和跨域 MDO。证据强，但更像方法工程分支，服务总体飞行器任务。
- 气动/FSI 机理与非定常建模。证据中-强，覆盖扑翼、植被 FSI、双旋弹、非定常载荷等，部分可能来自合作场景。
- 可靠性与不确定性传播。证据强，横跨结构可靠性、P-box、火箭多学科、材料 UQ，构成稳定方法支线。

试探方向：

- 模拟微重力转录组。证据弱：单篇出现，且方法/对象与热管理、复合材料、优化主线差异大，可能是航天医学合作或拓展入口。
- 部分纯材料热电论文。证据中：2018 后在 2024-2026 再次连续出现，已经超过单篇试探，但与系统级飞行器 TEG 的直接连接仍需更多证据。

正在上升方向：

- 稀疏传感 + 多保真/神经算子 + 在线热场重构。证据强：2025-2026 多篇围绕有限传感、全场恢复、低保真融合、实时推理。
- AI/ROM 气动与热流代理。证据强：POD+TSCN、KRR-DCR、DNN-TL、LSTM 等集中出现。
- 高熵/多机制热电材料与器件界面协同。证据中-强：材料端和器件端在 2024-2026 同时增强。

可能继续发展方向：

1. 机载热状态数字孪生：稀疏传感、低保真模型、历史测量、TFNO/POD、损伤识别合并成在线热安全评估流程。证据强。
2. 界面感知的热电能源器件：粗糙界面 TCR/ECR、承载框架、真实器件实验、材料调控进一步整合。证据强。
3. 不确定性约束下的飞行器热-结构-轨迹协同优化：MDO、SCP、UQ、field reconstruction 可能汇合到闭环设计。证据中-强。
4. 多尺度复合材料从有效性质预测走向制造不确定性/损伤容限/结构优化联动。证据中-强。

## 6. 论文之间的连续升级关系

### 6.1 单胞与多尺度复合材料链

2017 unit cell 热导规则 -> 2018 unit cell 热膨胀与 appropriate utilization -> 2025 minimum-size unit cell 多尺度 UQ -> 2026 stochastic porosity stiffness propagation。

复用的问题：如何用最小代表域保留真实物理边界，如何从微/介尺度传播到宏观有效性质。

复用的方法：结构对称性、平移/反射/旋转边界条件、单胞参数化、跨尺度传播、相关性解释。证据强。

### 6.2 热管理/TEG/界面链

2018 TE-material TPS -> 2019 active cooling TMS -> 2021 heat dissipation-transport-reuse 与 mechanical-thermal-electrical TPS -> 2022 ECR -> 2023 TCR/NFTR 与 quantitative contact -> 2025 multi-layer TEG 与 aerodynamic-heat-harvest TEG。

复用的问题：高热流如何从“防护对象”变成“可转运/可复用能源”，界面损失如何影响系统输出。

复用的方法：等效热平衡、overall HTC、热-电-力耦合、粗糙接触、TCR/ECR 等效层、器件级实验。证据强。

### 6.3 场预测、稀疏传感与在线重构链

2025 POD+TSCN 热流预测 -> 2025 多源传感物理场重构 -> 2025 温度场反演/损伤识别 -> 2026 TFNO 稀疏传感热场重构；旁支包括 2025 KRR-DCR 和 2026 LSTM 非定常气动载荷。

复用的问题：高维场不可全量求解/测量，但热管理、结构安全和控制需要全场或关键场。

复用的方法：POD/ROM、模态系数、传感器优化、低保真先验、高保真局部校准、时间历史输入、误差-效率双指标。证据强。

### 6.4 轨迹优化与制导链

2021 morphing aircraft MFK 规则 -> 2022 hp-adaptive RPD-SCP -> 2024 three-stage SCP -> 2025 WAPE-assisted ET-NMPG -> 2026 cross-domain vehicle MDO。

复用的问题：成熟优化方法在真实部署中会遇到计算成本、初值、离散误差、模型偏差、强耦合协调问题。

复用的方法：分阶段求解、凸化/松弛、自适应网格、事件触发、在线参数估计、分布式-集中式协调。证据强。

### 6.5 可靠性/UQ 链

2018 RBF sequential surrogate reliability -> 2024 hybrid time-variant reliability via BMPP trajectory -> 2024 distribution-free P-box nonlinear dynamics -> 2025 multidisciplinary UP with correlated field variables -> 2025 multi-scale UQ。

复用的问题：失效概率/不确定性传播需要大量昂贵模型调用，且相关性、时间变化、分布未知会破坏传统简化。

复用的方法：代理模型、主动采样、BMPP/trajectory 近似、Chebyshev/CADET、相关变量传播、Nataf。证据强。

### 6.6 气动/FSI 与流场机理链

2019 三维扑翼参数影响 -> 2022 vegetation canopy FSI -> 2024 FSI flow sensing -> 2024/2025 双旋弹 DNN-TL 与角运动特性 -> 2026 非定常气动载荷 LSTM。

复用的问题：复杂流动或流固耦合需要在高维流场、气动载荷和运动稳定性之间建立桥梁。

复用的方法：CFD/FSI、高维场降阶、涡结构/中间变量解释、数据驱动代理、轨迹/角运动闭环。证据中。

## 7. 证据强度标注汇总

| 判断 | 强度 | 原因 |
| --- | --- | --- |
| 801 样本长期围绕“复杂航空航天系统的高效可解释建模”展开 | 强 | 49 篇跨批次反复出现高超声速、热管理、ROM/代理、优化、UQ、场重构。 |
| 热管理/TEG 是核心主线之一 | 强 | 2018-2025 连续论文，且单篇深拆明确提到团队前作链条。 |
| 单胞/复合材料多尺度是核心主线之一 | 强 | 2016-2026 连续升级，2017/2018 方法被 2025 UQ 继承。 |
| 2024-2026 AI/ROM/稀疏传感方向正在上升 | 强 | 多篇集中在 AST、IJHFF、ICHMT 等期刊，主题和方法高度聚集。 |
| 轨迹优化/制导控制是稳定副线 | 强 | 2021-2026 多篇，SCP/NMPG/MDO 连续升级。 |
| 热电材料方向正在加强 | 中 | 2018 有早期结果，2024-2026 多篇材料论文，但与系统级 TEG 的直接复用链还需更多证据。 |
| FSI/双旋弹/扑翼是稳定气动副线 | 中 | 多篇存在，但对象分散，部分可能来自合作场景。 |
| 模拟微重力生物学代表团队转向 | 弱 | 单篇，和主方法/对象链条相距较远。 |
| 核心 PI 与具体分工 | 不可判断 | 只有作者列表和少量机构信息，缺少全量通讯作者/贡献声明。 |

## 8. 一句话结论

基于 801 样本，这个作者群体更像一个“高超声速与航天复杂系统的中间表示生产线”：长期把热、结构、材料、气动、控制和不确定性中的高成本/不可观测/强耦合问题，压缩成单胞、等效层、模态、代理模型、稀疏传感映射或阶段化优化流程，再用工程对象和定量指标证明它们能进入设计或在线评估。
