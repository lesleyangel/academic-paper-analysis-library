# Agent 4: Cross-paper AEI writing patterns for digital-twin / semantic-representation papers

本文件基于 `_extracted` 下 10 篇 AEI 论文的最新 `.md/.json` 抽取结果，并在需要判断 gap、contribution、case-study、discussion 写法时参考对应 `.txt` 原文上下文。目标不是总结论文主题，而是沉淀可迁移的 AEI 写作结构：怎样把 digital twin、knowledge graph、semantic model、SHM、workflow、case study 写成 AEI 喜欢的“representation + workflow + engineering task + evidence”。

## 0. 样本文献类型速写

为便于后文引用，10 篇文章可分成 5 类。

| ID | 标题/对象 | 类型 | 结构重心 |
|---|---|---|---|
| P1 | systematic review of digital twin about physical entities, virtual models, twin data, and applications | DT 综述 | 用 review methodology、component taxonomy、application taxonomy 建立领域地图 |
| P2 | Multi-domain ubiquitous digital twin model for information management of complex infrastructure systems | UDT 信息管理模型 | 六域 tuple representation + 多场景 instantiation |
| P3 | dynamic updating method of digital twin knowledge model based on fused memorizing-forgetting model | DT knowledge updating | ontology/multi-level representation + memory-forgetting update + workshop case |
| P4 | Hybrid monitoring methodology: model-data integrated DT framework for SHM and full-field virtual sensing | SHM-DT 框架 | FEM/BRIM/IoT 三层 DT + hybrid monitoring equations + bridge case |
| P5 | A Semantic Digital Twin for the Dynamic Scheduling of Industry 4.0-based Production of Precast Concrete Elements | semantic DT for scheduling | AAS/RDF/ontology + scheduler service + proof-of-concept |
| P6 | Hydro-steel structure digital twins: application in SHM and maintenance of large-scale reservoir | SHM-DT 工程应用 | five-dimensional DT model + platform + real reservoir case |
| P7 | Semantic Digital Twins in Construction: modular SRA based on Information Containers | semantic DT architecture | SRA + AAS/ICDD alignment + semantic layer + simulated curing case |
| P8 | Digital twin-based assembly process framework utilizing STEP and knowledge graph | STEP + KG assembly framework | DT-APIM -> DT-APKG -> reasoning engine -> assembly query case |
| P9 | closed-loop design approach based on KG and DT: high-speed train bogie case | KG-DT closed-loop design | metamodel DT + KG mapping + PSO/model correction + optimization case |
| P10 | Edge-to-cloud computing and intelligence for IoT-based SHM: comprehensive review | SHM review | three-perspective analytical framework + architecture/algorithm/application taxonomy |

跨文共同规律：AEI 不奖励“我有一个算法/公式/优化结果”本身，而奖励“我把工程信息怎样表示、怎样连接、怎样被查询/推理/调度/监测/更新、怎样支撑工程任务”。算法和公式通常是 workflow 中的一个层，而不是论文身份。

## 1. 标题风格

### 1.1 常见语法骨架

标题通常由 3 到 4 个部件组成：

1. representation/workflow object：Semantic Digital Twin, digital twin framework, knowledge model, System Reference Architecture, assembly process framework, closed-loop design approach, edge-to-cloud computing and intelligence。
2. engineering task：information management, dynamic scheduling, structural health monitoring, maintenance, full-field virtual sensing, assembly process reasoning, closed-loop design。
3. method carrier：knowledge graph, STEP, AAS, ICDD, fused memorizing-forgetting model, model-data integrated framework, Domain-Driven Design。
4. application scene：complex infrastructure systems, precast concrete elements, hydro-steel structures, high-speed train bogie, IoT-based SHM。

可复用模板：

- `A/An [representation object] for [engineering task] of/in [domain object]`
- `[Method/workflow] for [engineering task] and [engineering output]`
- `[Representation object]: [application/task scene]`
- `[Task/workflow] based on [method A] and [method B]: a [case object] case study`
- `[Semantic/knowledge/information]-driven [framework/model/architecture] to enable [engineering use]`
- `[Model-data/edge-cloud/KG-DT]-integrated [framework] for [task] under [deployment condition]`

### 1.2 连接词规律

`for` 是最高频、最安全的 AEI 标题连接词。它把技术对象从“名词堆叠”变成“服务某个工程任务”：`A Semantic Digital Twin for the Dynamic Scheduling...`、`framework for structural health monitoring...`。OIS 论文应优先用 `for` 明确任务，如 `for auditing information sufficiency in engineering digital twins`。

