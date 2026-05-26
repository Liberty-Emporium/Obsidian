# AI Store App Redesign Plan
## Liberty Emporium & Thrift — AI-Powered Image Processing Suite

### Current State (`app_with_ai.py` + `image_editor.html`)
- Flask app deployed on Railway, ~40 products in inventory
- Image editor: manual drawing tools (brush, shapes, text, crop, rotate, zoom, layers)
- Existing AI features (partially implemented):
  - `/enhance-image/<sku>` — auto background removal via `rembg` library, composites onto white
  - `/guided-remove-bg/<sku>` — user draws bounding box, `rembg` removes bg with that hint
  - `/enhance-all-images/<sku>` — batch bg removal for all product images
  - AI photo analysis on edit page — Claude analyzes photo → auto-fills title/desc/price
- Frontend: `image_editor.html` has drawing tools but the AI button just calls `enhance-image`
- All AI calls go through OpenRouter (Claude) except bg removal (local `rembg` Python lib)

---

### What We're Building: AI Image Studio

Replace the clunky manual-image-editor workflow with a streamlined AI-powered pipeline.

#### PHASE 1 — AI Background Removal (v2)
**User flow:** Upload photo → AI detects product → removes bg → offers white / transparent / custom color

- [ ] Replace current `rembg`-only with dual approach:
  - **Fast path:** Local `rembg` (u2net model) — works offline, no API cost
  - **Premium path:** OpenRouter vision model (Claude/Gemini) generates precise mask → better edges
- [ ] Add background options: White, Transparent (PNG), Custom color picker, AI-generated backdrop
- [ ] Progress bar + preview before saving
- [ ] One-click "Enhance All" for entire inventory

**API endpoints to add:**
```
POST /api/ai/remove-bg/<sku>
  body: { "mode": "fast"|"premium", "bg": "white"|"transparent"|"custom", "color": "#hex" }
  returns: { "success": true, "url": "...", "before_url": "..." }

POST /api/ai/remove-bg-batch
  body: { "skus": ["SKU1", "SKU2"], "mode": "fast" }
  returns: { "job_id": "..." }  ← async, poll for progress
```

#### PHASE 2 — AI Image Enhancement
**User flow:** Upload photo → AI enhances → side-by-side comparison → save

- [ ] Auto-enhance: fix lighting, color balance, sharpness, noise reduction
- [ ] AI upscale: 2x/4x upscaling for low-res photos using Real-ESRGAN or similar
- [ ] AI watermark removal: detect and remove watermarks/logos from thrift store photos
- [ ] Style transfer: "make it look like a professional product photo"

**API endpoints to add:**
```
POST /api/ai/enhance/<sku>
  body: { "type": "auto"|"upscale"|"denoise"|"watermark-removal", "strength": 0-100 }
  returns: { "before_url": "...", "after_url": "...", "enhancements_applied": [...] }
```

#### PHASE 3 — AI Scene Generation
**User flow:** Select product with transparent bg → choose scene template → AI composites product into scene

- [ ] Pre-built scene templates:
  - "On a shelf" — e-commerce style
  - "Lifestyle" — room context (living room, kitchen, bedroom)
  - "Flat lay" — arranged on surface with props
  - "Social media" — Instagram/TikTok ready with text overlay area
- [ ] AI generates contextual background based on product category
- [ ] User can type a prompt: "vintage lamp on a wooden nightstand beside a bed"
- [ ] Batch: apply same scene to multiple products

**Implementation:** Use OpenRouter image generation models (Stable Diffusion XL, Flux) or Replicate API for inpainting/compositing

**API endpoints to add:**
```
POST /api/ai/generate-scene/<sku>
  body: { "template": "shelf"|"lifestyle"|"flatlay"|"social"|"custom", "prompt": "...", "count": 3 }
  returns: { "urls": ["...", "...", "..."] }
```

#### PHASE 4 — AI Mockups
**User flow:** Select product → choose mockup template → AI places product → export

- [ ] Mockup templates library:
  - T-shirt / hoodie (for clothing items)
  - Mug / tumbler
  - Tote bag
  - Poster / framed print
  - Phone case
  - Greeting card
- [ ] AI intelligently warps/fits product into mockup perspective
- [ ] One-click export to all social sizes

**API endpoints to add:**
```
POST /api/ai/mockup/<sku>
  body: { "template": "tshirt"|"mug"|"poster"|"phone-case", "variant": "front"|"back" }
  returns: { "url": "...", "download_url": "..." }
```

#### PHASE 5 — One-Click Social Media Images
**User flow:** Select product → pick platform → AI generates ready-to-post image with text/crop

- [ ] Platform presets with exact dimensions:
  - Instagram post (1080×1080)
  - Instagram story (1080×1920)
  - Facebook post (1200×630)
  - Facebook Marketplace (varies)
  - TikTok (1080×1920)
  - Pinterest (1000×1500)
  - X/Twitter (1600×900)
  - Etsy listing (2700×2025)
