Taiwan Buses Insurance List - 台灣遊覽車投保一覽表
==================================================

* [公路汽車客運業](HIGHWAY.md)
* [遊覽車客運業](TOUR.md)
* [綜合列表](ALL.md)
* [原始資料來源](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_list)


Print Insurance Info - 列印遊覽車公司投保資訊
---------------------------------------------

```shell

$ python print_buses_insurance.py
#類型: 乘客責任險
================

| 金額 | 公司名稱 | 全文 | 連結 |
| --- | --- | --- | --- |
| 650 | 大都會汽車客運股份有限公司 | 富邦產險乘客運送責任險650萬(107.01.01-108.01.01) | [查看](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_details.aspx?id=4d5d19dd-90e0-44d2-bd4d-5804a9e77b84) |
| 600 | 豪泰汽車客運股份有限公司 | 富邦產險乘客責任險600萬(107.09.11-108.09.11) | [查看](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_details.aspx?id=ad203b2c-8d67-4750-8e54-a0f178b44710) |
| 600 | 和欣汽車客運股份有限公司 | 富邦產物保險公司600萬元108.05.01~109.05.01 | [查看](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_details.aspx?id=32c06f6c-b582-4834-b804-b7180ee71e93) |
| 550 | 長榮國際儲運股份有限公司 | 富邦產物550萬(107.02.01-108.02.01) | [查看](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_details.aspx?id=c7166c20-9dad-4cf4-9bfc-188ee063356e) |
| 350 | 統聯汽車客運股份有限公司 | 華南產物保險股份有限公司:每一乘客體傷責任:350萬元,108年1月1日至109年1月1日 | [查看](https://www.thb.gov.tw/sites/ch/modules/businesscoach/businesscoach_details.aspx?id=06c8639f-8405-4916-bec7-5e3515ec64a7) |
...
```


How to - 如何使用
-----------------

1. get_buses_list.py

從公路總局網站取得所有遊覽車公司資料之連結

2. get_buses_info.py

從前面取得的遊覽車公司資料之連結，取得所有遊覽車公司之資訊
(目前僅儲存投保資訊)

3. print_buses_insurance.py [tour|all] [int:total]

列印遊覽車公司投保資訊