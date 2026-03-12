# Playbook: Dynamic Priority Engine (Lead Systems Architect)

## Objective
Analyze the GitHub issue backlog and produce a triage_manifest.json that buckets tasks based on Business Impact, Fixability, Blast Radius, and Regression Risk. [cite: 52]

## Step 1: Denoising (The "Vanish" Protocol)
* List all open issues using GitHub CLI (gh issue list). [cite: 46]
* For each issue, attempt to reproduce the bug on the main branch. [cite: 47]
* If an issue is no longer reproducible, mark its status as "Stale" in the final output. [cite: 48]

## Step 2: Multi-Factor Scoring Matrix
Evaluate every active issue based on these four parameters: [cite: 52]
1. **Business Impact**: High if the code involves "revenue", "auth", or "security" keywords. [cite: 52]
2. **Fixability Score**: High if the bug is in a local logic file; Low if it involves complex legacy libraries. [cite: 52]
3. **Blast Radius**: High if the affected file is imported by more than 5 other modules. [cite: 52]
4. **Regression Risk**: High if the module has < 80% test coverage. [cite: 52]

## Step 3: Bucketing Logic
Assign each issue to one of the following buckets based on the scores: [cite: 54]
* **Auto-Fix**: High Fixability + Low Blast Radius + Low Impact. [cite: 54]
* **Agent Orchestrator**: High Impact + Medium/High Fixability (suitable for parallel Devin competition). [cite: 54]
* **Human Engineer**: High Blast Radius + High Impact + Low Fixability. [cite: 54]

## Output Format
Generate a triage_manifest.json in the root directory. [cite: 56]
