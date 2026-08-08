"""A minimal paper outline generator for PaperWritingAgent.

This script is an early Python prototype of the project. It takes a research
topic from user input, identifies a rough research direction, and prints a
structured academic paper outline.
"""


def detect_research_direction(topic):
    """Detect a rough research direction based on keywords in the topic."""
    topic_lower = topic.lower()

    if "cad" in topic_lower or "3d" in topic_lower or "机械" in topic:
        return "LLM + CAD / 3D 智能设计方向"

    if "agent" in topic_lower or "智能体" in topic or "多智能体" in topic:
        return "Agent / 多智能体方向"

    if "引用" in topic or "citation" in topic_lower or "reference" in topic_lower:
        return "论文引用检查方向"

    if "文献" in topic or "literature" in topic_lower:
        return "文献检索与综述整理方向"

    return "通用论文写作辅助方向"


def generate_title_suggestions(topic, direction):
    """Return three possible paper titles for the given topic."""
    return [
        f"{topic}方法研究",
        f"面向{direction}的论文写作辅助流程设计",
        f"基于智能体思想的{topic}研究规划原型设计",
    ]


def generate_literature_directions(direction):
    """Return recommended literature search directions."""
    if "CAD" in direction or "3D" in direction:
        return [
            "Text-to-CAD generation",
            "LLM for CAD code generation",
            "Multi-agent CAD design",
            "Tool-using LLM for engineering design",
            "Parametric 3D model generation",
        ]

    if "Agent" in direction or "多智能体" in direction:
        return [
            "ReAct agent framework",
            "Plan-and-Solve prompting",
            "Multi-agent collaboration",
            "Tool-using agents",
            "Agent evaluation methods",
        ]

    if "引用" in direction:
        return [
            "Citation checking",
            "Reference matching",
            "Academic writing tools",
            "Bibliography management",
            "Retrieval-augmented generation for citation support",
        ]

    if "文献" in direction:
        return [
            "Literature retrieval",
            "Research paper summarization",
            "Academic survey generation",
            "Keyword extraction",
            "Paper recommendation systems",
        ]

    return [
        "Academic writing assistance",
        "Paper outline generation",
        "Research planning",
        "LLM-assisted writing",
        "Agent-based workflow design",
    ]


def generate_outline(topic):
    """Generate a structured paper outline for the given topic."""
    direction = detect_research_direction(topic)
    titles = generate_title_suggestions(topic, direction)
    literature_directions = generate_literature_directions(direction)

    sections = [
        {
            "name": "第一章 引言",
            "goal": "说明研究背景、问题来源、研究意义和本文主要工作。",
        },
        {
            "name": "第二章 相关工作",
            "goal": "梳理已有研究，并总结不同方法之间的联系与不足。",
        },
        {
            "name": "第三章 方法设计",
            "goal": "介绍围绕研究主题设计的总体流程、核心模块和实现思路。",
        },
        {
            "name": "第四章 案例分析或实验设计",
            "goal": "结合具体案例或实验方案，说明方法的可行性和应用价值。",
        },
        {
            "name": "第五章 问题与挑战",
            "goal": "分析当前方法存在的局限，以及后续需要改进的方向。",
        },
        {
            "name": "第六章 总结与展望",
            "goal": "总结全文内容，并提出未来可能的研究方向。",
        },
    ]

    output = []
    output.append("=" * 60)
    output.append("PaperWritingAgent: 论文大纲生成原型 v2")
    output.append("=" * 60)
    output.append(f"研究主题：{topic}")
    output.append(f"识别方向：{direction}")
    output.append("")

    output.append("一、可能的论文题目")
    for index, title in enumerate(titles, start=1):
        output.append(f"{index}. {title}")
    output.append("")

    output.append("二、论文整体结构与写作目标")
    for section in sections:
        output.append(f"- {section['name']}")
        output.append(f"  写作目标：{section['goal']}")
    output.append("")

    output.append("三、建议补充检索的文献方向")
    for item in literature_directions:
        output.append(f"- {item}")
    output.append("")

    output.append("四、后续写作建议")
    output.append("- 先缩小研究主题，避免选题过大。")
    output.append("- 优先阅读摘要、引言、方法图和结论。")
    output.append("- 将文献按研究方向分类，再整理相关工作。")
    output.append("- 当前结果仅作为论文规划参考，需要研究者继续修改和补充。")

    return "\n".join(output)


def main():
    """Read a topic from the terminal and print the generated outline."""
    topic = input("请输入研究主题：").strip()

    if not topic:
        topic = "LLM 辅助 CAD 智能设计"
        print("未输入研究主题，使用默认主题：LLM 辅助 CAD 智能设计\n")

    outline = generate_outline(topic)
    print(outline)


if __name__ == "__main__":
    main()
