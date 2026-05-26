# Thermoelectric enhancement in perovskite type textured Me0.85TiO3 ceramics by synergistic high-entropy and microstructure manipulations

## 0. 读取说明

- 文本来源：`801/文本/txt/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.txt`，PyMuPDF 抽取，14 页。
- 抽取文本包含摘要、实验方法、XRD/SEM/EBSD/TEM/EDX 结构表征、热电性能、机制讨论、结论和主要图表标题。
- 原文图像信息非常密集，尤其 TEM、iDPC-STEM、EDX 和机制示意图，本文仅依据文本描述分析；所有原子像、界面、缺陷簇和“brick-wall”形貌细节均标注“需要 PDF 图像复核”。

## 1. 基本信息与论文身份

- 题名：Thermoelectric enhancement in perovskite type textured Me0.85TiO3 ceramics by synergistic high-entropy and microstructure manipulations。
- 作者：Ping Zhang, Zhihao Lou, Ziyao Wei, Shuyao Cao, Qinyou An, Jianjun Gou, Chao Chen, Chunlin Gong, Hui Mei, Jie Xu, Feng Gao。
- 期刊：Chemical Engineering Journal, 494 (2024) 153186。
- 领域：氧化物热电陶瓷、高熵钙钛矿、织构陶瓷、电子-声子输运解耦、界面/缺陷调控。
- 论文类型：材料制备 + 多尺度显微表征 + 热电性能测试 + 机制解释。
- 研究对象：A 位缺位高熵 `(La0.25Sr0.25Ba0.25Ca0.25)0.85TiO3` 基 Me0.85TiO3 织构陶瓷，简称 LSBC-T。
- 主要方法：固相反应制备基体粉，加入 10 wt% Bi2O3 和 10 wt% (001) 取向 SrTiO3 片状模板种子，通过 tape casting、TGG/RTGG 和还原退火获得高织构陶瓷，再用 XRD、BSE、EBSD、TEM、HAADF/iDPC-STEM、EDX、Hall 和热电参数测试建立结构-性能链。
- 论文身份判断：这是一篇典型的 CEJ 材料机制论文，核心不是单独报告 ZT，而是把高熵、织构、液相外延生长、多尺度界面和缺陷散射串成“电子去局域化、声子局域化”的性能提升机制。

## 2. 摘要与核心信息提取

本文核心主张是：在 n 型钙钛矿氧化物热电陶瓷中，将高熵组分设计与织构工程结合，可以同时维持/增强载流子输运并降低晶格热导，从而缓解传统高熵策略“降热导但伤电导”的矛盾。最优 LSBC-T-8(‖) 样品在 1073 K 获得 ZT = 0.27，约为非织构样品 ZT = 0.13 的两倍。

摘要中的证据密度很高：织构分数 92%；1073 K 下热导约 1.79 W/(m K)；多尺度缺陷覆盖 100 GHz-15 THz 声子；平行界面包括原子尺度 (00l) 晶面、纳米 core-shell 界面、Bi sandwich layer 和 brick-wall 织构晶界；电导和热导表现出明显各向异性。作者不是只说“高熵降低热导”，而是把低热导和各向异性归因到多尺度结构。

一句话浓缩：本文用高熵 A 位缺位基体、SrTiO3 模板织构和 Bi2O3 液相/金属 Bi 缺陷工程，构建了兼顾电子传输与声子散射的 n 型高温热电陶瓷。

## 3. 选题层深拆

选题从热电材料的经典矛盾切入：高 ZT 需要高 Seebeck 系数、高电导率和低热导率，但这些参数常常通过载流子浓度和微结构耦合在一起。金属氧化物热电材料具有高温稳定、环境友好、成本低等优点，但 SrTiO3 系材料热导偏高，且电子与声子输运难以解耦。

作者进一步把问题限定到高熵钙钛矿氧化物。高熵工程能通过质量/尺寸/价态无序降低晶格热导，但也可能引入载流子迁移率下降，导致电导率和 ZT 偏低。也就是说，单纯“加无序”不是充分答案。

本文的切入点是把 high-entropy engineering 与 texture engineering 叠加：高熵提供点缺陷、晶格畸变和低热导；织构提供方向性晶界/界面，使电导和热导出现各向异性；Bi2O3 和 SrTiO3 模板种子负责促进外延生长与局部导电/散射中心生成。这使选题从“降热导”升级为“通过多尺度微结构操控实现输运解耦”。

## 4. 领域位置与文献版图

文献版图分为四块。

第一块是热电性能评价与商业/高性能材料背景，如 Bi2Te3、SnSe、PbTe 等中低温材料，用于说明热电研究的性能标尺。第二块是氧化物热电材料，特别是 SrTiO3、CaTiO3、CaMnO3、ZnO 等，强调它们的高温稳定和低成本，但也指出高热导与耦合输运限制。

第三块是高熵热电陶瓷。作者承认高熵策略已被证明能降低 lattice thermal conductivity，但同时指出其可能降低 carrier mobility。这一块文献承担“已有方法有效但不够”的功能。第四块是织构陶瓷和 RTGG/TGG 方法，包括 p 型热电陶瓷和若干 n 型 SrTiO3 基材料的织构尝试。作者用这些文献说明：制备高织构分数的 n 型立方钙钛矿热电材料仍有挑战。

本文位于这四块的交叉点：不是单纯 composition design，也不是单纯 texture fabrication，而是把成分无序、A 位缺位、模板外延生长、液相 Bi 辅助和多尺度缺陷统一到热电输运机制里。

## 5. Gap 制造机制

本文的 gap 有三层。

