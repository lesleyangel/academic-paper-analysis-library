# A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory

## 0. 读取说明

本文拆解基于 `801/文本/txt/A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En.txt`。该文公式密集，txt 抽取中双栏串行导致部分公式、表格和图题混排；尤其是 Eq. (1)-(48)、Table 1-10、Fig. 1-12 的流程和曲线细节需要 PDF 图像复核。本文以摘要、Introduction、Problem statement、Proposed method、Examples、Conclusion 可识别内容为主。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Problem statement and direct solution method for HTRA, 3 The proposed method, 4 Examples and discussions, 5 Conclusion。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：A novel hybrid time-variant reliability analysis method through approximating bound-most-probable point trajectory。
- 作者：Nanzheng Zou, Chunlin Gong, Licong Zhang, Yunwei Zhang, Xiaowei Wang, Chunna Li。
- 期刊与年份：Probabilistic Engineering Mechanics, 2024, 75, 103558。
- 研究对象：同时含随机变量/随机过程与区间变量/区间过程的 hybrid time-variant reliability analysis（HTRA）。
- 论文类型：结构可靠性方法论文，含数值算例和工程算例验证。
- 核心方法：提出 bound-most-probable point trajectory（BMPPT）；通过时间离散将 HTRA 转成时不变串联系统可靠性问题；基于 BMPPT 线性化上下界极限状态函数为两个 Gaussian processes；用 active learning Kriging 近似 BMPPT，减少 BMPP 搜索；用 EOLE 与 MCS 估计时变失效概率上下界。
- 主要证据：corroded steel beam、10-bar truss、solid rocket engine shell、rocket inter-stage structure 四个例子；与 MCS、TDHTRA 对比；相对误差多小于 5%，BMPP 搜索和原始极限状态函数评估次数显著降低。

## 2. 摘要与核心信息提取

本文的一句话主张是：对于含 aleatory 和 epistemic 两类不确定性、且 epistemic 还随时间变化的 HTRA 问题，不必直接大规模逼近整个时变极限状态函数；只要近似 bound-most-probable point trajectory，就能高效线性化失效边界并估计失效概率上下界。

摘要的信息链条是：工程结构可靠性需要处理时变不确定性；信息不足导致部分不确定性不能用随机模型，只能用区间变量/过程描述；现有 HTRA 方法需要过多原函数评估；本文提出 BMPPT 和 HABMPPT；最后用两个数值例子和两个工程应用验证高精度与高效率。

