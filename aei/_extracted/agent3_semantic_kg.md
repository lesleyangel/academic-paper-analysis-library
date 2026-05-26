# Agent 3 literature notes: semantic DT / KG / information container

> 分析范围：`1-s2.0-S1474034624003252-main`, `1-s2.0-S1474034625003763-main`, `1-s2.0-S1474034625003957-main`, `1-s2.0-S1474034625008055-main`。本文只抽取 semantic DT / KG / information container 组的 AEI 写法逻辑，重点看显式知识表示、schema、query/reasoning、decision support 与 closed-loop redesign。

## 1. A Semantic Digital Twin for the Dynamic Scheduling of Industry 4.0-based Production of Precast Concrete Elements

### 标题

`A Semantic Digital Twin for the Dynamic Scheduling of Industry 4.0-based Production of Precast Concrete Elements`

标题结构是典型 AEI 式：`Semantic Digital Twin` 是信息表示载体，`Dynamic Scheduling` 是工程任务，`Industry 4.0-based production of precast concrete elements` 是应用域。标题没有把 DT 当口号，而是直接绑定到动态排产决策。

### 摘要压缩

预制混凝土生产受供应链、养护时间和设备扰动影响，需要根据实时生产数据动态调整排产。论文提出一个基于 AAS 和 Linked Data 的 Semantic DT 框架，用 RDF 序列化 AAS，并以生产系统 ontology 聚合生产、设备、工序和订单数据。仿真排产器通过 SoA 与 DT 交互，使用 SPARQL 查询和更新图数据库。验证方式是 proof of concept，展示该框架可在扰动条件下管理不确定性并重新生成生产计划。

### 结论压缩

论文结论强调三点：第一，实时生产数据要想支持动态计划，必须被组织成生产系统层级 DT，而不是散落在单个机器或构件端；第二，AAS+RDF+PROD ontology 使 product、machine、process、order、station、buffer、duration 等要素能被统一查询；第三，SoA 服务负责把 DT 数据转换为调度器输入，并把优化后的 schedule 通过 SPARQL Update 写回 DT。局限是缺少真实自动化循环线生产时间数据，且尚未实现由各资产 DT 自主分发优化计划的多智能体闭环。

### 全文简介

论文从“预制件生产排产已有算法，但很少接入实时生产数据”切入，将问题定义为 DT-based dynamic scheduling。引言先区分 DT 与 BIM/CPS，再铺垫 Linked Data、semantic DT、AAS 与预制生产排产文献。方法部分先建 Flexible Job Shop / circulation system 调度模型，随后建立 DT information model。核心实现由三块构成：AAS/RDF 表示的 DT 框架、PROD production ontology、以及服务应用与 Sim4BFT 调度器。评估设置两个场景：无 WIP 的静态排产，以及包含 WIP、设备故障和延迟的动态重排。

### Knowledge Representation Object

- 表示对象：生产系统的动态排产知识，而不是单纯的排产算法。
- 顶层容器：AAS，作为 Industry 4.0 资产 DT 的信息容器。
- 数据模型：AAS RDF serialization + PROD ontology + GraphDB。
- ontology 对象：`ProductionSubmodel`、`ProductionSystem`、`ProductionUnit`、`ProductionStation`、`Buffer`、`Order`、`PrecastElement`、`ProductionProcess`。
- schema 形成路线：先用 competency questions (CQs) 定义 ontology 能回答什么，再建 technology-neutral conceptual model，最后编码为 OWL/RDF，并与 AAS ontology 对齐。
- 关键语义关系：`prod:consistsOf`、`prod:hasItem`、`prod:isProducedBy`、`prod:canBeExecutedBy`、`prod:expectedDuration`、`prod:sequencePosition`、`prod:actualStart`、`prod:expectedStartTime`。

### Reasoning / Query / Use

- Query：CQs 被翻译成 SPARQL。示例包括查询 circulation system 的 process steps、production station、job order list。
- Reasoning：`prod:consistsOf` 被建为 transitive property，可通过推理简化 production system -> production unit -> station 的路径查询。
- Use：服务应用从 GraphDB SPARQL endpoint 抽取订单、工序、站点、持续时间、实际开始时间等状态，将其转换为 Sim4BFT 调度器输入；调度结果再转换为 SPARQL Update 写回 AAS/GraphDB。
- Decision support：输出是 optimized production schedule 和 Gantt chart；在 Curing Station 3 故障、Reinforcement Station 2 延迟时触发重排，更新后续工序开始时间。
- 闭环类型：生产数据 -> DT 图数据库 -> 服务转换 -> 调度优化 -> schedule 写回 DT。它是 operational closed loop，尚未发展到资产级自主协同闭环。