`of` 用来限定对象、数据或生命周期范围，但单独使用容易变成泛泛主题。P1 的 `of physical entities, virtual models, twin data, and applications` 是综述式对象枚举；P5 的 `of Industry 4.0-based Production...` 是生产系统对象限定。OIS 标题中 `of` 适合放在后半段，如 `information sufficiency of sensing-feature pipelines`，不宜标题只写 `uncertainty of digital twins`。

冒号 `:` 常用于“主方法 + 具体 case/应用”的二段式标题。P9 用 `A closed-loop design approach based on ...: a high-speed train bogie case study`；P6 用 `Hydro-steel structure digital twins: Application in ...`。冒号后通常不是再讲方法，而是落到应用场景、case 或 paper type。OIS 可以用冒号，但冒号后必须给工程对象或部署场景。

`based on` 用于把方法来源放进标题，但 AEI 中它不能压过任务。P3/P9 都是 `based on ...`，但后面仍有 knowledge model updating 或 case study。OIS 若用 `based on Fisher information / observation information`，应写成 `An observation information representation for ... based on ...`，不要写成纯数学方法标题。

`using/utilizing` 用于工具性方法，常见于 P8 `utilizing STEP and knowledge graph`。语义是“我使用这些工具构造可运行信息系统”。OIS 可用 `using deployed sensing-feature pipelines` 或 `using task-oriented information distinctions`，但不要让 `using` 后面只接单一指标。

`to enable` 多用于架构/语义模型论文，强调 representation 的工程效用：to enable semantic interoperability, dynamic scheduling, feedback control, decision support。OIS 可用 `to enable task-level sufficiency auditing`。

`under` 适合表达部署约束、工况和不确定性：under deployed sensing pipelines, under post-deployment drift, under limited observability, under evolving operation conditions。AEI 喜欢这种“方法在真实约束下服务工程任务”的标题气质。

### 1.3 对象-方法-任务-场景顺序

最稳妥顺序是：`representation/workflow object -> task -> scenario`。例如 `A Semantic Digital Twin for the Dynamic Scheduling of ...`。这种顺序一眼告诉审稿人：论文不是算法炫技，而是工程信息对象支撑工程任务。

第二种顺序是：`task/workflow -> method -> case`。例如 P9 的 closed-loop design approach based on KG and DT。适合任务非常明确、工程案例有吸引力的文章。

第三种顺序是：`domain object -> DT application`。例如 P6。适合工程对象稀缺且案例强，但风险是标题像应用报告；需要在摘要/引言中迅速补上 representation 与 workflow。

OIS 标题建议：

- 强推荐：`A Task-Oriented Observation Information Structure for Auditing Engineering Digital Twins under Deployed Sensing Pipelines`
- 稍工程化：`Information-Sufficiency Auditing of Sensing-Feature Pipelines for Engineering Digital Twins`
- 强 AEI：`From Sensing Features to Task Support: An Observation Information Structure for Engineering Digital Twin Audits`
- 避免：`A New Criterion for Digital Twin Cognitive Uncertainty`，因为它像指标论文而不是 informatics paper。

## 2. 摘要结构

### 2.1 六步摘要骨架

10 篇样本中，完整 AEI 摘要通常有 6 个 move：

1. 背景句：工程系统正在数字化、互联、复杂化、实时化，或某一工程任务受到不确定性/多源数据/生命周期变化影响。
2. 缺口句：现有 DT/AI/SHM/调度/设计方法缺少显式信息组织、语义互操作、动态更新、任务级数据获取，或不能跨模型/数据/业务逻辑连通。
3. 方法句：本文提出 framework/model/architecture/approach，并明确 representation object。
4. representation/workflow 句：说明实体、关系、子模型、tuple、ontology、KG、AAS/ICDD、FEM/BRIM/IoT、query/reasoning/service 如何组成 workflow。
5. case/evidence 句：用 proof of concept、case-specific implementation、real reservoir project、bridge model、aero-engine casing、bogie case、117 articles、20+ case studies 证明。
6. 贡献/结论句：输出不是单一精度，而是 interoperability、information integration、dynamic feedback、uncertainty management、decision-making、maintenance efficiency、data integration efficiency。

### 2.2 背景句写法

背景不是“某方法很重要”，而是“工程任务变得依赖信息结构”。常见句式：

- `The construction industry is increasingly adopting Digital Twin technology to support design, construction, and operation...`
- `Precast concrete construction enhances efficiency..., still ... is subject to uncertainties...`
- `With the increasing complexity of industrial products, ... lifecycle closed-loop design ...`
- `SHM is experiencing a paradigm shift from reactive, human-dependent systems toward proactive, autonomous entities...`

OIS 可写：

