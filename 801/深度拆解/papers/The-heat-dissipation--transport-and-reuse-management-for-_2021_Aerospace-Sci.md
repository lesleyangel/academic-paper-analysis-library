# The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.txt` 的全文抽取，并参考 `801/文本/metadata/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 的目录信息。metadata 中 title/author 字段为空，但首页和 toc 给出完整题名与作者。txt 存在双栏串栏，尤其是 Fig. 10-Fig. 18、Table 7-9 和结论段附近，曲线、表格与参考文献混排明显。本文以 txt 为主，不复述长段原文；所有涉及温度云图、TE-AFRSI 几何、冷却通道 CFD 云图、设计路线图和表格精确数值的判断均标注“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion。
- 作者：Jian-Jun Gou, Zheng-Wei Yan, Jia-Xin Hu, Ge Gao, Chun-Lin Gong。
- 期刊与年份：Aerospace Science and Technology, 108, 2021, Article 106373。
- DOI：10.1016/j.ast.2020.106373。
- 关键词：Thermal energy management；Hypersonic vehicle；Heat reuse；Thermoelectric conversion；Regenerative cooling。
- 论文类型：高超声速巡航飞行器热能管理系统设计论文，融合 passive TPS、regenerative cooling network 和 thermoelectric component。
- 研究对象：15 m 级高超声速巡航飞行器表面 20 个子区域的热量耗散、转运和复用。
- 核心方法：等效热平衡模型；overall equivalent HTC；TPS 概念分布与重量计算；RC 网络热容量与质量流量确定；JET-A 与 LH2 冷却剂对比；TE-AFRSI 概念建模与多目标优化；统一控制方程和设计 roadmap。
- 主要证据：heq=0-20 W/(m2 K)、Tb=300/367/440 K 的参数扫描；TPS 重量从 820 kg 降至 299 kg；LH2/JET-A 质量流量对比；TE-AFRSI 最大转换效率约 0.90%、最大复用比例 31.5%、局部区域电功率 6.16 kW、全车超过 20 kW 的潜力估算。
- 目标读者：高超声速热管理、再生冷却、热电转换、多功能 TPS 和飞行器总体能量管理研究者。

这篇论文是 2019 年 TMS 设计工作的扩展：2019 年主要是 passive TPS + ACN，这篇将热管理明确扩展为 heat dissipation、transport 和 reuse 三个过程，并把主动冷却从 ACN 扩展到 regenerative cooling 与 thermoelectric conversion 的组合。

## 2. 摘要与核心信息提取

一句话主张：高超声速飞行器热管理不应只考虑“防热”，而应管理气动热从产生后如何被 passive TPS 耗散、由 RC network 转运、并通过 RC 和 TE component 复用；overall equivalent HTC 可作为三子系统耦合设计的统一参数。

摘要的信息层次非常丰富。第一句直接定义 thermal energy management 要关注 heat dissipation、transport and reuse 全过程。随后将三个子系统对应到三个动作：passive TPS dissipates，RC network transports，RC network and TE component reuse。接着说明等效热平衡模型和 overall equivalent HTC 用于建立 aerodynamic heating 与 TM system 的 mutual correlation，而不是 one-way influence。再分别说明 TPS、RC、TE 的设计输出，最后给出 design roadmap 和 heq 的影响规律。

核心信息不是“加了热电转换”，而是“热量路径被系统化”：表面辐射/隔热只是第一段，进入 TPS 的热量要通过冷却剂运输，运输后的热量部分可以被燃料或热电组件复用。文章把热量看作需要管理的流，而不是单纯需要阻断的负担。

## 3. 选题层深拆

选题来源是高超声速巡航飞行器相比航天飞机面临更长时间大气飞行、更尖细外形和更严酷热积累。传统被动 TPS 依赖表面辐射和隔热，会产生重量和体积问题；热减阻/减热外形设计又可能损害气动性能。因此，作者选择“对已产生气动热进行高效耗散、转运和复用”作为技术路径。

作者把大问题收束成一个全车 TM 系统设计问题：给定巡航飞行器外形、轨迹和表面分区，如何确定被动 TPS 概念、RC 网络能力、冷却剂质量流量、TE-AFRSI 几何以及整体复用比例。这个问题明确地跨越材料、流体、传热、电转换和总体设计。

选题价值有三层。工程上，它为高超声速巡航器提供比“厚 TPS”更积极的热管理方案。方法上，它将 heq 从 2019 年的主动冷却参数扩展为可表示多种 heat take-away 技术的 overall equivalent HTC。学术写作上，它用“dissipation-transport-reuse”三动词建立完整叙事，比单独说 thermal protection 更有系统感。

这篇文章比 2019 年工作更复杂，也更容易被质疑过度集成。它的优势是系统完整，弱点是每个子模块都可能被专业审稿人追问细节，例如 RC 通道、TE 材料性能、接口热阻、燃料热裂解等。

## 4. 领域位置与文献版图

Introduction 先通过 NASP、Hyper-X、Skylon、LAPCAT、SpaceLiner 等项目说明新一代高超声速/空间飞行器热环境更严酷。随后将现有技术分为 heat reduction、heat dissipation、heat transport 和 heat reuse。

heat reduction 文献包括 blunt forebody、spikes、opposing jet、rear jet、lateral jet 等，作者指出这些手段会影响气动性能，因此不是本文主路。heat dissipation 主要依赖 passive TPS 的表面辐射与隔热，包括 NASA 发展出的 flexible blankets、ceramic tiles、metallic panels。heat transport 包括 heat pipe 和 coolant convection，作者强调 RC 在燃料作为冷却剂时可同时实现热转运与热复用。heat reuse 则包括 TE conversion，已有研究多集中在材料效率、汽车废热、小温差 TEG 或特定组件。

本文站位是把这些分散技术组织成全车热能管理系统：TPS 负责耗散，RC 负责转运和燃料预热复用，TE component 负责热电转换复用。它不是纯综述，也不是单一组件优化，而是系统集成设计。

