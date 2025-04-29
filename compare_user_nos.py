import json

def get_user_nos(json_path):
    """从 JSON 文件中提取所有学号（userNo）"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        resources = data.get("learningMaterialsStudentResource", [])
        user_nos = {item["userNo"] for item in resources if "userNo" in item}
        return user_nos
    except Exception as e:
        print(f"读取文件 {json_path} 出错: {str(e)}")
        return set()

def main():
    # 配置两个 JSON 文件路径
    file1 = "E:\json2excel\加快建设社会主义文化强国.json"
    file2 = "E:\json2excel\加快建设社会主义文化强国-read.json"
    
    # 提取学号集合
    user_nos1 = get_user_nos(file1)
    user_nos2 = get_user_nos(file2)
    
    # 计算交集
    common_nos = user_nos1 & user_nos2
    
    # 输出结果
    print(f"文件1中共有 {len(user_nos1)} 个学号")
    print(f"文件2中共有 {len(user_nos2)} 个学号")
    print("\n同时存在的学号 ({len(common_nos)} 个):")
    for no in sorted(common_nos):
        print(f"- {no}")

if __name__ == "__main__":
    main()