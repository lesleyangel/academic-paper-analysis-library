# The heat dissipation, transport and reuse management for hypersonic vehicles based on regenerative cooling and thermoelectric conversion

## 0. 读取说明

本文拆解基于 `801/文本/txt/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.txt` 的全文抽取，并参考 `801/文本/metadata/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 的目录信息。metadata 中 title/author 字段为空，但首页和 toc 给出完整题名与作者。txt 存在双栏串栏，尤其是 Fig. 10-Fig. 18、Table 7-9 和结论段附近，曲线、表格与参考文献混排明显。本文以 txt 为主，不复述长段原文；所有涉及温度云图、TE-AFRSI 几何、冷却通道 CFD 云图、设计路线图和表格精确数值的判断均标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The vehicle, TM system and the fuel-coolant, 3 Methodology of TM system design, 4 Results and discussions, 5 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-heat-dissipation--transport-and-reuse-management-for-_2021_Aerospace-Sci.md`。

中文译文：

> 文章历史记录： 收到日期 2020年8月3日 以修订形式收到 2020年11月18日 接受日期 2020年11月19日 在线提供 2020年11月26日 由 Cummings Russell 传播
>
> 高超声速飞行器的热能管理（TM）应关注散热、传输和再利用的全过程。本文提出高超声速巡洋舰的气动热通过被动热保护系统（TPS）消散，通过再生冷却（RC）网络传输，并由RC网络和热电（TE）转换组件重新利用。 TM系统相应地包括TPS、RC网络和TE组件三个子系统。建立了等效热平衡模型和整体等效传热系数，以建立气动加热和TM系统之间的相互关系，而不是单向影响，并解释TM子系统的耦合设计原理。
>
> 对于被动TPS，得到相关概念的分布、面积和权重；针对RC网络，建立了热容量和冷却剂质量流量的确定方法，并以碳氢化合物和液氢燃料为冷却剂，对特定车辆区域的热传输性能进行了数值分析；对于TE组件，通过将中低温TE阶段集成到先进的柔性可重复使用表面绝缘体（AFRSI）中，建立了TE-AFRSI概念，并通过考虑热防护、重量增量和热再利用性能来优化该概念。最后提出了TM系统的设计路线并明确了整体等效传热系数的影响。结果表明，气动热和输送或再利用的热量比例会增加，而被动式TPS的规模会随着整体等效传热系数的增加而减小。 © 2020 Elsevier Masson SAS。版权所有。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：However, although increasing Tb is a very efficient way, it is still limited by the material option and the internal environment requirement of the vehicle. The RC network with JET-A of the second and third leeward surface parts, for cases of heq = 0.1, 1 and 2 W/(m2·K), the required m f is mainly limited by Tb and it should be larger than 0.23 kg/s for Tb = 440 K and 2.27 kg/s for Tb = 300 K; while for cases of heq = 5 and 10 W/(m2·K), m f is mainly limited by the heat capacity of the RC network and it should be larger than 2.5 and 20.1 kg/s, respectively; for heq = 15 and 20 W/(m2·K), the RC coolant convection involved in this work is unable to meet the heat capacity requirment. 6. The RC network with LH2 of the second and third leeward surface parts, for cases of heq = 0.1, 1 and 2 W/(m2·K), the required m f is mainly limited by Tb and it should be larger than 0.015 and 0.02 kg/s for Tb = 440 and 300 K, respectively, while for cases of heq = 5 W/(m2·K), m f is mainly limited by the heat capacity of the RC network and it should be larger than 0.04 kg/s; for heq = 10, 15 and 20 W/(m2·K), the coolant convection involved in this work is unable to meet the heat capacity requirments. 7.
- 本文解决方式：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems. For passive TPS, the distribution, area and weight of relevant concepts are obtained; for RC network, the determination method of the heat capacity and coolant mass-flow-rate is developed, and the heat transport performance at specific vehicle regions is numerically analyzed by using hydrocarbon and liquid hydrogen fuel as coolants; for TE component, a TE-AFRSI concept is established by integrating midand low-temperature TE stages into the advanced flexible reusable surface insulation (AFRSI), and the concept is optimized by considering the thermal protection, weight increment and heat reuse performance. The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

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

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The vehicle, TM system and the fuel-coolant（对象/模块/过渡章节）
  - L3 p.3: 2.1 The hypersonic cruise vehicle and its TM system（对象/模块/过渡章节）
  - L3 p.4: 2.2 The fuel-coolant（对象/模块/过渡章节）
