# Crystallographic fatigue crack propagation in Ni-based single crystals: Mechanistic insights into cube slip activation influenced by load, orientation and temperature

## 0. 读取说明
- 源 PDF：`jmps/文献/Crystallographic-fatigue-crack-propagation-in-Ni-based-_2026_Journal-of-the-.pdf`
- 源 TXT：`jmps/文本/txt/Crystallographic-fatigue-crack-propagation-in-Ni-based-_2026_Journal-of-the-.txt`
- 图像核查：txt 可读章节、图题、结论和局限，但裂纹路径、γ/γ′ 颜色分区、局部路径重合程度需结合 PDF 图像核查。
- 论文类型：CPFEM-XFEM 机制建模论文，目标是解释 Ni 基单晶超合金中 cube slip 何时激活并控制晶体学裂纹扩展。

## 1. 基本信息与论文身份
- 作者：Vasilis Karamitros, Thomas Bellamy, Duncan W. MacLachlan, Fionn P.E. Dunne。
- 期刊/年份：Journal of the Mechanics and Physics of Solids, 214, 2026, 106638。
- DOI：10.1016/j.jmps.2026.106638。
- 关键词：tertiary Ni single-crystals；short crack growth；cube slip；γ-γ′ microstructure；XFEM。
- 研究对象：Ni 基单晶 γ′ 与 γ-γ′ 双相微结构内 cube/octahedral slip 竞争对裂纹路径和速率的影响。
- 方法类型：dislocation-based crystal plasticity + temperature-dependent slip properties + XFEM crack growth + 2D/3D microstructure models。
- 证据类型：文献参数校准、取向/温度/应力扫描、γ′ 和 γ-γ′ 模型、实验路径定性对比、mesh 和 `Gc` 敏感性分析。
- JMPS 定位：机制探索型材料建模论文，作者明确区分“机制一致性”与“定量疲劳寿命预测”。

## 2. 摘要与核心信息提取
摘要把 cube slip 写成高温、高应力和特定取向下可能被激活的 secondary deformation mode。方法上，作者用 CPFEM 与 XFEM，并补充捕捉 γ 和 γ′ slip properties 的方法，建立 2D/3D microstructurally sensitive crack growth framework。最关键的机制变量是 maximum slip `γs` 和 stored energy `G`：`γs` 负责 crack plane selection，`G` 负责 crack advance/growth rate。结果说明 orientation、stress、temperature 的组合会触发 cube-plane crack growth，并可解释实验观察到的高温高应力裂纹路径。

## 3. 选题层深拆
问题来自单晶高温合金叶片中 microstructurally short crack growth。γ 基体与 γ′ 析出相的温度依赖滑移性质不同，裂纹可被 γ channel 限制、在 γ/γ′ 界面迟滞，也可能在高温/高应力下切入 γ′ 并沿 cube slip plane 扩展。已有实验观察到 cube slip，但触发条件、与 octahedral slip 的竞争、对 crack path/growth rate 的影响仍不系统。本文把问题收窄为：在不同载荷、取向、温度和微结构条件下，cube slip 何时由次级模式转为主导裂纹扩展机制？

## 4. 领域位置与文献版图
文献版图有三条线。第一，Ni 基单晶 γ/γ′ 微结构短裂纹和高温疲劳实验，说明 crack confinement、interface barrier 和 crystallographic crack growth。第二，cube slip 与 octahedral slip 的温度依赖研究，包括 anomalous yield、KW locks、CRSS 随温度变化。第三，CPFEM/XFEM 与 stored energy crack growth 模型，为本文提供计算框架。本文在已有团队模型基础上扩展到 γ′ cube slip、双相微结构、跨温度/应力/取向比较。

## 5. Gap 制造机制
- 显式 gap：缺少系统解释 cube slip activation 如何受 load、orientation、temperature 和 γ-γ′ microstructure 共同影响的模型。
- 隐含 gap：实验数据分散，缺少同时报告 stress、temperature、orientation 和 local microstructure 的专门数据集。
- Gap 类型：机制 gap + 数据 gap + 多尺度模型 gap。
- 审稿追问：人为降低 `Gc` 是否影响路径机制？规则 γ-γ′ 几何是否过度理想化？与实验的 qualitative agreement 是否足够支撑主张？

