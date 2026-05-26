# Agent 2：SHM / 结构数字孪生组 AEI 文献细颗粒度分析

说明：本文件只分析用户指定的 3 篇文献，依据 2026-05-21 15:33 后重生成的 `_extracted` 下 `md/json`，并用对应 `txt` 交叉核查结论、正文和图表证据。分析主线采用 `asset/load -> response -> sensing/data -> representation/model -> decision/maintenance`。

---

## 1. `1-s2.0-S147403462400034X-main`

### 标题

Hybrid monitoring methodology: A model-data integrated digital twin framework for structural health monitoring and full-field virtual sensing

### 摘要压缩

本文提出面向桥梁 SHM 的全场虚拟感知框架，把 FEM、BRIM 和 IoT 组合成数字孪生。多尺度 FEM 作为机械孪生，从监测数据中识别隐藏特征；BRIM 作为数据孪生，承载设计到运维的全寿命信息；IoT 连接实体桥梁与网络空间。核心不是单一监测算法，而是用 hybrid monitoring 完成数据的转换、扩展、融合和可视化，并在三跨连续模型桥上验证。

### 结论压缩

结论强调三点：一是 FEM、BRIM、IoT 被整合为统一框架，用于结构状态虚拟感知、数据管理和 4D 可视化；二是 hybrid monitoring 将多源响应数据与 FEM 分析结合，实现荷载估计、全场位移重构、局部应变场重构、损伤检测与模型更新；三是大型桥梁模型验证了多尺度机械孪生和 BRIM 可将 FE 结果与现场监测数据集成到可视化界面。限制是多软件交互耗时、可靠更新 FEM 不总是可得、仍需真实在役桥梁验证。

### 全文简介

文章先从桥梁养护、视觉检查主观性、SHM 信息化需求进入，再指出 BIM-IoT 系统的关键缺陷：BIM 能管理和展示数据，但不能表达桥梁力学属性；IoT 采集的大量数据也需要被分析成可用信息。随后综述数字孪生在建筑施工、桥梁检查和运维中的使用，提出已有 DT 框架缺少长期服役场景下的实时数据处理模块，也不能联合表达几何信息、荷载-响应关系和力学行为。方法部分用 3 个模块建立 AEI 式信息链：第 3 节定义物理实体、FEM、BRIM 及 IoT 连接；第 4 节讲 hybrid monitoring，包括准静态响应、动态响应、损伤识别和模型更新；第 5 节用三跨模型桥展示 IoT 系统、多尺度 FEM、BRIM sensor family 和数据融合界面。

### 结构链

- **asset/load**：对象是三跨连续桥梁模型；荷载包括环境荷载、交通荷载、温度荷载，正文明确指出荷载的空间分布复杂且未知，是监测难点。
- **response**：关注全场位移、局部应变、动态响应、模态/频率、损伤导致的响应变化。
- **sensing/data**：模型桥安装 74 个传感器，包括 3 个位移计、11 个倾角计、32 个应变片、11 个加速度计、8 个反力计、9 个温度计；同时使用视频、环境、车辆位置和反力等异构数据。
- **representation/model**：FEM 是 mechanical twin，BRIM 是 data twin。FEM 层包含多尺度模型组：粗网格/梁单元模型用于全局响应和边界条件，细网格/壳或实体子结构用于局部应变场；BRIM 层把桥梁构件、传感器、损伤记录建成可访问的信息对象，传感器被分为 type parameter 与 instance parameter。
- **decision/maintenance**：输出不是信号指标本身，而是可用于桥梁管理的全场状态、交通荷载、损伤记录和可视化界面；文中举例包括桥梁临时关闭、交通密度降低、维修时机选择。损伤 family 可记录尺寸、检测时间、照片和损伤类型，但损伤程度量化仍需人工，是其未闭合部分。

### 图表/公式证据

