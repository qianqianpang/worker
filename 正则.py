import re

text = "哈哈哈哈2022年1-9月还可考虑"
time = ''
if re.search(r"(20\d{2}年\d{1}-\d{1}月)", text):
    temp = re.search(r"(20\d{2}年\d{1}-\d{1}月)", text).group(0)
    time += temp[0:5]
    time += temp[7]
    time = time.replace('年', '-')
elif re.search(r"(20\d{2}年\d{1,2}月\d{1,2}日至20\d{2}年\d{1,2}月\d{1,2}日)", text):
    temp = re.search(r"(20\d{2}年\d{1,2}月\d{1,2}日至20\d{2}年\d{1,2}月\d{1,2}日)", text).group(0)
    temp = temp[temp.find('至') + 1:-1]
    time += temp[0:temp.find('月')].replace('年', '-')
elif re.search(r"(20\d{2}-\d{1,2})", text):
    time += re.search(r"(20\d{2}-\d{1,2})", text).group(0)
elif re.search(r"(20\d{2}年\d{1,2})", text):
    time += re.search(r"(20\d{2}年\d{1,2})", text).group(0).replace('年', '-')
else:
    time = ''
print(time)
