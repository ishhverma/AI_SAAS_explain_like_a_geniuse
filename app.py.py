import gradio as gr
import random
import time
from typing import Dict, List, Optional
import json
from datetime import datetime

# Genius Engine Classes
class EinsteinEngine:
    """Einstein-style explanations using thought experiments"""
    
    def explain(self, topic: str, difficulty: str, length: str) -> str:
        thought_experiments = [
            f"Imagine you're riding on a beam of light, trying to understand {topic}...",
            f"Picture yourself in a falling elevator, observing how {topic} behaves...",
            f"Suppose you could travel at the speed of light while studying {topic}...",
            f"Visualize spacetime as a fabric, and {topic} as waves rippling through it..."
        ]
        
        explanations = {
            "short": f"""## 🧪 Einstein's Insight

*{random.choice(thought_experiments)}*

**The Core Principle:**
{topic} emerges from the fundamental geometry of the universe. Think of it not as a thing, but as a relationship between observations.

**The Beautiful Simplicity:**
When you truly understand {topic}, you realize nature is elegant—it's just that our perspective is limited.""",

            "medium": f"""## 🧪 Einstein's Thought Experiment

*{random.choice(thought_experiments)}*

### The Conceptual Framework

**The Deep Insight:**
{topic} isn't mysterious—it's the natural result of how the universe maintains consistency across all reference frames. Just as a moving clock ticks slower, {topic} reveals itself differently depending on how you look at it.

**A Simplified Model:**
Imagine the universe as a great cosmic dance. The dancers (particles, ideas, systems) follow steps determined by the music of fundamental laws. But here's the beautiful part—the dancers themselves create the music!

**Real-World Connection:**
Next time you experience {topic} in daily life, remember: you're witnessing the universe's elegant architecture in action.""",

            "long": f"""## 🧪 Einstein's Complete Analysis

*{random.choice(thought_experiments)}*

### Part 1: The Gedankenexperiment

Let's conduct a thought experiment together. Close your eyes and imagine...

### Part 2: Mathematical Beauty

The equations describing {topic} are like poetry—they tell us that nature's laws are the same for all observers. This principle of relativity leads us to profound conclusions about {topic}.

### Part 3: The Physical Reality

In our universe, {topic} manifests through these fundamental principles:

1. **Principle of Relativity**: The laws of physics are the same for all observers
2. **Constancy of Light Speed**: The cosmic speed limit reveals deep truths
3. **Equivalence Principle**: Gravity and acceleration are locally indistinguishable

### Part 4: Implications for Understanding

When you grasp {topic} through this lens, you're not just learning facts—you're understanding how the universe thinks."""
        }
        
        return explanations.get(length, explanations["medium"])
    
    def get_style_name(self):
        return "Albert Einstein (Conceptual)"


class FeynmanEngine:
    """Feynman-style intuitive explanations"""
    
    def explain(self, topic: str, difficulty: str, length: str) -> str:
        analogies = [
            f"Think of {topic} like a child playing with blocks...",
            f"It's like explaining why a ball falls down instead of up—simple when you think about it.",
            f"Imagine you're teaching {topic} to a curious 10-year-old...",
            f"Picture {topic} as a game of billiards where we can't see the balls..."
        ]
        
        explanations = {
            "short": f"""## 🎭 Feynman's Simple Take

*{random.choice(analogies)}*

**The One-Minute Explanation:**
Here's the thing about {topic}—it's actually simpler than experts make it sound. Nature is simple; our explanations get complicated.

**Key Insight:**
If you can't explain {topic} to a first-year student, you don't really understand it yourself.""",

            "medium": f"""## 🎭 Feynman's Intuitive Explanation

*{random.choice(analogies)}*

### Let Me Explain It Simply

**What's Really Happening:**
You see, when we look at {topic}, we're really looking at nature doing its thing. There's no magic—just cause and effect playing out in interesting ways.

**The Rubber Band Analogy:**
Think about stretching a rubber band. The more you stretch it, the more energy it stores. That's exactly like {topic}—it's all about relationships and stored potential.

**Why It's Not Complicated:**
The universe doesn't know it's complicated. That's a human invention. {topic} is just nature being nature, following simple rules that create interesting results.""",

            "long": f"""## 🎭 Feynman's Complete Walkthrough

*{random.choice(analogies)}*

### Part 1: The Child's Question

"Why?" That's the most important question in science. Let's answer it for {topic} like we're talking to an intelligent child.

### Part 2: Building Understanding Brick by Brick

First, we need to understand the simple pieces:
- **What happens**: The observable facts
- **How it happens**: The mechanism
- **Why it happens**: The underlying principle

### Part 3: The Famous Feynman Technique

To truly master {topic}:

1. **Explain it simply**: Use everyday language
2. **Identify gaps**: Find what you can't explain simply
3. **Go back to sources**: Learn the missing pieces
4. **Review and simplify**: Repeat until it's clear

### Part 4: The Joy of Discovery

The most exciting part about understanding {topic} isn't the knowledge itself—it's the feeling of "Aha! Now I see how nature works!" """
        }
        
        return explanations.get(length, explanations["medium"])
    
    def get_style_name(self):
        return "Richard Feynman (Intuitive)"