- **Fig. 1**：桥梁 SHM 数字孪生框架，由 physical entity、FEM、BRIM 组成，IoT 连接实体与网络空间。
- **Fig. 2**：hybrid monitoring 总览，把静态变形感知、动态响应监测、损伤识别组织为方法体系。
- **Fig. 3**：hybrid computing 示意，粗网格全局模型提供子结构边界条件，细网格子结构重构局部应变场。
- **Fig. 4**：模型更新流程，目标函数包含频率、振型和挠度影响线，通过高维响应面和优化校准参数，使 FEM 持续反映健康状态。
- **Table 1 / Fig. 8 / Fig. 9**：传感器布设和反力计位置，是 sensing/data 层证据。
- **Fig. 10**：用于机械数字孪生的 FEM 组，证实多尺度模型不是装饰性建模，而是对应不同计算精度和效率需求。
- **Fig. 16 / Fig. 17**：Matlab、Ansys、Revit 之间的数据传输和 4D 可视化流程；重构响应多数情况下 RMSE 低于 5%，车辆荷载识别平均 RMSE 3.80%，重构挠度平均 RMSE 1.73%，中心截面应变最大误差 10.01 με；数据存储 1 min 一次，框架 1 min latency，load estimation 0.002 s，FEM calculation 0.2673 s，data visualization 1.527 s。
- **Fig. 18**：损伤信息记录，说明 DT 信息容器从响应扩展到损伤管理。
- **公式线索**：`Y = WF + e`、`Y = Xβ + e`、TSVD/Pseudo-inverse、PLSR 温度效应、JISE 状态-输入估计、响应面模型更新。这些公式服务于“荷载/响应重构”和“模型更新”，不是独立信号处理模块。

### 引用分布

新版 `md/json` 给出的粗略引用分布显示：Introduction 18，digital twin literature review 24，方法小节每节约 1-2，case study 中 data fusion and visualization 5，References 69。写作上明显把引用密度压在问题定义和 DT/SHM 文献定位中；框架、公式和案例部分主要靠作者自己的方法链与实验结果支撑。

### 写作规律

- 先批判 BIM-IoT 的不足：有信息容器和传感器，但缺力学属性与实时数据分析模块。
- 再把 DT 定义为“几何/数据容器 + 力学模型 + IoT 连接 + 监测算法”的组合，而不是仅说 BIM 可视化。
- 方法章节用功能而非算法名组织：quasi-static response monitoring、dynamic response hybrid monitoring、damage sensing and model updating。
- AEI 感来自“数据如何被转换成信息对象和工程状态”：response data -> load distribution -> full-field response -> BRIM visualization -> management action。
- 结论明确列出 limitations，避免把模型桥验证夸成真实桥梁部署。

### 可用于我们论文哪个段落/claim

- **引言 claim**：传统 SHM 若只停留在传感器与信号处理，难以支持全寿命工程管理；AEI 式 DT 要把监测数据转为可查询、可可视化、可决策的状态信息。
- **方法总框架 claim**：可借鉴 “mechanical twin + data twin” 双层表达，把物理响应重构与信息容器分开写。
- **不确定性 claim**：荷载分布未知、温度效应、稀疏测点到全场响应的扩展、FEM 可靠更新，都是认知不确定性进入 DT 的自然入口。
- **限制段 claim**：多软件链路、模型可得性和真实结构复杂性，是结构 DT 从实验验证走向工程部署的主要阻碍。

---

## 2. `1-s2.0-S1474034624005731-main`

### 标题

Hydro-steel structure digital twins: Application in structural health monitoring and maintenance of large-scale reservoir

### 摘要压缩

本文面向大型水库水工钢结构在恶劣环境和长期服役下的事故风险，提出五维 DT 建模框架，并构建 DT-based SHM 方法与平台。平台包括 perception、interaction、analysis、decision-making 四阶段，在陆浑水库验证，提供状态监测、故障特征识别、健康状态评估和维护策略优化。贡献重点是将 DT 技术落到数据采集、模型优化、综合评价和维护决策的质量提升。

