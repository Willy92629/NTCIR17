# NTCIR
NTCIR Conference workshop</br>
In this study, we present three methods for judging the relationships between sentences. 


## Two-tiered Bert Classification (SMDT_1)

Using two tier of Bert model for Classification.</br>
The code is including Bert Training and Sentences Classifying.</br>
[Code](https://github.com/leonardo-lin/NTCIR/blob/main/Two_tiered_Bert_Classification.ipynb)</br></br>
The First-tiered Model is for separating none from support and attack.</br>
[bert for none and support with attack model](https://huggingface.co/Leonardolin/NTCIR_none_and_s_with_a)</br>
The Second-tiered Model is for separating support from attack.</br>
[bert for support and attack model](https://huggingface.co/Leonardolin/NTCIR_att_sup)</br>

## Mask LM (SMDT_2)
Using Masked Language Modeling (MLM) mechanism to enhance the domain knowledge of the Two-tiered BERT model in the financial domain.</br>
The code is including model training by MLM. </br>
[Code](https://github.com/leonardo-lin/NTCIR/blob/main/Bert_for_MLM.ipynb)</br>

The Training Mask LM Model for the stock and financial domain.</br>
[MLM model](https://huggingface.co/Leonardolin/MLM-for-Stock)</br>
The First-tiered Model is for separating none from support and attack.</br>
[MLM for none and support with attack model](https://huggingface.co/Leonardolin/MLM_NTCIR_none_and_s_with_a)</br>
The Second-tiered Model is for separating support from attack.</br>
[MLM for support and attack model](https://huggingface.co/Leonardolin/MLM_NTCIR_att_sup)</br>

## Boosting (SMDT_3)


