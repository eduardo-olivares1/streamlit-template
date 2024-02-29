# About 
`streamlit-service` is the primary service and front-end for analyzing and visualizing data

## File structure
`Home.py` - The homepage and main python script to be run with `streamlit run`

`pages/*.py` - Individual pages that simply serve as controllers for data from `models/` and page layouts from `views/layouts.py`

`models/*.py` - Files that serve as modules that export pandas dataframes to be used by `views/layouts.py`

`data/` - Location for raw data to be stored

`views/layouts.py` - Contains classes that define page layouts, use markdown from `_markdown/`, and use data from 
`models/`. To be imported from the corresponding `pages/*.py` file or `Home.py`

`_markdown` - Markdown files used to write sections more effectively and then imported from `views/layouts.py` 

## Running Locally 
To run this service locally ensure you are in the `streamlit-service` folder:

### Install dependencies:
```shell
pip install -r requirements.txt
```

### Run the service:
```shell
streamlit run Home.py
```
