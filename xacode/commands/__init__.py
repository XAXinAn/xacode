"""Slash Command 子系统：命令注册表、解析与补全、用户自定义命令加载。"""
from xacode.commands.loader import load_user_commands
from xacode.commands.parser import complete, parse_command
from xacode.commands.registry import (
    Command,
    CommandContext,
    CommandHandler,
    CommandRegistry,
    CommandType,
    UIController,
)


__all__ = [
    "Command",
    "CommandContext",
    "CommandHandler",
    "CommandRegistry",
    "CommandType",
    "UIController",
    "complete",
    "load_user_commands",
    "parse_command",
]
