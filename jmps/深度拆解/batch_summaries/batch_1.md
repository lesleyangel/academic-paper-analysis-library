# Batch 1 深度拆解摘要

## 完成文件
- `A-numerical-spectral-model-for-shear-transformat_2026_Journal-of-the-Mechani.md`：A numerical spectral model for shear transformation zone dynamics in heterogeneous metallic glasses
- `A-simple-quantitative-model-of-neuromodulation_2026_Journal-of-the-Mechanics.md`：A simple quantitative model of neuromodulation, Part II: Mechanosensitive channel gating
- `A-variational-phase-field-model-for-anisotropic-_2026_Journal-of-the-Mechani.md`：A variational phase-field model for anisotropic fracture accounting for multiple cohesive lengths
- `Asymptotic-representation-of-frictional--non-con_2026_Journal-of-the-Mechani.md`：Asymptotic representation of frictional, non-conforming contact edges under general periodic loading
- `Atomistic-analysis-of-stress-dependent-activation-energy_2026_Journal-of-the.md`：Atomistic analysis of stress-dependent activation energy and dominant factors for dislocation nucleation from planar faults in BCC metals: A comparative study to FCC metals
- `Configurational-forces-explain-echelon-cr_2026_Journal-of-the-Mechanics-and-.md`：Configurational forces explain echelon cracks in soft materials

## 本批论文的共同特征
本批 6 篇都属于 JMPS 典型的“机制问题 + 可计算框架 + 图表证据”组合。它们的共同点不是题材相同，而是都把复杂现象压缩成少数可计算变量：STZ-FFT 关注局部塑性事件如何贯通，neuromodulation 关注应变如何偏置通道门控，相场断裂关注 cohesive length 如何控制方向强度，接触渐近关注 KI/KII/LI 如何控制边缘耗散，原子模拟关注 μb^3 如何控制能垒，echelon cracks 关注构型力如何解释复杂前沿。它们都强依赖模型边界，因此写作上普遍有“强贡献 + 谨慎限定”的双层语气。

## 本批最值得学习的 5 个写法
1. 先把旧框架的适用边界说清楚，再自然引出新模型，而不是直接宣称前人不足。
2. 结果图按“基线 -> 单因素 -> 组合/高维 -> 边界”递进，让复杂模型的说服过程可跟随。
3. 强 claim 绑定明确图表或公式，例如强度面、归一化能垒、构型力方向、耗散密度或应变响应曲线。
4. Discussion 主动区分解释、预测和设计启发，避免把模型内趋势无限外推。
5. 图注承担大量复现信息：几何、载荷、参数、坐标、归一化方式常直接写在图注里。

## 本批最常见的审稿风险
- 模型理想化较强：真实材料微结构、真实细胞复杂性、真实接触粗糙、真实裂纹传播和真实晶界结构都比模型对象复杂。
- 参数可识别性与统计代表性不足：特别是神经模型、STZ 异质性、原子模拟热激活和构型力阈值。
- 图像/曲线需要人工核查：云图、裂纹形貌、拟合残差、能垒路径、滑移区和构型力方向不能只凭 txt 判断。
- 与最接近前人工作相比的定量增益有时不足，容易被要求增加同条件对照。
- 标题或摘要有时较强，正文证据更偏机制解释而非完整预测。

## 可沉淀到 JMPS 写作模板的规律
`领域痛点 -> 文献分流 -> 具体 gap -> 新框架 -> 基线验证 -> 参数/几何/材料变量扫描 -> 机制解释 -> 适用边界 -> 可迁移意义` 是本批最稳定的骨架。Introduction 中最好把 gap 写成“旧方法不能处理某个具体变量/条件”，Method 中先给总框架再给公式，Results 中每节标题尽量指向一个 claim，Discussion 中用限定语保护结论。

## 需要后续人工图像核查的内容
- STZ-FFT：Fig. 1-8 的应力场、等效应变、剪切带厚度和 3D 波状局部化形貌。
- Neuromodulation：TRPC1/阻断图像、钙成像 ROI、CASCADE 推断曲线、Fig. 12-14 拟合残差。
- Anisotropic phase-field：strength surface 图、极坐标临界应力、2D/3D 裂纹路径和层合偏转图。
- Frictional contact：Fig. 5-12 的耗散峰位置、非同相分离/滑移/粘着区域和相位趋势。
- Atomistic dislocation：FENEB 路径、鞍点结构、归一化能垒重合程度、频率图分界。
- Echelon cracks：实验形貌到理想几何的对应、构型力方向、spacing 扫描、coalescence 区域重分布。
