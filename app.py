import streamlit as st
from main import MainApplication

def run_interface():
    # Title/Change enteries with EXAMPLE in it
    st.title("EXAMPLE: (Predictive Analytics Engine)")
    st.subheader("Kalshi Market Interface")

    # Initialize backend application controller
    app_controller = MainApplication()
    system_ready, secrets = app_controller.initialize_system()

    # Graceful Interface Fallback if .env is missing
    if not system_ready:
        st.warning("Configuration Alert: Clear workspace detected...")
        st.info("The application is running in offline mode. Please configure your credentials later to enable live API streaming.")
    else:
        st.success("System fully configured!")

    # --- Interface Layout ---
    st.write("---")
    market_ticker = st.text_input("Enter Kalshi Market Ticker | EXAMPLE: (FED-26-HIKE):")
    
    if st.button("Generate Prediction"):
        if market_ticker:
            st.write(f"Analyzing market ticker: {market_ticker}...")
            # Future: Call conflict detection and prediction pipeline here
        else:
            st.error("Please enter a valid ticker.")

if __name__ == "__main__":
    run_interface()