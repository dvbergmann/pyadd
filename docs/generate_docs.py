from pathlib import Path
import mkdocs_gen_files
from setuptools import find_packages

nav = mkdocs_gen_files.Nav()
package = find_packages()[0]
DOCS_OUTPUT_DIR = Path().cwd() / 'docs' / 'reference'

print('RUNNING GEN FILES')

for path in sorted(Path(package).rglob("*py")):
    module_path = path.relative_to(package).with_suffix("")
    doc_path = path.relative_to(package).with_suffix(".md")
    full_doc_path = DOCS_OUTPUT_DIR / doc_path
    print(full_doc_path)

    parts = tuple(module_path.parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1] == "__main__":
        continue

    if parts:
        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            ident = ".".join(parts)
            fd.write(f"::: {package}.{ident}")
            print(fd)

        mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open(f"{DOCS_OUTPUT_DIR}/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())