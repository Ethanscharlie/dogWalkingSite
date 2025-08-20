import os
import shutil
import re
from src.controller.calendar import get_info_for_calendar

BUILD_DIR = "docs"
EVAL_REGEX_WITH_SYMBOLS = r'%%\s*.*?\s*%%'

def main():
    make_build_dir()
    copy_res_folder()

    for page_file in os.listdir("pages"):
        page_html = get_html_from_file(f"pages/{page_file}")

        page_html = apply_navbar(page_html)
        page_html = apply_calendar(page_html)

        write_html_to_file(page_html, page_file)

def apply_calendar(html: str) -> str:
    return html.replace(
        "{{ CALENDAR }}",
        '\n'.join([
            get_html_from_file("templates/calendar_day.html").replace("{{ DAY_INFO }}", day_string)
            for day_string in get_info_for_calendar()
        ])
    )

def apply_navbar(html: str) -> str:
    return html.replace(
        "{{ NAVBAR }}",
        get_html_from_file("templates/nav.html")
    )

def get_html_from_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read()

def write_html_to_file(html: str, file: str) -> None:
    with open(f"{BUILD_DIR}/{file}", "w+") as f:
        f.write(html)

def copy_res_folder() -> None:
    shutil.copytree("res", f"{BUILD_DIR}/res")

def make_build_dir() -> None:
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)

    os.makedirs(BUILD_DIR)

def run_evals_on_html(html: str) -> str:
    evals = re.findall(EVAL_REGEX_WITH_SYMBOLS, html)
    for expression_with_symbols in evals:
        expression = expression_with_symbols.replace("%%", "")

        html = html.replace(
            expression_with_symbols,
            str(eval(expression))
        )
    
    return html

if __name__ == '__main__':
    main()
