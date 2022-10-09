import csv
import json


if __name__ == '__main__':
    csv_file = '/Users/bytedance/Downloads/281474993427536-temp_page-查询 09-28 08_47-查询4.csv'
    save_csv = f"{csv_file.split('.csv')[0]}_sample.csv"

    csv_reader = csv.DictReader(open(csv_file, 'r'))
    next(csv_reader)

    fileldnames = csv_reader.fieldnames
    csv_writer = csv.DictWriter(open(save_csv, 'w'), fieldnames=fileldnames)
    csv_writer.writeheader()

    cnt_all = 0
    verify_results_cnt = {}
    for row in csv_reader:
        cnt_all += 1
        verify_results = json.loads(row['verify_results'])

        if len(verify_results) == 0:
            verify_results_cnt['未命中单点低质'] = verify_results_cnt.get('未命中单点低质', 0) + 1

        for verify_result in verify_results:
            cnt = verify_results_cnt.get(verify_result, 0)
            cnt += 1
            verify_results_cnt[verify_result] = cnt

            row['verify_results'] = verify_result
            csv_writer.writerow(row)

    print(f'ALL: {cnt_all}')
    for k, v in verify_results_cnt.items():
        print(f'{k}: {v}')