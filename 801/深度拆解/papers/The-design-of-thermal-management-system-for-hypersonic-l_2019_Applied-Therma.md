# The design of thermal management system for hypersonic launch vehicles based on active cooling networks

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.txt` 的全文抽取，并参考 `801/文本/metadata/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.json` 的目录与期刊信息。由于 txt 来自双栏 PDF，存在公式缺符号、图表说明与正文串栏、表格数值分列不完整等问题。涉及车辆外形、温度/热流分布图、TPS 分区图、主动冷却网络示意与 Fig. 17 曲线判读处均标注“需要 PDF 图像复核”。本文重点拆解学术说服机制：为什么 passive TPS 和 active cooling network 不能分开设计，等效热平衡模型如何构成 coupled design 的核心。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：Introduction, Results and discussions, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-design-of-thermal-management-system-for-hypersonic-l_2019_Applied-Therma.md`。

中文译文：

> 本文提出了一种高超声速飞行器热管理系统（TMS）的设计方法。该系统由被动热保护系统（TPS）和采用煤油冷却剂的主动冷却网络（ACN）组成。在以往的大多数研究中，被动式TPS和ACN总是分开设计，从而导致结果过于保守，偏离实际工程条件。目前的工作提出了一种耦合设计方法，该方法包括气动热计算、被动TPS概念分布的确定、TPS和ACN尺度的计算以及迭代设计。耦合设计基于两个关键实现，主动冷却通过等效热平衡模型耦合到TPS中的气动加热和传热，主动冷却的总体能力由等效传热系数表示。模型和系数分别作为整个过程的理论依据和等效参数。可重复使用运载火箭的TMS是在典型轨迹下建立的。研究了等效传热系数对气动加热、被动TPS和ACN的影响。结果表明，随着主动冷却的增强，被动TPS的重量减少，而冷却剂质量流量增加。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：However, for the whole vehicle, the mass flow rate will decrease from 30.6 to 0.612 kg/s, 305 to 6.12 kg/s, 608 to 12.15 kg/s, 1499 to 30.0 kg/s, 2926 to 58.5 kg/s, 5560 to 111 kg/s and 7945 to 159 kg/s, when the coolant temperature rise increases from 1 to 50 K for heq = 0.1, 1, 2, 5, 10, 20 and 30 W/(m2·K).
- 本文解决方式：In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed. A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design. The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: Introduction（背景定位/文献缺口）
- L2 p.3: The vehicle and its trajectory（对象/模块/过渡章节）
- L2 p.3: Methodology of TMS design（方法/模型/算法）
  - L3 p.3: Equivalent thermal equilibrium model and HTC（方法/模型/算法）
  - L3 p.4: Calculation of aerodynamic heat（对象/模块/过渡章节）
  - L3 p.4: Process of TMS design（对象/模块/过渡章节）
  - L3 p.6: TPS concept database（对象/模块/过渡章节）
- L2 p.6: Results and discussions（结果/验证/讨论）
  - L3 p.6: Thermal conditions（对象/模块/过渡章节）
  - L3 p.8: Heat transferred by active cooling（对象/模块/过渡章节）
  - L3 p.9: Passive TPS（对象/模块/过渡章节）
  - L3 p.12: Active cooling network（对象/模块/过渡章节）
  - L3 p.13: Influence of equivalent HTC（对象/模块/过渡章节）
- L2 p.13: Conclusions（结论/贡献回收）
- L2 p.13: Acknowledgments（尾部材料）
- L2 p.13: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| Introduction | 1 | 2 | 背景定位/文献缺口 |
| The vehicle and its trajectory | 3 | 2 | 对象/模块/过渡章节 |
| Methodology of TMS design | 3 | 2 | 方法/模型/算法 |
| Equivalent thermal equilibrium model and HTC | 3 | 3 | 方法/模型/算法 |
| Calculation of aerodynamic heat | 4 | 3 | 对象/模块/过渡章节 |
| Process of TMS design | 4 | 3 | 对象/模块/过渡章节 |
| TPS concept database | 6 | 3 | 对象/模块/过渡章节 |
| Results and discussions | 6 | 2 | 结果/验证/讨论 |
| Thermal conditions | 6 | 3 | 对象/模块/过渡章节 |
| Heat transferred by active cooling | 8 | 3 | 对象/模块/过渡章节 |
| Passive TPS | 9 | 3 | 对象/模块/过渡章节 |
| Active cooling network | 12 | 3 | 对象/模块/过渡章节 |
| Influence of equivalent HTC | 13 | 3 | 对象/模块/过渡章节 |
| Conclusions | 13 | 2 | 结论/贡献回收 |
| Acknowledgments | 13 | 2 | 尾部材料 |
| References | 13 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一段快速抬高工程背景：高飞行速度带来 severe aerodynamic heating，TMS 需要管理 transfer、dissipation 甚至 reuse。随后按 passive TPS 和 active TPS 路线展开文献，段落节奏是“技术可行性 -> 局限性 -> 本文选择 convection cooling”。最后一段制造 whole-vehicle gap 并提出 heq。

