# Advanced Disk Manager

A powerful command-line tool for managing disk operations, including partitioning, formatting, and disk health checks.

## Features
- Detects unpartitioned disks and allows partitioning and formatting.
- Supports multiple file systems: NTFS, FAT32, exFAT.
- Allows users to assign custom labels to formatted disks.
- Performs disk health checks to detect and report bad sectors.
- Fully supports command-line operation, making it ideal for remote management and automation.

## How It Works
- The script uses `wmic` commands to list unpartitioned disks on Windows.
- `diskpart` is used for disk partitioning and formatting operations.
- Command-line arguments are used to specify actions like formatting or health checks, replacing the need for a graphical user interface (GUI).

### Example Commands:
To format a disk:
```bash
python advanced_disk_manager.py --action format --disk D: --fs NTFS --label NewVolume
