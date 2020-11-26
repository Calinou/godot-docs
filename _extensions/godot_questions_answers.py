"""
    godot_questions_answers
    ~~~~~~~~~~~~~~~~~~~~~~~
    Sphinx extension that adds a ``.. questions-answers:: tag1 tag2 ...`` directive.
    This displays a link to view and ask questions on the Godot Questions & Answers platform.
    This role should be added at the bottom of relevant pages.
    :copyright: Copyright 2020 by The Godot Engine Community
    :license: MIT
"""

from docutils.parsers.rst import directives, Directive
from docutils import nodes

# See <https://github.com/coldfix/sphinx-code-tabs/blob/main/sphinx_code_tabs/__init__.py>
# for setup code inspiration.

# The URL to the questions & answers website.
GODOT_QA_URL = "https://godotengine.org/qa"


class QuestionsAnswersNode(nodes.General, nodes.Element):
    def __init__(self, tags):
        """
        :param str tags: Tags to search for in the Q&A.
        """
        super(QuestionsAnswersNode, self).__init__()
        self.tags = tags[0]

    @staticmethod
    def visit(spht, node):
        """Append opening tags to document body list."""
        spht.body.append(
            spht.starttag(node, "div", "", **{"class": "questions-answers"})
        )

        spht.body.append(spht.starttag(node, "h2", "User questions"))
        spht.body.append("</h2>")

        spht.body.append(
            spht.starttag(
                node,
                "iframe",
                "",
                title="Hello world",
                width=720,
                height=400,
                src="%s/search?q=%s" % (GODOT_QA_URL, node.tags),
                **{"class": "questions-answers-iframe"},
            )
        )
        spht.body.append("</iframe>")

        spht.body.append("<br>")

        spht.body.append(
            spht.starttag(
                node,
                "a",
                "Ask a question about “<strong>%s</strong>”" % node.tags,
                href="%s/ask?tags=%s" % (GODOT_QA_URL, node.tags),
                target="_blank",
                rel="noopener",
                title="Ask a question on the Godot Q&A platform (opens in a new tab)",
                **{"class": "questions-answers-btn"},
            )
        )
        spht.body.append("</a>")

    @staticmethod
    def depart(spht, node):
        """Append closing tags to document body list."""
        spht.body.append("</div>")
        # Separate the User questions box from th Previous and Next page buttons.
        spht.body.append("<hr>")


class QuestionsAnswers(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        return [QuestionsAnswersNode(self.content)]


def setup(app):
    app.add_directive("questions-answers", QuestionsAnswers)
    app.add_node(
        QuestionsAnswersNode,
        html=(QuestionsAnswersNode.visit, QuestionsAnswersNode.depart),
    )

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