### 图表/公式证据

- Fig. 4：AAS submodel 建模方法，支撑“先需求、再概念、再 ontology”的 schema 生成逻辑。
- Fig. 5：technology-neutral conceptual information model，显示从生产系统、订单、构件、工序到站点/缓冲区的类关系。
- Fig. 6：DT framework，AAS、PROD submodel、GraphDB、service application、simulation software 的 SoA 架构。
- Fig. 7-10：PROD ontology 概览、与 AAS ontology 集成、Order/PrecastElement/ProductionProcess、ProductionUnit/Station/Buffer 细部。
- Table 2：12 个 CQs，是 AEI 中 schema requirements 的典型证据。
- Table 3-5：SPARQL 查询结果，证明 ontology 可回答任务问题。
- Table 6：生产过程时间，作为调度仿真输入。
- Fig. 12-13：静态优化 schedule 与扰动后重排 Gantt chart。
- 公式弱：论文主要不是公式驱动，核心证据是 ontology/schema、query listings、service workflow 和 Gantt 输出。

### 引用分布

全文约 108 条参考文献。引用主要压在 Introduction、Background/Related research，尤其是 semantic DT / Linked Data / AAS / scheduling 几块；Method 和 Implementation 更依赖图、表、SPARQL listing 和系统实现。自动抽取的 rough distribution 显示：Linked Data and semantic DT 约 24 个 citation markers，AAS 约 14，precast scheduling 约 15，methodology 相关位置较密。这符合 AEI 规律：前文用文献建立信息层 gap，方法段用 schema 和 case evidence 承接。

### 写作规律

- 引言 gap 写法：已有 DS 文献存在，但孤立于 DT 系统，缺少实时数据采集、分析、提供与回写机制。
- 贡献写法：不是“提出算法”，而是“开发 production submodel + scheduling service + SPARQL-based data exchange”。
- 方法写法：把排产数学模型降为 workflow 内部层，把 ontology 和 service orchestration 放到 AEI 主贡献层。
- 证据写法：先用 CQs 证明 ontology scope，再用 SPARQL 输出证明可查询，最后用扰动场景证明工程任务可执行。
- 局限写法：明确说 proof of concept 和生产数据不可得，不夸大真实部署。

### 可用于我们论文哪个段落/claim

- Claim：数字孪生的不确定性管理不能只依赖预测模型，还需要显式表示生产对象、状态、工序和可查询关系。
- 可放段落：Introduction gap 中“real-time data is not decision-ready unless represented in a task-oriented semantic structure”。
- 可放 related work：semantic DT / AAS / Linked Data 支持工程任务的代表。
- 可借鉴方法：用 competency questions 定义我们的认知不确定性 schema 能回答哪些问题，例如“哪个状态量支持哪个设计/诊断任务”“哪类信息不足导致决策不可支持”。

## 2. Semantic Digital Twins in Construction: Developing a modular System Reference Architecture based on Information Containers

### 标题

`Semantic Digital Twins in Construction: Developing a modular System Reference Architecture based on Information Containers`

标题结构是 `Semantic DTs in domain: developing SRA based on information containers`。它把“信息容器”作为体系结构核心，而不是把 case study 放在标题主位。

### 摘要压缩

建筑 DT 面临异构数据源、生命周期需求变化和模块结构缺失的问题。论文提出一个 modular SRA，以 AAS 作为高层 DT 框架，并通过 Linked Data 语义层把 ICDD 作为标准化信息容器集成进 AAS。case study 是预制混凝土生产：一个 ICDD/BIM-derived semantic data submodel，一个 time series sensor data submodel；SPARQL 和 REST 查询用于实时监控与反馈控制。结果证明 SRA 可以集成异构数据、支持语义互操作并形成生命周期反馈机制。

### 结论压缩

