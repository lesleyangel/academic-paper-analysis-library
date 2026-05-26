# The mechanics of the Less In More Out artificial heart: Modeling fabric-based soft robotic devices

## 0. 读取说明
- 源 PDF：`jmps\文献\The-mechanics-of-the-Less-In-More-Out-artificial_2026_Journal-of-the-Mechani.pdf`
- 源 TXT：`jmps\文本\txt\The-mechanics-of-the-Less-In-More-Out-artificial_2026_Journal-of-the-Mechani.txt`
- 是否需要结合 PDF 图像核查：需要。TXT 能支持全文语义、图注、章节和公式附近文字，但不能可靠判断曲线细节、误差条、颜色条、三维形态和局部图像。
- 本文类型：常规 JMPS 研究论文；本文件按 0-19 深度模板拆解。上一轮 `jmps/拆解/papers` 仅作为事实校验底稿，本轮重新组织为“细致拆解 + 写作素材”。

## 1. 基本信息与论文身份
- 题名：The mechanics of the Less In More Out artificial heart: Modeling fabric-based soft robotic devices
- 作者/机构：Marin Lauber 等；完整机构见 PDF 首页。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 212 (2026) 106565. doi:10.1016/j.jmps.2026.106565
- DOI：10.1016/j.jmps.2026.106565
- 关键词：Soft robotics,Artificial heart,Fabric textile actuator,Fluidic actuation,Fatigue analysis,Numerical design optimization
- 研究对象：Less In More Out (LIMO) 流体驱动织物软体全人工心脏/soft ventricle
- 研究尺度：从具体材料/结构/图像对象进入机制、模型或设计规则；章节标题包括：1. Introduction；2. Methods；2.1. Geometry；2.2. Kinematics；2.3. Governing equations；2.4. Constitutive modeling；0.195 GPa and 𝜇= 0.101 GPa. This eﬀective linear elastic law in Green–Lagrange strain provides a ﬁrst-order approximatio；2.5. Numerical solver；2.6. Cavity volume calculation；3. Results；3.1. Deformation and pressure–volume relationship；3.2. Buckling and folding；3.3. Afterload sensitivity；3.4. Local stress concentration and fatigue risk；3.5. Principal strain ﬁelds；4. In silico design exploration；4.1. Eﬀect of valve support geometry；4.2. Eﬀect of relative endocardial-epicardial compliance；5. Discussion；6. Conclusion；Appendix A. Material model calibration；Appendix B. Mesh sensitivity study；Appendix C. Deformation under various ventricular pressures and various pouch numbers；Appendix D. Fatigue estimate for diﬀerent ventricular pressures and pouch numbers；Appendix E. Sensitivity to initial conditions；References
- 方法类型：几何/运动学建模、壳单元非线性有限元、St. Venant-Kirchhoff 有效材料、压力-体积计算、von Mises 应力、principal strain、strain-life fatigue screening、in silico design exploration
- 证据类型：图 2-5 压力-体积和 afterload 响应；图 6-8 应力/应变/疲劳风险；图 9-10 几何和材料改型；附录材料拟合、网格敏感性、初始条件敏感性
- 目标读者：JMPS 中关注材料机制、本构建模、结构稳定性、图像判据、软物质或工程设计诊断的读者。
- JMPS 风格定位：这篇不是孤立应用报告，而是把一个具体对象提升为可验证的力学问题，并试图输出可迁移的 benchmark、机制解释、判据或设计规则。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：摘要通常按“背景/传统理解 -> 未解决 gap -> 本文方法 -> 关键发现 -> 意义”推进。它的强处是让读者在第一页就知道本文改变了什么判断。
- 背景句承担什么：建立对象的重要性，给读者一个进入 JMPS 问题的理由，而不是泛泛科普。
- gap 句承担什么：指出现有测试、模型、判据或实验只能看到一部分，不能回答本文真正关心的状态、路径、局部场或统计性质。
- 方法句承担什么：说明作者如何隔离变量、构造模型、扫描参数或提取图像特征，使 gap 变成可回答问题。
- 结果句承担什么：用少量定量结果或清晰转变支撑主张，让 contribution 不停留在“提出方法”。
- 意义句承担什么：把结果翻译成更广义的本构、设计、分类或机制价值。
- 一句话主张：把仿真从“复现实验”推进到“发现实验看不到的设计风险”。
- 3-5 个核心关键词：Soft robotics,Artificial heart,Fabric textile actuator,Fluidic actuation,Fatigue analysis,Numerical design optimization