- L2 p.4: 3 Methodology of TM system design（方法/模型/算法）
  - L3 p.4: 3.1 The equivalent thermal equilibrium model and overall HTC（方法/模型/算法）
  - L3 p.5: 3.2 Correlation between aerodynamic heat and TM subsystems（对象/模块/过渡章节）
  - L3 p.6: 3.3 Calculation of aerodynamic heat（对象/模块/过渡章节）
  - L3 p.7: 3.4 Design rationale of passive TPS（对象/模块/过渡章节）
    - L4 p.7: 3.4.1 TPS concepts（对象/模块/过渡章节）
    - L4 p.7: 3.4.2 Design rationale（对象/模块/过渡章节）
  - L3 p.7: 3.5 RC network and its CFD model（方法/模型/算法）
  - L3 p.8: 3.6 TE concept and its optimization（对象/模块/过渡章节）
    - L4 p.8: 3.6.1 TE-AFRSI concept and its numerical model（方法/模型/算法）
    - L4 p.9: 3.6.2 The concept optimization（对象/模块/过渡章节）
  - L3 p.9: 3.7 The unified governing equation（对象/模块/过渡章节）
- L2 p.10: 4 Results and discussions（结果/验证/讨论）
  - L3 p.10: 4.1 Aerodynamic heat and its correlation with heq（对象/模块/过渡章节）
    - L4 p.10: 4.1.1 The aerodynamic heat and the take-away heat（对象/模块/过渡章节）
    - L4 p.12: 4.1.2 The reliability of aerodynamic heat calculation（对象/模块/过渡章节）
  - L3 p.12: 4.2 Passive TPS（对象/模块/过渡章节）
  - L3 p.12: 4.3 RC network（对象/模块/过渡章节）
    - L4 p.12: 4.3.1 The capacity of RC network（对象/模块/过渡章节）
    - L4 p.14: 4.3.2 CFD results of AFRSI-RC network（结果/验证/讨论）
    - L4 p.17: 4.3.3 The determination of AFRSI-RC network for FII−L and FIII−L（对象/模块/过渡章节）
  - L3 p.18: 4.4 Thermal protection and energy reuse performance of TE-AFRSI（对象/模块/过渡章节）
  - L3 p.19: 4.5 TM system and its design roadmap（对象/模块/过渡章节）
