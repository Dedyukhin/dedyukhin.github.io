/**
 * Main JavaScript for Ivan Dedyukhin's Academic Website
 */

/**
 * Toggle abstract/details visibility for publications and teaching cards
 * @param {string} id - The ID of the element to toggle
 * @param {HTMLElement} btn - Optional button element for ARIA attributes
 */
function toggleAbstract(id, btn) {
    const el = document.getElementById(id);
    if (!el) {
        console.warn(`Element with id "${id}" not found`);
        return;
    }

    const isHidden = el.style.display === "none" || el.style.display === "";

    if (isHidden) {
        el.style.display = "block";
        if (btn) {
            btn.setAttribute('aria-expanded', 'true');
        }
        // Scroll into view when opened
        el.scrollIntoView({ behavior: "smooth", block: "nearest" });
    } else {
        el.style.display = "none";
        if (btn) {
            btn.setAttribute('aria-expanded', 'false');
        }
    }
}

/**
 * AI Assistant Chat Widget
 */
class AcademicAssistant {
    constructor() {
        this.apiEndpoint = '/api/query';  // Update with your deployed API endpoint
        this.isOpen = false;
        this.conversationHistory = [];
        this.init();
    }

    init() {
        this.createWidget();
        this.attachEventListeners();
    }

    createWidget() {
        // Create widget HTML
        const widgetHTML = `
            <div id="ai-assistant-widget" class="ai-widget">
                <button id="ai-widget-toggle" class="ai-widget-toggle" aria-label="Toggle AI Assistant">
                    <span class="ai-icon">💬</span>
                    <span class="ai-text">Ask AI</span>
                </button>

                <div id="ai-widget-chat" class="ai-widget-chat" style="display: none;">
                    <div class="ai-chat-header">
                        <h3>AI Research Assistant</h3>
                        <button id="ai-chat-close" class="ai-chat-close" aria-label="Close chat">&times;</button>
                    </div>

                    <div class="ai-chat-intro">
                        <p>Hi! I can answer questions about Ivan's research, publications, CV, and teaching.</p>
                        <div class="ai-suggested-questions">
                            <p><strong>Try asking:</strong></p>
                            <button class="ai-suggestion" data-question="What does Ivan research?">What does Ivan research?</button>
                            <button class="ai-suggestion" data-question="What are Ivan's publications?">What are Ivan's publications?</button>
                            <button class="ai-suggestion" data-question="What courses does Ivan teach?">What courses does Ivan teach?</button>
                        </div>
                    </div>

                    <div id="ai-chat-messages" class="ai-chat-messages"></div>

                    <div class="ai-chat-input-wrapper">
                        <input
                            type="text"
                            id="ai-chat-input"
                            class="ai-chat-input"
                            placeholder="Ask about research, publications, CV..."
                            maxlength="500"
                        />
                        <button id="ai-chat-send" class="ai-chat-send" aria-label="Send message">
                            Send
                        </button>
                    </div>

                    <div class="ai-chat-footer">
                        <small>Powered by OpenAI • Answers are based on website content</small>
                    </div>
                </div>
            </div>
        `;

        // Append to body
        document.body.insertAdjacentHTML('beforeend', widgetHTML);
    }

    attachEventListeners() {
        const toggle = document.getElementById('ai-widget-toggle');
        const close = document.getElementById('ai-chat-close');
        const send = document.getElementById('ai-chat-send');
        const input = document.getElementById('ai-chat-input');
        const suggestions = document.querySelectorAll('.ai-suggestion');

        toggle.addEventListener('click', () => this.toggleChat());
        close.addEventListener('click', () => this.toggleChat());
        send.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });

        suggestions.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const question = e.target.getAttribute('data-question');
                this.askQuestion(question);
            });
        });
    }

    toggleChat() {
        this.isOpen = !this.isOpen;
        const chat = document.getElementById('ai-widget-chat');
        const toggle = document.getElementById('ai-widget-toggle');

        if (this.isOpen) {
            chat.style.display = 'flex';
            toggle.style.display = 'none';
            document.getElementById('ai-chat-input').focus();
        } else {
            chat.style.display = 'none';
            toggle.style.display = 'flex';
        }
    }

    async sendMessage() {
        const input = document.getElementById('ai-chat-input');
        const question = input.value.trim();

        if (!question) return;

        // Clear input
        input.value = '';

        // Ask question
        await this.askQuestion(question);
    }

    async askQuestion(question) {
        // Add user message
        this.addMessage('user', question);

        // Show loading
        const loadingId = this.addMessage('assistant', 'Thinking...', true);

        try {
            // Call API
            const response = await fetch(this.apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ question })
            });

            if (!response.ok) {
                throw new Error('API request failed');
            }

            const data = await response.json();

            // Remove loading message
            this.removeMessage(loadingId);

            // Add assistant response
            this.addMessage('assistant', data.answer, false, data.sources);

        } catch (error) {
            console.error('Error querying AI:', error);
            this.removeMessage(loadingId);
            this.addMessage('assistant', 'Sorry, I encountered an error. Please try again or contact Ivan directly at idedyukh@iu.edu.');
        }
    }

    addMessage(role, content, isLoading = false, sources = []) {
        const messagesContainer = document.getElementById('ai-chat-messages');
        const messageId = `msg-${Date.now()}`;

        const messageHTML = `
            <div id="${messageId}" class="ai-message ai-message-${role} ${isLoading ? 'ai-loading' : ''}">
                <div class="ai-message-content">${content}</div>
                ${sources && sources.length > 0 ? `
                    <div class="ai-message-sources">
                        <small><strong>Sources:</strong> ${sources.join(', ')}</small>
                    </div>
                ` : ''}
            </div>
        `;

        messagesContainer.insertAdjacentHTML('beforeend', messageHTML);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        // Hide intro after first message
        const intro = document.querySelector('.ai-chat-intro');
        if (intro && role === 'user') {
            intro.style.display = 'none';
        }

        return messageId;
    }

    removeMessage(messageId) {
        const message = document.getElementById(messageId);
        if (message) {
            message.remove();
        }
    }
}

// Initialize page
document.addEventListener('DOMContentLoaded', function() {
    console.log('Academic website loaded');

    // Add smooth scrolling to all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Initialize AI Assistant (only if API endpoint is configured)
    // Uncomment the line below once you've deployed the API
    // const assistant = new AcademicAssistant();
});
