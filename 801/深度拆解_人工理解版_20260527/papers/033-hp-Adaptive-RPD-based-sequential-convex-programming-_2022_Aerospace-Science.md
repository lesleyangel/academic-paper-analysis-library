## 1. 身份层

本文对应 cleantext 目录 “033-hp-Adaptive-RPD-based-sequential-convex-programming-_2022_Aerospace-Science”，metadata 中 title 与 authors 均为空；从 abstract 和正文可识别为一篇关于 “hp-Adaptive RPD-based sequential convex programming” 的再入轨迹优化论文。研究对象是高超声速/再入轨迹优化中 SCP 方法的离散误差、线性化误差和迭代效率问题。abstract、clean_body、figure captions、table captions、tables、equations、references、metadata 均已读取；abstract 开头含 “Communicated by Xingqun Zhan”，table captions 只有泛化编号，equations 有低置信度 OCR 噪声。

论文身份是“优化算法改进论文”，不是飞行器气动模型或控制律论文。它把 hp-adaptive Radau pseudospectral discretization 引入 sequential convex programming，并通过三阶段迭代管理提高再入轨迹优化的稳定性、精度和速度。

## 2. 主张层

核心主张是：SCP 的精度和效率不仅取决于凸化，还取决于离散策略和迭代阶段设计；通过 hp-adaptive RPD 在迭代中自适应调整离散点数量与位置，并配合初期约束松弛和后期正则化，可以在保持精度的同时显著降低 CPU 时间。

摘要给出的主张链是：现有 SCP 常用过于简单的均匀离散或预设 pseudospectral 离散，难以自动控制离散误差；作者将迭代分为 approach stage、hp update stage 和 convergence stage；第一阶段用约束松弛保证粗初值也可推进，第二阶段根据微分误差和状态曲率自适应加点或分段，第三阶段停止网格更新并用正则化降低线性化误差；算例中 CPU 时间相对其他 SCP 降低 40%-70%，约为 GPOPS-II 的二十分之一。

最强 claim 是“SCP 的工程效率瓶颈不只在凸优化求解器，而在离散网格、线性化误差和初值可行性之间的协同管理”。这比“hp-adaptive RPD 更准”更强，因为作者提出的是一个完整迭代流程：先让粗初值能走起来，再让网格在需要处变密，最后停止网格扰动专心收敛。

结论闭合度较高。摘要承诺的三阶段、约束松弛、自适应离散点更新、正则化收敛、CPU 时间优势都在 Section 5 中逐项验证。未闭合之处是理论收敛性：作者承认正则化没有改变线性收敛性质，未来才考虑 Hessian 权重，因此论文主要是工程算法验证而非严格收敛理论突破。

## 3. 选题层

选题抓住了再入轨迹优化从“能解”转向“快、稳、准”的需求。SCP 在航空航天中很受欢迎，因为非凸控制约束可通过 lossless convexification 和锥规划处理；但实际精度还受轨迹离散误差支配。均匀离散点太少会丢失局部剧烈变化，点太多又牺牲实时性。

作者的切入点不是重新发明凸化，而是把 hp 自适应伪谱方法的网格思想嵌入 SCP 迭代。这个问题对再入制导有吸引力，因为参考轨迹需要快速生成，同时路径约束如动压、热流和过载不能粗略处理。

## 4. 位置层

论文位于三类方法之间：直接法最优控制、SCP/锥规划轨迹优化、hp-adaptive pseudospectral 方法。已有 SCP 文献多用均匀离散和中心差分，或使用固定分段/固定阶数的伪谱离散；GPOPS-II 等通用最优控制软件精度高但计算量较大。

本文的位置是把“凸优化子问题的可解性”和“离散网格的自适应精度”合在一个迭代流程里。它相对 GPOPS-II 更工程轻量，相对固定 SCP 更自适应，相对普通 hp 方法则强调每一步仍是凸优化子问题。

gap 的成立来自传统 SCP 对离散的低估。许多 SCP 工作强调 lossless convexification 和二阶锥约束处理，但在轨迹离散上使用均匀节点或预设伪谱节点；这会导致两个问题：局部剧烈变化处误差大，平缓区又浪费节点。本文的 gap 是“缺少在 SCP 迭代过程中自动评估并更新离散误差的 hp-Radau 策略”。

文献版图中，Liu/Shen/Lu 等 entry SCP 工作提供凸化基线，hp pseudospectral 和 GPOPS-II 提供高精度离散思想，Radau collocation 提供数值积分基础，MOSEK/锥规划提供求解器基础。作者的定位不是替代所有最优控制软件，而是在再入 SCP 这一类问题中给出更轻量、可控、速度快的专用流程。