## 3. 选题层深拆
- 问题来源：- 问题来源：LIMO 设备已有实验展示全局性能，但实验难以测量内部应力场、应变路径和疲劳热点。 - 为什么重要：软体人工心脏需要在生理载荷下高效工作并承受大量循环，局部 seam 和 buckling 可能决定寿命。 - 研究边界：准静态结构模型；未耦合真实血流和循环系统；织物用有效各向同性材料近似。 - JMPS 取向：把软机器人器件从“能动起来”推进到“可解释、可优化、可做耐久性设计”。
- 问题为什么重要：重要性不只来自对象本身，还来自该对象暴露出的通用困难：常规实验混合多个过程，结构失稳路径难以控制，本构变量和微机制脱节，传统判据过强，或全局性能无法揭示局部风险。
- 问题为什么现在值得做：当前实验、数值、图像处理和物理约束学习工具足以把过去只能定性描述的现象转成可度量证据。
- 问题边界：边界被限定在本文材料、结构、加载、图像或数据窗口中。这个边界让证据链闭合，也意味着不能无条件外推到所有同类系统。
- 选题的 JMPS 味道：把一个具体系统写成“机制/模型/判据/设计规则”问题，而不是只报告工程性能。
- 选题可迁移性：可学的是重新切分对象和证据的动作：先找被传统观察遮蔽的层次，再设计能直接暴露该层次的实验或模型。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：- 既有版图：软机器人、织物驱动器、软人工心脏、mock loop 实验、心血管计算模型、疲劳分析。 - 作者制造的 gap：缺少一个实用且验证过的数值框架，能在 fabric-based fluidically actuated total artificial heart 中解析 stress/buckling/fatigue fields。 - gap 类型：工具 gap + 设计诊断 gap。 - gap 是否成立：成立。实验提供全局 PV/stroke/efficiency，但不能直接提供局部耐久性指标。
- 主要研究流派/方法路线：可分为经典理论或经验观察、现代实验/数值/图像工具、以及应用牵引的设计或预测需求三类。
- 每类研究解决了什么：经典文献提供概念和基本方程；方法文献提供实现路径；近年应用文献提供为什么需要更强预测能力的动机。
- 每类研究留下什么不足：不足通常在交叉处：已有研究能解释现象 A 或预测量 B，但不能隔离本文关心的状态、局部场、相图边界、统计判据或 feature 依赖。
- 本文站在哪条线上：本文站在已有工具之后，强调把工具组织成一个能回答具体 gap 的闭环。
- 最接近前人工作：上一轮底稿指出了相邻经典和近年工作；深度阅读时应重点核查 Introduction 中最接近方法是否被公平比较。
- 是否公平处理前人：总体是“继承 + 补足”的写法，很少直接贬低前人，这符合 JMPS 对累积性贡献的偏好。

## 5. Gap 制造机制
- 明示 gap：缺少一个实用且验证过的数值框架，能在 fabric-based fluidically actuated total artificial heart 中解析 stress/buckling/fatigue fields。
- 隐含 gap：如果不引入本文框架，读者只能得到现象描述或经验拟合，无法知道背后的状态变化、稳定性拓扑、微结构竞争、对称判据、成分调制或局部风险。
- gap 类型：对象 gap、机制 gap、方法 gap、数值 gap、判据 gap 或设计诊断 gap。
- gap 证据来自哪里：来自文献分组、baseline 对比、方法必要性和图表结果的递进。
- gap 是否足够窄：较窄；它被收束到具体材料、结构、参数、图像或器件，而非泛泛宣称领域空白。
- gap 是否足够重要：足够重要，因为解决后能产生可迁移的模型、实验基准、相图、图像指标或设计 workflow。
- 如果我是审稿人会如何追问：最可能追问最接近前人是否遗漏、参数窗口是否太小、机制证据是否直接、图像和误差是否支撑强 claim。

