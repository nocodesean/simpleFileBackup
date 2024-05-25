import os
import shutil
import datetime

def backup_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    backup_path = os.path.join(backup_dir, backup_name)
    
    shutil.make_archive(backup_path, 'zip', source_dir)
    print(f'Backup created at {backup_path}')

source_directory = '/path/to/source'
backup_directory = '/path/to/backup'
backup_files(source_directory, backup_directory)