第一层是性能机制 gap：高熵钙钛矿能降低热导，但经常伴随电导恶化，缺少同时优化电子和声子输运的策略。第二层是制备 gap：n 型 cubic structured thermoelectric ceramics 三个晶向生长速率近似各向同性，高织构分数难以获得。第三层是表征-解释 gap：很多材料论文报告低热导或高 ZT，但没有把原子位移、氧空位、界面、析出相、晶界取向与具体声子频段散射联系起来。

作者制造 gap 的技巧是把“高熵”和“织构”各自的不足先讲清楚：高熵降低热导但会拖累 mobility；织构能带来各向异性但立方 n 型材料难织构。本文的合理性由此产生：需要一个 combined optimization strategy，而不是单一材料调控手段。

## 6. 创新性判断

- 创新类型：材料设计策略 + 多尺度微结构机制 + 高温热电性能提升。
- 真实创新点 1：制备出 `f = 92%` 的 〈001〉织构 Me0.85TiO3 高熵陶瓷，对 n 型立方钙钛矿织构制备具有方法价值。
- 真实创新点 2：用 SrTiO3 模板种子、A 位缺位 LSBC 基体和 Bi2O3 液相辅助外延生长，形成 brick-wall 织构和多尺度平行界面。
- 真实创新点 3：通过 TEM/iDPC/EDX 定量说明 A 位原子位移、[TiO6] 畸变、氧空位、Bi/BiOx 和 TiOy 等缺陷来源。
- 真实创新点 4：把缺陷/界面对应到不同频段声子散射，并解释电导/热导各向异性如何帮助 decouple electron-phonon coupling。
- 创新强度：中等偏强。ZT = 0.27 不是绝对顶级热电材料水平，但在高熵 ABO3 钙钛矿氧化物体系中具备对比优势。
- 可挑战之处：材料体系和工艺链复杂，性能提升是否主要来自织构、Bi 相关缺陷、高熵或氧空位，很难完全解耦。

## 7. 论证链条复原

全文论证链如下：

1. 热电陶瓷要提高 ZT，必须同时优化电子和声子输运。
2. SrTiO3/ABO3 氧化物适合高温应用，但高热导和耦合输运限制性能。
3. 高熵能降低热导，却可能牺牲迁移率；织构能引入各向异性，但 n 型立方结构难以高织构。
4. 本文设计 A 位缺位 LSBC 基体、SrTiO3 片状模板和 Bi2O3 助熔/导电/缺陷源，通过 tape casting + TGG/RTGG 构建高织构。
5. XRD/EBSD 证明 〈001〉织构形成，BSE/TEM/EDX 证明模板外延、Bi/TiOy 析出、氧空位和多尺度界面存在。
6. Seebeck、电阻率、Hall 和 PF 数据证明电输运被改善，且平行/垂直方向出现差异。
7. 热导和 Debye-Callaway 相关讨论证明多尺度缺陷和界面增强声子散射，热导接近 glass-like 低值。
8. ZT 对比证明最优样品达到 0.27，并优于多篇高熵 ABO3 热电陶瓷。
9. 结论回扣：高熵+织构+微结构操控可实现电子去局域化和声子局域化，从而提升热电性能。

## 8. 方法/理论/模型细拆

制备方法分三步。第一步，按 `(La0.25Sr0.25Ba0.25Ca0.25)0.85TiO3` 配比球磨、干燥、1473 K 煅烧，得到 A 位缺位高熵基体粉；加入 10 wt% Bi2O3 并高能球磨，平均粒径约 0.231 μm。第二步，用两步熔盐法制备片状 SrTiO3 微片，平均径向尺寸约 8.65 μm、厚度 1.17 μm、长厚比 7.39，作为 10 wt% 模板种子。第三步，粉体、粘结剂、增塑剂和溶剂经 tape casting 成 100 mm × 100 mm × 36 μm 绿带，层压后烧除有机物，1573 K 分别保温 4/8/16 h，再于 1673 K 还原退火 1.5 h。

表征体系有明显的尺度递进：XRD 用 Lotgering factor 量化织构；BSE/EDX 看外延层和成分梯度；EBSD/PF 证明取向集中；TEM/HAADF/iDPC 进入原子尺度，识别氧空位、A 位偏移、[TiO6] 畸变和界面；Hall 测载流子浓度/迁移率；热电测试给出 S、ρ/σ、PF、κ 和 ZT。

关键定量证据包括：LSBC-T-8 最大 texture intensity 为 11.99，是非织构样品的 9.3 倍；〈001〉方向 pole density 为 10.76 mrd，而非织构约 0.88-1.07 mrd；约 45.7% Ca2+ 偏离理想晶格位置，最大位移 184 pm，平均 131 pm；Ba2+ 和 La3+ 平均位移约 152/155 pm，Sr2+ 约 72 pm；Ti-O 键长 1.80-2.03 Å，O-Ti-O 键角 83.9°-95.3°。

