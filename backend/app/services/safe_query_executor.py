import ast

import pandas as pd


ALLOWED_ATTRIBUTES = {
    "mean",
    "median",
    "sum",
    "min",
    "max",
    "count",
    "size",
    "nunique",
    "value_counts",
    "idxmax",
    "idxmin",
    "groupby",
    "agg",
    "apply",
    "reset_index",
    "sort_values",
    "head",
    "tail",
    "round",
    "to_frame",
    "isin",
    "iloc",
    "loc",
}

ALLOWED_NAMES = {
    "df",
    "x",
}

ALLOWED_NODES = (
    ast.Expression,
    ast.Call,
    ast.Attribute,
    ast.Name,
    ast.Load,
    ast.Constant,
    ast.Subscript,
    ast.Slice,
    ast.Compare,
    ast.Eq,
    ast.NotEq,
    ast.Gt,
    ast.GtE,
    ast.Lt,
    ast.LtE,
    ast.BoolOp,
    ast.And,
    ast.Or,
    ast.BinOp,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Mod,
    ast.UnaryOp,
    ast.USub,
    ast.UAdd,
    ast.List,
    ast.Tuple,
    ast.Dict,
    ast.keyword,
    ast.Lambda,
    ast.arguments,
    ast.arg,
)


class SafeQueryValidator(ast.NodeVisitor):
    """
    Validate AI-generated Pandas expressions
    before execution.
    """

    def visit(self, node):
        if not isinstance(node, ALLOWED_NODES):
            raise ValueError(
                f"Unsupported query operation: "
                f"{type(node).__name__}"
            )

        return super().visit(node)

    def visit_Name(self, node):
        if node.id not in ALLOWED_NAMES:
            raise ValueError(
                f"Unsafe variable detected: {node.id}"
            )

    def visit_Attribute(self, node):
        if node.attr.startswith("_"):
            raise ValueError(
                "Private attributes are not allowed."
            )

        if node.attr not in ALLOWED_ATTRIBUTES:
            raise ValueError(
                f"Method or attribute not allowed: "
                f"{node.attr}"
            )

        self.generic_visit(node)

    def visit_Lambda(self, node):
        if len(node.args.args) != 1:
            raise ValueError(
                "Only single-argument lambdas are allowed."
            )

        argument_name = node.args.args[0].arg

        if argument_name != "x":
            raise ValueError(
                "Lambda argument must be named x."
            )

        self.generic_visit(node)


def validate_query(pandas_query: str) -> ast.Expression:
    """
    Parse and validate a Pandas expression.
    """

    if not pandas_query.startswith("df"):
        raise ValueError(
            "Generated query must start with df."
        )

    try:
        parsed_query = ast.parse(
            pandas_query,
            mode="eval",
        )
    except SyntaxError as error:
        raise ValueError(
            f"Invalid query syntax: {str(error)}"
        ) from error

    validator = SafeQueryValidator()
    validator.visit(parsed_query)

    return parsed_query


def execute_safe_query(
    dataframe: pd.DataFrame,
    pandas_query: str,
):
    """
    Execute a validated Pandas expression.
    """

    parsed_query = validate_query(pandas_query)

    compiled_query = compile(
        parsed_query,
        filename="<ai-data-query>",
        mode="eval",
    )

    safe_dataframe = dataframe.copy()

    return eval(
        compiled_query,
        {"__builtins__": {}},
        {
            "df": safe_dataframe,
        },
    )