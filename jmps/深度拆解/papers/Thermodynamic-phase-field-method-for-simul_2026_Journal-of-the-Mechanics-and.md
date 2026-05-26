# Thermodynamic phase-field method for simulation of cement hydration

## 0. 读取说明
- 源 PDF：`jmps/文献/Thermodynamic-phase-field-method-for-simul_2026_Journal-of-the-Mechanics-and.pdf`
- 源 TXT：`jmps/文本/txt/Thermodynamic-phase-field-method-for-simul_2026_Journal-of-the-Mechanics-and.txt`
- 辅助参照：上一轮标准拆解用于核对主线，本文件重新按深度模板展开。
- 是否需要结合 PDF 图像核查：需要。TXT 可以读到模型变量、图注、结果叙事和参数研究，但微结构快照、温度/浓度场颜色、量热曲线吻合程度必须看 PDF。
- 本文类型：热力学相场模型 + 介观数值模拟 + 定性/归一化实验趋势对比。不是严格定量标定论文。
- 阅读覆盖：摘要、Introduction、水泥水化机制、数学框架、离散化、C3S 水化模拟、参数评估、结果与讨论、Conclusion、附录。

## 1. 基本信息与论文身份
- 题名：Thermodynamic phase-field method for simulation of cement hydration
- 作者/机构：Long Nguyen-Tuan；Timon Rabczuk。机构需以 PDF 首页为准。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 213 (2026) 106634。
- DOI：10.1016/j.jmps.2026.106634
- 关键词：Cement hydration；Meso-scale；Micro-structures；Phase-field；Thermodynamics；Heat release。
- 研究对象：C3S 水化过程中熟料溶解、C-S-H/CH 产物沉淀、离子输运、热释放和微结构演化。
- 研究尺度：介观二维 plane-pore 模型；局部相场、温度场和浓度场耦合。
- 方法类型：热力学相场、Kinetic Monte Carlo 成核、Allen-Cahn/Cahn-Hilliard 类相变-输运耦合、热守恒、有限差分/交错求解、参数敏感性分析。
- 证据类型：相分数演化、反应速率、温度/浓度场、热释放率与量热实验归一化对比、温度/溶解度/孔距参数研究。
- 目标读者：水泥水化建模、相场方法、多场耦合、早龄期材料性能预测和计算材料科学读者。
- JMPS 风格定位：把水泥化学问题力学化/热力学化，用局部自由能和守恒律解释经验量热曲线中的阶段性行为。

## 2. 摘要与核心信息提取
- 摘要的功能拆解：先说明溶解和沉淀建模对理解水泥水化机制重要；再提出热力学相场框架；随后强调模型在非平衡温度和浓度场下描述反应-输运耦合；最后给出 C3S 二维模拟结果和加速/减速阶段解释。
- 背景句承担什么：把水泥水化从工程材料问题转成“溶解-沉淀过程需要机制模型”的科学问题。
- gap 句承担什么：指出现有模型难以同时给出局部输运、热释放和非平衡浓度/温度耦合图像。
- 方法句承担什么：用 phase-field + thermodynamics + reaction-transport 说明框架新意。
- 结果句承担什么：宣称模型捕捉量热中常见的加速与减速阶段，并指出 diffusion-controlled 与 impingement-controlled 机制都重要。
- 意义句承担什么：指向早龄期水泥浆物理性质预测。
- 一句话主张：本文用热力学相场把 C3S 水化中的溶解、沉淀、离子输运和热释放统一起来，在二维介观模型中再现水化速率加速-减速并区分扩散与产物碰并机制。
- 3-5 个核心关键词：thermodynamic driving force；phase-field；reaction-transport；heat release；impingement-controlled deceleration。

## 3. 选题层深拆
- 问题来源：水泥水化速率曲线有典型诱导、加速、减速阶段，但经验模型多拟合总体热流，难以说明局部 C-S-H 产物如何阻碍离子输运、孔隙空间如何被填充、温度如何反过来影响反应。
- 问题为什么重要：早龄期强度、放热、开裂风险和微结构形成都取决于水化机制；减碳水泥和配方设计需要能解释机制的模型。
- 问题为什么现在值得做：相场方法已成熟，能够无显式追踪界面地描述微结构演化；水泥水化已有量热和显微实验可提供趋势对比；计算资源足以做二维介观耦合。
- 问题边界：主要是 C3S、二维 plane-pore、归一化热释放对比；成核部分仍有经验/KMC 设定；不是完整水泥浆 3D 多矿物预测。
- 选题的 JMPS 味道：用热力学自由能和守恒律替代经验速率，强调机制解释和多场耦合，而非单纯材料工程拟合。
- 选题可迁移性：可迁移到其他反应-输运-相变材料：把经验阶段曲线拆成局部场和界面动力学。

