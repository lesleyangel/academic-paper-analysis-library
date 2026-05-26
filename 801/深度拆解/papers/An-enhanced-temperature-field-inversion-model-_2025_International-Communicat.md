## 0. 读取说明

本文依据 `801/文本/txt/An-enhanced-temperature-field-inversion-model-_2025_International-Communicat.txt` 的全文抽取进行拆解。抽取文本包含摘要、机翼模型、热传输路径、样本生成、POD 降维、BPNN 超参数、GA 传感器优化、RF/RBFNN/CNN 对比和结论。温度云图、传感器布置图、误差分布图等视觉细节需要 PDF 图像复核。

<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS START -->
### 复核补充：抽取边界与合并状态

- 增补内容已并入原有主章节，不再作为独立追加章。
- 正文词频只统计正文主章节：1 Introduction, 2 The wing and the TFI problem, 3 Methodologies of the TFI model, 4 Creation of the TFI model, 5 Comparison model with POD-RF method, 6 Results and discussions, 7 Conclusions。
- 排除范围：摘要、References、图题/表题、页眉页脚、版权信息、期刊首页信息、旧分析文字。
- 正文切分告警：
- 无明显正文切分告警。
<!-- REAUDIT-INTEGRATED-2026-05-26:STATUS END -->

## 1. 基本信息与论文身份

- 题名：An enhanced temperature field inversion model by POD-BPNN-GA method for a 3D wing with limited sensors
- 期刊：International Communications in Heat and Mass Transfer, 164 (2025) 108778
- 作者：Jia-Xin Hu, Jian-Jun Gou, Chun-Lin Gong
- 机构：Northwestern Polytechnical University
- 关键词：Temperature field inversion; Heat transport path; Back propagation neural network; Genetic algorithm; Aircraft wing

论文身份是面向高速飞行器三维机翼的“有限传感器温度场反演”方法论文。它的核心不是单纯训练一个神经网络，而是把高保真温度场样本、POD 特征降维、BPNN 映射和 GA 传感器布局优化组合起来，在传感器数量减少 60% 的情况下保持全场温度反演精度。

## 2. 摘要与核心信息提取

摘要信息可拆成五点：

1. 高速飞行器全局温度场难以直接测量，但热防护和结构健康监测需要全场信息。
2. 论文以带热传输路径的 3D 机翼为对象，用有限局部传感器反演全局温度场。
3. BPNN 的训练轮数、网络宽度/深度和数据维度被系统优化。
4. POD 从预生成温度场中提取主特征，在大幅降低维度的同时保持精度。
5. GA 以误差和成本为目标优化传感器位置和数量，最终 MRE 0.063%、MAE 0.496 K，传感器减少 60%，并优于 RF、RBFNN、CNN 对比模型。

一句话浓缩：本文用 POD 把 1920 节点温度场压缩到低维特征，用 BPNN 学习传感器温度到全场特征的映射，再用 GA 找到少而有效的传感器布局。

<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT START -->
### 复核补充：摘要原文定位与中文译文

- 摘要抽取状态：成功。
- 完整英文摘要原文不在公开报告正文中展开；本地完整摘录见 `801/深度拆解/extracted_evidence/An-enhanced-temperature-field-inversion-model-_2025_International-Communicat.json` 的 `abstract` 字段，以及 `801/深度拆解/local_full_reports/An-enhanced-temperature-field-inversion-model-_2025_International-Communicat.md`。

中文译文：

> 由于真实数据只能通过非常有限的本地传感器获取，全球温度的准确反演对于高速飞行器的状态评估至关重要。在这项工作中，针对具有热传输路径的 3D 飞机机翼结构开发了结合真实传感器数据的温度场反演模型。该模型通过反向传播神经网络方法进行训练，并使用优化的关键超参数，即最大历元、宽度、深度和数据维度。预先生成的样本温度场被完全分解为适当的正交模式，提取主要特征以形成匹配的数据维度，模型构建效率显着提高，而精度损失很小。
>
> 综合考虑反演误差和成本，提出了一种混合遗传算法来同时优化传感器位置和数量，通过将传感器聚集到高温梯度区域，模型性能大大提高。测试结果表明，平均相对反演误差、平均绝对反演误差和传感器数量分别减少了0.063%、0.496K和60%，TFI模型具有良好的性能，并通过与随机森林、径向基函数神经网络和卷积神经网络方法的比较验证了TFI模型的优势。
<!-- REAUDIT-INTEGRATED-2026-05-26:ABSTRACT END -->

## 3. 选题层深拆

高速飞行器翼面温度场具有强空间梯度和强工况依赖。全场传感器布置成本高、重量高、可靠性差；但只看少量传感器又无法判断局部热点和整体热状态。温度场反演因此成为热防护系统和结构安全评估的关键中间技术。

选题中有三个矛盾：

第一，测量稀疏与场信息密集的矛盾。输入只有几十个局部温度，输出却是 1920 个节点的全场温度。

第二，模型精度与计算效率的矛盾。直接从传感器到 1920 维输出训练神经网络会导致数据维度高、训练慢、泛化难。

第三，传感器数量与布局质量的矛盾。减少传感器不能简单随机删点，而要保留对高温区、梯度区和热传输路径敏感的观测能力。

本文的选题价值就在于把这三个矛盾分别对应到 POD、BPNN 和 GA：POD 降输出维度，BPNN 建立非线性映射，GA 优化传感器数量与位置。