## 6. 创新性判断
作者贡献包括：建立跨 γ′ single crystal 和 γ-γ′ microstructure 的 CPFEM-XFEM 框架；引入温度依赖 slip properties；用 `γs/G` 控制裂纹路径和推进；识别 cube slip 激活的应力、温度、取向条件；与实验 crack path 做机制一致性对比。真实创新中高，强在整合和机制解释，不是某个单一算法全新。最易被挑战的是 `Gc` 为计算可行而取低值，因此绝对 crack growth rates 不能视作实验 da/dN。

## 7. 论证链条复原
背景：Ni 基单晶叶片由 γ/γ′ 微结构控制短裂纹行为，cube slip 在高温下可能出现。  
文献：cube/octahedral slip 的温度依赖已有实验，但触发条件分散。  
Gap：缺少统一框架把取向、温度、应力、微结构和裂纹路径联系起来。  
方法：dislocation-based CPFEM 提供 slip 与 stored energy；XFEM 推进裂纹；γ′ 与 γ-γ′ 模型分级分析；温度依赖 slip strength 校准。  
证据：Tables 1-7 参数；Fig. 4-6 滑移强度/温度关系；Fig. 12-16 γ′ 取向裂纹；Fig. 18-24 应力/温度对比；Fig. 25-26 实验路径对比；Appendix B/C 敏感性。  
结论：25°C 主要 octahedral；900°C/500 MPa γ′ 内 cube slip 更可能；500°C 是中间竞争状态；cyclic loading 加强 slip competition，constant high load 更稳定激活 cube slip。

## 8. 方法/理论/模型细拆
方法以 dislocation-based crystal plasticity 描述 γ/γ′ 滑移，用温度依赖 CRSS 和 activation parameters 捕捉 cube/octahedral slip 强度差异；以 maximum slip `γs` 决定裂纹面选择，以非局部 stored elastic energy `G` 与阈值 `Gc` 决定裂纹推进。关键参数包括 25/500/900°C，200/300/500/800 MPa，`Gc=0.8 J/m²`（γ′ single crystal）与 `7 J/m²`（γ-γ′）。关键假设是降低 `Gc` 不改变路径机制，规则 precipitate arrangement 足以捕捉相级 slip competition，quasi-3D 截面代表主要 crack-microstructure interaction。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| cube slip 激活受温度、应力和取向共同控制 | 摘要、Methods/Results | Fig. 4-6、orientation studies | 参数校准+模拟 | 强 | 文献数据分散 |
| `γs` 与 `G` 可控制 crack plane selection 与 advance | Methods、Limitations | CPFEM-XFEM 框架、sensitivity | 机制模型 | 中强 | `Gc` 人为降低 |
| 900°C/500 MPa 下 γ′ 内 cube plane crack growth 明显 | Conclusion | Fig. 21-24 | 数值模拟 | 中强 | 高应力代表性需限定 |
| 25°C 下 octahedral slip 主导裂纹增长 | Conclusion | 低温模型路径/速率 | 数值模拟 | 强 | 特殊取向可能例外 |
| cyclic loading 产生更 tortuous crack paths | Section 4 | low/high stress cyclic comparisons | 模拟对比 | 中强 | crack closure 处理需核查 |
| 模型与实验 crack path 拓扑一致 | Section 5 | Fig. 25-26 | 机制验证 | 中 | 非严格定量验证 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Fig. 1 | γ-γ′ crack trajectory 示意 | 问题定义 | 显示 crack confinement/phase path | 是 |
| Tables 1-7 | 材料与滑移参数 | 模型可复现 | 支撑温度依赖设定 | 否 |
| Fig. 4-6 | 取向、Schmid ratio、slip strength | cube/octahedral 竞争 | 参数物理化 | 是 |
| Fig. 11 | DD6 γ-γ′ yield strength | alloy strengthening calibration | 校准背景 | 是 |
| Fig. 12-16 | γ′ single crystal crack models | 取向和 cube slip 激活 | 分离单相机制 | 是 |
| Fig. 18-24 | 低/高应力和温度路径/速率 | stress-temperature effects | 主结果证据 | 是 |
| Fig. 25-26 | 实验路径对比 | 机制一致性 | validation 核心 | 是 |
| Appendix B/C | mesh/Gc sensitivity | 稳健性 | 回应审稿风险 | 是 |
| flow rule/stored energy equations | 位错塑性和裂纹推进 | `γs/G` 框架 | 避免纯经验准则 | 否 |

