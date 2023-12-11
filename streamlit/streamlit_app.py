import streamlit as st
import requests


cap_shape_values = ['x', 'b', 'f', 's', 'k', 'c']
cap_surface_values = ['s', 'y', 'f', 'g']
cap_color_values = ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r']
bruises_values = ['t', 'f']
odor_values = ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm']
gill_attachment_values = ['f', 'a']
gill_spacing_values = ['c', 'w']
gill_size_values = ['n', 'b']
gill_color_values = ['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o']
stalk_shape_values = ['e', 't']
stalk_root_values = ['e', 'c', 'b', 'r', '?']
stalk_surface_above_ring_values = ['s', 'f', 'k', 'y']
stalk_surface_below_ring_values = ['s', 'f', 'y', 'k']
stalk_color_above_ring_values = ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y']
stalk_color_below_ring_values = ['w', 'p', 'g', 'n', 'b', 'e', 'o', 'c', 'y']
veil_type_values = ['p']
veil_color_values = ['w', 'n', 'o', 'y']
ring_number_values = ['o', 't', 'n']
ring_type_values = ['p', 'e', 'l', 'f', 'n']
spore_print_color_values = ['w', 'n', 'k', 'h', 'r', 'u', 'o', 'y', 'b']
population_values = ['v', 'y', 's', 'n', 'a', 'c']
habitat_values = ['d', 'g', 'p', 'l', 'u', 'm', 'w']


def get_prediction(data):
	URL = "http://127.0.0.1:8000/predict"
	resp = requests.post(URL, json=data)
	return resp.json()


def main():
	overview = st.container()
	left, center, right = st.columns(3)
	prediction = st.container()

	with overview:
		st.title("Fungs")

	with left:
		cap_shape_radio = st.selectbox("Select cap shape:", cap_shape_values)
		cap_surface_radio = st.selectbox("Select cap surface:", cap_surface_values)
		cap_color_radio = st.selectbox("Select cap color:", cap_color_values)
		bruises_radio = st.selectbox("Select bruises:", bruises_values)
		odor_radio = st.selectbox("Select odor:", odor_values)
		gill_attachment_radio = st.selectbox("Select gill attachment:", gill_attachment_values)
		gill_spacing_radio = st.selectbox("Select gill spacing:", gill_spacing_values)

	with center:
		gill_size_radio = st.selectbox("Select gill size:", gill_size_values)
		gill_color_radio = st.selectbox("Select gill color:", gill_color_values)
		stalk_shape_radio = st.selectbox("Select stalk shape:", stalk_shape_values)
		stalk_root_radio = st.selectbox("Select stalk root:", stalk_root_values)
		stalk_surface_below_ring_radio = st.selectbox("Select stalk surface below ring:", stalk_surface_below_ring_values)
		stalk_color_above_ring_radio = st.selectbox("Select stalk color above ring:", stalk_color_above_ring_values)
		stalk_color_below_ring_radio = st.selectbox("Select stalk color below ring:", stalk_color_below_ring_values)
		veil_type_radio = st.selectbox("Select veil type:", veil_type_values)
	with right:
		stalk_surface_above_ring_radio = st.selectbox("Select stalk surface above ring:", stalk_surface_above_ring_values)
		veil_color_radio = st.selectbox("Select veil color:", veil_color_values)
		ring_number_radio = st.selectbox("Select ring number:", ring_number_values)
		ring_type_radio = st.selectbox("Select ring type:", ring_type_values)
		spore_print_color_radio = st.selectbox("Select spore print color:", spore_print_color_values)
		population_radio = st.selectbox("Select population:", population_values)
		habitat_radio = st.selectbox("Select habitat:", habitat_values)
		
	data = {
		"cap_shape": cap_shape_radio,
		"cap_surface": cap_surface_radio,
		"cap_color": cap_color_radio,
		"bruises": bruises_radio,
		"odor": odor_radio,
		"gill_attachment": gill_attachment_radio,
		"gill_spacing": gill_spacing_radio,
		"gill_size": gill_size_radio,
		"gill_color": gill_color_radio,
		"stalk_shape": stalk_shape_radio,
		"stalk_root": stalk_root_radio,
		"stalk_surface_above_ring": stalk_surface_above_ring_radio,
		"stalk_surface_below_ring": stalk_surface_below_ring_radio,
		"stalk_color_above_ring": stalk_color_above_ring_radio,
		"stalk_color_below_ring": stalk_color_below_ring_radio,
		"veil_type": veil_type_radio,
		"veil_color": veil_color_radio,
		"ring_number": ring_number_radio,
		"ring_type": ring_type_radio,
		"spore_print_color": spore_print_color_radio,
		"population": population_radio,
		"habitat": habitat_radio
	}

	URL = "http://127.0.0.1:8000/predict"
	resp = requests.post(URL, json=data)
	pred = resp.json()

	# 0 = poison
	# 1 = edible
	# st.button('Submit', on_click=get_prediction(data))


	with prediction:
		st.subheader("Czy grzyb jest trujacy?")
		st.subheader(("Tak" if pred["prediction"] == 0 else "Nie"))
		st.button('Submit', on_click=get_prediction(data))
		# st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][prediction][0] * 100))

if __name__ == "__main__":
	main()