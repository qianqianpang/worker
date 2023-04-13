import PyPDF2

# 读取PDF文件
with open('5.复方板蓝根使用说明.pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    output = ""

    # 遍历每一页并在开头添加字符串
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        content = page.extract_text().split('\n')
        con = ''
        for c in content:
            if c.strip() != '':
                con += c
        output += "#{}\n{}\n".format(i + 1, con)

    print(output)
