# Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates

## 0. 读取说明

本文拆解依据 `801/文本/txt/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.txt` 的全文抽取。该文为 Chinese Journal of Aeronautics 2025 article-in-press/预印版本，txt 中图 1-16、附录网格/时间步验证表和若干公式存在排版错位，流场图、涡结构和曲线细节需要 PDF 图像复核。以下以文本可确认的模型、结果趋势和结论为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：0 Table 5 Initial forebody spinning rates, 1. Introduction1 transonic and supersonic regimes, 1. Wang Y, Yu JY, Wang XM, et al, 2. Numerical method, 2. Norris J, Hameed A, Economou J, et al, 3. Computational model Fig, 3. Karimi J, Rajabi MR, Sadati SH, et al, 4. Results and discussion The parameter settings for the numerical, 4. Yin JT, Jiang SJ, Hu YW, et al, 5 June 2025, 5. Conclusions, 5. Zhu Z, Shi L, He C, et al, 6. Wang G, Zhang RT, Lin HZ, et al, 7. Chen SS, Cai FJ, Xiang XH, et al, 8. Calculate the new flow field x (t, 8. Askary F, Soltani MR, 9 September 2025, 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments,, 9. Zhao XX, Shi JG, Wang ZY, et al, 10. Update the time instant, t, 10. Shen Q, Qiu LL, Pu WY, et al, 11. Pokela R, Kumar R, Vasile JD, et al, 12. Li JM, He GL, Guo HY, 13. Jaiswal R, Kothari M, Abhishek A, 14. Liu XD, Wu XS, Yin JT, 15. Throughout the entire flight, the variation trends of, 15. Yin JT, Lei JM, Wu XS, et al, 16. Both the complex angle of attack and M R, 16. Ji W, Gong CL, Jia XY, et al, 17. Raza A, 18. Yan XY, Yang SX, Zhang C, 19 October 2025, 19. Hu X, Yang SX, 20. Zhang LP, Chang XH, Ma R, et al, 21. Shi K, Liu MB, 22. Wang C, Ding LB, Feng Y, et al, 23. Lu TY, Wu XS, Lei JM, et al, 24. Sahu J, Burchett B, Gruenwald B, 25. Saini D, Shafei B, 26. Burchett BT, Sahu J, Gruenwald BC, 27. Ernst Z, Drosendahl M, Robertson BE, et al, 28. Yan L, Chang XH, Wang NH, et al, 29. Yan L, Chang XH, Wang NH, et al, 30. Silton SI, Sahu J, Fresconi F, 31. Liu Y, Wang G, Ye ZY, 32. Wang G, Zeng Z, Suo Q, 33. Pang C, Gao ZH, Yang H, et al, 34. Wang G, Ye ZY, 35. Wang G, Jiang YW, Ye ZY, 36. Seve F, Theodoulis S, Wernert P, et al, 37. Jin CH, Wang G, He R, et al, 38. Lin TY, Zhang TY, Wang G, 39. Sahu J。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：Aerodynamic and angular motion characteristics of a fixed-canard dual-spin projectile under different forebody spinning rates
- 作者：Wen Ji, Chunlin Gong, Chunna Li, Gang Wang
- 期刊：Chinese Journal of Aeronautics, 2025, article in press, DOI 10.1016/j.cja.2025.103988
- 年份：2025
- 领域：双旋弹丸、非定常气动、CFD/RBD 耦合、角运动稳定性、前体旋转控制。
- 论文类型：数值模拟 + 机理分析 + 控制策略启示。
- 研究对象：固定鸭舵双旋弹丸在不同 forebody spinning rates 下的气动特性、角运动特性和稳定机制。
- 方法：基于 unsteady RANS 和滑移网格的固定轴旋转 CFD；HUNS3D 自研并行流场求解器；7-DOF RBD；CFD/RBD 耦合模拟；网格/时间步独立性和 ARL 弹丸验证。
- 主要证据：不同攻角/前体旋速下平均气动力和力矩；Q-criterion 涡结构；截面流线和压力系数；五种前体旋速飞行仿真；复攻角与合力矩投影；自由旋转验证。
- 目标读者：弹道/弹丸气动研究者、CFD/RBD 耦合模拟研究者、双旋弹丸控制系统设计者。

## 2. 摘要与核心信息提取

一句话主张：前体旋转通过改变左右鸭舵有效攻角和翼尖涡非对称性，显著影响双旋弹丸气动和角运动；合力矩在弹轴方向的投影是决定复攻角收敛或发散的关键机制。

摘要中的逻辑很集中：先用 RANS 非定常模拟分析固定轴旋转气动，发现前体旋转导致左右鸭舵有效攻角差异，进而产生非对称翼尖涡；再用 CFD/RBD 耦合分析飞行中的角运动，识别 resultant moment projection onto projectile axis 是主导因素；最后给出控制策略：为提高角运动稳定性，前体应反向旋转或保持静止。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Aerodynamic-and-angular-motion-characteristics-of-a-fixed_2025_Chinese-Journ.md`。

中文译文：

> 本文对固定鸭翼双旋弹丸进行了数值研究，探讨其气动性能和
> 不同前体旋转速率下的角运动特性。基于雷诺平均纳维-斯托克斯
> 方程，对双自旋弹丸绕其纵轴旋转的非定常模拟进行
> 研究其空气动力特性。结果表明，前体的旋转引起了差异
> 左右鸭翼之间的有效迎角。这种差异反过来又导致了不对称
> 翼尖涡结构最终对双旋射弹的气动特性产生重要影响。
>
> 此外，基于耦合计算流体动力学和刚体动力学方法，
> 研究了双自旋弹丸飞行过程中的气动和角运动特性，并
> 分析了角运动的机理。结果表明，前体旋转显着影响
> 弹丸的空气动力特性和角运动特性。其中底层
> 机制中，合力在弹丸轴上的投影被确定为主要贡献
> 因素。非正投影会导致复杂攻角的收敛，从而增强稳定性
> 旋转的射弹。基于这些发现，提出了一种控制策略：为了提高角运动稳定性，
> 前体要么被驱动向相反方向旋转，要么保持静止状态。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

问题来源是 fixed-canard dual-spin projectile 的精度和稳定性矛盾。双旋弹丸利用后体高速旋转提供陀螺稳定，同时通过前体鸭舵修正弹道。但前体/后体相对旋转使气动强非线性、非定常，并耦合横向和法向运动。

作者把问题收束为两个可研究对象：固定轴旋转下前体旋速如何改变气动特性；飞行中前体旋速如何改变角运动稳定性。进一步，文章把角运动机制收束到一个判据：resultant moment projection `M_R · e_Δ` 与复攻角幅值变化之间的关系。

选题价值主要是机理解释和控制设计启示。若能知道哪种前体旋转方向让复攻角收敛，就能为双旋弹丸控制系统提供简单而可操作的设计原则。

## 4. 领域位置与文献版图

文献版图分为三类。

第一类是带鸭舵/修正引信弹丸气动数值研究，说明 CFD 已用于预测 projectile aerodynamic coefficients 和 flow field structures，但多集中在稳态或特定参数。

第二类是旋转弹丸非定常气动研究，包括 sliding mesh、unsteady RANS 与理论公式对比。作者强调高速旋转时理论公式会有明显偏差，说明高保真 CFD 必要。

第三类是双旋弹丸角运动研究，包括气动插值表、线性化角运动微分方程、7-DOF 模型等。作者指出这些方法常忽略非定常气动效应和气动-飞行行为耦合。

本文站位是用 CFD/RBD 同时捕捉非定常气动和角运动，弥补仅靠插值表或线性化方程难以解释机制的问题。

## 5. Gap 制造机制

gap 的核心是“已有研究知道前体旋转影响气动，但不知道它如何通过流场和力矩机制影响角运动稳定性”。

- 机理 gap：生成 yawing moment 和 lateral force 的流动机制仍未充分理解。
- 方法 gap：角运动研究依赖气动插值表或线性化方程，忽略非定常气动与飞行行为耦合。
- 应用 gap：缺少将前体旋速方向和稳定控制策略直接关联的判据。

gap 的说服力较强，因为作者不仅说“需要 CFD/RBD”，还具体指出传统 CFD 难以模拟飞行动态过程，而 CFD/RBD 可以同步求解流场和飞行动力学。

## 6. 创新性判断

作者声明的贡献包括两点：分析不同前体旋速和攻角下鸭舵干扰效应对气动特性的影响；用 CFD/RBD 分析前体旋速对角运动和轨迹特性的影响，并揭示机制。

真实创新属于“非定常气动-角运动耦合机理识别”。最重要的创新不是使用 RANS 或 CFD/RBD 本身，而是提出 `M_R · e_Δ` 作为解释复攻角收敛/发散的关键物理量，并由此导出反向旋转或静止前体有利于稳定的控制策略。

创新强度为中等偏强。方法属于成熟高保真模拟，但机理提炼和控制启示比较清楚。若有风洞或飞行试验验证，创新可信度会更高。

## 7. 论证链条复原

双旋弹丸用于提高命中精度但角运动复杂 → 前体旋速过低/过高都会影响稳定和跟踪 → 现有气动和角运动研究对非定常耦合机制解释不足 → 本文用滑移网格 unsteady RANS 分析固定轴旋转气动 → 发现前体旋转造成左右鸭舵有效攻角差异和翼尖涡非对称 → 这种非对称改变 lateral force/yawing moment → 用 CFD/RBD 模拟不同前体旋速飞行 → 观察复攻角、俯仰/偏航、力矩随旋速变化 → 提出 `M_R · e_Δ` 判据解释角运动稳定性 → 自由旋转仿真进一步验证从发散到收敛的转变 → 得出前体反向旋转或静止可提高稳定性。

论证链条较完整。薄弱环节是缺少实验数据直接验证双旋弹丸流场和角运动，附录用 ARL spinning projectile 验证 CFD/RBD 方法，但对象不是同一构型。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state. By contrast, employing a control strategy in which the forebody spins in the opposite direction or remains stationary can reduce the projection of the moment onto the projectile’s axis, thereby enhancing the stability of its angular motion.
- 本文解决方式：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 学术或工程增量：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile. Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法名称：unsteady CFD + 7-DOF RBD coupled simulation for dual-spin projectile。

输入：弹丸几何、惯量参数、飞行初始状态、Ma/Re/密度、后体旋速、前体旋速、攻角、计算网格和时间步。输出：气动力/力矩系数、流场涡结构、压力系数分布、复攻角和角运动响应。

关键方法：

1. CFD：自研 HUNS3D 并行流场求解器，采用 ALE 形式 unsteady RANS、improved LU-SGS、SA turbulence model，滑移网格处理前体/后体相对运动。
2. RBD：7-DOF 双旋弹丸动力学，包括质心平动、前体/后体滚转和俯仰/偏航角运动。
3. CFD/RBD 耦合：先求初始稳态，再在每个时间步把 CFD 气动力/力矩传给 RBD，更新状态、网格和新流场。
4. 固定轴气动分析：Ma 0.72，Re 8.45×10^5，攻角 0-25°，后体旋速 500π rad/s，前体旋速 -500π 到 500π rad/s。
5. 飞行角运动分析：五种前体旋速 case，观察复攻角和力矩投影；再做前体自由旋转 case 验证。

## 9. 证据系统与 Claim-Evidence 表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 前体旋转显著影响横向气动而非纵向气动 | 结果 4.1/Fig. 5 | 前体旋速变化对 lateral force/yawing moment 显著，对 longitudinal characteristics 有限 | 强 | 图 5 曲线细节需 PDF 复核 |
| 前体旋转造成左右鸭舵有效攻角差异 | 摘要/结果 4.1 | Fig. 6/7：不同旋速下左右翼尖涡强度不同 | 中-强 | 流场云图需 PDF 复核 |
| 翼尖涡非对称改变压力分布和偏航力矩 | 结果 4.1/Table 3/Fig. 8 | Cp 特征点 A/B 随旋速变化；前体同向旋转增强 Magnus effect | 强 | 截面位置和色标需 PDF 复核 |
| 同向旋转使角运动幅值增加，稳定性降低 | 结果 4.2/Fig. 10 | forebody 与 aft body 同向时 angle of attack 和 attitude angle 幅值增加 | 强 | 曲线细节需 PDF 复核 |
| 反向旋转或静止有利于复攻角收敛 | 结果 4.2/Fig. 10/13 | `M_R · e_Δ` 为负或非正时复攻角收敛 | 强 | 判据推导较经验化 |
| `M_R · e_Δ` 是影响角运动的关键因素 | 结果 4.2/Fig. 12/16 | 自由旋转中投影变化与复攻角先增后降一致，最终收敛 | 强 | 因果性仍主要由仿真关联支撑 |
| 数值方法具有一定可信度 | Appendix A/B | 网格/时间步独立性；ARL projectile CFD/RBD 验证 | 中 | 缺少本构型实验数据 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键信息 | 复核需求 |
| --- | --- | --- | --- | --- |
| Eq. (1) ALE RANS | 给出非定常流场控制方程 | CFD 方法可信 | ALE 处理运动网格 | 公式排版需 PDF 复核 |
| Eq. (2)-(3) 7-DOF RBD | 建立双旋角运动模型 | CFD/RBD 耦合基础 | 前体/后体滚转与俯仰/偏航耦合 | 公式排版需 PDF 复核 |
| Algorithm 1/Fig. 2 耦合流程 | 说明流场与刚体动力学如何交互 | 方法闭环 | CFD loads → RBD states → grid update | 需要 PDF 图像复核 |
| Fig. 3-4 几何与网格 | 定义计算对象 | 数值模型边界 | 6.9 million cells，sliding interface | 需要 PDF 图像复核 |
| Fig. 5 气动力/力矩系数 | 第一核心结果 | 旋速影响横向气动 | 横向力和偏航力矩随前体旋速变化 | 曲线需 PDF 复核 |
| Fig. 6-7 涡结构/压力截面 | 解释气动变化机理 | 有效攻角差异 | 翼尖涡非对称、分离点偏移 | 需要 PDF 图像复核 |
| Table 3 Cp 特征点 | 量化压力不对称 | 压力分布影响力矩 | 左右点 Cp 随 pf 改变 | 可从 txt 确认 |
| Fig. 9-11 飞行状态与力矩 | 连接气动和角运动 | 旋速影响角运动 | 力/矩周期和幅值随旋速变 | 需要 PDF 图像复核 |
| Eq. (6)-(9) 复攻角和投影 | 机制判据 | `M_R · e_Δ` 控制稳定 | 复攻角定义与单位向量 | 公式排版需 PDF 复核 |
| Fig. 14-16 自由旋转验证 | 验证机制 | 复攻角由发散转收敛 | 1.8567 s 前后阶段变化 | 需要 PDF 图像复核 |

## 11. 章节结构与篇章布局

真实章节为：1 Introduction；2 Numerical method；3 Computational model；4 Results and discussion；5 Conclusions，并含 Appendix A/B。

结构是典型高保真数值机理论文：Introduction 制造机理 gap；Section 2 说明 CFD、RBD、耦合流程；Section 3 给几何、网格和验证；Section 4 分固定轴气动与飞行角运动两部分；Conclusion 以四条结论收束。

结果节布局非常关键：先在固定轴条件下解释“气动为什么变”，再在飞行耦合中解释“角运动为什么变”。这种先局部机理后系统动态的顺序值得学习。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.12: 0 Table 5 Initial forebody spinning rates（对象/模块/过渡章节）
  - L3 p.8: 0.72 The forebody spinning has a limited impact on（对象/模块/过渡章节）
- L2 p.3: 1. Introduction1 transonic and supersonic regimes（背景定位/文献缺口）
- L2 p.19: 1. Wang Y, Yu JY, Wang XM, et al（对象/模块/过渡章节）
- L2 p.4: 2. Numerical method（方法/模型/算法）
- L2 p.19: 2. Norris J, Hameed A, Economou J, et al（对象/模块/过渡章节）
  - L3 p.4: 2.2. RBD method（方法/模型/算法）
  - L3 p.5: 2.3. Coupled CFD/RBD method（方法/模型/算法）
- L2 p.6: 3. Computational model Fig（方法/模型/算法）
- L2 p.19: 3. Karimi J, Rajabi MR, Sadati SH, et al（对象/模块/过渡章节）
  - L3 p.6: 3.1. Geometric configuration（对象/模块/过渡章节）
  - L3 p.7: 3.2. Computational grid（对象/模块/过渡章节）
- L2 p.7: 4. Results and discussion The parameter settings for the numerical（结果/验证/讨论）
- L2 p.19: 4. Yin JT, Jiang SJ, Hu YW, et al（对象/模块/过渡章节）
  - L3 p.7: 4.1. Aerodynamic characteristics analysis in fixed-axis and the reference area is 0（对象/模块/过渡章节）
  - L3 p.11: 4.2. Aerodynamic and angular motion characteristics Table 4 Initial states for numerical（对象/模块/过渡章节）
- L2 p.1: 5 June 2025（对象/模块/过渡章节）
- L2 p.17: 5. Conclusions（结论/贡献回收）
- L2 p.19: 5. Zhu Z, Shi L, He C, et al（对象/模块/过渡章节）
- L2 p.19: 6. Wang G, Zhang RT, Lin HZ, et al（对象/模块/过渡章节）
- L2 p.19: 7. Chen SS, Cai FJ, Xiang XH, et al（对象/模块/过渡章节）
- L2 p.6: 8. Calculate the new flow field x (t（对象/模块/过渡章节）
- L2 p.19: 8. Askary F, Soltani MR（对象/模块/过渡章节）
- L2 p.1: 9 September 2025（对象/模块/过渡章节）
- L2 p.6: 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments,（对象/模块/过渡章节）
- L2 p.19: 9. Zhao XX, Shi JG, Wang ZY, et al（对象/模块/过渡章节）
- L2 p.6: 10. Update the time instant, t（对象/模块/过渡章节）
- L2 p.19: 10. Shen Q, Qiu LL, Pu WY, et al（对象/模块/过渡章节）
- L2 p.19: 11. Pokela R, Kumar R, Vasile JD, et al（对象/模块/过渡章节）
- L2 p.19: 12. Li JM, He GL, Guo HY（对象/模块/过渡章节）
- L2 p.20: 13. Jaiswal R, Kothari M, Abhishek A（对象/模块/过渡章节）
- L2 p.20: 14. Liu XD, Wu XS, Yin JT（对象/模块/过渡章节）
- L2 p.16: 15. Throughout the entire flight, the variation trends of（对象/模块/过渡章节）
- L2 p.20: 15. Yin JT, Lei JM, Wu XS, et al（对象/模块/过渡章节）
- L2 p.17: 16. Both the complex angle of attack and M R（对象/模块/过渡章节）
- L2 p.20: 16. Ji W, Gong CL, Jia XY, et al（对象/模块/过渡章节）
- L2 p.20: 17. Raza A（对象/模块/过渡章节）
- L2 p.20: 18. Yan XY, Yang SX, Zhang C（对象/模块/过渡章节）
- L2 p.1: 19 October 2025（对象/模块/过渡章节）
- L2 p.20: 19. Hu X, Yang SX（对象/模块/过渡章节）
- L2 p.20: 20. Zhang LP, Chang XH, Ma R, et al（对象/模块/过渡章节）
- L2 p.20: 21. Shi K, Liu MB（对象/模块/过渡章节）
- L2 p.20: 22. Wang C, Ding LB, Feng Y, et al（对象/模块/过渡章节）
- L2 p.20: 23. Lu TY, Wu XS, Lei JM, et al（对象/模块/过渡章节）
- L2 p.20: 24. Sahu J, Burchett B, Gruenwald B（对象/模块/过渡章节）
- L2 p.20: 25. Saini D, Shafei B（对象/模块/过渡章节）
- L2 p.20: 26. Burchett BT, Sahu J, Gruenwald BC（对象/模块/过渡章节）
- L2 p.20: 27. Ernst Z, Drosendahl M, Robertson BE, et al（对象/模块/过渡章节）
- L2 p.20: 28. Yan L, Chang XH, Wang NH, et al（对象/模块/过渡章节）
- L2 p.20: 29. Yan L, Chang XH, Wang NH, et al（对象/模块/过渡章节）
- L2 p.20: 30. Silton SI, Sahu J, Fresconi F（对象/模块/过渡章节）
- L2 p.20: 31. Liu Y, Wang G, Ye ZY（对象/模块/过渡章节）
- L2 p.20: 32. Wang G, Zeng Z, Suo Q（对象/模块/过渡章节）
- L2 p.20: 33. Pang C, Gao ZH, Yang H, et al（对象/模块/过渡章节）
- L2 p.20: 34. Wang G, Ye ZY（对象/模块/过渡章节）
- L2 p.21: 35. Wang G, Jiang YW, Ye ZY（对象/模块/过渡章节）
- L2 p.21: 36. Seve F, Theodoulis S, Wernert P, et al（对象/模块/过渡章节）
- L2 p.21: 37. Jin CH, Wang G, He R, et al（对象/模块/过渡章节）
- L2 p.21: 38. Lin TY, Zhang TY, Wang G（对象/模块/过渡章节）
- L2 p.21: 39. Sahu J（对象/模块/过渡章节）
- L2 p.19: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 0 Table 5 Initial forebody spinning rates | 12 | 2 | 对象/模块/过渡章节 |
| 0.72 The forebody spinning has a limited impact on | 8 | 3 | 对象/模块/过渡章节 |
| 1. Introduction1 transonic and supersonic regimes | 3 | 2 | 背景定位/文献缺口 |
| 1. Wang Y, Yu JY, Wang XM, et al | 19 | 2 | 对象/模块/过渡章节 |
| 2. Numerical method | 4 | 2 | 方法/模型/算法 |
| 2. Norris J, Hameed A, Economou J, et al | 19 | 2 | 对象/模块/过渡章节 |
| 2.2. RBD method | 4 | 3 | 方法/模型/算法 |
| 2.3. Coupled CFD/RBD method | 5 | 3 | 方法/模型/算法 |
| 3. Computational model Fig | 6 | 2 | 方法/模型/算法 |
| 3. Karimi J, Rajabi MR, Sadati SH, et al | 19 | 2 | 对象/模块/过渡章节 |
| 3.1. Geometric configuration | 6 | 3 | 对象/模块/过渡章节 |
| 3.2. Computational grid | 7 | 3 | 对象/模块/过渡章节 |
| 4. Results and discussion The parameter settings for the numerical | 7 | 2 | 结果/验证/讨论 |
| 4. Yin JT, Jiang SJ, Hu YW, et al | 19 | 2 | 对象/模块/过渡章节 |
| 4.1. Aerodynamic characteristics analysis in fixed-axis and the reference area is 0 | 7 | 3 | 对象/模块/过渡章节 |
| 4.2. Aerodynamic and angular motion characteristics Table 4 Initial states for numerical | 11 | 3 | 对象/模块/过渡章节 |
| 5 June 2025 | 1 | 2 | 对象/模块/过渡章节 |
| 5. Conclusions | 17 | 2 | 结论/贡献回收 |
| 5. Zhu Z, Shi L, He C, et al | 19 | 2 | 对象/模块/过渡章节 |
| 6. Wang G, Zhang RT, Lin HZ, et al | 19 | 2 | 对象/模块/过渡章节 |
| 7. Chen SS, Cai FJ, Xiang XH, et al | 19 | 2 | 对象/模块/过渡章节 |
| 8. Calculate the new flow field x (t | 6 | 2 | 对象/模块/过渡章节 |
| 8. Askary F, Soltani MR | 19 | 2 | 对象/模块/过渡章节 |
| 9 September 2025 | 1 | 2 | 对象/模块/过渡章节 |
| 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments, | 6 | 2 | 对象/模块/过渡章节 |
| 9. Zhao XX, Shi JG, Wang ZY, et al | 19 | 2 | 对象/模块/过渡章节 |
| 10. Update the time instant, t | 6 | 2 | 对象/模块/过渡章节 |
| 10. Shen Q, Qiu LL, Pu WY, et al | 19 | 2 | 对象/模块/过渡章节 |
| 11. Pokela R, Kumar R, Vasile JD, et al | 19 | 2 | 对象/模块/过渡章节 |
| 12. Li JM, He GL, Guo HY | 19 | 2 | 对象/模块/过渡章节 |
| 13. Jaiswal R, Kothari M, Abhishek A | 20 | 2 | 对象/模块/过渡章节 |
| 14. Liu XD, Wu XS, Yin JT | 20 | 2 | 对象/模块/过渡章节 |
| 15. Throughout the entire flight, the variation trends of | 16 | 2 | 对象/模块/过渡章节 |
| 15. Yin JT, Lei JM, Wu XS, et al | 20 | 2 | 对象/模块/过渡章节 |
| 16. Both the complex angle of attack and M R | 17 | 2 | 对象/模块/过渡章节 |
| 16. Ji W, Gong CL, Jia XY, et al | 20 | 2 | 对象/模块/过渡章节 |
| 17. Raza A | 20 | 2 | 对象/模块/过渡章节 |
| 18. Yan XY, Yang SX, Zhang C | 20 | 2 | 对象/模块/过渡章节 |
| 19 October 2025 | 1 | 2 | 对象/模块/过渡章节 |
| 19. Hu X, Yang SX | 20 | 2 | 对象/模块/过渡章节 |
| 20. Zhang LP, Chang XH, Ma R, et al | 20 | 2 | 对象/模块/过渡章节 |
| 21. Shi K, Liu MB | 20 | 2 | 对象/模块/过渡章节 |
| 22. Wang C, Ding LB, Feng Y, et al | 20 | 2 | 对象/模块/过渡章节 |
| 23. Lu TY, Wu XS, Lei JM, et al | 20 | 2 | 对象/模块/过渡章节 |
| 24. Sahu J, Burchett B, Gruenwald B | 20 | 2 | 对象/模块/过渡章节 |
| 25. Saini D, Shafei B | 20 | 2 | 对象/模块/过渡章节 |
| 26. Burchett BT, Sahu J, Gruenwald BC | 20 | 2 | 对象/模块/过渡章节 |
| 27. Ernst Z, Drosendahl M, Robertson BE, et al | 20 | 2 | 对象/模块/过渡章节 |
| 28. Yan L, Chang XH, Wang NH, et al | 20 | 2 | 对象/模块/过渡章节 |
| 29. Yan L, Chang XH, Wang NH, et al | 20 | 2 | 对象/模块/过渡章节 |
| 30. Silton SI, Sahu J, Fresconi F | 20 | 2 | 对象/模块/过渡章节 |
| 31. Liu Y, Wang G, Ye ZY | 20 | 2 | 对象/模块/过渡章节 |
| 32. Wang G, Zeng Z, Suo Q | 20 | 2 | 对象/模块/过渡章节 |
| 33. Pang C, Gao ZH, Yang H, et al | 20 | 2 | 对象/模块/过渡章节 |
| 34. Wang G, Ye ZY | 20 | 2 | 对象/模块/过渡章节 |
| 35. Wang G, Jiang YW, Ye ZY | 21 | 2 | 对象/模块/过渡章节 |
| 36. Seve F, Theodoulis S, Wernert P, et al | 21 | 2 | 对象/模块/过渡章节 |
| 37. Jin CH, Wang G, He R, et al | 21 | 2 | 对象/模块/过渡章节 |
| 38. Lin TY, Zhang TY, Wang G | 21 | 2 | 对象/模块/过渡章节 |
| 39. Sahu J | 21 | 2 | 对象/模块/过渡章节 |
| References | 19 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 前半段说明双旋弹丸应用和旋速稳定性矛盾，中段综述 CFD 与角运动研究，后段指出插值表/线性化方程不够，最后列贡献。节奏是从工程痛点到方法必要性。

方法段落偏硬技术叙述：每个模块先给求解器和方程，再解释变量。Results 段落图驱动明显，通常先描述图中趋势，再给流动机理解释，再连接到稳定性。

结论四条非常对应正文：气动影响、涡结构机理、力矩投影机制、控制策略。这种“每条结论都是一个 claim”很适合模仿。

## 13. 文笔画像与语言习惯

文笔偏机理型 CFD 论文，常用词包括 unsteady aerodynamic characteristics, angular motion characteristics, forebody spinning rate, wingtip vortex, effective angle of attack, resultant moment projection, complex angle of attack。

语气较强，常用 “significantly affects”, “dominant contributing factor”, “key factor”, 但通常由仿真图支撑。方法部分被动语态多；贡献和结论中主动句较多。

时态：摘要和结论用现在时陈述普遍发现；方法用过去/现在混合；结果解读用现在时。作者常用 “Compared to...”, “Conversely...”, “As the spinning rate increases...” 来组织对比。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：238984
- 高频词：spinning(505)；forebody(498)；projectile(491)；aerodynamic(389)；angle(370)；angular(333)；motion(308)；attack(265)；dual-spin(237)；moment(236)；rad(233)；characteristics(233)；coefficient(181)；rate(180)；direction(172)；rates(171)；flight(171)；cfd(167)；body(166)；yawing(152)
- 高频名词化/学术名词：motion(308)；moment(236)；characteristics(233)；direction(172)；stability(130)；velocity(113)；projection(81)；pressure(70)；simulation(64)；influence(45)；independence(41)；difference(37)；reference(32)；separation(32)；validation(31)
- 高频学术动词：presented(87)；compared(41)；analyzed(33)；developed(16)；indicate(12)；predicted(12)；analyze(9)；validated(8)；provide(4)；demonstrate(3)；identified(3)；evaluate(1)
- 高频形容词：aerodynamic(389)；moment(236)；coefficient(181)；different(137)；negative(105)；lateral(101)；initial(87)；computational(64)；numerical(63)；stationary(56)；resultant(48)；effective(47)；significant(45)；positive(44)；total(41)
- 高频副词：gradually(55)；significantly(48)；conversely(28)；freely(27)；accurately(15)；simultaneously(14)；additionally(13)；similarly(13)；typically(9)；nearly(9)；essentially(9)；generally(9)；correspondingly(9)；continuously(9)；eventually(9)
- 高频二词短语：forebody spinning(286)；angular motion(264)；angle attack(216)；dual-spin projectile(196)；spinning rate(153)；spinning rates(149)；cfd rbd(127)；aft body(126)；aerodynamic characteristics(124)；coupled cfd(109)；complex angle(104)；yawing moment(90)
- 高频三词短语：forebody spinning rates(116)；coupled cfd rbd(105)；forebody spinning rate(89)；complex angle attack(87)；angular motion characteristics(69)；different forebody spinning(59)；yawing moment coefficient(59)；aerodynamic angular motion(47)；effective angle attack(47)；characteristics dual-spin projectile(45)；cfd rbd method(43)；stability angular motion(41)
- 被动语态估计：393；`we + 动作动词` 主动句估计：0
- 一般现在时线索：950；一般过去时线索：1296；现在完成时线索：5；情态动词线索：105

分章节正文词频：

- 0 Table 5 Initial forebody spinning rates: angle(33)；projectile(31)；forebody(27)；spinning(26)；angular(24)；motion(21)；attack(20)；aerodynamic(19)
- 1. Introduction1 transonic and supersonic regimes: spinning(64)；projectile(64)；forebody(61)；aerodynamic(58)；angle(44)；angular(44)；motion(41)；attack(33)
- 2. Numerical method: grid(8)；flow(7)；projectile(7)；aerodynamic(7)；moments(7)；cfd(6)；method(6)；body(6)
- 3. Computational model Fig: forebody(50)；spinning(47)；projectile(39)；angle(37)；rad(28)；attack(26)；angular(26)；moment(25)
- 4. Results and discussion The parameter settings for the numerical: forebody(48)；spinning(46)；angle(37)；projectile(34)；rad(28)；attack(26)；angular(26)；moment(25)
- 5 June 2025: spinning(60)；forebody(58)；projectile(55)；aerodynamic(50)；angular(42)；motion(40)；angle(37)；characteristics(32)
- 5. Conclusions: forebody(8)；angular(6)；motion(6)；projectile(6)；spinning(6)；aerodynamic(5)；characteristics(5)；axis(4)
- 5. Zhu Z, Shi L, He C, et al: kinematic(2)；construction(1)；performance(1)；analysis(1)；suspension(1)；support(1)；wind(1)；tunnel(1)
- 8. Calculate the new flow field x (t: forebody(50)；spinning(49)；projectile(42)；angle(37)；aerodynamic(28)；rad(28)；attack(26)；angular(26)
- 9 September 2025: projectile(71)；spinning(70)；forebody(67)；aerodynamic(62)；angular(51)；motion(48)；angle(46)；characteristics(39)
- 9. Integrate the aerodynamic loads to updata aerodynamic forces and moments,: forebody(41)；spinning(39)；rad(26)；angle(26)；projectile(25)；rate(17)；coefficient(17)；angular(17)
- 9. Zhao XX, Shi JG, Wang ZY, et al: nonlinear(1)；aerodynamic(1)；modeling(1)；analysis(1)；body(1)；fixed(1)；canard(1)；dual-spin(1)
- 10. Update the time instant, t: forebody(50)；spinning(49)；projectile(42)；angle(37)；rad(28)；aerodynamic(26)；attack(26)；angular(26)
- 10. Shen Q, Qiu LL, Pu WY, et al: aerodynamic(1)；characteristics(1)；characterization(1)；double(1)；spin(1)；structure(1)；two-dimensional(1)；correction(1)
- 15. Throughout the entire flight, the variation trends of: angle(10)；attack(10)；forebody(9)；angular(8)；motion(8)；projectile(8)；moment(7)；direction(6)
- 16. Both the complex angle of attack and M R: projectile(21)；aerodynamic(18)；characteristics(12)；spinning(11)；dual-spin(11)；grid(11)；angle(10)；attack(10)
- 17. Raza A: dynamic(1)；stability(1)；analysis(1)；spin-stabilized(1)；projectile(1)；proceedings(1)；international(1)；bhurban(1)
- 19 October 2025: aerodynamic(37)；projectile(30)；angular(24)；motion(24)；characteristics(24)；spinning(22)；dual-spin(18)；cfd(18)
- 21. Shi K, Liu MB: eng(2)；trajectory(1)；analysis(1)；dual-spinstabilized(1)；projectile(1)；fixed-canards(1)；precision(1)；guidance(1)
- 22. Wang C, Ding LB, Feng Y, et al: research(1)；angular(1)；motion(1)；characteristics(1)；stability(1)；trajectorycorrected(1)；rocket(1)；projectile(1)
- 24. Sahu J, Burchett B, Gruenwald B: computational(2)；advanced(1)；cfdbased(1)；coupled(1)；approach(1)；prediction(1)；complex(1)；flight(1)
- 26. Burchett BT, Sahu J, Gruenwald BC: aiaa(2)；simulating(1)；extreme(1)；maneuvers(1)；flight(1)；conditions(1)；coupled(1)；rigid(1)
- 30. Silton SI, Sahu J, Fresconi F: aiaa(2)；comparison(1)；uncoupled(1)；coupled(1)；cfd-based(1)；simulation(1)；techniques(1)；prediction(1)
- 32. Wang G, Zeng Z, Suo Q: aiaa(2)；trajectory(1)；simulation(1)；spinning(1)；projectile(1)；variable(1)；step(1)；size(1)
- 34. Wang G, Ye ZY: mixed(1)；element(1)；type(1)；unstructured(1)；grid(1)；generation(1)；application(1)；viscous(1)
- 38. Lin TY, Zhang TY, Wang G: spectrum(1)；analysis(1)；aerodynamic(1)；interference(1)；canard(1)；shedding(1)；vortex(1)；dual-spin(1)
- 39. Sahu J: interests(3)；declare(2)；competing(2)；financial(2)；personal(2)；relationships(2)；editorial(2)；editor(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

- 背景句式：`To enhance hit accuracy, the fixed-canard dual-spin projectile... has been developed.`
- Gap 句式：`the flow mechanisms ... remain not fully understood.`
- 方法句式：`The coupled CFD/RBD method simultaneously solves...`
- 贡献句式：`The main contributions of this work are summarized as follows:`
- 机理句式：`This discrepancy, in turn, gives rise to...`
- 对比句式：`Conversely, when ..., the ...`
- 结果句式：`As the angle of attack increases, the impact ... becomes more significant.`
- 控制启示句式：`Based on these findings, a control strategy is proposed...`

可复用表达：把复杂动态机制浓缩为一个投影量或判据，是机理论文非常有力的写法。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
#### Gap/转折句
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  可迁移模板：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
- 原句：By contrast, employing a control strategy in which the forebody spins in the opposite direction or remains stationary can reduce the projection of the moment onto the projectile’s axis, thereby enhancing the stability of its angular motion.
  可迁移模板：By contrast, employing a control strategy in which the forebody spins in the opposite direction or remains stationary can reduce the projection of the moment onto the projectile’s axis, thereby enhancing the stability of its angular motion.
#### 方法提出句
- 原句：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed.
  可迁移模板：Furthermore, based on the coupled computational fluid dynamics and rigid body dynamics approach, the aerodynamic and angular motion characteristics of the dual-spin projectile during flight are investigated, and the mechanism of the angular motion is analyzed.
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  可迁移模板：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
#### 结果呈现句
- 原句：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
  可迁移模板：The results indicate that the spinning of the forebody induces a discrepancy in the effective angle of attack between the left and right canards.
- 原句：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
  可迁移模板：The results demonstrate that the forebody spinning significantly affects both the aerodynamic characteristics and angular motion characteristics of the projectile.
- 原句：This results in asymmetry in the wingtip vortex structures, and changes its aerodynamic characteristics. (3) The projection of the moment perpendicular to the body axis onto the projectile axis is a key factor influencing its angular motion.
  可迁移模板：This results in asymmetry in the wingtip vortex structures, and changes its aerodynamic characteristics. (X) The projection of the moment perpendicular to the body axis onto the projectile axis is a key factor influencing its angular motion.
#### 贡献/增量句
- 原句：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
  可迁移模板：Based on these findings, a control strategy is proposed: to improve angular motion stability, the forebody is either driven to spin in the opposite direction or remained in a stationary state.
#### 限制/边界句
- 未在摘要/引言/结论中稳定识别；正式使用时从对应章节人工补足。
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略先按对象后按方法。对象文献包括 spin-stabilized projectiles、canard-controlled projectiles、dual-spin projectiles；方法文献包括 CFD、unsteady RANS、sliding mesh、CFD/RBD、7-DOF 和线性化角运动方程。

作者对前人评价有两类：对 CFD 气动研究表示继承，对插值表和线性化角运动模型指出局限。引用不是为了罗列，而是为了证明“必须用 CFD/RBD 耦合方法研究气动-角运动耦合”。

gap 连接方式是：前人知道前体旋转影响气动，但机制不清；前人研究角运动，但忽略非定常气动耦合；因此本文同时分析流场结构和飞行动态。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：0
- Introduction 引文簇数量估计：0
- References 条目数：39
- 可识别年份条目数：45
- 2021 年及以后文献数：27
- 2010 年前经典文献数：2
- 同刊引用数（按 subject 粗匹配）：3
- 高频来源期刊：Chinese Journal of Aeronautics(3)
- 引文簇样例：未识别

带引文的 gap/转折句样例：

- 未稳定识别带引文的 gap 转折句；需要回到 Introduction 人工核对。

References 解析样例（前 8 条）：

- 1. Wang Y, Yu JY, Wang XM, et al. A guidance and control design with reduced information for a dual-spin stabilized projectile. Def Technol 2024;33:494–505. Chinese Journal of Aeronautics · 18 ·
- 2. Norris J, Hameed A, Economou J, et al. A review of dual-spin projectile stability. Def Technol 2020;16(1):1– 9.
- 3. Karimi J, Rajabi MR, Sadati SH, et al. Multidisciplinary design optimization of a dual-spin guided vehicle. Def Technol 2024;37:133–48.
- 4. Yin JT, Jiang SJ, Hu YW, et al. Aerodynamic characteristics and dynamic stability of coning motion of spinning finned projectile in supersonic conditions. Aerospace 2025;12(3):225.
- 5. Zhu Z, Shi L, He C, et al. Construction and kinematic performance analysis of a suspension support for wind tunnel tests of spinning projectiles based on wire-driven parallel robot with kinematic redundancy. Chin J Aeronaut 2024;37(12):404–15.
- 6. Wang G, Zhang RT, Lin HZ, et al. Study on influence of canard rotation speed on following stability of dual-spin projectile. Aero Weapon 2024;31(2):71–8 [Chinese].
- 7. Chen SS, Cai FJ, Xiang XH, et al. A low-diffusion robust flux splitting scheme towards wide-ranging Mach number flows. Chin J Aeronaut 2021;34(5):628–41.
- 8. Askary F, Soltani MR. Effects of Mach numbers on Magnus induced surface pressure. Chin J Aeronaut 2020;33(12):3058–72.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 主要证据来自数值模拟，缺少本构型风洞、自由飞或弹道实验验证。
2. RANS/SA 模型对复杂分离、旋转涡结构的预测精度可能受限。
3. ARL 弹丸验证对象与 fixed-canard dual-spin projectile 不同，只能说明 CFD/RBD 流程可信，不能完全验证本文构型。
4. `M_R · e_Δ` 判据的因果性主要来自仿真相关和物理解释，缺少严格解析推导。
5. 控制策略“反向旋转或静止”未考虑执行机构能耗、响应速度和制导任务需求。
6. 文章为 article in press，版式和细节可能在最终 Version of Record 中调整。

## 17. 可复用资产

- 选题套路：从工程稳定性问题进入，找一个可解释的物理判据连接流场和运动。
- 证据套路：固定轴气动机制 → 飞行耦合响应 → 自由旋转验证，三步递进。
- 图表资产：涡结构和压力截面用于解释力矩变化，复攻角和投影曲线用于解释稳定性。
- 写法资产：用 `Compared to`/`Conversely` 组织旋转方向影响，读者很容易跟踪正负旋速差异。
- 结论资产：把机理直接转成控制策略，是工程 CFD 论文很好的收束方式。

## 18. 对我写论文的启发

如果我写数值机理论文，不能只展示“参数变化导致结果变化”，还要像本文一样找一个中间机制变量：这里是有效攻角差异、翼尖涡不对称、`M_R · e_Δ`。这样论文才从参数扫描变成机理解释。

同时，要尽量补强验证链。本文有网格/时间步独立性和外部构型验证，但如果能增加本构型实验，审稿风险会明显降低。自己的论文也应提前设计“验证对象与研究对象一致性”的证据。

## 19. 最终浓缩

本文的核心贡献是解释 fixed-canard dual-spin projectile 中前体旋速如何通过鸭舵有效攻角差异、非对称翼尖涡和合力矩投影影响角运动稳定性。最强可复用点是将复杂角运动浓缩为 `M_R · e_Δ` 判据，并导出“前体反向旋转或静止更稳定”的控制启示。最大风险是数值模拟主导、实验验证不足。