理论解释依托 Mott relation 和 Debye-Callaway 散射框架。Mott relation 解释 Seebeck 与载流子浓度/迁移率能量依赖关系；热导部分用晶界散射、点缺陷散射、Umklapp 散射和电子-声子散射组合解释不同频段声子被覆盖。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| LSBC-T 可获得高 〈001〉织构 | 摘要、XRD/EBSD | 织构分数 f = 92%，texture intensity 11.99，pole density 10.76 mrd | 强 | EBSD 图像细节需要 PDF 图像复核 |
| 高熵与 A 位缺位带来显著原子位移和晶格畸变 | TEM/iDPC/EDX | Ca、Ba、La、Sr 位移定量；Ti-O 键长和键角偏离 | 强 | 原子列识别和统计区域需 PDF 复核 |
| Bi2O3 不只是烧结助剂，还参与导电和缺陷构造 | TEM/机制讨论 | Bi/BiOx cluster、TiOy、Bi sandwich layer、液相引导外延层 | 中强 | Bi 相长期稳定性未充分验证 |
| 织构使电/热输运出现各向异性 | Fig. 8-9 | σ(‖) 明显高于 σ(⊥)，κ(‖) 与 κ(⊥) 存在差异，S 方向差异小 | 强 | 各向异性对器件方向设计的外推需谨慎 |
| 多尺度缺陷覆盖宽频声子散射，导致低热导 | 机制讨论 | 缺陷覆盖 100 GHz-15 THz；κtotal 低至约 1.79 W/(m K) at 1073 K | 中强 | 频段对应主要来自模型解释而非直接声子谱测量 |
| 最优样品 ZT 翻倍 | 摘要、Fig. 9-10 | LSBC-T-8(‖) 1073 K ZT = 0.27，非织构样品 ZT = 0.13 | 强 | 绝对 ZT 仍不高，应用价值需结合高温稳定性 |
| 本文策略优于已有高熵 ABO3 热电陶瓷 | Fig. 10 | 与多篇报道 ZT 对比，显示本工作更高 | 中 | 对比需统一温度、测试方向和密度 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 1 XRD patterns | 用 (h00)/(200) 峰增强证明织构方向和保温时间影响 | 高织构形成 | 峰强、Lotgering 计算需 PDF 复核 |
| Eq. 1-3 Lotgering factor | 将“织构强”量化为 f | 织构分数 92% | 公式排版需 PDF 复核 |
| Fig. 2 BSE/EDX line scan | 展示不同保温时间、外延层和 A 位元素梯度 | 液相/模板引导外延 | 需要 PDF 图像复核 |
| Fig. 3 EBSD/Pole figures | 证明非织构随机、LSBC-T-8 〈001〉取向集中 | 织构有效 | 需要 PDF 图像复核 |
| Fig. 4-6 TEM/HAADF/iDPC/EDX | 定位氧空位、A 位位移、[TiO6] 畸变、Bi/TiOy/界面 | 多尺度缺陷机制 | 需要 PDF 图像复核 |
| Fig. 7 microstructural evolution schematic | 把制备过程解释为模板取向、液相外延、brick-wall 织构三阶段 | 机制闭环 | 需要 PDF 图像复核 |
| Eq. 7 Mott relation | 解释 Seebeck 和载流子输运关系 | 电输运解释 | 公式编号疑似与热导公式重复，需 PDF 复核 |
| Fig. 8 S/ρ/PF | 展示电性能随温度和方向变化 | PF 提升与各向异性 | 数值曲线需 PDF 复核 |
| Table 1 Hall data | 解释电导差异来自 mobility 而非浓度数量级差异 | 导电机制 | 表格抽取错列，需 PDF 复核 |
| Fig. 9 κ/ZT | 证明低热导和 ZT 翻倍 | 性能提升 | 曲线需要 PDF 图像复核 |
| Fig. 10 ZT comparison | 将本文置于高熵 ABO3 体系对比 | 外部性能定位 | 比较条件需复核 |

结果叙事安排非常典型：先证明“结构做出来了”，再证明“缺陷和界面真实存在”，然后给电性能、热性能，最后用 ZT 和文献对比收束。

## 11. 章节结构与篇章布局

文章结构是材料论文常见的 Introduction-Experimental-Results and discussion-Conclusion。真正的叙事核心在 Results and discussion，被拆成织构形成、原子尺度结构、微结构演化机制、热电性能和输运机制几层。

Introduction 的结构是“热电价值-ZT 参数耦合-氧化物优势-SrTiO3 痛点-高熵策略不足-织构策略潜力-本文工作”。Experimental 先给材料制备，再给表征方法，服务于后文多尺度证据链。

Results 部分的顺序非常值得学习：XRD/BSE/EBSD 确认宏观/介观织构，TEM/iDPC 进入微观和原子尺度，Fig. 7 用示意图把复杂表征整合成生长机制，然后再讨论热电性能。也就是说，作者先让读者相信结构机制，再让读者相信性能提升不是偶然。

标题命名偏好偏描述性，如 “Experimental section”“Results and discussion”“Conclusion”，但图题承担了大量信息密度。本文不是靠小节标题吸引读者，而是靠图题和图内证据推进论证。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：0
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：自动识别未抓到稳定章节标题，可能是 PDF 抽取换行或标题样式导致。
- 章节名主要风格：未稳定识别
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 未识别 | 描述型 | 需人工从 PDF 目录或版面核查 | 低 | 否 | 从 PDF 章节页重建标题 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 多用“先肯定、后转折”的段落节奏。作者先说氧化物稳定、SrTiO3 有高 PF 潜力，再用 “However” 转到高热导和耦合关系；再说高熵可以降低热导，又用 “However” 指出 mobility 和 ZT 受限；最后用 textured ceramics 引出解耦机会。

方法段落信息密集，典型节奏是“材料配方-工艺条件-命名规则-表征指标”。这类段落不追求修辞，而追求可复现。

结果段落则多采用“图像观察-定量指标-机制解释”的三步：例如 EBSD 后给 texture intensity 和 pole density；iDPC 后给原子位移和键角；热电性能后给 PF/κ/ZT，再连接到 Bi、界面和高熵缺陷。

Discussion 的节奏是从局部机制上升到总机制：多尺度缺陷增强声子散射，平行界面制造各向异性，最终实现 delocalization of electrons and localization of phonons。

## 13. 文笔画像与语言习惯

