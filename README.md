# asi_group1

## Requirements
- use Python < 3.11
- install requirements listed in requirements.txt

## File structure
-  **`/bestmodel`**: Contains the currently.
-  **`/data`**: Contains sqlite database with script and data to seed it.
-  **`/deprecated`**: Contains old and unused code.
-  **`/fastapi`**: Contains fastapi backend that uses **`bestmodel`** for prediction.
-  **`/mushrooms`**: Contains kedro pipeline for model training and evaluation. Also gives us kedro viz to visualize the pipeline
-  **`/streamlit`**: Contains a streamlit app that provides frontend that allows prediction and triggering kedro pipeline.

## Running
- Install requirements `pip install -r requirements.txt`
- Run fastapi backend `cd ./fastpi & uvicorn main:app`
- Run kedro viz `cd ./mushrooms & kedro viz`
- Login to wandb `wandb init`
- Run streamlit app `streamlit run ./streamlit_app.py`