## 5. 贡献层

第一项贡献是将 Radau pseudospectral discretization 用于 SCP 子问题离散，并用稀疏微分矩阵表达状态约束，使凸优化子问题保持可解规模。

第二项贡献是定义中点微分误差和最差状态曲率，作为 hp-adaptive RPD 的网格更新依据。若曲率分布相对均匀，则增加当前段的 LGR 点；若曲率集中，则按曲率密度重新分段并布置最少点数。

第三项贡献是三阶段迭代策略：approach stage 用微分约束松弛帮助粗初值接近真实轨迹；hp update stage 更新分段和节点以降低离散误差；convergence stage 停止网格变化并加入正则化项，抑制相邻子问题解的振荡。

## 6. 方法层

问题 formulation 使用能量作为独立变量，状态包括无量纲半径、经度、纬度、航迹角和航向角。控制变量由 bank angle 改写为 u1=cosσ、u2=sinσ，从而把归一化约束写成 ||u||²=1，并进一步松弛为二阶锥形式。路径约束包括动压、热流和过载，统一为随能量变化的高度下界。

凸化步骤对非线性动力学在参考轨迹处一阶线性化，得到线性时变系统；归一化控制约束使用 lossless convexification 处理。离散步骤将能量区间分段，每段使用 LGR 点和 Lagrange 多项式构造 Radau pseudospectral differentiation matrix，形成稀疏线性等式约束。

迭代步骤从 10 段、每段 4 个 LGR 点的粗网格和线性初值开始。每次求解凸子问题后，根据搜索效率 κ 更新参考轨迹，计算微分误差、曲率和曲率均匀性，再决定是否网格更新、保持松弛或进入正则化收敛阶段。

## 7. 证据层

基准算例是 CAV-H 再入最大经度问题，MOSEK 求解凸子问题。结果显示，优化轨迹与 Runge-Kutta 积分轨迹在高度-速度图和地面轨迹上高度重合。Table 2 显示最大高度误差约 23 m，经纬度最大误差分别约 0.0154° 和 0.0012°，多数相对误差很小；控制归一化误差大多低于 1e-7，支撑 lossless relaxation 有效。

收敛证据显示总共 19 次迭代、CPU 时间 2.377 s。前 7 次 approach stage 从直线初值接近真实轨迹；hp update stage 5 次迭代将离散点增至约 403 并降低微分误差；最后 7 次 convergence stage 快速降低状态残差。Monte Carlo 1000 个不同初值中，迭代次数 16-22，离散点 402-485，CPU 时间 1.68-3.461 s，说明对初值不敏感。

对比证据来自 UD、固定 hp RPD 和 GPOPS-II。Table 4/5 抽取虽有错位，但正文明确给出：提出方法 CPU 时间较 UD(800) 短 70.5%，较 RPD(150) 短 62.1%，约为 GPOPS-II 的 1/20，同时轨迹误差与密集离散方案和 GPOPS-II 接近。

Claim-Evidence 可拆为六组。Claim 1“控制约束可无损松弛”由 Hamiltonian 简要证明和控制归一化误差低于 1e-7 的结果支撑；Claim 2“hp 自适应网格能降低离散误差”由最大 differential error 在第二阶段下降和离散点从 41 增至 403 支撑；Claim 3“三阶段各有功能”由 Fig. 7-9 中曲线更新、残差/微分误差历史和 CPU/节点数历史支撑；Claim 4“结果精度可由积分复核”由 Runge-Kutta 积分轨迹与优化轨迹误差表支撑；Claim 5“初值不敏感”由 1000 次 Monte Carlo 统计表支撑；Claim 6“比固定离散和 GPOPS-II 更快”由方法对比表和 CPU 时间说明支撑。

关键表格的角色很清楚。Table 1/2 给问题设置与约束，Table 3 给状态误差，Table 4 给初值 Monte Carlo 统计，Table 5 给算法对比。虽然抽取后编号/列名有错位，但正文说明能重建它们的功能：先证明单次可行，再证明鲁棒，再证明相对效率。

公式链条也具有接口作用。能量域动力学减少速度状态；u1=cosσ、u2=sinσ 把 bank angle 非线性转成归一化控制；路径约束统一为高度下界；线性化公式形成凸子问题；RPD 微分矩阵形成稀疏等式；中点 differential error 和曲率公式驱动 hp 更新；正则化目标抑制后期振荡。

## 8. 结构语言层

文章结构非常工程算法化：Introduction 先指出 SCP 的离散误差短板；Problem formulation 给再入动力学、控制变量和路径约束；Convexification/discretization 给凸化与 RPD 子问题；Iterative algorithm 给误差指标、网格更新和三阶段流程；Numerical simulations 用精度、收敛、初值鲁棒性和方法对比收束。

