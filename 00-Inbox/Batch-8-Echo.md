# Echo Task Batch 8 — Final Polish

## P0 — SPEED + PERFORMANCE (store app, branch: main)

1. **Image Optimization**: 
   - Compress uploaded product images (max 1200px wide, 80% quality JPEG)
   - Generate thumbnails (300x300) for product grids
   - Use lazy loading on all product images (`loading="lazy"`)

2. **Database Indexing**: Add SQL indexes on: products(category, price), orders(status, created_at), customers(email)

3. **CSS/JS Minification**: Minify the main CSS and JS files. Use Flask-Assets or manual minification.

4. **Caching**: Add browser caching headers for static assets (CSS, JS, images). Cache product listings for 5 minutes server-side.

## P1 — ERROR HANDLING (store app, branch: main)

5. **Custom 404 Page**: Branded 404 page matching store design. Include search bar + link to homepage.

6. **Custom 500 Page**: Branded error page. "Something went wrong — we're on it!" + link to homepage.

7. **Form Validation**: All forms have proper client-side AND server-side validation. Error messages are clear and helpful.

8. **Empty States**: Empty cart shows "Your cart is empty — start shopping!" with link to store. Empty search results show "No results — try a different search."

## P2 — SEO FINAL PASS (store app, branch: main)

9. **Structured Data validation**: Test all product pages with Google Rich Results Test. Fix any errors.

10. **Meta descriptions**: Every page has a unique, compelling meta description under 160 characters.

11. **Alt text**: Every product image has descriptive alt text. No images missing alt attributes.

12. **Page titles**: Every page has a unique, keyword-rich title tag.

## P3 — SECURITY (store app, branch: main)

13. **CSRF Protection**: Add Flask-WTF CSRF protection to all forms.

14. **Rate Limiting**: Add Flask-Limiter to API endpoints (100 requests per minute per IP).

15. **Security Headers**: Add X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security headers.

## P4 — DASHBOARD (dashboard, branch: master)

16. **Fix require_auth decorator**: The @require_auth function is MISSING from app.py. It's used 10 times but never defined. ADD IT:

```python
def require_auth(f):
    """Decorator: require valid bearer token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not check_bearer_token():
            return jsonify({'error': 'unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated
```

Add this after the login_required function (around line 475).

## RULES
- Store → main. Dashboard → master.
- After ALL tasks, do a full QA walkthrough of every feature
- Write final summary to 80-Daily/2026-05-27.md
- Don't break existing features
- This is the FINAL batch — make it count!
