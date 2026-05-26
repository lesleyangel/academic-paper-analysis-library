# The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.txt` 的全文抽取，并参考 `801/文本/metadata/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 中的题名、期刊、目录与页数信息。该文长达 30 页，txt 抽取在公式、附录、表格和参考文献处存在明显双栏串行，尤其 Fig. 21-Fig. 24、Table 7、Appendix A-E 附近。本文依据可读文本做深度拆解，涉及温度云图、粗糙面拓扑图、TCR/ECR 曲线、输出功率公式和实验平台图像的细节均标注“需要 PDF 图像复核”。主体为中文分析，只保留 TCR、ECR、real-topology-based simulation、indirect test、equivalent layers 等关键词。

## 1. 基本信息与论文身份

- 题名：The quantitative study of interfacial contact effects in TEGs by real-topology-based simulations and novel indirect tests。
- 作者：Ge Gao, Dou Li, Jian-Jun Gou, Chun-Lin Gong, Shuang-Ming Li。
- 期刊与年份：International Journal of Heat and Mass Transfer, 201, 2023, Article 123579。
- DOI：10.1016/j.ijheatmasstransfer.2022.123579。
- 关键词：Quantitative study；Contact effects；Thermoelectric generators；Real-topology-based simulation；Indirect test。
- 论文类型：热电发电器界面热/电接触效应的定量建模、实验测量与简化公式论文。
- 研究对象：用于高超声速气动热采集潜力的 TEG 中，TE legs 与 electrodes 之间的热接触阻抗 TCR 和电接触阻抗 ECR。
- 核心方法：基于真实粗糙表面拓扑的接触对数值预测；考虑热传导、热辐射、弹塑性接触、电传导；新型间接 TCR 实验；ECR 与 TEG 输出实验；等效界面层模拟 TEG 热电转换；最大输出功率预测公式。
- 主要证据：不同温度、压力、gap medium 和 thermal radiation 下 TCR/ECR；TCR 间接测试平台与数值验证；TEG 电源输出实验；公式与数值最大偏差 7.7%；实验/数值电压最大差异 8.73%。
- 目标读者：热电器件、界面传热、电接触、粗糙面接触建模和高超声速热能采集研究者。

这篇论文是 Batch 7 中接触效应系列的基础方法论文。2025 年 TEG 论文把接触模型用于多界面真实器件，而本文更像“把 TCR/ECR 影响 TEG 输出的机制、测量和简化预测公式定量打通”。

## 2. 摘要与核心信息提取

一句话主张：TEG 中 TE legs 与 electrodes 的异质粗糙界面会产生显著 TCR/ECR，进而削弱热传递、电流流动和最大输出功率；本文用真实拓扑数值模拟和新型间接实验定量描述这些接触效应，并提出可预测最大输出功率的简化公式。

摘要按四步推进。第一步，预测不同 temperature、pressure、gap medium、thermal radiation 条件下的 TCR/ECR。第二步，开发依赖 TE conversion characteristics 的 novel indirect TCR test approach，并建立实验平台验证数值模型。第三步，用 equivalent layers 将接触效应纳入 TEG 热电转换模拟，并通过 TEG 输出功率实验验证。第四步，推导两个考虑接触效应的最大输出功率预测公式，公式与数值结果最大偏差 7.7%。

核心信息是“接触效应被从局部界面阻抗转化为整机输出功率预测”。文章没有停在“接触阻抗随压力变化”这一层，而是进一步问：这些 TCR/ECR 如何降低 TEG 的电压和功率？能不能用简化公式在设计阶段快速估算？

## 3. 选题层深拆

选题来源是高超声速飞行器热管理中的 TEG 可靠设计需求。TEG 可能将气动热转化为电能，但真实 TEG 包含多个 TE leg-electrode 界面，TE 材料和电极表面均为微尺度粗糙面，真实接触面积有限，大量接触间隙造成 heat flow 和 electric current constriction。这种 constriction 直接表现为 TCR/ECR，最终削弱输出功率。

作者把大问题收束为“定量描述异质界面接触效应”。这不是泛泛地说“接触不好会影响性能”，而是要在不同温度、压力、介质和辐射条件下预测 TCR/ECR，建立可测平台验证，并将其映射到最大输出功率公式。

选题价值有三层。物理层面，它把粗糙面真实接触、热辐射、热传导、电导通和 TE 转换连接起来。方法层面，它解决 TE 材料脆、难以打孔直接测 TCR 的测量难题，提出利用 Seebeck 特性的间接测试。工程层面，它给 TEG 设计提供接触效应快速估算公式，而不是每次都做微尺度数值模型。

这类选题非常适合 International Journal of Heat and Mass Transfer，因为它的核心是界面传热/传质/电传导与器件性能的定量关系。

## 4. 领域位置与文献版图

Introduction 首先从高超声速飞行器热积累和 TPS 重量问题引出 TE conversion。随后详细说明 TEG 的四个关键界面：N 型腿与电极热/冷侧、P 型腿与电极热/冷侧。这个界面枚举很重要，直接说明 TCR/ECR 不是单一界面小修正，而是每个 TE couple 的多界面系统问题。

文献版图分成 TCR 预测、TCR 测量、ECR 预测/测量、TCR/ECR 对 TEG 的影响几类。TCR 预测部分强调粗糙面表征、接触变形和传热分析；已有方法包括统计参数、semi-deterministic 和 measured real topology。作者指出许多材料是 Ti alloy、C/SiC 等，TE materials 研究有限。TCR 测量方面，steady-state 方法用于 bulk materials，但 TE leg-electrode 界面难以直接测量，因为 TE 材料脆、不易打孔测温。

ECR 文献则强调已有数值模型较少基于真实粗糙表面拓扑，实验方法对简单对象也可能复杂。TEG 性能影响文献承认已有理论/数值研究，但接触效应的定量公式和可验证间接测试仍不足。

本文站位：用 real-topology-based simulation 提升接触预测真实性，用 indirect tests 解决测量难题，用 formulas 连接界面效应和整机最大功率。

## 5. Gap 制造机制

文章制造 gap 的方式非常扎实。第一是材料/对象 gap：已有 TCR/ECR 研究多关注常规材料、TEG 与热/冷源界面，而不是 TE legs 与 electrodes 的异质界面。第二是测量 gap：直接测 TE leg-electrode TCR 困难，尤其 TE 材料脆、样品尺寸小、界面内部温度难以布点。第三是模型 gap：ECR/TCR 模型若不基于真实粗糙面拓扑，难以准确表示真实接触面积和间隙。第四是设计 gap：现有工作缺少把 TCR/ECR 快速映射到 TEG 最大输出功率的简化公式。

