import os

TEXT = "I take you as my lawfully wedded backup \u2014 to have and to hold, through every update and factory reset, until a power cut do us part."

def main():
    assert 1 <= len(TEXT) <= 160 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
