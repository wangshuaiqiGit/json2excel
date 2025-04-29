import pandas as pd
import json

# 配置输入文件和输出路径（直接修改这里！）
input_json_path = "E:\json2excel\加快建设社会主义文化强国.json"       # 你的 JSON 文件路径
output_excel_path = "E:\json2excel\加快建设社会主义文化强国.xlsx"   # 导出的 Excel 文件名

try:
    # 读取 JSON 文件
    with open(input_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 提取 learningMaterialsStudentResource 数据
    resources = data.get("learningMaterialsStudentResource", [])
    count = len(resources)
    print(f"learningMaterialsStudentResource 中共有 {count} 个元素")
    
    # 转换为 DataFrame 并导出 Excel
    df = pd.DataFrame(resources)
    df.to_excel(output_excel_path, index=False, engine="openpyxl")
    
    print(f"导出成功！文件已保存为：{output_excel_path}")

except FileNotFoundError:
    print(f"错误：JSON 文件 '{input_json_path}' 不存在，请检查路径！")
except json.JSONDecodeError:
    print("错误：JSON 文件格式不正确，请检查内容！")
except Exception as e:
    print(f"未知错误：{str(e)}")