#!/usr/bin/python3
def multiple_returns(sentences):
    if sentences == "":
        sentences[0] = None

    return len(sentences), sentences[0]