## 4. 领域位置与文献版图

领域版图包括三类研究。

第一类是温度场重构/反演。已有方法包括插值、响应面、卡尔曼滤波、机器学习等，但面对三维高速翼热路径结构和有限传感器时，精度和效率仍受限。

第二类是降阶建模，尤其 POD。POD 可从大量温度场快照中提取主模态，把高维场转成少量系数，适合与机器学习结合。

第三类是传感器布置优化。传感器位置决定反演信息质量，常用 GA、贪心算法或特征重要性选择。本文采用 GA 同时优化数量和位置，并与 RF 特征选择布局比较。

本文的定位是“POD-BPNN-GA 一体化反演流程”：不是单独发明 POD、BPNN 或 GA，而是面向带热传输路径的 3D 翼，把降维、回归和传感器优化组合成可验证方案。

## 5. Gap 制造机制

本文的 gap 是从实际可测性切入的。高速翼全局温度场重要，但全场测量不可行；已有有限传感器反演方法常有以下不足：

1. 直接高维输入/输出导致模型训练成本高。
2. 传感器布局不一定针对热传输路径和高温梯度区优化。
3. 传统机器学习模型如 RF、RBFNN、CNN 在小样本、高维输出下精度不足或成本较高。
4. 很多研究只关注算法精度，没有同时考虑传感器数量成本。

作者通过数据对比制造 gap：初始 60 传感器可得到较高精度，但 GA 最终用 24 个传感器即达到甚至略优结果，说明“少传感器但位置优化”比“多传感器平均布置”更有价值。与 RF/RBFNN/CNN 的对比进一步说明，POD-BPNN-GA 在该任务上兼具低误差和低传感器成本。

## 6. 创新性判断

强创新点：

- 将 POD-BPNN-GA 组合用于带热传输路径的 3D 高速翼温度场反演，并形成完整数据流。
- 系统优化 BPNN 的 epoch、网络宽度/深度和输入/输出降维维度，而不是直接套用默认网络。
- GA 同时优化传感器数量和位置，以误差与成本为目标，最终减少 60% 传感器。
- 与 RF、RBFNN、CNN 及不同传感器布局进行系统对比，证明组合方法优势。

中等创新点：

- 将温度场分为可测传感器温度 `Ts`、设计/表面温度 `Td` 和全局温度 `Tu` 等不同数据对象，并用 POD 处理映射关系。
- 传感器布局结果显示传感器集中于高温区、外缘/后缘和热传输路径边缘的高梯度区域，具有物理可解释性。

创新边界：

- 样本来自数值仿真，缺少真实飞行或实验测温数据验证。
- BPNN、POD、GA 都是成熟方法，创新主要在任务组合和参数调优。
- 泛化范围受限于训练工况网格：高度、速度、攻角组合之外的外推能力不明。

## 7. 论证链条复原

全文论证链如下：

1. 高速翼需要全局温度场，但只能布置有限传感器。
2. 建立带热传输路径的 3D 翼仿真模型，生成不同高度、速度、攻角下的温度场样本。
3. 直接高维温度场反演成本高，因此用 POD 提取主模态，压缩输入/输出维度。
4. 选择 BPNN 学习传感器 POD 特征到全场温度 POD 系数的非线性映射。
5. 通过 epoch、网络宽度/深度、输入/输出维度实验确定 BPNN 合理配置。
6. 初始 60 传感器布局已能实现较高精度，但存在冗余。
7. 用 GA 同时优化传感器数量和位置，在满足误差约束下减少传感器。
8. 与 RF、RBFNN、CNN 和 RF 布局对比，证明 POD-BPNN-GA 精度最高且传感器更少。
9. 温度云图和误差分布证明反演能捕捉高温区与梯度区。

<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC START -->
### 复核补充：问题-方法-增量闭环

- 提出的问题：需结合 Introduction 首段复核。
- 已有研究不足/GAP：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors. The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9]. International Communications in Heat and Mass Transfer 164 (2025) 108778 Contents lists available at ScienceDirect International Communications in Heat and Mass Transfer journal homepage: www.elsevier.com/locate/ichmt Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
- 本文解决方式：In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths. The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality. The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 学术或工程增量：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise. At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations. The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 逻辑复核重点：看 Introduction 的 gap 是否被 Method 的输入输出接住，Results 的评价指标是否回应该 gap，Conclusion 是否只回收已有证据支持的 claim。
<!-- REAUDIT-INTEGRATED-2026-05-26:LOGIC END -->

## 8. 方法/理论/模型细拆

机翼模型：根弦 1000 mm，尖弦 360 mm，展长 540 mm，六边形翼型最大厚度 50 mm。结构包含硅橡胶涂层、超合金蒙皮和 C/C 高导热热传输路径。热传输路径由 6 Ma、15 km 条件下拓扑优化得到，根部设置 150 mm 热沉，温度 293 K。

数据生成：表面网格 1920 节点，初始传感器 60 个。训练工况由高度 5000/10000/15000/20000/25000 m，速度 2/3/4/5/6 Ma，攻角 0/4/8/12° 组成，共 100 组；其中 90 组训练，10 组 LHS 测试。总体温度范围约 305-2085 K，设计工况 6 Ma、15 km 约 912-1747 K。

