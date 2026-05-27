# Liberty Agent USB — Phase 1 Build Plan

## Goal
A USB 3.0 drive that boots a portable Linux OS with Hermes pre-installed.
Plug into any Windows PC → boot from USB → Hermes auto-connects to Telegram.
Jay controls Hermes remotely from his phone. Customer's machine is untouched.

## What We Need

### Hardware
- USB 3.0+ flash drive, 128GB recommended
  - Recommended: SanDisk Extreme Pro 128GB or Samsung FIT Plus 128GB
  - USB 3.0 minimum — USB 2.0 will be painfully slow
  - Jay to purchase — about $15-25

### Software Stack
- **Puppy Linux** (FossaPup64 or BionicPup64) — ~300MB, runs in RAM, boots in 1-2 min
  - Download from puppylinux.com
  - Why Puppy: tiny, fast, designed for USB persistence, runs entirely in RAM
- **Python 3.10+** — Puppy ships with it or install via package manager
- **Node.js 18+** — needed for Hermes runtime
- **Hermes Agent** — full installation on the persistent partition
- **LUKS encryption** — encrypts the persistence partition so if USB is lost, keys are safe

## Build Steps

### Step 1: Flash Puppy Linux to USB
1. Download FossaPup64 ISO
2. Use Rufus (Windows) or Etcher (Mac/Linux) to flash ISO to USB
3. Boot from USB on Jay's machine to verify it works
4. Run the Puppy Installer → install to USB with persistence partition
5. Allocate at least 80GB for the persistence partition (Hermes + deps + files)

### Step 2: Set Up Puppy Linux Environment
1. Boot into Puppy from USB
2. Connect to WiFi
3. Open Puppy Package Manager
4. Install: Python 3.10+, pip, git, Node.js 18+, npm, vim/nano
5. Update all packages

### Step 3: Install Hermes Agent
1. Clone Hermes repo to the persistent partition
   ```
   cd /mnt/sda1/hermes (or wherever persistence mounts)
   git clone https://github.com/nousresearch/hermes-agent.git
   cd hermes-agent
   pip install -r requirements.txt
   ```
2. Run initial setup:
   ```
   ./hermes setup
   ```
3. Configure model providers (OpenRouter)
4. Set gateway token
5. Verify Hermes connects to Telegram

### Step 4: Pre-Load Jay's Credentials
Create config files on the USB:
- Telegram bot token
- OpenRouter API key
- GitHub PAT (test phase)
- Railway token
- Tailscale key
- Cal.com key
- Dashboard MASTER_API_KEY

**SECURITY NOTE:** All credentials stored on the USB. If USB is lost, these are exposed.
→ Solution: LUKS encrypt the persistence partition. Hermes prompts for passphrase on boot.
→ OR: store keys in a separate encrypted file that Jay downloads after booting.

### Step 5: Auto-Connect on Boot
Create a startup script:
```
#!/bin/bash
# /mnt/sda1/startup.sh
cd /mnt/sda1/hermes-agent
./hermes gateway start &
```

Add to Puppy's startup:
- Go to Puppy's boot manager or rc.local
- Add: `/mnt/sda1/startup.sh`
- Now Hermes starts automatically on every boot

### Step 6: Test on a Separate PC
1. Take USB to a different Windows PC
2. Restart → hit F12 (or Esc/F2) for boot menu
3. Select USB drive
4. Puppy boots → Hermes starts → Telegram connects
5. Jay messages Hermes from phone → Hermes responds on the remote machine
6. Jay runs commands on the remote machine through Hermes

## Step 7: Mac Compatibility (Phase 2 — Future)
Modern Macs require:
- Intel Mac: Hold Option at boot → select EFI Boot → works
- T2 Chip Mac: Recovery Mode → Security Utility → "Allow booting from external media" → restart → Option key
- Apple Silicon (M1/M2): Recovery Mode → Security Utility → "Reduce Security" → allow external boot → restart → hold power button → select USB

The Mac Jay mentioned may need Apple Store visit if:
- No admin password to change security settings
- T2/M1 chip with restrictive firmware
- We don't know the recovery password

## Step 8: Package as Product (Future)
For selling to customers as "Liberty Agent":
1. Pre-built USB with Hermes + auto-connect
2. Customer instruction card: "Plug in, restart, press F12, select USB"
3. Jay gets alerted when customer boots the USB
4. Jay provides remote support through Hermes
5. USB is customer's to keep — one-time purchase or included with service

## Phase 1 Checklist
- [ ] Jay purchases USB drive
- [ ] Flash Puppy Linux to USB
- [ ] Set up persistence partition (80GB+)
- [ ] Install Python, Node, git, dependencies
- [ ] Clone + install Hermes Agent
- [ ] Load Jay's credentials
- [ ] Configure auto-startup on boot
- [ ] Test boot on Jay's machine
- [ ] Test boot on a second PC (if available)
- [ ] Document the boot process for Jay

## Time Estimate
- Jay buys USB: 1 day shipping (Amazon) or local store
- Flashing + setup: 2-3 hours
- Hermes install + config: 1-2 hours
- Testing: 1 hour
- Total: ~1 weekend afternoon

## Risks
- Puppy Linux may have WiFi driver issues on some machines (keep a USB Ethernet adapter as fallback)
- Some corporate PCs have boot order locked in BIOS (need admin password to change)
- USB boot speed depends on USB quality — cheap drives will be slow
- Mac compatibility is messy (Phase 2 problem)
