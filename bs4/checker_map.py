CHECKER_MAP = {
    '#': lambda tag, tok: tag.get('id', None) == tok.split('#', 1)[1],
    '.': lambda tag, tok: set(tok.split('.', 1)[1].split('.')).issubset(tag.get('class', []))
}