文献版图的一个重要动作是引用作者前期 2019 工作，指出原模型主要处理 ACN/convective cooling，本研究将 equivalent thermal equilibrium model 和 overall heq 扩展到不同 take-away techniques，包括 RC 与 TE。

## 5. Gap 制造机制

文章的 gap 制造基于“热管理过程不完整”。已有研究可能关注减热、被动防热、局部再生冷却或热电转换，但很少把 hypersonic vehicle 的气动热按照生产、耗散、转运、复用完整链条来管理。

具体 gap 有四类。第一是系统 gap：TPS、RC、TE 通常分开研究，缺少 mutual correlation 的耦合设计。第二是路径 gap：气动热进入结构后，不应只问如何隔绝，还要问如何由冷却剂转运并再利用。第三是参数 gap：需要一个 overall equivalent HTC 将多种取热机制统一到气动热计算和子系统设计中。第四是设计路线 gap：如何从表面分区、热负荷、TPS 概念、RC 通道、TE-AFRSI 优化到整车 roadmap，仍缺清晰流程。

这个 gap 有一定强度，因为作者用“dissipation, transport and reuse”重新定义 thermal energy management。它不是局部技术缺口，而是系统边界扩大。风险是边界太大，导致每个模块深度有限。

## 6. 创新性判断

作者声明的创新包括：提出包含 passive TPS、RC network 和 TE component 的 TM 系统；发展等效热平衡模型和 overall equivalent HTC 建立气动热与 TM 系统的相互关联；给出 TPS 分布与重量、RC 热容量和质量流量设计方法；建立 TE-AFRSI 概念并做优化；提出 TM system design roadmap。

真实创新属于“系统集成框架 + 多功能 TPS 概念 + 设计路线图”。单独的 RC、TE 转换、TPS 概念和 heq 都有前期基础；新意在于把三者放入同一全车热量路径，并用 heq 做统一参数。

创新强度：中到强。强在系统叙事和多模块耦合，弱在每个模块的物理模型简化较多。例如 TE-AFRSI 转换效率最高约 0.90%，电功率密度等数值显示热电复用贡献有限，但作为热管理“复用”概念有启发意义。

最有价值的创新是设计 roadmap。它把复杂设计分成 aerodynamic heating/TPS/RC/TE/iteration 若干步骤，让读者看到系统设计如何推进，而不是只看一堆参数扫描。

## 7. 论证链条复原

全文论证链如下：

1. 新一代高超声速飞行器热负荷更严酷，纯被动 TPS 会带来重量和体积压力。
2. 热管理应从单一防热扩展为气动热的耗散、转运和复用。
3. passive TPS、RC network、TE component 分别承担这些功能，但三者相互影响，不能独立设计。
4. 引入等效热平衡模型和 overall heq，把 take-away heat qin 纳入气动热计算，并建立 aerodynamic heating 与 TM system 的双向关联。
5. 将车辆表面划分为 20 个子区域，按最保守区域结果确定每个子区域 TPS、RC、TE 参数。
6. 通过 heq 和 Tb 参数扫描得到壁温、气动热、传入 TPS 热量、TPS 重量和 RC 热容量需求。
7. 对 FII-L/FIII-L 等特定区域进行 AFRSI-RC CFD，比较 JET-A 与 LH2，确定质量流量限制。
8. 建立 TE-AFRSI 单元，优化热防护、重量增量、电功率和热复用比例。
9. 综合形成 TM system design roadmap，并指出 heq 增大时 TPS 规模减小、转运/复用比例提高、RC/TE 容量需求增强。

这条链的核心闭合点是“heq 影响所有子系统”：它既改变壁温和气动热，也改变 qin、TPS 重量、RC 容量和 TE 可用温差。文章真正想证明的是 heq 能作为全车热管理系统的牵引参数。

## 8. 方法/理论/模型细拆

方法从车辆和分区开始。研究对象为 15 m 长、约 6 m 翼展的高超声速巡航飞行器，表面被划分为 20 个子区域，如 fuselage leading edge、leeward/windward surfaces、compression surfaces、propulsion surfaces、wings、vertical fins 等。每个子区域按最保守热环境确定参数。

等效热平衡模型是方法核心。表面热平衡为气动对流输入等于表面辐射加进入 TPS 的热流。不同于前期 qin = heq(Tw - Tc)，本文为了兼容多种 take-away 技术，将 qin 表示为 heq * Tw，强调 heq 代表整体取热能力，而不限定为冷却剂对流。

RC 网络方法包括：采用 JET-A 3638 和 LH2 作为冷却剂，使用物性随温度变化数据；通过热容量需求 cp * mf 和允许温升估算质量流量；对 AFRSI-RC 网络做 CFD，分析不同通道尺寸和质量流量下底部温度、冷却剂出口温度和换热能力。作者指出 LH2 因比热大，所需质量流量显著小于 JET-A，且通道尺寸影响较小；JET-A 小通道速度更高时冷却效果更好。

TE-AFRSI 方法包括：将 mid- 和 low-temperature TE stages 集成进 AFRSI 概念，使用 ANSYS Multiphysics 做热-电分析，优化目标包括 TE conversion efficiency、单位体积/重量/面积电功率、热复用比例和底部温度等。该部分承认 TE 转换效率不高，但可以贡献局部电功率和热复用。

最后的 unified governing equation 将不同物理问题用统一形式表示，显示作者希望把热传导、流动和热电耦合纳入同一建模语言。

## 9. 证据系统与 Claim-Evidence 表

证据系统由设计计算、CFD、FEM/热电分析和参数扫描构成。它不是通过实验验证，而是通过多模块模型和一致趋势证明系统设计可行。

| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| TM 应覆盖热耗散、转运和复用全过程 | 摘要、Introduction、Fig. 1 | 系统由 TPS、RC network、TE component 三部分组成，对应 dissipation/transport/reuse | 概念框架 | 强 | 框架宽，子模块深度不均 |
| overall heq 可建立气动热与 TM 系统相互关联 | Section 3.1-3.2 | qin = heq Tw，heq 作为输入影响壁温、气动热和子系统规模 | 模型推导 | 中强 | heq 与真实多技术取热能力的映射需验证 |
| heq 增大降低壁温、增加转运/复用热比例、减少 TPS 规模 | Results、Conclusion | heq 0-20 W/(m2 K) 下壁温下降，TPS weight 从 820 kg 降至 299 kg | 参数扫描 | 强 | 表格和曲线需 PDF 图像复核 |
| LH2 冷却能力强于 JET-A，所需质量流量更小 | RC results、Conclusion 4/6 | LH2 因比热大，mf 明显小于 JET-A；JET-A 通道尺寸影响更明显 | 物性与 CFD 分析 | 强 | 未考虑燃料系统复杂性和安全性 |
| 特定区域 RC 网络有可满足和不可满足的 heq 边界 | Conclusion 5/6 | FII-L/FIII-L：低 heq 受 Tb 限制，高 heq 受 RC 热容量限制；高 heq 下 RC 无法满足 | CFD/公式交叉判断 | 中强 | 只针对选定区域与几何 |
| TE-AFRSI 可实现有限热电复用 | Section 4.4、Conclusion 7/8 | 最大转换效率 0.90%，最大复用比例 31.5%，局部 FII-L/FIII-L 电功率可约 6.16 kW，全车超过 20 kW | 热电仿真与尺度外推 | 中 | 转换效率低，重量增量大，接口和可靠性未充分考虑 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Fig. 1 | 展示飞行器和热管理系统概念 | 热量路径系统化 | passive TPS、RC、TE 的空间关系 | 需要 PDF 图像复核 |
| Fig. 2/Table 1 | 表面 20 子区域划分 | 分区设计基础 | 每个区域按保守热环境设计 | 需要 PDF 图像复核 |
| Fig. 3 | JET-A 与 LH2 物性 | 冷却剂性能差异 | LH2 比热优势导致质量流量更小 | 需要 PDF 图像复核 |
| Eq. (1)-(3) | 等效热平衡与 qin 模型 | heq 统一取热能力 | 从 qin 忽略转为 qin=heq Tw | 公式需 PDF 复核 |
| Fig. 4 | AFRSI-RC CFD 模型 | RC 子系统验证 | 通道几何、边界条件、热流输入 | 需要 PDF 图像复核 |
| Fig. 5 | TE-AFRSI 概念与网格 | TE 子系统设计 | 中低温 TE 阶段集成到 AFRSI | 需要 PDF 图像复核 |
| Fig. 6-Fig. 8 | 壁温、气动热和取热热量 | heq 影响热环境 | heq 增大，壁温降低，取热量比例上升 | 需要 PDF 图像复核 |
| Fig. 9/Table 7 | TPS 概念与尺度 | TPS 规模随 heq 改变 | TPS 概念分布与重量计算 | 表格需 PDF 复核 |
| Fig. 10-Fig. 16/Table 8 | RC 质量流量、温度场、出口温度 | RC 设计边界 | LH2/JET-A 对比，低/高 heq 约束不同 | 需要 PDF 图像复核 |
| Fig. 17/Table 9 | TE-AFRSI 温度、电势和优化结果 | TE 复用能力 | 不同目标下效率、电功率、重量增量取舍 | 需要 PDF 图像复核 |
| Fig. 18 | TM system design roadmap | 研究输出为流程 | 从 heq、TPS、RC、TE 到迭代设计 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 The vehicle, TM system and the fuel-coolant；3 Methodology of TM system design；4 Results and discussions；5 Conclusions。第 3 章非常长，包含 equivalent thermal equilibrium model、aerodynamic heat 与 TM 子系统关系、气动热计算、passive TPS 设计 rationale、RC network CFD、TE concept optimization、unified governing equation。第 4 章按气动热/TPS/RC/TE/TM roadmap 依次推进。

结构体现从概念到系统的扩展：先定义热管理三过程，再定义车辆和燃料，再逐个建立子系统模型，最后把结果合成 roadmap。它比 2019 论文更像“系统工程论文”，章节复杂度也更高。

标题命名偏功能叙述型，如 “Correlation between aerodynamic heat and TM subsystems”“Thermal protection and energy reuse performance of TE-AFRSI”。这些标题暴露了作者关心的不是单独性能，而是相关性和复用能力。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：11
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction                                                 The techniques of thermal protection system (TPS) are devel- | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 高 | 是 | 保留具体变量/对象 |
| 2.2 The fuel-coolant | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Methodology of TM system design | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.3 Calculation of aerodynamic heat | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.4 Design rationale of passive TPS                                    the temperature of the internal boundary is lower than the speci- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.4.1 TPS concepts                                               meeting the thermal protection requirement, otherwise the thick- | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.5 RC network and its CFD model | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4 Results and discussions                                   amount decrease from the leading edge, and a high-value area ap- | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |
| 4.1.1 The aerodynamic heat and the take-away heat                         tive cooling; while the aerodynamic heat amount increases with | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.4 Thermal protection and energy reuse performance of TE-AFRSI        one pattern is displayed, while different temperature legends are | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2 The wall temperature at the leading edge decreases from 1690 | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 先从项目背景和热环境严酷性展开，再把技术路线拆为 heat reduction、dissipation、transport、reuse。每个路线都先说明优势，再指出本文为什么选择/整合特定路线。最后一段把三子系统和 design roadmap 预告出来。

方法部分节奏密集，几乎每个段落都在定义变量、边界、材料或优化目标。它的叙事特点是“先系统，后部件，再统一”：先说明 heq 和 qin，再分别讲 TPS、RC、TE，最后给 unified governing equation。

结果部分用 heq 做主轴。4.1 展示 heq 改变热环境，4.2 展示 TPS 规模响应，4.3 展示 RC 能否承担取热，4.4 展示 TE-AFRSI 能复用多少热，4.5 汇总成 roadmap。这种节奏让文章虽然模块多，但仍有一个贯穿变量。

