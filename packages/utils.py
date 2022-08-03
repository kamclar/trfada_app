from transformers import RobertaConfig, RobertaModelWithHeads
from transformers import TrainingArguments, AdapterTrainer, EvalPrediction, RobertaTokenizer
MODEL_PATH = "models\\bert_model\\"
TOKENIZER_PATH = "models\\bert_model\\tokenizer\\"
ADAPTERS_PATH = "models\\ds_adapters\\"

def get_model():
    tokenizer = RobertaTokenizer.from_pretrained(TOKENIZER_PATH, max_len=512)
    config = RobertaConfig.from_pretrained(
        MODEL_PATH,
        num_labels=1,
        )
    model_r = RobertaModelWithHeads.from_pretrained(
        MODEL_PATH,
        config=config,
        )

    return model_r, tokenizer

def set_adapter(name, model_r):
    model_r.load_adapter(ADAPTERS_PATH+name)
    model_r.set_active_adapters(name)
    model_r.to("cuda")    

def get_adapt_name(column):
    name = column.replace('_docking_score', '')
    name = name.split('_')[-1]+'_'+ name.split('_')[0]
    
    return 'docking_score_'+name 