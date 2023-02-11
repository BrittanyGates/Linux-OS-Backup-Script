#!/usr/bin/python3
"""
This script uses the rsync command to back up specific computer files in the "home" folder onto the backup disk.
"""

import os
import datetime

today_date = datetime.date.today()
today_date = str(today_date)


"""
If you don't want to exclude any folders from backup then you can remove the --exclude tag.
However, you probably will keep it as rsync will copy all the hidden files in the "home" folder. Unless you want that to happen.
"""
os.system("rsync -av --exclude={'.*', 'add_additional_folders_here'}"
          " /home/username_goes_here/ /backup_disk_path_goes_here/-" + today_date)
