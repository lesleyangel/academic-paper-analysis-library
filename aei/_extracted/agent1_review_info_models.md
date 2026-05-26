# Agent 1 review notes: AEI literature on reviews and information models

资料来源：`_extracted` 下三篇 Elsevier AEI 论文的最新 `md/json/txt` 提取文件。本文只分析综述与信息模型组相关内容，重点观察 AEI 写法中“工程信息问题 -> 显式表征对象 -> 计算/更新流程 -> 场景证据 -> 工程输出”的链条。

## 1. Liu et al. (2023) - A systematic review of digital twin about physical entities, virtual models, twin data, and applications

### Bibliographic identity

- 文件：`1-s2.0-S1474034623000046-main`
- 期刊与编号：Advanced Engineering Informatics 55 (2023) 101876
- 题名：A systematic review of digital twin about physical entities, virtual models, twin data, and applications
- 作者：Xin Liu, Du Jiang, Bo Tao, Feng Xiang, Guozhang Jiang, Ying Sun, Jianyi Kong, Gongfa Li
- 关键词：Digital Twin; Physical entity; Virtual model; Twin data; Applications
- 文献类型：系统综述，面向数字孪生基本组成、应用场景与未来方向。

### Core content

本文的核心不是提出一个新模型，而是把数字孪生拆成三个可综述、可比较、可组织的基础对象：physical entities、virtual models、twin data。文章先通过数字孪生与 CPS 的差异澄清概念边界，再围绕三类组成要素梳理研究方法，最后把应用场景归纳为 design phase、operation process phase、dynamic interaction phase，并补充 food、agriculture、oil 等潜在应用。

从 AEI 角度看，本文的贡献在于把“数字孪生”这个大概念重新组织成信息模型研究可用的三层对象：实体选择与感知、模型范式与动态更新、数据采集与交换协议。它给 OIS/AEI 稿件的启发是：综述或引言不能只说 DT 很热，而要把 DT 的信息对象拆清楚，说明哪些信息被保留、哪些模型被更新、哪些数据通道实现物理-虚拟映射。

### Abstract logic

- 背景：数字孪生是智能制造和工业数字化转型的关键技术，已获得产业界与学界广泛关注。
- 问题：应用领域广泛导致参考模型和研究方法多样，基本组成部分缺乏系统整理。
- 对象：以 physical entities、virtual models、twin data 作为综述主线。
- 方法：分析 2017-2022 年 117 篇文献，并先澄清 DT 与 CPS 的关系。
- 内容展开：定义、特征、应用领域 -> 核心组成研究方法 -> 应用场景划分与潜力分析。
- 收束：给出研究结果和未来研究建议。

摘要写法上没有复杂结果数据，而是典型综述式“领域重要性 -> 多样性造成的整理需求 -> 文献范围 -> 分类维度 -> 输出”。可复用到我们的 OIS 综述段：先说明认知不确定性和观测信息结构在 DT/SHM/制造中的分散状态，再声明本文用某个结构化维度整理和重构。

### Conclusion logic

结论先复述数字孪生处在快速发展阶段，随后把全文贡献压缩为三点：

- 通过比较 DT 与 CPS，澄清 DT 的定义、特征和应用场景。
- 综述 physical entities、virtual models、twin data 的研究方法，包括物理信息获取、虚拟模型构建步骤、孪生数据获取和交换协议。
- 将数字孪生应用划分为设计、运行过程、动态交互三阶段，并通过新兴应用展示扩展潜力。

最后给出一个较强的领域判断：由于应用域多样，现有数字孪生参考框架和组成工具分散，缺少行业共识，因而需要面向多域数字孪生的通用软件平台，集成模型构建、测试和实施。

这类结论的写作规律是“总结分类贡献 -> 上升到领域瓶颈 -> 给出平台/共识/标准化未来方向”。它适合我们的综述组用来把文献归纳提升为 OIS 的必要性：现有 DT/信息模型各自有效，但缺少面向任务充分性的统一组织与审核结构。

### Section chain

