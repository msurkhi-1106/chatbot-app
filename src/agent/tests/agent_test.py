import pytest
from agent import Agent

nltk_dependencies = [
    'popular',
    'vader_lexicon'
]

agent = Agent(
    [],
    nltk_dependencies,
    "../../config/dataset.json",
    "../../chat_model",
    tokenizer_path = "../../tokenizer.pickle",
    label_encoder_path = "../../label_encoder.pickle"
)

def test_case_one():
    assert agent.query("What medicine should I take for a migraine?") == "If you have a migraine try taking a Tylenol or Advil. It should relive your headache. If your migraine persists for extended periods of time and after taking medicine, see a doctor."

def test_case_two():
    assert agent.query("treat, medicine, migraine") == "If you have a migraine try taking a Tylenol or Advil. It should relive your headache. If your migraine persists for extended periods of time and after taking medicine, see a doctor."

def test_case_three():
    assert agent.query("What should I do when I have the stomach flu?") == "Try to avoid solid foods. If you're hungry try to eat easier to digest foods like bananas, toast, soup, etc. Avoid coffee, nicotine, fatty foods, and alcohol. Make sure to get plenty of rest as well. If you want to know what medecine can be used to treat a stomach flu, just ask."