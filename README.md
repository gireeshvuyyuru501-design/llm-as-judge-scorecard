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

<!-- PORTFOLIO-OVERVIEW-START -->

## Project overview

Offline lexical-overlap scoring for evaluating response quality without live LLM inference.

### Technologies and concepts

 - python
 - llm evaluation
 - evaluation
 - ai testing
 - nlp

### Repository information

- **Category:** AI Quality Engineering / Software Testing
- **Evaluation type:** Offline and/or synthetic fixtures, as documented in this repository
- **Source code:** [GitHub repository](https://github.com/gireeshvuyyuru501-design/llm-as-judge-scorecard.git)
- **License:** MIT (subject to repository license file)

### AI Quality Engineering portfolio

This project is part of an 11-project portfolio covering evaluation datasets, structured-output validation, offline scoring, prompt regression, retrieval benchmarking, adversarial testing, agent tool calls, and quality monitoring.

[Explore the integrated AI Quality Engineering Platform](https://github.com/gireeshvuyyuru501-design/ai-quality-engineering-platform)

<!-- PORTFOLIO-OVERVIEW-END -->
