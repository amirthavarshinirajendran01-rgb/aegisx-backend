# 🛡️ AegisX — A Local-First Privacy Firewall for AI & Web Browsing
Hey there! 👋 I am a 1st-Year Engineering Student (Semester 1). I built AegisX to solve a real problem I noticed on campus: people accidentally leaking confidential code, passwords, and personal details into ChatGPT and web forms.
**Live Web Platform:** [aegisxassi.lovable.app](https://aegisxassi.lovable.app/) | **License:** MIT | **Core Engine:** C | **Backend:** FastAPI | **Compliance:** DPDP Act 2023
---
## 🌐 Try the Live Platform
You can test the interactive privacy engine directly in your browser without installing anything:  
👉 **https://aegisxassi.lovable.app/**
---
## 👨‍💻 About This Project (A First-Year Student's Initiative)
Just three weeks into my first year of college, I noticed something alarming: everyone around me—classmates, developers, and friends—was constantly pressing `Ctrl + V` into ChatGPT to debug their work or write essays.
Most people don't realize that in 2023, Samsung engineers accidentally leaked secret chip designs to ChatGPT in just 20 days because of the exact same habit. Research shows that 13% of all prompts sent to GenAI contain confidential credentials or PII. Worse, studies from Princeton and UC Davis revealed that thousands of websites secretly record your keystrokes on forms before you even click "Submit."
Existing global tools (like Microsoft Presidio) are built for the US. They flag random 12-digit numbers as Aadhaar cards, use dumb `[REDACTED]` boxes that break AI reasoning, and ignore India's new DPDP Act 2023.
I know I can't magically solve all cybersecurity overnight. But I wanted to build something that stops the most critical 10% to 15% vulnerability window right at the keyboard before data ever leaves the laptop.
---
## 🤖 Built via Human-AI Pair Programming
As a first-year student learning C programming in class this semester, I wanted to push myself beyond basic classroom assignments.
I built AegisX through **Human-AI Collaboration**:
- **My Role (Systems Architect & Product Lead):** I designed the privacy architecture, chose the focus on India's DPDP Act, researched the mathematical Verhoeff dihedral group algorithm, defined the regex patterns for Indian identifiers, and directed the entire product.
- **AI Agents (Developer Copilots):** I leveraged modern AI developer tools (Lovable and Antigravity) as my pair-programmers to help scaffold the React UI components, write boilerplate endpoints, and accelerate the build.
---
## 🔒 100% Zero-External-Cloud Guarantee (Solving the Cloud Leak Paradox)
Many so-called "privacy scanners" have a fatal flaw: they take your secret text and send it to an *external cloud AI* to detect the private data—leaking your secrets to a third-party server before even sanitizing them!
**AegisX strictly rejects this:**
- **Zero Third-Party AI Inspection:** AegisX **never** transmits unmasked, raw text to third-party cloud models (such as OpenAI, Anthropic, or Lovable AI) for scanning.
- **100% On-Device / Local-First Detection:** All PII detection, regex matching, and checksum validations occur deterministically inside the client's local browser sandbox or private RAM vault.
- **Volatile Ephemeral Memory:** Zero prompts or PII tokens are ever saved to disk, external databases, or server logs. When your session ends, the memory is purged.
---
## 🚀 Key Features
### 1. Smart Dummy Token Swapping (Context-Preserving)
Normal privacy tools cross out words with `[REDACTED]`. That confuses ChatGPT and makes it reply with broken answers. AegisX replaces sensitive secrets with realistic fake details (`Rahul` $\rightarrow$ `Alex`, real AWS key $\rightarrow$ synthetic dummy key). ChatGPT understands the question and gives a great answer, and AegisX lets you restore your real details on-screen locally!
### 2. India-First Aadhaar Validation (Pure C)
Instead of blindly flagging any random 12-digit number as an Aadhaar card, we implemented the actual mathematical **Verhoeff checksum algorithm** (based on the dihedral group $D_5$ symmetries of a regular pentagon). It checks valid Aadhaar numbers with zero false alarms, catching 100% of single-digit typos and transpositions.
### 3. DPDP Act 2023 Legal Suite
- **Section 12 Legal Notice Generator:** Under Section 12 of India’s DPDP Act 2023, citizens have the legal "Right to Erasure." AegisX includes a 1-click button that generates a formal legal email addressed to a company's Data Protection Officer (DPO) demanding personal data deletion.
- **Section 6 Consent Decoder:** Translates long 5,000-word terms of service into simple 5-bullet summaries in English, Hindi, Tamil, and Telugu.
### 4. Perimeter Website Auditor (Traffic Lights)
No confusing scores. Just simple, honest traffic lights:
- 🟢 **SAFE:** Valid HTTPS, modern security headers, and clean tracking baseline.
- 🟡 **MODERATE:** Watch out! The site uses tricky cookie pop-ups that hide the "Reject" button.
- 🔴 **HIGH RISK:** Danger! Background scripts detected that can record what you type before you click submit.
---
## 🏗️ System Architecture

  

[ User Input / LLM Prompt ]
│
▼
┌────────────────────────────────────────┐
│  AEGISX ENGINE (Local Sandbox / RAM)   │
│  - Verhoeff C-Core (Aadhaar/PAN)       │
│  - Deterministic PII Regex Filters     │
│  - Context-Preserving Token Swapping   │
└────────────────────────────────────────┘
│  (Sends ONLY Safe Synthetic Data)
▼
[ ChatGPT / External LLM ]
│  (Receives Reply with Synthetic Tokens)
▼
┌────────────────────────────────────────┐
│  AEGISX RE-HYDRATION LAYER (Local RAM) │
│  - Restores Original Secrets Locally   │
└────────────────────────────────────────┘
│
▼
[ Final Secure Output on Screen ]


  
---
## 🛠️ Tech Stack
- **Frontend Platform:** React, Tailwind CSS, Lucide Icons, Vite
- **Low-Level Core:** Pure C (`aegis_core.c`), Dihedral Group $D_5$ Math
- **Backend API:** Python 3, FastAPI, Asynchronous Uvicorn, Ctypes
- **Browser Extension:** Google Chrome Extensions (Manifest V3)
---
## 🏃 Running the Backend Locally
```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/aegisx-backend.git
cd aegisx-backend
# 2. Install Python requirements
pip install -r requirements.txt
# 3. Run the API server
python main.py
# Server runs at: http://localhost:8000
# Interactive API Docs (Swagger UI): http://localhost:8000/docs

  

  
🌟 What I Learned Building This

  

Building this project taught me:


  

  
How dihedral group abstract algebra applies to real-world Indian cybersecurity (Verhoeff checksum).

  
How to interface low-level C code with asynchronous Python APIs using ctypes.

  
How to structure a modern client-side React frontend with stateful token unmasking.

  
Why local-first privacy architectures are essential to avoid the "Cloud Leak Paradox."

  
How India's DPDP Act 2023 creates real legal obligations for tech companies.

  

  

  
📜 License

  

Distributed under the MIT License.
