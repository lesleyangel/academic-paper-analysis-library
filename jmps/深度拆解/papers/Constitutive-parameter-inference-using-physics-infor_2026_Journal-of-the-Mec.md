# Constitutive parameter inference using physics-informed full volume inverse modeling of intact and torn rotator cuff tendons

## 0. 读取说明
- 源 PDF：`jmps/文献/Constitutive-parameter-inference-using-physics-infor_2026_Journal-of-the-Mec.pdf`
- 源 TXT：`jmps/文本/txt/Constitutive-parameter-inference-using-physics-infor_2026_Journal-of-the-Mec.txt`
- 辅助参考：上一轮标准拆解仅用于核对结构与主张，本稿重新基于全文、图注、讨论和结论组织。
- 是否需要结合 PDF 图像核查：需要。txt 提供图注和正文描述，但位移云图、应变带、误差热区、纤维方向图的视觉细节必须结合 PDF 图像核查。
- 本文类型：生物软组织本构反演论文；全体积 MRI 实验数据 + 弱形式 VSI + PDE 约束优化 + 候选超弹性模型比较。

## 1. 基本信息与论文身份
- 题名：Constitutive parameter inference using physics-informed full volume inverse modeling of intact and torn rotator cuff tendons
- 作者/机构：Carla Nathaly Villacis Nunez 等；University of Michigan、Auburn University、USC 等。
- 期刊/年份/卷期：Journal of the Mechanics and Physics of Solids, 214, 2026, Article 106668。
- DOI：10.1016/j.jmps.2026.106668
- 关键词：Biomechanics weak formulation；PDE-constrained optimization；Variational system identification；Soft tissue modeling；Tendon hyperelasticity。
- 研究对象：绵羊肩袖肌腱完整态与 75% bursal footprint detachment 撕裂态，尤其是内部三维位移、应变、剪切、体积不变量和纤维各向异性。
- 方法类型：MRI 全体积位移/应变采集；VSI 弱形式识别；step-wise regression 参数抑制；adjoint/PDE-constrained optimization；neo-Hookean、modified HGO、reduced polynomial 模型对比。
- 证据类型：全体积位移场、应变场、不变量误差图、训练/验证划分、模型全局误差、网格收敛、边界条件和纤维方向重建。
- 目标读者：软组织力学、本构反演、医学影像力学、有限元肩袖建模、VFM/VSI 方法研究者。
- JMPS 风格定位：以临床问题开场，但真正贡献落在“原生几何 + 全场内部数据 + 物理约束反问题”的力学方法链。

## 2. 摘要与核心信息提取
摘要按“传统方法不足 -> 全体积数据 -> 反演框架 -> 模型比较 -> 谨慎意义”展开。背景句把 conventional approaches 限定为依赖 surface strains 或 excised specimens 的路线，gap 句强调这些路线无法保留 tendon native architecture，也看不到内部剪切和体积机制。方法句引入 voxel-wise displacement、VSI 弱平衡式和 PDE 约束优化，说明不是单纯拟合外部力-位移，而是在体素级空间场上识别本构机制。结果句做了三层比较：NH 失败、modified HGO 能合理捕捉、简化 polynomial 用少量项达到相近表现。意义句主动降调：现有模型尚不能完全复制复杂内部力学，但能捕捉完整和损伤组织的关键趋势。

一句话主张：全体积 MRI 位移场可把肩袖肌腱本构识别从表面/离体曲线拟合推进到保留原生结构的物理约束反问题，其中少量必要各向异性项已足以重现实验中的内部剪切趋势，但体积项、纤维方向和临床级外推仍需改进。

核心关键词：full volume MRI；VSI；PDE-constrained optimization；anisotropic tendon response；internal shear strain；parsimonious constitutive model。

## 3. 选题层深拆
问题来源有两个入口。临床入口是 partial-thickness rotator cuff tears 的管理仍依赖经验，尤其 high-grade tears 是否应手术存在争议，因为缺少能预测 tear progression 的机制框架。方法入口是传统 DIC、marker-to-marker deformation 和 surface-only 测量只看 bursal/articular 表面，无法看到 tendon through-thickness 内部应变、剪切和滑移。

