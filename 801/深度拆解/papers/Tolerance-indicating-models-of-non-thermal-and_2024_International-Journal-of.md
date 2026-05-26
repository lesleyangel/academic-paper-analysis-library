# Tolerance indicating models of non-thermal and thermal damages for a heat transport system

## 0. 读取说明

- 文本来源：`801/文本/txt/Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of.txt`，PyMuPDF 抽取，20 页。
- 抽取文本包含摘要、引言、HT 系统与拓扑优化模型、非热/热损伤数学模型、容限指示模型、拟合与验证、结论和主要图表。
- 原文双栏导致公式和表格局部错行，本文按上下文复原其功能；几何模型、热流方向、损伤位置和温度云图均需 PDF 图像复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The high-speed vehicle and its HT system, 3 The physical model and HT path design, 4 Mathematical models of damage, 5 The damage tolerance indicating model, 6 Results and discussions, 7 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Tolerance indicating models of non-thermal and thermal damages for a heat transport system。
- 作者：Jia-Xin Hu, Li-Qiang Ai, Nan Liu, Jian-Jun Gou, Chun-Lin Gong。
- 期刊：International Journal of Heat and Mass Transfer, 224 (2024) 125360。
- 领域：高速飞行器热输运系统、损伤容限、拓扑优化、热传导路径、随机损伤模型、概率热损伤模型。
- 论文类型：工程热物理建模 + 数值模拟 + 多项式拟合指标模型。
- 研究对象：可重复使用高速飞行器中的 dendritic heat transport path，以二维 volume-to-point (VP) 热传导问题作为基准模型。
- 主要方法：先用 SIMP/MMA 拓扑优化得到树枝状 HT path，再分别建立非热损伤随机圆形低导热区域模型和热损伤概率阈值模型，最后用 Tavg、Tmax、ST 构造 damage tolerance indicating models。
- 论文身份判断：这是“可靠性/损伤容限指标化”论文，不是单纯热传导拓扑优化论文。核心贡献是把损伤参数映射为 HT 性能损失与容限值。

## 2. 摘要与核心信息提取

本文核心主张是：可重复使用高速飞行器的热输运路径会在多次任务中累积非热损伤和热损伤，这些损伤会增加热阻、削弱性能甚至导致系统失效；因此需要能定量指示不同损伤容限的模型。作者将非热损伤描述为随机半径和体积分数模型，将热损伤描述为由温度、约束温度和概率梯度决定的概率模型，并用数值数据拟合得到两个容限指示模型。

摘要的结构很标准：先给工程场景，再定义两类损伤，再说明基准 HT path 来自拓扑优化，随后分析损伤尺寸/体积分数、约束温度/概率梯度对热性能的影响，最后提出并验证两个 indicating models。

