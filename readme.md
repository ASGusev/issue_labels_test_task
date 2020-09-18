# Issue label prediction test task

This repository implements label prediction on react issues.
The [download_issues](/download_issues.py) script downloads issues from provided repository and the [issue_labels_prediction](/issue_labels_prediction.ipynb) notebook provides models training.

## Running
### Downloading data
The download_issues.py script expects two arguments: repository in form <profile_name/repository_name> and target directory. The issues are saved in target directory as separate json files. React issues can be downloaded by: 
> python3 download_issues.py facebook/react react_issues

Github authorization is required to get enough request quota, so the script prompts for a github access token.
### Running training
The issue_labels_prediction.ipynb notebook can be executed sequentially provided that the React issues are downloaded to react_issues/ directory. 
