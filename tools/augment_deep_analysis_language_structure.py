from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "from",
    "are",
    "was",
    "were",
    "been",
    "being",
    "have",
    "has",
    "had",
    "not",
    "can",
    "could",
    "may",
    "might",
    "will",
    "would",
    "shall",
    "should",
    "into",
    "onto",
    "than",
    "then",
    "when",
    "where",
    "which",
    "while",
    "within",
    "without",
    "using",
    "used",
    "their",
    "there",
    "these",
    "those",
    "such",
    "also",
    "more",
    "most",
    "over",
    "under",
    "between",
    "because",
    "through",
    "during",
    "after",
    "before",
    "each",
    "only",
    "both",
    "all",
    "our",
    "they",
    "them",
    "its",
    "his",
    "her",
    "you",
    "your",
    "figure",
    "fig",
    "table",
    "journal",
    "mechanics",
    "physics",
    "solids",
    "elsevier",
    "page",
    "copyright",
    "license",
    "https",
    "doi",
}

ACADEMIC_NOUNS = {
    "model",
    "method",
    "framework",
    "mechanism",
    "analysis",
    "result",
    "results",
    "approach",
    "system",
    "response",
    "behavior",
    "parameter",
    "parameters",
    "simulation",
    "simulations",
    "experiment",
    "experiments",
    "validation",
    "comparison",
    "condition",
    "conditions",
    "assumption",
    "assumptions",
    "equation",
    "equations",
    "solution",
    "solutions",
    "field",
    "fields",
    "strain",
    "stress",
    "energy",
    "material",
    "materials",
    "structure",
    "structures",
    "interface",
    "interfaces",
    "deformation",
    "transition",
    "instability",
    "localization",
    "coupling",
    "property",
    "properties",
    "scale",
    "scales",
}

ACADEMIC_VERBS = {
    "propose",
    "proposed",
    "develop",
    "developed",
    "derive",
    "derived",
    "show",
    "shown",
    "shows",
    "demonstrate",
    "demonstrated",
    "reveal",
    "revealed",
    "indicate",
    "indicates",
    "suggest",
    "suggests",
    "validate",
    "validated",
    "compare",
    "compared",
    "estimate",
    "estimated",
    "predict",
    "predicted",
    "capture",
    "captured",
    "investigate",
    "investigated",
    "evaluate",
    "evaluated",
    "formulate",
    "formulated",
    "solve",
    "solved",
    "simulate",
    "simulated",
}

ACADEMIC_ADJECTIVES = {
    "significant",
    "substantial",
    "critical",
    "dominant",
    "robust",
    "local",
    "global",
    "nonlinear",
    "linear",
    "dynamic",
    "static",
    "elastic",
    "plastic",
    "viscoelastic",
    "anisotropic",
    "heterogeneous",
    "homogeneous",
    "numerical",
    "experimental",
    "theoretical",
    "analytical",
    "quantitative",
    "qualitative",
    "effective",
    "stable",
    "unstable",
    "finite",
    "large",
    "small",
    "high",
    "low",
}

ACADEMIC_ADVERBS = {
    "significantly",
    "substantially",
    "systematically",
    "numerically",
    "experimentally",
    "theoretically",
    "analytically",
    "approximately",
    "potentially",
    "generally",
    "locally",
    "globally",
    "strongly",
    "weakly",
    "notably",
    "therefore",
    "however",
    "furthermore",
    "moreover",
    "consequently",
}

SECTION_TYPE_KEYWORDS = {
    "背景/引言型": ["introduction", "background", "motivation"],
    "方法/模型型": ["method", "model", "framework", "formulation", "theory", "simulation", "numerical"],
    "实验/材料型": ["experiment", "experimental", "material", "specimen", "setup"],
    "结果/验证型": ["result", "results", "validation", "comparison", "evaluation"],
    "机制/讨论型": ["discussion", "mechanism", "effect", "role", "influence", "transition"],
    "结论/展望型": ["conclusion", "conclusions", "future", "summary"],
    "引用/附录型": ["reference", "references", "appendix", "declaration", "acknowledg"],
}


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z\-]{2,}", text)]


