# Batch 2 深度拆解摘要

## 完成文件
- `jmps/深度拆解/papers/Constitutive-parameter-inference-using-physics-infor_2026_Journal-of-the-Mec.md`
- `jmps/深度拆解/papers/Crack-tip-deformation-transitions-and-fracture-mecha_2026_Journal-of-the-Mec.md`
- `jmps/深度拆解/papers/Deformation-induced-domains-in-sili_2026_Journal-of-the-Mechanics-and-Physic.md`
- `jmps/深度拆解/papers/Design-of-a-specimen-to-train-path-dependent-deep-learnin_2026_Journal-of-th.md`
- `jmps/深度拆解/papers/Dynamic-control-of-rigidity-via-geometric-frustration-_2026_Journal-of-the-M.md`
- `jmps/深度拆解/papers/Dynamic-stress-response-kernels-for-dislocations-_2026_Journal-of-the-Mechan.md`

## 本批论文的共同特征
本批 6 篇都不是单纯“提出模型然后报误差”的文章，而是把一个不可直接观察或难以校准的内部机制转化成可组织的证据系统。肩袖肌腱论文用 full volume MRI 把内部位移/应变场变成反演证据；玻璃态聚合物论文用 D2min、塑性位点、键长和缠结把裂尖断裂拆成阶段链；硅橡胶论文用 X-ray/DVC 与 tracer 把异常体积应变解释为 mobile phase domain formation；试样设计论文把数据集不足改写成试样信息量不足；动态刚度论文把 self-stress/zero modes 转化为可调超材料设计；动态核函数论文把裂纹和位错统一到同一个 L(v)/p(v) 核对象。

共同的 JMPS 味道是：问题来自具体物理或工程瓶颈，但贡献必须落到力学结构、可复现指标、公式对象或图表证据上。它们都很重视“机制-证据”闭环，而不是只给方法流程。

## 本批最值得学习的 5 个写法
1. 用测量维度制造 gap：肩袖肌腱论文不是说已有本构模型都不行，而是说 surface/excised data 无法验证 full-volume internal mechanics。
2. 用阶段-指标-机制组织复杂演化：玻璃态聚合物论文把裂尖断裂写成 activation、coalescence、necking、disentanglement，而每一阶段都有对应指标。
3. 用相图统一反常现象：硅橡胶论文把拉伸、压缩、H/D 和 mobile phase concentration 压到同一 phase map 中。
4. 用下游任务评价方法贡献：试样设计论文不只展示优化几何，而是用 GRU unseen-path NRMSE、redundancy 和泛化测试证明试样有用。
5. 用核心对象统摄理论：动态应力核论文的 L(v)/p(v)、动态刚度论文的 self-stress/zero modes 都是全文导航锚点。

## 本批最常见的审稿风险
- 证据外推风险：动物肩袖到人类、CG 聚合物到真实聚合物、理论超材料到真实打印结构、数值试样到真实实验。
- 隐藏变量证据风险：硅橡胶 mobile phase 取向畴没有被直接成像，只能由 tracer、体积应变和模型间接支持。
- 方法代理指标风险：strain entropy、D2min threshold、plastic site cut-off、fiber direction interpolation、L(v) branch cuts 都可能被追问。
- 视觉证据依赖风险：多篇关键结论依赖图像场、相图、band structure 或快照，txt 只能提供图注和正文描述，必须结合 PDF 图像核查。
- claim 强度风险：本文完成的是 framework/blueprint/kernel derivation 的地方，不能写成临床工具、真实制造验证或完整数值实现已经完成。

## 可沉淀到 JMPS 写作模板的规律
- Introduction 可按“真实瓶颈 -> 已有路线贡献 -> 仍缺的内部变量/尺度/核对象 -> 本文如何使其可观察或可计算”组织。
- Method 不要只列步骤，要说明每个步骤在证据链中的功能：采集什么、反演什么、排除什么、验证什么。
- Results 可以按“先证明数据/方法可靠 -> 再展示核心现象 -> 再用指标解释机制 -> 最后做基线或参数稳健性”推进。
- Discussion 的好小标题应直接表达发现，例如“PDE-constrained optimization enhanced...”“Load-bearing network...”“Invariant-specific error maps revealed...”，而不是泛泛写“Discussion of results”。
- 局限最好转化为下一步模型需求：体积项误差指向 constitutive term 改进，DVC 平滑解释 sharp boundary 差异，branch cuts 留给 numerical implementation。

## 需要后续人工图像核查的内容
- 肩袖肌腱：Fig. 1-8 的位移/应变/不变量误差色标、内部剪切带、gripper 与 footprint detachment 附近误差位置。
- 玻璃态聚合物：Fig. 7-18 的裂尖形貌、D2min 空间分布、plastic site cluster、fibrillar zone 和 entanglement positions。
- 硅橡胶：Fig. 2-3、Fig. 6-11 的 DVC 体积应变、ZnI2 tracer 分布、phase map 边界、径向分布和实验轨迹。
- 试样设计：Fig. 5-10 及附录 A.1-A.8 的优化几何、strain path cloud、NRMSE 曲线、filter/mesh/postprocessing 影响。
- 动态刚度：Fig. 3、5、6、7 和 Fig. C.8 的 FEM 几何、模量数量级变化、band lifting 和局部应变集中。
- 动态应力核：无常规图像，但需人工核查公式编号、符号一致性、上下标、Fourier convention 和附录推导。

## 异常与注意事项
- 写作过程中发现 `jmps/深度拆解/papers` 中出现了其他批次文件；本批只创建并核查上述 6 个指定文件，没有修改其他 stem。
- 本批 6 篇均包含 `## 0` 到 `## 19` 的二级标题，并均包含 Claim-Evidence 表，单篇正文约 10,000-13,000 中文字符。
- 终端读取模板时出现编码显示异常，但深度说明结构和用户要求已按中文内容执行。
