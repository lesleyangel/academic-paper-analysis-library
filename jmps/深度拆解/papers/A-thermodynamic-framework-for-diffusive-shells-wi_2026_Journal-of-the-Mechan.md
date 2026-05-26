# A thermodynamic framework for diffusive shells with finite deformation: application to hydrogel systems

## 0. 读取说明
- 源 PDF：`jmps/文献/A-thermodynamic-framework-for-diffusive-shells-wi_2026_Journal-of-the-Mechan.pdf`
- 源 TXT：`jmps/文本/txt/A-thermodynamic-framework-for-diffusive-shells-wi_2026_Journal-of-the-Mechan.txt`
- 元数据：Journal of the Mechanics and Physics of Solids, 213 (2026) 106598, DOI: 10.1016/j.jmps.2026.106598。
- 是否需要结合 PDF 图像核查：需要。本文大量证据是公式、曲线和相图/参数图；txt 中图题抽取不完整，尤其 Fig. 4、Fig. 10-13、Fig. 17 及附录图需要 PDF 核查坐标、曲线分支、相分离不连续点和极限退化对比。
- 本文类型：有限变形扩散壳的热力学理论论文，应用于含大分子水凝胶球壳的自由膨胀/扩散分析。

## 1. 基本信息与论文身份
- 题名：A thermodynamic framework for diffusive shells with finite deformation: application to hydrogel systems。
- 作者/机构：Minghui Hu; Wenyi Wang; Xiaowei Yan; Chengxiang Zheng; Yan Wang; Zichen Deng; Tao Wu。机构为 Northwestern Polytechnical University。
- 关键词：Covariant theory; Thermodynamics; Finite deformation; Diffusive Shell; Hydrogel。
- 研究对象：有限变形下具有扩散行为的薄壳，特别是含内包大分子的 spherical hydrogel shell。
- 研究尺度：三维壳体到等效中面的降维理论；几何、力学、化学势、浓度、通量、自由能、曲率之间的耦合。
- 方法类型：covariant tensor analysis + Gaussian local coordinates + Gurtin continuum thermodynamics + thickness integration + uniform chemical potential approximation + hydrogel free energy specialization + asymptotic validation。
- 证据类型：理论推导、等效中面控制方程、球壳边值问题闭式解、Flory parameter/chemical potential/crosslinking/macromolecule percentage/radius-thickness ratio 参数分析、block/plate 极限退化验证。
- 目标读者：壳理论、水凝胶、软活性材料、扩散-力学耦合、有限变形热力学和药物递送微胶囊设计读者。
- JMPS 风格定位：重理论、重一致性。贡献不是某个算例性能，而是把扩散、有限变形、壳降维和热力学第二定律统一成中面理论。

## 2. 摘要与核心信息提取
摘要先声明建立 comprehensive thermodynamic theory，用于 analyzing finite deformations in diffusive shells。方法上用 covariant tensor analysis 和 Gaussian local coordinate parametrization 描述壳几何与运动学；基于 Gurtin framework，通过 velocity field 分解为 in-plane、transverse 和 rotational 三个独立运动学分量，推导 force equilibrium、orthogonal/lateral moment equilibria；再结合 mass conservation 做厚度积分，形成 equivalent mid-surface theory。关键简化是假定 chemical potential through thickness uniform，将 governing differential equations 转为 difference form，降低计算成本。应用上将理论用于 stimuli-responsive hydrogels with surface free energy，得到含大分子球壳在液体介质中的闭式解。结果揭示两个现象：Flory 参数对 hydrogel 与 inner solution 的反直觉影响，以及 phase separation 诱发的不连续变形。最后用两个极限验证：radius-thickness ratio 接近一时退化为 bulk hydrogel，曲率趋零时退化为 Kirchhoff plate。

一句话主张：通过协变几何、热力学厚度积分和均匀化学势假设，可以把三维扩散水凝胶壳降维为热力学一致的中面理论，并解释球壳膨胀中的参数敏感性与相分离不连续。

