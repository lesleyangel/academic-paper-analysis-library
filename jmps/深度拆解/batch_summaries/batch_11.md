# Batch 11 深度拆解摘要

## 完成文件
1. `jmps/深度拆解/papers/Hemodynamics-of-coronary-artery-with-syst_2026_Journal-of-the-Mechanics-and-.md`
2. `jmps/深度拆解/papers/Infimal-representation-of-Landau-p_2026_Journal-of-the-Mechanics-and-Physics.md`
3. `jmps/深度拆解/papers/Latent-Lagrangian-neural-networks-for-reduced-ord_2026_Journal-of-the-Mechan.md`
4. `jmps/深度拆解/papers/Learning-constitutive-relations-from-experi_2026_Journal-of-the-Mechanics-an.md`
5. `jmps/深度拆解/papers/Long-term-irradiation-transmutation-promoted-preci_2026_Journal-of-the-Mecha.md`
6. `jmps/深度拆解/papers/Macroscale-chirality-in-planar-elasticity--Predictions-o_2026_Journal-of-the.md`

## 本批论文的共同特征
这 6 篇都把复杂对象压缩成可计算、可验证、可迁移的力学框架：心肌桥文章把临床形态转成 RPD 和应力分类；Landau 势文章把相变路径转成 infimal 自由能；L-LNN 把机器学习降阶转成 Lagrangian/虚功结构保持；动态压痕把实验学习转成 PDE 约束优化；钨辐照把长时嬗变转成 PF-SR rate-MD 多尺度模型；平面手性把颗粒 motif 转成 micropolar 连续体验证。

## 本批最值得学习的 5 个写法
1. 用“变量耦合”制造 gap，而不是泛泛说 X 重要。
2. 先验证模型，再解释机制，避免直接从模型跳到应用结论。
3. 把复杂结果压缩成相图、尺度律、场变量对比或误差图。
4. 让 AI/数值方法服从物理结构，如 Lagrangian、virtual work、PDE constraint、adjoint。
5. 理论论文也要给概念图和示例，否则公式容易空转。

## 本批最常见的审稿风险
- 模型外推风险：从简化几何、合成系统或特定 motif 推到真实复杂系统时，需要更多验证。
- 参数/路径非唯一风险：Landau 势路径构造、动态压痕参数、钨辐照源项和缺陷参数都可能存在敏感性。
- 图像依赖风险：场变量、相图、微结构图和曲线细节均需结合 PDF 图像核查。
- benchmark 不足风险：L-LNN、动态压痕和 micropolar 手性文章都可继续加强与替代方法的定量比较。

## 可沉淀到 JMPS 写作模板的规律
`现象/工程需求 -> 现有方法不足 -> 可计算变量集合 -> 模型/理论构造 -> 验证 -> 参数或案例研究 -> 机制压缩 -> 边界和未来工作` 是本批最稳定的结构。Introduction 应把文献分成“基础理论、最接近方法、真实场景证据”三组；Results 应让每张图服务一个 claim；Discussion 应先解释机制，再限定外推范围。

## 需要后续人工图像核查的内容
- 心肌桥：RPD 相图、纤维化分组箱线图、应力相图。
- Landau 势：路径图、Moreau 正则化曲线、Fe 相变能量地形和微结构色标。
- L-LNN：能量拓扑图、误差方差图、噪声预测曲线。
- 动态压痕：力-深度曲线、塑性场 snapshot、独立拉伸曲线差异。
- 钨辐照：Re/缺陷场、HFIR 实验对比、粗化指数拟合区间和机制谱。
- 平面手性：micro FE 与 micropolar 位移/微旋转场、边界层厚度、appendix grain count 收敛图。
