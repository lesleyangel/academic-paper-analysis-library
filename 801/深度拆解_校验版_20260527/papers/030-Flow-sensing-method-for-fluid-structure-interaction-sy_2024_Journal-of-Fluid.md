# 论文深度拆解：Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition

> 生成依据：`801/cleantext/030-Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`030-Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid`
- 源 PDF：`F:\code\学术期刊蒸馏器\801\论文\Flow-sensing-method-for-fluid-structure-interaction-sy_2024_Journal-of-Fluid.pdf`
- 页数：34
- clean body 字符数：66707
- 摘要字符数：2499
- 参考文献条数：47
- 图题数：55
- 表题数：2
- 表格文件数：4
- 公式候选数：230
- 提取质量分：1.0
- 是否需人工复核：False
- 提取后剩余问题：[{"code": "caption_pollution", "severity": "medium", "message": "Many figure/table caption paragraphs remain in body text."}, {"code": "low_confidence_formulas", "severity": "medium", "message": "18 formula(s) need manual review."}]

## 1. 身份层

- 标题：Flow sensing method for fluid-structure interaction systems via multilayer proper orthogonal decomposition
- 年份：2024
- 期刊/来源：Journal of Fluid
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：方法/算法 + 数值验证型
- 研究对象：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 主要方法：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD model of structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 主要证据：图表 57 个标题、公式 230 个候选、参考文献 47 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“需结合 Introduction 首段复核；自动抽取未找到显式问题句。”，可以通过“In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD ”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures. The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices.
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：需结合 Introduction 首段复核；自动抽取未找到显式问题句。
- 问题来源：多来自工程瓶颈、计算/实验成本、复杂多物理场耦合、可靠性/不确定性传播或材料性能优化需求。
- 为什么重要：该类问题通常直接影响热防护设计、结构安全、飞行性能、能量管理、可靠性评估或材料服役性能。
- 研究边界：以本文模型、实验对象、材料体系、飞行轨迹、结构形式或数据集为边界；外推到其它平台或工况需谨慎。
- 可写作学习点：先给工程必要性，再把大问题压缩成可验证的模型/方法/性能指标问题。

## 4. 位置层：文献版图与 gap

- 已有研究分类推断：
  - 物理/数值模型类：提供机理和高保真基准，但成本较高或边界较窄。
  - 数据驱动/降阶/代理模型类：提升效率，但依赖数据覆盖和泛化验证。
  - 实验/测量类：提供真实证据，但工况、样本和尺度有限。
  - 优化/可靠性/不确定性类：处理设计决策，但常受模型复杂度和计算成本限制。
- 作者声明或文本中可见 gap：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing. In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022). While the black-b Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical science and engineering to obtain flow speed and direction (Wolf et al., 2018; Wang et al., 2022), distribute underwater sources (Zheng et al., 2018; Liu et al., 2018), reconstruct surface pressure of aircraft (Zhao et al., 2021), analysis fluid-structure stability (Yao et al., 2022), and optimize sensors (Xu et al., 2019) (Verma et al., 2020).
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD model of structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：方法/算法 + 数值验证型；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：方法/算法 + 数值验证型
- 输入：材料/结构/轨迹/工况/几何/传感器/样本/仿真参数等，需按方法章节和表格核查。
- 输出：性能指标、预测结果、优化方案、可靠性指标、温度/应力/流场/电热性能等。
- 关键步骤推断：
  1. 定义研究对象、几何/材料/工况边界；
  2. 建立理论、数值、实验或数据驱动模型；
  3. 设置参数、网格、样本、训练或测试条件；
  4. 与基准/实验/高保真模型对比；
  5. 用图表和误差/性能指标回收 claim。
- 关键假设：模型边界、材料参数、载荷/温度/流场条件、数据分布或实验测量条件。
- 复现信息充分性：中等。文本和表格提供主流程，但参数完整性、代码/数据开放性和 PDF 图像细节仍需人工核查。

## 7. 证据层

### 7.1 Claim-Evidence 全表

| Claim | 位置 | 证据 | 证据强度 | 风险 |
| --- | --- | --- | --- | --- |
| In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. | 摘要/引言/结论候选 | 图：Fig. 1. The architecture of DNN model. | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures. | 摘要/引言/结论候选 | 图：Fig. 2. The modeling and forecasting architectures of the flow sensing in FSI system using the multilayer ROM. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The proposed method is applied in two FSI systems, including the flow past a flexible filament clamped behind a cylinder and the flow past flexible filament set. | 摘要/引言/结论候选 | 图：Fig. 3. Schematic diagram of the IBM. | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices. | 摘要/引言/结论候选 | 表：Table 1 | 中-强 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical science and engineering  | 摘要/引言/结论候选 | 表：Table 2 | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |
| While the black-b Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical scienc | 摘要/引言/结论候选 | 公式/模型：[confidence=0.57; needs_review; source=equations; [page 1, bbox (39.0, 642.88, 349.4, 664.19)]] https://doi.org/10.1016/ | 中 | 需确认该证据是否覆盖全部工况、参数和对比对象 |

### 7.2 图表/公式功能表

| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |
| --- | --- | --- | --- | --- |
| Fig. 1. The architecture of DNN model. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 2. The modeling and forecasting architectures of the flow sensing in FSI system using the multilayer ROM. | 模型对象/边界条件说明 | 支撑方法、模型或结果可靠性 | 从标题看用于模型对象/边界条件说明 | 是，图像细节需 PDF 核查 |
| Fig. 3. Schematic diagram of the IBM. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 4. The solution process of LB-IM-FEM framework for FSI system. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 5. Schematic of computational domain in case A. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 6. Schematic of computational domain in case B. | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 7. The amplitude envelope of the flexible filament in case A. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 8. The modes and POD reconstruction for structure in case A. (a) The first 4 structural modes, mode 1: k1=62.88%, mode 2: k2=30.27%, mode 3: k3=6.57%, mode | 问题设定/方法框架可视化 | 支撑方法、模型或结果可靠性 | 从标题看用于问题设定/方法框架可视化 | 是，图像细节需 PDF 核查 |
| Fig. 9. The maximum reconstructed error of the flexible filament by POD in case A. | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 10. The mean flow and the first 4 POD modes of Vx in case A. The unit is m/s. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 11. The reconstruction error and modeling region of the multilayer POD for fluid in case A. (a), (c) and (e) are the reconstruction error of the first-laye | 结果对比/验证主张 | 支撑方法、模型或结果可靠性 | 从标题看用于结果对比/验证主张 | 是，图像细节需 PDF 核查 |
| Fig. 12. The forecasted results of the flow at t=1.196 s in the test set of case A. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 13. The forecasted streamlines (real-black; forecasted-red) at t=1.196 s in the test set of case A. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 14. The temporal performance with different layer number of POD for case A. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Fig. 15. The forecasted velocity isolines at three moments for case A, where the unit is m/s. | 辅助说明，需要结合 PDF 图像复核 | 支撑方法、模型或结果可靠性 | 从标题看用于辅助说明，需要结合 PDF 图像复核 | 是，图像细节需 PDF 核查 |
| Table 1 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| Table 2 | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |
| 公式：[confidence=0.57; needs_review; source=equations; [page 1, bbox (39.0, 642.88, 349.4, 664.19)]] https://doi.org/10.1016/j.jfluidstructs.2023 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.93, 462.02, 129.54, 470.88)]] D = [D1, D2, ⋯, Dr] | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.93, 531.07, 89.43, 546.98)]] d = ∑ r | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (79.65, 549.23, 87.67, 554.67)]] i=1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 3, bbox (62.93, 644.36, 509.91, 657.39)]] Di ≈[ξ1, ξ2, ⋯, ξm]ai + d (2) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 4, bbox (62.93, 560.85, 509.91, 573.89)]] t = ψ(s) (3) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.92; source=equations; [page 5, bbox (62.93, 182.6, 509.91, 195.63)] [ξs, as]] = fPOD(Ds) (4) | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |
| 公式：[confidence=0.67; needs_review; source=equations; [page 5, bbox (84.02, 297.95, 117.45, 315.6)]] ] = fPOD-1 | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |

### 7.3 摘要完整摘录

> Flow sensing is widely used to forecast flow field in fluid-structure interaction (FSI) systems. The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing. In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation. First, we establish the POD model of structural deformation. To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures. Then, we establish the multilayer model of flow field. Furthermore, the deep neural network model is employed to map the mode coefficients of the structure to all the mode coefficients of the multilayer POD. The proposed method is applied in two FSI systems, including the flow past a flexible filament clamped behind a cylinder and the flow past flexible filament set. Both constant inflow and transient flow conditions are considered. The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices.
> Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical science and engineering to obtain flow speed and direction (Wolf et al., 2018; Wang et al., 2022), distribute underwater sources (Zheng et al., 2018; Liu et al., 2018), reconstruct surface pressure of aircraft (Zhao et al., 2021), analysis fluid-structure stability (Yao et al., 2022), and optimize sensors (Xu et al., 2019) (Verma et al., 2020). Generally, the essence of flow sensing method is to obtain local or global flow properties from sensor measurements of the fluid or structure. In this method, flow modeling is required to map sensor measurements to flow properties. In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022). The white-box methods obtain accurate flow solutions directly by high-fidelity numerical method, but the computational time is considerably long. While the black-b

### 7.4 摘要中文翻译

> 流量传感广泛用于预测流固耦合（FSI）系统中的流场。具有多种柔性结构的FSI系统通常涉及复杂的非定常流动和大量的传感器，这使得流量传感变得困难。在本研究中，提出了一种通过多层本征正交分解（POD）的 FSI 系统流量传感方法，以利用结构变形实现流场的实时预测。首先，我们建立了结构变形的POD模型。为了提高流场模型的精度，我们提出了多层POD模型，主要关注流场结构复杂的区域的局部建模精度。然后，建立流场的多层模型。此外，采用深度神经网络模型将结构的模态系数映射到多层POD的所有模态系数。所提出的方法应用于两个 FSI 系统，包括流过夹在圆柱体后面的柔性细丝的流动和流过柔性细丝组的流动。恒定流入和瞬态流动条件均被考虑。结果表明，所提出的流量传感方法表现出优异的时空性能，流特性预测准确，适用于相干涡等复杂流结构的FSI系统。
> 
> 受节肢动物柔性纤毛结构和鱼类侧线系统等生物启发(Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021)，流量传感技术被提出并广泛应用于物理科学和工程中，以获取流速和方向(Wolf et al., 2018; Wang et al., 2022)、分配水下源(Zheng等人，2018；刘等人，2018），重建飞机表面压力（Zhao等人，2021），分析流固稳定性（Yao等人，2022），并优化传感器（Xu等人，2019）（Verma等人，2020）。一般来说，流量传感方法的本质是从流体或结构的传感器测量中获得局部或全局流动特性。在此方法中，需要进行流量建模以将传感器测量值映射到流量属性。一般来说，流建模方法可以分为三种类型：白盒、黑盒和灰盒（Loiseau et al., 2018；Zhang et al., 2022）。白盒方法直接通过高保真数值方法获得精确的流动解，但计算时间相当长。

### 7.5 结论完整摘录

识别到的结论位置：5. Conclusions

> In this work, a flow sensing method for FSI systems via multilayer POD is proposed. Two applications are carried out to validate and assess the proposed method. Conclusions are drawn as follows:
> 
> (a) Time evolution of tip displacement in x-direction for the filaments during 72.0 s. 
> (b) Time evolution of tip displacement in y-direction for the filaments during 72.0 s.
> 
> In particular, when using the above two algorithms to build model using the same data D, if $\gamma = \gamma ^ {*}$ , there are: $\pmb {m} = \pmb {m} ^ {*} , \pmb {\xi} = \pmb {\xi} ^ {*}$ , and a
> 
> 1. The proposed method can deal with the flow sensing problems with high-dimensional sensor measurements. For the fluid, the forecasted flow properties are close to the references, and the forecasting accuracy in the regions with complex flow structures can also be ensured due to the multilayer POD model. Moreover, the forecasting error do not accumulate over time, which shows the stable temporal performance of the proposed method.
> 
> 2. The raised multilayer POD model can greatly improve the flow field modeling accuracy. The reconstruction error of flow field decreases almost by an order of magnitude for each layer in two cases.
> 
> 3. The proposed flow sensing method can handle complex FSI system with multiple flexible filaments and address flow sensing problem with transient conditions. However, when it is applied in flow sensing problem with transient conditions, the method only suitable for a certain range of Reynolds numbers, which is the limitation in forecasting transient flows.

### 7.6 结论中文翻译

> 在这项工作中，提出了一种通过多层 POD 进行 FSI 系统的流量传感方法。进行了两次应用来验证和评估所提出的方法。结论如下： (a) 72.0 s 期间细丝尖端位移在 x 方向上的时间演变。 (b) 72.0 s 期间细丝 y 方向尖端位移的时间演变。特别地，当使用上述两种算法使用相同的数据D建立模型时，如果$\gamma = \gamma ^ {*}$，则有：$\pmb {m} = \pmb {m} ^ {*}，\pmb {\xi} = \pmb {\xi} ^ {*}$，并且a 1。该方法可以处理高维传感器测量的流量传感问题。对于流体来说，预测的流动特性与参考值接近，并且由于多层POD模型，在流动结构复杂的区域也能保证预测精度。此外，预测误差不会随着时间的推移而累积，这表明该方法具有稳定的时间性能。提出的多层POD模型可以大大提高流场建模精度。在两种情况下，每层流场重建误差几乎降低了一个数量级。所提出的流量传感方法可以处理具有多个柔性细丝的复杂 FSI 系统，并解决瞬态条件下的流量传感问题。然而，当应用于瞬态条件下的流量传感问题时，该方法仅适用于一定范围的雷诺数，这限制了瞬态流量的预测。

## 8. 结构语言层

### 8.1 章节结构与章节名分析

| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |
| ---: | --- | --- | ---: | --- |
| 1 | 1. Introduction | 问题引入/文献定位 | 9951 | 该节承担“问题引入/文献定位”功能，服务于从问题到证据的推进。 |
| 2 | 2.1. Proper orthogonal decomposition | 对象/条件/子问题展开 | 2370 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 3 | 2.2. Deep neural network | 对象/条件/子问题展开 | 1562 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 4 | 2.3. Flow sensing model via multilayer POD | 方法建构 | 12964 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 5 | 3.1. Lattice Boltzmann method for fluid | 方法建构 | 3327 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 6 | 3.2. Finite element method for structure | 方法建构 | 1553 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 7 | 3.3. Immersed boundary method | 方法建构 | 3017 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 8 | 4.1. Physical models and numerical settings of the FSI systems | 方法建构 | 2348 | 该节承担“方法建构”功能，服务于从问题到证据的推进。 |
| 9 | 4.2.1. POD for structure | 对象/条件/子问题展开 | 1784 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 10 | 4.2.2. Multilayer POD for fluid | 对象/条件/子问题展开 | 3524 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 11 | 4.2.3. Training and forecasting | 对象/条件/子问题展开 | 4975 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 12 | 4.2.4. Case A study with transient flow conditions | 对象/条件/子问题展开 | 5170 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 13 | 4.3.1. POD for structure | 对象/条件/子问题展开 | 1378 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 14 | 4.3.2. Multilayer POD for fluid | 对象/条件/子问题展开 | 3337 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 15 | 4.3.3. Training and forecasting | 对象/条件/子问题展开 | 4043 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 16 | 4.3.4. Case B study with transient flow conditions | 对象/条件/子问题展开 | 2593 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |
| 17 | 5. Conclusions | 主张回收/边界说明 | 1566 | 该节承担“主张回收/边界说明”功能，服务于从问题到证据的推进。 |
| 18 | CRediT authorship contribution statement | 对象/条件/子问题展开 | 258 | 该节承担“对象/条件/子问题展开”功能，服务于从问题到证据的推进。 |

### 8.2 章节推进逻辑

- 摘要：通常按“问题重要性 -> 既有方法不足 -> 本文方法 -> 验证对象 -> 主要结果/性能增量”组织。
- Introduction：先把工程/学术问题放大，再通过文献分类制造 gap，最后收束到本文贡献。
- Method/Model：把 claim 变成可执行流程，读者需要在这里看到变量、假设、输入输出和边界。
- Results/Discussion：把方法有效性转化为图表证据，常通过对比、误差、趋势和敏感性说明。
- Conclusion：回收主要发现，通常也暴露外推边界和未来工作。

### 8.3 段落功能样例

| 段落来源 | 功能 | 推进方式 | 可学习点 |
| --- | --- | --- | --- |
| Introduction 前段 | 背景/重要性 | 从工程必要性进入研究对象 | 先建立“为什么要研究” |
| Introduction 文献段 | 文献分类/gap | 用 however/limited/remain 等转折缩小问题 | gap 要和后文方法一一对应 |
| Method 开头 | 方法总览 | 先给框架，再拆步骤 | 降低复杂方法的阅读成本 |
| Results 开头 | 验证设置 | 说明对比对象和指标 | 让审稿人知道证据如何支撑 claim |
| Conclusion | 主张回收 | 用编号或并列句总结贡献 | 不新增未验证 claim |

### 8.4 词频、词类、短语与语态

- 高频词：mathrm(226)；mathbf(201)；flow(178)；pod(176)；error(66)；fluid(65)；modeling(65)；structure(60)；velocity(57)；sensing(52)；fig(52)；region(47)；field(46)；filament(43)；structural(40)；cdots(38)；forecasted(38)；tag(37)；modes(35)；multilayer(34)
- 高频学术名词/术语：structure(60)；velocity(57)；filament(43)；pressure(23)；reconstruction(23)；deformation(21)；performance(19)；prediction(19)；dimension(15)；simulation(14)；evolution(10)；motion(9)；distribution(8)；proportion(8)；density(8)
- 高频学术动词：obtained(12)；compared(8)；obtain(6)；predicted(5)；predict(4)；constructed(3)；construct(3)；validated(3)；investigated(2)；evaluate(2)；validate(2)；optimize(1)；developed(1)；presented(1)；propose(1)
- 高频形容词：filament(43)；structural(40)；transient(19)；flexible(18)；numerical(14)；boundary(11)；constant(9)；external(8)；displacement(8)；real(8)；coherent(7)；consistent(7)；moment(7)；temporal(7)；dynamic(6)
- 高频副词：respectively(22)；specifically(8)；gradually(6)；generally(5)；similarly(5)；mainly(5)；significantly(5)；widely(4)；greatly(4)；relatively(4)；directly(3)；especially(3)
- 高频二词短语：mathbf mathrm(86)；flow sensing(49)；flow field(35)；multilayer pod(33)；mathbf mathbf(30)；mathrm mathbf(28)；mathrm mathrm(27)；structural deformation(21)；mode coefficients(21)；mathrm pod(21)；mathrm cdots(19)；forecasting error(18)；fsi system(16)；widehat mathbf(16)；flow conditions(15)
- 高频三词短语：mathrm mathbf mathrm(27)；mathbf mathrm mathbf(18)；widehat mathbf mathrm(16)；transient flow conditions(11)；cdots mathbf mathrm(10)；mathbb mathrm times(10)；mathbf mathrm cdots(9)；mathrm cdots mathbf(9)；multilayer pod fluid(9)；flow field structural(8)；field structural deformation(8)；mathrm mathbb mathrm(8)
- 被动语态估计：135
- `we + 动作动词` 主动句估计：3
- 一般现在时线索：341
- 一般过去时线索：358
- 现在完成时线索：1
- 情态动词线索：57

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

### 背景/重要性句
- 未稳定识别，需从对应章节人工补充。
### gap/转折句
- 原句：The FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
  - 可迁移句型：{object} FSI system with multiple flexible structures usually involves complex unsteady flow and large number of sensors, which makes it difficult to perform flow sensing.
- 原句：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
  - 可迁移句型：{object} general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
- 原句：While the black-b Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical science and engineering to obtain flow speed and direction (Wolf et al., 2018; Wang et al., 2022), distribute underwater sources (Zheng et al., 2018; Liu et al., 2018), reconstruct surface pressure of aircraft (Zhao et al., 2021), analysis fluid-structure stability (Yao et al., 2022), and optimize sensors (Xu et al., 2019) (Verma et al., 2020).
  - 可迁移句型：{object} the black-b Inspired by bio-inspiration such as flexible cilia structure of arthropods and fish lateral line system (Tao and Yu, 2012; Tri antafyllou et al., 2016; Zhai et al., 2021), flow sensing technology is proposed and widely used in physical sci
- 原句：In general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
  - 可迁移句型：{object} general, flow modeling methods can be divided into three types: white-box, black-box, and gray-box (Loiseau et al., 2018; Zhang et al., 2022).
### 方法提出句
- 原句：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  - 可迁移句型：{object} This study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句：First, we establish the POD model of structural deformation.
  - 可迁移句型：{object}, we establish the POD model of structural deformation.
- 原句：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  - 可迁移句型：{object} improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 原句：Then, we establish the multilayer model of flow field.
  - 可迁移句型：{object}, we establish the multilayer model of flow field.
### 结果证明句
- 原句：In this study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
  - 可迁移句型：{object} This study, a flow sensing method for FSI systems via multilayer proper orthogonal decomposition (POD) is proposed to achieve real-time forecast of flow field using structural deformation.
- 原句：The results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices.
  - 可迁移句型：{object} results indicate that the proposed flow sensing method exhibits excellent spatial-temporal performance, performs accurately in flow properties forecasting, and is suitable for FSI systems with complex flow structures such as coherent vortices.
- 原句：For steady flow, (Zhao et al., 2021) constructed a compressed sensing method using proper orthogonal decomposition (POD), and achieved high-precision reconstruction of airfoil pressure by a few measurement data.
  - 可迁移句型：{object} steady flow, (Zhao et al., 2021) constructed a compressed sensing method using proper orthogonal decomposition (POD), and achieved high-precision reconstruction of airfoil pressure by a few measurement data.
- 原句：(2022) proposed a flow sensing method combining D The modeling and forecasting architectures of the proposed method are shown in $\mathrm{Fig}$ .
  - 可迁移句型：(2022) proposed a flow sensing method combining {object} The modeling and forecasting architectures of the proposed method are shown in $\mathrm{Fig}$ .
### 贡献收束句
- 原句：To improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
  - 可迁移句型：{object} improve model accuracy for flow field, we propose the multilayer POD model, which mainly focus on the local modeling accuracy in the region with complex flow structures.
- 原句：The gray-box methods build low-dimensional reduced-order models (ROMs) (Kim, 2016; Rowley and Dawson, 2017) to approximate the flow properties, which reduces modeling difficulty of high-dimensional data by extracting the coherent structures in flow.
  - 可迁移句型：{object} gray-box methods build low-dimensional reduced-order models (ROMs) (Kim, 2016; Rowley and Dawson, 2017) to approximate the flow properties, which reduces modeling difficulty of high-dimensional data by extracting the coherent structures in flow.
- 原句：While when $u _ {0}$ varies with time, the changing trend of $p _ {0}$ is consistent with that of du0 $/ \mathrm{d} t$ In this FSI system, pressure varies due to inlet flow conditions and boundary conditions provided ${\mathbf {b}} \mathbf {y}$ the structure.
  - 可迁移句型：{object} when $u _ {0}$ varies with time, the changing trend of $p _ {0}$ is consistent with that of du0 $/ \mathrm{d} t$ In this FSI system, pressure varies due to inlet flow conditions and boundary conditions provided ${\mathbf {b}} \mathbf {y}$ the structur
- 原句：The raised multilayer POD model can greatly improve the flow field modeling accuracy.
  - 可迁移句型：{object} raised multilayer POD model can greatly improve the flow field modeling accuracy.
### 边界/谨慎句
- 原句：In above studies, many deep learning algorithms are used in the black-box methods, but only POD is used in the gray-box methods.
  - 可迁移句型：{object} above studies, many deep learning algorithms are used in the black-box methods, but only POD is used in the gray-box methods.
- 原句：However, in real-world scenarios, the inflow magnitude is not constant and may change.
  - 可迁移句型：{object}, in real-world scenarios, the inflow magnitude is not constant and may change.
- 原句：The flow behavior may contain more modes, and the structural response will also exhibit long transient modal interactions.
  - 可迁移句型：{object} flow behavior may contain more modes, and the structural response will also exhibit long transient modal interactions.
- 原句：However, when it is applied in flow sensing problem with transient conditions, the method only suitable for a certain range of Reynolds numbers, which is the limitation in forecasting transient flows.
  - 可迁移句型：{object}, when it is applied in flow sensing problem with transient conditions, the method only suitable for a certain range of Reynolds numbers, which is the limitation in forecasting transient flows.

## 9. 引用风险层

- 正文引用簇估计：23
- 参考文献条数：47
- 可识别年份条目数：76
- 2021 年及以后参考文献数：34
- 2010 年以前经典文献数：4
- 高频来源粗略识别：J. Fluids Struct(6)；Comput. Methods Appl. Mech. Engrg(5)；Phys. Fluids(4)；J. Comput. Phys(2)；J. Bionic. Eng(2)；Build. Environ(1)；Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech(1)；Dynamic interactions of multiple wall-mounted flexible flaps. J. Fluid Mech(1)
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

- Calzolari, G., Liu, W., 2021. Deep learning to replace, improve, or aid CFD analysis in built environment applications: a review. Build. Environ. 206, 108315 https:// doi.org/10.1016/j.buildenv.2021.108315.
- Castellanos, R., Cornejo Maceda, G.Y., De La Fuente, I., Noack, B.R., Ianiro, A., Discetti, S., 2022. Machine-learning flow control with few sensor feedback and measurement noise. Phys. Fluids 34, 047118. https://doi.org/10.1063/5.0087208.
- Chen, S., Doolen, G.D., 1998. Lattice Boltzmann method for fluid flows. Annu. Rev. Fluid Mech. 30 (1), 329–364. https://doi.org/10.1146/annurev.fluid.30.1.329.
- Connor, J.O., Revell, A., 2019. Dynamic interactions of multiple wall-mounted flexible flaps. J. Fluid Mech. 870, 189–216. https://doi.org/10.1017/jfm.2019.266.
- Dang, F., Nasreen, S., Zhang, F., 2021. DMD-based background flow sensing for AUVs in flow pattern changing environments. IEEE Robot. Autom. Lett. 6 (3), 5207–5214. https://doi.org/10.1109/LRA.2021.3072570.
- Dubois, P., Gomez, T., Planckaert, L., Perret, L., 2022. Machine learning for fluid flow reconstruction from limited measurements. J. Comput. Phys. 448, 110733 https://doi.org/10.1016/j.jcp.2021.110733.
- Fang, Z., Gong, C., Revell, A., O’Connor, J., 2022. Fluid–structure interaction of a vegetation canopy in the mixing layer. J. Fluids Struct. 109, 103467 https://doi.org/ 10.1016/j.jfluidstructs.2021.103467.
- Favier, J., Revell, A., Pinelli, A., 2014. A Lattice Boltzmann – Immersed Boundary method to simulate the fluid interaction with moving and slender flexible objects. J. Comput. Phys. 261, 145–161. https://doi.org/10.1016/j.jcp.2013.12.052.
- Fresca, S., Manzoni, A., 2022. POD-DL-ROM: enhancing deep learning-based reduced order models for nonlinear parametrized PDEs by proper orthogonal decomposition. Comput. Methods Appl. Mech. Engrg. 388, 114181 https://doi.org/10.1016/j.cma.2021.114181.
- Gao, D., Deng, Z., Yang, W., Chen, W., 2021. Review of the excitation mechanism and aerodynamic flow control of vortex-induced vibration of the main girder for long-span bridges: a vortex-dynamics approach. J. Fluids Struct. 105, 103348 https://doi.org/10.1016/j.jfluidstructs.2021.103348.
- Gong, C., Fang, Z., Chen, G., 2018. A lattice Boltzmann-immersed boundary-finite element method for nonlinear fluid–solid interaction simulation with moving objects. Int. J. Comput. Methods. 15 (7), 1850063 https://doi.org/10.1142/S0219876218500639.
- Guo, Z., Zheng, C., Shi, B., 2002. Discrete lattice effects on the forcing term in the lattice Boltzmann method. Phys. Rev. E. 65, 046308 https://doi.org/10.1103/ PhysRevE.65.046308.
- Han, R., Wang, Y., Zhang, Y., Chen, G., 2019. A novel spatial-temporal prediction method for unsteady wake flows based on hybrid deep neural network. Phys. Fluids 31 (12), 127101. https://doi.org/10.1063/1.5127247.
- Harwood, A.R.G., Connor, J.O., Mu˜noz, J.S., Santasmasas, M.C., Revell, A.J., 2018. LUMA: a many-core, fluid-structure interaction solver based on the Lattice- Boltzmann method. SoftwareX 7, 88–94. https://doi.org/10.1016/j.softx.2018.02.004.
- Jia, X., Li, C., Ji, W., Gong, C., 2022. A hybrid reduced-order model combing deep learning for unsteady flow. Phys. Fluids 34, 097112. https://doi.org/10.1063/ 5.0104848.

### 9.2 审稿风险清单

| 风险 | 具体表现 | 严重度 | 应对方式 |
| --- | --- | --- | --- |
| gap 风险 | gap 若只靠泛化措辞而非最近文献支撑，会显得不够真实 | P1 | 增补最近五年最接近工作并公平比较 |
| 方法必要性 | 若简单 baseline 已可解决问题，新模型复杂度会被质疑 | P1 | 加入消融、复杂度收益和边界条件说明 |
| 证据外推 | 单一算例/样本/轨迹/材料体系支撑大 claim | P1 | 扩展工况或明确适用边界 |
| 图表可读性 | 文本抽取无法确认图像细节 | P2 | 回看 PDF 图像、坐标轴、误差条和图例 |
| 公式/符号 | 公式抽取可能低置信或符号缺失 | P2 | 按 PDF 逐式核查变量定义 |

## 10. 复用层

- 可复用选题角度：把复杂工程/物理问题转化为“效率、精度、可靠性、性能或可解释性”的可验证改进。
- 可复用 gap 表达：已有方法在高保真、低成本、跨工况、耦合机制或工程适用性之间存在张力。
- 可复用贡献表达：提出/构建一个面向具体对象的模型或实验框架，并通过对比验证其精度、效率或性能收益。
- 可复用论证链：问题重要性 -> 文献分类 -> 明确 gap -> 方法设计 -> 验证设置 -> 图表证据 -> 结论回收。
- 可复用图表设计：先给对象/框架示意图，再给流程图/参数表，最后给对比结果、误差和敏感性图。
- 不可直接模仿：具体数据、实验平台、材料体系、仿真模型、团队资源和未公开代码。
- 迁移到自己论文的三件事：
  1. 让 Introduction 的 gap 与 Method 的输入输出一一对应；
  2. 让每个强 claim 至少对应一个图表、一个指标和一个对比对象；
  3. 在 Conclusion 中只回收已验证内容，主动标注适用边界。

## 11. 质量自检

- 模式：精细拆解
- 对象：单篇论文
- 样本边界是否清晰：是
- 十层字段是否覆盖：是
- Claim-Evidence 是否完成：是，基于自动抽取的强 claim 候选和图表/公式/参考文献证据
- 图表功能是否解释：是，但图像细节需 PDF 核查
- 引用策略是否解释：是
- 风险是否具体：是
- 可复用资产是否具体：是
- 不确定项：公式符号、图像细节、部分图表标题和真实段落位置仍需 PDF 视觉核查
- 下一步建议：若要用于正式写作模仿，应人工复核 PDF 中关键图、公式和 Introduction 文献转折段。