- Introduction：从数字化转型与智能制造国家战略进入 DT；解释 DT 的三要素；用年度发文增长说明研究热度；引出已有综述的不足。
- Related review works：用表格比较已有综述的时间范围、文献数量、综述对象和结论，指出缺口是未强调 physical entities、virtual models、twin data 各自的研究方法，且应用综述偏向制造/工业。
- Purpose：列出四个目标：比较 DT/CPS，分析三要素，总结应用领域，提出未来方向。
- Research method：说明文献筛选标准、数据库、关键词、步骤；从 412 篇筛到 117 篇。
- Concept clarification：从 definition、core elements、virtual reality mapping method、application scenario 四方面区分 DT 与 CPS。
- Current development of digital twin components：主体综述三要素。物理实体关注定义、选择与信息感知；虚拟模型关注建模范式、变体、领域模型、动态更新；孪生数据关注采集与交换协议。
- Digital twin application scenarios：从 193 篇应用论文中提取 16 个应用领域，再归并为三阶段。
- Observations and recommendations：给出概念多样化、虚拟模型核心性、应用概念阶段、轻量建模、ML/DL 结合、3D 点云建模等观察。
- Conclusion：贡献压缩与未来平台化需求。

### Figure/table/formula evidence

- Fig. 1：年度发文数量。用于支撑“2017 年后快速增长、2021 年超过 800 篇、2022 年预计超过 1000 篇”的研究热度判断。
- Fig. 2：literature review methodology。对应文献收集、筛选、分类的三步流程，是综述可信度证据。
- Table 1：已有 DT 综述比较。用 timeframe、number of papers、object、key findings 显示本文综述定位差异。
- Table 2：文献收集方法。给出 time span、database、keyword、article type。
- Fig. 3/Fig. 4：国家与期刊分布。支撑 DT 研究地域与期刊集中度判断。
- Table 3/Table 4：DT 与 CPS 定义比较。支撑概念澄清。
- Fig. 5：三要素研究分布。显示 virtual models 占比最高 45.45%，physical entities 占比最低 21.59%。
- Fig. 6：physical information perception method。把环境、操作人员、设备工况等感知对象可视化。
- Fig. 7：virtual model component paradigms。对应几何、物理、行为、规则模型范式。
- Fig. 8：general steps of virtual model construction。把功能需求、范式适配、模型增删、模型构建组织成流程。
- Fig. 9-Fig. 13：数据构建、PLC/云平台、OPC UA、MTConnect 等数据通道证据。
- Table 5：部分数据交换协议，包括 TCP/IP、MQTT、AMQP、OPC UA、oneM2M、XMPP、MTConnect、Automation ML。
- Fig. 14-Fig. 16：应用领域数量、三阶段应用分割、其他应用领域。
- 公式：本文几乎没有方法公式，证据以统计图、分类表和流程图为主。

### Citation distribution

粗略统计：参考文献约 180 条，正文引用标记约 280 处。引用高度集中在 Introduction、Related review works、三要素综述和应用分类部分。方法部分主要引用较少，依靠筛选流程和表格说明可信度；结论基本不再引入新文献。

分布规律：

- Introduction 用高密度引用建立 DT 历史、制造数字化背景、三要素来源。
- Related review works 用表格驱动引用，服务于“已有综述不足”的定位。
- Component review 中按主题小节引用，每个小节由代表性方法串联。
- Application scenarios 中引用呈领域簇状分布，例如 design、fault diagnosis、medical、monitoring 等。
- Conclusion 不再堆引用，而把文献归纳转成未来研究建议。

### Reusable writing patterns

- 标题：`A systematic review of [broad technology] about [component A], [component B], [component C], and [applications]`。标题直接暴露综述维度。
- 综述缺口句式：已有综述已经讨论 concept/technology/application，但未强调核心组成要素各自的研究方法，也忽略潜力领域。
- 分类句式：先说明筛选范围和阈值，再给出分类结果，最后解释每类模型特征。
- 图表嵌入方式：每个分类判断尽量配一个表或图，而不是纯文字归纳。
- 未来方向写法：从现象性观察转成“common platform / lightweight modeling / ML-DL integration / point cloud construction”等可执行研究方向。

### How it can support our OIS/AEI manuscript

- 支持引言背景：可引用其 DT 三要素框架，说明 OIS 不是泛泛增加传感数据，而是重新组织 physical entity、virtual model、twin data 之间的任务相关信息。
- 支持综述框架：可借鉴“三要素 + 应用阶段”的分类方式，把 OIS 放在“信息是否足以支撑特定任务”的更细层。
- 支持问题定义：文章指出 DT 领域缺少共识平台和统一工具，我们可进一步缩小到“缺少观测信息结构对任务充分性、认知不确定性和模型更新能力的显式表达”。
- 支持写作证据：我们需要像该文一样把分类维度图示化，例如 OIS 中的观测对象、特征、模型映射、任务输出、认知不确定性来源。

