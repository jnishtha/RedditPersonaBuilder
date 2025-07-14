from scraper import get_user_content

def save_user_data(username, posts, comments):
    filename = f"{username}_raw_data.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"User: u/{username}\n\n")
        
        f.write("=== Posts ===\n")
        for post in posts:
            f.write(f"- Title: {post['title']}\n")
            f.write(f"  Body: {post['body']}\n")
            f.write(f"  URL: https://www.reddit.com{post['url']}\n\n")

        f.write("=== Comments ===\n")
        for comment in comments:
            f.write(f"- Comment: {comment['body']}\n")
            f.write(f"  URL: https://www.reddit.com{comment['url']}\n\n")
    
    print(f"\n✅ Raw data saved to: {filename}")

if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ")

    if "/user/" in url:
        username = url.split("/user/")[-1].strip("/")
        print(f"\n📥 Fetching data for u/{username} ...\n")
        posts, comments = get_user_content(username)
        save_user_data(username, posts, comments)
    else:
        print("❌ Invalid Reddit profile URL. Please include '/user/' in it.")