class BuffettEngine:
    """Buffett-style business-focused explanations"""
    
    def explain(self, topic: str, difficulty: str, length: str) -> str:
        business_analogies = [
            f"Think of {topic} as a business with a wide moat...",
            f"In the economy of ideas, {topic} has durable competitive advantages...",
            f"Like a great company, {topic} compounds in value over time...",
            f"Consider {topic} through the lens of intrinsic value..."
        ]
        
        explanations = {
            "short": f"""## 💼 Buffett's Business Perspective

*{random.choice(business_analogies)}*

**The Bottom Line:**
When analyzing {topic}, focus on the fundamentals. What's the moat? What are the long-term prospects?

**Simple Wisdom:**
Price is what you pay for understanding {topic}. Value is what you get.""",

            "medium": f"""## 💼 Buffett's Investment Framework

*{random.choice(business_analogies)}*

### The Business Analysis

Let's analyze {topic} like we're buying a company:

**The Moat:**
What protects {topic} from being easily replaced? In business, we look for competitive advantages. Here, we look for fundamental truths that withstand scrutiny.

**Circle of Competence:**
I only invest in businesses I understand. Similarly, let's stick to what we can grasp about {topic}. The key insights are often simpler than experts claim.

**Long-Term Thinking:**
The market is a voting machine in the short term and a weighing machine in the long term. Understanding {topic} is about weighing, not voting.""",

            "long": f"""## 💼 Buffett's Complete Analysis

*{random.choice(business_analogies)}*

### Part 1: The Annual Report

If {topic} were a company, here's what its annual report would say:

**Assets:**
- Fundamental principles that never change
- Applications across multiple domains
- Historical track record of relevance

**Liabilities:**
- Misconceptions and myths
- Overcomplication by experts
- Short-term thinking about long-term concepts

### Part 2: The Moat Analysis

Great businesses have moats—sustainable advantages. For {topic}, the moat includes:

1. **Fundamental truth** (can't be disrupted)
2. **Universal applicability** (works everywhere)
3. **Timeless relevance** (as true tomorrow as today)

### Part 3: The Margin of Safety

When investing, we buy below intrinsic value. When learning {topic}:

- Build understanding brick by brick
- Question everything until it's rock solid
- Leave room for nuance and complexity

### Part 4: The Long-Term Hold

The best investment is knowledge that compounds. Understanding {topic} isn't about quick gains—it's about building intellectual capital that pays dividends for life."""
        }
        
        return explanations.get(length, explanations["medium"])
    
    def get_style_name(self):
        return "Warren Buffett (Business)"


# Main Application Class
class ExplainLikeAGenius:
    def __init__(self):
        self.engines = {
            "Albert Einstein (Conceptual)": EinsteinEngine(),
            "Richard Feynman (Intuitive)": FeynmanEngine(),
            "Warren Buffett (Business)": BuffettEngine()
        }
        self.history = []
        
    def generate_explanation(self, topic, genius_style, difficulty, length):
        if not topic or not topic.strip():
            return "Please enter a topic to explore.", "No concepts yet.", "{}"
        
        # Clean the topic
        topic = topic.strip()
        
        # Get the selected engine
        engine = self.engines.get(genius_style, self.engines["Richard Feynman (Intuitive)"])
        
        # Generate explanation
        explanation = engine.explain(topic, difficulty, length)
        
        # Generate key concepts
        concepts = self._extract_concepts(explanation)
        
        # Save to history
        self.history.append({
            'topic': topic,
            'style': genius_style,
            'time': datetime.now().strftime("%H:%M, %b %d")
        })
        self.history = self.history[-5:]  # Keep last 5
        
        # Simple visualization data
        viz_data = {
            "nodes": [topic.capitalize(), "Principles", "Applications", "Examples"],
            "edges": [[0, 1], [0, 2], [2, 3]]
        }
        
        return explanation, concepts, json.dumps(viz_data)
    
    def _extract_concepts(self, explanation):
        """Extract key concepts from explanation"""
        lines = explanation.split('\n')
        concepts = []
        for line in lines:
            if '**' in line or '###' in line:
                clean_line = line.replace('**', '').replace('###', '').strip()
                if clean_line and len(clean_line) < 50:
                    concepts.append(f"• {clean_line}")
        
        if not concepts:
            concepts = ["• Understanding fundamentals", "• Practical applications", "• Key principles"]
        
        return '\n'.join(concepts[:5])
    
    def get_history_text(self):
        if not self.history:
            return "Your learning journey will appear here..."
        
        text = "### 📚 Recent Explorations\n\n"
        for item in reversed(self.history):
            text += f"**{item['topic']}**\n"
            text += f"*{item['style']}* • {item['time']}\n\n"
        return text
    
    def ask_followup(self, question, context):
        if not question or not question.strip():
            return "Ask me anything about the topic!"
        
        responses = [
            f"That's an excellent question about {question}. Let me explain...",
            f"To understand {question}, we need to look deeper at the fundamentals.",
            f"Great observation! Here's how I think about {question}...",
            f"The key to {question} is understanding the underlying principles."
        ]
        
        return random.choice(responses) + "\n\n*This is a simulated response. In production, this would connect to a real AI model.*"