这个 gap 的可信度很强，因为作者在 Introduction 中逐条说明了为什么传统方法不足，并在后文逐条回应：真实拓扑重构回应模型 gap，Seebeck 间接测量回应实验 gap，等效层和功率公式回应设计 gap。

可被追问的是：真实拓扑测量本身来自有限样本，是否能代表批量 TE legs/electrodes；间接测试依赖若干热电参数和模型近似，误差传播如何控制；公式适用范围较窄，能否推广到其他尺寸和材料。

## 6. 创新性判断

作者声明的创新包括：基于重构真实粗糙表面预测 TCR/ECR；提出利用 TE 转换特性的间接 TCR 测试方法和平台；将接触效应用 equivalent layers 纳入 TEG 热电转换模拟；建立两个最大输出功率预测公式，并验证其最大偏差为 7.7%。

真实创新属于“实验方法 + 多尺度定量桥接 + 简化公式”。其中最强的是 indirect TCR test approach：它利用 TE 材料的 Seebeck 效应，通过电势/温差关系反推出界面热阻，绕开直接测界面温度的困难。第二个强点是把 TCR/ECR 分别和共同作用下的 TEG 最大功率降低建立公式，使研究不只是现象报告。

创新强度：强。虽然接触热阻和电接触阻抗本身是经典问题，但对象、实验方法和公式桥接使本文有较明确的方法贡献。它比 2025 TEG 论文更偏基础定量方法。

创新边界也很清楚：公式适用范围在 loading pressure 0.104-0.187 MPa、temperature 323-523 K、roughness 3.55-32.53 μm、vacuum/air/silver-epoxy gap medium 内，作者在结论中明确写出，这有助于控制外推风险。

## 7. 论证链条复原

全文论证链如下：

1. 高超声速飞行器热电采集需要可靠 TEG，而 TEG 的 TE leg-electrode 粗糙界面会产生 TCR/ECR。
2. TCR/ECR 由真实接触面积、间隙介质、压力、温度和热辐射共同决定，传统简化模型不够。
3. 基于真实拓扑重构的数值模型可更准确预测 contact mechanics、heat transfer 和 electric conduction。
4. TE leg-electrode TCR 难以直接测量，可利用 Seebeck 转换特性设计间接测试平台，并同步测 ECR 和输出功率。
5. 数值模型在不同压力/温度下与实验结果相对吻合，说明 TCR/ECR 预测可信。
6. 将 TCR/ECR 用 equivalent layers 表示，嵌入 TEG 热电模型，可量化接触效应对电压、温差、内阻和最大输出功率的影响。
7. TCR 与 ECR 单独/共同影响可被解耦近似，进而推导最大输出功率预测公式。
8. 公式与数值最大偏差 7.7%，实验电压最大差异 8.73%，证明方法可用于设计估算。

这条链的关键是从界面参数到整机输出的闭合。很多界面论文只到 TCR/ECR 曲线，本文继续走到 TEG 最大输出功率，这让接触效应对工程设计的意义变得可量化。

## 8. 方法/理论/模型细拆

研究对象为用于飞行器背风区域的 TEG，工作温度约 600-800 K 背景来自前期飞行器描述。样品包括 alumina ceramic substrates、N/P TE legs、copper electrodes 和 PEEK shell。TEG 有四类关键界面，界面粗糙导致真实接触区域有限，vacuum/air gap 下热量通过真实接触固体传导和间隙热辐射传递，电流只能通过真实接触区域；silver-epoxy adhesive gap 下，热流和电流还可通过介质传递。

数值模型包括接触力学、热传导、电传导和 TE 耦合。接触力学考虑弹性/塑性阶段，求真实接触面积和间隙距离；TCR 计算考虑 solid conduction、gap/radiation；ECR 计算考虑电流收缩和真实接触路径；TEG 整机中用 equivalent layers 表示接触阻力。

实验方法的创新点在 TCR 间接测量。基本思路是：设置加载压力和热源温度，待稳态后由不锈钢块温度梯度计算热流，通过电极测得 TE leg 电势差，再结合 TE leg 电阻和 ECR，利用 TE 转换特性推算热端/冷端界面 TCR。平台还可调整用于 ECR 和 TEG power generation 测量。

公式方法将最大输出功率写成电势差和内阻的函数，再引入 TCR 导致的温差变化、ECR 导致的内阻增加，以及二者耦合影响。作者比较 decoupling prediction 与更保守的乘积预测，指出 silver-epoxy gap 下预测精度高，vacuum/air 下公式趋于保守。

## 9. 证据系统与 Claim-Evidence 表

