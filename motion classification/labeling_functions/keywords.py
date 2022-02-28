from snorkel.labeling import LabelingFunction

# Set voting values.
ABSTAIN = -1
MOTION = 1
NOT_MOTION = 0

lf_set_keywords = []


def keyword_lookup(x, keywords, label):
    if any(word in x.text.lower() for word in keywords):
        return label
    return ABSTAIN


def make_keyword_lf(keywords, label=MOTION):
    return LabelingFunction(
        name=f"keyword: {keywords[0]}",
        f=keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )


"""Motions contain 'motion of'."""
keyword__of = make_keyword_lf(keywords=["motion of"])
lf_set_keywords.append(keyword__of)

"""Motions contain 'motion to'."""
keyword__motion_to = make_keyword_lf(keywords=["motion to"])
lf_set_keywords.append(keyword__motion_to)

"""Motions contain 'motion by'."""
keyword__motion_by = make_keyword_lf(keywords=["motion by"])
lf_set_keywords.append(keyword__motion_by)

"""Motions contain 'motion (oral)'."""
keyword__motion_oral = make_keyword_lf(keywords=["motion (oral)"])
lf_set_keywords.append(keyword__motion_oral)

"""Motions contain 'joint motion'."""
keyword__joint_motion = make_keyword_lf(keywords=["joint motion"])
lf_set_keywords.append(keyword__joint_motion)

"""Notice of motions contain 'notice of motion'."""
keyword__notice_of_motion = make_keyword_lf(keywords=["notice of motion"], label=NOT_MOTION)
lf_set_keywords.append(keyword__notice_of_motion)

"""Notice of motions contain 'notice'."""
keyword__notice = make_keyword_lf(keywords=["notice"], label=NOT_MOTION)
lf_set_keywords.append(keyword__notice)

"""Judgements contain 'judgement'."""
keyword__judgement = make_keyword_lf(keywords=["judgement"], label=NOT_MOTION)
lf_set_keywords.append(keyword__judgement)

"""Denying a motion contains 'denying motion'."""
keyword__denying_motion = make_keyword_lf(keywords=["denying motion"], label=NOT_MOTION)
lf_set_keywords.append(keyword__denying_motion)

"""Final pretrial conference contains 'final pretrial conference'."""
keyword__final_pretrial_conference = make_keyword_lf(keywords=["final pretrial conference"], label=NOT_MOTION)
lf_set_keywords.append(keyword__final_pretrial_conference)

"""Documents refer to motions with 'regarding motion'"""
keyword__regarding_motion = make_keyword_lf(keywords=["regarding motion"], label=NOT_MOTION)
lf_set_keywords.append(keyword__regarding_motion)
