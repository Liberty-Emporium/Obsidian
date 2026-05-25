# Agent Operating System

> Design for Jay's unified AI agent workspace — all agents, one brain.

## 7 Layers (from Julian P.)

1. **Hardware** — Jay's Kali machine + customer machines
2. **Memory** ← THIS VAULT. Obsidian = shared brain for all agents
3. **Brain** — Claude Sonnet, DeepSeek, etc. via OpenRouter
4. **Agents** — Hermes (local), KiloClaw (orchestrator), Claude Code, delegated subagents
5. **Command Center** — EcDash at alexanderai.site
6. **Production** — SEO, content, studio (images/video), social media
7. **Loop** — Auto-save outputs back into this vault

## The Feedback Loop (Layer 7)

Every time an agent produces something:
1. Output gets saved to the correct vault folder
2. INDEX.md gets updated with links
3. Next agent session reads the vault → starts smarter

### Auto-Save Rules
| Output Type | Vault Folder | Example |
|-------------|-------------|---------|
| Session summary | `80-Daily/` | `2026-05-25.md` |
| Client notes | `20-Clients/` | `Sweet Spot — May Update.md` |
| Project updates | `30-Projects/` | `Emporium-and-Thrift-App.md` |
| Content created | `40-Content-Ideas/` | `Blog — What is an AI agent.md` |
| Meeting notes | `50-Meetings-Notes/` | `2026-05-25 — Strategy Call.md` |
| Resources | `60-Resources/` | `SEO Tools.md` |

## Vault Sync
- Git-backed: `Liberty-Emporium/Obsidian` (private repo)
- Hermes writes here after every significant task
- KiloClaw reads/writes here too
- Jay edits on phone via Obsidian Mobile + GitHub sync