- `Engineering digital twins increasingly couple sensing, simulation, and feature extraction pipelines to support task-specific decisions after deployment.`
- 中文逻辑：先讲“部署后的 DT 决策依赖观测信息能否保留任务区分”，不要先讲 Fisher information 或数学不确定性。

### 2.3 缺口句写法

AEI gap 不止是“accuracy low”。它通常是 information-level gap：

- P2：多利益相关方、跨场景、change propagation 导致 cyber-physical resources 不能被 consistent established, connected, utilized。
- P5：dynamic scheduling 需要 real-time production-relevant data，但现有 DS 很难贯穿生产过程获取/分析。
- P7：heterogeneous data sources 和 lifecycle requirements 会变，built environment 中 DT modules 的 clear definition and structure 缺失。
- P8：information silos 来自 assembly process 中 multi-source heterogeneous data 的 ineffective exchange。
- P9：multi-source data format/semantic inconsistency、model parameters dynamic updating、model-data associations mapping 困难。
- P10：既有综述 fragmented，没有用 unified lens 连接 IoT systems、AI methods、SHM applications。

OIS gap 要收束为：

- 不是“现有方法没有考虑认知不确定性”这么虚。
- 应写成“现有 DT sensing/feature pipelines 往往报告局部估计精度或预测误差，但缺少一种显式表示 task requirement、retained distinctions、observation pipeline 与 audit outputs 的结构，因此难以判断部署系统是否真正支持指定工程任务。”

### 2.4 方法句与 representation/workflow 句

样本中方法句几乎都不只说“we propose an algorithm”。它们会跟一句 representation/workflow 展开：

- P2：`UDT model` 后立刻说 `six domains`、`sequential or parallel tuples`、`shared understanding`。
- P5：`DS framework` 后立刻说 `Semantic DT based on AAS and Linked Data`、`RDF serialization`、`ontological representation`、`simulation-based scheduler`、`SPARQL`。
- P7：`modular SRA` 后立刻说 `AAS submodels`、`ICDD`、`semantic layer of ontologies`、`SPARQL and REST-based queries`。
- P8：`DT-APF` 后立刻说 `DT-APIM`、`DT-APKG`、`ASP reasoning engine`。
- P9：`closed-loop design approach` 后立刻说 `information model / mechanism model / field model`、`KG mediator`、`querying and reasoning`、`continuous feedback loop`。

OIS 摘要必须有类似一句：

`The structure represents asset states, deployed sensing pipelines, feature mappings, task schemas, operational resolution, retained task distinctions, information-folding witnesses, and audit outputs in a unified workflow.`

### 2.5 evidence 句写法

AEI evidence 不是必须大型真实部署，但必须清楚 evidence type：

- review：117 articles / 20+ case studies / bibliometric analysis。
- proof-of-concept：dynamic scheduling with disruptive events。
- simulated case-specific implementation：precast concrete curing process。
- physical model bridge：verification of hybrid DT。
- real project：Luhun Reservoir hydro-steel structure。
- industrial product case：aero-engine casing, high-speed train bogie。

OIS 可用分层 evidence：

1. controlled digital-twin pipeline：证明 OIS 从 feature 到 task support 的诊断链。
2. post-deployment drift audit：证明 local-global disagreement / information folding。
3. constrained public-data example：证明迁移性，但只说 `constrained demonstration`，不说 universal validation。

## 3. 引言结构

### 3.1 常见段落功能分布

AEI 引言通常 6-9 段，功能顺序稳定：

1. 工程背景段：领域复杂性、数字化趋势、DT/IoT/AI/SHM/Industry 4.0 的任务需求。
2. 工程瓶颈段：多源异构数据、生命周期变化、实时响应、模型更新、信息孤岛、跨利益相关方/跨系统互操作。
3. 相关研究概览段：DT、KG、semantic web、AAS、SHM、hybrid monitoring、scheduling、closed-loop design 已有进展。
4. 方法族局限段：现有方法强调模型、预测、优化、监测、可视化，但没有把数据/语义/任务/服务连成可重用 representation。
5. gap 收束段：明确 2-4 个 gap，常用 bullet 或 numbered list。P5/P7 都有 `identified research gaps`；P9 单独设 `Research gaps and motivations`。
6. proposed solution 段：本文提出何种 framework/model/architecture，承接 gap。
7. contributions 段：3-4 个贡献，每个贡献都是 artifact + engineering use + evidence。
8. organization 段：极短，Section 2 review, Section 3 model, Section 4 workflow, Section 5 case, Section 6 discussion/conclusion。

### 3.2 引文如何集中

引文的高密度通常出现在 Introduction 和 Related Work。样本的粗略引文分布显示：

