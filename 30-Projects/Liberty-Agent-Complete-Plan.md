# Liberty Agent USB — Complete Build Plan

## Two Products in One

### Product 1: Portable Hermes Runtime (Folder/USB)
- A folder (or USB drive) with Hermes + startup scripts
- Runs INSIDE the customer's existing OS (Windows or Mac)
- No reboot needed — just run the script
- Jay controls Hermes remotely via Telegram
- Can interact with customer's files, browser, programs
- LIMITATION: Can't fix OS-level problems (runs inside the OS)

### Product 2: Puppy Linux Bootable USB (Full OS)
- USB that boots into its own Linux OS
- Completely replaces the customer's OS temporarily
- Can fix ANYTHING — OS problems, malware, passwords, recovery
- No access to customer's files/programs (different OS)
- REQUIRES: Reboot + BIOS boot menu access
- LIMITATION: Some PCs/Macs lock the boot order

## What to Sell Customers

**"Liberty Agent — Remote AI Support"**
- Standard ($49): Portable Hermes runtime — plug in, run script, I fix your stuff while you watch
- Premium ($99): Includes bootable recovery USB — for when your computer won't even start

## Phase 1 Status (May 27 2026)
- [x] Portable runtime folder structure created
- [x] start.sh (Linux/Mac) written
- [x] start.bat (Windows) written
- [x] Config templates created (.env, config.yaml)
- [x] README written
- [ ] Test on a second PC
- [ ] Add LUKS encryption for security
- [ ] Purchase USB drive (128GB USB 3.0)
- [ ] Flash Puppy Linux for Product 2

## Folder Location
`/home/lol/Desktop/openclaw/liberty-agent-portable/`

## Next Steps
1. Jay gets USB drive
2. Copy liberty-agent-portable folder to USB
3. Add real API keys to .env
4. Test on a different PC
5. Build Puppy Linux bootable USB for Product 2
6. Package and sell!
