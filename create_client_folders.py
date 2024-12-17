import os

def load_client_ids(file_path):
    """
    Load client IDs from a file. Assumes one client ID per line.
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            client_ids = [line.strip() for line in file if line.strip()]
        print(f"Loaded {len(client_ids)} client IDs from {file_path}")
        return client_ids
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []

def get_existing_folders(directory):
    """
    Get a list of folder names in the specified directory.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory {directory} does not exist.")
        return []

    folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    print(f"Found {len(folders)} existing folders in {directory}")
    return folders

def create_missing_folders(missing_ids, directory):
    """
    Create folders for the missing client IDs.
    """
    created_folders = []
    for client_id in missing_ids:
        folder_path = os.path.join(directory, client_id)
        try:
            os.makedirs(folder_path)
            created_folders.append(client_id)
            print(f"Created folder: {folder_path}")
        except Exception as e:
            print(f"Error creating folder for {client_id}: {e}")
    return created_folders

def main():
    # File path for client ID list and target directory
    client_file = '//ses.int/global/Advanced Visualization/Production/Common/Keane/client_ids.txt'  # Replace with your file path
    target_directory = '//ses.int\global\Advanced Visualization\Staging'  # Replace with your directory path

    # Load client IDs
    client_ids = load_client_ids(client_file)
    if not client_ids:
        print("No client IDs to process. Exiting.")
        return

    # Get existing folders
    existing_folders = get_existing_folders(target_directory)

    # Find missing client IDs
    missing_ids = [client_id for client_id in client_ids if client_id not in existing_folders]
    print(f"Missing client folders: {len(missing_ids)}")

    # Create folders for missing client IDs
    if missing_ids:
        created_folders = create_missing_folders(missing_ids, target_directory)
        print(f"Successfully created {len(created_folders)} folders.")
    else:
        print("All client folders already exist. Nothing to create.")

if __name__ == "__main__":
    main()