一句话浓缩：本文把“热输运路径受损后还能不能工作”转化为由 Tavg、Tmax 和温度标准差共同度量的非热/热损伤容限指标。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Tolerance-indicating-models-of-non-thermal-and_2024_International-Journal-of.md`。

中文译文：

> 对于可重复使用的高速车辆，在多次执行任务期间传热路径中的损坏累积会导致阻力增大、性能下降，甚至热传输（HT）系统故障。对各种损坏的耐受性的定量表征对于可靠的 HT 系统至关重要。在这项工作中，使用尺寸和体积分数的随机模型来描述由机械振动、冲击、腐蚀等各种非热载荷引起的非热损伤，并建立了考虑概率梯度和局部、参考、极限和约束温度的概率模型来表征随着温度升高而产生的热损伤。通过拓扑优化得到了以几何平均温度最低为目标的树枝状高温体系，并分析了非热损伤和热损伤多重分布的传热情况。阐明了非热损伤的尺寸和体积分数以及热损伤的约束温度和概率梯度对HT性能的影响。然后通过多项式拟合提出了考虑 HT 性能的两个损伤容限指示模型，并通过扩展数值数据进行了验证。
>
> 导电率石墨纤维增强金属基复合材料（在 200–400 K 下密度高于 400 W/(m⋅K)，低密度）作为 20 世纪 90 年代电子设备的散热器 [14]。卢等人。 [4]基于卫星相控阵天线用高导热金刚石，开发了导热系数为1600 W/(m·K)的温控薄膜，地面和飞行试验表明表面温差小于3 K。为了提高材料在高温下的热性能，提出了基于ZrB2和HfB2的超高温陶瓷(UHTC)和C/SiC复合材料。乡绅等人。 [15]利用具有高温能力和高导热性的二硼化物基UHTC设计了高速车辆的锋利前缘，这种HT结构可以使停滞区域附近的气动热量快速传导到较冷的区域并辐射回环境。塞塞雷等人。 [16] 和罗等人。 [17]利用ZrB2-SiC基UHTC和ZrB2-ZrC改性C/SiC制备了锋利的前缘结构，他们的研究证明该结构在高温下能够保持一致的导热性，测试结果表明形成了ZrO2骨架，从而提高了耐烧蚀性。蒙吉格拉等人。
>
> [18,19]提出了一种由基于 ZrB2 的超高温陶瓷基复合材料（UHTCMC）制成的近零烧蚀 HT 系统，密度为 4300 kg/m3，导热率为 49
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题的现实入口是 reusable high-speed vehicles。高速飞行器既有外部气动加热，也有内部电子设备发热，需要通过高导热材料、热管、主动冷却等 HT 系统把热从高温区导向低温区。一次任务中 HT 系统可能还能工作，但多次任务后的腐蚀、振动、冲击、氧化、烧蚀、疲劳和堵塞会让热输运路径逐步退化。

作者没有把问题泛化成“结构损伤评估”，而是聚焦在热输运系统的功能性容限：损伤出现后，平均温度、最高温度和温度不均匀性如何恶化；这种恶化能否用损伤体积分数、半径、约束温度和概率梯度预测。

这个选题的价值在于把“可靠性”从定性安全余量变成可计算指标。HT 系统的目标不是结构强度本身，而是维持热性能，因此容限指标必须服务于温度场性能。

## 4. 领域位置与文献版图

引言先铺高速飞行器热管理背景：热防护、热输运、高导热复合材料、UHTC、热管、主动冷却和再生冷却。随后作者转向损伤：高导热材料会因氧化/烧蚀降低性能，冷却通道会因腐蚀/疲劳/堵塞失效。

第二条文献线是 HT path 设计，尤其是 volume-to-point 问题和拓扑优化。作者用 topology optimization 而非预设形状，因为树枝状热输运路径可以在固定体积分数下形成接近最优的热通道。

第三条线是损伤/失效建模。非热损伤借鉴腐蚀坑、随机生成、泊松/正态分布等思想；热损伤借鉴随温度升高而形成的概率损伤和温度归一化指标。作者最终把这些文献整合成一个“HT path 损伤容限指标”的模型。

本文站位在热管理设计与可靠性建模之间：它不是优化一个更好的路径，而是在已有优化路径上问“损伤到什么程度仍可容忍”。

## 5. Gap 制造机制

本文 gap 的关键是：已有 HT 系统研究重视无损状态下的高效热传输，但对多任务损伤累积后的容限缺少统一定量描述。

更具体地说，现有材料和结构研究往往回答“如何提高热导/抗烧蚀/散热效率”，但较少把不同损伤来源统一映射为热性能指标。非热损伤和热损伤的成因不同，几何形态不同，若只用一个“损伤面积”描述，会忽略热损伤与温度场相互耦合的特点。

作者通过区分 non-thermal damage 与 thermal damage 制造了模型必要性：前者来自腐蚀、振动、冲击等非温度载荷，可用随机位置、半径和体积分数表示；后者随温度场生成，需要由 normalized temperature、constraint temperature 和 probability gradient 描述。

## 6. 创新性判断

- 创新类型：损伤模型指标化 + HT 性能归一化 + 工程容限拟合模型。
- 真实创新点 1：为 dendritic HT path 分别建立非热损伤和热损伤生成模型，而不是把损伤统一处理为固定孔洞。
- 真实创新点 2：用 Tavg、Tmax、ST 三个温度场指标共同定义容限，兼顾全局升温、局部热点和温度分布均匀性。
- 真实创新点 3：通过多项式拟合将损伤参数映射到热性能归一化值，再反推出 Ent 和 Et。
- 真实创新点 4：比较同体积分数下非热损伤和热损伤容限，指出热损伤容限更差。
- 创新强度：中等。模型框架有工程价值，但拟合形式依赖特定 2D VP benchmark 和参数范围。
- 可挑战之处：损伤形态、材料退化方式和热-力-化学耦合被大幅简化，距离真实飞行器 HT 系统仍有差距。

## 7. 论证链条复原

1. 可重复使用高速飞行器需要稳定 HT 系统，但多次任务会累积损伤。
2. 损伤会阻塞或削弱热输运路径，使平均温度、最大温度和温度标准差上升。
3. 为了研究损伤容限，先用拓扑优化得到一个具有代表性的 dendritic HT path。
4. 将损伤按成因分为 non-thermal 和 thermal 两类，分别建模。
5. 非热损伤由体积分数 V、典型半径 R、随机位置和圆形低导热区域表示。
6. 热损伤由温度归一化、约束温度 Tf、最大概率梯度 β 和阈值 Th > 0.99 生成。
7. 对不同参数组合进行热传导模拟，得到 Tavg、Tmax、ST。
8. 用归一化热性能拟合 f3/f4，再定义 Ent = 1/f3、Et = 1/f4。
9. 用扩展样本验证拟合模型，报告预测偏差。
10. 比较容限范围后得出：同等损伤水平下，热损伤对 HT path 更不利。

这条链条的优势是闭合，风险是从第 7 步到第 8 步的多项式拟合带有经验性。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Thus, a certain tolerance of damages is essential for a qualified HT system.
- 已有研究不足/GAP：For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for Tmax. 3.
- 本文解决方式：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing. Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data. conductivity graphite fiber reinforced Metal Matrix Composites (higher than 400 W/(m⋅K) in 200–400 K with low density) as heat sinks for electronic devices in the 1990s [14]. Lu et al. [4] developed a temper ature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
- 学术或工程增量：Lu et al. [4] developed a temper ature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K. To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on ZrB2 and HfB2 are proposed. Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

基准 HT path 来自二维 VP 问题。设计域为 100 mm × 100 mm，底部 2 mm 冷源保持 293 K，其余边界绝热，热源载荷选取 5 W、10 W、15 W 测试。后续以 Q = 10 W 作为 benchmark。材料热导率高导区域为 238 W/(m K)，低导区域为 0.238 W/(m K)，体积分数约束 30%。拓扑优化使用密度法 SIMP，并用 MMA 在 COMSOL Multiphysics 6.0 中求解，网格约 25,920 个方形单元、26,243 个节点。

非热损伤模型把损伤看作圆形低导热区域，热导率为原始材料的 1%，即 2.38 W/(m K)。体积分数 V 转换为损伤数量 N，N 服从泊松分布；半径 ri 服从以 R0 为期望的正态分布，标准差取 R0/3；损伤位置由均匀概率生成，并假设不重叠、不出现在冷源处。

热损伤模型从温度场出发。作者定义 normalized temperature，再用双曲正切函数将温度映射为 damage probability Th。Tf 表示损伤概率增长最快的约束温度，β 表示概率梯度。Th > 0.99 的区域被视为热损伤区域，并替换为低导热材料。

容限模型的输出不是单一温度，而是三项热性能：average temperature Tavg、maximum temperature Tmax、standard deviation ST。无损基准为 Tavg0 = 428.05 K、Tmax0 = 488.79 K、ST0 = 36.34 K。损伤后指标按基准归一化，再用权重 k1/k2/k3 或 p1/p2/p3 组合成 f3/f4，最后取倒数得到 Ent/Et。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| 损伤会显著恶化 HT path 热性能 | Section 5 | 示例损伤使 Tavg、Tmax、ST 分别增加 20.25 K、159.98 K、13.15 K | 强 | 损伤形态为理想低导热区 |
| 非热损伤的 V 和 R 越大，容限越差 | Section 6.1/6.3 | V0 2%-12%、R0 1-5 mm 正交设计；Ent 随 V/R 增大而降低 | 强 | 随机性导致 Tmax 奇异点 |
| 热损伤由 β 和 Tf 控制 | Section 4.2/6.2 | β 增大使高概率损伤区扩大；Tf 增大使损伤阈值提高 | 强 | 热损伤概率函数是建模假设 |
| 三指标模型能预测损伤后热性能 | Section 6.3 | 非热模型平均 Tavg/Tmax/ST 最大偏差 0.83%、-7.54%、7.90% | 中强 | Tmax 和 ST 对随机位置敏感 |
| 热损伤模型在较大损伤体积分数下预测可靠 | 结论 | Et 模型最大偏差 0.90%、-1.50%、-4.82% when V > 10.98% | 中强 | 小损伤体积分数下预测可能不稳定 |
| 同体积分数下热损伤容限低于非热损伤 | Fig. 21、结论 | Et 范围 0.13-0.787，Ent 范围 0.302-0.926，且同 V 下 Et 较小 | 中强 | 依赖本文定义的热损伤空间分布 |
| Tavg 最易预测，Tmax/ST 更受局部随机影响 | Section 6.3 | 作者指出 Tavg 为全局平均，Tmax 常出现在损伤附近，ST 受局部梯度影响 | 强 | 需要更多随机样本统计置信区间 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 1 高速飞行器与 HT systems | 建立应用场景，说明热从高温区输运到低温区 | 选题重要性 | 需要 PDF 图像复核 |
| Fig. 2 拓扑优化模型 | 定义 VP benchmark、设计域、热源和冷源 | 基准 HT path | 需要 PDF 图像复核 |
| Fig. 3 HT path 和温度分布 | 证明拓扑优化路径能输运 5/10/15 W 热载荷 | 模型可用 | 温度云图需复核 |
| Eq. 1-3 SIMP/MMA 优化公式 | 把 HT path 设计形式化 | 路径非预设 | 公式排版需 PDF 复核 |
| Fig. 4 非热损伤几何/网格 | 展示随机圆形低导热损伤如何嵌入路径 | 非热模型 | 需要 PDF 图像复核 |
| Fig. 5-8 热损伤概率和区域 | 展示 Tf/β 如何控制损伤概率和损伤域 | 热损伤模型 | 需要 PDF 图像复核 |
| Table 4 / Fig. 9 | 对比有损/无损温度场 | 损伤恶化性能 | 表格和云图需复核 |
| Fig. 10-15 | 正交设计、均值趋势、一阶/二阶拟合 | 非热损伤模型拟合 | 拟合曲线需复核 |
| Eq. 14-18 | 定义 Ent/Et 和归一化指标 | 容限指标 | 公式错行需 PDF 复核 |
| Fig. 18-20 | 扩展样本验证预测值与仿真值 | 模型验证 | 需要 PDF 图像复核 |
| Fig. 21 | 比较 V 与 Ent/Et 关系 | 热损伤容限更低 | 需要 PDF 图像复核 |

结果叙事的关键是“先证明损伤会改变温度场，再把改变压缩为三个指标，最后把指标转成容限值”。这让一个复杂的随机损伤问题变成工程上可比较的数字。

## 11. 章节结构与篇章布局

文章结构为：Introduction；The high-speed vehicle and its HT system；The physical model and HT path design；Mathematical models of damage；The damage tolerance indicating model；Results and discussions；Conclusion。

前半部分是模型准备，后半部分是拟合和验证。第 2 章用概念图把 HT 系统和路径类型讲清楚，第 3 章构造 benchmark，第 4 章建立两类损伤，第 5 章定义容限指标，第 6 章用大量参数组合把公式填实。

章节命名偏好非常工程化：对象明确、功能明确，不追求花哨标题。最值得学习的是第 5 章的位置：作者没有把指标定义混在结果里，而是单独把 indicating model 的输入、输出、归一化和容限解释清楚，再进入结果。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The high-speed vehicle and its HT system（对象/模块/过渡章节）
- L2 p.3: 3 The physical model and HT path design（方法/模型/算法）
- L2 p.5: 4 Mathematical models of damage（方法/模型/算法）
  - L3 p.5: 4.1 The mathematical model of non-thermal damage（方法/模型/算法）
  - L3 p.6: 4.2 The mathematical model of thermal damage（方法/模型/算法）
- L2 p.8: 5 The damage tolerance indicating model（方法/模型/算法）
- L2 p.9: 6 Results and discussions（结果/验证/讨论）
  - L3 p.9: 6.1 The non-thermal damage model（方法/模型/算法）
  - L3 p.14: 6.2 The thermal damage model（方法/模型/算法）
  - L3 p.14: 6.3 The damage tolerance for HT path（对象/模块/过渡章节）
    - L4 p.14: 6.3.1 The non-thermal damage tolerance（对象/模块/过渡章节）
    - L4 p.16: 6.3.2 The thermal damage tolerance（对象/模块/过渡章节）
    - L4 p.18: 6.3.3 The relationships between volume fraction and damage tolerance（对象/模块/过渡章节）
- L2 p.18: 7 Conclusion（结论/贡献回收）
- L2 p.19: CRediT authorship contribution statement（尾部材料）
- L2 p.19: Declaration of competing interest（尾部材料）
- L2 p.19: Data availability（尾部材料）
- L2 p.19: Acknowledgment（尾部材料）
- L2 p.19: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The high-speed vehicle and its HT system | 3 | 2 | 对象/模块/过渡章节 |
| 3 The physical model and HT path design | 3 | 2 | 方法/模型/算法 |
| 4 Mathematical models of damage | 5 | 2 | 方法/模型/算法 |
| 4.1 The mathematical model of non-thermal damage | 5 | 3 | 方法/模型/算法 |
| 4.2 The mathematical model of thermal damage | 6 | 3 | 方法/模型/算法 |
| 5 The damage tolerance indicating model | 8 | 2 | 方法/模型/算法 |
| 6 Results and discussions | 9 | 2 | 结果/验证/讨论 |
| 6.1 The non-thermal damage model | 9 | 3 | 方法/模型/算法 |
| 6.2 The thermal damage model | 14 | 3 | 方法/模型/算法 |
| 6.3 The damage tolerance for HT path | 14 | 3 | 对象/模块/过渡章节 |
| 6.3.1 The non-thermal damage tolerance | 14 | 4 | 对象/模块/过渡章节 |
| 6.3.2 The thermal damage tolerance | 16 | 4 | 对象/模块/过渡章节 |
| 6.3.3 The relationships between volume fraction and damage tolerance | 18 | 4 | 对象/模块/过渡章节 |
| 7 Conclusion | 18 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 19 | 2 | 尾部材料 |
| Declaration of competing interest | 19 | 2 | 尾部材料 |
| Data availability | 19 | 2 | 尾部材料 |
| Acknowledgment | 19 | 2 | 尾部材料 |
| References | 19 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的节奏是“热环境压力-HT 系统方案-损伤来源-现有不足-本文模型”。每个段落都在缩小范围：从飞行器到热输运，从热输运到损伤，从损伤到容限指标。

方法段落常用“定义变量-解释物理含义-给出公式-说明取值范围”的节奏。非热损伤模型段落尤其典型：先说成因，再说圆形损伤，再说体积分数/半径，再说概率分布和假设。

结果段落采用“图表观察-趋势解释-异常点说明-拟合表达”的结构。作者承认随机损伤会造成 singularities，尤其影响 Tmax，这种承认让模型更可信。

结论是编号式，依次总结指标构成、非热损伤规律、热损伤规律、两类容限范围、模型偏差和横向比较。结论的信息密度较高，但略受双栏抽取干扰。

## 13. 文笔画像与语言习惯

本文语言是典型工程建模论文风格：术语重复稳定，claim 主要围绕 model、indicator、performance、tolerance、damage。高频词中 damage、thermal、temperature、model、path、performance、tolerance 极集中，说明文章焦点清晰。

作者偏好被动语态和定义句，如 “is used to describe”“is obtained by”“can be characterized by”。这类表达适合模型论文，因为重点是变量关系和计算流程。

动词多为 characterize、describe、obtain、propose、validate、clarify、indicate。形容词比较克制，常见 quantitative、stochastic、thermal、non-thermal、dendritic、normalized。

时态上，模型定义用一般现在时，具体算例和结果用过去时，结论用一般现在时/现在完成时。情态动词 `can` 出现较多，用于表达模型能力；`should` 较少，说明文章不是规范性指南，而是指标模型。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：47287
- 高频词：damage(154)；thermal(103)；temperature(71)；non-thermal(48)；model(46)；heat(44)；tolerance(42)；path(39)；performance(37)；maximum(30)；obtained(29)；average(29)；damages(25)；paths(23)；conductivity(22)；volume(22)；system(21)；fraction(21)；sample(21)；probability(20)
- 高频名词化/学术名词：temperature(71)；tolerance(42)；performance(37)；conductivity(22)；fraction(21)；probability(20)；prediction(17)；optimization(13)；deviation(13)；simulation(9)；generation(9)；resistance(8)；structure(8)；element(8)；density(7)
- 高频学术动词：indicate(12)；developed(7)；analyzed(4)；achieve(4)；indicated(3)；validated(2)；revealed(2)；optimized(2)；predict(2)；presented(1)；identify(1)；provided(1)；constructed(1)；evaluate(1)
- 高频形容词：thermal(103)；non-thermal(48)；material(18)；gradient(14)；ent(12)；mathematical(12)；represent(11)；various(10)；specific(10)；boundary(9)；different(8)；numerical(8)；typical(8)；element(8)；dendritic(7)
- 高频副词：generally(4)；rapidly(4)；quickly(2)；linearly(2)；slowly(2)；specifically(1)；nearly(1)；highly(1)；separately(1)；mainly(1)；closely(1)；numerically(1)；partly(1)；mostly(1)；theoretically(1)
- 高频二词短语：non-thermal damage(33)；thermal damage(32)；damage tolerance(31)；thermal performance(24)；thermal conductivity(20)；volume fraction(18)；average temperature(15)；avg max(15)；high thermal(10)；tolerance indicating(10)；damage model(10)；maximum temperature(9)
- 高频三词短语：avg max deviations(9)；damage tolerance indicating(7)；sample avg max(7)；geometric average temperature(6)；tolerance indicating models(6)；standard deviation temperature(6)；high thermal conductivity(5)；non-thermal thermal damages(5)；average temperature maximum(5)；thermal damage tolerance(5)；thermal performance path(5)；damage tolerance path(5)
- 被动语态估计：130；`we + 动作动词` 主动句估计：0
- 一般现在时线索：259；一般过去时线索：289；现在完成时线索：0；情态动词线索：71

分章节正文词频：

- 1 Introduction: temperature(29)；thermal(29)；heat(20)；system(17)；damage(17)；high(12)；conductivity(11)；cooling(9)
- 2 The high-speed vehicle and its HT system: paths(9)；heat(8)；high-speed(4)；path(4)；parallel(4)；material(4)；damages(4)；domain(3)
- 3 The physical model and HT path design: heat(13)；temperature(7)；optimization(7)；material(7)；thermal(6)；conductivity(6)；problem(5)；paths(5)
- 4 Mathematical models of damage: damage(37)；thermal(17)；model(14)；temperature(13)；non-thermal(10)；probability(10)；mathematical(10)；increases(9)
- 5 The damage tolerance indicating model: damage(12)；thermal(7)；indicators(6)；path(6)；obtained(5)；performance(5)；temperature(5)；models(4)
- 6 Results and discussions: damage(69)；thermal(34)；tolerance(25)；non-thermal(21)；sample(21)；performance(18)；path(17)；model(16)
- 7 Conclusion: damage(18)；thermal(8)；non-thermal(7)；damages(7)；model(6)；temperature(6)；tolerance(5)；models(5)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：damage tolerance, heat transport system, non-thermal damage, thermal damage, volume fraction, probability gradient, constraint temperature, average temperature, maximum temperature, standard deviation。

可复用 gap 句式：

- “The quantitative characterization of tolerance for various damages becomes crucial to...”
- “The accumulation of various damages will influence the performance and even lead to functional failures.”
- “The inputs and outputs of the indicating model should be normalized.”

可复用方法句式：

- “A stochastic model of size and volume fraction is used to describe...”
- “A probability model considering ... is developed to characterize...”
- “The tolerance indicating model is proposed with inputs of ... and outputs of ...”

可复用结果句式：

- “The lower value reveals weaker thermal performance.”
- “The prediction accuracy of Tmax decreases with increasing... because Tmax usually occurs near damage.”
- “A larger value of E means the damage has less influence on HT performance.”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Thus, a certain tolerance of damages is essential for a qualified HT system.
  可迁移模板：Thus, a certain tolerance of damages is essential for a qualified METHOD system.
- 原句：Zhao et al. [28] established a simulation method to investigate the effect of pressure on the thermal cracking of RP-3 kerosene under supercritical conditions and found that heat transfer is enhanced as pressure increases when the fuel tempera ture is below 830 K.
  可迁移模板：Zhao et al. [X] established a simulation method to investigate the effect of pressure on the thermal cracking of METHOD-Xkerosene under supercritical conditions and found that heat transfer is enhanced as pressure increases when the fuel tempera ture is below METHOD.
#### Gap/转折句
- 原句：However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
  可迁移模板：However, research by Liu et al. [X] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
- 原句：For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for Tmax. 3.
  可迁移模板：For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for Tmax. X.
#### 方法提出句
- 原句：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing.
  可迁移模板：In this work, a stochastic model of size and volume fraction is used to describe the non-thermal damage which is caused by various non-thermal loads like mechanical vibration, impact, corrosion, etc., and a probability model considering probability gradient and local, reference, limit, and constraint temperatures is developed to char acterize the thermal damage which is generated with the temperature increasing.
- 原句：Two damage tolerance indicating models considering HT perfor mance are then proposed by polynomial fittings and validated by extended numerical data. conductivity graphite fiber reinforced Metal Matrix Composites (higher than 400 W/(m⋅K) in 200–400 K with low density) as heat sinks for electronic devices in the 1990s [14].
  可迁移模板：Two damage tolerance indicating models considering METHOD perfor mance are then proposed by polynomial fittings and validated by extended numerical data. conductivity graphite fiber reinforced Metal Matrix Composites (higher than METHOD/(m⋅K) in X–METHOD with low density) as heat sinks for electronic devices in the Xs [X].
- 原句：Lu et al. [4] developed a temper ature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
  可迁移模板：Lu et al. [X] developed a temper ature control film with a thermal conductivity of METHOD/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than METHOD.
- 原句：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on ZrB2 and HfB2 are proposed.
  可迁移模板：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (METHOD) and C/SiC composite based on ZrB2 and HfB2 are proposed.
- 原句：For instance, Li et al. [12] and Wang et al. [13] proposed HT systems based on C/C composite materials with high thermal conduc tivities (higher than 500 W/(m⋅K) in [12]).
  可迁移模板：For instance, Li et al. [X] and Wang et al. [X] proposed METHOD systems based on C/C composite materials with high thermal conduc tivities (higher than METHOD/(m⋅K) in [X]).
#### 结果呈现句
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
  可迁移模板：Cecere et al. [X] and Luo et al. [X] prepared sharp leading edge structures using ZrB2-SiC based METHOD and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
  可迁移模板：Cecere et al. [X] and Luo et al. [X] prepared sharp leading edge structures using ZrB2-SiC based METHOD and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 原句：UHTC based on ZrB2 and HfB2 could achieve thermal con ductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
  可迁移模板：METHOD based on ZrB2 and HfB2 could achieve thermal con ductivities of X–METHOD/(m⋅K) [X], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of X–METHOD/(m⋅K) [X].
- 原句：However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
  可迁移模板：However, research by Liu et al. [X] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.
- 原句：Qiao et al. [10] proposed an active HT system with multiple parallel channels of the leading edge and analysis results showed that the “diamond” channel with coolant of kerosene RP-3 could improve the cooling performance.
  可迁移模板：Qiao et al. [X] proposed an active METHOD system with multiple parallel channels of the leading edge and analysis results showed that the “diamond” channel with coolant of kerosene METHOD-Xcould improve the cooling performance.
#### 贡献/增量句
- 原句：Lu et al. [4] developed a temper ature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
  可迁移模板：Lu et al. [X] developed a temper ature control film with a thermal conductivity of METHOD/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than METHOD.
- 原句：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on ZrB2 and HfB2 are proposed.
  可迁移模板：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (METHOD) and C/SiC composite based on ZrB2 and HfB2 are proposed.
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
  可迁移模板：Cecere et al. [X] and Luo et al. [X] prepared sharp leading edge structures using ZrB2-SiC based METHOD and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 原句：Lu et al. [4] developed a temper ature control film with a thermal conductivity of 1600 W/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than 3 K.
  可迁移模板：Lu et al. [X] developed a temper ature control film with a thermal conductivity of METHOD/(m⋅K) based on the high thermal conductivity diamonds for a satellite phased array antenna, the ground and flight tests revealed a surface temperature difference of smaller than METHOD.
- 原句：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (UHTC) and C/SiC composite based on ZrB2 and HfB2 are proposed.
  可迁移模板：To improve the thermal performance of materials under high temperatures, Ultra-High Temperature Ceramics (METHOD) and C/SiC composite based on ZrB2 and HfB2 are proposed.
#### 限制/边界句
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
  可迁移模板：Cecere et al. [X] and Luo et al. [X] prepared sharp leading edge structures using ZrB2-SiC based METHOD and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 原句：Cecere et al. [16] and Luo et al. [17] prepared sharp leading edge structures using ZrB2-SiC based UHTC and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
  可迁移模板：Cecere et al. [X] and Luo et al. [X] prepared sharp leading edge structures using ZrB2-SiC based METHOD and ZrB2-ZrC modified C/SiC, their studies proved that the structures could maintain consistent thermal conductivity at high tem peratures, and test results indicated that a ZrO2 skeleton was formed resulting in improvement of the ablation resistance.
- 原句：UHTC based on ZrB2 and HfB2 could achieve thermal con ductivities of 55–60 W/(m⋅K) [20], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of 100–200 W/(m⋅K) [21].
  可迁移模板：METHOD based on ZrB2 and HfB2 could achieve thermal con ductivities of X–METHOD/(m⋅K) [X], while C/C composites based on ZrB2 could achieve in-plane thermal conductivities of X–METHOD/(m⋅K) [X].
- 原句：For local HT paths, the configurations of structures and properties of ma terials are studied to improve thermal performance [10,27,28]; for global HT networks, propellant distribution and power allocation should be considered [9,29].
  可迁移模板：For local METHOD paths, the configurations of structures and properties of ma terials are studied to improve thermal performance [X,X,X]; for global METHOD networks, propellant distribution and power allocation should be considered [X,X].
- 原句：Qiao et al. [10] proposed an active HT system with multiple parallel channels of the leading edge and analysis results showed that the “diamond” channel with coolant of kerosene RP-3 could improve the cooling performance.
  可迁移模板：Qiao et al. [X] proposed an active METHOD system with multiple parallel channels of the leading edge and analysis results showed that the “diamond” channel with coolant of kerosene METHOD-Xcould improve the cooling performance.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略分为背景铺垫、系统设计、损伤建模和方法支撑四类。背景引用覆盖高超声速飞行器热防护、UHTC、C/C、热管和主动冷却；系统设计引用支撑 HT path 和 topology optimization；损伤引用支撑腐蚀、疲劳、堵塞、烧蚀等成因；方法引用支撑 VP 问题、SIMP/MMA、概率损伤和温度归一化。

作者对前人态度是“应用丰富但缺少容限量化”。并不直接否定已有 HT 系统设计，而是说在 reusable 任务下，损伤累积对可靠性至关重要。这个引用姿态使本文从“优化设计”自然转向“损伤后评价”。

文献与 gap 的关系较稳：先证明 HT 系统会被用在真实高热场景中，再证明损伤来源真实存在，最后指出缺少把损伤和热性能联系起来的 indicating model。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：94
- Introduction 引文簇数量估计：34
- References 条目数：57
- 可识别年份条目数：93
- 2021 年及以后文献数：31
- 2010 年前经典文献数：9
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：International Journal of Heat and Mass Transfer(2)
- 引文簇样例：[14], [4], [4,5], [15], [16], [17], [12], [13], [18,19], [12], [29], [20]

带引文的 gap/转折句样例：

- However, research by Liu et al. [22] indicated that ZrO2 has a very low thermal conductivity, which will accelerate heat accumulation on the surface of the composites and result in a gradual temperature increase.

References 解析样例（前 8 条）：

- 1. The damage tolerance indicating models encompass the average temperature, Tavg, the maximum temperature, Tmax, and the stan dard deviation of temperature, ST, to evaluate the thermal perfor mance of an HT path.
- 2. For non-thermal damages, the damage region increases while the thermal performance and tolerance decreases with the increasing volume fraction, V and radius, R of damage; however, the random ness of damages will lead to some singularities, especially for Tmax.
- 3. For thermal damages, the transition region increases, the hightemperature region decreases and the damage tolerance of the HT path is thus enhanced with the decrease of the maximum damage probability gradient, β and the increase of constraint temperature, Tf.
- 4. The tolerances of non-thermal damages vary between 0.302 and 0.926 when the volume fraction and radius vary between 2.12% to 16.33% and 0.94 mm to 5.00 mm; the maximum deviations of the damage model are 0.83%, −7.54%, and 7.90% for average Tavg, Tmax, and ST, respectively.
- 5. The tolerances of thermal damages vary between 0.13 and 0.787 when β and Tf vary between 13.5 to 15.5 and 373 K to 383 K; the maximum deviations of the damage model are 0.90%, −1.50%, and −4.82% for average Tavg, Tmax, and ST, respectively, when the damage volume fraction is larger than 10.98%.
- 6. For a dendritic HT path with certain damages, the thermal perfor
mance can be obtained by the damage models, and the tolerance of non-thermal damage is better than that of thermal damage under the same damage level.
CRediT authorship contribution statement
Jia-Xin Hu: Conceptualization, Methodology, Formal analysis, Investigation, Visualization, Writing – original draft. Li-Qiang Ai: Data curation, Writing – review & editing, Funding acquisition. Nan Liu: Validation, Resources, Writing – review & editing. Jian-Jun Gou: Su pervision, Writing – review & editing, Funding acquisition. Chun-Lin Gong: Conceptualization, Resources, Supervision, Project administration.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
Data availability
Data will be made available on request.
Acknowledgment
This study is supported by the National Natural Science Foundation of China (52232014, 51806175).
International Journal of Heat and Mass Transfer 224 (2024) 125360
References
- [1] F. Gori, S. Corasaniti, W.M. Worek, W.J. Minkowycz, Theoretical prediction of thermal conductivity for thermal protection systems, Appl. Therm. Eng. 49 (2012) 124–130, https://doi.org/10.1016/j.applthermaleng.2011.07.012.
- [2] B. Behrens, M. Müller, Technologies for thermal protection systems applied on reusable launcher, Acta Astronaut. 55 (2004), https://doi.org/10.1016/j. actaastro.2004.05.034.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 模型简化风险：非热损伤被设为圆形低导热区域，无法覆盖裂纹、分层、通道堵塞、界面脱粘等复杂形态。
2. 热损伤概率函数风险：Th 的 tanh 映射和 0.99 阈值具有经验性，需要更强物理或实验标定。
3. 拟合泛化风险：f3/f4 的多项式来自固定 Q、Vc、L 的二维 benchmark，换几何、材料或边界条件后未必适用。
4. 统计可靠性风险：随机损伤对 Tmax 影响很强，需要置信区间、重复样本数和不确定性传播说明。
5. 三指标权重风险：k1/k2/k3 或 p1/p2/p3 取 1/3 只是均权，实际任务中最高温度可能远比平均温度重要。
6. 真实飞行器映射风险：从二维 VP path 到三维复杂 HT 系统仍有尺度和物理机制差距。
7. 图表复核风险：损伤位置、温度云图和拟合曲线对理解结论很关键，需要 PDF 图像复核。

## 17. 可复用资产

- 选题资产：从“高效系统在多次任务后会退化”切入，比单次性能优化更贴近 reusable 工程需求。
- 模型资产：把不同损伤成因分开建模，再统一到同一性能指标体系。
- 指标资产：Tavg/Tmax/ST 三指标兼顾全局、局部和均匀性，可迁移到其他热场可靠性研究。
- 图表资产：应用场景图、拓扑优化路径图、损伤重构图、概率损伤图、温度云图、拟合图、容限-体积分数关系图。
- 写作资产：先定义容限指标，再报告容限范围，使结论可比较。
- 审稿防御资产：主动说明随机性导致 Tmax 奇异，有助于降低审稿人对异常点的质疑。

## 18. 对我写论文的启发

这篇论文最值得学习的是“把性能退化转化成指标模型”。很多工程论文只展示系统无损状态下的优化结果，但真实应用更关心失效前的余量。只要能把退化变量和性能指标建立映射，就能形成新的论文空间。

第二个启发是，复杂损伤不必一开始追求全物理细节。作者先把损伤分成两类，用可计算参数描述，再逐步验证拟合模型。这个策略适合早期建立工程评价框架。

第三个启发是，容限指标要与任务目标一致。HT 系统的容限不是强度容限，而是温度场性能容限，因此 Tavg、Tmax、ST 比单纯损伤面积更有说服力。

## 19. 最终浓缩

这篇论文把可重复使用高速飞行器 HT path 的损伤问题拆成非热随机损伤和热概率损伤两类，并用 Tavg、Tmax、ST 构建 Ent/Et 容限指标。它的主要贡献不是提出新的热输运路径，而是提供了一个把损伤几何/概率参数转化为热性能退化和容限值的评价框架。

最大风险是模型强依赖简化损伤形态和固定 benchmark，外推到真实三维飞行器热输运系统前需要实验或高保真仿真校准。

可迁移到自己论文中的三件事：第一，把“损伤成因分类”作为模型入口；第二，用多个性能指标避免单指标片面；第三，报告容限范围和预测偏差，让模型从概念变成可评价工具。
