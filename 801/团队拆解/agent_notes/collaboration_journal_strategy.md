# 801 合作网络、作者角色与期刊策略画像

## 0. 样本与证据边界

- 样本规模：49 篇。
- 年份范围：2016-2026。
- 主要依据：`801/文本/_manifest.json`，`801/深度拆解/papers/*.md` 的基本信息，少量首页作者/机构/通讯作者信息，以及代表性 CRediT 片段。
- 证据边界：本文只分析论文公开证据能支持的作者、机构、合作结构和期刊策略。不把作者顺序、通讯作者或 CRediT 之外的信息扩展为未公开的团队分工。作者角色无法稳定判断处，明确写“不可判断”。

证据强度说明：

- 强证据：多篇论文反复出现，且跨年份/跨方向稳定。
- 中证据：某一方向或某一阶段反复出现。
- 弱证据：少数论文出现，可能来自合作方或单次场景。
- 不可判断：现有论文信息不足以支持。

## 1. 基本身份

801 样本本质上是一个以航空航天复杂工程系统为主场、兼具复合材料/热防护/热管理/不确定性/数据驱动降阶建模能力的综合型工程方法团队。

| 维度 | 画像 | 证据强度 |
| --- | --- | --- |
| 主要学科 | 航空航天工程、飞行器设计、气动热/热防护、热管理、复合材料力热性能、可靠性/不确定性、降阶模型与机器学习代理建模 | 强 |
| 主要期刊 | Aerospace Science and Technology 是主战期刊；Applied Thermal Engineering、Composite Structures、International Journal of Heat and Mass Transfer 是稳定出口；Probabilistic Engineering Mechanics、Chinese Journal of Aeronautics、Journal of Fluids and Structures 是方向性出口 | 强 |
| 年份范围 | 2016-2026 | 强 |
| 研究对象 | 高超声速/再入飞行器、热防护系统、热管理系统、TEG/热电材料与器件、复合材料单胞和有效性质、气动/热/结构物理场重构、轨迹优化和制导 | 强 |
| 方法体系 | CFD/CHT/CST、有限元与单胞模型、POD/ROM、Kriging/RBF/KRR/深度网络、Nataf/Monte Carlo/UQ、MDO/ALC、序列凸优化、实验测量和多尺度验证 | 强 |
| 应用场景 | 高超声速飞行器设计、再入热环境预测、热防护与热能管理、热电能量回收、飞行器结构优化、可靠性评估、在线/快速场预测 | 强 |

## 2. 核心作者、通讯作者与机构

### 2.1 核心作者

- Chunlin / Chun-Lin Gong：可判断为样本的核心锚点作者。深度拆解作者字段中几乎全样本反复出现；在多篇首页通讯作者信息中也出现 `leonwood@nwpu.edu.cn`。其位置覆盖第一作者、末位作者、中间作者和通讯作者，说明其角色横跨多个方向，但具体每篇的实际贡献需以 CRediT 为准。证据强度：强。
- Jian-Jun Gou / Jianjun Gou：可判断为热防护、热管理、热电器件、复合材料单胞/UQ 等方向的高频核心作者之一。多篇样本与 Chunlin Gong 共同出现，并在多篇首页通讯作者信息中出现 `jj.gou@nwpu.edu.cn`。证据强度：强。
- Chunna Li：在气动/热流/场重构/不确定性传播/双旋弹丸等数据驱动与航空方法论文中反复出现，且多篇作为通讯作者或 CRediT 中承担 review/editing、supervision/project 相关职责。证据强度：中强。
- 方向性稳定合作者：Hua Su、Jiaxin Hu、Ge Gao、Liangxian Gu、Xuyi Jia、Xiaobing Ma、Tengfei Zhang、Wen Ji、Yu-Cheng Yang 等在各子方向中多次出现。证据强度：中。

### 2.2 通讯作者与 PI 边界

- 可判断：Chunlin Gong、Jian-Jun Gou、Chunna Li 在多篇论文中承担通讯作者或监督/项目管理角色。
- 不可稳定判断：不能仅凭样本确定唯一核心 PI、实验室内部层级、学生导师关系或长期课题组组织结构。
- CRediT 线索显示：学生/青年第一作者常承担 writing-original draft、software、methodology、data curation、validation；高频核心作者常承担 supervision、project administration、conceptualization、writing-review & editing、funding acquisition。但这只适用于已读取到 CRediT 的代表性论文，不能外推到所有论文。

