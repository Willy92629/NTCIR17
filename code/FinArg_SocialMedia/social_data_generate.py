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


#gen_data("./../../../data/FinArg_SocialMedia/train_social.json","./../../../data/FinArg_SocialMedia/train_social_2classification2.json")
def gen_data2(filepath,outpath,outpath2):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf-8') as f:
        datas=json.load(f)
        for i in datas:
            #print(i)
            if i[2]==0:
                continue
            if i[2]==2:
                i[2]=0
            output.append(i)
            
        #output=output+zero_data+zero_data+zero_data+zero_data+zero_data
        
        random.shuffle(output)
        print(len(output)) 
        output_1=output[0:5334]
        output_2=output[5334:5834]
    with open(outpath,'w',encoding='utf-8') as f2:
        json.dump(output_1,f2,ensure_ascii=False)
    with open(outpath2,'w',encoding='utf-8') as f2:
        json.dump(output_2,f2,ensure_ascii=False)

def gen_data3(filepath,outpath):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf-8') as f:
        datas=json.load(f)
        for i in datas:
            #print(i)
            if i[2]==0:
                continue
            if i[2]==2:
                i[2]=0
            output.append(i)
            
        #output=output+zero_data+zero_data+zero_data+zero_data+zero_data
        
        random.shuffle(output)
        print(len(output)) 
        #output_1=output[0:5334]
        #output_2=output[5334:5834]
    with open(outpath,'w',encoding='utf-8') as f2:
        json.dump(output,f2,ensure_ascii=False)
    #with open(outpath2,'w',encoding='utf-8') as f2:
    #    json.dump(output_2,f2,ensure_ascii=False)

#gen_data2("./../../../data/FinArg_SocialMedia/train_social.json","./../../../data/FinArg_SocialMedia/train_social_att_sup.json","./../../../data/FinArg_SocialMedia/test_social_att_sup.json")
gen_data3("./../../../data/FinArg_SocialMedia/dev_social.json","./../../../data/FinArg_SocialMedia/dev_social_att_sup.json")