问题为何重要：肩袖肌腱具有层状、异质和弯曲附着结构，撕裂扩展很可能由内部应变集中、剪切带和骨-肌腱边界附近的局部场驱动；如果参数仍来自 excised tendon 或一维 stress-strain 曲线，FE 模型即使几何复杂，也缺少内部力学验证。

为何现在值得做：displacement-encoded MRI 已能提供 through-thickness strain；VSI/VFM 等全场反演方法需要信息丰富、非均匀场来提高可辨识性；本文实验的弯曲几何和撕裂状态正好激活 volumetric、tensile、shear 机制，给反演提供“富信息”数据。

问题边界：本文不是人体临床参数库，也不是直接预测患者撕裂进展；它在绵羊 infraspinatus tendon 上证明一套 full-volume constitutive inference workflow。其转化价值在“同一框架可应用于 human MRI datasets”，而不是本文参数可直接用于人类 supraspinatus。

选题的 JMPS 味道：把医学影像数据转化为连续介质反问题，把“看不见的内部变形”写成“本构机制可辨识性”的核心条件。

## 4. 领域位置与文献版图
作者将前人组织成四类：第一类是临床/组织力学研究，说明 partial tears 进展和 strain concentrations 的现实重要性；第二类是表面测量和 excised specimen 实验，贡献是提供局部应变或一维曲线，缺口是无法保持 native attachments 和内部结构；第三类是 rotator cuff FE 模型，能模拟姿态、骨-肌腱接触和局部应力，但常依赖文献参数或表面校准；第四类是全场反演方法，如 VFM/VSI，已在材料识别中证明价值，但尚未充分用于原生肌腱全体积 MRI 数据。

本文站位：不是推翻 FE，也不是发明 VSI，而是把 full-volume MRI、VSI、PDE-constrained solver、voxel-wise fiber direction 和 torn/intact tendon 组合起来，补上“模型参数来自真实内部响应”的一环。

最接近前人：作者自己的 MRI shoulder/tendon 全体积测量工作、Wang 等 VSI 弱形式识别、Luetkemeyer/Scheven/Estrada 等 MRI-derived strain mapping，以及 HGO/soft tissue hyperelasticity。处理前人姿态整体友好，常用“已有研究显著推进，但仍不能……”式补足。

## 5. Gap 制造机制
显式 gap：partial thickness tears 的内部 loading environment 难以由传统表面测量获得；既有 FE 模型缺少 full volume mechanics validation；VSI 虽可识别机制，但尚未与原生肩袖肌腱全体积数据、撕裂状态和纤维方向场结合。

隐含 gap：肌腱本构模型不只是参数拟合问题，而是候选 strain energy terms 是否与真实内部机制对应的问题。若只看整体力/位移，NH、HGO、polynomial 的差异可能被遮蔽；只有体素级位移/应变/不变量误差图才能判断哪个机制缺失。

gap 类型：数据 gap、方法整合 gap、内部验证 gap、各向异性可辨识性 gap。

gap 是否足够窄：足够。它被收束到“ovine tendon intact/torn + full volume displacement + three constitutive model families + VSI/PDE optimization”。

审稿人可能追问：样本数 n=12 和单一 quasi-uniaxial 协议是否足够支撑“first full volume constitutive characterization”；MRI 分辨率和边界条件抽取误差是否会主导反演；完整态和撕裂态材料参数是否真的可视为同一均质材料。

## 6. 创新性判断
作者声明的贡献包括：用全体积 MRI 数据训练和验证肌腱本构模型；用 VSI 识别主导变形机制并筛选参数；用 PDE-constrained optimization 得到更物理合理的参数；比较 NH、m-HGO 和 reduced polynomial 模型对完整/撕裂内部场的预测。

