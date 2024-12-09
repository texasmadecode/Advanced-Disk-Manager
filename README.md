# Advanced Disk Manager

A standalone tool for managing disk operations, including partitioning, formatting, and disk health checks.

## Features
- Detects unpartitioned disks and formats them.
- Allows users to choose file systems (NTFS, FAT32, exFAT).
- Assign custom labels to disks.
- Performs disk health checks to detect bad sectors.

## Download
[![Download EXE](https://img.shields.io/badge/Download-EXE-blue?style=for-the-badge)](https://github.com/username/Advanced-Disk-Manager/raw/main/advanced_disk_manager.exe)

## How to Use
1. **Download the EXE**:
   - Click the "Download EXE" button above.
2. **Copy to USB**:
   - Save the downloaded file to your USB drive.
3. **Run on Target System**:
   - Insert the USB drive into the target computer.
   - Right-click on `advanced_disk_manager.exe` and select **Run as Administrator**.
4. **Follow Prompts**:
   - The tool will guide you through managing your disks.

## How It Works
- The script uses `psutil` to detect unpartitioned disks.
- `diskpart` commands are issued for disk operations.
- A Tkinter-based UI handles user prompts and input.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License.
