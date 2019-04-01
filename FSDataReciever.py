import csv

print("选择模式：输入“1”进入财务舞弊识别方式，输入“2”进入样本集更新方式。")
modeid = int(input())

indexName = ['应收账款周转率', '营业收入', '营业利润', '流动资产', '固定资产', '资产总计', '净利润', '所有者权益']
indexList = ['RTR', 'OI', 'OR', 'CA', 'FA', 'TA', 'NR', 'SE']

if modeid == 1:
    loopend = 0
    while loopend == 0:
        csvfile = open("logistics.csv", "a+", newline='')
        writer = csv.writer(csvfile)

        for i, value in enumerate(indexList):
            print("请输入最近一年和上一年的【"+indexName[i]+"】，两个数据之间以单个空格分隔：")
            _temp = str(input())
            locals()[value] = [float(_temp[0:_temp.find(" ")]), float(_temp[_temp.find(" ")+1:])]
        id1 = RTR[0] / RTR[1]
        id2 = OR[0] / OI[0] / OR[1] * OI[1]
        id3 = (1 - (CA[0] + FA[0]) / TA[0]) / (1 - (CA[1] + FA[1]) / TA[1])
        id4 = OI[0] / OI[1]
        id5 = NR[0] / SE[0] / NR[1] * SE[1]

        print("保荐机构是否曾涉及舞弊？0代表无，1代表是。")
        fraudspns = int(input())

        writer.writerow([id1, id2, id3, id4, id5, fraudspns])
        print("如果训练集录入没有结束，请输入0继续，输入1结束。")
        loopend = int(input())

    csvfile.close()
else:
    if modeid == 2:
        for i, value in enumerate(indexList):
            print("请输入最近一年和上一年的【"+indexName[i]+"】，两个数据之间以单个空格分隔：")
            _temp = str(input())
            globals()[value] = [float(_temp[0:_temp.find(" ")]), float(_temp[_temp.find(" ")+1:])]
        id1 = RTR[0] / RTR[1]
        id2 = OR[0] / OI[0] / OR[1] * OI[1]
        id3 = (1 - (CA[0] + FA[0]) / TA[0]) / (1 - (CA[1] + FA[1]) / TA[1])
        id4 = OI[0] / OI[1]
        id5 = NR[0] / SE[0] / NR[1] * SE[1]

        print("保荐机构是否曾涉及舞弊？0代表无，1代表是。")
        fraudspns = int(input())
        valvar = [int(1), id1, id2, id3, id4, id5, fraudspns]