真实创新点：第一，把 MRI voxel-wise displacement 直接放入弱平衡式，避免只拟合外部响应。第二，把撕裂态内部 shear bands 和 sliding behavior 用作各向异性项必要性的证据。第三，用 reduced polynomial 模型显示高阶 I1/I2 项不一定必要，第二阶 fiber-related invariant 可以承担主要作用。第四，把误差拆成 displacement-specific、strain-specific、invariant-specific，从而指出下一代模型应改体积项和纤维方向场。

创新类型：方法整合创新 + 生物软组织全场数据创新 + 证据表达创新。创新强度：中高。单个工具并非全新，但组合场景和证据闭环强。

易被挑战的创新点：如果审稿人认为“全体积数据 + inverse modeling”在其他组织中已有，本文新意就要落在 rotator cuff native architecture/torn state；如果参数在多样本间不稳定，parsimonious model 的结论会被削弱。

## 7. 论证链条复原
临床管理 partial tears 需要机制预测 -> 表面测量和离体实验看不到内部全体积响应 -> FE 模型若缺少内部校准就无法临床可信 -> displacement-encoded MRI 可提供完整/撕裂肌腱体素位移和应变 -> tendon 弯曲几何与撕裂边界在单一加载中激活 tensile、shear、volumetric 机制 -> VSI 利用弱平衡式从候选能量项中识别主导机制 -> step-wise regression 去掉不必要高阶项 -> PDE-constrained optimization 修正 near-incompressibility 和位移场一致性 -> 前向预测表明 NH 不能重现撕裂内部剪切，m-HGO 和 reduced polynomial 更好 -> 不变量误差显示 volumetric/I3 与 fiber/I4 表征仍不足 -> 框架可迁移到人类 MRI 和患者特异模型，但当前参数为准静态、绵羊、单载荷下的有效参数。

最薄弱环节：从“模型可重现实验趋势”到“可支撑临床管理”的距离仍大；作者通过 limitations 和 future work 降低了风险。

## 8. 方法/理论/模型细拆
方法总框架分五步。第一，制备绵羊肩袖 tendon，保持 humeral attachment 和 intramuscular tendon section，在 intact 与 75% bursal detachment torn 状态下做 1 mm/2 mm 拉伸，预处理降低粘弹影响。第二，用 MRI-based strain acquisition 得到 full volume displacement/strain maps。第三，根据高分辨率图像重建边界、humeral head/enthesis 条件和 voxel-wise fiber direction。第四，在 strain energy density 中将 W 分解为 volumetric、isochoric、anisotropic，候选不变量包括 I1、I2、I3/J、I4。VSI 用弱形式平衡和 data-evaluated stress operators 建线性/稀疏参数识别。第五，PDE-constrained solver 以位移场一致性为目标继续优化参数，最后进行前向预测和误差评估。

关键概念：VSI 的作用是“机制筛选”和初值/parsimonious model 识别；PDE-constrained optimization 的作用是“物理参数修正”和位移场拟合；二者不是互相替代，而是前后衔接。

关键假设：肌腱可先近似为连续体、准静态、近不可压缩、均质材料参数但空间纤维方向可变；撕裂不改变材料固有属性或至少可先用同一建模框架处理；MRI 位移噪声和网格误差可被二阶四面体、训练/验证和误差图控制。

