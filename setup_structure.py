import os

# Define the folder structure
folders = [
    "data",
    "models/nemo_model",
    "models/final_model",
    "notebooks",
    "scripts",
    "logs/nemo_patch_generation",
    "outputs/predictions",
    "outputs/metrics"
]

# Define additional files to create
files = [
    "README.md",
    "requirements.txt",
    "CONTRIBUTING.md",
    "LICENSE",
    ".gitignore"
]

def create_structure(repo_name):
    try:
        # Create root folder for repository
        os.makedirs(repo_name, exist_ok=True)
        print(f"Created repository folder: {repo_name}")
        
        # Create folders
        for folder in folders:
            path = os.path.join(repo_name, folder)
            os.makedirs(path, exist_ok=True)
            print(f"Created folder: {path}")
        
        # Create files
        for file in files:
            path = os.path.join(repo_name, file)
            with open(path, 'w') as f:
                f.write("")  # Create empty file
            print(f"Created file: {path}")
        
        print("Repository structure created successfully!")
    except Exception as e:
        print(f"Error creating structure: {str(e)}")

# Set repository name
repository_name = "Project-SWE-bench"

# Create the structure
create_structure(repository_name)