POD：对温度场快照做分解，得到基准温度、脉动温度、相关矩阵和模态。文本显示初始传感器前 5 阶最大 RE 约 0.60%，`Td` 前 5 阶最大 RE 约 0.85%，`Tu` 前 10 阶最大 RE 约 0.95%；最终输出保留 12 阶时绝对误差小于 2.5 K、相对误差小于 1%。

BPNN：采用 tanh 激活、MSE 损失和 Bayesian regularization。超参数实验显示 epoch 3000 是精度与时间折中点；单隐层 20 神经元效果较好；输入/输出维度 5/12 时训练时间约 56.12 s，`Td/Tu` mMRE 约 0.015/0.068，MAE 约 0.103/0.560 K。

GA 传感器优化：目标综合 `Td` MRE、`Tu` MRE 和传感器数量。约束要求 MAE/AE 不超过初始布局。染色体由两部分组成：前 60 位二进制表示传感器是否启用，后 60 个 Gray 编码表示节点位置，每个节点号用 11 位表示。种群 30，迭代 30 代，变异概率 0.005/generation。

## 9. 证据系统与 Claim-Evidence 表

| Claim | Evidence | 论证功能 | 潜在限制 |
|---|---|---|---|
| POD 可大幅压缩温度场且损失小 | 初始传感器前 5 阶最大 RE 0.60%，`Td` 前 5 阶 0.85%，`Tu` 前 10 阶 0.95%；输出 12 阶误差 <2.5 K、<1% | 支撑降维不会破坏主要温度场信息 | POD 基于训练样本，外推工况可能失效 |
| BPNN 超参数需要系统调优 | epoch 从 1000 到 5000 对误差和时间有明显影响，3000 epoch 在精度和成本间折中；单隐层 20 神经元优于更宽/更深网络 | 证明不是简单套用神经网络 | 调参范围有限，随机种子影响未详述 |
| 输入/输出降维显著提升效率 | 输入/输出 5/12 时训练时间 56.12 s，mMRE 0.015/0.068；无输入降维 60/12 时训练 1170 s，且 `Td` 误差更高 | 支撑 POD+BPNN 的效率优势 | 高维输入是否经更强网络可改善未验证 |
| GA 能在保持精度下减少传感器 | Gen 23 有效个体使用 24 个传感器，mMRE 0.014/0.062，MAE 0.088/0.478；传感器减少 60% | 证明布局优化价值 | GA 结果对初始种群和随机性敏感 |
| 最终 POD-BPNN-GA 精度优于对比方法 | Table 9：POD-BPNN-GA 时间 70.95 s，mMRE 0.014/0.063，MAE 0.091/0.496；RF/RBFNN/CNN 误差显著更高 | 支撑方法优越性 | 对比模型调参深度可能不同 |
| 传感器布局具有物理解释性 | 优化后传感器聚集在外缘/后缘高温区域和热传输路径边缘高梯度区域 | 说明 GA 不只是数值搜索，也捕捉热物理关键区 | 布局图需 PDF 图像复核 |
| 反演误差在高温测试中仍较小 | 测试集 1 最大温度 426 K 时最大 AE 1.2 K、最大 RE 0.3%；高温测试集约 1500 K 时仍保持低误差 | 证明不同温度水平下鲁棒 | 具体误差云图需 PDF 图像复核 |

## 10. 图表、公式与结果叙事提取

| 类型 | 内容 | 论证功能 | 复核备注 |
|---|---|---|---|
| 3D wing geometry 图 | 根弦、尖弦、展长、六边形翼型、材料层 | 定义反演对象 | 需要 PDF 图像复核 |
| Heat transport path 图 | C/C 高导热路径与热沉位置 | 说明温度场空间结构来源 | 需要 PDF 图像复核 |
| 样本工况表 | 高度、速度、攻角组合 100 组，90/10 训练测试 | 交代数据覆盖范围 | 数值来自文本抽取 |
| POD 公式 | snapshot decomposition、相关矩阵、模态和系数 | 说明降维机制 | 公式编号需 PDF 核对 |
| POD 模态误差图/表 | 前 5/10/12 阶重构误差 | 决定降维阶数 | 需要 PDF 图像复核 |
| BPNN 结构图 | 输入 POD 特征、隐层、输出 POD 系数 | 展示映射模型 | 需要 PDF 图像复核 |
| Table 2 | epoch 对时间和误差的影响 | 选择 3000 epoch | 数值来自文本抽取 |
| Table 3 | 网络宽度/深度对误差的影响 | 选择单隐层 20 神经元 | 数值来自文本抽取 |
| Table 4 | 输入/输出维度对时间和误差的影响 | 选择 5/12 维组合 | 数值来自文本抽取 |
| GA 编码图 | 60 位启用标志 + 60 个 Gray 节点编码 | 说明传感器数量/位置如何同时优化 | 需要 PDF 图像复核 |
| 传感器布局图 | 初始 60、GA 24、RF top24 等布局 | 展示传感器向高温/梯度区聚集 | 需要 PDF 图像复核 |
| Table 9 | POD-BPNN-GA 与 RF/RBFNN/CNN 对比 | 最终方法优越性证据 | 数值来自文本抽取 |
| 温度/误差云图 | 测试集反演温度和误差分布 | 证明空间场重构质量 | 需要 PDF 图像复核 |

