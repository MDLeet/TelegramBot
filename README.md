
# TelegramBot
Detailed explanation of the program's function:
This program is an automated Telegram bot that uses Telethon to monitor selected source channels and then processes new messages before posting them to a target channel. During processing, several steps are performed, such as:


## **🔹What does the code do now?**

✅ **Copies posts** from source channels
✅ Supports posting **images** and **videos** with **text**
✅ Cleans up text of redundant links like `[ ] (link)`
✅ Maintains **Instant View** without issues
✅ Translates text **while preserving English words**
✅ Publishes to the target channel with **hashtags**

## **Detailed program steps:**

**1️⃣ Monitoring source channels**
The program monitors the channels specified in source_channels.
When a new message arrives in one of these channels, the `my_event_handler` event is executed.
**2️⃣ Cleaning the text and extracting the link**
The text is cleaned using `clean_text(text)`.
Any link in the message is searched using `re.findall(r'https?://\S+', text)`.
**3️⃣ Getting the page title and replacing the link**
When a link is found, an HTTP request is sent to the site to retrieve the page title using `get_page_title(url)`.
The link is replaced with the page title in bold using **Markdown**
**4️⃣ Translate into Arabic while preserving the English words.**
The text is passed to `translate_text(text)`.
The translation is done using the **GoogleTranslator library**.
The original English words are searched and returned to the translation so that technical website names are not mistranslated.
**5️⃣ Add Hashtags and Publish the Message**
The hashtags #Pentesting #Hacking #Cybersecurity #infosec #EthicalHacking are appended to the end of the message.
The translated message is published in the target channel.
