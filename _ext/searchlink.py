from urllib.parse import quote

from docutils import nodes
from sphinx.util.docutils import SphinxRole
from sphinx.util import logging

logger = logging.getLogger(__name__)


class SearchLinkRole(SphinxRole):
    """A Sphinx role that generates search links.

    When used in reStructuredText, this role creates a clickable
    search link that directs users to the Sphinx search results page
    with the role's text as the search query. The link includes a
    magnifying glass emoji and is styled with the CSS class
    'search-link'.

    Search links are only rendered in HTML output; other formats will
    emit a warning and return the input text unchanged.

    Example usage in reST:
        :searchlink:`POSITIONS_ABS`
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Generate search link from role directive."""
        if "html" not in self.env.app.tags:
            logger.warning(
                "Search links are only supported in HTML output.",
                location=self.get_source_info(),
            )

            return [nodes.Text(self.text)], []

        url = f"/search.html?q={quote(self.text)}"
        html = f'<a href="{url}" class="search-link">🔍︎ {self.text}</a>'

        return [nodes.raw("", html, format="html")], []


def setup(app):
    """Register the `searchlink` role with the Sphinx application."""
    app.add_role("searchlink", SearchLinkRole())
    return {"version": "0.1"}
