def read(input_: str, cast: type = str) -> list:
    if len(input_) == 0:
        return []
    return list(map(cast, input_.split()))


def read_line_by_line(input_: str, cast: type = str) -> list:
    if len(input_) == 0:
        return []
    return list(map(cast, input_.split('\n')))


def read_paragraph_by_paragraph(input_: str, cast: type = str) -> list:
    if len(input_) == 0:
        return []
    return list(map(cast, input_.split('\n\n')))


def read_character_matrix(input_: str) -> list:
    if len(input_) == 0:
        return []
    return list(list(row) for row in input_.split('\n'))
