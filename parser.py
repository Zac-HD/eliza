#! python3
"""
A simple parser for ELIZA MAD-SLIP script files (an ancient LISP).

Inspired by http://norvig.com/lispy.html - "how hard can it be?".
"""

from collections import deque
from pprint import pprint
import re


TOKEN_PATTERNS = dict(
    paren_open=r"\(",
    paren_close=r"\)",
    equals=r"=",
    subs_priority=r"\d+",
    star=r"\*",
    word=r"[=/]?[\-\'A-Z]+[,\.]?",  # TODO: split logically distinct cases
)


def read_from_tokens(tokens: deque) -> list:
    """Read one token or branch from `tokens`, recursively."""
    token = tokens.popleft()
    if token == "(":
        subtree = []
        while tokens and tokens[0] != ")":
            subtree.append(read_from_tokens(tokens))
        if tokens:
            tokens.popleft()  # pop off ")"
        return subtree
    assert token != ")"
    return token


def tree_to_string(tree: list, depth: int = 0) -> str:
    """Convert a (sub)tree to a string."""
    space = 4 * depth * " "
    if not isinstance(tree, list):
        return space + tree
    elif not any(isinstance(tok, list) for tok in tree):
        return f"    ({' '.join(tree)})"
    tokens = [tree_to_string(elem, depth + 1).strip() for elem in tree]
    ws = "\n" + space
    return f"    ({ws}{ws.join(tokens)}{ws[:-4]})"


class AST:
    def __init__(self, tokens):
        """Turn a flat list of tokens into an AST."""
        self.tokens = tokens
        self.tree = read_from_tokens(deque(["("] + tokens + [")"]))
        while isinstance(self.tree, list) and len(self.tree) == 1:
            self.tree = self.tree[0]

    @classmethod
    def from_file(cls, fname):
        """Read an AST from the named file."""
        with open(fname) as f:
            return cls.from_string(f.read())

    @classmethod
    def from_string(cls, string):
        """Parse the string to an abstract syntax tree."""
        flat = string.replace("(", " ( ").replace(")", " ) ").replace("*", " * ")
        tokens = [token.strip() for token in flat.split()]
        for t in tokens:
            # Check for invalid tokens, e.g. typos or OCR errors.
            assert re.fullmatch(
                "|".join(TOKEN_PATTERNS.values()), t
            ), f"Invalid token {t!r}"
        return cls(tokens)

    def __str__(self):
        """Convert AST back to string."""
        string = tree_to_string(self.tree).strip()[1:-1].strip()
        assert self.__class__.from_string(string).tree == self.tree
        return string


if __name__ == "__main__":
    print(AST.from_file("DOCTOR.txt"))