## 13. 文笔画像与语言习惯

文笔是系统工程与传热设计混合风格。高频词包括 thermal energy management、aerodynamic heat、passive TPS、RC network、TE component、overall equivalent HTC、heat amount proportion、coolant mass-flow-rate、TE-AFRSI、design roadmap。

作者喜欢用三元结构：dissipation、transport、reuse；TPS、RC、TE；distribution、area、weight；thermal protection、weight increment、heat reuse performance。这种并列结构强化“系统完整性”。

语气整体积极，但在局限处也相对诚实。例如承认 RC/TE 设计相对 time-consuming，若全部替换为 CFD 会难以收敛；承认 Tb 提高虽能减重但受材料和内部环境限制。结果句常用 “with the increasing of heq...” 引出趋势。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：heat(231)；temperature(132)；tps(113)；aerodynamic(81)；network(79)；heq(75)；respectively(70)；work(69)；thermal(63)；surface(61)；electric(61)；concept(57)；coolant(55)；cooling(50)；vehicle(48)；lines(45)；system(44)；power(43)；model(40)；thus(39)
- 高频学术名词：temperature(132)；system(44)；model(40)；capacity(38)；results(37)；analysis(28)；materials(27)；science(24)；uence(24)；calculation(24)；convection(23)；structure(22)；conditions(22)；energy(21)；equation(20)；performance(20)
- 高频学术动词：shown(36)；show(17)；developed(16)；shows(13)；indicates(8)；proposed(6)；indicate(4)；compared(3)；formulated(2)；predicted(1)；reveal(1)；evaluated(1)；investigated(1)；simulate(1)；validated(1)；compare(1)
- 高频形容词：aerodynamic(81)；thermal(63)；electric(61)；coolant(55)；passive(38)；cient(31)；boundary(30)；hypersonic(28)；component(27)；equivalent(24)；different(22)；thermoelectric(21)；potential(20)；dynamic(18)；material(16)；convective(15)
- 高频副词/连接副词：respectively(70)；supply(20)；mainly(14)；however(12)；nally(6)；widely(5)；therefore(4)；theoretically(4)；tively(4)；fully(4)；relatively(3)；numerically(2)；early(2)；spectively(2)；accordingly(1)；extremely(1)
- 高频二词短语：aerodynamic heat(55)；passive tps(35)；heat transfer(30)；heat capacity(30)；electric power(24)；aerospace science(23)；science technology(23)；coe cient(23)；gou yan(21)；yan aerospace(21)；electric potential(19)；power supply(18)；per unit(15)；tps concept(15)；increasing heq(15)；overall equivalent(14)
- 高频三词短语：aerospace science technology(23)；gou yan aerospace(21)；yan aerospace science(21)；transfer coe cient(12)；heat transfer coe(11)；electric power supply(11)；supply per unit(9)；aerosp sci technol(9)；overall equivalent htc(8)；power supply per(8)；heat capacity network(8)；int heat mass(8)

**主动、被动与句法**

- 被动语态估计次数：278
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：799
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：567
- 一般过去时线索：52
- 现在完成时线索：4
- 情态动词线索：121
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：heat(12)；thermal(5)；reuse(4)；hypersonic(4)；vehicle(4)；system(4)；tps(4)；network(4)
- 1. Introduction                                                 The techniques of thermal protection system (TPS) are devel-：heat(46)；tps(34)；aerodynamic(23)；surface(22)；vehicle(21)；thermal(18)；electric(15)；area(15)
- 2.2. The fuel-coolant：heat(8)；surface(6)；emissivity(5)；temperature(4)；wall(3)；work(3)；jet-a(3)；tps(3)
- 3. Methodology of TM system design：heat(27)；temperature(24)；qin(17)；aerodynamic(15)；work(14)；coolant(14)；network(12)；calculation(11)
- 3.4. Design rationale of passive TPS                                    the temperature of the internal boundary is lower than the speci-：bottom(1)；temperature(1)；concept(1)；considered(1)
- 3.4.1. TPS concepts                                               meeting the thermal protection requirement, otherwise the thick-：concept(27)；work(23)；temperature(19)；heat(19)；model(19)；tps(18)；boundary(16)；materials(14)
- 4. Results and discussions                                   amount decrease from the leading edge, and a high-value area ap-：heq(2)；pears(1)；third-stage(1)；compression(1)；surface(1)；larger(1)；slope(1)；aerodynamic(1)
- 4.1.1. The aerodynamic heat and the take-away heat                         tive cooling; while the aerodynamic heat amount increases with：heat(60)；temperature(52)；heq(49)；lines(45)；respectively(40)；results(27)；tps(26)；network(25)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：heat dissipation、heat transport、heat reuse、thermal energy management、overall equivalent heat transfer coefficient、take-away heat、heat amount proportion、regenerative cooling、thermoelectric conversion、TE-AFRSI。

可复用定义句式：`The thermal energy management of a hypersonic vehicle should concern the full process of heat dissipation, transport and reuse.` 适合扩大研究对象边界。

可复用 gap 句式：`The three subsystems influence each other and thus the design should be a coupling process.` 适合多子系统耦合论文。

可复用方法句式：`The primary function of the equivalent model is to establish mutual correlation rather than one-way influence.` 适合说明耦合模型价值。

可复用结果句式：`With the increase of overall equivalent HTC, the required capacity of active subsystems should be enhanced, while the scale of passive TPS can be reduced.` 适合 trade-off 叙述。

可复用 roadmap 句式：`The design roadmap consists of the determination of thermal loads, subsystem capacities, component optimization, and iterative convergence under vehicle-level constraints.`

## 15. 引用策略与文献使用

引用策略以“技术路径分类”为主。作者先引用高超声速项目和热环境背景，再引用减热技术、被动 TPS 技术、RC 技术、TE 转换技术和多功能 TPS 概念。每个路径都有“为什么重要、为什么不够”的功能。

