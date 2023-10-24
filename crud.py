from database import inject_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from table import Text

@inject_db
def add_text(text, db:Session):
    text = Text(text=text)
    db.add(text)
    db.commit()
    return db.refresh(text)

@inject_db
def delete_text_by_id(id, db:Session):
    
    if not db.query(Text).filter(Text.id == id).first():
        return False
    
    db.query(Text).filter(Text.id == id).delete()
    db.commit()
    return True

@inject_db
def delete_all_texts(db:Session):
    db.query(Text).delete()
    db.commit()
    return True


@inject_db
def get_limit_offset(limit, offset, db:Session):
    return db.query(Text).limit(limit).offset(offset).all()

@inject_db
def get_unparsed_limit_offset(limit, offset, db:Session):
    return db.query(Text).filter(Text.is_parsed == False).limit(limit).offset(offset).all()

@inject_db
def get_all_texts(db:Session):
    return db.query(Text).all()


@inject_db
def update_parse_by_id(id:int,parse_result:str, db:Session):
    
    if not db.query(Text).filter(Text.id == id).first():
        return False
    
    db.query(Text).filter(Text.id == id).update(
        {"parse_result":parse_result,
         "is_parsed":True,
         "update_time":func.now()}
    )
    
    db.commit()

    return True

@inject_db
def get_num_prased(db:Session):
    return db.query(Text).filter(Text.is_parsed == True).count()

@inject_db
def add_text_with_key(text, key, db:Session):
    text = Text(text=text, key=key)
    db.add(text)
    db.commit()
    return db.refresh(text)

def add_dataframe(df, text_col:str = "text", key_col:str = None):
    
    texts = df[text_col].tolist()
    
    if key_col is not None:
        keys = df[key_col].tolist()
        for text, key in zip(texts, keys):
            add_text_with_key(text, key)
    else:
        for text in texts:
            add_text(text)
            
    return True


def reset_all_text(db:Session):
    db.query(Text).update(
        {"parse_result":None,
         "is_parsed":False,
         "update_time":func.now()}
    )
    db.commit()
    return True

@inject_db
def reset_breaking_records(db:Session):
    # update those records with is_parse = True and parse_result = None
    # set is_parse = False
    db.query(Text).filter(Text.is_parsed == True, Text.parse_result == None).update(
        {"is_parsed":False, "update_time":func.now()}
    )
    
    return True
 