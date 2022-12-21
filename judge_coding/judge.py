import os
import shutil
from pathlib import Path
import interview as iw
import json
import re
import traceback


def compare_dataJson(i):#i:第几个testcase
    result = {}
    f = open('answer/bz_data' + str(i) + '.json', encoding="utf-8")
    bz_dataJson = json.load(f)
    f.close()
    f = open('interview_result/data' + str(i) + '.json', encoding="utf-8")
    dataJson = json.load(f)
    f.close()
    key_list = ["主题", "日期", "开始时间", "结束时间", "地点", "主持人", "记录人", "应出席人数", "实际出席人数","缺席人数", "出席率"]
    for e in key_list:
        if e in dataJson:
            if bz_dataJson[e] != dataJson[e]:
                result[e] = {"answer": bz_dataJson[e], 'result': dataJson[e]}
        else:
            result[e] = {"answer": bz_dataJson[e], 'result': "Key不存在"}

    bz_dataJson["参会人详细信息"].sort(key=lambda k: (k.get('姓名', 0)))
    if "参会人详细信息" in dataJson:
        dataJson["参会人详细信息"].sort(key=lambda k: (k.get('姓名', 0)))
        for i in range(len(bz_dataJson["参会人详细信息"])):
            if bz_dataJson["参会人详细信息"][i] != dataJson["参会人详细信息"][i]:
                result["各组出勤情况"] = {"answer": bz_dataJson["参会人详细信息"][i],
                                                  'result': dataJson["参会人详细信息"][i]}
    else:
        result["各组出勤情况"] = {"answer": bz_dataJson["各组出勤情况"], 'result': "Key不存在"}


    if "各组出勤情况" in dataJson:
        count = 1
        result["各组出勤情况"]={}
        for d in bz_dataJson["各组出勤情况"]:
            if d in dataJson["各组出勤情况"]:
                if dataJson["各组出勤情况"][d] != bz_dataJson["各组出勤情况"][d]:
                    result["各组出勤情况"][str(count)]={
                        "answer":bz_dataJson["各组出勤情况"][d],
                        'result':dataJson["各组出勤情况"][d]
                    }
                    count += 1
            else:
                result["各组出勤情况"] = {"answer": d, 'result': d + "不存在"}
    else:
        result["各组出勤情况"] = {"answer": bz_dataJson["各组出勤情况"], 'result': "Key不存在"}

    return result

