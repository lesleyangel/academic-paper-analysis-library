# Transcriptome sequencing reveals the promotion of apoptosis and M1 polarization of microglia under simulated microgravity

## 0. 读取说明

- 文本来源：`801/文本/txt/Transcriptome-sequencing-reveals-the-promotion-of-apoptosis-an_2024_Acta-Ast.txt`，PyMuPDF 抽取，9 页。
- 抽取文本包含摘要、引言、BV2 细胞/RPM 方法、细胞活性/极化/凋亡实验、RNA-seq、GO/KEGG、qPCR 验证、讨论和结论。
- 原文多处双栏交错，尤其 Discussion 与 qPCR 验证段落互相穿插；本文根据章节顺序复原。流式门控图、火山图、热图、富集气泡图和 qPCR 柱状图均需要 PDF 图像复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Materials and methods, 3 Results, 4 Discussion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Transcriptome sequencing reveals the promotion of apoptosis and M1 polarization of microglia under simulated microgravity。
- 作者：Hui Yu, Xu-Yi Jia, Li-Na Gao, Ting Huyan, Jian-Jun Gou, Chun-Lin Gong, Liang-Xian Gu。
- 期刊：Acta Astronautica, 219 (2024) 722-730。
- 领域：航天生物医学、模拟微重力、微胶质细胞、神经炎症、转录组测序。
- 论文类型：细胞实验 + 流式检测 + RNA-seq 差异表达 + 富集分析 + qPCR 验证。
- 研究对象：BV2 microglial cells 在随机定位机 RPM 模拟微重力下的活性、形态、M1 极化、凋亡和基因表达变化。
- 主要方法：RPM 24 h 处理，CCK-8 检测活性，CD80/CD86 流式检测 M1 极化，Annexin V-FITC/PI 检测凋亡，Illumina RNA-seq 筛选 DEGs，GO/KEGG 富集，qPCR 验证 10 个候选基因。
- 论文身份判断：这是一篇航天医学方向的机制探索论文，核心不是直接证明宇航员认知损伤，而是用 BV2 细胞模型提供微重力影响微胶质炎症/凋亡的转录组线索。

## 2. 摘要与核心信息提取

本文核心主张是：模拟微重力会降低 BV2 微胶质细胞活性，诱导 M1 极化并显著增加晚期凋亡；转录组测序发现 142 个差异表达基因，其中多个与炎症、细胞因子信号和凋亡通路相关，这些变化可能参与微重力导致的神经炎症和神经退行性风险。

摘要的证据链由三层组成：细胞表型层，RPM 处理后细胞活性下降、M1 极化、晚期凋亡增加；转录组层，142 个 DEGs 与 microglial phenotype 和 inflammation 相关；验证层，qPCR 对候选 DEGs 进行确认。最后作者把结果上升到长期载人航天和深空探索医学支持。