核心关键词：diffusive shell；finite deformation；mid-surface reduction；uniform chemical potential；hydrogel shell；phase separation；limit recovery。

## 3. 选题层深拆
问题来源是软活性壳结构的 chemo-mechanical coupling。水凝胶球壳、微胶囊、药物递送系统在溶剂环境中会发生溶胀、扩散、曲率变化和厚度变形，三维全模型计算成本高，传统薄壳模型又常不足以处理有限变形与扩散热力学。

问题重要性有两层。理论上，扩散壳不是单纯弹性壳，需要同时满足力平衡、矩平衡、质量守恒和熵不等式；工程上，含大分子内溶液的水凝胶壳可用于 responsive microcapsules/drug delivery，其膨胀和相分离直接影响释放、稳定性和形态。

问题为什么现在值得做：Gurtin continuum thermodynamics、covariant shell theory 和水凝胶 Flory-Rehner 类型自由能已成熟，但它们需要一个统一的 finite deformation diffusive shell formulation，尤其是能在中面上表达化学势、通量和等效自由能。

问题边界：理论假定壳厚相对面内尺度小，采用一阶 deformation field；uniform chemical potential through thickness 是关键简化；应用算例为球壳自由膨胀，不覆盖复杂边界、非均匀加载、断裂、三维屈曲或动力学失稳。

选题 JMPS 味道很浓：不是用有限元跑水凝胶，而是从热力学和几何出发做维度约化，最后用物理极限恢复来证明理论一致性。

## 4. 领域位置与文献版图
虽然当前抽取重点在摘要和目录，仍能看出作者的文献位置：一条线是 classical continuum thermodynamics，特别是 Gurtin 框架；一条线是 finite deformation shell theory/covariant theory；一条线是 hydrogel swelling/diffusion/free energy；另一条线是 soft active shells 和 microcapsule applications。

已有研究通常能处理单一层面：三维扩散-力学模型物理完整但计算重；传统壳理论处理几何和力矩平衡但扩散/化学势耦合不足；水凝胶模型能处理体材料溶胀但不直接适合曲率壳和中面降维。

本文站在三条线交点：把三维热力学不等式和控制方程投影/积分到壳中面，同时保留 bending/twisting moments、surface flux、equivalent concentration 和 chemical potential。

最接近前人应是 Gurtin 的连续体框架、Kirchhoff/Koiter 类壳理论、Flory-Rehner 水凝胶理论、扩散界面理论。作者通过 block 和 plate 极限退化来证明自己不是孤立新模型，而是能回到经典理论。

风险：如果前人已有类似 diffusive shell 中面理论，本文需明确说明其 finite deformation、rotation tensor、uniform chemical potential simplification 或 hydrogel/macromolecule application 的差异。

## 5. Gap 制造机制
明示 gap：缺少适用于 finite deformation diffusive shells 的 comprehensive thermodynamic framework，可从三维理论系统降维到中面，并同时处理力学平衡、矩平衡、质量守恒和扩散。

隐含 gap：直接三维建模成本高；传统薄壳模型对 through-thickness diffusion 和 chemical potential 边界处理不够高效；球壳内包大分子导致内外化学势和相分离效应，简单体模型难以体现曲率和厚度。

gap 类型：理论 gap + 降维 gap + 应用解释 gap。理论上需要第二定律一致性；降维上需要从三维壳到中面变量；应用上需要解释水凝胶球壳参数如何影响 hoop stretch、thickness stretch 和 volume change。

gap 证据来自摘要中的“comprehensive thermodynamic theory”和结论中的“middle surface equivalent theory”。作者不靠大规模文献批评制造 gap，而是靠理论构造的完整性。

审稿追问：uniform chemical potential through thickness 是否适用于快速扩散或厚壳；一阶 kinematics 是否能充分捕捉厚度方向变化；闭式解是否依赖强对称；相分离不连续是否由自由能模型参数选择导致。

