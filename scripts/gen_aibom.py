#!/usr/bin/env python3
import os
import pkg_resources
import datetime

AI_LIBRARIES = {
    "transformers",
    "torch",
    "tensorflow",
    "keras",
    "diffusers",
    "openai",
    "langchain",
    "sentence-transformers",
    "pytorch-lightning",
    "scikit-learn",
    "xgboost",
    "lightgbm",
    "stable-diffusion",
    "gpt",
}

def detect_ai_packages():
    installed = {d.project_name.lower() for d in pkg_resources.working_set}
    detected = installed.intersection(AI_LIBRARIES)
    return detected

def write_aibom(detected):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    with open("aibom.md", "w") as f:
        f.write("# AI Bill of Materials\n\n")
        f.write(f"Generated: {now}\n\n")
        if detected:
            f.write("## Detected AI/ML Libraries\n")
            for lib in sorted(detected):
                f.write(f"- {lib}\n")
            f.write("\n## Policy\n")
            f.write("- No AI-generated runtime code allowed.\n")
            f.write("- Manual review required for all AI-related libraries.\n")
        else:
            f.write("## No AI/ML libraries detected.\n")
            f.write("\n## Ethical Commitments\n")
            f.write("- Assistive use only.\n")
            f.write("- No generated credentials.\n")
            f.write("- No undisclosed training datasets.\n")

if __name__ == "__main__":
    detected = detect_ai_packages()
    write_aibom(detected)
    if detected:
        print("AI libraries detected! Manual review required.")
        exit(1)
    else:
        print("No AI libraries found. AIBOM generated.")
