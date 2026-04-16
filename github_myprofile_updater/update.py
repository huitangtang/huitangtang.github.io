def load_section(filepath):
    """安全读取并清理章节内容"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"⚠️  Warning: {filepath} not found, skipping...")
        return ""

def generate_readme(output_path='README.md'):
    """聚合各章节内容生成 README.md"""
    base_dir = '../_pages/includes'
    
    # 定义章节配置：(标题前缀，文件路径)
    # 注：GitHub Actions 运行于 Linux 环境，直接使用 '/' 拼接路径即可
    sections = [
        ('', base_dir + '/intro.md'),
        ('##', base_dir + '/homepage.md'),
        # ('##', base_dir + '/news.md'),
        # ('##', base_dir + '/pub_short.md'),  # 按需启用
    ]
    
    # 构建内容
    content_parts = ['## Hi there!']  # 固定 header
    for prefix, filepath in sections:
        content = load_section(filepath)
        if content:  # 仅添加非空章节
            content_parts.extend(['', prefix, content])
    
    # 统一写入
    full_content = '\n'.join(content_parts) + '\n'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ README.md generated successfully ({len(full_content)} chars)")

if __name__ == '__main__':
    generate_readme()