def content_tokens(text: str) -> list[str]:
    return [t for t in tokenize(text) if t not in STOPWORDS and not t.isdigit()]


def body_text_for_language_stats(text: str) -> str:
    """Keep article body for language statistics and avoid references noise."""
    text = re.sub(r"(?m)^# Source PDF:.*$", "", text)
    text = re.sub(r"(?m)^# Extracted at:.*$", "", text)
    text = re.sub(r"(?m)^# Extraction method:.*$", "", text)
    text = re.sub(r"(?m)^# Pages:.*$", "", text)
    text = re.sub(r"(?m)^# PDF SHA256:.*$", "", text)
    text = re.sub(r"(?m)^=+ PAGE \d+ / \d+ =+\s*$", "", text)
    references = re.search(r"(?mi)^\s*References\s*$", text)
    if references:
        text = text[: references.start()]
    return text


def top(counter: Counter[str], n: int = 12) -> str:
    if not counter:
        return "无明显高频项"
    return "；".join(f"{word}({count})" for word, count in counter.most_common(n))


def ngrams(tokens: list[str], n: int) -> Counter[str]:
    grams: Counter[str] = Counter()
    for i in range(len(tokens) - n + 1):
        gram = tokens[i : i + n]
        if any(item in STOPWORDS for item in gram):
            continue
        grams[" ".join(gram)] += 1
    return grams


def heading_type(title: str) -> str:
    lower = title.lower()
    for label, keywords in SECTION_TYPE_KEYWORDS.items():
        if any(keyword in lower for keyword in keywords):
            return label
    if re.search(r"\b(effect|role|influence|dependence|transition|scaling|law)\b", lower):
        return "问题/机制型"
    return "描述型"


def heading_function(label: str) -> str:
    return {
        "背景/引言型": "建立问题背景、研究动机和文献缺口",
        "方法/模型型": "交代模型、公式、算法、参数或求解流程",
        "实验/材料型": "说明样品、实验设置、数据来源或测量方式",
        "结果/验证型": "展示核心结果、对比、验证或参数分析",
        "机制/讨论型": "解释结果背后的物理机制或理论含义",
        "结论/展望型": "收束贡献、边界和未来工作",
        "引用/附录型": "提供支撑材料、声明或文献来源",
        "问题/机制型": "围绕变量关系或机制问题组织读者预期",
        "描述型": "描述章节内容，信息量取决于标题具体程度",
    }.get(label, "描述章节内容")


def extract_section_headings(text: str) -> list[tuple[str, str]]:
    headings: list[tuple[str, str]] = []
    seen = set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or len(line) > 140:
            continue
        if re.match(r"=+ PAGE", line):
            continue
        match = re.match(r"^(\d+(?:\.\d+){0,3})\.?\s+([A-Z][A-Za-z0-9 ,;:\-\(\)/]+)$", line)
        if not match:
            continue
        number, title = match.groups()
        lower = title.lower()
        if lower.startswith(("doi", "https", "journal", "received")):
            continue
        key = (number, title)
        if key in seen:
            continue
        seen.add(key)
        headings.append((number, title))
    return headings[:30]


def split_sections(text: str, headings: list[tuple[str, str]]) -> dict[str, str]:
    chunks: dict[str, str] = {}
    if not headings:
        chunks["全文"] = text
        return chunks
    pattern_parts = [
        re.escape(f"{number}. {title}") for number, title in headings[:20]
    ] + [re.escape(f"{number} {title}") for number, title in headings[:20]]
    pattern = re.compile(r"(?m)^(" + "|".join(pattern_parts) + r")\s*$")
    matches = list(pattern.finditer(text))
    if not matches:
        chunks["全文"] = text
        return chunks
    chunks["Abstract/首页"] = text[: matches[0].start()]
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        chunks[match.group(1)] = text[start:end]
    return chunks


