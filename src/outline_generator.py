"""A minimal paper outline generator for PaperWritingAgent.

This script is the first Python prototype of the project. It takes a research
topic from user input and prints a fixed but reusable academic paper outline.
"""


def generate_title_suggestions(topic):
    """Return three possible paper titles for the given topic."""
    return [
        f"{topic}方法研究",
        f"面向{topic}的论文写作辅助流程设计",
        f"基于智能体思想的{topic}研究规划原型设计",
    ]


def generate_outline(topic):
    """Generate a structured paper outline for the given topic."""
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

    titles = generate_title_suggestions(topic)

    output = []
    output.append("=" * 60)
    output.append("PaperWritingAgent: 论文大纲生成原型")
    output.append("=" * 60)
    output.append(f"研究主题：{topic}")
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
    output.append(f"- {topic} 的基础概念和应用背景")
    output.append(f"- {topic} 相关的最新研究论文")
    output.append("- Agent、工具调用、任务规划等相关方法")
    output.append("- 与该主题相关的案例、实验或应用场景")
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
