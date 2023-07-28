from pathlib import Path

code_path = Path(__file__).parent / "nonebot_plugin_analysenumber" / "__init__.py"

head = """from nonebot import on_fullmatch
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me

__plugin_meta__ = PluginMetadata(
    name="分析数字",
    description="分析数字属性",
    usage="请给出一个不多于5位的正整数",
    type="application",
    homepage="https://github.com/A-kirami/nonebot-plugin-analysenumber",
)
"""

template = """
num{num} = on_fullmatch("{num}", rule=to_me())


@num{num}.handle()
async def num_{num}() -> None:
    await num{num}.finish("{msg}")
"""

digit = ("个", "十", "百", "千", "万", "十万", "百万", "千万", "亿", "十亿")

codes = [head]
for i in range(1, 100000):
    num_str = str(i)
    num_len = len(num_str)
    inv_num = num_str[::-1]
    texts = [f"是{num_len}位数"]
    texts.extend(f"{digit[i]}位是{inv_num[i]}" for i in range(num_len))
    texts.append(f"倒过来是: {inv_num}")
    codes.append(template.format(num=num_str, msg="\\n".join(texts)))

code_path.write_text("\n".join(codes), encoding="utf-8")