## 2. Jiang et al. (2023) - Multi-domain ubiquitous digital twin model for information management of complex infrastructure systems

### Bibliographic identity

- 文件：`1-s2.0-S1474034623000794-main`
- 期刊与编号：Advanced Engineering Informatics 56 (2023) 101951
- 题名：Multi-domain ubiquitous digital twin model for information management of complex infrastructure systems
- 作者：Yishuo Jiang, Ming Li, Wei Wu, Xiqiang Wu, Xiaoning Zhang, Xinyan Huang, Ray Y. Zhong, George G.Q. Huang
- 关键词：Digital twin; Ubiquitous model; Information management; Industrial infrastructure systems; Transdisciplinary management; Domain-Driven Design (DDD)
- 文献类型：信息模型/参考模型论文，面向复杂基础设施跨场景、多域信息管理。

### Core content

本文提出 Ubiquitous Digital Twin (UDT) model，用于复杂工业基础设施系统的信息管理。它的关键不是提高某个预测指标，而是用 Domain-Driven Design 把数字孪生系统描述为六个域：geometry、structure、data、interaction、application、timespan。其中 geometry、structure、data 被称为 sequential-attribute domains，interaction、application、timespan 被称为 parallel-attribute domains。

文章用一个智慧核电站场景进行分层实例化：水泵用于设计与部署阶段，装配式建造用于施工阶段，智慧核电站系统用于运维阶段。每个实例都用 UDT 六域配置表达，并通过雷达图、类图、FSM、轨迹/调度公式、LSTM 预测等展示模型如何承载信息管理任务。

从 AEI 角度看，这是一篇高贴合的信息模型论文：工程任务是复杂基础设施信息管理；知识/信息表征是六域 tuple；工程使用是统一描述、跨团队共享理解、跨场景复用、监测/控制/预测；证据是三个层级场景实例和与已有 DT 模型的比较。

### Abstract logic

- 背景：数字孪生是对象或活动的综合数字等价体，通过虚拟模型和数据反映语义、几何属性与行为。
- 应用域：DT 和相关信息技术被用于基础设施建造、运行与维护。
- 问题：长期、跨场景管理涉及多学科利益相关者，经验、知识、利益差异导致冲突。
- 深层缺口：伴随数字孪生变化传播，网络-物理资源无法通过选择性简化和结构化方法，被高效、一致地建立、连接和利用。
- 方法：提出基于 DDD 的 UDT 模型，用于复杂基础设施系统信息管理。
- 表征：用六个域和顺序/并行 tuple 实现整体系统框架或功能模块的统一结构化描述。
- 证据：用一个智慧核电站管理场景中的三个案例进行层级实例化。

摘要六步非常 AEI：先定义信息对象，再说明工程管理场景，再指出利益相关者/跨域资源冲突，随后给出表征模型和案例证据。我们的 OIS 摘要可借鉴此结构：先定义 OIS 是面向任务的观测信息表征，再指出 DT/SHM 在部署后会遭遇信息不充分与认知不确定性，再提出结构化审计/诊断框架。

### Conclusion logic

结论按照“模型 -> 路线图 -> 案例 -> 贡献 -> 局限”展开：

- 提出 UDT 模型，用于复杂工业基础设施系统跨场景、多域数字孪生的统一简化和结构化描述。
- 基于 DDD 部署六个域，每个域具有顺序或并行集合，以支持对整体系统或功能模块的共享理解。
- 给出协同设计、开发、部署与实施路线图。
- 用水泵、装配式施工、智慧核电站三个层级案例展示 IoT-enabled self-detection 和 AI-enabled self-optimization 服务。
- 贡献总结为：统一参考规范与描述方法；支持多学科技术团队协作信息管理；为 Construction 4.0 中智慧设施 DT 信息管理提供理论和实践基础。
- 局限包括：自动控制和执行仍弱，D2P bridge 受阻；各阶段连接和通信没有充分探索；近实时融合、集成和可视化海量异构数据仍具挑战。

