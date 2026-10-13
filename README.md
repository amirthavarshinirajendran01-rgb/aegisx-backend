# 🛡️ AegisX

### Local-First Privacy Firewall for Generative AI, Web & Media
> Built by a 1st-Year Engineering Student (Semester 1) to solve real campus privacy leaks before data leaves the laptop.

[![Live Demo](https://img.shields.io/badge/Live%20Platform-aegisxassi.lovable.app-10B981?style=for-the-badge&logo=firefox)](https://aegisxassi.lovable.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Core: Pure C](https://img.shields.io/badge/Core-Pure%20C%20(D5%20Math)-A855F7?style=for-the-badge)](c_engine/aegis_core.c)
[![Backend: FastAPI](https://img.shields.io/badge/Backend-FastAPI-06B6D4?style=for-the-badge)](main.py)
[![Compliance](https://img.shields.io/badge/Compliance-DPDP%20Act%202023-amber?style=for-the-badge)](https://www.meity.gov.in/)

---

## ⚡ Quick Pitch: What is AegisX?

When you press `Ctrl + V` into ChatGPT or a website, **your data is already compromised**.
- In 2023, Samsung engineers leaked trade secrets to ChatGPT in under 20 days.
- 13% of all prompts sent to GenAI leak PII or API credentials.
- Websites silently record your keystrokes on forms before you even hit "Submit."
- Photos uploaded to social media are scraped by AI face-swap bots.

**AegisX intercepts and sanitizes your data right inside your browser RAM—before a single byte touches the internet.**

---

## ⚔️ The 3 Core Defense Pillars

| Pillar | How it Works | Key Tech |
| :--- | :--- | :--- |
| **📝 Text & Prompt Shield** | Replaces real secrets with synthetic dummy tokens (`Rahul` $\rightarrow$ `Alex`). ChatGPT understands context; AegisX restores the real data locally on screen. | Context-Preserving Swapping (CPEP) |
| **🖼️ Image Armor** | Strips hidden GPS/camera metadata and injects imperceptible micro-noise into image pixels to disrupt deepfake facial-landmark detectors. | 100% Client-Side HTML5 Canvas |
| **🌐 Web & Wiretap Auditor** | Scans websites using instant traffic lights (🟢/🟡/🔴) to flag keystroke-recording scripts and cookie dark patterns. | Browser DOM Interceptor |

---

## 🧠 Why Not Traditional Tools?

| Problem | Traditional Tools (e.g. Presidio) | AegisX Engine |
| :--- | :--- | :--- |
| **AI Reasoning** | Uses `[REDACTED]` boxes that break LLM grammar and logic | **Synthetic Token Swapping** preserves full context |
| **Indian IDs** | Flags any random 12-digit number as an Aadhaar card | **Verhoeff Algorithm in Pure C** (Dihedral Group $D_5$) = 0% false alarms |
| **Privacy Irony** | Many tools upload text to *another cloud AI* to scan it | **100% Local-First**: zero external cloud inspection |
| **Media Safety** | Ignores photos completely | **Client-Side EXIF Wiper + Anti-AI Cloak** |
| **Legal Recourse** | Generic US/EU policies | **DPDP Act 2023 (Sec 12) & IT Rules (Rule 3(2)(b))** automated takedowns |

---

## 🔒 The Zero-Retention Rule 
         ┌──────────────────────┐
         │    USER INPUT         │
         │ Prompts • Images      │
         │ Documents             │
         └──────────┬───────────┘
                    ▼
    ╔════════════════════════════════╗
    ║       AEGISX FIREWALL          ║
    ║                                ║
    ║  01  Identity Checksum Core    ║
    ║  02  Image & Metadata Sanitizer║
    ║  03  Synthetic Token Engine    ║
    ╚════════════════╤═══════════════╝
                     │
                     ▼
         ┌──────────────────────┐
         │   SANITIZED OUTPUT   │
         │ Synthetic Data Only  │
         └──────────┬───────────┘
                    ▼
         ┌──────────────────────┐
         │   PUBLIC LLMs / API  │
         └──────────────────────┘

    
> **Zero Cloud Leaks:** Your raw prompts and photos never touch our backend, databases, or external AI. Everything evaporates when your browser tab closes.

---

## 🛠️ The Tech Stack

- **Frontend:** React, Tailwind CSS, Lucide Icons, Vite ([Live App](https://aegisxassi.lovable.app/))
- **Core Math Engine:** Pure C (`aegis_core.c`) — Dihedral Group $D_5$ permutations
- **Backend API:** Python 3, FastAPI, Asynchronous Uvicorn, `ctypes` bridge
- **Media Cloak:** HTML5 Canvas, In-Memory Pixel Perturbations (`image_armor.js`)
- **Browser Security:** Google Chrome Extensions (Manifest V3)

---

## 💻 Running the Backend Locally

```bash
# 1. Clone repo
git clone https://github.com/YOUR_USERNAME/aegisx-backend.git
cd aegisx-backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI server
python main.py
# 🚀 API running at: http://localhost:8000
# 📖 Swagger docs at: http://localhost:8000/docs
---

## 🎓 Behind the Build

> *"In 2023, senior engineers at Samsung made global headlines when they accidentally leaked proprietary semiconductor source code to ChatGPT in under three weeks. If world-class engineers at a tech giant can fall into the habit of careless copy-pasting, everyday developers and students definitely will.*
> 
> *Just three weeks into my first year of B.Tech in Information Technology, I watched classmates and peers routinely paste confidential code, passwords, and personal details into AI prompts without thinking twice. At the same time, the rapid rise of open-source deepfake bots scraping social media photos made it obvious that everyday privacy is breaking right at the user's keyboard.*
> 
> *I knew I couldn't solve all of cybersecurity overnight as a first-year student. But rather than building another generic classroom form, I wanted to build a practical, local-first shield that stops data leaks before they happen.*
> 
> *I acted as the Systems Architect—identifying the threat vectors, choosing the Verhoeff group theory algorithm in C, mapping India's DPDP Act and IT Rules, and directing the entire user flow. I collaborated with modern agentic AI developer tools as pair-programming copilots to scaffold the components and bring this vision to life in month one.*
> 
> *AegisX is proof that with the right problem, ethical curiosity, and modern engineering tools, even a beginner can build software that stands up for user dignity."*

📜 License
Distributed under the MIT License.
