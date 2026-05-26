# Weight-adaptive parameter estimation assisted event-triggered model predictive guidance for reentry 深度拆解

## 0. 读取说明

本拆解基于 `801/文本/txt/Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science.txt` 的 PyMuPDF 全文抽取结果完成。抽取文本为双栏论文，部分位置存在左右栏交错，尤其是公式、图注和正文并排处；因此本文对模型、公式和图表功能的判断以抽取出的章节文字、图表标题、表格数值和作者解释为主。涉及曲线形态、图中颜色、局部约束穿越位置、参数估计散点分布等视觉细节，均标注为需要 PDF 图像复核。

这篇论文属于航空航天制导控制方法论文。它不是在提出全新的飞行动力学模型，而是在已有非线性模型预测制导（NMPG）和事件触发思想基础上，加入在线模型参数估计，解决再入飞行中“模型偏差导致制导触发过密、在线轨迹优化不可行、路径约束难以保持”的工程问题。拆解重点放在：作者如何制造 gap，如何把 WAPE 嵌入 ET-NMPG，如何用仿真证据把“精度、计算资源、约束安全”三者连接起来。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 Problem formulation, 3 The ET-NMPG method, 4 WAPE and change point detection, 5 The guidance framework, 6 Simulation results and discussion, 7 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 标题：Weight-adaptive parameter estimation assisted event-triggered model predictive guidance for reentry
- 作者：Tengfei Zhang, Licong Zhang, Chunlin Gong, Songyu Liu, Hua Su
- 机构：西北工业大学航天学院陕西省航天飞行器设计重点实验室；上海机电工程研究所
- 期刊：Aerospace Science and Technology, Volume 158, 2025, Article 109938
- 时间线：Received 2024-09-02; revised 2024-12-26; accepted 2025-01-05; online 2025-01-10
- 关键词：Event-triggered; Model predictive guidance; Online trajectory optimization; Weight-adaptive; Parameter estimation
- 研究对象：无动力翼身/翼面再入飞行器的再入制导过程，状态包括半径/高度、经纬度、速度、航迹角、航向角，控制量为攻角和倾侧角。
- 论文类型：方法型 + 数值仿真验证型。主体贡献是制导框架和在线参数估计机制，不是实飞数据论文。
- 方法组合：再入运动模型、在线轨迹优化 TOP、非线性模型预测制导 NMPG、事件触发机制 ET-NMPG、权重自适应参数估计 WAPE、突变点检测、Monte Carlo 仿真。
- 主要证据：典型工况对比、300 组 Latin Hypercube Monte Carlo、32 组飞行中参数突变样本、关键指标表格（制导次数、计算时间、成功率、终端误差）。
- 目标读者：再入制导、在线轨迹优化、模型预测控制、航天飞行器 GNC 方法研究者。

论文身份可以概括为：一篇面向工程可用性的模型预测制导改进论文。它的“卖点”不是让 TOP 求得更快，而是让 NMPG 在模型偏差和路径约束压力下少触发、少失败、仍保持精度。换言之，它将制导问题从单纯的在线优化问题，改写成“在线优化 + 触发调度 + 模型校正 + 数据筛选”的闭环计算框架。

## 2. 摘要与核心信息提取

一句话主张：作者提出 WAPE-assisted ET-NMPG，通过事件触发减少不必要在线优化，通过权重自适应参数估计在线修正大气和气动模型，从而在再入制导中兼顾制导精度、计算资源和路径约束安全。

摘要的说服结构很清楚：

1. 先指出在线轨迹优化制导的基本矛盾：复杂问题中，制导精度与指令计算效率存在 trade-off。
2. 再引入事件触发：当状态偏差超过阈值才更新制导律，可以降低计算资源消耗。
3. 随即反转：真实模型参数偏离参考值时，事件触发会变得过于频繁，甚至让轨迹优化不可行。
4. 方法回应：在通用 ET-NMPG 框架中嵌入 WAPE，对模型参数在线更新。
5. 工程价值：对再入过程而言，这不仅改善精度和制导频率，还帮助飞行状态维持在可接受路径约束内。
6. 风险补丁：加入 change point detection，避免飞行中故障或参数突变导致历史数据污染。
7. 证据承诺：数值仿真确认有效性。