- Introduction：通常 7-18 个 citation markers。P4 18，P9 15，P7 14，P2 13，P6 12。
- Related Work / State of the art：通常更密。P4 literature review 24，P8 literature review 25，P5 linked data and semantic DT 24、AAS 14、scheduling 15，P7 SRA/layered/component/SoA 架构共很高。
- Method：引用显著降低，更多依赖图、表、定义、公式、流程。方法中只引用标准、基础模型、关键技术来源。
- Case：引用很少，靠案例数据、图表、结果说话。
- Discussion：引用重新升高但少于 related work，用于定位贡献、限制和与领域趋势对话。P7 discussion 中 design rationale 引用较高。

OIS 引文策略：

- Introduction 用 20 左右 citation groups 覆盖 engineering DT、SHM/monitoring、uncertainty/identifiability、semantic/KG/representation、sensor placement/information criteria。
- Related Work 分 4 类，不按作者流水账：DT information management, semantic/knowledge representation, sensing-feature pipelines, information sufficiency/identifiability/audit。
- Method 不堆引文，只在 OIS 定义、Fisher/CRLB、KG/semantic comparison、audit workflow 基础处引用。
- Case 少引用，重点放图表、audit report、failure stage、redesign candidates。

### 3.3 gap 如何收束

AEI gap 收束常从“大而散”变成“可操作的信息缺失”。常见句法：

- `However, ... still faces limitations in ...`
- `Current studies mainly focus on ..., while ... remains insufficiently addressed.`
- `These limitations point to a fundamental gap: the absence of ...`
- `After a comprehensive analysis of ..., we identify the following research gaps:`
- `To address these issues, this paper proposes ...`

OIS 的 gap 不要停在“cognitive uncertainty is not well studied”。应收束为 3 个可被 OIS 解决的 gap：

1. Task gap：已有 DT 不显式表示任务所需区分、QoI、operation resolution。
2. Pipeline gap：已有 sensing/feature pipelines 不能说明信息在哪一层被折叠或丢失。
3. Audit gap：已有 numerical metrics 难以输出工程可行动的 unsupported tasks, witnesses, likely failure stage, redesign candidates。

### 3.4 contribution 写法

贡献 bullet 的 AEI 结构是：`We develop/formulate/implement/demonstrate + artifact + use`。避免只写 `we propose a new metric`。

OIS contribution 模板：

- `We formulate post-deployment information sufficiency as a task-oriented representation problem for engineering digital twins, rather than as a standalone numerical identifiability criterion.`
- `We develop an Observation Information Structure that links asset states, observation pipelines, feature representations, task schemas, retained distinctions, and audit outputs.`
- `We implement an audit workflow that reports unsupported task distinctions, near-folded witnesses, local-global disagreement, likely information-loss stages, and redesign candidates.`
- `We demonstrate the workflow through controlled DT pipelines and a constrained public-data example, clarifying what can and cannot be claimed from the available evidence.`

## 4. 章节结构模板

### 4.1 Review paper 模板

适用于 P1/P10。结构不是“主题随便分”，而是先给 review lens，再用 lens 组织文献。

模板：

1. Introduction：趋势、碎片化、需要统一视角。
2. Review methodology / analytical framework：数据库、时间范围、筛选标准、分类逻辑。
3. Concept clarification / data infrastructure：先定义核心概念和边界。
4. Component taxonomy：physical entity / virtual model / data，或 perception / network / cognition / data processing。
5. Paradigm or application taxonomy：centralized/distributed/cloud/fog/edge，或 design/operation/interaction phases。
6. Case studies / representative examples：不是逐篇罗列，而是把案例映射到 taxonomy。
7. Discussion：challenges, enablers, practical insights。
8. Conclusion：研究地图 + 未解决问题 + future directions。

OIS 若写相关工作综述部分，可借这个结构：先提出 `task-level information sufficiency` lens，再把 DT/KG/SHM/identifiability 文献按 lens 归类。

### 4.2 Framework paper 模板

适用于 P2/P4/P6。结构重心是“先定义组件，再定义连接，再定义运行流程，再验证”。

模板：

1. Introduction。
2. State of the art / literature review。
3. Framework/model definition：列出 dimensions/components/domains，如 PE/VE/DTD/CN/Ss，或 FEM/BRIM/IoT，或 G/S/D/I/A/T。
4. Operating workflow：perception -> interaction -> analysis -> decision，或 input -> data fusion -> model update -> visualization。
5. Case study：对象、系统、数据、建模、运行过程。
6. Application effects / discussion：对 conventional approach 的比较、平台功能、效率/响应/维护改进。
7. Conclusion and future work。

OIS 可对应：

