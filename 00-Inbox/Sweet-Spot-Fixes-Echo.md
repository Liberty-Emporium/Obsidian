# Echo — Sweet Spot Cakes Fixes

## P0 — Staff Login in Footer (ALL pages)

**Problem**: Staff login link is buried in the top-right corner. Hard to find.

**Fix**: Add a "Staff Login" link to the footer on EVERY page including the landing page.

### Changes needed:

**1. `templates/base.html`** — Add footer with staff login BEFORE the closing `</body>` tag (after line 290, before the AI widget script):

Find this line:
```html
{% block extra_js %}{% endblock %}
<script src="https://ai-agent-widget-production.up.railway.app/widget/Fx9e5L1JSpqJtjnhl2jLsQ.js"></script>
```

Replace with:
```html
{% block extra_js %}{% endblock %}

<!-- Footer with Staff Login -->
<footer style="margin-left:230px;padding:24px 28px;border-top:1px solid #3d1a28;text-align:center;font-size:.82rem;color:#9d8890;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
  <span>&copy; {{ now().year if now is defined else '2026' }} Sweet Spot Custom Cakes. All rights reserved.</span>
  <a href="/login" style="display:inline-flex;align-items:center;gap:6px;background:linear-gradient(135deg,#f472b6,#ec4899);color:#fff;padding:8px 20px;border-radius:8px;font-weight:600;font-size:.85rem;text-decoration:none;transition:opacity .2s" onmouseover="this.style.opacity='.88'" onmouseout="this.style.opacity='1'">🔐 Staff Login</a>
</footer>

<style>
@media(max-width:900px){
  footer{margin-left:0 !important;padding:16px !important;flex-direction:column;gap:8px}
}
</style>

<script src="https://ai-agent-widget-production.up.railway.app/widget/Fx9e5L1JSpqJtjnhl2jLsQ.js"></script>
```

**2. `templates/index.html`** — The landing page uses its own HTML (not base.html). Add the SAME footer at the bottom. Find the closing `</body>` tag and add the same footer HTML BEFORE it. Also add a small "Staff Login" link in the hero buttons area:

In the hero buttons div (around line 19-24), add a third button:
```html
<a href="/login" class="btn btn-ghost" style="font-size:.85rem;padding:10px 20px">🔐 Staff Login</a>
```

Also add the full footer before `</body>` in index.html.

## P1 — Login Flow Cleanup

**Problem**: Login page has both employee PIN AND staff email/password. Jay wants:
- **Administrators only** → email + password login  
- **Everyone else** → PIN number login (no email/password needed)

**Fix**: `templates/login.html`

Change the login form to default to PIN login (show PIN pad first, hide email/password behind a toggle or secondary option). The PIN tab should be the DEFAULT active tab, not the email tab.

In the JavaScript that controls the tab switching, make the PIN tab active on page load:
- Find the JS that handles tab switching (something like `showTab('pin')` or `showTab('email')`)
- Change the default to PIN tab

Also update the tab labels:
- Tab 1: "🔑 Staff PIN" (default active)  
- Tab 2: "👤 Administrator" (for email/password)

## P2 — What Else to Fix

Looking at the app, here are additional issues to address:

1. **Remove echo_reporter from Sweet Spot** — This is a monitoring tool that doesn't belong in a client's production app. Remove:
   - Line 2: `from echo_reporter import install_reporter`
   - Line 44: `install_reporter(app, 'Sweet Spot Custom Cakes')`
   
2. **Verify the menu page works for ordering** — The `/menu` page shows products, and the `/order` page handles customer orders. Test that a customer can:
   - Browse the menu
   - Select a cake size/flavor
   - Add to order
   - Submit the order
   - Reach the confirmation page
   
3. **Check the database has seed data** — If staff can't log in, the `employees` and `users` tables might need default records inserted.

## RULES
- Sweet Spot Cakes → push to `main` branch on `Liberty-Emporium/sweet-spot-cakes`
- verify live at sweet-spot-cakes.up.railway.app after each push
- DO NOT touch any other repo
