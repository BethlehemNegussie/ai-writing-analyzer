# Writing Analyzer by AI


A Python-based AI-powered writing analysis tool that assesses sentence structure, tone, and readability to assist writers in refining their work.
This tool provides feedback on writing clarity, emotional tone, and structural complexity after analyzing essays, stories, or letters.

# Characteristics

* Sentiment Analysis
  determines whether a text has a positive, negative, or neutral emotional tone.

* Evaluation of Readability
  determines the text's readability by calculating the Flesch Reading Ease score.

* Sentence Structure Analysis
  identifies excessively complex writing by measuring the average sentence length.

* Automated Writing Recommendations
  gives comments based on tone, readability, and sentence length.

Technologies Used
Python
Hugging Face Transformers (NLP models)
PyTorch
TextStat (readability analysis)

Installation
1. Clone the repository:
git clone https://github.com/bethlehemnegussie/ai-writing-analyzer.git
2. Navigate into the project folder:
cd ai-writing-analyzer
3. Install the required dependencies:
pip install -r requirements.txt

Usage

1. Run the analyzer as:

 python ai_writing_analyzer.py
2. Then paste your essay, story, or text when prompted.

Example:
Enter your text or writing: 
I think it's awesome that we have free will.

Example output
*******************
AI Writing Analyzer
*******************
Word count: 9
Average sentence length: 4.5 words
Tone: POSITIVE
Confidence: 1.00

Readability score: 103.7

Suggestions:
-Sentences are concise and the text is easy to read.
-Positive and engaging tone!