## 6. 创新性判断
- 作者声称的贡献：建立计算框架；复现实验 PV 行为；比较 pouch number；识别 seams 和 buckling zones；探索 valve support 和 endocardial/epicardial compliance。
- 我判断的真实创新：把全局泵血性能指标和局部疲劳风险放在同一模型里权衡，而不是单纯优化 stroke volume。
- 创新类型：计算工具 + 设计优化示范 + 风险地图。
- 创新强度：中等偏高。器件特定性强，但对织物软机器人有方法迁移价值。
- 创新必要性：必要性来自 gap：没有本文的隔离、调谐、正则化、判据或局部场解析，就无法支撑主张。
- 创新与证据匹配度：核心 claim 有图表支撑；外推性意义需要按作者给出的边界理解。
- 容易被挑战的创新点：材料模型一阶近似；疲劳用 bulk TPU 数据，不能给 bonded fabric seams 的绝对寿命。

## 7. 论证链条复原
用 `背景 -> 文献 -> gap -> 问题 -> 方法 -> 证据 -> 发现 -> 机制 -> 意义` 复原：织物软体人工心脏有潜力但耐久性是瓶颈 -> 实验只能看全局压力-体积和失效位置 -> 作者建立 LIMO soft ventricle FE 模型并与 published static inflation experiments 对标 -> 模型复现 nonlinear PV、inflation onset 和 afterload sensitivity -> pouch 数少带来更大 stroke volume 但更高峰值应力和疲劳风险 -> full-field 结果显示 heat-sealed seams、tension paths 和 buckling zones 是风险热点 -> 设计探索显示降低 valve support aspect ratio 或软化 endocardial surface 可降低峰值应力且保持输出 -> 框架可指导下一代软体心脏和织物软机器人。

深度拆解看，这条链的关键是“每一步让下一步不可避免”。背景给重要性，文献给已有能力，gap 给必要性，方法给可验证路径，图表给证据，Discussion 再把证据转成机制或设计语言。写作时可以模仿这种递进，但不能省略 baseline，否则创新会显得悬空。

## 8. 方法/理论/模型细拆
- 方法总框架：定义几何和 pouch number -> 建立运动学/控制方程 -> 有效材料拟合 -> 非线性壳有限元求解 -> 计算 cavity volume/PV -> 后处理应力、主应变和 fatigue index -> 改型探索。
- 关键概念：Soft robotics,Artificial heart,Fabric textile actuator,Fluidic actuation,Fatigue analysis,Numerical design optimization
- 关键变量/参数：从 TXT 可见的变量包括章节标题、公式附近符号、图注中的控制参数和输出指标；完整符号表需结合 PDF 核查。
- 核心假设：织物可用各向同性 StVK 有效材料一阶表示；准静态足以比较设计；bulk TPU strain-life 可作相对疲劳筛查。
- 边界条件：本文只对其测试/模拟/图像/数据范围内的 claim 最可靠。
- 方法步骤：先定义对象和 baseline，再引入本文方法，随后做对比、参数扫描或验证，最后讨论机制与边界。
- 复现信息：TXT 足以提取方法逻辑，但完整复现需要 PDF 图、参数表、补充材料、代码/数据可用性说明。
- 方法复杂度是否合理：合理，因复杂度对应 gap；但写作时要防止公式或网络/数值细节压倒问题主线。
- 方法与 gap 的对应关系：本文方法不是装饰，而是为了看见传统路径看不到的那一层证据。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 把仿真从“复现实验”推进到“发现实验看不到的设计风险”。 | 摘要/结论 | 摘要主张、核心图表、Discussion 收束共同支撑 | 综合证据 | 中强 | 各向同性 StVK 无法捕捉织物各向异性、弯曲刚度、纱线旋转和摩擦锁定。 |
| 把全局泵血性能指标和局部疲劳风险放在同一模型里权衡，而不是单纯优化 stroke volume。 | Introduction/Results | 方法设计与 baseline 对比显示本文并非单纯重复已有工作 | 方法+对比 | 中强 | 需确认最接近前人是否充分比较 |
| 本文的结果链能够从现象推进到机制或设计规则 | Results/Discussion | 图表按 baseline、核心结果、参数/机制、意义展开 | 图表叙事 | 中强 | 机制有时是推断而非直接观测 |
| 方法复杂度与 gap 基本匹配 | Method/Theory | 实验、数值、理论或网络模块分别对应隔离、预测、分类、调谐或筛查任务 | 方法论证 | 中 | 参数与复现细节需查 PDF |
| 作者主动控制外推边界 | Discussion/Conclusion | 结尾列出材料、载荷、图像、模型或数据窗口限制 | 边界说明 | 强 | 摘要和标题的强表述仍需正文支撑 |
| 图表系统承担主要说服功能 | Figures/Tables | 图注和正文显示多图共同完成对象、方法、结果、机制、应用的分工 | 视觉证据 | 中强 | 图像本体必须核查 |