方法段落以公式驱动：先给原始热平衡，再指出 qin=0 的传统简化不够；接着引入真实 ACN 位于 TPS 底部的关系；然后提出等效模型和 heq。这个节奏很清楚，读者能看到每一步简化的原因。

结果段落主要使用“Fig. X shows / from Fig. X one can find that”的图表驱动写法。它先报告 heq 对壁温、热流、TPS weight、ACN capacity 的影响，再在 4.5 把这些影响综合成设计曲线。结论段不是泛泛总结，而是按编号列出可用于设计的定量规律。

## 13. 文笔画像与语言习惯

文笔是 Applied Thermal Engineering 常见的工程设计语气：名词密集、变量明确、结论直接。高频词包括 thermal management system、passive TPS、active cooling network、equivalent HTC、aerodynamic heat、wall temperature、coolant mass flow rate、cold side temperature。

作者常用 “in this work” 限定范围，用 “from the point view of” 表示设计视角，用 “it can be found that” 引出图表趋势。语气不追求修辞，强调设计参数和工程后果。主动语态多用于提出模型，如 “we proposed an equivalent HTC”；被动语态多用于设计过程，如 “is adopted”“is calculated”“is determined”。

claim 控制相对稳健，很多地方说明“preliminary design”“real engineering design provides constraints”。但对 heq 的有效性表述较强，若写自己的论文，最好进一步补充 heq 与实际冷却通道 CFD 或实验之间的桥接验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：23763
- 高频词：tps(62)；heat(58)；temperature(39)；acn(38)；cooling(32)；aerodynamic(31)；coolant(30)；vehicle(26)；system(25)；heq(23)；active(21)；passive(21)；flow(21)；design(20)；equivalent(20)；fuel(20)；thermal(19)；surface(19)；rate(18)；work(17)
- 高频名词化/学术名词：temperature(39)；protection(7)；capacity(6)；propulsion(6)；high-temperature(5)；distribution(5)；insulation(5)；convection(5)；density(5)；proportion(5)；management(4)；calculation(4)；influence(4)；addition(4)；dissipation(3)
- 高频学术动词：developed(10)；indicate(3)；indicated(1)；develop(1)；analyzed(1)；evaluated(1)；reveal(1)
- 高频形容词：aerodynamic(31)；coolant(30)；active(21)；passive(21)；equivalent(20)；thermal(19)；regenerative(8)；reusable(7)；metallic(7)；coefficient(6)；temporary(6)；efficient(5)；specific(5)；management(4)；ceramic(4)
- 高频副词：especially(3)；mainly(2)；averagely(2)；finally(2)；separately(1)；obviously(1)；purely(1)；widely(1)；similarly(1)；sharply(1)；closely(1)；perfectly(1)；jointly(1)；directly(1)
- 高频二词短语：aerodynamic heat(21)；flow rate(18)；passive tps(17)；active cooling(16)；mass flow(14)；equivalent htc(14)；heat flux(11)；aerodynamic heating(9)；tps acn(9)；fuel tank(9)；regenerative cooling(8)；temperature rise(8)
- 高频三词短语：mass flow rate(14)；cold side temperature(7)；average maximum heq(6)；maximum heq rising(6)；active cooling network(5)；passive tps acn(5)；coolant mass flow(5)；aerodynamic heat flux(5)；regenerative cooling system(5)；coolant temperature rise(5)；thermal management system(4)；thermal protection system(4)
- 被动语态估计：56；`we + 动作动词` 主动句估计：0
- 一般现在时线索：113；一般过去时线索：153；现在完成时线索：0；情态动词线索：36

