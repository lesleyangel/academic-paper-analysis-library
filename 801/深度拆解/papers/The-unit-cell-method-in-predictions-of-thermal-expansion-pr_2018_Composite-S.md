# The unit cell method in predictions of thermal expansion properties of textile reinforced composites

## 0. 读取说明

- 文本来源：`801/文本/txt/The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S.txt`，PyMuPDF 抽取，19 页。
- 抽取文本包含摘要、引言、理论推导、单胞构造、材料参数、结果讨论、结论和主要图表标题，可支撑深度拆解。
- 原文双栏排版导致部分结论与参考文献交错，图中位移云图、边界面编号和非均匀位移细节均标注为“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：Introduction, Mathematical formulation, Results and discussion, Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：The unit cell method in predictions of thermal expansion properties of textile reinforced composites。
- 作者：Jian-Jun Gou, Chun-Lin Gong, Liang-Xian Gu, Shuguang Li, Wen-Quan Tao。
- 期刊：Composite Structures, 195 (2018) 99-117。
- 领域：织物增强复合材料、热膨胀系数、单胞方法、对称结构、热-力耦合数值预测。
- 论文类型：理论规则总结 + 单胞边界条件推导 + 多类复合材料算例验证。
- 研究对象：UD 单向纤维复合材料、plain woven 平纹织物复合材料、多综 satin woven 织物复合材料。
- 主要方法：从平移、反射、180°旋转三类结构对称性出发，总结均匀温度变化下对称节点位移关系，推导不同尺寸 unit cell 的约束边界条件，并用有限元计算有效 CTE、等效弹性参数和局部位移/应力场。
- 论文身份判断：这不是一篇“报告某种材料 CTE 数值”的材料论文，而是一篇方法论论文，核心是让小尺寸单胞在热膨胀问题中具备严格物理边界。

## 2. 摘要与核心信息提取

本文的核心主张是：具有结构对称性的织物增强复合材料，其有效热膨胀性质可以通过缩小后的 unit cell 高效预测；但每一次利用平移、反射或 180°旋转对称性缩小几何域，都必须同步推导新的位移边界条件，否则单胞虽然几何上代表了原结构，力学上却可能不代表原结构。

摘要的说服方式很清楚：先说热膨胀性质可由尺寸受限的单胞计算，再说边界条件推导需要三类对称结构中的位移场规则；随后用 UD、plain woven 和多综 satin woven 三类材料覆盖从简单周期结构到复杂织物结构的谱系。最终通过不同尺寸单胞得到相同有效性质，以及与文献结果一致，证明规则不是个别算例技巧。

