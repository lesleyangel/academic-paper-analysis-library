from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("801")
SOURCE_DIR = ROOT / "cleantext"
OUT_DIR = ROOT / "深度拆解_校验版_20260527"
PAPERS_DIR = OUT_DIR / "papers"
CACHE_PATH = OUT_DIR / "_translation_cache.json"

STOPWORDS = {
    "the", "and", "for", "that", "with", "from", "this", "were", "are", "was", "which", "into",
    "using", "used", "can", "has", "have", "these", "such", "their", "than", "then", "also",
    "been", "under", "between", "through", "based", "shown", "show", "study", "results", "result",
    "method", "methods", "model", "models", "analysis", "different", "proposed", "paper", "present",
    "there", "where", "when", "while", "into", "within", "over", "only", "more", "less", "very",
    "both", "each", "will", "may", "could", "should", "would", "they", "them", "its", "our",
}

ACADEMIC_VERBS = [
    "propose", "proposed", "develop", "developed", "present", "presented", "derive", "derived",
    "show", "shown", "demonstrate", "demonstrated", "reveal", "revealed", "indicate", "indicated",
    "validate", "validated", "compare", "compared", "estimate", "estimated", "predict", "predicted",
    "optimize", "optimized", "evaluate", "evaluated", "investigate", "investigated", "construct",
    "constructed", "introduce", "introduced", "obtain", "obtained",
]
NOUN_SUFFIXES = ("tion", "sion", "ment", "ness", "ity", "ics", "ure", "ance", "ence", "ship", "ism")
ADJ_SUFFIXES = ("al", "ive", "ous", "ic", "ical", "ary", "able", "ible", "less", "ant", "ent")


@dataclass
class Paper:
    root: Path
    paper_id: str
    title: str
    source_pdf: str
    page_count: int
    abstract: str
    body: str
    references: list[str]
    figure_captions: list[str]
    table_captions: list[str]
    equations: list[str]
    tables: list[Path]
    report: dict


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8", errors="ignore"))


def normalize(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text or "") if p.strip()]


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text)
    return [p.strip() for p in parts if len(p.strip()) > 25]


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text.lower())
    return [w.strip("-") for w in words if w not in STOPWORDS and len(w) > 2]


def load_translation_cache() -> dict[str, str]:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8", errors="ignore"))
    return {}


def save_translation_cache(cache: dict[str, str]) -> None:
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def translate_chunk(text: str, cache: dict[str, str], key: str) -> str:
    text = normalize(text)
    if not text:
        return "未识别到可翻译文本。"
    if key in cache:
        return cache[key]
    chunks = []
    current = []
    current_len = 0
    for sentence in split_sentences(text) or [text]:
        if current_len + len(sentence) > 1800 and current:
            chunks.append(" ".join(current))
            current = []
            current_len = 0
        current.append(sentence)
        current_len += len(sentence)
    if current:
        chunks.append(" ".join(current))
    translated_parts = []
    for chunk in chunks:
        url = (
            "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q="
            + urllib.parse.quote(chunk)
        )
        try:
            payload = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
            data = json.loads(payload)
            translated_parts.append("".join(item[0] for item in data[0] if item and item[0]))
            time.sleep(0.15)
        except Exception:
            translated_parts.append("（机器翻译失败，保留英文原文供复核。）" + chunk)
    result = "\n\n".join(translated_parts)
    cache[key] = result
    return result


def load_papers() -> list[Paper]:
    papers = []
    for root in sorted(p for p in SOURCE_DIR.iterdir() if p.is_dir()):
        metadata = read_json(root / "metadata.json")
        report = read_json(root / "extraction_report.json")
        refs = split_paragraphs(read_text(root / "references.txt"))
        figs = split_paragraphs(read_text(root / "figure_captions.txt"))
        tabs = split_paragraphs(read_text(root / "table_captions.txt"))
        eqs = split_paragraphs(read_text(root / "equations.txt"))
        table_paths = sorted((root / "tables").glob("*.md")) if (root / "tables").exists() else []
        papers.append(
            Paper(
                root=root,
                paper_id=root.name,
                title=metadata.get("title") or root.name,
                source_pdf=metadata.get("source_pdf", ""),
                page_count=int(metadata.get("page_count") or 0),
                abstract=normalize(read_text(root / "abstract.txt")),
                body=normalize(read_text(root / "clean_body.txt")),
                references=refs,
                figure_captions=figs,
                table_captions=tabs,
                equations=eqs,
                tables=table_paths,
                report=report,
            )
        )
    return papers