def compare_summary(i):
    result = {}
    txt = open('answer/bz_summary' + str(i) + '.txt', encoding="utf-8")
    bz_summary = txt.read().replace("\n", " ")
    txt.close()
    txt = open('interview_result/summary' + str(i) + '.txt', encoding="utf-8")
    summary = txt.read().replace("\n", " ")
    txt.close()
    txt = open('answer/bz_data' + str(i) + '.json', encoding="utf-8")
    bz_dataJson = json.load(txt)
    txt.close()
    strDate1 = re.findall(r"部门协调会于(.+)日", bz_summary)[0]
    strDate1 += "日"

    if strDate1 not in summary:
        result["日期"] = {"answer": strDate1, 'result': "匹配不到标准答案内容"}
    compare_list=["主题","实际出席人数","应出席人数","开始时间","结束时间","缺席人数"]
    for e in compare_list:
        if str(bz_dataJson[e]) not in summary:
            result[e] = {"answer": bz_dataJson[e], 'result': "匹配不到标准答案内容"}

    # 比较缺席会议的人员名单
    if "0位" in bz_summary:
        if "0位" in summary or "没" in summary:
            pass
        else:
            result["缺席人数"] = {"answer": 0, 'result': "非0"}
    else:
        bz_absence_info = re.findall(r"其中(.+?)缺席会议", bz_summary)[0]
        absence_info = re.findall(r"其中(.+?)缺席会议", summary)[0]
        if "（" in absence_info:
            bz_absence_info = bz_absence_info.replace("(", "（")
            bz_absence_info = bz_absence_info.replace(")", "）")
        else:
            bz_absence_info = bz_absence_info.replace("（", "(")
            bz_absence_info = bz_absence_info.replace("）", ")")
        bz_absence_info = bz_absence_info[:-4]
        absence_info = absence_info[:-4]
        bz_absence_list = bz_absence_info.split("、")
        for e in bz_absence_list:
            if e not in absence_info or absence_info.count(e) != 1:
                result["缺席名单"] = {"answer": bz_absence_info, 'result': absence_info}

    # 比较迟到早退的人员名单
    bz_late_info = re.findall(r"请会后将会议全程录屏抄送给他们： (.+?)  签到表上部分同事未来得及签名", bz_summary)[0]
    late_info = re.findall(r"请会后将会议全程录屏抄送给他们： (.+) ", summary)[0]
    if "(" in late_info:  # 排除括号的错误
        bz_late_info = bz_late_info.replace("（", "(")
        bz_late_info = bz_late_info.replace("）", ")")
    else:
        bz_late_info = bz_late_info.replace("(", "（")
        bz_late_info = bz_late_info.replace(")", "）")
    bz_late_list = bz_late_info.split(" ")
    for e in bz_late_list:
        if e not in late_info or late_info.count(e) != 1:
            result["迟到早退的人员名单名单"] = {"answer": bz_late_info, 'result': late_info}
            break

    # 比较未签到的人员名单
    bz_buqian_info = str(re.findall(r"未签到同事：(.+)", bz_summary))
    buqian_info = str(re.findall(r"未签到同事：(.+)", summary))
    if bz_buqian_info == "[]":
        if buqian_info != "[]":
            result["未签到的人员名单"] = {"answer": "", 'result': "非空"}
    else:
        bz_buqian_info = bz_buqian_info.replace("[", "")
        bz_buqian_info = bz_buqian_info.replace("]", "")
        bz_buqian_info = bz_buqian_info.replace("'", "")
        bz_buqian_list = bz_buqian_info.split("、")
        for e in bz_buqian_list:
            if e not in buqian_info or buqian_info.count(e) != 1:
                result["未签到的人员名单"] = {"answer": bz_buqian_info, 'result': buqian_info}
                break
    return result


def saveAs_json(path1, path2):
    with open(path1, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    with open(path2, 'w', encoding='utf-8') as f:
        json.dump(load_dict, f, ensure_ascii=False)
    os.remove(path1)


def saveAs_txt(path1, path2):
    with open(path1, "rb") as f:
        f1 = f.read()

    with open(path2, "wb") as fw:
        fw.write(f1)
    os.remove(path1)


if __name__ == '__main__':
    if os.path.exists("compareResult.json"):
        os.remove("compareResult.json")
    shutil.rmtree("interview_result", True)
    Path("interview_result").mkdir(exist_ok=True)

    case_lists = ["testcase/testcase1.xlsx", "testcase/testcase2.xlsx", "testcase/testcase3.xlsx","testcase/testcase4.xlsx", "testcase/testcase5.xlsx"]
    is_run = [True, True, True, True, True]
    compare_result = {}
    # 运行前4个例子
    for i in range(0, 5):
        try:
            iw.run(case_lists[i])
        except Exception as e:
            is_run[i] = False
            print(f'第{str(i + 1)}个case运行失败')
            traceback.print_exc()
        if is_run[i]:
            saveAs_json("data.json", "interview_result/data" + str(i + 1) + ".json")
            saveAs_txt("summary.txt", "interview_result/summary" + str(i + 1) + ".txt")
            compare_result["data" + str(i + 1) + ".json"] = compare_dataJson(i + 1)
            compare_result["summary" + str(i + 1) + ".txt"] = compare_summary(i + 1)
    with open("compareResult.json", "w", encoding='utf-8', ) as f:
        json.dump(compare_result, f, indent=4, sort_keys=True, ensure_ascii=False)
