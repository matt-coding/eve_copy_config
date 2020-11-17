Eve Online Copy Configuration
=============

This python script is used to copy configuration (from your cache/settings folder) from one account/character to another. It is written based on the steps [here](https://forums.eveonline.com/t/manually-copy-settings-between-characters-and-accounts/32704). 

Important Notes
------------
* Only Windows is supported.
* This script will copy one character's configuration to overwrite **ALL** other character's configuration.
* This script currently only supports the Default (settings_Default) profile. If you have changed the profile using the [Profile Management Tool](https://support.eveonline.com/hc/en-us/articles/212689029-Profile-Management-Tool) this script won't currently work correctly.
* Backing up your profiles may take a while to complete.
* This script works correctly for me but there is always a chance something could go wrong and break [things](https://www.eveonline.com/article/about-the-boot.ini-issue).
* If you find an issue please let me know either via github or via email at matt-coding_github at protonmail dot com

Usage
------------

1. Backup your "e_eve_sharedcache_tq_tranquility" folder, usually located: C:\Users\Alice\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility where Alice is your username. This script will also create a backup but just in case it's worth backing up manually.
1. Install Python. See [here](https://www.python.org/downloads/) for further information.
1. Download the python script called eve_copy_config.py from this page.
1. Run ```python .\eve_copy_config.py --help``` in Windows Powershell and read the information provided.
1. Run again with correct arguments.

Examples
------------

* Where your settings folder is "C:\Users\Alice\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility". Create backup of your profiles in "C:\Users\Alice\Documents\Gaming". Overwrite all other characters data with data of character "core_char_169813716.dat". Overwrite all other accounts (user) data with of account (user) "core_user_9428114.dat". Create backup of your profiles in C:\Users\Alice\Documents\Gaming:
python .\eve_copy_config.py "C:\Users\Alice\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility" -b C:\Users\Alice\Documents\Gaming -c core_char_169813716.dat -u core_user_9428114.dat

* Create backup of your profiles in E:\Downloads where your settings folder is "C:\Users\Bob\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility":
python .\eve_copy_config.py "C:\Users\Bob\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility" -b E:\Downloads

* Restore your profiles from a backup where your settings folder is "C:\Users\Bob\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility" and your backup file to restore is "E:\Downloads\eve_copy_config_backup20201120T132937.zip".
python .\eve_copy_config.py "C:\Users\Bob\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility" -r "E:\Downloads\eve_copy_config_backup20201120T132937.zip"
