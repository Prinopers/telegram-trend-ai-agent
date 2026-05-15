from src.telegram_sender import send_message

platforms = [
    "YouTube",
    "Reddit",
    "TikTok",
    "X",
    "Instagram"
]

def scan_trends():
    for platform in platforms:
        message = f"Scanning trends from {platform}..."
        
        print(message)
        send_message(message)

if __name__ == "__main__":
    scan_trends()