结果叙事很有层次：先证明 POD 可压缩，再证明 BPNN 参数选择，再证明 GA 可减少传感器，最后用多模型对比和云图展示最终方案优势。

## 11. 章节结构与篇章布局

文章结构大致为：

1. Introduction：温度场反演需求、有限传感器问题、机器学习与降维方法现状。
2. Wing thermal model and data generation：带热传输路径的 3D 翼模型、工况样本和传感器设置。
3. POD-BPNN inversion model：POD 降维、BPNN 映射、超参数设定。
4. GA sensor optimization：染色体编码、目标函数、约束和优化流程。
5. Results and discussion：POD 阶数、BPNN 参数、GA 布局、方法对比、测试集云图。
6. Conclusions：总结精度、传感器减少和方法优越性。

篇章布局是“数据对象 -> 降维模型 -> 学习模型 -> 传感器优化 -> 对比验证”。这种结构适合复合算法论文，因为每个模块都有自己的必要性和验证指标。

<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE START -->
### 复核补充：严格章节树与章节名功能

严格章节树：

- L2 p.1: 1 Introduction（背景定位/文献缺口）
- L2 p.3: 2 The wing and the TFI problem（问题定义）
  - L3 p.3: 2.1 The wing with HT paths and initial sensor layout（对象/模块/过渡章节）
  - L3 p.3: 2.2 Mathematical description of TFI problem（问题定义）
- L2 p.3: 3 Methodologies of the TFI model（方法/模型/算法）
  - L3 p.3: 3.1 POD-based data dimensionality reduction（对象/模块/过渡章节）
  - L3 p.5: 3.2 BPNN-based temperature field inversion（对象/模块/过渡章节）
  - L3 p.7: 3.3 GA-based sensor layout optimization（对象/模块/过渡章节）
- L2 p.7: 4 Creation of the TFI model（方法/模型/算法）
  - L3 p.7: 4.1 ROMs of temperature field data with POD method（方法/模型/算法）
  - L3 p.8: 4.2 TFI model construction with POD-BPNN method（方法/模型/算法）
    - L4 p.8: 4.2.1 The determination of max epochs（对象/模块/过渡章节）
    - L4 p.10: 4.2.2 The determination of width and depth（对象/模块/过渡章节）
    - L4 p.10: 4.2.3 The determination of data dimensionality（对象/模块/过渡章节）
  - L3 p.12: 4.3 Sensor layout optimization by GA（对象/模块/过渡章节）
- L2 p.12: 5 Comparison model with POD-RF method（方法/模型/算法）
  - L3 p.12: 5.1 RF-based temperature field inversion method（方法/模型/算法）
  - L3 p.14: 5.2 The construction of POD-RF model（方法/模型/算法）
    - L4 p.14: 5.2.1 The determination of regression trees（对象/模块/过渡章节）
    - L4 p.15: 5.2.2 The determination of minimum leaf size（对象/模块/过渡章节）
    - L4 p.15: 5.2.3 The determination of data dimensionality（对象/模块/过渡章节）
    - L4 p.15: 5.2.4 Sensor layout optimization（对象/模块/过渡章节）
- L2 p.15: 6 Results and discussions（结果/验证/讨论）
  - L3 p.15: 6.1 Comparison of performance（对象/模块/过渡章节）
  - L3 p.16: 6.2 Performance of POD-BPNN-GA model（方法/模型/算法）
  - L3 p.17: 6.3 Performance of POD-RF model（方法/模型/算法）
- L2 p.18: 7 Conclusions（结论/贡献回收）
- L2 p.18: CRediT authorship contribution statement（尾部材料）
- L2 p.18: Declaration of competing interest（尾部材料）
- L2 p.18: Acknowledgements（尾部材料）
- L2 p.18: Data availability（尾部材料）
- L2 p.18: References（尾部材料）

章节名功能表：

| 章节/小节名 | 页码 | 层级 | 功能判断 |
| --- | ---: | ---: | --- |
| 1 Introduction | 1 | 2 | 背景定位/文献缺口 |
| 2 The wing and the TFI problem | 3 | 2 | 问题定义 |
| 2.1 The wing with HT paths and initial sensor layout | 3 | 3 | 对象/模块/过渡章节 |
| 2.2 Mathematical description of TFI problem | 3 | 3 | 问题定义 |
| 3 Methodologies of the TFI model | 3 | 2 | 方法/模型/算法 |
| 3.1 POD-based data dimensionality reduction | 3 | 3 | 对象/模块/过渡章节 |
| 3.2 BPNN-based temperature field inversion | 5 | 3 | 对象/模块/过渡章节 |
| 3.3 GA-based sensor layout optimization | 7 | 3 | 对象/模块/过渡章节 |
| 4 Creation of the TFI model | 7 | 2 | 方法/模型/算法 |
| 4.1 ROMs of temperature field data with POD method | 7 | 3 | 方法/模型/算法 |
| 4.2 TFI model construction with POD-BPNN method | 8 | 3 | 方法/模型/算法 |
| 4.2.1 The determination of max epochs | 8 | 4 | 对象/模块/过渡章节 |
| 4.2.2 The determination of width and depth | 10 | 4 | 对象/模块/过渡章节 |
| 4.2.3 The determination of data dimensionality | 10 | 4 | 对象/模块/过渡章节 |
| 4.3 Sensor layout optimization by GA | 12 | 3 | 对象/模块/过渡章节 |
| 5 Comparison model with POD-RF method | 12 | 2 | 方法/模型/算法 |
| 5.1 RF-based temperature field inversion method | 12 | 3 | 方法/模型/算法 |
| 5.2 The construction of POD-RF model | 14 | 3 | 方法/模型/算法 |
| 5.2.1 The determination of regression trees | 14 | 4 | 对象/模块/过渡章节 |
| 5.2.2 The determination of minimum leaf size | 15 | 4 | 对象/模块/过渡章节 |
| 5.2.3 The determination of data dimensionality | 15 | 4 | 对象/模块/过渡章节 |
| 5.2.4 Sensor layout optimization | 15 | 4 | 对象/模块/过渡章节 |
| 6 Results and discussions | 15 | 2 | 结果/验证/讨论 |
| 6.1 Comparison of performance | 15 | 3 | 对象/模块/过渡章节 |
| 6.2 Performance of POD-BPNN-GA model | 16 | 3 | 方法/模型/算法 |
| 6.3 Performance of POD-RF model | 17 | 3 | 方法/模型/算法 |
| 7 Conclusions | 18 | 2 | 结论/贡献回收 |
| CRediT authorship contribution statement | 18 | 2 | 尾部材料 |
| Declaration of competing interest | 18 | 2 | 尾部材料 |
| Acknowledgements | 18 | 2 | 尾部材料 |
| Data availability | 18 | 2 | 尾部材料 |
| References | 18 | 2 | 尾部材料 |
<!-- REAUDIT-INTEGRATED-2026-05-26:STRUCTURE END -->

