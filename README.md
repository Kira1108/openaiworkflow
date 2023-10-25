# MultiThread Openai

1. Create database
```bash
# try python main.py --help
python main.py --file_path data/data.csv --textcol text
```


2. Run your AI in a notebook.
```python
import openai
from chat import DescriptionParser
from crud import get_limit_offset
openai.api_key = "You api key"

parse = DescriptionParser()

parse(size = 100)

get_limit_offset(limit = 100, offsite = 0)
```

3. Implemenet a prompt
```python
class DescriptionParser:
    
    def __init__(self, testing:bool = True, batch_sleep:float = 0.2, timeout = 30):
        self.ai = get_completion if not testing else mock_ai
        self.batch_sleep = batch_sleep
        self.timeout = timeout

    def parse_single(self, text_id: int, **kwargs):
        try:
            # format the prompt, handle input
            prompt = description.prompt.format(**kwargs)

            # use ai to parse prompt
            result = self.ai(prompt, timeout = self.timeout)

            # update database
            update_parse_by_id(text_id, result)
        except Exception as e:
            print("Error while prasing text.")
            pass
        
    def prase_batch(self, size:int):
        
        if size > 10:
            print(f"Concurrent size {size} is too large. Consider using a smaller size.")
            
        # fetch from database
        current_batch = get_unparsed_limit_offset(limit =size, offset = 0)
    
        if len(current_batch) == 0:
            print("No more unprased text.")
            return False
        
        results = []
        
        with ThreadPoolExecutor(max_workers=size) as executor:
            for text in current_batch:
                # pass parameter to prompt
                future = executor.submit(self.parse_single, text.id, description=text.text)
                results.append(future)   
           
        time.sleep(self.batch_sleep)
    
        print("Finished Batch. Currently parsed texts: ", get_num_prased())
        return True
    
    def __call__(self, size:int, **kwargs):
        return self.prase_batch(size, **kwargs)
```