## 11. 章节结构与篇章布局
Introduction 由 γ/γ′ 短裂纹、cube slip 实验和温度依赖机制引出问题。Methods 很长，先讲 CP 和材料性质，再讲 cube slip strength、octahedral strength、3D 模型、XFEM 和微结构模型。Section 3 隔离 γ′ 单晶机制，Section 4 放入 γ-γ′ 双相微结构，Section 5 做实验路径对比，Section 6 独立写局限，Conclusion 五条分温度、载荷和模型优势收束。最值得模仿的是把 limitations 独立成章，清楚说明 exploratory rather than quantitative fatigue life prediction。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Crystallographic-fatigue-crack-propagation-in-Ni-based-_2026_Journal-of-the-.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：16
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Methods and material | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Computational methodology and material properties | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.1.1 Dislocation-based crystal plasticity | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.2 Material properties | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2 Calculation of cube slip in Ni3Al single crystals | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.4 Modeling of Ni single crystal alloy in 3D | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.5 Dislocation-based stored energy density (G) and eXtended finite element method (XFEM) | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.5.1 Computational framework for crystallographic XFEM crack growth | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.6.3 Comparative assessment of dislocation-based crack growth models with experimental cube crack paths | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 4.1 Crack growth paths and rates at low stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 4.2 Crack growth paths and rates at high stress | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 5.1 Crack growth in Ni-based single crystals at macroscale and microscale | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 6 Limitations and scope of current methodological approach | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 用实验现象堆叠复杂性；Methods 通过多级小节管理大量参数；Results 段落通常先给温度/应力/取向条件，再描述裂纹穿过 γ 或 γ′ 时的加速、迟滞和 slip system 切换；Limitations 段落承担降 claim 功能，把路径机制有效性和绝对速率有效性分开。

## 13. 文笔画像与语言习惯
整体语气偏工程材料机制，强在 physical consistency。常用词包括 microstructurally faithful、mechanistic consistency、phase-sensitive fracture、slip system competition、temperature dependent deformation mechanisms。作者对路径机制表述较强，对定量速率谨慎，用 exploratory、qualitative agreement、computational tractability 控制边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：crack(430)；slip(321)；growth(242)；cube(212)；octahedral(126)；stress(93)；mpa(89)；temperature(84)；systems(83)；path(72)；single(69)；model(69)；along(68)；crystal(66)；rate(65)；crystallographic(53)；oct(52)；activation(51)；energy(50)；applied(47)
- 高频学术名词：stress(93)；temperature(84)；model(69)；activation(51)；energy(50)；orientation(44)；propagation(37)；analysis(32)；system(32)；conditions(31)；direction(31)；microstructure(29)；resistance(27)；dislocation(26)；properties(25)；framework(24)
- 高频学术动词：shown(29)；predicted(15)；derived(13)；shows(13)；developed(10)；develop(8)；capture(7)；predict(6)；suggests(4)；investigate(4)；captured(4)；demonstrate(4)；investigated(4)；evaluated(3)；simulate(3)；demonstrated(3)
- 高频形容词：octahedral(126)；experimental(88)；critical(66)；crystal(66)；crystallographic(53)；local(50)；high(29)；microstructural(28)；active(27)；plastic(26)；mechanistic(26)；dominant(24)；elastic(22)；low(21)；physical(17)；element(15)
- 高频副词/连接副词：respectively(18)；therefore(16)；microstructurally(16)；approximately(14)；consequently(14)；however(12)；physically(10)；thermally(9)；early(9)；systematically(8)；subsequently(7)；explicitly(7)；directly(7)；significantly(6)；accurately(5)；finally(5)
- 高频二词短语：crack growth(209)；cube slip(141)；slip systems(74)；octahedral slip(59)；crack path(53)；octahedral cube(44)；single crystal(42)；growth rate(40)；crack propagation(32)；growth rates(30)；stored energy(29)；slip system(29)；crack tip(28)；cube crack(26)；single crystals(25)；applied stress(25)
- 高频三词短语：cube slip systems(43)；octahedral cube slip(37)；crack growth rate(30)；cube crack growth(21)；octahedral slip systems(20)；crack growth rates(17)；cube slip planes(14)；crack growth along(13)；short crack growth(12)；cube slip activation(10)；gpa gpa gpa(10)；stored energy density(9)