自引/团队链条较明显：2018 TE-material based TPS、2019 active cooling TMS、2021 mechanical-thermal-electrical TPS 等共同构成本文基础。这种引用方式让文章像连续研究计划的一环，也可能被审稿人视为外部验证不足。

对于 TE 文献，作者引用了材料效率、汽车废热、太阳能、scramjet 冷却热等场景，目的是说明 TE conversion 作为 heat reuse 已有基础，但 hypersonic 全车集成仍不足。文献服务于“从分散技术到系统集成”的 gap。

## 16. 审稿人视角风险

1. 系统过宽风险：TPS、RC、TE 三个子系统都很复杂，单篇论文难以充分验证每个模型。
2. heq 物理映射风险：overall equivalent HTC 将多种取热技术统一为 qin=heq Tw，可能掩盖局部热路径差异。
3. RC 真实工程风险：泵功、压降、燃料热裂解、结焦、管路布置、安全性和可靠性未充分纳入。
4. TE 贡献风险：TE 转换效率仅约 0.90%，重量增量可能抵消收益；全车 20 kW 估算需要谨慎。
5. 热电接口风险：TE-AFRSI 未充分考虑接触热阻、热应力、循环寿命和连接工艺。
6. 参数范围风险：heq、Tb 和轨迹固定，设计规律不可直接外推到其他飞行器。
7. 图表复核风险：Fig. 10-18 和 Table 7-9 是关键结果，txt 抽取混排明显，需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：用“dissipation-transport-reuse”重构 thermal protection 话题，扩大论文贡献边界。
- 框架资产：将子系统功能映射到热量路径，形成系统工程叙事。
- 参数资产：overall equivalent HTC 作为全系统牵引变量。
- 证据资产：用 heq 同时串联壁温、TPS 重量、RC 质量流量和 TE 复用比例。
- 图表资产：design roadmap 图将复杂多模块设计压缩成可复用流程。
- 讨论资产：主动说明各技术的效率、重量、可实现性取舍，而非只报最好指标。

## 18. 对我写论文的启发

这篇文章最大的启发是：如果一个领域长期把问题写成“防止损失”，可以尝试把它改写成“管理资源”。气动热在传统 TPS 中是负担，在本文中被写成可耗散、可转运、可复用的能量流，选题立刻变得更系统。

第二个启发是同一参数可以承担叙事主轴。heq 贯穿气动热、TPS、RC、TE 和 roadmap，使多模块论文不至于散。自己写跨子系统论文时，也应寻找一个能把所有模块串起来的变量或指标。

第三个启发是系统集成论文要诚实呈现权衡。TE-AFRSI 的效率不高，但作者仍从复用比例、电功率、重量增量和热防护性能多角度讨论，而不是只拿最大电功率做宣传。

## 19. 最终浓缩

这篇论文把高超声速热管理从“被动防热”扩展为“热耗散、热转运、热复用”的全流程管理。它用 overall equivalent HTC 统一 passive TPS、RC network 和 TE component 的耦合设计，展示 heq 增大时壁温下降、TPS 规模减小、转运/复用比例增加，但 RC/TE 容量需求也增强。最值得学习的是三动词系统框架和 roadmap 写法；最需要复核的是 TE-AFRSI 的图表细节、RC 质量流量限制、Table 9 的优化结果，以及全车电功率外推的工程可行性。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.txt` 与 `801/文本/metadata/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.3: 2 The vehicle, TM system and the fuel-coolant （对象/问题/模块）
  - L3 p.3: 2.1 The hypersonic cruise vehicle and its TM system （对象/问题/模块）
  - L3 p.4: 2.2 The fuel-coolant （对象/问题/模块）
- L2 p.4: 3 Methodology of TM system design （方法/模型）
  - L3 p.4: 3.1 The equivalent thermal equilibrium model and overall HTC （方法/模型）
  - L3 p.5: 3.2 Correlation between aerodynamic heat and TM subsystems （对象/问题/模块）
  - L3 p.6: 3.3 Calculation of aerodynamic heat （对象/问题/模块）
  - L3 p.7: 3.4 Design rationale of passive TPS （对象/问题/模块）
    - L4 p.7: 3.4.1 TPS concepts （对象/问题/模块）
    - L4 p.7: 3.4.2 Design rationale （对象/问题/模块）
  - L3 p.7: 3.5 RC network and its CFD model （方法/模型）
  - L3 p.8: 3.6 TE concept and its optimization （对象/问题/模块）
    - L4 p.8: 3.6.1 TE-AFRSI concept and its numerical model （方法/模型）
    - L4 p.9: 3.6.2 The concept optimization （对象/问题/模块）
  - L3 p.9: 3.7 The unified governing equation （对象/问题/模块）
- L2 p.10: 4 Results and discussions （结果/讨论/验证）
  - L3 p.10: 4.1 Aerodynamic heat and its correlation with heq （对象/问题/模块）
    - L4 p.10: 4.1.1 The aerodynamic heat and the take-away heat （对象/问题/模块）
    - L4 p.12: 4.1.2 The reliability of aerodynamic heat calculation （对象/问题/模块）
  - L3 p.12: 4.2 Passive TPS （对象/问题/模块）
  - L3 p.12: 4.3 RC network （对象/问题/模块）
    - L4 p.12: 4.3.1 The capacity of RC network （对象/问题/模块）
    - L4 p.14: 4.3.2 CFD results of AFRSI-RC network （结果/讨论/验证）
    - L4 p.17: 4.3.3 The determination of AFRSI-RC network for FII−L and FIII−L （对象/问题/模块）
  - L3 p.18: 4.4 Thermal protection and energy reuse performance of TE-AFRSI （对象/问题/模块）
  - L3 p.19: 4.5 TM system and its design roadmap （对象/问题/模块）
