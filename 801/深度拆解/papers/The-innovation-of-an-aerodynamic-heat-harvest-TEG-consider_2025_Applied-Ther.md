# The innovation of an aerodynamic-heat-harvest TEG considering multi-interface contact effect for a high-speed flight vehicle

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.txt` 的全文抽取，并参考 `801/文本/metadata/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.json` 的目录与元数据。txt 存在双栏串栏，尤其是 Introduction 首页、Table 11-13、Conclusion 与 References 附近，正文和表格/参考文献混排明显。涉及 TEG 爆炸图、粗糙表面重构、微尺度接触云图、Mises 应力云图、电压/输出功率曲线和实验平台照片处均标注“需要 PDF 图像复核”。主体以中文分析为主，只短引 TEG、TCR、ECR、silver-epoxy adhesive、force-bearing frame 等关键词。

## 1. 基本信息与论文身份

- 题名：The innovation of an aerodynamic-heat-harvest TEG considering multi-interface contact effect for a high-speed flight vehicle。
- 作者：Shi-Yuan Chen, Hai-Peng Chen, Ge Gao, Chun-Lin Gong, Yang Wu, Jian-Jun Gou。
- 期刊与年份：Applied Thermal Engineering, 258, 2025, Article 124687。
- DOI：10.1016/j.applthermaleng.2024.124687。
- 关键词：Aerodynamic heat harvest；Thermoelectric generator；Thermal contact resistance；High-speed flight vehicles。
- 论文类型：面向高速飞行器气动热采集的 TEG 结构设计、接触效应建模和实验/数值验证论文。
- 研究对象：安装于压缩面、同时承担 heat-harvest 与 force-bear 功能的多界面 TEG，包含 27 对圆柱 TE legs、54 对 electrodes、两个 substrates、绝缘层和 force-bearing frame。
- 核心方法：接触式粗糙度测量 + W-M fractal 重构；TCR/ECR 微尺度数值模型；等效界面层；TEG 热-电-力耦合评价；TCR 间接实验、TEG 输出电压实验验证。
- 主要证据：加载压力 0.8179-3.041 MPa、不同平均温度、vacuum/air/silver-epoxy clearance 下 TCR/ECR 变化；TCR 模型最大偏差 13.4%；整机最大电压 6.978 V、输出功率 12.41 W、转换效率 2.334%；等效界面模型偏差 0.444%；实验输出电压最大偏差 -19.69%。
- 目标读者：高超声速热电能量采集、多功能 TPS、热电器件接触热/电阻、飞行器载荷集成设计研究者。

这篇论文是从“接触效应定量研究”走向“真实整机 TEG 设计制备”的一篇。它的价值不在单纯证明 TCR/ECR 影响 TEG，而是在多界面、可承载、真实制备的 TEG 中把接触效应纳入设计评价。

## 2. 摘要与核心信息提取

一句话主张：高速飞行器压缩面存在可采集的大温差气动热，本文设计并制备一种具有承载框架和 27 对圆柱热电腿的气动热采集 TEG，并在考虑多异质界面 TCR/ECR 的条件下预测和实验验证其电输出与力学性能。

摘要按“三步贡献”组织。第一步是结构设计与制备：TEG 包含 force-bearing frame、twenty-seven couples cylindrical TE legs、fifty-four couples electrodes、substrates、insulation layer 和 heterogeneous interfaces，使其具备 heat-harvest 与 force-bear 双功能。第二步是界面建模：基于接触式测量与 W-M function 重构 TE legs/electrodes 粗糙表面，建立 TCR/ECR 数值模型并用间接实验验证，分析 pressure、temperature、clearance medium 影响。第三步是整机性能：在典型气动条件下分析热电转换与力学性能，得到最大电压 6.978 V、输出功率 12.41 W。

核心信息是“多界面接触效应不再是后验修正，而是整机 TEG 评价模型的一部分”。文章特别强调 imperfect contact 会导致 heat/electrical flow shrinkage，即热流和电流收缩效应，从而表现为 TCR 和 ECR，显著影响 TE transfer and conversion process。

## 3. 选题层深拆

选题来源是高速/高超声速飞行器长航时飞行造成严重气动热积累，而压缩面天然具有外热源与内冷端之间的大温差。传统 TPS 主要依赖高发射率涂层和低导热隔热结构，热容量和能量利用有限；将 TEG 集成到 TPS 或压缩面可以把一部分气动热转成电能，为热管理与载荷供电提供新路径。

作者把选题收束到“真实 TEG 的多界面接触效应与承载设计”。已有很多 TEG 在低温差、小载荷或理想接触条件下工作，高速飞行器压缩面却同时有高温差、气动力/机械载荷和多异质界面。TEG 不能只是热电腿和电极的串联，还要通过 force-bearing frame 抵抗外载，避免 TE legs 局部应力过大。

选题价值分三层。工程价值是气动热 harvest：将原本必须防护/散出的热转化为电输出。结构价值是 force-bear：TEG 不仅发电，还要在压缩面服役。方法价值是 contact-aware：将 TCR/ECR、粗糙面形貌、加载压力、温度和介质等因素纳入评价。这个选题比单纯“优化 TEG 输出功率”更接近真实飞行器集成问题。

## 4. 领域位置与文献版图

Introduction 先把高速飞行器气动热与传统 TPS 限制作为背景，再引入 integrating TEG into TPS 的路线。作者指出高飞行器相比多数小温差 TEG，有更大的温度梯度，但也要求更稳定的高温差性能。

随后文献转向接触效应。作者说明 TEG 的 TE legs 与 electrodes 之间存在多界面，粗糙表面导致真实接触面积有限和接触间隙，大量热流/电流通过微接触点收缩，形成 TCR/ECR。前人研究多集中在金属材料接触、单对或少数 TE couples、热源/冷源与 TEG 接触，而 TE materials 与 electrodes 的多界面整机接触效应研究较少。

第三部分是粗糙表面表征与实验测量文献：W-M fractal、GW statistical、semi-deterministic、direct measurement 等。作者指出 27 对 TE couples 意味着 108 个 TE leg surfaces 和 108 个 electrode surfaces，全部光学测量成本不可承受，因此采用接触式测量确认 + W-M fractal 重构的折中路径。

本文站位是承接 2023 年团队的 contact effects quantitative study，但把对象从较小 TEG/接触对推广到真实多界面 TEG，并增加制备、承载框架和气动载荷验证。

## 5. Gap 制造机制

文章制造 gap 的方式是“真实高速飞行器 TEG 需要同时考虑热电、接触和力学，而已有研究常只处理其中一部分”。具体来说：

1. 应用 gap：大多数 TEG 研究面向小温差废热、汽车、太阳能或普通热源，少有面向高速飞行器压缩面气动热采集。
2. 接触 gap：TCR/ECR 研究多集中于常规金属或少数 TE couples，缺少多界面 TE materials/electrodes 接触效应。
3. 测量 gap：整机大量界面若全部实测表面形貌，成本不可承受，需要可扩展粗糙面重构方法。
4. 结构 gap：高速飞行器外表面 TEG 必须承载，普通 square TE legs 易有应力集中，需结构设计降低局部损伤风险。
5. 验证 gap：仅有接触模型或热电仿真不够，整机输出电压/功率需要实验平台验证。

这个 gap 的说服力较强，因为它将传统 TEG 的三个常被分开的议题合并：界面接触、热电转换、结构承载。风险是每个 gap 都较大，文章必须用足够多的图表和实验支撑，因而结构复杂。

## 6. 创新性判断

作者声明/体现的创新包括：设计并制备具有 force-bearing frame 的气动热采集 TEG；采用圆柱 TE legs 避免方形腿应力集中；基于接触式测量和 W-M function 重构大量 TE/electrode 粗糙表面；建立 TCR/ECR 模型并通过间接实验验证；建立等效界面层评价整机；在典型气动条件下给出电输出和力学响应。

真实创新属于“真实器件设计 + contact-aware 多尺度评价”。相比 2023 年偏方法化的定量研究，2025 年论文更强调器件创新与制备：27 对 TE legs、54 对 electrodes、圆柱腿、承载框架、压缩面应用。接触模型是支撑手段，器件构型和整机验证是贡献中心。

创新强度：中到强。TEG 发电原理、W-M fractal、TCR/ECR 模型不是新理论；但在高速飞行器气动热场景下，构建可承载、多界面、实验验证的 TEG，工程贡献较强。

可被挑战的是“innovation”标题略强：从算法/理论角度可能是整合与工程实现，而不是基础创新。但在 Applied Thermal Engineering 的工程应用语境下，真实制备和多界面评价足以支撑。

## 7. 论证链条复原

全文论证链如下：

1. 高速飞行器产生长时大气动热，压缩面有气动热采集潜力。
2. TEG 可将温差转为电能，但飞行器 TEG 必须面对高温差、机械载荷和多异质界面。
3. 多界面 imperfect contact 导致热流/电流收缩，表现为 TCR/ECR，影响 TEG 输出。
4. 真实 TEG 界面数量大，直接测量所有粗糙面不可承受，因此采用接触式测量 + W-M fractal 重构。
5. 建立接触对微尺度模型，计算 loading pressure、temperature、clearance medium 对 TCR/ECR 的影响，并用间接实验验证。
6. 将微尺度接触效应等效为界面层，嵌入整机 TEG 热电力模型。
7. 在车辆典型气动条件下评价电压、功率、转换效率和 Mises 应力。
8. 用 TEG 实验平台验证整机电压输出，证明模型可用于 contact-aware TEG 评价。

这条链的核心是“从微界面到整机”。如果没有等效界面层，微尺度接触模型很难进入 27 对 TE legs 的整机；如果没有实验验证，整机预测容易被质疑。因此文章用微尺度、等效层、整机、实验四层闭合。

## 8. 方法/理论/模型细拆

器件设计部分：TEG 被放在三段压缩面上，用于采集压缩面气动热。结构包括 force-bearing frame、27 对圆柱 N/P TE legs、54 对 electrodes、two substrates、PEEK insulation layer、cover plate 等。圆柱腿选择的理由是避免方形截面应力集中并便于制造。TE legs 串联形成电路，温差和电压由气动热通过 TE legs 自然形成。

粗糙面重构部分：由于界面数量巨大，作者用接触式测量获得 TE legs 和 electrodes 的表面形貌特征，并用 W-M fractal function 重构具有自相似/自仿射特征的粗糙面。W-M 的作用是降低全量表面实测成本，同时保留统计形貌。

接触模型部分：在微尺度接触对中分析弹塑性接触、真实接触面积、clearance medium、热传导/辐射和电传导。TCR 由固体真实接触传导、间隙介质传导和辐射共同影响；ECR 主要由真实接触面积和介质导电性决定。加载压力提高会增大真实接触面积，从而降低 TCR/ECR；银环氧胶作为 high-thermal/electrical conductivity medium 可显著降低阻抗。

整机模型部分：将微尺度接触阻力用 equivalent interfacial layers 表示，嵌入 TEG 热电耦合有限元模型；再施加典型气动热/力边界，计算温度、电势、输出功率、转换效率和 Mises 应力。实验部分包括 TCR 间接测量和 TEG 电压/功率测量，用于验证模型。

## 9. 证据系统与 Claim-Evidence 表

证据系统很丰富，覆盖结构、接触、整机和实验四类。其强点是同一 claim 往往有数值和实验两类证据；弱点是一些实验偏差仍较大，如整机输出电压最大偏差 -19.69%。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 所设计 TEG 兼具 heat-harvest 与 force-bear 功能 | 摘要、Section 2、Fig. 1-3 | force-bearing frame、圆柱 TE legs、PEEK 绝缘层、实物制备流程 | 结构设计/制备 | 强 | 真实飞行振动与长期热循环未验证 |
| TCR/ECR 受压力、温度和介质显著影响 | Section 5.1、Conclusion 1 | 压力 0.8179-3.041 MPa 下 TCR/ECR 下降；silver-epoxy 显著降低阻抗 | 数值模型 | 强 | 表格数值需 PDF 复核 |
| W-M 重构和接触模型可用于多界面 TEG | Section 2.3、3.2、5.1 | 粗糙面重构、微尺度接触对网格和 TCR/ECR 计算 | 建模验证 | 中强 | W-M 统计面是否代表每个真实界面仍有不确定 |
| TCR 模型得到间接实验验证 | Section 4.1、Conclusion 2 | 间接实验最大偏差 13.4% | 实验验证 | 中强 | 偏差不小，需说明测量不确定性 |
| 整机 TEG 可在典型气动条件下输出可观电功率 | 摘要、Table 11、Conclusion 3 | 0.1 MPa、silver-epoxy、热端 700 K 下电压 6.978 V、功率 12.41 W、效率 2.334% | 数值计算 | 强 | 是否满足实际用电需求需进一步讨论 |
| 等效界面层可替代微尺度模型用于整机评价 | Section 5.2.1、Conclusion 4 | 最大模型偏差 0.444% | 模型对比 | 强 | 只在本文条件/几何下验证 |
| 实验测量验证整机评价模型 | Section 4.2/5.2.4、Conclusion 5 | 输出电压实验最大偏差 -19.69% | 实验对比 | 中 | 偏差较大，可能来自手工连接、多 TE couples 不一致等 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | TEG 在高速飞行器压缩面上的应用示意 | 选题场景具体化 | 压缩面气动热被 TEG 采集 | 需要 PDF 图像复核 |
| Fig. 2/Fig. 3/Table 1-3 | TEG 结构、材料和制备 | 器件真实制备 | 27 对圆柱腿、54 对电极、承载框架 | 需要 PDF 图像复核 |
| Fig. 4/Table 4 | 粗糙表面测量与重构 | W-M 重构可扩展到大量界面 | 接触式测量校准粗糙面 | 需要 PDF 图像复核 |
| Fig. 5-Fig. 7/Table 5-6 | 接触对和整机网格/边界 | 数值模型可信度 | 微尺度接触与整机模型连接 | 需要 PDF 图像复核 |
| Fig. 8-Fig. 9 | 实验平台 | TCR 与 TEG 输出验证 | 间接测量 TCR、测量 TEG power supply | 需要 PDF 图像复核 |
| Fig. 10-Fig. 13/Table 7-10 | 接触力学、TCR、ECR | 压力/温度/介质影响接触阻力 | silver-epoxy 显著降低阻抗 | 需要 PDF 图像复核 |
| Fig. 14 | 等效模型和微尺度模型对比 | equivalent interfacial layer 可用 | 最大偏差 0.444% | 需要 PDF 图像复核 |
| Fig. 15-Fig. 16 | 温度和 Mises 应力分布 | TEG 热力耦合可承载 | force-bearing frame 承担最大应力 | 需要 PDF 图像复核 |
| Fig. 17-Fig. 19/Table 11-12 | 电压、输出功率、效率 | 热电性能随温度/介质/压力变化 | 最大 6.978 V、12.41 W、2.334% | 表格需 PDF 复核 |
| Table 13 | 实验与数值电压对比 | 模型实验验证 | 最大电压偏差 -19.69% | 需 PDF 复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The TEG design and preparation；3 Two-scale TEG evaluation model；4 Experimental platform and models' validation；5 Results and discussions；6 Conclusion。第 2 章先展示器件结构和制备，第 3 章建立两尺度模型，第 4 章讲实验平台，第 5 章分 contact effects 和 TEG performance 两大块。

这是一种“先器件、再模型、再实验、再结果”的布局。与许多先模型后对象的论文不同，本文先让读者看到 TEG 是真实设计出来的，这有助于支撑标题中的 innovation。模型章节再解释如何处理多界面接触，结果章节先微尺度后整机，符合从局部机制到系统性能的逻辑。

标题命名偏工程对象型，例如 “The TEG with multi-interfaces”“Equivalent interfacial layers in TEG”“Thermo-mechanical performance”。标题直接暴露关键贡献：multi-interface 和 equivalent layer。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 结果/验证型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3.4 Meshed models | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5 Boundary conditions                                          and U2 are applied on surfaces P1 and P2, respectively, while surface P3 | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Power supply measurement of TEG | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5 Results and discussions | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Contact effects | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1.1 Contact mechanics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 5.1.3 The comparison with experimental results | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 5.2.2 Thermo-mechanical performance | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段先说高速飞行器气动热与 TEG 潜力；随后立即引入多界面接触效应，说明 TCR/ECR 是 TEG 真实性能的瓶颈。接着按粗糙面表征、接触变形、TE transfer/conversion、实验测量依次综述，最后给出本文整机设计。

方法段落节奏是“实体结构 -> 粗糙面 -> 控制方程 -> 接触阻抗 -> 等效层 -> 边界条件”。这使读者先明白器件是什么，再明白为什么需要两尺度评价。实验段落插在结果之前，起到增强可信度的作用。

结果段落先讨论 contact mechanics，然后 TCR/ECR，再比较实验，最后进入整机性能。这样的顺序避免了直接报 12.41 W 而缺少机制解释。输出功率、转换效率和 Mises 应力放在后面，形成“接触模型可信 -> 整机预测可信”的叙事。

## 13. 文笔画像与语言习惯

文笔是工程器件论文风格，名词非常密集。高频词包括 aerodynamic heat harvest、thermoelectric generator、multi-interface、contact effects、thermal contact resistance、electrical contact resistance、rough surfaces、loading pressure、clearance medium、force-bearing frame、output power。

作者喜欢用 first/second/third 组织贡献，摘要中尤其明显。结果部分常用 “decrease with the increase of loading pressure and average temperature”“influenced by clearance medium”等规律句。数字 claim 较多，且常在结论中重复关键量，如 6.978 V、12.41 W、2.334%、13.4%、0.444%、-19.69%。

语气较强，题名用 innovation，摘要用 innovatively created。正文则通过大量制备和实验细节支撑这种强语气。若自己模仿，需要确保“创新”不只是模型命名，而有真实结构、实验或应用边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：teg(94)；contact(94)；thermal(88)；temperature(68)；clearance(66)；legs(63)；heat(61)；surfaces(45)；surface(44)；pressure(42)；respectively(40)；electrical(39)；silver-epoxy(39)；adhesive(37)；model(35)；equivalent(34)；tcr(33)；electrodes(32)；performance(32)；air(31)
- 高频学术名词：temperature(68)；clearance(66)；pressure(42)；model(35)；analysis(32)；performance(32)；stress(27)；simulation(24)；materials(22)；resistance(21)；deformation(20)；conditions(18)；measurement(16)；conductivity(16)；interfaces(15)；difference(15)
- 高频学术动词：shown(20)；shows(12)；evaluated(6)；validated(4)；show(3)；indicates(3)；capture(3)；simulated(2)；evaluate(2)；developed(2)；compared(1)；simulate(1)；indicate(1)；revealed(1)；demonstrated(1)
- 高频形容词：thermal(88)；experimental(52)；electrical(39)；adhesive(37)；equivalent(34)；thermoelectric(29)；interfacial(25)；real(23)；numerical(22)；aerodynamic(17)；measurement(16)；fractal(16)；heterogeneous(12)；elastic(12)；potential(9)；local(8)
- 高频副词/连接副词：respectively(40)；numerically(20)；experimentally(8)；however(6)；mainly(6)；assembly(5)；significantly(4)；tively(4)；simultaneously(3)；effectively(3)；accurately(3)；supply(3)；slightly(3)；therefore(2)；substantially(2)；generally(2)
- 高频二词短语：silver-epoxy adhesive(25)；loading pressure(24)；applied thermal(19)；thermal engineering(19)；real contact(18)；rough surfaces(18)；adhesive clearance(18)；chen applied(17)；thermal contact(16)；clearance medium(16)；contacting pairs(15)；contact resistance(14)；side temperature(13)；p-type legs(12)；equivalent interfacial(12)；teg performance(12)
- 高频三词短语：applied thermal engineering(19)；chen applied thermal(17)；silver-epoxy adhesive clearance(14)；thermal contact resistance(10)；real contact area(9)；appl therm eng(9)；heat mass transf(9)；int heat mass(8)；hot side temperature(7)；equivalent interfacial layers(7)；twenty-seven couples cylindrical(6)；couples cylindrical legs(6)

**主动、被动与句法**

- 被动语态估计次数：128
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：698
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：232
- 一般过去时线索：47
- 现在完成时线索：4
- 情态动词线索：32
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：teg(54)；thermal(52)；contact(52)；legs(33)；heat(31)；electrical(31)；temperature(30)；surface(29)
- 3.5. Boundary conditions                                          and U2 are applied on surfaces P1 and P2, respectively, while surface P3：clearance(47)；contact(42)；teg(40)；temperature(38)；thermal(36)；pressure(32)；legs(30)；heat(30)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：aerodynamic-heat-harvest TEG、multi-interface contact effect、thermal/electrical contact resistance、rough surface reconstruction、W-M function、equivalent interfacial layer、force-bearing frame、cylindrical TE legs、clearance medium。

可复用 gap 句式：`Most published reports on contact effects focused on conventional metallic materials, with fewer studies on the TCR and ECR of TE materials.` 适合材料/界面领域 gap。

可复用方法句式：`The surface topography is reconstructed based on contact-type measurement and W-M function.` 适合大量界面无法逐一测量的建模问题。

可复用结构句式：`The device is designed to possess heat-harvest and force-bear functions simultaneously.` 适合多功能结构设计。

可复用结果句式：`The TCR and ECR decrease with the increase of loading pressure and average interface temperature, and are reduced by the presence of clearance medium.` 适合接触效应规律。

可复用验证句式：`The equivalent interfacial model can be used to evaluate the performance under consideration of interfacial contact effects with a maximum model deviation of ...`

## 15. 引用策略与文献使用

引用策略分为四组。第一组是高速飞行器热管理与 TEG 应用，证明气动热采集有需求。第二组是 TCR/ECR 接触效应文献，覆盖金属接触、焊接、热界面材料和 TE 系统。第三组是粗糙面重构和接触模型，包括 W-M fractal、GW statistical、direct measurement、弹塑性接触等。第四组是团队前作，包括 2023 定量接触效应和 2022 ECR 研究，支撑本研究的模型基础。

作者对前人评价的方式是“已有基础，但对象不够真实/尺度不够大”：已有接触效应研究多是金属或少数 TE couples；已有 TEG 研究多是小温差或热源/冷源接触；本文转向多界面整机和飞行器压缩面。

自引较多但有合理性，因为本文确实延续同一团队的 TEG 接触效应模型。若投稿更偏国际广泛读者，需确保外部文献覆盖足够，避免贡献显得只是团队内迭代。

## 16. 审稿人视角风险

1. 实验偏差风险：整机电压实验最大偏差 -19.69%，需要解释误差来源，如装配误差、材料参数、界面不均匀、接线损耗。
2. 飞行环境风险：实验平台不是真实高超声速飞行环境，气动热、振动、冲击、热循环和氧化/烧蚀未完全复现。
3. 粗糙面代表性风险：W-M fractal 重构的表面是否能代表 216 个真实接触面，需要统计不确定性。
4. 接触介质可行性：silver-epoxy 在高温、高载荷、长期飞行和热循环下的稳定性需要验证。
5. 力学安全风险：Mises 应力较低并不等于疲劳、热应力和界面脱粘安全。
6. 输出功率意义风险：12.41 W 对单个 TEG 可观，但系统级供电能力、布置面积、重量和线束复杂性需评估。
7. 图表复核风险：Table 11-13、Fig. 17-19 和 TEG 结构图需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把气动热从“需要防护的损失”转为“可采集能源”，形成热管理新角度。
- 结构资产：将承载框架和热电模块合并，强调 flight vehicle integration。
- 方法资产：微尺度接触模型 + 等效界面层 + 整机模型的两尺度评价路径。
- 证据资产：压力/温度/介质三因素扫描，能把接触效应规律讲清楚。
- 图表资产：先器件爆炸图，再粗糙面，再微接触，再整机性能，视觉叙事完整。
- 写作资产：将最大电压、功率、效率、模型偏差、实验偏差集中在结论，方便读者抓贡献。

## 18. 对我写论文的启发

这篇论文最值得学习的是“从模型走向器件”。如果前期已经有某种接触模型或仿真方法，下一篇论文可以通过真实器件设计、制备和实验验证扩大贡献边界。本文就把 2023 年的 contact effects 研究推进到多界面 TEG 整机。

第二个启发是工程创新要包含功能冲突：TEG 既要导热发电，又要绝缘、承载、避免应力集中。圆柱 TE legs 和 force-bearing frame 让结构设计有具体理由，而不是随意画一个模块。

第三个启发是“等效层”是连接尺度的好工具。微观粗糙面模型无法直接用于整机每个界面时，可以先做局部模型，再提取等效属性嵌入整机。

## 19. 最终浓缩

这篇论文的核心是设计并制备一种面向高速飞行器压缩面的气动热采集 TEG，并把多异质界面的 TCR/ECR 纳入整机评价。它通过 W-M 粗糙面重构、微尺度接触模型、等效界面层、TEG 热电力模型和实验验证，证明压力、温度和介质显著影响接触阻抗，silver-epoxy 条件下整机可达到 6.978 V、12.41 W 和 2.334% 转换效率。最值得学习的是“真实器件 + 接触机制 + 整机验证”的论证链；最需要复核的是实验偏差、表格数值、TEG 图像细节和飞行环境可实现性。
