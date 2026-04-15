# CO — Continuous Optimization

Optimizations applied:

- Evaluation logic: track ungated violations separately to prevent false FULLY_ADMISSIBLE
- Annotation clutter: cap at MAX_ANNOTATIONS = 30 with thinning
- Compliance rate: guard against ZeroDivisionError on empty data
- Matplotlib style: cross-version fallback (seaborn-v0_8-whitegrid → seaborn-whitegrid → default)