结论的写作规律是把“模型定义”转为“管理能力”，再用局限保护贡献边界。对我们的文章有启发：OIS 不能只说提高可解释性，要明确输出是 unsupported task、information sufficiency report、redesign candidates 或 uncertainty diagnosis。

### Section chain

- Introduction：从复杂基础设施信息管理需求进入，强调海量异构数据、多学科功能需求和复合结构；再引出 DT 在基础设施中的作用；最后提出缺少 domain-driven model、跨场景资源复用差、工业案例缺失三类缺口。
- State of the art：综述基础设施信息管理、DT/CPS/digital shadow/digital thread、5D-DT、DTaaS、biomimicry DT、Skin Model Shapes 等参考模型，最后收束到 selective simplification 和 structural description。
- UDT model：定义 UDT = {G,S,D,I,A,T}，并逐一定义六个域和内部 tuple。该节是全文表征核心。
- UDT-based instantiations：分三层实例化智慧核电站场景。每个实例用六域 tuple 配置，并说明不同场景的几何粒度、结构层级、数据状态、交互模式、应用目标和时间属性。
- Discussions：比较 UDT 与 5D-DT、C2PS、DTaaS、Biomimicry DT；用 generality、usability、maintainability 评价 UDT 质量。
- Conclusion and future research：压缩贡献与局限。

### Figure/table/formula evidence

- Fig. 1：UDT 六域模型。用雷达图表达六域 tuple，是全文的总表征图。
- Definition 1：`UDT = {G,S,D,I,A,T}`。六域分别为 geometry、structure、data、interaction、application、timespan。
- Definition 2：geometry domain 五元组 `{GP, GD, GF, φG, δG}`，把位置性、可展示性、细粒度和两类转换函数纳入几何域。
- Definition 3：structure domain 六元组 `{SI, SS, SMS, R, HS, NHS}`，区分个体、系统、多系统、关系、层级关系与非层级关系。
- Definition 4：data domain 五元组 `{DM, DI, DK, μD, ηD}`，对应 metadata、information、knowledge 及从元数据到信息、信息到知识的转换。
- Definition 5-7：interaction、application、timespan 域分别描述 M2M/H2M/HI，computing/rendering/integrated application，historical/real-time/predictive 及预测函数。
- Fig. 2：智慧核电站 HUALONG One 的 DT-enabled information management 场景总图。
- Fig. 3/Fig. 4：水泵实例，展示细粒度结构件、IoT 测点和 FSM 实时状态。
- Formula (2)：水泵实时状态 FSM `TR = {S, Σ, δ, sO, sF}`，把状态、输入、转移、初始/终止状态形式化。
- Fig. 5/Fig. 6：装配式施工实例与信息管理系统框架。
- Formula (4)：预制构件空间-时间轨迹 `Tra(Ci)`，把构件流经多个阶段的入/出时间和等待关系串起来。
- Formula (5)：构件-车辆分配关系，`rij=-1/0/1` 表示未分配、待定、已分配。
- Fig. 7：UDT 与 OPSE 的机器人试验床性能比较，包括 holding time 与 construction progress。
- Fig. 8-Fig. 11：智慧核电站运维、骨架图、增强可视化 DT、LSTM 预测维护模型。
- Table 1：机器人试验床不确定性生成参数。
- Table 2：UDT 与 5D-DT、C2PS、DTaaS、Biomimicry DT 的比较，按 key components、key functions、key characteristics 对照。

### Citation distribution

粗略统计：参考文献约 57 条，正文引用标记约 100 处。引用主要集中于 Introduction 和 State of the art，方法模型节引用较少，更多依靠定义、tuple、公式和图示自证。实例化和讨论部分引用很少，证据由案例、实验和模型比较承担。

分布规律：

- Introduction 引用基础设施信息管理、DT、数字化转型、跨学科协作。
- State of the art 是引用最高密度区域，集中建立相邻模型谱系：CPS、digital shadow、digital thread、5D-DT、DTaaS 等。
- UDT model 基本以定义和形式化表达推进，不依赖大量引用。
- Instantiation 部分让图、公式、案例数据替代引文，体现 AEI 中“模型输出要落到工程场景”。
- Discussion 中少量引用用于对比已有 DT 模型。

### Reusable writing patterns

