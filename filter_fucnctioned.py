import os
os.chdir("D:\\Study\\CL\\pythonProject")
#!pip install langdetect
#!pip install difflib
#!pip install thefuzz
#!pip install python-Levenshtein
import string
import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize, wordpunct_tokenize
from nltk.stem.snowball import SnowballStemmer
from thefuzz import fuzz
stemmer = SnowballStemmer("russian")
##### 0 emulate inputs
# original text
with open("rbk_orig.txt", "r", encoding='utf-8') as orig:
    orig=str(orig.read())
#profanity lexis
with open("obscene.txt", "r", encoding='utf-8') as obs:
    obs=str(obs.read())
    obs=obs.translate(str.maketrans("", "", string.punctuation))
    obs=obs.strip(" ")
#profanity stemmed list
obs_tk= wordpunct_tokenize(obs)
obs_st=[]
for word in obs_tk:
  obs_st.append(stemmer.stem(word))
#answer 1 good
with open("rbk_inp.txt", "r", encoding='utf-8') as inp:
    inp=str(inp.read())
#answer 2 small with profanity
with open("rbk_inp2.txt", "r", encoding='utf-8') as inp2:
    inp2=str(inp2.read())    
#answer 3 different with random strings
with open("rbk_inp3.txt", "r", encoding='utf-8') as inp3:
    inp3=str(inp3.read()) 
#answer 4 html part
with open("rbk_inp4.txt", "r", encoding='utf-8') as inp4:
    inp4=str(inp4.read())     

#length original
orig_len=len(orig)
filt_result={}
#create filter DF

#list of obscene prepositions
prep_list=["не","по","твою","мать"]

#check 1 length
def volume_check(input_1,orig_volume):
  inp_vol= len(input_1)
  if (inp_vol/orig_volume) > 1.1000:
    filt_result["vol_chk"]=1
    filt_result["vol_comm"]="Longer than expected"
  elif (inp_vol/orig_volume) <0.90000:
    filt_result["vol_chk"]=1
    filt_result["vol_comm"]="Smaller than expected"
  else:
    filt_result["vol_chk"]=0
    filt_result["vol_comm"]=""
#CHECK
volume_check(inp2,orig_len)
filt_result

#check2 text similarity
def similarity_check(input_1,original_text):
  sim_rat=fuzz.ratio(original_text,input_1)
  if sim_rat < 90:
    filt_result["sml_chk"] = "1"
    filt_result["sml_comm"] = "Different for more than 10%. Similarity rate is "+str(sim_rat)
  else:
    filt_result["sml_chk"] = "0"
    filt_result["sml_comm"] = "Similarity rate is "+str(sim_rat) 
#CHECK
similarity_check(inp2,orig)
filt_result["sml_chk"]
filt_result["sml_comm"]
similarity_check(inp3,orig)
filt_result["sml_chk"]
filt_result["sml_comm"]

#check3 html tagging
def html_check (input_1):
  html_tags=re.findall ("<[^>]+>",string=input_1)
  htg_len=len(html_tags)
  if htg_len > 0:
    filt_result["html_chk"] = "1"
    filt_result["html_text"] = html_tags
  else:
    filt_result["html_chk"] = "0"
    filt_result["html_text"] = ""
#CHECK
html_check(inp)
filt_result["html_chk"] 
filt_result["html_text"]
html_check(inp4)
filt_result["html_chk"] 
filt_result["html_text"]

#check4 obscene lexis
def obscene_check (input_1):
  #token-stem
  inp_tk=input_1.translate(str.maketrans("", "", string.punctuation))  
  inp_tk= wordpunct_tokenize(inp_tk)
  inp_st=[]
  for word_inp in inp_tk:
    inp_st.append(stemmer.stem(word_inp))
  inp_st_str=str(inp_st)
  #prep
  obs_wrd_lst=[]
  ind_lst=[]
  orig_wrd_lst=[]
  #check
  for i1 in obs_st:
    if i1 in inp_st and i1 not in prep_list :
      obs_wrd= i1
      ind_obs=inp_st.index(i1)
      orig_wrd=inp_tk[ind_obs]
      obs_wrd_lst.append(obs_wrd)
      ind_lst.append(ind_obs)
      orig_wrd_lst.append(orig_wrd)
    else:
      pass
    #write check
  if len(obs_wrd_lst) > 0:
    filt_result["obscene_chk"] = "1"
    filt_result["obscene_text"] = obs_wrd_lst
    filt_result["obscene_text_orignal"] = orig_wrd_lst
  else:
    filt_result["obscene_chk"] = "0"
    filt_result["obscene_text"] = ""
    filt_result["obscene_text_orignal"] = ""
#CHECK
obscene_check (inp)
filt_result["obscene_chk"]
filt_result["obscene_text"]
filt_result["obscene_text_orignal"]
obscene_check (inp4)
filt_result["obscene_chk"]
filt_result["obscene_text"]
filt_result["obscene_text_orignal"]


#THE Function
def filter_text (input_1,original_text,orig_volume,person_id):
  filt_result={}
  filt_result["ID"]=person_id
  volume_check(input_1,orig_volume)
  similarity_check(input_1,original_text)
  html_check (input_1)
  obscene_check (input_1)
  return filt_result



#check output
f_df = pd.DataFrame()
cur=filter_text(inp,orig,orig_len,"001")
cur=pd.DataFrame(cur,index=[0])
pd.concat(f_df, cur, ignore_index=True)

f_df.to_csv("Filter_results.csv", sep=';',encoding="CP1251")



  
  