### 结论压缩

结论把 HSS 的 DT 表达为 PE、VE、DTD、CN、Ss 五个维度，通过传感器、嵌入式系统和手持设备采集运行数据，将数据传到虚拟实体并与算法/模型集成分析，形成含监测与维护数据的高保真虚拟模型。该方法建立了虚实集成机制、动态健康评估机制和闭环 SHM/维护管理平台。局限和未来工作包括增加监测数据以减少定性指标、建立更全面的 HSS DT 模型、研究成熟度/成本收益评价，以及探索 foundation models 在数据分析、模型优化和算法训练中的应用。

### 全文简介

文章从高水头、大流量、大型水工钢结构的运行风险切入，指出传统人工监测和单一指标无法支撑复杂运维决策。Related works 分三层铺垫：HSS 运维挑战、SHM 应用、DT 在水利工程中的应用。第 3 节是全文的 AEI 核心：给出五维 DT 模型、PE/VE/DTD/CN/Ss 的形式化定义、数据服务表、连接协议和服务封装。第 4 节在水库径向闸门上验证 perception-interaction-analysis-decision 流程，包括传感器与 PLC 采集、有限元模型校准、响应面优化、健康评估、SWPE-SVM 故障诊断和知识图谱维护推荐。第 5 节讨论相较常规 SHM 的优势与实际部署挑战。

### 结构链

- **asset/load**：对象是 reservoir spillway radial gate 等 HSS；载荷包括自重、静水压力、动水压力、波浪荷载、地震动水压力、水锤压力、泥沙压力和风压力。PE 层还把功能部件拆成 panel、girder、radial arm、trunnion、hydraulic system 等。
- **response**：结构侧响应包括应力、应变、振动、倾角、位移、自然频率、局部模态变化；运维侧还包括开度、启闭力、启闭速度、电流电压、水位、流速、温湿度等。
- **sensing/data**：现场布设应变片、加速度传感器、双轴倾角仪、气象站，并接入 PLC 控制器；数据经智能网关和 Modbus/TCP 传到远程监控中心。DTD 被定义为 `Dp, Dv, Ds, Dk, Df`，对应物理数据、虚拟实体数据、服务数据、知识数据和融合数据。
- **representation/model**：核心表示是 `DT-HSS = {PE, VE, DTD, CN, Ss}`。VE 又分为 `Gv, Pv, Bv, Rv`，分别表示几何、物理、行为、规则模型；CN 定义 `CN_SD, CN_PD, CN_VD, CN_PS, CN_VS, CN_PV`，并把每个连接写成 `Datasource, Unit, Value, Scope, Samplinginterval`；Ss 定义为 `Function, Input, Output, Quality, State`。
- **decision/maintenance**：输出包括状态监测、健康评估、故障诊断、维护决策。决策阶段基于运维知识图谱推荐启闭速度、开度等控制参数，并先在 virtual SG 中验证，再执行到 physical SG。

### 图表/公式证据