1. OIS conceptual framework。
2. OIS representation schema。
3. Information sufficiency audit workflow。
4. Case study: deployed sensing-feature pipeline。
5. Audit outputs and redesign implications。
6. Discussion: relation to semantic DT/KG/sensor placement/numerical identifiability。

### 4.3 Semantic / KG paper 模板

适用于 P3/P5/P7/P8/P9。核心是“语义 representation 不是装饰，而是让工程数据能被 query/reason/update/control”。

模板：

1. Related work 分成 DT、semantic/KG/ontology、task domain 三组。
2. Research gaps 单独成节或小节。
3. Methodology：先说 development procedure，不急于结果。
4. Conceptual information model / ontology / KG schema：实体、属性、关系、submodels、competency questions、mapping rules。
5. Implementation：RDF/AAS/ICDD/SPARQL/REST/STEP/EXPRESS-G/GraphDB/ASP/PSO 等工具落地。
6. Service / reasoning / scheduling / feedback workflow：query 如何进入，结果如何回到工程任务。
7. Case study：用具体工业对象实例化。
8. Evaluation：query results、integration efficiency、schedule response、model correction、comparison table。
9. Discussion：interoperability、modularity、portability、limitations。

OIS 若不用完整 ontology，也要有 `representation schema table`，否则 AEI 审稿人会觉得是数值指标论文。可以把 OIS 看成轻量 semantic representation：entities = state/task/pipeline/feature/witness/output；relations = observes/maps-to/supports/folds/violates/recommends。

### 4.4 SHM-DT 模板

适用于 P4/P6/P10。SHM 类 AEI 文章的套路是“物理对象风险 -> monitoring data -> digital representation -> diagnosis/decision service”。

模板：

1. Introduction：安全、长期服役、恶劣环境、人工巡检/单一传感不足。
2. Related works：operational challenges, SHM applications, DT applications。
3. DT model：physical entity, virtual entity, DT data, connection, services。
4. Monitoring methodology：load estimation, data fusion, model updating, damage sensing, hybrid computing。
5. Platform/workflow：perception, interaction, analysis, decision。
6. Case：bridge/reservoir/gate/sensor layout/FEM/IoT system。
7. Results：monitoring, diagnosis, health assessment, maintenance optimization。
8. Discussion：real deployment constraints, model maintenance, data acquisition, service integration。

OIS 可借 SHM-DT 模板，但要避免变成 SHM 方法论文。重点放在“观测信息是否足以支撑任务”的 audit，而不是直接做 damage detection。

## 5. 图表结构

### 5.1 Framework figure

功能：第一眼把“工程对象-信息表示-计算/服务-输出任务”连起来。P2 UDT 六域模型、P4 bridge SHM DT framework、P6 five-dimensional DT model、P9 KG-DT closed-loop design 都承担这个功能。

OIS 必备 Fig. 1：

- 左：physical asset / operating state / sensing deployment。
- 中：observation pipeline：sensor -> signal -> feature -> model/update。
- 右：task schema / QoI / retained distinctions / audit report。
- 下：numerical diagnostic layers，如 Fisher/CRLB/support coverage/local-global disagreement。
- 输出：unsupported task, witness pairs, failure stage, redesign candidate。

### 5.2 Architecture figure

功能：说明系统如何部署，尤其 semantic DT / AAS / ICDD / service / database / API。P5 有 AAS + GraphDB + service application；P7 有 logical architecture、AAS/ICDD alignment；P4 有 FEM/BRIM/IoT；P6 有 platform architecture。

OIS 如果有原型系统，应画 architecture figure：

- Data layer：raw signals, simulation data, feature store。
- Representation layer：OIS schema, task schema, state set, pipeline graph。
- Audit layer：metric calculators, witness search, drift checker。
- Service/output layer：dashboard/report/recommendation。

### 5.3 Workflow table / algorithm table

功能：把抽象 framework 转成可复现步骤。样本中常见 workflow 是 stepwise：literature filtering steps、DT-based SHM operating process、methodology of AAS submodel modeling、DT-APIM -> DT-APKG conversion、closed-loop design process。

OIS 必备 table：

| Step | Input | OIS entity/relation updated | Diagnostic operation | Engineering output |
|---|---|---|---|---|
| Task encoding | QoI, decision threshold | Task schema | define retained distinctions | task requirement |
| Pipeline encoding | sensors/features/models | Pipeline graph | map observation transformations | deployed representation |
| Audit | state-feature responses | witness/support metrics | detect folding/disagreement | unsupported tasks |
| Redesign | audit report | recommendation relation | rank interventions | sensor/feature/model changes |

### 5.4 Case table