结论把贡献落在 architecture 而非单个控制算法：AAS 适合 modular DT 的高层组织，Linked Data 提供语义表达、跨域链接和 advanced querying，AAS+ICDD 的统一实现可集成静态 BIM 与动态时序数据。局限也很清楚：BIM 到 ICDD 的集成仍偏手工，AASX 与 RDF 兼容性不足，Linked Data/SPARQL 维护有认知成本，未来需要 semantic mapping tools、reusable templates、AASX-RDF converter 和更大规模分布式验证。

### 全文简介

论文首先将建筑 DT 难点归结为 architectural fragmentation、semantic inconsistency、lifecycle integration 和 information container formalization 不足。State of the art 分层讨论 DT implementation challenges、SRA 类型、layered/component-based/SoA/microservice、container-based implementation 和 Semantic Web。方法分 conceptualization、implementation、validation 三步。框架设计提出 logical components、logical architecture 和 modularity facets。方法核心是 Section 5：用 ontology alignment 把 ICDD 映射为 AAS submodel。case study 用 Y 型预制件养护过程证明 static design data + dynamic temperature data 可以通过服务形成反馈控制。

### Knowledge Representation Object

- 表示对象：模块化 construction DT 的系统参考架构，而非某个单一资产模型。
- 信息容器：AAS 作为 superordinate DT framework；ICDD 作为 BIM/IFC/文档/链接信息容器；time series submodel 作为传感数据容器。
- 语义技术：RDF、RDFS、ontologies、Linked Data、GraphDB。
- ontology 对齐对象：`aas:Submodel`、`aas:SubmodelElement`、`aas:Reference`、`aas:Key` 与 `ct:ContainerDescription`、`ct:Document`、`ct:Linkset`、`ct:Link`、`ct:LinkElement`、`ls:Identifier`。
- 对齐策略：使用 `rdfs:subClassOf` 而不是 `rdfs:equivalentClass`，因为“每个 ICDD container 可以是 AAS submodel，但不是每个 AAS submodel 都是 ICDD container”。这个单向逻辑是 schema 设计里很值得学的精细判断。
- namespace/table 证据：Table 4 列出 AAS、BOT、ICDD Container、ICDD Linkset、PROPS、RDF、RDFS 等命名空间。

### Reasoning / Query / Use

- Query：GraphDB 承载由 AAS/ICDD alignment 得到的 common knowledge graph，提供 SPARQL endpoint。
- RDFS reasoning：case 中对 ICDD submodel 应用 RDFS inference，使 IFC/RDF entities 和 AAS terminology 可统一查询。
- Use：service 先通过 SPARQL 查询 time series endpoint/query string，再查询 ICDD-based submodel 中的 curing heat threshold；之后通过 REST 请求 InfluxDB 读实时温度，并通过 REST 控制 oven DT。
- Decision support：服务每两分钟轮询温度，若超过阈值则触发 oven temperature control。输出不是模型精度，而是“可跨两个 DT 进行反馈动作”的信息流证明。
- 闭环类型：BIM/design data -> ICDD semantic submodel；sensor/time-series data -> AAS time series submodel；service queries both -> feedback control to oven DT。它是 lifecycle-oriented feedback loop。

### 图表/公式证据

- Fig. 1：SRA 开发方法，概念化-实现-验证。
- Fig. 2：component- and service-oriented DT architecture。
- Fig. 3：modularity facets，包括 lifecycle、process、spatial modularity。
- Fig. 5-7：AAS ontology、ICDD ontologies、AAS-ICDD alignment。
- Fig. 9：RDFS inference 后的 submodel data，证明 ICDD container 可作为 AAS submodel 查询。
- Fig. 10-11：Time Series Submodel ontology 与 Linked class。
- Fig. 12：building information data 与 time series data 两类 submodel 的 prototype implementation。
- Fig. 13：Y-module DT、oven DT 与 service 的 data exchange sequence。
- Listing 1-5：SPARQL query、Flux query、REST service 实现片段，是 query/use 证据。

### 引用分布

全文约 95 条参考文献。引用集中在 Introduction 与 State of the art，尤其是 DT implementation challenges、SRA、layered/component/SoA/microservice architecture、container-based implementation 和 Semantic Web。自动 rough distribution 显示：2.1 约 23，2.2 约 17，layered 约 23，component 约 15，SoA/microservice 约 12，container 约 6，Semantic Web 约 5；方法、case 和结论引用较少，主要靠架构图、ontology alignment 和 prototype 说明。

