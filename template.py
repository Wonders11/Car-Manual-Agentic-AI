import os
from pathlib import Path

package_name = "CarManualAgenticAI"

list_of_files = [
    "github/workflows/.gitkeep",

    f"{package_name}/agents/__init__.py",
    f"{package_name}/agents/tata_agent.py",
    f"{package_name}/agents/hyundai_agent.py",
    f"{package_name}/agents/maruti_agent.py",

    f"{package_name}/vector_store/ingestion.py",
    f"{package_name}/vector_store/db_utils.py",
    f"{package_name}/vector_store/manuals/.gitkeep",  # To keep the manuals folder tracked in git

    f"{package_name}/langgraph_app/router.py",
    f"{package_name}/langgraph_app/llm_utils.py",

    f"{package_name}/api/app.py",

    f"{package_name}/config.py",
    f"{package_name}/main.py",

    "notebooks/research.ipynb",
    ".gitignore",
    "requirements.txt",
    ".env",
]

# Create files and directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creates empty file
    else:
        print(f"{filepath} already exists")





# import os
# from pathlib import Path

# package_name="CarManualAgenticAI"

# list_of_files=[
#     "github/workflows/.gitkeep",
#     f"src/{package_name}/__init__.py",
#     f"src/{package_name}/components/__init__.py",
#     f"src/{package_name}/components/data_ingestion.py",
#     f"src/{package_name}/components/data_transformation.py",
#     f"src/{package_name}/components/model_trainer.py",
#     f"src/{package_name}/pipelines/__init__.py",
#     f"src/{package_name}/pipelines/training_pipeline.py",
#     f"src/{package_name}/pipelines/prediction_pipeline.py",
#     f"src/{package_name}/logger.py",
#     f"src/{package_name}/exception.py",
#     f"src/{package_name}/utils/__init__.py",
#     "notebooks/research.ipynb",
#     "notebooks/data/.gitkeep",
#     "requirements.txt",
#     "setup.py",
#     "init_setup.sh",
# ]


# # here will create a directory

# for filepath in list_of_files:
#     filepath=Path(filepath) # generates system compatible path (considers / or \ slash for file location)
#     filedir,filename=os.path.split(filepath) # it splits file location and file name
    
#     """ how exist_ok works:if "directory" already exists, 
#     os.makedirs() will not raise an error, and it will do nothing. 
#     If "my_directory" doesn't exist, it will create the directory.
#     """
#     if filedir != "":
#         os.makedirs(filedir,exist_ok=True)
        
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#         with open(filepath,"w") as f:
#             pass
#     else:
#         print("file already exists")

# # here will use the file handling