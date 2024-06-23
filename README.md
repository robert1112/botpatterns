# Bot List Updater

This repository contains a GitHub Actions workflow that updates a list of bot user agents once a week. The list is fetched from a public repository and saved to a file in this repository. The workflow runs every Sunday at midnight Taiwan time.

## Workflow

The GitHub Actions workflow is defined in `.github/workflows/update-bot-list.yml`. It performs the following steps:
1. Checks out the repository.
2. Sets up Python.
3. Installs the required dependencies.
4. Runs a Python script to fetch and update the bot list.
5. Commits and pushes the changes to the repository.

## Schedule

The workflow is scheduled to run:
- **Every Sunday at midnight Taiwan time** (which is 4 PM UTC on Saturday).

## Manual Trigger

The workflow can also be triggered manually from the GitHub Actions tab.

## Ensure the Correct Directory Structure:
your-repository/
├── .github/
│   └── workflows/
│       └── update-bot-list.yml
├── update_bot_list.py