### 2.3 机构

- 主机构：Northwestern Polytechnical University / School of Astronautics / Shaanxi Aerospace Flight Vehicle Design Key Laboratory。该机构在多篇首页作者机构中反复出现，是样本最稳定机构。证据强度：强。
- 工程合作机构：China Academy of Launch Vehicle Technology、Research and Development Department / Research and Development Center、Beijing Institute of Spacecraft System Engineering、Beijing Institute of Astronautical System Engineering、Beijing Institute of Space Long March Vehicle 等在若干论文中出现。证据强度：中。
- 国际合作机构：University of Nottingham、University of Manchester 等在单胞/复合材料或流固耦合相关论文中出现。证据强度：弱到中。
- 材料方向合作机构：Northwestern Polytechnical University 内部的材料/固化/智能材料相关平台，以及 Harbin Institute of Technology 等在材料实验论文中出现。证据强度：中。

## 3. 合作结构

### 3.1 稳定合作者

- Gong + Gou 是最稳定组合之一，覆盖热防护、热管理、热电、复合材料、多尺度 UQ、结构优化等方向。证据强度：强。
- Gong + Chunna Li 在数据驱动气动/热流/物理场重构、不确定性传播、飞行器气动建模中反复出现。证据强度：中强。
- Gou + Jiaxin Hu / Ge Gao / Xiaobing Ma / Yu-Cheng Yang 更常见于热管理、热电器件、结构/热防护、多尺度复合材料方向。证据强度：中。
- Gong + Hua Su / Tengfei Zhang / Licong Zhang 更常见于轨迹优化、制导、可靠性和不确定性传播方向。证据强度：中。
- Gong + Xuyi Jia / Wen Ji 更常见于流固耦合、流场感知、双旋弹丸、非定常气动建模。证据强度：中。

### 3.2 新合作者与学生梯队

样本呈现“高频核心作者 + 方向性第一作者/青年作者”的结构：Wenyu Huang、Weiji Wang、Yu-Cheng Yang、Tengfei Zhang、Ge Gao、Jiaxin Hu、Wen Ji、Xiaobing Ma 等以第一作者或前列作者出现，并围绕一个方法/对象方向连续产出。是否为学生梯队不可判断，但从论文结构看，团队具备稳定吸纳新主题执行者的机制。证据强度：中。

### 3.3 跨学科合作

- 航空航天 + 机器学习：热流预测、流场重构、稀疏传感器重构、非定常气动建模等。
- 航空航天 + 热科学：热防护、热管理、气动热、CHT/CST、TEG 界面热电接触。
- 航空航天 + 材料科学：热电陶瓷、高熵材料、复合材料单胞、热膨胀/刚度/热导。
- 航空航天 + 可靠性/UQ：结构可靠性、火箭系统多学科不确定性、复合材料多尺度 UQ。

证据强度：强。

### 3.4 产业/工程场景合作

China Academy of Launch Vehicle Technology 和多个北京航天工程类机构在热流预测、热电/热管理、结构损伤识别、不确定性传播等论文中出现，说明部分论文嵌入真实飞行器、火箭或航天器系统工程问题。具体数据来源、项目关系和产业分工不可判断。证据强度：中。

### 3.5 国际合作

University of Nottingham 在单胞/复合材料相关论文中出现，University of Manchester 在流固耦合论文中出现。可判断存在国际学术合作出口，但不是样本的主导合作结构。证据强度：弱到中。

## 4. 合作功能表

