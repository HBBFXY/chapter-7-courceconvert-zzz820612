import keyword

reserved_words = set(keyword.kwlist)

def convert_python_file(source_file, target_file):
    """
    读取Python源文件，将除保留字外的小写字母转换为大写字母
    """
    try:
        # 读取源文件
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("原始文件内容:")
        print(content)
        print("\n" + "="*50 + "\n")
        
        # 转换处理
        converted_content = convert_content(content)
        
        # 写入目标文件
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(converted_content)
        
        print("转换后文件内容:")
        print(converted_content)
        print(f"\n转换完成！结果已保存到: {target_file}")
        
    except FileNotFoundError:
        print(f"错误：找不到文件 {source_file}")
    except Exception as e:
        print(f"处理文件时出错: {e}")

def convert_content(content):
    """
    转换文件内容，保留关键字不变，其他小写字母转大写
    """
    import re
    
    lines = content.split('\n')
    converted_lines = []
    
    for line in lines:
        converted_line = convert_line(line)
        converted_lines.append(converted_line)
    
    return '\n'.join(converted_lines)

def convert_line(line):
    """
    转换单行内容
    """
    import re
    
    # 用于存储转换结果
    result = []
    # 当前位置
    pos = 0
    
    while pos < len(line):
        # 检查当前位置是否是字母开头
        if line[pos].isalpha():
            # 提取完整的单词
            word_end = pos
            while word_end < len(line) and line[word_end].isalpha():
                word_end += 1
            
            word = line[pos:word_end]
            
            # 检查是否是保留字
            if word in reserved_words:
                result.append(word)  # 保留关键字不变
            else:
                result.append(word.upper())  # 非关键字转大写
            
            pos = word_end
        else:
            # 非字母字符直接保留
            result.append(line[pos])
            pos += 1
    
    return ''.join(result)

# 主程序
if __name__ == "__main__":
    source_file = "random_int.py"
    target_file = "converted_random_int.py"
    
    convert_python_file(source_file, target_file)