## 6. 创新性判断
作者声称的贡献是 finite deformation diffusive shells 的 thermodynamic framework，并应用于 hydrogel systems。真实创新包括：1. 以 covariant tensor + Gaussian coordinates 描述壳几何；2. 将速度场分解为 in-plane、transverse、rotational 分量，推导 force/moment equilibria；3. 通过厚度积分建立等效中面 free energy、concentration、flux 和 balance laws；4. 用 uniform chemical potential 简化扩散分析；5. 对球形水凝胶壳给闭式解并揭示 phase separation/参数反直觉现象；6. 通过 block/plate 极限恢复验证。

创新类型：理论框架创新 + 应用解析解 + 极限一致性验证。创新强度高但受限于假设范围。对 JMPS 而言，热力学一致性和极限退化是强加分项。

创新必要性：强。如果没有等效中面理论，扩散壳设计要么用全 3D 模型计算昂贵，要么用过度简化模型丢失 bending/twisting 和化学势边界。

容易被挑战点：公式推导复杂，读者需要相信 approximations；应用只到球壳，缺少一般几何数值例子；chemical potential uniform assumption 可能是最关键也最脆弱的简化。

## 7. 论证链条复原
背景：软活性壳在溶胀、扩散、药物递送和微胶囊中常经历有限变形。 -> 文献/理论基础：三维连续体热力学、covariant shell kinematics、水凝胶自由能。 -> gap：缺少将三维扩散-力学热力学系统降维到中面的统一壳理论。 -> 问题：如何在保留力/矩平衡和质量守恒的同时建立有限变形扩散壳模型。 -> 方法：定义壳几何和运动学；分解速度场；应用第二定律和三维 constitutive relation；厚度积分获得中面等效方程；假定化学势厚度均匀；指定水凝胶自由能。 -> 证据：推导方程、Table 1 方程总结、球壳边值问题、参数曲线、相分离不连续、block/plate 极限恢复。 -> 发现：Flory parameters、crosslinking、chemical potential、macromolecule percentage、radius-thickness ratio 控制 hoop/thickness stretch；内外 Flory 参数对不同方向伸长有反直觉影响；特定大分子比例导致相分离不连续。 -> 意义：为 diffusive soft shells 和 responsive microcapsules 提供热力学一致设计基础。

链条强处是“推导 -> 特化 -> 极限验证”。薄弱处是“理论曲线 -> 真实系统”的实验验证不足。

## 8. 方法/理论/模型细拆
几何运动学：用 Gaussian local coordinates 参数化壳，material point 的位置写成中面点运动加厚度方向相对运动。附录强调一阶 kinematics `x(p, zeta, t)=f(p,t)+zeta l(p,t)` 的合理性，其中 `l` 含 stretch 和 rotation tensor，可捕捉 bending/twisting，而不是简单 membrane。

热力学推导：基于三维自由能和熵不等式，推导 constitutive relations 和 balance laws。速度场分解为 in-plane、transverse、rotational 三个独立分量，从而分别得到 force equilibrium、orthogonal/lateral moment equilibria。

中面降维：沿厚度积分得到 equivalent stress、couple stress、body force/couple、concentration、flux 和 surface free energy。mass conservation 与 solvent flux 被转化为中面方程。

扩散简化：uniform chemical potential across thickness 假设将复杂厚度方向微分问题简化为上下表面化学势差/通量差形式。附录 II 通过 Taylor expansion 和 leading-order approximation 给出论证。

水凝胶特化：指定 free energy density 后处理球形 hydrogel shell，包含内部 macromolecules 和外部 solvent reservoir。输出指标是 hoop stretch ratio lambda、thickness stretch ratio alpha、volume change ratio 等。

验证：radius-thickness ratio 接近 1 时退化为 bulk/block hydrogel free swelling；curvature 接近 0 时退化为 plate theory。这个验证方式比单纯数值收敛更适合理论论文。