证据系统覆盖数值趋势、实验验证、公式验证和不确定性附录。结论中列出 7 条，基本对应全文 claim。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 基于真实粗糙拓扑的模型可预测不同温度/压力/介质下 TCR | Conclusion 1、Fig. 8-15 | 重构 TE legs/electrodes 粗糙面，计算热传导和辐射 | 数值模型 | 强 | 拓扑样本代表性需复核 |
| thermal radiation 对 TCR 的影响随界面平均温度升高而增强 | Conclusion 2、Fig. 11-13 | vacuum/air gap 下辐射贡献随温度增大；vacuum 主要受 TE 材料导热影响，air 下 TCR 随温度升高下降 | 数值分析 | 中强 | 近场辐射被简化，附录说明多数间隙 >5 μm |
| 加载压力增加会降低 TCR，且趋势放缓 | Conclusion 3、Fig. 14-15 | pressure 增大真实接触面积，TCR 下降；air gap 约为 vacuum 的一半，silver-epoxy 约为 vacuum 的千分之一 | 数值曲线 | 强 | 具体数量需 PDF 图像复核 |
| 间接 TCR 测试平台可获得合理实验结果 | Conclusion 4、Fig. 5-7/Table 4-6 | 实验与数值最大差异 -27.51%，平台也可测 ECR 和 TEG power supply | 实验验证 | 中 | -27.51% 偏差较大 |
| ECR 对 TEG 的负面影响在 vacuum/air 下高于 TCR | Conclusion 5、Fig. 22-24 | vacuum/air 下 ECR 降低电场/输出更显著；silver-epoxy 下 TCR 略高于 ECR | 数值比较 | 强 | 依赖特定材料和界面 |
| contact effects 在 silver-epoxy gap 下导致性能退化不超过 4%，air gap 下超过 96% | Conclusion 5、Fig. 24 | 相比 perfect contact，air/vacuum 下最大输出功率降低约 96.3-97.8%，silver-epoxy 降低约 2.6-3.8% | 整机模拟 | 强 | silver-epoxy 高温可靠性未完全验证 |
| 最大输出功率预测公式最大偏差 7.7% | Abstract、Conclusion 7、Table 7 | loading pressure 0.104-0.187 MPa、temperature 323-523 K、roughness 3.55-32.53 μm 等范围内公式与数值吻合 | 公式验证 | 强 | 适用范围较窄 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | TEG 与界面接触示意 | 研究对象具体化 | 四类 TE leg-electrode 界面和 gap medium | 需要 PDF 图像复核 |
| Fig. 2 | 粗糙面重构与接触模型 | real-topology-based simulation | 真实粗糙拓扑进入接触计算 | 需要 PDF 图像复核 |
| Fig. 3-Fig. 4 | 边界条件与网格 | 模型可复现性 | 接触对和 TEG 网格设置 | 需要 PDF 图像复核 |
| Fig. 5-Fig. 6 | 间接 TCR 测试方法与平台 | 实验方法创新 | 利用 TE 转换特性反推 TCR | 需要 PDF 图像复核 |
| Fig. 7/Table 7 | ECR 与 TEG power generation 实验 | 整机输出验证 | 电压实验与数值最大差异 8.73% | 表格需 PDF 复核 |
| Fig. 8-Fig. 10 | 不同介质下温度/热流云图 | TCR 机制 | vacuum/air/silver-epoxy 热路径不同 | 需要 PDF 图像复核 |
| Fig. 11-Fig. 15 | 辐射、温度、压力对 TCR 影响 | TCR 定量规律 | TCR 随压力下降；silver-epoxy 最低 | 需要 PDF 图像复核 |
| Fig. 16-Fig. 21 | TCR 对 TEG 温差、平均温度和最大功率影响 | TCR 降低热电输出 | contact effects 改变 TE legs 温差 | 需要 PDF 图像复核 |
| Fig. 22-Fig. 24 | TCR+ECR 耦合影响与功率预测 | ECR/TCR 共同削弱输出 | air/vacuum 功率降幅巨大，公式最大偏差 7.7% | 需要 PDF 图像复核 |
| Appendix A-E | 辐射、边界、实验、不确定性 | 控制审稿风险 | 近场辐射、边界条件和测量不确定性说明 | 公式需 PDF 复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The TEG, rough surfaces and electric power generation；3 Numerical models；4 Experimental measurement；5 Results and discussions；6 Conclusion，并有 Appendix A-E。第 2 章先定义 TEG、材料、理论功率和粗糙面；第 3 章给控制方程、TCR/ECR 计算、边界条件和网格；第 4 章讲 TCR、ECR 和输出功率实验；第 5 章分 contact mechanics/heat transfer、TCR/ECR、contact effects in TEG 三大块。

结构逻辑是“对象与理论 -> 数值模型 -> 实验测量 -> 结果与公式”。比 2025 TEG 论文更基础，因为它先花大量篇幅解释 TCR/ECR 如何定义和测量，再进入整机 TEG。

附录很重要：Appendix A 处理 thermal radiation，Appendix B 给接触模型边界，Appendix C/D 给实验测量细节，Appendix E 给不确定性分析。这说明作者预判审稿人会追问辐射简化、边界条件和测量误差。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：11
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 结论/展望型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                       leads to thermal contact resistance (TCR) and electrical contact re- | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 3.1.1 Equilibrium equation                                         The source term for the energy equation (heat conduction) of | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1.2 Geometric equation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.4 Constitutive equations for plastic stage | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Boundary conditions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Meshed models | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Experimental measurement                                           for the hot- and cold side of TE leg, respectively; P is the maximum | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 5.3 The quantitative description of contact effects in TEG | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 5.3.1 Considering the impact of TCR | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.2.5 Electrical contact resistance                                  gap is close to that of the air condition, while the average temper- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 6 Conclusion                                                7 The prediction formulas for the maximum output power of the | 结论/展望型 | 收束贡献、边界和未来工作 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段从高超声速热积累和 TE-TPS 潜力进入，随后马上拆出 TEG 中至少四个关键界面，制造接触效应重要性。然后分别综述 TCR 预测、TCR 测量、ECR 预测/测量和 contact effects 对 TEG 的影响。最后一段列出本文流程，几乎就是后文目录。

方法段落节奏偏严密：先讲材料和几何，再讲理论功率公式，再讲粗糙面接触模型。公式较多，读者负担大，但每个公式都服务于后面“最大输出功率预测”。

结果段落采用从局部到整机的节奏。5.1 先讲 contact mechanics and heat transfer，5.2 讲 TCR/ECR 的影响因素和实验，5.3 讲 TEG 中 contact effects 的量化描述和公式。这个顺序合理，因为没有前两节的 TCR/ECR 定量，后面的功率公式就缺支撑。

## 13. 文笔画像与语言习惯

文笔是 IJHMT 典型的机理-模型-实验混合风格。高频词包括 precise quantitative description、heterogeneous interfaces、real-topology-based predictions、novel indirect tests、thermal radiation、loading pressure、gap medium、maximum output power。

作者喜欢用 “First/Second/Third/Finally” 串联贡献，用 “it should be noted that” 处理假设和边界，用 “in good agreement” 描述模型验证。结果描述非常数字化，结论中保留适用范围和最大偏差，显示作者重视定量可信度。

语气总体谨慎。即使 claim 较强，也会给出最大差异、适用范围和保守性说明。例如 decoupling method 在 vacuum/air 下趋于 conservative，这比单纯说公式准确更有工程可信度。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：tcr(193)；temperature(179)；contact(158)；teg(145)；gap(144)；leg(133)；heat(131)；thermal(117)；type(107)；about(100)；ecr(90)；legs(84)；electrodes(84)；resistance(73)；air(72)；respectively(72)；side(71)；loading(71)；power(69)；electrode(65)
- 高频学术名词：temperature(179)；condition(78)；resistance(73)；pressure(53)；measurement(47)；interface(43)；analysis(32)；simulation(32)；radiation(32)；difference(32)；materials(31)；prediction(30)；conductivity(30)；displacement(30)；model(29)；method(28)
- 高频学术动词：shown(38)；shows(29)；compared(13)；show(12)；simulated(9)；developed(8)；predicted(7)；validated(7)；predict(6)；proposed(3)；derived(3)；indicates(2)；simulate(2)；indicate(2)；estimate(2)；estimated(1)
- 高频形容词：thermal(117)；experimental(100)；numerical(98)；electric(56)；measurement(47)；adhesive(45)；electrical(39)；potential(35)；international(31)；displacement(30)；real(28)；different(24)；thermoelectric(21)；cient(21)；elastic(20)；material(17)
- 高频副词/连接副词：respectively(72)；gradually(17)；mainly(15)；numerically(8)；supply(8)；relatively(7)；tively(7)；slightly(6)；cantly(5)；finally(3)；greatly(3)；therefore(2)；generally(2)；furthermore(2)；however(2)；ually(2)
- 高频二词短语：type leg(62)；loading pressure(44)；heat mass(38)；output power(38)；maximum output(37)；air gap(35)；cold side(34)；silver-epoxy adhesive(34)；hot side(33)；international heat(31)；mass transfer(31)；contact resistance(31)；rough surfaces(30)；gao gou(29)；gou international(29)；adhesive gap(28)
- 高频三词短语：maximum output power(32)；international heat mass(31)；heat mass transfer(31)；gao gou international(29)；gou international heat(29)；thermal contact resistance(21)；silver-epoxy adhesive gap(20)；output power teg(18)；average interface temperature(17)；seebeck coe cient(15)；perfect contact condition(15)；surface type leg(14)