方法复杂度合理性：合理。问题本身是 full-field inverse problem，单轴曲线拟合无法回答内部剪切和体积不变量误差。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 全体积 MRI 能激活并捕捉 tendon 多种变形机制 | 摘要、3.2、5.1 | Fig. 1 位移场、Fig. 2 normal/shear strain mechanisms，完整/撕裂 1 mm/2 mm 工况 | 实验全场数据 | 强 | 图像细节需 PDF 核查；MRI 分辨率限制 |
| VSI 可识别 parsimonious constitutive representation | 3.3、4.1、5.2 | step-wise regression 后高阶 I1/I2 项被抑制，m-HGO 与 reduced polynomial 保留关键项 | 反演结果/模型筛选 | 中强 | 参数可辨识性受单一加载影响 |
| PDE-constrained optimization 使 near-incompressible 参数更物理 | 4.3、5.3 | VSI bulk modulus 不合理，PDE 阶段改善 bulk/shear 关系和位移预测 | 优化对比 | 中强 | local minimum、lower bounds 和 volumetric locking 风险 |
| 各向异性模型对 torn tendon 内部剪切必要 | 4.2、5.5 | NH 无法重现内部 shear strain bands 和 sliding；m-HGO/Pol 更好 | 前向预测/应变图 | 强 | 需核查图像中的剪切带位置和尺度 |
| reduced polynomial 少量项可接近 m-HGO 表现 | 摘要、4.1、5.2 | Pol 模型保留 neo-Hookean + fiber-related terms，误差与 m-HGO 同量级 | 模型对比 | 中强 | 是否跨样本稳定需进一步统计 |
| 主要模型不足集中在体积项和纤维方向项 | 5.6、5.7 | I3 error 最大，I4 error 在 footprint detachment 和 gripper 附近集中 | invariant error maps | 中 | 不变量误差受位移微分噪声放大 |

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Eq. 1-15 | W 分解、I1/I2/I3/I4、PK stress operator、弱形式残差 | VSI 机制识别有物理基础 | 把数据反演接到连续体平衡 | 公式排版需核查 |
| Fig. 1 | MRI 全体积位移地图 | 数据不是表面测量 | 证明 full volume acquisition 的空间覆盖 | 是 |
| Fig. 2 | normal/shear strain mechanisms | 单一实验激活多机制 | 支撑可辨识性来源 | 是 |
| Fig. 3 | intact/torn 边界条件 | 原生几何/边界被纳入模型 | 降低“边界想象”风险 | 是 |
| Fig. 4 | 体素纤维方向流程 | 各向异性方向有数据依据 | 支撑 HGO/Pol fiber terms | 是 |
| Fig. 5-6 | 位移预测和误差图 | PDE 优化/模型对比 | 从视觉和体素误差证明差异 | 是 |
| Fig. 7 | 应变图 | anisotropy captures internal shear | 显示 NH 的机制失败 | 是 |
| Fig. 8 | invariant error maps | I3/I4 是改进点 | 把局限定位到能量项 | 是 |

结果叙事顺序很讲究：先参数识别，防止读者只把图看作图像展示；再用 full volume maps 展示预测；最后全局误差比较，把“看起来像”转成定量支持。

## 11. 章节结构与篇章布局
Abstract 是五句式：背景限制、方法框架、模型候选、结果发现、谨慎意义。Introduction 从临床争议切入，再层层转向测量盲区、FE 参数不足、MRI 全体积数据、VSI 适配性，最后给出本文框架。

Mathematical framework 先讲能量函数和不变量，再讲弱形式，保证方法不是黑箱。Methods 是工程化主体：实验、机制激活、VSI、参数抑制、PDE 优化、候选模型、边界/纤维/网格/数据划分/误差指标。Results 只做三件事：参数、全体积预测、全局误差。Discussion 分成 8 个小节，每节标题直接表达一个发现或局限，这是可模仿的高密度讨论结构。Conclusion 回到 full volume inference、parsimonious mechanisms、anisotropy 和 human MRI extension。

最值得模仿：Discussion 小标题不是“Discussion of X”，而是“X revealed/ enabled/ yielded/ enhanced...”，标题本身就是论点。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/Constitutive-parameter-inference-using-physics-infor_2026_Journal-of-the-Mec.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：29
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：实验/材料型, 描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Mathematical framework | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3 Methods | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1 Full volume experimental data acquisition | 实验/材料型 | 说明样品、实验设置、数据来源或测量方式 | 高 | 是 | 保留具体变量/对象 |
| 3.1.1 Sample preparation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.1.2 MRI sequence for strain acquisition | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.1.3 Data processing pipeline | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2 Activation mechanisms and features of interest | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 3.3.2 Parameter suppression with step-wise regression | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3.4 Candidate constitutive models | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5 Model setup and evaluation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5.1 Boundary conditions | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5.3 Mesh convergence | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.5.4 Dataset partitioning approach | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Introduction 段落推进：临床重要性 -> 表面测量限制 -> FE 模型进展但内部校准不足 -> MRI 全体积数据成为机会 -> VSI 适配 -> 本文贡献和章节导航。