- L2 p.19: 5 Conclusions （结论）
- L2 p.21: Declaration of competing interest （对象/问题/模块）
- L2 p.21: Acknowledgements （对象/问题/模块）
- L2 p.21: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 The vehicle, TM system and the fuel-coolant | 3 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 The hypersonic cruise vehicle and its TM system | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 The fuel-coolant | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Methodology of TM system design | 4 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 The equivalent thermal equilibrium model and overall HTC | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Correlation between aerodynamic heat and TM subsystems | 5 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Calculation of aerodynamic heat | 6 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 Design rationale of passive TPS | 7 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4.1 TPS concepts | 7 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4.2 Design rationale | 7 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.5 RC network and its CFD model | 7 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.6 TE concept and its optimization | 8 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.6.1 TE-AFRSI concept and its numerical model | 8 | 4 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.6.2 The concept optimization | 9 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.7 The unified governing equation | 9 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Results and discussions | 10 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1 Aerodynamic heat and its correlation with heq | 10 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1.1 The aerodynamic heat and the take-away heat | 10 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.1.2 The reliability of aerodynamic heat calculation | 12 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.2 Passive TPS | 12 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3 RC network | 12 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.1 The capacity of RC network | 12 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.2 CFD results of AFRSI-RC network | 14 | 4 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.3.3 The determination of AFRSI-RC network for FII−L and FIII−L | 17 | 4 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.4 Thermal protection and energy reuse performance of TE-AFRSI | 18 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4.5 TM system and its design roadmap | 19 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 19 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 21 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 21 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 文章历史记录： 收到日期 2020年8月3日 以修订形式收到 2020年11月18日 接受日期 2020年11月19日 在线提供 2020年11月26日 由 Cummings Russell 传播
> 
> 高超声速飞行器的热能管理（TM）应关注散热、传输和再利用的全过程。本文提出高超声速巡洋舰的气动热通过被动热保护系统（TPS）消散，通过再生冷却（RC）网络传输，并由RC网络和热电（TE）转换组件重新利用。 TM系统相应地包括TPS、RC网络和TE组件三个子系统。建立了等效热平衡模型和整体等效传热系数，以建立气动加热和TM系统之间的相互关系，而不是单向影响，并解释TM子系统的耦合设计原理。
> 
> 对于被动TPS，得到相关概念的分布、面积和权重；针对RC网络，建立了热容量和冷却剂质量流量的确定方法，并以碳氢化合物和液氢燃料为冷却剂，对特定车辆区域的热传输性能进行了数值分析；对于TE组件，通过将中低温TE阶段集成到先进的柔性可重复使用表面绝缘体（AFRSI）中，建立了TE-AFRSI概念，并通过考虑热防护、重量增量和热再利用性能来优化该概念。最后提出了TM系统的设计路线并明确了整体等效传热系数的影响。结果表明，气动热和输送或再利用的热量比例会增加，而被动式TPS的规模会随着整体等效传热系数的增加而减小。 © 2020 Elsevier Masson SAS。版权所有。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 本文针对长度为15 m、翼展约6 m的高超声速飞行器在一定巡航轨迹下设计了TM系统。该系统由无源TPS、RC网络和TE组件组成，气动热由无源TPS散发，由RC网络传输，并由RC网络和TE组件重新利用。建立了等效热平衡模型，建立了气动加热与TM系统之间的相互关系，引入了整体等效传热系数来表示
> 
> 阐述了 RC 网络和 TE 组件的热容量，以及这种 TM 系统设计的基本原理。对于被动TPS，确定相关概念的分布、面积和权重；对于RC网络，得到整车热容量需求分布，建立AFRSI-RC的CFD模型，考虑碳氢化合物和液氢燃料作为冷却剂，确定质量流量的最小限制；对于TE组件，引入了TE-AFRSI概念，根据不同目标的优化得到最优概念。研究了总等效HTC（heq = 0至20 W/（m2·K））和冷侧温度（Tb = 300、367和440 K）对气动热和TM系统的影响。结果显示了一些结论：
> 
> J.-J。郭，Z.-W。
> 
> 严，J.-X。胡等人。航天科技108(2021)106373
> 
> 1、随着heq的增加：壁温降低，气动热增加；输送和再利用的热量比例增加，散发的热量比例减少；需要提高RC网络和TE组件的容量，同时减少TPS的规模。 2、当heq从0增加到20 W/(m2·K)时，前缘壁温由1690 K降低至1675 K，背风面中线最低壁温由762 K降低至601 K，第三压缩面最高壁温由1 028 K降低至964 K。 3. TPS权重随着Tb和heq的增加而减小，当Tb小时，增加heq更有效，反之亦然。然而，虽然增加Tb是一种非常有效的方法，但它仍然受到材料选择和车辆内部环境要求的限制。当heq = 0、0.1、1、2、5、10、15和20 W/(m2·K)时，TPS的重量分别减少了62.7%、54.0%、36.4%、1.3%、0.7%、0%、0%和0%。 4.对于RC网络，随着冷却剂温升的增加，冷却剂m f 减小且趋势减慢。由于LH2的比热容较大，LH2所需的m f 比JET-A小得多，这表明LH2具有更强的冷却能力。
> 
> 对于LH2，通道尺寸对冷却性能影响很小，而对于JET-A，通道尺寸越小，冷却性能越好。 5、第二、第三背风面部分采用JET-A的RC网络，对于heq=0.1、1、2W/(m2·K)的情况，所需的m f 主要受Tb限制，Tb=440K时应大于0.23kg/s，Tb=300K时应大于2.27kg/s；而对于heq = 5和10 W/(m2·K)的情况，m f 主要受RC网络热容量的限制，应分别大于2.5和20.1 kg/s；对于heq = 15和20 W/(m2·K)，本工作涉及的RC冷却剂对流无法满足热容量要求。 6、第二、第三背风面部分LH2的RC网络，对于heq = 0.1、1、2 W/(m2·K)的情况，所需m f 主要受Tb限制，对于Tb = 440、300 K分别应大于0.015和0.02 kg/s，而对于heq = 5 W/(m2·K)的情况，m f 主要为受RC网络热容量限制，应大于0.04 kg/s；对于heq = 10、15和20 W/(m2·K)，本工作涉及的冷却剂对流无法满足热容量要求。 7.
> 
> 对于本工作中的TE-AFRSI概念和巡航轨迹，最大TE转换效率为0.90%，单位体积密度的最大电力供应为14.2×10−6
> 
> W·m3/kg，单位重量最大供电量为9.56 W/kg，单位面积最大供电量为178.4 W/m，单位面密度最大供电量为0.94×10−3 W·m2/kg。 8、RC网络和TE组件可重复利用的最大热量比例为31.5%；如果在第二、第三背风面部分采用这样的TE-AFRSI理念，最大供电功率可以达到6.16kW左右，而如果在整个车辆表面采用这样的TE-AFRSI理念，最大供电功率可以达到20kW以上。

