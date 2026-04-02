#!/usr/bin/env python3

import requests
import sys
import os
from urllib.parse import urljoin

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

# Common WCF endpoints
ENDPOINTS = [
    "",
    "/mex",
    "?wsdl",
    "/service.svc",
    "/service.svc?wsdl",
    "/Service.svc",
    "/Service.svc?wsdl",
    "/api",
    "/api/values",
    "/metadata",
    "/wsdl"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (WCF-Enum)",
    "Accept": "*/*"
}

def test_url(base_url):
    results = []

    for endpoint in ENDPOINTS:
        url = base_url.rstrip("/") + endpoint
        try:
            r = requests.get(url, headers=HEADERS, timeout=5, verify=False)

            if r.status_code not in [404]:
                results.append({
                    "url": url,
                    "status": r.status_code,
                    "length": len(r.text)
                })
                print(f"[+] {url} -> {r.status_code} ({len(r.text)} bytes)")

        except requests.exceptions.RequestException:
            pass

    return results


def process_target(target):
    ip, port = target.split(":")

    print(f"\n[+] Testing {ip}:{port}")

    urls = [
        f"http://{ip}:{port}",
        f"https://{ip}:{port}"
    ]

    all_results = []

    for url in urls:
        print(f"\n[*] Checking {url}")
        results = test_url(url)
        all_results.extend(results)

    return all_results


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <IP:PORT | file>")
        sys.exit(1)

    input_arg = sys.argv[1]
    final_results = []

    if os.path.isfile(input_arg):
        with open(input_arg) as f:
            targets = [line.strip() for line in f if line.strip()]
    else:
        targets = [input_arg]

    for target in targets:
        try:
            res = process_target(target)
            final_results.extend(res)
        except Exception as e:
            print(f"[-] Error processing {target}: {e}")

    # Save results
    with open("wcf_results.txt", "w") as f:
        for r in final_results:
            f.write(f"{r['url']} | {r['status']} | {r['length']}\n")

    print("\n[+] Results saved to wcf_results.txt")


if __name__ == "__main__":
    main()