- **Fig. 1**：HSS 五维 DT 框架，是全文 AEI 身份的总图。
- **Fig. 2 / Fig. 3**：径向闸门载荷传递与物理实体组成，支撑 asset/load 层。
- **Fig. 5 / Fig. 6**：虚拟实体与物理-虚拟系统集成架构，展示 Gv/Pv/Bv/Rv 如何接入 IoT 平台、Ansys 和 Unity。
- **Fig. 7 / Fig. 8**：DT data 与 data service system 架构，明确数据不是原始传感器流，而是设计、监测、维护、服务、知识、融合数据的组织。
- **Table 2**：CN 的实现方法，包含 OPC-UA、MQTT、Modbus/TCP、Socket、RPC、MQSeries、JDBC、ODBC 等协议/接口，是“连接可实现”的证据。
- **Fig. 9 / Fig. 10**：DT-based SHM and maintenance management platform 与四阶段工作流：Perception、Interaction、Analysis、Decision。
- **Table 3**：SHM 关键数据采集，包括振动、应力应变、倾角、闸门开度、启闭力/速度、电流电压、水位、流速、温湿度等。
- **Fig. 15 / Fig. 16 / Table 5 / Table 6**：有限元模型与 VE 参数修正流程。模型包含 32,150 个壳单元、1,129 个实体单元、66,997 个节点，流体域包含 16,320 个实体单元和 18,970 个节点；修正参数包括几何厚度、泊松比、弹性模量、密度等，目标函数包括应力值和前两阶自然频率。
- **Table 9 / Table 10**：参数优化前后与 DT 仿真结果对比；相对经验参数，频率/应力误差分别降低 2.78%、3.57%、4.63%、3.68%；静水工况下仿真与传感器应力趋势一致，相对误差在 10% 以内。
- **Fig. 18 / Fig. 19 / Table 8**：故障诊断流程，使用平均振动位移分级、SWPE 特征和 SVM 分类；基于数据驱动参数设计和仿真结果进行 false alarm verification，误报减少约 85%。
- **Fig. 20 / Fig. 26 / Fig. 27**：维护决策、DT 驱动健康评估和常规方法对比；综合评价为 B 级，并可结合知识库形成针对性维护计划。
- **公式线索**：`DT-HSS = {PE, VE, DTD, CN, Ss}`、`VE = {Gv, Pv, Bv, Rv}`、`DTD = {Dp, Dv, Ds, Dk, Df}`、`CN_XX = {Datasource, Unit, Value, Scope, Samplinginterval}`、`Ss = {Function, Input, Output, Quality, State}`、`SEs = {MSEs, WSEs, OSEs}`、响应面模型、R2、加权优化目标、虚实一致性阈值、Shannon/Wavelet packet entropy、SVM。

### 引用分布

粗略引用分布显示：Introduction 12，HSS operational challenges 14，SHM applications 7，DT hydraulic engineering 11；方法定义处引用少，多为 Tao/DT 基础框架引用；Analysis 小节约 10，Conclusion 6，References 约 88。该文的引用结构是“前端铺设事故/SHM/DT必要性，方法段靠符号定义、图表和工程平台支撑”。

### 写作规律

- AEI fit 很强，因为它不是把 SWPE、SVM、FEM 当核心贡献，而是把它们封装进 `PE-VE-DTD-CN-Ss` 的信息架构。
- 先按工程对象定义 PE 和载荷传递，再定义 VE、数据、连接和服务，符合“源量/响应/状态/决策”分层。
- 每个抽象概念都有工程落地表：CN 有协议表，DTD 有数据字段，Ss 有功能-输入-输出-质量-状态。
- 诊断算法被放在 Analysis 阶段，维护知识图谱被放在 Decision 阶段，使信号处理成为平台服务链的一环。
- 讨论部分用 conventional SHM 对比 DT-based SHM，形成 reviewer 友好的“为什么这是 informatics 而不是监测算法”的答案。

### 可用于我们论文哪个段落/claim

- **AEI 定位 claim**：可作为“数字孪生的工程信息学贡献来自数据、模型、知识、服务和连接的显式组织”的强证据。
- **框架段 claim**：`PE/VE/DTD/CN/Ss` 可借鉴为认知不确定性数字孪生的外层结构，但需要替换成我们自己的不确定性状态变量与证据链。
- **决策段 claim**：维护知识图谱 + 虚拟实体先验验证 + 物理实体执行，是把健康评估推进到 maintenance decision 的典型写法。
- **不确定性段 claim**：该文把人因、设备管理、环境复杂性区分为运维不确定性来源；可用于我们说明认知不确定性不只来自材料/模型，也来自监测、解释和管理链。

---

## 3. `1-s2.0-S1474034625011930-main`

### 标题

Edge-to-cloud computing and intelligence for IoT-based Structural Health Monitoring: A comprehensive review