Method 段落推进：每段先定义对象，再说明为什么它服务反演。比如 fiber direction 段不是单独介绍图像处理，而是解释为什么 a0 field 进入 I4 项；dataset partitioning 段不是统计形式，而是说明训练/验证如何避免只拟合一个场。

Results 段落推进：先报告模型输出，再解释空间分布，再与生物/力学机制对应。典型写法是“although surface displacement maps appear similar, internal strain maps reveal...”，用表面相似和内部差异制造层次。

Discussion 段落推进：每节先用一句话回扣发现，再解释机制，再给文献或局限。段落收束常指向“therefore future models should...”。

可复用段落模板：现有数据揭示 X -> 传统模型只看 Y 因而漏掉 X -> 我们的全场/物理约束方法把 X 转化为可比较的误差或参数 -> 该结果说明 Z 项必要，但也暴露 A 项不足。

## 13. 文笔画像与语言习惯
整体语气：强方法、谨慎外推。作者敢说 first/full-volume/tendon-specific，但遇到临床、人类迁移和模型完整性时快速降调。

claim 强度：对“framework demonstrated”“anisotropic terms essential”较强；对“clinical-grade prediction”“patient-specific management”使用 foundation/potential/future。

问题表达偏好：surface-limited approach；absence of mechanistic framework；cannot properly validate full volume mechanics；limited clinical applicability。

贡献表达偏好：full volume MRI enabled；parsimonious representations；dominant deformation mechanisms；minimal yet essential anisotropic contribution；physically plausible parameters。

机制表达偏好：activated volumetric, tensile and shear mechanisms；sliding behavior between detached and attached tissue bundles；internal shear strain patterns；reduced identifiability under complex deformations。

限定表达偏好：reasonable accuracy；do not fully replicate；effective quasi-static properties；local minimum；requires further validation。

术语密度：高，但多为可解释术语；公式段硬，Discussion 转为机制解释，利于跨学科读者。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：tendon(130)；strain(107)；model(93)；models(79)；tendons(69)；displacement(63)；vsi(61)；ber(53)；full(51)；volume(48)；error(47)；m-hgo(46)；inference(43)；shear(43)；torn(42)；direction(42)；parameter(41)；function(41)；parameters(39)；pde-constrained(38)
- 高频学术名词：strain(107)；model(93)；deformation(66)；displacement(63)；validation(58)；inference(43)；direction(42)；parameter(41)；function(41)；condition(40)；parameters(39)；optimization(31)；framework(29)；equation(26)；nement(25)；thickness(22)
- 高频学术动词：capture(16)；captured(11)；shown(9)；evaluated(8)；revealed(6)；compared(6)；indicates(6)；indicate(6)；validated(5)；evaluate(5)；derived(5)；developed(5)；suggests(4)；proposed(4)；predicted(4)；demonstrate(3)
- 高频形容词：experimental(66)；displacement(63)；anisotropic(32)；constitutive(31)；internal(30)；longitudinal(28)；nement(25)；boundary(23)；material(21)；bursal(21)；element(18)；volumetric(17)；global(16)；representative(16)；polynomial(14)；humeral(14)
- 高频副词/连接副词：generally(18)；particularly(17)；however(15)；respectively(15)；approximately(8)；experimentally(8)；directly(8)；accurately(8)；importantly(7)；therefore(6)；consequently(6)；cally(6)；physically(5)；previously(5)；similarly(5)；strongly(4)
- 高频二词短语：full volume(44)；shear strain(24)；tendon gripper(21)；m-hgo pol(20)；pde-constrained optimization(19)；strain energy(19)；ber direction(19)；pol models(19)；energy density(18)；density function(16)；deformation mechanisms(15)；m-hgo model(15)；intact torn(14)；error maps(14)；parameter inference(13)；humeral head(13)
- 高频三词短语：m-hgo pol models(19)；strain energy density(18)；energy density function(16)；ber direction eld(12)；near tendon gripper(11)；mpa mpa mpa(10)；vsi adjoint change(6)；writing review editing(6)；ann arbor michigan(5)；full volume datasets(5)；system identi cation(5)；partial thickness tears(5)