## 9. 证据系统与 Claim-Evidence 表
| Claim | 位置 | 支撑证据 | 证据类型 | 强度 | 风险 |
| --- | --- | --- | --- | --- | --- |
| 可建立热力学一致的有限变形扩散壳中面理论 | Theory/Section 2 | covariant kinematics、second law、balance laws、thickness integration | 理论推导 | 强 | 推导细节需读 PDF 公式 |
| 速度场三分解能导出 force 和 moment equilibria | Abstract/Section 2.3 | in-plane/transverse/rotational components，对应平衡方程 | 理论结构 | 强 | 依赖一阶壳运动假设 |
| uniform chemical potential 能显著简化扩散分析 | Abstract/Appendix II | 化学势厚度均匀，微分方程转 difference form | 近似论证 | 中强 | 厚壳/快速扩散条件可能失效 |
| 理论可给水凝胶球壳闭式解 | Section 3 | spherical hydrogel shell boundary value problem | 解析特化 | 中强 | 只适用于高对称场景 |
| Flory 参数等会显著影响 hoop/thickness/volume response | Fig. 10-13 等 | 参数曲线展示 lambda、alpha、V/V0 变化 | 参数分析 | 中强 | 需 PDF 核查曲线和数值范围 |
| 相分离可导致 stretch ratios 不连续变化 | Abstract/Conclusion | 初始大分子约 4% 或 2% 时出现 phase separation 诱发 jumps | 理论预测 | 中 | 需实验或相图验证 |
| 理论能恢复 block 和 plate 极限 | Section 3.3/Conclusion | radius-thickness ratio -> 1；curvature -> 0 | 极限一致性 | 强 | 极限过程细节需核查 |

证据系统以数学一致性为主，图表是理论结果展示，不是实验验证。阅读时应把“validated”理解为模型极限验证，而非实验验证。

## 10. 图表、公式与结果叙事提取
| 图/表/公式 | 功能 | 对应 claim | 说服作用 | 需要图像核查 |
| --- | --- | --- | --- | --- |
| Nomenclature | 变量系统 | 理论复杂度管理 | 降低阅读门槛 | 否 |
| Table 1 | 对应方程总结 | 中面控制方程体系 | 让理论可查 | 是/需核公式 |
| Fig. 4 | spherical hydrogel shell 初始/膨胀几何和化学势 | 应用算例定义 | 说明边值问题 | 是 |
| Fig. 10 | lambda、alpha、V/V0 vs crosslinking degree | crosslinking 控制膨胀 | 参数敏感性 | 是 |
| Fig. 11 | stretch/volume vs initial macromolecule percentage | 内包大分子影响与相分离 | 核心发现 | 是 |
| Fig. 12 | stretch/volume vs non-dimensional chemical potential | 环境化学势调控 | 外部 reservoir 效应 | 是 |
| Fig. 13 | stretch/volume vs radius-thickness ratio | 曲率/厚度影响 | 壳效应证据 | 是 |
| Fig. 17 | diffusive analysis/chemical potential reservoir 相关 | 扩散过程说明 | 需核坐标和趋势 | 是 |
| Eq. kinematics | `x=f+zeta l` | 壳降维基础 | 支撑 bending/twisting | 否 |
| Entropy imbalance/free energy equations | constitutive relations | 热力学一致性 | 理论核心 | 否 |

图表叙事没有实验论文那样丰富，但理论论文的“图表功能”在于让抽象参数有物理后果。最值得学的是 Nomenclature 和 equation summary table 对复杂理论的管理。

## 11. 章节结构与篇章布局
- Abstract：理论框架、简化假设、应用结果和极限验证。
- Introduction：应建立扩散壳理论的背景和现有不足。
- Theory of diffusive shells：全文核心，按 geometry/kinematics、constitutive relations/balance laws、free energy specification 组织。
- Spherical hydrogel shell：从一般理论特化到可解析应用，先给边值问题，再讨论 equilibrium/diffusion，再做 limit validation。
- Conclusions：总结中面理论、参数影响、phase separation 和两类极限。
- Appendices：为关键近似兜底，尤其是一阶 deformation field 与 uniform chemical potential。

最值得模仿的是主文和附录的分工：主文保持理论主线，附录专门为可能被审稿人质疑的近似做论证。

