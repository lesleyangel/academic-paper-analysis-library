# JMPS 论文拆解批次 6 摘要

## 批次范围
本批次覆盖 6 篇 2026 年 JMPS 论文：

1. The out-of-plane bifurcation and narrow stability interval of planar solutions in the Euler-Plateau problem
2. The strange mechanics of an elastic rod under null-resultant transverse loads
3. Thermo-chemo-mechanical modeling and parameter identification of epoxy resin curing
4. Thermodynamic phase-field method for simulation of cement hydration
5. Uniqueness of solutions in high-energy x-ray based 'eigenstrain tomography' and other inverse eigenstrain problems
6. Unveiling scaling laws for wrinkling in compressed fiber-reinforced bilayers at any elastic mismatch

## 批次共性
- 这批论文都不是单纯“做仿真给结果”，而是围绕一个高价值的理论或方法瓶颈建立可检验条件：临界值、广义方程、唯一性下限、参数可识别性、相场驱动力、regime 阈值。
- JMPS 风格非常明显：即使有工程/材料对象，论文也会回到能量、变分、热力学一致性、稳定性、适定性或渐近标度。
- 图表承担的功能不是装饰，而是验证论证闭环：收敛性图、分支图、装置图、参数识别流程图、相场快照、null field 可视化、regime phase diagram。
- 多数论文都主动承认边界：后分岔未做、机械载荷未充分验证、二维模型仅定性、真实实验几何更复杂、简化本构需实验检验。

## 单篇高价值提炼
- Euler-Plateau：用二次变分和半解析特征值求根把出平面分岔临界值从前人 `4.3790` 修正为 `3.7402`，并解释非圆平面分支为何实验上难以观测。
- Null-resultant transverse loads：把“零合力横向载荷无效”的直觉翻转为 `Ta + Tt` 的广义 Euler elastica，并用理论、有限元、实验三重验证。
- Epoxy curing：工程本构长文的范例，关键不只在模型复杂，而在热力学一致性、实验矩阵、多步参数唯一性和有限元验证的组合。
- Cement hydration phase-field：把水泥水化加速/减速曲线拆成相变、扩散、热释放和 impingement 机制，二维示范清楚但定量预测仍需 3D 和参数实验。
- Eigenstrain tomography：用显式 null fields 证明单/双分量 eigenstrain tomography 不适定，并给出三分量测量和对角 eigenstrain 搜索空间的最低要求。
- Fiber-reinforced wrinkling：把复杂起皱参数空间整理成 film-mediated direct laws 与 substrate-governed dual laws，并用阈值 `ρ*ML` 判别 regime。

## 可复用写作资产
- 选题套路：修正一个被接受的临界值；挑战一个经典理想化；给出一个反演方法的适定性下限；把经验曲线拆成局部机制；把复杂参数空间归纳成 regime 图谱。
- 论证套路：前人现象/方法 -> 隐含缺口 -> 理论条件或能量框架 -> 数值/实验/反例验证 -> 明确适用边界。
- 文笔套路：强 claim 之后跟限定条件；结果段先给数字或图，再解释与前人差异；结论中把抽象参数转译为实验可观测量。
- 图表套路：概念示意图 + 关键临界曲线 + 收敛/误差图 + 机制分解图 + 适用域图。

## 批次风险与核查事项
- 本批次拆解基于 `jmps/文本/txt` 的全文抽取、references 和 figure captions；未直接读取 PDF 图像本体。
- 对所有涉及曲线形态、相图颜色、实验照片、误差棒和三维形状的判断，均需结合 PDF 图像进一步核查。
- 个别论文大量关键推导位于 supplementary material，txt 中仅有正文描述；若用于复现公式，需要另查补充材料。
