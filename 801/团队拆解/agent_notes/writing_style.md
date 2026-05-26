# 801 团队写作画像：文笔习惯与表达系统

## 0. 证据范围与读法

本笔记基于 `801/深度拆解/papers/*.md` 的 `## 11` 到 `## 15`、自动词频/语言块，以及 `801/深度拆解/batch_summaries/*.md`。质量报告显示深度拆解文件 49 篇、batch summary 9 个，整体可支撑团队层面的写作画像。

证据等级沿用团队模板：

- **强证据**：跨批次、跨年份、跨主题反复出现。
- **中证据**：某一方向或某一类期刊中稳定出现。
- **弱证据**：少数论文出现，可能来自合作方、期刊栏目或单篇选题。
- **不可判断**：现有深拆材料不足以支撑。

需要注意：自动词频来自 PDF 抽取文本，受双栏串栏、公式和参考文献影响，个别噪声词如 `org`, `cient` 不作为风格判断依据。

## 1. 标题偏好

**总体判断：强证据。** 801 论文标题偏“工程对象 + 方法/模型 + 适用场景/条件”的长名词链，不追求短促概念化标题。标题通常先让审稿人知道研究对象，再说明方法或作用机制，最后给出应用边界。

按 49 篇标题粗略统计，介词/结构词出现频率为：`of` 30 篇、`for` 25 篇、`with` 9 篇、`based on` 6 篇、`under` 4 篇、`via` 3 篇、`using` 1 篇。`for` 和 `based on` 是最有辨识度的标题骨架，常用于“方法服务任务”；`with/under` 常用于强调约束、物理条件或真实使用环境；`via` 多见于数据驱动/传感重构；`using` 反而较少。

常见标题骨架：

- `A/An + method/model/approach + for + engineering task + based on/via + technique`
- `A/An + efficient/enhanced/integrated + model/method + with + key constraint`
- `The design/determination/quantitative study of X for Y based on Z`
- `X under thermal/mechanical/vibration/hypersonic conditions`
- `X considering/contacting/encompassing Y effects`

标题类型有明显重叠，但主轴清楚：

- **方法型/模型型**：如 prediction method、reconstruction method、optimization method、uncertainty propagation method、contact model。约半数标题直接暴露方法或模型。
- **应用型/对象型**：hypersonic vehicles、re-entry module、TEG、thermal protection system、flight vehicle、composites、projectile 等对象常在标题中出现。对象锚定与方法型几乎并行。
- **任务型/工程动作型**：design、determination、identification、evaluation、fabrication、sensing、control 等动作词较多，说明标题倾向把论文写成“可交付任务”。
- **机制型/效应型**：contact effects、interfacial resistance、degradation、thermoelectric enhancement、aerodynamic/angular motion characteristics 等集中在材料、界面和气动机制方向。机制型不是主流，但在高影响热电/界面论文中更强。

标题通常不用冒号，少数例外如路径跟随控制题名中的 `From take-off to landing`。更常见的做法是用多个介词短语把任务、对象、方法和边界一次性串完。

## 2. 摘要偏好

**总体判断：强证据。** 摘要最稳定的结构是：

`工程背景/重要性 -> however 型 gap -> proposed method/model -> 验证对象/工程算例 -> 定量结果 -> 边界或应用意义`

这种摘要写法有三个特征。

第一，**工程背景先行**。开头很少从纯数学 novelty 入手，而是从高超声速热环境、再入安全、结构可靠性、稀疏传感、热电转换、复合材料不确定性、飞行控制实时性等工程压力切入。背景句的功能不是泛泛铺垫，而是给后面的 gap 设置“为什么必须解决”的外部约束。

第二，**gap 通常不是“无人研究”，而是“已有研究在真实工程条件下不足”**。常见 gap 包括计算成本、分离设计、耦合缺失、边界条件失真、有限数据/传感器、真实接触界面、模型偏差、损伤容限不足。摘要中经常用 `however`、`limited attention`、`separately designed`、`difficult to support repeated evaluations` 这类温和但明确的转折。

