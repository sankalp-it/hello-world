import os
import streamlit as st
from datetime import date
from real_api_client import RealAPIClient  #
# from dummy_client_api import DummyAPIClient

def main():
	st.title("🚗 Vehicle Warranty Coverage Checker")
	# Read from environment or use Streamlit sidebar for override
	base_url = os.getenv("BASE_URL", "http://localhost:8000")
	endpoint = os.getenv("ENDPOINT_PATH", "/api/coverage")

	st.sidebar.title("API Configuration")
	base_url = st.sidebar.text_input("Base URL", base_url)
	endpoint = st.sidebar.text_input("Endpoint Path", endpoint)
	with st.form("vehicle_form"):
		year = st.number_input("Year", min_value=1900, max_value=2100, step=1, value=2021)
		make = st.text_input("Make")
		model = st.text_input("Model")
		trim = st.text_input("Trim")
		current_mileage = st.number_input("Current Mileage", min_value=0, step=1, value=10000)
		parts_input = st.text_input("Parts (comma-separated)")
		initial_sale_date = st.date_input("Initial Sale Date", value=date(2021, 1, 1))
		has_vpp_coverage = st.checkbox("Has VPP Coverage?", value=False)
		submitted = st.form_submit_button("Check Coverage")

	if submitted:
		parts_list = [part.strip() for part in parts_input.split(",") if part.strip()]
		payload = {
			"year": year,
			"make": make,
			"model": model,
			"trim": trim,
			"current_mileage": current_mileage,
			"parts": parts_list,
			"initial_sale_date": str(initial_sale_date),
			"has_vpp_coverage": has_vpp_coverage
		}

		# client = DummyAPIClient()
		client = RealAPIClient(base_url, endpoint)
		result = client.get_coverage(payload)
		if "error" in result:
			st.error(f"❌ {result['message']}")
			# st.json(result)
		else:
			st.success("✅ Warranty Check Result")
			# st.subheader("✅ Warranty Check Result")
			st.json(result)


if __name__ == "__main__":
    main()