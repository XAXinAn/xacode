"""多人协作（Team）子系统的对外导出。"""
from xacode.teams.mailbox import Mailbox, MailboxMessage, create_message
from xacode.teams.models import (
    AgentTeam,
    BackendType,
    TeammateInfo,
    resolve_team_dir,
    unique_team_name,
)
from xacode.teams.progress import TeammateProgress, ToolActivity
from xacode.teams.registry import AgentNameRegistry
from xacode.teams.shared_task import SharedTask, SharedTaskStore


__all__ = [
    "AgentTeam",
    "AgentNameRegistry",
    "BackendType",
    "Mailbox",
    "MailboxMessage",
    "SharedTask",
    "SharedTaskStore",
    "TeammateInfo",
    "TeammateProgress",
    "ToolActivity",
    "create_message",
    "resolve_team_dir",
    "unique_team_name",
]
