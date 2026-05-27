# Echo — Sweet Spot Cakes Rollback Instructions

## The Problem
Your "revert" commit (4949b77) did NOT restore the original code. It still has:
- echo_reporter import (line 2)
- install_reporter call in app.py
- New CSV restore feature code
- Modified templates (base.html, menu.html, customers.html, order_detail.html, settings.html)

The revert was done wrong — it removed SOME of your Batch 7A code but left behind the echo_reporter additions and added NEW features on top.

## The Fix — Complete Clean Rollback

Run these commands IN ORDER:

```bash
cd /path/to/sweet-spot-cakes

# Step 1: Reset to the LAST clean commit before you touched anything
# The last clean commit is: 2a07982 (fix: resolve Internal Server Error on /order page)
git reset --hard 2a07982

# Step 2: Force push to overwrite the bad history on GitHub
git push --force-with-lease origin main

# Step 3: Verify — app.py should NOT contain "echo_reporter" or "install_reporter"
grep -n "echo_reporter\|install_reporter" app.py
# Should return NOTHING. If it finds lines, the rollback failed.

# Step 4: Verify templates — base.html should NOT have Echo monitoring injected
grep -n "echo_reporter\|ecdash\|EcDash" templates/base.html
# Should return NOTHING.
```

## What This Does
- `git reset --hard 2a07982` — moves the local HEAD back to the last known clean commit, discarding ALL of Echo's commits (both the Batch 7A ones AND the bad revert)
- `git push --force-with-lease` — overwrites GitHub history to match, removing the bad commits from the remote
- The `-with-lease` flag is safer than `--force` — it will fail if someone else pushed in the meantime

## After Rollback — What to Fix Before Going Live
Once the rollback is clean, these are the issues Jay mentioned that need fixing on Sweet Spot:

1. **Staff login not working** — Admin/staff can't log in. Check the login route and auth flow.
2. **Menu ordering broken** — Customers can't order from the menu. Check the menu page and order flow.
3. **General QA** — Walkthrough the entire site: homepage, menu, cart, checkout, admin pages.

## RULES FROM NOW ON
- BEFORE pushing ANY code: run `git remote -v` and confirm you're pushing to the RIGHT repo
- BEFORE pushing ANY code: run `grep -rn "echo_reporter\|install_reporter" .` and confirm ZERO matches
- BEFORE pushing to ANY repo other than Emporium-and-Thrift-App: get explicit confirmation from Jay
- If unsure, ASK before pushing. No push without a second pair of eyes.
