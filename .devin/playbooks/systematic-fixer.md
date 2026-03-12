# Playbook: Systematic Fixer (The Ralph Wiggum Loop)

## Phase 1: Context & Reproduction
1. **Locate**: Identify the target file in `src/` based on the issue description.
2. **Reproduce**: Create a `repro.py` script that fails due to the bug. 
   *Requirement*: You MUST prove the failure before editing code.

## Phase 2: Workstream Execution (Personality-Based)
Follow the constraints assigned to your specific Agent Role:

### Agent Alpha (The Minimalist)
**Objective**: Fix the bug with the absolute minimum number of lines changed.
**Constraint**: Do not refactor architecture; only fix the immediate logic error.

### Agent Beta (The Refactor) 
**Objective**: Modernize the code while fixing the bug
**Constraint**: Use `decimal.Decimal` for all currency/math. Do not use floats.

### Agent Gamma (The Robust) 
**Objective**: Provide a "Gold Standard" enterprise fix.
**Constraint**: Perform the Beta refactor PLUS add 5 additional edge-case unit tests.

## Phase 3: The Ralph Wiggum Loop (Autonomous Correction)
1. **Apply Fix**: Modify the code according to your role.
2. **Verify**: Run `scripts/verify.py`.
3. **Loop**: If it fails, capture the traceback, analyze the error, and re-apply a fix. Repeat until passes.
4. **Guardrail**: Do not move to the next file until the current one passes all unit tests.

## Phase 4: Final Validation
* Delete `repro.py` and temporary artifacts.
* Regressions: Run the full pytest suite to ensure no other logic broke.
* Push changes to your assigned sub-branch (e.g., `fix/gamma`).