- 标题：`[Representation scope] digital twin model for [engineering task] of [complex domain]`。模型对象、任务、场景三者完整。
- 引言缺口三连：缺少 domain-driven model；复用率低、成本高；缺少工业案例。
- 方法节写法：先定义总 tuple，再逐个域定义子 tuple，最后把计算/预测公式嵌入信息域和时间域。
- 案例节写法：同一模型在不同尺度和阶段重复实例化，形成“模型泛化能力”的证据。
- 讨论节写法：先与经典模型比较，再从 generality、usability、maintainability 三个软件质量属性评价。

### How it can support our OIS/AEI manuscript

- 支持 OIS 的 AEI 定位：可借鉴其“表征对象 + 工程管理任务 + 场景实例”的结构，把 OIS 写成任务导向观测信息表征，而不是传感器布置或不确定性指标。
- 支持方法建模：六域 tuple 的写法启发我们用显式元组定义 OIS，例如 observation object、feature/state variable、model mapping、task/QoI、uncertainty status、diagnostic output。
- 支持案例论证：一个模型最好在多个层级或任务上实例化，而不是只给一个指标。可设计 composite/structure monitoring 中的不同任务层级来展示 OIS 的复用。
- 支持讨论框架：可借用 generality、usability、maintainability，但需替换为 OIS 更贴切的 sufficiency、traceability、diagnosability、redesignability。

## 3. Liu et al. (2023) - A dynamic updating method of digital twin knowledge model based on fused memorizing-forgetting model

### Bibliographic identity

- 文件：`1-s2.0-S1474034623002434-main`
- 期刊与编号：Advanced Engineering Informatics 57 (2023) 102115
- 题名：A dynamic updating method of digital twin knowledge model based on fused memorizing-forgetting model
- 作者：Shimin Liu, Pai Zheng, Liqiao Xia, Jinsong Bao
- 关键词：Digital twin; Knowledge modeling; Knowledge graph; Dynamic update of knowledge
- 文献类型：知识模型与动态更新方法论文，面向 DT-based manufacturing system 中资源与过程知识管理。

### Core content

本文面向复杂产品定制制造中的数据冗余、知识浪费和动态过程管理困难，提出基于 fused memorizing-forgetting model (FMFM) 的 digital twin knowledge model (DTKM) 动态更新方法。文章先用知识图谱构建资源、工艺流程和制造数据的多层表征，再用记忆-遗忘机制对知识进行动态激励、融合、更新和淘汰，最后用船舶分段制造车间验证建模、查询、更新和知识淘汰效果。

核心链条是：复杂定制生产带来 DT 数据爆炸 -> 需要把数据转成可复用、可更新的知识 -> DTKM 将静态资源知识与时序过程知识图谱化 -> FMFM 根据重复频率、时效性、新旧知识关联进行更新 -> 原型系统在船舶分段制造中验证二级更新、查询效率和过时知识删除。

从 AEI 角度看，本文不是单纯知识图谱论文，而是“动态知识表征 + 更新机制 + 制造过程信息管理”的工程信息学论文。它最值得我们借鉴的是把认知/记忆类概念落成可计算公式、算法和图谱更新输出。

### Abstract logic

- 背景：复杂产品定制制造具有随机性和动态性，海量信息积累造成高数据管理成本和数据浪费。
- 强化问题：DT-based workshop 的高保真、强交互机制产生更多数据，加剧管理难度。
- 挑战：复杂制造过程与动态批量生产共同造成 DT 数据管理挑战。
- 方法：提出基于 memorizing-forgetting model 的数字孪生知识更新方法。
- 表征：先提出多层表示模型，融合 product、process flow、manufacturing data。
- 更新：提出 FMFM 对数字孪生知识进行动态更新。
- 证据：以 ship block manufacturing 为例，通过资源和过程知识的可视化分析证明建模与融合分析有效。
- 工程价值：支持车间资源与制造过程精细控制，并提升海量加工数据使用效率。

摘要的写作规律是“复杂制造场景 -> 数据/知识管理痛点 -> 表征模型 -> 更新机制 -> 案例验证 -> 管理价值”。我们的 OIS 摘要可借鉴“高保真 DT 反而加剧信息管理难度”的反直觉问题意识：更多观测并不自动等于更低认知不确定性，关键是任务相关信息如何被结构化、更新和淘汰。

### Conclusion logic

结论围绕数据冗余和知识浪费问题重申 FMFM 更新方法，并把贡献压缩为两点：

