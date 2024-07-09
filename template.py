import os 
from pathlib import Path 


Project_name = "US-Visa-Approval"

list_of_files = [

    f"{Project_name}/__init__.py",
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/components/data_ingestion.py",
    f"{Project_name}/components/data_validation.py",
    f"{Project_name}/components/data_transformation.py",
    f"{Project_name}/components/model_trainer.py",
    f"{Project_name}/components/model_evaluation.py",
    f"{Project_name}/components/model_pusher.py",
    f"{Project_name}/configuration/__init__.py",
    f"{Project_name}/constants/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/entity/config_entity.py",
    f"{Project_name}/entity/artifact_entity.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/pipeline/training_pipeline.py",
    f"{Project_name}/pipeline/prediction_pipeline.py",
    f"{Project_name}/utils/__init__.py",
    f"{Project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "config/model.yaml"
    "config/schema.yaml"

]



for filepath in list_of_files:
    filepath = Path(filepath)   # Do not differentitate between front slash and backward , Path ka dhyaan rakhne waala
    filedir , filename = os.path.split(filepath) # this will split the path into directorya and file 
    if filedir != "":
        os.makedirs(filedir,exist_ok="True")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath,"w") as f:  # As we are opening file in write mode , if this file doesn't exist then it will create one 
            pass
    
    else :
        print(f"file is present at : {filepath}")