### 摘要压缩

本文综述 IoT-based SHM 从 reactive、human-dependent 系统向 proactive、autonomous intelligent systems 的转变。文章用 ubiquitous computing and intelligence 作为统一视角，把 edge-to-cloud 架构、计算智能算法和 SHM 应用域组织成三视角分析框架。核心结论是 SHM 正从中心化云平台转向分布式智能，但仍受资源-性能权衡、数据质量、隐私/共享冲突和实时可靠性约束。

### 结论压缩

结论认为 ubiquitous computing and intelligence 正把 SHM 转化为可泛在感知、实时分析和智能决策的自主系统。综述分析 2016-2025 年 7326 篇文献，AI/ML 方法比例从 2016 年 2.4% 增至 2025 年 50.5%，AI-enabled 文献占总数据集 33.4%。文章通过架构、算法、应用三条线串联 edge/fog/cloud、知识驱动/AI 驱动方法，以及 measurement 到 damage quantification 的监测生命周期。案例显示 edge intelligence 可带来最多 64 倍处理时间降低和约 33 倍功耗降低，PINN 在特定状态推断任务中可达 0.1% 重构误差，LLM 在特定实现中达到 95.24% 损伤识别精度；但作者明确提示这些是个案结果，不可作为通用保证。未来重点是资源约束、数据质量、实时通信、系统可靠性、软硬件平台和标准化。

### 全文简介

文章是综述型 AEI 写法。第 1 节提出 3 个研究问题：如何用 computing principles 统一 edge-to-cloud SHM ecosystem，哪些架构/算法/应用视角支撑智能自主 SHM，关键挑战和方向是什么。第 2 节建立 IoT-based SHM 的 data infrastructure and workflow，包括 perception/actuation、network/communication、cognition，以及 acquisition、preprocessing、transmission、storage、fusion、analysis、application。第 3 节比较 centralized、distributed、cloud、fog、edge computing。第 4 节综述 knowledge-based 与 AI-based approaches，包括 PINN、Bayesian、GNN、federated learning、reinforcement learning、LLM/agents 等。第 5 节按 SHM 任务组织应用：measurement、system identification、damage detection、localization、quantification。第 6-7 节用案例和挑战/使能技术/工程考虑完成落地讨论。

### 结构链

- **asset/load**：综述对象是 generic structures，包括桥梁、建筑、隧道、管线等；load 不作为单独力学主题展开，而是隐含在结构状态、运行环境和事件触发监测中。该文的“外部约束”还包括网络带宽、功耗、通信延迟、隐私、数据所有权和部署成本。
- **response**：响应包括 vibration、strain、displacement、damage indicators、modal/system identification features、anomaly/fault signals，以及点云、图像/视频、音频和文本等非传统 SHM 数据。
- **sensing/data**：IoT 系统被写成 sensing devices、communication networks、processing units 和 data pipeline；数据管线分为 acquisition/preprocessing、transmission/storage/fusion、analysis/application。
- **representation/model**：不是单个 FE 模型，而是架构-算法-应用三视角表示：edge/fog/cloud 计算范式决定资源位置，knowledge-based/AI-based 方法决定推理方式，measurement-to-quantification 决定任务输出。文中还强调 cloud 的 semantic consistency 和 centralized metadata governance，以及 distributed systems 的 local autonomy。
- **decision/maintenance**：决策输出包括实时 fault detection、本地事件触发感知、跨站点诊断、长期趋势追踪、damage identification、adaptive sensor scheduling、autonomous structural control、dynamic resource allocation。该文把 SHM 从“收集数据”提升为“按任务、延迟、数据位置和资源可用性分配计算与决策”。

### 图表/公式证据