## 4. 领域位置与文献版图
- 作者如何划分已有研究：经验/JMAK 反应模型、微结构几何模型、lattice 或 cellular automata 模型、MD/atomistic 模拟、已有 phase-field/TDM 模型、实验量热/显微表征。
- 主要研究流派/方法路线：经验模型拟合总体速率；几何模型模拟颗粒形貌；MD 看局部分子机制；相场模型处理界面演化；实验用于热流和微结构验证。
- 每类研究解决了什么：经验模型易用；MD 解释纳米级反应；几何模型可给产物空间分布；相场可处理复杂界面；实验提供可校验趋势。
- 每类研究留下什么不足：经验模型缺局部场；MD 尺度太小；几何模型常预设形状或速率；已有相场仍可能使用独立经验速率，非等温/非等浓度耦合不足。
- 本文站在哪条线上：站在相场/TDM 和水泥水化机制之间，试图通过热力学驱动力统一溶解、沉淀、热和浓度。
- 最接近前人工作：Petersen 等水泥相场/TDM 研究，以及 Naber 等量热数据和 C3S 水化机制文献。
- 是否公平处理前人：基本公平，承认已有模型价值，同时强调其局部输运和统一热力学耦合不足。

## 5. Gap 制造机制
- 明示 gap：缺少一个能在介观尺度同时模拟溶解、沉淀、非等温、非平衡浓度和热释放的热力学相场框架。
- 隐含 gap：即使能拟合热流，也不一定能解释减速来自扩散阻碍还是产物 impingement；模型需要区分机制。
- gap 类型：方法 gap + 机制解释 gap + 多场耦合 gap。
- gap 证据来自哪里：Introduction 对比经验速率、MD、lattice 和已有 phase-field；结果中用窄孔距、温度和溶解度参数研究展示机制区分能力。
- gap 是否足够窄：中等。对象限定在 C3S 和二维局部孔隙，但模型目标较大。
- gap 是否足够重要：重要，因为水化热曲线的加速/减速是早龄期建模核心现象。
- 如果我是审稿人会如何追问：成核如果仍由 KMC/预设种子控制，是否削弱“热力学”主张？二维归一化对比是否足以证明预测能力？单一 nominal concentration 能否代表真实多离子溶液？这些是主要风险。

## 6. 创新性判断
- 作者声称的贡献：提出热力学相场框架模拟水泥水化；耦合反应动力学、离子输运和热释放；再现加速与减速阶段；展示温度和溶解度影响。
- 我判断的真实创新：把总自由能和局部驱动力用于界面运动，并让温度/浓度场与相变双向耦合；同时用局部场解释量热曲线。
- 创新类型：模型框架创新、机制分解、数值展示。
- 创新强度：中强。框架有新意，但数值验证偏定性。
- 创新必要性：必要。若只用经验热流模型，无法回答产物层阻碍、孔距缩小、局部浓度过饱和等机制问题。
- 创新与证据匹配度：对“能再现典型阶段和机制趋势”匹配；对“预测早龄期性质”仍需更多 3D 和参数标定。
- 容易被挑战的创新点：成核、参数取值、二维化、归一化量热对比和多离子简化。

## 7. 论证链条复原
背景：水泥水化涉及熟料溶解、产物沉淀、热释放和离子输运，决定早龄期性能。

文献：已有经验模型、几何模型、MD 和相场方法各能解释部分现象，但局部反应-输运-热耦合不足。

gap：缺少统一热力学相场框架来解释加速/减速阶段和微结构场演化。

问题：能否用局部自由能驱动相界面运动，并与温度和浓度守恒耦合，模拟 C3S 水化？

方法：定义相场变量表示 C3S、C-S-H、CH 和 pore solution；写相变、热守恒、浓度守恒和总自由能；离散求解二维 plane-pore。

证据：相分数变化、反应速率曲线、场分布、归一化热释放对比、温度和溶解度敏感性、窄孔距模拟。

