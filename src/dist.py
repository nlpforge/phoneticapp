import jellyfish
import pronouncing

from spellchecker import SpellChecker

spell = SpellChecker()

def is_candidates_valid(l):
    return len(spell.unknown(l)) == 0

def candidates_to_phones(l):
    assert(is_candidates_valid(l))
    return ' '.join([pronouncing.phones_for_word(w)[0] for w in l])

def phonetic_distance(target, cands):
    
    t_metaphone = jellyfish.metaphone(target)
    c_metaphone = ''.join([jellyfish.metaphone(c) for c in cands])
    
    t_phone = pronouncing.phones_for_word(target)[0]
    c_phone = candidates_to_phones(cands)
    
    m_dist = jellyfish.levenshtein_distance(t_metaphone, c_metaphone)
    p_dist = jellyfish.levenshtein_distance(t_phone, c_phone)
    
    score = (0.5 * m_dist) + (0.5 * p_dist)
    return score