| 合作对象类型 | 可能提供的资源 | 论文证据 | 判断 |
| --- | --- | --- | --- |
| 核心航天方法合作者 | 飞行器问题定义、总体建模、气动/热/结构耦合框架、论文组织和项目管理 | Gong/Gou/Chunna Li 等在多篇论文中高频出现，并在代表性 CRediT 中承担 supervision、conceptualization、project administration、review/editing | 强证据，但具体个人分工按单篇 CRediT 判断 |
| 第一作者/前列作者 | 具体方法实现、数值仿真、数据整理、初稿写作、图表和验证 | 已读取 CRediT 中，Wenyu Huang、Yu-Cheng Yang、Ge Gao 等承担 writing-original draft、software、methodology、data curation、validation 等 | 中强证据 |
| 工程机构合作者 | 工程应用场景、飞行器/火箭/航天器对象、工程约束或经费支持 | CALVT、Beijing Institute 系机构在多篇首页机构中出现；个别 CRediT 中外部作者承担 funding acquisition | 中证据；具体是否提供数据不可判断 |
| 材料/实验合作者 | 材料制备、显微表征、热电性能测试、界面接触实验、复合材料实验 | 热电陶瓷、TEG 接触、FRP 热-力退化、太阳辐射加热装置等论文含实验测量与材料表征；材料平台和 HIT/NPU 材料机构出现 | 中证据 |
| 理论/单胞合作者 | 单胞理论、边界条件、复合材料多尺度建模 | Unit cell 系列论文中 University of Nottingham / Shuguang Li / Wen-Quan Tao 等出现，且方法与单胞边界条件理论强相关 | 中证据 |
| 数据/AI 方法合作者 | ROM、POD、KRR、TFNO、TSCN、稀疏传感器重构、多保真数据融合 | 2024-2026 多篇数据驱动流场/热场/气动模型论文反复出现 POD、CNN/TCN/LSTM/KRR/TFNO 等 | 中强证据 |
| 写作/期刊策略合作者 | 综述式引言结构、工程 claim 包装、跨期刊语言转换 | 多方向论文均采用“工程高成本/耦合缺口 -> 方法替代 -> 精度/效率数字验证”的写法 | 中证据；无法判断具体由谁负责 |

## 5. 期刊策略

### 5.1 主战期刊

- Aerospace Science and Technology：49 篇中 11 篇，是最明确的主战期刊。适配主题包括高超声速飞行器、气动热、飞行器热管理、热防护、轨迹优化、制导、气动建模、结构优化和多学科设计。证据强度：强。

### 5.2 稳定产出期刊

- Applied Thermal Engineering：4 篇。适合热管理系统、主动冷却、TEG 热电器件、工程热优化和应用型热工模型。证据强度：强。
- Composite Structures：3 篇。适合复合材料、ITPS、单胞、多尺度力热性能、结构热力耦合。证据强度：中强。
- International Journal of Heat and Mass Transfer：3 篇。适合界面热/电接触、TEG 多界面、热输运、热损伤和传热机理/模型。证据强度：中强。

### 5.3 方法论文期刊

- Aerospace Science and Technology：工程方法与飞行器算例结合最常见，例如 POD+TSCN 热流、KRR-DCR 流场重构、MDO、制导、轨迹优化。
- Probabilistic Engineering Mechanics：可靠性、不确定性传播、时变可靠性等概率方法出口。
- Chinese Journal of Aeronautics：航空航天方法和不确定性/气动应用的补充出口。
- Computer Methods in Applied Mechanics and Engineering：更偏通用计算力学/数值方法，如跨尺度刚度传播。

证据强度：中强。

### 5.4 应用论文期刊

- Applied Thermal Engineering：热管理系统、主动冷却网络、气动热采集 TEG、RTG/TEG 应用。
- International Journal of Heat and Mass Transfer / International Communications in Heat and Mass Transfer：传热、界面接触、温度场反演、热损伤模型。
- Composite Structures：ITPS、复合材料单胞、结构热力行为。

证据强度：强。

### 5.5 跨学科出口

- Journal of Fluids and Structures：流固耦合、气动弹性剪裁、FSI 流场感知。
- Journal of Alloys and Compounds、Chemical Engineering Journal、Journal of the European Ceramic Society、Results in Physics：热电材料和高熵陶瓷材料方向。
- Acta Astronautica：空间环境/微重力生物效应类跨界主题。
- ISA Transactions：控制与无人机路径跟踪。

证据强度：中。

## 6. 不同成果对应不同期刊的规律

