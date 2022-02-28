from snorkel.labeling import LabelingFunction

# Set voting values.
ABSTAIN = -1
MOTION = 1
NOT_MOTION = 0

lf_set_missing_keywords = []


def missing_keyword_lookup(x, keywords, label):
    if not any(word in x.text.lower() for word in keywords):
        return label
    return ABSTAIN


def make_missing_keyword_lf(keywords, label=MOTION):
    return LabelingFunction(
        name=f"missing keyword: {keywords[0]}",
        f=missing_keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )


"""NOT Motions do not contain 'motion'."""
missing_keyword__motion = make_missing_keyword_lf(keywords=["motion"], label=NOT_MOTION)
lf_set_missing_keywords.append(missing_keyword__motion)
