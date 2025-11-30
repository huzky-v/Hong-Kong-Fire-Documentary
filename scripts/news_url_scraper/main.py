"""
Extract latest news url from sites into markdown
"""

import glob
import importlib
import os


def main():
    """"""
    scrapers = [importlib.import_module(i.replace("/", ".").replace(".py", "")) for i in glob.glob("scrapers/*.py")]
    [save_as_markdown(i[0], i[1]) for i in [i.scrape() for i in scrapers]]


def save_as_markdown(title: str, content: list[tuple[str, str, str]]) -> None:
    """
    Format string and save as markdown.

    Args:
            title: title of the md file
            content: A list of tuple containing (date, article title, url)

    """

    if not os.path.exists("./output"):
        os.mkdir("./output")
    if not os.path.isdir("./output"):
        if input(f"remove {os.path.abspath('./output')}? [Y/n]") == "Y":
            os.remove("./output")
            os.mkdir("./output")

    pre_date: str = sorted(content)[0][0]
    md: str = ""
    md += f"# {title}\n\n"
    md += f"### {pre_date}\n"
    md += "| links |\n| --- |\n"

    for i in sorted(content):
        if pre_date != i[0]:
            pre_date = i[0]
            md += f"### {i[0]}"
            md += "\n| links |\n| --- |\n"
        md += f"| [{i[1]}]({i[2]}) |\n"

    with open(f"./output/{title}.md", "w") as f:
        f.write(md)


if __name__ == "__main__":
    main()