第三，**贡献表达偏模块化和定量化**。摘要喜欢把方法拆成二到三步：如 POD-RBFNN-DE、Kriging-BPNN、整机-板-单元、多尺度/两尺度模型、事件触发 + WAPE + 突变检测。定量结果通常放在摘要末端，例如效率提升、误差降低、传感器减少、质量降低、输出功率、ZT、成功率或计算时间。

边界控制也较明显。概念验证类论文会用 `concept`、`evaluation`、`potential`；仿真主导论文通常把 claim 限定到特定工况、结构、参数范围或算例；工程方法论文常强调“accuracy + efficiency + applicability”，避免把单一精度指标写成普适结论。

## 3. Introduction 偏好

**总体判断：强证据。** Introduction 的基本节奏是：

`工程需求 -> 文献/方法谱系分类 -> 每类方法的价值与边界 -> 本文 gap -> 方法/贡献列表 -> 文章结构预告`

文献组织方式以“分类综述”最常见。不是逐篇堆文献，而是把前人工作分成方法流派、物理路径、子系统或工程环节。例如可靠性论文按方法族谱展开，热管理论文按 heat reduction/dissipation/transport/reuse 展开，TEG 论文按粗糙面、TCR/ECR、实验测量、系统性能展开，ML/ROM 论文按高保真、降阶、回映、传感布置或实时推理展开。

gap 制造的高频方式是“承认价值 + 限定边界”。典型骨架是：

- `Existing methods solve A, but do not address B under C conditions.`
- `Previous studies mainly focused on local/simple/single-source cases.`
- `The subsystem is usually designed separately, although X and Y influence each other.`
- `High-fidelity simulation is accurate, but too expensive for repeated design.`
- `The phenomenon has been observed, but the bridge to system-level performance is still missing.`

贡献列法较常见，尤其在方法复杂的 AST、Probabilistic Engineering Mechanics、Composite Structures、IJHMT 类论文中。贡献通常不是简单列 novelty，而是按“模型/算法/验证/工程结果”拆开，让读者先获得阅读地图。

organization paragraph 有中等稳定性。不是每篇都有固定模板，但很多长方法论文会在 Introduction 最后一段预告 workflow、本文各模块或章节安排。有些论文的最后一段几乎就是后文目录：模型、实验平台、结果分析、设计路线、验证算例依次出现。

## 4. Discussion/Conclusion 偏好

**总体判断：结果段写法为强证据，独立 Discussion 与 limitation/future work 为中证据。**

801 论文多数采用 `Results and discussions` 合并结构。Discussion 不一定单独成章，而是嵌入每个结果小节：先读图，再解释趋势，再落到机制或工程意义。batch summary 中反复出现的结果段骨架是：

`Fig. X shows -> trend -> reason/mechanism -> design implication`

机制解释偏好很强，但机制的深浅随方向变化。热管理/TEG 方向喜欢从 `heq`、TCR/ECR、loading pressure、gap medium、thermal radiation、mass flow rate 等中间变量解释系统指标；材料方向喜欢把性能回到 defect、oxygen vacancy、grain boundary、phonon scattering、texture；气动/流固耦合方向喜欢用 vortex、frequency、shock、modal coefficient 等解释宏观结果；控制/优化方向则把机制写成触发频率、迭代次数、约束满足、路径安全。

Conclusion 通常偏编号化和定量化。每条结论对应前文一个 gap：精度是否够、效率提升多少、边界是否更真实、系统耦合是否闭合、工程约束是否满足、设计建议是什么。常见做法是把强 claim 放进数值表或结论条目中，正文解释保持稳健。

limitation/future work 写法不是所有论文都完整，但在控制、ML、微重力生物、系统集成和实验不足的论文中较明显。常见限制包括：参数范围有限、未考虑真实飞行/长期热循环/压降/寿命、模型简化、实验不足、外推范围、真实部署条件。future work 常落在更多变量、更复杂模型、实验/实飞验证、长期可靠性、更多场景或在线部署。