一句话浓缩：本文用 RPM-BV2 细胞模型和 RNA-seq 说明，微重力可能通过促炎极化和凋亡路径损害微胶质细胞稳态。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Transcriptome-sequencing-reveals-the-promotion-of-apoptosis-an_2024_Acta-Ast.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Transcriptome-sequencing-reveals-the-promotion-of-apoptosis-an_2024_Acta-Ast.md`。

中文译文：

> 空间科学技术领域的突飞猛进，方便了宇航员在太空环境中的长期居住。然而，宇航员的神经和认知障碍已成为直接阻碍航天任务顺利完成的主要因素。研究表明，微重力可以通过改变大脑微环境（BME）来削弱神经元功能和认知能力。小胶质细胞是负责调节血脑屏障完整性的重要免疫细胞，已被确定为微重力条件下观察到的神经功能恶化的主要影响因素。这项研究的主要目的是了解微重力条件下小胶质细胞行为的分子过程。我们的研究使用随机定位机 (RPM) 模拟微重力，发现微重力会降低 BV2 小胶质细胞的活力，诱导 M1 极化，并显着增加晚期细胞凋亡。转录组分析揭示了 142 个与小胶质细胞表型和炎症相关的差异表达基因，并通过 qPCR 验证了选定的 DEG。这些结果阐明了微重力下小胶质细胞行为的分子机制，突出了基因表达变化和细胞损伤。
>
> 该研究为理解微重力对神经系统的影响、建立针对航天飞行对神经系统功能损伤的对策提供了概念框架，为未来深空探测和长期载人航天医疗保障提供了参考。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自长期太空驻留带来的神经与认知风险。微重力、辐射、低磁场、封闭环境和心理压力都会影响宇航员健康，其中认知和神经系统损伤会直接影响任务完成。已有研究多关注肌肉骨骼、心血管和脑血流变化，但微胶质细胞如何响应微重力仍不充分清楚。

作者把宏大问题收束到一个可实验化对象：microglia 是中枢神经系统的主要免疫细胞，能通过 M1/M2 极化调节 brain microenvironment。若微重力诱导微胶质过度激活、促炎因子释放和凋亡，可能成为神经炎症和认知损伤的中间机制。

这篇论文的选题价值在于“机制前哨”。它不直接研究宇航员大脑，也不做动物模型，而是先用 BV2 细胞和转录组找到微重力影响微胶质的候选通路，为后续体内研究和干预策略提供靶点。

## 4. 领域位置与文献版图

文献版图分三层。

第一层是航天环境对人体系统影响，包括微重力对肌肉、骨骼、心血管、脑血管、神经和免疫系统的影响。它为选题提供任务重要性。

第二层是微胶质细胞在脑微环境中的作用。作者引用微胶质 M1/M2 极化、神经炎症、神经退行性疾病、创伤性脑损伤等研究，说明微胶质状态变化可能影响神经功能。

第三层是微重力与神经/免疫细胞变化。作者提到已有模拟微重力可能增强微胶质活性、改变小鼠脊髓灰质/白质中胶质细胞基因表达等研究，但认为微胶质响应机制仍有限。本文位于“微重力-微胶质-转录组机制”的交叉位置。

## 5. Gap 制造机制

本文的 gap 是典型的机制不足 gap：已有证据表明微重力会损害神经功能和认知能力，也有研究提示微胶质可能参与其中，但微胶质在微重力下的表型变化、凋亡变化和分子通路仍缺少系统数据。

作者没有把 gap 写成“无人研究微胶质”，而是说 current understanding is still limited，需要进一步 clarify mechanisms。这种表述比较稳，因为微重力和微胶质已有相关研究，但缺少 RNA-seq 层面的全面观察。

另一个隐含 gap 是“表型与基因之间的桥”。单独观察细胞活性或凋亡，只能说明受损；单独 RNA-seq 又可能缺少功能表型。本文把 CCK-8、流式极化、凋亡和 transcriptome 结合，试图让表型和分子证据互相支撑。

## 6. 创新性判断

- 创新类型：航天医学细胞模型 + 转录组机制探索。
- 真实创新点 1：以 BV2 microglia 为对象，系统检测模拟微重力下活性、形态、M1 极化和凋亡变化。
- 真实创新点 2：RNA-seq 识别 142 个 DEGs，其中 121 个上调、21 个下调，并将其连接到炎症和凋亡通路。
- 真实创新点 3：通过 qPCR 验证候选基因，9/10 个基因趋势与 RNA-seq 一致，提高转录组结果可信度。
- 真实创新点 4：将 Il1b、Ptgs2/COX-2、Src、Fos、Arg1、Clec7a 等基因与微胶质炎症、极化和神经退行性风险联系起来。
- 创新强度：中等。细胞模型和 RNA-seq 组合并不罕见，但用于微重力下微胶质表型/转录组分析具有航天医学针对性。
- 可挑战之处：BV2 永生化细胞、RPM 模拟微重力、24 h 单时间点和缺少因果干预，使机制结论仍偏探索。

## 7. 论证链条复原

1. 长期载人航天中神经和认知损伤是任务风险。
2. 微胶质细胞调控脑微环境，过度 M1 激活和凋亡可能导致神经炎症。
3. 微重力对微胶质的具体分子机制仍不清楚。
4. 使用 RPM 随机定位机模拟微重力，处理 BV2 细胞 24 h。
5. 先检测细胞层面表型：细胞浓度/活性下降，形态变圆变大，M1 标记 CD80/CD86 增强，晚期凋亡增加。
6. 再用 RNA-seq 筛选差异表达基因，获得 142 个 DEGs。
7. GO/KEGG 富集显示 cytokine-mediated signaling、defense response、apoptotic signaling、IL-17、NF-kappa B、TNF 等通路。
8. qPCR 验证候选 DEGs，9 个与 RNA-seq 一致，F10 不一致。
9. Discussion 将 Il1b、Ptgs2、Src、Fos 等上调基因与神经炎症联系起来，将 Arg1/Clec7a 等下调与修复/吞噬调节联系起来。
10. 最后提出微重力诱导的微胶质改变可能影响神经炎症和认知功能，但需要体内和真实空间环境进一步验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：In conclusion, our study suggests that microgravity-induced changes in microglia could affect neuroinflammation and neurodegeneration in the brain, potentially impacting critical cognitive functions such as attention and memory, essential for space missions.
- 已有研究不足/GAP：However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions. However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions.
- 本文解决方式：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support. Presently, the rapid advancement of space research and technology has facilitated the prolonged habitation of astronauts in the space environment [1].
- 学术或工程增量：The primary objective of this study was to provide an understanding of the molecular processes underlying the behavior of microglia under conditions of microgravity. Transcriptome analysis revealed 142 differentially expressed genes related to microglial phenotype and inflammation, with qPCR validating selected DEGs. This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

RPM 系统为双轴随机旋转装置，速度随机变化约 0-8 rpm，目标是平均掉地球重力矢量。BV2 细胞被接种到载玻片并置于专用培养瓶中，37 °C、5% CO2 条件下处理 24 h。对照组在正常重力条件下培养。

细胞表型检测包括四部分。第一，显微镜和 Vi-CELL 观察细胞浓度和形态。第二，CCK-8 在 450 nm 检测细胞活性。第三，CD86 和 CD80 作为 M1 极化标记，通过流式细胞术检测。第四，Annexin V-FITC/PI 双染区分活细胞、早期凋亡和晚期凋亡/坏死。

RNA-seq 方法包括总 RNA 提取、mRNA 富集、片段化、cDNA 合成、文库构建和 Illumina 测序。质量控制中 Q30 bases 每个样本不低于 95.88%。clean reads 对齐到 mouse reference genome GRCm38.p6，使用 hisat2、Rsubread、limma、edgeR/DESeq2 等工具进行表达和差异分析。筛选阈值为 fold change ≥ 2、adjusted p < 0.05。

富集分析使用 enrichGO 和 enrichKEGG。qPCR 选择 Arg1、Il1b、Ptgs2、Src、Fos、Clec7a、F10 以及 Gm44851、Gm22748、Gm9831 等 10 个候选基因，GAPDH 为内参，使用 2^-ΔΔCt 计算表达量。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| RPM 模拟微重力降低 BV2 活性 | Fig. 1、Results 3.1 | 显微/Vi-CELL 显示细胞浓度下降，CCK-8 显示 viability 被显著抑制 | 中强 | 需要排除旋转剪切和培养瓶因素 |
| 模拟微重力诱导 BV2 M1 极化 | Fig. 2、Results 3.2 | CD86/CD80 流式检测显示 M1 phenotype BV2 cells 增加 | 中强 | M1/M2 仅靠 CD80/CD86 较有限 |
| 模拟微重力显著增加晚期凋亡 | Fig. 3、Results 3.3 | Annexin V-FITC/PI 显示 early apoptosis 无显著差异，late apoptosis/necrosis 增加 | 强 | 晚期凋亡与坏死区分需门控复核 |
| RNA-seq 捕捉到广泛表达变化 | Fig. 4、Results 3.4 | 142 DEGs，121 up-regulated、21 down-regulated | 强 | 样本数和批次效应需复核 |
| DEGs 富集于炎症和凋亡相关通路 | Fig. 5、Results 3.5 | GO 包括 cytokine-mediated signaling、apoptotic signaling、inflammatory response；KEGG 包括 IL-17、NF-kappa B、TNF | 强 | 富集结果是相关性，非因果证明 |
| qPCR 基本验证 RNA-seq | Fig. 6、Results 3.6 | 10 个候选基因中 9 个趋势一致，F10 不一致 | 中强 | F10 不一致提示需扩大验证 |
| Il1b/Ptgs2/Src/Fos 上调可能连接神经炎症 | Discussion | 结合文献解释这些基因在微胶质炎症和神经退行性中的作用 | 中 | 需要干预实验验证因果 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 1 RPM 系统与细胞形态/活性 | 同时展示模拟微重力装置、细胞形态变化和 CCK-8 结果 | 微重力降低活性 | RPM 结构和柱状显著性需 PDF 图像复核 |
| Fig. 2 CD86/CD80 流式 | 证明 BV2 细胞 M1 marker 增强 | M1 极化 | 流式门控需要 PDF 复核 |
| Fig. 3 Annexin V/PI 凋亡 | 区分 viable、early apoptotic、late apoptotic/necrotic | 晚期凋亡增加 | 门控象限需 PDF 复核 |
| Fig. 4 火山图/热图 | 展示 DEGs 的数量、方向和样本聚类 | 转录组改变 | 色标、阈值和样本聚类需复核 |
| Fig. 5 GO/KEGG bar/chord/bubble | 将 DEGs 映射到生物过程和通路 | 炎症/凋亡机制 | 需要 PDF 图像复核 |
| Fig. 6 qPCR 验证 | 验证候选 DEGs 表达趋势 | RNA-seq 可信度 | 柱状图和显著性需 PDF 复核 |
| Table 1 qPCR primers | 保障 qPCR 可复现 | 验证方法 | 引物序列从文本可读，但需 PDF 复核 |
| 2^-ΔΔCt 方法 | 将 qPCR Ct 值转化为相对表达 | 基因验证 | 文本确认 |

结果叙事是“细胞损伤现象-转录组变化-通路解释-候选基因讨论”。它先让读者看到微重力确实改变细胞，再用 RNA-seq 解释可能原因。

## 11. 章节结构与篇章布局

文章结构为 Introduction；Materials and methods；Results；Discussion；Conclusion/Declarations。Results 进一步分为 reduced cell activity、M1 polarization、late apoptosis、transcriptome differential expression、enrichment analysis、DEG validation。

Introduction 从航天长期驻留的健康风险开场，再聚焦脑微环境和 microglia，最后给出本文实验设计。Methods 按实验流程排列，先细胞与 RPM，再活性、凋亡、RNA-seq、差异分析、qPCR、统计方法。Results 则按证据层级从细胞表型到基因表达推进。

小节标题偏结果型，直接暴露主要发现，如 “Reduced cell activity under simulated microgravity”“Activation M1 polarization...” 这让读者即使只扫标题也能看到论文结论。Discussion 将结果放回认知损伤、神经炎症和候选基因功能中。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Materials and methods（方法/模型/算法）
  - L3 p.2: 2.1 Cells（对象/模块/过渡章节）
  - L3 p.2: 2.2 RPM system（对象/模块/过渡章节）
  - L3 p.2: 2.3 Observation and identification of cell concentration and phenotype（对象/模块/过渡章节）
  - L3 p.2: 2.4 BV2 cell viability（对象/模块/过渡章节）
  - L3 p.3: 2.5 BV2 cell apoptosis（对象/模块/过渡章节）
  - L3 p.3: 2.6 Transcriptome sequencing（对象/模块/过渡章节）
  - L3 p.3: 2.7 Differential expression analysis and enrichment analysis（对象/模块/过渡章节）
  - L3 p.4: 2.8 Quantitative real-time PCR analysis（对象/模块/过渡章节）
  - L3 p.4: 2.9 Statistical analysis（对象/模块/过渡章节）
- L2 p.4: 3 Results（结果/验证/讨论）
  - L3 p.4: 3.1 Reduced cell activity under simulated microgravity（对象/模块/过渡章节）
  - L3 p.4: 3.2 Activation M1 polarization of BV2 cells under simulated microgravity（对象/模块/过渡章节）
  - L3 p.4: 3.3 Induced late apoptosis of BV2 cells under simulated microgravity（对象/模块/过渡章节）
  - L3 p.4: 3.4 Transcriptome sequencing for differential expression analysis（对象/模块/过渡章节）
  - L3 p.4: 3.5 Enrichment analysis of DEGs（对象/模块/过渡章节）
  - L3 p.5: 3.6 Validation of the DEGs（结果/验证/讨论）
- L2 p.5: 4 Discussion（结果/验证/讨论）
- L2 p.8: Declaration of competing interest（尾部材料）
- L2 p.8: Acknowledgments（尾部材料）
- L2 p.8: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Materials and methods | 2 | 2 | 方法/模型/算法 |
| 2.1 Cells | 2 | 3 | 对象/模块/过渡章节 |
| 2.2 RPM system | 2 | 3 | 对象/模块/过渡章节 |
| 2.3 Observation and identification of cell concentration and phenotype | 2 | 3 | 对象/模块/过渡章节 |
| 2.4 BV2 cell viability | 2 | 3 | 对象/模块/过渡章节 |
| 2.5 BV2 cell apoptosis | 3 | 3 | 对象/模块/过渡章节 |
| 2.6 Transcriptome sequencing | 3 | 3 | 对象/模块/过渡章节 |
| 2.7 Differential expression analysis and enrichment analysis | 3 | 3 | 对象/模块/过渡章节 |
| 2.8 Quantitative real-time PCR analysis | 4 | 3 | 对象/模块/过渡章节 |
| 2.9 Statistical analysis | 4 | 3 | 对象/模块/过渡章节 |
| 3 Results | 4 | 2 | 结果/验证/讨论 |
| 3.1 Reduced cell activity under simulated microgravity | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Activation M1 polarization of BV2 cells under simulated microgravity | 4 | 3 | 对象/模块/过渡章节 |
| 3.3 Induced late apoptosis of BV2 cells under simulated microgravity | 4 | 3 | 对象/模块/过渡章节 |
| 3.4 Transcriptome sequencing for differential expression analysis | 4 | 3 | 对象/模块/过渡章节 |
| 3.5 Enrichment analysis of DEGs | 4 | 3 | 对象/模块/过渡章节 |
| 3.6 Validation of the DEGs | 5 | 3 | 结果/验证/讨论 |
| 4 Discussion | 5 | 2 | 结果/验证/讨论 |
| Declaration of competing interest | 8 | 2 | 尾部材料 |
| Acknowledgments | 8 | 2 | 尾部材料 |
| References | 8 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“航天风险-神经系统重要性-微胶质机制-研究不足-本文实验”。它把宏观航天任务风险逐步收束到 BV2 细胞。

Methods 段落细节密集，以实验可复现为主。每个方法段落都包含样品、试剂/仪器、处理时间、检测平台和分析方法。

Results 段落多采用“结果先行”写法：先说 RPM 造成什么变化，再引用 Fig. 1/2/3/4/5/6。转录组结果段落先给 DEG 数量，再给火山图/热图，再进入 GO/KEGG。这种节奏符合生物实验论文常规。

Discussion 段落从“宇航员认知风险”重新打开视野，再逐步解释 M1 极化、凋亡和候选基因。最后的 limitation 段落较完整，主动承认细胞实验局限、需要 in vivo、需要 single-cell sequencing、模拟微重力和真实空间环境存在差异。

## 13. 文笔画像与语言习惯

本文语言风格是航天生物医学的跨学科叙述：宏观段落用 spaceflight、astronauts、cognitive impairment、space missions；机制段落用 microglia、M1 polarization、apoptosis、DEGs、cytokine、NF-kappa B。

语气整体偏谨慎。作者常用 “may”“potentially”“suggests”“could affect” 来处理从细胞结果到宇航员认知风险的外推，避免直接因果过强。相比材料和工程论文，这篇的结论更强调 conceptual framework 和 future research。

被动语态用于实验方法，如 “cells were collected”“DEGs were identified”；主动语态用于研究目标和结果概括，如 “our study found”。时态上，背景用现在完成时和一般现在时，实验结果用过去时，机制推测用情态动词。

高频词 microgravity、cells、microglia、BV2、apoptosis、RPM、genes、polarization 显示文章焦点集中。常见形容词包括 neurological、cognitive、inflammatory、differential、simulated。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：32590
- 高频词：microgravity(54)；cells(47)；microglia(28)；cell(27)；space(22)；analysis(22)；system(22)；research(21)；rpm(21)；genes(19)；apoptosis(16)；degs(16)；cognitive(15)；study(15)；gene(15)；brain(14)；sequencing(14)；changes(13)；expression(13)；reverse(12)
- 高频名词化/学术名词：microgravity(54)；expression(13)；treatment(11)；environment(10)；function(10)；activity(10)；polarization(9)；future(8)；gravity(6)；viability(6)；concentration(6)；activation(5)；investigation(5)；culture(5)；enrichment(5)
- 高频学术动词：provide(6)；identified(4)；analyzed(4)；revealed(3)；demonstrated(3)；compared(3)；indicated(2)；analyze(2)；validated(2)；validate(2)；indicate(1)；presented(1)；achieve(1)；provided(1)；demonstrate(1)
- 高频形容词：cognitive(15)；microglial(11)；treatment(11)；environment(10)；nervous(9)；significant(8)；neurological(7)；neuronal(7)；biological(7)；recent(6)；total(6)；library(6)；various(6)；potential(6)；enrichment(5)
- 高频副词：subsequently(6)；differentially(4)；potentially(4)；additionally(4)；consequently(4)；significantly(3)；effectively(3)；family(3)；statistically(3)；directly(2)；specifically(2)；independently(2)；ultimately(2)；initially(2)；previously(2)
- 高频二词短语：ensmusg forward(11)；rpm system(10)；nervous system(8)；simulated microgravity(7)；cell viability(6)；control group(6)；transcriptome sequencing(6)；micro gravity(5)；gene expression(5)；future research(5)；space environment(4)；immune cells(4)
- 高频三词短语：central nervous system(4)；differentially expressed genes(3)；technology facilitated prolonged(2)；facilitated prolonged habitation(2)；prolonged habitation astronauts(2)；habitation astronauts space(2)；astronauts space environment(2)；cardiovascular cerebrovascular systems(2)；major factor directly(2)；successful completion space(2)；completion space missions(2)；microgravity diminish neuronal(2)
- 被动语态估计：69；`we + 动作动词` 主动句估计：0
- 一般现在时线索：54；一般过去时线索：307；现在完成时线索：8；情态动词线索：27

分章节正文词频：

- 1 Introduction: microgravity(21)；space(15)；microglia(14)；cells(8)；microglial(8)；brain(7)；study(7)；system(7)
- 2 Materials and methods: cells(18)；rpm(10)；system(10)；analysis(8)；cell(7)；sequencing(7)；china(6)；usa(6)
- 3 Results: cells(13)；genes(12)；analysis(11)；ensmusg(11)；forward(11)；reverse(11)；degs(9)；microgravity(8)
- 4 Discussion: microgravity(21)；research(17)；microglia(13)；cognitive(10)；cell(9)；apoptosis(8)；cells(8)；brain(7)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：simulated microgravity, microglia, BV2 cells, M1 polarization, apoptosis, transcriptome sequencing, differentially expressed genes, GO enrichment, KEGG pathway, qPCR validation。

可复用 gap 句式：

- “The current understanding of X is still limited, and additional investigation is required to clarify the mechanisms.”
- “The present study aims to provide an understanding of the molecular process underlying...”
- “This study provides a theoretical foundation for elucidating...”

可复用结果句式：

- “Transcriptome analysis revealed X differentially expressed genes...”
- “The qPCR results validated the expression of ... which were consistent with the RNA-seq result, with the exception of...”
- “These results elucidate the molecular mechanisms of... highlighting gene expression changes and cellular damage.”

可复用限制句式：

- “It should be noted that the data acquired from cytological assays exhibits certain limitations.”
- “More investigations involving in vivo research are warranted.”
- “There exist disparities between simulated microgravity and the authentic space environment.”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Understanding the nuanced interplay between microglial and macrophage cells underscores the complexity of CNS immunity and highlights the critical role of microglia in maintaining CNS homeostasis and responding to pathological conditions.
  可迁移模板：Understanding the nuanced interplay between microglial and macrophage cells underscores the complexity of METHOD immunity and highlights the critical role of microglia in maintaining METHOD homeostasis and responding to pathological conditions.
- 原句：In conclusion, our study suggests that microgravity-induced changes in microglia could affect neuroinflammation and neurodegeneration in the brain, potentially impacting critical cognitive functions such as attention and memory, essential for space missions.
  可迁移模板：In conclusion, our study suggests that microgravity-induced changes in microglia could affect neuroinflammation and neurodegeneration in the brain, potentially impacting critical cognitive functions such as attention and memory, essential for space missions.
#### Gap/转折句
- 原句：However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions.
  可迁移模板：However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions.
- 原句：However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions.
  可迁移模板：However, the neurological and cognitive impairments of astronauts have become major factor that directly impede the successful completion of space missions.
- 原句：However, persistent external stressors can lead to microglial overactivation, escalating the inflammatory response.
  可迁移模板：However, persistent external stressors can lead to microglial overactivation, escalating the inflammatory response.
- 原句：Overall, the current understanding of microglial responses to microgravity is still limited, and additional investigation is required in order to comprehensively clarify the mech anisms that underlie these alterations.
  可迁移模板：Overall, the current understanding of microglial responses to microgravity is still limited, and additional investigation is required in order to comprehensively clarify the mech anisms that underlie these alterations.
#### 方法提出句
- 原句：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
  可迁移模板：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
- 原句：Presently, the rapid advancement of space research and technology has facilitated the prolonged habitation of astronauts in the space environment [1].
  可迁移模板：Presently, the rapid advancement of space research and technology has facilitated the prolonged habitation of astronauts in the space environment [X].
- 原句：The present study aims to provide an understanding of the molecular process underlying the behavior of microglia under conditions of microgravity.
  可迁移模板：The present study aims to provide an understanding of the molecular process underlying the behavior of microglia under conditions of microgravity.
- 原句：In this study, BV2 cells, representative of microglia, were cultivated in a Random Positioning Machine (RPM) system, specifically a 3D-clinostat to simulate microgravity.
  可迁移模板：In this study, BV2 cells, representative of microglia, were cultivated in a Random Positioning Machine (METHOD) system, specifically a METHOD-clinostat to simulate microgravity.
#### 结果呈现句
- 原句：These results elucidate the molecular mechanisms of microglial behavior under microgravity, highlighting gene expression changes and cellular damage.
  可迁移模板：These results elucidate the molecular mechanisms of microglial behavior under microgravity, highlighting gene expression changes and cellular damage.
- 原句：These results elucidate the molecular mechanisms of microglial behavior under microgravity, highlighting gene expression changes and cellular damage.
  可迁移模板：These results elucidate the molecular mechanisms of microglial behavior under microgravity, highlighting gene expression changes and cellular damage.
- 原句：Studies have demonstrated that microgravity can diminish neuronal function and cognitive abilities by altering the microenvironment of the brain (BME) [11,12].
  可迁移模板：Studies have demonstrated that microgravity can diminish neuronal function and cognitive abilities by altering the microenvironment of the brain (METHOD) [X,X].
- 原句：Another study indicated that unloading the hind limbs of mice can result in decreased gene expression alterations in the gray and white matter of the spinal cord of mice, as well as phenotypic changes in microglia and astrocytes [20].
  可迁移模板：Another study indicated that unloading the hind limbs of mice can result in decreased gene expression alterations in the gray and white matter of the spinal cord of mice, as well as phenotypic changes in microglia and astrocytes [X].
- 原句：Further research will validate these initial results and explore effective protection strategies.
  可迁移模板：Further research will validate these initial results and explore effective protection strategies.
#### 贡献/增量句
- 原句：The primary objective of this study was to provide an understanding of the molecular processes underlying the behavior of microglia under conditions of microgravity.
  可迁移模板：The primary objective of this study was to provide an understanding of the molecular processes underlying the behavior of microglia under conditions of microgravity.
- 原句：Transcriptome analysis revealed 142 differentially expressed genes related to microglial phenotype and inflammation, with qPCR validating selected DEGs.
  可迁移模板：Transcriptome analysis revealed Xdifferentially expressed genes related to microglial phenotype and inflammation, with qPCR validating selected DEGs.
- 原句：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
  可迁移模板：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
- 原句：The primary objective of this study was to provide an understanding of the molecular processes underlying the behavior of microglia under conditions of microgravity.
  可迁移模板：The primary objective of this study was to provide an understanding of the molecular processes underlying the behavior of microglia under conditions of microgravity.
- 原句：Transcriptome analysis revealed 142 differentially expressed genes related to microglial phenotype and inflammation, with qPCR validating selected DEGs.
  可迁移模板：Transcriptome analysis revealed Xdifferentially expressed genes related to microglial phenotype and inflammation, with qPCR validating selected DEGs.
#### 限制/边界句
- 原句：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
  可迁移模板：This study provides a conceptual framework for comprehending the influence of microgravity on the neurological system, establishing countermeasures against functional damage to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
- 原句：In recent years, it has been discovered that microglia may be the primary factor in microgravity-induced neurological decline.
  可迁移模板：In recent years, it has been discovered that microglia may be the primary factor in microgravity-induced neurological decline.
- 原句：Overall, the current understanding of microglial responses to microgravity is still limited, and additional investigation is required in order to comprehensively clarify the mech anisms that underlie these alterations.
  可迁移模板：Overall, the current understanding of microglial responses to microgravity is still limited, and additional investigation is required in order to comprehensively clarify the mech anisms that underlie these alterations.
- 原句：This study provides a theoretical foundation for elucidating the impact of microgravity on the nervous system, establishing countermeasures against functional dam age to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
  可迁移模板：This study provides a theoretical foundation for elucidating the impact of microgravity on the nervous system, establishing countermeasures against functional dam age to the nervous system caused by space flight, and serving as a reference for future deep space exploration and long-term manned space medical support.
- 原句：In order to gain a thorough understanding of the mechanisms in question, it is impera tive to conduct comprehensive and systematic studies, which will serve as the primary focus of future research endeavors.
  可迁移模板：In order to gain a thorough understanding of the mechanisms in question, it is impera tive to conduct comprehensive and systematic studies, which will serve as the primary focus of future research endeavors.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用服务三类功能。第一类是航天医学背景，引用微重力对脑结构、脑血流、认知功能和神经系统影响的研究。第二类是微胶质生物学，引用 M1/M2 极化、脑微环境、神经炎症和神经退行性疾病。第三类是候选基因解释，引用 Il1b、Ptgs2/COX-2、Src、Fos、Arg1、Clec7a 等在微胶质和神经炎症中的作用。

作者对前人研究采取“延伸”态度：已有研究提示微重力可能影响神经系统和微胶质，但还需要更具体分子机制。Discussion 中引用用于把本文 DEGs 放进已知炎症网络，而不是证明每个基因都是新发现。

引用风险在于，部分候选基因功能来自地面神经炎症或疾病模型，迁移到微重力场景仍需实验验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：82
- Introduction 引文簇数量估计：16
- References 条目数：49
- 可识别年份条目数：50
- 2021 年及以后文献数：14
- 2010 年前经典文献数：7
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Acta Astronautica(1)
- 引文簇样例：[9], [10], [1], [2,3], [11,12], [13], [4], [5,6], [7,8], [14], [15], [16]

带引文的 gap/转折句样例：

- Upon detecting external stimuli such as pressure, dam age, hypoxia, ischemia, infection, and oxidative stress, microglia pri marily regulate the BME through shifts in the M1 (pro-inflammatory) and M2 (anti-inflammatory) phenotypes [15].
- Another study indicated that unloading the hind limbs of mice can result in decreased gene expression alterations in the gray and white matter of the spinal cord of mice, as well as phenotypic changes in microglia and astrocytes [20].

References 解析样例（前 8 条）：

- [1] R.S. Krishnamurthy, J. Hatton, Space science and technologies to advance healthrelated sustainable development goals, Bull. World Health Organ. 96 (2018), 3-3a.
- [2] L.A. Kramer, K.M. Hasan, M.B. Stenger, A. Sargsyan, S.S. Laurie, C. Otto, R. J. Ploutz-Snyder, K. Marshall-Goebel, R.F. Riascos, B.R. Macias, Intracranial effects of microgravity: a prospective longitudinal MRI study, Radiology 295 (2020) 640–648.
- [3] E. Pechenkova, I. Nosikova, A. Rumshiskaya, L. Litvinova, I. Rukavishnikov, E. Mershina, V. Sinitsyn, A. Van Ombergen, B. Jeurissen, S. Jillings, S. Laureys, J. Sijbers, A. Grishin, L. Chernikova, I. Naumov, L. Kornilova, F.L. Wuyts, E. Tomilovskaya, I. Kozlovskaya, Alterations of functional brain connectivity after long-duration spaceflight as revealed by fMRI, Front. Physiol. 10 (2019).
- [4] A.R. Hargens, D.E. Watenpaugh, Cardiovascular adaptation to spaceflight, Med. Sci. Sports Exerc. 28 (1996) 977–982.
- [5] B. Yulug, G. Erkol, E. Kilic, An interesting link between microgravity and psychiatric diseases, J. Neuropsychiatry Clin. Neurosci. 22 (2010) E12. E12.
- [6] H.S. Cooper Jr., The loneliness of the long-duration astronaut, Air Space 11 (1996) 37–45.
- [7] T. Mano, N. Nishimura, S. Iwase, Sympathetic neural influence on bone metabolism in microgravity (Review), Acta Physiol. Hung. 97 (2010) 354–361.
- [8] M. Zayzafoon, V.E. Meyers, J.M. McDonald, Microgravity: the immune response and bone, Immunol. Rev. 208 (2005) 267–280.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 模拟微重力有效性风险：RPM 可能引入剪切、流体扰动和培养条件差异，不等同真实空间微重力。
2. 细胞模型风险：BV2 为永生化细胞系，与 primary microglia 和体内微胶质存在差异。
3. 时间维度不足：24 h 单一时间点无法区分短期应激、适应性恢复和长期损伤。
4. M1/M2 简化风险：微胶质极化谱系复杂，仅用 CD80/CD86 概括 M1 可能过度简化。
5. 凋亡解释风险：Annexin V/PI 晚期凋亡/坏死区间需要谨慎，不宜直接等同单一凋亡机制。
6. RNA-seq 因果风险：DEGs 和富集通路只是相关证据，缺少基因敲降/抑制剂/救援实验。
7. 样本和统计风险：文本未充分展示生物学重复、批次效应和多重检验细节。
8. 外推风险：从 BV2 细胞到宇航员认知功能之间跨度很大，作者虽谨慎但仍需后续 in vivo 支撑。

## 17. 可复用资产

- 选题资产：从航天任务风险切入，落到可实验的细胞机制问题。
- 证据链资产：细胞活性/形态、流式极化、凋亡、RNA-seq、GO/KEGG、qPCR 多层证据递进。
- 图表资产：装置+细胞图、流式图、凋亡图、火山图、热图、富集图、qPCR 验证图。
- 写作资产：跨尺度外推时使用 “suggest”“potentially”“may” 控制 claim 强度。
- 限制资产：主动写出 cytological assays、in vivo、single-cell sequencing、真实空间环境差异，能降低审稿风险。
- 机制资产：用 Il1b/Ptgs2/Src/Fos 上调和 Arg1/Clec7a 下调构建炎症-凋亡解释框架。

## 18. 对我写论文的启发

这篇论文最值得学习的是“表型结果和组学结果的配对”。如果只有 RNA-seq，读者会问生物学意义；如果只有细胞活性和凋亡，读者会问机制。本文用两者互相支撑，形成探索性机制论文的基本闭环。

第二个启发是，跨尺度外推必须谨慎。作者从 BV2 细胞推到神经炎症和认知功能时使用情态表达，并在 limitations 中明确需要体内和真实空间验证，这种写法比直接夸大更容易被接受。

第三个启发是，候选基因讨论要有选择。作者没有逐个解释 142 个 DEGs，而是挑 Il1b、Ptgs2、Src、Fos、Arg1、Clec7a 等与微胶质功能最相关的基因深入讨论，避免结果扩散。

## 19. 最终浓缩

这篇论文用 RPM 模拟微重力处理 BV2 微胶质细胞，发现细胞活性下降、M1 极化增强、晚期凋亡增加，并通过 RNA-seq 识别 142 个 DEGs，将其富集到炎症、凋亡、IL-17、NF-kappa B 和 TNF 等通路。它的贡献是为“微重力如何通过微胶质影响神经炎症和认知风险”提供一组细胞层面的候选机制。

最大风险是模型仍停留在体外模拟和相关性组学层面，真实空间环境、体内脑微环境和因果机制都需要后续验证。

可迁移到自己论文中的三件事：第一，表型实验和组学分析要互相配套；第二，跨尺度结论要用谨慎语气并写清限制；第三，组学结果要收束到少数关键通路和候选基因，而不是堆完整列表。
