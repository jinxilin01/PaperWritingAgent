"""Simple tests for PaperWritingAgent outline generator.

These tests check whether different research topics can be mapped to different
rough research directions.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

from outline_generator import detect_research_direction


def test_cad_direction():
    topic = "LLM 辅助 CAD 智能设计"
    direction = detect_research_direction(topic)
    assert direction == "LLM + CAD / 3D 智能设计方向"


def test_agent_direction():
    topic = "多智能体论文写作辅助"
    direction = detect_research_direction(topic)
    assert direction == "Agent / 多智能体方向"


def test_citation_direction():
    topic = "论文引用检查工具"
    direction = detect_research_direction(topic)
    assert direction == "论文引用检查方向"


def test_literature_direction():
    topic = "文献综述自动整理"
    direction = detect_research_direction(topic)
    assert direction == "文献检索与综述整理方向"


def test_general_direction():
    topic = "科研写作流程规划"
    direction = detect_research_direction(topic)
    assert direction == "通用论文写作辅助方向"


if __name__ == "__main__":
    test_cad_direction()
    test_agent_direction()
    test_citation_direction()
    test_literature_direction()
    test_general_direction()
    print("All tests passed.")