**主动、被动与句法**

- 被动语态估计次数：198
- `we + 动作动词` 主动句估计次数：5
- 名词化表达估计次数：1307
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：137
- 一般过去时线索：241
- 现在完成时线索：29
- 情态动词线索：82
- 时态判断：过去时相对突出，说明文本中实验/仿真步骤和已完成操作占比较高；现在时仍用于图表说明和一般性判断。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：michigan(11)；model(9)；university(8)；states(8)；engineering(6)；edu(6)；department(5)；ann(5)
- 1. Introduction：tears(16)；full(15)；volume(13)；rotator(12)；tendon(11)；strain(10)；models(10)；thickness(9)
- 2. Mathematical framework：function(8)；element(8)；invariants(5)；functions(5)；method(4)；displacement(4)；eld(4)；test(4)
- 3. Methods：无明显高频项
- 3.1. Full volume experimental data acquisition：无明显高频项
- 3.1.1. Sample preparation：device(3)；performed(2)；infraspinatus(2)；tendons(2)；human(2)；sample(2)；xture(2)；loading(2)
- 3.1.2. MRI sequence for strain acquisition：protocol(6)；displacement(6)；mri(6)；loading(5)；encoding(3)；sequence(3)；acquisition(3)；voxel(3)
- 3.1.3. Data processing pipeline：version(4)；full(3)；volume(3)；inc(3)；mri(3)；algorithm(3)；maps(2)；displacement(2)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 表达模式：Unlike conventional approaches relying on X, our framework leverages Y while preserving Z.
- 可复用骨架：不同于依赖单点/表面的传统方法，本文利用全场/体素级数据，在保留原生结构的同时识别内部机制。
- 中文启发：gap 不要写“没人做过”，要写“已有方法因测量维度/样品状态而无法验证目标机制”。

### 14.2 方法与框架表达
- 表达模式：We implemented an approach termed X to solve the weak form of Y using Z.
- 可复用骨架：我们将 X 方法嵌入 Y 控制方程的弱形式，并以 Z 全场数据作为输入。
- 中文启发：把算法动词和物理方程绑定，减少“黑箱优化”观感。

### 14.3 结果与趋势表达
- 表达模式：Although A appeared visually similar, B revealed notable differences.
- 可复用骨架：尽管宏观/表面响应相近，内部/局部指标揭示了模型之间的机制差异。

### 14.4 机制解释表达
- 表达模式：This behavior is likely associated with X, which increases sensitivity to Y.
- 可复用骨架：这一误差可能来自 X 区域信号幅值小/边界远/微分噪声大，因此对 Y 更敏感。

### 14.5 贡献与意义表达
- 表达模式：The proposed framework lays the foundation for future data-driven tools that integrate A and B.
- 可复用骨架：该框架不是终点，而是为后续结合患者几何、载荷和学习模型的预测工具打基础。

### 14.6 局限与未来工作表达
- 表达模式：The inferred parameters should be interpreted as effective quasi-static properties.
- 可复用骨架：当前参数应解释为特定加载/测量协议下的有效参数，不应直接外推到速率依赖或临床场景。

## 15. 引用策略与文献使用
引用密度集中在 Introduction 和 Methods。Introduction 先用临床流行病学和 tear progression 文献证明问题重要，再用 DIC/marker/surface measurement 文献证明测量限制，然后用 FE 文献证明计算模型已有但参数来源不足，最后用 MRI 和 VSI/VFM 文献证明现在有可行工具。Methods 引用经典 HGO、VSI、FEniCS/优化框架和 MRI strain acquisition。Discussion 引用相对少，更多依赖本文图表。

经典文献用途：Mooney/Rivlin 类不在本文核心，HGO 与 continuum biomechanics 文献用于模型合法性；肩袖解剖和临床文献用于问题合法性。

近年文献用途：MRI-based strain acquisition、full volume inverse modeling、患者特异化 FE、机器学习展望。

