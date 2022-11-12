from nanogenmo2022.storygeneration.main import StoryGeneration


def test_storygeneration_is_not_empty():
    story_generation = StoryGeneration()
    story = story_generation.generate()
    assert story is not None
    assert story != ""