发现：模型能给出加速-减速趋势；C-S-H 产物层造成扩散限制；孔隙中产物碰并也可导致减速。

机制：反应产生或消耗热与离子，局部浓度和温度改变热力学驱动力，产物层逐步形成输运屏障。

意义：为将来预测早龄期水泥浆物理性质和 3D 微结构演化提供框架。

## 8. 方法/理论/模型细拆
- 方法总框架：以多相相场变量描述固-液和产物；以热守恒追踪反应热；以浓度守恒追踪离子扩散和界面源项；以总自由能变分给出界面运动驱动力。
- 关键概念：C3S dissolution；C-S-H/CH precipitation；phase fraction；thermodynamic force；non-isothermal field；non-equilibrium concentration；diffusion-controlled；impingement-controlled。
- 关键变量/参数：相场 `phi_i`、温度 `T`、浓度 `C`、反应速率 `k_c`、热释放项、扩散系数、界面能参数、溶解度、初始温度、孔距。
- 核心假设：二维 plane-pore 可代表局部机制；一个浓度变量可概括离子环境；C-S-H/CH 可用相场处理；成核可用 KMC 或设定规则。
- 边界条件：局部孔隙模型中的初始相分布、温度、浓度和边界热/质输运条件；具体数值需核对 PDF 参数表。
- 方法步骤：1. 描述 C3S 水化机制；2. 建立相变方程；3. 建立热和浓度守恒；4. 定义自由能；5. 空间时间离散；6. 设定二维 C3S/pore 初始结构；7. 参数分析和结果讨论。
- 复现信息：公式、参数分析和边界描述较多，但真实复现需要代码、网格、时间步、KMC 成核细节和参数表核查。
- 方法复杂度是否合理：合理。水化过程本身多场耦合，phase-field 是合适选择；问题在于参数和验证是否支撑预测性。
- 方法与 gap 的对应关系：gap 是缺局部机制图像，方法直接输出相分数、热场、浓度场和微结构快照。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 热力学相场可描述 C3S 水化溶解与沉淀 | 摘要、第 3-5 节 | 相变方程、自由能、二维模拟 | 模型 + 数值 | 中强 | 参数和成核仍经验化 |
| 模型捕捉水化速率加速与减速阶段 | 摘要、第 6 节 | 反应速率曲线、热释放曲线与量热趋势 | 数值 + 归一化对比 | 中 | 不是绝对热流定量验证 |
| 扩散控制参与减速 | 摘要、第 6.2/6.4 | C-S-H 层、浓度场、窄孔距模拟 | 场分布 + 机制分析 | 中强 | 图像需 PDF 核查 |
| impingement 控制也参与减速 | 摘要、第 6.4 | 窄孔距和产物相互接触导致空间受限 | 数值机制演示 | 中 | 依赖二维几何设定 |
| 初始温度和溶解度影响水化进程 | 第 6.3 | 参数敏感性图 | 参数研究 | 中 | 实验对比有限 |
| 框架可为早龄期性能预测铺路 | 摘要、Conclusion | 多场输出和机制解释 | 推论 | 弱到中 | 需要 3D、多矿物和力学性能耦合 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | C3S 水化模型示意 | 溶解-沉淀-热-浓度耦合 | 提供变量关系总览 | 是 |
| 相变/热/浓度方程 | 数学框架 | 多场耦合 | 说明模型不是纯经验曲线 | 否，需核对符号 |
| 总自由能公式 | 热力学驱动力 | 相界面运动由能量变分驱动 | 支撑“thermodynamic”定位 | 否 |
| Fig. 2-4 | 参数分析和自由能形态 | 参数影响反应速率和驱动力 | 解释模型敏感性 | 是 |
| Fig. 6-10 | 相分数、反应速率、温度/浓度场 | 模型再现微结构与场演化 | 从局部场解释总热流 | 是 |
| Fig. 11 | 热释放率与量热归一化对比 | 捕捉加速/减速阶段 | 提供实验趋势支撑 | 是 |
| Fig. 14-15 | 窄孔距/impingement 模拟 | 减速机制分解 | 区分扩散与碰并控制 | 是 |

图表顺序服务论证的方式：先用概念图定义系统，再用公式给模型，再用参数图说明驱动力如何受温度/浓度影响，最后用微结构快照和热流曲线连回实验现象。整体是“概念-公式-机制-趋势对比”的叙事。