- 提出 DTKM 多层表征模型。基于制造车间资源、过程和数据分析，用模块化知识上下文描述实现统一表征、管理和维护，提高知识复用性。
- 提出 FMFM 动态更新 DTMS 知识。通过长时记忆、感觉记忆和短时记忆之间的激励与融合机制，在任务积累过程中动态更新知识库，保证知识模型的时效性和准确性。

随后说明原型系统帮助管理者快速准确掌握制造过程信息状态，降低人工成本、提高生产效率，并承认局限：尚未验证多模态知识模型，未来需要研究 multimodal KG；HRC 制造过程中的知识更新也是未来方向。

这类结论的关键是“方法机制 -> 知识质量属性 -> 管理效果 -> 未覆盖数据类型”。对 OIS 有用的是把局限写成信息模态和场景边界，而不是泛泛说 future work。

### Section chain

- Introduction：从 DT 虚实交互与 DTMS 应用进入；转向定制制造导致数据、模型、计划、报告积累；提出数据爆炸、重复知识占用空间、数据低利用三类问题；最后引出 KG 多层表征和 FMFM。
- Related work：先综述 DT knowledge modeling and updating，再综述 dynamic update method of knowledge，最后明确两个 research gaps：DTMS 数据/知识冗余与低效利用；动态制造知识需要随时间演化且旧知识要被识别删除。
- Knowledge acquisition：提出 DTKM 概念，定义静态与时序知识集合；构建 ontology-based multi-level representation model；说明资源和过程知识的获取与自动图映射。
- Dynamic update：构建 FMFM，定义记忆强度、初始激励、重复激励、相似度匹配、图实例融合和两个算法。
- Case study：以船舶分段制造车间为例，介绍流程、硬件/软件部署、可视化系统、KG 生成更新、分段工艺模型、查询与更新时间比较、记忆强度变化。
- Discussion：总结更新耗时约 128.4 s，约为制造时间的 1/5；查询和更新满足现场应用需求；过时 knowledge A 在阈值以下被删除。
- Conclusion：贡献、工程价值、局限与未来方向。

### Figure/table/formula evidence

- Fig. 1：CMFM 与 IMFM 对比。用于说明已有记忆-遗忘模型的不足。
- Fig. 2：processing knowledge dynamic renewal。显示 knowledge acquisition 与 knowledge fusion/update 两个模块协同。
- Fig. 3：DTKM 组织形式。将 DTKM 定义为带方向、节点标记和边标记的多图。
- Formula (1)-(5)：定义 `DTKM = <E,R,S,T>`，其中 E 为实体集，R 包含静态关系 `Rs` 和时序关系 `Rt`，S 包含静态知识 `Ss` 和时序知识 `St`，T 为时间信息集合；静态和时序三元组分别形式化。
- Table 1：semantic relations 定义，包括 FlowTo、Has、HasPart、Is、Involved:T、HasWork:T 等，是图谱语义关系证据。
- Fig. 4：ontology-based multi-level representation model。采用 root/branch/leaf 层组织资源与过程知识。
- Fig. 5：process resource and process knowledge acquisition and automatic graph mapping process。说明从加工任务数据流、产品设计数据、车间历史数据中获取知识，并映射为静态网络和动态图实例。
- Fig. 6：FMFM 总图。划分 sensory、short-term、inherent、learning memory。
- Formula (6)-(7)：记忆强度衰减微分方程与指数衰减形式，`dXi(t)/dt = -KiXi(t)`，`Xi(t)=Ci e^{-Kit}`。
- Formula (8)-(11)：初始激励、重复激励和综合记忆强度更新。
- Formula (12)-(15)：候选实体匹配，包含 Levenshtein 距离、归一化距离、语义相似度和混合相似度 `SimS`。
- Algorithm 1：knowledge forgetting algorithm。当记忆强度低于阈值时删除，重现或复用时按不同系数更新。
- Algorithm 2：production process dynamic knowledge updating。将短时记忆转成融合记忆矩阵，匹配感觉记忆，连接固有记忆，再转成学习记忆。
- Fig. 9/Fig. 10：船舶分段制造流程与车间数据流。
- Fig. 11：资源与过程知识可视化分析系统。
- Table 2：切割站一天加工数据流。
- Fig. 12/Table 3：AB01C-4F5 分段模型、BOM/工艺信息示例。
- Table 4：静态知识库和时序知识库节点/边分布。静态资源知识库总节点 4072、关系 3626；时序知识库总节点 2590、关系 3932。
- Formula (16)-(19)：KG 更新总时间、产品质量知识模型生成时间、实体查询时间、关系查询时间。
- Fig. 14：传统方法与本文方法的更新时间/查询时间比较。
- Fig. 15：不同知识元素记忆强度比较，展示过时知识 A 在第 147 天低于 0.1 阈值后被删除。

