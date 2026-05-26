# A solar radiant heating apparatus for measuring the thermal behavior of silica fiber phenolic composite for thermal protection applications

## 0. 读取说明

本拆解基于 `801/文本/txt/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.txt`。文本抽取可确认实验装置、材料配比、耦合模型、主要图表和结论；但装置照片、试样形貌、切片显微结构和曲线细节需要 PDF 图像复核。由于该文包含 experimental apparatus、数学模型和材料热响应三条线，拆解重点放在“实验平台如何支撑模型验证”。

## 1. 基本信息与论文身份

- 题名：A solar radiant heating apparatus for measuring the thermal behavior of silica fiber phenolic composite for thermal protection applications
- 作者：Shengbo Shi, Fajun Yi, Shuo Tang, Chunlin Gong, Yifan Wang
- 期刊与年份：Applied Thermal Engineering, 106, 2016, 236-243
- 领域：热防护材料测试、太阳辐照加热、硅纤维/酚醛复合材料、烧蚀/热解建模
- 论文类型：实验装置开发 + 材料热响应测试 + 耦合温度-扩散-膨胀模型验证
- 研究对象：silica fiber reinforced phenolic composite，试样约 10 mm × 10 mm × 15 mm。
- 主要方法：Fresnel lens + prism 二次汇聚太阳光产生高辐射热流；热电偶测温；热暴露后毫米切片测热影响区；SEM 观察；建立 temperature-diffusion-expansion 模型。
- 主要证据：装置示意/照片、试样表面形貌、切片密度剖面、温度曲线、分解度、气体质量通量和显微结构。

这篇论文不是单纯测试材料烧蚀率，而是把低成本全光谱太阳辐照装置、可测数据和数值模型验证组合成一个实验方法贡献。

## 2. 摘要与核心信息提取

摘要首先强调装置：阳光经 Fresnel lens 一次汇聚，再由 prism 二次汇聚，能在短时间产生已知高热流。随后说明测量：热电偶监测深度温度，热暴露后切片确定热影响区厚度。最后给出模型：建立多孔材料温度-扩散-膨胀耦合模型，并用实验数据验证。

一句话主张：作者开发了一套低成本全光谱太阳辐射高热流实验台，并用它获取硅纤维酚醛复合材料的温度、热影响区和微观结构数据，从而验证耦合热解-扩散-膨胀模型。

核心信息：

- 装置可产生最高约 4 MW/m2 的辐射热流。
- 装置成本约 25,000 美元，低于文中比较的 oxyacetylene torch、arc-jet wind tunnel 和 plasma wind tunnel。
- 热影响区深度随加热时间从约 8.27 mm (100 s) 增至约 11.97 mm (200 s)。
- 结论强调全光谱加热、低成本易维护、模型能预测一侧热流下 FRP 热响应、材料从炭化层到热解区到原始材料的行为变化清晰。

## 3. 选题层深拆

选题来自热防护材料验证的实验瓶颈。高超声速/再入环境下，材料会发生不可逆物理化学过程；数值模型需要准确实验数据；但 arc-jet、plasma tunnel 等装置昂贵且复杂，氧乙炔火焰又可能改变流场和边界。

作者把问题收束为“能否设计一种低成本、全光谱、短时间高热流、边界可控的太阳辐照实验装置，并产生可用于模型验证的深度温度与热影响区数据”。这个问题定义有两个优点：装置目标可衡量，数据用途也明确。

选题价值主要是实验方法价值和模型验证价值。对于热防护材料研究，装置本身就是基础设施；如果能降低成本并给出可复现实验流程，会有较强迁移性。

## 4. 领域位置与文献版图

文献版图按加热方式和材料响应模型组织：

- 高温加热测试：arc heated wind tunnel、high frequency plasma wind tunnel、oxyacetylene torch，可产生高热流但成本高或边界复杂。
- 电/磁加热：induction heating、electric resistance heating，可研究热机械行为，但热流不均且难实现一侧加热边界。
- 辐射加热：laser、carbon arc、resistance furnace、tungsten filament lamps 等可控，但非全光谱，材料吸收率波段差异会影响热流。
- 复合材料热解模型：已有模型关注温度、热解、气体扩散、热化学膨胀，但需要实验数据校准。

本文站位是“测试平台补缺 + 模型验证”。它不是为了替代 arc-jet 的全部功能，而是提供一种可经济地产生高辐射热流并获取材料响应数据的方法。

## 5. Gap 制造机制

作者的 gap 通过“现有装置不满足理想测试条件”制造：

