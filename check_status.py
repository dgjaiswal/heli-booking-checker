import requests
import sys

def check_heli_booking():
    url = 'https://www.heliyatra.irctc.co.in/'
    # The text we expect to see when it is CLOSED
    closed_text = 'Booking is currently closed. Test failure text.'
    
    try:
        # Adding a User-Agent header to look like a real browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        
        # LOGIC: If the 'closed' text is NOT there, we want the script to FAIL
        if closed_text not in response.text:
            print("!!! ALERT: Booking text not found. Bookings might be OPEN !!!")
            # Exit with code 1 forces a GitHub Action Failure
            sys.exit(1) 
        else:
            print("Status: Still closed. Script finishing successfully.")
            sys.exit(0)
            
    except Exception as e:
        print(f"Network or Website Error: {e}")
        # We don't exit(1) here because we don't want false alarms for tiny network glitches
        sys.exit(0) 

if __name__ == "__main__":
    check_heli_booking()