gap 搭建方式：不是用单篇文献打靶，而是把每个分支都写成“有贡献但不足以独立解决 full volume internal mechanics validation”。

引用风险：若缺少最接近的人体 full-volume tendon modeling 工作，first claim 会被挑战；对 phase-field fracture 和 geometric learning 的 future work 需要避免显得跳跃。

## 16. 审稿人视角风险
- 最大攻击面：样本量、单一动物模型和单一 quasi-uniaxial 协议不足以支撑广泛本构结论。
- claim 是否过强：对方法示范和模型比较可接受；对 clinical-grade/patient-specific 应保持展望语气。
- 证据不足：如果只看全局误差，m-HGO 与 Pol 的差异可能不强；必须依赖内部应变和不变量误差图来支撑机制判断。
- 方法可复现性：MRI acquisition、fiber interpolation、boundary extraction、PDE solver settings、lower bounds 和 mesh convergence 要足够详细。
- 边界条件风险：humeral head/enthesis 和 gripper 区域误差可能由实验夹具而非本构模型引起。
- 替代解释：撕裂后局部损伤、纤维重排或材料性质变化，而非同一均质模型的各向异性项，可能解释内部剪切差异。
- 图像核查：Fig. 5-8 的误差热区、剪切带和不变量分布需结合 PDF 图像确认，txt 不能判断色阶和空间细节。

## 17. 可复用资产
- 选题角度：用新测量维度重审老本构问题；把“缺少全场内部数据”写成核心 gap。
- gap 制造方式：临床/工程痛点 -> 表面测量盲区 -> FE 参数来源不足 -> 全场反演机会。
- 论证链：全体积数据 -> 弱形式机制筛选 -> 稀疏模型 -> PDE 修正 -> 前向全场验证 -> 误差地图定位模型缺陷。
- 图表设计：采集示意、机制激活图、边界条件图、纤维方向图、预测-实验并排图、误差图、全局误差统计。
- 段落结构：先说“为什么传统证据不够”，再说“本文数据如何打开内部空间”，最后用“误差反推模型改进方向”收束。
- 句型骨架：Although global responses are comparable, spatially resolved fields reveal mechanism-specific discrepancies.
- 引用组织：临床背景文献只铺问题，方法文献只证明工具，真正说服交给本文全场证据。
- 不宜直接模仿：没有全场数据、边界条件或内部机制图时，不应借用本文的“full volume inverse modeling”强叙事。

## 18. 对我写论文的启发
如果写类似论文，可以学三点。第一，把数据优势写成方法必要性，而不是“我们也测了很多图”。本文把 MRI 全体积数据直接和 VSI 可辨识性绑定，这比单纯展示图像更有力。第二，模型比较要落到机制空间：NH 不是因为误差数字大而失败，而是因为不能重现撕裂内部剪切和滑移。第三，Discussion 可以把每个局限变成下一代模型需求：I3 误差指向体积项，I4 误差指向纤维方向场，low-displacement error 指向测量噪声和参数驱动区域。

可迁移到 Introduction：用“传统测量维度不足”制造 gap。可迁移到 Method：把每个处理步骤都解释为反演链中的必要环节。可迁移到 Results/Discussion：用误差地图说明模型在哪里不对，而不只报告平均误差。

需要避免：过早把方法示范写成临床工具；在数据不足时声称材料参数普适；把神经网络展望加入结论时要明确它是 future work。

## 19. 最终浓缩
最值得学习：用全体积空间场作为本构反演证据，把“模型能不能解释内部机制”从抽象讨论变成体素级预测/误差问题。

最大风险：MRI 分辨率、边界条件、纤维方向估计、单一加载和动物模型限制，使参数外推必须谨慎。

三个可迁移动作：
1. 在 Introduction 中把测量盲区写清楚：已有方法不是错，而是看不到本文 claim 需要的内部变量。
2. 在 Results 中同时给模型参数、空间预测和误差分解，形成“参数-场-机制”的闭环。
3. 在 Discussion 中用局部误差反推 future constitutive terms，主动承认模型不完美并把局限转化为研究路线。
