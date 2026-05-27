## 1. 身份层

这是一篇热电材料驱动的多功能热防护结构论文。metadata 中题名和作者均为空；根据目录名和摘要，题名可推断为 “A novel TE-material based thermal protection structure and its performance evaluation for hypersonic flight vehicles” 一类。论文比 007 更早，重点是提出 TE-material based TPS 单元并评估其在高超声速轨迹中的热-力-电性能。

材料读取边界：本报告读取了 `metadata.json`、`abstract.txt`、`clean_body.md`、`figure_captions.txt`、`table_captions.txt`、`tables/*.md`、`equations.txt`、`references.txt`。核心文件均存在；明显抽取问题是 metadata 题名/作者缺失，正文误抽出 `Mechanical:`、`Planes:` 等标题，结论标题未按编号抽取，部分边界公式与单位 OCR 噪声较大。

论文的身份是概念结构+材料制备+数值评估的混合型论文。它既选择 p/n 型 TE 材料，也制备 n-type Sr0.9La0.1TiO3，还用工程热计算和有限元单胞模型评估飞行轨迹下的温度、电势、功率和效率。

## 2. 主张层

中心主张是：传统非烧蚀 TPS 主要通过辐射和隔热被动处理气动热，能量利用效率低；在热防护结构中嵌入热电材料，可以在保证隔热的同时把部分热流转化为电能，为高超声速飞行器提供辅助供电潜力。

摘要中的主张包括三个环节：基于 reusable launch vehicle 的轨迹进行气动热计算；设计由 C/C-SiC、Saffil insulation、p/n 型 TE 材料和 Ti-6Al-4V 底板组成的 multifunctional TPS；用 unsteady mechanical-thermoelectric unit cell model 评估 thermoelectric conversion efficiency。

结论中的主张是：周期边界条件对单胞模型至关重要；底板温度随对流换热系数显著变化，h=10/50/100/300 W/m²K 时底部最高温度约为 639/497/431/364 K；0.01 m²、128 对 p-n couple 的结构可获得约 18-20 V 峰值电势和 2-3 W 量级峰值功率，30 m² 面积外推可达 kW 量级。

## 3. 选题层

选题的直接背景是高超声速飞行器热环境严酷，壁面温度可能超过 1800 K，TPS 是必需系统；但传统 TPS 只把热挡住或辐射出去，没有利用气动热能。热电材料提供了把温差转化为电势的可能性，因此很自然地成为 multifunctional TPS 的候选。

本文的选题包含材料和结构两层。材料层，p-type 选择 Ca3Co4O9，n-type 制备 Sr0.9La0.1TiO3，并关注高温 Seebeck、热导率和热膨胀。结构层，将 TE legs 放入 C/C-SiC 与钛合金底板之间，通过 Saffil insulation 和对流边界形成温差。

相比只讨论 TE 材料 ZT 的论文，这个选题把材料性能放到具体飞行轨迹和热防护构型中检验。它的创新不在单一材料性能突破，而在“TE material based TPS”的结构化应用评估。

## 4. 位置层

论文位于 aerodynamic heating calculation、TPS design、thermoelectric material 和 finite element unit cell modeling 之间。已有研究多关注热防护或热电材料单独性能，少数研究讨论 hypersonic TE-TPS，但系统化结构和轨迹耦合评估有限。

本文的位置是早期概念验证：先用工程方法快速获得某高超声速飞行器轨迹下的热流边界，再把该边界加载到周期单胞上，评估隔热和发电性能。它没有像后续 MTPS 那样加入整机结构位移和承载框架细节。

文献位置上的优势是跨界清晰，风险是简化也明显。工程热计算比 CFD 便宜但精度有限，单胞周期边界适合代表性结构但不代表真实整机局部变形，发电功率的大面积外推也需要谨慎。

## 5. 贡献层

第一项贡献是提出三层 TE-TPS 结构：上层 5 mm C/C-SiC heat-resistant layer，中间为 Saffil insulation 和 p/n 型 TE legs，下层为 5 mm Ti-6Al-4V。p/n legs 尺寸为 3 mm × 3 mm × 15 mm，热量路径被分解为辐射、TE 通道、对流和内部传热。

第二项贡献是制备并表征 n-type Sr0.9La0.1TiO3。工艺包括 ball milling、1200°C calcination、pressing、500°C binder removal、1450°C Ar sintering、1350°C graphite/Ar annealing，并测量 Seebeck 等热电属性。

第三项贡献是建立基于 translational symmetry 的热-力-电单胞有限元模型。模型包含周期机械边界、热边界和电势边界，顶部加载随时间变化的气动热流，底部施加不同对流换热系数，并讨论 thermal contact resistance 对结果的影响。

第四项贡献是给出飞行轨迹下的温度、电势、功率和效率估计。0.01 m² 模块、128 对 p-n couple 的峰值电势约 18.4-19.7 V，峰值功率约 2.33-2.68 W，平均效率约 0.237%-0.607%，并提出主动冷却可提高 TE 性能。