- L2 p.19: 5 Conclusions（结论/贡献回收）
- L2 p.21: Declaration of competing interest（尾部材料）
- L2 p.21: Acknowledgements（尾部材料）
- L2 p.21: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The vehicle, TM system and the fuel-coolant | 3 | 2 | 对象/模块/过渡章节 |
| 2.1 The hypersonic cruise vehicle and its TM system | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 The fuel-coolant | 4 | 3 | 对象/模块/过渡章节 |
| 3 Methodology of TM system design | 4 | 2 | 方法/模型/算法 |
| 3.1 The equivalent thermal equilibrium model and overall HTC | 4 | 3 | 方法/模型/算法 |
| 3.2 Correlation between aerodynamic heat and TM subsystems | 5 | 3 | 对象/模块/过渡章节 |
| 3.3 Calculation of aerodynamic heat | 6 | 3 | 对象/模块/过渡章节 |
| 3.4 Design rationale of passive TPS | 7 | 3 | 对象/模块/过渡章节 |
| 3.4.1 TPS concepts | 7 | 4 | 对象/模块/过渡章节 |
| 3.4.2 Design rationale | 7 | 4 | 对象/模块/过渡章节 |
| 3.5 RC network and its CFD model | 7 | 3 | 方法/模型/算法 |
| 3.6 TE concept and its optimization | 8 | 3 | 对象/模块/过渡章节 |
| 3.6.1 TE-AFRSI concept and its numerical model | 8 | 4 | 方法/模型/算法 |
| 3.6.2 The concept optimization | 9 | 4 | 对象/模块/过渡章节 |
| 3.7 The unified governing equation | 9 | 3 | 对象/模块/过渡章节 |
| 4 Results and discussions | 10 | 2 | 结果/验证/讨论 |
| 4.1 Aerodynamic heat and its correlation with heq | 10 | 3 | 对象/模块/过渡章节 |
| 4.1.1 The aerodynamic heat and the take-away heat | 10 | 4 | 对象/模块/过渡章节 |
| 4.1.2 The reliability of aerodynamic heat calculation | 12 | 4 | 对象/模块/过渡章节 |
| 4.2 Passive TPS | 12 | 3 | 对象/模块/过渡章节 |
| 4.3 RC network | 12 | 3 | 对象/模块/过渡章节 |
| 4.3.1 The capacity of RC network | 12 | 4 | 对象/模块/过渡章节 |
| 4.3.2 CFD results of AFRSI-RC network | 14 | 4 | 结果/验证/讨论 |
| 4.3.3 The determination of AFRSI-RC network for FII−L and FIII−L | 17 | 4 | 对象/模块/过渡章节 |
| 4.4 Thermal protection and energy reuse performance of TE-AFRSI | 18 | 3 | 对象/模块/过渡章节 |
| 4.5 TM system and its design roadmap | 19 | 3 | 对象/模块/过渡章节 |
| 5 Conclusions | 19 | 2 | 结论/贡献回收 |
| Declaration of competing interest | 21 | 2 | 尾部材料 |
| Acknowledgements | 21 | 2 | 尾部材料 |
| References | 21 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 先从项目背景和热环境严酷性展开，再把技术路线拆为 heat reduction、dissipation、transport、reuse。每个路线都先说明优势，再指出本文为什么选择/整合特定路线。最后一段把三子系统和 design roadmap 预告出来。

方法部分节奏密集，几乎每个段落都在定义变量、边界、材料或优化目标。它的叙事特点是“先系统，后部件，再统一”：先说明 heq 和 qin，再分别讲 TPS、RC、TE，最后给 unified governing equation。

结果部分用 heq 做主轴。4.1 展示 heq 改变热环境，4.2 展示 TPS 规模响应，4.3 展示 RC 能否承担取热，4.4 展示 TE-AFRSI 能复用多少热，4.5 汇总成 roadmap。这种节奏让文章虽然模块多，但仍有一个贯穿变量。

## 13. 文笔画像与语言习惯

文笔是系统工程与传热设计混合风格。高频词包括 thermal energy management、aerodynamic heat、passive TPS、RC network、TE component、overall equivalent HTC、heat amount proportion、coolant mass-flow-rate、TE-AFRSI、design roadmap。

作者喜欢用三元结构：dissipation、transport、reuse；TPS、RC、TE；distribution、area、weight；thermal protection、weight increment、heat reuse performance。这种并列结构强化“系统完整性”。

语气整体积极，但在局限处也相对诚实。例如承认 RC/TE 设计相对 time-consuming，若全部替换为 CFD 会难以收敛；承认 Tb 提高虽能减重但受材料和内部环境限制。结果句常用 “with the increasing of heq...” 引出趋势。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：46918
- 高频词：heat(141)；tps(65)；aerodynamic(61)；temperature(60)；heq(57)；network(52)；surface(44)；electric(32)；vehicle(30)；work(30)；capacity(29)；should(28)；cooling(28)；system(27)；coolant(27)；lines(26)；thermal(25)；passive(24)；increasing(24)；cases(23)
- 高频名词化/学术名词：temperature(60)；capacity(29)；influence(14)；conversion(12)；proportion(12)；convection(12)；performance(10)；density(9)；reduction(8)；calculation(8)；distribution(7)；determination(7)；insulation(7)；emissivity(7)；propulsion(7)
- 高频学术动词：developed(19)；indicated(10)；optimized(5)；analyzed(3)；indicate(2)；compared(2)；evaluated(1)；compare(1)；validated(1)
- 高频形容词：aerodynamic(61)；electric(32)；coolant(27)；thermal(25)；passive(24)；component(20)；hypersonic(15)；specific(12)；different(12)；equivalent(11)；coefficient(10)；convective(9)；material(8)；potential(7)；requirement(7)
- 高频副词：mainly(13)；supply(12)；relatively(4)；fully(4)；widely(3)；numerically(2)；finally(2)；accordingly(1)；early(1)；extremely(1)；efficiently(1)；firstly(1)；theoretically(1)；adaptively(1)；correspondingly(1)
- 高频二词短语：aerodynamic heat(46)；heat capacity(24)；passive tps(23)；electric power(19)；heat transfer(15)；heat flux(15)；gou yan(14)；cases heq(14)；network component(12)；aerodynamic heating(12)；power supply(12)；increasing heq(12)
- 高频三词短语：electric power supply(10)；largest electric power(9)；heat transfer coefficient(8)；surface parts iii(7)；heat capacity network(7)；tps network component(6)；heat amount proportion(6)；convective heat transfer(6)；cases heq required(6)；heq required mainly(6)；required mainly limited(6)；aerodynamic heat flux(5)
- 被动语态估计：140；`we + 动作动词` 主动句估计：0
- 一般现在时线索：279；一般过去时线索：292；现在完成时线索：0；情态动词线索：67