# Create the app instance
app = ExplainLikeAGenius()

# Custom CSS for better styling
custom_css = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
.genius-header {
    text-align: center;
    margin-bottom: 2rem;
}
.genius-header h1 {
    font-size: 2.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.genius-subtitle {
    font-size: 1.2rem;
    color: #666;
}
.feature-card {
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}
"""

# Create the Gradio interface
with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.HTML("""
    <div class="genius-header">
        <h1>🧠 Explain Like a Genius</h1>
        <div class="genius-subtitle">Learn anything through the lens of history's greatest thinkers</div>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            # Main input area
            topic = gr.Textbox(
                label="What would you like to understand?",
                placeholder="e.g., quantum entanglement, inflation, neural networks, blockchain...",
                lines=2
            )
            
            with gr.Row():
                genius = gr.Dropdown(
                    choices=["Albert Einstein (Conceptual)", 
                            "Richard Feynman (Intuitive)", 
                            "Warren Buffett (Business)"],
                    label="Choose your genius",
                    value="Richard Feynman (Intuitive)"
                )
                
                difficulty = gr.Dropdown(
                    choices=["Beginner", "Intermediate", "Advanced"],
                    label="Depth",
                    value="Beginner"
                )
                
                length = gr.Dropdown(
                    choices=["short", "medium", "long"],
                    label="Length",
                    value="medium"
                )
            
            generate_btn = gr.Button("✨ Generate Explanation", variant="primary", size="lg")
            
            # Output tabs
            with gr.Tabs():
                with gr.TabItem("📝 Explanation"):
                    output = gr.Markdown(label="Your explanation will appear here...")
                
                with gr.TabItem("🔑 Key Concepts"):
                    concepts = gr.Textbox(label="Key takeaways", lines=8, interactive=False)
                
                with gr.TabItem("📊 Concept Map"):
                    viz = gr.JSON(label="Knowledge structure")
            
            # Follow-up section
            gr.Markdown("---")
            gr.Markdown("### 💭 Dive Deeper")
            
            with gr.Row():
                followup = gr.Textbox(
                    label="Ask a follow-up question",
                    placeholder="e.g., Can you give me a real-world example?",
                    scale=4
                )
                ask_btn = gr.Button("Ask", scale=1)
            
            followup_out = gr.Markdown()
        
        with gr.Column(scale=1):
            # Sidebar
            gr.Markdown("### 🎯 Try these")
            examples = [
                "quantum entanglement",
                "how does inflation work",
                "what is blockchain",
                "neural networks explained",
                "why is the sky blue",
                "how do vaccines work"
            ]
            
            for ex in examples:
                gr.Button(ex, size="sm").click(
                    fn=lambda x=ex: x,
                    outputs=topic
                )
            
            gr.Markdown("---")
            history = gr.Markdown(app.get_history_text())
            refresh_btn = gr.Button("🔄 Refresh", size="sm")
    
    # Event handlers
    generate_btn.click(
        fn=app.generate_explanation,
        inputs=[topic, genius, difficulty, length],
        outputs=[output, concepts, viz]
    ).then(
        fn=app.get_history_text,
        outputs=history
    )
    
    ask_btn.click(
        fn=app.ask_followup,
        inputs=[followup, output],
        outputs=followup_out
    )
    
    refresh_btn.click(
        fn=app.get_history_text,
        outputs=history
    )
    
    # Footer
    gr.HTML("""
    <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f5f5f5; border-radius: 10px;">
        <p>Made with 🧠 for curious minds | 
        <a href="https://huggingface.co/spaces">Deploy your own</a></p>
    </div>
    """)

# Launch the app
if __name__ == "__main__":
    demo.launch()