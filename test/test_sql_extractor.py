import pytest
import pandas as pd
from unittest.mock import MagicMock, patch
from src.extract.sql_extractor import extract


def test_extract_returns_generator():
    mock_engine = MagicMock()
    mock_conn = MagicMock()
    mock_engine.connect.return_value.__enter__ = MagicMock(return_value=mock_conn)
    mock_engine.connect.return_value.__exit__ = MagicMock(return_value=False)

    chunks = [pd.DataFrame({"id": [1, 2], "col1": ["a", "b"]})]

    with patch("src.extract.sql_extractor.pd.read_sql_query", return_value=iter(chunks)):
        result = extract(mock_engine, "LTS", "fishes")
        import types
        assert isinstance(result, types.GeneratorType)

def test_extract_yields_dataframes():
    mock_engine = MagicMock()
    mock_conn = MagicMock()
    mock_engine.connect.return_value.__enter__ = MagicMock(return_value=mock_conn)
    mock_engine.connect.return_value.__exit__ = MagicMock(return_value=False)

    sample_data = [
        pd.DataFrame({"id": range(10_000), "col1": ["x"] * 10_000}),
        pd.DataFrame({"id": range(10_000, 15_000), "col1": ["y"] * 5_000}),
    ]

    with patch("src.extract.sql_extractor.pd.read_sql_query", return_value=iter(sample_data)):
        chunks = list(extract(mock_engine, "LTS", "fishes"))

    assert len(chunks) == 2
    assert all(isinstance(c, pd.DataFrame) for c in chunks)

def test_extract_empty_result():
    mock_engine = MagicMock()
    mock_conn = MagicMock()
    mock_engine.connect.return_value.__enter__ = MagicMock(return_value=mock_conn)
    mock_engine.connect.return_value.__exit__ = MagicMock(return_value=False)

    with patch("src.extract.sql_extractor.pd.read_sql_query", return_value=iter([])):
        chunks = list(extract(mock_engine, "LTS", "fishes"))

    assert chunks == []