## 12. 段落功能与叙事节奏

引言先讲全局温度场的重要性，再讲有限传感器的测量约束，随后引入机器学习和传感器优化。它不是一上来讲 BPNN，而是先建立“为什么需要反演”的工程场景。

方法段落按数据流展开：有限传感器温度 `Ts` 进入 POD-BPNN，输出全局温度 `Tu` 或设计温度 `Td` 的 POD 系数，再重构温度场。读者能沿着输入输出跟踪模型。

结果段落的节奏是先局部调参、再整体优化。POD 阶数、epoch、宽度/深度、维度这些小实验先把模型确定下来；GA 和对比模型再证明最终组合方法有效。这样避免了“黑箱神经网络直接给结果”的印象。

## 13. 文笔画像与语言习惯

本文文风偏机器学习工程应用，常见词包括 “temperature field inversion”, “limited sensors”, “principal features”, “mean relative error”, “sensor layout”, “genetic algorithm”。句子较直接，强调数值指标和对比。

语言习惯：

- “The POD method is adopted to reduce the dimensionality of...”
- “The BPNN is trained to establish the mapping relationship between...”
- “The GA is used to optimize the number and locations of sensors...”
- “Compared with RF/RBFNN/CNN, the proposed method achieves...”
- “The optimized sensors are mainly distributed in...”

文章的语言重心是“enhanced”：增强体现在不是单一网络，而是 POD、BPNN 和 GA 共同降低维度、提升精度、减少传感器。

<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE START -->
### 复核补充：正文词频、词类、语态与时态

统计口径：仅正文主章节；不含摘要、References、图表题注、页眉页脚、版权/期刊信息和任何分析报告文本。

- 正文统计字符数：43149
- 高频词：method(71)；data(69)；model(68)；temperature(66)；sensor(48)；performance(47)；inversion(41)；training(35)；case(34)；dimensionality(32)；input(32)；field(30)；layout(30)；number(28)；optimization(26)；pod(26)；obtained(25)；sensors(24)；tfi(23)；regression(22)
- 高频名词化/学术名词：temperature(66)；performance(47)；inversion(41)；dimensionality(32)；optimization(26)；regression(22)；importance(20)；feature(15)；influence(13)；reduction(12)；construction(9)；function(9)；section(9)；reconstruction(8)；information(8)
- 高频学术动词：construct(7)；constructed(7)；optimize(5)；compared(5)；developed(4)；optimized(4)；indicate(4)；analyzed(3)；compare(3)；provide(2)；reveal(2)；evaluate(2)；analyze(2)；predict(1)；derive(1)
- 高频形容词：initial(15)；optimal(15)；variable(9)；neural(8)；independent(8)；coefficient(7)；thermal(7)；different(7)；relative(6)；objective(6)；represent(6)；total(6)；less(6)；orthogonal(5)；subsequent(5)
- 高频副词：significantly(5)；additionally(4)；slightly(4)；simultaneously(3)；effectively(3)；generally(3)；relatively(3)；similarly(3)；mainly(3)；randomly(3)；fully(2)；greatly(2)；particularly(2)；possibly(2)；finally(2)
- 高频二词短语：temperature field(27)；sensor layout(23)；sensor data(13)；tfi model(12)；pod method(12)；data dimensionality(11)；initial sensor(11)；regression trees(11)；inversion performance(10)；training time(10)；tfi problem(9)；field data(9)
- 高频三词短语：initial sensor layout(9)；temperature field data(8)；minimum leaf size(8)；sensor layout optimization(6)；independent repeated training(5)；repeated training runs(5)；temperature field inversion(4)；dimensionalities input output(4)；average value independent(4)；number regression trees(4)；input output dimensionalities(4)；regions high errors(4)
- 被动语态估计：144；`we + 动作动词` 主动句估计：0
- 一般现在时线索：286；一般过去时线索：288；现在完成时线索：0；情态动词线索：64