### 20.7 论文逻辑脉络复核

- 提出的问题：需结合 Introduction 首段复核。
- 旧方法/已有研究不足：However, although increasing Tb is a very efficient way, it is still limited by the material option and the internal environment requirement of the vehicle. The RC network with JET-A of the second and third leeward surface parts, for cases of heq = 0.1, 1 and 2 W/(m2·K), the required m f is mainly limited by Tb and it should be larger than 0.23 kg/s for Tb = 440 K and 2.27 kg/s for Tb = 300 K; while for cases of heq = 5 and 10 W/(m2·K), m f is mainly limited by the heat capacity of the RC network and it should be larger than 2.5 and 20.1 kg/s, respectively; for heq = 15 and 20 W/(m2·K), the RC coolant convection involved in this work is unable to meet the heat capacity requirment. 6. The RC network with LH2 of the second and third leeward surface parts, for cases of heq = 0.1, 1 and 2 W/(m2·K), the required m f is mainly limited by Tb and it should be larger than 0.015 and 0.02 kg/s for Tb = 440 and 300 K, respectively, while for cases of heq = 5 W/(m2·K), m f is mainly limited by the heat capacity of the RC network and it should be larger than 0.04 kg/s; for heq = 10, 15 and 20 W/(m2·K), the coolant convection involved in this work is unable to meet the heat capacity requirments. 7.
- 本文解决方式：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems. For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance. The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
- 学术/工程增量：需结合 Results/Conclusion 的量化结果复核。
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：118
- Introduction 引用簇数量（估计）：32
- References 条目数（解析）：58
- 可识别年份条目数：58
- 近五年/近年文献（2021+）数量：2
- 经典文献（2010年前）数量：11
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Aerospace Science and Technology(2)
- 引用簇样例：[1], [2], [3], [11,12], [13], [4], [14,15], [5], [6], [7], [15], [8,9]

带引用的 gap/转折句样例：

- It should be noted that the present primary concepts are those developed by NASA in Space Shuttle and subsequent NASP and Hyper-X programs, and can be classified into flexible ceramic blankets, rigid ceramic tiles and metallic panels [10].
- The heat pipe technique is widely used in high-temperature components like vehicle leading edges [15] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.

References 解析样例（前12条）：

- [1] O. Tran, M. Heldmann, J. Fort, ECLSS Heat Sink for the NASP. 2nd International Aerospace Planes Conference, American Institute of Aeronautics and Astronautics, 1990.
- [2] S. Balland, V.F. Villace, J. Steelant, Thermal and Energy Management for Hypersonic Cruise Vehicles - Cycle Analysis. 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics,
- 2015.
J.-J. Gou, Z.-W. Yan, J.-X. Hu et al. Aerospace Science and Technology 108 (2021) 106373
- [3] T. Schwanekamp, F. Meyer, T. Reimer, I. Petkov, A. Tröltzsch, M. Siggel, System Studies on Active Thermal Protection of a Hypersonic Suborbital Passenger Transport Vehicle. 19th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics, 2014.
- [4] M.Y.M. Ahmed, N. Qin, Recent advances in the aerothermodynamics of spiked hypersonic vehicles, Prog. Aerosp. Sci. 47 (6) (2011) 425–449.
- [5] J. Huang, W-X. Yao, Heat reduction mechanism and aerodynamic optimization of combined non-ablative thermal protection system concept, Int. J. Heat Mass Transf. 152 (2020) 119549.
- [6] J. Huang, W-X. Yao, Parameter study on drag and heat reduction of a novel combinational spiked blunt body and rear opposing jet concept in hypersonic flows, Int. J. Heat Mass Transf. 150 (2020) 119236.
- [7] L. Zhu, Y. Li, X. Chen, H. Li, W. Li, C. Li, Hypersonic flow characteristics and relevant structure thermal response induced by the novel combined spikeaerodome and lateral jet strategy, Aerosp. Sci. Technol. 95 (2019) 105459.
- [8] B. Behrens, M. Müller, Technologies for thermal protection systems applied on re-usable launcher, Acta Astronaut. 55 (3–9) (2004) 529–536.
- [9] Y. Rong, Y. Wei, R. Zhan, Research on thermal protection by opposing jet and transpiration for high speed vehicle, Aerosp. Sci. Technol. 48 (Supplement C) (2016) 322–327.
- [10] D.E. Myers, C.J. Martin, M.L. Blosser, Parametric Weight Comparison of Advanced Metallic, Ceramic Tile, and Ceramic Blanket Thermal Protection Systems, NASA Langley Technical Report Server, 2000.
- [11] Y. Li, L. Zhang, R. He, Y. Ma, K. Zhang, X. Bai, B. Xu, Y. Chen, Integrated thermal protection system based on C/SiC composite corrugated core sandwich plane structure, Aerosp. Sci. Technol. 91 (2019) 607–616.

### 20.9 常用词、词类、语态与时态