功能：把案例从叙述变成 evidence。P5/P7/P8/P9 常用 case tables 展示 requirements、queries、submodels、results、comparison。

OIS case table 应包含：

- engineering task
- asset/state variables
- sensing/feature pipeline
- task distinctions
- perturbation/drift setting
- audit output
- engineering interpretation

### 5.5 Comparison table

功能：不是简单列优缺点，而是证明本方法在 AEI 关心的维度上补 gap：interoperability, modularity, dynamic update, query/reasoning, task support, lifecycle feedback。

OIS comparison table 的列建议：

- Method family：prediction accuracy, sensor placement, semantic DT/KG, uncertainty quantification, OIS audit。
- Represents task requirements?
- Represents deployed observation pipeline?
- Reports information-loss stage?
- Produces engineering redesign candidates?
- Evidence type。

### 5.6 Figure/table 数量信号

样本中图表很重：P4 27 图、P6 37 图、P9 32 图；semantic 架构论文图少一些但每张承担 schema/architecture/alignment 任务。AEI 喜欢可视化 workflow 和 representation，不喜欢只靠文字解释抽象框架。

OIS 最低配置建议：6-8 图 + 4-6 表。

- Fig. 1 overall OIS framework。
- Fig. 2 representation schema / graph。
- Fig. 3 audit workflow。
- Fig. 4 local vs global sufficiency illustration。
- Fig. 5 case pipeline。
- Fig. 6 audit report / redesign loop。
- Table 1 related work comparison。
- Table 2 OIS entities/relations。
- Table 3 audit outputs and interpretation。
- Table 4 case settings。
- Table 5 comparison with baseline metrics。

## 6. 公式使用规律

### 6.1 AEI 中公式的角色

公式服务 representation/workflow，不抢主线。样本有三类公式：

1. Representation formulas：tuple、set、ontology-like definitions。P2 `UDT={G,S,D,I,A,T}`；P6 `DT-HSS={PE,VE,DTD,CN,Ss}`；P9 `DTMi={IM,PM,FM...}`。这些公式定义信息对象。
2. Workflow/computation formulas：data fusion、load estimation、model updating、memory-forgetting、mapping rules、optimization。它们说明一个环节如何运算。
3. Result/evaluation formulas：accuracy、time consumption、optimization objective、performance index。通常很少，不作为全文核心。

P4 和 P6 公式多，但文章仍有 DT framework、hybrid monitoring workflow、case platform。P5/P7/P8 公式少，靠 ontology/schema/query/service 也能成立。说明 AEI 不要求数学多，要求 representation 明确。

### 6.2 OIS 公式写法规则

OIS 可以有数学，但要按下面顺序：

1. 先定义 OIS tuple：`OIS = {X, Y, Phi, T, R, D, A}` 之类，明确每个符号是工程信息对象。
2. 再定义 task distinction / operational resolution / retained distinction。
3. 再放 Fisher/CRLB/support metric 作为 diagnostic layer。
4. 再定义 audit outputs：unsupported task set, witness pairs, disagreement index, failure-stage attribution。
5. 最后给 redesign ranking，而不是直接把优化目标当主贡献。

写作上每个公式后必须有一句工程解释：

- 不只说 `where ...`，还要说 `This relation is used to identify which task distinctions are no longer preserved by the deployed pipeline.`
- 不只报告 scalar score，要说明 score 如何触发 audit report。

### 6.3 数学红线

避免：

- 连续 2-3 页公式没有 framework figure/table。
- 摘要第一句就是 metric。
- 贡献写成 `we derive a new criterion`，但没有 representation schema、workflow、case output。
- 把 `validated` 建立在单一仿真上。

安全表达：

- `used as a diagnostic layer within the audit workflow`
- `formalizes the task-level information retained by a deployed pipeline`
- `reports engineering-facing audit outputs rather than replacing domain judgment`
- `demonstrated in controlled and constrained-data settings`

## 7. 引文分布规律

### 7.1 Section-level 密度

从 10 篇抽取结果看：

- Introduction：中高密度，通常 8-18 个 citation markers。作用是建立领域重要性、工程痛点和 gap。
- Related Work / State of the art：最高密度。P5 在 semantic DT/AAS/scheduling 等小节有 14-24 个 marker；P7 的 architecture 小节密集；P8 literature review 25。
- Method / Framework：低密度。P2 UDT model、P4 DT framework、P6 DT components、P9 KG mapping 多用定义、图、表、公式，而不是堆文献。
- Implementation / Case：低密度。引用只用于标准、工具、数据源或对比方法。
- Discussion：中低密度，用于和 previous studies、limitations、future development 对话。P7 design rationale 引用多，说明架构论文 discussion 可以回到文献定位。
- Review paper：主体各 taxonomy 小节都高密度，因为文章身份就是文献地图。