- 成本 gap：arc-jet/plasma tunnel 成本和操作复杂度高。
- 光谱 gap：常用辐射源不是全光谱，可能因材料波段吸收差异导致热流偏差。
- 边界 gap：某些加热方法热流不均，无法稳定实现 one-sided heating boundary condition。
- 数据 gap：热解模型需要温度剖面和热影响区厚度等实验数据。

gap 的可信度较强，因为作者不仅指出限制，还给出成本对比和装置能力。风险是太阳辐照依赖天气、太阳角度和校准条件，论文需要说明可重复性和不确定度；文本中这部分相对简略。

## 6. 创新性判断

作者声明的创新包括全光谱太阳辐射高热流装置、二次汇聚设计、热响应实验数据和耦合 TDE 模型。

真实创新判断：

- 装置创新：较强。Fresnel lens + prism 的全光谱、低成本高热流平台是核心卖点。
- 数据创新：中等。提供深度温度、密度/热影响区和 SEM 观察，用于模型验证。
- 模型创新：中等。耦合温度、扩散、热化学膨胀，更多是整合已有物理项。
- 写作创新：中等。Highlights 和 Graphical abstract 提前打出“装置价值”。

创新最容易被质疑的是装置与真实再入气动热环境的等效性：太阳辐照可模拟辐射热流，但不能替代剪切、气动压力、化学非平衡等环境。

## 7. 论证链条复原

论证链条：

热防护材料在高温下发生复杂热解/烧蚀，模型需要准确实验边界和数据 -> 现有高热流装置昂贵、复杂或光谱/边界不理想 -> 太阳光是全光谱能源，若二次汇聚可形成高辐射热流 -> 设计装置并校准热流，将试样一侧加热，测深度温度并切片确定热影响区 -> 建立温度-扩散-膨胀耦合模型 -> 用实验温度剖面、密度剖面、分解度、气体质量通量和微观形貌验证模型 -> 得出该装置经济有效且材料热行为层化明显。

逻辑闭合较好。最强环节是装置-数据-模型之间的闭环。薄弱环节是实验重复性、不确定度和与真实气动热环境的相似准则。

## 8. 方法/理论/模型细拆

实验装置：

- Fresnel lens：80 cm × 80 cm，焦距约 130 cm，用于一次汇聚太阳光。
- Prism：K9 glass，用于二次汇聚。
- 测量系统：热电偶温度测量、热流校准系统、陶瓷管/石墨夹具/铝片反射以实现一侧加热边界。
- 能力：短时间产生最高约 4 MW/m2 辐射热流。

实验流程：

1. 调整装置使太阳光垂直入射试样。
2. 用隔热板在调节阶段保护试样。
3. 施加高热流后记录不同深度温度。
4. 热暴露后沿厚度方向毫米切片，计算密度剖面并判断炭化层、热解区、原始材料。
5. SEM 观察不同切片微观形貌。

模型：

- 能量守恒：考虑固相/气相热容、热传导、气体流动携热、热解吸热等。
- 质量转化：纤维、聚合物、炭、孔隙/气体相之间转化。
- 热化学膨胀：通过分解度和实验膨胀因子描述。
- 气体扩散：多孔骨架中热解气体流动，采用 Darcy law。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 太阳辐照装置能产生高热流且成本低 | Highlights、2.1、结论 | 最高约 4 MW/m2；成本约 25,000 美元，与其他装置成本比较 | 强 | 需复核热流校准不确定度和天气依赖 |
| 装置可提供模型验证数据 | 摘要、2.2、4 | 热电偶温度、切片热影响区、密度剖面、SEM 图像 | 强 | 样本数量和重复性文本不充分 |
| TDE 模型能预测材料热响应 | 摘要、4、结论 | 计算温度剖面与实验值比较；Fig. 8 | 中-强 | 曲线吻合程度需要 PDF 图像复核 |
| 热影响区随加热时间增厚 | 4 | 热影响区深度约 8.27 mm (100 s) 到 11.97 mm (200 s) | 强 | 由切片/分解度判定，边界识别有误差 |
| 材料热行为呈炭化层-热解区-原始材料层化 | 4、结论 | 切片密度、形貌、SEM Fig. 6-Fig. 11 | 强 | 图像细节需要 PDF 图像复核 |
| 全光谱辐射更适合理论测试高温行为 | 2.1、结论 | 与非全光谱辐射源对比，指出吸收率波段差异问题 | 中 | 需要光谱实测或吸收率数据加强 |

## 10. 图表、公式与结果叙事提取

