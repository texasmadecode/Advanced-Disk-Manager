import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
import psutil

def list_unpartitioned_disks():
    """Lists unpartitioned disks."""
    disks = []
    for part in psutil.disk_partitions(all=True):
        if part.fstype == "":
            disks.append(part.device)
    return disks

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
        messagebox.showinfo("Health Check", f"Health check for {disk}:\n\n{result.stdout}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to perform health check on {disk}: {str(e)}")

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
        messagebox.showinfo("Success", f"Disk {disk} has been formatted with {file_system} and label '{label}'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to format disk {disk}: {str(e)}")

def handle_disk_operations():
    """Handles user prompts and disk operations."""
    unpartitioned_disks = list_unpartitioned_disks()
    if not unpartitioned_disks:
        messagebox.showinfo("Info", "No unpartitioned disks found.")
        return

    for disk in unpartitioned_disks:
        # Prompt for health check
        health_check = messagebox.askyesno(
            "Disk Health Check",
            f"Do you want to perform a health check on disk {disk}?"
        )
        if health_check:
            disk_health_check(disk)

        # Ask user if they want to format the disk
        response = messagebox.askyesno(
            "Disk Found",
            f"Unpartitioned disk detected: {disk}. Do you want to partition and format it?"
        )
        if response:
            # Get file system choice
            file_system = simpledialog.askstring(
                "File System", 
                "Enter the file system (NTFS, FAT32, exFAT):", 
                initialvalue="NTFS"
            )
            if file_system is None:
                file_system = "NTFS"

            # Get volume label
            label = simpledialog.askstring(
                "Volume Label",
                "Enter a label for the disk:",
                initialvalue="NewVolume"
            )
            if label is None:
                label = "NewVolume"

            # Format the disk
            format_disk(disk, file_system, label)

# Main UI
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    if messagebox.askyesno("Disk Manager", "Scan for unpartitioned disks?"):
        handle_disk_operations()
    else:
        messagebox.showinfo("Exit", "No action taken.")
