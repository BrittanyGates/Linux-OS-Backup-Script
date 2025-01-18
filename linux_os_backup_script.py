#!/usr/bin/env python3
"""Linux OS Backup Script
Creator: Brittany Gates (https://github.com/BrittanyGates) | (https://www.linkedin.com/in/brittanycgates) |
(https://brittbot.com/)
About: Back up specific directories in the Home Directory to a local backup device.
"""

import os
import datetime

today_date = datetime.date.today()
today_date = str(today_date)


def main() -> None:
    """Runs the rsync command to back up specific directories onto a backup device.
    :return: None
    """
    os.system(
        "rsync -av --exclude={'.*', 'add_additional_folders_here'} /home/$username/ /mnt/backup_disk_path/-" + today_date)


if __name__ == '__main__':
    main()