**主动、被动与句法**

- 被动语态估计次数：237
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：996
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：595
- 一般过去时线索：98
- 现在完成时线索：2
- 情态动词线索：92
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：contact(8)；effects(7)；indirect(4)；thermal(4)；numerical(4)；heat(3)；quantitative(3)；tegs(3)
- 1. Introduction                                                       leads to thermal contact resistance (TCR) and electrical contact re-：type(51)；leg(47)；tcr(45)；teg(43)；ecr(37)；heat(36)；electric(35)；electrode(31)
- 3.1.1. Equilibrium equation                                         The source term for the energy equation (heat conduction) of：materials(2)；effect(2)；see(2)；potential(2)；seebeck(2)；stress(2)；electrical(2)；coe(2)
- 3.1.2. Geometric equation：contact(4)；difference(3)；strain(3)；elastic(3)；temperature(2)；calculation(2)；tcr(2)；ecr(2)
- 3.1.4. Constitutive equations for plastic stage：gap(9)；elements(9)；teg(8)；meshed(8)；nodes(8)；model(7)；respectively(7)；heat(7)
- 4. Experimental measurement                                           for the hot- and cold side of TE leg, respectively; P is the maximum：temperature(72)；tcr(62)；gap(57)；about(56)；increases(49)；leg(48)；heat(35)；average(33)
- 5.2.5. Electrical contact resistance                                  gap is close to that of the air condition, while the average temper-：teg(57)；gap(49)；temperature(44)；tcr(40)；condition(31)；maximum(31)；air(27)；about(27)
- 6. Conclusion                                                7 The prediction formulas for the maximum output power of the：contact(65)；thermal(60)；heat(40)；resistance(39)；tcr(35)；temperature(30)；measurement(25)；teg(24)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：thermal contact resistance、electrical contact resistance、real contact area、gap medium、thermal radiation、real-topology-based simulation、indirect test、equivalent layers、maximum output power、loading pressure。

可复用问题句式：`The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing TEGs.` 适合界面/器件论文开头。

可复用 gap 句式：`Few published reports are on measuring the TCR between TE legs and electrodes.` 简洁地把测量对象具体化。

可复用方法句式：`A novel indirect TCR test approach relying on the TE conversion characteristics is developed.` 适合强调测量创新。

可复用结果句式：`Compared with the perfect contact condition, the maximum output power is reduced by ...` 适合量化非理想效应。

可复用边界句式：`The prediction formulas are applicable for loading pressure from ..., temperature from ..., roughness from ..., and gap medium of ...` 适合公式论文主动限定范围。

## 15. 引用策略与文献使用

引用策略按问题链组织。作者先引用高超声速热防护和 TE-TPS 文献，说明应用动机；再引用粗糙面 TCR 模型，包括统计、真实拓扑和 diffuse interface 等；随后引用 TCR 测量方法，区分 steady-state 和 transient；再引用 ECR 预测/实验；最后引用 TCR/ECR 对 TEG 性能影响的理论与数值研究。

这种引用不是按时间线，而是按“预测-测量-器件影响”组织，正好对应本文三项贡献。每类文献都被指出一个具体不足：对象不是 TE leg-electrode、直接测量困难、ECR 模型不基于真实粗糙面、缺少简化公式。

引用中团队前作较多，如 C/C-SiC/Ti alloy 真实拓扑 TCR 模型、高超声速 TEG 多级研究等。这说明本文是已有真实拓扑方法向 TE 界面的迁移与扩展。

## 16. 审稿人视角风险

1. 间接测试误差较大：TCR 实验与数值最大差异 -27.51%，需要充分解释误差来源和不确定性。
2. 公式适用范围有限：压力、温度、粗糙度和介质范围明确，但超出范围不能外推。
3. silver-epoxy 假设风险：其在高温、热循环、长期服役中的导热/导电和粘接稳定性需验证。
4. 近场辐射简化风险：附录解释多数间隙大于 5 μm，近场影响有限，但在更光滑/更高压界面可能不同。
5. TE 参数温度依赖风险：材料 Seebeck、电导、热导和接触状态随温度变化，参数不确定会传递到公式。
6. TEG 实验尺度风险：样品尺寸和真实飞行器大面积 TEG 阵列之间仍有尺度差异。
7. 图表复核风险：Fig. 16-24 和 Table 7 是关键功率证据，需 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把器件性能下降追溯到异质界面接触效应，形成从微观界面到宏观功率的链条。
- 方法资产：真实拓扑模拟 + 间接测试 + 等效层 + 简化公式的四段式。
- 实验资产：利用 Seebeck 特性反推 TCR，绕开直接测界面温度困难。
- 公式资产：将 TCR/ECR 引起的温差变化和内阻变化转成最大输出功率估算。
- 风险控制资产：在结论中明确公式适用范围和最大偏差。
- 附录资产：把辐射模型、边界条件、实验测量和不确定性放入附录，增强方法可信度。

## 18. 对我写论文的启发

这篇论文最值得学习的是“不要停在局部参数”。如果研究界面接触，不只报告 TCR 随压力变化，还要说明它如何影响器件输出、系统效率或设计公式。本文通过最大输出功率公式把界面研究推到了工程可用层。

第二个启发是实验方法可以来自被测对象的物理特性。TE 材料有 Seebeck 效应，作者就用这个效应做间接 TCR 测试。自己的研究中也可以寻找“对象自带的物理响应”来设计测量方法。

第三个启发是公式要写边界。作者明确 pressure、temperature、roughness、gap medium 范围，使公式看起来更可信。模糊地说“适用于 TEG”反而容易被审稿人攻击。

## 19. 最终浓缩

