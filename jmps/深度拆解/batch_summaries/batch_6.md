# Batch 6 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/The-out-of-plane-bifurcation-and-narrow-stability_2026_Journal-of-the-Mechan.md`
- `jmps/深度拆解/papers/The-strange-mechanics-of-an-elastic-rod-unde_2026_Journal-of-the-Mechanics-a.md`
- `jmps/深度拆解/papers/Thermo-chemo-mechanical-modeling-and-parameter_2026_Journal-of-the-Mechanics.md`
- `jmps/深度拆解/papers/Thermodynamic-phase-field-method-for-simul_2026_Journal-of-the-Mechanics-and.md`
- `jmps/深度拆解/papers/Uniqueness-of-solutions-in-high-energy-x-ray-based--eige_2026_Journal-of-the.md`
- `jmps/深度拆解/papers/Unveiling-scaling-laws-for-wrinkling-in-compress_2026_Journal-of-the-Mechani.md`

本批 6 篇均已按深度拆解模板写入，覆盖 `## 0` 到 `## 19` 的全部二级标题，并包含 Claim-Evidence 表、图表/公式功能表、文笔画像、常用句式骨架、引用策略、审稿风险和可迁移写法。所有仅能从 TXT 图注判断的图像细节均标注为需结合 PDF 图像核查。

## 本批论文的共同特征
- 都不是单纯“报告结果”的论文，而是围绕一个可检验的力学主张建立说服闭环：临界值、反常识载荷、热-化-力模型、相场机制、逆问题唯一性、双 regime 标度律。
- JMPS 风格很明显：问题边界通常收得很窄，但证据链要求很硬。即使应用背景很广，正文也会落到一个明确的模型、临界条件、参数识别流程或唯一性定理上。
- 多数论文都在修正或约束已有认识：Euler-Plateau 修正数值临界值；横向零合力载荷修正常识直觉；eigenstrain tomography 限制少分量反演；wrinkling 标度律限制经典高失配公式适用域。
- 本批常见证据形态是“理论推导 + 数值/图谱/验证补强”，而不是大规模实验统计。实验出现时，多承担验证或校准角色。
- 章节组织倾向于先建立严密对象，再给机制或适用域。好的论文都会把抽象结果翻译成可观测量、实验要求或使用规则。

## 本批最值得学习的 5 个写法
1. 用“前人已有但不够适定/不够精确/不够全域”制造高质量 gap。典型如 eigenstrain tomography 的唯一性、Euler-Plateau 的出平面临界值、wrinkling 的任意 mismatch 标度律。
2. 把核心结果压缩成一个容易记忆的判据或数字：`nu_crit≈3.7402`、`Ta + Tt`、三分量最低要求、direct/dual scaling、transition mismatch。
3. 反常识或负结果论文要给建设性出口。Bigoni 的论文用多模型和实验验证正向新机制；Wensrich 的论文在否定单分量后给三分量和对角 eigenstrain 条件。
4. 复杂模型论文要把参数识别写成贡献。环氧固化论文的亮点不是只建方程，而是把实验矩阵、Maxwell 参数唯一性和 FE 验证打通。
5. 标度律/相场论文要配适用域和机制图谱。wrinkling 论文用 regime map，水泥水化论文用局部场解释热流阶段，这比单独给公式更可迁移。

## 本批最常见的审稿风险
- 模型边界与强 claim 不完全匹配：二维相场能否支撑早龄期性质预测，SRM 标度律能否外推真实组织，固化本构能否外推未验证机械加载。
- 图像和曲线是关键证据，但 TXT 无法核查视觉细节。需要人工确认误差棒、曲线重合度、相图区域、模态形态和实验装置细节。
- 复杂参数模型存在可识别性和过拟合风险，尤其是多 Maxwell 元件、shift 函数、相场参数和纤维本构参数。
- 理论结果对假设敏感：星形参数化、dead-load 实现、各向同性弹性、半无限基底、完美粘结、零牵引边界等。
- 部分论文缺少直接实验验证，依赖数值对比或定性趋势。写作中应把“mechanistic demonstration”和“quantitative prediction”区分开。

## 可沉淀到 JMPS 写作模板的规律
- Introduction 可按“现象/应用 -> 经典解释 -> 最近进展 -> 未闭合条件 -> 本文精确处理”组织，比泛泛背景更有效。
- 对理论论文，摘要应明确写出：控制参数、已知临界/旧公式、本文方法、新临界/新公式、物理后果。
- Claim-Evidence 最好对应到图、公式或定理，而不是只对应段落。JMPS 读者通常会追问每个强 claim 的数学或实验支点。
- Discussion 的高价值做法是把公式转换成实验或设计语言：半径差、最低扫描分量、选择哪套标度律、哪些参数需校准。
- 局限不要写成客套话，应紧贴模型边界：二维到三维、onset 到 post-buckling、ideal full-field 到 noisy tomography、calibration 到 independent validation。

## 需要后续人工图像核查的内容
- Euler-Plateau：Fig. 4-7 的临界值、收敛性和模态形态；Fig. 10-12 的能量分解和非凸区域贡献。
- 横向零合力载荷杆：Fig. 5-6 的 FE/elastica 后屈曲曲线重合度；Fig. 7-8 的实验装置、误差棒和临界关系。
- 环氧固化：拉伸/松弛/流变拟合图、参数表、Fig. 18-21 类全场验证图和偏差来源。
- 水泥水化相场：微结构快照、温度/浓度场颜色、Fig. 11 归一化量热曲线、窄孔距 impingement 图。
- Eigenstrain tomography：Fig. 2-3 null field 可视化和花形拟合，Fig. 4 边界条件示意。
- Wrinkling 标度律：Fig. 2-12 的极坐标趋势、误差图、transition mismatch contour、direct/dual regime 切换。
