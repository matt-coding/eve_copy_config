import shutil
from datetime import datetime
import os
import re
import argparse

def backup_settings(backup_path, eve_settings_folder):
    now = datetime.now()
    backup_name = backup_path + 'eve_copy_config_backup' +  now.strftime('%Y%m%dT%H%M%S')
    try:
        shutil.make_archive(backup_name, 'zip', eve_settings_folder)
    except:
        print('Failed to create backup, exiting.')
        return False
    else:
        print('Backup complete: ' + backup_name + '.zip')
        return True

def restore_settings(backup_name, eve_settings_folder):
    try:
        shutil.rmtree(eve_settings_folder)
    except:
        print('Failed to delete settings folder before restore. Please try re-running the program.')
        return
    try:
        shutil.unpack_archive(backup_name, eve_settings_folder)
    except:
        print('Failed to restore backup.')
    else:
        print('Restore complete from ' + backup_name + ' to ' + eve_settings_folder)

def overwrite_core_files(path, master_file, regex):
    settings_default_folder = path + 'settings_Default\\'
    if not os.path.isdir(settings_default_folder):
        print('Could not find settings_Default folder within ' + path)
        return False

    core_files = get_files(settings_default_folder, regex)
    if master_file in core_files:
        core_files.remove(master_file)
        for core_file in core_files:
            shutil.copy2(settings_default_folder + master_file, settings_default_folder + core_file)
            print('Overwritten ' + settings_default_folder + core_file + ' with ' + settings_default_folder + master_file)
        return True
    else:
        print('Could not find ' + master_file + ' matching correct file name format in ' + settings_default_folder)
        return False

def overwrite_core_char(path, master_char_file):
    core_char_regex = '^core_char_\d+\.dat$'
    return overwrite_core_files(path, master_char_file, core_char_regex)

def overwrite_core_user(path, master_user_file):
    core_user_regex = '^core_user_\d+\.dat$'
    return overwrite_core_files(path, master_user_file, core_user_regex)

def get_files(path, file_regex):
    file_regex = re.compile(file_regex)
    file_list = []
    for root, dirs, files in os.walk(path):
        for current_file in files:
            if file_regex.match(current_file):
                file_list.append(current_file)
    return file_list

def main():
    parser = argparse.ArgumentParser(description='Restore, backup or copy the EVE settings/config folder named e_eve_sharedcache_tq_tranquility. \
        See: https://forums.eveonline.com/t/manually-copy-settings-between-characters-and-accounts/32704 for more details \
        and to help you decide what to provide for the --char and --user arguments. Please note environment variables such as %%USERNAME%% will \
        not work correctly in paths. This script currently only supports the Default (settings_Default) profile. If you have changed the profile using the \
        Profile Management Tool this script won\'t currently work correctly.')
    parser.add_argument('eve_settings_folder', help='Full path of the eve settings/config folder, \
        for Tranquility this will be called e_eve_sharedcache_tq_tranquility. Example argument: \
        C:\\Users\Bob\AppData\Local\CCP\EVE\e_eve_sharedcache_tq_tranquility')
    parser.add_argument('-r', '--restore', help='File name of the file to restore.')
    parser.add_argument('-b', '--backup', help='Directory where to store the backup zip file. \
        Backup files will be named eve_copy_config_backupTIMESTAMP.zip E.g. eve_copy_config_backup20201120T132937.zip')
    parser.add_argument('-c', '--char', help='File name of the core_char file to overwrite others. E.g. core_char_916230538.dat')
    parser.add_argument('-u', '--user', help='File name of the core_user file to overwrite others. E.g. core_user_124210597.dat')
    parser.add_argument('-f', '--force', help='Force overwrite without backing up. NOT RECOMMENDED, please use backup option.', action='store_true')
    args = parser.parse_args()

    # Validate arguments
    if (args.char or args.user) and args.backup is None:
        if args.force:
            pass
        else:
            print('Overwriting files without backing up is very dangerous. Please use backup option or use force flag (-f) (NOT RECOMMENDED).')
            return

    if args.backup and args.restore:
        print('Cannot use backup and restore option at the same time.')
        return

    if (args.char or args.user) and args.restore:
        print('Cannot use char or user options and restore option at the same time.')
        return

    # Strip trailing quote
    eve_settings_folder = args.eve_settings_folder.strip('"')
    # Add slash
    eve_settings_folder = os.path.join(eve_settings_folder, '')

    if not os.path.isdir(eve_settings_folder):
        print('Could not locate eve settings folder.')
        return

    if args.backup:
        # Strip trailing quote
        backup_path = args.backup.strip('"')
        # Add slash
        backup_path = os.path.join(backup_path, '')
        # Validate paths for backup
        if not os.path.isdir(backup_path):
            print('Invalid backup directory')
            return
        if not backup_settings(backup_path, eve_settings_folder):
            # Backup failed
            return

    if args.restore:
        if os.path.isfile(args.restore):
            restore_settings(args.restore, eve_settings_folder)
        else:
            print('Restore file not found.')
            return

    if args.char:
        if overwrite_core_char(eve_settings_folder, args.char):
            print('Overwritten core_char files successfully.')


    if args.user:
        if overwrite_core_user(eve_settings_folder, args.user):
            print('Overwritten core_user files successfully.')

if __name__ == '__main__':
    main()