# LLM-as-Judge Scorecard — Offline Baseline

A reproducible **starting point** for an LLM evaluation scorecard. Currently computes lexical precision/recall/F1 overlap between candidate responses and reference answers, and retains optional human ratings for later comparison. **This is not an LLM judge yet**; it does not call a model, and lexical overlap cannot reliably detect factual correctness (see the Kyoto example).

## Run

```bash
python -m unittest discover -s tests -v
python scorecard.py
```

Output: `scorecard_report.json` (generated, not tracked). No dependencies or API key required.

## Roadmap

- Import a licensed, public human-judgment dataset with provenance
- Add Gemini judge adapter and rubric dimensions (correctness, grounding, relevance)
- Compare model judgments to human ratings with agreement statistics
- Add prompt injection safeguards and judge calibration
- Expose results through FastAPI and a shared React dashboard

The bundled `data/sample_cases.json` contains **four synthetic fixtures**, not a public benchmark dataset. No model-based results are claimed.
