# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'

# # IEMOCAP数据处理

# 数据包括视频、音频、文本。视频是以对话形式录制的。



import os
import json
import re
import os
import pandas as pd


data_path = 'D:\dataset\IEMOCAP_full_release\IEMOCAP_full_release'


#获取数据标签
def get_labels(data_path):
    # 从每一个session的ialog\\EmoEvaluation中获取每一句话的标签，结果输出到iemocap_label.csv文件中
    info_line = re.compile(r'\[.+\]\n', re.IGNORECASE)
    start_times, end_times, wav_file_names, emotions, vals, acts, doms = [], [], [], [], [], [], []
    for sess in range(1, 6):
        emo_evaluation_dir = data_path+'\\Session{}\\dialog\\EmoEvaluation\\'.format(sess)
        evaluation_files = [l for l in os.listdir(emo_evaluation_dir) if 'Ses' in l]
        for file in evaluation_files:
            with open(emo_evaluation_dir + file) as f:
                content = f.read()
            info_lines = re.findall(info_line, content)
            for line in info_lines[1:]:  # the first line is a header
                start_end_time, wav_file_name, emotion, val_act_dom = line.strip().split('\t')
                start_time, end_time = start_end_time[1:-1].split('-')
                val, act, dom = val_act_dom[1:-1].split(',')
                val, act, dom = float(val), float(act), float(dom)
                start_time, end_time = float(start_time), float(end_time)
                start_times.append(start_time)
                end_times.append(end_time)
                wav_file_names.append(wav_file_name)
                emotions.append(emotion)
                vals.append(val)
                acts.append(act)
                doms.append(dom)
    df_iemocap = pd.DataFrame(columns=['starttime', 'endtime', 'sentence', 'emotion', 'val', 'act', 'dom'])
    df_iemocap['starttime'] = start_times
    df_iemocap['endtime'] = end_times
    df_iemocap['sentence'] = wav_file_names
    df_iemocap['emotion'] = emotions
    df_iemocap['val'] = vals
    df_iemocap['act'] = acts
    df_iemocap['dom'] = doms
    print(df_iemocap.tail())
    df_iemocap.to_csv(data_path+'\\pre_processed\\iemocap_label.csv', index=False)      

# 音频文件处理.wav














# ## 文本数据处理
# 
# 将文本整理保存为JSON文件，数据格式如下
# "Session1": sessionm名
#     {"Ses01F_impro01":文件名 
#         [{"sentence": "Ses01F_impro01_F000", "startime": "006.2901", "endtime": "008.2357", "text": "Excuse me."}, 话语信息包括句话语编号，起始时间，结束时间，文本内容
#         {"sentence": "Ses01F_impro01_M000", "startime": "007.5712", "endtime": "010.4750", "text": "Do you have your forms?"},
#         ...],
#     "Ses01F_impro02": 
#         [{"sentence": "Ses01F_impro02_F000", "startime": "007.2688", "endtime": "016.6000", "text": "Did you get the mail? So you saw my letter?"},
#         ...],
#     ...
#     }
# "Session2":
#     {
#         ...
#     }
# ...
def get_textJSON(data_path):
    text_dir ={}
    iemocap_filename = {}
    for i in range(5):
        list_path  = data_path + '\\Session'+str(i+1)+'\\dialog\\transcriptions'
        session_dir = {}
        txt_list = os.listdir(list_path)
        for txt in txt_list:
            txt_path = os.path.join(list_path,txt)
            with open(txt_path,'r',encoding="utf-8") as f:
                linelist = f.read().split("\n")
                result =[]
                for line in linelist:
                    if len(line) > 30 and "]:" in line:
                        sentence = line.split(' ')[0]
                        startime = line.split(" ")[1].split('-')[0][1:]
                        endtime = line.split(" ")[1].split('-')[1][:-2]
                        text = line.split("]: ")[1]
                        item = {
                            'sentence':sentence,
                            'startime':startime,
                            'endtime':endtime,
                            'text':text
                        }
                        result.append(item)
            session_dir[txt[:-4]] = result
        iemocap_filename['Session'+ str(i+1)] = txt_list
        text_dir['Session'+ str(i+1)] = session_dir
    #将文本保存为json           
    with open('IEMOCAP_text.json', 'w') as dump_f:
        json.dump(text_dir,dump_f)
    #将iemocap数据库中的文件名，即视频，音频，文本名字保存
    with open('iemocap_filename.json', 'w') as dump_f:
        json.dump(iemocap_filename,dump_f)   


# 读取JSON文件
# with open('IEMOCAP_text.json', 'r',encoding="utf-8") as load_f:
#     text = json.load(load_f)
#     print(text['Session1']["Ses01F_impro01"][0])

if __name__ =='__main__':
    #获取标签
    # get_labels(data_path)
    #获取文本数据
    get_textJSON(data_path)
