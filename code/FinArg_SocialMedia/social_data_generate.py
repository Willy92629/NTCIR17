print("hi")
import json
import random
def gen_data(filepath,outpath):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf8') as f:
        datas=json.load(f)
        for i in datas:
            #print(i)
            if i[2]==2:
                i[2]=1
            output.append(i)
            if i[2]==0:
                zero_data.append(i)
        output=output+zero_data+zero_data+zero_data+zero_data+zero_data
        
        random.shuffle(output)
        print(len(output)) 
        output_1=output[0:9500]
        output_2=output[9500:9939]
    with open(outpath,'w',encoding='utf-8') as f2:
        json.dump(output,f2,ensure_ascii=False)
    #with open("test_social_2classification.json",'w',encoding='utf-8') as f2:
    #    json.dump(output_2,f2,ensure_ascii=False)


gen_data("./../../../data/FinArg_SocialMedia/train_social.json","./../../../data/FinArg_SocialMedia/train_social_2classification2.json")
#gen_data("dev_social.json","dev_social_2classification.json")

