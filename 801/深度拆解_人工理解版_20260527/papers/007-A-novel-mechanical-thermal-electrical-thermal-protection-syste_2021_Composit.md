## 1. 身份层

这是一篇面向高超声速飞行器的机械-热-电多功能热防护结构论文。metadata 中题名和作者均为空；根据目录名、摘要和正文，可推断题名指向 “A novel mechanical-thermal-electrical thermal protection system” 一类主题。论文关注 MTPS，即同时承担隔热、承载和热电转换发电的 thermal protection system。

材料读取边界：本报告读取了 `metadata.json`、`abstract.txt`、`clean_body.md`、`figure_captions.txt`、`table_captions.txt`、`tables/*.md`、`equations.txt`、`references.txt`。核心文件均存在；明显抽取问题是 metadata 题名/作者缺失，部分表题缺失，Eq7 等公式严重乱码，正文与结论中的个别应力数值存在口径不一致。

论文的研究对象是一个三级尺度系统：整机飞行器、1 m² MTPS plate、以及含 thermoelectric module 和 gap TPS 的 MTPS unit。它不是单纯 TE 材料论文，而是把 TE 转换嵌入热防护承载结构，并用多尺度边界传递评估热-力-电性能。

## 2. 主张层

中心主张是：高超声速飞行器热防护系统不应只把气动热排掉或隔开，还可以将部分热流转换为电能；通过设计含两级热电材料、承载框架、蜂窝芯、陶瓷层、嵌入导电板和低模量胶层的 MTPS，可以同时实现 load bearing、heat protection 和 power supply。

摘要中的主张是 multi-scale analysis 必不可少。整机气动载荷和结构位移先传给 MTPS plate，再从 plate 传给 unit；若只用零位移或周期边界条件，无法反映真实飞行器局部变形对 TE module 的影响。

结论中的主张包括：8 块 MTPS plates、288 个 TE modules 串联可布置于二级压缩面；unit 内壁温度可保持在约 360 K；两级 TE layer 比前期单级设计提高平均输出功率和效率，从约 0.82 W/0.45% 提高到约 0.88 W/0.51%；全 MTPS 平均输出约 253.44 W。

## 3. 选题层

选题的背景是传统 TPS 的功能单一。ITPS 可承载和隔热，但容易出现 thermal short-circuit；ATPS 可主动冷却，但系统复杂且依赖工质；UHTC 可耐高温但韧性和连接问题突出；烧蚀 TPS 多为一次性。高超声速飞行中的气动热是巨大能量源，如果只能被辐射或隔热耗散，系统效率较低。

作者的切口是把 thermoelectric conversion 放进 TPS，但不把它当作一层脆弱材料夹在中间，而是设计成可承载的多层单元。TE module 包括 alumina ceramic、fiber insulation、高/中温 TE layers、load-bearing frame/honeycomb、embedded conducting plates 和 low-modulus adhesives，这些细节说明选题重点是工程结构集成。

与前期工作相比，本文不是只做单级 TE 层和热应力评估，而是引入两级 TE layers、气动载荷、真实飞行器位移边界和多尺度传递。这让选题从概念验证推进到更接近飞行器结构评估。

## 4. 位置层

论文处于 TPS、ITPS、热电材料和多尺度结构仿真交叉位置。TPS 文献提供隔热和承载背景，TE 文献提供材料选择与发电机制，飞行器结构仿真提供载荷和边界条件，本文的独特位置是把这些合成一个 MTPS unit/plate/vehicle 体系。

相对于传统 unit-cell 周期边界分析，本文强调真实 vehicle-to-plate-to-unit 边界传递。因为 MTPS 位于二级压缩面，整机变形和气动压力不满足简单周期性，unit 的侧面位移必须来自上一级 plate 插值。

文献位置上的压力在于结构设计复杂而材料性能有限。TE 发电效率平均仅 0.51%，重量又较大；因此论文的贡献更适合表述为“多功能集成与可行性评估”，而不是“高效率能量回收方案”。

## 5. 贡献层

第一项贡献是提出具体 MTPS 架构。unit 由 TE module 和 gap TPS 组成，gap TPS 包括 C/C-SiC heat-resistant layer、Saffil insulation、Ti wall、phase-change temperature-control layer 和 adhesives；TE module 包含 TC11 frame、honeycomb cores、两级 TE layers、alumina ceramics、QZr conducting plates 等。

第二项贡献是建立整机-板-单元多尺度传递流程。整机模型给出二级压缩面压力、热流和位移；MTPS plate 用插值获得局部位移边界；MTPS unit 再接收侧面位移、气动热流和气动力，完成热-力-电耦合评估。

第三项贡献是把热电结构细节落到可制造形态。正文展示 3D printed model，给出 unit 尺寸、module 尺寸、TE layers 尺寸和质量分解：MTPS unit 约 1156.97 g，TE module 约 904.1 g，TE layers 约 733 g，gap TPS 约 252.87 g。

第四项贡献是定量评估飞行过程中的温度、应力、电势、输出功率和效率。最大热端温度约 927 K，unit average power 约 0.88 W，效率平均约 0.51%，288 个模块平均输出约 253.44 W。

## 6. 方法层

