# check meta data

```sh
# make venv
python3 -m venv venv

# activate venv
source venv/bin/activate

#install dependencies
pip install -r reqirements.txt

# test data
git clone https://git.tizen.org/cgit/scm/meta/qb

# test
python main.py ./qb
```