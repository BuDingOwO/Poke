import time

from nonebot import get_driver

from .config import Config

global_config = get_driver().config
config = Config.parse_obj(global_config)

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Event

__help_plugin_name__ = '戳一戳,rua一rua'
__help_version__ = '1.0'

__des__ = "戳一戳"
__cmd__ = f"""
指令前缀 + 指令
当前配置的指令前缀为: {" ".join(list(get_driver().config.command_start))}
""".strip()
__list__ = """

戳我 | 连续戳你自己 5 次，每次间隔 1s
戳@qq | 连续戳 被艾特到的兽兽 5次，每次间隔1s

""".strip()
__usage__ = f"{__des__}\n\nUsage:\n{__cmd__}\n\nCommandList:[指令名 | 指令介绍]\n{__list__}"

matcher = on_command("戳我", priority=5, )


@matcher.handle()
async def poke(event: Event, matcher: Matcher):
    user_id = event.get_user_id()
    await matcher.send('[CQ:at,qq=' + user_id + ']' + '[CQ:face,id=28]' + '[CQ:face,id=109]' +
                       '[CQ:face,id=183]' + "rua死你！！！")
    count = 0
    while count <= 8:
        await matcher.send('[CQ:poke,qq=' + user_id + ']')
        count = count + 2
        time.sleep(1)

    await matcher.finish('[CQ:poke,qq=' + user_id + ']')
