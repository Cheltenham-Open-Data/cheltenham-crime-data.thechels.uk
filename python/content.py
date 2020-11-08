
import json
import pathlib
import os
import re

def replace_chunk(content, marker, chunk):
    replacer = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return replacer.sub(chunk, content)

rows = ""
# output
if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()
    with open( root / "data/AA3_all_crime.json", 'r+') as filehandle:
        crimes = json.load(filehandle)
        for crime in crimes:
            rows += f"\n<tr><td>{crime['id']}</td><td>{crime['category']}</td><td>{crime['month']}</td><td>{crime['location']['street']['name']}</td></tr>"
index_page = root / "index.html"
index_contents = index_page.open().read()
final_output = replace_chunk(index_contents, "table_marker", f"{rows}")
index_page.open("w").write(final_output)