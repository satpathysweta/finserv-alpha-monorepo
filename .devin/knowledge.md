# FinServ Business Logic & Standards
- **Currency Rule:** NEVER use `float` for money. Always use `decimal.Decimal`.
- **Logic:** We use Compound Interest: A = P(1 + r/n)^{nt}.
- **Formatting:** Currency must always be prefixed with `$` and rounded to 2 decimal places.
