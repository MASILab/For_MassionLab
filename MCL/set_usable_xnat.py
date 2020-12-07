import dax
import pandas as pd
xnat = dax.XnatUtils.get_interface()

## 20201114
# df = pd.read_csv('/nfs/masi/MCL/xnat/MCL_all.csv')
# df = df.query('step1_usable == 1')
# cnt = 0
# for i, item in df.iterrows():
#     proj_id = 'MCL'
#     if cnt % 50 == 0:
#         print (cnt, len(df))
#     subject_label = str(item['subject_label']).replace('.0', '')
#     session_label = item['session_label']
#     scan_label = str(item['as_label']).replace('.0', '')
#     print (subject_label,session_label, scan_label)
#     scan = xnat.select_scan('MCL',subject_label,session_label, scan_label)
#     scan.attrs.set('quality','usable')
#     cnt += 1
    
df = pd.read_csv('/nfs/masi/MCL/xnat/xnat20201203_EDRN/download_report.csv')
df = df.query('new_usable == 1')
cnt = 0
for i, item in df.iterrows():
    proj_id = 'MCL'
    if cnt % 50 == 0:
        print (cnt, len(df))
    subject_label = str(item['subject_label']).replace('.0', '')
    session_label = item['session_label']
    scan_label = str(item['as_label']).replace('.0', '')
    print (subject_label,session_label, scan_label)
    scan = xnat.select_scan('MCL',subject_label,session_label, scan_label)
    scan.attrs.set('quality','usable')
    cnt += 1