分章节正文词频：

- Introduction: tps(30)；heat(28)；cooling(21)；aerodynamic(16)；thermal(13)；active(13)；technology(13)；system(12)
- Results and discussions: heat(25)；temperature(24)；tps(22)；acn(22)；fuel(18)；heq(17)；vehicle(16)；surface(15)
- Conclusions: tps(10)；acn(9)；equivalent(7)；temperature(7)；htc(6)；coolant(5)；heat(5)；heq(5)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频概念词：thermal management system、passive thermal protection system、active cooling network、equivalent thermal equilibrium model、equivalent heat transfer coefficient、aerodynamic heat load、coolant mass flow rate、temperature rise、coupled design。

可复用 gap 句式：`In most previous studies, the passive TPS and active cooling network are designed separately, leading to over-conservative results that deviate from real engineering conditions.` 适合写系统耦合设计 gap。

可复用方法句式：`The model and the coefficient act as the rationale and equivalent parameter of the whole process.` 适合说明一个抽象参数如何支撑全流程。

可复用结果句式：`The weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.` 这是典型 trade-off 句。

可复用讨论句式：`Under real design constraints, the curves can be referenced to determine the feasible design zone.` 适合将参数扫描结果转成设计指南。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS).
  可迁移模板：The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than METHOD [X–X]) and brings great challenges for thermal management system (METHOD).
- 原句：The film cooling means a coolant film will be formed on the high-temperature surface to prevent the aerodynamic heating; however, the technology requires additional coolant consumption.
  可迁移模板：The film cooling means a coolant film will be formed on the high-temperature surface to prevent the aerodynamic heating; however, the technology requires additional coolant consumption.
#### Gap/转折句
- 原句：For TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission.
  可迁移模板：For METHOD based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a METHOD is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [X–X]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission.
- 原句：The film cooling means a coolant film will be formed on the high-temperature surface to prevent the aerodynamic heating; however, the technology requires additional coolant consumption.
  可迁移模板：The film cooling means a coolant film will be formed on the high-temperature surface to prevent the aerodynamic heating; however, the technology requires additional coolant consumption.
- 原句：However, most previous In this paper, a design method of thermal management system (TMS) for reusable flight vehicles is developed.
  可迁移模板：However, most previous In this paper, a design method of thermal management system (METHOD) for reusable flight vehicles is developed.
- 原句：However, for the whole vehicle, the mass flow rate will decrease from 30.6 to 0.612 kg/s, 305 to 6.12 kg/s, 608 to 12.15 kg/s, 1499 to 30.0 kg/s, 2926 to 58.5 kg/s, 5560 to 111 kg/s and 7945 to 159 kg/s, when the coolant temperature rise increases from 1 to 50 K for heq = 0.1, 1, 2, 5, 10, 20 and 30 W/(m2·K).
  可迁移模板：However, for the whole vehicle, the mass flow rate will decrease from Xto Xkg/s, Xto Xkg/s, Xto Xkg/s, Xto Xkg/s, Xto Xkg/s, Xto Xkg/s and Xto Xkg/s, when the coolant temperature rise increases from Xto METHOD for heq = X, X, X, X, X, Xand METHOD/(m2·K).
#### 方法提出句
- 原句：In this paper, a design method of thermal management system (TMS) for hypersonic vehicles is developed.
  可迁移模板：In this paper, a design method of thermal management system (METHOD) for hypersonic vehicles is developed.
- 原句：A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive TPS concept distribution, computation of TPS and ACN scales, and iterative design.
  可迁移模板：A coupled design method is developed in present work, and the process includes calculation of aerodynamic heat, determination of passive METHOD concept distribution, computation of METHOD and METHOD scales, and iterative design.
- 原句：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
  可迁移模板：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in METHOD by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
- 原句：The model and the coefficient act as the rationale and the equivalent parameter of the whole process, respectively.
  可迁移模板：The model and the coefficient act as the rationale and the equivalent parameter of the whole process, respectively.