这篇论文的核心贡献是定量打通 TEG 中 TE leg-electrode 界面接触效应与整机最大输出功率之间的关系。作者用真实拓扑接触模型预测 TCR/ECR，用基于 Seebeck 特性的间接实验验证 TCR，并将接触效应用等效层纳入 TEG 热电模型，最终给出最大输出功率预测公式，最大偏差 7.7%。最值得学习的是“微观界面 -> 实验测量 -> 整机性能 -> 设计公式”的完整论证链；最需要复核的是 TCR 实验偏差、Fig. 16-24 的功率/场图细节、Table 7 电压数据和公式适用范围。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.txt` 与 `801/文本/metadata/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 The TEG, rough surfaces and electric power generation （对象/问题/模块）
  - L3 p.3: 2.1 The TEG and material properties （对象/问题/模块）
  - L3 p.4: 2.2 Theoretical power generation of TEG with consideration of contact effects （对象/问题/模块）
  - L3 p.5: 2.3 Rough surfaces and contacting models （方法/模型）
- L2 p.5: 3 Numerical models （方法/模型）
  - L3 p.5: 3.1 Governing equations （对象/问题/模块）
    - L4 p.6: 3.1.1 Equilibrium equation （对象/问题/模块）
    - L4 p.6: 3.1.2 Geometric equation （对象/问题/模块）
    - L4 p.6: 3.1.3 Constitutive equations for elastic stage （对象/问题/模块）
    - L4 p.6: 3.1.4 Constitutive equations for plastic stage （对象/问题/模块）
  - L3 p.6: 3.2 Calculation methods of TCR and ECR （方法/模型）
  - L3 p.6: 3.3 Boundary conditions （对象/问题/模块）
  - L3 p.7: 3.4 Meshed models （方法/模型）
- L2 p.8: 4 Experimental measurement （对象/问题/模块）
  - L3 p.8: 4.1 Experimental method for TCR （方法/模型）
  - L3 p.9: 4.2 Experimental platform for TCR （对象/问题/模块）
  - L3 p.9: 4.3 Experimental measurements of ECR and power generation （对象/问题/模块）
- L2 p.9: 5 Results and discussions （结果/讨论/验证）
  - L3 p.9: 5.1 Contact mechanics and heat transfer （对象/问题/模块）
  - L3 p.13: 5.2 Thermal and electrical contact resistance （对象/问题/模块）
    - L4 p.13: 5.2.1 The influence of thermal radiation （对象/问题/模块）
    - L4 p.13: 5.2.2 The influence of average interface temperature （对象/问题/模块）
    - L4 p.15: 5.2.3 The influence of loading pressure （对象/问题/模块）
    - L4 p.16: 5.2.4 The experimental results of thermal contact resistance （结果/讨论/验证）
    - L4 p.19: 5.2.5 Electrical contact resistance （对象/问题/模块）
  - L3 p.19: 5.3 The quantitative description of contact effects in TEG （对象/问题/模块）
    - L4 p.19: 5.3.1 Considering the impact of TCR （对象/问题/模块）
    - L4 p.23: 5.3.2 Considering the impact of both TCR and ECR （对象/问题/模块）
- L2 p.26: 6 Conclusion （结论）
- L2 p.26: Data availability statement （对象/问题/模块）
- L2 p.26: Declaration of Competing Interest （对象/问题/模块）
- L2 p.26: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.26: Acknowledgments （对象/问题/模块）
- L2 p.26: Appendix A Calculation method of thermal radiation （方法/模型）
- L2 p.27: Appendix B Boundary conditions of contacting models （方法/模型）
- L2 p.27: Appendix C Experimental measurement of TCR （附录）
- L2 p.28: Appendix D Experimental measurement of power generation （附录）
- L2 p.28: Appendix E Uncertainty analysis （附录）
- L2 p.29: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 The TEG, rough surfaces and electric power generation | 3 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 The TEG and material properties | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Theoretical power generation of TEG with consideration of contact effects | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.3 Rough surfaces and contacting models | 5 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Numerical models | 5 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Governing equations | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1.1 Equilibrium equation | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1.2 Geometric equation | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1.3 Constitutive equations for elastic stage | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1.4 Constitutive equations for plastic stage | 6 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Calculation methods of TCR and ECR | 6 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Boundary conditions | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 Meshed models | 7 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Experimental measurement | 8 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Experimental method for TCR | 8 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Experimental platform for TCR | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 Experimental measurements of ECR and power generation | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Results and discussions | 9 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.1 Contact mechanics and heat transfer | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2 Thermal and electrical contact resistance | 13 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2.1 The influence of thermal radiation | 13 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2.2 The influence of average interface temperature | 13 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2.3 The influence of loading pressure | 15 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2.4 The experimental results of thermal contact resistance | 16 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.2.5 Electrical contact resistance | 19 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3 The quantitative description of contact effects in TEG | 19 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3.1 Considering the impact of TCR | 19 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5.3.2 Considering the impact of both TCR and ECR | 23 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 6 Conclusion | 26 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability statement | 26 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of Competing Interest | 26 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 26 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgments | 26 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix A Calculation method of thermal radiation | 26 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix B Boundary conditions of contacting models | 27 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix C Experimental measurement of TCR | 27 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix D Experimental measurement of power generation | 28 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix E Uncertainty analysis | 28 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 29 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 异质界面接触效应的精确定量描述是开发具有高超音速气动热收集潜力的热电发电机（TEG）的关键问题。本文通过基于实拓扑的数值预测和新颖的间接实验测试研究了热电（TE）腿和电极之间的热电接触效应，并提出了两个简化公式来定量表达它们对 TEG 的影响。首先，预测了不同温度、压力、间隙介质和热辐射条件下的热接触电阻和电接触电阻。其次，开发了一种基于TE转换特性的新型间接热接触热阻（TCR）测试方法，建立了相应的平台并对数值模型进行了验证。第三，考虑等效层的接触效应，模拟了TEG的TE转换过程，开发了TCR测试平台来测量TEG的输出功率，并对数值模型进行了验证。最后推导了考虑接触效应的TEG最大输出功率预测的两个预测公式，与数值结果吻合较好，最大偏差为7.7%。 © 2022 Elsevier Ltd. 保留所有权利。

### 20.5 结论完整摘录（本地证据）