分章节正文词频：

- 1 Introduction: temperature(13)；data(10)；field(9)；model(7)；inversion(6)；tfi(6)；heat(5)；sensor(5)
- 2 The wing and the TFI problem: wing(13)；model(12)；temperature(11)；optimization(9)；problem(8)；heat(7)；thermal(7)；data(7)
- 3 Methodologies of the TFI model: data(14)；temperature(12)；matrix(11)；mode(10)；sensor(10)；number(10)；field(9)；optimization(8)
- 4 Creation of the TFI model: data(18)；performance(18)；sensor(17)；training(15)；input(15)；case(15)；temperature(13)；output(13)
- 5 Comparison model with POD-RF method: method(23)；model(23)；regression(19)；importance(18)；features(16)；trees(15)；data(15)；feature(14)
- 6 Results and discussions: method(16)；performance(11)；inversion(9)；model(8)；layout(8)；cnn(7)；case(7)；nodes(7)
- 7 Conclusions: model(6)；temperature(6)；sensors(6)；method(5)；data(5)；performances(4)；field(3)；dimensionality(3)
<!-- REAUDIT-INTEGRATED-2026-05-26:LANGUAGE END -->

## 14. 常用词、句式与可复用表达提取

可复用关键词：

- temperature field inversion
- limited sensors
- proper orthogonal decomposition
- back propagation neural network
- genetic algorithm
- sensor layout optimization
- heat transport path
- mean relative error
- mean absolute error
- dimensionality reduction

可复用句式：

- “The high-dimensional temperature field is projected onto a low-dimensional POD subspace before training the neural network.”
- “The sensor layout is optimized by balancing inversion accuracy and measurement cost.”
- “The optimized sensors tend to be located in high-temperature and high-gradient regions, which provides a physical explanation for the data-driven result.”
- “The comparison with RF, RBFNN and CNN demonstrates that the proposed framework is more suitable for small-sample high-dimensional field inversion.”
- “Dimensionality reduction improves both computational efficiency and generalization performance.”

中文可复用表达：

- “温度场反演的关键不是把传感器越铺越密，而是在最有信息量的位置获取最少但最有效的观测。”
- “POD 在这里承担的是把场变量从像素级输出转化为模态系数输出的桥梁作用。”

<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES START -->
### 复核补充：多句型库

以下句型来自该论文的摘要、引言和结论，不从分析报告或 References 中抽取。

#### 背景/问题定位句
- 原句：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
  可迁移模板：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
- 原句：The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4].
  可迁移模板：The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [X–X], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [X].
- 原句：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
  可迁移模板：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
#### Gap/转折句
- 原句：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
  可迁移模板：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
- 原句：The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
  可迁移模板：The METHOD problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [X,X,X].
- 原句：Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
  可迁移模板：Liu et al. [X] introduced the physics-informed neural network method to solve the METHOD problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
- 原句：Lu et al. [4] proposed a 3D TFI model based on NN to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.
  可迁移模板：Lu et al. [X] proposed a METHOD METHOD model based on METHOD to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.
#### 方法提出句
- 原句：In this work, a temperature field inversion model combining real sensor data is developed for a 3D aircraft wing structure with heat transport paths.
  可迁移模板：In this work, a temperature field inversion model combining real sensor data is developed for a METHOD aircraft wing structure with heat transport paths.
- 原句：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
  可迁移模板：The model is trained by the Back Propagation Neural Network method with optimized critical hyperparameters, i.e., max epochs, width, depth and data dimensionality.
- 原句：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
  可迁移模板：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 原句：A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient region.
  可迁移模板：A hybrid genetic algorithm is proposed to optimize the sensor locations and numbers simultaneously with integrated considerations of inversion error and cost, and the model performance is greatly enhanced by gathering sensors to high temperature gradient region.
- 原句：The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.
  可迁移模板：The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of X, METHOD and X, respectively and the advantages of the METHOD model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.
#### 结果呈现句
- 原句：The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of 0.063 %, 0.496 K and 60 %, respectively and the advantages of the TFI model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.
  可迁移模板：The test results indicate great performance with the mean relative inversion error, the mean absolute inversion error and the sensor number reduction of X, METHOD and X, respectively and the advantages of the METHOD model are verified by the comparison with Random Forest, Radial Basis Function Neural Network and Convolutional Neural Network methods.
- 原句：With the development of artificial intelligence, machine learning methods such as Neural Networks (NN) and Random Forest (RF) have shown great * Corresponding author.
  可迁移模板：With the development of artificial intelligence, machine learning methods such as Neural Networks (METHOD) and Random Forest (METHOD) have shown great * Corresponding author.
#### 贡献/增量句
- 原句：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
  可迁移模板：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 原句：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
  可迁移模板：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
- 原句：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
  可迁移模板：The pre-generated sample temperature fields are fully decomposed into proper orthogonal modes, the principal features are extracted to form matched data dimensionality, and the model construction efficiency is significantly improved with very little accuracy compromise.
- 原句：Niu et al. [17] proposed an approach of light field compression and noise reduction to extract the main features of the projection matrix and improve the performance of 3D temperature field reconstruction.
  可迁移模板：Niu et al. [X] proposed an approach of light field compression and noise reduction to extract the main features of the projection matrix and improve the performance of METHOD temperature field reconstruction.
