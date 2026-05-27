# Echo Task Batch 5 — Session 3

## P0 — PUSH + VERIFY (both repos)
1. Push all Batch 4 commits (store → main, dashboard → master). Railway auto-deploys.
2. Verify live: homepage, products, cart/checkout, wishlist, discount codes, order tracking. Report bugs.

## P1 — STOREFRONT POWER FEATURES (store app, branch: main)
3. Customer Accounts + Login: /register, /login, order history, bcrypt passwords, wishlist migration
4. Categories + Navigation: Category model, /category/<name> pages, admin category management
5. Product Image Gallery Manager: Multi-image upload, drag-reorder, primary image — integrated into product creation
6. Recently Viewed Products: Last 10 viewed, session-based, shown on homepage + product pages
7. Facebook Marketplace Phase 2: Real posting via facebook-sdk, FB_ACCESS_TOKEN env var, /admin/facebook with test post button
8. Storefront Blog: /blog index, /blog/<slug>, /admin/blog editor, Markdown content, SEO meta tags

## P2 — DASHBOARD POLISH (dashboard, branch: master)
9. Support Clients panel: Clients DB table, cards for Sweet Spot/Billy Flood/Liberty Oil, status + next actions
10. Notifications system: Bell icon, task completion alerts, new order alerts, read/unread state
11. Mobile PWA: manifest.json, service worker, add-to-home-screen, native app feel

## RULES
- Dashboard → master. Store → main.
- After each task, POST to /api/tasks to mark complete.
- Write progress to 80-Daily/2026-05-27.md.
- Don't break existing features. Test locally before pushing.
- Do NOT touch Sweet Spot Cakes.

## Jay Action Items
- Give Echo new GitHub PAT so he can push Batch 4
- Facebook Developer access token for real Marketplace posting
- MAIL_SERVER / MAIL_USERNAME / MAIL_PASSWORD on Railway (store app)
- Upload model photo in AI Studio (fixes Try-On)
