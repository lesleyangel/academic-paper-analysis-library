# High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks

## 0. 读取说明

本拆解基于 `801/文本/txt/High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.txt` 的全文抽取。抽取文本包含公式、表格数值、图题和结论，但部分双栏文本顺序混杂；本拆解以可确认的正文叙述为准。压力云图、模态形状和误差分布的视觉细节标注“需要 PDF 图像复核”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Dual modal space model, 3 DMS-LSTM surrogate modeling, 4 Test case, 5 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：High-fidelity modeling of unsteady aerodynamic loads under structural vibration using dual modal spaces and LSTM networks。
- 作者：Xuanhe Ding、Chunlin Gong、Hua Su、Chunna Li、Wei Li、Xuyi Jia。
- 期刊：Aerospace Science and Technology，176，2026，111927。
- 领域：非定常气动载荷建模、降阶模型、气动弹性、深度学习代理模型。
- 论文类型：方法提出 + 数值验证。
- 研究对象：结构振动诱导的高维非定常气动载荷分布。
- 主要方法：结构模态空间 + 气动 POD 模态空间耦合成 Dual Modal Space (DMS)，以 generalized aerodynamic forces 为中间变量，再用 LSTM 预测时序演化，并通过显式映射重构气动载荷。
- 对比基线：POD-LSTM、DMS-OpInf、POD-OpInf；三维翼算例中主要对比 DMS-LSTM 与 POD-LSTM。
- 核心指标：POD 系数 RMSE/NSE、升力系数 RMSE/NSE、表面压力系数重构误差、全局重构精度。

## 2. 摘要与核心信息提取

一句话主张：传统 POD-ROM 在结构振动条件下会遭遇模态混叠和高阶系数高频振荡，DMS 通过把气动载荷投影到结构模态空间，构造具有物理含义且更平滑的 generalized aerodynamic forces，从而让 LSTM 更准确、稳定地预测非定常气动载荷分布。