### 写作规律

- 引言 gap 写法：不是“缺少 DT”，而是“缺少标准化、模块化、语义化、生命周期可扩展的 DT 架构”。
- Related work 组织：按 architecture patterns 和 information container 分类，而不是按作者时间线。
- Framework 图写法：先给 logical architecture，再给 modularity facets，再给 data model alignment，层层从系统架构落到 schema 细节。
- Case study 写法：选一个小而完整的 feedback control case，用它证明 SRA 的模块组合能力。
- Discussion 写法：反复回答“表示层让什么变得可见”：静态 BIM 数据、动态时序数据、跨 DT 服务控制、跨技术栈互操作。

### 可用于我们论文哪个段落/claim

- Claim：工程 DT 的核心瓶颈常常不是单个模型精度，而是跨生命周期数据的容器化、语义对齐和任务级查询。
- 可放段落：Related Work 中“information container and semantic interoperability for DTs”。
- 可用于方法启发：我们的认知不确定性可以被写成一个 modular submodel / information container，而不是算法附属变量；不同阶段的不确定性来源可按 lifecycle/process/spatial facets 组织。
- 可用于限制讨论：semantic approach 的成本包括 manual mapping、template 缺失、RDF/AASX 兼容和 SPARQL 专门知识。

## 3. Digital twin-based assembly process framework utilizing STEP and knowledge graph

### 标题

`Digital twin-based assembly process framework utilizing STEP and knowledge graph`

标题结构是 `DT-based process framework utilizing standard schema + KG`。与 Kosse 的 AAS/ICDD 不同，这篇从制造数据标准 STEP 出发，把隐式关系转为 KG 显式关系。

### 摘要压缩

装配 DT 的基础是有效的信息组织与数据分析，但多源异构数据交换差导致 information silos，并限制装配参数相关性分析。论文提出 DT-APF，通过对象实例化建立 DT-APIM，再将 DT-APIM 转为 DT-APKG，实现多阶段数据深度集成。ASP 算法作为知识推理引擎，构建覆盖装配生命周期的数据组织和知识推理系统。航空发动机机匣装配 case 表明，ASP 推理能识别 assembly performance correlations，DT-APF 相比传统 KG 构建方法提升 31.6% 数据集成效率。

### 结论压缩

论文结论把贡献压缩为“Data Standardization (STEP)-Knowledge Formalization (KG)-Service Intelligence (AI)”范式。STEP 扩展提供 assembly project-procedure-step 的标准化 schema，OntoSTEP 将静态 STEP 实例转为动态 KG，ASP 支持语义相关性分析和参数优化。局限与未来方向是继续接入实时 sensor data streams、提高 assembly semantic completeness，并把 KG constraints 与 reinforcement learning 结合，向自主装配策略演化。

### 全文简介

论文从智能装配中的数据孤岛和参数相关性分析不足切入，先说明 STEP 在 CAD/制造交换中有标准优势，但 EXPRESS 关系隐式，推理能力不足；ontology 有语义推理但维护成本和性能瓶颈；KG 有动态扩展和信息挖掘能力但缺少统一标准。因此论文提出 STEP+KG hybrid architecture。Section 3 先构建 DT-APIM，包括 assembly project、procedure、step、part、assembly feature、constraint、execution equipment、inspection equipment；再用 OntoSTEP 转为 DT-APKG；最后用 ASP 做自然语言问答式实体关系抽取和图查询。Section 4 用 aero-engine casing 验证建模、查询与构建效率。

### Knowledge Representation Object

- 表示对象：装配过程全生命周期信息，尤其是装配特征、装配约束、装备、检测数据与性能参数之间的关系。
- 标准 schema：扩展 STEP/EXPRESS，形成 DT-APF。
- 实例模型：DT-APIM，即特定装配对象的标准化信息模型。
- 知识图谱：DT-APKG，即由 DT-APIM 转换得到的 graph-based semantic representation。
- 层级结构：assembly project -> assembly procedure -> assembly step。
- 实体对象：part、assembly_feature、constraint、execution_equipment、inspection_equipment。
- assembly feature：single/compound/replicate；single feature 包括 surface、shaft_hole、spherical、thread。
- constraint：coincidence、parallelism、verticality、distance。
- 转换机制：STEP Part 21 syntax parser 解构文件层级和语法元素，OntoSTEP 将 STEP instance 实例化为 KG individuals，并解释 attribute domains。

