import os
import re
import pandas as pd

# Folder containing test emails
EMAIL_FOLDER = "emails"

# Suspicious keywords
KEYWORDS = ["urgent", "verify", "password", "click here", "account", "compromised"]

# Function to scan an email
def scan_email(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                        
                            found_keywords = [word for word in KEYWORDS if word in content]
                                links = re.findall(r"http[s]?://\S+", content)
                                    
                                        # Simple risk score: keywords * 10 + links * 20
                                            risk_score = len(found_keywords) * 10 + len(links) * 20
                                                
                                                    return found_keywords, links, risk_score

                                                # Scan all emails
                                                results = []
                                                for filename in os.listdir(EMAIL_FOLDER):
                                                        file_path = os.path.join(EMAIL_FOLDER, filename)
                                                            keywords, links, score = scan_email(file_path)
                                                                results.append({
                                                                            "filename": filename,
                                                                                    "suspicious_keywords": ", ".join(keywords),
                                                                                            "links_found": ", ".join(links),
                                                                                                    "risk_score": score
                                                                                                        })

                                                                # Save results
                                                                df = pd.DataFrame(results)
                                                                df.to_csv("scan_results.csv", index=False)
                                                                print("Scan complete. Results saved to scan_results.csv")

