"""子 agent 子系统：定义解析、加载、工具白名单、fork、trace 与后台任务管理。"""
from xacode.agents.parser import AgentDef, AgentParseError, parse_agent_file
from xacode.agents.loader import AgentLoader
from xacode.agents.tool_filter import resolve_agent_tools
from xacode.agents.fork import build_forked_messages, ForkError
from xacode.agents.trace import TraceManager, TraceNode
from xacode.agents.task_manager import TaskManager, BackgroundTask
from xacode.agents.notification import format_task_notification, inject_task_notifications


__all__ = [
    "AgentDef",
    "AgentParseError",
    "parse_agent_file",
    "AgentLoader",
    "resolve_agent_tools",
    "build_forked_messages",
    "ForkError",
    "TraceManager",
    "TraceNode",
    "TaskManager",
    "BackgroundTask",
    "format_task_notification",
    "inject_task_notifications",
]
