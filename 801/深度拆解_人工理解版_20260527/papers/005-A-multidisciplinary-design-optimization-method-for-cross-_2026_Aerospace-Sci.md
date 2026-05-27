## 1. 身份层

这是一篇跨域飞行器多学科设计优化方法论文，题名为 “A multidisciplinary design optimization method for cross-domain vehicles based on distributed-centralized augmented Lagrangian coordination”。metadata 中作者为空；论文主题是用分布式-集中式增强拉格朗日协调策略求解几何、气动、结构、轨迹、热防护和质量等强耦合 MDO 问题。

材料读取边界：本报告读取了 `metadata.json`、`abstract.txt`、`clean_body.md`、`figure_captions.txt`、`table_captions.txt`、`tables/*.md`、`equations.txt`、`references.txt`。核心文件均存在；明显抽取问题包括正文中出现误抽的 `## Table 6`，部分轨迹/ALC 公式 OCR 噪声较大，metadata 作者缺失。

论文的对象是 X-37B-like cross-domain vehicle，任务涉及大气层内、跨大气层和再入段。它不是单一外形优化论文，而是把 3D CST 几何参数化、气动/结构协同建模、轨迹/TPS/质量估算和 MDO 协调算法整合到同一设计流程中。

## 2. 主张层

中心主张是：跨域飞行器的学科耦合强、单学科计算耗时高，传统 MDF 或现有 ALC 分解方式要么串行低效，要么过度解耦导致收敛困难；本文提出的 distributed-centralized augmented Lagrangian coordination 可以在保持并行性的同时减少一致性约束误差，提高求解效率和优化质量。

摘要中的主张包含两部分。方法侧，作者提出基于增强拉格朗日协调的 nested MDO，并建立 3D CST 驱动的几何-气动-结构联合参数化模型。效果侧，在 X37-like cross-domain vehicle 上以 payload mass 为目标，优化后 payload mass 增加 70.2%。

结论部分把方法收益落到工程量：相对 MDF，综合性能提升约 19.8%；payload mass 从约 454 kg 增到 772.5 kg，增加 318.5 kg；结构质量下降 143.45 kg；结构、气动、轨迹等学科共同决定最终结果，而不是单变量局部优化。

## 3. 选题层

选题针对的是跨域飞行器设计中“高耦合+高成本”的典型痛点。再入和跨域任务要求外形、热防护、承载结构、轨迹和质量同时满足约束，任何单学科优化都容易把问题推给其他学科，导致全局最优丢失。

作者没有只做一个新的优化器，也没有只做一个外形参数化工具，而是把两者结合起来：一方面用 3D CST 消除几何、气动网格和结构网格之间的转换割裂；另一方面用新的 ALC 协调策略处理学科间一致性约束。这让选题既有算法贡献，也有工程流程贡献。

选题的现实吸引力在于 payload mass。跨域飞行器优化若只谈阻力、升阻比或结构应力，读者可能难以判断系统价值；以有效载荷质量作为总目标，可以把气动、结构、TPS 和轨迹变化统一到一个航天任务指标下。

## 4. 位置层

论文在 MDO 文献中的位置是对 CO、CSSO、BLISS、ATC、传统 ALC、distributed ALC、distributed parallel ALC、centralized ALC 和 dominant ALC 等分解策略的折中。它承认增强拉格朗日协调已有收敛优势，但指出已有分布式/集中式变体在并行效率、一致性约束数量和协调成本之间存在冲突。

本文提出的 distributed-centralized ALC 试图把“较强耦合变量集中协调”和“耗时学科分布式并行”结合起来。它不像完全分布式方法那样把变量全部拆开，也不像集中式方法那样让 master problem 承担过重耦合。

在工程建模文献中的位置则依赖 3D CST。作者把 CST 从外形表示扩展到气动网格和结构网格生成，使几何变化能同步传给多个学科模型。这个位置支撑了 MDO 的可执行性，否则算法只停留在抽象协调框架。

## 5. 贡献层

第一项贡献是建立跨域飞行器的 3D CST 几何-气动-结构联合参数化模型。外形参数变化可以直接驱动气动面、结构网格和质量估算，减少传统 CAD/网格转换中的手工步骤。

第二项贡献是提出 distributed-centralized ALC 模型和自适应异步乘子更新策略。该策略把较大耦合拆成 master part 和 subproblem part，并用不同更新规则处理快/慢收敛约束，目标是在精度和并行效率之间取得平衡。

第三项贡献是用数学算例比较五种 ALC 变体，显示 proposed distributed-centralized ALC 在迭代次数、误差和时间上取得较优折中。文中称其相对 dominant/centralized 和 distributed/distributed parallel 方法降低一致性误差，且保持较好计算效率。

第四项贡献是完成 X37-like 飞行器 MDO 应用。优化变量包括头体、翼面、厚度等几何参数，约束包括热载荷、翼展、应力、变形等，目标为有效载荷质量最大化。最终 payload mass 增加 70.2%，给出结构质量、TPS 质量、应力变形和轨迹变化的系统解释。

## 6. 方法层

