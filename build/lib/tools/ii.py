from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re

class CustomStyleExtension(Extension):
    def extendMarkdown(self, md):
        # 使用 CustomStylePreprocessor 來處理 Markdown 中的 "!> ... !>"
        md.preprocessors.register(CustomStylePreprocessor(md), 'custom_style_preprocessor', 25)

class CustomStylePreprocessor(Preprocessor):
    # 定義正則表達式來匹配 "!>" 和 "!>" 之間的內容，且這些標記在單獨的行中
    RE = re.compile(r'^\!\>(.*?)\!\>$', re.DOTALL | re.MULTILINE)

    def run(self, lines):
        new_lines = []
        inside_custom_block = False
        custom_block_content = []

        for line in lines:
            if line.strip() == "!>":  # 如果是開頭或結尾的 "!>"
                if inside_custom_block:
                    # 如果在自定義塊內，則結束塊並生成 HTML
                    new_lines.append(f'<div class="i">{"<br>".join(custom_block_content)}</div>')
                    custom_block_content = []
                    inside_custom_block = False
                else:
                    # 開始自定義塊
                    inside_custom_block = True
            elif inside_custom_block:
                # 如果在自定義塊內，收集內容
                custom_block_content.append(line.strip())
            else:
                # 非自定義塊內容，直接添加
                new_lines.append(line)

        return new_lines

# 創建一個函數來載入這個擴展
def makeExtension(**kwargs):
    return CustomStyleExtension(**kwargs)