### Reasoning / Query / Use

- Reasoning：ASP-based reasoning engine 把自然语言 query 转为 entity-relation tuples，再用这些实体和关系在 DT-APKG 中检索相关节点和关系。
- Query use：构建 Q&A-style reasoning system，用于识别航空发动机机匣装配中影响 assembly quality / performance parameters 的相关因素。
- 性能指标：ASP 模型实体抽取 P/R/F1 为 89.83/86.88/88.33，关系抽取 P/R/F1 为 94.12/80.00/86.49。
- 工程输出：快速检索 correlation nodes，推理装配参数关系，支持装配质量追溯、参数优化和智能决策。
- 更新机制：DT-APF 提出由 DT-APIM 更新驱动 DT-APKG 同步的机制，虽然实时性仍有优化空间，但比纯文本抽取 KG 更适合工程一致性。

### 图表/公式证据

- Fig. 1：DT-APIM EXPRESS-G 层级结构。
- Fig. 2：基于装配特征和约束的装配过程示例。
- Fig. 3-7：part、assembly feature、constraint、execution equipment、inspection equipment 的 EXPRESS-G 表示。
- Fig. 8：DT-APIM 到 DT-APKG 的转换。
- Fig. 9：DT-APF 执行机制。
- Fig. 10/12：APKG-ASP 的装配参数相关因素推理与查询界面。
- Fig. 11：航空发动机机匣简化装配。
- Table 1：STEP、ontology、KG 的优劣比较，是 introduction gap 的关键表。
- Table 2：DT-APKG 规模，78 类节点、1527 个节点、129 类关系。
- Table 3-5：ASP 参数、训练结果和 query-response 结果。
- Table 6：与 TCEEKG、GRBE、ontology-based model 对比，DT-APF 构图时间 15 h，较 25/23/20 h 缩短 40%、34.8%、25%，平均效率提升 31.6%。

### 引用分布

全文约 52 条参考文献。Introduction 引用相对少，Literature review 集中铺垫装配 DT、STEP、ontology、KG、推理算法和智能决策。自动 rough distribution 中 Literature review citation markers 最多，Method 和 Case 只少量引用标准、OntoSTEP、ASP 和对比方法。写法上属于“窄领域方法论文”：引用量不如 SRA 论文大，但通过 Table 1 的方法比较来补足 gap 可信度。

### 写作规律

- Gap 三段式：DT 装配需要实时/自适应 -> 数据异构形成 information silos -> STEP 标准化但关系隐式，ontology 可推理但成本高，KG 灵活但缺标准。
- Contribution 三件套：标准化信息模型、KG 转换机制、AI 推理闭环。
- Framework 写法：先定义 schema，再定义 schema-to-KG，再定义 query/reasoning engine。
- Case study 写法：先展示 KG 规模，再展示 reasoning system，再做与其他 KG 构建方法的效率/一致性对比。
- AEI 风险：文章有“closed-loop optimization”表述，但证据更多是 query/reasoning 和 KG 更新机制，真正物理闭环不如第四篇充分。

### 可用于我们论文哪个段落/claim

- Claim：显式知识表示可以把标准文件中隐式关系转化为可查询、可推理的关系网络。
- 可放段落：Related Work 中“standard schema to KG transformation”。
- 可用于方法启发：我们可以把认知不确定性从工程数据表/仿真结果中的隐式变量，转为 entity-relation schema，例如 `feature -> supports -> QoI`、`measurement -> constrains -> state variable`、`uncertainty source -> affects -> decision criterion`。
- 可用于 case 论证：KG 的价值不只是存储，还在于查询“哪些因素影响某性能参数”这种任务级问题。

## 4. A closed-loop design approach based on the combination of knowledge graph and digital twin: a high-speed train bogie case study

### 标题

`A closed-loop design approach based on the combination of knowledge graph and digital twin: a high-speed train bogie case study`