- 高频词：heat(66)；tps(42)；surface(30)；aerodynamic(28)；vehicle(25)；thermal(25)；system(21)；area(16)；temperature(16)；electric(15)；passive(14)；hypersonic(13)；cooling(12)；network(12)；component(11)；reuse(10)；conversion(10)；cient(10)；coolant(10)；thus(10)
- 高频名词化/学术名词：temperature(16)；conversion(10)；management(7)；uence(7)；emissivity(7)；capacity(6)；density(6)；science(5)；dissipation(5)；performance(5)；insulation(5)；high-temperature(5)；propulsion(5)；protection(4)；equation(4)
- 高频学术动词：developed(8)；optimized(1)
- 高频形容词：aerodynamic(28)；thermal(25)；electric(15)；passive(14)；hypersonic(13)；component(11)；cient(10)；coolant(10)；management(7)；equivalent(7)；regenerative(5)；thermoelectric(5)；current(5)；personic(4)；dynamic(4)
- 高频副词：respectively(8)；mainly(4)；widely(3)；relatively(2)；accordingly(1)；numerically(1)；nally(1)；early(1)；extremely(1)；ciently(1)；rstly(1)；theoretically(1)；merically(1)；only(1)；supply(1)
- 高频二词短语：aerodynamic heat(16)；passive tps(12)；heat transfer(9)；coe cient(8)；aerodynamic heating(7)；tps concepts(7)；surface parts(7)；parts iii(7)；transport reuse(6)；transfer coe(6)；aerospace science(5)；science technology(5)
- 高频三词短语：surface parts iii(7)；heat transfer coe(6)；transfer coe cient(6)；aerospace science technology(5)；power per unit(4)；parts iii propulsion(4)；iii propulsion system(4)；dissipation transport reuse(3)；thermal energy management(3)；transport reuse aerodynamic(3)；reuse aerodynamic heat(3)；thermal protection system(3)
- 被动语态估计：53；`we + 动作动词` 主动句估计：0
- 一般现在时线索：109；一般过去时线索：127；现在完成时线索：0；情态动词线索：17

章节词频：

- Abstract: heat(10)；thermal(4)；system(4)；tps(4)；network(4)；equivalent(4)；november(3)；aerodynamic(3)
- Introduction: heat(50)；tps(30)；aerodynamic(25)；thermal(18)；electric(15)；passive(13)；system(12)；temperature(12)
- Conclusion: heat(13)；network(12)；heq(12)；capacity(8)；decreases(7)；while(7)；largest(7)；tps(6)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
  可迁移模板：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
- 原句/结构：The heat pipe technique is widely used in high-temperature components like vehicle leading edges [15] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.
  可迁移模板：The heat pipe technique is widely used in high-temperature components like vehicle leading edges [X] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.
- 原句/结构：However, the research on this topic is still very limited.
  可迁移模板：However, the research on this topic is still very limited.
#### 方法句
- 原句/结构：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems.
  可迁移模板：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and METHOD system instead of the one-way influence, and account for the coupling design rationale of the METHOD subsystems.
- 原句/结构：For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
  可迁移模板：For passive METHOD, the distribution, area and weight of relevant concepts are obtained; for METHOD network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for METHOD component, a METHOD concept is established by integrating mid- and low-temperature METHOD stages into the advanced flexible reusable surface insulation (METHOD), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
- 原句/结构：The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
  可迁移模板：The design roadmap of METHOD system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
#### 结果句
- 原句/结构：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient. © 2020 Elsevier Masson SAS.
  可迁移模板：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive METHOD will be reduced by the increase of overall equivalent heat transfer coefficient. © XElsevier Masson METHOD.
- 原句/结构：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive TPS will be reduced by the increase of overall equivalent heat transfer coefficient. © 2020 Elsevier Masson SAS.
  可迁移模板：The results show that the aerodynamic heat and the transported or reused heat proportion will increase, while the scale of passive METHOD will be reduced by the increase of overall equivalent heat transfer coefficient. © XElsevier Masson METHOD.
- 原句/结构：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and TM system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of RC network and TE component, and the rationale of the design of such a TM system is stated.
  可迁移模板：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and METHOD system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of METHOD network and METHOD component, and the rationale of the design of such a METHOD system is stated.
#### 贡献句
- 原句/结构：For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
  可迁移模板：For passive METHOD, the distribution, area and weight of relevant concepts are obtained; for METHOD network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for METHOD component, a METHOD concept is established by integrating mid- and low-temperature METHOD stages into the advanced flexible reusable surface insulation (METHOD), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
- 原句/结构：For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating mid- and low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
  可迁移模板：For passive METHOD, the distribution, area and weight of relevant concepts are obtained; for METHOD network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for METHOD component, a METHOD concept is established by integrating mid- and low-temperature METHOD stages into the advanced flexible reusable surface insulation (METHOD), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance.
- 原句/结构：An equivalent thermal equilibrium model is developed to establish the mutual correlation between the aerodynamic heating and TM system.
  可迁移模板：An equivalent thermal equilibrium model is developed to establish the mutual correlation between the aerodynamic heating and METHOD system.
#### 限制/边界句
- 原句/结构：Article history: Received 3 August 2020 Received in revised form 18 November 2020 Accepted 19 November 2020 Available online 26 November 2020 Communicated by Cummings Russell The thermal energy management (TM) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
  可迁移模板：Article history: Received XAugust XReceived in revised form XNovember XAccepted XNovember XAvailable online XNovember XCommunicated by Cummings Russell The thermal energy management (METHOD) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
- 原句/结构：Aerospace Science and Technology 108 (2021) 106373 Contents lists available at ScienceDirect Aerospace Science and Technology www.elsevier.com/locate/aescte The thermal energy management (TM) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
  可迁移模板：Aerospace Science and Technology X(X) XContents lists available at ScienceDirect Aerospace Science and Technology www.elsevier.com/locate/aescte The thermal energy management (METHOD) of a hypersonic vehicle should concern the full process of the heat dissipation, transport and reuse.
- 原句/结构：The aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive TPS, and a qualified passive TPS should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [8,9].
  可迁移模板：The aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive METHOD, and a qualified passive METHOD should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [X,X].

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