摘要的信息层次很完整：重要性是 aircraft performance evaluation and safety assurance；旧方法不足是 POD 系数难以从结构变形映射、模态混叠、高阶系数高频振荡；方法是 DMS + LSTM；机制解释是空间积分滤除与结构响应弱相关的小尺度高频流动结构；证据是二维 NACA65A004 和三维 AGARD445.6 翼，精度超过 97.2%，压力分布误差约降低 50%，升力误差在三维翼中最高改善约 80.7%。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/High-fidelity-modeling-of-unsteady-aerodynamic-loads-und_2026_Aerospace-Scie.md`。

中文译文：

> 快速准确地预测结构振动引起的气动载荷分布对于飞机性能评估和安全保证至关重要。然而，对于这种强非定常流动预测问题，现有的基于适当正交分解（POD）的降阶模型（ROM）面临着重大挑战，包括由于模态混合现象而难以将物理输入（例如结构变形）映射到模态系数，以及由于高阶模态系数的高频振荡引起的代理建模中的收敛问题。本研究提出了一种双模态空间（DMS）模型，将结构模态和气动 POD 模态整合到统一的降维低维空间中，建立高维气动载荷场和低维广义气动力之间的映射。由于广义空气动力保留了明确的物理属性，并且是通过投影到结构模式上获得的，因此空间积分过滤掉了与结构响应相关性较差的小尺度、高频流动结构。结果，避免了模态混合现象，并且抑制了高阶气动 POD 系数中存在的高频振荡。
>
> 将 DMS 与长短期记忆 (LSTM) 神经网络相结合，产生一个有效的代理模型，用于预测结构振动下的广义空气动力。使用 DMS 中创建的双模态映射矩阵，可以根据预测的广义气动力精确重建气动载荷分布。亚音速条件下的数值验证表明，DMS-LSTM对气动载荷分布的预测精度保持在97.2%以上。与传统的 POD-LSTM 模型相比，2D NACA65A004 翼型的预测误差减少了 50.762%，3D AGARD445.6 机翼的预测误差减少了 50.134%。所提出的模型有效地缓解了传统POD-ROM在结构振动条件下的精度限制，并且有可能在测试的参数范围内促进亚音速范围内规定结构运动的开环非定常气动载荷预测。通常用于高精度地解决此类流固耦合问题。然而，它们的计算成本仍然非常高，特别是对于涉及动态变形几何形状的长时间不稳定模拟。
>
> 这种限制限制了它们在迭代设计过程和时间关键的预测场景中的适用性，从而促进了平衡效率和准确性的降阶模型（ROM）的开发。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来自航空结构轻量化和柔性化带来的强非定常气动问题。高保真 CFD 虽准，但长时间、变形边界模拟成本过高；数据驱动 ROM 可提速，却在结构振动场景下因为输入/输出物理空间不匹配而失稳。

作者没有把问题泛化成“深度学习预测气动载荷”，而是聚焦到一个更尖锐的建模矛盾：POD 模态是按气动能量排序的，结构振动输入却在结构模态空间中表达，两者直接映射会出现 modal mixing。这个问题定义很有效，因为它让 DMS 的必要性不是“换一种神经网络”，而是“换一个低维状态变量”。

选题价值在于：它同时面向工程效率、物理可解释性和模型泛化稳定性。对 AST 读者来说，单纯 LSTM 不够新，但“结构模态对齐的气动载荷降阶表示”更贴近气动弹性建模传统。

## 4. 领域位置与文献版图

文献版图分为四组。第一组是高保真 CFD 和气动弹性背景，用于说明准确预测载荷的重要性和成本瓶颈。第二组是黑箱数据驱动模型，如深度网络、operator learning，它们灵活但数据需求高、解释性弱。第三组是灰箱 ROM，尤其 POD-LSTM，它有能量最优基础但在结构振动条件下暴露 modal mixing。第四组是 SPOD、DMD、Koopman、physics-informed learning 等扩展方向，作者承认它们提供互补视角，但指出与结构对齐气动表示的结合仍是 open challenge。

本文站位是“不是发明更复杂的 surrogate，而是重构 surrogate 的状态空间”。这使得 DMS-LSTM 与普通 POD-LSTM 的差异更像物理表示差异，而非网络调参差异。

## 5. Gap 制造机制

Gap 的制造有两层。显性 gap：现有 POD-LSTM 在结构振动诱导的非定常气动载荷预测中困难显著，包括结构变形到 POD 系数映射困难、高阶系数高频振荡导致 surrogate 收敛和泛化问题。隐性 gap：许多数据驱动模型追求 latent complexity，但没有解决结构动力学与气动载荷之间的物理一致性。

作者用 generalized aerodynamic forces 填补 gap：它们由 CFD 载荷投影到结构模态基得到，每个力都对应特定结构振型贡献，因此比 POD 系数更有物理意义、更平滑，也更适合作为学习目标。

Gap 的可信度较强，因为后文不只说 POD 不好，而是在二维和三维算例中显示高阶 POD 系数的误差与频谱失真，并用 DMS 在不同 surrogate（LSTM 和 OpInf）中均改善来证明主要收益来自空间构造。

## 6. 创新性判断

作者声明的创新是 DMS 模型、DMS-LSTM 框架、generalized aerodynamic forces 中间表示、显式双向映射 Q-a-F，以及二维/三维验证。

真实创新属于“表示层创新 + 工程验证”。LSTM、POD、结构模态投影都不是新概念；新意在于把结构模态空间和气动 POD 空间通过 dual modal mapping matrix H 连接，使低维变量既能学习又能重构。这类创新的强度取决于是否能证明 DMS 比 POD 的优势来自物理空间对齐，而不是算例偶然性。论文通过 DMS-OpInf 的辅助对比增强了这一点。

容易被挑战的地方：DMS 要求结构模态数与 POD 模态数匹配，并依赖 H 的可逆/条件数；目前限于线性结构模态、开放环 prescribed structural motions、亚声速测试参数范围。

## 7. 论证链条复原

1. 柔性航空结构导致结构振动与气动载荷强耦合，高维非定常载荷需要快速准确预测。
2. CFD 成本高，POD-LSTM 等 ROM 是合理方向。
3. 但 POD 系数是气动能量模态，结构输入是结构模态，两者直接学习会 modal mixing，且高阶 POD 系数高频振荡难学。
4. 因此需要一个与结构动力学一致的低维气动表示。
5. generalized aerodynamic forces 由气动载荷投影到结构模态得到，保留物理含义，并滤除弱相关小尺度高频结构。
6. DMS 构造 H=Phi_A^T Phi_p，实现 Q 与 POD 系数 a 的显式映射，再由 a 重构载荷 F。
7. LSTM 学 q 和历史 Q 到当前 Q 的时序映射，降低直接预测高维 F 或高频 a 的难度。
8. 二维、复杂激励、三维算例均显示 DMS-LSTM 在 RMSE/NSE、升力和压力分布重构上优于 POD-LSTM。
9. 结论收束为：DMS 提升主要来自模态空间构造，并为后续非线性结构/闭环气动弹性扩展铺路。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Accurate and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [3,4].
- 已有研究不足/GAP：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries. However, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads.
- 本文解决方式：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients. This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces. As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed.
- 学术或工程增量：Lightweight and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [1,2]. As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations presen This paper presents a DMS-LSTM reduced-order modeling frame work for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency. By projecting aerodynamic loads onto the structural modal space, the formulation effectively miti gates modal mixing and provides a reduced representation that is well aligned with structural dynamics.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

DMS 的输入是结构模态矩阵 Phi_s、映射到气动网格的结构模态 Phi_A、CFD 载荷快照 F、POD 气动模态 Phi_p。结构方程 M Xddot + C Xdot + KX = F 投影到结构模态，得到 generalized coordinate q 和 generalized aerodynamic force Q=Phi_s^T F；在气动网格上则用 Phi_A 表示结构模态。

气动 POD 对载荷快照去均值后构造协方差，保留 r 个主模态，得到 F(t)=Phi_p a(t)+F_bar。DMS 核心是把 Q 与 a 联系起来：Q-Q0=H a，其中 H=Phi_A^T Phi_p，Q0=Phi_A^T F_bar。预测时先由 LSTM 得到 Q，再 a=H^{-1}(Q-Q0)，最后 F=Phi_p a+F_bar。

LSTM 数据组织采用滑动窗口。输入包含过去和当前 generalized displacement q，以及过去 generalized aerodynamic forces Q；输出为当前 Q。二维 case 使用两层 64 hidden units，三维 case 使用两层 128 hidden units，窗口长度 W=2，Adam 学习率 0.001，RMSE loss。

验证设计有三层：二维 NACA65A004 常规多频激励，对比 DMS-LSTM/POD-LSTM/DMS-OpInf/POD-OpInf；二维复杂激励同时改变 Mach、攻角和宽带结构模态；三维 AGARD445.6 翼用 40 模态验证真实复杂度下的性能。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| POD-LSTM 在结构振动下的主要困难是 modal mixing 和高阶系数高频振荡 | Introduction/4.1/4.2 | Fig. 10、Fig. 35 中 POD 系数非线性增强，Fig. 11/36 高阶误差增大 | 强 | 高频结构视觉与频谱需 PDF 图像复核 |
| generalized aerodynamic forces 更平滑、更适合作为学习变量 | Section 2/4.1/4.2 | 投影定义 Q=Phi_A^T F，结果段称 DMS 空间线性可分性更好 | 中强 | 平滑性主要由图和定性描述支撑 |
| DMS-LSTM 在二维基准算例中优于 POD-LSTM | 4.1.2 | Table 2：升力 RMSE 1.844e-4 vs 4.151e-4，NSE 6.082e-3 vs 1.612e-2 | 强 | 训练随机性需多次运行统计，文中有 box plot |
| DMS 优势不是 LSTM 独有，而来自模态空间构造 | 4.1.2 | DMS-OpInf 也优于 POD-OpInf；作者明确比较两类 surrogate | 强 | OpInf 设置和正则化参数可能影响公平性 |
| 复杂激励下 DMS-LSTM 仍更稳 | 4.1.3 | Table 4：DMS-LSTM RMSE 4.87e-3，POD-LSTM 1.06e-2；box plot 离散度更小 | 强 | 仍是 interpolation within tested range |
| 三维翼中 DMS-LSTM 优势更明显 | 4.2 | Table 5：升力 RMSE 2.935e-5 vs 1.519e-4，误差降低 80.678% | 强 | 只对比 LSTM，未含 OpInf |
| DMS-LSTM 维持超过 97.2% 的全局重构精度 | Abstract/4.2 | 三维表面压力 RMSE 平均 1.485e-3，约低于 POD-LSTM 50.134% | 中强 | “global accuracy”具体定义需 PDF/公式复核 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核备注 |
| --- | --- | --- | --- | --- |
| Fig. 1 | DMS 概念图 | 结构模态与气动 POD 可统一 | 给读者先验框架 | 需要 PDF 图像复核 |
| Eq. 1-5 | 结构模态空间和 generalized force 定义 | Q 有明确物理意义 | X=Phi_s q，Q=Phi_s^T F | 文本可确认 |
| Eq. 6-14 | POD 气动模态空间 | 传统气动降阶表示 | F=Phi_p a+F_bar | 文本可确认 |
| Eq. 15-18 | DMS 双向映射核心 | Q-a-F 可显式重构 | H=Phi_A^T Phi_p，a=H^-1(Q-Q0) | 文本可确认 |
| Fig. 3-4 | DMS-LSTM 训练和预测流程 | 模型闭环完整 | 数据生成、降维、LSTM、重构 | 需要 PDF 图像复核 |
| Fig. 10/35 | 对比 POD 系数与 generalized forces | DMS 表示更易学习 | 高阶 POD 非线性更明显 | 需要 PDF 图像复核 |
| Fig. 11-18 | 二维基准结果 | DMS-LSTM 减少模态和载荷误差 | 升力、压力分布双指标支持 | 需要 PDF 图像复核 |
| Fig. 19-28 | 复杂激励结果 | 非定常气动条件下仍稳定 | Mach/攻角/宽带结构输入同时变化 | 需要 PDF 图像复核 |
| Fig. 29-41 | 三维 AGARD 翼验证 | 复杂三维流中优势放大 | 高阶模式和压力重构改善 | 需要 PDF 图像复核 |
| Table 2-6 | 量化证据 | 误差降低百分比 | 50%+ 压力误差降低，三维升力 80.678% 改善 | 文本可确认 |

## 11. 章节结构与篇章布局

章节为：Introduction -> Dual modal space model -> DMS-LSTM surrogate modeling -> Test case -> Conclusion。结构是典型方法论文：先解释旧方法失效点，再建数学框架，再给学习流程，最后多算例验证。

Introduction 的说服节奏很清楚：航空轻量化背景 -> CFD 成本瓶颈 -> ROM 分类 -> POD-LSTM 局限 -> generalized forces/DMS 方案。Section 2 负责让读者相信 DMS 是物理上闭合的；Section 3 负责让读者相信 DMS 可被神经网络使用；Section 4 用层层加难的算例证明从二维到三维都有效。

标题偏方法型和算例型，如 “Dual modal space model”、“DMS-LSTM surrogate modeling”、“Case A/B”。小节标题不花哨，但变量暴露充分。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Dual modal space model（方法/模型/算法）
  - L3 p.3: 2.1 Structural modal space（对象/模块/过渡章节）
  - L3 p.3: 2.2 Aerodynamic modal space via POD（对象/模块/过渡章节）
  - L3 p.4: 2.3 DMS by integrating structural and aerodynamic modes（对象/模块/过渡章节）
- L2 p.4: 3 DMS-LSTM surrogate modeling（方法/模型/算法）
- L2 p.7: 4 Test case（结果/验证/讨论）
  - L3 p.9: 4.1 Case A: Two-dimensional airfoils（结果/验证/讨论）
    - L4 p.9: 4.1.1 Case setup（结果/验证/讨论）
    - L4 p.10: 4.1.2 Result and discussion（结果/验证/讨论）
    - L4 p.14: 4.1.3 Further analysis with complex excitation conditions（对象/模块/过渡章节）
  - L3 p.17: 4.2 Case B: Three-dimensional wing（结果/验证/讨论）
    - L4 p.17: 4.2.1 Case setup（结果/验证/讨论）
    - L4 p.17: 4.2.2 Result and discussion（结果/验证/讨论）
- L2 p.19: 5 Conclusion（结论/贡献回收）
- L2 p.19: CRediT authorship contribution statement（尾部材料）
- L2 p.19: Declaration of competing interest（尾部材料）
- L2 p.19: Acknowledgements（尾部材料）
- L2 p.19: Data availability（尾部材料）
- L2 p.19: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Dual modal space model | 3 | 2 | 方法/模型/算法 |
| 2.1 Structural modal space | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Aerodynamic modal space via POD | 3 | 3 | 对象/模块/过渡章节 |
| 2.3 DMS by integrating structural and aerodynamic modes | 4 | 3 | 对象/模块/过渡章节 |
| 3 DMS-LSTM surrogate modeling | 4 | 2 | 方法/模型/算法 |
| 4 Test case | 7 | 2 | 结果/验证/讨论 |
| 4.1 Case A: Two-dimensional airfoils | 9 | 3 | 结果/验证/讨论 |
| 4.1.1 Case setup | 9 | 4 | 结果/验证/讨论 |
| 4.1.2 Result and discussion | 10 | 4 | 结果/验证/讨论 |
| 4.1.3 Further analysis with complex excitation conditions | 14 | 4 | 对象/模块/过渡章节 |
| 4.2 Case B: Three-dimensional wing | 17 | 3 | 结果/验证/讨论 |
| 4.2.1 Case setup | 17 | 4 | 结果/验证/讨论 |
| 4.2.2 Result and discussion | 17 | 4 | 结果/验证/讨论 |
| 5 Conclusion | 19 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 19 | 2 | 尾部材料 |
| Declaration of competing interest | 19 | 2 | 尾部材料 |
| Acknowledgements | 19 | 2 | 尾部材料 |
| Data availability | 19 | 2 | 尾部材料 |
| References | 19 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

方法段落多采用“定义变量 -> 写公式 -> 解释物理意义 -> 指出计算优势”的节奏。结果段落常用“先分析 POD 现象 -> 再解释 DMS 优势 -> 最后给误差表”。

作者特别重视“隔离变量”的叙事：通过 DMS-OpInf vs POD-OpInf 说明不是 LSTM 技巧导致提升；通过复杂激励说明不是简单周期输入下偶然有效；通过三维翼说明高非线性场景中优势更明显。

结论段落非常标准：第一段概括框架，第二段概括 DMS 物理映射，第三段概括数值提升，第四段承认线性模态和开放环限制。

## 13. 文笔画像与语言习惯

文风是工程方法论文的“稳态推进”：术语密度高，句子偏长，名词化强。高频名词包括 generalized aerodynamic forces、modal coefficients、structural modes、POD modes、unsteady aerodynamic load distribution、surrogate model、reconstruction accuracy。

作者常用强解释动词：mitigate、suppress、retain、establish、reconstruct、outperform、facilitate、align。谨慎限定词包括 within the tested parametric range、open-loop、prescribed structural motions、subsonic conditions。这些限定词在摘要和结论中重复出现，用于防止模型泛化 claim 过强。

被动语态用于方法定义，如 “is computed as”、“is reconstructed using”；主动语态用于贡献表达，如 “the proposed model effectively mitigates”。时态上方法用现在时，算例结果用现在时/过去时混合，结论用现在时。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：48585
- 高频词：aerodynamic(118)；structural(87)；modal(82)；pod(55)；generalized(51)；modes(49)；model(44)；load(43)；unsteady(39)；modeling(37)；distribution(35)；models(34)；prediction(30)；forces(29)；coefficients(28)；reduced-order(25)；space(25)；accuracy(25)；time(25)；dms(24)
- 高频名词化/学术名词：distribution(35)；prediction(30)；reconstruction(20)；vibration(19)；pressure(16)；excitation(15)；decomposition(11)；performance(10)；dynamics(10)；displacement(10)；deformation(10)；section(9)；formulation(9)；inference(8)；tion(7)
- 高频学术动词：predicted(12)；compared(9)；constructed(8)；evaluate(6)；evaluated(4)；demonstrate(4)；presented(4)；provide(3)；construct(3)；achieve(2)；demonstrated(1)；analyze(1)；indicated(1)；indicate(1)
- 高频形容词：aerodynamic(118)；structural(87)；modal(82)；physical(21)；coefficient(19)；dynamic(15)；temporal(14)；dominant(14)；dual(12)；three-dimensional(11)；numerical(10)；displacement(10)；two-dimensional(10)；computational(9)；spectral(7)
- 高频副词：significantly(10)；directly(6)；consistently(6)；effectively(5)；particularly(5)；separately(5)；approximately(5)；strongly(4)；widely(3)；commonly(3)；typically(3)；specifically(3)；inherently(3)；physically(3)；implicitly(3)
- 高频二词短语：aerodynamic load(37)；generalized aerodynamic(28)；load distribution(26)；aerodynamic forces(24)；unsteady aerodynamic(24)；structural modal(20)；modal space(16)；modal coefficients(15)；rmse nse(13)；dual modal(12)；structural modes(12)；pod modal(12)
- 高频三词短语：aerodynamic load distribution(23)；generalized aerodynamic forces(21)；unsteady aerodynamic load(14)；pod modal coefficients(10)；dual modal space(7)；generalized aerodynamic force(7)；dominant vibration modes(6)；structural modal matrix(5)；unsteady aerodynamic loads(5)；modes selected dominant(5)；selected dominant vibration(5)；aerodynamic load distributions(4)
- 被动语态估计：127；`we + 动作动词` 主动句估计：0
- 一般现在时线索：225；一般过去时线索：460；现在完成时线索：0；情态动词线索：15

分章节正文词频：

- 1 Introduction: aerodynamic(33)；structural(28)；modal(22)；pod(16)；unsteady(12)；forces(11)；generalized(11)；vibration(9)
- 2 Dual modal space model: aerodynamic(27)；structural(17)；modal(16)；pod(15)；modes(11)；force(10)；space(10)；load(10)
- 3 DMS-LSTM surrogate modeling: aerodynamic(19)；load(12)；generalized(12)；lstm(11)；structural(9)；model(8)；input(8)；distribution(7)
- 4 Test case: aerodynamic(31)；modal(31)；modes(31)；structural(27)；models(25)；time(21)；rmse(21)；modeling(20)
- 5 Conclusion: aerodynamic(8)；modal(7)；structural(6)；work(3)；unsteady(3)；load(3)；nonlinear(3)；dms-lstm(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- Gap 句式：Existing POD-based ROMs face significant challenges, including... 可复用为“列举式方法不足”。
- 方法定位句：This study proposes a DMS model that integrates X and Y into a unified reduced low-dimensional space.
- 物理解释句：Since Q retains explicit physical property..., the spatial integration filters out...
- 对比句：Compared to traditional POD-LSTM models, prediction errors were reduced by...
- 限定句：The present work focuses on open-loop prediction with prescribed structural vibrations...
- 机制归因句：The improvement mainly stems from the modal space construction rather than the specific surrogate modeling technique.
- 未来工作句：Future work will focus on extending the proposed framework to...

可复用短语：physically interpretable representation、bidirectional mapping、modal mixing phenomenon、high-frequency oscillations、surface pressure reconstruction、time-domain and frequency-domain metrics、global reconstruction accuracy。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Rapid and accurate prediction of aerodynamic load distribution induced by structural vibrations is critical for aircraft performance evaluation and safety assurance.
  可迁移模板：Rapid and accurate prediction of aerodynamic load distribution induced by structural vibrations is critical for aircraft performance evaluation and safety assurance.
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  可迁移模板：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (METHOD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
- 原句：This limitation restricts their applicability in iterative design processes and time-critical pre diction scenarios, motivating the development of reduced-order models (ROMs) that balance efficiency and accuracy.
  可迁移模板：This limitation restricts their applicability in iterative design processes and time-critical pre diction scenarios, motivating the development of reduced-order models (ROMs) that balance efficiency and accuracy.
- 原句：Accurate and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [3,4].
  可迁移模板：Accurate and efficient prediction of these unsteady aerodynamic load distributions is therefore essential for aeroelastic analysis, flight stability assessment, and multidisciplinary design optimization [X,X].
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  可迁移模板：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (METHOD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
#### Gap/转折句
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  可迁移模板：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (METHOD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
- 原句：Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
  可迁移模板：Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
- 原句：However, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads.
  可迁移模板：However, increased structural flexibility also leads to strong coupling between structural vibration and aerodynamic loads.
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  可迁移模板：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (METHOD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
- 原句：Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
  可迁移模板：Nevertheless, their computational cost remains prohibitively high, particularly for long-time unsteady simulations involving dynamically deforming geometries.
#### 方法提出句
- 原句：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (POD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
  可迁移模板：However, for this kind of strong unsteady flow prediction problems, existing proper orthogonal decomposition (METHOD) based reduced-order models (ROMs) face significant challenges, including difficulty in mapping physical inputs (e.g., structural deformations) to modal coefficients due to modal mixing phenomena, and convergence issues in surrogate modeling caused by high-frequency os cillations of higher-order modal coefficients.
- 原句：This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
  可迁移模板：This study proposes a Dual Modal Space (METHOD) model that in tegrates structural modes and aerodynamic METHOD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
- 原句：As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic POD coefficients are sup pressed.
  可迁移模板：As a result, the modal mixing phenomenon is avoided and the high-frequency oscillations present in higher-order aerodynamic METHOD coefficients are sup pressed.
- 原句：Combining DMS with Long Short-Term Memory (LSTM) neural networks yields an efficient surrogate model for predicting generalized aerodynamic forces under structural vibrations.
  可迁移模板：Combining METHOD with Long Short-Term Memory (METHOD) neural networks yields an efficient surrogate model for predicting generalized aerodynamic forces under structural vibrations.
- 原句：Compared to traditional POD-LSTM models, prediction errors were reduced by 50.762 % for a 2D NACA65A004 airfoil, and 50.134 % for a 3D AGARD445.6 wing.
  可迁移模板：Compared to traditional METHOD models, prediction errors were reduced by X for a METHOD NACA65A004 airfoil, and X for a METHOD AGARD445.Xwing.
#### 结果呈现句
- 原句：Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution.
  可迁移模板：Numerical validation under subsonic conditions shows that METHOD main tains over X prediction accuracy of aerodynamic load distribution.
- 原句：Numerical validation under subsonic conditions shows that DMS-LSTM main tains over 97.2 % prediction accuracy of aerodynamic load distribution.
  可迁移模板：Numerical validation under subsonic conditions shows that METHOD main tains over X prediction accuracy of aerodynamic load distribution.
- 原句：Although such POD–LSTM frameworks have shown promising performance in many unsteady flow problems, their limitations become particularly pronounced when structural vibration is involved.
  可迁移模板：Although such METHOD–METHOD frameworks have shown promising performance in many unsteady flow problems, their limitations become particularly pronounced when structural vibration is involved.
- 原句：The effectiveness of the proposed framework is demonstrated through twodimensional and three-dimensional benchmark cases.
  可迁移模板：The effectiveness of the proposed framework is demonstrated through twodimensional and three-dimensional benchmark cases.
- 原句：The remainder of this paper is organized as follows: Section 2 presents the DMS formulation, Section 3 introduces the DMS-LSTM modeling framework, Section 4 discusses numerical results, and Section 5 concludes the paper.
  可迁移模板：The remainder of this paper is organized as follows: Section Xpresents the METHOD formulation, Section Xintroduces the METHOD modeling framework, Section Xdiscusses numerical results, and Section Xconcludes the paper.
#### 贡献/增量句
- 原句：This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
  可迁移模板：This study proposes a Dual Modal Space (METHOD) model that in tegrates structural modes and aerodynamic METHOD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
- 原句：Lightweight and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [1,2].
  可迁移模板：Lightweight and flexible structures are widely used in modern aerospace vehicles to improve aerodynamic performance and structural efficiency [X,X].
- 原句：This study proposes a Dual Modal Space (DMS) model that in tegrates structural modes and aerodynamic POD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
  可迁移模板：This study proposes a Dual Modal Space (METHOD) model that in tegrates structural modes and aerodynamic METHOD modes into a unified reduced low-dimensional space, establishing mappings between high-dimensional aerodynamic load field and low-dimensional generalized aerodynamic forces.
- 原句：It is worth noting that other modal decomposition techniques, such as spectral POD (SPOD), dynamic mode decomposition (DMD), and phase-based POD, as well as recent developments in Koopman-based modeling and physics-informed machine learning, provide comple mentary perspectives on unsteady flow modeling [32–35].
  可迁移模板：It is worth noting that other modal decomposition techniques, such as spectral METHOD (METHOD), dynamic mode decomposition (METHOD), and phase-based METHOD, as well as recent developments in Koopman-based modeling and physics-informed machine learning, provide comple mentary perspectives on unsteady flow modeling [X–X].
- 原句：This paper presents a DMS-LSTM reduced-order modeling frame work for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency.
  可迁移模板：This paper presents a METHOD reduced-order modeling frame work for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency.
#### 限制/边界句
- 原句：The proposed model effectively mitigates the accuracy limitations of traditional POD-ROM under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic regime, within the tested parametric range. commonly employed to resolve such fluid–structure interaction prob lems with high accuracy.
  可迁移模板：the proposed METHOD under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic regime, within the tested parametric range. commonly employed to resolve such fluid–structure interaction prob lems with high accuracy.
- 原句：The proposed model effectively mitigates the accuracy limitations of traditional POD-ROM under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic regime, within the tested parametric range. commonly employed to resolve such fluid–structure interaction prob lems with high accuracy.
  可迁移模板：the proposed METHOD under structural vibration conditions, and has potential to facilitate open-loop unsteady aerodynamic load prediction for prescribed structural motions in the subsonic regime, within the tested parametric range. commonly employed to resolve such fluid–structure interaction prob lems with high accuracy.
- 原句：In contrast, gray-box ROMs embed physical knowledge into the modeling process, most commonly through modal decomposition.
  可迁移模板：In contrast, gray-box ROMs embed physical knowledge into the modeling process, most commonly through modal decomposition.
- 原句：The present study is limited to linear structural modal representa tions and open-loop aerodynamic load prediction driven by prescribed structural motions.
  可迁移模板：The present study is limited to linear structural modal representa tions and open-loop aerodynamic load prediction driven by prescribed structural motions.
- 原句：Future work will focus on extending the proposed frame work to nonlinear structural dynamics and fully coupled aeroelastic simulations, as well as incorporating adaptive modal representations X.
  可迁移模板：Future work will focus on extending the proposed frame work to nonlinear structural dynamics and fully coupled aeroelastic simulations, as well as incorporating adaptive modal representations X.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用按功能分布：前几篇用于轻量化/气动弹性背景；CFD 和 ROM 文献用于说明效率瓶颈；POD-LSTM 文献用于建立主流基线；Taira、Berkooz、Lumley 等用于 POD/模态分析理论背书；Kramer、Koopman、SPOD、DeepONet 等用于显示作者知道最新 ROM 生态；Bisplinghoff/Ashley 等气动弹性经典用于 generalized aerodynamic force 的物理基础。

引用姿态偏中性补充，不尖锐批判。作者通常说现有方法 “shown promising performance”，随后用 “however” 指出在 structural vibration 场景下局限突出。这样的写法能避免把 gap 写成稻草人。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：41
- Introduction 引文簇数量估计：4
- References 条目数：40
- 可识别年份条目数：55
- 2021 年及以后文献数：22
- 2010 年前经典文献数：8
- 同刊引用数（按 subject 粗匹配）：2
- 高频来源期刊：Aerospace Science and Technology(2)
- 引文簇样例：[1,2], [5,6], [3,4], [28], [36], [1], [2], [3], [4], [5], [6], [7]

带引文的 gap/转折句样例：

- Data-driven approaches for unsteady aerodynamic modeling can generally be categorized as black-box or gray-box models [5,6].
- Black-box models, such as deep neural networks and operator-learning frameworks, aim to directly learn the mapping between structural mo tion and aerodynamic response from data [7–9].
- While flexible, these models typically require large training datasets and provide limited Nomenclature POD proper orthogonal decomposition ROM reduced-order model DMS dual modal spaces LSTM long short-term memory OpInf operator inference RMSE root mean square error NSE normalized spectral error AoA angle of attack CVT constant volume transformation X nodal displacement vector q generalized coordinate vector physical interpretability, which can reduce robustness and generaliza tion capability under strongly coupled aeroelastic conditions [10–12].
- It is worth noting that other modal decomposition techniques, such as spectral POD (SPOD), dynamic mode decomposition (DMD), and phase-based POD, as well as recent developments in Koopman-based modeling and physics-informed machine learning, provide comple mentary perspectives on unsteady flow modeling [32–35].

References 解析样例（前 8 条）：

- 5. Conclusion
This paper presents a DMS-LSTM reduced-order modeling frame work for predicting unsteady aerodynamic load distributions induced by structural vibrations, with improved accuracy and physical consistency.
The proposed Dual Modal Space (DMS) formulation couples struc tural modal bases with aerodynamic POD modes, enabling an explicit and bidirectional mapping between generalized aerodynamic forces and unsteady aerodynamic load distributions. By projecting aerodynamic loads onto the structural modal space, the formulation effectively miti gates modal mixing and provides a reduced representation that is well aligned with structural dynamics.
When integrated with LSTM networks, the DMS-based reduced rep resentation facilitates efficient learning of the nonlinear temporal evo lution of unsteady aerodynamic loads. Numerical investigations on a two-dimensional NACA65A004 airfoil and a three-dimensional AGARD445.6 wing demonstrate that the proposed DMS-LSTM model consistently outperforms conventional POD-LSTM approaches in both time-domain and frequency-domain metrics, achieving over 50 % reduction in surface pressure reconstruction error and up to 80.7 % improvement in lift coefficient prediction, while maintaining more than 97.2 % global reconstruction accuracy under broadband excitations and time-varying aerodynamic conditions.
The present study is limited to linear structural modal representa tions and open-loop aerodynamic load prediction driven by prescribed structural motions. Although nonlinear flow effects are implicitly captured through high-fidelity CFD data, the modal decompositions employed remain linear, and fully coupled aeroelastic feedback is not considered. Future work will focus on extending the proposed frame work to nonlinear structural dynamics and fully coupled aeroelastic simulations, as well as incorporating adaptive modal representations
X. Ding et al. Aerospace Science and Technology 176 (2026) 111927
and physics-informed learning strategies to enhance robustness and generalization under more complex flow conditions.
CRediT authorship contribution statement
Xuanhe Ding: Writing – original draft, Validation, Methodology, Investigation, Formal analysis. Chunlin Gong: Writing – review & editing, Supervision, Project administration, Conceptualization. Hua Su: Writing – review & editing, Software, Funding acquisition, Data curation, Conceptualization. Chunna Li: Writing – review & editing. Wei Li: Writing – review & editing. Xuyi Jia: Writing – review & editing.
Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
Acknowledgements
The research was supported by the National Natural Science Foun dation of China (NSFC Grant No. U92471206).
Data availability
Data will be made available on request.
References
- [1] C. Herrmann, W. Dewulf, M. Hauschild, et al., Life cycle engineering of lightweight structures, Cirp Ann. 67 (2) (2018) 651–672, https://doi.org/10.1016/j. cirp.2018.05.008.
- [2] D P Wells, B L Horvath, L A McCullers, The Flight Optimization System Weights Estimation Method, National Aeronautics and Space Administration, 2017.
- [3] E. Livne, Future of airplane aeroelasticity, J. Aircr. 40 (6) (2003) 1066–1092,
https://doi.org/10.2514/2.7218.
- [4] N F Giannelis, G A Vio, O. Levinski, A review of recent developments in the understanding of transonic shock buffet, Prog. Aerosp. Sci. 92 (2017) 39–84, https://doi.org/10.1016/j.paerosci.2017.05.004.
- [5] J. Kou, W. Zhang, Data-driven modeling for unsteady aerodynamics and aeroelasticity, Prog. Aerosp. Sci. 125 (2021) 100725, https://doi.org/10.1016/j. paerosci.2021.100725.
- [6] J C Loiseau, B R Noack, S L Brunton, Sparse reduced-order modelling: sensor-based dynamics to full-state estimation, J. Fluid Mech. 844 (2018) 459–490, https://doi. org/10.1017/jfm.2018.147.
- [7] H. Bai, Z. Wang, X. Chu, et al., Data-driven modeling of unsteady flow based on deep operator network, Phys. Fluids 36 (6) (2024), https://doi.org/10.1063/ 5.0213233.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. DMS 依赖线性结构模态；大变形、非线性结构、模态耦合强时可能失效。
2. 当前是 prescribed structural motions 的开放环预测，没有完全闭合 FSI/aeroelastic feedback。
3. H 矩阵可逆性和条件数在更复杂构型中可能成为稳定性瓶颈。
4. 结构模态数与 POD 模态数匹配的策略可能不总是最优，缺少模态数敏感性。
5. LSTM 超参数、训练集规模和数据划分对结果影响需要更系统报告。
6. 三维算例只与 POD-LSTM 对比，没有保留 DMS-OpInf/POD-OpInf 或其他深度模型对比。
7. “高保真”依赖 CFD 数据，但实验验证缺失；湍流模型、网格和动态网格误差可能传递到训练标签。
8. 泛化范围被限定为 tested parametric range，外推到跨 Mach、跨攻角、跨结构参数仍待证明。

## 17. 可复用资产

- 表示创新套路：不要先换网络，先重定义物理一致的低维变量。
- 贡献验证套路：同一表示配两个 surrogate，证明收益来自表示；同一 surrogate 配两个表示，证明 DMS 优势。
- 指标组合：RMSE 管时间域，NSE 管频域，再用 lift coefficient 和 pressure distribution 连接工程量。
- 限定写法：在摘要和结论中主动写 open-loop、prescribed motion、subsonic、tested range，降低过度承诺。
- 图表组织：概念图 -> 数学流程图 -> 训练/预测流程 -> modal coefficient 对比 -> 物理量重构。

## 18. 对我写论文的启发

如果自己的方法是“模型 + AI”，最怕被审稿人认为只是把神经网络套上去。本文的启发是：把创新点放在物理表示上，再让 AI 成为自然使用该表示的工具。这样贡献从“拟合器更准”升级成“状态变量更对”。

另外，DMS-OpInf 的设置非常值得学。它相当于一个消融实验，用来证明 DMS 不是 LSTM 特例，而是对多种 surrogate 都有帮助。

## 19. 最终浓缩

这篇论文提出 DMS-LSTM，把结构模态和气动 POD 模态连接起来，用 generalized aerodynamic forces 替代直接 POD 系数作为学习目标，从而缓解模态混叠和高阶高频振荡。最值得学习的是 gap 定义精确、方法变量有物理意义、对比实验能隔离创新来源。主要复核点是三维图像细节、H 矩阵稳定性、开放环预测向闭环气动弹性的扩展。