本文语言具有材料机制论文的“高密度名词串”特征：high-entropy textured ceramics、A-site deficient、multi-scale parallel interfaces、electron-phonon coupling、brick-wall morphology 等短语反复出现，形成明确术语场。

作者常用强机制动词：enhance、suppress、decouple、facilitate、promote、manipulate、reveal、clarify。与单胞论文的克制规范语不同，这篇更偏材料性能论文，claim 强度更高。

时态上，制备和表征结果多用过去时；机制规律和材料属性多用一般现在时；结论中用 “provides”“presents”“clarified” 同时表达理论基础和技术支持。被动语态很多，尤其在实验方法和图像结果描述中；主动语态主要出现在贡献声明。

形容词/副词使用较多，如 significant、remarkable、obvious、unique、complex、synergistic。这能增强材料故事性，但也带来审稿风险：每个强修饰词最好有定量数据支撑。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：textured(88)；ceramics(77)；high-entropy(61)；thermoelectric(56)；org(52)；lsbc-t(51)；srtio(48)；grain(48)；lsbc-t-(43)；matrix(36)；ceramic(35)；conductivity(34)；thermal(33)；zhang(32)；template(31)；growth(29)；phonon(28)；grains(27)；phase(26)；engineering(25)
- 高频学术名词：structure(40)；conductivity(34)；analysis(30)；mechanism(24)；performance(22)；results(21)；texture(21)；energy(20)；temperature(19)；transition(18)；properties(18)；microstructure(18)；materials(17)；interfaces(16)；addition(15)；method(13)
- 高频学术动词：shown(14)；compared(7)；shows(7)；demonstrated(4)；reveal(3)；revealed(2)；estimated(1)；show(1)；captured(1)；propose(1)；investigate(1)；developed(1)
- 高频形容词：thermoelectric(56)；ceramic(35)；thermal(33)；electrical(21)；high(20)；atomic(20)；chemical(19)；low(16)；total(16)；material(11)；large(10)；epitaxial(10)；displacement(9)；crystal(9)；different(9)；supplementary(9)
- 高频副词/连接副词：furthermore(10)；significantly(8)；therefore(5)；highly(5)；respectively(5)；however(4)；effectively(4)；mainly(4)；specifically(3)；simultaneously(3)；greatly(3)；continuously(3)；substantially(2)；approximately(2)；notably(2)；strongly(2)
- 高频二词短语：textured ceramics(32)；thermal conductivity(25)；chemical engineering(15)；template seeds(14)；lsbc-t textured(14)；template seed(13)；thermoelectric performance(13)；zhang chemical(13)；high-entropy matrix(13)；srtio template(13)；textured grains(12)；electron phonon(11)；high-entropy textured(11)；textured ceramic(10)；grain boundaries(9)；electrical conductivity(9)
- 高频三词短语：zhang chemical engineering(13)；lsbc-t textured ceramics(12)；srtio template seed(7)；high-entropy textured ceramics(6)；srtio template seeds(6)；writing review editing(6)；electrical thermal conductivity(5)；electron phonon coupling(5)；lsbc high-entropy matrix(5)；chem eng org(5)；state key laboratory(4)；multi-scale parallel interfaces(4)

**主动、被动与句法**

- 被动语态估计次数：100
- `we + 动作动词` 主动句估计次数：0
- 名词化表达估计次数：742
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：56
- 一般过去时线索：163
- 现在完成时线索：13
- 情态动词线索：32
- 时态判断：过去时相对突出，说明文本中实验/仿真步骤和已完成操作占比较高；现在时仍用于图表说明和一般性判断。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- 全文：textured(88)；ceramics(77)；high-entropy(61)；thermoelectric(56)；org(52)；lsbc-t(51)；srtio(48)；grain(48)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

高频术语：textured ceramics, high-entropy, SrTiO3 template seeds, thermal conductivity, thermoelectric performance, grain growth, electron-phonon coupling, phonon scattering, A-site deficient。

可复用 gap 句式：

- “High-entropy engineering can effectively lower κ, but also cause the deterioration of carrier mobility.”
- “Preparing n-type cubic structured thermoelectric materials with a high texture fraction remains a significant challenge.”
- “It is urgent to propose a combined optimization strategy encompassing entropy engineering and interfacial engineering.”

可复用机制句式：

- “The combined effect of the aforementioned factors results in...”
- “These multi-scale defects act as additional phonon scattering centers while affecting carrier transport.”
- “By employing a strategy that involves the delocalization of electrons and the localization of phonons...”

可复用结果句式：

- “A peak ZT of X was attained at Y K, which was twice that of...”
- “The results provided direct verification for...”
- “The optimal value obtained in this work exhibits superior performance when compared to reported data...”

## 15. 引用策略与文献使用

引用主要服务四个功能：定义热电指标和材料背景；说明氧化物热电和 SrTiO3 系的优势/不足；铺垫高熵、缺陷、织构和 RTGG/TGG 技术；最后在 Fig. 10 中进行 ZT 横向对比。

作者对前人采取“拼图式继承”策略。高熵文献提供低热导逻辑，织构文献提供各向异性逻辑，SrTiO3 文献提供高 PF 和稳定性逻辑，缺陷/声子散射文献提供机制解释。本文把这些拼图组合成一个更复杂的材料设计方案。

gap 的引用连接比较自然：不是说某一篇文献错，而是说单一策略都有短板。这样一来，本文的“synergistic manipulations”显得必要。

## 16. 审稿人视角风险

