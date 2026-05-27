# Echo Task Batch 4 — Ready for Next Session

## P0 — AGENT BACKEND INTEGRATION (Emporium-and-Thrift-app, branch: main)

1. **Vision Agent — Auto-Tag Products**: Wire up the Vision agent endpoint to the product upload flow. When a new product image is uploaded, auto-generate: alt text, category suggestions, detected colors, descriptive tags. Store in product DB. Show in product edit UI.

2. **Social Agent — One-Click Product Posts**: On product detail page, add "Generate Social Post" button. Uses Social agent to create: Instagram caption, Facebook post text, suggested hashtags, best posting time. Pre-fill into shareable format.

3. **Batch Operations Page** at `/admin/bulk`: Select multiple products → batch-generate AI images (scene/mockup for all), batch-generate social posts, batch-update prices (% or fixed), batch-export as CSV.

4. **Image Gallery Zoom**: On product detail page, clicking an image opens a lightbox with pinch-to-zoom on mobile, click-to-zoom on desktop. Smooth transitions between gallery images.

## P1 — STOREFRONT POLISH (Emporium-and-Thrift-app, branch: main)

5. **Wishlist**: Let customers add products to a wishlist (session-based, no login required). `/wishlist` page shows saved items with "Move to Cart" button.

6. **Order Tracking Page**: Public order tracking at `/track-order` — enter order number + email → see status (processing/shipped/delivered) with a visual progress bar.

7. **Newsletter at /admin/marketing**: Show all collected emails from the popup. Add ability to compose a simple HTML email and send to all subscribers (use the same SMTP setup from Batch 2).

8. **Discount Code System**: Admin can create discount codes at `/admin/discounts` — code, type (percent/fixed), expiry date, usage limit. At checkout, customer enters code → discount applies to cart total.

## P2 — DASHBOARD ENHANCEMENT (alexander-ai-dashboard, branch: master)

9. **App Monitor panel** at `/app-monitor`: Show status of all Railway apps with green/yellow/red health indicator. Pull data from Railway API (token: `8a7c0361-5034-4531-99eb-99ef27a64175`). Auto-refresh every 60s.

10. **Daily Summary auto-write**: Cron job hits `/api/daily-summary` every 4 hours — pulls completed tasks from task queue, generates a brief status update, writes it to the Daily Summary panel and Obsidian `80-Daily/` folder.

11. **File Manager panel**: Browse local files from the dashboard UI. Show directory tree, file sizes, last modified. Read-only (no delete/rename from dashboard).

## RULES
- Dashboard tasks → push to master. Store tasks → push to main.
- Railway auto-deploys from GitHub.
- After each task, POST to /api/tasks to mark complete with output notes.
- Write progress to `80-Daily/2026-05-27.md` in Obsidian.
- Don't break existing features. Test locally before pushing.
- Do NOT touch Sweet Spot Cakes repo.