这张表说明：核心 claim 通常由多种证据共同支撑，而不是只靠一张图。写作时应避免把 Discussion 中的机制推断写成与实验观察同等强度的事实。

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig./Table | Fig. 1. Computational domain of the soft ventricle and deformation during inﬂation. Isometric view of the computational domain Ω0 = | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 2. Deformation during pouch inﬂation under zero-afterload conditions. Devices with pouch numbers 𝑁𝑝∈{4, 6, 8, 10} are shown under a | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 3. Pressure–volume relationship of the soft ventricle under a ventricular pressure of 3.8 kPa for various pouch numbers 𝑁𝑝∈ | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 4. Local buckling-induced jump in the pressure–volume response. Left: Detail of the pressure–volume relationship curve for a represen- | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 5. Afterload sensitivity and mechanical eﬃciency across pouch numbers. Top left: Actuation (pouch) volume versus actuation pressure | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 6. Local stress concentrations across pouch numbers and ventricular pressures. Von Mises stress distribution at 𝑃𝑎= 𝑃𝑎,max for pouch | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 7. Fatigue life risk index for the device. Left: Strain–life curve for a pure TPU polymer with plastic and elastic parts and the experimental | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 8 visualizes the maximum principal strain direction 𝒗1 on the outer epicardial and inner endocardial surfaces of the device. | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 8. Inner and outer principal strain directionality in the soft artiﬁcial heart design. Direction of the maximum principal strain 𝒗1 repre- | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 9. Eﬀect of valve support geometry on global performance and local stress concentrations. Pressure–volume response and von Mises | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |
| Fig./Table | Fig. 10. Eﬀect of relative endocardial-epicardial compliance on global performance and local stress concentrations. Pressure–volume re- | 支撑本文核心 claim 的阶段性证据 | 图注可判断功能，图像细节需核查 | 是 |

图表顺序服务于论证节奏：先交代对象和方法，再给 baseline，随后展示核心变化，最后用参数图、机制图、误差图或风险图把结果变成可复用规律。由于 TXT 只能读图注，涉及图像本体的判断必须回到 PDF。

