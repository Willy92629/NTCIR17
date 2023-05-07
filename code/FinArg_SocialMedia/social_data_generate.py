print("hi")
import json
import random
def gen_relation_2classification(filepath,outpath,outpath2):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf8') as f:
        datas=json.load(f)
        for i in datas:
            #print(i)
            if i[2]==2:
                i[2]=1
            if i[2]==1:
                output.append(i)
            
            if i[2]==0:
                zero_data.append(i)
        random.shuffle(zero_data)
        random.shuffle(output)
        z_data=zero_data[0:600]
        ztest_data=zero_data[600:684]
        print(len(output))
        output1=output[0:5734]
        output_test=output[5734:5834]
        print(len(output1))
        print(len(z_data))
        output1=output1+z_data+z_data+z_data+z_data+z_data+z_data+z_data
        
        print(len(output_test))
        print(len(ztest_data))
        output_test=output_test+ztest_data
        random.shuffle(output1)
        random.shuffle(output_test)
        print(len(output1)) 
        print(len(output_test))
        output_1=output1
        output_2=output_test
    with open(outpath,'w',encoding='utf-8') as f2:
        json.dump(output_1,f2,ensure_ascii=False)
    with open(outpath2,'w',encoding='utf-8') as f2:
        json.dump(output_2,f2,ensure_ascii=False)



#gen_data("./../../../data/FinArg_SocialMedia/train_social.json","./../../../data/FinArg_SocialMedia/train_social_2classification.json","./../../../data/FinArg_SocialMedia/test_social_2classification.json")
def gen_att_support_data(filepath,outpath,outpath2):
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

def gen_dev_att_support_data(filepath,outpath):
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
#gen_data3("./../../../data/FinArg_SocialMedia/dev_social.json","./../../../data/FinArg_SocialMedia/dev_social_att_sup.json")
def gen_final_3classification_data(filepath,filepath2,outpath):
    output=[]
    zero_data=[]
    with open(filepath,'r',encoding='utf-8') as f:
        datas=json.load(f)
        for i in datas:
            #print(i)
            output.append(i)
            
        #output=output+zero_data+zero_data+zero_data+zero_data+zero_data
    with open(filepath2,'r',encoding='utf-8') as f:
        datas=json.load(f)  
        for i in datas:
            #print(i)
            if i[2]==0:
                output.append(i)  
        random.shuffle(output)
        print(len(output)) 
        #output_1=output[0:5334]
        #output_2=output[5334:5834]
    with open(outpath,'w',encoding='utf-8') as f2: 
        json.dump(output,f2,ensure_ascii=False)
    #with open(outpath2,'w',encoding='utf-8') as f2:
    #    json.dump(output_2,f2,ensure_ascii=False)
gen_data4("./../../../data/FinArg_SocialMedia/test_social_att_sup.json","./../../../data/FinArg_SocialMedia/test_social_2classification.json","./../../../data/FinArg_SocialMedia/test_social.json")