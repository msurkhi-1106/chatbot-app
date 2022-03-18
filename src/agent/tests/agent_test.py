import pytest
from agent import Agent



def test_case_one():
    plugins = [
        SpellCheck,
        PosTag,
        EntityRecognition,
        SentimentAnalysis
    ]

    agent = Agent(plugins)
    assert 1 == 1