- **Fig. 2**：2016-2025 核心期刊 SHM 关键词共现网络，用于说明领域结构。
- **Fig. 3**：AI/ML-enabled publications 的方法分布，支撑 AI 方法增长趋势。
- **Fig. 4**：全文总框架图，把 IoT data infrastructure/data pipeline 与三视角 analytical framework 连接起来。
- **Fig. 5**：IoT-based SHM data infrastructure and associated data flow，对应 perception、communication、cognition 和 device/network/application 层。
- **Fig. 6 / Fig. 7 / Fig. 9 / Table 1**：网络结构、OSI 协议和无线协议选择，说明 AEI 综述会把通信层作为工程部署证据，而不只讲算法。
- **Table 2**：centralized vs distributed computing，对比 latency、bandwidth、resilience、privacy、typical use cases。集中式适合 trend analysis/cross-site diagnosis，分布式适合 event-triggered sensing/local detection。
- **Table 5**：IoT-based SHM representative case studies，按 device、paradigm、algorithm、application、highlights 组织，是综述把案例转化为可比较知识表的关键。
- **Fig. 13**：potential enablers 总览，将 challenges、key technologies 和工程实现连接。
- **量化证据**：7326 篇文献；AI/ML 比例 2.4% -> 50.5%；AI-enabled 占 33.4%；edge intelligence 个案 64 倍处理时间降低、约 33 倍功耗降低；PINN 个案 0.1% 重构误差；LLM 个案 95.24% 损伤识别准确率；作者明确限制这些不是普适性能保证。

### 引用分布

粗略引用分布显示：Introduction 8；Perception and actuation 15；Network/communication 7；Cognition 12；Transmission/storage/fusion 13；Distributed computing 14；Edge computing 24；AI-based approaches 14；若干 AI 子方法密集处约 27；Challenges 23；Potential enablers 12；References 总量约 157+。写作特点是“数据基础设施、edge computing、AI 子方法、挑战”处引用密度最高，应用任务小节引用相对较少。

### 写作规律

- 综述不是按传感器/算法清单排列，而是先提出统一 lens：ubiquitous computing and intelligence。
- 使用“三视角框架”消化跨学科内容：架构决定计算在哪里，算法决定如何推理，应用决定工程输出是什么。
- 把通信协议、资源约束、隐私治理、实时性和标准化写入正文，避免变成 MSSP 式算法综述。
- 对高性能数字保持克制：给出个案结果，同时说明不可普适化，这是 AEI review 中降低 overclaim 风险的写法。
- Discussion 不是泛泛未来展望，而是按 cost/resource、data quality、privacy/governance、real-time communication、scalability/adaptability、automation/interoperability 组织工程阻碍。

### 可用于我们论文哪个段落/claim

- **相关工作 claim**：SHM 正从 centralized data collection 向 edge-cloud distributed intelligence 转变，可用于说明数字孪生认知层不能只放在云端后处理。
- **体系结构 claim**：我们的 cognitive uncertainty DT 可借鉴 edge/fog/cloud 分层，把局部快速判断、区域融合和全局模型更新分开写。
- **不确定性 claim**：数据质量、资源约束、隐私共享、实时可靠性、非 IID 分布和模型迁移，是 SHM 信息链中的认知/信息不确定性来源。
- **综述写法 claim**：可借鉴 “unified lens + three-perspective framework + case table + engineering considerations” 来组织我们论文的相关工作或讨论段。

---

## 本组抽象：SHM 类 AEI 文章如何把数据/模型/监测变成 informatics

### 1. 先定义工程对象和服务任务，而不是先定义算法

AEI 的 SHM-DT 文章通常不以“我们提出一个信号处理算法”开场，而是先定义工程对象和服务任务：桥梁管理、水工钢结构维护、IoT-based SHM ecosystem。算法只有在回答状态感知、模型校准、故障诊断、健康评估、维护决策时才出现。

可写成：工程对象长期服役 -> 荷载/环境/运维复杂 -> 单一监测指标不足 -> 需要把多源数据、力学模型、知识规则和服务输出组织为可持续更新的信息系统。

