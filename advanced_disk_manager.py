import subprocess
import argparse

def list_disks():
    """Lists all disks (both partitioned and unpartitioned)."""
    disks = []
    # Check for physical disks (disk drives) using WMIC
    result = subprocess.check_output("wmic diskdrive get caption", shell=True).decode()
    # Extract disk names from the output
    for line in result.splitlines():
        if line.strip() and line.strip().lower() != "caption":
            disks.append(line.strip())
    return disks

def list_partitions(disk):
    """Lists partitions for a given disk."""
    partitions = []
    try:
        result = subprocess.check_output(f"wmic logicaldisk where \"DeviceID='{disk}'\" get caption", shell=True).decode()
        for line in result.splitlines():
            if line.strip() and line.strip().lower() != "caption":
                partitions.append(line.strip())
    except subprocess.CalledProcessError:
        pass
    return partitions

def disk_health_check(disk):
    """Checks the disk for bad sectors."""
    try:
        result = subprocess.run(
            ["chkdsk", disk],
            text=True,
            capture_output=True,
            check=True,
            shell=True
        )
        print(f"Health check for {disk}:\n\n{result.stdout}")
    except Exception as e:
        print(f"Failed to perform health check on {disk}: {str(e)}")

def format_disk(disk, file_system="NTFS", label="NewVolume"):
    """Formats the specified disk with user-selected options."""
    try:
        disk_commands = f"""
        select disk {disk}
        clean
        create partition primary
        format fs={file_system.lower()} label={label} quick
        assign
        """
        subprocess.run(["diskpart"], input=disk_commands, text=True, check=True, shell=True)
        print(f"Disk {disk} has been formatted with {file_system} and label '{label}'.")
    except Exception as e:
        print(f"Failed to format disk {disk}: {str(e)}")

def handle_disk_operations(action, disk, file_system="NTFS", label="NewVolume"):
    """Handles disk operations based on user action."""
    disks = list_disks()
    if disk not in disks:
        print(f"Disk {disk} is not available.")
        return

    partitions = list_partitions(disk)
    if partitions:
        print(f"Disk {disk} already has partitions: {', '.join(partitions)}")
        return

    if action == "healthcheck":
        disk_health_check(disk)

    elif action == "format":
        format_disk(disk, file_system, label)
    else:
        print("Invalid action specified.")

# Main CLI logic
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Disk Management Tool")
    parser.add_argument("--action", choices=["format", "healthcheck"], required=True, help="Action to perform on the disk")
    parser.add_argument("--disk", required=True, help="Disk to operate on (e.g., 'C:', 'D:')")
    parser.add_argument("--fs", default="NTFS", help="File system to format with (e.g., 'NTFS', 'FAT32')")
    parser.add_argument("--label", default="NewVolume", help="Volume label for the formatted disk")

    args = parser.parse_args()

    handle_disk_operations(args.action, args.disk, args.fs, args.label)

#i was here hehe
