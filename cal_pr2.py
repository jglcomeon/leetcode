import os 
import json

import pandas as pd

file_name = "/Users/bytedance/Downloads/281474993522880-temp_page-查询 06-24 18_43-查询24.csv"

df = pd.read_csv(file_name, encoding="utf-8", usecols=["item_id","audit_label","verify_score","verify_results","meta_predict","date","save_hour","thunder_url"])

audio_readable = []
video_blur = []
video_fore_back = []
total_cnt = 0
tf = open('pred_readable_data.csv', 'w')
tf.write('item_id' + '\t' + 'verify_results' + '\t' + 'thunder_url' + '\n')
for row_index, row in df.iterrows():
    total_cnt += 1
    item_id = row["item_id"]
    audit_label = row["audit_label"]
    verify_score = row["verify_score"]
    verify_results = row["verify_results"]
    thunder_url = row["thunder_url"]
    meta_predict = json.loads(row["meta_predict"])
    try:
        video_audio_visual_quality_model_meta = json.loads(meta_predict["meta_predict"]["video_audio_visual_quality_model"])
        video_audio_quality = video_audio_visual_quality_model_meta['meta_predict']['video_audio_quality']
        video_readable_model = video_audio_quality['video_readable_model']
        if int(video_readable_model['verify_score']) == 2:
            tf.write(str(item_id) + '\t' + str(video_readable_model['verify_results']) + '\t' + thunder_url + '\n')
        print('success')

    except Exception as e:
        print(meta_predict["meta_predict"]["video_audio_visual_quality_model"])
        print(e)
