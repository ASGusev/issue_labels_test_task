from pathlib import Path
from time import sleep
import json
from argparse import ArgumentParser

from github import Github
from github.GithubException import RateLimitExceededException


ISSUES_DIR_PATH = Path('issues')
RETRY_DELAY = 10 * 60


def download_issue(issue, target_directory):
    issue_file_path = target_directory / f'{issue.number}.json'
    while not issue_file_path.exists():
        try:
            issue_properties = {
                'id': issue.id,
                'number': issue.number,
                'title': issue.title,
                'body': issue.body,
                'has_pr': issue.pull_request is not None,
                'user': issue.user.login,
                'labels': [label.name for label in issue.labels]
            }
            with issue_file_path.open('wt', encoding='utf-8') as issue_file:
                json.dump(issue_properties, issue_file)
        except RateLimitExceededException:
            sleep(RETRY_DELAY)


def download_issues(repo, target_directory):
    issues = repo.get_issues(state='all')
    for issue in issues:
        download_issue(issue, target_directory)


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('repo')
    arg_parser.add_argument('target_dir')
    args = arg_parser.parse_args()

    target_dir = Path(args.target_dir)
    if not target_dir.exists():
        target_dir.mkdir()

    print('Enter token:')
    token = input()

    gh = Github(token)
    download_issues(gh.get_repo(args.repo), target_dir)