- 原句：The BPNN method is used to realize the inversion of temperature field, and the efficiency is improved with the reducedorder samples.
  可迁移模板：The METHOD method is used to realize the inversion of temperature field, and the efficiency is improved with the reducedorder samples.
#### 限制/边界句
- 原句：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
  可迁移模板：Accurate inversion of global temperature is crucial to the state evaluation of high-speed aircraft since the real data can only be acquired by very limited local sensors.
- 原句：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
  可迁移模板：At present, the real temperature can be measured by sensors which only provide local data, while the global temperature field can be obtained by numerical simulations which necessarily include certain deviations.
- 原句：The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
  可迁移模板：The METHOD problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [X,X,X].
- 原句：Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
  可迁移模板：Liu et al. [X] introduced the physics-informed neural network method to solve the METHOD problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
- 原句：Lu et al. [4] proposed a 3D TFI model based on NN to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.
  可迁移模板：Lu et al. [X] proposed a METHOD METHOD model based on METHOD to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.
<!-- REAUDIT-INTEGRATED-2026-05-26:SENTENCES END -->

## 15. 引用策略与文献使用

引用策略应是三段式：先引用高速飞行器热防护与温度监测文献，说明全场温度的重要性；再引用温度场反演和机器学习文献，说明已有数据驱动方法；最后引用 POD 降阶和传感器优化文献，说明本文组合方法的基础。

这篇论文的引用作用主要是给组合式方法找位置。单独的 POD、BPNN 或 GA 并不新，所以文献使用需要证明：已有方法很少在带热传输路径 3D 翼、有限传感器、低维反演和传感器数量优化四者同时成立的场景中系统验证。

<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS START -->
### 复核补充：引文密度、References 与 gap 构造

- 全文引文簇数量估计：73
- Introduction 引文簇数量估计：9
- References 条目数：42
- 可识别年份条目数：67
- 2021 年及以后文献数：45
- 2010 年前经典文献数：8
- 同刊引用数（按 subject 粗匹配）：0
- 高频来源期刊：未稳定识别
- 引文簇样例：[16], [17], [4], [8], [4], [4,8,9], [10], [11], [12], [18], [34], [19]

带引文的 gap/转折句样例：

- The extreme aerodynamic force and heat effect brings great challenges to high-speed aircraft structures [1–3], and the accurate acquisition of structural states such as temperature field is crucial to its state and performance evaluations [4].
- The TFI problem studied in this paper focuses on the reconstruction of temperature field based on the limited sensor data of structures [4,8,9].
- Liu et al. [8] introduced the physics-informed neural network method to solve the TFI problem with limited observations, and developed a coefficient matrix condition number based position selection of observations method to alleviate the noises effect in observations.
- Lu et al. [4] proposed a 3D TFI model based on NN to predict the heat transfer boundary conditions of a hexahedral geometry from limited surface sensors.

References 解析样例（前 8 条）：

- 7. Conclusions
In this work, the TFI model based on POD-BPNN-GA method is constructed to invert the temperature field of a 3D wing with HT paths. The POD method is introduced to project the sample data into proper orthogonal modes, and the principal features are extracted to reduce the data dimensionality. The BPNN method is used to realize the inversion of temperature field, and the efficiency is improved with the reducedorder samples. A hybrid optimization approach based on GA is developed to optimize the sensors numbers and locations simultaneously, and the optimal layout obtains better performance with the sensors gathering to high temperature gradient region. Compared with models based on RF, RBFNN and CNN methods, the TFI model proposed in this paper obtains superior performance. The conclusions are as follows:
(1) The POD method effectively converts high-dimensional temperature data into low-dimensional modal coefficients, simplifying analysis while retaining the principal features of data. The dimensionality of temperature field data in this paper is reduced from 1920 to 12, with an absolute error of less than 2.5 K and a relative error of less than 1 %. (2) For the initial layout with 60 sensors and the input dimensionality of 5, the performances of POD-BPNN model are m-MREs of 0.015 % and 0.068 %, m-MAEs of 0.103 K and 0.560 K for Td and Tu, respectively. The performances of POD-RF model are m-MREs of 2.535 % and 3.208 %, m-MAEs of 13.96 K and 20.35 K for Td and Tu, respectively. (3) The optimal layout obtained by GA includes 24 sensors gathering to high temperature and high gradient regions. For the RF method, the top 24 sensors ranked by importance are concentrated in the regions with maximum and minimum temperatures. (4) With the optimal parameters and sensors, the performances of POD-BPNN-GA model are m-MREs of 0.014 % and 0.063 %, mMAEs 0.091 K and 0.496 K for Td and Tu, respectively. The performances of POD-RF model are m-MREs of 0.601 % and 1.205 %, m-MAEs of 4.600 K and 11.47 K for Td and Tu, respectively.
CRediT authorship contribution statement
Jia-Xin Hu: Writing – original draft, Visualization, Methodology, Investigation, Formal analysis, Conceptualization. Jian-Jun Gou: Writing – review & editing, Supervision, Funding acquisition. Chun-Lin Gong: Supervision, Resources, Project administration, Conceptualization.
Declaration of competing interest
The authors declare that they have no know competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
J.-X. Hu et al. International Communications in Heat and Mass Transfer 164 (2025) 108778
Acknowledgements
This study is supported by the National Natural Science Foundation of China (51806175).
Data availability
Data will be made available on request.
References
- [1] O. Uyanna, H. Najafi, Thermal protection systems for space vehicles: a review on technology development, current challenges and future prospects, Acta Astronaut. 176 (2020), https://doi.org/10.1016/j.actaastro.2020.06.047.
- [2] G. Lu, Z. Shi, R. Zhang, Y. Li, K. Zhang, Probabilistic design and optimization of thermal protection system with variable thickness based on non-uniform aerodynamic heating, Int. J. Heat Mass Transf. 225 (2024), https://doi.org/ 10.1016/j.ijheatmasstransfer.2024.125386.
- [3] J.-J. Gou, S.-Z. Jia, J.-X. Li, S. Xiao, C.-L. Gong, The determination of physical dimensions of a hypersonic three-stage compression system considering panel vibration effects, Aerosp. Sci. Technol. 140 (2023) 108431, https://doi.org/ 10.1016/j.ast.2023.108431.
- [4] D. Lu, C. Wang, Three-dimensional temperature field inversion calculation based on an artificial intelligence algorithm, Appl. Therm. Eng. 225 (2023), https://doi. org/10.1016/j.applthermaleng.2023.120237.
- [5] M.T. Hughes, G. Kini, S. Garimella, Status, challenges, and potential for machine learning in understanding and applying heat transfer phenomena, J. Heat Transf. 143 (2021), https://doi.org/10.1115/1.4052510.
- [6] S.L. Brunton, J.N. Kutz, K. Manohar, A.Y. Aravkin, K. Morgansen, J. Klemisch, N. Goebel, J. Buttrick, J. Poskin, A.W. Blom-Schieber, T. Hogan, D. McDonald, Data-driven aerospace engineering: reframing the industry with machine learning, AIAA J. 59 (2021), https://doi.org/10.2514/1.J060131.
- [7] H. Chen, X. Tang, Z. Liu, Z. Liu, H. Zhou, Predicting the temperature field of thermal cloaks in homogeneous isotropic multilayer materials based on deep learning, Int. J. Heat Mass Transf. 219 (2024), https://doi.org/10.1016/j. ijheatmasstransfer.2023.124849.
<!-- REAUDIT-INTEGRATED-2026-05-26:CITATIONS END -->

