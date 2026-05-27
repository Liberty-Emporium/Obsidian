# Echo Task Batch 6 — Session 4

## P0 — STOREFRONT PRODUCT FEATURES (store app, branch: main)
1. **Recently Viewed fix + enhance**: Make sure Recently Viewed actually works on the live site. Show thumbnail + title + price. Add a "Clear Recently Viewed" button. Place section above footer on homepage AND sidebar on product pages.

2. **Related Products algorithm**: Already built — verify it's working on live product pages. Should show 4 related products based on: same category (primary), similar price +/- 30%, most popular first. Don't show out-of-stock items.

3. **Product Image Gallery Manager**: Multi-image upload on product edit page, drag-to-reorder, set primary image. Integrate the existing Image Manager (from AI Studio) into the product creation flow.

4. **Inventory Low Stock Alerts**: When product quantity drops below 5 (configurable), show a yellow warning badge on the product in admin. At /admin/inventory, show all products sorted by stock level.

5. **Discount Code improvements**: Add ability to set: minimum order amount, one-time use per customer, product-specific discounts (only applies to certain products). Show discount code usage count in admin.

## P1 — AI FEATURES (store app, branch: main)
6. **AI Product Description Generator**: On product edit page, add "Generate with AI" button. Sends product name + category + existing description to OpenRouter. Returns a compelling, SEO-friendly product description. User can edit before saving.

7. **Vision Agent Auto-Tagging**: When a product image is uploaded, auto-generate: alt text, category suggestions, detected colors, descriptive tags. Store in product DB. Display in product edit UI for review/editing.

8. **Social Media Post Generator**: On product detail page, add "Create Social Post" button. Generates: Instagram caption (with emojis + hashtags), Facebook post text, Twitter/X post (280 chars), suggested hashtags. Uses OpenRouter.

## P2 — DASHBOARD (dashboard, branch: master)
9. **App Monitor panel**: Show all Railway projects with health status (green/yellow/red). Pull from Railway API. Auto-refresh every 60s. Show: project name, status, last deploy date.

10. **Daily Summary auto-write**: Build a /api/daily-summary endpoint. When called, pulls completed tasks from task queue, generates a brief status update, writes to Daily Summary panel AND Obsidian 80-Daily/ folder. Set up cron to hit it every 4 hours.

11. **File Manager panel**: Browse local files from dashboard UI. Show directory tree, file sizes, last modified date. Read-only (no delete/rename from dashboard).

## RULES
- Store → main branch. Dashboard → master branch.
- Railway auto-deploys from GitHub.
- POST task completions to /api/tasks API.
- Write progress to 80-Daily/2026-05-27.md in Obsidian.
- Don't break existing features. Test locally before pushing.
- Do NOT touch Sweet Spot Cakes repo.
- SKIP email/SMTP tasks — Jay handling that separately.
