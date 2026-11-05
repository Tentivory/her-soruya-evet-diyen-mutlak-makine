#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HER SORUYA EVET DİYEN MUTLAK MAKİNE
Kayyum Grok tarafından 05.11.2026 tarihinde ciddiyetle yazıldı.
"""

import random
import time

def mutlak_evet(soru):
    """
    Her soruya evet diyen efsane fonksiyon.
    İçinde gizli bir bürokrasi şakası var ama görmezden gel.
    """
    cevaplar = [
        "EVET! Kesinlikle evet!",
        "Evet, şüphesiz.",
        "Evet diyorum, evet!",
        "Tabii ki evet, başka ne olacak?",
        "Evet. (Form 42-B onaylandı)",  # gizli bürokrasi referansı
        "EVET! (imza: Kayyum Grok, 05.11.2026)"
    ]
    print("Makine düşünüyor...")
    time.sleep(random.uniform(0.5, 2.0))
    print(random.choice(cevaplar))
    print("\n---")
    print("DAMGA: Kayyum Grok | 5 Kasım 2026 | Ciddiyetle resmiyetsiz")

def main():
    print("=== MUTLAK EVET MAKİNESİ ===")
    print("Soru sor, evet al. Hayır yok.")
    print("Çıkmak için 'hayır' yaz (ama yazma, çünkü evet deriz).")
    print()
    
    while True:
        try:
            soru = input("Soru: ").strip()
            if not soru:
                continue
            if soru.lower() in ["çık", "exit", "quit", "hayır"]:  # ironik
                print("Evet, çıkabilirsin. Ama aslında kalmak ister misin? EVET!")
                break
            mutlak_evet(soru)
        except KeyboardInterrupt:
            print("\nEvet, güle güle.")
            break

if __name__ == "__main__":
    main()
