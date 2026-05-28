# ECHO TASK — Auto Tag AI → SEO Integration

**Priority:** High — Jay says SEO is what puts us first on Google

**Problem:** Auto Tag AI generates 10 tags and detects colors from product images, but it only DISPLAYS them on screen. They don't get saved anywhere or used in SEO fields.

**Solution:** Wire the AI-generated tags and colors into the product's SEO meta data:

1. **Meta keywords** — auto-populate with AI-generated tags
2. **Meta description** — optionally use AI tags to improve descriptions
3. **Image alt text** — auto-fill alt attribute with AI tags
4. **schema.org JSON-LD** — add tags to the `keywords` property in the structured data

**Where:** `Emporium-and-Thrift-App` → `main` branch

**Key files:**
- `agents/vision.py` — `auto_tag()` function (line 148)
- `app_with_ai.py` — `/api/agents/auto-tag` route (line 5082)
- Product model / database schema needs a `tags` field if it doesn't have one

**Note:** `OPENROUTER_API_KEY` is NOT set on Railway yet. Even after coding, the feature won't work in production until Jay sets that env var.
