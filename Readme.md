# 🧠 Reddit User Persona Builder

This project scrapes Reddit posts and comments from a user profile and generates a detailed user persona using an LLM (Claude or Gemini).  
All Reddit data is collected using PRAW, and output is saved as a text file.

---
## 🔧 Technologies Used

- Python
- PRAW (Reddit API wrapper)
- dotenv
- Claude AI (for persona generation)
---
```
## 📦 Folder Structure

RedditPersonaBuilder/
├── main.py # Main driver script
├── scraper.py # Reddit scraper logic
├── .env # Contains Reddit API credentials (not committed)
├── kojied_raw_data.txt # Scraped Reddit content
├── output/
│ └── user_persona_kojied.txt # Final user persona (generated by LLM)
```
---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jnishtha/RedditPersonaBuilder.git
cd RedditPersonaBuilder
```
2. Install dependencies
```bash
pip install praw python-dotenv
```

3. Setup .env
Create a .env file in the root directory and add:

```env
Copy code
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=UserPersonaBuilder/0.0.1
```

4. Run the script
```bash
python main.py
```
Enter a Reddit profile URL when prompted:
```ruby
https://www.reddit.com/user/kojied/
```
## 💬Persona Generation 
Paste the contents of kojied_raw_data.txt into Claude using this prompt:

I want you to act like a user persona generator for Reddit profiles. Based on the following posts and comments by a user, create a detailed user persona with the following sections:

Personality Traits

Interests and Hobbies

Communication Style

Beliefs or Opinions (if evident)

Emotional Tone or Attitude

For each characteristic, cite the post or comment that supports it.

Save the result in:

```bash
output/user_persona_kojied.txt
```
## 📝 Example Output
kojied_raw_data.txt → Raw scraped Reddit content

user_persona_kojied.txt → AI-generated persona from Claude

## 📜 License
This project is created for educational and evaluation purposes only.

All Reddit content belongs to their respective authors as per Reddit's terms of service.

Do not use this project for commercial or redistribution purposes without permission.

## 👩‍💻 Author
Nishtha Jain




