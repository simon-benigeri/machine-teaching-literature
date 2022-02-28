from snorkel.labeling import labeling_function

# Set voting values.
ABSTAIN = -1
MOTION = 1
NOT_MOTION = 0

lf_set_heuristics = []


@labeling_function()
def lf_first_word_motion(x):
    """Tokenizes the text to check if first word is motion."""
    _first_token = x.text.lower().split()[0]
    return MOTION if "motion" == _first_token else ABSTAIN


lf_set_heuristics.append(lf_first_word_motion)


@labeling_function()
def lf_motion_not_in_first_three_words(x):
    """Tokenizes the text to check if motion is not in first 3 words."""
    _tokens = x.text.lower().split()[:3]
    return NOT_MOTION if not "motion" in _tokens else ABSTAIN


lf_set_heuristics.append(lf_motion_not_in_first_three_words)


@labeling_function()
def lf_motion_mentioned_later(x):
    """Tokenizes the text to check if first word is motion."""
    # Motion is mentioned somewhere in the middle of the docket entry
    # and Motion is not mentioned at the start
    _tokens = x.text.lower().split()
    condition = "motion" in _tokens[3:] and "motion" not in _tokens[:2]
    return NOT_MOTION if condition else ABSTAIN


lf_set_heuristics.append(lf_motion_mentioned_later)


@labeling_function()
def lf_motion_early(x):
    """Tokenizes the text to check if motion is mentioned in first 5 words"""
    # Motion is mentioned somewhere in the middle of the docket entry
    # and Motion is not mentioned at the start
    _tokens = x.text.lower().split()
    condition = "motion" in _tokens[:5] and "motion" not in _tokens[6:]
    return MOTION if condition else ABSTAIN


lf_set_heuristics.append(lf_motion_early)