标题结构是 `closed-loop design approach based on KG+DT: engineering case`。它的 AEI 信号不是 semantic web 标准，而是 KG 如何把运行反馈变成再设计信息。

### 摘要压缩

复杂工业产品需要生命周期闭环反馈设计，但多源数据格式/语义不一致、模型参数动态更新困难、模型-数据关联映射困难会降低优化迭代的准确性和效率。论文提出 KG+DT 闭环设计方法：基于 metamodel theory 把 DT 分为 information model、mechanism model 和 field model，建立统一表达；用 KG 作为物理数据与 DT 模型之间的信息交换媒介，管理多源异构数据交互；再结合 KG 查询推理能力修正 DT 模型参数，形成 continuous feedback knowledge update loop。高铁转向架 case 表明，低阶模态频率修正准确率提高到 97.79%，最大应力、轻量化和安全指标分别改善 14.96%、13.81%、2.82%，关键位置刚度最高改善 17.79%。

### 结论压缩

结论把贡献归纳为：第一，提出 metamodel-based DT construction，将 DT 分为 IM/FM/PM，并用 KG ontology 实现信息关联和映射；第二，用 KG query/reasoning 与 PSO 修正模型参数，使 4-6 阶模态频率误差分别改善 1.14%、1.14%、1.33%；第三，经过初始应力/轻量化优化后，将运行阶段实际频率信息反馈到 KG，进行二次优化，最大应力、体积和频率指标改善 14.96%、13.81%、2.82%；第四，实物试验验证优化后关键测点刚度均提升，位置 3 最高 17.79%。未来关注用户认知、个性化设计、模块化与数据流协同、适应性/柔性/可复用性的系统知识表达。

### 全文简介

论文先把 closed-loop design 的困难抽象为 source-response-decision 链条中的断裂：多源信息语义不一致、DT 模型参数依靠先验假设、运行数据没有反馈到设计模型。Related works 分 KG for knowledge management 和 DT for multidimensional modeling。Research gaps 明确指出现有方法缺少支持多维信息融合、语义关联和动态反馈的统一 mapping mechanism。方法部分先以 metamodel theory 定义 object、attribute、relationship、mapping、method 五要素，再将 DT 分为 IM、PM、FM；随后定义 KG-based multidimensional information mapping，包括 inheritance、polymeric、additive、extraction 四种映射；最后建立设计侧-运行侧的 closed-loop bidirectional mapping。Case study 用转向架缩比模型、模态实验、ABAQUS 仿真、Neo4j KG、SWRL/SQWRL 规则和 PSO 修正，完成模型校准、拓扑优化和二次优化。

### Knowledge Representation Object

- 表示对象：设计-制造/运行反馈-再设计过程中的多维信息映射关系。
- DT 三维模型：IM information model、PM mechanism/physical model、FM field/application model。
- metamodel 五要素：`O=<C,A,R,L,M>`，包括 concept、attribute、relation、logical rules、mapping mechanism。
- 属性层：静态属性如尺寸、材料；动态属性如加速度信号、载荷、应变、模态频率。
- KG 模块：data processing module、key technology module、knowledge ontology module。
- ontology 层级：IM、PM、FM 三层，包含 acceleration sensor data、bogie structure data、experimental conditions、design requirements、simulation results 等实体，以及 `has_frequency`、`has_load`、`has_a` 等属性关系。
- 四种 mapping semantic：`inheritTo`、`polymerizeTo`、`addTo`、`extractTo`。

### Reasoning / Query / Use

- Query：从 KG 中查询模态实验参数、材料属性边界、运行频率范围和设计约束。
- Rule reasoning：当实验模态频率与仿真频率误差超过 5% 时，规则触发模型参数修正；通过 `sqwrl:select` 输出频率误差分析和参数修正建议。
- Algorithm use：KG 推理得到参数范围和修正变量后，PSO 求解密度 E 和竖向弹簧刚度 Kz 等参数；敏感性分析显示密度和竖向弹簧刚度对受约束模态影响最大。
- Decision support：先用修正后的 DT 做应力/轻量化拓扑优化，再查询实际运行频率，发现高铁荷载导致的地面振动主要集中于 0-50 Hz，缩比模型需远离 0-200 Hz，由此进行二次优化。
- Closed-loop redesign：运行响应 `Y_IMI` -> KG 反馈与推理 -> 修正系统参数 `Q_A|YIMI` -> 替代先验参数 `Q_IMI` -> 更新 PM/FM -> 指导下一代方案。