方法输入包括飞行器外形和质量分布、再入轨迹代表时刻、CFD 气动压力/热流、结构边界条件、MTPS 几何和材料性能、TE 材料 Seebeck 系数及电阻等。输出是整机应力、plate 变形与应力、unit 温度场、应力场、电势、功率和效率。

整机层采用 MSC Patran/Nastran 建模，包含 beam、shell 和 concentrated mass；气动压力来自 FLUENT。代表时刻包括 0、182.5、525.5、1063.5、1367.5 s 等，用于筛选力学和热-力综合关键工况。

plate 层使用 ABAQUS C3D8R 单元，将整机局部位移插值到 1 m² MTPS plate 上。unit 层使用 C3D8T 热-力耦合单元，包含 443356 个单元、835354 个节点，边界为顶部气动热流、底部对流、侧面来自 plate 的位移，界面多用 ideal Tie。

电学计算基于 Seebeck effect，选取高温和中温 p/n 型 TE 材料各 50 对。温差产生电势，再结合内阻估算输出功率和 conversion efficiency。两级 TE 设计意在让高温层和中温层分别处于更合适温区。

## 7. 证据层

图 1 展示飞行器与 MTPS 布置，图 2 展示 CAD、截面和 3D 打印模型，是结构可实现性的证据。图 3 给出多尺度分析步骤，图 4 到图 6 展示整机、plate 和 unit 模型。

整机证据显示 t=0 时气动力导致较高应力，fuselage 和 second-stage compression surface 最大应力分别约 562 MPa 和 548 MPa；热流在 280-495 s 快速上升，最大约 0.13 MW/m²。作者选择 t=0 作为气动载荷关键点，t=182.5 s 作为热-力综合关键点。

plate 和 unit 证据显示，多尺度边界比简单周期/固定边界更合理。plate 在 t=0 时局部最大应力约 600 MPa，t=182.5 s 时 TE module 最大应力约 250.1 MPa；unit 热分析中最大温度约 927 K，内壁温度可维持约 360 K。

电学证据显示，高温层最大电势约 15.3 V，中温层约 5.1 V，总电势最大约 19.8 V；unit 最大输出功率约 14.42 W，平均输出约 0.88 W，平均效率约 0.51%。全系统 288 个模块平均输出约 253.44 W。

## 8. 结构语言层

文章结构按尺度展开：先定义 vehicle 和 MTPS 概念，再给 governing equations 和三个尺度模型，随后依次汇报 vehicle、plate、unit 的 thermal-mechanical 与 electrical 结果。这种结构把复杂系统拆成可追踪的边界传递链。

语言上，作者用 “mechanical-thermal-electrical”“multi-scale”“load bearing, heat protection and power supply” 等词把论文从传统 TPS 拓展为 multifunctional structure。重点不是单个材料 ZT，而是系统级功能整合。

可复用的写法是用“前期概念不足-本研究工程细化”建立连续性。作者明确指出之前工作只有单级 TE layer、缺少 mesoscopic details、未考虑 aerodynamic force；本文通过两级 TE、真实载荷和多尺度模型补足。

抽取层面，正文中公式和表题有明显噪声，metadata 题名/作者缺失。还有一个需要人工警惕的内容口径：正文局部结果出现 frame 或 TE materials 应力较高数值，而结论中又说 bearing components 和 TE materials 低于某些限值，可能是 OCR、局部应力集中剔除或组件口径不同导致，复用时应回查原 PDF。

## 9. 引用风险层

引用链覆盖传统 TPS、ITPS、ATPS、UHTC、TE materials、热电发电和作者前期 MTPS 概念。作为“热防护结构热电能量回收”和“多功能 TPS 设计”引用比较合适。

主要风险是质量与效率。unit 重量约 1.16 kg，288 个模块会带来显著质量代价；平均效率仅 0.51%，平均总功率约 253 W。若引用时只强调“可发电”，容易忽略重量收益比。

第二个风险是材料与界面可靠性。嵌入导电板、胶层、陶瓷、TE 材料和金属框架在热循环、振动、氧化和界面脱粘下的长期可靠性并未充分实验验证。本文更偏数值评估和概念结构设计。

第三个风险是边界和材料数据依赖。CFD、结构模型、Tie 接触、对流系数和 TE 材料参数都会影响结果；如果迁移到另一飞行器或轨迹，必须重新做 multi-scale transfer。

## 10. 复用层

可复用的选题模板是：把热防护系统从 single-function insulation 扩展为 multifunctional energy-harvesting load-bearing structure，但必须同时评估热、力、电和质量代价。

可复用的方法链是：`vehicle aero-structural analysis -> plate boundary interpolation -> unit thermal-mechanical-electrical model -> component stress check -> temperature/electric potential/power/efficiency evaluation`。

可复用的证据组织是从整机到单元逐层给边界条件和结果，避免直接用理想单胞边界推导系统性能。对于 TE-TPS 论文，尤其要同时给温度安全性、应力安全性、发电量和重量。

自检：本报告只使用十个指定标题；摘要、结论、图表、公式、引用风险和抽取问题均收进十层。明显抽取问题为 metadata 题名/作者缺失、公式乱码、表题缺失和局部应力口径不一致。