**主动、被动与句法**

- 被动语态估计次数：202
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：1121
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：346
- 一般过去时线索：74
- 现在完成时线索：23
- 情态动词线索：34
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：slip(12)；crack(10)；cube(9)；growth(6)；propagation(4)；mechanistic(4)；temperature(4)；single(3)
- 1. Introduction：slip(48)；crack(47)；cube(37)；growth(29)；octahedral(19)；temperature(17)；along(14)；single(12)
- 2. Methods and material：crack(9)；slip(6)；growth(5)；crystal(4)；systems(4)；single(3)；cube(3)；finite(2)
- 2.1. Computational methodology and material properties：无明显高频项
- 2.1.1. Dislocation-based crystal plasticity：slip(25)；cube(14)；oct(12)；systems(9)；octahedral(8)；crack(7)；plastic(5)；given(5)
- 2.1.2. Material properties：slip(19)；gpa(14)；properties(11)；phases(9)；octahedral(8)；single(6)；cube(6)；phase(5)
- 2.2. Calculation of cube slip in Ni3Al single crystals：slip(22)；octahedral(12)；cube(12)；single(10)；strength(9)；crystals(7)；temperature(7)；schmid(7)
- 2.4. Modeling of Ni single crystal alloy in 3D：alloying(22)；model(17)；temperature(14)；slip(13)；strength(11)；resistance(10)；binary(8)；yield(8)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
`Although X has been observed experimentally, the conditions under which Y becomes active remain unclear.`

### 14.2 方法与框架表达
`By leveraging drivers A and B, the model offers qualitative insights into C and quantitative assessments of D.`

### 14.3 结果与趋势表达
`At low temperature, X dominates; at elevated temperature, the governing mechanism shifts toward Y.`

### 14.4 机制解释表达
`Crack propagation is governed by an interplay of slip-system competition, applied stress, and temperature-dependent mechanisms.`

### 14.5 贡献与意义表达
`The framework provides a physically grounded computational basis against which future experiments may be benchmarked.`

### 14.6 局限与未来工作表达
`Absolute rates should not be interpreted as direct quantitative predictions, but the mechanistic conclusions retain validity.`

## 15. 引用策略与文献使用
引用以实验现象和材料参数为主：Ni 基单晶短裂纹、cube slip、KW locks、温度依赖 CRSS、CPFEM/XFEM 和 stored energy 模型。Section 5 引用最新 experimental crack path observation 做机制一致性对照。引用风险在于 alloy composition、应力状态和温度条件不完全一致，因此作者使用 mechanistic consistency 而非 strict validation 是正确策略。

## 16. 审稿人视角风险
最大攻击面是人为降低 `Gc`，导致绝对 crack growth rates 不可当作 fatigue life prediction。第二是 γ-γ′ 几何规则化，忽略 rafting、缺陷、通道不均匀和长期 creep-fatigue 演化。第三是实验验证主要是路径拓扑定性一致。Fig. 25-26 的路径重合度必须结合 PDF 核查。

## 17. 可复用资产
- 选题角度：把偶尔观察到的 secondary mechanism 转化为触发条件图谱。
- 论证链：参数校准 -> 单相机制隔离 -> 双相竞争 -> 实验路径对比 -> 局限声明。
- 图表设计：crack path 与 growth-rate 曲线并列。
- 句型骨架：`mechanistic consistency rather than strict quantitative validation`。
- 不宜直接模仿：没有参数校准时不要做跨温度/应力大范围结论。

## 18. 对我写论文的启发
本文最适合学习“模型 claim 分层”：路径选择、机制转变可以强说；绝对寿命预测必须弱说。复杂材料建模中，局限章节不是削弱论文，而是告诉审稿人哪些结论受控、哪些不受控。写结果时应把 crack path complexity 归因到 phase barrier、slip-system competition 和 temperature-dependent strength。

