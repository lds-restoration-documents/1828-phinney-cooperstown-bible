"""Helper for scripts that read phinney-bible-1828.md: remove its YAML frontmatter."""


def strip_frontmatter(t):
    """Remove the YAML frontmatter block that compile_markdown.py puts at the top of phinney-bible-1828.md."""
    if t.startswith('---\n'):
        end = t.find('\n---\n', 4)
        if end != -1:
            return t[end + 5:].lstrip('\n')
    return t
