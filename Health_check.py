import shutil
import psutil


def check_usage_disk(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 25


def check_cpu_usafe():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_usage_disk("/") and check_cpu_usafe():
    print("Error!")
else:
    print("Every thing is okay")
