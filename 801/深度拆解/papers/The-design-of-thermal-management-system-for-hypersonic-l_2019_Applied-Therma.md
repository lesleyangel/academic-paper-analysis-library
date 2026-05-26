# The design of thermal management system for hypersonic launch vehicles based on active cooling networks

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.txt` 的全文抽取，并参考 `801/文本/metadata/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.json` 的目录与期刊信息。由于 txt 来自双栏 PDF，存在公式缺符号、图表说明与正文串栏、表格数值分列不完整等问题。涉及车辆外形、温度/热流分布图、TPS 分区图、主动冷却网络示意与 Fig. 17 曲线判读处均标注“需要 PDF 图像复核”。本文重点拆解学术说服机制：为什么 passive TPS 和 active cooling network 不能分开设计，等效热平衡模型如何构成 coupled design 的核心。

## 1. 基本信息与论文身份

- 题名：The design of thermal management system for hypersonic launch vehicles based on active cooling networks。
- 作者：Jian-Jun Gou, Yue Chang, Zheng-Wei Yan, Bing Chen, Chun-Lin Gong。
- 期刊与年份：Applied Thermal Engineering, 159, 2019, Article 113938。
- DOI：10.1016/j.applthermaleng.2019.113938。
- 关键词：Thermal management system；Hypersonic launch vehicle；Active cooling；TPS design。
- 论文类型：高超声速可重复使用运载器热管理系统设计方法论文，含工程算例和参数影响分析。
- 研究对象：由被动热防护系统 TPS 与以煤油为冷却剂的主动冷却网络 ACN 共同构成的热管理系统。
- 核心方法：等效热平衡模型；等效热传递系数 heq；气动热计算、TPS 概念分布与尺度、ACN 容量与冷却剂质量流量的迭代设计。
- 主要证据：30 m 级可重复使用运载器典型轨迹；heq=0-30 W/(m2 K) 和 Tb=330/367/440 K 的参数扫描；壁温、气动热、TPS 重量、ACN 容量和质量流量曲线。
- 目标读者：高超声速热防护设计、主动冷却、再生冷却、飞行器总体热管理研究者。

这篇文章是 Gou/Gong 团队热管理路线中的早期系统设计论文。它的定位是把主动冷却从“局部冷却结构”提升到“全飞行器热管理设计参数”。它不是做某个冷却通道 CFD 细节，而是提出一个设计级等效参数 heq，让气动加热、被动 TPS 和主动冷却容量进入同一个迭代流程。

## 2. 摘要与核心信息提取

一句话主张：高超声速可重复使用运载器的 TMS 应将 passive TPS 与 ACN 耦合设计，而不是分别保守设计；通过等效热平衡模型和等效 HTC，可以把主动冷却容量纳入气动热与 TPS 设计，并得到 TPS 重量与冷却剂质量流量之间的定量权衡。

摘要的结构非常工程化：先提出 TMS 由 passive TPS 和 ACN 组成；再指出 previous studies 常常 separately design，导致 over-conservative；随后介绍 coupled design process，包括 aerodynamic heat calculation、passive TPS concept distribution、TPS and ACN scales、iterative design；再给出两个关键：equivalent thermal equilibrium model 和 equivalent heat transfer coefficient；最后用典型轨迹下可重复使用运载器算例说明 heq 对 aerodynamic heating、passive TPS 和 ACN 的影响。

摘要中的核心结果是方向性关系：随着主动冷却增强，passive TPS weight decreases，而 coolant mass flow rate increases。这不是单纯的性能提升，而是设计权衡：减少结构热防护重量需要付出更高冷却容量和燃料流量代价。

本文最值得抓住的核心不是“主动冷却有效”，而是“heq 把全局热管理能力变成可扫参、可约束、可画设计区间的总体参数”。这让原本复杂的局部冷却通道、壁温、热流、TPS 厚度和燃料流量被压缩成一套可用于早期设计的路线图。

## 3. 选题层深拆

选题来源是高超声速可重复使用运载器的热管理困境。飞行速度高导致气动加热严重，文中提及高于 1800 K 量级的严酷热环境；可重复使用要求不能像烧蚀防热那样靠材料消耗完成保护；大面积被动 TPS 又会带来尺寸和重量不可接受的问题。因此，TMS 不仅要“挡热”，还要管理热量的传递、散出和可能的再利用。

作者把大问题收束到一个具体设计问题：对于给定外形和典型轨迹，如何同时确定被动 TPS 的概念分布/重量和 ACN 的冷却容量/质量流量。这个问题比“研究主动冷却”更具体，因为它明确了输出变量：壁温、TPS 概念、TPS 尺度、ACN 容量、冷却剂质量流量。

选题价值有三层。工程层面，它为 30 m 级可重复使用运载器提供初步 TMS 设计流程。方法层面，它用 heq 将局部冷却能力等效成全局热平衡参数，使 TPS 和 ACN 能在同一模型中迭代。写作层面，它把“分开设计会保守”作为主 gap，并通过重量-流量曲线说明 coupled design 的必要性。

这类选题对 Applied Thermal Engineering 很合适：它不是追求基础热物理新机理，而是把热传递模型、工程简化和系统级设计结合起来，服务高热流装备设计。

## 4. 领域位置与文献版图

Introduction 的文献组织按热防护技术路线展开。第一类是 passive TPS，包括 NASA Space Shuttle 工程中发展的 flexible ceramic blankets、rigid ceramic tiles 和 metallic panels。作者承认这些概念成熟，但指出被动防热主要依靠表面辐射和材料内能增加，效率相对低，高超声速大面积应用会导致重量问题。

第二类是 active TPS，如 ablative TPS、heat-pipe-cooled TPS、film cooling TPS、coolant convection TPS。作者对每一类都做“可解决什么、为何不适合本文”的评价：烧蚀不适合可重复使用；热管能转移高温区热量但最终仍需散热措施，不适合大面积表面；气膜冷却需要额外冷却剂消耗；冷却剂对流/再生冷却可把热量带走并用燃料吸热，最适合从全飞行器角度发展 TMS。

第三类是 coolant convection cooling / regenerative cooling 的具体应用，主要集中在燃烧室、喷管、scramjet 或局部结构。作者的站位是：已有研究大多围绕 specific structures，尚缺少从 whole vehicle point of view 设计 TMS 的方法。这一句“from the point view of the whole vehicle”构成了本文的文献缺口。

本文位于传统 TPS 设计与主动冷却结构研究之间。它不替代局部通道设计，而是为总体阶段给出“主动冷却容量应该多大、被动 TPS 因此如何减重”的设计级方法。

## 5. Gap 制造机制

文章的 gap 制造很直接：以往 passive TPS 和 ACN always designed separately，导致 over-conservative results，偏离 real engineering conditions。这个 gap 不强调“没人研究主动冷却”，而强调“研究对象分割导致系统级设计不真实”。

具体 gap 有三类。第一是耦合 gap：真实热传递中气动热、壁温、传入 TPS 的热流、被动 TPS 厚度和主动冷却容量相互影响；分开设计会把 qin 简化为 0 或把冷却能力视作后处理。第二是参数 gap：ACN 的局部换热系数 hl 随区域而变，不能直接作为全车设计参数；需要等效 heq 表示整体主动冷却能力。第三是设计流程 gap：缺少从气动热计算到 TPS 概念分布、ACN 容量、再到迭代收敛的清晰流程。

这个 gap 的说服力较强，因为作者在模型部分马上解释了为什么 qin 不能忽略、为什么 hl 不适合直接输入设计、为什么需要 heq。审稿风险在于 heq 本身是强简化参数，能否代表真实复杂冷却网络的局部分布和通道约束，需要后续更细模型验证。

## 6. 创新性判断

作者声明的创新主要包括：提出由 passive TPS 和 ACN 构成的 TMS；基于等效热平衡模型发展 TPS-ACN 耦合设计方法；提出等效 HTC 表示 ACN 整体能力；将方法用于高超声速运载器典型轨迹并分析 heq 对系统设计的影响。

真实创新属于“系统设计框架 + 等效参数创新”。公式本身并非复杂新理论，核心在于设计抽象：把冷却通道从底部真实位置等效到近壁热平衡中，用 qin = heq(Tw - Tc) 将冷却能力带入气动热计算和 TPS 尺度设计。这个参数化使得系统级 trade-off 可以被扫参和画图。

创新强度：中等偏强。对于基础传热理论读者，创新可能显得工程简化；对于飞行器 TMS 设计读者，heq 作为早期设计参数很实用。文章的贡献主要不在精细 CFD 或新型材料，而在把“被动防热-主动冷却”的相互作用从后处理关系变成正向耦合设计关系。

可能被挑战的是：heq 的物理唯一性和可实现性。不同 ACN 拓扑可能具有相同 heq，但实际泵功、压降、温升、通道布置和可靠性完全不同。本文承认它是 preliminary design 参数，而不是最终通道设计模型。

## 7. 论证链条复原

全文论证链如下：

1. 高超声速可重复使用运载器气动加热严酷，纯被动 TPS 会带来重量/尺度压力。
2. 主动冷却网络可把热量带走，冷却剂为煤油时还可服务再生冷却，因此适合全飞行器 TMS。
3. 传统研究多关注局部结构，且 passive TPS 与 ACN 分开设计，忽略实际热传递耦合。
4. 真实热平衡中，气动热、辐射、传入 TPS 的热流 qin 和 ACN 取热能力相互影响。
5. 用等效热平衡模型和等效 HTC heq 将 ACN 容量引入气动热计算，使 qin 与 Tw、Tc 相连。
6. 在给定车辆和轨迹上计算热环境、确定 TPS 概念分布和尺度，再由 qin 推导 ACN 容量和冷却剂质量流量。
7. 通过 heq 与 Tb 参数扫描展示设计权衡：heq 越大，壁温降低、被 ACN 带走热量增加、TPS 减重，但所需冷却流量/容量增加。
8. 给出 Fig. 17 等设计曲线，可在总体约束下选择 ACN 能力区间。

这条链很闭合，尤其是从 Eq. (1) 到 Eq. (3) 的转折：从被动热平衡 `qaero = radiation + qin` 转到主动冷却等效取热 `qin = heq(Tw - Tc)`，将 gap 直接落到模型。

## 8. 方法/理论/模型细拆

方法分为五步。第一，定义车辆外形和典型轨迹：约 30 m 长、翼展 15 m，飞行速度从 0 到 Mach 8，最高高度约 60 km，轨迹分为 Ascent 和 Return。第二，计算气动热：基于工程算法，低 Mach 区段用插值，边界层外采用理想气体/等熵关系，边界层内采用 reference temperature 方法。第三，建立等效热平衡模型：表面满足气动对流输入、辐射散出和传入 TPS/ACN 的热通量平衡。

第四，确定 TPS 概念分布与尺度。作者使用 Space Shuttle/NASA 体系中典型 TPS 概念，依据最高壁温选择概念，依据冷侧温度 Tb 和传热约束确定厚度/重量。第五，设计 ACN 容量。通过 qin 与面积得到热量，再用 `qin * A = mf * c * ΔT` 估算冷却剂质量流量与温升乘积。冷却剂为 Chinese No. 3 kerosene / RP-3，热容假定为常数 2100 J/(kg K)。

方法的关键假设包括：heq 可作为全车主动冷却能力的等效设计参数；Tc 在初步设计中可取保守值 280 K；材料/表面发射率可按文献/概念库给定；轨迹与车辆尺度固定；冷却网络可按并联或等效形式初步估算，而不是先详细布置所有通道。

这个方法适合 early-stage design，不适合直接作为 final ACN design。它的优势是能快速得到系统级权衡；弱点是局部通道流动、压降、泵功、燃料热裂解、非均匀管路、结构集成等尚未充分进入。

## 9. 证据系统与 Claim-Evidence 表

证据系统由参数扫描和工程算例构成。作者不是用实验验证，而是用给定飞行器、典型轨迹、热计算算法和 TPS 概念库，展示 heq 对热流、壁温、TPS 分区、TPS 重量和 ACN 质量流量的系统影响。强证据来自趋势一致性和量化曲线，弱点是缺乏高保真 CFD/实验闭环验证。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| passive TPS 与 ACN 分开设计会过于保守，需耦合设计 | 摘要、Introduction、Methodology | 真实变量如 qaero、Tw、qin、TPS weight、mf 相互影响；提出等效热平衡模型 | 机理推导与设计逻辑 | 中强 | 缺少与“分开设计”方案的完整数值对比 |
| 等效 HTC heq 可作为 ACN 整体能力参数 | Section 3.1、Eq. (3)-(4) | qin = heq(Tw - Tc)，并可换算局部 hl | 模型定义 | 中强 | heq 与真实复杂网络之间非唯一 |
| heq 增大时壁温降低、ACN 带走热量比例提高 | Results thermal conditions | Fig. 6-11 显示壁温、气动热、主动带走热沿中线变化；风/背风线带走比例随 heq 增加 | 参数扫描 | 强 | 云图和曲线细节需要 PDF 图像复核 |
| heq 增大可降低 TPS 重量 | Results passive TPS、Conclusions | heq 从 0 到 30 W/(m2 K) 时，Tb=330 K 下 TPS weight 减少 40.0%，Tb=440 K 下减少 14.1% | 设计计算 | 强 | TPS 概念库和厚度算法需 PDF 表格复核 |
| heq 增大导致 ACN 容量和冷却剂质量流量需求上升 | Results ACN、Fig. 15-17 | head network 容量从 9.4 到 2565 kg K/s，全车从 30.6 到 7945 kg K/s；质量流量随 ΔT 和 heq 变化 | 公式估算与曲线 | 强 | 真实泵功/压降未纳入 |
| Fig. 17 可作为总体设计约束查图 | Section 4.5 | 若 TPS weight 小于 3.5 tons，可在图中寻找 heq 设计区间 | 设计图谱 | 中强 | 只适用于本文车辆/轨迹/材料假设 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 车辆与轨迹定义 | 算例具有完整飞行任务背景 | 30 m 级运载器，Mach 与高度随时间变化 | 需要 PDF 图像复核 |
| Eq. (1) | 表面热平衡基础式 | 气动热、辐射和传入 TPS 热流耦合 | qaero 与 Tw、qin 相连 | 公式符号需 PDF 复核 |
| Fig. 2 / Eq. (2)-(4) | 真实 ACN 与等效 ACN 模型 | heq 作为整体冷却能力参数 | 将底部冷却通道等效到表面取热关系 | 需要 PDF 图像复核 |
| Fig. 4 | TMS 设计流程 | 方法是迭代流程而非单步计算 | 气动热 -> TPS 分布/尺度 -> ACN 尺度 -> 迭代 | 需要 PDF 图像复核 |
| Fig. 6-Fig. 8 | 最高壁温与瞬态壁温 | 主动冷却改变热环境 | heq 增大降低壁温 | 云图/曲线需 PDF 复核 |
| Fig. 9-Fig. 11 | 热流、主动取热和 local HTC | ACN 带走热量随 heq 增加 | 风/背风线被取走热量比例上升 | 需要 PDF 图像复核 |
| Fig. 12-Fig. 13/Table 3 | 表面分区与 TPS 概念分布 | 从热环境落到结构/材料选择 | 不同区域采用不同 TPS 概念 | 需要 PDF 图像复核 |
| Table 4/Fig. 15 | TPS 重量和 ACN 容量 | heq 增大使 TPS 减重但 ACN 负担加大 | Tb=330 K 减重更明显 | 表格需 PDF 复核 |
| Fig. 16 | 冷却剂质量流量-温升关系 | ACN 设计需考虑 ΔT 限制 | ΔT 越大所需 mf 越小；全车流量可能过高 | 需要 PDF 图像复核 |
| Fig. 17 | TPS weight 与 mf 的总体权衡 | 可用于设计区间选择 | TPS 重量约束与流量约束可在同图判断 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：Introduction；The vehicle and its trajectory；Methodology of TMS design；Results and discussions；Conclusions。Methodology 下分 Equivalent thermal equilibrium model and HTC、Calculation of aerodynamic heat、Process of TMS design、TPS concept database。Results 下分 Thermal conditions、Heat transferred by active cooling、Passive TPS、Active cooling network、Influence of equivalent HTC。

文章结构是典型工程设计论文：先讲为什么需要系统设计，再固定设计对象和轨迹，然后给模型和流程，最后按变量类别报告结果。它没有单独的“model validation”大章节，验证主要来自文献热流对比和设计趋势合理性；这与后续更高保真论文相比是一个弱点。

标题命名非常功能化，例如 “Thermal conditions”“Passive TPS”“Active cooling network”。每个结果小节对应一个设计输出，使读者能沿“热环境 -> 防热重量 -> 冷却容量 -> 综合 heq 影响”顺序理解。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：8
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3 Methodology of TMS design | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Equivalent thermal equilibrium model and HTC | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 440 K in this work, respectively, while the coking of autoxidation re-     leading edge, such an engineering-based method may have lower ac- | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Calculation of aerodynamic heat | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 1366 K for SA-HC and SA-HC2, 1478 K for TABI and AMHC, 1644 K for | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Heat transferred by active cooling | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.3 Passive TPS | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4.4 Active cooling network | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段快速抬高工程背景：高飞行速度带来 severe aerodynamic heating，TMS 需要管理 transfer、dissipation 甚至 reuse。随后按 passive TPS 和 active TPS 路线展开文献，段落节奏是“技术可行性 -> 局限性 -> 本文选择 convection cooling”。最后一段制造 whole-vehicle gap 并提出 heq。

方法段落以公式驱动：先给原始热平衡，再指出 qin=0 的传统简化不够；接着引入真实 ACN 位于 TPS 底部的关系；然后提出等效模型和 heq。这个节奏很清楚，读者能看到每一步简化的原因。

结果段落主要使用“Fig. X shows / from Fig. X one can find that”的图表驱动写法。它先报告 heq 对壁温、热流、TPS weight、ACN capacity 的影响，再在 4.5 把这些影响综合成设计曲线。结论段不是泛泛总结，而是按编号列出可用于设计的定量规律。

## 13. 文笔画像与语言习惯

文笔是 Applied Thermal Engineering 常见的工程设计语气：名词密集、变量明确、结论直接。高频词包括 thermal management system、passive TPS、active cooling network、equivalent HTC、aerodynamic heat、wall temperature、coolant mass flow rate、cold side temperature。

作者常用 “in this work” 限定范围，用 “from the point view of” 表示设计视角，用 “it can be found that” 引出图表趋势。语气不追求修辞，强调设计参数和工程后果。主动语态多用于提出模型，如 “we proposed an equivalent HTC”；被动语态多用于设计过程，如 “is adopted”“is calculated”“is determined”。

claim 控制相对稳健，很多地方说明“preliminary design”“real engineering design provides constraints”。但对 heq 的有效性表述较强，若写自己的论文，最好进一步补充 heq 与实际冷却通道 CFD 或实验之间的桥接验证。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：tps(117)；heat(110)；temperature(108)；cooling(75)；thermal(69)；vehicle(68)；acn(66)；aerodynamic(54)；design(50)；coolant(50)；active(48)；passive(41)；work(41)；respectively(41)；flow(41)；equivalent(40)；system(39)；surface(37)；heq(37)；htc(35)
- 高频学术名词：temperature(108)；system(39)；capacity(23)；protection(20)；results(19)；analysis(18)；method(16)；structure(16)；distribution(16)；scale(14)；conditions(13)；influence(13)；model(12)；condition(12)；calculation(11)；parameters(9)
- 高频学术动词：shown(30)；shows(18)；developed(13)；indicate(9)；show(5)；proposed(5)；evaluated(3)；indicates(3)；compared(1)；reveal(1)；develop(1)；simulate(1)
- 高频形容词：thermal(69)；aerodynamic(54)；coolant(50)；active(48)；passive(41)；equivalent(40)；local(16)；hypersonic(15)；boundary(15)；regenerative(13)；specific(13)；numerical(12)；metallic(12)；coefficient(9)；ceramic(9)；different(9)
- 高频副词/连接副词：respectively(41)；however(12)；finally(8)；therefore(5)；mainly(4)；especially(3)；widely(2)；directly(2)；similarly(2)；tively(2)；closely(2)；averagely(2)；spectively(2)；separately(1)；obviously(1)；purely(1)
- 高频二词短语：active cooling(38)；aerodynamic heat(35)；passive tps(34)；flow rate(30)；equivalent htc(26)；mass flow(26)；heat flux(24)；thermal protection(20)；tps acn(17)；wall temperature(17)；temperature rise(17)；leading edge(17)；applied thermal(15)；thermal engineering(15)；heat transfer(15)；whole vehicle(15)
- 高频三词短语：mass flow rate(26)；applied thermal engineering(15)；gou applied thermal(13)；coolant mass flow(11)；appl therm eng(10)；passive tps acn(9)；aerodynamic heat flux(9)；thermal protection system(8)；cold side temperature(8)；aerosp sci technol(8)；active cooling network(7)；thermal management system(6)

**主动、被动与句法**

- 被动语态估计次数：168
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：538
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：312
- 一般过去时线索：40
- 现在完成时线索：2
- 情态动词线索：100
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：tps(51)；heat(47)；cooling(34)；thermal(28)；aerodynamic(27)；vehicle(26)；temperature(26)；design(23)
- 440 K in this work, respectively, while the coking of autoxidation re-     leading edge, such an engineering-based method may have lower ac-：tps(4)；tms(3)；acn(3)；passive(3)；occurs(2)；design(2)；vehicle(2)；temperature(2)
- 3.2. Calculation of aerodynamic heat：temperature(31)；tps(16)；concept(13)；heat(12)；based(9)；vehicle(9)；shown(8)；concepts(8)
- 1366 K for SA-HC and SA-HC2, 1478 K for TABI and AMHC, 1644 K for：temperature(49)；heat(48)；tps(46)；acn(36)；cooling(35)；thermal(34)；respectively(32)；vehicle(31)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频概念词：thermal management system、passive thermal protection system、active cooling network、equivalent thermal equilibrium model、equivalent heat transfer coefficient、aerodynamic heat load、coolant mass flow rate、temperature rise、coupled design。

可复用 gap 句式：`In most previous studies, the passive TPS and active cooling network are designed separately, leading to over-conservative results that deviate from real engineering conditions.` 适合写系统耦合设计 gap。

可复用方法句式：`The model and the coefficient act as the rationale and equivalent parameter of the whole process.` 适合说明一个抽象参数如何支撑全流程。

可复用结果句式：`The weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.` 这是典型 trade-off 句。

可复用讨论句式：`Under real design constraints, the curves can be referenced to determine the feasible design zone.` 适合将参数扫描结果转成设计指南。

## 15. 引用策略与文献使用

作者引用策略围绕技术谱系和应用边界展开。先引用高超声速热环境和 TPS 背景文献，建立问题重要性；再引用 NASA/Space Shuttle TPS 概念，说明被动 TPS 概念库来源；随后引用烧蚀、热管、气膜冷却、再生冷却等主动技术，逐类评价为何本文选择 coolant convection。

对前人的评价不是简单否定，而是“局部有效、全车不足”。例如烧蚀适合再入或燃烧室但不适合可重复使用外形；热管适合 leading edge 但不适合大面积；已有再生冷却多用于燃烧室和喷管，缺少 whole vehicle TMS 视角。这种引用策略能避免把 gap 写成虚假空白。

此外，作者引用自己或团队相近车辆/方法文献来支撑车辆外形和计算方法。这在工程设计论文中可接受，但也意味着方法的独立外部验证偏弱。

## 16. 审稿人视角风险

1. 等效参数过强简化：heq 把复杂 ACN 拓扑压成一个全局系数，可能掩盖局部过热、流量分配、压降和泵功问题。
2. 冷却剂模型简化：RP-3 热容取常数，温升和物性变化、热裂解、结焦等真实燃料问题没有深入。
3. 缺少高保真验证：气动热采用工程算法，若没有充分 CFD/实验对照，热环境可能影响后续所有设计结论。
4. TPS 概念库边界：NASA TPS 概念迁移到该运载器是否满足结构、维护、连接和服役寿命要求，需要更多论证。
5. 全车 ACN 可实现性：全车大面积主动冷却可能带来管路复杂性和可靠性风险，文章也提到 real engineering may choose head only。
6. 结果适用范围：Fig. 17 类设计图只对本文车辆、轨迹、Tb 和材料假设成立，不能直接外推。
7. 文本抽取异常：Fig. 6-17 和 Table 1-4 的图表细节需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：用“分开设计导致保守”打开系统耦合设计论文。
- 参数资产：构造一个等效参数，把复杂子系统能力带入总体热平衡。
- 证据资产：用参数扫描展示 trade-off，而不是只展示单一优化解。
- 图表资产：将 TPS weight 和 coolant mass flow rate 放到同一图，形成设计区间图。
- 结构资产：章节按设计输出组织，适合工程读者检索。
- 语言资产：`coupled design rationale`、`equivalent parameter`、`design zone` 这些表达可迁移。

## 18. 对我写论文的启发

如果研究对象是复杂工程系统，最有价值的创新有时不是更精细的局部模型，而是把分散变量压缩成能驱动总体设计的参数。本文 heq 的价值就在这里：它把“主动冷却多强”变成可输入、可扫参、可约束的设计量。

另一点启发是 trade-off 要写透。文章没有把主动冷却包装成单向利好，而是清楚说明 TPS 减重与冷却质量流量增加并存。工程论文越能诚实地写出代价，越像真实设计而不是性能宣传。

第三点启发是 gap 应该来自流程而非名词。本文不是说“缺少 ACN 研究”，而是说“TPS 与 ACN 被分开设计”，这是更强的 gap，因为它直接指向工程决策错误。

## 19. 最终浓缩

这篇论文的核心是把高超声速运载器 TMS 从“被动 TPS + 后置主动冷却”的分离式设计，改写为基于等效热平衡模型和等效 HTC 的耦合设计。heq 是全文的枢纽：它把 ACN 容量引入气动热计算、TPS 尺度和冷却剂流量估算，使设计者能看到 TPS weight 降低与 coolant mass flow rate 增加之间的权衡。最值得学习的是它如何用一个简单等效参数支撑整套工程设计流程；最需要复核的是 heq 与真实冷却网络之间的物理对应、各图表曲线细节和全车 ACN 可实现性。
