# Playbook: Dynamic Priority Engine (Lead Systems Architect)

## Objective
Analyze the GitHub issue backlog and produce a triage_manifest.json that buckets tasks based on Business Impact, Fixability, Blast Radius, and Regression Risk.

## Step 1: Denoising (The "Vanish" Protocol)
* List all open issues using GitHub CLI (gh issue list). 
* For each issue, attempt to reproduce the bug on the main branch.
* If an issue is no longer reproducible, mark its status as "Stale" in the final output.

## Step 2: Multi-Factor Scoring Matrix
Evaluate every active issue based on these four parameters:
1. **Business Impact**: High if the code involves "revenue", "auth", or "security" keywords. 
2. **Fixability Score**: High if the bug is in a local logic file; Low if it involves complex legacy libraries. 
3. **Blast Radius**: High if the affected file is imported by more than 5 other modules. 
4. **Regression Risk**: High if the module has < 80% test coverage. 

## Step 3: Bucketing Logic
Assign each issue to one of the following buckets based on the scores: 
* **Auto-Fix**: High Fixability + Low Blast Radius + Low Impact. 
* **Agent Orchestrator**: High Impact + Medium/High Fixability (suitable for parallel Devin competition). 
* **Human Engineer**: High Blast Radius + High Impact + Low Fixability.

## Output Format
Generate a triage_manifest_new.json in the root directory. 
