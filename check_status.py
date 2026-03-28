import requests
import sys

def check_heli_booking():
    url = 'https://www.heliyatra.irctc.co.in/'
    target_text = 'Booking is currently closed. You will be notified as soon as it reopens'
    expected_count = 4
    
    # ADVANCED HEADERS: Makes the script look like a real Chrome browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    
    try:
        # Create a 'Session' to handle cookies automatically
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=30)
        
        # Check if we got blocked (403) or not found (404)
        if response.status_code != 200:
            print(f"Website returned status code: {response.status_code}")
            # We exit 0 here to avoid a "false alarm" failure if it's just a temporary block
            sys.exit(0)

        actual_count = response.text.count(target_text)
        
        if actual_count == expected_count:
            print(f"Status: Found '{target_text}' exactly {actual_count} times.")
            sys.exit(0) 
        else:
            print(f"!!! ALERT: Count is {actual_count} instead of {expected_count} !!!")
            sys.exit(1) # TRIGGER PHONE NOTIFICATION
            
    except Exception as e:
        print(f"Network Error: {e}")
        sys.exit(0) 

if __name__ == "__main__":
    check_heli_booking()