### 7.2 OIS 引文配置建议

OIS 不是 review paper，建议：

- Introduction：20-30 citation groups，覆盖 DT/SHM/engineering informatics、uncertainty/identifiability、sensing pipeline、semantic/KG/representation。
- Related Work：40-60 citation groups，按问题族组织，不按时间线。
- Method：8-15 citation groups，主要引用信息理论、DT representation、semantic/KG/audit 类基础。
- Case：3-8 citation groups，引用数据/benchmark/实验对象来源。
- Discussion：8-15 citation groups，对照 semantic DT、sensor placement、uncertainty quantification、engineering decision support。

### 7.3 引文句式

高密度段落常用“类群总结”而非逐篇复述：

- `Existing studies have explored ...`
- `Recent work has emphasized ...`
- `In the construction/manufacturing/SHM domain, ...`
- `However, these studies mainly ...`
- `Although ... has been addressed, ... remains less explicit.`

OIS 要避免每句一个作者。用 2-4 组 citation 支撑一个 problem family，然后用一句 gap 收束。

## 8. 常用词句

### 8.1 高频术语

AEI 安全高频词：

- representation, information model, semantic model, ontology, knowledge graph, submodel, schema
- framework, architecture, system reference architecture, workflow, pipeline
- interoperability, integration, mapping, alignment, modularity, reusability, scalability
- query, reasoning, updating, feedback, service, decision-making
- engineering task, requirements, lifecycle, deployment, case study, proof of concept
- heterogeneous data, multi-source data, real-time data, cyber-physical resources
- monitoring, diagnosis, assessment, maintenance, scheduling, optimization, visualization

OIS 专属建议词：

- observation information structure
- task-oriented information sufficiency
- deployed sensing-feature pipeline
- retained task distinction
- task-support coverage
- information-folding witness
- local-global disagreement
- audit output
- redesign candidate
- post-deployment drift audit

### 8.2 句式模板

背景：

- `As engineering systems become increasingly connected and data-intensive, [task] depends on [representation/use of information].`
- `Digital twins provide a bridge between physical operations and digital capabilities, but their engineering value depends on [task-level information use].`

gap：

- `However, existing approaches mainly emphasize [prediction/optimization/monitoring], leaving [representation/task-level information use] insufficiently explicit.`
- `This creates a gap between [local metric] and [engineering decision sufficiency].`
- `Without an explicit representation of [task requirements/pipeline/retained distinctions], [system] may appear informative while failing to support [task].`

method：

- `This paper introduces [framework/model/structure] for [engineering task].`
- `The proposed [structure] represents [entities] and connects them through [relations/workflow].`
- `Numerical measures are embedded as diagnostic layers within the workflow rather than used as standalone claims.`

evidence：

- `The framework is demonstrated through [case type], where [audit/service/query] produces [engineering output].`
- `The results show how [representation] transforms [raw metric/data] into [decision-support output].`

discussion：

- `The main value of the framework is diagnostic: it makes [hidden information loss/interoperability gap] visible before [decision/deployment].`
- `The approach complements semantic digital twins and knowledge-graph methods by focusing on [task-level sufficiency].`

### 8.3 AEI 安全表达

用：

- `demonstrates feasibility`
- `proof-of-concept`
- `case-specific implementation`
- `constrained public-data demonstration`
- `supports / facilitates / enables`
- `provides a structured representation`
- `improves interpretability / interoperability / information integration`
- `identifies potential redesign candidates`
- `suggests / indicates / illustrates`

### 8.4 AEI 红线表达

慎用或避免：

- `validated`：除非有多案例、真实部署、统计充分证据。单个 case 用 `demonstrated`。
- `universal/general framework`：除非跨域实证强。可说 `reusable structure` 或 `generalizable logic`。
- `intelligent`：除非有明确 autonomous reasoning/control。否则说 `decision-support`。
- `real-world deployment`：如果只是实验平台/公开数据，不要这么说。
- `optimal`：除非数学上严格优化且和工程目标一致。可说 `improved` 或 `ranked`.
- `cognitive uncertainty solved`：太大。可说 `task-level information sufficiency audited`。

## 9. 给当前 OIS 论文的可复用写作规则

### 9.1 一句话定位

OIS 论文应被写成：

`A task-oriented engineering-informatics framework that explicitly represents what observation information a deployed digital-twin pipeline retains for a specified engineering task, and turns numerical information measures into audit outputs engineers can use.`

中文定位：