1. 归因过密风险：高熵、A 位缺位、Bi2O3、SrTiO3 模板、氧空位、TiOy、Bi/BiOx、织构晶界同时存在，单独变量贡献不易拆分。
2. 绝对性能风险：ZT = 0.27 虽在高熵 ABO3 中有优势，但与商业或高性能热电材料相比仍低，应用表述需控制。
3. 稳定性风险：Bi 金属/氧化物簇和还原态 Ti 相关缺陷在长期高温循环中的稳定性未充分展示。
4. 方向性风险：平行方向性能最好，但实际器件能否利用该方向性，需要器件结构设计支持。
5. 表征代表性风险：TEM/iDPC 区域是否能代表整体样品，需要更多统计支撑。
6. 对比风险：Fig. 10 的文献 ZT 对比需要统一温度、氧分压、测量方向和样品密度，否则可能被审稿人质疑。
7. 图像依赖风险：大量机制依赖原子图像和界面图，必须 PDF 图像复核。

## 17. 可复用资产

- 选题资产：把“单一策略有副作用”转化为“协同调控”的选题逻辑。
- Gap 资产：高熵降热导但伤 mobility；织构可解耦但立方 n 型难织构。
- 方法资产：用制备工艺、织构定量、原子尺度表征、输运测试组成完整证据链。
- 图表资产：XRD 织构图、EBSD pole figure、TEM/iDPC 原子图、EDX 元素图、微结构演化示意图、S/ρ/PF/κ/ZT 性能图、ZT 文献对比图。
- 机制资产：delocalized electrons + localized phonons 的总结框架。
- 写作资产：每个强性能 claim 都配一个定量指标和一个结构机制。

## 18. 对我写论文的启发

如果写材料性能论文，可以学习本文的“结构证据先行”顺序。先证明材料确实形成了目标结构，再解释该结构如何影响输运，最后给性能提升。这样比一开始直接展示 ZT 更有说服力。

第二个启发是，复杂机制可以通过“尺度层级”来组织：宏观织构、介观晶粒、纳米析出相、原子位移、声子频段。层级清楚后，即使材料体系很复杂，读者仍能跟上论证链。

第三个启发是，要主动防止贡献被看成“堆工艺”。本文用 Fig. 7 的演化机制和 Fig. 9-10 的性能闭环，把工艺、结构和性能串在一起，这是材料论文最值得模仿的地方。

## 19. 最终浓缩

这篇论文最值得学习的是它把高熵、织构和多尺度缺陷从多个分散手段组织成一条热电输运解耦链：高熵和缺位制造低热导，模板和液相促进高织构，平行界面引入各向异性，Bi/TiOy/氧空位等缺陷增强声子散射，最终把 LSBC-T-8(‖) 的 ZT 推到 0.27。

最大风险是机制归因过于复合，许多结构因素同时变化，单因子贡献和长期稳定性仍需更直接验证。

可迁移到自己论文中的三件事：第一，用“单一策略短板”制造协同调控 gap；第二，用多尺度表征构造机制证据链；第三，性能提升必须同时回答“数值提高多少”和“为什么会提高”。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.txt` 与 `801/文本/metadata/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 Experimental section （对象/问题/模块）
  - L3 p.2: 2.1 Materials and method （方法/模型）
  - L3 p.3: 2.2 Characterization （对象/问题/模块）
- L2 p.3: 3 Results and discussion （结果/讨论/验证）
- L2 p.12: 4 Conclusion （结论）
- L2 p.12: CRediT authorship contribution statement （对象/问题/模块）
- L2 p.12: Declaration of competing interest （对象/问题/模块）
- L2 p.12: Data availability （对象/问题/模块）
- L2 p.12: Acknowledgements （对象/问题/模块）
- L2 p.13: Appendix A Supplementary data （附录）
- L2 p.13: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Experimental section | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Materials and method | 2 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Characterization | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Results and discussion | 3 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Conclusion | 12 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| CRediT authorship contribution statement | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Declaration of competing interest | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Data availability | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 12 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Appendix A Supplementary data | 13 | 2 | 附录 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 13 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 提高热电陶瓷的品质因数（ZT）本质上需要旨在同时优化电子和声子传输特性以解耦它们的耦合关系的策略。该工作采用流延工艺结合模板晶粒生长法制备了<001>织构的Me0.85TiO3(Me=La,Sr,Ba,Ca)陶瓷(LSBC-T)，其织构分数为92%，其中10wt%(001)取向的板状SrTiO3作为模板种子，A位缺陷高熵材料采用(La0.25Sr0.25Ba0.25 Ca0.25)0.85TiO3复合材料作为基体材料。平行于流延方向的样品在 1073 K 处达到 0.27 的峰值 ZT，这是无纹理样品的 ZT = 0.13 的两倍。 A位元素原子位移无序的定量分析将提供对晶粒取向演化的原子尺度理解，该晶粒取向演化具有高织构度和1073 K时1.79 W/(m‧K)的低热导率。复杂的多尺度缺陷包括阳离子和氧空位、边缘位错、平行晶界、相界面、纳米级金属/无机共存团簇和金属Bi夹层，它们在影响载流子的同时充当额外的声子散射中心传输，涵盖所有频率声子（100 GHz-15 THz）。
> 
> 此外，多尺度平行界面，包括SrTiO3晶种的原子级晶体(00l)面、平行于(00l)面的纳米级“核壳”界面、在SrTiO3晶种中形成夹层的金属Bi粒子以及“砖墙”织构晶界，使得LSBC-T高熵织构陶瓷的电导率和导热率表现出明显的各向异性。该工作通过利用高熵系统中的织构工程，为微观结构操控的进展提供理论基础和技术支撑，以降低固有的晶格导热系数，实现电导率和导热率各向异性以解耦电子-声子耦合关系，从而增强热电性能。

### 20.5 结论完整摘录（本地证据）