结论章节识别：6 Conclusion；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/The-quantitative-study-of-interfacial-contact-effec_2023_International-Journ.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 在这项工作中，通过基于真实拓扑的预测和新颖的间接测试，研究了应用于高超声速飞行器的TE腿和电极之间的热电接触效应，并通过相应的模拟和测量阐明了它们对TEG的影响，并最终提出了两个预测公式。首先，根据重建的粗糙表面预测热阻和电接触电阻，并分析温度、加载压力、间隙介质和热辐射的影响。另一方面，开发了一种新颖的间接TCR测试方法并建立了相应的平台，测量了不同温度和加载压力下的TCR并验证了数值模型。该平台还经过改造，可以测量 TEG 的 ECR 和电源。第三，考虑等效层界面接触效应，模拟了TEG的传热和转换过程，测量了TEG在不同温度下的供电情况，并对数值模型进行了验证。最后，考虑了 TEG 的热阻和热电接触电阻，建立了两个简化的最大输出功率预测公式。
> 
> 结果显示了一些结论：
> 
> 1 在TCR的数值预测中，考虑了热传导和热辐射，并根据重建的TE腿和电极的真实粗糙表面形貌建立了模型。该方法可用于预测不同温度、负载压力和间隙介质下的接触热阻。 2 热辐射对TCR的影响随着真空或气隙下平均界面温度的升高而逐渐增大。当间隙介质为真空时，TCR主要受TE材料导热系数的影响；而当间隙介质为空气时，TCR随着平均界面温度的升高而降低。 3 随着加载压力的增加，TCR降低，但趋势减慢。空气间隙下的TCR约为真空间隙下的一半，银胶间隙下的TCR约为真空间隙下的千分之一。 4 所开发的 TCR 测试方法对于获得包含一条 TE 腿和两个电极的测试样品的合理实验结果至关重要。相应的实验平台可以测量不同温度和加载压力下的TCR，实验结果与数值结果吻合较好，最大差异为-27.51%。
> 
> 该平台还可以进行更改以测量 TEG 的 ECR 和电源。 5 ECR对TEG的负面影响高于真空或气隙下TCR的负面影响；而在银环氧胶间隙下TCR略高于ECR。银环氧胶间隙下接触效应引起的TEG的TE性能下降不超过4%；而气隙则超过96%。 6 通过测量 TEG 的供电电源来验证所提出的评估接触效应对 TEG 影响的数值模型，最大差异为 8.73%。

### 20.7 论文逻辑脉络复核

- 提出的问题：The TCR under air gap is about half of that under vacuum gap, and the TCR under the silverepoxy adhesive gap is about one-thousandth of that under vacuum gap. 4 The developed TCR test approach is essential to obtain reasonable experimental results for the test sample containing one TE leg and two electrodes.
- 旧方法/已有研究不足：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 本文解决方式：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest. In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG. Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 学术/工程增量：需结合 Results/Conclusion 的量化结果复核。
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：83
- Introduction 引用簇数量（估计）：31
- References 条目数（解析）：42
- 可识别年份条目数：83
- 近五年/近年文献（2021+）数量：16
- 经典文献（2010年前）数量：1
- 同刊引用数量（按 subject 粗略匹配）：2
- 高频来源期刊（粗略）：International Journal of Heat and Mass Transfer(2)
- 引用簇样例：[1], [6], [7], [8], [9], [10], [11], [12], [22], [23], [24], [16]

带引用的 gap/转折句样例：

- 未在 Introduction 中自动识别到带引用的 gap 句；需人工复核文献转折段。

References 解析样例（前12条）：

- [1] JJ Gou, JX Hu, ZW Yan, G Gao, CL. Gong, Effects of physical dimensions, temperature ranges and interfacial thermal contacts on the multi-stage thermoelectric generators for a hypersonic vehicle, Int. J. Energy Res. 46 (2022) 20 021–20 038, doi: 10.1002/er.7799 .
- [2] JJ Gou, ZW Yan, JX Hu, G Gao, CL. Gong, The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion, Aerosp. Sci. Technol. 108 (2021) 106373, doi: 10.1016/j.ast.2020.106373 .
- [3] BX Shen, WQ. Liu, Insulating and absorbing heat of transpiration in a combinational opposing jet and platelet transpiration blunt body for hypersonic vehicle, Int. J. Heat Mass Transf. 138 (2019) 314–325, doi: 10.1016/j. ijheatmasstransfer.2019.04.057 .
- [4] G Gao, J-J Gou, C-L Gong, J-X Hu, R-C. Gao, A novel mechanical-thermalelectrical thermal protection system concept and its multi-scale performance evaluation for hypersonic launch vehicles, Compos. Struct. 268 (2021) 113962, doi: 10.1016/j.compstruct.2021.113962 .
- [5] CL Gong, JJ Gou, JX Hu, F. Gao, A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles, Aerosp. Sci. Technol. 77 (2018) 458–470, doi: 10.1016/j.ast.2018.03.028 .
- [6] T Cui, Q Li, Y. Xuan, Characterization and application of engineered regular rough surfaces in thermal contact resistance, Appl. Therm. Eng. 71 (2014) 400– 409, doi: 10.1016/j.applthermaleng.2014.07.020 .
- [7] J Liu, C Ma, S Wang, S Wang, B. Yang, Thermal contact resistance between bearing inner ring and shaft journal, Int. J. Therm. Sci. 138 (2019) 521–535, doi: 10.1016/j.ijthermalsci.2019.01.022 .
G. Gao, D. Li, J.-J. Gou et al. International Journal of Heat and Mass Transfer 201 (2023) 123579
- [8] PG Siddappa, A. Tariq, Contact area and thermal conductance estimation based on the actual surface roughness measurement, Tribol. Int. 148 (2020) 106358, doi: 10.1016/j.triboint.2020.106358 .
- [9] A Aalilija, C-A Gandin, E. Hachem, A simple and efficient numerical model for thermal contact resistance based on diffuse interface immersed boundary method, Int. J. Therm. Sci. 166 (2021) 106817, doi: 10.1016/j.ijthermalsci.2020. 106817 .
- [10] J-J Gou, X-J Ren, Y-J Dai, S. Li, Study of thermal contact resistance of rough surfaces based on the practical topography, Comput. Fluids 164 (2018) 2–11, doi: 10.1016/J.COMPFLUID.2016.09.018 .
- [11] YJ Dai, JJ Gou, XJ Ren, F Bai, WZ Fang, WQ. Tao, A test-validated prediction model of thermal contact resistance for Ti-6Al-4V alloy, Appl. Energy 228 (2018) 1601–1617, doi: 10.1016/j.apenergy.2018.06.134 .
- [12] XJ Ren, YJ Dai, JJ Gou, WQ. Tao, Numerical prediction of thermal contact resistance of 3D C/C-SiC needled composites based on measured practical topography, Int. J. Heat Mass Transf. 131 (2019) 176–188, doi: 10.1016/j. ijheatmasstransfer.2018.08.137 .

### 20.9 常用词、词类、语态与时态