结构风险：章节和公式密度很高，若缺少 schematic 或 table，读者容易迷失；应用只占一个球壳算例，可能被认为展示面有限。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/A-thermodynamic-framework-for-diffusive-shells-wi_2026_Journal-of-the-Mechan.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：17
- 结构类型判断：接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。
- 标题并列性：同级标题并列性一般，更偏按内容对象自然展开。
- 章节名主要风格：描述型, 方法/模型型, 机制/讨论型, 背景/引言型
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
| 1 Unit tensor in R3 | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 1 Introduction | 背景/引言型 | 建立问题背景、研究动机和文献缺口 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2 Theory of diffusive shells | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1 Geometry and kinematics | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.1.1 Geometry | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.2.1 Volume integration approximation | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 2.3 Constitutive relations and balance laws | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 2.3.1 Three-dimensional formulations for constitutive relation | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.3.2 Integrated formulations on the equivalent mid-surface | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 2.3.3 Specification of free energy density | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 高 | 是 | 保留具体变量/对象 |
| 3 Spherical hydrogel shell: specialization and discussion | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 高 | 是 | 保留具体变量/对象 |
| 3.1 Formulation of the boundary value problem | 方法/模型型 | 交代模型、公式、算法、参数或求解流程 | 高 | 是 | 保留具体变量/对象 |
| 3.2 Discussions | 机制/讨论型 | 解释结果背后的物理机制或理论含义 | 中 | 是 | 可加入核心变量或机制词增强信息量 |
| 3.2.1 Equilibrium analysis | 描述型 | 描述章节内容，信息量取决于标题具体程度 | 中 | 是 | 可加入核心变量或机制词增强信息量 |

写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->

## 12. 段落功能与叙事节奏
Theory 段落节奏是“定义符号 -> 写几何关系 -> 写物理平衡 -> 积分降维 -> 解释等效量”。这种顺序非常适合理论论文：先让读者知道变量来自哪里，再给定律。

Application 段落节奏是“指定几何/化学势/自由能 -> 写边值问题 -> 给解或方程 -> 逐个参数讨论”。参数讨论中每段通常只改变一个物理量，观察 lambda、alpha、V/V0 三个输出。

Conclusion 段落按贡献层级写：先理论构造，再水凝胶球壳结果，再极限验证，最后给总体意义。没有引入新的大 claim。

可复用模板：`To reduce the three-dimensional chemo-mechanical problem to an equivalent surface theory, we integrate [balance law/free energy] through the thickness and define [equivalent variables]. Under the assumption of [approximation], the resulting equations take [simplified form], enabling [application].`

## 13. 文笔画像与语言习惯
文笔高度理论化，名词化强，常用 establish, derive, decompose, integrate, specify, validate, reduce, recover。claim 主要围绕 consistency、framework、closed-form solutions、limit cases。

谨慎表达体现在 approximation 和 validation：uniform chemical potential 被明确称为 assumption；附录论证一阶 kinematics 为什么在 intended applications 中合理。作者在结果处使用 reveals、shows、is affected by 等中性动词，避免把理论预测写成实验事实。

