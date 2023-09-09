# NTCIR
NTCIR Conference workshop
In this study, we present three methods for judging the relationships between sentences. 


## Two-tiered Bert Classification (SMDT_1)
Using two tier of Bert model for Classification.
The code is include Bert Training and Sentences Classifying. Following Models is for classifying</br>

The First-tiered Model is for separating none from support and attack.</br>
[bert for none and support with attack model](https://huggingface.co/Leonardolin/NTCIR_none_and_s_with_a)</br>
The Second-tiered Model is for separating support from attack.</br>
[bert for support and attack model](https://huggingface.co/Leonardolin/NTCIR_att_sup)</br>

## Mask LM (SMDT_2)
Using Masked Language Modeling (MLM) mechanism to enhance the domain knowledge of the Two-tiered BERT model in the financial domain.

The Training Mask LM Model for the stock and financial domain.</br>
[MLM model](https://huggingface.co/Leonardolin/MLM-for-Stock)</br>
The First-tiered Model is for separating none from support and attack.</br>
[MLM for none and support with attack model](https://huggingface.co/Leonardolin/MLM_NTCIR_none_and_s_with_a)</br>
The Second-tiered Model is for separating support from attack.</br>
[MLM for support and attack model](https://huggingface.co/Leonardolin/MLM_NTCIR_att_sup)</br>

## Boosting (SMDT_3)


