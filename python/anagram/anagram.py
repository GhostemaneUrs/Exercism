from collections import Counter


def find_anagrams(word, candidates):
    word = word.lower()
    candi = Counter(word)
    result = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if word == candidate_lower:
            continue
        candidat = Counter(candidate_lower)
        if candidat == candi:
            result.append(candidate)
    return result
