import streamlit as st
from packages.utils import get_model, set_adapter, get_adapt_name

def predict_scores(score_types, df, batch_size=32):
    model_r, tokenizer = get_model()
    preds_df = df[['smiles']].copy()

    if score_types != []:
        for i, name in enumerate(score_types):
            start = 0
            preds = []
            st.code('computing values for: '+ str(name))   
            set_adapter(name, model_r)
            
            bat = list(range(batch_size, df.shape[0], batch_size)) + [df.shape[0]+1]
            for b in bat:
                encoded = tokenizer(df['smiles'].to_list()[start:b], max_length=256, 
                                truncation=True, 
                                add_special_tokens=True,
                                padding="max_length", return_tensors="pt")
                encoded.to("cuda")
                logits = model_r(**encoded)[0]
                a = logits.cpu()
                a = a.detach().numpy()
                start += batch_size
                preds.append(a.ravel())

            arr = []
            for a in preds:
                arr = arr + list(a)
                
            preds_df['preds_'+name] = arr
    else:
        return -1

    return preds_df