结论章节识别：4 Conclusion；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/Thermoelectric-enhancement-in-perovskite-type-textured-Me0_2024_Chemical-Eng.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 以缺A位(La0.25Sr0.25Ba0.25Ca0.25)0.85TiO3为基体材料，以10wt%(001)取向SrTiO3为模板种子，采用(R)TGG结合流延法成功制备了f=92%的钙钛矿Me0.85TiO3(Me=La、Sr、Ba、Ca)基织构陶瓷。在A位缺陷高熵中构建和操纵了独特的晶粒取向微观结构、纳米尺寸的Bi/BiOx团簇以及多尺度界面和分级缺陷

### 20.7 论文逻辑脉络复核

- 提出的问题：Enhancing the figure-of-merit (ZT) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship. There is a great demand for thermoelectric material candidates that possess * Corresponding authors. Contents lists available at ScienceDirect Chemical Engineering Journal journal homepage: www.elsevier.com/locate/cej Enhancing the figure-of-merit (ZT) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship.
- 旧方法/已有研究不足：需结合 Introduction 的文献转折句复核。
- 本文解决方式：This work developed 〈001〉-textured Me0.85TiO3(Me = La, Sr, Ba, Ca) ceramics (LSBC-T) with a texture fraction of 92 % fabricated by a tape casting process combined with template grain-growth method, in which 10 wt% (001) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.25Sr0.25Ba0.25 Ca0.25)0.85TiO3 composite was used as matrix material. This work developed 〈001〉-textured Me0.85TiO3(Me = La, Sr, Ba, Ca) ceramics (LSBC-T) with a texture fraction of 92 % fabricated by a tape casting process combined with template grain-growth method, in which 10 wt% (001) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.25Sr0.25Ba0.25 Ca0.25)0.85TiO3 composite was used as matrix material. In addition, multi-scale parallel interfaces, including atomic-scale crystal (00l) plane of SrTiO3 seed, nano-scale “core-shell” The perovskite Me0.85TiO3(Me = La, Sr, Ba, Ca) based textured ce ramics with f = 92 % were successfully prepared by (R)TGG combined with tape casting method through matrix materials of A-site deficient (La0.25Sr0.25Ba0.25Ca0.25)0.85TiO3 and template seeds of 10 wt% (001) oriented SrTiO3.
- 学术/工程增量：Quantitative analysis of atomic displacement disorder of A-site elements would provide an atomistic-scale understanding of grain orientation evolution with high texture degree and the low thermal conductivity of 1.79 W/(m‧K) at 1073 K. By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties. The global energy system has begun to transition from fossil fuels to clean energy, thermoelectric conversion has attracted considerable attention for its potential to achieve effective, multi-level energy man agement, offering a promising solution to address the escalating energy crisis [1–3].
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：89
- Introduction 引用簇数量（估计）：24
- References 条目数（解析）：51
- 可识别年份条目数：76
- 近五年/近年文献（2021+）数量：29
- 经典文献（2010年前）数量：10
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：未识别
- 引用簇样例：[4,5], [6,7], [8,9], [10], [11], [12], [13], [14], [15], [16], [17], [18]

带引用的 gap/转折句样例：

- However, its high thermal conductivity, specifically κ = 11 W/(m‧ K) at 300 K for single crystal [19] and ranges from 7.16 to 2.89 W/(m‧K) for polycrystalline bulk systems over 300 K to 1073 K [20], combined with the isotropic electron and phonon coupling relationship pose challenges in enhancing the ZT value.

References 解析样例（前12条）：

- [1] Q.Y. Yan, M.G. Kanatzidis, High-performance thermoelectrics and challenges for practical devices, Nat. Mater. 21 (5) (2022) 503–513, https://doi.org/10.1038/ s41563-021-01109-w.
- [2] M. Zebarjadi, K. Esfarjani, M.S. Dresselhaus, Z.F. Ren, G. Chen, Perspectives on thermoelectrics: from fundamentals to device applications, Energy Environ. Sci. 5 (1) (2012) 5147–5162, https://doi.org/10.1039/C1EE02497C.
- [3] S. Twaha, J. Zhu, Y.Y. Yan, B. Li, A comprehensive review of thermoelectric technology: materials, applications, modelling and performance improvement, Renew. Sust. Energy Rev. 65 (2016) 698–726, https://doi.org/10.1016/j. rser.2016.07.034.
- [4] I.T. Witting, T.C. Chasapis, F. Ricci, M. Peters, N.A. Heinz, G. Hautier, G.J. Snyder, The thermoelectric properties of Bismuth Telluride, Adv. Electron. Mater. 5 (6) (2019) 1800904, https://doi.org/10.1002/aelm.201800904.
- [5] B. Zhu, X.X. Liu, Q. Wang, Y. Qiu, Z. Shu, Z.T. Guo, Y. Tong, J. Cui, M. Gu, J.Q. He, Realizing record high performance in n-type Bi2Te3-based thermoelectric materials, Energy Environ. Sci. 13 (7) (2020) 2106–2114, https://doi.org/ 10.1039/D0EE01349H.
- [6] H.X. Wang, C. Tan, Y.Q. Sun, A. Abbas, Z.H. Li, C.L. Wang, H.C. Wang, Enhanced thermoelectric performance in cubic SnSe-based alloys via manipulation of grain boundary scattering and phonon transport, Chem. Eng. J. 480 (2024) 148002, https://doi.org/10.1016/j.cej.2023.148002.
- [7] B.C. Qin, D.Y. Wang, T. Hong, Y.P. Wang, D.R. Liu, Z.Y. Wang, X. Gao, Z.H. Ge, L. D. Zhao, High thermoelectric efficiency realized in SnSe crystals via structural modulation, Nat. Commun. 14 (2023) 1366, https://doi.org/10.1038/s41467-02337114-7.
- [8] J.P. Heremans, V. Jovovic, E.S. Toberer, A. Saramat, K. Kurosaki, A. Charoenphakdee, S. Yamanaka, G.J. Snyder, Enhancement of thermoelectric efficiency in PbTe by distortion of the electronic density of states, Science 321 (5888) (2008) 554–557, https://doi.org/10.1126/science.1159725.
- [9] H.T. Liu, Q. Sun, Y. Zhong, C.L. Xia, Y. Chen, Z.G. Chen, R. Ang, Achieving highperformance n-type PbTe via synergistically optimizing effective mass and carrier concentration and suppressing lattice thermal conductivity, Chem. Eng. J. 428 (2022) 132601, https://doi.org/10.1016/j.cej.2021.132601.
- [10] S. Saini, H.S. Yaddanapudi, K. Tian, Y.N. Yin, D. Magginetti, A. Tiwari, Terbium ion doping in Ca3Co4O9: A step towards high-performance thermoelectric materials, Sci. Rep. 7 (2017) 44621, https://doi.org/10.1038/srep44621.
- [11] S. Tajima, T. Tani, S. Isobe, K. Koumoto, Thermoelectric properties of highly textured NaCo2O4 ceramics processed by the reactive templated grain growth (RTGG) method, Mater. Sci. Eng. B 86 (1) (2001) 20–25, https://doi.org/10.1016/ S0921-5107(01)00633-X.
- [12] Y. Liu, L.D. Zhao, Y.C. Zhu, Y.C. Liu, F. Li, M.J. Yu, D.B. Liu, W. Xu, Y.H. Lin, C. W. Nan, Synergistically optimizing electrical and thermal transport properties of BiCuSeO via a dual-doping approach, Adv. Energy Mater. 6 (9) (2016) 1502423, https://doi.org/10.1002/aenm.201502423.

