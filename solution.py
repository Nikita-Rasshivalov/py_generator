from string import Template

def triple_quote_repr(s: str) -> str:
    escaped = s.replace('\\', '\\\\').replace("'''", "\\'''")
    template = Template("'''$content'''")
    return template.substitute(content=escaped)

def escape_for_js_template_literal(s: str) -> str:
    return s.replace('\\', '\\\\').replace('`', '\\`')

py_code_template = '''
from string import Template

def triple_quote_repr(s: str) -> str:
    escaped = s.replace('\\\\', '\\\\\\\\').replace("\'''", "\\\\\'''")
    template = Template("\'''$content\'''")
    return template.substitute(content=escaped)

def escape_for_js_template_literal(s: str) -> str:
    return s.replace('\\\\', '\\\\\\\\').replace('`', '\\\\`')

py_code_template = {body_repr}

full_py_code = py_code_template.format(body_repr=triple_quote_repr(py_code_template))

escaped_for_backticks = escape_for_js_template_literal(full_py_code)

js_code_template = f"""var py_code = `{{escaped_for_backticks.strip()}}`;
console.log(py_code);"""

print(js_code_template)'''

full_py_code = py_code_template.format(body_repr=triple_quote_repr(py_code_template))

escaped_for_backticks = escape_for_js_template_literal(full_py_code)

js_code_template = f"""var py_code = `{escaped_for_backticks.strip()}`;
console.log(py_code);"""

print(js_code_template)