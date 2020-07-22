from SublimeLinter.lint import Linter


class Selene(Linter):
    cmd = ('selene', '${file}', '--display-style=quiet')
    regex = (
        r'.+:(?P<line>\d+):(?P<col>\d+): '
        r'(?:warning\[(?P<warning>.+)|error\[(?P<error>.+))\]: '
        r'(?P<message>.+)'
    )
    tempfile_suffix = '-'
    defaults = {
        'selector': 'source.lua'
    }