## 5. 常用词与句式

**总体判断：强证据。** 自动词频合计显示，801 语言高度服务于工程模型与物理中间变量。高频核心词包括 `heat`、`temperature`、`thermal`、`model`、`method`、`contact`、`optimization`、`aerodynamic`、`flow`、`TEG`、`unit cell`、`damage`、`reconstruction`、`error`、`field`。高频动词以 `shown/show/shows`、`proposed`、`compared`、`developed`、`indicates`、`predicted`、`formulated`、`validated` 为主。高频连接副词包括 `respectively`、`however`、`therefore`、`significantly`、`mainly`、`generally`、`finally`。

常用功能句骨架如下。

**背景句**

- `Accurate and rapid determination of X is essential for Y.`
- `X plays an important role in Y under Z conditions.`
- `With the development of hypersonic/reusable/aerospace systems, X becomes critical.`

**gap 句**

- `However, X remains challenging because of Y.`
- `Existing methods can solve A, but B is still not considered under C.`
- `Limited attention has been paid to system-level/multi-source/real-interface conditions.`
- `X and Y are usually designed separately, although they influence each other.`

**方法句**

- `To address this issue, a ... method/model/framework is proposed.`
- `The proposed method consists of A, B and C.`
- `X is reconstructed/predicted/estimated based on Y.`
- `A surrogate/reduced/equivalent model is developed to reduce computational cost.`

**贡献句**

- `The main contributions are summarized as follows.`
- `For accuracy holding, ...; for cost control, ...`
- `First, ...; second, ...; third, ...`
- `The method introduces an intermediate variable/layer to connect A with B.`

**结果句**

- `The results show/indicate that...`
- `Compared with X, the proposed method reduces/improves Y by...`
- `Good agreement is obtained between numerical and experimental results.`
- `With the increase of X, Y decreases/increases, while Z...`

**机制解释句**

- `This indicates/suggests that...`
- `This can be attributed to...`
- `The reason is mainly that...`
- `X establishes a mutual correlation between A and B.`

**工程意义句**

- `The proposed model can be used for...`
- `These results provide design guidance for...`
- `From the perspective of the whole vehicle/system, ...`
- `The framework supports real-time/repeated/system-level evaluation.`

**局限句**

- `It should be noted that...`
- `The present model does not consider...`
- `The conclusions are limited to the tested parameter range.`
- `Further experimental/flight/in vivo validation is needed.`

**未来工作句**

- `Future work will consider more complex conditions and additional variables.`
- `The long-term reliability and deployment performance need further investigation.`
- `More experimental data will be used to validate and improve the model.`

## 6. 语态、时态、claim 强度与 hedging

**总体判断：强证据。** 自动语言块显示 49 篇合计约有被动语态线索 6832 次、`we + 动作动词` 主动句线索 64 次、名词化表达线索 34728 次。这说明 801 写作强烈偏“客观过程链”：模型被建立、样本被生成、结果被验证、变量被分析，而不是突出作者主体。

时态上，一般现在时线索约 12352 次，明显高于一般过去时 2674 次和现在完成时 282 次。现在时主要服务于模型定义、图表解释、一般规律和结论性 claim；过去时用于实验、仿真、样本生成和已完成操作；现在完成时多用于连接已有研究。

情态动词线索约 2610 次，说明 hedging 不是弱，而是稳定策略。`can` 用于表达方法能力和工程可用性，`may/could` 用于外推、风险和潜在机制，`should` 用于设计准则或建模规范。强 claim 通常有数值或对比表支撑；弱证据或外推结论则通过条件、范围、模型假设控制。

claim 强度的典型分层：

