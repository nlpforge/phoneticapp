import streamlit as st

from src.dist import phonetic_distance, is_candidates_valid

st.title('Phonetic Game')

target = st.text_input("Select target word", '').lower()

if target:

	st.markdown(f"Target Word is: **{target}**")

	st.text("Player 1 Turn")
	candidates_1 = st.text_input(f"Enter candidates separated by space", '', key="first").lower()

	if candidates_1:
		cands_1 = candidates_1.split(' ')
		if not is_candidates_valid(cands_1):
			st.text("Inputs are not valid dictionary words, score is set to 0")
			score_1 = 0.0
		else:
			score_1 = int(100 - phonetic_distance(target, cands_1))
		st.text(f"Your score is {str(score_1)} out of 100")

		st.text("Player 2 Turn")
		candidates_2 = st.text_input(f"Enter candidates separated by space", '', key="second").lower()

		if candidates_2:
			cands_2 = candidates_2.split(' ')
			if not is_candidates_valid(cands_2):
				st.text("Inputs are not valid dictionary words, score is set to 0")
				score_2 = 0.0
			else:
				score_2 = int(100 - phonetic_distance(target, cands_2))
			st.text(f"Your score is {str(score_2)} out of 100")

			if score_1 > score_2:
				st.text("Player 1 wins!")
			else:
				st.text("Player 2 wins!")