### Citation distribution

粗略统计：参考文献约 55 条，正文引用标记约 99 处。引用集中在 Introduction、Related work 2.1 和 2.2，之后方法节引用少，主要依靠定义、公式、算法和案例数据。结论仅少量引用 HRC 未来方向。

分布规律：

- Introduction 用引用建立 DTMS、定制制造、数据管理困难背景。
- Related work 分两条线密集引用：DT knowledge modeling/update 与 knowledge dynamic update/memorizing-forgetting。
- Research gap 单独成节，把引用综述转成两个明确缺口。
- Method 中引用只用于模型来源，主体由公式和算法推进。
- Case/Discussion 以系统实现和数值证据为主，避免把案例写成二次综述。

### Reusable writing patterns

- 标题：`A dynamic updating method of [knowledge/model object] based on [mechanism]`。直接暴露对象与机制。
- 引言问题三分法：数据爆炸；重复/相同知识占用空间并增加成本；信息只是记录存储、利用效率低。
- 缺口段写法：先总结已有方法能做什么，再指出“不能满足 DTMS 中复杂多模态信息和动态生产”的场景差异。
- 方法链条：定义知识模型 -> 定义记忆机制 -> 定义相似度与融合 -> 给算法 -> 给案例系统。
- 结果解释：先读图表定量现象，再给管理含义，例如更新时间满足工序间隔、查询满足现场应用、重复使用知识被保留。
- 局限写法：只验证结构化数据，多模态知识模型尚未验证；未来扩展到 HRC。

### How it can support our OIS/AEI manuscript

- 支持“认知不确定性不是静态误差”的论证：该文把知识时效性、重复使用频率、新旧知识融合写成动态机制。OIS 也可把观测信息充分性写成随任务、模型和数据流变化的状态。
- 支持知识/信息更新模块：FMFM 的写法启发我们区分 retained information、outdated observation、task-relevant evidence、uncertain inference，并给出更新/遗忘/触发机制。
- 支持图谱表达：DTKM 的静态关系和时序关系可借鉴为 OIS 中的结构关系与观测时序关系。
- 支持验证设计：需要不仅展示预测效果，还要展示信息结构带来的查询、诊断、更新和淘汰能力。
- 支持 AEI 贡献措辞：从“提出算法”改写为“提出用于统一表征、维护和更新任务相关观测知识的模型，支持工程决策中的信息可追踪与认知不确定性管理”。

## 4. Group-level common patterns for review and information-model papers

### 标题风格

- 综述型标题常用 `A systematic review of X about A, B, C, and applications`，用 about 后的对象列出综述坐标系。
- 信息模型型标题常用 `[model/framework] for [engineering task] of/in [domain]`，其中 `for information management`、`for complex infrastructure systems` 直接显示 AEI 任务。
- 动态更新型标题常用 `A dynamic updating method of [knowledge model] based on [mechanism]`，对象和机制都出现在题名中。
- 对我们的 OIS 题名启发：标题应包含 `observation information structure` 或 `task-oriented observation representation`，再接 `for cognitive uncertainty diagnosis / information sufficiency assessment in engineering digital twins`，避免只写 digital twin 或 uncertainty。

### 摘要六步

- Step 1 背景对象：说明 DT、复杂基础设施、定制制造或智能制造的数字化背景。
- Step 2 工程问题：强调多域、多源、多阶段、多利益相关者、动态生产或数据积累造成的信息管理困难。
- Step 3 信息层缺口：指出缺少显式组成整理、统一结构化描述、动态知识更新或任务相关信息利用。
- Step 4 方法/表征：提出 review framework、UDT 六域模型、DTKM/FMFM 等可命名对象。
- Step 5 证据：给出文献数量、筛选范围、场景实例、原型系统、图表/算法/性能比较。
- Step 6 工程价值：落到共享理解、复用、实时监测、动态控制、精细管理、知识质量或未来平台化。

