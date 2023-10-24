prompt = """
I will provide you with a transaction_description in Spanish, \
Analyze the description and extract the following information: \
1. transaction content type(categorize transaction into different types, 1-2 english words, connected with underscore `_`, for example, 
    - purchase
    - bank
    - salary
    - loan
    - credit_card
    - personal_expenditure
    - service_subscription
    - refund
    - insurance
    - etc.
2. keywords(a list of words in original language that you think is important to determine the transaction type in previous step, 0-2 words) \
3. English translation
Format your result into a valid json object with keys being \
"english_translation"(string),
"transaction_type"(string) and "keywords"(list[str]). \
the transaction description is delimited with triple backticks \
transaction_description=```{description}```
NOTE: you are expected to maximize the returned information.
parse_result = 
""".strip()
