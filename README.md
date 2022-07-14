# IPL_Team

Sample python framework for test validation from JSON file

# JSON file

URL = https://gist.githubusercontent.com/kumarpani/1e759f27ae302be92ad51ec09955e765/raw/184cef7125e6ef5a774e60de31479bb9b2884cb5/TeamRCB.json

# Usage
Sample has one test file with two test cases

# Setup
Install pytest
```
pip install pytest
```

Install pytest-html for report generation
```
pip install pytest-html
```

# Run

1. Go to Pycharm terminal
2. Run all tests in pytest (single threaded)
```
python -m pytest
```
3. Report results
```
python -m pytest --html=report.html
```