- Fig. 1：装置与仪器示意，承担方法框架图功能。
- Fig. 2：太阳辐照实验装置照片，支撑装置可实现性；需要 PDF 图像复核。
- Fig. 3：FRP 高温响应示意，解释温度、热解、气体扩散、膨胀耦合机制。
- Fig. 5：热暴露后表面形貌，证明表面炭化和材料变化；需要 PDF 图像复核。
- Fig. 6-Fig. 7：切片图像和密度剖面，承担热影响区判定功能。
- Fig. 8：实验/计算温度剖面对比，同时比较 moving boundary 与无 moving boundary，是模型验证关键图。
- Fig. 9：分解度随深度和时间变化，对应热影响区厚度。
- Fig. 10：热解气体质量通量，支撑扩散模型不是装饰项。
- Fig. 11：不同切片显微结构，支撑“炭化层-热解区-原始材料”叙事。
- 公式 (1)：能量守恒方程，服务温度预测。
- 公式 (2)：Darcy law 形式的气体速度，服务扩散。
- 公式 (7)-(9)：密度、质量转化和分解度，服务热影响区判定。
- 热化学膨胀公式：把分解度和膨胀耦合，服务 TDE 模型。

## 11. 章节结构与篇章布局

真实章节：1 Introduction -> 2 Design of the novel solar radiant heating test -> 3 Formulations of the coupled temperature-diffusion-expansion problem -> 4 Results and discussion -> 5 Conclusions。

结构是“装置先于模型”的实验方法论文。作者先说为什么需要装置，再详细描述 apparatus 和 procedure，然后给模型公式，最后用实验数据验证模型和材料现象。这个顺序合理，因为读者先要相信边界和数据来源，才会相信模型比较。

