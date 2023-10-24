import openai
from prompt import description
from crud import (
    update_parse_by_id, 
    get_unparsed_limit_offset,
    get_num_prased
)
from concurrent.futures import ThreadPoolExecutor
import time
from config import get_settings

settings = get_settings()

def get_completion(prompt:str, model="gpt-3.5-turbo", timeout:int = 30):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        timeout = timeout
    )
    return response.choices[0].message["content"]


def mock_ai(prompt:str, model="davinci", timeout:int = 30):
    import string
    import random
    return "success " + ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        
        
class DescriptionParser:
    
    def __init__(self, testing:bool = True, batch_sleep:float = 0.2, timeout = 30):
        self.ai = get_completion if not testing else mock_ai
        self.batch_sleep = batch_sleep
        self.timeout = timeout

    def parse_single(self, text_id: int, **kwargs):
        try:
            prompt = description.prompt.format(**kwargs)
            result = self.ai(prompt, timeout = self.timeout)
            update_parse_by_id(text_id, result)
        except Exception as e:
            print("Error while prasing text.")
            pass
        
    def prase_batch(self, size:int):
        
        if size > 10:
            print(f"Concurrent size {size} is too large. Consider using a smaller size.")
            
        current_batch = get_unparsed_limit_offset(limit =size, offset = 0)
    
        if len(current_batch) == 0:
            print("No more unprased text.")
            return False
        
        results = []
        
        with ThreadPoolExecutor(max_workers=size) as executor:
            for text in current_batch:
                future = executor.submit(self.parse_single, text.id, description=text.text)
                results.append(future)   
           
        time.sleep(self.batch_sleep)
    
        print("Finished Batch. Currently parsed texts: ", get_num_prased())
        return True
    
    def __call__(self, size:int, **kwargs):
        return self.prase_batch(size, **kwargs)