## 16. 审稿人视角风险

1. 数据来源风险：训练和测试均来自数值仿真，缺少风洞、热试验或飞行测温验证。
2. 传感器噪声风险：实际传感器有噪声、漂移、热惯性和安装误差，文中未充分纳入。
3. 外推风险：训练工况为离散高度、速度、攻角组合，对飞行包线外或中间强非线性工况的泛化不确定。
4. 样本量风险：100 组样本、90 组训练相对较小，神经网络结果可能对样本划分敏感。
5. 对比公平性风险：RF/RBFNN/CNN 的结构和调参深度可能影响结论，CNN 在小样本场景下天然吃亏。
6. 工程安装风险：优化传感器位置位于高温/高梯度区，实际布线、耐温、维护和结构影响未讨论。

## 17. 可复用资产

可复用工作流：

1. 构建高保真热仿真模型。
2. 在代表性工况下生成温度场快照。
3. 对输入传感器温度和输出全场温度分别做 POD。
4. 选择低维 POD 系数作为神经网络输入输出。
5. 系统调参确定网络结构和降维阶数。
6. 以误差和传感器数量为目标优化布局。
7. 与传统机器学习模型和不同布局方法对比。
8. 用温度云图、误差云图和统计指标共同验证。

可复用指标：

- MRE / mMRE
- MAE
- AE / RE 分布
- training time
- sensor reduction ratio
- POD reconstruction error
- layout physical interpretability

可复用图表：

- 工况样本矩阵。
- POD 阶数误差表。
- BPNN 超参数表。
- 传感器优化代际表。
- 多模型对比表。
- 真实/预测/误差温度场云图。

## 18. 对我写论文的启发

这篇论文的启发是，组合算法论文要把每个模块的“必要性”证明出来。POD 不是装饰，因为直接高维输入会使训练时间从 56 s 级变成 1170 s；GA 不是装饰，因为它把传感器从 60 减到 24 且误差不升；BPNN 不是随意选择，因为作者用 RF/RBFNN/CNN 对比证明它在该数据结构下更合适。

第二个启发是传感器优化结果最好有物理解释。若优化点集中在高温区和热路径边缘，读者会更容易相信模型捕捉了热传输机制，而不是只是在训练集上过拟合。

第三个启发是小样本高维场反演可以优先考虑“先降维再学习”，不要让神经网络直接承担从低维测量到高维场的全部压力。

## 19. 最终浓缩

本文提出 POD-BPNN-GA 温度场反演框架，用有限传感器重构带热传输路径的 3D 高速翼全局温度场。POD 将 1920 节点温度场压缩为少量主模态，BPNN 学习传感器特征到全场 POD 系数的非线性映射，GA 同时优化传感器数量和位置。经过超参数和维度优化后，最终方案使用 24 个传感器，相比初始 60 个减少 60%，仍达到 `Tu` MRE 约 0.063%、MAE 约 0.496 K，并显著优于 RF、RBFNN 和 CNN 对比方法。论文的核心价值在于把有限测量、降阶表示、非线性映射和传感器成本统一到一个可验证的温度场反演流程中。
