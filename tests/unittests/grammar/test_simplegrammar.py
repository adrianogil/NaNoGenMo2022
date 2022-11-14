from nanogenmo2022.grammar.grammar import SimpleGrammar


def test_grammar_instantiation():
    grammar = SimpleGrammar()
    assert grammar is not None

def test_grammar_gen_text_no_tags():
    grammar = SimpleGrammar()
    grammar.set_text("Test")

    generated_text = grammar.evaluate()

    assert generated_text == "Test"