- 高频词：tcr(193)；temperature(178)；contact(145)；teg(145)；gap(144)；leg(132)；heat(123)；fig(112)；type(107)；thermal(102)；about(100)；when(96)；ecr(90)；legs(84)；electrodes(84)；air(72)；respectively(72)；side(71)；loading(71)；power(68)
- 高频名词化/学术名词：temperature(178)；resistance(63)；pressure(53)；measurement(44)；condition(39)；difference(32)；radiation(30)；conductivity(30)；compression(30)；displacement(30)；prediction(28)；conduction(22)；distribution(21)；deviation(20)；uence(20)
- 高频学术动词：compared(13)；developed(8)；predicted(7)；validated(7)；predict(5)；derived(3)；indicate(2)；estimate(2)；indicated(1)；estimated(1)
- 高频形容词：thermal(102)；electric(55)；experimental(49)；numerical(46)；adhesive(45)；measurement(44)；potential(35)；journal(31)；electrical(31)；international(30)；displacement(30)；real(28)；table(24)；cient(21)；material(17)
- 高频副词：respectively(72)；gradually(17)；mainly(15)；only(8)；supply(8)；relatively(7)；tively(7)；slightly(6)；cantly(5)；numerically(4)；finally(3)；greatly(3)；ually(2)；july(1)；quantitatively(1)
- 高频二词短语：type leg(62)；loading pressure(44)；output power(38)；maximum output(37)；heat mass(35)；air gap(35)；cold side(34)；silver-epoxy adhesive(34)；hot side(33)；international journal(30)；journal heat(30)；mass transfer(30)
- 高频三词短语：maximum output power(32)；international journal heat(30)；journal heat mass(30)；heat mass transfer(30)；page gao gou(28)；gao gou international(28)；gou international journal(28)；silver-epoxy adhesive gap(20)；thermal contact resistance(18)；output power teg(18)；average interface temperature(17)；seebeck coe cient(15)
- 被动语态估计：213；`we + 动作动词` 主动句估计：0
- 一般现在时线索：531；一般过去时线索：483；现在完成时线索：2；情态动词线索：92

章节词频：

- Abstract: contact(6)；effects(5)；thermal(4)；numerical(4)；teg(3)；thermoelectric(2)；tegs(2)；electrical(2)
- Introduction: tcr(41)；leg(32)；ecr(28)；type(26)；teg(26)；heat(24)；contact(24)；electrode(22)
- Conclusion: gap(14)；tcr(13)；teg(12)；thermal(8)；contact(8)；loading(6)；power(6)；vacuum(6)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Proper characterization of rough surfaces is essential for the accurate estimation of TCR.
  可迁移模板：Proper characterization of rough surfaces is essential for the accurate estimation of METHOD.
- 原句/结构：The essential assumptions involved in above characterizations weakens their accuracy.
  可迁移模板：The essential assumptions involved in above characterizations weakens their accuracy.
- 原句/结构：ECRs play an important role in ensuring the energy efficiency, thermal behavior and stable operation of electrical connections.
  可迁移模板：ECRs play an important role in ensuring the energy efficiency, thermal behavior and stable operation of electrical connections.
#### Gap句
- 原句/结构：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  可迁移模板：METHOD legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 原句/结构：The study of TE materials is very limited, Nomenclature Abbreviations TCR thermal contact resistance ECR electrical contact resistance TE thermoelectric TEG thermoelectric generator TEC thermoelectric cooler TPS thermal protection system PEEK poly-ether-ether-ketone Symbols S Seebeck coefficient k electrical conductivity T absolute temperature T 1 hot side temperature of contacting pairs in simulation T 2 cold side temperature of contacting pairs in simulation T S average temperature of rough surfaces T h temperature of the electrode on the hot side of test sample T c temperature of the electrode on the cold side of test sample T T Eh hot side temperature for TE leg of test sample T T Ec cold side temperature for TE leg of test sample T h P hot side temperature of P -type TE leg T c P cold side temperature of P -type TE leg T h N hot side temperature of N -type TE leg T c N cold side temperature of N -type TE leg T h E hot side temperature of electrodes T c E cold side temperature of electrodes �T temperature difference �T T CR T Ea v g average temperature difference of TE legs with TCR �T PC E temperature difference of electrodes without TCR or ECR x , y , z Cartesian coordinate u , v , w displacements in x , y and zdirection w c compression displacements q heat flux q c heat flux of solid conduction q r heat flux of thermal radiation q P heat flux through P -type TE leg q N heat flux through N -type TE leg F view factor E surface emissivity D e elasticity matrix D p plasticity matrix ¯d average distance of rough surfaces c p specific heat capacity P maximum output power of tested TE leg P T CR max maximum output power of TEG with TCR P ECR max maximum output power of TEG with ECR P PC max maximum output power of TEG without TCR or ECR P T & E max maximum output power of TEG with TCR and ECR A cross-sectional area of TE leg U electric potential �U electric potential difference U PC electric potential of TEG without TCR or ECR U T CR electric potential of TEG with TCR j electrical current density R T h TCR between hot side of TE leg and electrode of test sample G.
  可迁移模板：The study of METHOD materials is very limited, Nomenclature Abbreviations METHOD thermal contact resistance METHOD electrical contact resistance METHOD thermoelectric METHOD thermoelectric generator METHOD thermoelectric cooler METHOD thermal protection system METHOD poly-ether-ether-ketone Symbols S Seebeck coefficient k electrical conductivity T absolute temperature T Xhot side temperature of contacting pairs in simulation T Xcold side temperature of contacting pairs in simulation T S average temperature of rough surfaces T h temperature of the electrode on the hot side of test sample T c temperature of the electrode on the cold side of test sample T T Eh hot side temperature for METHOD leg of test sample T T Ec cold side temperature for METHOD leg of test sample T h P hot side temperature of P -type METHOD leg T c P cold side temperature of P -type METHOD leg T h N hot side temperature of N -type METHOD leg T c N cold side temperature of N -type METHOD leg T h E hot side temperature of electrodes T c E cold side temperature of electrodes �T temperature difference �T T METHOD T Ea v g average temperature difference of METHOD legs with METHOD �T METHOD E temperature difference of electrodes without METHOD or METHOD x , y , z Cartesian coordinate u , v , w displacements in x , y and zdirection w c compression displacements q heat flux q c heat flux of solid conduction q r heat flux of thermal radiation q P heat flux through P -type METHOD leg q N heat flux through N -type METHOD leg F view factor E surface emissivity D e elasticity matrix D p plasticity matrix ¯d average distance of rough surfaces c p specific heat capacity P maximum output power of tested METHOD leg P T METHOD max maximum output power of METHOD with METHOD P METHOD max maximum output power of METHOD with METHOD P METHOD max maximum output power of METHOD without METHOD or METHOD P T & E max maximum output power of METHOD with METHOD and METHOD A cross-sectional area of METHOD leg U electric potential �U electric potential difference U METHOD electric potential of METHOD without METHOD or METHOD U T METHOD electric potential of METHOD with METHOD j electrical current density R T h METHOD between hot side of METHOD leg and electrode of test sample G.