对 OIS 摘要可压缩为：DT/SHM 需要任务可靠决策 -> 更多传感与模型并不保证信息充分 -> 缺少能表达观测对象、特征、模型映射、任务输出和认知不确定性的结构 -> 提出 OIS/audit workflow -> 用案例展示 unsupported task、uncertainty diagnosis、redesign output -> 支持工程数字孪生的信息可追踪与任务适配。

### 引言逻辑

- 先从工程数字化与复杂系统管理需求进入，而不是直接讲算法。
- 第二层强调信息问题：异构数据、跨域资源、模型更新、数据冗余、知识浪费、虚实映射不一致。
- 第三层回顾相邻技术：DT、CPS、digital shadow、digital thread、5D-DT、KG、ontology、Bayesian/dynamic update 等。
- 第四层明确缺口：现有研究不是没有模型，而是缺少某种“任务导向、跨域一致、动态更新、可复用”的信息组织方式。
- 第五层给贡献：表征对象、工作流、场景验证、工程输出。

GJJ 式判断：引言必须保持“对象-变量-映射-输出”分层。不要把 sensor、DT、uncertainty、knowledge graph、decision support 混成概念清单。每个背景对象都要说明它后面如何进入 OIS：作为观测源、模型状态、任务变量、认知不确定性来源，还是决策输出。

### 方法/结果结构

- 综述文：方法证据是检索策略、筛选流程、分类标准、图表统计和已有综述对照。结果结构是概念澄清 -> 组成要素 -> 应用场景 -> 观察建议。
- 信息模型文：方法证据是 tuple/definition/schema/workflow。结果结构是模型定义 -> 分域解释 -> 分层实例化 -> 与已有模型比较 -> 质量属性评价。
- 动态知识文：方法证据是 KG/ontology、时序关系、记忆强度公式、相似度匹配、算法。结果结构是系统实现 -> 数据/节点/边规模 -> 更新/查询时间 -> 知识淘汰机制 -> 管理意义。
- 对 OIS：方法节建议分开写 representation 和 computation。先定义 OIS 的实体、关系、任务和输出，再把 Fisher/CRLB、uncertainty metric、sensor placement 或 diagnostic algorithm 放进工作流中。

### 常用词句

- 工程信息任务：information management, decision support, refined control, real-time monitoring, dynamic control, predictive maintenance, shared understanding, cross-domain collaboration。
- 表征对象：physical entity, virtual model, twin data, metadata, information, knowledge, semantic relation, tuple, domain, ontology, knowledge graph。
- 结构化动作：unified and structured description, selective simplification, formalized definition, multi-level representation, automatic graph mapping, dynamic updating。
- 证据动作：instantiated, evaluated, compared, validated, demonstrated, visualized, queried, updated。
- 质量属性：generality, scalability, usability, maintainability, timeliness, accuracy, reusability, traceability。
- 缺口表达：lack of domain-driven models; poor reusability; lack of shared understanding; cannot be efficiently and consistently established, connected, and utilized; data redundancy and knowledge waste; not sensitive to timeliness。
- 结论表达：the proposed model provides a unified reference specification; the mechanism ensures timeliness and accuracy; the system helps managers quickly grasp process information; future work should address multimodal data and near-real-time fusion。

### 对我们 OIS/AEI 稿件的合并启发

- OIS 应被写成一种“任务导向观测信息表征”，不是传感器集合、特征集合或不确定性指标集合。
- 我们需要显式区分 source quantity、response quantity、observed feature、state variable、task/QoI、decision output。GJJ 式链条可以写成：观测源 -> 特征/状态表征 -> 模型映射 -> 认知不确定性诊断 -> 信息充分性判断 -> 传感/模型重设计建议。
- 图表证据至少需要三类：OIS schema 表、workflow 图、case audit/report 输出。仅有误差曲线不够 AEI。
- 引用分布建议：Introduction 和 Related Work 承担 DT/SHM/KG/uncertainty/decision support 的引用密度；Method 少量引用标准和关键模型；Case 主要靠输出报告和对比图表。
- 写作上要把“uncertainty”从抽象名词落到对象：是哪一类任务信息不足、哪一个映射缺失、哪一个状态变量不可辨识、哪一种观测无法支撑决策。