分章节正文词频：

- 1 Introduction: heat(50)；tps(30)；aerodynamic(25)；thermal(18)；electric(15)；passive(13)；system(12)；temperature(12)
- 2 The vehicle, TM system and the fuel-coolant: area(10)；vehicle(8)；surface(7)；cruise(6)；three(6)；work(5)；iii(5)；will(4)
- 3 Methodology of TM system design: surface(16)；heat(11)；tps(8)；emissivity(6)；iii(5)；wall(5)；system(4)；aerodynamic(4)
- 4 Results and discussions: heat(65)；heq(44)；temperature(37)；network(30)；aerodynamic(27)；lines(26)；cfd(22)；tps(20)
- 5 Conclusions: heat(13)；network(12)；heq(12)；capacity(8)；decreases(7)；largest(7)；tps(6)；component(6)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：heat dissipation、heat transport、heat reuse、thermal energy management、overall equivalent heat transfer coefficient、take-away heat、heat amount proportion、regenerative cooling、thermoelectric conversion、TE-AFRSI。

可复用定义句式：`The thermal energy management of a hypersonic vehicle should concern the full process of heat dissipation, transport and reuse.` 适合扩大研究对象边界。

可复用 gap 句式：`The three subsystems influence each other and thus the design should be a coupling process.` 适合多子系统耦合论文。

可复用方法句式：`The primary function of the equivalent model is to establish mutual correlation rather than one-way influence.` 适合说明耦合模型价值。

可复用结果句式：`With the increase of overall equivalent HTC, the required capacity of active subsystems should be enhanced, while the scale of passive TPS can be reduced.` 适合 trade-off 叙述。

可复用 roadmap 句式：`The design roadmap consists of the determination of thermal loads, subsystem capacities, component optimization, and iterative convergence under vehicle-level constraints.`

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
#### Gap/转折句
- 原句：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
  可迁移模板：However, all the above heat reduction techniques will influence the vehicles’ aerodynamic performance for certain, thus, developing techniques to efficiently dissipate, transport and reuse the aerodynamic heat is another promising technology path.
- 原句：The heat pipe technique is widely used in high-temperature components like vehicle leading edges [15] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.
  可迁移模板：The heat pipe technique is widely used in high-temperature components like vehicle leading edges [X] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.
- 原句：However, the research on this topic is still very limited.
  可迁移模板：However, the research on this topic is still very limited.
- 原句：However, although increasing Tb is a very efficient way, it is still limited by the material option and the internal environment requirement of the vehicle.
  可迁移模板：However, although increasing Tb is a very efficient way, it is still limited by the material option and the internal environment requirement of the vehicle.
#### 方法提出句
- 原句：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems.
  可迁移模板：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and METHOD system instead of the one-way influence, and account for the coupling design rationale of the METHOD subsystems.
- 原句：The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
  可迁移模板：The design roadmap of METHOD system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