- 原句：In this work, the TPS concepts are mainly those developed in Space Shuttle engineering by NASA [4], which consists of three types, i.e., flexible ceramic blankets ⁎ Corresponding author.
  可迁移模板：In this work, the METHOD concepts are mainly those developed in Space Shuttle engineering by METHOD [X], which consists of three types, i.e., flexible ceramic blankets ⁎ Corresponding author.
#### 结果呈现句
- 原句：In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
  可迁移模板：In most previous studies, the passive METHOD and METHOD are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
- 原句：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
  可迁移模板：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in METHOD by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
- 原句：The results show that the weight of passive TPS decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
  可迁移模板：The results show that the weight of passive METHOD decreases, while the coolant mass flow rate increases with the enhancement of active cooling.
- 原句：In most previous studies, the passive TPS and ACN are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
  可迁移模板：In most previous studies, the passive METHOD and METHOD are always designed separately and thus leads to over-conservative results that deviating from real engineering conditions.
- 原句：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in TPS by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
  可迁移模板：The coupled design is realized based on two keys, the active cooling is coupled in aerodynamic heating and heat transfer in METHOD by an equivalent thermal equilibrium model, and the overall capacity of active cooling is indicated by an equivalent heat transfer coefficient.
#### 贡献/增量句
- 原句：The TMS of a reusable launch vehicle is established under a typical trajectory.
  可迁移模板：The METHOD of a reusable launch vehicle is established under a typical trajectory.
- 原句：The TMS of a reusable launch vehicle is established under a typical trajectory.
  可迁移模板：The METHOD of a reusable launch vehicle is established under a typical trajectory.
#### 限制/边界句
- 原句：The well designed TMS should be able to manage the transfer process, and control the dissipation and even the reuse of aerodynamic heat in an efficient way.
  可迁移模板：The well designed METHOD should be able to manage the transfer process, and control the dissipation and even the reuse of aerodynamic heat in an efficient way.
- 原句：The design key for such a TPS is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulation layer).
  可迁移模板：The design key for such a METHOD is to obtain optimum distribution of concepts (allowable temperature should be higher than the aerodynamic heated wall temperature) and scales (size and weight) of concept (larger heat load needs larger thickness of insulation layer).
- 原句：Sometimes, especially for hypersonic vehicles, the size and the weight of such a purely passive TPS could be unacceptable.
  可迁移模板：Sometimes, especially for hypersonic vehicles, the size and the weight of such a purely passive METHOD could be unacceptable.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

作者引用策略围绕技术谱系和应用边界展开。先引用高超声速热环境和 TPS 背景文献，建立问题重要性；再引用 NASA/Space Shuttle TPS 概念，说明被动 TPS 概念库来源；随后引用烧蚀、热管、气膜冷却、再生冷却等主动技术，逐类评价为何本文选择 coolant convection。

对前人的评价不是简单否定，而是“局部有效、全车不足”。例如烧蚀适合再入或燃烧室但不适合可重复使用外形；热管适合 leading edge 但不适合大面积；已有再生冷却多用于燃烧室和喷管，缺少 whole vehicle TMS 视角。这种引用策略能避免把 gap 写成虚假空白。

此外，作者引用自己或团队相近车辆/方法文献来支撑车辆外形和计算方法。这在工程设计论文中可接受，但也意味着方法的独立外部验证偏弱。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：75
- Introduction 引文簇数量估计：13
- References 条目数：45
- 可识别年份条目数：50
- 2021 年及以后文献数：0
- 2010 年前经典文献数：15
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Applied Thermal Engineering(1)
- 引文簇样例：[4], [19], [5,6], [7], [11,12], [20,21], [22], [14], [23], [17,18], [24], [25]

带引文的 gap/转折句样例：

- The high flight speed of hypersonic aerospace vehicles leads to severe aerodynamic heating (e.g., higher than 1800 K [1–3]) and brings great challenges for thermal management system (TMS).
- For TPS based on ablative technology, part of the aerodynamic heat will be dissipated by the ablation of relevant materials; such a TPS is widely used in external thermal protection of reentry vehicles and also rocket combustion chambers [13–16]; however, it is not appropriate to reusable vehicles due to its changing configuration during the flight mission.
- The heat pipe can transfer aerodynamic heat from high-temperature region to low-temperature region in a short time; it is popular in thermal protection of critical components like vehicle leading edges [17,18]; however, the heat pipe only transfers heat from dangerous region to safety region, and the final heat dissipation has to resort to surface radiation or other additional measures, thus such heat-pipe-cooled thermal protection technology is not suitable for surfaces of large area.