### 图表/公式证据

- Fig. 1：metamodel-based DT framework。
- Fig. 2：multi-dimensional DT model construction framework。
- Fig. 3：KG multidimensional information management。
- Fig. 4：四类 KG mapping types。
- Fig. 5：KG+DT closed-loop design process。
- Fig. 6：bogie frame closed-loop design process。
- Fig. 7-10：缩比模型、实验平台、频响曲线、试验-仿真误差。
- Fig. 11-14：bogie ontology 的 mapping path、ontology structure、KG、semantic rules。
- Fig. 15-17：KG+PSO 模型修正、敏感性分析、迭代过程。
- Fig. 18-20：载荷路径、应力云图、优化结果。
- Fig. 21-22：优化前后实物实验和应变曲线。
- Table 2：mapping semantic definition。
- Table 4：bogie ontology mapping and semantic modeling instances。
- Table 7：模型修正对比，4-6 阶弹性模态误差降低。
- Table 9：最大应力 211.68 -> 141.00 MPa，体积 2.10e-3 -> 1.81e-3 m3，频率 210.62 -> 216.56 Hz。
- Table 10：应变实验，关键位置刚度提升，位置 3 最高 17.79%。

### 引用分布

全文约 44 条参考文献。引用集中在 Introduction、KG for knowledge management、DT multidimensional modeling 和 research gaps；方法与 case 部分引用少，主要依靠数学定义、ontology/schema、实验数据和优化结果支撑。自动 rough distribution 显示 Introduction 约 15，KG 相关 13，DT 建模 7，research gaps 7。AEI 逻辑是“文献建立闭环设计的信息映射缺口，方法与 case 用实验证据证明 KG+DT 能把反馈转成再设计”。

### 写作规律

- 引言 gap 写法：closed-loop design 的瓶颈不是没有优化算法，而是多源数据语义不一致、模型参数不能动态更新、模型-数据关联映射困难。
- 方法写法：先给抽象 formalism，再给 mapping semantics，再给闭环流程，最后进入具体对象。
- GJJ 式链条：运行数据/载荷状态 -> 结构响应/模态频率 -> 参数修正/健康状态一致性 -> 设计目标/约束更新 -> 放行或再设计决策。
- Case study 写法：保留主结构和关键载荷路径，先用实测修正模型，再用修正模型优化，最后用新结构实验验证。
- AEI 强项：有清楚的 closed loop，且决策输出是结构再设计，不只是 KG 查询结果。
- AEI 风险：部分术语中 PM/FМ 命名有不一致痕迹，需借鉴其逻辑而不要照搬符号。

### 可用于我们论文哪个段落/claim

- Claim：闭环设计中的认知不确定性应被建模为“先验参数与运行反馈之间的可解释映射偏差”，并通过 KG 查询/规则/参数修正进入设计决策。
- 可放段落：Introduction 中“why uncertainty representation must support redesign rather than only prediction”。
- 可放 method motivation：将 uncertain information 分为 IM/PM/FM 类似层次，明确 source quantity、response quantity、decision quantity。
- 可借鉴验证路线：真实/仿真响应差异 -> KG 触发修正规则 -> 参数更新 -> 设计目标二次优化 -> 实验验证。

## 本组抽象：AEI 中 semantic / KG / DT 论文的组织规律

### 标题如何组织

高适配标题通常同时包含三件事：表示载体、工程任务、应用域。

- `A Semantic Digital Twin for [task] of [domain]`
- `[Semantic DT / KG / information container]-based [framework/architecture] for [decision/control/scheduling/design]`
- `[Standard schema + KG] for [information organization/reasoning] in [engineering process]`
- `[KG + DT] closed-loop [design/optimization/control] approach: [case study]`

不要只写 `Digital twin for composites` 或 `Knowledge graph method`。AEI 更吃 `representation + use + engineering output`。

### 摘要如何组织

四篇的摘要基本是六步：