### 2. 保持 source-response-state-decision 分层

GJJ 式链条在三篇中都很清楚：

- source/load：交通、温度、风、水压、动水、环境和运维操作。
- response：位移、应变、振动、倾角、频率、损伤特征。
- sensing/data：传感器、视频、PLC、IoT、协议、数据表、历史维护记录。
- representation/model：FEM/BRIM、PE/VE/DTD/CN/Ss、edge/fog/cloud、knowledge/AI models。
- decision/maintenance：关闭/限流/维修、启闭参数优化、健康等级、故障分类、维护计划。

关键写法是不要让“数据”直接跳到“决策”，中间必须有状态变量、表示结构、模型一致性或知识规则。

### 3. 把 representation 显式化，AEI 感才成立

三篇的 representation 不同，但都很显式：

- Sun et al.：FEM = mechanical twin，BRIM = data twin，IoT = connection。
- Li et al.：`PE, VE, DTD, CN, Ss` 五维 DT，且每个维度都有公式/表/字段。
- Cui et al.：architecture、algorithm、application 三视角框架，配合 edge/fog/cloud 和 data pipeline。

因此，我们论文若写“认知不确定性”，必须显式说明它被表示为什么：变量、证据项、置信度、知识节点、状态分布、模型残差、任务风险，或者决策约束。不能只说 uncertainty exists。

### 4. 数据操作要写成信息转换，而不是数据处理

AEI 文章常用的动作词是 conversion、expansion、fusion、integration、interaction、calibration、consistency verification、service encapsulation。它们对应信息学贡献：

- 稀疏响应 -> 荷载估计 -> 全场响应；
- 物理传感器 -> DTD 字段 -> 服务输入；
- 监测残差 -> VE 参数修正 -> 虚实一致性；
- 振动信号 -> 特征向量 -> 故障类型 -> 维护建议；
- edge 事件 -> fog 聚合 -> cloud 长期趋势与模型管理。

MSSP 式写法会停在 transform/classify/detect；AEI 式写法会继续说明这些结果如何进入模型、知识、平台和决策。

### 5. 图表证据要服务于链条

这类 AEI 文献常见高价值图表包括：

- 总体框架图：把 physical、cyber/model、data、service、decision 放在同一图。
- 数据流/工作流图：说明采集、传输、计算、融合、可视化、反馈的顺序。
- 模型层级图：粗细模型、多尺度模型、PE/VE、edge/fog/cloud。
- 字段/协议/服务表：证明系统不是概念图，而是可实现的信息系统。
- 案例对比表：把常规 SHM 与 DT-based SHM 在能力、效率、可靠性上对照。

我们论文应避免只放算法流程图；需要至少有一张“状态-证据-模型-决策”链条图。

### 6. 验证指标不只准确率，还包括一致性、延迟、可维护性和服务效果

三篇使用的证据类型包括：

- 响应重构误差、荷载识别误差、应变误差；
- 虚实一致性阈值、仿真-传感器相对误差；
- 模型参数优化前后误差降低；
- 误报减少、健康等级识别、维护响应时间降低；
- latency、processing time、power consumption、bandwidth/privacy trade-off；
- 案例结果的适用边界。

这提示我们：认知不确定性 DT 的验证不能只写预测精度，也应写不确定性是否改善了模型更新、状态解释、决策置信度或维护效率。

### 7. SHM-DT 进入 AEI 的一句话模板

可抽象为：

> The contribution is not a monitoring algorithm alone, but an engineering information chain that converts sparse, heterogeneous observations under uncertain loads into explicit state representations, synchronizes them with physics/knowledge models, and exposes decision-oriented services for inspection, maintenance, and risk control.

对应中文论文表达：

> 该类工作的工程信息学价值不在于单一监测算法，而在于将不确定荷载作用下的稀疏异构观测，转化为显式结构状态表征，并通过物理模型、知识规则和平台服务完成虚实同步、状态解释与维护决策。

