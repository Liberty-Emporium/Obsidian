# Echo Task Batch 7A — No Email Required

## P0 — ADVANCED STOREFRONT (store app, branch: main)
IMPORTANT: Do NOT take the store down. Your mom is adding products live. Every push must keep the site running.

1. **Advanced CRM — Customer Notes + Follow-ups**:
   - On /admin/customers, add a "Notes" text area per customer. Admin can write notes like "Called on 5/27 — interested in bulk order."
   - Add a "Follow-up date" field. At /admin/customers, highlight customers whose follow-up date is today or past due.
   - Add a "Last contact" auto-timestamp that updates whenever admin adds a note.

2. **Order Timeline Tracking**:
   - On the order detail page (/admin/orders/<id>), add a visual timeline: Order Placed → Processing → Shipped → Delivered
   - Each step shows timestamp when it was marked complete
   - Customers can see a simplified version at /track-order
   - When status changes, add a note to the order timeline automatically (e.g., "Status changed to Shipped on 5/27 at 2:15 PM")

3. **Product Search Autocomplete**:
   - Add a search bar to the store header (not just /search page)
   - As customer types, show dropdown with matching product names + thumbnails (AJAX fetch)
   - Click a result → go to product page
   - Debounce at 300ms to avoid flooding requests

4. **Store Announcement Banner**:
   - At /admin/settings, add a "Store Announcement" text field
   - When filled, shows a colored banner at the top of every store page (admin can set color: green/yellow/red)
   - Example: "Free shipping on orders over $50 this week!"
   - Dismissible by customer (saved in session/cookie)
   - Default: hidden

## P1 — FACEBOOK + MARKETING (store app, branch: main)
5. **Facebook Marketplace — Phase 2 (Real Posting)**:
   - Already have the scheduler (/admin/facebook) from Batch 3. Upgrade it.
   - Add `FB_ACCESS_TOKEN` env var on Railway when Jay provides it
   - When admin clicks "Post to Facebook", actually post to Facebook via the Graph API
   - Show success/failure status per post
   - If no FB_ACCESS_TOKEN is set, show a banner: "Connect Facebook to enable auto-posting" with a setup guide link

6. **SEO Structured Data (Schema.org)**:
   - Add JSON-LD structured data to every product page: Product name, description, price, availability, image, brand (Liberty Emporium), review aggregate
   - Add Organization schema to homepage
   - Add BreadcrumbList schema to category and product pages
   - This makes Google show rich snippets (star ratings, price) in search results
   - Test with Google's Rich Results Test tool

7. **Social Sharing Buttons**:
   - On every product page, add share buttons: Facebook, Pinterest, Twitter/X, WhatsApp, Email
   - Each button opens a pre-filled share dialog with product title, image, and link
   - Small, clean icons — not obtrusive
   - Mobile: show in a horizontal row below product description
   - Desktop: show as floating sidebar on left of product image

## P2 — DASHBOARD (dashboard, branch: master)
8. **Echo Performance Dashboard**:
   - Add a "Stats" section to the Command Center showing:
     - Total tasks completed (from tasks DB)
     - Tasks per session
     - Average tasks per hour
     - Current session task count
   - Show a simple bar chart (use Chart.js CDN) of tasks per session
   - Update in real-time as Echo posts completions

## RULES — CRITICAL
- ⚠️ DO NOT BREAK THE LIVE STORE. Your mom is actively adding products.
- After EVERY push, verify the site still loads.
- If something breaks, IMMEDIATELY revert the commit.
- Store → main branch. Dashboard → master branch.
- POST completions to /api/tasks.
- Write progress to 80-Daily/2026-05-28.md in Obsidian.
- Do NOT touch Sweet Spot Cakes repo.