- 原句：With the retirement of Space Shuttle, several subsequent hypersonic and space vehicle programs are proposed, such as NASP and succedent Hyper-X of USA, Skylon of UK, LAPCAT of EU, SpaceLiner of Germany.
  可迁移模板：With the retirement of Space Shuttle, several subsequent hypersonic and space vehicle programs are proposed, such as METHOD and succedent Hyper-X of METHOD, Skylon of METHOD, METHOD of METHOD, SpaceLiner of Germany.
- 原句：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and TM system instead of the one-way influence, and account for the coupling design rationale of the TM subsystems.
  可迁移模板：An equivalent thermal equilibrium model and an overall equivalent heat transfer coefficient are developed to build up the mutual correlation between the aerodynamic heating and METHOD system instead of the one-way influence, and account for the coupling design rationale of the METHOD subsystems.
- 原句：The design roadmap of TM system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
  可迁移模板：The design roadmap of METHOD system is finally proposed and the influence of the overall equivalent heat transfer coefficient is clarified.
#### 结果呈现句
- 原句：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and TM system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of RC network and TE component, and the rationale of the design of such a TM system is stated.
  可迁移模板：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and METHOD system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of METHOD network and METHOD component, and the rationale of the design of such a METHOD system is stated.
- 原句：The required m f of LH2 is much smaller than JET-A due to the larger specific heat capacity of LH2, and indicates that LH2 has stronger cooling ability.
  可迁移模板：The required m f of LH2 is much smaller than METHOD-A due to the larger specific heat capacity of LH2, and indicates that LH2 has stronger cooling ability.
- 原句：For LH2, the channel size has very little influence on the cooling performance, while for JET-A, the smaller channel size results into better cooling performance. 5.
  可迁移模板：For LH2, the channel size has very little influence on the cooling performance, while for METHOD-A, the smaller channel size results into better cooling performance. X.
#### 贡献/增量句
- 原句：The techniques of thermal protection system (TPS) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs.
  可迁移模板：The techniques of thermal protection system (METHOD) are developed and improved as responses to the severe aerodynamic heating with the progress of these programs.
- 原句：The thermal energy can be converted into electric energy based on the Seebeck effect of TE materials, and the conversion efficiency can be improved (5-20% or higher) by doping, nano-structuring, etc. [30].
  可迁移模板：The thermal energy can be converted into electric energy based on the Seebeck effect of METHOD materials, and the conversion efficiency can be improved (X-X or higher) by doping, nano-structuring, etc. [X].
- 原句：An equivalent thermal equilibrium model is developed to establish the mutual correlation between the aerodynamic heating and TM system.
  可迁移模板：An equivalent thermal equilibrium model is developed to establish the mutual correlation between the aerodynamic heating and METHOD system.
- 原句：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and TM system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of RC network and TE component, and the rationale of the design of such a TM system is stated.
  可迁移模板：An equivalent thermal equilibrium model is developed and the mutual correlation between the aerodynamic heating and METHOD system is established, an overall equivalent heat transfer coefficient is introduced to indicate the heat capacity of METHOD network and METHOD component, and the rationale of the design of such a METHOD system is stated.
#### 限制/边界句
- 原句：The aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive TPS, and a qualified passive TPS should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [8,9].
  可迁移模板：The aerodynamic heat dissipation is mainly dependent on the thermal radiation at the surface of passive METHOD, and a qualified passive METHOD should be capable of bearing high temperature as well as insulating the heat from entering the inner structure [X,X].
- 原句：It should be noted that the present primary concepts are those developed by NASA in Space Shuttle and subsequent NASP and Hyper-X programs, and can be classified into flexible ceramic blankets, rigid ceramic tiles and metallic panels [10].
  可迁移模板：It should be noted that the present primary concepts are those developed by METHOD in Space Shuttle and subsequent METHOD and Hyper-X programs, and can be classified into flexible ceramic blankets, rigid ceramic tiles and metallic panels [X].
- 原句：Most of the aerodynamic heat is dissipated through thermal radiation on the passive TPS surface, for the part that enters passive TPS, it should be transported (“take-away”) to regions of low temperature or places of heat consuming.
  可迁移模板：Most of the aerodynamic heat is dissipated through thermal radiation on the passive METHOD surface, for the part that enters passive METHOD, it should be transported (“take-away”) to regions of low temperature or places of heat consuming.
