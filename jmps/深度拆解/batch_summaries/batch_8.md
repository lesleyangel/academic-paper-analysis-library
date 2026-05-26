# Batch 8 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Correlating-dislocation-waviness-and-strength-with-co_2026_Journal-of-the-Me.md`
- `jmps/深度拆解/papers/Couplant-free-and-high-purity-excitation-of-uni_2026_Journal-of-the-Mechanic.md`
- `jmps/深度拆解/papers/Crystallographic-fatigue-crack-propagation-in-Ni-based-_2026_Journal-of-the-.md`
- `jmps/深度拆解/papers/Crystal-plasticity-phase-field-modeling-of-shock-wav_2026_Journal-of-the-Mec.md`
- `jmps/深度拆解/papers/Curvature-corrected-crack-tip-fields-on-curved-_2026_Journal-of-the-Mechanic.md`
- `jmps/深度拆解/papers/Curvature-enabled-topological-phase-transitio_2026_Journal-of-the-Mechanics-.md`

## 本批论文的共同特征
这 6 篇都不是单纯展示结果，而是把一个传统框架的隐含假设或工程瓶颈改写成新的控制变量：SFE/w landscape、normal-encoding、`γs/G` crack drivers、shock-wave-induced twin fields、manifold curvature、curvature/thickness topological couplings。共同的 JMPS 味道是：先把问题缩到可数学化的机制缺口，再用理论、仿真、实验或外部数据形成闭环。

## 本批最值得学习的 5 个写法
1. 用“从 A 转向 B”的范式句表达创新：tangential-pushing -> normal-encoding；flat Euclidean fields -> curved manifold fields。
2. 用理想化场做机制剥离，再回到随机/真实场景：位错 SFE landscape 论文最典型。
3. 把复杂模型压成少数 mechanistic drivers：Ni 裂纹论文用 `γs` 和 `G`，曲率断裂论文用奇异阶与角函数。
4. 用图表链条推进说服：概念图 -> 方程/参数 -> 受控模拟 -> 实验/外部验证 -> 局限。
5. 显式写局限：mechanistic rather than quantitative prediction、proof-of-concept、first-order curvature、2D projection 等都被主动处理。

## 本批最常见的审稿风险
- 强 claim 的边界：governing factor、first solution、defect-immune、high-purity 等词都需要严格证据。
- 模型简化：SRO 被 w/SFE landscape 代理，γ-γ′ 微结构被规则化，shock Mg 用 2D 投影和简化背应力。
- 验证不足：topological shell 主要是仿真，meta-exciter 实验仍是 proof-of-concept，Ni crack 是机制一致而非定量寿命验证。
- 图像依赖强：裂纹路径、波场、孪晶分布、band structures、位错曲率场均需 PDF 图像核查。

## 可沉淀到 JMPS 写作模板的规律
- Introduction 可按“经典能力 -> 隐含假设/瓶颈 -> 新控制变量 -> 本文闭环”组织。
- Method 要把核心变量和物理量映射关系单独说明，如 `w-γusf`、phase gradient-angle、curvature-angular eigenfunctions。
- Results 适合先用可控简化模型证明因果，再用复杂情景证明稳健性。
- Discussion 应主动比较同类方法的结构性限制，而不是只说本文更好。
- Conclusion 最好按“方法贡献、机制发现、应用意义、边界/未来”分层。

## 需要后续人工图像核查的内容
- 位错论文：Fig. 13-15 中 `∂2γusf/∂y∂x` 场、waviness 与 CRSS 散点关系。
- Meta-exciter：Fig. 10-11 实验波场和 FFT 主能量方向是否足够清晰。
- Ni crack：Fig. 25-26 模型 crack path 与实验红虚线重合程度。
- Mg twinning：Fig. 29-36 三阶段孪晶、detwinning 和预存孪晶影响的空间细节。
- Curved fracture：Fig. 8 flat MTS 与 curvature-corrected MTS 的全路径差异。
- Curved topology：Fig. 6-8 的 band gap、edge localization、twist/deformation transmission。

## 异常与说明
- 6 篇均为常规研究论文；没有 editorial、preface 或 correction。
- 文件基于 txt 全文、metadata、图题和正文描述生成；未直接读取 PDF 图像本体，因此视觉细节均保留“需结合 PDF 图像核查”。
- 未手工追加自动词频统计块，等待主线程统一追加。