## 11. 章节结构与篇章布局
- Abstract：压缩整篇论证，突出反转或新能力。
- Introduction：从广背景快速收束到具体 gap，文献按能力组织。
- Related Work/Background：若没有独立小节，则嵌入 Introduction 与 Method。
- Method/Theory/Model：承担“为什么本文能回答 gap”的技术可信度。
- Results：按 baseline、核心结果、参数/机制、意义推进。
- Discussion：- Introduction：从软机器人到人工心脏，再明确实验无法获取内部力学场。 - Methods：几何、运动学、控制方程、材料、求解器、体积计算，工程可复现感强。 - Results：先全局 PV，再 buckling/afterload，再局部 stress/fatigue/strain。 - In silico design：用两个低成本设计变量展示框架价值。 - Discussion：每段标题都是结论，同时坦诚材料与流固耦合限制。 - Conclusion：强调 transferable workflow。
- Conclusion：把发现收束成可迁移贡献，同时限制外推。
- 章节之间如何过渡：过渡靠问题链，而不是机械地介绍下一节。
- 哪一节最值得模仿：Results 到 Discussion 的转换最值得学，因为它把图表事实变成机制/设计语言。
- 哪一节可能存在结构风险：方法密集小节可能让非本领域读者失去主线，需要流程图和主题句。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-mechanics-of-the-Less-In-More-Out-artificial_2026_Journal-of-the-Mechani.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：15
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Geometry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Kinematics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Governing equations | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.4 Constitutive modeling | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.5 Numerical solver | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.6 Cavity volume calculation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Results | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Buckling and folding | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Afterload sensitivity | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Local stress concentration and fatigue risk | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 In silico design exploration | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Discussion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：对象重要性 -> 既有研究能力 -> 未解 gap -> 本文策略和贡献。
- Method 段落推进：对象定义 -> 变量/方程/实验/算法 -> 实现细节 -> 验证路线。
- Results 段落推进：每段围绕一个图或一个 claim，先给趋势，再给机制解释。
- Discussion/Conclusion 段落推进：先整合结果，再对照文献，最后给边界和迁移价值。
- 常见段落开头方式：`To isolate...`、`We first...`、`Having established...`、`These results suggest...`。
- 常见段落收束方式：用 `Together`、`This indicates`、`These findings` 把事实收束到机制。
- 可复用段落模板：`传统理解/基线 -> 本文操作 -> 图中差异 -> 机制解释 -> 对模型或设计的启发`。

## 13. 文笔画像与语言习惯
- 整体语气：- 整体语气：工程设计诊断型，强调 `framework`, `hotspots`, `trade-offs`, `proof of concept`。 - 常用问题表达：`experiments alone cannot resolve`, `durability-limiting features` - 常用贡献表达：`reproduces key global observations`, `resolving full-field...` - 常用机制表达：`buckling-induced jump`, `tension-line load paths`, `stress concentrations along heat-sealed seams` - 常用限定表达：`first-order`, `relative fatigue risk`, `quasi-static`, `effective isotropic` - 可复用句式：`X improves Y while preserving Z` 用于设计优化结果。
- claim 强度：核心范围内强，外推处谨慎。
- 谨慎表达：常用 `suggest`, `consistent with`, `over the explored range`, `relative`, `first-order`, `requires further validation`。
- 问题表达：强调“现有方法遮蔽/无法解析/判据不适用”，比简单说“缺少研究”更高级。
- 贡献表达：把贡献写成能力，如 isolate、recast、reshape、capture、detect、predict、screen、enable。
- 机制表达：常通过 transition、competition、coupling、state、landscape、hotspot、feature dependency 组织。
- 对比表达：baseline 对比是文笔骨架。
- 限定边界表达：Discussion/Conclusion 主动承认限制。
- 术语密度：高，但围绕少数核心术语重复。
- 长句/短句习惯：方法段长句多，结果主题句较短。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：pressure(122)；device(89)；pouch(81)；volume(76)；ventricular(76)；actuation(69)；stress(64)；strain(51)；kpa(51)；valve(49)；deformation(47)；fatigue(44)；ation(43)；stroke(37)；erent(36)；soft(34)；support(34)；pressures(34)；con(33)；pouches(32)
- 高频学术名词：pressure(122)；deformation(94)；actuation(69)；stress(64)；strain(51)；ation(43)；model(29)；guration(29)；material(25)；conditions(25)；reference(24)；ness(17)；framework(16)；sensitivity(16)；response(14)；performance(14)
- 高频学术动词：shown(16)；shows(14)；predicted(7)；investigate(6)；show(6)；capture(5)；estimate(5)；demonstrate(4)；evaluated(3)；simulated(3)；validate(2)；suggest(2)；suggests(2)；reveal(2)；compared(2)；evaluate(2)
- 高频形容词：local(54)；experimental(54)；numerical(38)；erent(36)；global(34)；fabric(27)；material(25)；initial(25)；cial(23)；mechanical(22)；principal(20)；elastic(18)；static(16)；total(16)；computational(16)；present(16)
- 高频副词/连接副词：experimentally(34)；respectively(21)；approximately(16)；however(10)；weakly(8)；therefore(7)；nearly(5)；strongly(4)；uidically(4)；fully(4)；recently(3)；connolly(3)；robustly(3)；linearly(3)；similarly(3)；slightly(3)
- 高频二词短语：ventricular pressure(43)；actuation pressure(39)；stroke volume(32)；valve support(29)；pressure volume(25)；con guration(24)；arti cial(23)；pouch numbers(23)；von mises(21)；pressure kpa(21)；ventricular pressures(20)；sti ness(17)；stress concentrations(16)；mises stress(16)；principal strain(15)；fatigue life(14)
- 高频三词短语：ventricular pressure kpa(17)；von mises stress(16)；arti cial heart(11)；valve support aspect(10)；arti cial hearts(10)；local stress concentrations(10)；peak von mises(9)；total arti cial(8)；initial con guration(8)；pressure volume response(8)；support aspect ratio(7)；soft arti cial(7)

