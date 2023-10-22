# 🕵️ ANONYMIZER 🛡️

Palm-2 Streamlit integration for anonymzing / obfuscating entire codebases and repos

##🌠 Inspiration:
The creation of our code anonymizer project was deeply influenced by the challenges faced by industry giants like Samsung. They encountered significant issues related to code leaks when their proprietary code inadvertently surfaced on platforms like ChatGPT. This unsettling experience highlighted the pressing need for a robust solution to protect sensitive and valuable code assets.

##🛠️ What it does:
Anonymizer is a cutting-edge tool that empowers developers to safeguard their intellectual property by obfuscating their code. With our advanced obfuscation techniques, your original work remains impenetrable to prying eyes, protecting your software's integrity and uniqueness.

##🚀 How we built it:
We harnessed Google's formidable Palm2 language model, in conjunction with Streamlit, a Python framework renowned for user-friendly interfaces, to create our code anonymizer. Employing rigorous data validation and multiple layers of iterative refinement, our efforts culminated in a powerful solution. This tool can not only detect code efficiently but also perform precise code obfuscation and anonymization. It's a robust, user-centric resource poised to safeguard intellectual property and sensitive code, allowing individuals and organizations to work with peace of mind, confident that their code remains protected from unintended exposure. Our dedication to code security and innovation drives our mission.

##🧩 Challenges we ran into:
In the development of our advanced anonymizer, a significant challenge arose when validating whether the input prompt contained code or not, and determining the appropriate response. To overcome this hurdle, we implemented a multi-layered approach featuring intricate conditionals and refinements. This refined system adeptly discerns between code and non-code inputs, ensuring precise anonymization when code is detected, and generating non-code responses for all other inputs. Our commitment to robust code protection and innovation has driven us to create a solution that effortlessly addresses this fundamental challenge, allowing users to trust their code's security with confidence.

##🏆 Accomplishments that we're proud of:
Struggling with Streamlit was a challenging journey, but perseverance paid off. After numerous hours of tinkering, the moment finally arrived when the Streamlit app came to life. The sense of accomplishment was immense. It felt like conquering a mountain, and that moment was my summit. All the frustration and setbacks dissolved into a wave of pride and satisfaction. This achievement wasn't just about code; it was a testament to the power of determination and the thrill of mastering something new. From struggle to success, it was a journey worth every effort, and the working Streamlit app stood as a beacon of triumph.

##📚 What we learned:
Our journey was a profound learning experience. We delved into the intricacies of interacting with APIs, honed our skills in data validation, and triumphantly harnessed the power of the Streamlit framework. These lessons weren't just technical; they were a testament to our ability to adapt and grow. From navigating data sources to crafting a seamless Python frontend, our newfound knowledge became the backbone of our project. It was more than a development process; it was a transformative journey that enriched our capabilities and marked a significant milestone in our pursuit of creating an effective solution for code anonymization.

##🌍 What's next for Anonymizer:
Our tool is able to keep information from companies and users confidential. A company might want to share a snippet of their code to their co workers while preserving sensitive skims of code. LM’s can also use this to preserve user’s style in databases. For future implementation, the Anonymizer could be used to instantly anonymize a whole github repo by just linking it, and the application would create a clone with obfuscated code. 
