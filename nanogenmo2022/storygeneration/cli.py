
def cli(args=None):
    from nanogenmo2022.storygeneration.main import StoryGeneration

    story_generation = StoryGeneration()
    story = story_generation.generate()

    print(story)
