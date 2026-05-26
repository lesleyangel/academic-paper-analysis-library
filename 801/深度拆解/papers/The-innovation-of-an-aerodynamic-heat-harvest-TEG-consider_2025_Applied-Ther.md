# The innovation of an aerodynamic-heat-harvest TEG considering multi-interface contact effect for a high-speed flight vehicle

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.txt` 的全文抽取，并参考 `801/文本/metadata/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.json` 的目录与元数据。txt 存在双栏串栏，尤其是 Introduction 首页、Table 11-13、Conclusion 与 References 附近，正文和表格/参考文献混排明显。涉及 TEG 爆炸图、粗糙表面重构、微尺度接触云图、Mises 应力云图、电压/输出功率曲线和实验平台照片处均标注“需要 PDF 图像复核”。主体以中文分析为主，只短引 TEG、TCR、ECR、silver-epoxy adhesive、force-bearing frame 等关键词。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The TEG design and preparation, 3 Two-scale TEG evaluation model, 4 Experimental platform and models’ validation, 5 Results and discussions, 6 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-innovation-of-an-aerodynamic-heat-harvest-TEG-consider_2025_Applied-Ther.md`。

中文译文：

> 高速飞行器在长时间飞行中会产生大量的气动热量，因此基于热电（TE）转换的气动热量收集是最有前途的热管理技术之一。在这项工作中，充分考虑多种异质界面效应，创新地创建和评估了热收集热电发电机（TEG）。首先，设计并制作了一个由受力框架、27对圆柱形TE腿、54对电极、两个基板、绝缘层和两种异质界面组成的TEG，使其同时具有吸热和受力功能。其次，基于接触式测量和W-M函数重建了TE腿和电极的表面形貌，通过间接实验测量建立并验证了热电阻和电接触电阻的数值模型，并阐明了压力、温度和间隙介质的影响。
>
> 再次，考虑微尺度接触电阻，分析了发电机的TE传递和转换过程；对车辆典型气动条件下的TE和机械性能进行了数值和实验评估，得出TEG的最大电压和输出功率分别为6.978 V和12.41 W。 TEG主要由几对通过电极串联的TE腿（N型和P型）组成，然而，TE腿和电极之间的多个界面处的不完美接触导致热和电流的收缩效应。这种接触效应表现为热接触电阻（TCR）和电接触电阻（ECR），并显着影响TE转移和转换过程[20,21]。刘等人。 [22]研究了轴承内圈与轴颈之间的TCR，发现过盈配合降低了TCR，因为过盈配合减少了界面接触面积。万等人。 [23]研究了铝对镀锌钢电阻点焊过程中的ECR和TCR，并探讨了界面处机械接触压力和温度对电阻值的强烈影响。任等人。
>
> [24]发现导热垫的弹性模量在两个固体之间的传热中充当间隙介质，影响粗糙接触界面的真实接触面积，从而进一步影响TCR，同时也表明TCR受到材料特性的影响。可见，界面温度、压力、间隙介质和材料性能是影响TCR的常见因素，本文对此进行了考虑。然而，大多数已发表的关于接触效应的报告都集中在传统金属上
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles. * Corresponding author.
- 已有研究不足/GAP：The TEG mainly consists of several couples of TE legs (Nand P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows. However, most published reports on contact effects focused on conventional metallic High-speed flight vehicles experience harsh aerodynamic heating process, and the long-duration high-speed flight brings about severe heat accumulation [1,2]. Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
- 本文解决方式：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified. Secondly, the surface topography of TE legs and electrodes are reconstructed based on th In this work, an aerodynamic-heat-harvest TEG is innovatively developed and evaluated based on the full consideration of the multi- S.-Y. The surface topography of TE legs and electrodes are reconstructed based on the contacttype measurement and W-M function, numerical models of thermal and electrical contact resistances are established and experimentally validated, and the influences of pressure, temperature and clearance medium are clarified.
- 学术或工程增量：Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The TEG design and preparation（对象/模块/过渡章节）
  - L3 p.3: 2.1 The TEG with multi-interfaces（对象/模块/过渡章节）
  - L3 p.4: 2.2 Fabrication and assembly of TEGs（对象/模块/过渡章节）
  - L3 p.5: 2.3 Rough surfaces measurement and reconstruction（对象/模块/过渡章节）
- L2 p.6: 3 Two-scale TEG evaluation model（方法/模型/算法）
  - L3 p.6: 3.1 Governing equations（对象/模块/过渡章节）
  - L3 p.7: 3.2 Calculation method of TCR and ECR（方法/模型/算法）
  - L3 p.8: 3.3 Equivalent interfacial layers in TEG（对象/模块/过渡章节）
  - L3 p.9: 3.4 Meshed models（方法/模型/算法）
  - L3 p.10: 3.5 Boundary conditions（对象/模块/过渡章节）
- L2 p.10: 4 Experimental platform and models’ validation（方法/模型/算法）
  - L3 p.10: 4.1 TCR measurements under different pressure and temperature（对象/模块/过渡章节）
  - L3 p.11: 4.2 Power supply measurement of TEG（对象/模块/过渡章节）
- L2 p.11: 5 Results and discussions（结果/验证/讨论）
  - L3 p.11: 5.1 Contact effects（对象/模块/过渡章节）
    - L4 p.11: 5.1.1 Contact mechanics（对象/模块/过渡章节）
    - L4 p.11: 5.1.2 Thermal and electrical contact resistances（对象/模块/过渡章节）
    - L4 p.12: 5.1.3 The comparison with experimental results（结果/验证/讨论）
  - L3 p.13: 5.2 TEG performance（对象/模块/过渡章节）
    - L4 p.13: 5.2.1 Validation of the equivalent interfacial layers（结果/验证/讨论）
    - L4 p.13: 5.2.2 Thermo-mechanical performance（对象/模块/过渡章节）
    - L4 p.14: 5.2.3 TEG performance（对象/模块/过渡章节）
    - L4 p.14: 5.2.4 The comparison with experimental results（结果/验证/讨论）
- L2 p.14: 6 Conclusion（结论/贡献回收）
- L2 p.17: CRediT authorship contribution statement（尾部材料）
- L2 p.17: Declaration of competing interest（尾部材料）
- L2 p.17: Acknowledgements（尾部材料）
- L2 p.17: datalink4（对象/模块/过渡章节）
- L2 p.17: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The TEG design and preparation | 3 | 2 | 对象/模块/过渡章节 |
| 2.1 The TEG with multi-interfaces | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Fabrication and assembly of TEGs | 4 | 3 | 对象/模块/过渡章节 |
| 2.3 Rough surfaces measurement and reconstruction | 5 | 3 | 对象/模块/过渡章节 |
| 3 Two-scale TEG evaluation model | 6 | 2 | 方法/模型/算法 |
| 3.1 Governing equations | 6 | 3 | 对象/模块/过渡章节 |
| 3.2 Calculation method of TCR and ECR | 7 | 3 | 方法/模型/算法 |
| 3.3 Equivalent interfacial layers in TEG | 8 | 3 | 对象/模块/过渡章节 |
| 3.4 Meshed models | 9 | 3 | 方法/模型/算法 |
| 3.5 Boundary conditions | 10 | 3 | 对象/模块/过渡章节 |
| 4 Experimental platform and models’ validation | 10 | 2 | 方法/模型/算法 |
| 4.1 TCR measurements under different pressure and temperature | 10 | 3 | 对象/模块/过渡章节 |
| 4.2 Power supply measurement of TEG | 11 | 3 | 对象/模块/过渡章节 |
| 5 Results and discussions | 11 | 2 | 结果/验证/讨论 |
| 5.1 Contact effects | 11 | 3 | 对象/模块/过渡章节 |
| 5.1.1 Contact mechanics | 11 | 4 | 对象/模块/过渡章节 |
| 5.1.2 Thermal and electrical contact resistances | 11 | 4 | 对象/模块/过渡章节 |
| 5.1.3 The comparison with experimental results | 12 | 4 | 结果/验证/讨论 |
| 5.2 TEG performance | 13 | 3 | 对象/模块/过渡章节 |
| 5.2.1 Validation of the equivalent interfacial layers | 13 | 4 | 结果/验证/讨论 |
| 5.2.2 Thermo-mechanical performance | 13 | 4 | 对象/模块/过渡章节 |
| 5.2.3 TEG performance | 14 | 4 | 对象/模块/过渡章节 |
| 5.2.4 The comparison with experimental results | 14 | 4 | 结果/验证/讨论 |
| 6 Conclusion | 14 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 17 | 2 | 尾部材料 |
| Declaration of competing interest | 17 | 2 | 尾部材料 |
| Acknowledgements | 17 | 2 | 尾部材料 |
| datalink4 | 17 | 2 | 对象/模块/过渡章节 |
| References | 17 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一段先说高速飞行器气动热与 TEG 潜力；随后立即引入多界面接触效应，说明 TCR/ECR 是 TEG 真实性能的瓶颈。接着按粗糙面表征、接触变形、TE transfer/conversion、实验测量依次综述，最后给出本文整机设计。

方法段落节奏是“实体结构 -> 粗糙面 -> 控制方程 -> 接触阻抗 -> 等效层 -> 边界条件”。这使读者先明白器件是什么，再明白为什么需要两尺度评价。实验段落插在结果之前，起到增强可信度的作用。

结果段落先讨论 contact mechanics，然后 TCR/ECR，再比较实验，最后进入整机性能。这样的顺序避免了直接报 12.41 W 而缺少机制解释。输出功率、转换效率和 Mises 应力放在后面，形成“接触模型可信 -> 整机预测可信”的叙事。

## 13. 文笔画像与语言习惯

文笔是工程器件论文风格，名词非常密集。高频词包括 aerodynamic heat harvest、thermoelectric generator、multi-interface、contact effects、thermal contact resistance、electrical contact resistance、rough surfaces、loading pressure、clearance medium、force-bearing frame、output power。

作者喜欢用 first/second/third 组织贡献，摘要中尤其明显。结果部分常用 “decrease with the increase of loading pressure and average temperature”“influenced by clearance medium”等规律句。数字 claim 较多，且常在结论中重复关键量，如 6.978 V、12.41 W、2.334%、13.4%、0.444%、-19.69%。

语气较强，题名用 innovation，摘要用 innovatively created。正文则通过大量制备和实验细节支撑这种强语气。若自己模仿，需要确保“创新”不只是模型命名，而有真实结构、实验或应用边界。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：34204
- 高频词：contact(52)；clearance(52)；temperature(47)；teg(46)；legs(41)；heat(38)；thermal(33)；adhesive(31)；tcr(29)；silver-epoxy(28)；electrical(27)；pressure(26)；electrodes(24)；surface(23)；equivalent(23)；medium(21)；ecr(21)；surfaces(20)；electrode(19)；performance(18)
- 高频名词化/学术名词：clearance(52)；temperature(47)；pressure(26)；performance(18)；conductivity(15)；difference(14)；measurement(12)；conversion(11)；deformation(11)；deviation(11)；function(10)；radiation(9)；conduction(8)；resistance(7)；simulation(7)
- 高频学术动词：evaluated(6)；validated(5)；construct(2)；developed(2)；constructed(2)；evaluate(2)；analyzed(1)；revealed(1)；demonstrated(1)；provided(1)；provide(1)；compared(1)
- 高频形容词：thermal(33)；adhesive(31)；electrical(27)；equivalent(23)；interfacial(15)；real(14)；aerodynamic(13)；experimental(13)；measurement(12)；fractal(11)；potential(8)；thermoelectric(6)；coefficient(6)；different(6)；heterogeneous(5)
- 高频副词：numerically(6)；experimentally(4)；effectively(4)；accurately(3)；mainly(2)；directly(2)；indirectly(2)；highly(2)；relatively(2)；innovatively(2)；simultaneously(2)；significantly(2)；totally(2)；commonly(2)；supply(2)
- 高频二词短语：silver-epoxy adhesive(28)；clearance medium(19)；adhesive clearance(18)；loading pressure(14)；contact effects(11)；side temperature(11)；surface topography(10)；real contact(10)；heat flux(10)；rough surfaces(9)；equivalent thermal(9)；force-bearing frame(8)
- 高频三词短语：silver-epoxy adhesive clearance(17)；pressure clearance medium(7)；hot side temperature(7)；loading pressure clearance(6)；real contact area(5)；real contact elements(5)；equivalent interfacial layers(5)；clearance silver-epoxy adhesive(5)；substrates insulation layer(4)；typical aerodynamic conditions(4)；voltage output power(4)；cold side temperature(4)
- 被动语态估计：93；`we + 动作动词` 主动句估计：0
- 一般现在时线索：164；一般过去时线索：194；现在完成时线索：1；情态动词线索：25

分章节正文词频：

- 1 Introduction: contact(20)；teg(18)；temperature(18)；tcr(16)；heat(14)；thermal(13)；surface(10)；side(10)
- 2 The TEG design and preparation: legs(18)；electrode(12)；electrodes(10)；electrical(10)；surfaces(10)；heat(9)；adhesive(8)；conductivity(8)
- 3 Two-scale TEG evaluation model: contact(15)；thermal(13)；elements(13)；equivalent(11)；clearance(10)；nodes(8)；teg(7)；ijkl(7)
- 4 Experimental platform and models’ validation: temperature(7)；heat(6)；voltage(4)；channels(4)；data(3)；acquisition(3)；measurement(3)；stainless-steel(3)
- 5 Results and discussions: clearance(23)；silver-epoxy(13)；adhesive(13)；pressure(8)；temperature(8)；air(7)；legs(7)；measured(7)
- 6 Conclusion: clearance(10)；teg(8)；pressure(7)；adhesive(6)；loading(5)；medium(5)；voltage(5)；temperature(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：aerodynamic-heat-harvest TEG、multi-interface contact effect、thermal/electrical contact resistance、rough surface reconstruction、W-M function、equivalent interfacial layer、force-bearing frame、cylindrical TE legs、clearance medium。

可复用 gap 句式：`Most published reports on contact effects focused on conventional metallic materials, with fewer studies on the TCR and ECR of TE materials.` 适合材料/界面领域 gap。

可复用方法句式：`The surface topography is reconstructed based on contact-type measurement and W-M function.` 适合大量界面无法逐一测量的建模问题。

可复用结构句式：`The device is designed to possess heat-harvest and force-bear functions simultaneously.` 适合多功能结构设计。

可复用结果句式：`The TCR and ECR decrease with the increase of loading pressure and average interface temperature, and are reduced by the presence of clearance medium.` 适合接触效应规律。

可复用验证句式：`The equivalent interfacial model can be used to evaluate the performance under consideration of interfacial contact effects with a maximum model deviation of ...`

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Thus, a highly stable TEG performance over a relatively large temperature range is essential for high-speed flight vehicles. * Corresponding author.
  可迁移模板：Thus, a highly stable METHOD performance over a relatively large temperature range is essential for high-speed flight vehicles. * Corresponding author.
- 原句：Wang et al. [36] found that the study of TCR requires the use of elastoplastic deformation model.
  可迁移模板：Wang et al. [X] found that the study of METHOD requires the use of elastoplastic deformation model.
#### Gap/转折句
- 原句：The TEG mainly consists of several couples of TE legs (Nand P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows.
  可迁移模板：The METHOD mainly consists of several couples of METHOD legs (Nand P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between METHOD legs and electrodes lead to a shrinkage effect of the heat and electrical flows.
- 原句：However, most published reports on contact effects focused on conventional metallic High-speed flight vehicles experience harsh aerodynamic heating process, and the long-duration high-speed flight brings about severe heat accumulation [1,2].
  可迁移模板：However, most published reports on contact effects focused on conventional metallic High-speed flight vehicles experience harsh aerodynamic heating process, and the long-duration high-speed flight brings about severe heat accumulation [X,X].
- 原句：Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
  可迁移模板：Traditional thermal protection system (METHOD) is mainly based on the thermal-proof coatings with high radiation emissivity [X] and thermal-insulation structures with low conduction ability [X], leading to very limited heat capacity and thermal protection efficiency.
- 原句：The TEG mainly consists of several couples of TE legs (Nand P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between TE legs and electrodes lead to a shrinkage effect of the heat and electrical flows.
  可迁移模板：The METHOD mainly consists of several couples of METHOD legs (Nand P-type) which are connected in series by electrodes, however, the imperfect contact at the multiple interfaces between METHOD legs and electrodes lead to a shrinkage effect of the heat and electrical flows.
- 原句：In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes one Nand P-type TE leg), totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured, leading to unaffordable cost.
  可迁移模板：In the authors’ previous works [X,X], an optical profiler is used to measure the real surface topography and construct METHOD and METHOD models for one or two METHOD couples, however, in this work, the METHOD consists of twenty-seven METHOD couples (one METHOD couple includes one Nand P-type METHOD leg), totally Xsurfaces of METHOD legs and Xsurfaces of electrodes need to be measured, leading to unaffordable cost.
#### 方法提出句
- 原句：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
  可迁移模板：Secondly, the surface topography of METHOD legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
- 原句：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
  可迁移模板：Secondly, the surface topography of METHOD legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
- 原句：Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [25], GW statistical models [26], Euclidean geometrical statistical models [27], semi-deterministic-based approaches [28], and direct measurement of real surface topography [29].
  可迁移模板：Various methods can be employed to reconstruct rough surfaces, including W-M fractal models [X], METHOD statistical models [X], Euclidean geometrical statistical models [X], semi-deterministic-based approaches [X], and direct measurement of real surface topography [X].
- 原句：In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes one Nand P-type TE leg), totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured, leading to unaffordable cost.
  可迁移模板：In the authors’ previous works [X,X], an optical profiler is used to measure the real surface topography and construct METHOD and METHOD models for one or two METHOD couples, however, in this work, the METHOD consists of twenty-seven METHOD couples (one METHOD couple includes one Nand P-type METHOD leg), totally Xsurfaces of METHOD legs and Xsurfaces of electrodes need to be measured, leading to unaffordable cost.
- 原句：The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, which are commonly employed for rough surface reconstructions [22,32–35].
  可迁移模板：The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, which are commonly employed for rough surface reconstructions [X,X–X].
#### 结果呈现句
- 原句：Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is affected by the material properties.
  可迁移模板：Ren et al. [X] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the METHOD, and also showed that the METHOD is affected by the material properties.
- 原句：Ren et al. [24] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the TCR, and also showed that the TCR is affected by the material properties.
  可迁移模板：Ren et al. [X] found that the elastic modulus of a thermal pad acts like a clearance medium in the heat transfer between two solids, affecting the real contact area of the rough contact interface, which further affects the METHOD, and also showed that the METHOD is affected by the material properties.
- 原句：Karthick et al. [42] empirically demonstrated that the TCR can be effectively reduced by enhancing surface smoothness, applying pressure between contacting surfaces, and using thermal interface materials (TIMs).
  可迁移模板：Karthick et al. [X] empirically demonstrated that the METHOD can be effectively reduced by enhancing surface smoothness, applying pressure between contacting surfaces, and using thermal interface materials (TIMs).
#### 贡献/增量句
- 原句：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
  可迁移模板：Secondly, the surface topography of METHOD legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
- 原句：Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively.
  可迁移模板：Thirdly, the METHOD transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the METHOD and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of METHOD are revealed to be METHOD and METHOD, respectively.
- 原句：Secondly, the surface topography of TE legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
  可迁移模板：Secondly, the surface topography of METHOD legs and electrodes are reconstructed based on the contact-type measurement and W-M function, numerical models of thermal and electrical contact resistances are established and validated by in-direct experimental measurements, and the influences of pressure, temperature and clearance medium are clarified.
- 原句：Thirdly, the TE transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the TE and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of TEG are revealed to be 6.978 V and 12.41 W, respectively.
  可迁移模板：Thirdly, the METHOD transfer and conversion processes of the generator is analyzed considering the micro-scale contact resistances; the METHOD and mechanical performances under the vehicle’s typical aerodynamic conditions are numerically and experimentally evaluated, and the maximum voltage and output power of METHOD are revealed to be METHOD and METHOD, respectively.
- 原句：Li et al. [43] found that when the TEG system was used at high heat source temperatures, large pressure loads, and with thermally conductive grease as the interfacing material, it provided better performance at relatively low TCR and ECR.
  可迁移模板：Li et al. [X] found that when the METHOD system was used at high heat source temperatures, large pressure loads, and with thermally conductive grease as the interfacing material, it provided better performance at relatively low METHOD and METHOD.
#### 限制/边界句
- 原句：Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
  可迁移模板：Traditional thermal protection system (METHOD) is mainly based on the thermal-proof coatings with high radiation emissivity [X] and thermal-insulation structures with low conduction ability [X], leading to very limited heat capacity and thermal protection efficiency.
- 原句：The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, which are commonly employed for rough surface reconstructions [22,32–35].
  可迁移模板：The W-M fractal method can effectively capture the geometric self-similarity and self-affinity of rough surfaces, allowing similar surface topography to be observed at different magnifications, regardless of spatial scale, which are commonly employed for rough surface reconstructions [X,X–X].
- 原句：However, the experimental measurement of the TE transfer and conversion performance of the TEG is still limited.
  可迁移模板：However, the experimental measurement of the METHOD transfer and conversion performance of the METHOD is still limited.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略分为四组。第一组是高速飞行器热管理与 TEG 应用，证明气动热采集有需求。第二组是 TCR/ECR 接触效应文献，覆盖金属接触、焊接、热界面材料和 TE 系统。第三组是粗糙面重构和接触模型，包括 W-M fractal、GW statistical、direct measurement、弹塑性接触等。第四组是团队前作，包括 2023 定量接触效应和 2022 ECR 研究，支撑本研究的模型基础。

作者对前人评价的方式是“已有基础，但对象不够真实/尺度不够大”：已有接触效应研究多是金属或少数 TE couples；已有 TEG 研究多是小温差或热源/冷源接触；本文转向多界面整机和飞行器压缩面。

自引较多但有合理性，因为本文确实延续同一团队的 TEG 接触效应模型。若投稿更偏国际广泛读者，需确保外部文献覆盖足够，避免贡献显得只是团队内迭代。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：77
- Introduction 引文簇数量估计：18
- References 条目数：53
- 可识别年份条目数：50
- 2021 年及以后文献数：25
- 2010 年前经典文献数：5
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Applied Thermal Engineering(2)
- 引文簇样例：[1,2], [20,21], [22], [3], [4], [23], [24], [41], [42], [25], [26], [43]

带引文的 gap/转折句样例：

- Traditional thermal protection system (TPS) is mainly based on the thermal-proof coatings with high radiation emissivity [3] and thermal-insulation structures with low conduction ability [4], leading to very limited heat capacity and thermal protection efficiency.
- In the authors’ previous works [30,31], an optical profiler is used to measure the real surface topography and construct TCR and ECR models for one or two TE couples, however, in this work, the TEG consists of twenty-seven TE couples (one TE couple includes one N- and P-type TE leg), totally 108 surfaces of TE legs and 108 surfaces of electrodes need to be measured, leading to unaffordable cost.

References 解析样例（前 8 条）：

- 1. The TCR and ECR decrease with the increase of loading pressure and average temperature of the interfaces, and they are reduced by the presence of clearance medium. When the loading pressure varies from 0.8179 to 3.041 MPa, the TCR decreases from 12.63 × 10−4 to 2.920 × 10−4, 6.571 × 10−4 to 2.106 × 10−4 and 3.377 × 10−5 to 2.485 × 10−5 (K⋅m2)/W under vacuum, air and silver-epoxy adhesive clearance, respectively; the ECR varies from 17.20 × 10−8 to 4.348 × 10−8, 8.151 × 10−10 to 6.919 × 10−10 Ω⋅m2 under air/ vacuum and silver-epoxy adhesive clearance, respectively.
- 2. The TCR model is validated by indirect experimental measurements with the maximum deviation of 13.4 %.
- 3. The fabricated TEG has the ability to capture aerodynamic heat to generate power with the maximum voltage, output power and conversion efficiency are 6.978 V, 12.41 W and 2.334 %, respectively (at 0.1 MPa and under the silver-epoxy adhesive clearance).
- 4. The equivalent interfacial model can be used to evaluate the performance of the TEG under consideration of interfacial contact effects with a maximum model deviation of 0.444 %. The thermoelectric and mechanical performance are influenced by the loading pressure and the clearance medium, and the force-bearing frame has the highest Mises stress of 7.88 MPa under the silverepoxy adhesive clearance and 7.68 MPa under air clearance.
- 5. Experimental measurements validated the TEG evaluation model with a maximum deviation in output voltage of −19.69 %.
CRediT authorship contribution statement
Shi-Yuan Chen: Conceptualization, Data curation, Methodology, Software, Writing – original draft, Writing – review & editing. Hai-Peng Chen: Data curation, Validation. Ge Gao: Software, Data curation. Chun-Lin Gong: Conceptualization, Project administration, Supervision. Yang Wu: Investigation, Validation. Jian-Jun Gou: Conceptualization, Funding acquisition, Project administration, Writing – review & editing.
S.-Y. Chen et al. Applied Thermal Engineering 258 (2025) 124687
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
Acknowledgements
This study is supported by the National Natural Science Foundation of China (52232014, 51806175).
Data availability
Data will be made available on request.
References
- [1] X.F. Ma, P.X. Jiang, Y.H. Zhu, Dynamic simulation and analysis of transient characteristics of a thermal-to-electrical conversion system based on supercritical CO2 Brayton cycle in hypersonic vehicles, Appl. Energy 359 (2024).
- [2] J.J. Gou, Z.W. Yan, J.X. Hu, G. Gao, C.L. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021).
- [3] W.Z. Yang, X.Y. Zhang, Y. Cui, Z.T. Chen, Thermal and fracture analysis of collinear interface cracks in graded coating systems under ramp-type heating, Int. J. Heat Mass Transf. 216 (2023).
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

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