标题命名偏功能型：`Design of the novel solar radiant heating test`、`Formulations of the coupled...`。第 3 节小标题按物理过程划分：energy conservation、mass transforming、thermochemical expansion、gas diffusion，结构清晰。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `801/文本/txt/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：3
- 结构类型判断：非严格 IMRaD，更像按模型、机制或结果模块组织。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 结果/验证型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 3.4 Gas diffusion equation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.3 Formulations for thermochemical expansion | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 4 Results and discussion | 结果/验证型 | 展示核心结果、对比、验证或参数分析 | 高 | 是 | 保留具体变量/对象 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏

Introduction 第一段从 TPS 需求和材料高温过程切入；第二段综述各类高温测试装置及限制；第三段转向太阳辐照和本文工作。段落推进是“复杂材料行为需要数据 -> 现有设备不足 -> 本文装置补位”。

第 2 节段落像实验说明书，强调尺寸、材料、价格、热流能力和操作流程。第 3 节段落偏物理建模，逐一解释控制方程中的变量。第 4 节段落按证据链推进：表面形貌 -> 切片/密度 -> 温度对比 -> 分解度 -> 气体通量 -> SEM 微观结构。

这种结果顺序很值得学习：先给肉眼/宏观证据，再给定量剖面，再给模型曲线，最后给微观机制。

## 13. 文笔画像与语言习惯

整体语气是实验平台可信度建设型。常用 `designed and built`, `capable of producing`, `used to investigate`, `suitable for verification`, `satisfactorily predicts`。claim 强度适中，装置能力表述较强，模型表述较谨慎。

时态：装置和实验用过去时，模型方程用一般现在时，结果图表用现在时。被动语态高频出现于实验步骤和模型公式，如 `was designed`, `were embedded`, `was determined`，体现客观实验写法。

高频名词：`apparatus`, `radiant heat flux`, `specimen`, `temperature`, `silica/phenolic composite`, `pyrolysis`, `density`, `diffusion`, `expansion`。形容词常用 `full spectrum`, `high radiant`, `one-sided`, `coupled`, `porous`。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：thermal(82)；heat(53)；heating(48)；composites(39)；high(34)；phenolic(33)；temperature(31)；material(29)；silica(28)；radiant(26)；test(26)；apparatus(24)；composite(24)；specimen(24)；experimental(22)；model(21)；materials(21)；pyrolysis(20)；protection(19)；mass(19)
- 高频学术名词：temperature(31)；material(29)；materials(21)；model(21)；pyrolysis(20)；protection(19)；decomposition(17)；equation(16)；behavior(16)；density(13)；analysis(12)；exposure(12)；energy(11)；response(10)；thickness(10)；conditions(9)
- 高频学术动词：shown(8)；proposed(7)；developed(7)；predicted(5)；shows(3)；investigate(3)；estimated(2)；validate(2)；evaluate(2)；suggests(2)；predict(2)；indicates(2)；simulate(2)；estimate(2)；compared(1)；evaluated(1)
- 高频形容词：thermal(82)；experimental(44)；high(34)；phenolic(33)；material(29)；radiant(26)；numerical(16)；boundary(13)；mathematical(7)；schematic(6)；evident(5)；porous(5)；various(5)；structural(5)；initial(4)；hypersonic(4)
- 高频副词/连接副词：generally(6)；however(5)；respectively(5)；theoretically(4)；spatially(4)；therefore(3)；rstly(3)；vertically(3)；completely(3)；moreover(2)；secondly(2)；tively(2)；thermally(2)；simultaneously(2)；roughly(2)；furthermore(1)
- 高频二词短语：silica phenolic(21)；thermal protection(19)；frp composites(14)；pro les(13)；radiant heat(12)；radiant heating(11)；thermal exposure(11)；phenolic composites(11)；phenolic composite(10)；applied thermal(9)；thermal engineering(9)；solar radiant(9)；heat uxes(9)；wind tunnel(9)；virgin material(8)；high temperatures(8)
- 高频三词短语：silica phenolic composites(10)；applied thermal engineering(9)；silica phenolic composite(9)；shi applied thermal(7)；solar radiant heating(6)；temperature pro les(6)；radiant heating apparatus(5)；specimen thermal exposure(5)；zone virgin material(5)；high radiant heat(4)；radiant heat uxes(4)；heat affected zone(4)

**主动、被动与句法**

- 被动语态估计次数：92
- `we + 动作动词` 主动句估计次数：1
- 名词化表达估计次数：368
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：106
- 一般过去时线索：81
- 现在完成时线索：1
- 情态动词线索：28
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：thermal(49)；heat(34)；heating(31)；high(24)；test(22)；radiant(20)；apparatus(20)；material(17)
- 3.3. Formulations for thermochemical expansion：expansion(3)；thermal(3)；henderson(2)；equation(2)；calculate(2)；rate(2)；change(2)；frp(2)
- 4. Results and discussion：thermal(30)；composites(23)；phenolic(19)；heat(19)；silica(17)；heating(16)；composite(16)；pro(15)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取

背景句：

- `To provide insight into this complex high-temperature behavior, a controlled heating environment... is necessary.`
- 模仿：为了理解 X 的复杂响应，需要一个边界条件明确且可重复的测试环境。

Gap 句：

- `These apparatus are capable of producing high heat flux... however...`
- 模仿：已有装置虽能实现 A，但在成本、边界可控性和测量便利性上仍存在限制。

方法句：

- `The thermocouples were embedded in the test specimen to monitor...`
- 模仿：将传感器嵌入试样不同深度，以获取随时间变化的内部响应。

结果句：

- `Variation in the thermal behavior from char layer to pyrolysis zone to virgin material is evident.`
- 模仿：从表层损伤区到未受影响区，材料响应呈现清晰的空间分层。

局限可补句：

- 虽然原文局限不多，类似论文可补：该装置主要模拟辐射热流，尚不能完全复现气动剪切和化学非平衡环境。

## 15. 引用策略与文献使用

引用主要集中在 Introduction 和模型背景：

- TPS 和高温材料需求引用支撑问题重要性。
- 高温测试装置引用用于分类比较，制造设备 gap。
- 复合材料热解模型引用支撑 TDE 模型各物理项。
- 实验设备价格和性能对比增强工程说服力。

作者对前人姿态是“承认能力 + 指出限制”：arc-jet 能复现再入热流，但成本高；辐射源可控，但非全光谱；电阻/感应加热可研究热机械行为，但边界不理想。这种姿态适合装置论文。

## 16. 审稿人视角风险

- 太阳源稳定性：天气、太阳角度、环境条件对热流可重复性影响需要误差分析。
- 相似准则：辐射热流不能完全替代真实气动加热、剪切、压力和氧化环境。
- 样本统计：文本中重复次数、误差条和不确定度不够突出。
- 模型参数：热解动力学、膨胀因子、渗透率等参数来源和敏感性需复核。
- 图像判读：热影响区边界由颜色/密度/分解度判定，可能存在主观误差。
- 安全和操作：高聚光太阳装置操作安全、校准流程和季节可用性未充分讨论。

## 17. 可复用资产

- 选题套路：把昂贵复杂测试平台的问题转化为低成本可复现装置创新。
- 论证套路：装置能力 -> 数据采集 -> 模型公式 -> 实验验证 -> 微观形貌解释。
- 图表套路：装置示意/照片、试样照片、切片密度、温度曲线、分解度、气体通量、SEM。
- 表达套路：`capable of producing`, `suitable for verification`, `one-sided heat flux`, `coupled temperature-diffusion-expansion problem`。
- 实验设计资产：后测切片 + 密度剖面 + SEM 可以作为热影响区判定的组合证据。

## 18. 对我写论文的启发

如果写实验装置论文，不能只说“装置便宜”，还要证明它能产生目标边界、能采集模型需要的数据、能解释材料行为。本文把装置贡献和模型验证绑定在一起，这是说服力来源。

另一个启发是结果顺序要从直观到抽象：先照片/形貌，再密度/温度，再模型变量，再微观结构。这样读者不会被方程直接淹没。

## 19. 最终浓缩

最值得学习：用低成本全光谱太阳辐照装置建立“可控热流-内部温度-热影响区-模型验证”的完整实验链。

最大风险：太阳辐照装置与真实气动热环境的相似性和实验重复性仍需更强误差证据。

可迁移三点：

1. 装置论文要同时证明边界能力、测量能力和模型验证能力。
2. 复杂材料热响应可用切片密度和显微结构形成强证据链。
3. 结论可以按“装置能力-成本优势-模型预测-材料分层”组织。

<!-- REAUDIT-2026-05-26 START -->

## 20. 复核增强：严格抽取、翻译、引文与句型

> 本区块由 `tools/upgrade_801_deep_analysis.py` 基于 `801/文本/txt/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.txt` 与 `801/文本/metadata/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.json` 重新抽取生成；用于修正旧报告中章节未全、引文缺失、摘要/结论未完整摘录的问题。双栏 PDF 抽取仍可能存在断行，引用和公式编号以 PDF 版面为最终准绳。

### 20.1 严格章节树（按 PDF/metadata TOC）

- L2 p.1: 1 Introduction （背景/领域定位）
- L2 p.2: 2 Design of the novel solar radiant heating test （对象/问题/模块）
  - L3 p.2: 2.1 Apparatus （对象/问题/模块）
  - L3 p.3: 2.2 Experimental procedure （对象/问题/模块）
- L2 p.3: 3 Formulations of the coupled temperature-diffusion-expansion problem （方法/模型）
  - L3 p.3: 3.1 Energy conservation equation （对象/问题/模块）
  - L3 p.4: 3.2 Mass transforming relationship （对象/问题/模块）
  - L3 p.4: 3.3 Formulations for thermochemical expansion （方法/模型）
  - L3 p.4: 3.4 Gas diffusion equation （对象/问题/模块）
- L2 p.5: 4 Results and discussion （结果/讨论/验证）
- L2 p.6: 5 Conclusions （结论）
- L2 p.7: Acknowledgements （对象/问题/模块）
- L2 p.7: References （参考文献）

### 20.2 章节名功能分析

| 章节/小节名 | 页码 | 层级 | 类型 | 复核说明 |
| --- | ---: | ---: | --- | --- |
| 1 Introduction | 1 | 2 | 背景/领域定位 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2 Design of the novel solar radiant heating test | 2 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.1 Apparatus | 2 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 2.2 Experimental procedure | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3 Formulations of the coupled temperature-diffusion-expansion problem | 3 | 2 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.1 Energy conservation equation | 3 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.2 Mass transforming relationship | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.3 Formulations for thermochemical expansion | 4 | 3 | 方法/模型 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 3.4 Gas diffusion equation | 4 | 3 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 4 Results and discussion | 5 | 2 | 结果/讨论/验证 | 来自 metadata TOC，正式分析按此章节点名复核 |
| 5 Conclusions | 6 | 2 | 结论 | 来自 metadata TOC，正式分析按此章节点名复核 |
| Acknowledgements | 7 | 2 | 对象/问题/模块 | 来自 metadata TOC，正式分析按此章节点名复核 |
| References | 7 | 2 | 参考文献 | 来自 metadata TOC，正式分析按此章节点名复核 |

### 20.3 摘要完整摘录（本地证据）

抽取状态：成功

> 公开库不直接展示完整英文摘要原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.4 摘要中文翻译

> 摘要
> 
> 设计并搭建了一套完整的太阳辐射热通量实验装置。太阳光经过菲涅尔透镜会聚，再经过棱镜会聚，作为能源。该测试台能够在短时间内产生已知的高辐射热通量，用于研究为航天器设计的热防护材料的热和烧蚀行为。将热电偶嵌入测试样本中以监测随时间变化的温度。此外，热影响区的厚度是通过在热暴露后将样品切成毫米段来确定的。这些实验数据适合用于数值模型的验证。提出了多孔材料温度-扩散膨胀耦合问题的数学模型。预测了二氧化硅纤维酚醛复合材料的热响应，并将其与相同边界和初始条件下的实验值进行比较，以评估模型的准确性。 �2016 Elsevier Ltd. 保留所有权利。

### 20.5 结论完整摘录（本地证据）

结论章节识别：5 Conclusions；状态：独立结论章节

> 公开库不直接展示完整英文结论原文；完整摘录保存在本地忽略目录 `801/深度拆解/extracted_evidence/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.json` 的 `conclusion` 字段，以及 `801/深度拆解/local_full_reports/A-solar-radiant-heating-apparatus-for-measuring-the-thermal_2016_Applied-The.md`。本节保留抽取状态、中文译文和分析内容，便于公开阅读与本地复核。

### 20.6 结论中文翻译

> 研制了太阳光两次会聚的全光谱太阳辐射热通量装置。进行温度测量是为了提供评估数值模型准确性所需的实验数据。将热暴露后的样品切成毫米段以确定热影响区的厚度。考虑到耦合的热、传质和热化学膨胀过程，提出了数学模型，并预测了二氧化硅/酚醛复合材料的温度分布、分解程度和气体质量通量。主要结论如下：
> 
> (1)该装置可产生高辐射热通量。全谱辐射加热过程有利于从理论上测试热防护材料的高温行为。 (2)装置价格便宜，易于施工和维护。 (3)数学模型令人满意地预测了FRP复合材料暴露于一侧热通量的热响应。 (4) 热暴露后，二氧化硅/酚醛复合材料从炭层到热解区再到原始材料的热行为变化是明显的。图10.不同加热时间下二氧化硅/酚醛复合材料气体的空间相关质量通量分布。 242 S.Shi 等人。 / 应用热能工程 106 (2016) 236–243

### 20.7 论文逻辑脉络复核

- 提出的问题：Therefore, there is a need to design a novel test bench which produces easily a high heat flux in a short time and simultaneously measures temperature profiles and thickness of heat affected zone of the material.
- 旧方法/已有研究不足：However, the thermal protection material experiences an irreversible physico-chemical process of ablation under elevated and high temperatures [4].
- 本文解决方式：These experimental data are suitable for use in verification of numerical models. A mathematical model for the coupled temperature-diffusionexpansion problem of porous materials was proposed. The thermal responses of a silica fiber phenolic composite were predicted and compared with experimental values for the same boundary and initial conditions to assess the accuracy of the model. �2016 Elsevier Ltd.
- 学术/工程增量：To provide insight into this complex high-temperature behavior, a controlled heating environment with well defined boundary conditions which can simulate the actual operating conditions of the thermal protection material is necessary. The temperature measurements were conducted to provide the experimental data necessary to evaluate the accuracy of the numerical model.
- 复核判断：正式阅读时应检查 Introduction 的 gap 是否与 Method 的输入输出、Results 的评价指标和 Conclusion 的 claim 完全闭合；若摘要中的强 claim 没有在结果图表或结论中回收，应在审稿风险中标注。

### 20.8 引文分析补全

- 全文引用簇数量（估计）：52
- Introduction 引用簇数量（估计）：14
- References 条目数（解析）：32
- 可识别年份条目数：35
- 近五年/近年文献（2021+）数量：1
- 经典文献（2010年前）数量：7
- 同刊引用数量（按 subject 粗略匹配）：0
- 高频来源期刊（粗略）：Applied Thermal Engineering(1)
- 引用簇样例：[4], [5], [29], [9,10], [11,12], [13,14], [15,16], [18], [22], [23], [24], [25]

带引用的 gap/转折句样例：

- However, the thermal protection material experiences an irreversible physico-chemical process of ablation under elevated and high temperatures [4].
- However, fabrication and operating costs of this equipment system is higher because of a number of sophisticated components, also adjustment and calibration of the heat flux parameters is difficult [11,12].

References 解析样例（前12条）：

- [1] W. Li, H. Huang, B. Ai, Z. Zhang, On the novel designs of charring composites for thermal protection application in reentry vehicles, Appl. Therm. Eng. 93 (2016) 849–855.
- [2] R. Upadhyay, P.T. Bauman, R. Stogner, K.W. Schulz, O. Ezekoye, Steady-state ablation model coupling with hypersonic flow, in: Proceedings of the 48th AIAA Aerospace Sciences Meeting Including the New Horizons Forum and Aerospace Exposition, Orlando, Florida, 4–7 January 2010, 2010.
- [3] R.A. Rana, R. Li, Thermal protection from a finite period of heat exposure – heat survival of flight data recorders, Appl. Therm. Eng. 75 (2015) 748–755.
- [4] G. Xiao, Y. Du, Y. Gui, et al., Heat transfer characteristics and limitations analysis of heat-pipe-cooled thermal protection structure, Appl. Therm. Eng. 70 (1) (2014) 655–664.
- [5] Y.I. Dimitrienko, Thermomechanics of Composites Under High Temperatures, Kluwer Academic Publishers, London, UK, 1999, pp. 1–108.
- [6] G. Pezzella, E. Bucchignani, Numerical assessment of the flowfield features at the exit of Scirocco plasma wind tunnel nozzle, Math. Comput. Simul. 82 (1) (2011) 118–131.
- [7] Y. Ma, Q. Li, S. Dong, Z. Wang, et al., Microstructures and ablation properties of 3D 4-directional Cf/ZrC–SiC composite in a plasma wind tunnel environment, Ceram. Int. 40 (7) (2014) 11387–11392.
- [8] F. Monteverde, R. Savino, M.D.S. Fumo, A.D. Maso, Plasma wind tunnel testing of ultra-high temperature ZrB2ASiC composites under hypersonic re-entry conditions, J. Eur. Ceram. Soc. 30 (11) (2010) 2313–2321.
- [9] L. Paglia, J. Tirillò, F. Marra, et al., Carbon-phenolic ablative materials for reentry space vehicles: plasma wind tunnel test and finite element modeling, Mater. Des. 90 (2016) 1170–1180.
- [10] C. Ground, L. Maddalena, V. Viti, Numerical analysis and characterization of the dissociated flowfield inside a 1.6 MW arc-heated wind tunnel facility, Aerosp. Sci. Technol. 30 (1) (2013) 306–314.
- [11] V. Carandente, R. Savino, A. Esposito, G. Zuppardi, V. Caso, Experimental and numerical simulation, by an arc-jet facility, of hypersonic flow in Titan’s atmosphere, Exp. Therm. Fluid Sci. 48 (2013) 97–101.
- [12] A. Cecere, R. Savino, C. Allouis, F. Monteverde, Heat transfer in ultra-high temperature advanced ceramics under high enthalpy arc-jet conditions, Int. J. Heat Mass Transfer 91 (2015) 747–755.

### 20.9 常用词、词类、语态与时态

- 高频词：thermal(70)；heat(47)；heating(46)；phenolic(33)；fig(31)；composites(29)；material(29)；silica(28)；high(28)；temperature(27)；radiant(25)；test(24)；specimen(24)；apparatus(23)；experimental(20)；pyrolysis(20)；materials(19)；composite(18)；pro(18)；gas(18)
- 高频名词化/学术名词：temperature(27)；decomposition(17)；expansion(16)；protection(14)；density(13)；exposure(11)；thickness(10)；equation(8)；prism(6)；ablation(6)；reaction(6)；tion(5)；conversion(5)；gure(5)；variation(4)
- 高频学术动词：developed(7)；presented(6)；predicted(5)；validate(2)；estimate(2)；estimated(2)；compared(1)；predict(1)
- 高频形容词：thermal(70)；phenolic(33)；material(29)；radiant(25)；experimental(20)；boundary(13)；mathematical(6)；schematic(6)；evident(5)；numerical(5)；porous(5)；various(5)；initial(4)；thermochemical(4)；dependent(4)
- 高频副词：respectively(5)；spatially(4)；rstly(3)；generally(3)；vertically(3)；completely(3)；secondly(2)；tively(2)；theoretically(2)；simultaneously(2)；only(2)；roughly(2)；perfectly(1)；easily(1)；neously(1)
- 高频二词短语：silica phenolic(21)；thermal protection(14)；pro les(13)；frp composites(12)；radiant heating(11)；radiant heat(11)；after thermal(11)；thermal exposure(11)；phenolic composites(11)；phenolic composite(10)；solar radiant(9)；heat uxes(9)
- 高频三词短语：after thermal exposure(11)；silica phenolic composites(10)；silica phenolic composite(9)；applied thermal engineering(8)；solar radiant heating(6)；page shi applied(6)；shi applied thermal(6)；temperature pro les(6)；radiant heating apparatus(5)；specimen after thermal(5)；zone virgin material(5)；high radiant heat(4)
- 被动语态估计：82；`we + 动作动词` 主动句估计：1
- 一般现在时线索：103；一般过去时线索：284；现在完成时线索：0；情态动词线索：28

章节词频：

- Abstract: thermal(4)；heat(3)；experimental(3)；radiant(2)；flux(2)；designed(2)；converged(2)；test(2)
- Introduction: thermal(22)；heating(13)；heat(12)；high(11)；protection(10)；materials(9)；experimental(8)；test(8)
- Conclusion: thermal(6)；heat(5)；composites(4)；flux(3)；temperature(3)；mass(3)；silica(3)；phenolic(3)

### 20.10 句型库扩充（每类多句）

#### 背景句
- 未在抽取文本中稳定识别，需人工从对应章节补充。
#### Gap句
- 原句/结构：However, the thermal protection material experiences an irreversible physico-chemical process of ablation under elevated and high temperatures [4].
  可迁移模板：However, the thermal protection material experiences an irreversible physico-chemical process of ablation under elevated and high temperatures [X].
- 原句/结构：However, fabrication and operating costs of this equipment system is higher because of a number of sophisticated components, also adjustment and calibration of the heat flux parameters is difficult [11,12].
  可迁移模板：However, fabrication and operating costs of this equipment system is higher because of a number of sophisticated components, also adjustment and calibration of the heat flux parameters is difficult [X,X].
#### 方法句
- 原句/结构：These experimental data are suitable for use in verification of numerical models.
  可迁移模板：These experimental data are suitable for use in verification of numerical models.
- 原句/结构：A mathematical model for the coupled temperature-diffusionexpansion problem of porous materials was proposed.
  可迁移模板：A mathematical model for the coupled temperature-diffusionexpansion problem of porous materials was proposed.
- 原句/结构：The thermal responses of a silica fiber phenolic composite were predicted and compared with experimental values for the same boundary and initial conditions to assess the accuracy of the model. �2016 Elsevier Ltd.
  可迁移模板：The thermal responses of a silica fiber phenolic composite were predicted and compared with experimental values for the same boundary and initial conditions to assess the accuracy of the model. �XElsevier Ltd.
#### 结果句
- 原句/结构：Although oxyacetylene torch test could be utilized to study the high temperature oxidation performance and ablation behavior of ablative materials, the oxyacetylene flame may alter the flowfield around the ablator, which, in turn, affects the measured results [13,14].
  可迁移模板：Although oxyacetylene torch test could be utilized to study the high temperature oxidation performance and ablation behavior of ablative materials, the oxyacetylene flame may alter the flowfield around the ablator, which, in turn, affects the measured results [X,X].
#### 贡献句
- 原句/结构：To provide insight into this complex high-temperature behavior, a controlled heating environment with well defined boundary conditions which can simulate the actual operating conditions of the thermal protection material is necessary.
  可迁移模板：To provide insight into this complex high-temperature behavior, a controlled heating environment with well defined boundary conditions which can simulate the actual operating conditions of the thermal protection material is necessary.
- 原句/结构：The temperature measurements were conducted to provide the experimental data necessary to evaluate the accuracy of the numerical model.
  可迁移模板：The temperature measurements were conducted to provide the experimental data necessary to evaluate the accuracy of the numerical model.
#### 限制/边界句
- 原句/结构：Although oxyacetylene torch test could be utilized to study the high temperature oxidation performance and ablation behavior of ablative materials, the oxyacetylene flame may alter the flowfield around the ablator, which, in turn, affects the measured results [13,14].
  可迁移模板：Although oxyacetylene torch test could be utilized to study the high temperature oxidation performance and ablation behavior of ablative materials, the oxyacetylene flame may alter the flowfield around the ablator, which, in turn, affects the measured results [X,X].
- 原句/结构：Besides, the additional electric or magnetic fields may affect the microstructures of the experimental materials.
  可迁移模板：Besides, the additional electric or magnetic fields may affect the microstructures of the experimental materials.
- 原句/结构：Therefore, the interferences mentioned above should be avoided when we theoretically test the various responses of the thermal protection materials with temperature, and the radiant heating is thought to be the desired heating method.
  可迁移模板：Therefore, the interferences mentioned above should be avoided when we theoretically test the various responses of the thermal protection materials with temperature, and the radiant heating is thought to be the desired heating method.

### 20.11 抽取失败与人工复核提示

- 摘要抽取：正常
- 结论抽取：正常
- 引文解析：正常
- 章节树：正常
- 路径复核：本次增强区统一使用 `801/文本/txt` 与 `801/文本/metadata` 作为可追溯来源。

<!-- REAUDIT-2026-05-26 END -->
