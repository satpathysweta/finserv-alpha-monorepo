# Systematic Fixer SOP

## Phase 1: Context & Reproduction
1. **Initialize:** Read `.devin/agents.md` and `.devin/knowledge.md`.
2. **Baseline:** Run `pytest`. Confirm the existing code fails the financial logic tests.
3. **Hypothesis:** Based on the strategy provided in the session start (Alpha, Beta, or Gamma), formulate a fix plan.

## Phase 2: The Ralph Wiggum Loop
1. **Apply:** Implement the fix in `src/interest_calculator.py`.
2. **Verify:** Run `python3 scripts/verify.py`.
3. **Loop:** If verification fails:
   - Capture the error logs.
   - Revert the file to its last known state.
   - Adjust the hypothesis and repeat Step 1.
4. **Exit:** Only proceed once `verify.py` returns exit code 0.

## Phase 3: Final Validation
1. **Regressions:** Run the full `pytest` suite to ensure no other logic broke.
2. **Push:** Create a new branch named `fix/batch-1-[strategy-name]` and push the changes.