- [ ] AI auto-generates catchy caption + hashtags
- [ ] Brand overlay: store logo watermark option
- [ ] Batch: generate all sizes for multiple products at once

**API endpoints to add:**
```
POST /api/ai/social/<sku>
  body: { "platforms": ["instagram-post", "facebook", "etsy"], "include_caption": true, "style": "minimal"|"bold"|"elegant" }
  returns: { "images": [{ "platform": "...", "url": "...", "caption": "...", "hashtags": [...] }] }
```

#### PHASE 6 — Batch Processing Dashboard
**User flow:** Select multiple products → choose AI action → watch progress → download all

- [ ] Grid view of all products with checkboxes
- [ ] Bulk actions: Remove bg, Enhance, Generate scenes, Create social images
- [ ] Progress dashboard with real-time status per product
- [ ] Download all results as ZIP
- [ ] Schedule: "process all new uploads overnight"

**API endpoints to add:**
```
POST /api/ai/batch
  body: { "skus": [...], "actions": ["remove-bg", "enhance", "social-all"], "notify_email": "..." }
  returns: { "job_id": "...", "total": 40, "estimated_minutes": 15 }

GET /api/ai/batch/<job_id>
  returns: { "status": "running"|"done"|"error", "progress": 65, "results": [...], "errors": [...] }

GET /api/ai/batch/<job_id>/download
  returns: ZIP file download
```

#### PHASE 6 — AI Virtual Try-On
**User flow:** Upload photo of clothing item (on floor/hanging) → select model photo → AI puts clothing on person → export

- [ ] **Garment segmentation** — AI detects and extracts the clothing item from the uploaded photo (built on Phase 1 bg removal + specialized segmentation)
- [ ] **Pose detection** — AI identifies body landmarks on the model photo
- [ ] **Garment warping** — AI stretches/fits the clothing to match the body pose, shape, and proportions
- [ ] **Realistic rendering** — Shadows, fabric folds, natural blending
- [ ] **Model selection** — Choose from pre-loaded diverse model photos OR upload a custom model photo
- [ ] **Multi-gender / multi-size** — Try same dress on different body types
- [ ] **Batch try-on** — Upload one garment, try on 5+ models at once

**How it works (technical):**
```
1. User uploads dress photo (flat on floor)
    ↓
2. AI segments the dress (rembg + cloth-specific model)
    ↓
3. User selects a model photo (pre-loaded or uploads their own)
    ↓
4. AI detects pose + body shape on model
    ↓
5. Virtual try-on model warps dress onto body
    ↓
6. Post-processing: shadow matching, color correction, edge blending
    ↓
7. Output: photorealistic image of model wearing the dress
```

**Recommended AI models for try-on:**
| Model | Provider | Cost | Quality |
|-------|----------|------|---------|
| IDM-VTON | Replicate | ~$0.03/img | ⭐⭐⭐⭐⭐ |
| HR-VITON | Replicate | ~$0.02/img | ⭐⭐⭐⭐ |
| ShoeTryOn | Replicate | ~$0.02/img | ⭐⭐⭐ (shoes only) |
| Custom Flux inpainting | OpenRouter | ~$0.01/img | ⭐⭐⭐ |

**API endpoints to add:**
```
POST /api/ai/tryon/<sku>
  body: { "model_photo": "model_01.jpg" | upload, "garment_image": "..." | null }
  returns: { "success": true, "url": "...", "before_url": "...", "after_url": "..." }

GET /api/ai/tryon-models
  returns: { "models": [{ "id": "model_01", "name": "Woman S", "url": "..." }, ...] }

POST /api/ai/tryon-batch/<sku>
  body: { "model_ids": ["model_01", "model_02", "model_03"] }
  returns: { "results": [{ "model": "model_01", "url": "..." }, ...] }
```

#### PHASE 7 — Batch Processing Dashboard

Replace the current image editor's complex tool panels with a clean AI workflow:

```
┌─────────────────────────────────────────────────┐
│  🖼️ AI Image Studio                    ⚙️  👤  │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌───────┐ │
│  │ 1.Upload │→│ 2.Remove │→│ 3.Scene │→│4.Export│ │
│  │   📷    │ │   🪄    │ │   🎨    │ │  📤   │ │
│  │  done   │ │  active │ │ pending │ │pending │ │
│  └─────────┘ └─────────┘ └─────────┘ └───────┘ │
│                                                  │
│  ┌──────────────────┐  ┌──────────────────────┐ │
│  │                  │  │ ✨ AI Actions         │ │
│  │   Image Preview  │  │                       │ │
│  │                  │  │ [🪄 Remove Background]│ │
│  │   (drag & drop)  │  │ [✨ Auto Enhance]     │ │
│  │                  │  │ [🎨 Generate Scene]   │ │
│  │                  │  │ [👕 Create Mockup]    │ │
│  │                  │  │ [👗 Virtual Try-On]   │ │
│  │                  │  │ [📱 Social Images]    │ │
│  │                  │  │ ─────────────────     │ │
│  │                  │  │ [📦 Batch Process All]│ │
│  └──────────────────┘  └──────────────────────┘ │
│                                                  │
│  ┌──────────────────────────────────────────────┐│
│  │ 📋 Processing Queue                           ││
│  │ ✅ Chair_001.jpg — bg removed                 ││
│  │ 🔄 Lamp_002.jpg — generating scene... 65%    ││
│  │ ⏳ Vase_003.jpg — waiting                     ││
│  └──────────────────────────────────────────────┘│
└─────────────────────────────────────────────────┘
```

