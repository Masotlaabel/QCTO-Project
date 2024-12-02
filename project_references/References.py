import os
import subprocess

def create_references_file_and_github_link(
    folder_name="project_references", 
    file_name="references.txt", 
    git_repo_path=r"C:\Users\MASOT\OneDrive\Desktop\QCTO-Project",  # Path to your local repo
    github_repo_url="https://github.com/Masotlaabel/QCTO-Project"
):
    """
    Creates a references file in a specified folder within a GitHub repository,
    adds the file to Git, and generates a GitHub link to the file.

    Args:
        folder_name (str): Name of the folder to store the file.
        file_name (str): Name of the file to store references.
        git_repo_path (str): Path to the local GitHub repository.
        github_repo_url (str): URL of the GitHub repository.

    Returns:
        str: Full path to the references file and its GitHub URL.
    """
    # Create the folder path within the GitHub repository
    folder_path = os.path.join(git_repo_path, folder_name)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Create the file path
    file_path = os.path.join(folder_path, file_name)

    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("# References and Sources\n\n")
            file.write("This file contains all the references and sources consulted during the project.\n")
    
    print(f"References file created at: {file_path}")

    # Add the file to Git tracking
    try:
        # Ensure Git repository is initialized
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=git_repo_path, check=True)
        print("Git repository detected. Adding the file for tracking...")
        
        subprocess.run(["git", "add", file_path], cwd=git_repo_path, check=True)
        print(f"File {file_path} added to Git tracking.")
    except subprocess.CalledProcessError:
        print("No Git repository detected in the specified path. Please initialize one with 'git init'.")
    
    # Construct the GitHub URL to the file
    relative_path = os.path.relpath(file_path, git_repo_path).replace("\\", "/")
    github_file_url = f"{github_repo_url}/blob/main/{relative_path}"
    print(f"GitHub URL to the file: {github_file_url}")

    return file_path, github_file_url

# Example usage:
references_file_path, github_file_url = create_references_file_and_github_link()

# Print the GitHub file link
print(f"Access your references file here: {github_file_url}")
