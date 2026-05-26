#!/usr/bin/env python3
"""
ecdash_to_obsidian.py — Pull data from Echo/Hermes/EcDash into Obsidian vault

Connects to:
  - Echo (KiloClaw) via Agent Zero API — client list, status
  - Hermes (this machine) via local API — client machines
  - Railway — app health checks

Writes to:
  - Obsidian vault at ~/Desktop/openclaw/obsidian-vault/

Run: python3 ecdash_to_obsidian.py [--all] [--clients] [--status] [--notes]
Cron: 0 */4 * * *  (every 4 hours)
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

VAULT_PATH = os.environ.get("OBSIDIAN_VAULT_PATH", "/home/lol/Desktop/openclaw/obsidian-vault")

# Echo / Agent Zero
ECHO_AZ_BASE = "https://agent-zero-install-production.up.railway.app"
ECHO_KEY = os.environ.get("ECHO_API_KEY", "98e879f12c4ada6ed7fa2337cf270793638c1cb9b4b61424e007119bd78b8276")

# Hermes (this machine's Hermes Agent if running an API, otherwise skip)
HERMES_BASE = "http://localhost:18789"  # Hermes gateway port

# Railway apps to health-check
RAILWAY_APPS = [
    ("Liberty Inventory",    "liberty-emporium-and-thrift-inventory-app-production.up.railway.app"),
    ("Sweet Spot Cakes",     "sweet-spot-cakes.up.railway.app"),
    ("KYS",                  "ai-api-tracker-production.up.railway.app"),
    ("Pet Vet AI",           "pet-vet-ai-production.up.railway.app"),
    ("GymForge",             "web-production-1c23.up.railway.app"),
    ("Contractor Pro AI",    "contractor-pro-ai-production.up.railway.app"),
    ("Dropship Shipping",    "dropship-shipping-production.up.railway.app"),
    ("Consignment Solutions","web-production-43ce4.up.railway.app"),
    ("EcDash / Portfolio",   "jay-portfolio-production.up.railway.app"),
    ("Support Dashboard",    "agents.alexanderai.site"),
]

TIMEOUT = 8

# ── Helpers ───────────────────────────────────────────────────────────────────

def api_get(url, headers=None, timeout=TIMEOUT):
    """GET request, returns JSON or None."""
    try:
        hdrs = {"Content-Type": "application/json", **(headers or {})}
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return None

def echo_headers():
    return {"X-Echo-Key": ECHO_KEY, "Content-Type": "application/json"}

def echo_get(path):
    return api_get(f"{ECHO_AZ_BASE}{path}", headers=echo_headers())

def check_health(url):
    """Check if a Railway app is up. Returns status emoji."""
    try:
        req = urllib.request.Request(f"https://{url}/", method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return "🟢" if resp.status < 400 else "🟡"
    except urllib.error.HTTPError as e:
        return "🟢" if e.code < 500 else "🟡"
    except:
        return "🔴"

def today():
    return datetime.now().strftime("%Y-%m-%d")

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def write_note(folder, filename, content):
    """Write a note to the vault."""
    dirpath = Path(VAULT_PATH) / folder
    dirpath.mkdir(parents=True, exist_ok=True)
    filepath = dirpath / f"{filename}.md"
    filepath.write_text(content)
    rel = f"{folder}/{filename}.md"
    print(f"  ✅ {rel}")
    return rel

# ── Pull: Echo Clients ──────────────────────────────────────────────────────

def pull_clients():
    """Pull client list from Echo via Agent Zero."""
    print("\n📋 Pulling clients from Echo...")
    
    data = echo_get("/api/echo/clients")
    
    if not data:
        print("  ⚠ Echo unreachable, using local client list")
        write_fallback_clients()
        return
    
    clients = data.get("clients", data) if isinstance(data, dict) else data
    
    lines = [
        "# 📋 Client Dashboard",
        "",
        f"> Synced from Echo at {now()}",
        "",
        "| # | Client | Plan | Status | Since |",
        "|---|--------|------|--------|-------|",
    ]
    
    if isinstance(clients, list):
        for i, c in enumerate(clients, 1):
            name = c.get("name", c.get("client_name", "Unknown"))
            plan = c.get("plan", c.get("subscription", "-"))
            status = c.get("status", "active")
            since = c.get("created", c.get("since", "-"))
            lines.append(f"| {i} | [[{name}]] | {plan} | {status} | {since} |")
    
    lines.extend(["", f"_Last synced: {now()}_"])
    
    write_note("20-Clients", "Client Dashboard", "\n".join(lines))
    
    # Also update individual client notes
    if isinstance(clients, list):
        for c in clients:
            name = c.get("name", c.get("client_name", "Unknown"))
            lines = [
                f"# 👤 {name}",
                "",
                f"> Synced from Echo at {now()}",
                "",
                f"- **Status:** {c.get('status', 'active')}",
                f"- **Plan:** {c.get('plan', '-')}",
                f"- **Email:** {c.get('email', '-')}",
                f"- **Machines:** {c.get('machine_count', c.get('machines', 0))}",
                "",
                "## Notes",
                "",
                c.get("notes", "_No notes yet_"),
                "",
                "---",
                f"_Last synced: {now()}_",
            ]
            write_note("20-Clients", f"Client — {name}", "\n".join(lines))
    
    print(f"  📝 Synced {len(clients) if isinstance(clients, list) else '?'} clients")

def write_fallback_clients():
    """Write client list from local knowledge when Echo is unreachable."""
    lines = [
        "# 📋 Client Dashboard",
        "",
        f"> Last updated {now()} (offline — from local memory)",
        "",
        "| # | Client | Status | Notes |",
        "|---|--------|--------|-------|",
        "| 1 | Sweet Spot Custom Cakes | 🟢 Active | Bakery app, live. Next: CRM features before May 30 |",
        "| 2 | Billy Flood App | 🟡 Waiting | Hasn't paid yet. Needs repo when paid |",
        "| 3 | Liberty Oil & Propane | 🔴 Back burner | 1 HTML page, low priority |",
        "",
        "---",
        f"_Last synced: {now()}_",
    ]
    write_note("20-Clients", "Client Dashboard", "\n".join(lines))
    print("  📝 Wrote fallback client list")

# ── Pull: App Health / Status ──────────────────────────────────────────────

def pull_status():
    """Health-check all Railway apps and write status."""
    print("\n📊 Checking app health...")
    
    lines = [
        f"# 📊 System Status — {today()}",
        "",
        f"> Auto-generated at {now()}",
        "",
        "## Railway Apps",
        "",
        "| App | URL | Status |",
        "|-----|-----|--------|",
    ]
    
    for name, url in RAILWAY_APPS:
        status = check_health(url)
        lines.append(f"| **{name}** | `{url}` | {status} |")
    
    lines.extend([
        "",
        "## Legend",
        "- 🟢 Up and responding",
        "- 🟡 Degraded (slow or partial)",
        "- 🔴 Down or unreachable",
        "",
        "---",
        f"_Next check: run again or wait for cron_",
    ])
    
    write_note("30-Projects", f"System Status — {today()}", "\n".join(lines))
    print(f"  📝 Checked {len(RAILWAY_APPS)} apps")

# ── Pull: Hermes Message (send to Echo) ────────────────────────────────────

def hermes_to_echo(message):
    """Send a message to Echo via Hermes proxy."""
    data = echo_get("/api/echo/clients")  # test connection first
    if not data:
        print("  ⚠ Echo unreachable")
        return None
    
    # Use the echo-proxy run endpoint
    result = api_get(
        f"{ECHO_AZ_BASE}/api/echo/run",
        headers=echo_headers(),
    )
    return result

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    run_all = "--all" in args or not args
    
    print(f"🔄 EcDash → Obsidian Sync")
    print(f"   Vault: {VAULT_PATH}")
    print(f"   Time:  {now()}")
    
    if run_all or "--clients" in args:
        pull_clients()
    
    if run_all or "--status" in args:
        pull_status()
    
    print(f"\n✅ Sync complete at {now()}")

if __name__ == "__main__":
    main()