核心卖点是“近似轨迹而非近似函数”。这与很多 surrogate reliability 方法不同：后者试图全局替代 limit-state function，而本文只近似最关键的 bound MPP 随时间移动轨迹，降低维度和评估成本。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/A-novel-hybrid-time-variant-reliability-analysis-metho_2024_Probabilistic-En.md`。

中文译文：

> 在工程领域，时变可靠性分析（TRA）用于衡量时变不确定性下结构的安全水平。由于缺乏信息或数据，一些不确定性无法直接量化为随机模型，导致大多数问题同时存在偶发性和认知性不确定性。一般来说，随机模型和区间模型分别用于描述偶然和认知不确定性。对于考虑两种不确定性的混合TRA（HTRA）问题，现有方法需要过度评估原始时变极限状态函数，这对于工程问题来说代价太大。为了解决这个问题，我们提出了边界最可能点轨迹（BMPPT）的概念，它可用于构造极限状态超曲面的近似。此外，我们开发了一种基于近似BMPPT的HTRA方法，可以进一步提高计算效率。首先，基于时间离散化，我们将HTRA问题转化为与时间无关的串联系统可靠性问题，该问题可以通过在所有离散时刻搜索最有可能点（BMPP）来解决。然后，通过 BMPPT，时变极限状态函数的下限和上限被线性化为两个高斯过程。
>
> 最后，进行扩展最优线性估计和蒙特卡罗模拟来估计时变可靠性。为了避免过多的 BMPP 搜索，使用主动学习克里金法来近似 BMPPT。对悬臂梁和10杆桁架的两个数值算例以及固体火箭发动机壳体和火箭级间结构的两个工程应用进行了研究，结果表明该方法能够高精度、高效地求解HTRA问题。通过计算极限状态函数的极值分布来估计失效概率。在复杂的工程应用中，通过分析获得极值的概率特征可能具有挑战性。基于模拟的方法，例如蒙特卡罗模拟（MCS）和重要性采样方法[9]，提供了一种替代但昂贵的方法来估计极值分布。为了减轻计算负担，替代模型，例如克里金法[10,11]和人工神经网络[12,13]，已被引入基于模拟的方法中。单环克里金法（SILK）[14]方法和混合高效全局优化（m-EGO）[15]方法基于极值函数构建的代理模型来近似极值分布。
>
> 实时估计误差引导主动学习克里金法（REAL）[16]方法直接为时变极限状态函数建立代理模型。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来源是工程可靠性中的混合不确定性。实际结构同时存在固有随机性（aleatory uncertainties）和信息不足导致的认知不确定性（epistemic uncertainties），后者常用 interval variables 或 interval processes 描述。再加上载荷、腐蚀、强度退化等随时间变化，问题就变成 hybrid time-variant reliability。

作者把问题定义为：如何估计在时间区间 `[ts, te]` 内的失效概率上下界 `[PLf, PUf]`，其中极限状态函数同时含随机输入、随机过程、区间变量和区间过程。这个定义使文章既区别于传统 TRA，也区别于静态 hybrid reliability。

选题价值在于工程计算成本。直接 MCS 或 TDHTRA 需要在大量时间点搜索 BMPP 或评估原始极限状态函数；对于有限元/复杂结构，这会不可承受。因此更高效的近似对象和主动学习策略有实际意义。

## 4. 领域位置与文献版图

Introduction 先把 TRA 分为 extreme value-based 和 first passage-based 两类，再细分 first passage 中的 out-crossing rate methods 与 time discretization-based TRA。作者指出 out-crossing rate 依赖独立越界假设，TDTRA 可避免越界率计算但需要在大量离散时间点做 FORM/MPP 搜索。

随后文章引入 uncertainty 类型：aleatory 来自物理系统固有变化，epistemic 来自主观认知/数据不足。已有 TRA 多基于概率理论，只能处理 aleatory；hybrid reliability 方法能处理随机与区间，但 hybrid time-variant reliability 尤其包含 interval processes 的研究较少。

本文站位是继承 MPPT/AMPPT 思路，但将 MPP trajectory 扩展为 bound MPP trajectory，用于 HTRA 上下界失效概率估计；同时借 active learning Kriging 避免每个时间点直接搜索 BMPP。

## 5. Gap 制造机制

本文 gap 是典型计算成本 gap 与问题类型 gap。问题类型 gap：现有 TRA 多处理随机变量/随机过程，对时间变化的 epistemic uncertainties 处理不足。计算成本 gap：已有 HTRA 若用深度网络或 surrogate 逼近原始极限状态函数，在高维随机/区间/过程输入下成本和难度迅速上升；TDHTRA 直接离散又要大量 BMPP 搜索。

作者制造 gap 的方式是“替代近似对象”：不是说 surrogate 不好，而是说复杂 HTRA 中精确逼近整个 limit-state function 太难；根据 TDTRA 经验，只要掌握 MPP/BMPP 轨迹，就能较准估计时变可靠性。因此本文近似 BMPPT 更合适。

这个 gap 说服力强，因为 reliability 领域非常关注函数评估次数（NFE）和 MPP 搜索次数。可被追问的是：BMPPT 是否平滑、是否存在跳跃/多峰、Kriging 近似是否可靠，这些会影响方法稳定性。

## 6. 创新性判断

作者声明的三项贡献是：提出 BMPPT 概念；基于 BMPPT 线性化时变极限状态函数上下界以高效估计失效概率；用 active learning Kriging 近似 BMPPT，减少 BMPP 搜索次数。

真实创新属于可靠性方法创新。它不是简单把 Kriging 放进 MCS，而是把 HTRA 的关键对象从高维 limit-state surface 降到随时间变化的 bound-most-probable point trajectory，再通过 Gaussian process 表示线性化后的上下界过程。

创新强度：强。原因是概念层面的 BMPPT 明确扩展了 MPPT 思路，并且四个算例覆盖数值结构和航天工程结构，效率收益明显。风险在于方法依赖 FORM 线性化思想，对强非线性、多设计点或非平滑 BMPPT 的问题可能失效。

## 7. 论证链条复原

全文论证链条如下：

1. 结构时变可靠性需要评估整个寿命区间内不失效的概率。
2. 实际结构同时存在随机和区间不确定性，且部分 epistemic uncertainties 随时间变化。
3. 直接 MCS 或 TDHTRA 成本高，尤其是每个时间点都要搜索 BMPP 或评估原函数。
4. 在传统 TRA 中，MPPT 可减少 MPP 搜索；对 HTRA 可类似定义 lower/upper BMPPT。
5. 基于时间离散，搜索少量 LBMPP/UBMPP 作为训练点，用 active learning Kriging 近似整条 BMPPT。
6. 在近似 BMPPT 上线性化上下界极限状态函数，转成两个 Gaussian processes。
7. 用 EOLE 生成过程样本，再用 MCS 估计失效概率上下界。
8. 四个例子显示误差通常小于 5%，NFE 和 BMPP 搜索次数远少于 TDHTRA/MCS。

逻辑闭合度高。最薄弱环节在于 FORM/BMPP 线性化对复杂非线性极限状态边界的适用性；作者在结尾也承认 correlated uncertainties、BMPP 更高效求解、非光滑/不连续 BMPPT 等仍需研究。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems. In complex engineering applications, obtaining the probability characteristics of the extreme value analyti cally can be challenging. For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
- 已有研究不足/GAP：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures. Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 本文解决方式：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems. In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties. For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
- 学术或工程增量：Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency. Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function. Simulation-based methods, such as Monte Carlo simulation (MCS) and importance sampling method [9], provide an alternative but expensive way to estimate the extreme value distri bution.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法第一步是问题转化。传统 TRA 中随机变量 X 和随机过程 S(t) 经变换进入独立标准正态空间；HTRA 进一步包含区间变量 Y 和区间过程 I(t)。区间过程通过 truncated interval K-L expansion 表示为标准区间向量。

第二步是 BMPPT 定义。对每个离散时刻，在独立标准空间中分别搜索 lower BMPP 和 upper BMPP，它们随时间形成 lower/upper BMPPT。BMPP 搜索本身是两层嵌套优化：内层处理区间分析，外层搜索 bound MPP；作者用 sequential single-loop（SSL）求解。

第三步是 active learning Kriging。先在少量均匀时间点搜索 LBMPP/UBMPP，构造初始训练集；随后用学习函数识别误差最大的时间点，补充 BMPP 搜索，直到误差阈值满足。

第四步是概率估计。基于近似 BMPPT 对上下界极限状态函数线性化，得到 HL(t)、HU(t) 两个 Gaussian processes；通过 EOLE 和 MCS 估计 `[PLf, PUf]`。

关键参数包括初始时间点数、Kriging 误差阈值、离散时间点数、EOLE 截断、MCS 样本数、区间变量采样数。复现需要详细表格和公式，txt 中多处需 PDF 复核。

## 9. 证据系统与 Claim-Evidence 表

证据系统特别可靠性工程化：每个例子都给失效概率上下界、相对误差、BMPP 搜索数、原函数评估次数，与 MCS/TDHTRA 对照。它直接服务于“准确且高效”的 claim。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| HABMPPT 能准确求解 corroded steel beam HTRA | 4.1、Fig. 6、Table 3 | 下/上失效概率约 5.252e-2 和 3.853e-1，相对误差约 0.57%/2.33%，仅 8 次 BMPP 搜索 | 强 | 表格和例子编号需 PDF 复核 |
| HABMPPT 对 10-bar truss 保持高精度且更高效 | 4.2、Fig. 8、Table 5 | 相对误差约 4.72%/3.17%，NFE 2690，远低于 TDHTRA | 强 | 非线性程度和有限元计算细节需复核 |
| solid rocket engine shell 工程应用中效率显著 | 4.3、Fig. 10、Table 7 | HABMPPT 相对误差约 3.70%/0.71%，仅 8 次 BMPP 搜索、944 FEs | 强 | 使用响应面/模型简化，需复核工程真实性 |
| rocket inter-stage structure 中 HABMPPT 与 MCS 曲线吻合 | 4.4、Fig. 12、Table 10 | 下/上失效概率约 1.128e-3 和 5.134e-3，误差 2.27%/2.91%，平均 16.4 BMPP 搜索 | 强 | BPNN 替代有限元最大应力，代理误差需计入 |
| active learning Kriging 可大幅减少 BMPP 搜索 | 方法与四例结果 | 相比 TDHTRA 每个时间点搜索，HABMPPT 通常少于十分之一 FEs | 强 | 若 BMPPT 不光滑，主动学习可能需要更多样本 |
| BMPPT 线性化可将 HTRA 转化为两个 Gaussian processes | 3.3-3.4 | 理论推导和流程 Table 1 | 中强 | FORM 线性化在强非线性边界下风险较高 |

## 10. 图表、公式与结果叙事提取

| 图表/公式 | 论证功能 | 对应 claim | 关键发现 | 复核说明 |
| --- | --- | --- | --- | --- |
| Eq. (1)-(12) | 定义 TRA/HTRA 与 MCS 直接解 | 问题形式清楚 | 随机/区间/过程输入导致失效概率上下界 | 公式需 PDF 复核 |
| Fig. 1 | MPPT 示意 | 从 MPP 轨迹引出 BMPPT | MPP 在标准正态空间随时间移动 | 需要 PDF 图像复核 |
| Fig. 2 | limit-state strip | 区间不确定性形成上下界带 | HTRA 不是单一极限状态面 | 需要 PDF 图像复核 |
| Fig. 3 | SSL 求 LBMPP 流程 | BMPP 搜索可执行 | 两层嵌套优化转单循环 | 需要 PDF 图像复核 |
| Fig. 4/Table 1 | HABMPPT 总流程 | 方法可复现 | 初始采样、Kriging 更新、线性化、MCS 估计 | 需要 PDF/表格复核 |
| Fig. 5-6/Table 2-3 | 腐蚀梁算例 | 准确性/效率 | HABMPPT 近似 MCS 且少量 BMPP 搜索 | 需要 PDF 图像复核 |
| Fig. 7-8/Table 4-5 | 10-bar truss | 中等复杂结构验证 | 相对误差小于 5%，NFE 大幅下降 | 需要 PDF 复核 |
| Fig. 10/Table 6-7 | 固体火箭发动机壳体 | 航天工程应用 | 与 MCS/TDHTRA 接近，FEs 极少 | 需要 PDF 复核 |
| Fig. 11-12/Table 8-10 | 级间段结构 | 有限元/代理工程应用 | BPNN 应力模型 + HTRA 估计，误差约 3% 内 | 需要 PDF 复核 |

## 11. 章节结构与篇章布局

真实结构大致为：1 Introduction；2 Problem statement and direct solution method for HTRA；3 The proposed method，含 BMPPT definition、approximation、linearization、failure probability estimation、implementation；4 Examples and discussions，含 corroded steel beam、10-bar truss、solid rocket engine shell、rocket inter-stage structure；5 Conclusion。

结构非常标准且有教学感。Section 2 先把 conventional TRA 和 HTRA 公式化，顺便说明 MCS 直接解为何贵。Section 3 分五个小节逐步从概念到算法。Section 4 按“简单数值例 → 桁架 → 火箭发动机壳体 → 级间段结构”逐渐提高工程复杂度。Conclusion 用三条结论和未来工作收束。

标题命名偏问题-方法型，信息量高。最值得模仿的是 “Definition of the bound-most-probable point trajectory” 和 “Linearization of the bound of limit-state function”，标题直接对应创新链条。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 Problem statement and direct solution method for HTRA（方法/模型/算法）
  - L3 p.3: 2.1 Time-variant reliability analysis problems（问题定义）
  - L3 p.3: 2.2 Direct solution method for HTRA based on MCS（方法/模型/算法）
- L2 p.4: 3 The proposed method（方法/模型/算法）
  - L3 p.4: 3.1 Definition of the bound-most-probable point trajectory（对象/模块/过渡章节）
  - L3 p.4: 3.2 Approximation of the bound-most-probable point trajectory（对象/模块/过渡章节）
  - L3 p.5: 3.3 Linearization of the bound of limit-state function（对象/模块/过渡章节）
  - L3 p.6: 3.4 Estimation of time-variant failure probability using MCS（对象/模块/过渡章节）
  - L3 p.6: 3.5 The implementation procedure of the HABMPPT（对象/模块/过渡章节）
- L2 p.6: 4 Examples and discussions（结果/验证/讨论）
  - L3 p.7: 4.1 A corroded steel beam（对象/模块/过渡章节）
  - L3 p.7: 4.2 A 10-bar truss（对象/模块/过渡章节）
  - L3 p.9: 4.3 A solid rocket engine shell structure（对象/模块/过渡章节）
  - L3 p.10: 4.4 A rocket inter-stage structure（对象/模块/过渡章节）
- L2 p.12: 5 Conclusion（结论/贡献回收）
- L2 p.12: Declaration of competing interest（尾部材料）
- L2 p.12: Data availability（尾部材料）
- L2 p.13: Acknowledgments（尾部材料）
- L2 p.13: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Problem statement and direct solution method for HTRA | 3 | 2 | 方法/模型/算法 |
| 2.1 Time-variant reliability analysis problems | 3 | 3 | 问题定义 |
| 2.2 Direct solution method for HTRA based on MCS | 3 | 3 | 方法/模型/算法 |
| 3 The proposed method | 4 | 2 | 方法/模型/算法 |
| 3.1 Definition of the bound-most-probable point trajectory | 4 | 3 | 对象/模块/过渡章节 |
| 3.2 Approximation of the bound-most-probable point trajectory | 4 | 3 | 对象/模块/过渡章节 |
| 3.3 Linearization of the bound of limit-state function | 5 | 3 | 对象/模块/过渡章节 |
| 3.4 Estimation of time-variant failure probability using MCS | 6 | 3 | 对象/模块/过渡章节 |
| 3.5 The implementation procedure of the HABMPPT | 6 | 3 | 对象/模块/过渡章节 |
| 4 Examples and discussions | 6 | 2 | 结果/验证/讨论 |
| 4.1 A corroded steel beam | 7 | 3 | 对象/模块/过渡章节 |
| 4.2 A 10-bar truss | 7 | 3 | 对象/模块/过渡章节 |
| 4.3 A solid rocket engine shell structure | 9 | 3 | 对象/模块/过渡章节 |
| 4.4 A rocket inter-stage structure | 10 | 3 | 对象/模块/过渡章节 |
| 5 Conclusion | 12 | 2 | 结论/贡献回收 |
| Declaration of competing interest | 12 | 2 | 尾部材料 |
| Data availability | 12 | 2 | 尾部材料 |
| Acknowledgments | 13 | 2 | 尾部材料 |
| References | 13 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 第一段定义 reliability 和 TRA 必要性，第二段按 extreme value/first passage 分类，第三段引出 aleatory/epistemic，第四段聚焦 HTRA 缺口并列贡献。节奏是“领域框架 → 方法分类 → 新问题 → 本文贡献”。

方法段落非常递进：先讲传统 MPP，再扩展到 BMPP；先讲精确搜索，再讲近似轨迹；先讲线性化，再讲 Gaussian process 和 MCS。每一步都以“为了减少计算”作为隐含主线。

算例段落固定模板：介绍结构与极限状态函数 → 给变量概率/区间特性表 → 说明 MCS/TDHTRA/HABMPPT 设置 → 展示曲线 → 用表格比较效率与误差。这个模板可直接复用到可靠性方法论文。

## 13. 文笔画像与语言习惯

整体语气是可靠性方法型，常用 time-variant reliability、hybrid uncertainties、interval process、limit-state function、most-probable point、active learning Kriging、failure probability。claim 强度较强但有明确边界，例如 “high accuracy and efficiency”“typically smaller than 5%”“acceptable for engineering problems”。

主动语态用于贡献：“we propose”“we develop”“we use”；被动语态用于算法过程：“is transformed”“is linearized”“is estimated”。时态上，方法定义用现在时，文献回顾用过去/现在完成，结果解释用现在时配合表图。

常用限定词包括 generally、typically、efficiently、accurately、excessively、significantly。学术名词高度技术化，适合 Probabilistic Engineering Mechanics 的方法读者。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：45569
- 高频词：interval(73)；time(70)；mpp(67)；method(62)；function(56)；time-variant(52)；process(40)；variables(39)；limit-state(34)；instants(34)；failure(34)；probability(31)；htra(29)；reliability(28)；bmppt(28)；samples(27)；uncertainties(26)；model(25)；habmppt(24)；structure(22)
- 高频名词化/学术名词：function(56)；failure(34)；probability(31)；reliability(28)；structure(22)；pressure(8)；expansion(7)；autocorrelation(7)；procedure(7)；estimation(6)；characteristics(6)；combustion(6)；measure(5)；approximation(5)；discretization(5)
- 高频学术动词：estimate(12)；developed(10)；estimated(9)；construct(7)；evaluate(6)；constructed(4)；propose(3)；achieve(3)；develop(2)；compared(2)；reveal(1)；provide(1)；presented(1)；provided(1)；identified(1)
- 高频形容词：interval(73)；time-variant(52)；stochastic(20)；active(16)；normal(16)；variable(13)；epistemic(12)；initial(12)；equidistant(11)；instant(8)；coefficient(8)；efficient(7)；independent(7)；deterministic(7)；computational(6)
- 高频副词：directly(8)；efficiently(8)；tively(5)；widely(4)；uniformly(4)；effectively(3)；evenly(3)；recently(2)；generally(2)；finally(2)；accurately(2)；significantly(2)；accordingly(2)；similarly(2)；successfully(1)
- 高频二词短语：time instants(34)；limit-state function(30)；failure probability(25)；interval process(19)；time-variant reliability(18)；discrete time(16)；active learning(16)；lower upper(13)；epistemic uncertainties(12)；reliability analysis(11)；time-variant limit-state(11)；upper bounds(11)
- 高频三词短语：discrete time instants(12)；lower upper bounds(11)；time-variant failure probability(10)；time-variant reliability analysis(9)；time-variant limit-state function(9)；failure probability estimated(9)；equidistant time instants(9)；active learning kriging(8)；time-variant epistemic uncertainties(6)；interval process variables(6)；initial training samples(6)；bounds limit-state function(6)
- 被动语态估计：166；`we + 动作动词` 主动句估计：9
- 一般现在时线索：224；一般过去时线索：347；现在完成时线索：0；情态动词线索：60

分章节正文词频：

- 1 Introduction: method(31)；time-variant(26)；uncertainties(22)；reliability(18)；out-crossing(16)；interval(15)；tra(14)；function(14)
- 2 Problem statement and direct solution method for HTRA: interval(12)；variables(11)；time-variant(8)；function(8)；method(7)；max(7)；mcs(6)；processes(5)
- 3 The proposed method: mpp(55)；function(18)；time(17)；model(14)；step(13)；samples(11)；instants(10)；interval(10)
- 4 Examples and discussions: time(33)；interval(31)；process(18)；tdhtra(17)；structure(16)；function(15)；habmppt(14)；instants(14)
- 5 Conclusion: bmppt(8)；variables(7)；htra(6)；efficiently(5)；interval(5)；process(5)；time(5)；method(4)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

高频术语：time-variant reliability analysis、hybrid uncertainties、interval process、limit-state function、failure probability、BMPP、BMPPT、active learning Kriging、Gaussian process、MCS、TDHTRA。

可复用背景句：`Lacking in information or data, some uncertainties cannot be directly quantified as stochastic models.`

可复用 gap 句：`The existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.`

可复用贡献句：`We propose the concept of X, which is defined as the moving trajectory of Y in the independent standard normal space varying with time.`

可复用方法句：`Based on time discretization, the problem is transformed into a time-independent series-system reliability problem.`

可复用结果句：`The relative errors compared with MCS are typically smaller than X%, which is acceptable for engineering problems.`

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Compared with the TDHTRA which directly searches BMPPs at all discrete time instants, the HABMPPT requires less than one-tenth number of FEs needed by the TDHTRA with similar accuracy in estimating the failure probability. (3) The results of four examples show that, for the HABMPPT, the relative errors compared with MCS are typically smaller than 5 % which is acceptable for engineering problems.
  可迁移模板：Compared with the METHOD which directly searches BMPPs at all discrete time instants, the METHOD requires less than one-tenth number of FEs needed by the METHOD with similar accuracy in estimating the failure probability. (X) The results of four examples show that, for the METHOD, the relative errors compared with METHOD are typically smaller than X which is acceptable for engineering problems.
#### Gap/转折句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  可迁移模板：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures.
  可迁移模板：In the past few decades, many static reliability analysis methods [X–X] have been widely developed to measure the safety of structures.
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  可迁移模板：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
  可迁移模板：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
- 原句：However, research about TRA with hybrid uncertainties has been rarely performed.
  可迁移模板：However, research about METHOD with hybrid uncertainties has been rarely performed.
#### 方法提出句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  可迁移模板：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties.
  可迁移模板：In general, stochastic and interval models are respectively used to describe aleatory and epistemic uncertainties.
- 原句：For the hybrid TRA (HTRA) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
  可迁移模板：For the hybrid METHOD (METHOD) problem considering the two kinds of uncertainties, the existing method needs to excessively evaluate the original time-variant limit-state function, which is too expensive for engineering problems.
- 原句：To address this issue, we propose the concept of bound-most-probable point trajectory (BMPPT) which can be used to construct the approximation of the limit-state hyper-surface.
  可迁移模板：To address this issue, we propose the concept of bound-most-probable point trajectory (METHOD) which can be used to construct the approximation of the limit-state hyper-surface.
- 原句：Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency.
  可迁移模板：Moreover, we develop a METHOD method based on approximating METHOD which can further improve the computational ef ficiency.
#### 结果呈现句
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  可迁移模板：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
  可迁移模板：Two numerical examples including a cantilever beam, and a X-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed METHOD problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
- 原句：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
  可迁移模板：Lacking in information or data, some uncertainties cannot be directly quan tified as stochastic models, which results in the simultaneous existence of aleatory and epistemic uncertainties in most of problems.
- 原句：Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
  可迁移模板：Two numerical examples including a cantilever beam, and a X-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed METHOD problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
- 原句：To achieve time-variant reli ability with acceptable accuracy, the TDTRA methods introduced above should directly perform the FORM or MPP searches at numerous discrete time instants, which is computationally expensive.
  可迁移模板：To achieve time-variant reli ability with acceptable accuracy, the METHOD methods introduced above should directly perform the METHOD or METHOD searches at numerous discrete time instants, which is computationally expensive.
#### 贡献/增量句
- 原句：Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency.
  可迁移模板：Moreover, we develop a METHOD method based on approximating METHOD which can further improve the computational ef ficiency.
- 原句：Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
  可迁移模板：Two numerical examples including a cantilever beam, and a X-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed METHOD problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
- 原句：Simulation-based methods, such as Monte Carlo simulation (MCS) and importance sampling method [9], provide an alternative but expensive way to estimate the extreme value distri bution.
  可迁移模板：Simulation-based methods, such as Monte Carlo simulation (METHOD) and importance sampling method [X], provide an alternative but expensive way to estimate the extreme value distri bution.
- 原句：Moreover, we develop a HTRA method based on approximating BMPPT which can further improve the computational ef ficiency.
  可迁移模板：Moreover, we develop a METHOD method based on approximating METHOD which can further improve the computational ef ficiency.
- 原句：Two numerical examples including a cantilever beam, and a 10-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed method can solve the HTRA problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
  可迁移模板：Two numerical examples including a cantilever beam, and a X-bar truss, and two engineering applications of the solid rocket engine shell and the rocket inter-stage structure are investigated, and the results reveal that the proposed METHOD problems with high ac curacy and efficiency. failure probability is estimated by calculating the extreme value distri bution of the limit-state function.
#### 限制/边界句
- 原句：Based on whether or not the out-crossing rate should be calculated, the first passage-based method can be classified into two types: the out-crossing rate method and the time discretization-based TRA (TDTRA) method.
  可迁移模板：Based on whether or not the out-crossing rate should be calculated, the first passage-based method can be classified into two types: the out-crossing rate method and the time discretization-based METHOD (METHOD) method.
- 原句：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
  可迁移模板：However, those out-crossing rate methods may lead to large errors for the problems where out-crossing events are strongly dependent.
- 原句：To achieve time-variant reli ability with acceptable accuracy, the TDTRA methods introduced above should directly perform the FORM or MPP searches at numerous discrete time instants, which is computationally expensive.
  可迁移模板：To achieve time-variant reli ability with acceptable accuracy, the METHOD methods introduced above should directly perform the METHOD or METHOD searches at numerous discrete time instants, which is computationally expensive.
- 原句：The two categories of TRA methods mentioned above are based on probabilistic theory and can only solve problems with aleatory uncertainties.
  可迁移模板：The two categories of METHOD methods mentioned above are based on probabilistic theory and can only solve problems with aleatory uncertainties.
- 原句：In this situation, uncertain factors could be described as non-probabilistic interval variables [31].
  可迁移模板：In this situation, uncertain factors could be described as non-probabilistic interval variables [X].
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略层级清晰。第一层引用 static reliability 与 TRA 基础文献，建立领域合法性；第二层引用 extreme value、first passage、PHI2、TRPD、NEWREL、MPPT 等方法，说明时间维度处理方式；第三层引用 aleatory/epistemic、interval variables、interval processes 和 hybrid reliability；第四层引用 Kriging/active learning/surrogate 相关方法。

作者对前人姿态以继承和扩展为主。对 TDTRA/MPPT 是继承：它们证明离散时间和 MPP 轨迹有用；对已有 HTRA 是补充：它们考虑混合不确定性，但 time-variant interval processes 或复杂工程高维输入下效率不足。

引用风险较小，但若要进一步强化，应比较更多 active learning reliability 方法和非 FORM 的时变可靠性方法，尤其是多设计点、非高斯过程和非光滑极限状态边界。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：96
- Introduction 引文簇数量估计：29
- References 条目数：48
- 可识别年份条目数：71
- 2021 年及以后文献数：18
- 2010 年前经典文献数：14
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Probabilistic Engineering Mechanics(1)
- 引文簇样例：[9], [1,2], [10,11], [12,13], [6], [14], [15], [16], [7,8], [31], [17,18], [19]

带引文的 gap/转折句样例：

- In the past few decades, many static reliability analysis methods [3–5] have been widely developed to measure the safety of structures.
- Time-variant uncertainties encountered in practical engineering [6], such as dynamic load and strength degradation, cannot be handled by those static methods.

References 解析样例（前 8 条）：

- [1] A. Singh, Z.P. Mourelatos, J. Li, Design for lifecycle cost using time-dependent reliability, J. Mech. Des. 132 (9) (2010), 091008, https://doi.org/10.1115/ 1.4002200.
- [2] Z. Meng, J. Zhao, C. Jiang, An efficient semi-analytical extreme value method for time-variant reliability analysis, Struct. Multidiscip. Optim. 64 (3) (2021) 1469–1480, https://doi.org/10.1007/s00158-021-02934-y.
- [3] H. Pang, T. Yu, B. Song, Failure mechanism analysis and reliability assessment of an aircraft slat, Eng. Fail. Anal. 60 (2016) 261–279, https://doi.org/10.1016/j. engfailanal.2015.11.032.
- [4] Z. Sun, J. Wang, R. Li, C. Tong, LIF: a new Kriging based learning function and its application to structural reliability analysis, Reliab. Eng. Syst. Saf. 157 (2017) 152–165, https://doi.org/10.1016/j.ress.2016.09.00.
- [5] G. Li, B. Li, H. Hu, A novel first–order reliability method based on performance measure approach for highly nonlinear problems, Struct. Multidiscip. Optim. 57 (4) (2018) 1593–1610, https://doi.org/10.1007/s00158-017-1830-1.
- [6] M. Di Paola, L. Galuppi, G. Royer Carfagni, Fractional viscoelastic characterization of laminated glass beams under time-varying loading, Int. J. Mech. Sci. 196 (2021), 106274, https://doi.org/10.1016/j.ijmecsci.2021.106274.
- [7] Z. Hu, X. Du, A sampling approach to extreme value distribution for timedependent reliability analysis, J. Mech. Des. 135 (7) (2013), 071003, https://doi. org/10.1115/1.4023925.
- [8] Z. Wang, P. Wang, A nested extreme response surface approach for time-dependent reliability-based design optimization, J. Mech. Des. 134 (12) (2012), 121007, https://doi.org/10.1115/1.4007931.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. FORM/BMPP 线性化可能低估强非线性、多失效域或多设计点问题的失效概率。
2. BMPPT 若不光滑或存在跳变，Kriging 近似轨迹可能失效，作者也在未来工作中承认。
3. 区间过程 K-L 展开截断项和自相关函数选择会影响结果，但敏感性分析不够显式。
4. 工程算例中使用响应面或 BPNN 替代部分复杂分析，代理误差是否计入可靠性结果需要复核。
5. MCS 基准自身对区间分析采用有限样本，可能不是严格“真值”。
6. 对 correlated uncertainties 的处理仍是未来工作，当前方法假设可能限制应用范围。

## 17. 可复用资产

可复用选题套路：把高维函数近似难题转为低维关键轨迹近似，形成“换近似对象”的方法创新。

可复用论证链：传统 TRA → 混合不确定性 → interval process → 直接 HTRA 成本高 → 定义关键轨迹 → 主动学习近似 → 线性化为 Gaussian processes → 四个算例验证。

可复用图表：MPPT/BMPPT 概念图；limit-state strip 示意；SSL 搜索流程图；总算法流程表；每个算例的结构图、失效概率曲线和效率/误差表。

可复用指标：NBMPP、NFE、PLf/PUf、relative error、failure probability curve。可靠性方法论文一定要同时报告精度和函数评估次数。

## 18. 对我写论文的启发

这篇论文最值得学的是“概念命名 + 算法流程 + 多例验证”的组合。BMPPT 这个命名把方法贡献压缩成一个可传播的对象，随后所有推导都围绕它展开。

如果自己写方法论文，可以学习它的验证梯度：先简单数值例验证准确性，再中等结构例验证复杂度，最后工程例证明应用价值。每个例子用相同表格模板比较 MCS/基准/本文方法，读者很容易扫描。

需要避免的是对基准“真值”的过度依赖。若 MCS 或 TDHTRA 本身也用近似，最好说明误差来源和计算设置，并进行重复实验。

## 19. 最终浓缩

本文最值得学的是：不去全局逼近复杂 HTRA 极限状态函数，而是近似 bound-most-probable point trajectory，并通过主动学习大幅减少 BMPP 搜索。

最大风险是：方法依赖轨迹平滑性和 FORM 线性化，对非光滑、多失效域、强非线性问题需要谨慎。

可迁移的三件事：一是用“关键轨迹”替代“全函数”作为近似对象；二是用 NBMPP/NFE/误差表同时证明效率和精度；三是用从数值例到工程例的阶梯式验证增强可信度。
