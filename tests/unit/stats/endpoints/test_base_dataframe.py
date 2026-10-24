from pandas import MultiIndex

from nba_api.stats.endpoints._base import Endpoint


def _frame(headers, rows=None):
    return Endpoint.DataSet({"headers": headers, "data": rows or []}).get_data_frame()


def test_column_span_repeats_each_name():
    df = _frame(
        [
            {"name": "SHOT_CATEGORY", "columnSpan": 3, "columnNames": ["A", "B"]},
            {
                "name": "columns",
                "columnSpan": 1,
                "columnNames": ["x", "y", "z", "x", "y", "z"],
            },
        ]
    )
    assert isinstance(df.columns, MultiIndex)
    assert list(df.columns) == [
        ("A", "x"),
        ("A", "y"),
        ("A", "z"),
        ("B", "x"),
        ("B", "y"),
        ("B", "z"),
    ]
    assert list(df.columns.names) == ["SHOT_CATEGORY", "columns"]


def test_missing_column_span_defaults_to_one():
    df = _frame([{"columnNames": ["A", "B"]}, {"columnNames": ["x", "y"]}])
    assert list(df.columns) == [("A", "x"), ("B", "y")]


def test_columns_to_skip_prepends_blanks():
    df = _frame(
        [
            {"name": "top", "columnsToSkip": 2, "columnSpan": 2, "columnNames": ["A"]},
            {"name": "bottom", "columnNames": ["id", "name", "x", "y"]},
        ]
    )
    assert list(df.columns) == [
        ("", "id"),
        ("", "name"),
        ("A", "x"),
        ("A", "y"),
    ]


def test_level_without_name_gets_positional_name():
    df = _frame(
        [
            {"name": "named", "columnNames": ["A"]},
            {"columnNames": ["x"]},
            {"columnNames": ["y"]},
        ]
    )
    assert list(df.columns.names) == ["named", "LEVEL_1", "LEVEL_2"]


def test_rows_align_with_columns():
    df = _frame(
        [
            {"columnSpan": 2, "columnNames": ["A", "B"]},
            {"columnNames": ["x", "y", "x", "y"]},
        ],
        [[1, 2, 3, 4]],
    )
    assert df[("B", "x")].tolist() == [3]


def test_labels_are_plain_str():
    df = _frame(
        [
            {"columnSpan": 2, "columnNames": ["A"]},
            {"columnNames": ["x", "y"]},
        ]
    )
    for level in range(df.columns.nlevels):
        for label in df.columns.get_level_values(level):
            assert type(label) is str


def test_zero_span_drops_names():
    df = _frame(
        [
            {"columnSpan": 0, "columnNames": ["A"], "columnsToSkip": 1},
            {"columnNames": ["id"]},
        ]
    )
    assert list(df.columns) == [("", "id")]