- 原句/结构：Since the TE material is brittle (difficult to punch signal holes), it is difficult to measure the TCR by direct methods.
  可迁移模板：Since the METHOD material is brittle (difficult to punch signal holes), it is difficult to measure the METHOD by direct methods.
#### 方法句
- 原句/结构：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
  可迁移模板：The precise quantitative description of contact effects at heterogeneous interfaces is the crucial issue in developing thermoelectric generators (TEGs) with potential of hypersonic aerodynamic heat harvest.
- 原句/结构：In this paper, the thermal and electrical contact effects between thermoelectric (TE) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on TEG.
  可迁移模板：In this paper, the thermal and electrical contact effects between thermoelectric (METHOD) legs and electrodes are studied by real-topology-based numerical predictions and novel indirect experimental tests, and two simplified formulas are proposed to quantitatively express their effects on METHOD.
- 原句/结构：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
#### 结果句
- 原句/结构：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd.
  可迁移模板：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of X. © XElsevier Ltd.
- 原句/结构：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of 7.7%. © 2022 Elsevier Ltd.
  可迁移模板：Finally, two prediction formulas for the maximum output power prediction of TEGs with considering the contact effects are derived, and good agreement with numerical results is obtained by the maximum deviation of X. © XElsevier Ltd.
- 原句/结构：Finally, two simplified formulas to predict the maximum output power of the TEG are established, which are in good agreement with the numerical results.
  可迁移模板：Finally, two simplified formulas to predict the maximum output power of the METHOD are established, which are in good agreement with the numerical results.
#### 贡献句
- 原句/结构：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句/结构：Second, a novel indirect thermal contact resistance (TCR) test approach relying on the TE conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
  可迁移模板：Second, a novel indirect thermal contact resistance (METHOD) test approach relying on the METHOD conversion characteristics is developed, a corresponding platform is established and the numerical models are then validated.
- 原句/结构：The authors tried to establish TCR prediction models based on the measured real topology and the models have relatively good agreement with experiments.
  可迁移模板：The authors tried to establish METHOD prediction models based on the measured real topology and the models have relatively good agreement with experiments.
#### 限制/边界句
- 原句/结构：TE legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
  可迁移模板：METHOD legs and electrodes have micro-scale rough surfaces, and such type of roughness will lead to the very limited real contact region and a large proportion of contact gap.
- 原句/结构：The study of TE materials is very limited, Nomenclature Abbreviations TCR thermal contact resistance ECR electrical contact resistance TE thermoelectric TEG thermoelectric generator TEC thermoelectric cooler TPS thermal protection system PEEK poly-ether-ether-ketone Symbols S Seebeck coefficient k electrical conductivity T absolute temperature T 1 hot side temperature of contacting pairs in simulation T 2 cold side temperature of contacting pairs in simulation T S average temperature of rough surfaces T h temperature of the electrode on the hot side of test sample T c temperature of the electrode on the cold side of test sample T T Eh hot side temperature for TE leg of test sample T T Ec cold side temperature for TE leg of test sample T h P hot side temperature of P -type TE leg T c P cold side temperature of P -type TE leg T h N hot side temperature of N -type TE leg T c N cold side temperature of N -type TE leg T h E hot side temperature of electrodes T c E cold side temperature of electrodes �T temperature difference �T T CR T Ea v g average temperature difference of TE legs with TCR �T PC E temperature difference of electrodes without TCR or ECR x , y , z Cartesian coordinate u , v , w displacements in x , y and zdirection w c compression displacements q heat flux q c heat flux of solid conduction q r heat flux of thermal radiation q P heat flux through P -type TE leg q N heat flux through N -type TE leg F view factor E surface emissivity D e elasticity matrix D p plasticity matrix ¯d average distance of rough surfaces c p specific heat capacity P maximum output power of tested TE leg P T CR max maximum output power of TEG with TCR P ECR max maximum output power of TEG with ECR P PC max maximum output power of TEG without TCR or ECR P T & E max maximum output power of TEG with TCR and ECR A cross-sectional area of TE leg U electric potential �U electric potential difference U PC electric potential of TEG without TCR or ECR U T CR electric potential of TEG with TCR j electrical current density R T h TCR between hot side of TE leg and electrode of test sample G.
  可迁移模板：The study of METHOD materials is very limited, Nomenclature Abbreviations METHOD thermal contact resistance METHOD electrical contact resistance METHOD thermoelectric METHOD thermoelectric generator METHOD thermoelectric cooler METHOD thermal protection system METHOD poly-ether-ether-ketone Symbols S Seebeck coefficient k electrical conductivity T absolute temperature T Xhot side temperature of contacting pairs in simulation T Xcold side temperature of contacting pairs in simulation T S average temperature of rough surfaces T h temperature of the electrode on the hot side of test sample T c temperature of the electrode on the cold side of test sample T T Eh hot side temperature for METHOD leg of test sample T T Ec cold side temperature for METHOD leg of test sample T h P hot side temperature of P -type METHOD leg T c P cold side temperature of P -type METHOD leg T h N hot side temperature of N -type METHOD leg T c N cold side temperature of N -type METHOD leg T h E hot side temperature of electrodes T c E cold side temperature of electrodes �T temperature difference �T T METHOD T Ea v g average temperature difference of METHOD legs with METHOD �T METHOD E temperature difference of electrodes without METHOD or METHOD x , y , z Cartesian coordinate u , v , w displacements in x , y and zdirection w c compression displacements q heat flux q c heat flux of solid conduction q r heat flux of thermal radiation q P heat flux through P -type METHOD leg q N heat flux through N -type METHOD leg F view factor E surface emissivity D e elasticity matrix D p plasticity matrix ¯d average distance of rough surfaces c p specific heat capacity P maximum output power of tested METHOD leg P T METHOD max maximum output power of METHOD with METHOD P METHOD max maximum output power of METHOD with METHOD P METHOD max maximum output power of METHOD without METHOD or METHOD P T & E max maximum output power of METHOD with METHOD and METHOD A cross-sectional area of METHOD leg U electric potential �U electric potential difference U METHOD electric potential of METHOD without METHOD or METHOD U T METHOD electric potential of METHOD with METHOD j electrical current density R T h METHOD between hot side of METHOD leg and electrode of test sample G.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