一句话浓缩：本文把“如何为热膨胀问题建立可缩小、可验证、边界条件严格的复合材料单胞”从经验操作整理成一套对称性驱动的方法。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/The-unit-cell-method-in-predictions-of-thermal-expansion-pr_2018_Composite-S.md`。

中文译文：

> 具有一定结构对称性的织物增强复合材料的热膨胀性能可以通过尺寸有限的晶胞有效地计算。本文提出了建立这种晶胞模型的通用方法。在晶胞边界条件的推导中，根据均匀温度变化载荷下平移、反射和180°旋转对称结构的位移场，总结出3条规则。从热学和力学的角度阐明了本晶胞方法的应用范围。然后研究了三种典型的复合材料，即单向纤维增强复合材料、平纹编织复合材料和多线(4HS、5HS、6HS、7HS和8HS)缎纹编织复合材料，并分别配制了四个、三个和两个尺寸减小的晶胞。分析了每种复合材料的热膨胀行为，并预测了有效热膨胀系数。阐明了结构对称性对晶胞模型变形模式的影响。数值模型通过从不同尺寸的晶胞获得的相同结果以及文献中可用的结果进行验证。本文开发的方法可应用于具有相关结构对称性的任何其他复合材料的热膨胀研究。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自高温飞行器和热防护结构中一个非常实际的问题：复合材料在严酷热环境下工作，温度快速升高会诱发组分间热膨胀失配，继而导致局部应力、损伤和结构失效。要在工程设计前掌握这些材料的有效 CTE 和局部应力分布，直接建立宏观全结构模型代价很高，因此需要代表性单胞。

作者把大问题收束成一个更小但更尖锐的问题：以往纺织复合材料热性质研究大多只用基于平移对称的周期单胞；但许多织物结构还包含反射和 180°旋转对称性，可以进一步缩小模型。缩小几何尺寸本身并不难，真正难的是热膨胀下位移约束如何随对称路径变化。

这篇论文的选题价值不在“预测了几个 CTE 数值”，而在“阻止单胞建模中一种隐性错误”：把几何代表性等同于物理代表性。作者用统一规则告诉读者，单胞的可用性由两件事共同决定：几何是否来自真实对称性，边界条件是否能恢复宏观均匀温度载荷下的位移场。

## 4. 领域位置与文献版图

文献版图先从复合材料有效性质预测展开：一类是 Mori-Tanaka、自洽、微分法等解析/半解析均匀化方法，优点是效率高，缺点是几何限制强；另一类是 FE/RVE 数值方法，能捕捉局部场，但依赖模型尺寸、微结构重构和边界条件。

随后作者区分随机复合材料 RVE 和有序结构 unit cell。随机材料只能近似代表宏观统计结构；规则织物和单向纤维复合材料具有明确对称性，理论上可以得到“准确代表”的单胞，但前提是边界条件严格。这个区分为本文站位提供了基础：作者并不是要替代所有 RVE 方法，而是在有序对称复合材料这一子域中完善 UC 方法。

文献使用上，作者把前人工作放在三条线上：热膨胀/热导率有效性质预测、织物/编织复合材料单胞建模、作者团队此前关于热导率单胞的工作。本文相当于把热导率论文中的温度分布规则迁移到热膨胀问题，并补上位移分布规则。

## 5. Gap 制造机制

本文制造 gap 的方式是“方法使用边界未被澄清”。

第一层 gap：既有研究广泛使用 unit cell，但大多默认周期边界足够，未充分利用反射和旋转对称性进一步缩小计算域。这个 gap 指向效率。

第二层 gap：利用更高阶对称性后，边界条件不能沿用普通周期条件。热膨胀问题不是纯热传导问题，载荷是均匀温度变化，响应是位移场和应变场；因此需要对称节点的相对位移关系，而不是只需要温度关系。这个 gap 指向正确性。

第三层 gap：很多单胞研究关注有效性质结果是否接近，却较少分析边界面上的法向位移是否均匀、是否由反射对称性保证。作者把“边界位移模式”作为新的检查对象，使 gap 从公式推导延伸到可视化验证。

这个 gap 的强度在于它能解释一个工程建模痛点：错误边界条件有时仍会给出看似合理的有效性质，但会误导局部应力/损伤分析。

## 6. 创新性判断

- 创新类型：理论规则总结 + 方法规范化 + 多结构算例验证。
- 真实创新点 1：将均匀温度变化下三类结构对称性中的相对位移关系写成统一形式，用 `k, m, n` 参数区分平移、反射和 180°旋转。
- 真实创新点 2：明确热膨胀单胞方法的适用范围，即建立在均匀宏观应变场假设上，只适合均匀温度加载或等效热残余应力问题。
- 真实创新点 3：对 UD、plain woven、多综 satin woven 分别构造多尺寸单胞，并用不同单胞得到一致有效性质来验证边界条件。
- 创新强度：中等偏强。它不是新材料发现，也不是新有限元算法，但对复合材料多尺度建模中的“正确边界条件”问题有明显规范化价值。
- 可挑战之处：单胞规则建立在理想周期/对称几何上，对真实织物缺陷、纱线偏移、孔隙和温度梯度不直接适用。

## 7. 论证链条复原

全文论证链可以复原为：

1. 高温环境下复合材料热膨胀失配会导致损伤，因此需要可靠预测有效 CTE 和局部热应力。
2. 宏观模型成本高，unit cell 是高效替代；但 unit cell 必须同时具备几何代表性和物理边界代表性。
3. 现有热膨胀单胞多依赖平移周期性，未系统利用反射和 180°旋转对称性。
4. 对称性缩小单胞后，必须推导相应的位移边界条件。
5. 作者先从三类基本对称结构总结对称节点相对位移规则，并用简单数值算例验证。
6. 再把规则应用到 UD、plain woven、satin woven 的具体几何，逐步构造 UC1/UC2/UC3/UC4 等模型。
7. 用相同材料参数和温度载荷计算不同尺寸 UC 的位移场、弹性参数和 CTE。
8. 若不同尺寸 UC 给出一致有效性质，说明边界条件推导正确；若边界法向位移模式与对称性解释一致，说明物理机制闭合。
9. 最后回到应用边界：该方法适合均匀温度变化，且可为局部应力/损伤分析提供基础。

薄弱环节在第 8 步：一致性验证主要是数值自洽和文献对比，缺少真实热膨胀实验的系统验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell. Composite Structures 195 (2018) 99–117 Contents lists available at ScienceDirect Composite Structures journal homepage: www.elsevier.com/locate/compstruct T Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell.
- 本文解决方式：In this paper, a general approach is developed for the establishment of such a unit cell model. The application scope of present unit cell method is clarified from the thermal and mechanical point of views. The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
- 学术或工程增量：需结合 Results/Conclusion 的量化结果复核。
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法的理论核心是把单胞构造拆成两个动作：识别结构对称性，推导边界条件。平移对称得到基础 UC1，反射和 180°旋转可进一步得到更小 UC，但每次缩小都会产生新的边界面和更复杂的位移约束。

位移规则来自宏观均匀应变场。平移对称中，对称节点的相对位移保持同号；反射面垂直某方向时，该方向位移相对量变号，平行方向保持同号；180°旋转轴平行某方向时，轴向位移保持同号，垂直方向位移变号。作者把这些关系整理为 `uM-uO = k(uM'-uO')`、`vM-vO = m(vM'-vO')`、`wM-wO = n(wM'-wO')`。

算例层面，UD 复合材料用于展示最清楚的对称性递进：由平移对称得到 UC1，再由反射和旋转对称缩小到 UC2、UC3、UC4。Plain woven 用三种 UC 展示二维织物中 in-plane 反射对称和 through-thickness 平移结构的差异。Satin woven 用 4HS 至 8HS 多综结构展示复杂纱线走向下的统一边界公式。

数值模型中，纤维和树脂作为示例材料，弹性模量分别为 10 GPa 和 1 GPa，CTE 分别为 5 和 50 `10^-6 /°C`，泊松比分别为 0.2 和 0.3。温度载荷通常为 20 °C，参考温度为 0 °C。Plain woven 的纱线体积分数约 0.5421，对应纤维体积分数 0.33；satin woven 纱线体积分数约 0.45，对应纤维体积分数 0.27。

复现要点是：不能只复现几何尺寸和材料参数，还要复现每个边界面上对称节点的配对方式、局部坐标系、相同网格要求和冗余顶点约束处理。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
|---|---|---|---|---|
| 对称结构复合材料的有效 CTE 可以用缩小单胞高效预测 | 摘要、结论 | UD、plain woven、satin woven 多尺寸 UC 得到近似相同弹性参数和 CTE | 强 | 仅限理想对称几何 |
| 热膨胀单胞边界条件必须基于位移分布规则，而不能照搬热传导温度规则 | Section 2 | 三类对称结构中相对位移关系 Eq. 4-9，并用数值位移场验证 | 强 | 推导依赖均匀宏观应变假设 |
| 不同尺寸单胞的结果一致可验证 BC 正确性 | Results | Plain woven 三个 UC 最大偏差约 0.56%；satin woven 两个 UC 最大偏差约 0.19% | 强 | 自洽验证多于外部实验验证 |
| 该方法可同时得到有效性质和局部应力/位移场 | 结论 | 位移场图、应力/变形图和有效参数表共同展示 | 中 | 局部应力细节依赖网格和材料模型，需要 PDF 图像复核 |
| 反射对称相关边界可出现均匀法向位移，平移/旋转边界未必均匀 | Section 5.4、Table 13 | UD、plain woven、satin woven 的 normal displacement pattern 汇总 | 强 | “relative uniform” 的图像判断需要 PDF 复核 |
| 方法适用范围是均匀温度变化导致的热膨胀，不适合任意非均匀温度场 | 结论 | 作者明确说明 BC 基于 uniform macro strain field，可由 uniform temperature loading 引起 | 强 | 后续读者若用于温度梯度场会越界 |
| 对复杂 satin woven 也可写成统一边界条件 | Section 4-5 | 4HS-8HS 使用同一类几何参数和边界公式，表中 CTE/弹性参数一致 | 中强 | 真实 satin 织物几何误差未纳入 |

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 复核备注 |
|---|---|---|---|
| Fig. 1-4 三类对称结构与位移场 | 证明平移、反射、旋转对称下相对位移规则可被数值场验证 | BC 推导有物理基础 | 位移云图需要 PDF 图像复核 |
| Eq. 3 温度关系与 Eq. 4-9 位移关系 | 将热导率单胞规则扩展到热膨胀问题 | 热膨胀需要位移边界 | 公式符号已从文本提取，排版需 PDF 复核 |
| Table 1 `k,m,n` 参数 | 把不同对称性压缩成可查表的推导工具 | 统一 BC 推导 | 表头方向关系需 PDF 复核 |
| Fig. 6-8 UD、plain woven、satin woven 单胞 | 展示几何缩小路径 | 每次利用对称性都生成新 UC | 图中边界编号需要 PDF 复核 |
| Fig. 12 meshed models / Table 7 grid cost | 说明缩小 UC 带来计算成本节省 | 方法有工程效率价值 | 具体节点/单元数需 PDF 复核 |
| Table 10-12 有效性质结果 | 用不同 UC 的结果一致性验证 BC | 数值自洽性 | 表格因双栏抽取可能错行，需 PDF 复核 |
| Fig. 14-20 位移场与变形图 | 展示各 UC 的位移分布与变形一致性 | 局部场也被保留 | 图像细节需要 PDF 图像复核 |
| Table 13 normal displacement pattern | 将复杂图像观察归纳成边界均匀/非均匀规则 | 边界模式与对称性相关 | 需要 PDF 图像复核 |

结果叙事的顺序是“先有规则，再有几何，再有数值一致性，再有边界位移解释”。这使论文避免沦为多个材料算例的罗列，而像一个规则被逐层验证的工具论文。

## 11. 章节结构与篇章布局

真实章节顺序为：Introduction；Temperature and displacement distributions in symmetric structures；Development of unit cells；Numerical model；Results and discussion；Conclusions。结构并非标准 IMRaD，而是“规则提出-单胞构造-算例验证”的方法论文结构。

Introduction 用高温复合材料应用价值开场，随后进入有效性质预测方法比较，再指出现有单胞多依赖平移对称。第二章承担理论地基功能：不急于进入材料，而是先把三类对称结构中的位移关系讲清楚。第三章将规则映射到具体单胞几何。第四章处理数值实现细节，包括材料参数、网格和局部坐标。第五章才展示 UD、plain woven 和 satin woven 的结果。

章节命名偏好是描述性而非结果性标题，例如 “Development of unit cells”“Results and discussion”。小节标题按对象组织：先 UD，再 plain woven，再 satin woven，最后 normal displacement on boundary planes。最值得模仿的是最后一个小节：作者没有只给表格结果，而是回头解释边界位移模式，把方法规则的物理意义再次扣紧。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: Introduction（背景定位/文献缺口）
- L2 p.2: Mathematical formulation（方法/模型/算法）
  - L3 p.2: Constitutive equations（对象/模块/过渡章节）
  - L3 p.3: Temperature and displacement distributions in symmetric structures（对象/模块/过渡章节）
    - L4 p.3: Translational symmetric structure（对象/模块/过渡章节）
    - L4 p.4: Reflectional symmetric structure（对象/模块/过渡章节）
    - L4 p.4: 180° rotational symmetric structure（对象/模块/过渡章节）
    - L4 p.4: Summary of displacement distribution rules（对象/模块/过渡章节）
    - L4 p.5: Application scopes（结果/验证/讨论）
- L2 p.5: Development of unit cells（对象/模块/过渡章节）
  - L3 p.6: Unit cells of fiber yarns（对象/模块/过渡章节）
    - L4 p.6: Formulation of unit cells（方法/模型/算法）
    - L4 p.7: Boundary conditions（对象/模块/过渡章节）
  - L3 p.7: Unit cells of plane woven composites（对象/模块/过渡章节）
    - L4 p.7: Formulation of unit cells（方法/模型/算法）
    - L4 p.8: Boundary conditions（对象/模块/过渡章节）
  - L3 p.8: Unit cells of satin woven composites（对象/模块/过渡章节）
    - L4 p.8: Formulation of unit cells（方法/模型/算法）
    - L4 p.9: Boundary conditions（对象/模块/过渡章节）
  - L3 p.9: Summary（对象/模块/过渡章节）
- L2 p.9: Numerical modeling（方法/模型/算法）
  - L3 p.9: Application of boundary conditions（结果/验证/讨论）
  - L3 p.11: Model discretization（方法/模型/算法）
  - L3 p.13: Material properties（对象/模块/过渡章节）
- L2 p.13: Results and discussion（结果/验证/讨论）
  - L3 p.13: Thermal expansion of UD composite（对象/模块/过渡章节）
    - L4 p.13: Thermal expansion behaviors（对象/模块/过渡章节）
    - L4 p.13: Effective CTE and validation of numerical models（方法/模型/算法）
  - L3 p.13: Thermal expansion of plain woven composite（对象/模块/过渡章节）
    - L4 p.13: Thermal expansion behaviors（对象/模块/过渡章节）
    - L4 p.14: Effective CTE and validation of boundary conditions（结果/验证/讨论）
  - L3 p.14: Thermal expansion of satin woven composite（对象/模块/过渡章节）
    - L4 p.14: Thermal expansion behaviors（对象/模块/过渡章节）
    - L4 p.15: Effective CTE and validation of boundary conditions（结果/验证/讨论）
  - L3 p.15: Normal displacement on boundary planes（对象/模块/过渡章节）
- L2 p.17: Conclusions（结论/贡献回收）
- L2 p.18: Acknowledgment（尾部材料）
- L2 p.18: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| Introduction | 1 | 2 | 背景定位/文献缺口 |
| Mathematical formulation | 2 | 2 | 方法/模型/算法 |
| Constitutive equations | 2 | 3 | 对象/模块/过渡章节 |
| Temperature and displacement distributions in symmetric structures | 3 | 3 | 对象/模块/过渡章节 |
| Translational symmetric structure | 3 | 4 | 对象/模块/过渡章节 |
| Reflectional symmetric structure | 4 | 4 | 对象/模块/过渡章节 |
| 180° rotational symmetric structure | 4 | 4 | 对象/模块/过渡章节 |
| Summary of displacement distribution rules | 4 | 4 | 对象/模块/过渡章节 |
| Application scopes | 5 | 4 | 结果/验证/讨论 |
| Development of unit cells | 5 | 2 | 对象/模块/过渡章节 |
| Unit cells of fiber yarns | 6 | 3 | 对象/模块/过渡章节 |
| Formulation of unit cells | 6 | 4 | 方法/模型/算法 |
| Boundary conditions | 7 | 4 | 对象/模块/过渡章节 |
| Unit cells of plane woven composites | 7 | 3 | 对象/模块/过渡章节 |
| Formulation of unit cells | 7 | 4 | 方法/模型/算法 |
| Boundary conditions | 8 | 4 | 对象/模块/过渡章节 |
| Unit cells of satin woven composites | 8 | 3 | 对象/模块/过渡章节 |
| Formulation of unit cells | 8 | 4 | 方法/模型/算法 |
| Boundary conditions | 9 | 4 | 对象/模块/过渡章节 |
| Summary | 9 | 3 | 对象/模块/过渡章节 |
| Numerical modeling | 9 | 2 | 方法/模型/算法 |
| Application of boundary conditions | 9 | 3 | 结果/验证/讨论 |
| Model discretization | 11 | 3 | 方法/模型/算法 |
| Material properties | 13 | 3 | 对象/模块/过渡章节 |
| Results and discussion | 13 | 2 | 结果/验证/讨论 |
| Thermal expansion of UD composite | 13 | 3 | 对象/模块/过渡章节 |
| Thermal expansion behaviors | 13 | 4 | 对象/模块/过渡章节 |
| Effective CTE and validation of numerical models | 13 | 4 | 方法/模型/算法 |
| Thermal expansion of plain woven composite | 13 | 3 | 对象/模块/过渡章节 |
| Thermal expansion behaviors | 13 | 4 | 对象/模块/过渡章节 |
| Effective CTE and validation of boundary conditions | 14 | 4 | 结果/验证/讨论 |
| Thermal expansion of satin woven composite | 14 | 3 | 对象/模块/过渡章节 |
| Thermal expansion behaviors | 14 | 4 | 对象/模块/过渡章节 |
| Effective CTE and validation of boundary conditions | 15 | 4 | 结果/验证/讨论 |
| Normal displacement on boundary planes | 15 | 3 | 对象/模块/过渡章节 |
| Conclusions | 17 | 2 | 结论/贡献回收 |
| Acknowledgment | 18 | 2 | 尾部材料 |
| References | 18 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是“应用压力-方法选择-已有工作-缺口-本文做什么”。作者先用高温飞行器温升和热失配制造现实压力，再用 RVE/FE/解析方法比较引出 unit cell 的必要性。

理论段落的节奏是“定义结构-设定对称节点-写出关系式-数值场验证-推广到边界条件”。这种写法适合复杂公式论文，因为每个公式都有几何图和验证图跟随，读者不会被抽象符号直接推走。

结果段落的节奏是“图示位移场-指出一致性-给出表格有效性质-解释偏差/均匀性”。强 claim 往往紧跟表格和图像，语气较稳，不大量使用夸张词。

结论段落采用编号式收束，先总结方法价值，再限定适用范围，最后给出边界位移规律。这种顺序避免了只说“方法有效”，而是把“何时有效、为什么有效、哪些边界表现不同”说清楚。

## 13. 文笔画像与语言习惯

整体语气是工程方法论文常见的克制型 assertive：作者经常使用 “can be”“should be”“is derived based on”“is validated by” 等表达，强调规则和约束，而不是夸大性能提升。

高频名词集中在 unit cell、boundary conditions、thermal expansion、displacement fields、symmetric structures、plain/satin woven composite。词频服务于贡献焦点，没有明显偏离主题。

句法上被动语态很多，例如 “unit cells are formulated”“boundary conditions are derived”“models are validated”。这是为了突出方法流程和客观规则，而不是突出研究者动作。主动语态主要出现在 “we can have”“we know”等推导说明中，用来带读者走公式。

时态上，Introduction 用一般现在时描述领域事实，方法推导用一般现在时，数值结果用一般过去时或现在时混合，结论回到一般现在时。情态动词 `should` 很关键，用于强调建模规范；`can` 则用于表达方法能力和适用性。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：30373
- 高频词：thermal(63)；unit(58)；uniform(42)；temperature(37)；expansion(36)；displacement(36)；cell(33)；composites(32)；symmetric(31)；composite(29)；symmetries(26)；relative(26)；boundary(25)；woven(25)；bcs(25)；cells(24)；structure(23)；method(23)；boundaries(22)；normal(22)
- 高频名词化/学术名词：temperature(37)；expansion(36)；displacement(36)；structure(23)；distribution(15)；deformation(10)；reflection(9)；rotation(8)；reference(8)；derivation(6)；direction(6)；application(4)；formulation(4)；homogenization(4)；conduction(4)
- 高频学术动词：derived(10)；developed(4)；derive(4)；compared(2)；indicated(2)；predict(2)；analyzed(1)；predicted(1)；validated(1)；propose(1)；develop(1)；enable(1)；validate(1)；revealed(1)
- 高频形容词：thermal(63)；displacement(36)；symmetric(31)；relative(26)；boundary(25)；normal(22)；reflectional(18)；effective(17)；rotational(16)；periodic(15)；macroscopic(14)；different(13)；translational(13)；numerical(12)；mechanical(11)
- 高频副词：widely(2)；carefully(2)；mainly(2)；efficiently(2)；fully(2)；frequently(1)；primarily(1)；entirely(1)；functionally(1)；completely(1)；similarly(1)；unfortunately(1)；totally(1)；easily(1)；separately(1)
- 高频二词短语：thermal expansion(36)；unit cell(33)；unit cells(24)；normal displacement(16)；uniform temperature(14)；boundary planes(14)；satin woven(13)；symmetric structures(12)；plain woven(10)；woven composite(10)；displacement distribution(10)；uniform normal(10)
- 高频三词短语：thermal expansion behaviors(9)；uniform normal displacement(8)；unit cell model(6)；reflectional rotational symmetric(6)；reflection plane rotation(6)；plane rotation axis(6)；displacement distribution rules(6)；thermal expansion coefficient(5)；translational reflectional rotational(5)；rotational symmetric structures(5)；satin woven composites(5)；composite thermal expansion(5)
- 被动语态估计：122；`we + 动作动词` 主动句估计：0
- 一般现在时线索：161；一般过去时线索：229；现在完成时线索：0；情态动词线索：78

分章节正文词频：

- Introduction: unit(24)；thermal(20)；method(20)；cell(20)；composites(17)；composite(13)；symmetries(12)；structure(10)
- Mathematical formulation: temperature(29)；thermal(26)；symmetric(18)；uniform(16)；bcs(15)；relative(15)；macroscopic(13)；expansion(13)
- Results and discussion: uniform(20)；normal(19)；boundary(18)；displacement(16)；boundaries(15)；planes(14)；woven(11)；thermal(10)
- Conclusions: unit(11)；thermal(7)；formulated(7)；cells(6)；expansion(5)；composites(5)；displacement(5)；woven(5)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：unit cell, boundary condition, displacement field, thermal expansion coefficient, symmetric structure, translational symmetry, reflectional symmetry, 180° rotational symmetry, uniform temperature loading。

常用问题句式：

- “However, for a unit cell, we need additional constraint BCs except for the macroscopic loading.”
- “This leaves some room for us to...”
- “It should be pointed out that...”

可复用 gap 表达：

- 已有方法完成了 A，但尚未澄清 B 的 general rules and concepts。
- 模型几何可代表原结构，但边界条件才赋予模型 physical meanings。
- Inappropriate boundary conditions may lead to approximate accurate results, but the physical mechanism is wrong.

可复用贡献表达：

- “A general approach is developed for...”
- “The application scope of the present method is clarified from ... point of view.”
- “The numerical models are validated by identical results obtained from unit cells of different sizes.”

结果句式可模仿为：“As shown in the table, the maximum deviation is only X, which validates the derived boundary conditions.” 这个句型适合把表格偏差直接连接到方法有效性。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Therefore, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
  可迁移模板：Therefore, a unit cell model has two essential elements, the identification of structure symmetries and the derivation of accurate BCs.
- 原句：Boundary conditions are the relations between the micro unit cell model and the macro real composite (essential conditions of homogenization).
  可迁移模板：Boundary conditions are the relations between the micro unit cell model and the macro real composite (essential conditions of homogenization).
#### Gap/转折句
- 原句：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell.
  可迁移模板：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell.
- 原句：However, if the reflectional and rotational symmetries are involved, the BC would be more complex and its implementation would raise some particular requirement of mesh generations.
  可迁移模板：However, if the reflectional and rotational symmetries are involved, the METHOD would be more complex and its implementation would raise some particular requirement of mesh generations.
#### 方法提出句
- 原句：In this paper, a general approach is developed for the establishment of such a unit cell model.
  可迁移模板：In this paper, a general approach is developed for the establishment of such a unit cell model.
- 原句：The application scope of present unit cell method is clarified from the thermal and mechanical point of views.
  可迁移模板：The application scope of present unit cell method is clarified from the thermal and mechanical point of views.
- 原句：The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
  可迁移模板：The influence of structure symmetries on the deformation pattern of unit cell models is clarified.
- 原句：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
  可迁移模板：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
- 原句：The approach developed in this paper can be applied to thermal expansion studies of any other composites with relevant structure symmetries.
  可迁移模板：The approach developed in this paper can be applied to thermal expansion studies of any other composites with relevant structure symmetries.
#### 结果呈现句
- 原句：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
  可迁移模板：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
- 原句：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
  可迁移模板：The numerical models are validated by the identical results obtained from unit cells of different sizes and also by the results available in literatures.
- 原句：The results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the FE method is more capable in capturing details like the local physical fields.
  可迁移模板：The results of Ref. [X] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the METHOD method is more capable in capturing details like the local physical fields.
#### 贡献/增量句
- 原句：In this paper, a general approach is developed for the establishment of such a unit cell model.
  可迁移模板：In this paper, a general approach is developed for the establishment of such a unit cell model.
- 原句：In this paper, a general approach is developed for the establishment of such a unit cell model.
  可迁移模板：In this paper, a general approach is developed for the establishment of such a unit cell model.
- 原句：Li and his team also contribute a lot of extraordinary works on the unit cell method for mechanical studies of various textile reinforced composite [24,25].
  可迁移模板：Li and his team also contribute a lot of extraordinary works on the unit cell method for mechanical studies of various textile reinforced composite [X,X].
#### 限制/边界句
- 原句：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell.
  可迁移模板：Thermal expansion properties of textile reinforced composites with certain structure symmetries can be efficiently calculated by a size-limited unit cell.
- 原句：The temperature of certain location in highspeed aerospace vehicles may increase from room temperature to above 1000 °C in a short time of 600 s [1].
  可迁移模板：The temperature of certain location in highspeed aerospace vehicles may increase from room temperature to above X°C in a short time of Xs [X].
- 原句：Under this condition, the thermal expansion behaviors of relevant composites and structures should be carefully considered, since the mismatch of thermal expansion coefficient between different phases may lead to damages of the composite, and that between different composites may lead to final failures of the structure.
  可迁移模板：Under this condition, the thermal expansion behaviors of relevant composites and structures should be carefully considered, since the mismatch of thermal expansion coefficient between different phases may lead to damages of the composite, and that between different composites may lead to final failures of the structure.
- 原句：Before its application, the corresponding behaviors and effective properties should be well understood primarily.
  可迁移模板：Before its application, the corresponding behaviors and effective properties should be well understood primarily.
- 原句：The results of Ref. [3] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the FE method is more capable in capturing details like the local physical fields.
  可迁移模板：The results of Ref. [X] show that the Mori-Tanaka method is more efficient, whereas has some limitations such as the inclusions should have ellipsoidal shapes of low aspect ratios; the strong contrast method has good performance for spherical inclusions; while the METHOD method is more capable in capturing details like the local physical fields.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略分三类：背景引用、方法谱系引用、验证引用。背景引用用于说明高温飞行器和复合材料热环境；方法谱系引用用于比较解析方法、FE/RVE、Mori-Tanaka、织物复合材料单胞；验证引用用于与已有 plain woven、satin woven、编织复合材料结果对照。

作者对前人总体采取“继承+补充”姿态，很少直接批判。常见写法是：已有研究已经做了 homogenization 和 unit cell，但多基于 translational symmetries only，因此仍有空间利用更多结构对称性。这个姿态减少了与前人冲突，同时给自己留下明确贡献空间。

gap 与引用的连接方式是“先承认已有研究丰富，再指出其共同默认”。这种写法比单独说 “few studies” 更有说服力，因为它不是说领域没人做，而是说大家做了相近的事但漏掉了一个共性问题。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：63
- Introduction 引文簇数量估计：11
- References 条目数：44
- 可识别年份条目数：43
- 2021 年及以后文献数：0
- 2010 年前经典文献数：17
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Composite Structures(1)
- 引文簇样例：[2], [3], [1], [3], [3], [4], [23], [24,25], [26], [27], [28], [22]

带引文的 gap/转折句样例：

- According to Ref. [3], excluding the larger computational cost, another disadvantage of FE method is its dependency on the size of RVE.

References 解析样例（前 8 条）：

- 1. For a composite with symmetric structures, the effective coefficient of thermal expansion can be efficiently calculated by a unit cell model. Such unit cell should be formulated based on structure symmetries, and relevant BCs can be derived based on displacement distribution rules summarized in this work. Such unit cell models can also be used to predict the local stress distributions in fiber yarns or textile reinforced composites and thus has potentials for damage analysis of these composites.
- 2. The boundary conditions of unit cells are derived based on the assumption of uniform macro strain field, which can be resulted in by a uniform temperature loading. Thus, the current unit cell method can only be used to simulate thermal expansion behaviors under a uniform temperature loading, such as the thermal residual stresses after a specific heat treating.
- 3. For boundaries that can be formulated by reflectional symmetries, the uniform normal displacement and the uniform deformation can be obtained in thermal expansion calculations; for boundaries that can only be formulated based on translational or rotational symmetries, the normal displacement and the relevant deformation are non-uniform.
Acknowledgment
This study is supported by the Fundamental Research Funds for the Central Universities (3102017OQD068).
UC P1 P2 P3 P4 P5 P6
References
- [1] Chen X, Liu L, Yue Z. Coupled analysis of aerodynamic heating, radiative heat transfer and heat conduction for hypersonic vehicles. 20th AIAA International Space Planes and Hypersonic Systems and Technologies Conference. American Institute of Aeronautics and Astronautics; 2015.
- [2] Gommers B, Verpoest I, Van Houtte P. The Mori-Tanaka method applied to textile composite materials. Acta Mater 1998;46(6):2223–35.
- [3] Mortazavi B, Baniassadi M, Bardon J, Ahzi S. Modeling of two-phase random composite materials by finite element, Mori-Tanaka and strong contrast methods. Compos B Eng 2013;45(1):1117–25.
- [4] Yang B. A distributed transfer function method for heat conduction problems in multilayer composites. Numer Heat Transf, Part B: Fundam 2008;54(4):314–37.
- [5] Li DS, Fang DN, Jiang N, Yao XF. Finite element modeling of mechanical properties of 3D five-directional rectangular braided composites. Compos Part B: Eng 2011;42(6):1373–85.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 适用边界风险：方法基于 uniform temperature loading 和 uniform macro strain field，若用于强温度梯度、局部热冲击或非均匀热载荷，边界条件可能不成立。
2. 几何理想化风险：UD、plain woven、satin woven 都采用理想周期结构，真实织物中的纱线波动、孔隙、偏心和制造缺陷会破坏对称性。
3. 外部验证不足：主要验证来自不同 UC 结果一致和文献数值/实验对比，缺少针对本文模型的独立热膨胀实验。
4. 材料模型简化：示例材料参数较简单，未考虑温度依赖、各向异性非线性、界面脱粘或损伤演化。
5. 局部应力 claim 风险：结论提到可用于损伤分析，但正文并未系统开展损伤准则验证。
6. 图像复核风险：normal displacement 均匀/非均匀判断高度依赖位移云图尺度，需 PDF 图像复核。

## 17. 可复用资产

- 选题资产：从“常用方法的隐性边界条件错误”切入，而不是从新材料/新算法切入。
- 论证资产：几何代表性与物理边界代表性分开讨论，适合所有多尺度单胞论文。
- 方法资产：先在基本对称结构中推导规则，再在复杂真实结构中应用规则。
- 验证资产：用多尺寸单胞的一致结果作为边界条件正确性的证据。
- 图表资产：对称结构示意图、单胞缩小路径图、边界编号图、位移云图、有效参数对比表、边界均匀性汇总表。
- 写作资产：在结论中不仅说“方法有效”，还明确适用范围和不可越界条件。

## 18. 对我写论文的启发

如果我要写类似方法论文，最值得学习的是“先澄清概念，再展示算例”。本文没有一开始堆复杂织物模型，而是先把三类对称结构的节点关系讲清楚，让读者接受方法的逻辑地基。

第二个启发是：方法论文可以把“常见但不严谨的工程操作”作为 gap。只要能说明这个操作会影响物理机制或局部场，即使结果误差有时不大，也足以成为论文贡献。

第三个启发是：验证不一定只靠实验，也可以靠等价模型之间的一致性。但这种验证要谨慎写，最好配合适用范围声明，避免被审稿人认为只是“自己证明自己”。

## 19. 最终浓缩

这篇论文最值得学习的是它把 unit cell 方法拆成“结构对称性识别”和“边界条件推导”两个不可替代的环节，并用 UD、plain woven、satin woven 三类材料证明：只有当位移边界条件严格对应对称性时，缩小单胞才真正代表原结构。

最大风险是方法边界较窄：它服务于均匀温度变化下的热膨胀问题，不应直接推广到任意热梯度和真实缺陷织物。

可迁移到自己论文中的三件事：第一，把“几何模型”和“物理约束”分开写；第二，用简单原型结构推导规则，再用复杂对象验证；第三，在结论中主动写清楚适用范围，让贡献更可信。
