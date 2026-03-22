import requests
import sys

def check_heli_booking():
    url = 'https://www.heliyatra.irctc.co.in/'
    target_text = 'Booking is currently closed'
    expected_count = 2
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        # Increased timeout to 30s as IRCTC can be slow
        response = requests.get(url, headers=headers, timeout=30)
        
        # Count occurrences of the specific string
        actual_count = response.text.count(target_text)
        
        if actual_count == expected_count:
            print(f"Status: Found '{target_text}' exactly {actual_count} times. Bookings are still closed.")
            sys.exit(0) # Success = No notification
        else:
            print(f"!!! ALERT !!!")
            print(f"Expected count: {expected_count}")
            print(f"Actual count found: {actual_count}")
            print("This mismatch suggests the page layout changed or bookings opened!")
            sys.exit(1) # Failure = PUSH NOTIFICATION TO PHONE
            
    except Exception as e:
        # We log the error but exit(0) to avoid "False Alarm" notifications 
        # caused by random internet timeouts in the GitHub data center.
        print(f"Network/Website Error: {e}")
        sys.exit(0) 

if __name__ == "__main__":
    check_heli_booking()