`OIS 不是一个新指标论文，而是一个把资产状态、观测管线、特征表示、任务需求、保留区分和审计输出连起来的工程信息表示与审计 workflow。`

### 9.2 标题规则

标题必须包含至少 3 个元素：

1. `Observation Information Structure / information-sufficiency auditing`
2. `engineering digital twins / deployed sensing-feature pipelines`
3. `task support / audit / decision support / post-deployment drift`

推荐标题：

- `A Task-Oriented Observation Information Structure for Auditing Engineering Digital Twins under Deployed Sensing Pipelines`
- `Information-Sufficiency Auditing of Sensing-Feature Pipelines for Engineering Digital Twins`
- `From Sensing Features to Task Support: An Observation Information Structure for Engineering Digital Twin Audits`

### 9.3 摘要规则

摘要按 6 句或 6 组写：

1. 工程背景：DT 部署后依赖 sensing/feature pipeline 支撑具体任务。
2. 缺口：现有方法多报告局部精度/预测误差/信息量，但不显式表示任务需求和保留区分。
3. 后果：系统可能局部精确但全局不足，无法诊断哪个任务 unsupported、信息在哪一层丢失。
4. 方法：提出 OIS。
5. workflow：OIS 表示 asset states、observation pipeline、feature representation、task schema、operational resolution、retained distinctions、audit outputs；数值指标作为 diagnostic layer。
6. evidence/contribution：通过 controlled DT pipeline、drift audit、constrained public-data example 展示，输出 unsupported tasks、witnesses、local-global disagreement、failure stage、redesign candidates。

### 9.4 引言规则

OIS 引言建议 8 段：

1. Engineering DT 背景：sensing/simulation/features 支撑决策。
2. 部署后信息问题：数据多不等于任务足够；pipeline 会压缩/折叠信息。
3. 现有 DT/SHM/sensor/AI 进展：强调监测、预测、优化、融合。
4. 现有 semantic/KG/ontology 进展：强调互操作和知识表示，但较少审计 observation information sufficiency。
5. 现有 numerical identifiability/information criteria 进展：有局部指标，但少有工程-facing audit representation。
6. gap synthesis：task schema、pipeline representation、audit output 三缺口。
7. proposed OIS + contributions。
8. paper organization。

### 9.5 Method section 规则

Method 不要从公式开始。建议小节：

1. `Overview of the OIS audit workflow`
2. `Task-oriented observation information representation`
3. `Representation of deployed sensing-feature pipelines`
4. `Information sufficiency diagnostics`
5. `Audit outputs and redesign candidates`
6. `Implementation details`

每个小节都要回答：

- represented entity 是什么？
- relation 是什么？
- workflow 中输入/输出是什么？
- 工程师能用输出做什么？

### 9.6 Case section 规则

Case 按 AEI 方式写，不按“实验 1/实验 2”堆结果：

1. Engineering scenario and task schema。
2. Deployed sensing-feature pipeline。
3. OIS instantiation。
4. Audit setup。
5. Audit outputs。
6. Engineering interpretation and redesign implication。
7. Transferability/limitation。

### 9.7 Discussion 规则

Discussion 不重复结果，要回答 5 个 AEI 问题：

1. OIS 让什么信息损失变得可见？
2. 它怎样把数值指标转成工程审计报告？
3. 它和 semantic DT / KG 的关系是什么？互补，而不是替代。
4. 它和 sensor placement / Fisher information / CRLB 的关系是什么？把这些作为 diagnostic layers。
5. 它的限制是什么？task schema 依赖专家、case 有限、public data observability constrained、需要更多部署数据。

### 9.8 必备 claim-evidence 对齐

| Claim | 必须配的证据 |
---|---|
| OIS is a representation framework | OIS schema table + framework figure |
| OIS audits task-level sufficiency | audit workflow figure + task distinction table |
| OIS detects information folding | witness examples + local/global disagreement plot |
| OIS supports redesign | redesign candidate table + before/after audit comparison |
| OIS is useful for engineering DTs | case study with engineering interpretation, not only metric |
| OIS has transferability | constrained second case or explicit mapping to another pipeline |

### 9.9 最重要的写作纪律

- 每出现一个数学量，下一句解释它对应的工程信息对象。
- 每出现一个 framework，必须有图或表。
- 每出现 `support/enable/improve`，必须说明 support 什么工程任务。
- 不把 `digital twin` 当装饰词；必须说清 physical asset、virtual model/data、observation pipeline、task output 的关系。
- 不把 `cognitive uncertainty` 写成心理学或哲学概念；写成工程系统中“任务相关区分是否被观测与特征表示保留”的信息问题。
- 不把 case 写成“指标更好”；写成“审计发现什么、解释什么、建议什么”。