References 解析样例（前 8 条）：

- 5. Conclusions
In this paper, a design method of thermal management system (TMS) for reusable flight vehicles is developed. The system consists of a passive thermal protection system (TPS) and an active cooling network (ACN) with kerosene as coolant. Based on an equivalent heat equilibrium model, the TPS and ACN are designed in a coupled way. A parameter equivalent HTC, heq, is proposed to indicate the capacity of active cooling. The design process includes four steps, the calculation of aerodynamic heat, the determination of TPS concept distribution, the calculation of scales of TPS and ACN, and the final design of TMS after several iterations. A reusable launch vehicle of 30 m long with a certain trajectory is studied in this work. The influence of equivalent HTC
(heq = 0–30 W/(m2 K)) and cold side temperature (Tb = 330, 367 and 440 K) on aerodynamic heat, TPS and ACN are studied. The results show some useful conclusions:
(1) The aerodynamic heat flux and the proportion of heat taken by ACN increase, while the wall temperature decreases with the rise of equivalent HTC. (2) The higher equivalent HTC will result in lighter TPS while higher product of coolant mass flow rate and coolant temperature rise for ACN. (3) Increasing the constrained cold side temperature is very useful for the weight reduction of passive TPS, and it is more efficient with small equivalent HTC. The weight of TPS is reduced by 30.1%, 16.9%, 8.5%, 7.3%, 0.9%, 0% and 0% with Tb increasing from 330 to 440 K, for heq = 0, 0.1, 1, 2, 5, 10, 20, and 30 W/(m2·K), respectively. (4) The ACN can reduce the TPS weight, and it is more efficient with low cold side temperature. The weight of passive TPS is reduced by 40.0% and 14.1% with the equivalent HTC increases from 0 to 30 W/(m2·K) for Tb = 330 and Tb = 440, respectively. (5) The method proposed in this work can be used to design ACN for the whole vehicle, as well as specific regions like the head of fuselage. For ACN of the vehicle head, the required mass flow rate decreases from 9.4 to 0.188 kg/s, 93.4 to 1.87 kg/s, 187 to 3.73 kg/ s, 462 to 9.25 kg/s, 910 to 18.2 kg/s, 1765 to 35.3 kg/s and 2565 to 51.3 kg/s, when the coolant temperature rise increases from 1 to 50 K for heq = 0.1, 1, 2, 5, 10, 20 and 30 W/(m2·K), respectively. However, for the whole vehicle, the mass flow rate will decrease from 30.6 to 0.612 kg/s, 305 to 6.12 kg/s, 608 to 12.15 kg/s, 1499 to 30.0 kg/s, 2926 to 58.5 kg/s, 5560 to 111 kg/s and 7945 to 159 kg/s, when the coolant temperature rise increases from 1 to 50 K for heq = 0.1, 1, 2, 5, 10, 20 and 30 W/(m2·K).
Acknowledgments
This study is supported by the National Natural Science Foundation of China (51806175).
References
- [1] B. Behrens, M. Müller, Technologies for thermal protection systems applied on reusable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [2] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130.
- [3] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [4] D.E. Myers, C.J. Martin, M.L. Blosser, Parametric Weight Comparison of Advanced Metallic, Ceramic Tile, and Ceramic Blanket Thermal Protection Systems, NASA Langley Technical Report Server, 2000.
- [5] A. Riccio, F. Raimondo, A. Sellitto, V. Carandente, R. Scigliano, D. Tescione, Optimum design of ablative thermal protection systems for atmospheric entry vehicles, Appl. Therm. Eng. 119 (2017) 541–552.
- [6] M. Rivier, J. Lachaud, P.M. Congedo, Ablative thermal protection system under uncertainties including pyrolysis gas composition, Aerosp. Sci. Technol. 84 (2019) 1059–1069.
- [7] N. Blet, S. Lips, V. Sartre, Heats pipes for temperature homogenization: A literature review, Appl. Therm. Eng. 118 (2017) 490–509.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

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