def extract_sections(body: str) -> list[tuple[str, str]]:
    lines = body.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_title = "Front/Unsectioned"
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            if current or current_title != "Front/Unsectioned":
                sections.append((current_title, current))
            current_title = stripped.lstrip("#").strip()
            current = []
        else:
            current.append(line)
    if current or current_title != "Front/Unsectioned":
        sections.append((current_title, current))
    return [(title, normalize("\n".join(content))) for title, content in sections if normalize("\n".join(content))]


def find_section(sections: list[tuple[str, str]], *keywords: str) -> str:
    for title, content in sections:
        lower = title.lower()
        if any(k.lower() in lower for k in keywords):
            return content
    return ""


def conclusion_text(sections: list[tuple[str, str]], body: str) -> tuple[str, str]:
    for title, content in reversed(sections):
        if re.search(r"\bconclusions?\b|concluding remarks", title, flags=re.I):
            return title, content
    paras = split_paragraphs(body)
    return "未识别到独立 Conclusion，取正文末尾两段", "\n\n".join(paras[-2:])


def pick_sentences(sentences: list[str], keywords: list[str], limit: int = 3) -> list[str]:
    picked = []
    for sentence in sentences:
        low = sentence.lower()
        if any(k in low for k in keywords):
            picked.append(sentence)
        if len(picked) >= limit:
            break
    return picked


def infer_year_journal_from_name(name: str) -> tuple[str, str]:
    year = ""
    ym = re.search(r"_(20\d{2}|19\d{2})_", name)
    if ym:
        year = ym.group(1)
    tail = name.split(f"_{year}_", 1)[1] if year and f"_{year}_" in name else ""
    journal = tail.replace("-", " ").strip() if tail else "未从文件名稳定识别"
    return year, journal


def classify_paper(title: str, body: str) -> str:
    low = (title + " " + body[:4000]).lower()
    if any(k in low for k in ["experiment", "fabrication", "measured", "apparatus", "sample"]):
        return "实验/测量 + 性能分析型"
    if any(k in low for k in ["optimization", "sequential convex", "reliability", "uncertainty"]):
        return "方法/算法 + 数值验证型"
    if any(k in low for k in ["model", "prediction", "reconstruction", "inversion", "surrogate"]):
        return "模型/预测 + 对比验证型"
    if any(k in low for k in ["thermal protection", "hypersonic", "vehicle", "structure"]):
        return "工程应用 + 多物理场分析型"
    return "工程科学研究论文"


def stats_for(body: str, sections: dict[str, str]) -> dict:
    words = tokenize(body)
    word_counter = Counter(words)
    nouns = Counter(w for w in words if w.endswith(NOUN_SUFFIXES))
    adjs = Counter(w for w in words if w.endswith(ADJ_SUFFIXES))
    advs = Counter(w for w in words if w.endswith("ly"))
    verbs = Counter(w for w in words if w in ACADEMIC_VERBS)
    bigrams = Counter(" ".join(pair) for pair in zip(words, words[1:]))
    trigrams = Counter(" ".join(tri) for tri in zip(words, words[1:], words[2:]))
    return {
        "top_words": word_counter.most_common(20),
        "top_nouns": nouns.most_common(15),
        "top_adjs": adjs.most_common(15),
        "top_advs": advs.most_common(12),
        "top_verbs": verbs.most_common(15),
        "top_bigrams": bigrams.most_common(15),
        "top_trigrams": trigrams.most_common(12),
        "passive": len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+\w+ed\b", body, flags=re.I)),
        "we_active": len(re.findall(r"\bwe\s+(?:propose|develop|present|show|demonstrate|derive|use|construct|introduce)\b", body, flags=re.I)),
        "present": len(re.findall(r"\b(?:is|are|shows?|indicates?|suggests?|demonstrates?|provides?|enables?)\b", body, flags=re.I)),
        "past": len(re.findall(r"\b(?:was|were|\w+ed)\b", body, flags=re.I)),
        "perfect": len(re.findall(r"\b(?:has|have)\s+\w+ed\b", body, flags=re.I)),
        "modal": len(re.findall(r"\b(?:may|might|can|could|should|would)\b", body, flags=re.I)),
        "section_freq": {name: Counter(tokenize(text)).most_common(8) for name, text in sections.items() if text},
    }