- **强 claim**：放在摘要末尾、结果表、Conclusion 条目中，通常配合误差、效率、功率、质量、ZT、成功率等数字。
- **中 claim**：放在 Results and discussions 中，用 `indicate/suggest/can be attributed to` 解释机制。
- **弱/边界 claim**：放在 limitation、future work 或 remarks 中，用 `may/could/should/under the tested range` 限制。

这种写法让论文显得“工程上有底气，学术上不冒进”。

## 7. 这些写法如何服务期刊发表

**总体判断：强证据。** 801 的写作系统服务期刊发表，核心不是文采，而是降低审稿人的不确定性。

第一，标题和摘要把贡献放进明确的工程任务中。`method/model for X`、`based on Y`、`under Z` 让编辑和审稿人快速判断稿件属于哪个领域、解决什么问题、证据应如何审。

第二，Introduction 的分类综述避免“稻草人 gap”。作者通常先承认前人方法有效，再指出其边界，审稿人不容易觉得作者在否定整个领域。这对工程期刊尤其重要。

第三，方法写法善于构造“中间层”。无论是 `heq`、TCR/ECR、unit cell、POD coefficient、damage grade、equivalent layer、modal space、correlation matrix，801 都会把复杂系统压缩成可解释变量，再用图表证明这个变量能连接方法与工程指标。这个中间层是论文可发表性的核心资产。

第四，结果段同时报告精度、效率和工程意义。很多论文不只说预测准，还说快多少、少多少传感器、减多少质量、提高多少成功率、输出多少功率、约束是否满足。这使 claim 更贴近工程期刊的评价标准。

第五，边界控制保护强 claim。仿真论文不轻易写成工程成熟度，概念论文常用 `concept/evaluation/potential`，系统论文主动承认接口、寿命、压降、真实飞行、长期可靠性或参数范围限制。这会减少审稿人对过度外推的反感。

## 8. 证据强度标注

| 判断 | 证据强度 | 依据 |
| --- | --- | --- |
| 标题偏方法/对象/工程任务型，常用 `for`、`based on`、`with`、`under` | 强 | 49 篇标题统计；batch summaries 多次指出 method/model/application anchor |
| 摘要采用“工程背景 -> gap -> 方法 -> 验证 -> 定量结果”的结构 | 强 | 多篇单文 `## 2` 和 batch 1/2/4/7/9 明确归纳 |
| Introduction 通过方法流派/技术路径分类制造温和 gap | 强 | 绝大多数 `## 12/15` 提到分类综述、承认价值再指出边界 |
| Results/Discussion 用“读图 -> 趋势 -> 机制 -> 工程意义”推进 | 强 | batch 3/6/7/8 反复出现；单文 `## 12-14` 中大量对应句式 |
| Conclusion 偏编号、定量、对应前文 gap | 强 | batch summaries 反复总结；方法/工程论文尤为稳定 |
| limitation/future work 总是完整展开 | 中 | 部分论文明显，尤其控制、ML、系统集成、生物方向；短材料/方法论文较弱 |
| 语态偏被动、名词化和现在时，`we` 主动句很少 | 强 | 49 篇自动语言统计：被动 6832、`we` 主动 64、名词化 34728 |
| claim 强度采用“强数字 + 条件限定”的双层策略 | 强 | 结果表/结论数字密集，batch summaries 多次提示边界与参数范围 |
| `organization paragraph` 是固定模板 | 中 | 多篇长方法论文存在，但不是所有期刊/短文都固定出现 |
| 冒号标题是团队偏好 | 弱 | 少数标题出现，整体更偏长名词链与介词短语 |
| 写作风格完全来自 801 团队而非期刊/合作方 | 不可判断 | 样本跨期刊、跨合作方向；只能判断论文集合呈现出的稳定风格 |

## 9. 一句话总结

801 的写作系统可以概括为：用工程背景抬高问题价值，用温和分类综述制造可接受 gap，用方法/模型中间层承接复杂耦合，用图表和定量指标证明精度、效率与工程意义，再用边界条件控制 claim 强度。它不是华丽文风，而是一套非常审稿友好的工程论文表达机器。
