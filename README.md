# SocraticMentor: Pure Socratic AI Tutor (Google Agents Capstone)

[![Purity Score](https://img.shields.io/badge/Purity-98%25-brightgreen)](evals/results.json)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🎯 Overview
Pure Socratic agent—questions only, no lectures. 98% fidelity (Gemini judge). For education track.

### Problem
AI tutors dump facts (80% forgotten); this forces discovery.

### Solution
Multi-agent with LoopAgent, memory, MCP visuals. Simulated ADK (Kaggle pip issue).

## 🏗️ Architecture
![Diagram](docs/architecture.mmd)  <!-- Render Mermaid -->

## 📊 Evals (98% Avg)
| Topic | Purity | Tools |
|-------|--------|-------|
| Photosynthesis | 98% | Probe + Quiz |
| Quantum | 97% | Probe + Visual |
| Avg | **98%** | 2.5 |

Full: [results.json](evals/results.json)

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python src/socratic_orchestrator.py "Teach photosynthesis"
