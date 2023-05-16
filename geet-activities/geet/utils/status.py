'''
[Module] Status command utils.
'''
import os
import json
import hashlib


def get_current_path() -> str:

    return  os.getcwd() + '/'


def get_tree_files(path: str) -> list:

    root_len = len(get_current_path())
    tree_files = []

    for root, dirs, files in os.walk(path, topdown=False):
        # Añade archivos a tree_files
        for file in files:
            tree_files.append(os.path.join(root, file)[root_len:])

        # Añade directorios vacíos a tree_files
        for directory in dirs:
            dir_path = os.path.join(root, directory)[root_len:]
            if not os.listdir(os.path.join(root, directory)):
                tree_files.append(dir_path)

    return tree_files

    

def list_files(path: str) -> list:

    files_to_ignore_raw = read_file_by_lines(path + '.geet/.geetignore')
    files_to_ignore = [file_name[:-1] for file_name in files_to_ignore_raw]
    all_files = get_tree_files(path)
    non_geet_files = []

    for file_name in all_files:
        if file_name[:5] != '.geet':
            non_geet_files.append(file_name)
    
    files = []

    for file in non_geet_files:
        if file not in files_to_ignore:
            files.append(file)

    return files


def read_file(path: str) -> str:

    with open(path, 'r') as reader:
        return reader.read()


def read_file_by_lines(path: str) -> list:

    with open(path, 'r') as reader:
        return reader.readlines()


def hash_file(path: str) -> str:
    with open(path, 'rb') as file:
        file_content = file.read()
        return hashlib.sha1(file_content).hexdigest()



def get_hash_dict(path: str) -> dict:
    
    files = list_files(path)
    hash_collection = {}

    for file in files:
        hash_collection[file] = hash_file(path + file)
        
    return hash_collection


def save_hash_dict(path: str) -> None:

    with open(path + '.geet/.hashdict.json', 'w') as writer:
        hash_dict = get_hash_dict(path)
        json.dump(hash_dict, writer)

    return None


def read_current_hash_dict(path: str) -> dict:

    with open(path + '.geet/.hashdict.json', 'r') as reader:
        file = reader.read()
        return json.loads(file)


def scan_for_new_files(path: str) -> list:

    previous_files = read_current_hash_dict(path).keys()
    current_files = get_hash_dict(path).keys()
    new_files = []

    for file in current_files:
        if file not in previous_files:
            new_files.append(file)

    return new_files


def scan_for_deleted_files(path: str) -> list:
 
    previous_files = read_current_hash_dict(path).keys()
    current_files = get_hash_dict(path).keys()
    deleted_files = []

    for file in previous_files:
        if file not in current_files:
            deleted_files.append(file)

    return deleted_files


def scan_for_modified_files(path: str) -> list:

    previous_hash_dict = read_current_hash_dict(path)
    current_hash_dict = get_hash_dict(path)
    previous_files = previous_hash_dict.keys()
    current_files = current_hash_dict.keys()
    modified_files = []

    for file in current_files:
        if file in previous_files:
            if previous_hash_dict[file] != current_hash_dict[file]:
                modified_files.append(file)

    return modified_files
        