### 20.9 常用词、词类、语态与时态

- 高频词：ceramics(19)；thermoelectric(18)；textured(18)；conductivity(14)；high-entropy(12)；thermal(12)；tio(11)；engineering(10)；srtio(10)；materials(9)；lsbc-t(9)；matrix(9)；phonon(8)；electrical(8)；its(8)；electron(7)；texture(7)；process(7)；grain(7)；high(7)
- 高频名词化/学术名词：ceramics(19)；conductivity(14)；texture(7)；performance(7)；orientation(5)；structure(5)；microstructure(4)；university(4)；relationship(4)；fraction(4)；direction(4)；evolution(4)；information(3)；enhance(3)；stability(3)
- 高频学术动词：reveal(2)；optimize(1)；developed(1)；demonstrated(1)；optimized(1)；propose(1)
- 高频形容词：thermoelectric(18)；thermal(12)；electrical(8)；chemical(6)；journal(5)；material(5)；metal(5)；ceramic(4)；available(3)；deficient(3)；potential(3)；isotropic(3)；supplementary(3)；polytechnical(2)；crystal(2)
- 高频副词：effectively(3)；specifically(3)；significantly(2)；subsequently(2)；highly(2)；essentially(1)；rently(1)；substantially(1)；commercially(1)；family(1)；remarkably(1)；comprehensively(1)；additionally(1)；simultaneously(1)；greatly(1)
- 高频二词短语：thermal conductivity(10)；textured ceramics(7)；electron phonon(6)；thermoelectric performance(5)；chemical engineering(4)；engineering journal(4)；key laboratory(4)；coupling relationship(4)；texture fraction(4)；tape casting(4)；matrix material(4)；electrical conductivity(4)
- 高频三词短语：chemical engineering journal(4)；electrical thermal conductivity(3)；electron phonon coupling(3)；textured tio ceramics(2)；state key laboratory(2)；polytechnical university china(2)；electron phonon transport(2)；oriented plate-like srtio(2)；high-entropy textured ceramics(2)；lattice thermal conductivity(2)；phonon coupling relationship(2)；page zhang chemical(2)
- 被动语态估计：29；`we + 动作动词` 主动句估计：0
- 一般现在时线索：13；一般过去时线索：138；现在完成时线索：4；情态动词线索：8

章节词频：

- Abstract: parallel(4)；thermal(4)；conductivity(4)；ceramics(3)；phonon(3)；textured(3)；texture(3)；srtio(3)
- Introduction: thermoelectric(16)；ceramics(14)；conductivity(14)；textured(12)；thermal(12)；phonon(8)；electrical(8)；engineering(7)
- Conclusion: phonon(4)；high-entropy(3)；electron(3)；perovskite(2)；tio(2)；textured(2)；a-site(2)；deficient(2)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 原句/结构：Enhancing the figure-of-merit (ZT) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship.
  可迁移模板：Enhancing the figure-of-merit (METHOD) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship.
- 原句/结构：Contents lists available at ScienceDirect Chemical Engineering Journal journal homepage: www.elsevier.com/locate/cej Enhancing the figure-of-merit (ZT) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship.
  可迁移模板：Contents lists available at ScienceDirect Chemical Engineering Journal journal homepage: www.elsevier.com/locate/cej Enhancing the figure-of-merit (METHOD) for thermoelectric ceramics essentially needs strategies that aim to concur rently optimize electron and phonon transport properties to decouple their coupling relationship.
#### Gap句
- 原句/结构：However, its high thermal conductivity, specifically κ = 11 W/(m‧ K) at 300 K for single crystal [19] and ranges from 7.16 to 2.89 W/(m‧K) for polycrystalline bulk systems over 300 K to 1073 K [20], combined with the isotropic electron and phonon coupling relationship pose challenges in enhancing the ZT value.
  可迁移模板：However, its high thermal conductivity, specifically κ = METHOD/(m‧ K) at METHOD for single crystal [X] and ranges from Xto METHOD/(m‧K) for polycrystalline bulk systems over METHOD to METHOD [X], combined with the isotropic electron and phonon coupling relationship pose challenges in enhancing the METHOD value.