## 11. 章节结构与篇章布局
- Abstract：强调模型、耦合、C3S 示例和机制发现。
- Introduction：从水泥低碳和早龄期性质切入，再综述经验/微观/相场模型不足。
- Related Work/Background：第 2 节单独讲 hydration phenomena and mechanisms，是一个很好的物理背景缓冲。
- Method/Theory/Model：第 3-4 节按相变、热、浓度、自由能和离散化展开。
- Results：第 5-6 节，先设定 C3S 模拟，再按相分数、场分布、参数效应和窄孔距讲结果。
- Discussion：第 6 节与结果合并，每个结果后直接给机制解释。
- Conclusion：总结模型能力，并承认未来需要 3D 随机颗粒和可靠内禀参数。
- 章节之间如何过渡：机制背景引出变量选择；数学框架引出数值模拟；相分数结果引出热和浓度场解释。
- 哪一节最值得模仿：第 2 节。复杂模型前先讲清物理机制，能显著降低读者理解成本。
- 哪一节可能存在结构风险：参数评估部分可能偏经验，若没有 PDF 表格辅助，读者难判断参数可靠性。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Thermodynamic-phase-field-method-for-simul_2026_Journal-of-the-Mechanics-and.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：16
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 背景/引言型, 问题/机制型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Phenomena and mechanisms of cement hydration | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 3 Mathematical framework | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Phase transformation: | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Conservation law for heat: | 问题/机制型 | 围绕变量关系或机制问题组织读者预期 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Conservation law for ion concentration: | 问题/机制型 | 围绕变量关系或机制问题组织读者预期 | 高 | 是 | 保留具体变量/对象 |
| 3.4 Total free energy and functional derivative | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4 Spatial and temporal discretization | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5 Numerical simulation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1 Modelling the hydration of tricalcium silicate | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 5.2 Parameter, initial and boundary conditions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.3 Evaluation of model parameters | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 6 Result and discussion | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 6.1 Evolution of phase fractions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
- Introduction 段落推进：应用重要性 -> 现有模型类别 -> 每类不足 -> 相场机会 -> 本文贡献。
- Method 段落推进：每个变量先有物理含义，再有守恒律或自由能公式，最后说明耦合项。
- Results 段落推进：先观察相/场图，再解释局部机制，再联系热释放或实验曲线。
- Discussion/Conclusion 段落推进：结果被压缩为机制：扩散屏障、产物碰并、温度加速、溶解度改变驱动力。
- 常见段落开头方式：`Fig. X illustrates...`；`The model highlights...`；`The simulation results suggest...`。
- 常见段落收束方式：以机制归因或未来参数/3D 改进收束。
- 可复用段落模板：图像观察 -> 局部场变化 -> 对反应速率的影响 -> 与实验阶段性现象对应。