def estimate_voice_and_tense(text: str) -> dict[str, int]:
    lower = text.lower()
    passive = len(
        re.findall(
            r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en)\b",
            lower,
        )
    )
    active_we = len(
        re.findall(
            r"\bwe\s+(?:propose|develop|derive|show|demonstrate|present|introduce|investigate|evaluate|compare|formulate|use|apply)\b",
            lower,
        )
    )
    present_perfect = len(re.findall(r"\b(?:has|have)\s+(?:been\s+)?\w+(?:ed|en|wn)\b", lower))
    past = len(re.findall(r"\b(?:was|were|used|showed|demonstrated|observed|obtained|performed|computed|measured|found)\b", lower))
    present = len(re.findall(r"\b(?:is|are|shows|demonstrates|indicates|suggests|provides|reveals|depends|increases|decreases)\b", lower))
    modal = len(re.findall(r"\b(?:may|might|can|could|should|would)\b", lower))
    nominal = len(re.findall(r"\b\w+(?:tion|ment|ity|ness|ance|ence|sis|ing)\b", lower))
    return {
        "passive": passive,
        "active_we": active_we,
        "present_perfect": present_perfect,
        "past": past,
        "present": present,
        "modal": modal,
        "nominal": nominal,
    }


def classify_word_counters(tokens: list[str]) -> dict[str, Counter[str]]:
    token_counter = Counter(tokens)
    nouns = Counter({word: token_counter[word] for word in ACADEMIC_NOUNS if word in token_counter})
    verbs = Counter({word: token_counter[word] for word in ACADEMIC_VERBS if word in token_counter})
    adjectives = Counter(
        {word: token_counter[word] for word in ACADEMIC_ADJECTIVES if word in token_counter}
    )
    adverbs = Counter(
        {word: token_counter[word] for word in ACADEMIC_ADVERBS if word in token_counter}
    )

    suffix_nouns = Counter(
        {
            word: count
            for word, count in token_counter.items()
            if re.search(r"(tion|ment|ity|ness|ance|ence|sis|ism|ure)$", word)
        }
    )
    suffix_adjectives = Counter(
        {
            word: count
            for word, count in token_counter.items()
            if re.search(r"(al|ive|ous|ic|able|ible|ary|ent|ant|less)$", word)
        }
    )
    suffix_adverbs = Counter(
        {word: count for word, count in token_counter.items() if word.endswith("ly")}
    )

    nouns.update(suffix_nouns)
    adjectives.update(suffix_adjectives)
    adverbs.update(suffix_adverbs)
    return {
        "all": token_counter,
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives,
        "adverbs": adverbs,
        "bigrams": ngrams(tokens, 2),
        "trigrams": ngrams(tokens, 3),
    }


def infer_heading_parallelism(headings: list[tuple[str, str]]) -> str:
    if len(headings) < 3:
        return "章节标题数量较少，难以判断并列性。"
    first_words = [title.split()[0].lower() for _, title in headings if title.split()]
    repeated = Counter(first_words).most_common(1)[0][1] if first_words else 0
    if repeated >= max(3, math.ceil(len(first_words) * 0.35)):
        return "同级标题存在一定句法并列性，多个标题以相似关键词或名词结构起始。"
    return "同级标题并列性一般，更偏按内容对象自然展开。"