- 原句/结构：However, perovskite structure poly crystalline ceramics usually have equiaxed grains and isotropic physical properties.
  可迁移模板：However, perovskite structure poly crystalline ceramics usually have equiaxed grains and isotropic physical properties.
- 原句/结构：The strong coupling relationship between electrical and thermal transport properties, which depends on carrier concentration, it is often possible to improve electrical conductivity while deteriorating thermal conductivity and vice versa, making it became a huge challenge to achieve breakthroughs in ZT.
  可迁移模板：The strong coupling relationship between electrical and thermal transport properties, which depends on carrier concentration, it is often possible to improve electrical conductivity while deteriorating thermal conductivity and vice versa, making it became a huge challenge to achieve breakthroughs in METHOD.
#### 方法句
- 原句/结构：This work developed 〈001〉-textured Me0.85TiO3(Me = La, Sr, Ba, Ca) ceramics (LSBC-T) with a texture fraction of 92 % fabricated by a tape casting process combined with template grain-growth method, in which 10 wt% (001) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.25Sr0.25Ba0.25 Ca0.25)0.85TiO3 composite was used as matrix material.
  可迁移模板：This work developed 〈X〉-textured Me0.XTiO3(Me = La, Sr, Ba, Ca) ceramics (METHOD-T) with a texture fraction of X fabricated by a tape casting process combined with template grain-growth method, in which Xwt% (X) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.XSr0.XBa0.XCa0.X)XTiO3 composite was used as matrix material.
- 原句/结构：This work developed 〈001〉-textured Me0.85TiO3(Me = La, Sr, Ba, Ca) ceramics (LSBC-T) with a texture fraction of 92 % fabricated by a tape casting process combined with template grain-growth method, in which 10 wt% (001) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.25Sr0.25Ba0.25 Ca0.25)0.85TiO3 composite was used as matrix material.
  可迁移模板：This work developed 〈X〉-textured Me0.XTiO3(Me = La, Sr, Ba, Ca) ceramics (METHOD-T) with a texture fraction of X fabricated by a tape casting process combined with template grain-growth method, in which Xwt% (X) oriented plate-like SrTiO3 serves as template seed and A-site deficient high-entropy (La0.XSr0.XBa0.XCa0.X)XTiO3 composite was used as matrix material.
- 原句/结构：Dense and highly textured ceramics with typical perovskite-type struc ture can be successfully fabricated via the reactive templated grain growth (RTGG) method [33,34].
  可迁移模板：Dense and highly textured ceramics with typical perovskite-type struc ture can be successfully fabricated via the reactive templated grain growth (METHOD) method [X,X].
#### 结果句
- 原句/结构：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties.
  可迁移模板：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties.
- 原句/结构：The global energy system has begun to transition from fossil fuels to clean energy, thermoelectric conversion has attracted considerable attention for its potential to achieve effective, multi-level energy man agement, offering a promising solution to address the escalating energy crisis [1–3].
  可迁移模板：The global energy system has begun to transition from fossil fuels to clean energy, thermoelectric conversion has attracted considerable attention for its potential to achieve effective, multi-level energy man agement, offering a promising solution to address the escalating energy crisis [X–X].
- 原句/结构：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties. high Seebeck coefficients (S), superior electrical conductivity (σ), lower thermal conductivity (κ), and can be applied to a wide temperature range with excellent high-temperature stability.
  可迁移模板：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties. high Seebeck coefficients (S), superior electrical conductivity (σ), lower thermal conductivity (κ), and can be applied to a wide temperature range with excellent high-temperature stability.
#### 贡献句
- 原句/结构：Quantitative analysis of atomic displacement disorder of A-site elements would provide an atomistic-scale understanding of grain orientation evolution with high texture degree and the low thermal conductivity of 1.79 W/(m‧K) at 1073 K.
  可迁移模板：Quantitative analysis of atomic displacement disorder of A-site elements would provide an atomistic-scale understanding of grain orientation evolution with high texture degree and the low thermal conductivity of METHOD/(m‧K) at METHOD.
- 原句/结构：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties.
  可迁移模板：By utilizing texture engineering in high-entropy systems, this work provides a theoretical foundation and technical support for the advancement of microstructure manipulations to reduce the inherent lattice thermal conductivity, achieve electrical and thermal conductivity anisotropy to decouple the electron–phonon coupling relationship, and thereby enhance thermo electric properties.
- 原句/结构：Quantitative analysis of atomic displacement disorder of A-site elements would provide an atomistic-scale understanding of grain orientation evolution with high texture degree and the low thermal conductivity of 1.79 W/(m‧K) at 1073 K.
  可迁移模板：Quantitative analysis of atomic displacement disorder of A-site elements would provide an atomistic-scale understanding of grain orientation evolution with high texture degree and the low thermal conductivity of METHOD/(m‧K) at METHOD.
#### 限制/边界句
- 原句/结构：Gao). https://doi.org/10.1016/j.cej.2024.153186 Received 24 March 2024; Received in revised form 18 May 2024; Accepted 14 June 2024 Available online 16 June 2024 1385-8947/© 2024 Elsevier B.V.
  可迁移模板：Gao). https://doi.org/X/j.cej.XReceived XMarch X; Received in revised form XMay X; Accepted XJune XAvailable online XJune METHOD-X/© XElsevier B.V.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