## 13. 文笔画像与语言习惯
- 整体语气：模型展示型，强调 capability、mechanism 和 qualitative agreement。
- claim 强度：中等偏强。对捕捉阶段性趋势较强，对预测早龄期性质较谨慎。
- 谨慎表达：`qualitative agreement`、`paving the way`、`carefully designed experiments are required`。
- 问题表达：`do not provide a picture`、`plays a key role`、`simplified`。
- 贡献表达：`we propose`、`we present`、`successfully captures`、`enables`。
- 机制表达：`transport-limiting barrier`、`diffusion-controlled`、`impingement-controlled`、`thermodynamic driving force`。
- 对比表达：与经验模型、MD、几何模型对比时多用功能差异。
- 限定边界表达：二维、C3S、normalized heat、future 3D。
- 术语密度：中高，化学符号和相场术语混合。
- 长句/短句习惯：模型描述长句多，结果解释较短。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：phase(81)；c-s-h(62)；hydration(54)；rate(49)；concentration(47)；dissolution(43)；pore(42)；heat(38)；model(34)；reaction(33)；temperature(32)；solution(31)；cement(30)；energy(30)；precipitation(28)；phases(28)；surface(27)；eld(26)；growth(25)；time(22)
- 高频学术名词：solution(62)；hydration(54)；concentration(47)；dissolution(43)；model(34)；reaction(33)；temperature(32)；energy(30)；cement(30)；precipitation(28)；simulation(22)；interface(21)；function(19)；equation(18)；parameter(17)；deceleration(17)
- 高频学术动词：proposed(7)；simulate(7)；compared(5)；demonstrate(5)；shown(5)；simulated(5)；derived(4)；investigated(4)；formulated(2)；solve(2)；indicate(2)；derive(1)；suggest(1)；investigate(1)；predict(1)；capture(1)
- 高频形容词：cement(30)；numerical(24)；thermodynamic(19)；local(18)；experimental(18)；ionic(15)；total(13)；stable(12)；initial(12)；chemical(10)；present(10)；critical(8)；unstable(8)；cient(8)；thermal(8)；spatial(8)
- 高频副词/连接副词：however(12)；consequently(10)；therefore(7)；approximately(6)；cantly(6)；typically(4)；respectively(4)；accordingly(4)；furthermore(3)；nally(3)；relatively(3)；physically(3)；simultaneously(3)；directly(3)；highly(3)；progressively(3)
- 高频二词短语：pore solution(24)；phase- eld(20)；cement hydration(19)；dissolution precipitation(16)；free energy(16)；nguyen-tuan rabczuk(14)；heat release(13)；reaction rate(10)；ionic concentration(9)；time step(9)；equilibrium concentration(8)；growth rate(8)；hydration process(7)；hydration products(7)；total free(7)；energy function(7)
- 高频三词短语：total free energy(7)；chemical free energy(6)；ionic concentration pore(5)；concentration pore solution(5)；bulk chemical free(5)；ective surface reactivity(5)；dissolution precipitation processes(4)；dissolution precipitation rates(4)；ect frequency factor(4)；growth rate c-s-h(4)；impingement hydration products(4)；acceleration deceleration stages(3)

**主动、被动与句法**

- 被动语态估计次数：120
- `we + 动作动词` 主动句估计次数：7
- 名词化表达估计次数：740
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：206
- 一般过去时线索：35
- 现在完成时线索：8
- 情态动词线索：21
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：hydration(7)；cement(6)；model(4)；phase-(3)；eld(3)；reaction(3)；thermodynamic(2)；simulation(2)
- 1. Introduction：hydration(8)；cement(6)；dissolution(6)；precipitation(5)；reaction(5)；phase(4)；however(4)；rate(4)
- 2. Phenomena and mechanisms of cement hydration：concentration(7)；phases(6)；phase(6)；hydration(5)；pore(5)；solution(5)；ionic(5)；heat(5)
- 3. Mathematical framework：eld(4)；hydration(2)；phase-(2)；c-s-h(2)；model(2)；dissolution(2)；precipitation(2)；based(1)
- 3.1. Phase transformation:：phase(10)；phases(4)；process(4)；rate(4)；function(4)；nucleation(3)；growth(3)；phase-(3)
- 3.2. Conservation law for heat:：heat(4)；thermal(4)；temperature(3)；phase(3)；equation(2)；rate(2)；total(2)；free(2)
- 3.3. Conservation law for ion concentration:：phase(7)；concentration(5)；usion(3)；coe(3)；cient(3)；solution(2)；term(2)；second(2)
- 3.4. Total free energy and functional derivative：energy(12)；function(9)；free(8)；phase(8)；bulk(6)；chemical(5)；term(4)；functional(4)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 原文表达模式：`Modelling dissolution and precipitation plays a key role in understanding mechanisms...`
- 可复用句型骨架：`Capturing the coupled dissolution-precipitation process is essential for explaining the staged evolution of X.`
- 中文写作启发：从“解释阶段性演化”而不是“提高拟合精度”切入，更有机制感。

### 14.2 方法与框架表达
- 原文表达模式：`a thermodynamic framework based on a phase-field approach is proposed...`
- 可复用句型骨架：`We formulate a phase-field framework in which interface motion, transport, and heat release are coupled through a thermodynamic driving force.`
- 中文写作启发：明确三类耦合对象和耦合媒介。

### 14.3 结果与趋势表达
- 原文表达模式：模型捕捉 acceleration and deceleration stages。
- 可复用句型骨架：`The simulated rate curve reproduces the characteristic acceleration-deceleration sequence observed in experiments.`
- 中文写作启发：趋势对比要说明“特征阶段”而不是只说吻合。