摘要里有两个核心信息值得复用。第一，作者没有把事件触发说成万能方案，而是主动暴露“模型偏差会诱发过高触发频率和 TOP 不可行”这一二阶问题。第二，WAPE 的价值不是孤立的估计精度，而是通过提升模型预测精度来降低制导调用频率、增强约束满足能力。这个贡献表述比“提出一种参数估计算法”更工程化，也更容易被 AST 这样的期刊接受。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/Weight-adaptive-parameter-estimation-assisted-event-t_2025_Aerospace-Science.md`。

中文译文：

> 詹兴群通讯
>
> 本文提出了一种权重自适应参数估计（WAPE）辅助的事件触发模型预测制导（ET-NM PG）方法，并将其应用于再入制导。基于在线轨迹优化（TO）的制导方法在处理复杂问题时常常面临制导精度和制导命令计算效率之间的权衡。通过将状态偏差超过阈值作为事件触发条件，可以在保证一定的制导精度的同时，有效减少计算资源消耗。然而，实际模型参数值经常偏离参考值，导致事件触发频率过高，并可能导致轨迹优化不可行。为了解决这个问题，我们建议在通用 ET-NMPG 框架内使用 WAPE 在线更新模型参数，从而提高制导精度并降低制导频率。重要的是，对于再入过程，这种方法可以进一步确保飞行状态保持在可接受的路径限制内。此外，我们设计了一个变化点检测步骤，以避免 i-flight 故障（参数突变）情况下的数据污染。数值模拟结果验证了该方法的有效性。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

选题来源是再入制导中的工程瓶颈。翼式再入飞行器要满足安全、可复用、低维护成本等目标，但无动力滑翔再入不像有动力巡航那样有充分控制余量。传统“轨迹设计 + 跟踪制导”策略通常只跟踪少数状态量，例如阻力加速度、高度、经纬度，因此在飞行中和终端会产生较大状态散布，影响安全着陆和重复使用。

作者把问题进一步压缩到在线轨迹优化制导。计算制导与控制（CG&C）正在替代传统制导，NMPG 能把在线 TOP 解作为开环制导律反复更新，理论上比固定参考轨迹跟踪更强。但 NMPG 的难点在于：每次更新都要解非线性规划，计算代价高；如果不及时更新，又会在路径约束附近失控。于是选题自然落到“何时调用 NMPG”和“用什么模型调用 NMPG”两个问题。

本文真正的切入点是第二个问题。事件触发机制已经能回答“何时调用”：状态偏差超过阈值就重新优化。但再入飞行中的大气密度、气动系数、质量等参数可能与参考模型不同，导致预测模型持续偏离真实飞行。这样事件触发会被频繁激活，NMPG 反而变成高频、低可靠的计算负担。作者据此提出：仅仅做事件触发不够，还必须把模型参数在线校正纳入框架。

选题价值有三层：

- 工程价值：减少在线优化调用次数，降低机载计算负担，同时提高再入制导成功率。
- 安全价值：在热流、动压、过载等路径约束附近，通过更准模型降低 TOP 不可行和约束越界风险。
- 方法价值：把事件触发控制、在线参数估计和非线性模型预测制导整合到一个可仿真的再入制导流程。

这个选题不是“完全新理论”，而是典型的工程方法整合型创新。它成立的关键在于作者找到一个高影响应用场景：再入飞行的不可完全控制、路径约束强、模型偏差真实存在、在线计算资源有限。只要这些条件被读者接受，WAPE-assisted ET-NMPG 就不是为了复杂而复杂，而是针对真实瓶颈的必要补丁。

## 4. 领域位置与文献版图

作者在 Introduction 中把文献版图分成几条线。

第一条线是传统再入制导。作者从航天飞机退役、翼式飞行器未来可能回归空间运输讲起，用 [1-3] 建立再入制导的重要性；随后引用传统“轨迹设计 + 跟踪制导”及相关精确再入制导文献 [4-6]，指出传统方法受欠驱动系统和有限跟踪变量约束，容易产生状态散布。

第二条线是计算制导和在线轨迹优化。作者引用 CG&C 概念 [7]，再把模型型方法 [8,9] 与数据型方法 [10-13] 分开，并明确本文聚焦前者。随后用伪谱法、SCP、MPSP 等文献 [14-23] 说明 TOP 求解效率一直是领域关注点。这一组文献为 NMPG 提供技术背景。

第三条线是 NMPG 调用策略。作者将生成在线制导命令的策略分成 UI-NMPG 和 FC-NMPG：前者上一轮优化完成后立刻下一轮，计算资源要求高；后者固定周期调用，周期、效率和精度之间存在冲突。引用 [24-26] 后，作者为事件触发策略的必要性铺垫。

第四条线是 MPC/ET-MPC。作者把 NMPG 视为 MPC 的特殊应用，引用 MPC 基础 [27] 和事件触发控制综述/应用 [28-32]，再用自己团队此前的 ascent guidance ET-NMPG 工作 [33] 表明事件触发 NMPG 已有基础，但尚未解决再入路径约束和模型偏差耦合问题。

第五条线是在线模型识别与参数估计。作者引用 Morelli and Klein [34] 作为模型参数估计基础，再列举 F-16 气动参数估计 [35,36] 和小行星轨迹/参数估计 [37]。文献姿态比较谨慎：这些工作证明在线估计有价值，但不能直接解决高超声速再入中实时数据有限、噪声大、气动模型强非线性的问题。

文献版图的总体策略是“横向嫁接 + 纵向补缺”：从 MPC 借事件触发，从飞行试验参数估计借在线 PE，从再入制导问题中提出路径约束和模型偏差的特定矛盾。本文的位置是：继承 ET-NMPG，但补上模型参数偏差下的在线估计和故障突变数据处理。

## 5. Gap 制造机制

本文的 gap 是多层制造的，不是单句“previous studies did not...”。它先制造工程 gap，再制造方法 gap，最后制造数据/鲁棒性 gap。

第一层 gap：传统再入轨迹跟踪制导无法充分抑制状态散布。作者强调再入飞行器欠驱动，只能选择少量状态变量跟踪，终端状态散布会影响安全着陆和可复用性。这一层让读者接受“不能只靠传统 FLG”。

第二层 gap：NMPG 虽然可用在线 TOP 生成更优制导律，但 UI-NMPG 与 FC-NMPG 都有问题。UI-NMPG 计算资源消耗大，FC-NMPG 受固定周期限制，在路径约束附近不能及时更新。这个 gap 推出 ET-NMPG。

第三层 gap：ET-NMPG 仍然依赖参考模型。真实飞行中大气密度、气动系数、质量等参数偏离参考值时，模型预测误差会使状态偏差持续超过阈值，触发频率升高；更严重的是，当前状态可能已在路径约束边界外，使 TOP 初始化不可行。这个 gap 推出 WAPE。

第四层 gap：直接最小二乘估计在数据少、噪声大、气动非线性强时会给出不合理参数。尤其再入轨迹上的速度/攻角覆盖有限，样本点可能接近平行某个坐标轴，导致某些气动参数不可辨或弱可辨。这个 gap 推出“权重自适应”而不是普通 LS。

第五层 gap：如果飞行中参数突变，继续混用突变前后的历史数据会污染估计。这个 gap 推出 change point detection。

这个 gap 制造机制很值得学习：作者不是只说“已有 ET-NMPG 没有参数估计”，而是把每个新模块都绑定一个失败模式。事件触发对应高频在线优化；WAPE 对应模型偏差；权重对应少数据和噪声；突变点检测对应故障数据污染。每个模块都有自己的必要性。

## 6. 创新性判断

作者声明的核心创新包括：WAPE-assisted ET-NMPG 再入制导框架、在线估计大气和气动模型参数、权重自适应最小二乘、参数突变检测、与 FLG/FC-NMPG/ET-NMPG 的系统仿真对比。

真实创新强度可以分层判断：

- 框架创新：中等偏强。把 WAPE 嵌入 ET-NMPG 并服务于再入路径约束，是本文最有工程说服力的创新。
- 算法创新：中等。WAPE 本质是带基准参数惩罚项和数据量/覆盖度权重的增强最小二乘，不是全新估计理论，但针对再入气动参数弱可辨识问题做了有效工程设计。
- 问题创新：中等。模型偏差导致 ET-NMPG 触发过密和 TOP 不可行，这个问题定义比较具体，且紧扣再入路径约束。
- 证据创新：中等偏强。作者不只给单一算例，还给 300 组 Monte Carlo 和 32 组 in-flight fault 样本，这让贡献从“示例有效”提升为“统计上更可靠”。
- 理论创新：偏弱。论文没有给出闭环稳定性、递归可行性或估计收敛性的严格证明；主要依赖数值仿真。

最值得肯定的是贡献表达的节制。作者没有声称 WAPE 能精确估计所有气动参数，反而明确指出 CL2,3 和 CD2,3 难以早期准确估计，但它们对模型影响低于 CL0,1 和 CD0,1，只要主要参数被修正，制导仍可显著改善。这个处理降低了审稿人对“估计精度”单点攻击的强度。

可能被挑战的创新点是：事件触发 + 参数估计 + MPC 的组合在控制领域并不罕见，本文新意主要来自再入 NMPG 应用和 WAPE 权重设计。如果审稿人要求理论深度，本文会显得更像工程集成；如果期刊重视 AST 的工程仿真和制导应用，则这个创新强度足够。

## 7. 论证链条复原

整篇论文的论证链可以还原为：

空间运输和翼式飞行器复用需求 -> 再入制导是可靠性和安全性的关键 -> 传统轨迹跟踪对欠驱动再入系统控制余量不足 -> 在线 TOP/NMPG 能提高制导能力 -> 但 NMPG 计算代价和更新时机存在矛盾 -> 事件触发可以减少不必要更新 -> 然而模型参数偏差会导致事件触发频繁、路径约束失守、TOP 不可行 -> 因此需要在线参数估计修正模型 -> 直接 LS 在少数据、噪声和强非线性下不稳 -> 因此需要权重自适应估计，并在故障突变时剔除污染数据 -> 将 WAPE 嵌入 ET-NMPG 后，通过仿真证明制导次数减少、成功率提高、终端误差降低、路径约束更可控。

论证中的关键闭环是“模型预测精度 -> TOP 可行性 -> 制导调用频率 -> 飞行安全”。作者没有把参数估计作为独立任务来证明，而是把估计结果放回制导流程中，用成功率、制导次数、计算时间和终端误差来评价。这是方法论文很重要的一点：中间模块的好坏最终要由任务指标验证。

最薄弱环节在于“模型偏差的真实代表性”。论文使用随机正弦叠加扰动、参数偏差区间、Latin Hypercube 样本来构造环境，但这些是否充分代表真实再入飞行不完全可证。作者在结论里也承认未来需要考虑实际飞行过程中的各种偏差来源、阈值选择和 robust NMPG，这相当于主动收束了外推范围。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation. On this basis, the method for selecting the event-triggered threshold and the potential need for introducing robust NMPG should be explored in more detail.
- 已有研究不足/GAP：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible. Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints. However, people believe that as technology contin ues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
- 本文解决方式：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance. Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems. However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 学术或工程增量：Unlike most guidance methods based on online optimization (i.e., NMPG) that use time-triggered strategies, the ET-NMPG with an event-triggered mechanism achieves a better balance between guidance accuracy and computational resource consumption. Building on this, we incorporated a parameter estimation step into the ET-NMPG pro cess to improve model prediction accuracy, thereby further reducing the number of guidance cycles, enhancing guidance precision, and ensuring flight safety. Simulation results demonstrate that WAPE-assisted ET NMPG offers greater application potential compared to existing methods such as UI-NMPG, FC-NMPG, and ET-NMPG.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

方法可以拆成六个模块。

第一，标准再入运动模型。状态为 `x=[r, theta, phi, v, gamma, psi]^T`，控制为 `u=[alpha, sigma]^T`。模型包括地球自转、重力、升力、阻力，升阻力由动压、参考面积和升阻系数决定。气动系数采用攻角和速度的参数化表达，大气密度采用指数模型。这个模块的功能是提供可优化、可预测的基准模型。

第二，真实运动与扰动模型。作者把真实模型写成参考动力学加参数偏差和动态扰动：真实参数 `Pt` 不等于基准参数 `Pb`，扰动 `Psi` 作用在速度、航迹角、航向角相关动态方程上。扰动用 20 个不同频率和相位的正弦波叠加，并按动压比例缩放。这个设定有两个功能：一是制造模型-真实系统差异，二是让扰动与气动力相关，贴近再入过程中气动扰动占主导的直觉。

第三，再入制导 TOP。基础问题 P1 以航迹角变化率平方积分最小为性能指标，约束包括动力学、初末状态和路径约束。路径约束为动压、热流和过载上限。因为真实飞行状态可能在调用 NMPG 时已接近甚至越过约束，作者把 P1 改成 P2：引入 `eta_r` 放松路径约束比例，并用大惩罚 `Kp` 抑制过度放松；同时放松终端航向角约束。这个设计直接服务于 TOP 可行性。

第四，ET-NMPG 触发机制。作者定义状态误差 `epsilon_x` 为实际状态与参考状态差异，定义事件函数 `ET=min(sigma-epsilon_x)`。当 `ET<=0` 时，说明至少一个状态误差超过阈值，触发 NMPG 更新开环制导律和参考轨迹；否则继续使用当前制导律。这个机制把周期调用变成偏差驱动调用。

第五，在线优化求解技巧。作者区分 MRTO 和 FSTO：MRTO 使用 hp-adaptive mesh refinement，FSTO 使用固定网格单步优化。只有当实际初始状态偏离离线参考轨迹或主要模型参数变化时调用 MRTO，其他情况使用 FSTO。作者还使用 mesh truncation、mesh reduction 和初值插值，并在 NMPG 前预测计算延迟期间的状态，以缓解“优化结果出来时实际状态已经变了”的问题。

第六，WAPE 与突变点检测。大气参数通过对数形式的最小二乘估计 `rho0` 和 `beta`。气动参数估计更复杂：由于加速度由气动力和质量共同决定，气动系数和质量不可同时唯一估计，作者转而使用相对气动参数/“气动加速度系数”。随后构造增强最小二乘目标：一部分拟合加速度残差，一部分惩罚参数相对基准值的偏离。权重由数据量和样本覆盖范围决定：数据少时更相信基准模型，数据多且攻角/速度覆盖充分时更相信 LS 估计。突变点检测通过模型相似性序列 `Upsilon_P` 的 range 阈值识别突变，再用残差函数定位突变点，丢弃突变前数据。

这个方法的工程逻辑是“先保守，后放开”。数据不足时不急于改模型；数据充分时允许参数远离基准；发现突变时不让旧数据拖累新估计。它比普通在线估计更适合安全敏感的再入制导。

## 9. 证据系统与 Claim-Evidence 表

本文证据系统由三层构成：典型算例说明机制，Monte Carlo 证明统计收益，飞行中故障场景验证突变检测和 WAPE 适应能力。作者把证据指标分成四类：路径/轨迹曲线、制导命令曲线、参数估计曲线、统计表格。表格承担强 claim，曲线承担机制解释。

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| 传统 FLG 在存在较大初始偏差时难以准确跟踪优化参考轨迹，而 NMPG 类方法能达到目标终端状态 | Section 6.1; Fig. 5; Fig. 6 | 无偏差与有初始偏差两个样例，FLG 在大初始偏差下失败，三类 NMPG 轨迹相近并达到终端目标 | 中等；典型样例直观 | 需要 PDF 图像复核轨迹细节；样例数量有限 |
| FC-NMPG 固定周期更新会在路径约束附近更新不及时，ET-NMPG 更能防止状态越界 | Section 6.1; Fig. 7 | 动态扰动样例中，FC-NMPG 因未及时更新导致违反约束而失败，ET-NMPG 更好维持路径约束 | 中等；机制和曲线对应 | FC 周期取 30 s，是否公平需讨论 |
| 模型参数偏差大时，单纯 ET-NMPG 仍可能 TOP 多次失败；加入 WAPE 后飞行状态可保持在放松边界内且触发间隔变长 | Section 6.1; Fig. 8-10 | 具有初始偏差、参数偏差、扰动的样例，WAPE-assisted ET-NMPG 轨迹和制导命令更平稳，参数更新后事件触发间隔较长 | 较强；直接对应核心机制 | “可接受路径约束”依赖 eta_r 放松，需 PDF 图像复核越界位置 |
| WAPE 能快速估计大气参数和主要气动参数，但次要指数项参数难以早期准确估计 | Section 6.1; Fig. 11; Section 6.2; Fig. 13-14 | 大气参数首轮后接近真实值；CL0,1 和 CD0,1 几次估计后收敛；CL2,3 和 CD2,3 需要低速数据，早期随机性强 | 较强；作者主动解释可辨识差异 | 估计基于仿真真实值，缺少实飞噪声验证 |
| WAPE 显著降低 ET-NMPG 的制导调用次数并提高成功率 | Section 6.2; Table 4 | 300 组样本中 FC 成功 59/300，ET 成功 134/300，WAPE-assisted ET 成功 213/300；平均制导次数 WAPE 为 13.2，ET 为 121.7 | 强；统计样本支持 | 样本分布和参数偏差区间由作者设定 |
| WAPE-assisted ET-NMPG 总体终端精度最好，尤其速度误差更小 | Section 6.2; Table 5 | WAPE 的终端速度误差最大/平均/最小为 1.234/0.113/-1.179 m/s，明显优于 FC 和 ET；角度误差也总体更小 | 强；量化表格 | 航向角约束被放松，因此该指标可比性较弱 |
| 即使 CL2,3 和 CD2,3 不能早期准确估计，只要主要参数修正合理，制导仍能满足路径约束并避免终端减速不足 | Section 6.2; Fig. 13-14 | 参数估计误差分布显示主导参数收敛快；成功率提升说明不需要所有参数都准确 | 中等偏强；推断链合理 | 这是从成功率反推参数作用，非严格因果证明 |
| 突变点检测能在飞行中参数突变时避免历史数据污染，突变时刻识别误差不超过 3 s | Section 6.3; Fig. 15-17; Table 6 | 32 组 in-flight fault 样本，突变检测均能识别，且误差不超过 3 s；主气动系数通常 100 s 内修正接近真实值 | 较强；有多样本验证 | 只有仿真突变，且本节未考虑大气密度和初始状态偏差 |

证据系统最强的位置是 Table 4 和 Table 5。Table 4 同时给出制导次数、单次计算时间、总仿真时间和成功率，避免只拿一个指标说话；Table 5 进一步用终端状态误差证明“减少调用次数”没有牺牲精度。最需要复核的是 Fig. 8-10 和 Fig. 15-17 的曲线视觉细节，因为正文对它们的解释承载了路径约束、安全边界和突变检测效果。

## 10. 图表、公式与结果叙事提取

| 图/表/公式 | 论证功能 | 对应 claim | 关键发现/作用 | 需要复核点 |
| --- | --- | --- | --- | --- |
| Fig. 1 坐标系和状态定义 | 建立再入运动变量体系 | 本文问题可被标准再入动力学表述 | 说明 `r, theta, phi, v, gamma, psi, sigma` 等变量 | 图像细节可不复核，公式变量需核对 |
| Eq. (1)-(3) | 基准动力学和气动模型 | NMPG 与 WAPE 都有共同模型基础 | 给出升阻力、动压、气动系数参数化 | 抽取文本公式有栏间交错，建议 PDF 复核 |
| Eq. (4)-(7) | 区分基准模型与真实模型 | 模型偏差和扰动是 ET-NMPG 失败来源 | `Pb` 与 `Pt` 区分；扰动由正弦叠加并按动压缩放 | 公式排版需要 PDF 复核 |
| Eq. (8) | 明确路径约束 | 再入制导不只看终端位置，还要看热流、动压、过载 | 动压、热流、过载三个约束构成安全边界 | 无 |
| Eq. (9)-(10) | 从 P1 到 P2 的可行性改造 | 缓冲约束让 NMPG 在约束附近仍可求解 | 引入 `eta_r` 和 `Kp`，放松路径和航向角约束 | P2 公式抽取交错，需 PDF 复核 |
| Eq. (11)-(12) | 定义事件触发 | 状态偏差超过阈值时才调用 NMPG | `ET<=0` 是触发标志 | 无 |
| Eq. (13)-(15) | 处理计算延迟 | 在线 TOP 求解时间会导致新制导律生效时状态已变化 | 通过预测状态作为下一次 TOP 初始状态 | 公式细节需 PDF 复核 |
| Eq. (16)-(17) | 大气参数 LS 估计 | 大气密度参数较易在线校正 | 对数化指数大气模型估计 `rho0, beta` | 无 |
| Eq. (18)-(25) | 气动参数增强 LS | 普通 LS 不稳，且质量与气动系数不可同时唯一估计 | 使用相对气动参数，并加入基准偏离惩罚项 | 公式排版高度交错，需 PDF 复核 |
| Eq. (26)-(27); Fig. 3 | 权重自适应机制 | 数据少时保守，数据多和覆盖充分时更相信估计 | `rho_lsq` 随数据量变化；权重随攻角/速度覆盖变化 | Fig. 3 曲线需 PDF 图像复核 |
| Eq. (28)-(30) | 突变点检测 | 飞行中故障需剔除突变前数据 | 用模型相似性序列和残差函数定位突变点 | 公式和阈值可复核 |
| Fig. 4 | 框架流程图 | 不同 NMPG 策略区别在调用机制 | 展示 UI/FC/ET/WAPE-assisted ET 的流程关系 | 需要 PDF 图像复核颜色和流程箭头 |
| Table 1 | 算法参数 | 复现实验设置 | 包含 `Kp=500`, 状态阈值、采样周期、`m_min=50`, `t_min=80`, `S_Upsilon=0.01` 等 | 无 |
| Table 2 | 初始/终端状态和偏差范围 | 仿真问题定义 | 初始高度 80 km，终端高度 20 km，速度从 6800 到 780 m/s 等 | 无 |
| Table 3 | 模型参数基准值与偏差 | Monte Carlo 参数空间 | 列出大气、气动、质量等偏差范围 | 无 |
| Fig. 5-7 | 方法对比曲线 | FLG/FC/ET 的基本有效性与局限 | FLG 在大偏差下失败，FC 在约束附近更新不及时，ET 改善 | 需要 PDF 图像复核曲线和约束边界 |
| Fig. 8-11 | WAPE 核心样例 | WAPE 能修正模型并减少触发 | WAPE 后轨迹更可行，参数估计逐渐接近真实值 | 需要 PDF 图像复核 |
| Fig. 12; Table 4-5 | Monte Carlo 统计证据 | WAPE 提高成功率、降低制导次数、改善精度 | 成功率 71.0%，平均制导次数 13.2，终端误差最优 | Fig. 12 分布需 PDF 复核 |
| Fig. 13-14 | 参数估计误差统计 | 主导气动参数收敛快，次要项难估 | CL0,1/CD0,1 两次后多在 20% 内；CL2,3/CD2,3 后期才可估 | 需要 PDF 图像复核 |
| Fig. 15-17; Table 6 | 飞行中故障证据 | 突变检测和 WAPE 对参数突变仍有效 | 32 组样本突变识别误差不超过 3 s，主参数 100 s 内修正 | 图像细节需 PDF 复核 |

图表叙事的特点是：前半部分图表解释方法必要性，后半部分表格锁定量化 claim。作者没有只用“轨迹好看”来证明方法，而是不断把曲线解释落到 TOP 是否失败、路径约束是否被触及、制导次数是否减少、终端误差是否缩小。

## 11. 章节结构与篇章布局

真实章节结构如下：

1. Introduction
2. Problem formulation
   - 2.1 Standard motion equations
   - 2.2 Deviations and disturbances
   - 2.3 Reentry guidance problem
3. The ET-NMPG method
   - 3.1 Definition of TOP
   - 3.2 Process of ET-NMPG
   - 3.3 Tricks for TO online
4. WAPE and change point detection
   - 4.1 PE for atmosphere
   - 4.2 PE for aerodynamics
   - 4.3 Change point detection
5. The guidance framework
6. Simulation results and discussion
   - 6.1 Comparison of different methods
   - 6.2 Monte Carlo simulation
   - 6.3 Results with in-flight faults
7. Conclusions

这是一种标准“问题公式化 -> 基础方法 -> 新模块 -> 总框架 -> 仿真验证”的方法论文结构。值得注意的是，作者没有一上来就写 WAPE，而是先写 ET-NMPG 和 TOP 的可行性处理。这样读者会先理解事件触发 NMPG 为什么有用、为什么仍会失败，再接受 WAPE 是必要增强。

Section 2 的功能是把工程问题变成数学对象：状态、控制、参数、扰动、约束、假设。Section 3 的功能是定义 NMPG 如何在线调用 TOP，尤其通过 P2、mesh、状态预测处理计算可行性。Section 4 才是论文新模块，负责估计参数和处理突变。Section 5 是把方法组合成完整流程，并交代 UI/FC/ET 的比较基准。Section 6 以三段递进验证：先单工况比较，再 300 样本统计，再飞行中故障。

章节命名偏好是功能型标题。作者不用很花的标题，而是直接用 `Problem formulation`, `The ET-NMPG method`, `WAPE and change point detection`, `Simulation results and discussion`。小节标题也偏方法模块名，便于工程读者快速定位。这种命名的优点是清晰，缺点是卖点暴露度一般；比如 Section 5 “The guidance framework” 可以更具体地命名为 “WAPE-assisted ET-NMPG guidance framework”。

结构上最值得学习的是 Section 6 的证据顺序。作者先用典型例子解释失败机制，再用 Monte Carlo 给统计指标，最后用故障突变场景验证异常处理模块。这个顺序比直接上统计表更易读，因为读者先看懂“为什么失败/为什么改善”，再接受“改善是否普遍”。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.2: 2 Problem formulation（方法/模型/算法）
  - L3 p.2: 2.1 Standard motion equations（对象/模块/过渡章节）
  - L3 p.3: 2.2 Deviations and disturbances（对象/模块/过渡章节）
  - L3 p.3: 2.3 Reentry guidance problem（问题定义）
- L2 p.3: 3 The ET-NMPG method（方法/模型/算法）
  - L3 p.3: 3.1 Definition of TOP（对象/模块/过渡章节）
  - L3 p.4: 3.2 Process of ET-NMPG（对象/模块/过渡章节）
  - L3 p.4: 3.3 Tricks for TO online（对象/模块/过渡章节）
    - L4 p.4: 3.3.1 Mesh refinement or not（对象/模块/过渡章节）
    - L4 p.4: 3.3.2 Mesh scheme and initial value（对象/模块/过渡章节）
    - L4 p.4: 3.3.3 State prediction before NMPG（对象/模块/过渡章节）
- L2 p.5: 4 WAPE and change point detection（对象/模块/过渡章节）
  - L3 p.5: 4.1 PE for atmosphere（对象/模块/过渡章节）
  - L3 p.5: 4.2 PE for aerodynamics（对象/模块/过渡章节）
  - L3 p.6: 4.3 Change point detection（对象/模块/过渡章节）
- L2 p.7: 5 The guidance framework（方法/模型/算法）
- L2 p.7: 6 Simulation results and discussion（结果/验证/讨论）
  - L3 p.7: 6.1 Comparison of different methods（方法/模型/算法）
  - L3 p.9: 6.2 Monte Carlo simulation（对象/模块/过渡章节）
  - L3 p.11: 6.3 Results with in-flight faults（结果/验证/讨论）
- L2 p.12: 7 Conclusions（结论/贡献回收）
- L2 p.12: CRediT authorship contribution statement（尾部材料）
- L2 p.12: Declaration of competing interest（尾部材料）
- L2 p.12: Data availability（尾部材料）
- L2 p.12: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 Problem formulation | 2 | 2 | 方法/模型/算法 |
| 2.1 Standard motion equations | 2 | 3 | 对象/模块/过渡章节 |
| 2.2 Deviations and disturbances | 3 | 3 | 对象/模块/过渡章节 |
| 2.3 Reentry guidance problem | 3 | 3 | 问题定义 |
| 3 The ET-NMPG method | 3 | 2 | 方法/模型/算法 |
| 3.1 Definition of TOP | 3 | 3 | 对象/模块/过渡章节 |
| 3.2 Process of ET-NMPG | 4 | 3 | 对象/模块/过渡章节 |
| 3.3 Tricks for TO online | 4 | 3 | 对象/模块/过渡章节 |
| 3.3.1 Mesh refinement or not | 4 | 4 | 对象/模块/过渡章节 |
| 3.3.2 Mesh scheme and initial value | 4 | 4 | 对象/模块/过渡章节 |
| 3.3.3 State prediction before NMPG | 4 | 4 | 对象/模块/过渡章节 |
| 4 WAPE and change point detection | 5 | 2 | 对象/模块/过渡章节 |
| 4.1 PE for atmosphere | 5 | 3 | 对象/模块/过渡章节 |
| 4.2 PE for aerodynamics | 5 | 3 | 对象/模块/过渡章节 |
| 4.3 Change point detection | 6 | 3 | 对象/模块/过渡章节 |
| 5 The guidance framework | 7 | 2 | 方法/模型/算法 |
| 6 Simulation results and discussion | 7 | 2 | 结果/验证/讨论 |
| 6.1 Comparison of different methods | 7 | 3 | 方法/模型/算法 |
| 6.2 Monte Carlo simulation | 9 | 3 | 对象/模块/过渡章节 |
| 6.3 Results with in-flight faults | 11 | 3 | 结果/验证/讨论 |
| 7 Conclusions | 12 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 12 | 2 | 尾部材料 |
| Declaration of competing interest | 12 | 2 | 尾部材料 |
| Data availability | 12 | 2 | 尾部材料 |
| References | 12 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

Introduction 的段落节奏是“背景扩展 -> 传统不足 -> 新领域进展 -> 旧策略局限 -> 借用外部概念 -> 特定场景失败 -> 本文方案”。作者先从翼式航天器和再入制导重要性进入，随后指出传统轨迹跟踪的状态散布问题，再将视角转向 CG&C 和 TOP。这个开头不是急于报方法，而是给再入制导问题赋予工程重量。

方法段落的节奏偏“定义 -> 问题 -> 修改”。例如 TOP 部分先定义 P1，再解释路径约束会使当前状态附近的 TOP 不可行，最后引入 buffered hard constraint 和 P2。WAPE 部分类似：先定义大气参数估计，再指出气动参数与质量不可同时估计，最后转向相对气动系数；先指出样本覆盖不足导致 LS 不准，再加入权重惩罚。

结果段落的节奏是“图表指向 -> 现象描述 -> 原因解释 -> 限定”。典型句式是先说 Fig. X shows，然后说 can be observed，再解释 because 或 mainly because，最后用 should be noted 收束。例如作者对 Fig. 11 的解释并不只说估计准确，而是区分大气参数、主导气动参数、次要气动参数，并说明非零均值扰动会影响误差下降。

段落功能表：

| 段落类型 | 功能 | 常见推进方式 | 可学习点 |
| --- | --- | --- | --- |
| 背景段 | 抬高再入制导重要性 | 航天器发展 -> 关键技术 -> 安全/复用需求 | 用工程场景而非空泛重要性开头 |
| 文献段 | 划分方法谱系 | 传统制导 -> CG&C -> TOP -> NMPG -> ET-MPC | 每一类文献都导向下一类方法 |
| Gap 段 | 暴露失败模式 | 旧方法有效处 -> 但是 -> 特定场景失败 | gap 不是“没人做”，而是“做了仍失败” |
| 方法定义段 | 给变量和公式 | 状态/控制/参数 -> 目标函数 -> 约束 | 先统一符号，减少后文歧义 |
| 方法补丁段 | 提出改造 | 不可行/不可辨/数据污染 -> 新变量/权重/检测 | 每个补丁对应一个风险 |
| 结果读图段 | 解释证据 | 图表 -> 观察 -> 机制 -> 限定 | 不只描述曲线，还解释为什么 |
| 结论段 | 回扣贡献和未来工作 | 方法总结 -> 对比优势 -> 未解决问题 | 主动承认阈值、偏差来源、robust NMPG 等后续问题 |

整体叙事节奏偏工程稳健型：不追求概念华丽，而是不断用“failure mode -> mitigation”推进。这种节奏适合制导控制论文，因为读者最关心方法是否能在边界条件下工作。

## 13. 文笔画像与语言习惯

整体语气是谨慎的工程方法文风。作者常使用 `can`, `may`, `usually`, `as much as possible`, `in most cases` 等限定词，避免把仿真结果夸大为普遍理论。强 claim 通常放在摘要、结论和结果表格附近，而正文解释中会用 `it can be observed`, `it should be noted`, `mainly because` 降低语气强度。

常用问题词包括：trade-off, deviation, disturbance, infeasible, constraint, failure, insufficient, challenging。它们围绕“在线制导在真实偏差下可能失效”服务。

常用贡献词包括：propose, incorporate, assist, update, reduce, enhance, ensure, detect。贡献表达偏动词化，强调方法对系统流程的作用。

常用机制词包括：event trigger, parameter estimation, model deviation, path constraints, guidance frequency, trajectory optimization, model similarity, changepoint。机制词高度集中，说明文章核心并不分散。

常用对比词包括：however, in contrast, unlike, compared with, while, whereas。Introduction 和 Results 都依赖对比推进：UI vs FC，FC vs ET，ET vs WAPE-assisted ET。

主动/被动使用：方法贡献处常用主动 `we propose`, `we incorporate`, `we assume`；客观定义和结果处常用被动或无主句，例如 `is defined`, `is represented`, `can be observed`。这种切换让贡献归属清晰，同时保持工程论文的客观感。

时态使用：一般现在时用于模型、方法和普遍判断；一般过去时用于仿真过程和观察结果；现在完成时较少，用于“has been applied/has begun”等文献进展。结论回到一般现在时，表示本文方法的稳定贡献。

形容词和副词：significant, substantial, accurate, computational, online, dynamic, robust, acceptable, unreasonable, feasible, promptly。形容词大多服务于工程性能和约束，而不是修辞性赞美。

这篇论文的文笔有一个明显特点：喜欢用 Remark 主动解释方法边界。Remark 1 说明即便放松 TOP，真实升力偏差仍可能使轨迹低于优化轨迹，从而强调 PE 的意义；Remark 5/6 说明数据不足时不做 WAPE，以及过快更新会使命令不平滑。这种写法能在方法论文中提前化解审稿疑问。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：41270
- 高频词：guidance(87)；state(46)；model(41)；parameter(40)；flight(38)；data(33)；estimation(33)；et-nmpg(32)；nmpg(29)；reentry(28)；parameters(27)；trajectory(24)；mesh(22)；method(19)；will(18)；control(18)；law(18)；deviations(18)；deviation(16)；time(16)
- 高频名词化/学术名词：guidance(87)；estimation(33)；deviation(16)；performance(14)；section(14)；optimization(12)；reference(12)；simulation(11)；motion(10)；density(8)；function(8)；detection(7)；acceleration(5)；ance(5)；pressure(5)
- 高频学术动词：provide(4)；estimated(4)；propose(3)；demonstrate(3)；compared(3)；estimate(3)；compare(3)；achieve(2)；presented(2)；constructed(2)；optimized(2)；provided(1)；identify(1)；construct(1)；predicted(1)
- 高频形容词：aerodynamic(14)；dynamic(13)；initial(13)；event(11)；terminal(10)；atmospheric(10)；coefficient(9)；actual(7)；interval(7)；optimal(7)；subsequent(7)；relative(7)；different(7)；predictive(6)；current(6)
- 高频副词：finally(5)；specifically(4)；relatively(4)；usually(3)；fully(3)；significantly(3)；consequently(3)；accurately(3)；highly(2)；additionally(2)；apply(2)；slightly(2)；directly(2)；ally(2)；strictly(2)
- 高频二词短语：parameter estimation(17)；guidance law(16)；flight state(14)；reentry guidance(12)；initial state(10)；wape-assisted et-nmpg(10)；trajectory optimization(9)；guidance command(8)；guidance commands(7)；atmospheric density(7)；model predictive(6)；model parameters(6)
- 高频三词短语：change point detection(4)；model predictive control(4)；update guidance law(4)；reentry guidance problem(4)；open-loop guidance law(4)；event-triggered model predictive(3)；guidance law reference(3)；law reference trajectory(3)；latin hypercube sampling(3)；initial state deviation(3)；model predictive guidance(2)；weight adaptive parameter(2)
- 被动语态估计：87；`we + 动作动词` 主动句估计：6
- 一般现在时线索：156；一般过去时线索：250；现在完成时线索：2；情态动词线索：48

分章节正文词频：

- 1 Introduction: guidance(39)；model(24)；reentry(14)；control(13)；flight(11)；method(10)；parameter(10)；nmpg(10)
- 2 Problem formulation: reentry(8)；guidance(8)；state(7)；dynamic(6)；disturbances(5)；motion(4)；equations(4)；angle(4)
- 3 The ET-NMPG method: mesh(22)；trajectory(14)；state(14)；nmpg(11)；guidance(11)；top(9)；law(8)；problem(8)
- 4 WAPE and change point detection: data(19)；parameter(11)；aerodynamic(10)；parameters(8)；model(8)；function(6)；estimation(6)；atmospheric(5)
- 5 The guidance framework: guidance(4)；data(4)；wape(3)；amount(3)；parameter(3)；three(2)；et-nmpg(2)；law(2)
- 6 Simulation results and discussion: guidance(20)；et-nmpg(17)；estimation(15)；state(14)；parameter(12)；flight(12)；parameters(11)；deviations(10)
- 7 Conclusions: guidance(5)；et-nmpg(4)；nmpg(3)；wape-assisted(2)；method(2)；methods(2)；event-triggered(2)；accuracy(2)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

抽取文本词频显示，高频核心词包括 guidance, model, state, parameter, ET-NMPG, control, estimation, flight, reentry, data, NMPG, trajectory, mesh, terminal, deviation, constraints, aerodynamic, optimization, law, simulation, WAPE-assisted。这些词几乎完全覆盖论文的贡献结构：制导对象、模型偏差、估计方法、触发策略、轨迹优化、仿真验证。

可复用背景句式：

- 在工程系统背景下引出关键技术：`Among the key technologies, X is crucial for...`
- 从传统方法转到问题：`Most conventional X uses a ... strategy. However, ...`
- 把领域趋势引到本文：`With the rapid development of ..., Y is gradually replacing...`

可复用 gap 句式：

- `However, both strategies have limitations: ...`
- `These problems can be attributed to the fact that...`
- `Direct least-squares estimation often does not...`
- `For this reason, we propose...`

可复用方法句式：

- `Denote the solution of problem P as...`
- `The complete trajectory optimization problem is represented as follows...`
- `To improve the comprehensive performance of..., X is invoked only when...`
- `The weight is used to characterize the extent to which...`

可复用结果句式：

- `It can be observed that...`
- `The results are shown in Figs. X to Y.`
- `This is mainly because...`
- `It should be noted that...`
- `In conclusion, X is effective for Y.`

可复用限制句式：

- `Further research is warranted to...`
- `It is important to comprehensively consider...`
- `The potential need for introducing X should be explored in more detail.`

中文仿写模板：

- 背景：随着 X 的发展，基于 Y 的 Z 正在从离线评估工具转向在线工程应用。
- Gap：已有 A 能缓解 B，但当 C 存在时，A 会引发 D，甚至导致 E 不可行。
- 方法：为解决该问题，本文在 A 框架中引入 B，并通过 C 控制估计结果偏离基准模型的程度。
- 结果：在 N 组样本中，所提方法将成功率从 a 提升到 b，同时将调用次数从 c 降至 d。
- 限制：需要注意的是，本文结论依赖于给定偏差区间和仿真扰动模型，真实飞行中的不确定性来源仍需进一步建模。

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  可迁移模板：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  可迁移模板：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
- 原句：However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guid ance, and control system, while the latter is constrained by coflicting relationships between guidance cycle duration, TO efficiency, and guid ance accuracy.
  可迁移模板：However, both strategies have limitations: the former requires substantial computing resources and demands constant high sensitivity from the entire navigation, guid ance, and control system, while the latter is constrained by coflicting relationships between guidance cycle duration, METHOD efficiency, and guid ance accuracy.
- 原句：Hence, to improve the accuracy of the guidance, online model identfication is very important.
  可迁移模板：Hence, to improve the accuracy of the guidance, online model identfication is very important.
- 原句：In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation.
  可迁移模板：In addition, it is important to comprehensively consider the sources and magnitudes of uncertainties based on the actual situation.
#### Gap/转折句
- 原句：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
  可迁移模板：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  可迁移模板：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
- 原句：However, people believe that as technology contin ues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
  可迁移模板：However, people believe that as technology contin ues to advance, winged vehicles will eventually regain their relevance in space transportation [X].
- 原句：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
  可迁移模板：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  可迁移模板：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
#### 方法提出句
- 原句：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (ET-NM PG) method assisted by weight adaptive parameter estimation (WAPE) and applies it to reentry guidance.
  可迁移模板：Communicated by Xingqun Zhan This paper proposes an event-triggered model predictive guidance (METHOD METHOD) method assisted by weight adaptive parameter estimation (METHOD) and applies it to reentry guidance.
- 原句：Guidance methods based on online trajectory optimization (TO) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems.
  可迁移模板：Guidance methods based on online trajectory optimization (METHOD) often face a trade-off between guidance accuracy and the efficiency of guidance command computation when dealing with complex problems.
- 原句：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
  可迁移模板：However, the actual model parameter values often deviate from the reference values, leading to an excessively high event trigger frequency and potentially rendering the trajectory optimization unfeasible.
- 原句：To address this issue, we propose updating the model parameters online using WAPE within the general ET-NMPG framework, thereby enhancing guidance accuracy and reducing guidance frequency.
  可迁移模板：To address this issue, we propose updating the model parameters online using METHOD within the general METHOD framework, thereby enhancing guidance accuracy and reducing guidance frequency.
- 原句：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
  可迁移模板：Importantly, for reentry processes, this approach can further ensure that the flight state remains within acceptable path constraints.
#### 结果呈现句
- 原句：The numerical simulation results cofirm the effectiveness of the proposed method.
  可迁移模板：The numerical simulation results cofirm the effectiveness of the proposed method.
- 原句：This results in a wide range of state dispersion during and at the end of the reentry flight, which is not conducive to safe landing and reuse of the vehicle. * Corresponding author.
  可迁移模板：This results in a wide range of state dispersion during and at the end of the reentry flight, which is not conducive to safe landing and reuse of the vehicle. * Corresponding author.
- 原句：The numerical simulation results cofirm the effectiveness of the proposed method.
  可迁移模板：The numerical simulation results cofirm the effectiveness of the proposed method.
- 原句：Since various pseudospectral methods [14] have begun to demonstrate excellent performance in solving trajectory optimization problems (TOP), many researchers have been trying to apply them to actual flight control [15--17] rather than simply using them as an of fline flight performance evaluation tool.
  可迁移模板：Since various pseudospectral methods [X] have begun to demonstrate excellent performance in solving trajectory optimization problems (METHOD), many researchers have been trying to apply them to actual flight control [X--X] rather than simply using them as an of fline flight performance evaluation tool.
- 原句：Zhang et al. [33] proposed an event-triggered model predictive guidance (ET-NMPG) method to achieve optimal ascent guid ance of the launch vehicle, which shows better guidance performance and stronger potential for practical application than the traditional iter ative guidance and other NMPG strategies.
  可迁移模板：Zhang et al. [X] proposed an event-triggered model predictive guidance (METHOD) method to achieve optimal ascent guid ance of the launch vehicle, which shows better guidance performance and stronger potential for practical application than the traditional iter ative guidance and other METHOD strategies.
#### 贡献/增量句
- 原句：For a long time, the main goal of related research has been to improve the efficiency of trajectory opti mization (TO), such as the sequential convex optimization (SCP) method and its many improved versions [17--19].
  可迁移模板：For a long time, the main goal of related research has been to improve the efficiency of trajectory opti mization (METHOD), such as the sequential convex optimization (METHOD) method and its many improved versions [X--X].
- 原句：Hence, to improve the accuracy of the guidance, online model identfication is very important.
  可迁移模板：Hence, to improve the accuracy of the guidance, online model identfication is very important.
- 原句：Sun et al. [35] proposed a new recursive sequence identfication method for aerody namic model identfication of the NASA F-16; Chowdhary et al. [36] compared the performance of three recursive parameter estimation al gorithms for aerodynamic parameter estimation of two aircraft from real flight data; Silva et al. [37] proposed to improve spacecraft orbit control effectiveness by introducing online estimation of asteroid parameters.
  可迁移模板：Sun et al. [X] proposed a new recursive sequence identfication method for aerody namic model identfication of the METHOD F-X; Chowdhary et al. [X] compared the performance of three recursive parameter estimation al gorithms for aerodynamic parameter estimation of two aircraft from real flight data; Silva et al. [X] proposed to improve spacecraft orbit control effectiveness by introducing online estimation of asteroid parameters.
- 原句：The standard reentry motion model, the motion model considering deviations and disturbances, and the reentry guidance problem are provided in Section 2.
  可迁移模板：The standard reentry motion model, the motion model considering deviations and disturbances, and the reentry guidance problem are provided in Section X.
- 原句：Building on this, we incorporated a parameter estimation step into the ET-NMPG pro cess to improve model prediction accuracy, thereby further reducing the number of guidance cycles, enhancing guidance precision, and ensuring flight safety.
  可迁移模板：Building on this, we incorporated a parameter estimation step into the METHOD pro cess to improve model prediction accuracy, thereby further reducing the number of guidance cycles, enhancing guidance precision, and ensuring flight safety.
#### 限制/边界句
- 原句：In addition, since the reentry dynamics system is an underactuated system, only one to three state variables can be selected for tracking (e.g., drag acceleration, altitude, latitude, and lon gitude) when performing tracking guidance [5,6].
  可迁移模板：In addition, since the reentry dynamics system is an underactuated system, only one to three state variables can be selected for tracking (e.g., drag acceleration, altitude, latitude, and lon gitude) when performing tracking guidance [X,X].
- 原句：Event-triggered model predictive control (ET-MPC) [28] has become a very popular control strategy in recent years, which, unlike the traditional time-triggered, periodic control strategy, executes update commands only when an event occurs, thus avoiding unnec essary complex computations and achieving a good balance between system performance and resource utilization [29,30].
  可迁移模板：Event-triggered model predictive control (METHOD) [X] has become a very popular control strategy in recent years, which, unlike the traditional time-triggered, periodic control strategy, executes update commands only when an event occurs, thus avoiding unnec essary complex computations and achieving a good balance between system performance and resource utilization [X,X].
- 原句：Meanwhile, a winged spaceplane needs to have flexible windows and reusable features so that the external environment and its inherent characteristics may differ slightly from one mission to another.
  可迁移模板：Meanwhile, a winged spaceplane needs to have flexible windows and reusable features so that the external environment and its inherent characteristics may differ slightly from one mission to another.
- 原句：One of the main difficulties is that real time flight data is limited and noisy, and the aerodynamic model of the reentry vehicle exhibits strong nonlinearity.
  可迁移模板：One of the main difficulties is that real time flight data is limited and noisy, and the aerodynamic model of the reentry vehicle exhibits strong nonlinearity.
- 原句：Direct least-squares estima tion often does not reduce the parameter deviation but may yield very unreasonable estimation results.
  可迁移模板：Direct least-squares estima tion often does not reduce the parameter deviation but may yield very unreasonable estimation results.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用密度主要集中在 Introduction 和问题建模假设处。作者没有在 Results 中大量引用，因为结果是本文仿真证据；引用主要用于建立领域版图、证明方法来源和支撑假设。

引用功能可以分成六类：

| 引用组 | 位置 | 功能 | 姿态 |
| --- | --- | --- | --- |
| [1-3] | Introduction 开头 | 说明翼式航天器和再入制导的重要性 | 背景认同 |
| [4-6] | 传统再入制导 | 支撑“轨迹设计 + 跟踪制导”和终端精确制导问题 | 继承 + 指出不足 |
| [7-13] | CG&C 与模型/数据范式 | 说明计算制导发展和本文选择模型型路线 | 分类定位 |
| [14-23] | 伪谱、SCP、MPSP、TOP | 说明在线轨迹优化效率是长期主题 | 方法谱系 |
| [24-26] | UI-NMPG/FC-NMPG | 构造 NMPG 调用策略对比基准 | 对比铺垫 |
| [27-33] | MPC/ET-MPC/ET-NMPG | 把事件触发概念从控制引入制导 | 迁移借用 |
| [34-37] | 参数估计 | 说明在线模型识别已有基础但不直接适用 | 继承 + 转折 |
| [38-42] | 气动模型、导航、传感、控制假设 | 支撑模型形式和系统假设 | 假设背书 |

引用策略的高明处在于，作者没有逐篇批评前人，而是用“类别限制”制造 gap。UI-NMPG 不是错，而是太耗资源；FC-NMPG 不是错，而是周期固定；robust MPC 不是错，而是多面向 LTI 系统，不适合再入制导；在线 PE 不是错，而是常用于离线建模或其他飞行器，难以直接用于实时再入 NMPG。这样的评价姿态更稳，不容易被审稿人认为是在稻草人攻击。

近年文献占比较高，尤其 2023-2024 年的 Aerospace Science and Technology、Chinese Journal of Aeronautics、TAES 等文献用于证明前沿性。同时保留 MPC 经典书籍和早期 JGCD 文献作为理论基础。该引用组合适合工程方法论文：近期应用证明问题热度，经典文献证明方法根基。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：69
- Introduction 引文簇数量估计：21
- References 条目数：45
- 可识别年份条目数：70
- 2021 年及以后文献数：32
- 2010 年前经典文献数：7
- 同刊引用数（按 subject 粗匹配）：1
- 高频来源期刊：Aerospace Science and Technology(1)
- 引文簇样例：[7], [8,9], [1], [14], [2], [3], [4], [20], [5,6], [24], [25,26], [27]

带引文的 gap/转折句样例：

- However, people believe that as technology contin ues to advance, winged vehicles will eventually regain their relevance in space transportation [2].
- We cannot expect the NMPG to provide guidance commands in real-time like traditional algorithms, and current research has primarily employed two strate gies for generating guidance commands through TO: the uninterrupted NMPG (UI-NMPG) strategy [24], which immediately carries out TO af ter completing the previous one; and the fixed cycle NMPG (FC-NPMGP) strategy [25,26], which establishes a longer interval to ensure optimal guidance law generation within that period.
- However, most model identfication is carried out offline for modeling purposes and cannot be directly used for real-time guidance [34].

References 解析样例（前 8 条）：

- 17. PE results with in-flight faults.
Data availability
Data will be made available on request.
References
- [1] L. Van Den Abeelen, Spaceplane HERMES-Europe’s Dream of Independent Manned
Spacflight, Springer International Publishing, Hilversum, the Netherlands, 2017.
- [2] M.A. Bentley, Spaceplanes: From Airport to Spaceport, Springer, New York, NY,
2009.
- [3] Z. Liu, G. Zheng, B. Zhang, J. Wei, H. Huang, J. Yan, Predictor-corrector reentry guidance for hypersonic glide vehicles based on high-precision analytical solutions, Aerosp. Sci. Technol. (2024) 109545, https://doi.org/10.1016/j.ast.2024.109545.
- [4] R. Chai, A. Tsourdos, A. Savvaris, S. Chai, Y. Xia, C. Chen, Review of advanced guidance and control algorithms for space/aerospace vehicles, Prog. Aerosp. Sci. 122 (2021) 100696, https://doi.org/10.1016/j.paerosci.2021.100696.
- [5] P. Lu, Regulation about time-varying trajectories: precision entry guidance illus
trated, J. Guid. Control Dyn. 22 (6) (1999) 784--790, https://doi.org/10.2514/2. 4479.
- [6] A. Vitiello, E.M. Leonardi, M. Pontani, Multiple-sliding-surface guidance and control for terminal atmospheric reentry and precise landing, J. Spacecr. Rockets 60 (3) (2023) 912--923, https://doi.org/10.2514/1.A35438.
- [7] P. Lu, Introducing computational guidance and control, J. Guid. Control Dyn. 40 (2) (2017) 193, https://doi.org/10.2514/1.G002745.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 仿真代表性风险。所有核心证据都来自数值仿真，没有实飞数据、半物理仿真或硬件在环验证。随机扰动由正弦叠加并按动压缩放，参数偏差区间由作者设定，可能不足以代表真实再入环境。

2. 假设较强。作者假设导航系统足够准确、大气密度可由机载设备直接测量、控制系统能很好跟踪制导命令。这些假设把 GNC 中的 N 和 C 风险排除在外，使 G 的效果更清晰，但真实系统耦合下性能可能下降。

3. 可辨识性与估计理论不足。论文承认气动系数和质量不可同时唯一估计，也承认 CL2,3 和 CD2,3 早期难以准确估计。WAPE 用相对气动参数和权重惩罚处理，但缺少严格收敛性、误差界或可辨识条件分析。

4. 阈值和权重选择可能经验化。事件触发阈值、`Kp`, `eta_r`, `m_min`, `t_min`, `S_Upsilon`, 权重函数形式都对结果有影响。论文给出参数表，但缺少系统灵敏度分析。

5. 比较基准公平性。UI-NMPG 因单次仿真耗时超过飞行时长而未纳入数值比较；FC-NMPG 固定周期取 30 s，若调整周期，成功率和计算量可能变化。审稿人可能要求更多基准周期或自触发策略对比。

6. 路径约束放松的安全解释。P2 允许路径约束放松到 `eta_r in [1,1.2]`，结果中也说 WAPE 后状态略超原始严格边界但在放松边界内。对于安全关键再入任务，什么叫“acceptable path constraints”需要更强工程解释。

7. 计算时间解释需要谨慎。Table 4 中 WAPE 单次 TOP 时间显著高于 ET-NMPG，但总仿真时间更短。作者解释 PE 只需约 5 ms，耗时增加主要来自 TO 变慢；这个现象可能需要更细的 solver 迭代统计支撑。

8. 数据可复现性有限。Data availability 写“on request”，但轨迹优化 solver、mesh 细节、随机种子、LHS 样本等若不公开，复现难度较高。

9. 稳定性/递归可行性缺失。MPC/ET-MPC 论文常被问到稳定性和递归可行性。本文以工程仿真为主，缺少理论保证，可能在控制理论审稿人处被要求补充讨论。

10. change point detection 场景仍简化。飞行中故障部分没有考虑大气密度模型偏差和初始状态偏差，只聚焦气动参数突变。真实故障可能多源并发，突变检测的鲁棒性还有待验证。

## 17. 可复用资产

可复用选题套路：在已有“触发式/在线式/自适应式”方法上寻找二阶失败模式。本文不是简单说 ET-NMPG 好，而是问“ET-NMPG 在模型偏差下会怎样失败”，再提出补丁。这种套路可以迁移到热防护、结构健康监测、可靠性分析、热管理优化等方向：先承认已有方法的价值，再找其工程部署时的隐藏瓶颈。

可复用 gap 表达：已有方法 A 在理想模型下可降低计算量，但当真实系统参数偏离参考模型时，A 会频繁触发/不稳定/不可行。因此，需要一个能随数据质量自适应更新模型的机制。

可复用方法结构：事件触发负责“何时更新”，在线估计负责“用什么模型更新”，突变检测负责“哪些历史数据还能用”。这个三模块结构很适合写成框架型论文。

可复用图表设计：

- 框架流程图：对比 UI/FC/ET/本文方法的调用逻辑。
- 典型失败曲线：用一组样例展示旧方法如何失败。
- 参数估计曲线：展示估计值与真实值随时间/迭代变化。
- Monte Carlo 散点图：展示终端误差分布集中程度。
- 统计表：把成功率、计算时间、调用次数、精度放在同一张表中。

可复用论证链：方法不是为了估计而估计，而是让估计改善下游任务指标。写自己的论文时，应避免只报告中间模块误差，要证明中间模块如何改善系统级目标。

可复用审稿防守：主动用 Remark 说明不可辨识、数据不足、更新过快、约束放松等问题。把潜在批评放进方法说明，比在审稿回复中被动解释更稳。

## 18. 对我写论文的启发

第一，好的工程方法论文可以从“已有方法的部署失败”切入，而不是从“没人做过”切入。本文的 gap 很具体：ET-NMPG 已经能减少调用，但模型偏差会让它触发过密甚至不可行。这个 gap 比泛泛说“提高精度和效率”更有说服力。

第二，贡献要绑定系统级指标。WAPE 的估计误差不是终点，成功率、制导次数、总计算时间、终端误差和路径约束才是终点。写自己的论文时，如果有代理模型、降阶模型、参数识别模型，也要把它接回最终工程任务。

第三，仿真验证要分层。单个样例负责解释机制，Monte Carlo 负责统计可信度，故障场景负责鲁棒性。这个三层验证结构比只堆很多工况更清晰。

第四，承认局部失败反而增强可信度。作者承认某些气动参数难以早期准确估计，但解释它们影响较小且不应固定。这样的写法让论文显得成熟：不是每个子指标都完美，但核心任务指标改善。

第五，图表功能要明确。Table 4 是整篇最关键的“卖点表”：一次性呈现调用次数、单次计算时间、总时间和成功率。自己的论文也应设计这种能承载核心 claim 的表，而不是让读者在多张图之间拼结论。

第六，未来工作要回扣真实边界。本文结论没有泛化到所有再入场景，而是明确说要进一步研究实际偏差来源、阈值选择和 robust NMPG。一个好的 limitation 不是削弱论文，而是表明作者知道方法的工程边界。

## 19. 最终浓缩

这篇论文最值得学习的是：把“事件触发 NMPG”从一个省计算资源的策略，升级成一个带在线模型校正和数据筛选的再入制导框架。作者抓住的核心矛盾是，真实模型参数偏差会破坏事件触发的收益，导致触发频繁、TOP 不可行和路径约束风险。WAPE 的作用不是单纯估计参数，而是让后续 NMPG 用更接近真实系统的模型生成制导律。

最强证据是 300 组 Monte Carlo：WAPE-assisted ET-NMPG 成功率达到 71.0%，高于 ET-NMPG 的 44.7% 和 FC-NMPG 的 19.7%；平均制导次数从 ET-NMPG 的 121.7 降到 13.2；终端速度等状态误差也显著更小。飞行中故障仿真进一步显示，突变检测能在 32 组样本中以不超过 3 s 的误差识别突变时刻。

最大风险是证据仍以仿真为主，且依赖较强假设、经验阈值和给定参数偏差区间。若要迁移这篇论文的写法，最应学习的是它的论证组织：旧方法失败模式清楚，新模块逐一回应失败模式，结果表格同时覆盖性能、计算和安全指标。