def section_analysis_block(text: str, record: dict) -> str:
    headings = extract_section_headings(text)
    if not headings:
        heading_rows = "| 未识别 | 描述型 | 需人工从 PDF 目录或版面核查 | 低 | 否 | 从 PDF 章节页重建标题 |\n"
        heading_summary = "自动识别未抓到稳定章节标题，可能是 PDF 抽取换行或标题样式导致。"
        heading_count = 0
    else:
        rows = []
        for number, title in headings[:14]:
            label = heading_type(title)
            info = "高" if len(title.split()) >= 5 or label in {"问题/机制型", "结果/验证型"} else "中"
            mimic = "是" if label not in {"引用/附录型"} else "否"
            suggestion = "保留具体变量/对象" if info == "高" else "可加入核心变量或机制词增强信息量"
            rows.append(
                f"| {number} {title} | {label} | {heading_function(label)} | {info} | {mimic} | {suggestion} |"
            )
        heading_rows = "\n".join(rows) + "\n"
        heading_summary = infer_heading_parallelism(headings)
        heading_count = len(headings)

    major = [h for h in headings if "." not in h[0]]
    imrad_terms = " ".join(title.lower() for _, title in major)
    imrad = (
        "接近标准 IMRaD，但带有 JMPS 常见的理论/模型/验证扩展。"
        if all(term in imrad_terms for term in ["introduction"])
        and any(term in imrad_terms for term in ["method", "model", "result", "conclusion"])
        else "非严格 IMRaD，更像按模型、机制或结果模块组织。"
    )

    return f"""<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->

### 11.x 章节结构与章节名分析（补充）

> 自动分析说明：以下基于 `jmps/文本/txt/{record['stem']}.txt` 的章节标题抽取与标题关键词判断生成；PDF 抽取可能漏掉跨行小标题，最终章节名仍建议结合原 PDF 目录和版面核查。

- 识别到的章节/小节数量：{heading_count}
- 结构类型判断：{imrad}
- 标题并列性：{heading_summary}
- 章节名主要风格：{', '.join(sorted(set(heading_type(title) for _, title in headings[:12]))) if headings else '未稳定识别'}
- 标题信息量判断：若标题含具体变量、机制、效应、验证对象，信息量较高；若只写 `Results` / `Discussion`，则更依赖正文推进。

| 章节/小节名 | 标题类型 | 章节功能 | 信息量 | 是否可模仿 | 改写建议 |
| --- | --- | --- | --- | --- | --- |
{heading_rows}
写作启发：章节名不要只是目录标签，而应承担“读者导航”功能。若本文标题已经暴露变量或机制，可学习其标题信息密度；若标题偏泛，则在自己的论文中可把核心对象、作用变量或验证任务写进小节名。

<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->
"""


def language_analysis_block(text: str, record: dict) -> str:
    stats_text = body_text_for_language_stats(text)
    tokens = content_tokens(stats_text)
    counters = classify_word_counters(tokens)
    stats = estimate_voice_and_tense(stats_text)
    chunks = split_sections(stats_text, extract_section_headings(stats_text))
    section_freq_lines = []
    for name, chunk in list(chunks.items())[:8]:
        section_freq_lines.append(f"- {name}：{top(Counter(content_tokens(chunk)), 8)}")
    section_freq = "\n".join(section_freq_lines) if section_freq_lines else "- 未能稳定分章统计。"

    passive = stats["passive"]
    active = stats["active_we"]
    voice_comment = (
        "被动语态明显多于 we 主动句，说明作者倾向把实验、求解和结果写成客观过程。"
        if passive > active * 2
        else "we 主动句与被动语态都较明显，说明作者既强调本文动作，也保留客观过程表述。"
    )
    tense_comment = (
        "一般现在时最突出，适合图表说明、模型定义和领域事实；过去时用于本文操作或已完成结果；现在完成时主要连接已有研究。"
        if stats["present"] >= stats["past"]
        else "过去时相对突出，说明文本中实验/仿真步骤和已完成操作占比较高；现在时仍用于图表说明和一般性判断。"
    )

    return f"""<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->

### 13.x 词频、词类与语法统计（补充）

> 自动分析说明：以下为基于 TXT 的启发式统计，适合发现语言习惯；它不是严格 NLP 词性标注。公式符号、作者信息、参考文献和 PDF 断行可能影响个别词频，使用时应结合正文语境判断。

**词频总览**

- Top 高频词：{top(counters['all'], 20)}
- 高频学术名词：{top(counters['nouns'], 16)}
- 高频学术动词：{top(counters['verbs'], 16)}
- 高频形容词：{top(counters['adjectives'], 16)}
- 高频副词/连接副词：{top(counters['adverbs'], 16)}
- 高频二词短语：{top(counters['bigrams'], 16)}
- 高频三词短语：{top(counters['trigrams'], 12)}

**主动、被动与句法**

- 被动语态估计次数：{passive}
- `we + 动作动词` 主动句估计次数：{active}
- 名词化表达估计次数：{stats['nominal']}
- 语态判断：{voice_comment}
- 句法习惯：若高频名词化和被动语态较多，说明文章倾向把研究过程写成“模型/结果/参数”的客观链条；若 `we` 主动句较多，则更强调作者的框架构建和贡献动作。

**时态与情态**

- 一般现在时线索：{stats['present']}
- 一般过去时线索：{stats['past']}
- 现在完成时线索：{stats['present_perfect']}
- 情态动词线索：{stats['modal']}
- 时态判断：{tense_comment}
- 写作启发：Introduction 和图表说明通常适合现在时；本文实验、仿真、参数识别适合过去时；已有研究综述常用现在完成时；外推、局限和未来工作要用 may/could/should 控制强度。

**章节词频分布**

{section_freq}

**可复用观察**

- 高频名词若集中在研究对象、模型变量和机制词上，说明论文语言服务核心贡献；若高频词过散，读者会难以抓住主线。
- 高频动词中 `show/demonstrate/validate` 偏结果证明，`suggest/indicate` 偏机制解释，`propose/develop/formulate` 偏方法贡献。拆论文时应看这些动词是否与证据强度匹配。
- 形容词和副词要检查证据支撑：`significant/substantial/robust` 需要量化或多条件验证；`potentially/approximately/likely` 则说明作者在主动控制 claim 边界。

<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->
"""