术语密度很高：covariant basis, mid-surface, chemical potential, equivalent flux, free energy density, hoop stretch, thickness stretch, Flory parameter, phase separation。写作上要学习它用 Nomenclature 控制术语负担。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：shell(177)；chemical(139)；hydrogel(134)；stretch(125)；thickness(115)；potential(102)；flory(95)；ratio(89)；mid-surface(73)；parameter(73)；volume(70)；deformation(68)；surface(68)；solvent(66)；hoop(66)；inner(64)；interface(63)；equivalent(54)；interior(48)；grad(47)
- 高频学术名词：deformation(136)；thickness(115)；solution(80)；parameter(73)；interface(63)；parameters(45)；condition(42)；reference(32)；energy(30)；analysis(30)；stress(28)；concentration(27)；configuration(24)；equations(23)；model(23)；balance(22)
- 高频学术动词：shown(16)；formulated(9)；proposed(9)；developed(8)；indicates(7)；compared(5)；demonstrated(5)；derived(5)；investigated(5)；capture(4)；reveal(4)；shows(4)；derive(3)；indicate(3)；validated(2)；suggests(2)
- 高频形容词：chemical(139)；potential(102)；solvent(66)；equivalent(54)；normal(41)；spherical(32)；gradient(31)；current(30)；boundary(27)；diffusive(24)；initial(24)；external(23)；local(16)；covariant(16)；internal(16)；constitutive(16)
- 高频副词/连接副词：consequently(48)；notably(16)；significantly(16)；however(12)；generally(10)；approximately(10)；therefore(8)；similarly(8)；effectively(7)；respectively(7)；initially(7)；additionally(6)；equivalently(6)；directly(6)；furthermore(5)；specifically(5)
- 高频二词短语：chemical potential(96)；flory parameter(66)；hoop stretch(54)；thickness stretch(53)；stretch ratio(47)；hydrogel flory(35)；inner flory(30)；bex bin(28)；free energy(27)；flory parameters(25)；solvent molecules(25)；spherical shell(21)；energy density(20)；inner solution(19)；chemical potentials(19)；volume change(19)
- 高频三词短语：hydrogel flory parameter(27)；hoop stretch ratio(23)；thickness stretch ratio(22)；free energy density(20)；inner flory parameter(19)；subdomains bex bin(13)；hydrogel spherical shell(13)；stretch ratio thickness(13)；ratio thickness stretch(13)；inner flory parameters(11)；volume change ratio(11)；uniform chemical potential(10)

**主动、被动与句法**

- 被动语态估计次数：212
- `we + 动作动词` 主动句估计次数：3
- 名词化表达估计次数：1428
- 语态判断：被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：415
- 一般过去时线索：41
- 现在完成时线索：6
- 情态动词线索：79
- 时态判断：一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

- Abstract/首页：equivalent(11)；interface(11)；mid-surface(10)；deformation(9)；shell(9)；chemical(9)；reference(9)；tensor(8)
- 1. Introduction：deformation(16)；theory(16)；hydrogel(12)；shell(10)；plate(10)；diffusion(10)；thickness(10)；potential(9)
- 2. Theory of diffusive shells：shells(2)；section(1)；theories(1)；diffuse(1)；formulated(1)；covariant(1)；theory(1)；unified(1)
- 2.1. Geometry and kinematics：geometry(2)；shell(2)；subsection(1)；kinematics(1)；specified(1)；covariant(1)；theory(1)；defined(1)
- 2.1.1. Geometry：grad(15)；mid-surface(14)；point(9)；reference(8)；normal(8)；surface(8)；vector(7)；shell(5)
- 2.2.1. Volume integration approximation：interface(12)；volume(7)；surface(7)；field(6)；thickness(6)；geometry(5)；mid-surface(5)；element(4)
- 2.3.1. Three-dimensional formulations for constitutive relation：interface(38)；bex(22)；bin(21)；chemical(12)；jex(12)；jin(12)；subdomains(10)；sex(9)
- 2.3.2. Integrated formulations on the equivalent mid-surface：shell(29)；surface(23)；equivalent(21)；chemical(21)；thickness(18)；detf(16)；divm(14)；potential(13)

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->

## 14. 常用词、句式与可复用表达提取
### 14.1 问题与 gap 表达
- 句型骨架：`This study establishes a comprehensive thermodynamic theory for analyzing finite deformations in [coupled system].`
- 中文启发：理论论文可用“establishes a framework”开门见山，但后文必须证明完整性。

### 14.2 方法与框架表达
- 句型骨架：`The geometric description employs [mathematical tool] with [coordinate/parameterization] to characterize [kinematics].`
- 句型骨架：`Building upon [classical framework], we derive [balance laws] through systematic decomposition of [field].`

### 14.3 结果与趋势表达
- 句型骨架：`The impacts of key physical and geometrical parameters are investigated, including [A], [B], and [C].`
- 句型骨架：`Our analysis reveals [phenomenon 1] and [phenomenon 2].`

### 14.4 机制解释表达
- 句型骨架：`The assumption of [uniform variable] simplifies [analysis] by converting [differential form] into [reduced form].`