1. 工程场景变复杂：生产/装配/建筑/产品生命周期数据多源异构。
2. 信息层问题：数据孤岛、语义不一致、模块结构缺失、模型参数不能动态更新。
3. 决策后果：不能动态排产、不能统一检索、不能识别参数相关性、不能闭环再设计。
4. 表示方案：AAS/ICDD/RDF/ontology、STEP/DT-APIM/DT-APKG、IM-PM-FM ontology。
5. 查询/推理/服务：SPARQL、RDFS inference、ASP、SWRL/SQWRL、PSO、REST service。
6. 证据输出：Gantt 重排、反馈控温、query-response、构图效率、应力/质量/频率改善、实物实验。

可复用句法：`However, existing DT methods remain limited by ...` 后面必须接信息层 gap；`To address this issue, this study proposes ...` 后面必须明确 represented knowledge；`The results demonstrate ...` 后面必须是工程输出，不只是 accuracy。

### 引言 gap 如何组织

AEI 的 gap 不是“已有算法不够准”，而是：

- 数据没有被组织成任务可用知识；
- 标准/容器之间没有语义对齐；
- 标准 schema 中关系隐式，不能推理；
- KG 有图结构但缺工程标准约束；
- 运行反馈没有映射回模型参数和设计约束；
- 单点 DT 或单一模型不能跨生命周期复用。

写我们论文时可把 gap 定义为：现有复合材料孔隙/数字孪生研究多关注缺陷识别、性能预测或模型更新，但缺少面向认知不确定性的显式表示对象，导致不确定性来源、可观测证据、模型响应、设计/制造决策之间的关系难以查询、推理和闭环修正。

### Framework 图如何画

四类图最关键：

- Architecture 图：AAS/ICDD/GraphDB/service/simulator 或 IM/PM/FM/KG/optimizer 的模块关系。
- Schema 图：ontology classes、EXPRESS-G、entity-relation mapping、submodel alignment。
- Query/reasoning 图：SPARQL/ASP/SQWRL 如何从图中取出任务相关信息。
- Closed-loop 图：physical data -> representation -> reasoning/update -> decision/control/redesign -> feedback。

图中必须避免“DT 云朵 + AI 箭头”的空泛画法。每条箭头最好标注数据对象或操作：`SPARQL query`、`RDFS inference`、`parameter correction`、`schedule update`、`threshold retrieval`、`secondary optimization`。

### Case study 如何组织

AEI case study 不是展示一个结果，而是证明 representation 被用起来：

1. 定义工程任务和 task schema。
2. 列出输入数据与信息容器。
3. 展示 ontology/schema/KG 规模或关键类关系。
4. 给出 query/reasoning setup。
5. 输出可解释诊断、控制或设计建议。
6. 用图表或实验说明建议产生工程效果。
7. 承认 prototype、manual mapping、数据规模或真实部署限制。

### Conclusion 如何组织

结论应按“信息问题-表示方案-工程输出-限制/未来”收束：

- 先重申工程信息问题，而不是重复背景口号。
- 再说 representation object：AAS/ICDD、PROD ontology、DT-APIM/DT-APKG、IM-PM-FM KG。
- 然后说 query/reasoning/use 的输出：dynamic schedule、feedback control、correlation-factor query、parameter correction、secondary optimization。
- 最后列出限制：真实数据不足、手工语义映射、标准格式兼容、实时更新、规模化部署、自动化模板。

### 对我们论文的综合启发

我们要写“数字孪生的认知不确定性构建”，最稳的 AEI 路线不是直接说“提出认知不确定性指标”，而是把它写成一个 task-oriented representation problem：

- 表示对象：uncertainty source、observed evidence、state variable、model assumption、QoI、decision criterion、redesign action。
- schema：实体、属性、关系、约束、mapping rules。
- query：给定一个决策任务，能查询哪些证据支持/不支持；给定一个不确定性来源，能追踪它影响哪些模型响应和决策。
- reasoning：通过规则或图推理识别 unsupported decision、conflicting evidence、missing observation、parameter correction candidate。
- decision support：输出可解释的诊断或再设计建议，而不是只输出预测误差。
- closed-loop redesign：新观测进入后更新知识状态，修正模型假设或设计变量，并记录从“认知不确定性”到“工程修改”的路径。

一句话写法：AEI 中 semantic/KG/DT 论文的核心不是“模型更智能”，而是“工程知识被显式表示、可查询、可推理，并能通过服务或规则进入具体决策闭环”。
