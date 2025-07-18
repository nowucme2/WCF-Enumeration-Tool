# WCF Enumeration Tool

A Python-based tool to automate the enumeration of WCF service endpoints. Supports both HTTP/HTTPS, automatic screenshot capturing, 403 bypass attempts, and interactive file path selection with TAB completion.

## 🔧 Features
- Enumerates common WCF endpoints
- Auto HTTP/HTTPS fallback
- Headers to bypass basic 403 protections
- Saves all results clearly (200, 403, 404)
- Screenshots for every result
- TAB completion for input file path
- Clean output structure in `results/`

## 📂 Output Structure
results/
├── found_endpoints.txt # Only valid 200 OK
├── log.txt # Full log (200, 403, etc.)
└── screenshots/ # Screenshots of all responses

## Prepare Input File:
20.203.77.217:10002
192.168.1.100:443

## Pre-requisite
pip install -r requirements.txt

## Run the Tool:
python3 wcf_enum.py

