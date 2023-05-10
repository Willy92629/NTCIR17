print("hi")
import json
import random
def gen_relation_2classification(filepath,outpath,outpath2):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf8') as f:
        datas=json.load(f)
        random.shuffle(datas)
        output_1=datas[0:6218]
        output_2=datas[6218:6518]
    with open(outpath,'w',encoding='utf-8') as f2:
        json.dump(output_1,f2,ensure_ascii=False)
    with open(outpath2,'w',encoding='utf-8') as f2:
        json.dump(output_2,f2,ensure_ascii=False)



gen_relation_2classification("./../../../data/FinArg_SocialMedia/train_social.json","./../../../data/FinArg_SocialMedia/train_data2.json","./../../../data/FinArg_SocialMedia/test_data2.json")