| 成果类型 | 常见期刊出口 | 规律判断 | 证据强度 |
| --- | --- | --- | --- |
| 飞行器级方法 + 工程算例 | Aerospace Science and Technology | 只要对象是高超声速/再入/飞行器总体，并能给出效率、精度、约束满足或工程收益，优先投 AST | 强 |
| 热管理/热防护系统设计 | Applied Thermal Engineering、Aerospace Science and Technology | 系统热管理、主动冷却、热电集成更偏 ATE；若强调飞行器总体/高超声速系统价值，也进入 AST | 强 |
| 复合材料单胞/ITPS/有效性质 | Composite Structures、Applied Thermal Engineering、Computer Methods in Applied Mechanics and Engineering | 工程结构和复合材料性能投 Composite Structures；传热/热导规则投 ATE；方法更通用时投 CMAE | 中强 |
| 界面传热/热电接触 | International Journal of Heat and Mass Transfer、Applied Thermal Engineering | 机理建模、接触热阻/电阻、实验验证偏 IJHMT；器件/系统创新偏 ATE | 强 |
| 可靠性/UQ | Probabilistic Engineering Mechanics、Chinese Journal of Aeronautics、Composite Structures | 概率方法本身投 PEM；航空系统应用或工程方法投 CJA/AST；复合材料多尺度 UQ 投 Composite Structures | 中强 |
| 物理场重构/ROM/AI 代理模型 | Aerospace Science and Technology、International Journal of Heat and Fluid Flow、Journal of Fluids and Structures | 飞行器热流/气动场工程 ROM 投 AST；热流体场重构或神经算子投 IJHFF；FSI 场感知投 JFS | 中强 |
| 材料制备与热电性能 | Chemical Engineering Journal、Journal of Alloys and Compounds、Journal of the European Ceramic Society、Results in Physics | 机制协同和高影响材料性能投 CEJ；合金/陶瓷材料体系投 JAC/JECS；短发现或性能现象投 Results in Physics | 中 |
| 控制/轨迹/制导 | Aerospace Science and Technology、ISA Transactions | 再入/航天飞行器轨迹优化和制导偏 AST；控制算法与实飞/无人机验证可投 ISA Transactions | 中 |

## 7. 期刊策略画像

这个团队不是“单一期刊重复投稿”型，而是“同一资源按贡献类型分发”型：

1. 飞行器工程问题和方法集成，优先进入 Aerospace Science and Technology。
2. 热管理/热防护/热电系统，按侧重点在 Aerospace Science and Technology、Applied Thermal Engineering、International Journal of Heat and Mass Transfer 之间切换。
3. 复合材料单胞、热膨胀、刚度、ITPS 结构，进入 Composite Structures、Applied Thermal Engineering 或 Computer Methods in Applied Mechanics and Engineering。
4. 概率可靠性和不确定性传播，进入 Probabilistic Engineering Mechanics 或航空类期刊。
5. 材料本体性能提升，转向材料/化工/陶瓷期刊。

关键策略是：同一长期母题会被包装成不同期刊可接受的语言。比如“高超声速热问题”可以写成 AST 的飞行器热管理，也可以写成 ATE 的系统热优化、IJHMT 的界面传热、Composite Structures 的热防护结构、材料期刊的热电材料性能。证据强度：强。

## 8. 不可判断边界

- 不可判断唯一 PI：Chunlin Gong 和 Jian-Jun Gou 都是高频核心作者，但样本不能稳定推出唯一 PI 或实验室层级。
- 不可判断学生关系：第一作者/前列作者可能是学生、博士后或合作方执行者，但论文证据不足以确认。
- 不可判断每个合作者的真实资源贡献：除 CRediT、机构和论文方法外，不能推断谁提供设备、数据、代码或项目。
- 不可判断产业数据真实性质：CALVT/北京航天机构出现说明工程合作线索，但无法判断是否提供真实型号数据、工程保密数据或仅提供场景/经费。
- 不可判断期刊关系：不能把高频发表解释为特殊期刊关系，只能判断期刊适配策略成熟。

## 9. 一句话结论

801 样本展现的是一个以 NPU 航天学院/陕西飞行器设计重点实验室为核心、由 Gong-Gou-Chunna Li 等高频作者牵引、多方向青年/合作作者执行的工程方法生产网络；其期刊策略是把“高超声速复杂系统中的热、气动、结构、材料和不确定性问题”拆成不同贡献类型，再分别投向 AST、ATE、Composite Structures、IJHMT、PEM/CJA/JFS 及材料类期刊。
