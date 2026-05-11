"""
generate_data_architecture_audit.py
-----------------------------------
Script này đọc tất cả các file .md trong thư mục 'tables/' và 'context/05_TABLE_DESC.md' 
để tổng hợp các mối quan hệ ảo (Virtual Relations) dựa trên mô tả của từng cột,
từ đó sinh ra file Data Architecture Audit (relations.md).
"""

import os
import re
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def parse_table_descriptions(table_desc_path):
    table_desc_map = {}
    if not os.path.exists(table_desc_path):
        return table_desc_map
        
    with open(table_desc_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for line in content.split('\n'):
        if line.startswith('|') and 'Tên Bảng' not in line and '---' not in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 4:
                nhom = parts[1]
                table = parts[2].replace('`', '')
                desc = parts[3]
                if table:
                    table_desc_map[table.lower()] = desc
    return table_desc_map

def extract_virtual_relations(tables_dir, allowed_tables):
    relations = []
    if not os.path.exists(tables_dir):
        return relations
        
    for fname in os.listdir(tables_dir):
        if not fname.endswith('.md'):
            continue
            
        table_name = fname.replace('.md', '')
        if table_name.lower() not in allowed_tables:
            continue
            
        with open(os.path.join(tables_dir, fname), 'r', encoding='utf-8') as f:
            content = f.read()
            
        in_columns = False
        for line in content.split('\n'):
            if line.startswith('## Columns'):
                in_columns = True
                continue
            if line.startswith('## Indexes') or line.startswith('---'):
                if in_columns and line.startswith('---'):
                    pass # might just be a separator
                else:
                    in_columns = False
                
            if in_columns and line.startswith('| `'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 4:
                    col_name = parts[1].replace('`', '')
                    col_desc = parts[3]
                    
                    # Heuristic to find references (liên kết)
                    # For example: "Tham chiếu bảng ABC" or "Chứa ID của bảng XYZ"
                    # We just record any column that has a description.
                    if col_desc and col_desc != '':
                        relations.append({
                            'table': table_name,
                            'column': col_name,
                            'desc': col_desc
                        })
    return relations

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    tables_dir = os.path.join(base_dir, 'tables')
    table_desc_path = os.path.join(base_dir, 'context', '05_TABLE_DESC.md')
    out_path = os.path.join(base_dir, 'context', '06_DATA_ARCHITECTURE.md')
    
    print("📋 Đang đọc danh mục ý nghĩa các bảng từ 05_TABLE_DESC.md...")
    table_desc_map = parse_table_descriptions(table_desc_path)
    
    print("📋 Đang quét thư mục tables/ để tìm các mối quan hệ ảo (mô tả cột)...")
    relations = extract_virtual_relations(tables_dir, table_desc_map.keys())
    
    lines = [
        "# 06 — Data Architecture Audit (Relations & References)",
        "",
        "> Document này ghi nhận các mối quan hệ logic (Virtual Relations) giữa các bảng trong hệ thống.",
        "> Hệ thống không sử dụng Foreign Keys cứng, các liên kết được suy luận từ mô tả (Description) của cột.",
        "",
        "## 1. Các Liên Kết Logic (Dựa trên mô tả cột)",
        "",
        "| Bảng (Table) | Cột (Column) | Mô tả (Mối quan hệ) |",
        "|--------------|--------------|---------------------|"
    ]
    
    if relations:
        for r in relations:
            lines.append(f"| `{r['table']}` | `{r['column']}` | {r['desc']} |")
    else:
        lines.append("| *(Không tìm thấy)* | *(Trống)* | *(Chưa có mô tả nào trong thư mục tables/)* |")
        
    lines.extend([
        "",
        "---",
        "",
        "## 2. Gợi ý Suy luận Liên kết Tự động (Heuristic Relations)",
        "",
        "> AI tự động suy luận liên kết nếu cột có đuôi `ID`, `_ID` hoặc `REF` trùng với tên bảng khác.",
        "",
        "| Bảng Hiện Tại | Cột | Dự đoán Tham Chiếu (Bảng Đích) |",
        "|---------------|-----|--------------------------------|"
    ])
    
    # Auto-infer based on naming convention
    all_tables = [f.replace('.md', '').lower() for f in os.listdir(tables_dir) if f.endswith('.md')]
    all_tables_case = {f.replace('.md', '').lower(): f.replace('.md', '') for f in os.listdir(tables_dir) if f.endswith('.md')}
    
    inferred_count = 0
    for fname in os.listdir(tables_dir):
        if not fname.endswith('.md'):
            continue
        table_name = fname.replace('.md', '')
        if table_name.lower() not in table_desc_map:
            continue
            
        with open(os.path.join(tables_dir, fname), 'r', encoding='utf-8') as f:
            for line in f.read().split('\n'):
                if line.startswith('| `'):
                    parts = line.split('|')
                    if len(parts) >= 2:
                        col_name = parts[1].replace('`', '').strip()
                        
                        # Guess ref table
                        ref_tbl = None
                        if col_name.endswith('ID') and len(col_name) > 2 and col_name != table_name + 'ID':
                            possible = col_name[:-2].lower()
                            if possible in table_desc_map:
                                ref_tbl = all_tables_case.get(possible)
                        elif col_name.endswith('REF'):
                            possible = col_name[:-3].lower()
                            if possible in table_desc_map:
                                ref_tbl = all_tables_case.get(possible)
                                
                        if ref_tbl:
                            lines.append(f"| `{table_name}` | `{col_name}` | ──→ `{ref_tbl}` |")
                            inferred_count += 1
                            
    if inferred_count == 0:
        lines.append("| *(Không)* | *(Không)* | *(Không suy luận được)* |")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    print(f"✅ Hoàn tất! Đã tạo file Data Architecture Audit tại: {out_path}")

if __name__ == '__main__':
    main()
