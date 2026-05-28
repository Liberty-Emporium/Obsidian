# AI Studio Competitor Research & Rewrite Plan

**Date:** 2026-05-28
**Author:** OWL for Jay Alexander

---

## What Jay Wants

Jay saw AI photo apps on Google Play that do amazing things:
- Remove backgrounds with one click
- Put clothes on mannequins automatically
- Generate professional product photos from phone shots
- Create marketing images that look like a pro photographer did them
- Do it all in seconds

**Jay's quote:** "There's a lot of stuff on Google Play that takes out the background, puts clothes on a mannequin, does so much... We just need to reverse engineer and make it ours."

**His verdict on our current AI Studio:** "I absolutely hate it. It sucks. Nowhere near the competition."

---

## Competition Analysis

### Top Competitors on Google Play

| App | Rating | Key Features |
|-----|--------|-------------|
| **Photonoom: AI Photo Editor** | 4.7⭐ | Background remover, AI image generator, virtual model, product staging, background generator, batch editing, Shopify integration |
| **Pixelcut AI Photo Editor** | 4.2⭐ | Background removal, AI generation, upscaling, batch editing, expand/resize, shadow generation |
| **Product Plus: AI Product Photo** | 5.0⭐ | Specifically for product photos, AI backgrounds, mockups |
| **Canva: AI Photo & Video** | 4.8⭐ | Full design suite, AI background remover, Magic Edit, text-to-image |
| **Adobe Express** | 4.6⭐ | AI-powered, background removal, resize, brand kit |
| **VogueShot: AI Fashion Studio** | 4.1⭐ | AI fashion photos, virtual models, clothing on mannequins |
| **Dressify - AI Clothes Changer** | 4.4⭐ | Put clothes on virtual models automatically |
| **Relatable: AI Fashion Photos** | N/A | AI-generated fashion photos for ecommerce |

### Key Features Our Competition Has (That We Don't)

1. **One-click background removal** — Works on ANY product, even transparent/glass items
2. **AI-generated lifestyle scenes** — Place products in contextual backgrounds (food on table, jewelry on velvet, shoes on street)
3. **Virtual model/mannequin** — Clothing items automatically appear on a human model or mannequin
4. **Batch processing** — Edit 100+ images at once
5. **Smart shadows** — Realistic drop shadows that match the scene
6. **Image expansion** — Extend image boundaries with AI (outpainting)
7. **Text-to-image backgrounds** — Type "rustic kitchen table" → get that background
8. **Brand kit** — Save colors, logos, fonts for consistent branding
9. **Social media templates** — Pre-sized for Instagram, Facebook, TikTok
10. **Upscaling** — Enhance low-res product photos to 4K
11. **One-click mockups** → t-shirt on hanger, mug on table, poster on wall

---

## What's Broken in Our Current AI Studio

### Bug 1: Can't Delete Images
- `removeImage()` in JS (line 995) only removes from frontend array — never calls server delete endpoint
- `deleteSelectedImages()` (line 1021) deletes ALL non-primary images instead of letting user SELECT which to delete
- No selection UI — there's no way to checkmark images to delete
- The `delete-image/<sku>` endpoint EXISTS (line 713) but is never called from the AI Studio

### Bug 2: Images Showing Sideways
- Likely EXIF orientation not being handled when displaying images
- Need to read EXIF data and apply correct rotation

### Bug 3: Links Don't Work
- Multiple broken links in the AI Studio interface
- Need to audit all `onclick` handlers and `href` attributes

### Bug 4: AI Scene Generation is Fake
- `generate_scene_api()` (ai_studio.py line 342) has a comment: "For now, create a nice template composite locally"
- It just falls back to colored backgrounds — AI was NEVER actually called
- The prompt templates exist in SCENE_TEMPLATES but are never sent to OpenRouter

### Bug 5: Mockups are Geometric Outlines
- `create_mockup()` (ai_studio.py line 463) draws t-shirt outlines with polygon lines
- Mug is just circles and rectangles
- Looks like a child's drawing, not a professional product photo

### Bug 6: No Real AI Integration
- Auto-tag works but results aren't saved anywhere
- All AI features are basically TODO stubs with colored background fallbacks

---

## Rewrite Plan for Echo

### Priority 1: Fix Broken Stuff (Quick Wins)
1. Fix image deletion — add proper selection UI with checkboxes, call `/delete-image/<sku>` endpoint
2. Fix sideways images — handle EXIF orientation
3. Fix broken links audit
4. Wire auto-tag results into product SEO fields

### Priority 2: Real AI Integration
1. Actually call OpenRouter's image generation API for scene generation
2. Professional mockups using AI image generation
3. Real contextual scenes based on product type
4. Social media post generator with proper layouts

### Priority 3: New Features (Matching Competition)
1. Virtual model/mannequin for clothing
2. Batch processing (select multiple products → apply AI to all)
3. Image expansion/outpainting
4. Smart shadow generation
5. Background text-to-image ("describe your ideal background")
6. Brand kit (save store colors, logo, default fonts)