语言上核心词是 “discretization error”、“linearization error”、“hp-adaptive”、“constraint relaxation”、“regularization”、“CPU time”。作者不是单纯说算法更快，而是把速度解释为“子问题规模逐渐增加”和“高误差区域才加密”；把稳定性解释为“初期松弛”和“后期正则化阻尼振荡”。

段落组功能是“问题 formulation - 可凸化 - 可离散 - 可迭代 - 可比较”。前两节负责把再入 OCP 转成 SCP 可处理形式；第三节把非凸性和离散性处理掉；第四节是论文真正的算法核心；第五节按可行性、收敛性、鲁棒性、比较四步验证。这种推进适合算法论文，因为读者需要先相信问题被正确转写，再相信算法更快。

语言上大量使用 “accuracy”、“efficiency”、“stability”、“discretization error”、“linearization error”。作者把每个阶段命名为 approach、hp update、convergence，是一种很强的叙事工具：名称本身解释了阶段功能。语态以被动和过程描述为主，尤其在算法段落中使用 “is calculated”、“is updated”、“is introduced”，让算法像流程规范而非经验脚本。

## 9. 引用风险层

引用主要支撑再入轨迹优化、直接法/间接法、SCP 航天应用、lossless convexification、伪谱最优控制、hp 自适应和 GPOPS-II。风险在于，论文验证集中在一个典型 CAV-H 最大经度算例，且目标函数较简单；复杂多目标、多阶段、强非凸路径约束或在线扰动情况下的表现仍需验证。

审稿风险包括：lossless convexification 证明依赖特定控制约束形式；网格更新参数如 ε、ζ、pmin、κ 具有经验性；CPU 时间依赖 MATLAB、MOSEK、硬件和实现细节；与 GPOPS-II 的比较可能受参数设置影响；正则化只改善表现，不改变线性收敛性质。抽取层面，metadata 缺题名/作者，表格错位明显，具体对比数值需回 PDF 核查。

更具体的审稿风险包括：第一，示例目标是最大终端经度，目标函数较简单，复杂多目标或带禁飞区/热防护裕度目标时表现未知；第二，参数 κ、ε、δr、pmin、ζ 等需要人工设定，论文没有系统灵敏度分析；第三，CPU 时间比较依赖 MATLAB/MOSEK/硬件和实现细节，若 GPOPS-II 调参不同，比例可能变化；第四，lossless convexification 的证明针对特定控制约束形式，不能自动推广到所有再入控制问题。

抽取风险较高：metadata 缺 title/authors；abstract 带 communicated 信息；table captions 只有 Table 1-4 泛称；table_005 对比表错位但又是核心证据；equations 中部分符号置信度低。后续若要引用具体 CPU、误差和迭代次数，应优先回 PDF 表 3-5 和 Fig. 7-11。

## 10. 复用层

可复用的是“误差类型分治”的算法写法：SCP 中线性化误差靠序列迭代降低，离散误差靠自适应网格降低，初值不可行靠松弛处理，末端振荡靠正则化处理。这个结构可迁移到着陆、上升段、无人机路径规划和其他直接法轨迹优化问题。

也可复用它的证据组织：先证明单次结果可积分复核，再展示迭代阶段如何工作，再做初值 Monte Carlo，最后与固定离散和通用软件对比。不可直接复用的是 CAV-H 参数、路径约束高度下界、hp 更新阈值和 CPU 提升比例；换问题后必须重新调参和验证。

可复用的论证链是“现有算法忽略某一误差源 - 定义可计算误差指标 - 在迭代中按误差自适应调整模型规模 - 用阶段化策略处理初值和末端收敛 - 用积分复核与基线对比证明精度/效率”。这个链条不仅适合轨迹优化，也适合自适应网格 PDE 优化、模型预测控制和在线规划算法。

可复用的图表顺序是“问题几何/状态示意 - 离散网格/稀疏矩阵示意 - 轨迹与积分对比 - 控制约束误差 - 迭代过程轨迹更新 - 残差和微分误差历史 - 节点数/CPU 历史 - 多算法对比”。不可模仿的是 CAV-H 参数、能量域动力学、路径约束合并方式和 CPU 提升比例；换任务后只能复用阶段化思想，不能复用数值结论。

本篇自检：十层字段已覆盖；摘要和结论已归入主张层；图表/公式/Claim-Evidence 已归入证据层；语言画像已归入结构语言层；引用和审稿风险已归入引用风险层；可复用与不可模仿内容已归入复用层；仍需 PDF 核查的项目包括 metadata 缺题名/作者、table captions 泛化、表格错位、低置信度公式和具体比较数值。
