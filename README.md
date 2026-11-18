# Lab 6: Code and Branch Coverage Analysis

SRN: PES2UG24CS049

## Files
- `mobile_data_plan.py` — application supplied with the lab.
- `CodeCoverageTest_PES2UG24CS049_application.py` — test cases for line/code coverage.
- `BranchCoverageTest_PES2UG24CS049_application.py` — test cases exercising decision branches.

## Install
```bash
python -m pip install pytest coverage
```

## Stage 1: Code coverage
Run this from the Lab 6 folder:
```bash
coverage run -m pytest -v CodeCoverageTest_PES2UG24CS049_application.py
coverage report -m
```
The application module achieved 95% line coverage in the validation run (above the 90% requirement).

Save a screenshot of the successful test output and coverage report in `ScreenShots/CodeCoverage_SS.png`.

## Stage 2: Branch coverage
Run this from the Lab 6 folder:
```bash
coverage run --branch -m pytest -v BranchCoverageTest_PES2UG24CS049_application.py
coverage report -m
```
The application module achieved 100% line and branch coverage in the validation run.

Save a screenshot of the successful test output and coverage report in `ScreenShots/BranchCoverage_SS.png`.

## Submission / commits
The handout requires two commits:
1. Commit the code-coverage test file and its terminal screenshot.
2. Commit the branch-coverage test file and its terminal screenshot.

Do not submit screenshots from an earlier run if they show less than 90% coverage. Capture the terminal after the final successful run for each stage.