## 19. 最终浓缩
最值得学：用 `γs/G` 两个可解释驱动量组织复杂 γ/γ′ 裂纹扩展。最大风险：机制模型不能直接当寿命模型。三个可迁移动作：设定清晰驱动量；把绝对数值和机制趋势分开；用局限章节保护贡献边界。

补充写作素材库：本文适合提取“复杂材料机制建模”的词汇骨架。对象词包括 γ matrix channel、γ′ precipitate、dual phase microstructure、microstructurally short crack、crystallographic crack path。机制词包括 cube slip activation、octahedral slip competition、phase-sensitive fracture behavior、interface retardation、crack closure effects、temperature-dependent slip strength。方法词包括 dislocation-based CPFEM、XFEM crack growth、stored energy density、critical stored energy threshold、microstructurally faithful 3D model、quasi-3D cross-section。边界词包括 exploratory mechanistic investigation、not a quantitative life prediction tool、artificially low `Gc`、qualitative agreement、computational tractability。

可迁移段落 1：本文的 Introduction 可转化为“次级机制触发条件”模板。先说主导机制已经被广泛研究，再指出某个次级机制在特定极端条件下反复被观察到，但其触发条件和与主机制的竞争关系不清楚。然后把研究目标写成“establish the physical conditions under which X is expected to occur”。这个模板适合研究高温变形、相变、损伤、界面脱粘等现象。

可迁移段落 2：方法贡献不要只列模型组件，而要解释每个组件回答哪个物理问题。CPFEM 回答 slip activity，temperature-dependent slip properties 回答高温机制切换，XFEM 回答裂纹推进，`γs/G` 回答裂纹面选择与增长驱动力，γ-γ′ microstructure 回答相级 barrier。这样的“组件-问题”对应关系可显著降低复杂模型的阅读门槛。

可迁移段落 3：局限声明是本文最值得学的部分。作者并不回避 `Gc` 人为降低，而是明确说绝对 crack growth rates 不能解释为实验 da/dN，但 crystallographic path、slip competition 和 temperature sensitivity 由 crystal plasticity 控制，因此机制结论仍有效。这种写法的核心是把“数值量级”和“机制拓扑”分开。写自己的建模论文时，也应明确哪些输出是定量预测，哪些输出只是机制排序或路径趋势。

可迁移段落 4：实验对比可用“mechanistic consistency rather than strict quantitative validation”保护边界。若数据集缺少完全相同的 stress-temperature-orientation-microstructure 条件，不应强行写 validation，而应写“model predictions are consistent with the experimentally observed topology of crack paths”。这既诚实，也能说明模型有 benchmark 价值。

审稿回复策略：若被质疑 `Gc` 过低，可回应其目的不是预测真实循环寿命，而是在可计算时间内触发 crack advance，以便比较 slip-system-controlled path selection；路径拓扑、相界阻滞和温度驱动机制由 constitutive law 控制，不由 `Gc` 的绝对值单独决定。若被质疑微结构规则化，可承认真实 precipitate morphology 更复杂，但规则 γ-γ′ 几何能隔离 phase-level competition，是机制研究的第一步。若被要求更强验证，可建议未来实验同时报告 local orientation、temperature、stress amplitude、γ/γ′ geometry 和 crack path，用于把本文框架从 mechanistic consistency 推进到 quantitative benchmark。

最终使用提醒：这篇最适合沉淀到“机制模型不是寿命模型”的写法库。复杂材料计算经常会被要求给寿命或绝对速率，但如果模型目标是机制触发条件，就必须像本文一样提前声明预测层级：路径拓扑、机制排序、相对趋势可以讨论；绝对 da/dN 或寿命要等待专门校准。

入库标签：机制探索；次级滑移触发；相级裂纹阻滞；定性验证；寿命预测边界。

进一步可迁移提醒：这篇还适合学习如何写“工业相关但不工程化”的论文。作者多次提到 turbine blades 和 localized overstress，但没有把文章包装成直接设计工具，而是坚持机制解释。这种克制对高水平期刊很重要。
