from pathlib import Path
from typing import Literal

from vet.imbue_core.agents.agent_api.data_types import AgentOptions


class OpenCodeOptions(AgentOptions):
    object_type: Literal["OpenCodeOptions"] = "OpenCodeOptions"

    model: str | None = None
    cli_path: Path | None = None
    is_cached: bool = False