方法输入包括任务需求、初始 X37-like 外形、3D CST 几何设计变量、气动/结构/轨迹/TPS/质量学科模型、学科耦合变量和约束。输出是满足热、结构、几何与轨迹约束的优化外形和质量分配。

建模流程先由 3D CST 生成几何；气动模块由参数化表面和网格计算升阻特性，文中与文献结果比较误差约 4%；结构模块由同一几何生成结构网格并计算应力/变形；轨迹模块使用 3DOF 方程并约束热流、动压和过载；TPS 和质量模块用估算公式闭合任务指标。

协调算法把一般 MDO 问题转化为带辅助变量和一致性约束的问题，再用增强拉格朗日项放松约束。distributed-centralized ALC 的关键是选择强耦合变量进行集中协调，同时允许耗时学科作为分布式子问题并行求解。乘子更新采用自适应异步策略，根据约束收敛速度调整。

优化应用中还加入敏感性分析。作者用 correlation、regression、Sobol 和神经网络等方法识别重要变量，发现 head-body joint shape factor、wing thickness、head shape factor 对目标更敏感，从而帮助解释优化结果而不是只给最终数值。

## 7. 证据层

图 1 展示跨域飞行器任务剖面，图 2 展示参数化网格，图 3 是学科 DSM，三者共同说明问题确实是多学科耦合。图 4 和图 5 给出 ALC 模型与求解流程，是算法贡献的核心图。

数学算例证据集中在图 6 到图 9 和对应表格。它通过同一问题下五种 ALC 方法的 objective iteration、time、consistency convergence 对比，证明 proposed distributed-centralized ALC 不是只在工程算例中“看起来有效”，而是先在可控算例中展示收敛行为。

工程优化证据包括图 10、图 11 的敏感性结果，图 12 的 MDO 流程，图 13 的目标历史，图 14 的外形变化，图 15 的应力/变形云图和图 16 的轨迹曲线。表格给出质量分解、设计变量范围、敏感性排行和优化前后结果。

结果数值最直接的证据是 payload mass 从约 454 kg 增至 772.5 kg，增加 318.5 kg；结构质量下降约 143.45 kg；最大应力约 5.914e7 Pa，最大变形约 2.487e-3 m，满足约束。轨迹结果显示优化后早期减速更快、后段轨迹更平缓，说明质量/气动变化没有破坏任务可行性。

## 8. 结构语言层

文章结构偏系统工程：先讲 cross-domain vehicle 和任务需求，再讲几何/气动/结构联合建模，之后讲其他学科和 DSM，接着引入 distributed-centralized ALC，最后用数学算例和真实飞行器算例验证。结构上先“建可算系统”，再“放优化算法”，最后“证明工程收益”。

语言上，作者不断使用 “balance efficiency and parallel computation”“adaptive asynchronous multiplier update”“joint geometric/aerodynamic/structural parametric modeling” 等组合词，目的在于把论文从单纯优化算法扩展成可落地的 MDO framework。

可复用的表达策略是用 payload mass 统摄多学科结果。气动、结构、TPS 和轨迹各自有指标，但最终都落到有效载荷这个任务指标上，读者更容易理解优化为什么有价值。

抽取层面风险较高。正文中误抽出一个 `Table 6` 作为二级标题，轨迹方程和 ALC 更新公式有乱码，部分表格列名错位。当前 markdown 足以理解论文逻辑和主要数值，但不适合直接复写算法公式。

## 9. 引用风险层

引用链覆盖 MDO 分解方法、增强拉格朗日协调、CST 参数化、跨域/可重复使用飞行器设计、质量估算和轨迹优化。作为“跨域飞行器 MDO 框架”引用是合适的，尤其适合放在强耦合系统优化和 ALC 变体讨论中。

主要风险是工程模型精度。气动、结构、TPS、质量和轨迹模型中部分属于工程估算或简化模型；payload mass 增加 70.2% 是在该模型体系内成立，不应被写成真实飞行器设计的无条件收益。

第二个风险是算法对分解方式选择敏感。distributed-centralized ALC 的效果依赖哪些变量集中、哪些变量分布式、乘子如何更新。若换一个学科耦合结构，收益可能不同。

第三个风险是数据可得性。文中 Data availability 表述为数据可按请求提供，且当前抽取中公式和表格噪声明显；若要复现，不能只依赖 cleantext。

## 10. 复用层

可复用的选题模板是：在复杂飞行器 MDO 中，不要只强调“优化算法更快”，而要同时说明几何-气动-结构数据链如何打通，以及系统目标如何把学科指标合并。

可复用的方法链是：`unified geometry parameterization -> discipline models -> DSM coupling analysis -> ALC decomposition -> adaptive multiplier update -> benchmark comparison -> mission-level MDO demonstration`。

可复用的证据结构是先用数学算例验证协调算法，再用真实工程算例验证系统收益。这样可以避免审稿人质疑工程算例太复杂、无法看清算法本身贡献。

自检：本报告未增设十层之外的并列标题；摘要、结论、图表、公式、引用风险和抽取问题均收进十层。明显抽取问题为 spurious `Table 6` 标题、公式 OCR 噪声、metadata 作者缺失和部分表格错位。