### 14.4 机制解释表达
- 原文表达模式：C-S-H 产物层形成 transport-limiting barrier。
- 可复用句型骨架：`The growth of the product layer gradually forms a transport-limiting barrier, thereby reducing the supply of reactants to the interface.`
- 中文写作启发：用“产物层-输运屏障-反应减速”三连表达机制。

### 14.5 贡献与意义表达
- 原文表达模式：`paving the way for predicting early-age physical properties...`
- 可复用句型骨架：`The framework provides a mechanistic basis for future prediction of process-dependent properties once calibrated in three-dimensional microstructures.`
- 中文写作启发：意义句要加前提，避免过度预测。

### 14.6 局限与未来工作表达
- 原文表达模式：需要 3D 随机颗粒、可靠参数和更精细实验。
- 可复用句型骨架：`Future work should extend the present two-dimensional demonstration to statistically representative three-dimensional microstructures and independently calibrated kinetic parameters.`
- 中文写作启发：未来工作要指向当前最弱证据。

## 15. 引用策略与文献使用
- 引用密度：Introduction 密集，结果部分少量引用实验量热和显微机制。
- 引用主要集中位置：水泥水化机制、经验模型、MD、相场、量热数据。
- 经典文献用途：水化动力学和相场自由能基础。
- 近年文献用途：说明相场水泥模拟和低碳水泥研究仍在发展。
- 方法文献用途：相场、KMC、离散化和热力学模型。
- 对比/批判性引用：温和指出已有方法“不能提供局部图像”或“依赖经验速率”。
- gap 如何靠引用搭建：先铺应用和机制文献，再用模型类别比较说明统一耦合不足。
- references 暗示的研究共同体：水泥化学、计算材料、相场、热分析实验。
- 引用风险：若“首次”类表述过强，可能被相场水泥文献挑战。

## 16. 审稿人视角风险
- 最大攻击面：定量验证不足和参数经验性。
- claim 是否过强：捕捉阶段趋势可接受；预测早龄期性质必须加未来条件。
- 证据是否不足：热流为归一化对比，不是绝对校准。
- 方法是否可复现：公式和参数说明有帮助，但成核、网格、代码细节可能不足。
- 对比是否充分：与实验趋势对比有，但与其他模型定量 benchmark 较弱。
- 边界条件是否清楚：二维 C3S plane-pore 边界较清楚，但外推范围有限。
- 替代解释是否排除：扩散与 impingement 都被讨论，但其他化学机制未充分验证。
- 图表是否需要进一步核查：所有微结构快照、热流曲线和参数图都需 PDF。

## 17. 可复用资产
- 可复用选题角度：把经验阶段曲线背后的局部场机制作为选题核心。
- 可复用 gap 制造方式：`已有模型能拟合总体量 -> 但不能给局部场解释 -> 需要多场热力学框架`。
- 可复用论证链：机制背景 -> 相场变量 -> 守恒律 -> 自由能 -> 介观模拟 -> 实验趋势对比。
- 可复用图表设计：概念示意图、相场快照、温度/浓度场、归一化实验对比、几何敏感性图。
- 可复用段落结构：每个结果段都用“图-场-机制-实验现象”闭环。
- 可复用句型骨架：`This behavior is attributed to...`；`The primary discrepancy likely stems from...`；`The model enables the simulation of...`。
- 可复用引用组织：按模型类别而非时间线组织文献。
- 不宜直接模仿之处：如果验证仅定性，不宜宣称强预测；如果成核经验化，不宜过度强调完全热力学自洽。

## 18. 对我写论文的启发
- 如果我要写类似论文，可以学什么：先讲物理机制，再讲模型变量，否则多场方程会显得任意。
- 可以迁移到 Introduction 的写法：把模型不足写成“缺少局部图像”和“缺少机制区分”。
- 可以迁移到 Method 的写法：每个场变量都要对应一个可观察机制。
- 可以迁移到 Results/Discussion 的写法：用参数研究证明模型能区分不同机制，而不只是拟合同一曲线。
- 需要避免的问题：不要用二维归一化对比支撑过强的三维预测 claim。

## 19. 最终浓缩
- 这篇论文最值得学：如何把多场相场模型写成一个解释实验阶段曲线的机制工具。
- 这篇论文最大风险：二维定性验证与预测早龄期性质之间仍有距离。
- 三个可迁移动作：1. 用概念图先交代变量耦合；2. 用局部场解释总体曲线；3. 在结论中明确 3D 和参数标定是下一步。