### 14.5 贡献与意义表达
- 句型骨架：`The theory demonstrates mathematical consistency through asymptotic recovery of [limit case A] and [limit case B].`

### 14.6 局限与未来工作表达
- 可复用骨架：`Future work should test the limits of the [assumption] under transient diffusion, thick-shell geometries, and experimentally measured swelling paths.`

## 15. 引用策略与文献使用
从结构看，引用应主要服务四个功能：1. 经典热力学与 continuum theory，提供第二定律和 free energy imbalance 合法性；2. shell/covariant theory，支撑几何和中面降维；3. hydrogel swelling/free energy，支撑 Flory 参数和 crosslinking 等；4. applications，如 drug delivery 和 microcapsules，支撑工程意义。

引用姿态应该是继承和扩展，不是批判。理论论文更常说“building upon classical framework, we derive...”而不是“existing methods fail”。gap 通过“尚无统一降维框架”隐性制造。

引用风险：壳理论和水凝胶理论都有庞大文献，若遗漏相邻 diffusive shell 或 poroelastic shell 工作，审稿人会敏感。极限恢复有助于缓解这类风险，因为它显示作者知道经典边界。

## 16. 审稿人视角风险
最大攻击面：uniform chemical potential assumption。对于厚壳、快速溶胀、强边界通量、内外化学势差大或瞬态扩散早期，厚度方向化学势可能不均匀。

第二风险：一阶 kinematics 是否足够。附录解释 bending/twisting 可通过 rotation tensor 捕捉，但对于厚壳或高阶剪切/厚度变形，可能需要二阶理论或全 3D。

第三风险：相分离和不连续变形是理论预测，缺少实验验证或数值 full 3D 对照。审稿人可能要求比较现有 hydrogel shell 实验或高保真有限元。

claim 是否过强：应用意义如 drug delivery/microcapsule design 应写为 relevance，而非已验证设计准则。

复现风险：公式多、符号多，若 equation table 不够清楚，读者难以独立实现。

## 17. 可复用资产
- 可复用选题角度：从三维多物理问题的计算负担切入，建立热力学一致降维理论。
- 可复用 gap 制造：全 3D 太重，经典壳太简，本文做扩散-力学中面理论。
- 可复用论证链：几何运动学 -> 热力学不等式 -> 平衡方程 -> 厚度积分 -> 等效变量 -> 特化自由能 -> 参数分析 -> 极限恢复。
- 可复用图表设计：Nomenclature + 方程总结表 + 参数曲线 + 极限验证图，是理论论文的稳健配置。
- 可复用句型：`The developed framework yields closed-form solutions for [specialized system] and recovers [classical theories] in limiting cases.`
- 不宜直接模仿处：如果无法证明近似假设或做极限恢复，不要声称 thermodynamic framework 完整。

## 18. 对我写论文的启发
写理论框架论文时，可以学它把“复杂”变成“可导航”：先列清符号，再分解运动学，再推导 balance，再应用到一个高对称但有物理意义的例子。不要一上来就给全部方程，而是让每个数学动作都有物理原因。

Introduction 可迁移写法：不要泛泛说模型不足，而要指出三维模型和壳模型之间缺一个热力学一致中间层。Method 可迁移写法：把关键近似放到附录深入论证。Results 可迁移写法：用极限恢复作为理论可信度证据。

需要避免的问题：只给复杂公式不做物理解释；只做一个算例却声称广泛适用；忽略近似条件和极限边界。

## 19. 最终浓缩
这篇论文最值得学的是：如何把 finite deformation、diffusion、shell kinematics 和 thermodynamics 系统降维为中面理论，并用闭式球壳解和经典极限恢复来证明框架可信。

最大风险是：uniform chemical potential 和一阶壳运动学假设决定了理论适用边界，真实瞬态厚壳扩散或复杂几何可能超出范围。

三个可迁移动作：1. 用“全 3D 与简化理论之间缺中间层”制造理论 gap；2. 用 Nomenclature/方程表管理复杂公式；3. 用极限退化而不只是曲线展示来验证理论一致性。
