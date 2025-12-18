import random

TOKENS=["🧱⭐🧱","☢️♠️🍄","⚛️♣️🧱","🧱✨⭐🧱"]

def jump(token):
    target=random.choice([t for t in TOKENS if t!=token])
    print(f"{token} → {target}")

if __name__=="__main__":
    import sys
    jump(sys.argv[1] if len(sys.argv)>1 else "🧱⭐🧱")