---

### Technical Architecture

#### AI Backend Options

| Feature | Local (Free) | OpenRouter | Replicate | Cleanup.pics API |
|---------|-------------|------------|-----------|------------------|
| BG Removal | rembg (u2net) | Claude vision mask | BRIA-REMOVAL | ✅ best quality |
| Enhancement | PIL basics | GPT-4V guidance | Real-ESRGAN | — |
| Scene Gen | — | Flux/SD XL | Flux inpainting | — |
| Mockups | PIL compositing | GPT-4V layout | FLUX depth | — |
| Social Images | PIL text overlay | Claude copy + FLUX | — | — |

**Recommended stack (cost-conscious):**
1. BG removal → `rembg` local (free, fast, "good enough" for most items)
2. Scene gen → OpenRouter `flux-1.1-pro` or `stable-diffusion-3.5` ($0.001-0.003 per image)
3. Social images → Claude generates caption, PIL composites image with text (free)
4. Mockups → PIL-based template compositing with perspective transform (free)
5. Enhancement → PIL + OpenCV auto-adjustments (free) + optional AI upscale via Replicate

#### New Files to Create
```
Emporium-and-Thrift-App/
├── ai_studio.py          ← New: all AI image processing functions
├── ai_batch.py           ← New: batch job queue + worker
├── templates/
│   ├── ai_studio.html    ← New: replaces image_editor.html for AI workflow
│   └── ai_batch.html     ← New: batch processing dashboard
├── static/
│   ├── ai_studio.css     ← New: modern mobile-friendly styles
│   └── ai_studio.js      ← New: step-by-step workflow JS
└── mockups/              ← New: mockup template images
    ├── tshirt-front.png
    ├── tshirt-back.png
    ├── mug.png
    ├── poster.png
    └── phone-case.png
```

#### Route Additions to `app_with_ai.py`
```python
# AI Studio
@app.route('/ai-studio/<sku>')
@app.route('/ai-studio')  # new product flow
def ai_studio(sku=None):

# API endpoints (all POST, JSON in/out)
@app.route('/api/ai/remove-bg/<sku>', methods=['POST'])
@app.route('/api/ai/enhance/<sku>', methods=['POST'])
@app.route('/api/ai/generate-scene/<sku>', methods=['POST'])
@app.route('/api/ai/mockup/<sku>', methods=['POST'])
@app.route('/api/ai/social/<sku>', methods=['POST'])
@app.route('/api/ai/batch', methods=['POST'])
@app.route('/api/ai/batch/<job_id>', methods=['GET'])
@app.route('/api/ai/batch/<job_id>/download', methods=['GET'])
```

---

### Implementation Order

**Week 1 — Foundation**
1. Create `ai_studio.py` with all AI functions
2. Build new `ai_studio.html` template (mobile-first)
3. Implement Phase 1: AI Background Removal v2 (fast + premium modes)
4. Implement Phase 2: AI Image Enhancement
5. Test locally, push to Railway

**Week 2 — Creative Features**
6. Implement Phase 3: AI Scene Generation
7. Implement Phase 4: AI Mockups + Virtual Try-On (Phase 6)
8. Implement Phase 5: One-Click Social Media Images
9. Add progress tracking + preview system

**Week 3 — Batch + Polish**
10. Implement Phase 7: Batch Processing Dashboard
11. Add ZIP download for batch results
12. Mobile optimization pass
13. End-to-end testing with real products
14. Deploy to production

---

### Cost Estimate (per 100 images processed)

| Operation | Local Cost | API Cost |
|-----------|-----------|----------|
| BG Removal (rembg) | $0 | — |
| BG Removal (premium) | — | ~$0.50 |
| Enhancement | $0 | — |
| Scene Generation | — | ~$0.30 |
| Mockups | $0 | — |
| Social Images | $0 | ~$0.10 (caption only) |
| **Total (all local)** | **$0** | **$0** |
| **Total (all premium)** | — | **~$0.90** |

**Recommendation:** Default to local/free, offer premium as upgrade. Jay stays broke-friendly. 💪

---

### What Happens to the Old Image Editor?

Keep `image_editor.html` accessible at `/editor/<sku>` for power users who want manual drawing tools. But the **default** image editing flow becomes the new AI Studio. Add a banner on the old editor: "🚀 Try the new AI Image Studio →"

---

*Plan created by OWL for Jay Alexander — Liberty Emporium & Thrift*
*Date: May 26, 2026*
