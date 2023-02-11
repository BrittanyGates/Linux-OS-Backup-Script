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
You can add a folder name to the path of the backup disk. The folder doesn't have to be created beforehand as the script will create it if isn't.

Finally, be careful not to remove spaces between the exclude and the "home" path, as rsync needs a space to separate the options in the command.

Example of how to configure the script for your use:

os.system("rsync -av --exclude={'.*', 'Downloads', 'Public'}"
          " /home/johndoe/ /mnt/backup_disk/backup-" + today_date)
"""

os.system("rsync -av --exclude={'.*', 'add_additional_folders_here'}"
          " /home/username_goes_here/ /backup_disk_path_goes_here/-" + today_date)
