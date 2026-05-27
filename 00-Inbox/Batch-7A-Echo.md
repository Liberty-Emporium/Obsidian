# Echo Task Batch 7A — Storefront UX Fixes + Features

## CRITICAL: Do NOT break the live store. Jay's mom is actively adding products.

## P0 — UX FIXES (store app, branch: main)

Fix these 4 items Jay found on the live store:

1. **Cart icon in header**: Add a cart icon with item count badge to the store header/nav on ALL pages. Clicking goes to /cart. Show cart count badge (red circle with number) that updates via JS.

2. **Login/Profile in hamburger menu**: 
   - When logged out: show "Create Account" and "Login" links
   - When logged in: show "My Orders", "Profile", "Logout" links
   - On desktop, show a "Hi, [name]!" dropdown in the nav

3. **Categories in navigation**: 
   - Show category links in the hamburger menu and/or the main nav bar
   - Each category links to /category/<slug>
   - Only show categories that have at least 1 product
   - Auto-update the nav when new categories are added via /admin/categories

4. **Store header cleanup**: Make sure the logo area shows the store name prominently. Keep it clean and professional.

## P1 — STOREFRONT FEATURES (store app, branch: main)

5. **Advanced CRM**: Add customer notes on /admin/customers. Follow-up date field. Highlight overdue follow-ups.

6. **Order Timeline**: Visual timeline on /admin/orders/<id> (Placed → Processing → Shipped → Delivered). Auto-note on status change.

7. **Search Autocomplete**: Search bar in store header. Dropdown with product names + thumbnails. Debounce 300ms.

8. **Announcement Banner**: At /admin/settings. Color picker (green/yellow/red). Shows banner on all store pages. Customer can dismiss.

## RULES
- Store → main branch
- Verify after EACH push
- POST completions to /api/tasks
- Write to 80-Daily/2026-05-27.md in Obsidian
- Don't break existing features