- 原句：However, the research on this topic is still very limited.
  可迁移模板：However, the research on this topic is still very limited.
- 原句：With the increasing of heq: the wall temperature decreases, while the aerodynamic heat increases; the heat amount proportion that transported and reused increases, while that dissipated decreases; the required capacity of RC network and TE component should be enhanced, while the scale of TPS can be reduced. 2.
  可迁移模板：With the increasing of heq: the wall temperature decreases, while the aerodynamic heat increases; the heat amount proportion that transported and reused increases, while that dissipated decreases; the required capacity of METHOD network and METHOD component should be enhanced, while the scale of METHOD can be reduced. X.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略以“技术路径分类”为主。作者先引用高超声速项目和热环境背景，再引用减热技术、被动 TPS 技术、RC 技术、TE 转换技术和多功能 TPS 概念。每个路径都有“为什么重要、为什么不够”的功能。

自引/团队链条较明显：2018 TE-material based TPS、2019 active cooling TMS、2021 mechanical-thermal-electrical TPS 等共同构成本文基础。这种引用方式让文章像连续研究计划的一环，也可能被审稿人视为外部验证不足。

对于 TE 文献，作者引用了材料效率、汽车废热、太阳能、scramjet 冷却热等场景，目的是说明 TE conversion 作为 heat reuse 已有基础，但 hypersonic 全车集成仍不足。文献服务于“从分散技术到系统集成”的 gap。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：118
- Introduction 引文簇数量估计：32
- References 条目数：58
- 可识别年份条目数：58
- 2021 年及以后文献数：2
- 2010 年前经典文献数：11
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：Aerospace Science and Technology(2)
- 引文簇样例：[1], [2], [3], [11,12], [13], [4], [14,15], [5], [6], [7], [15], [8,9]

带引文的 gap/转折句样例：

- It should be noted that the present primary concepts are those developed by NASA in Space Shuttle and subsequent NASP and Hyper-X programs, and can be classified into flexible ceramic blankets, rigid ceramic tiles and metallic panels [10].
- The heat pipe technique is widely used in high-temperature components like vehicle leading edges [15] to transport aerodynamic heat to low-temperature region in a short time, however, the final heat dissipation has to resort to other additional measures, thus heat pipes are not suitable for vehicle surfaces of large area.

References 解析样例（前 8 条）：

- [1] O. Tran, M. Heldmann, J. Fort, ECLSS Heat Sink for the NASP. 2nd International Aerospace Planes Conference, American Institute of Aeronautics and Astronautics, 1990.
- [2] S. Balland, V.F. Villace, J. Steelant, Thermal and Energy Management for Hypersonic Cruise Vehicles - Cycle Analysis. 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics,
- 2015.
J.-J. Gou, Z.-W. Yan, J.-X. Hu et al. Aerospace Science and Technology 108 (2021) 106373
- [3] T. Schwanekamp, F. Meyer, T. Reimer, I. Petkov, A. Tröltzsch, M. Siggel, System Studies on Active Thermal Protection of a Hypersonic Suborbital Passenger Transport Vehicle. 19th AIAA International Space Planes and Hypersonic Systems and Technologies Conference, American Institute of Aeronautics and Astronautics, 2014.
- [4] M.Y.M. Ahmed, N. Qin, Recent advances in the aerothermodynamics of spiked hypersonic vehicles, Prog. Aerosp. Sci. 47 (6) (2011) 425–449.
- [5] J. Huang, W-X. Yao, Heat reduction mechanism and aerodynamic optimization of combined non-ablative thermal protection system concept, Int. J. Heat Mass Transf. 152 (2020) 119549.
- [6] J. Huang, W-X. Yao, Parameter study on drag and heat reduction of a novel combinational spiked blunt body and rear opposing jet concept in hypersonic flows, Int. J. Heat Mass Transf. 150 (2020) 119236.
- [7] L. Zhu, Y. Li, X. Chen, H. Li, W. Li, C. Li, Hypersonic flow characteristics and relevant structure thermal response induced by the novel combined spikeaerodome and lateral jet strategy, Aerosp. Sci. Technol. 95 (2019) 105459.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

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