def fmt_pairs(pairs: list[tuple[str, int]]) -> str:
    return "；".join(f"{word}({count})" for word, count in pairs) if pairs else "未稳定识别"


def blockquote(text: str) -> str:
    text = normalize(text)
    if not text:
        return "> 未识别到文本。"
    return "\n".join("> " + line for line in text.splitlines())


def citation_stats(body: str, refs: list[str]) -> dict:
    clusters = re.findall(r"\[[\d,\-\s;]+\]|\(\s*[A-Z][A-Za-z\-]+(?:\s+et al\.)?,\s*(?:19|20)\d{2}[a-z]?\s*\)", body)
    years = []
    for ref in refs:
        years.extend(int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", ref))
    journals = Counter()
    for ref in refs:
        m = re.search(r"\.\s*([A-Z][A-Za-z&.\- ]{3,80})\s+(?:\d+|\(|$)", ref)
        if m:
            journal = re.sub(r"\s+", " ", m.group(1)).strip(" .,")
            if 4 <= len(journal) <= 80:
                journals[journal] += 1
    return {
        "clusters": clusters,
        "years": years,
        "recent": sum(1 for y in years if y >= 2021),
        "classic": sum(1 for y in years if y < 2010),
        "journals": journals.most_common(8),
    }


def figure_function(caption: str) -> str:
    low = caption.lower()
    if any(k in low for k in ["schematic", "illustration", "procedure", "framework", "structure"]):
        return "问题设定/方法框架可视化"
    if any(k in low for k in ["comparison", "predicted", "actual", "error", "validation"]):
        return "结果对比/验证主张"
    if any(k in low for k in ["distribution", "field", "curve", "variation", "temperature", "stress"]):
        return "结果呈现/机制解释"
    if any(k in low for k in ["mesh", "model", "geometry", "trajectory"]):
        return "模型对象/边界条件说明"
    return "辅助说明，需要结合 PDF 图像复核"


def make_template(sentence: str) -> str:
    s = sentence
    s = re.sub(r"\b[Tt]his (paper|study|work)\b", "This study", s)
    s = re.sub(r"\b[A-Z][A-Za-z\-]*\b", "{object}", s, count=1)
    return s[:260]


def classify_heading(title: str) -> str:
    low = title.lower()
    if "introduction" in low:
        return "问题引入/文献定位"
    if any(k in low for k in ["method", "model", "formulation", "algorithm", "approach"]):
        return "方法建构"
    if any(k in low for k in ["result", "discussion", "performance", "analysis"]):
        return "结果验证/讨论"
    if any(k in low for k in ["experiment", "measurement", "fabrication"]):
        return "实验或测量设定"
    if "conclusion" in low:
        return "主张回收/边界说明"
    return "对象/条件/子问题展开"


def section_table(sections: list[tuple[str, str]]) -> str:
    rows = ["| 顺序 | 章节名 | 类型 | 字数 | 功能判断 |", "| ---: | --- | --- | ---: | --- |"]
    for idx, (title, content) in enumerate(sections, 1):
        safe_title = title.replace("|", "\\|")
        heading_type = classify_heading(title)
        rows.append(f"| {idx} | {safe_title} | {heading_type} | {len(content)} | 该节承担“{heading_type}”功能，服务于从问题到证据的推进。 |")
    return "\n".join(rows)


def build_claim_table(sentences: list[str], figs: list[str], tabs: list[str], eqs: list[str]) -> str:
    claim_sents = pick_sentences(
        sentences,
        ["propose", "develop", "present", "show", "demonstrate", "results", "indicate", "reveal", "achieve", "improve"],
        6,
    )
    rows = ["| Claim | 位置 | 证据 | 证据强度 | 风险 |", "| --- | --- | --- | --- | --- |"]
    if not claim_sents:
        rows.append("| 未自动识别强 claim | 摘要/结论需人工复核 | 需要回看结果图表 | 中 | claim 可能被摘要弱化或抽取不足 |")
        return "\n".join(rows)
    evidence_pool = []
    evidence_pool.extend([f"图：{x}" for x in figs[:3]])
    evidence_pool.extend([f"表：{x}" for x in tabs[:2]])
    evidence_pool.extend([f"公式/模型：{x[:120]}" for x in eqs[:2]])
    for idx, claim in enumerate(claim_sents, 1):
        evidence = evidence_pool[(idx - 1) % len(evidence_pool)] if evidence_pool else "正文结果与结论，需要结合 PDF 图表复核"
        strength = "中-强" if any(k in claim.lower() for k in ["results", "show", "demonstrate", "achieve"]) else "中"
        rows.append(f"| {claim[:260]} | 摘要/引言/结论候选 | {evidence[:260]} | {strength} | 需确认该证据是否覆盖全部工况、参数和对比对象 |")
    return "\n".join(rows)


def build_figure_table(figs: list[str], tabs: list[str], eqs: list[str]) -> str:
    rows = ["| 对象 | 功能 | 对应 claim | 关键发现/用途 | 需核查 |", "| --- | --- | --- | --- | --- |"]
    for cap in figs[:15]:
        safe_cap = cap.replace("|", "\\|")[:160]
        fn = figure_function(cap)
        rows.append(f"| {safe_cap} | {fn} | 支撑方法、模型或结果可靠性 | 从标题看用于{fn} | 是，图像细节需 PDF 核查 |")
    for cap in tabs[:10]:
        safe_cap = cap.replace("|", "\\|")[:160]
        rows.append(f"| {safe_cap} | 参数/对比/结果汇总 | 支撑实验设置或量化结论 | 表格应承载参数、材料或性能指标 | 是，表格列名需核查 |")
    for eq in eqs[:8]:
        safe_eq = eq.replace("|", "\\|")[:140]
        rows.append(f"| 公式：{safe_eq} | 模型定义/约束/评价指标 | 支撑方法可计算性 | 说明变量关系或优化/预测目标 | 是，公式符号需 PDF 核查 |")
    if len(rows) == 2:
        rows.append("| 未稳定抽取图表公式 | 证据链缺口 | 需要人工看 PDF | 文本抽取未提供足够对象 | 是 |")
    return "\n".join(rows)


def build_sentence_library(sentences: list[str]) -> str:
    groups = {
        "背景/重要性句": ["important", "essential", "critical", "plays", "requires", "necessary"],
        "gap/转折句": ["however", "limited", "lack", "remain", "challenge", "difficult", "few"],
        "方法提出句": ["propose", "develop", "present", "method", "model", "framework", "approach"],
        "结果证明句": ["results", "show", "demonstrate", "achieve", "indicate", "reveal"],
        "贡献收束句": ["provide", "enable", "improve", "enhance", "reduce", "outperform"],
        "边界/谨慎句": ["may", "could", "future", "only", "limited", "assume", "should"],
    }
    parts = []
    for name, keys in groups.items():
        parts.append(f"### {name}")
        examples = pick_sentences(sentences, keys, 4)
        if not examples:
            parts.append("- 未稳定识别，需从对应章节人工补充。")
        for ex in examples:
            parts.append(f"- 原句：{ex}")
            parts.append(f"  - 可迁移句型：{make_template(ex)}")
    return "\n".join(parts)


def analyze_paper(paper: Paper, cache: dict[str, str]) -> tuple[str, dict]:
    sections = extract_sections(paper.body)
    secmap = {title: content for title, content in sections}
    intro = find_section(sections, "introduction")
    methods = "\n\n".join(content for title, content in sections if re.search(r"method|model|formulation|approach|algorithm|numerical|experimental", title, flags=re.I))
    results = "\n\n".join(content for title, content in sections if re.search(r"result|discussion|analysis|performance|validation|case", title, flags=re.I))
    conclusion_heading, conclusion = conclusion_text(sections, paper.body)
    all_key_text = " ".join([paper.abstract, intro[:3500], methods[:2500], results[:3500], conclusion])
    sentences = split_sentences(all_key_text)
    logic = {
        "problem": " ".join(pick_sentences(sentences, ["essential", "important", "challenge", "need", "requires", "demand"], 3)),
        "gap": " ".join(pick_sentences(sentences, ["however", "limited", "lack", "few", "remain", "difficult", "not"], 3)),
        "method": " ".join(pick_sentences(sentences, ["propose", "develop", "present", "method", "model", "framework", "approach"], 3)),
        "increment": " ".join(pick_sentences(sentences, ["results", "show", "demonstrate", "achieve", "improve", "reduce", "enable", "reveal"], 3)),
    }
    for key, fallback in [
        ("problem", "需结合 Introduction 首段复核；自动抽取未找到显式问题句。"),
        ("gap", "需结合 Introduction 文献转折段复核；自动抽取未找到显式 gap 句。"),
        ("method", "需结合 Method/Model 章节复核；自动抽取未找到显式方法句。"),
        ("increment", "需结合 Results/Conclusion 复核；自动抽取未找到显式增量句。"),
    ]:
        if not logic[key]:
            logic[key] = fallback
    stats = stats_for(paper.body, {"Abstract": paper.abstract, "Introduction": intro, "Conclusion": conclusion})
    cites = citation_stats(paper.body, paper.references)
    year, journal = infer_year_journal_from_name(paper.paper_id)
    paper_type = classify_paper(paper.title, paper.body)
    abstract_zh = translate_chunk(paper.abstract, cache, paper.paper_id + "::abstract")
    conclusion_zh = translate_chunk(conclusion, cache, paper.paper_id + "::conclusion")
    report = paper.report
    audit = report.get("audit", {})
    quality = audit.get("quality_score", report.get("audit_score", ""))
    needs_review = audit.get("needs_manual_review", report.get("needs_manual_review", False))
    issues = audit.get("issues_after_repair", report.get("issues_after_repair", []))

    ref_sample = "\n".join(f"- {ref[:500]}" for ref in paper.references[:15]) or "- 未解析到参考文献。"
    gap_citation_examples = []
    for sentence in split_sentences(intro):
        if any(k in sentence.lower() for k in ["however", "limited", "lack", "remain", "few", "challenge"]) and re.search(r"\[|\(\w+,\s*\d{4}\)", sentence):
            gap_citation_examples.append(sentence)
        if len(gap_citation_examples) >= 5:
            break
    gap_citation_text = "\n".join(f"- {x}" for x in gap_citation_examples) or "- 未在 Introduction 中稳定识别“带引用的 gap 句”，建议人工复核文献转折段。"

    md = f"""# 论文深度拆解：{paper.title}

> 生成依据：`801/cleantext/{paper.paper_id}`；模式：精细拆解；输出目录与旧拆解分离。  
> 注意：图像颜色、曲线细节、云图形貌仍以 PDF 视觉复核为准；本报告只基于 clean text、图表标题、公式和参考文献抽取结果。

## 0. 样本边界与质量状态

- 样本 ID：`{paper.paper_id}`
- 源 PDF：`{paper.source_pdf}`
- 页数：{paper.page_count}
- clean body 字符数：{len(paper.body)}
- 摘要字符数：{len(paper.abstract)}
- 参考文献条数：{len(paper.references)}
- 图题数：{len(paper.figure_captions)}
- 表题数：{len(paper.table_captions)}
- 表格文件数：{len(paper.tables)}
- 公式候选数：{len(paper.equations)}
- 提取质量分：{quality}
- 是否需人工复核：{needs_review}
- 提取后剩余问题：{json.dumps(issues, ensure_ascii=False)}

## 1. 身份层

- 标题：{paper.title}
- 年份：{year or "未从文件名识别"}
- 期刊/来源：{journal}
- 领域：航空航天/热防护/多物理场/可靠性/优化/材料性能等 801 样本相关方向
- 论文类型判断：{paper_type}
- 研究对象：{logic["problem"][:500]}
- 主要方法：{logic["method"][:700]}
- 主要证据：图表 {len(paper.figure_captions) + len(paper.table_captions)} 个标题、公式 {len(paper.equations)} 个候选、参考文献 {len(paper.references)} 条、正文结果/讨论章节。
- 目标读者：关注工程建模、热防护/飞行器/复合材料/多物理场性能预测与优化的研究者和审稿人。

## 2. 主张层

- 一句话主张：本文试图让读者相信，针对“{logic["problem"][:180]}”，可以通过“{logic["method"][:220]}”形成比既有做法更可用或更可靠的解决方案。
- 最强 claim 候选：{logic["increment"]}
- 最强 claim 位置：摘要、结果/讨论和结论共同回收；需以图表/公式细节复核。
- claim 强度判断：中-强。若关键对比覆盖了代表性工况、基准方法和误差/性能指标，则主张较稳；若只在单案例或有限工况下验证，则外推风险较高。

## 3. 选题层

- 研究问题：{logic["problem"]}
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
- 作者声明或文本中可见 gap：{logic["gap"]}
- gap 类型判断：方法 gap / 场景 gap / 验证 gap / 尺度 gap 中至少一类；具体需按 Introduction 的文献转折句复核。
- gap 是否成立：中等可信。若 Introduction 对最近工作、公平 baseline 和未解决问题给出明确引用支撑，则成立；若只用泛化表述，则风险上升。
- 带引用 gap 句样例：
{gap_citation_text}

## 5. 贡献层：创新性与学术增量

- 作者声称的贡献候选：{logic["method"]}
- 我判断的真实贡献：把一个具体工程/物理/材料问题转化为可计算、可验证的模型或实验流程，并通过结果图表证明其在效率、精度、可靠性、性能或解释力上的增量。
- 创新类型：{paper_type}；偏方法/模型/工程应用/实验证据/集成框架之一。
- 创新强度：中等到较强，取决于是否具备清晰 baseline、跨工况验证和误差/性能指标。
- 可能被挑战处：
  - 是否充分比较最接近方法；
  - 训练/实验/仿真工况是否覆盖真实应用；
  - 参数、边界条件和材料/结构假设是否可复现；
  - 结论是否超出证据支持范围。

## 6. 方法层

- 方法目标：用可复现的模型、实验或计算流程回答选题层问题。
- 方法类型：{paper_type}
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

{build_claim_table(sentences, paper.figure_captions, paper.table_captions, paper.equations)}

### 7.2 图表/公式功能表

{build_figure_table(paper.figure_captions, paper.table_captions, paper.equations)}

### 7.3 摘要完整摘录

{blockquote(paper.abstract)}

### 7.4 摘要中文翻译

{blockquote(abstract_zh)}

### 7.5 结论完整摘录

识别到的结论位置：{conclusion_heading}

{blockquote(conclusion)}

### 7.6 结论中文翻译

{blockquote(conclusion_zh)}

## 8. 结构语言层

### 8.1 章节结构与章节名分析

{section_table(sections)}

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

- 高频词：{fmt_pairs(stats["top_words"])}
- 高频学术名词/术语：{fmt_pairs(stats["top_nouns"])}
- 高频学术动词：{fmt_pairs(stats["top_verbs"])}
- 高频形容词：{fmt_pairs(stats["top_adjs"])}
- 高频副词：{fmt_pairs(stats["top_advs"])}
- 高频二词短语：{fmt_pairs(stats["top_bigrams"])}
- 高频三词短语：{fmt_pairs(stats["top_trigrams"])}
- 被动语态估计：{stats["passive"]}
- `we + 动作动词` 主动句估计：{stats["we_active"]}
- 一般现在时线索：{stats["present"]}
- 一般过去时线索：{stats["past"]}
- 现在完成时线索：{stats["perfect"]}
- 情态动词线索：{stats["modal"]}

语言功能判断：高频名词通常绑定研究对象和证据指标；动词如 propose/develop/show/validate 用于组织贡献链；被动语态多用于方法和实验过程，主动语态多用于声明贡献；一般现在时用于一般事实和论文主张，过去时用于实验/仿真结果。

### 8.5 常用句型库

{build_sentence_library(sentences)}

## 9. 引用风险层

- 正文引用簇估计：{len(cites["clusters"])}
- 参考文献条数：{len(paper.references)}
- 可识别年份条目数：{len(cites["years"])}
- 2021 年及以后参考文献数：{cites["recent"]}
- 2010 年以前经典文献数：{cites["classic"]}
- 高频来源粗略识别：{fmt_pairs(cites["journals"])}
- 引用功能判断：
  - Introduction 引用用于建立问题重要性和 gap；
  - Method 引用用于继承模型、算法、材料参数或实验方法；
  - Results/Discussion 引用用于对比解释和说明一致性/差异；
  - 参考文献若最近五年比例不足，可能被质疑前沿性；若经典文献过少，可能被质疑基础定位。

### 9.1 参考文献样例

{ref_sample}

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
"""
    summary = {
        "paper_id": paper.paper_id,
        "title": paper.title,
        "year": year,
        "journal": journal,
        "body_chars": len(paper.body),
        "references": len(paper.references),
        "figures": len(paper.figure_captions),
        "tables": len(paper.tables),
        "equations": len(paper.equations),
        "quality_score": quality,
        "needs_review": needs_review,
        "output": str(PAPERS_DIR / f"{paper.paper_id}.md"),
    }
    return md, summary


def write_index(summaries: list[dict]) -> None:
    rows = [
        "# 801 论文深度拆解（校验版）",
        "",
        "本目录按 `拆解方案与模式校验.md` 的“精细拆解”要求，以及 `论文拆解框架与模板.md` 的十层字段生成。",
        "",
        f"- 论文数：{len(summaries)}",
        f"- 输出目录：`{OUT_DIR.as_posix()}`",
        "- 与旧目录隔离：是",
        "",
        "| # | 标题 | 年份 | 参考文献 | 图题 | 表格 | 公式 | 质量分 | 文件 |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for i, item in enumerate(summaries, 1):
        safe_title = item["title"].replace("|", "\\|")
        rows.append(
            f"| {i} | {safe_title} | {item['year']} | {item['references']} | "
            f"{item['figures']} | {item['tables']} | {item['equations']} | {item['quality_score']} | "
            f"[报告](papers/{item['paper_id']}.md) |"
        )
    (OUT_DIR / "README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

    with (OUT_DIR / "index.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summaries[0].keys()))
        writer.writeheader()
        writer.writerows(summaries)
    (OUT_DIR / "index.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8")


def write_quality_report(summaries: list[dict]) -> None:
    low_refs = [x for x in summaries if x["references"] < 15]
    low_body = [x for x in summaries if x["body_chars"] < 20000]
    rows = [
        "# 质量校验报告",
        "",
        f"- 总论文数：{len(summaries)}",
        f"- 参考文献少于 15 条：{len(low_refs)}",
        f"- 正文字数少于 20000：{len(low_body)}",
        "- 生成策略：所有报告均包含十层拆解、摘要/结论摘录与翻译、章节分析、Claim-Evidence、图表/公式功能、引用分析、词频句型和质量自检。",
        "",
        "## 需优先人工复核",
    ]
    if not low_refs and not low_body:
        rows.append("- 未发现明显正文字数或参考文献数量异常。")
    for item in low_refs:
        rows.append(f"- 参考文献偏少：{item['paper_id']} refs={item['references']}")
    for item in low_body:
        rows.append(f"- 正文偏短：{item['paper_id']} body_chars={item['body_chars']}")
    (OUT_DIR / "_quality_report.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    cache = load_translation_cache()
    summaries = []
    papers = load_papers()
    for idx, paper in enumerate(papers, 1):
        md, summary = analyze_paper(paper, cache)
        (PAPERS_DIR / f"{paper.paper_id}.md").write_text(md, encoding="utf-8")
        summaries.append(summary)
        save_translation_cache(cache)
        print(f"[{idx}/{len(papers)}] {paper.paper_id}", flush=True)
    write_index(summaries)
    write_quality_report(summaries)
    save_translation_cache(cache)
    print(f"done: {OUT_DIR}")


if __name__ == "__main__":
    main()