**主动、被动与句法**

- 被动语态估计次数：83
- `we + 动作动词` 主动句估计次数：22
- 名词化表达估计次数：949
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：197
- 一般过去时线索：47
- 现在完成时线索：5
- 情态动词线索：28
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：arti(4)；cial(4)；soft(4)；device(4)；fatigue(4)；heart(3)；devices(3)；department(3)
- 1. Introduction：soft(11)；fatigue(11)；arti(9)；cial(9)；stress(7)；devices(6)；arfaee(6)；hearts(6)
- 2. Methods：无明显高频项
- 2.1. Geometry：pouches(8)；device(7)；ventricle(5)；pouch(5)；odd(4)；pressure(4)；physical(3)；fabric(3)
- 2.2. Kinematics：valve(24)；con(16)；guration(15)；initial(10)；support(9)；device(8)；reference(8)；mapping(7)
- 2.3. Governing equations：pressure(14)；tensor(7)；ventricular(6)；stress(4)；vector(3)；cauchy(3)；deformation(3)；initial(3)
- 2.4. Constitutive modeling：kirchho(3)；coated(3)；fabric(3)；stress(3)；gpa(3)；tpu-coated(2)；nylon(2)；tensile(2)
- 2.5. Numerical solver：nite(3)；element(3)；sti(3)；use(2)；pressure(2)；loading(2)；hilber(2)；shell(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：先承认已有进展，再指出关键对象仍被混淆、不可测、不可控或判据不适用。
- 可复用句型骨架：`Although X has been extensively studied, Y remains unresolved because Z.`
- 中文写作启发：gap 要写“为什么现有方法看不到”，不要只写“研究较少”。
### 14.2 方法与框架表达
- 原文表达模式：`To decouple/capture/detect/control X, we combine A with B.`
- 可复用句型骨架：`We first establish a baseline, then introduce X to quantify Y.`
- 中文写作启发：方法模块要和 gap 一一对应。
### 14.3 结果与趋势表达
- 原文表达模式：先总体趋势，再关键定量，再与 baseline 比较。
- 可复用句型骨架：`Increasing X shifts the response from A to B, while C remains nearly unchanged.`
- 中文写作启发：结果要提炼成转变、边界或权衡。
### 14.4 机制解释表达
- 原文表达模式：`This behavior can be attributed to...` / `These observations suggest...`
- 可复用句型骨架：`The competition between X and Y governs the transition from A to B.`
- 中文写作启发：机制推断要和证据强度匹配。
### 14.5 贡献与意义表达
- 原文表达模式：贡献被写成新能力，而非仅“提出模型”。
- 可复用句型骨架：`This work recasts X from Y into Z and provides a framework for A.`
- 中文写作启发：让读者知道读完后能做什么。
### 14.6 局限与未来工作表达
- 原文表达模式：主动限定窗口、模型和数据。
- 可复用句型骨架：`The present study focuses on X; extending it to Y requires Z.`
- 中文写作启发：局限写得好，会保护主 claim。

## 15. 引用策略与文献使用
- 引用密度：- 引用密度：Introduction 和 Discussion 高，方法部分引用较少。 - 文献组织：软机器人和织物驱动器 -> 软体人工心脏 -> 计算建模和 fatigue -> 织物材料局限。 - 引用姿态：对实验原型是继承和补充；对织物材料模型局限主动承认。 - 引用偏好：近年软机器人/人工心脏文献多，搭配疲劳与织物力学经典文献。
- 引用主要集中位置：Introduction、Method 选择依据和 Discussion 机制对照。
- 经典文献用途：建立概念合法性和理论基线。
- 近年文献用途：说明应用需求与当前技术窗口。
- 方法文献用途：支撑实验规范、数值方法、图像算法、网络结构或本构模型。
- 对比/批判性引用：多用温和转折，少用直接否定。
- gap 如何靠引用搭建：把已有研究分成“能解决什么/不能解决什么”。
- references 暗示的研究共同体：本文通常跨越固体力学、材料科学、计算方法和具体应用社群。
- 引用风险：若缺少最接近 competitor，审稿人会质疑 gap。

## 16. 审稿人视角风险
- 最大攻击面：- 最容易被质疑：各向同性 StVK 无法捕捉织物各向异性、弯曲刚度、纱线旋转和摩擦锁定。 - claim 与证据匹配：相对设计比较和热点识别匹配；绝对疲劳寿命不应过度解读。 - 方法风险：未耦合血流惯性、循环边界和患者特异性；省略局部连接/入口/裙边可能影响热点。 - 需进一步核查：图 6-8 的 stress/strain/fatigue maps 和图 9-10 的百分比改善需结合 PDF 图像确认。
- claim 是否过强：核心范围内可接受；标题和摘要中的广义意义需靠正文限定。
- 证据是否不足：宏观或数值证据较足，微观/真实工况/长期循环/多材料泛化可能不足。
- 方法是否可复现：需要 PDF、补充材料和参数表进一步核查。
- 对比是否充分：baseline 有，但最接近前人对比需重点检查。
- 边界条件是否清楚：正文通常清楚，摘要较强。
- 替代解释是否排除：部分机制仍可能存在替代解释。
- 图表是否需要进一步核查：需要，尤其所有图像本体。

## 17. 可复用资产
- 可复用选题角度：- 可复用选题角度：从全局性能实验转向局部失效机制和设计权衡。 - 可复用论证套路：实验基准 -> 模型复现全局响应 -> 解析不可测局部场 -> 相对疲劳筛查 -> 低成本改型示范。 - 可复用写法：主动把简化模型定位为 first-order screening，避免被绝对预测要求击穿。 - 可复用图表：PV 曲线 + stress map + principal strain directions + fatigue risk index + design variable 对比。 - 不宜直接模仿：没有实验基准时，不宜宣称计算框架可优化医疗器械设计。
- 可复用 gap 制造方式：从传统方法遮蔽的层次入手。
- 可复用论证链：baseline -> intervention/framework -> evidence -> mechanism -> boundary。
- 可复用图表设计：对象图、方法图、核心曲线、参数/相图、机制示意、边界/风险图。
- 可复用段落结构：主题句 + 图中事实 + 机制解释 + 下一步引导。
- 可复用句型骨架：`X is often viewed as Y; here we show that Z.`
- 可复用引用组织：文献按能力分组。
- 不宜直接模仿之处：没有直接证据时不要模仿强反转标题。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：- 最值得学习：把仿真从“复现实验”推进到“发现实验看不到的设计风险”。 - 最大风险：材料和疲劳模型简化使局部定量可靠性有限。 - 可迁移三件事：全局验证先行；局部风险用相对指标表达；把设计改型做成保输出、降风险的权衡叙事。
- 可以迁移到 Introduction 的写法：先把大问题收窄到一个可测/可算/可判定 gap。
- 可以迁移到 Method 的写法：每个方法模块都对应一个 claim。
- 可以迁移到 Results/Discussion 的写法：Results 讲证据，Discussion 讲机制和边界。
- 需要避免的问题：不要把特定系统结论外推成普遍定律；不要让复杂方法掩盖问题链。

## 19. 最终浓缩
- 这篇论文最值得学：把仿真从“复现实验”推进到“发现实验看不到的设计风险”。
- 这篇论文最大风险：材料和疲劳模型简化使局部定量可靠性有限。
- 三个可迁移动作：建立 baseline；设计直接对准 gap 的方法；把图表结果翻译成机制、判据或设计规则，并明确边界。
