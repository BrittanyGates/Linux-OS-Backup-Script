# Linux OS Backup Script

![A computer sitting on a desk transfers its files onto a backup disk also sitting on the desk.](linux_os_backup_script_gemini_generated.jpeg)

Back up specific directories in the Home Directory to a local backup device.

## About The Program

The script uses the rsync command to exclude any directories from the backup. By default, the script excludes all
hidden directories, also called dot directories.

The rsync options in the script:

* a = Archive
* v = Verbose

Example of how to configure the script:

* How to exclude multiple directories:

```
os.system("rsync -av --exclude={'.*', 'Downloads', 'Public'}" /home/johndoe/ /mnt/backups/-" + today_date)
```

## Dependencies

The project requires the following programs to execute correctly:

> I recommend installing these in a Python Virtual Environment (virtualenv).
> 
> You can also run my project in a virtualenv.
> 
> Learn more about virtualenvs, including how to create one, from
> the [official Python Documentation](https://docs.python.org/3/library/venv.html).

* Python 3
    * Linux users: Python is already installed.
* rsync
    * Some Linux distributions do not have rsync installed by default.
    * It can be installed via the distribution's
      package manager.

## Download Options

* To run the program you can do either of the following:
    * Clone the repo: https://github.com/BrittanyGates/Linux-OS-Backup-Script.git
    * Download the ZIP file from the
      repo: https://github.com/BrittanyGates/Linux-OS-Backup-Script/archive/refs/heads/master.zip

## Running The Program

1. Open the Terminal.
2. Change directory (`cd`) to the directory of the downloaded program's directory path. If you downloaded the files into
   your `Downloads` directory then you can use this command:
    - `cd /home/$username/Downloads/Linux-OS-Backup-Script-master`
3. Type the following command to run the program: `python main.py` or `python3 main.py`.

## Help

Please file a new issue using the [Issues](https://github.com/BrittanyGates/Linux-OS-Backup-Script/issues) tab on the
repo.

## Creator

Brittany Gates

* [Website](https://brittbot.com)
* [Email](mailto:support@brittbot.com)
* [LinkedIn](https://www.linkedin.com/in/brittanycgates/)
* [Twitter / X](https://x.com/brittany__gates)
* [YouTube](https://www.youtube.com/c/BrittanyGates)

## Version History

* Latest release notes as of February 2025:
  * Updated the README.
* Latest release notes as of late December 2024:
    * Added a README.
    * Updated the content in the docstring and its formatting.
    * Reconfigured the rsync command.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[Dominique Pizzie](https://gist.github.com/DomPizzie) for the simple README template