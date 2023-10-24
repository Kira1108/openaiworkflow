# MultiThread Openai

1. Create database
```
# try python main.py --help
python main.py --file_path data/data.csv --textcol text
```


2. Run your AI in a notebook.
```
import openai
from chat import DescriptionParser
from crud import get_limit_offset
openai.api_key = "You api key"

parse = DescriptionParser()

parse(size = 100)

get_limit_offset(limit = 100, offsite = 0)
```