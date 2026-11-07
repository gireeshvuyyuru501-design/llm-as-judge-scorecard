"""Offline rubric-based QA scorecard. NOT an LLM-as-judge inference implementation."""
import json
import re
from pathlib import Path

TOKEN = re.compile(r"\b\w+\b")

def tokens(text):
    return set(TOKEN.findall(text.lower()))

def score_case(case):
    """Compute reproducible lexical overlap and basic response checks."""
    response = case['response']
    reference = case['reference']
    rt, gt = tokens(response), tokens(reference)
    precision = len(rt & gt) / len(rt) if rt else 0.0
    recall = len(rt & gt) / len(gt) if gt else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {'id': case['id'], 'lexical_f1': round(f1, 4), 'nonempty': bool(response.strip()), 'human_rating': case.get('human_rating')}

def evaluate(cases):
    if not cases:
        raise ValueError('At least one case required')
    results = [score_case(c) for c in cases]
    return {'method': 'offline_lexical_baseline_not_llm_judge', 'count': len(results), 'mean_lexical_f1': round(sum(r['lexical_f1'] for r in results)/len(results), 4), 'results': results}

def main():
    base = Path(__file__).resolve().parent
    cases = json.loads((base / 'data' / 'sample_cases.json').read_text(encoding='utf-8'))
    report = evaluate(cases)
    (base / 'scorecard_report.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