## 6. 方法层

方法输入包括飞行器几何和轨迹、表面点 M 的气动热流、材料热/力/电参数、单胞几何、对流换热系数和界面热阻假设。输出包括结构温度场、位移场、电势分布、输出功率和效率。

气动热计算使用工程算法。外部热平衡写成 convective heat flux 等于辐射项加传导项；C/C-SiC emissivity 取 0.8；不同飞行构型和 Mach 区间采用不同平板/边界层近似，Ma<2 区间精度不足时用线性插值。

有限元单胞模型基于周期对称。顶部加载时间变化 heat flux，底部设置 h=10、50、100、300 W/m²K 的对流，初始温度 300 K、电势 0 V。界面 thermal contact resistance 可取 0 或 1e-4 K m²/W，通过薄层近似模拟。

电学计算采用热电耦合方程，温差导致 p/n legs 产生电势；最大功率按理想匹配负载 `E²/(4r)` 估算。作者也提醒真实负载通常更大，因此实际功率可能低于理想最大值。

## 7. 证据层

图 1 给出飞行器外形和轨迹，图 2 给出热流随时间变化，说明热载荷在约 450 s 附近达到峰值，随后在稀薄气体阶段降低。图 3 和图 4 展示 TE-TPS 结构和热传路径，是概念结构证据。

图 5 和图 6 支撑材料选择与 n-type 材料制备，展示制备流程、测试方法和 TE properties。表 2 给出 TE 材料热导率、热膨胀等物性，是后续数值模型基础。

图 9 到图 12 是热-力证据。h=10 时顶部温度从约 302 K 升至 918 K，底部最高约 639 K；h=100 时顶部峰值相近但底部最高约 431 K。非周期边界会导致不合理位移，说明周期边界对代表性单胞必要。

图 13 到图 16 和表 3 是电学证据。单个 p-n couple 最大电势约 0.144-0.154 V；128 couples 的 0.01 m² 模块最大电势约 18.4-19.7 V，最大功率约 2.33-2.68 W，平均功率约 0.406-0.913 W，平均效率约 0.237%-0.607%。TCR 对最大电势影响约 4%，对功率/效率影响最大约 9%。

## 8. 结构语言层

文章结构是“飞行器与轨迹-热流计算-材料与结构设计-数值模型-性能结果”。它不像纯材料论文那样从晶体结构写起，而是先把 hypersonic flight environment 建出来，再讨论 TE 材料是否能嵌入 TPS。

语言上，作者使用 “multifunctional TPS”“convert heat to electricity”“performance evaluation” 这类概念词，强调系统功能而非材料单点性能。它的表达目标是证明 TE-TPS 有潜力，而不是宣称已经成熟可飞。

可复用的写法是把工程热计算作为快速边界生成器，再把有限元模型作为结构细节评估器。对于早期概念论文，这种组合比直接上全飞行器 CFD/结构耦合更轻。

抽取层面，当前 clean_body 中误抽了 `Mechanical:`、`Planes:` 等并列标题，公式和边界条件段落存在乱码，references 中还混入 conflict statement。写作或复现时应回查 PDF，避免误读边界条件。

## 9. 引用风险层

引用链覆盖 aerodynamic heating、TPS、C/C-SiC、Saffil、Ca3Co4O9、SrTiO3 热电材料和热电转换基础。作为 TE-TPS 概念来源或早期评估论文引用是合适的。

主要风险是热流计算精度。工程算法适合快速估算，但对于复杂三维激波/边界层干扰、真实壁温反馈和局部峰值热流，可能与 CFD 有差距。用该论文结果做设计依据时应补充高保真热环境分析。

第二个风险是功率外推。30 m² 面积推算出 >6000 W 瞬时和 >1000 W 平均功率，是按单胞/模块线性放大得到，未充分考虑布线、遮挡、局部热流非均匀、结构质量和电气管理系统损耗。

第三个风险是个别抽取数值疑似错误。例如不同 h 下 average potential 中出现 0.69 V 的量级异常，更可能是 0.069 V；正式引用时需核对原表或原图。

## 10. 复用层

可复用的选题模板是：把 TPS 从被动防热结构扩展为“防热+发电”结构，用具体轨迹热流而非恒定温差来评估 TE 材料的工程价值。

可复用的方法链是：`trajectory and heat-flux estimation -> TE material selection/fabrication -> periodic unit-cell model -> transient thermal-mechanical response -> electric potential/power/efficiency -> area scaling with caution`。

可复用的证据组织是同时报告隔热效果和发电效果：底板温度证明 TPS 基本功能，电势/功率/效率证明新增功能，边界条件敏感性和 TCR 分析证明模型稳健性。

自检：本报告只使用十个指定标题；摘要、结论、图表、公式、引用风险和抽取问题均收进十层。明显抽取问题为 metadata 题名/作者缺失、误抽标题、公式乱码、references 混入冲突声明和个别数值疑似 OCR 错误。
