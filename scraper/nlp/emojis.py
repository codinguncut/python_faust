from emoji.core import get_emoji_regexp

RE_EMOJI = get_emoji_regexp()


def init():
    pass


def emojis(analyzer, text):
    return set(RE_EMOJI.findall(text))