def replace_or_insert(text: str, block: str, start_marker: str, end_marker: str, before_pattern: str) -> str:
    pattern = re.compile(
        re.escape(start_marker) + r".*?" + re.escape(end_marker),
        flags=re.DOTALL,
    )
    if pattern.search(text):
        return pattern.sub(block.strip(), text)
    match = re.search(before_pattern, text, flags=re.MULTILINE)
    if not match:
        return text.rstrip() + "\n\n" + block.strip() + "\n"
    return text[: match.start()].rstrip() + "\n\n" + block.strip() + "\n\n" + text[match.start() :]


def augment_file(md_path: Path, txt_path: Path, record: dict) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    txt_text = txt_path.read_text(encoding="utf-8", errors="replace")
    section_block = section_analysis_block(txt_text, record)
    language_block = language_analysis_block(txt_text, record)
    md_text = replace_or_insert(
        md_text,
        section_block,
        "<!-- AUTO-AUGMENT:SECTION-ANALYSIS START -->",
        "<!-- AUTO-AUGMENT:SECTION-ANALYSIS END -->",
        r"^## 12\.",
    )
    md_text = replace_or_insert(
        md_text,
        language_block,
        "<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY START -->",
        "<!-- AUTO-AUGMENT:LANGUAGE-FREQUENCY END -->",
        r"^## 14\.",
    )
    md_path.write_text(md_text.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Augment deep JMPS analyses with language and section statistics.")
    parser.add_argument("--manifest", default="jmps/文本/_manifest.json")
    parser.add_argument("--txt-dir", default="jmps/文本/txt")
    parser.add_argument("--analysis-dir", default="jmps/深度拆解/papers")
    args = parser.parse_args()

    records = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    txt_dir = Path(args.txt_dir)
    analysis_dir = Path(args.analysis_dir)
    updated = 0
    missing: list[str] = []

    for record in records:
        stem = record["stem"]
        md_path = analysis_dir / f"{stem}.md"
        txt_path = txt_dir / f"{stem}.txt"
        if not md_path.exists() or not txt_path.exists():
            missing.append(stem)
            continue
        augment_file(md_path, txt_path, record)
        updated += 1

    print(f"updated={updated} missing={len(missing)}")
    if missing:
        for stem in missing:
            print(f"missing: {stem}")


if __name__ == "__main__":
    main()
